"""
VLearn CBC Grade 10 Geography — Topic 10: Agriculture
Visual Enrichment Engine (Vector SVGs, Verified Wikimedia Images & Educational Videos)

Subject: Geography (Grade 10 CBC, Subject ID: 37)
Topic 10: Agriculture

Attaches:
  - 15 First-Card Photographic Visual Hooks (100% Tested HTTP 200 OK Direct Wikimedia URLs)
  - 15 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - Educational YouTube Video for Food Security (Lesson 12)
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade10_geography_topic10.py
"""

import os
import sys
import re
import json
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, Lesson, LessonBlock, LessonAsset
)

def sanitize_svg(svg: str) -> str:
    """Ensures SVG is clean, responsive, and stripped of unneeded XML/DOCTYPE headers."""
    svg = re.sub(r'<\?xml.*?\?>', '', svg)
    svg = re.sub(r'<!DOCTYPE.*?>', '', svg)
    return svg.strip()

# =============================================================================
# 15 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 10: AGRICULTURE
# =============================================================================

# SVG 1: Subsistence vs Commercial Classification Tree (Lesson 1)
SVG_CLASSIFICATION_TREE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">TAXONOMY OF AGRICULTURAL SYSTEMS</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Classification by Economic Objective, Scale, Capital, and Labor Intensity</text>

  <!-- Root Node -->
  <rect x="290" y="80" width="220" height="35" rx="8" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="400" y="103" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">GLOBAL AGRICULTURE</text>

  <!-- Branch lines -->
  <path d="M 400 115 L 400 135 L 200 135 L 200 155" stroke="#94a3b8" stroke-width="2" fill="none"/>
  <path d="M 400 115 L 400 135 L 600 135 L 600 155" stroke="#94a3b8" stroke-width="2" fill="none"/>

  <!-- Left: Subsistence Branch -->
  <g transform="translate(40, 155)">
    <rect x="0" y="0" width="320" height="40" rx="8" fill="#047857" stroke="#34d399" stroke-width="1.5"/>
    <text x="160" y="25" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">1. SUBSISTENCE SYSTEMS</text>

    <!-- Connectors -->
    <path d="M 160 40 L 160 60 L 50 60 L 50 80" stroke="#64748b" stroke-width="1.5" fill="none"/>
    <path d="M 160 60 L 160 80" stroke="#64748b" stroke-width="1.5" fill="none"/>
    <path d="M 160 60 L 270 60 L 270 80" stroke="#64748b" stroke-width="1.5" fill="none"/>

    <!-- Sub-box 1: Shifting Cultivation -->
    <rect x="0" y="80" width="100" height="150" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
    <rect x="0" y="80" width="100" height="24" rx="6" fill="#065f46"/>
    <text x="50" y="96" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Shifting Cult.</text>
    <text x="50" y="120" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Slash-and-burn</text>
    <text x="50" y="138" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Plot rotation</text>
    <text x="50" y="156" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Forest fallow</text>
    <text x="50" y="174" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Ash fertility</text>
    <text x="50" y="205" font-size="8" font-weight="bold" fill="#6ee7b7" text-anchor="middle">Tropical Forests</text>

    <!-- Sub-box 2: Pastoral Nomadism -->
    <rect x="110" y="80" width="100" height="150" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
    <rect x="110" y="80" width="100" height="24" rx="6" fill="#065f46"/>
    <text x="160" y="96" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Pastoral Nomad.</text>
    <text x="160" y="120" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Seasonal trek</text>
    <text x="160" y="138" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Camels / Goats</text>
    <text x="160" y="156" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Communal land</text>
    <text x="160" y="174" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Scant rainfall</text>
    <text x="160" y="205" font-size="8" font-weight="bold" fill="#6ee7b7" text-anchor="middle">Kenyan ASALs</text>

    <!-- Sub-box 3: Intensive Subsistence -->
    <rect x="220" y="80" width="100" height="150" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
    <rect x="220" y="80" width="100" height="24" rx="6" fill="#065f46"/>
    <text x="270" y="96" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Intensive Subs.</text>
    <text x="270" y="120" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• High labor/ha</text>
    <text x="270" y="138" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Tiny plots</text>
    <text x="270" y="156" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Intercropping</text>
    <text x="270" y="174" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Family diet</text>
    <text x="270" y="205" font-size="8" font-weight="bold" fill="#6ee7b7" text-anchor="middle">Highlands &amp; Asia</text>
  </g>

  <!-- Right: Commercial Branch -->
  <g transform="translate(440, 155)">
    <rect x="0" y="0" width="320" height="40" rx="8" fill="#b91c1c" stroke="#f87171" stroke-width="1.5"/>
    <text x="160" y="25" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">2. COMMERCIAL SYSTEMS</text>

    <!-- Connectors -->
    <path d="M 160 40 L 160 60 L 50 60 L 50 80" stroke="#64748b" stroke-width="1.5" fill="none"/>
    <path d="M 160 60 L 160 80" stroke="#64748b" stroke-width="1.5" fill="none"/>
    <path d="M 160 60 L 270 60 L 270 80" stroke="#64748b" stroke-width="1.5" fill="none"/>

    <!-- Sub-box 1: Plantations -->
    <rect x="0" y="80" width="100" height="150" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <rect x="0" y="80" width="100" height="24" rx="6" fill="#991b1b"/>
    <text x="50" y="96" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Plantations</text>
    <text x="50" y="120" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Monoculture</text>
    <text x="50" y="138" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Tea / Coffee</text>
    <text x="50" y="156" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• High capital</text>
    <text x="50" y="174" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Export focus</text>
    <text x="50" y="205" font-size="8" font-weight="bold" fill="#fca5a5" text-anchor="middle">Kericho / Murang'a</text>

    <!-- Sub-box 2: Floriculture / Urban -->
    <rect x="110" y="80" width="100" height="150" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <rect x="110" y="80" width="100" height="24" rx="6" fill="#991b1b"/>
    <text x="160" y="96" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Horticulture</text>
    <text x="160" y="120" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Greenhouses</text>
    <text x="160" y="138" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Hydroponics</text>
    <text x="160" y="156" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Cut flowers</text>
    <text x="160" y="174" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Cold chains</text>
    <text x="160" y="205" font-size="8" font-weight="bold" fill="#fca5a5" text-anchor="middle">Lake Naivasha</text>

    <!-- Sub-box 3: Commercial Ranching -->
    <rect x="220" y="80" width="100" height="150" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <rect x="220" y="80" width="100" height="24" rx="6" fill="#991b1b"/>
    <text x="270" y="96" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Ranching/Grain</text>
    <text x="270" y="120" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Mechanization</text>
    <text x="270" y="138" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Vast acreages</text>
    <text x="270" y="156" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Beef / Wheat</text>
    <text x="270" y="174" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Fenced paddocks</text>
    <text x="270" y="205" font-size="8" font-weight="bold" fill="#fca5a5" text-anchor="middle">Laikipia / Rift</text>
  </g>

  <!-- Footer summary -->
  <rect x="40" y="395" width="720" height="25" rx="5" fill="#334155"/>
  <text x="400" y="412" font-size="10.5" fill="#e2e8f0" text-anchor="middle">Key Differentiator: Subsistence prioritizes family survival; Commercial optimizes market profitability and scale.</text>
</svg>
""")

# SVG 2: Intensive vs Extensive Farming Systems Matrix (Lesson 2)
SVG_INTENSIVE_EXTENSIVE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">INTENSIVE VS. EXTENSIVE FARMING SYSTEMS</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Input Density per Hectare vs. Total Spatial Land Footprint</text>

  <!-- Left: Intensive Farming Box -->
  <g transform="translate(45, 85)">
    <rect x="0" y="0" width="335" height="325" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="335" height="34" rx="10" fill="#15803d"/>
    <text x="167" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">INTENSIVE AGRICULTURE</text>

    <!-- Visual schematic: Small box, dense inputs, high output -->
    <rect x="25" y="50" width="80" height="80" rx="6" fill="#334155" stroke="#4ade80" stroke-width="2"/>
    <text x="65" y="95" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Small Plot</text>
    
    <!-- Arrows showing dense inputs -->
    <path d="M 120 65 L 170 65" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrow)" fill="none"/>
    <text x="180" y="69" font-size="10" fill="#fbbf24">High Capital &amp; Fertilizer</text>
    <path d="M 120 90 L 170 90" stroke="#f59e0b" stroke-width="3" fill="none"/>
    <text x="180" y="94" font-size="10" fill="#fbbf24">High Labor / Tech Density</text>
    <path d="M 120 115 L 170 115" stroke="#22c55e" stroke-width="3" fill="none"/>
    <text x="180" y="119" font-size="10" font-weight="bold" fill="#4ade80">MAX Output per Ha</text>

    <line x1="20" y1="145" x2="315" y2="145" stroke="#334155" stroke-width="1.5"/>

    <!-- Properties -->
    <g transform="translate(20, 160)">
      <text x="0" y="15" font-size="11" font-weight="bold" fill="#4ade80">• Land Area:</text>
      <text x="110" y="15" font-size="11" fill="#cbd5e1">Small to moderate (0.5 - 50 ha)</text>
      <text x="0" y="35" font-size="11" font-weight="bold" fill="#4ade80">• Input Density:</text>
      <text x="110" y="35" font-size="11" fill="#cbd5e1">Very High ($/ha, seeds, drip)</text>
      <text x="0" y="55" font-size="11" font-weight="bold" fill="#4ade80">• Yield per Ha:</text>
      <text x="110" y="55" font-size="11" fill="#cbd5e1">Extremely High</text>
      <text x="0" y="75" font-size="11" font-weight="bold" fill="#4ade80">• Location:</text>
      <text x="110" y="75" font-size="11" fill="#cbd5e1">Densely populated highlands, peri-urban</text>
      <text x="0" y="95" font-size="11" font-weight="bold" fill="#4ade80">• Examples:</text>
      <text x="110" y="95" font-size="11" fill="#cbd5e1">Naivasha flowers, Kiambu tea, Hydroponics</text>
    </g>
  </g>

  <!-- Right: Extensive Farming Box -->
  <g transform="translate(420, 85)">
    <rect x="0" y="0" width="335" height="325" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="335" height="34" rx="10" fill="#0369a1"/>
    <text x="167" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">EXTENSIVE AGRICULTURE</text>

    <!-- Visual schematic: Large box, low inputs, moderate output -->
    <rect x="25" y="50" width="130" height="80" rx="6" fill="#334155" stroke="#38bdf8" stroke-width="2"/>
    <text x="90" y="95" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Vast Acreage (1,000+ ha)</text>
    
    <!-- Arrows showing dispersed inputs -->
    <path d="M 170 65 L 210 65" stroke="#94a3b8" stroke-width="2" fill="none"/>
    <text x="215" y="69" font-size="10" fill="#cbd5e1">Low $/ha input</text>
    <path d="M 170 90 L 210 90" stroke="#94a3b8" stroke-width="2" fill="none"/>
    <text x="215" y="94" font-size="10" fill="#cbd5e1">Low labor per ha</text>
    <path d="M 170 115 L 210 115" stroke="#38bdf8" stroke-width="2" fill="none"/>
    <text x="215" y="119" font-size="10" fill="#7dd3fc">High TOTAL output</text>

    <line x1="20" y1="145" x2="315" y2="145" stroke="#334155" stroke-width="1.5"/>

    <!-- Properties -->
    <g transform="translate(20, 160)">
      <text x="0" y="15" font-size="11" font-weight="bold" fill="#38bdf8">• Land Area:</text>
      <text x="110" y="15" font-size="11" fill="#cbd5e1">Vast (Hundreds to 10,000+ ha)</text>
      <text x="0" y="35" font-size="11" font-weight="bold" fill="#38bdf8">• Input Density:</text>
      <text x="110" y="35" font-size="11" fill="#cbd5e1">Low capital/labor per hectare</text>
      <text x="0" y="55" font-size="11" font-weight="bold" fill="#38bdf8">• Yield per Ha:</text>
      <text x="110" y="55" font-size="11" fill="#cbd5e1">Modest to low per ha</text>
      <text x="0" y="75" font-size="11" font-weight="bold" fill="#38bdf8">• Location:</text>
      <text x="110" y="75" font-size="11" fill="#cbd5e1">Sparsely populated rangelands &amp; plains</text>
      <text x="0" y="95" font-size="11" font-weight="bold" fill="#38bdf8">• Examples:</text>
      <text x="110" y="95" font-size="11" fill="#cbd5e1">Laikipia beef ranches, Australian sheep</text>
    </g>
  </g>
</svg>
""")

# SVG 3: Physical & Human Factors Matrix (Lesson 3)
SVG_FACTORS_MATRIX = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">FACTORS INFLUENCING AGRICULTURAL DISTRIBUTION</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Physical Environmental Constraints vs. Human Socio-Economic Variables</text>

  <!-- Left: Physical Factors -->
  <g transform="translate(40, 85)">
    <rect x="0" y="0" width="340" height="325" rx="10" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
    <rect x="0" y="0" width="340" height="32" rx="10" fill="#0369a1"/>
    <text x="170" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">PHYSICAL ENVIRONMENTAL FACTORS</text>

    <!-- Item 1: Climate -->
    <g transform="translate(15, 45)">
      <rect x="0" y="0" width="310" height="60" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="18" font-size="11" font-weight="bold" fill="#38bdf8">1. Climate (Rainfall &amp; Temperature)</text>
      <text x="10" y="34" font-size="9.5" fill="#cbd5e1">• Moisture limits: Tea/Coffee (&gt;1,200mm) vs Millet (&lt;500mm)</text>
      <text x="10" y="48" font-size="9.5" fill="#cbd5e1">• Thermal limits: Frost halts highland growth; cocoa needs &gt;25°C</text>
    </g>

    <!-- Item 2: Relief -->
    <g transform="translate(15, 115)">
      <rect x="0" y="0" width="310" height="60" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="18" font-size="11" font-weight="bold" fill="#38bdf8">2. Relief &amp; Altitude (Topography)</text>
      <text x="10" y="34" font-size="9.5" fill="#cbd5e1">• Slope gradient: Plains favor tractors; steep slopes need terraces</text>
      <text x="10" y="48" font-size="9.5" fill="#cbd5e1">• Altitudinal zonation: Lowland savannah to alpine pyrethrum</text>
    </g>

    <!-- Item 3: Edaphic -->
    <g transform="translate(15, 185)">
      <rect x="0" y="0" width="310" height="60" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="18" font-size="11" font-weight="bold" fill="#38bdf8">3. Edaphic Factors (Soil Chemistry &amp; Depth)</text>
      <text x="10" y="34" font-size="9.5" fill="#cbd5e1">• Soil acidity (pH 4.5-5.5) and volcanic drainage favor tea</text>
      <text x="10" y="48" font-size="9.5" fill="#cbd5e1">• Heavy alluvial/black cotton clays suit cotton and rice</text>
    </g>

    <!-- Item 4: Biotic -->
    <g transform="translate(15, 255)">
      <rect x="0" y="0" width="310" height="55" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="18" font-size="11" font-weight="bold" fill="#38bdf8">4. Biotic Pressures</text>
      <text x="10" y="34" font-size="9.5" fill="#cbd5e1">• Pests: Tsetse fly limits cattle; Armyworms attack cereals</text>
      <text x="10" y="46" font-size="9.5" fill="#cbd5e1">• Beneficial organisms: Bees and nitrogen-fixing bacteria</text>
    </g>
  </g>

  <!-- Right: Human Factors -->
  <g transform="translate(420, 85)">
    <rect x="0" y="0" width="340" height="325" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="340" height="32" rx="10" fill="#d97706"/>
    <text x="170" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">HUMAN SOCIO-ECONOMIC FACTORS</text>

    <!-- Item 1: Capital -->
    <g transform="translate(15, 45)">
      <rect x="0" y="0" width="310" height="60" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="18" font-size="11" font-weight="bold" fill="#fbbf24">1. Financial Capital &amp; Credit</text>
      <text x="10" y="34" font-size="9.5" fill="#cbd5e1">• Liquidity to buy hybrid seeds, fertilizers, and solar pumps</text>
      <text x="10" y="48" font-size="9.5" fill="#cbd5e1">• Collateral barriers: Lack of title deeds locks out smallholders</text>
    </g>

    <!-- Item 2: Labor -->
    <g transform="translate(15, 115)">
      <rect x="0" y="0" width="310" height="60" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="18" font-size="11" font-weight="bold" fill="#fbbf24">2. Labor Availability &amp; Skills</text>
      <text x="10" y="34" font-size="9.5" fill="#cbd5e1">• Plucking tea and coffee requires dense, skilled manual labor</text>
      <text x="10" y="48" font-size="9.5" fill="#cbd5e1">• Agronomic knowledge and extension training services</text>
    </g>

    <!-- Item 3: Transport & Markets -->
    <g transform="translate(15, 185)">
      <rect x="0" y="0" width="310" height="60" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="18" font-size="11" font-weight="bold" fill="#fbbf24">3. Transport Infrastructure &amp; Markets</text>
      <text x="10" y="34" font-size="9.5" fill="#cbd5e1">• Perishables (milk/flowers) need all-weather roads &amp; airports</text>
      <text x="10" y="48" font-size="9.5" fill="#cbd5e1">• Market proximity dictates profit margins vs middleman cuts</text>
    </g>

    <!-- Item 4: Government Policies -->
    <g transform="translate(15, 255)">
      <rect x="0" y="0" width="310" height="55" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="18" font-size="11" font-weight="bold" fill="#fbbf24">4. Government Policies &amp; Land Tenure</text>
      <text x="10" y="34" font-size="9.5" fill="#cbd5e1">• Fertilizer subsidies, price guarantees, and export tax waivers</text>
      <text x="10" y="46" font-size="9.5" fill="#cbd5e1">• Inheritance laws driving extreme land fragmentation</text>
    </g>
  </g>
</svg>
""")

# SVG 4: Agricultural System Open Cycle: Inputs -> Processes -> Outputs (Lesson 4)
SVG_SYSTEM_CYCLE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">AGRICULTURAL SYSTEM AS AN OPEN THERMODYNAMIC CYCLE</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Energy and Matter Transformation: Inputs, On-Farm Processes, Outputs, and Feedback Loops</text>

  <!-- 1. INPUTS BOX -->
  <g transform="translate(35, 90)">
    <rect x="0" y="0" width="215" height="230" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="215" height="32" rx="10" fill="#0369a1"/>
    <text x="107" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. SYSTEM INPUTS</text>
    
    <text x="12" y="55" font-size="10.5" font-weight="bold" fill="#38bdf8">Physical Inputs:</text>
    <text x="12" y="73" font-size="9.5" fill="#cbd5e1">• Solar radiation &amp; light</text>
    <text x="12" y="89" font-size="9.5" fill="#cbd5e1">• Rainfall / Surface water</text>
    <text x="12" y="105" font-size="9.5" fill="#cbd5e1">• Soil nutrients &amp; minerals</text>
    
    <text x="12" y="130" font-size="10.5" font-weight="bold" fill="#fbbf24">Human / Capital Inputs:</text>
    <text x="12" y="148" font-size="9.5" fill="#cbd5e1">• Certified hybrid seeds</text>
    <text x="12" y="164" font-size="9.5" fill="#cbd5e1">• Chemical / Organic fertilizers</text>
    <text x="12" y="180" font-size="9.5" fill="#cbd5e1">• Tractors &amp; fuel / Tools</text>
    <text x="12" y="196" font-size="9.5" fill="#cbd5e1">• Labor &amp; management knowledge</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <path d="M 255 205 L 290 205" stroke="#f59e0b" stroke-width="4" fill="none"/>
  <polygon points="290,198 305,205 290,212" fill="#f59e0b"/>

  <!-- 2. PROCESSES BOX -->
  <g transform="translate(305, 90)">
    <rect x="0" y="0" width="190" height="230" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="190" height="32" rx="10" fill="#d97706"/>
    <text x="95" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. ON-FARM PROCESSES</text>

    <text x="12" y="55" font-size="10.5" font-weight="bold" fill="#fbbf24">Crop Operations:</text>
    <text x="12" y="73" font-size="9.5" fill="#cbd5e1">• Plowing &amp; harrowing</text>
    <text x="12" y="89" font-size="9.5" fill="#cbd5e1">• Sowing / Transplanting</text>
    <text x="12" y="105" font-size="9.5" fill="#cbd5e1">• Weeding &amp; thinning</text>
    <text x="12" y="121" font-size="9.5" fill="#cbd5e1">• Drip irrigating &amp; spraying</text>
    <text x="12" y="137" font-size="9.5" fill="#cbd5e1">• Harvesting &amp; threshing</text>

    <text x="12" y="162" font-size="10.5" font-weight="bold" fill="#4ade80">Livestock Operations:</text>
    <text x="12" y="180" font-size="9.5" fill="#cbd5e1">• Fodder feeding &amp; grazing</text>
    <text x="12" y="196" font-size="9.5" fill="#cbd5e1">• Milking &amp; dipping</text>
    <text x="12" y="212" font-size="9.5" fill="#cbd5e1">• Veterinary care</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <path d="M 500 205 L 535 205" stroke="#22c55e" stroke-width="4" fill="none"/>
  <polygon points="535,198 550,205 535,212" fill="#22c55e"/>

  <!-- 3. OUTPUTS BOX -->
  <g transform="translate(550, 90)">
    <rect x="0" y="0" width="215" height="230" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="215" height="32" rx="10" fill="#15803d"/>
    <text x="107" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. SYSTEM OUTPUTS</text>

    <text x="12" y="55" font-size="10.5" font-weight="bold" fill="#4ade80">Primary Market Goods:</text>
    <text x="12" y="73" font-size="9.5" fill="#cbd5e1">• Maize grain &amp; pulses</text>
    <text x="12" y="89" font-size="9.5" fill="#cbd5e1">• Fresh milk, beef &amp; eggs</text>
    <text x="12" y="105" font-size="9.5" fill="#cbd5e1">• Tea leaves, coffee berries, flowers</text>

    <text x="12" y="130" font-size="10.5" font-weight="bold" fill="#f87171">By-Products &amp; Waste:</text>
    <text x="12" y="148" font-size="9.5" fill="#cbd5e1">• Animal manure &amp; slurry</text>
    <text x="12" y="164" font-size="9.5" fill="#cbd5e1">• Crop stalks / chaff stubble</text>
    <text x="12" y="180" font-size="9.5" fill="#cbd5e1">• Soil runoff &amp; chemical leachates</text>
    <text x="12" y="196" font-size="9.5" fill="#cbd5e1">• Greenhouse gases (CH4, N2O)</text>
  </g>

  <!-- FEEDBACK LOOP (Bottom curve from 3 back to 1) -->
  <path d="M 650 325 L 650 375 L 140 375 L 140 325" stroke="#10b981" stroke-width="2.5" stroke-dasharray="6,4" fill="none"/>
  <polygon points="140,325 134,338 146,338" fill="#10b981"/>
  
  <rect x="250" y="360" width="300" height="30" rx="6" fill="#065f46" stroke="#34d399"/>
  <text x="400" y="380" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">CLOSED FEEDBACK LOOP: Manure &amp; Stubble Recycled</text>
</svg>
""")

# SVG 5: Farm to Fork Agribusiness Value Chain (Lesson 5)
SVG_VALUE_CHAIN = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">FARM TO FORK: THE AGRIBUSINESS VALUE CHAIN</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Progressive Economic Value Addition from Input Supply to Consumer Retail</text>

  <!-- 5 Horizontal Stages -->
  <!-- Stage 1 -->
  <g transform="translate(30, 95)">
    <rect x="0" y="0" width="135" height="240" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="135" height="30" rx="8" fill="#0369a1"/>
    <text x="67" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. INPUT SUPPLY</text>
    <text x="67" y="60" font-size="9" fill="#94a3b8" text-anchor="middle">Certified Seeds</text>
    <text x="67" y="78" font-size="9" fill="#94a3b8" text-anchor="middle">Fertilizers &amp; Feeds</text>
    <text x="67" y="96" font-size="9" fill="#94a3b8" text-anchor="middle">Veterinary Meds</text>
    <text x="67" y="114" font-size="9" fill="#94a3b8" text-anchor="middle">Micro-Credit</text>
    <rect x="10" y="195" width="115" height="30" rx="4" fill="#1e293b"/>
    <text x="67" y="214" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Base Cost ($)</text>
  </g>

  <!-- Arrow 1->2 -->
  <path d="M 170 215 L 182 215" stroke="#64748b" stroke-width="3" fill="none"/>

  <!-- Stage 2 -->
  <g transform="translate(185, 95)">
    <rect x="0" y="0" width="135" height="240" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="135" height="30" rx="8" fill="#15803d"/>
    <text x="67" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. PRODUCTION</text>
    <text x="67" y="60" font-size="9" fill="#94a3b8" text-anchor="middle">Cultivation / Care</text>
    <text x="67" y="78" font-size="9" fill="#94a3b8" text-anchor="middle">Harvesting Crop</text>
    <text x="67" y="96" font-size="9" fill="#94a3b8" text-anchor="middle">Milking Cows</text>
    <text x="67" y="114" font-size="9" fill="#94a3b8" text-anchor="middle">Farm-gate Sale</text>
    <rect x="10" y="195" width="115" height="30" rx="4" fill="#1e293b"/>
    <text x="67" y="214" font-size="9.5" font-weight="bold" fill="#4ade80" text-anchor="middle">Raw Good: $0.40/L</text>
  </g>

  <!-- Arrow 2->3 -->
  <path d="M 325 215 L 337 215" stroke="#64748b" stroke-width="3" fill="none"/>

  <!-- Stage 3 -->
  <g transform="translate(340, 95)">
    <rect x="0" y="0" width="135" height="240" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="135" height="30" rx="8" fill="#d97706"/>
    <text x="67" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. BULKING/TRANS.</text>
    <text x="67" y="60" font-size="9" fill="#94a3b8" text-anchor="middle">Co-op Collection</text>
    <text x="67" y="78" font-size="9" fill="#94a3b8" text-anchor="middle">Chilling Tanks</text>
    <text x="67" y="96" font-size="9" fill="#94a3b8" text-anchor="middle">Grading Quality</text>
    <text x="67" y="114" font-size="9" fill="#94a3b8" text-anchor="middle">Insulated Trucks</text>
    <rect x="10" y="195" width="115" height="30" rx="4" fill="#1e293b"/>
    <text x="67" y="214" font-size="9.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">Bulked: $0.60/L</text>
  </g>

  <!-- Arrow 3->4 -->
  <path d="M 480 215 L 492 215" stroke="#64748b" stroke-width="3" fill="none"/>

  <!-- Stage 4 -->
  <g transform="translate(495, 95)">
    <rect x="0" y="0" width="135" height="240" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <rect x="0" y="0" width="135" height="30" rx="8" fill="#be185d"/>
    <text x="67" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4. PROCESSING</text>
    <text x="67" y="60" font-size="9" fill="#94a3b8" text-anchor="middle">Pasteurization</text>
    <text x="67" y="78" font-size="9" fill="#94a3b8" text-anchor="middle">Yogurt / Cheese</text>
    <text x="67" y="96" font-size="9" fill="#94a3b8" text-anchor="middle">Tetra-Pak Carton</text>
    <text x="67" y="114" font-size="9" fill="#94a3b8" text-anchor="middle">Brand Labeling</text>
    <rect x="10" y="195" width="115" height="30" rx="4" fill="#1e293b"/>
    <text x="67" y="214" font-size="9.5" font-weight="bold" fill="#f472b6" text-anchor="middle">Packaged: $1.20/L</text>
  </g>

  <!-- Arrow 4->5 -->
  <path d="M 635 215 L 647 215" stroke="#64748b" stroke-width="3" fill="none"/>

  <!-- Stage 5 -->
  <g transform="translate(650, 95)">
    <rect x="0" y="0" width="120" height="240" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="0" y="0" width="120" height="30" rx="8" fill="#7e22ce"/>
    <text x="60" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">5. RETAIL</text>
    <text x="60" y="60" font-size="9" fill="#94a3b8" text-anchor="middle">Supermarkets</text>
    <text x="60" y="78" font-size="9" fill="#94a3b8" text-anchor="middle">Local Kiosks</text>
    <text x="60" y="96" font-size="9" fill="#94a3b8" text-anchor="middle">Export Airfreight</text>
    <text x="60" y="114" font-size="9" fill="#94a3b8" text-anchor="middle">Final Consumer</text>
    <rect x="10" y="195" width="100" height="30" rx="4" fill="#1e293b"/>
    <text x="60" y="214" font-size="9.5" font-weight="bold" fill="#c084fc" text-anchor="middle">Retail: $2.50/L</text>
  </g>

  <!-- Value Escalator Bar -->
  <g transform="translate(30, 355)">
    <rect x="0" y="0" width="740" height="35" rx="6" fill="#1e293b" stroke="#334155"/>
    <text x="370" y="22" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">ECONOMIC VALUE MULTIPLIER: Industrial Value Addition Increases Product Worth by 500%+</text>
  </g>
</svg>
""")

# SVG 6: Agricultural Economic Multiplier & Industrial Linkages (Lesson 6)
SVG_ECONOMIC_LINKAGES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">THE SOCIO-ECONOMIC PILLARS OF AGRICULTURE</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">How Farm Production Fuels National GDP, Employment, Forex, and Manufacturing</text>

  <!-- Center Hub -->
  <circle cx="400" cy="225" r="65" fill="#047857" stroke="#34d399" stroke-width="2"/>
  <text x="400" y="220" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">PRIMARY</text>
  <text x="400" y="238" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">AGRICULTURE</text>

  <!-- Node 1: GDP (Top Left) -->
  <g transform="translate(60, 90)">
    <rect x="0" y="0" width="220" height="95" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="110" y="25" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. GDP CONTRIBUTION</text>
    <text x="110" y="48" font-size="10" fill="#cbd5e1" text-anchor="middle">• Directly generates 22% of GDP</text>
    <text x="110" y="66" font-size="10" fill="#cbd5e1" text-anchor="middle">• Indirectly accounts for 27%</text>
    <text x="110" y="84" font-size="10" font-weight="bold" fill="#7dd3fc" text-anchor="middle">Total Impact: &gt;50% of Economy</text>
  </g>
  <line x1="280" y1="145" x2="340" y2="185" stroke="#38bdf8" stroke-width="2"/>

  <!-- Node 2: Employment (Top Right) -->
  <g transform="translate(520, 90)">
    <rect x="0" y="0" width="220" height="95" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="110" y="25" font-size="12" font-weight="bold" fill="#4ade80" text-anchor="middle">2. EMPLOYMENT &amp; LABOR</text>
    <text x="110" y="48" font-size="10" fill="#cbd5e1" text-anchor="middle">• 40% of national labor force</text>
    <text x="110" y="66" font-size="10" fill="#cbd5e1" text-anchor="middle">• &gt;70% of rural household income</text>
    <text x="110" y="84" font-size="10" font-weight="bold" fill="#86efac" text-anchor="middle">Key Source of Rural Livelihoods</text>
  </g>
  <line x1="520" y1="145" x2="460" y2="185" stroke="#22c55e" stroke-width="2"/>

  <!-- Node 3: Forex (Bottom Left) -->
  <g transform="translate(60, 265)">
    <rect x="0" y="0" width="220" height="95" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="110" y="25" font-size="12" font-weight="bold" fill="#fbbf24" text-anchor="middle">3. FOREIGN EXCHANGE</text>
    <text x="110" y="48" font-size="10" fill="#cbd5e1" text-anchor="middle">• Export leaders: Tea, Flowers, Coffee</text>
    <text x="110" y="66" font-size="10" fill="#cbd5e1" text-anchor="middle">• Earns billions in foreign currency</text>
    <text x="110" y="84" font-size="10" font-weight="bold" fill="#fde68a" text-anchor="middle">Funds Fuel, Medicine &amp; Tech Imports</text>
  </g>
  <line x1="280" y1="305" x2="340" y2="265" stroke="#f59e0b" stroke-width="2"/>

  <!-- Node 4: Agro-Processing (Bottom Right) -->
  <g transform="translate(520, 265)">
    <rect x="0" y="0" width="220" height="95" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <text x="110" y="25" font-size="12" font-weight="bold" fill="#f472b6" text-anchor="middle">4. INDUSTRIAL LINKAGES</text>
    <text x="110" y="48" font-size="10" fill="#cbd5e1" text-anchor="middle">• Supplies textile mills (cotton)</text>
    <text x="110" y="66" font-size="10" fill="#cbd5e1" text-anchor="middle">• Supplies edible oil &amp; sugar factories</text>
    <text x="110" y="84" font-size="10" font-weight="bold" fill="#fbcfe8" text-anchor="middle">Drives 70% of Manufacturing</text>
  </g>
  <line x1="520" y1="305" x2="460" y2="265" stroke="#ec4899" stroke-width="2"/>

  <!-- Bottom summary bar -->
  <rect x="60" y="385" width="680" height="28" rx="6" fill="#334155"/>
  <text x="400" y="403" font-size="11" fill="#e2e8f0" text-anchor="middle">Conclusion: Agricultural growth is the most powerful catalyst for national poverty eradication in Africa.</text>
</svg>
""")

# SVG 7: African Agricultural Eco-zones Map (Lesson 7)
SVG_AFRICA_ECOZONES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">AFRICAN AGRO-CLIMATIC &amp; AGRICULTURAL REGIONS</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Spatial Alignment of Continental Climate Belts and Dominant Farming Types</text>

  <!-- Stylized Africa Outline -->
  <g transform="translate(60, 85)">
    <!-- Mediterranean North -->
    <path d="M 50 20 L 220 20 L 250 50 L 30 50 Z" fill="#38bdf8" opacity="0.8"/>
    <text x="140" y="38" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Mediterranean North (Citrus, Olives, Wheat)</text>

    <!-- Saharan Arid -->
    <path d="M 30 50 L 250 50 L 270 120 L 20 120 Z" fill="#d97706" opacity="0.6"/>
    <text x="140" y="88" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Sahara Desert &amp; Oases (Date Palms, Camels)</text>

    <!-- Sahelian Pastoral -->
    <path d="M 20 120 L 270 120 L 270 150 L 15 150 Z" fill="#eab308" opacity="0.7"/>
    <text x="140" y="138" font-size="9.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Sahel Belt (Nomadic Pastoralism &amp; Millet)</text>

    <!-- Equatorial Rain Belt -->
    <path d="M 15 150 L 270 150 L 250 230 L 70 230 L 40 180 Z" fill="#059669" opacity="0.85"/>
    <text x="150" y="190" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Equatorial Belt (Cocoa, Oil Palm, Rubber)</text>

    <!-- Savannah Mixed -->
    <path d="M 70 230 L 250 230 L 220 290 L 110 290 Z" fill="#84cc16" opacity="0.8"/>
    <text x="160" y="260" font-size="9.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Savannah (Maize, Sorghum, Cattle)</text>

    <!-- Mediterranean South -->
    <path d="M 110 290 L 220 290 L 180 320 L 130 320 Z" fill="#38bdf8" opacity="0.8"/>
    <text x="155" y="310" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Cape (Viticulture &amp; Wheat)</text>
  </g>

  <!-- Right: Key Agricultural Zones Legend & Details -->
  <g transform="translate(420, 85)">
    <rect x="0" y="0" width="340" height="325" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    
    <g transform="translate(15, 20)">
      <rect x="0" y="0" width="14" height="14" fill="#38bdf8" rx="2"/>
      <text x="22" y="11" font-size="11" font-weight="bold" fill="#38bdf8">1. Mediterranean Zones (N &amp; S)</text>
      <text x="22" y="27" font-size="9.5" fill="#cbd5e1">• Winter rains, dry summers; Olives, citrus, grapes</text>
    </g>

    <g transform="translate(15, 65)">
      <rect x="0" y="0" width="14" height="14" fill="#d97706" rx="2"/>
      <text x="22" y="11" font-size="11" font-weight="bold" fill="#fbbf24">2. Arid &amp; Semi-Arid (ASALs)</text>
      <text x="22" y="27" font-size="9.5" fill="#cbd5e1">• Rain &lt;300mm; Pastoral nomadism (camels, goats)</text>
    </g>

    <g transform="translate(15, 110)">
      <rect x="0" y="0" width="14" height="14" fill="#eab308" rx="2"/>
      <text x="22" y="11" font-size="11" font-weight="bold" fill="#fde047">3. Sahelian Transition Zone</text>
      <text x="22" y="27" font-size="9.5" fill="#cbd5e1">• Drought-tolerant sorghum, millet, extensive grazing</text>
    </g>

    <g transform="translate(15, 155)">
      <rect x="0" y="0" width="14" height="14" fill="#059669" rx="2"/>
      <text x="22" y="11" font-size="11" font-weight="bold" fill="#34d399">4. Equatorial Rainforest Belt</text>
      <text x="22" y="27" font-size="9.5" fill="#cbd5e1">• Heavy rain &gt;1,600mm; Cocoa, oil palm, rubber estates</text>
    </g>

    <g transform="translate(15, 200)">
      <rect x="0" y="0" width="14" height="14" fill="#84cc16" rx="2"/>
      <text x="22" y="11" font-size="11" font-weight="bold" fill="#a3e635">5. Tropical Savannah &amp; Highlands</text>
      <text x="22" y="27" font-size="9.5" fill="#cbd5e1">• Bimodal rain; Tea, coffee, maize, mixed dairy-crop</text>
    </g>

    <g transform="translate(15, 245)">
      <rect x="0" y="0" width="14" height="14" fill="#64748b" rx="2"/>
      <text x="22" y="11" font-size="11" font-weight="bold" fill="#94a3b8">6. Temperate Highveld Plains</text>
      <text x="22" y="27" font-size="9.5" fill="#cbd5e1">• Large-scale mechanized commercial wheat and beef</text>
    </g>
  </g>
</svg>
""")

# SVG 8: Digital Agriculture & Agribusiness Ecosystem (Lesson 8)
SVG_DIGITAL_ECOSYSTEM = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">DIGITAL AGRONOMY &amp; AGRITECH ECOSYSTEM IN AFRICA</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">How Mobile Platforms, Satellite Data, Solar Cold Chains, and FinTech Empower Smallholders</text>

  <!-- Central Mobile Hub -->
  <g transform="translate(325, 110)">
    <rect x="0" y="0" width="150" height="230" rx="16" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
    <rect x="15" y="20" width="120" height="180" rx="8" fill="#1e293b"/>
    <circle cx="75" cy="215" r="6" fill="#38bdf8"/>
    <text x="75" y="45" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">FARMER APP</text>
    <text x="75" y="70" font-size="9" fill="#cbd5e1" text-anchor="middle">Weather Alert</text>
    <text x="75" y="88" font-size="9" fill="#cbd5e1" text-anchor="middle">Market Price: $0.85</text>
    <text x="75" y="106" font-size="9" fill="#cbd5e1" text-anchor="middle">Pest AI Scan: OK</text>
    <text x="75" y="124" font-size="9" fill="#cbd5e1" text-anchor="middle">Mobile Loan: Paid</text>
    <rect x="30" y="145" width="90" height="25" rx="4" fill="#0284c7"/>
    <text x="75" y="162" font-size="9.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Sell Harvest</text>
  </g>

  <!-- 4 Connected Nodes -->
  <!-- Top Left: Satellite & Drone Sensing -->
  <g transform="translate(45, 95)">
    <rect x="0" y="0" width="220" height="100" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="110" y="24" font-size="11.5" font-weight="bold" fill="#4ade80" text-anchor="middle">1. SATELLITE &amp; DRONE AGTECH</text>
    <text x="110" y="48" font-size="9.5" fill="#cbd5e1" text-anchor="middle">• NDVI crop vigor indices</text>
    <text x="110" y="66" font-size="9.5" fill="#cbd5e1" text-anchor="middle">• 7-day localized rainfall forecasts</text>
    <text x="110" y="84" font-size="9.5" fill="#cbd5e1" text-anchor="middle">• Automated index drought insurance</text>
  </g>
  <line x1="265" y1="145" x2="325" y2="175" stroke="#22c55e" stroke-width="2"/>

  <!-- Bottom Left: Solar Cold-Chain -->
  <g transform="translate(45, 240)">
    <rect x="0" y="0" width="220" height="100" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="110" y="24" font-size="11.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">2. SOLAR COLD STORAGE</text>
    <text x="110" y="48" font-size="9.5" fill="#cbd5e1" text-anchor="middle">• Off-grid solar-powered chill rooms</text>
    <text x="110" y="66" font-size="9.5" fill="#cbd5e1" text-anchor="middle">• Extends tomato/milk life to 21 days</text>
    <text x="110" y="84" font-size="9.5" fill="#cbd5e1" text-anchor="middle">• Eliminates panic farm-gate dumping</text>
  </g>
  <line x1="265" y1="290" x2="325" y2="255" stroke="#f59e0b" stroke-width="2"/>

  <!-- Top Right: Mobile Money & FinTech -->
  <g transform="translate(535, 95)">
    <rect x="0" y="0" width="220" height="100" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="110" y="24" font-size="11.5" font-weight="bold" fill="#c084fc" text-anchor="middle">3. MOBILE FINTECH &amp; CREDIT</text>
    <text x="110" y="48" font-size="9.5" fill="#cbd5e1" text-anchor="middle">• Instant M-Pesa digital payments</text>
    <text x="110" y="66" font-size="9.5" fill="#cbd5e1" text-anchor="middle">• Collateral-free seasonal micro-loans</text>
    <text x="110" y="84" font-size="9.5" fill="#cbd5e1" text-anchor="middle">• Direct purchase of certified seeds</text>
  </g>
  <line x1="535" y1="145" x2="475" y2="175" stroke="#a855f7" stroke-width="2"/>

  <!-- Bottom Right: Direct E-Commerce -->
  <g transform="translate(535, 240)">
    <rect x="0" y="0" width="220" height="100" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <text x="110" y="24" font-size="11.5" font-weight="bold" fill="#f472b6" text-anchor="middle">4. B2B AGRI-COMMERCE</text>
    <text x="110" y="48" font-size="9.5" fill="#cbd5e1" text-anchor="middle">• Connects farmers to urban retailers</text>
    <text x="110" y="66" font-size="9.5" fill="#cbd5e1" text-anchor="middle">• Bypasses exploitative brokers</text>
    <text x="110" y="84" font-size="9.5" fill="#cbd5e1" text-anchor="middle">• Cuts supply chain losses to &lt;5%</text>
  </g>
  <line x1="535" y1="290" x2="475" y2="255" stroke="#ec4899" stroke-width="2"/>

  <!-- Footer -->
  <rect x="45" y="375" width="710" height="28" rx="6" fill="#334155"/>
  <text x="400" y="393" font-size="11" fill="#e2e8f0" text-anchor="middle">Impact: Information transparency and FinTech unlock commercial prosperity for smallholder farmers.</text>
</svg>
""")

# SVG 9: Kenya Agro-Ecological Zones & Climate Hazard Vulnerability (Lesson 9)
SVG_CLIMATE_HAZARDS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">KENYA AGRO-ECOLOGICAL HAZARDS &amp; THREAT MATRIX</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Vulnerability to Rainfall Volatility, Invertebrate Pests, and Crop Diseases</text>

  <!-- 3 Hazard Columns -->
  <!-- Col 1: Climate Hazards -->
  <g transform="translate(35, 85)">
    <rect x="0" y="0" width="225" height="325" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="225" height="32" rx="10" fill="#b91c1c"/>
    <text x="112" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. CLIMATIC HAZARDS</text>

    <text x="12" y="55" font-size="11" font-weight="bold" fill="#f87171">• Over-Reliance on Rain:</text>
    <text x="12" y="73" font-size="9.5" fill="#cbd5e1">&gt;80% of Kenya is rainfed farming</text>
    <text x="12" y="89" font-size="9.5" fill="#cbd5e1">Vulnerable to delayed seasonal onset</text>

    <text x="12" y="120" font-size="11" font-weight="bold" fill="#f87171">• Recurrent Severe Droughts:</text>
    <text x="12" y="138" font-size="9.5" fill="#cbd5e1">Stunts cereal growth</text>
    <text x="12" y="154" font-size="9.5" fill="#cbd5e1">Pastoral cattle mortality in ASALs</text>

    <text x="12" y="185" font-size="11" font-weight="bold" fill="#f87171">• Flash Floods &amp; Mudslides:</text>
    <text x="12" y="203" font-size="9.5" fill="#cbd5e1">Washes away fertile highland topsoil</text>
    <text x="12" y="219" font-size="9.5" fill="#cbd5e1">Destroys bridges and rural roads</text>

    <rect x="15" y="260" width="195" height="45" rx="6" fill="#1e293b"/>
    <text x="112" y="280" font-size="9" font-weight="bold" fill="#fca5a5" text-anchor="middle">Hotspots: Turkana, Garissa,</text>
    <text x="112" y="295" font-size="9" fill="#cbd5e1" text-anchor="middle">Kitui, Mandera, Wajir</text>
  </g>

  <!-- Col 2: Biological Pests -->
  <g transform="translate(285, 85)">
    <rect x="0" y="0" width="225" height="325" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="225" height="32" rx="10" fill="#d97706"/>
    <text x="112" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. INVASIVE PESTS</text>

    <text x="12" y="55" font-size="11" font-weight="bold" fill="#fbbf24">• Fall Armyworm:</text>
    <text x="12" y="73" font-size="9.5" fill="#cbd5e1">Bores into maize whorls &amp; cobs</text>
    <text x="12" y="89" font-size="9.5" fill="#cbd5e1">Causes 30-50% harvest destruction</text>

    <text x="12" y="120" font-size="11" font-weight="bold" fill="#fbbf24">• Desert Locust Swarms:</text>
    <text x="12" y="138" font-size="9.5" fill="#cbd5e1">Migratory swarms consume 100%</text>
    <text x="12" y="154" font-size="9.5" fill="#cbd5e1">of green vegetation in hours</text>

    <text x="12" y="185" font-size="11" font-weight="bold" fill="#fbbf24">• Storage Weevils &amp; Rodents:</text>
    <text x="12" y="203" font-size="9.5" fill="#cbd5e1">Infests unsealed wooden granaries</text>
    <text x="12" y="219" font-size="9.5" fill="#cbd5e1">Consumes 20% of stored cereals</text>

    <rect x="15" y="260" width="195" height="45" rx="6" fill="#1e293b"/>
    <text x="112" y="280" font-size="9" font-weight="bold" fill="#fde68a" text-anchor="middle">Hotspots: Trans-Nzoia,</text>
    <text x="112" y="295" font-size="9" fill="#cbd5e1" text-anchor="middle">Uasin Gishu, Samburu</text>
  </g>

  <!-- Col 3: Pathogens & Land Degradation -->
  <g transform="translate(535, 85)">
    <rect x="0" y="0" width="225" height="325" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="0" y="0" width="225" height="32" rx="10" fill="#7e22ce"/>
    <text x="112" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. PATHOGENS &amp; SOIL</text>

    <text x="12" y="55" font-size="11" font-weight="bold" fill="#c084fc">• Maize Lethal Necrosis:</text>
    <text x="12" y="73" font-size="9.5" fill="#cbd5e1">Viral disease causing complete chlorosis</text>
    <text x="12" y="89" font-size="9.5" fill="#cbd5e1">Zero grain yield in infected plots</text>

    <text x="12" y="120" font-size="11" font-weight="bold" fill="#c084fc">• Coffee Berry Disease (CBD):</text>
    <text x="12" y="138" font-size="9.5" fill="#cbd5e1">Fungal rotting of green berries</text>
    <text x="12" y="154" font-size="9.5" fill="#cbd5e1">Halts cash crop export revenue</text>

    <text x="12" y="185" font-size="11" font-weight="bold" fill="#c084fc">• Soil Nutrient Depletion:</text>
    <text x="12" y="203" font-size="9.5" fill="#cbd5e1">Continuous monoculture without fallow</text>
    <text x="12" y="219" font-size="9.5" fill="#cbd5e1">Severe topsoil acidification</text>

    <rect x="15" y="260" width="195" height="45" rx="6" fill="#1e293b"/>
    <text x="112" y="280" font-size="9" font-weight="bold" fill="#e9d5ff" text-anchor="middle">Hotspots: Nyeri, Murang'a,</text>
    <text x="112" y="295" font-size="9" fill="#cbd5e1" text-anchor="middle">Bomet, Kisii highlands</text>
  </g>
</svg>
""")

# SVG 10: Post-Harvest Loss Interventions & Storage (Lesson 10)
SVG_POST_HARVEST = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">CURBING POST-HARVEST LOSSES (PHL) IN KENYA</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Traditional Vulnerabilities vs. Modern Technological Storage Interventions</text>

  <!-- Left: Traditional Loss Points -->
  <g transform="translate(45, 85)">
    <rect x="0" y="0" width="335" height="325" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="335" height="34" rx="10" fill="#b91c1c"/>
    <text x="167" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">TRADITIONAL STORAGE LOSSES (30-40%)</text>

    <g transform="translate(15, 45)">
      <text x="0" y="15" font-size="11" font-weight="bold" fill="#f87171">1. Unsealed Wooden Granaries:</text>
      <text x="0" y="32" font-size="9.5" fill="#cbd5e1">• Rodents (rats) and weevils bore into bags</text>
      <text x="0" y="48" font-size="9.5" fill="#cbd5e1">• Rain dampness causes fungal aflatoxin contamination</text>
    </g>

    <g transform="translate(15, 115)">
      <text x="0" y="15" font-size="11" font-weight="bold" fill="#f87171">2. Muddy Feeder Roads:</text>
      <text x="0" y="32" font-size="9.5" fill="#cbd5e1">• Trucks get stuck during seasonal harvest rains</text>
      <text x="0" y="48" font-size="9.5" fill="#cbd5e1">• Perishable tomatoes, milk, and mangoes rot</text>
    </g>

    <g transform="translate(15, 185)">
      <text x="0" y="15" font-size="11" font-weight="bold" fill="#f87171">3. Lack of On-Farm Cold Storage:</text>
      <text x="0" y="32" font-size="9.5" fill="#cbd5e1">• Farmers forced to sell to middlemen at throwaway prices</text>
      <text x="0" y="48" font-size="9.5" fill="#cbd5e1">• Severe financial depression for rural households</text>
    </g>

    <rect x="15" y="260" width="305" height="45" rx="6" fill="#450a0a" stroke="#f87171"/>
    <text x="152" y="287" font-size="11" font-weight="bold" fill="#fca5a5" text-anchor="middle">Net Economic Loss: &gt;KSh 50 Billion Annually</text>
  </g>

  <!-- Right: Modern Interventions -->
  <g transform="translate(420, 85)">
    <rect x="0" y="0" width="335" height="325" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="335" height="34" rx="10" fill="#15803d"/>
    <text x="167" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">MODERN CSA INTERVENTIONS (&lt;5% LOSS)</text>

    <g transform="translate(15, 45)">
      <text x="0" y="15" font-size="11" font-weight="bold" fill="#4ade80">1. Hermetic PICS Storage Bags:</text>
      <text x="0" y="32" font-size="9.5" fill="#cbd5e1">• Airtight triple-layer plastic suffocates weevils</text>
      <text x="0" y="48" font-size="9.5" fill="#cbd5e1">• Zero synthetic chemical insecticide dusts required</text>
    </g>

    <g transform="translate(15, 115)">
      <text x="0" y="15" font-size="11" font-weight="bold" fill="#4ade80">2. Solar Bubble Dryers &amp; Metal Silos:</text>
      <text x="0" y="32" font-size="9.5" fill="#cbd5e1">• Dries grain to &lt;13.5% moisture, stopping aflatoxin</text>
      <text x="0" y="48" font-size="9.5" fill="#cbd5e1">• Galvanized metal silos block all rodents</text>
    </g>

    <g transform="translate(15, 185)">
      <text x="0" y="15" font-size="11" font-weight="bold" fill="#4ade80">3. Pay-As-You-Store Solar Chillers:</text>
      <text x="0" y="32" font-size="9.5" fill="#cbd5e1">• Decentralized cooling rooms at rural trading markets</text>
      <text x="0" y="48" font-size="9.5" fill="#cbd5e1">• Farmers hold produce until market prices peak</text>
    </g>

    <rect x="15" y="260" width="305" height="45" rx="6" fill="#064e3b" stroke="#34d399"/>
    <text x="152" y="287" font-size="11" font-weight="bold" fill="#86efac" text-anchor="middle">Farmer Incomes Increase by 25 - 40%</text>
  </g>
</svg>
""")

# SVG 11: Climate-Smart Agriculture Matrix (Lesson 11)
SVG_CSA_MATRIX = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">CLIMATE-SMART AGRICULTURE (CSA) ENGINEERING</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Soil Conservation, Terracing Mechanics, Agroforestry, and Drip Fertigation</text>

  <!-- 3 CSA Technology Panels -->
  <!-- Panel 1: Fanya Juu Terracing -->
  <g transform="translate(35, 85)">
    <rect x="0" y="0" width="225" height="325" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="225" height="32" rx="10" fill="#15803d"/>
    <text x="112" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. FANYA JUU TERRACING</text>

    <!-- Cross section graphic -->
    <path d="M 20 80 L 80 130 L 140 100 L 205 150" stroke="#f59e0b" stroke-width="2" fill="none"/>
    <polygon points="80,130 110,85 140,100" fill="#78350f"/>
    <text x="112" y="75" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">Ridge (Soil Thrown Uphill)</text>
    <text x="50" y="150" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Trench (Infiltration)</text>

    <text x="12" y="185" font-size="10.5" font-weight="bold" fill="#4ade80">Mechanics:</text>
    <text x="12" y="203" font-size="9.5" fill="#cbd5e1">• Trench dug along contour line</text>
    <text x="12" y="219" font-size="9.5" fill="#cbd5e1">• Soil thrown uphill creates ridge</text>
    <text x="12" y="235" font-size="9.5" fill="#cbd5e1">• Napier grass binds ridge roots</text>
    <text x="12" y="251" font-size="9.5" fill="#cbd5e1">• Over time forms flat benches</text>
    <text x="12" y="280" font-size="10" font-weight="bold" fill="#86efac">Benefit: 100% Runoff Trapped</text>
  </g>

  <!-- Panel 2: Agroforestry Systems -->
  <g transform="translate(285, 85)">
    <rect x="0" y="0" width="225" height="325" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="225" height="32" rx="10" fill="#0369a1"/>
    <text x="112" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. AGROFORESTRY</text>

    <!-- Tree graphic -->
    <path d="M 112 75 L 112 140" stroke="#78350f" stroke-width="6"/>
    <circle cx="112" cy="75" r="28" fill="#15803d"/>
    <circle cx="95" cy="85" r="18" fill="#16a34a"/>
    <circle cx="130" cy="85" r="18" fill="#16a34a"/>
    <path d="M 90 140 Q 112 170 112 180 Q 112 170 135 140" stroke="#94a3b8" stroke-width="1.5" fill="none"/>
    <text x="112" y="165" font-size="8.5" fill="#38bdf8" text-anchor="middle">Deep Taproots</text>

    <text x="12" y="195" font-size="10.5" font-weight="bold" fill="#38bdf8">Mechanics:</text>
    <text x="12" y="213" font-size="9.5" fill="#cbd5e1">• Trees integrated with food crops</text>
    <text x="12" y="229" font-size="9.5" fill="#cbd5e1">• Deep roots access deep water</text>
    <text x="12" y="245" font-size="9.5" fill="#cbd5e1">• Leaves fix atmospheric nitrogen</text>
    <text x="12" y="261" font-size="9.5" fill="#cbd5e1">• Provides firewood, fruit &amp; timber</text>
    <text x="12" y="285" font-size="10" font-weight="bold" fill="#7dd3fc">Species: Grevillea, Calliandra</text>
  </g>

  <!-- Panel 3: Solar Drip & Mulching -->
  <g transform="translate(535, 85)">
    <rect x="0" y="0" width="225" height="325" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="225" height="32" rx="10" fill="#d97706"/>
    <text x="112" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. DRIP &amp; MULCHING</text>

    <!-- Drip pipe with drops -->
    <rect x="25" y="80" width="175" height="10" rx="3" fill="#334155"/>
    <circle cx="60" cy="100" r="4" fill="#38bdf8"/>
    <circle cx="112" cy="100" r="4" fill="#38bdf8"/>
    <circle cx="165" cy="100" r="4" fill="#38bdf8"/>
    <!-- Mulch layer -->
    <rect x="25" y="115" width="175" height="12" rx="2" fill="#ca8a04"/>
    <text x="112" y="140" font-size="8.5" fill="#fde047" text-anchor="middle">Organic Mulch Barrier</text>

    <text x="12" y="185" font-size="10.5" font-weight="bold" fill="#fbbf24">Mechanics:</text>
    <text x="12" y="203" font-size="9.5" fill="#cbd5e1">• Drip pipes deliver water to root zone</text>
    <text x="12" y="219" font-size="9.5" fill="#cbd5e1">• Uses 90% less water than floods</text>
    <text x="12" y="235" font-size="9.5" fill="#cbd5e1">• Mulch stops solar evaporation</text>
    <text x="12" y="251" font-size="9.5" fill="#cbd5e1">• Suppresses weed growth naturally</text>
    <text x="12" y="280" font-size="10" font-weight="bold" fill="#fde68a">Powered by: Mini Solar PV</text>
  </g>
</svg>
""")

# SVG 12: Food Security 4-Pillars Pillar Model (Lesson 12)
SVG_FOOD_SECURITY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">THE FOUR PILLARS OF FOOD SECURITY</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">FAO Conceptual Framework: Availability, Access, Utilization, and Stability</text>

  <!-- Pediment (Top Roof) -->
  <polygon points="400,80 100,120 700,120" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="400" y="110" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">COMPLETE NATIONAL &amp; HOUSEHOLD FOOD SECURITY</text>

  <!-- 4 Pillars -->
  <!-- Pillar 1: Availability -->
  <g transform="translate(110, 125)">
    <rect x="0" y="0" width="125" height="230" rx="4" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="125" height="28" fill="#15803d"/>
    <text x="62" y="19" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1. AVAILABILITY</text>
    <text x="62" y="48" font-size="9.5" font-weight="bold" fill="#4ade80" text-anchor="middle">Is Food Present?</text>
    <text x="62" y="75" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Domestic crop yields</text>
    <text x="62" y="95" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• National grain silos</text>
    <text x="62" y="115" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Commercial imports</text>
    <text x="62" y="135" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Emergency reserves</text>
    <text x="62" y="155" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Livestock stocks</text>
  </g>

  <!-- Pillar 2: Access -->
  <g transform="translate(255, 125)">
    <rect x="0" y="0" width="125" height="230" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="125" height="28" fill="#0369a1"/>
    <text x="62" y="19" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2. ACCESS</text>
    <text x="62" y="48" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Can People Buy It?</text>
    <text x="62" y="75" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Household incomes</text>
    <text x="62" y="95" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Affordable food prices</text>
    <text x="62" y="115" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Feeder road transport</text>
    <text x="62" y="135" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Social safety nets</text>
    <text x="62" y="155" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Fair market access</text>
  </g>

  <!-- Pillar 3: Utilization -->
  <g transform="translate(400, 125)">
    <rect x="0" y="0" width="125" height="230" rx="4" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect x="0" y="0" width="125" height="28" fill="#d97706"/>
    <text x="62" y="19" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">3. UTILIZATION</text>
    <text x="62" y="48" font-size="9.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">Is It Nutritious?</text>
    <text x="62" y="75" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Balanced nutrition</text>
    <text x="62" y="95" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Clean drinking water</text>
    <text x="62" y="115" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Safe food handling</text>
    <text x="62" y="135" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Micronutrient density</text>
    <text x="62" y="155" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• No hidden hunger</text>
  </g>

  <!-- Pillar 4: Stability -->
  <g transform="translate(545, 125)">
    <rect x="0" y="0" width="145" height="230" rx="4" fill="#0f172a" stroke="#ec4899" stroke-width="2"/>
    <rect x="0" y="0" width="145" height="28" fill="#be185d"/>
    <text x="72" y="19" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">4. STABILITY</text>
    <text x="72" y="48" font-size="9.5" font-weight="bold" fill="#f472b6" text-anchor="middle">Is It Consistent Year-Round?</text>
    <text x="72" y="75" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Climate resilience</text>
    <text x="72" y="95" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Price spike controls</text>
    <text x="72" y="115" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Strategic buffer grain</text>
    <text x="72" y="135" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Sustainable farming</text>
    <text x="72" y="155" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Political peace</text>
  </g>

  <!-- Foundation (Bottom Base) -->
  <rect x="90" y="360" width="620" height="35" rx="6" fill="#334155" stroke="#475569"/>
  <text x="400" y="382" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">FOUNDATION: SUSTAINABLE AGRICULTURAL PRODUCTIVITY &amp; EQUITABLE ECONOMIC GROWTH</text>
</svg>
""")

# SVG 13: Fieldwork Agricultural Data Collection Flow (Lesson 13)
SVG_FIELDWORK_FLOW = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">AGRICULTURAL FIELDWORK INQUIRY LIFECYCLE</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Scientific Protocols for Primary Farm Data Collection, Mapping, and Synthesis</text>

  <!-- 4 Step Flow -->
  <!-- Step 1 -->
  <g transform="translate(35, 95)">
    <rect x="0" y="0" width="165" height="230" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="165" height="30" rx="10" fill="#0369a1"/>
    <text x="82" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 1: PREPARATION</text>

    <text x="10" y="55" font-size="10" font-weight="bold" fill="#38bdf8">• Research Objectives:</text>
    <text x="10" y="72" font-size="9" fill="#cbd5e1">Formulate focused goals</text>
    <text x="10" y="95" font-size="10" font-weight="bold" fill="#38bdf8">• Design Instruments:</text>
    <text x="10" y="112" font-size="9" fill="#cbd5e1">Checklists &amp; questionnaires</text>
    <text x="10" y="135" font-size="10" font-weight="bold" fill="#38bdf8">• Logistics &amp; Ethics:</text>
    <text x="10" y="152" font-size="9" fill="#cbd5e1">Farmer consent &amp; routes</text>
    <text x="10" y="175" font-size="10" font-weight="bold" fill="#38bdf8">• Safety Equipment:</text>
    <text x="10" y="192" font-size="9" fill="#cbd5e1">Boots, hats, first aid kits</text>
  </g>

  <!-- Connector 1->2 -->
  <polygon points="208,210 220,210 220,205 230,210 220,215 220,210" fill="#f59e0b"/>

  <!-- Step 2 -->
  <g transform="translate(230, 95)">
    <rect x="0" y="0" width="165" height="230" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="165" height="30" rx="10" fill="#d97706"/>
    <text x="82" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 2: ON-SITE DATA</text>

    <text x="10" y="55" font-size="10" font-weight="bold" fill="#fbbf24">• Transect Walk:</text>
    <text x="10" y="72" font-size="9" fill="#cbd5e1">Ridge to valley profiling</text>
    <text x="10" y="95" font-size="10" font-weight="bold" fill="#fbbf24">• Observation Matrix:</text>
    <text x="10" y="112" font-size="9" fill="#cbd5e1">Record crops, terraces, pests</text>
    <text x="10" y="135" font-size="10" font-weight="bold" fill="#fbbf24">• Farmer Interviews:</text>
    <text x="10" y="152" font-size="9" fill="#cbd5e1">Input costs, yields, margins</text>
    <text x="10" y="175" font-size="10" font-weight="bold" fill="#fbbf24">• Soil Sampling:</text>
    <text x="10" y="192" font-size="9" fill="#cbd5e1">Texture, pH &amp; moisture tests</text>
  </g>

  <!-- Connector 2->3 -->
  <polygon points="403,210 415,210 415,205 425,210 415,215 415,210" fill="#22c55e"/>

  <!-- Step 3 -->
  <g transform="translate(425, 95)">
    <rect x="0" y="0" width="165" height="230" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="165" height="30" rx="10" fill="#15803d"/>
    <text x="82" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 3: DATA ANALYSIS</text>

    <text x="10" y="55" font-size="10" font-weight="bold" fill="#4ade80">• Quantitative Stats:</text>
    <text x="10" y="72" font-size="9" fill="#cbd5e1">Yield/acre &amp; loss rates</text>
    <text x="10" y="95" font-size="10" font-weight="bold" fill="#4ade80">• Spatial Mapping:</text>
    <text x="10" y="112" font-size="9" fill="#cbd5e1">Draw farm layout sketch</text>
    <text x="10" y="135" font-size="10" font-weight="bold" fill="#4ade80">• Cross-Tabulation:</text>
    <text x="10" y="152" font-size="9" fill="#cbd5e1">Correlate inputs vs profit</text>
    <text x="10" y="175" font-size="10" font-weight="bold" fill="#4ade80">• Identify Constraints:</text>
    <text x="10" y="192" font-size="9" fill="#cbd5e1">Pinpoint bottleneck causes</text>
  </g>

  <!-- Connector 3->4 -->
  <polygon points="598,210 610,210 610,205 620,210 610,215 610,210" fill="#ec4899"/>

  <!-- Step 4 -->
  <g transform="translate(620, 95)">
    <rect x="0" y="0" width="145" height="230" rx="10" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <rect x="0" y="0" width="145" height="30" rx="10" fill="#be185d"/>
    <text x="72" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 4: REPORT</text>

    <text x="10" y="55" font-size="10" font-weight="bold" fill="#f472b6">• Research Report:</text>
    <text x="10" y="72" font-size="9" fill="#cbd5e1">Formal academic write-up</text>
    <text x="10" y="95" font-size="10" font-weight="bold" fill="#f472b6">• Policy Brief:</text>
    <text x="10" y="112" font-size="9" fill="#cbd5e1">Recommendations for leaders</text>
    <text x="10" y="135" font-size="10" font-weight="bold" fill="#f472b6">• Extension Poster:</text>
    <text x="10" y="152" font-size="9" fill="#cbd5e1">Visual guide for farmers</text>
    <text x="10" y="175" font-size="10" font-weight="bold" fill="#f472b6">• Community Feedback:</text>
    <text x="10" y="192" font-size="9" fill="#cbd5e1">Share insights with hosts</text>
  </g>

  <!-- Bottom bar -->
  <rect x="35" y="360" width="730" height="30" rx="6" fill="#334155"/>
  <text x="400" y="379" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Fieldwork Golden Rule: Respect farmer privacy, secure informed consent, and practice rigorous data hygiene.</text>
</svg>
""")

# SVG 14: Policy Brief Infographic Layout (Lesson 14)
SVG_POLICY_BRIEF = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">AGRICULTURAL POLICY BRIEF ARCHITECTURE</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Translating Geographical Research into High-Impact Actionable Policy Recommendations</text>

  <!-- Policy Brief Mockup Document -->
  <g transform="translate(60, 85)">
    <rect x="0" y="0" width="680" height="325" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>

    <!-- 1. Header Banner -->
    <rect x="15" y="12" width="650" height="40" rx="6" fill="#0284c7"/>
    <text x="340" y="32" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">POLICY BRIEF: SCALING SOLAR DRIP IRRIGATION IN MACHAKOS COUNTY</text>
    <text x="340" y="46" font-size="9" fill="#e0f2fe" text-anchor="middle">Target Audience: County Executive Committee (CEC) for Agriculture &amp; Farmer Cooperatives</text>

    <!-- 2. Executive Summary -->
    <g transform="translate(15, 60)">
      <rect x="0" y="0" width="650" height="42" rx="4" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="16" font-size="10" font-weight="bold" fill="#fbbf24">EXECUTIVE SUMMARY:</text>
      <text x="10" y="32" font-size="9" fill="#cbd5e1">Delayed rains have triggered a 40% loss in seasonal maize harvests across 50,000 households. Transitioning to subsidized solar drip kits will double yields while using 85% less water.</text>
    </g>

    <!-- 3. Problem Statement & 4. Empirical Evidence (2 columns) -->
    <g transform="translate(15, 110)">
      <!-- Left: The Problem -->
      <rect x="0" y="0" width="315" height="90" rx="4" fill="#1e293b" stroke="#ef4444"/>
      <text x="10" y="18" font-size="10" font-weight="bold" fill="#f87171">THE CRISIS (EVIDENCE-BASED):</text>
      <text x="10" y="36" font-size="8.5" fill="#cbd5e1">• Over 88% of smallholders rely on rainfed monoculture</text>
      <text x="10" y="52" font-size="8.5" fill="#cbd5e1">• Mid-season dry spells cause 55% kernel abortion in maize</text>
      <text x="10" y="68" font-size="8.5" fill="#cbd5e1">• Post-harvest rotting causes KSh 120M annual loss</text>

      <!-- Right: Research Evidence Graphic -->
      <rect x="335" y="0" width="315" height="90" rx="4" fill="#1e293b" stroke="#22c55e"/>
      <text x="345" y="18" font-size="10" font-weight="bold" fill="#4ade80">EMPIRICAL TRIAL RESULTS (FIELD DATA):</text>
      <text x="345" y="36" font-size="8.5" fill="#cbd5e1">• Solar drip plots achieved 3.8 tons/ha vs 1.1 tons rainfed</text>
      <text x="345" y="52" font-size="8.5" fill="#cbd5e1">• Water efficiency improved from 25% to 92%</text>
      <text x="345" y="68" font-size="8.5" fill="#cbd5e1">• Payback period on 1-acre solar kit is 1.4 seasons</text>
    </g>

    <!-- 5. Actionable Recommendations -->
    <g transform="translate(15, 210)">
      <rect x="0" y="0" width="650" height="95" rx="4" fill="#1e293b" stroke="#38bdf8"/>
      <text x="10" y="18" font-size="10.5" font-weight="bold" fill="#38bdf8">ACTIONABLE POLICY RECOMMENDATIONS:</text>
      <text x="10" y="36" font-size="9" fill="#cbd5e1">1. <tspan font-weight="bold" fill="#ffffff">Budget Allocation:</tspan> Direct 12% of County Ward Development Funds to co-finance 500 community solar drip kits.</text>
      <text x="10" y="54" font-size="9" fill="#cbd5e1">2. <tspan font-weight="bold" fill="#ffffff">Cooperative Aggregation:</tspan> Partner with local micro-lenders to provide zero-interest kit financing to registered women's groups.</text>
      <text x="10" y="72" font-size="9" fill="#cbd5e1">3. <tspan font-weight="bold" fill="#ffffff">Extension Scaling:</tspan> Deploy 30 technical extension agronomists to train farmers on drip fertigation and contour mulching.</text>
    </g>
  </g>
</svg>
""")

# SVG 15: Master Agriculture Synthesis & Decision Tree (Lesson 15)
SVG_MASTER_SYNTHESIS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">MASTER SYNTHESIS: SUSTAINABLE AGRICULTURAL GEOGRAPHY</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Holistic Architecture Connecting Environmental Drivers, Challenges, CSA Solutions, and Food Security</text>

  <!-- 4 Step Sequential Process -->
  <!-- Step 1: System Baseline -->
  <g transform="translate(30, 90)">
    <rect x="0" y="0" width="165" height="235" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
    <rect x="0" y="0" width="165" height="28" rx="8" fill="#0369a1"/>
    <text x="82" y="19" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1. SYSTEM BASELINE</text>
    
    <text x="10" y="50" font-size="9.5" font-weight="bold" fill="#38bdf8">Physical Drivers:</text>
    <text x="10" y="68" font-size="8.5" fill="#cbd5e1">• Rainfall &amp; Temp</text>
    <text x="10" y="84" font-size="8.5" fill="#cbd5e1">• Volcanic soil &amp; slope</text>
    
    <text x="10" y="110" font-size="9.5" font-weight="bold" fill="#38bdf8">Human Drivers:</text>
    <text x="10" y="128" font-size="8.5" fill="#cbd5e1">• Capital &amp; labor</text>
    <text x="10" y="144" font-size="8.5" fill="#cbd5e1">• Transport &amp; market</text>
    
    <text x="10" y="170" font-size="9.5" font-weight="bold" fill="#38bdf8">Classification:</text>
    <text x="10" y="188" font-size="8.5" fill="#cbd5e1">• Subsistence vs Comm.</text>
    <text x="10" y="204" font-size="8.5" fill="#cbd5e1">• Intensive vs Exten.</text>
  </g>

  <!-- Arrow 1->2 -->
  <polygon points="200,205 212,205 212,200 220,205 212,210 212,205" fill="#ef4444"/>

  <!-- Step 2: System Challenges -->
  <g transform="translate(225, 90)">
    <rect x="0" y="0" width="165" height="235" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="165" height="28" rx="8" fill="#b91c1c"/>
    <text x="82" y="19" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2. KEY CHALLENGES</text>

    <text x="10" y="50" font-size="9.5" font-weight="bold" fill="#f87171">Climatic Risks:</text>
    <text x="10" y="68" font-size="8.5" fill="#cbd5e1">• &gt;80% rainfed farming</text>
    <text x="10" y="84" font-size="8.5" fill="#cbd5e1">• Droughts &amp; floods</text>

    <text x="10" y="110" font-size="9.5" font-weight="bold" fill="#f87171">Biological Threats:</text>
    <text x="10" y="128" font-size="8.5" fill="#cbd5e1">• Armyworms &amp; Locusts</text>
    <text x="10" y="144" font-size="8.5" fill="#cbd5e1">• Maize Lethal Necrosis</text>

    <text x="10" y="170" font-size="9.5" font-weight="bold" fill="#f87171">Structural Hurdles:</text>
    <text x="10" y="188" font-size="8.5" fill="#cbd5e1">• Land fragmentation</text>
    <text x="10" y="204" font-size="8.5" fill="#cbd5e1">• 30-40% Post-harvest loss</text>
  </g>

  <!-- Arrow 2->3 -->
  <polygon points="395,205 407,205 407,200 415,205 407,210 407,205" fill="#22c55e"/>

  <!-- Step 3: CSA Interventions -->
  <g transform="translate(420, 90)">
    <rect x="0" y="0" width="165" height="235" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="165" height="28" rx="8" fill="#15803d"/>
    <text x="82" y="19" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">3. CSA SOLUTIONS</text>

    <text x="10" y="50" font-size="9.5" font-weight="bold" fill="#4ade80">Soil Conservation:</text>
    <text x="10" y="68" font-size="8.5" fill="#cbd5e1">• Fanya Juu terraces</text>
    <text x="10" y="84" font-size="8.5" fill="#cbd5e1">• Contour mulching</text>

    <text x="10" y="110" font-size="9.5" font-weight="bold" fill="#4ade80">Agronomic Tech:</text>
    <text x="10" y="128" font-size="8.5" fill="#cbd5e1">• Agroforestry trees</text>
    <text x="10" y="144" font-size="8.5" fill="#cbd5e1">• Solar drip irrigation</text>

    <text x="10" y="170" font-size="9.5" font-weight="bold" fill="#4ade80">Digital Innovation:</text>
    <text x="10" y="188" font-size="8.5" fill="#cbd5e1">• Mobile agronomy apps</text>
    <text x="10" y="204" font-size="8.5" fill="#cbd5e1">• Hermetic PICS bags</text>
  </g>

  <!-- Arrow 3->4 -->
  <polygon points="590,205 602,205 602,200 610,205 602,210 602,205" fill="#ec4899"/>

  <!-- Step 4: Desired Outcomes -->
  <g transform="translate(615, 90)">
    <rect x="0" y="0" width="155" height="235" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <rect x="0" y="0" width="155" height="28" rx="8" fill="#be185d"/>
    <text x="77" y="19" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">4. OUTCOMES</text>

    <text x="10" y="50" font-size="9.5" font-weight="bold" fill="#f472b6">Food Security:</text>
    <text x="10" y="68" font-size="8.5" fill="#cbd5e1">• Availability</text>
    <text x="10" y="84" font-size="8.5" fill="#cbd5e1">• Economic Access</text>
    <text x="10" y="100" font-size="8.5" fill="#cbd5e1">• Healthy Utilization</text>
    <text x="10" y="116" font-size="8.5" fill="#cbd5e1">• Year-round Stability</text>

    <text x="10" y="145" font-size="9.5" font-weight="bold" fill="#f472b6">Economic Growth:</text>
    <text x="10" y="163" font-size="8.5" fill="#cbd5e1">• High farm incomes</text>
    <text x="10" y="179" font-size="8.5" fill="#cbd5e1">• Rural industrial jobs</text>
    <text x="10" y="195" font-size="8.5" fill="#cbd5e1">• Foreign exchange</text>
  </g>

  <!-- Final Unifying Ribbon -->
  <rect x="30" y="350" width="740" height="45" rx="6" fill="#334155"/>
  <text x="400" y="375" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">UNIFIED CONCLUSION: Climate-Smart Agriculture is the definitive pathway to African food sovereignty and prosperity.</text>
</svg>
""")

TOPIC_10_SVGS = {
    1: SVG_CLASSIFICATION_TREE,
    2: SVG_INTENSIVE_EXTENSIVE,
    3: SVG_FACTORS_MATRIX,
    4: SVG_SYSTEM_CYCLE,
    5: SVG_VALUE_CHAIN,
    6: SVG_ECONOMIC_LINKAGES,
    7: SVG_AFRICA_ECOZONES,
    8: SVG_DIGITAL_ECOSYSTEM,
    9: SVG_CLIMATE_HAZARDS,
    10: SVG_POST_HARVEST,
    11: SVG_CSA_MATRIX,
    12: SVG_FOOD_SECURITY,
    13: SVG_FIELDWORK_FLOW,
    14: SVG_POLICY_BRIEF,
    15: SVG_MASTER_SYNTHESIS
}

def enrich_topic_10():
    print("=" * 80)
    print("Starting Visual Enrichment: CBC Grade 10 Geography — Topic 10: Agriculture")
    print("=" * 80)

    # 1. Target Topic 10 under Subject Geography (ID: 37)
    subject = Subject.objects.filter(id=37).first() or Subject.objects.filter(grade__name__icontains="10", name="Geography").first()
    if not subject:
        raise ValueError("Subject 'Geography' (ID: 37) not found!")

    topic = Topic.objects.filter(subject=subject, order=10).first()
    if not topic:
        raise ValueError("Topic 10 'Agriculture' not found under Geography!")

    # 2. Load verified Wikimedia images
    json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grade10_geography_topic10_verified_images.json")
    with open(json_path, "r") as f:
        verified_images = json.load(f)

    lessons = topic.lessons.all().order_by("learning_unit__order")
    print(f"Enriching {lessons.count()} Lessons for Topic 10: {topic.name}...")

    for lesson in lessons:
        u_order = str(lesson.learning_unit.order)
        print(f"\n--- Lesson {u_order}: {lesson.title} ---")

        # 1. Attach First-Card Photographic Visual Hook
        img_data = verified_images.get(u_order)
        if img_data:
            hook_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=1,
                block_type="suggested_image"
            ).first()

            if hook_block:
                hook_block.content = {
                    "text": hook_block.content.get("text", "") if hook_block.content else "",
                    "url": img_data['url'],
                    "resolved_image_url": img_data['url'],
                    "caption": f"Visual Hook: {hook_block.title}",
                    "author": img_data.get('author', 'Wikimedia Commons'),
                    "licensing": img_data.get('licensing', 'CC BY-SA')
                }
                hook_block.save()

                asset, _ = LessonAsset.objects.get_or_create(
                    lesson=lesson,
                    title=f"Lesson {u_order} Visual Hook: {hook_block.title}",
                    defaults={
                        "asset_type": "image",
                        "source_type": "external",
                        "storage_type": "url",
                        "status": "attached",
                        "url": img_data['url'],
                        "metadata": {
                            "author": img_data.get('author', 'Wikimedia Commons'),
                            "licensing": img_data.get('licensing', 'CC BY-SA'),
                            "commons_url": img_data.get('commons_url', ''),
                            "unit_order": int(u_order),
                            "topic_order": 10
                        }
                    }
                )
                asset.url = img_data['url']
                asset.status = "attached"
                asset.save()
                asset.blocks.add(hook_block)
                print(f"  + Attached Wikimedia Photographic Hook: {img_data['url'][:65]}...")

        # 2. Attach Custom Responsive Vector SVG
        svg_xml = TOPIC_10_SVGS.get(int(u_order))
        if svg_xml:
            diagram_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="diagram"
            ).first()

            if diagram_block:
                diagram_block.content = {
                    "svg_content": svg_xml,
                    "title": diagram_block.title,
                    "caption": diagram_block.content.get("caption", diagram_block.title) if diagram_block.content else diagram_block.title
                }
                diagram_block.save()

                svg_asset, _ = LessonAsset.objects.get_or_create(
                    lesson=lesson,
                    title=f"Lesson {u_order} Diagram: {diagram_block.title}",
                    defaults={
                        "asset_type": "diagram",
                        "source_type": "ai_generated",
                        "storage_type": "embed",
                        "status": "attached",
                        "metadata": {
                            "svg_content": svg_xml,
                            "unit_order": int(u_order),
                            "topic_order": 10
                        }
                    }
                )
                svg_asset.metadata["svg_content"] = svg_xml
                svg_asset.status = "attached"
                svg_asset.save()
                svg_asset.blocks.add(diagram_block)
                print(f"  + Attached Custom Responsive Vector SVG to block '{diagram_block.title}'")

        # 3. Attach YouTube Video (Lesson 12)
        video_block = LessonBlock.objects.filter(
            lesson=lesson,
            block_type="video"
        ).first()

        if video_block:
            c = video_block.content or {}
            vid_url = c.get("url") or "https://www.youtube.com/watch?v=D-w_iUvBvQk"
            v_asset, _ = LessonAsset.objects.get_or_create(
                lesson=lesson,
                title=f"Lesson {u_order} Video: {video_block.title}",
                defaults={
                    "asset_type": "youtube",
                    "source_type": "external",
                    "storage_type": "url",
                    "status": "attached",
                    "url": vid_url,
                    "metadata": {
                        "youtube_url": vid_url,
                        "unit_order": int(u_order),
                        "topic_order": 10
                    }
                }
            )
            v_asset.url = vid_url
            v_asset.status = "attached"
            v_asset.save()
            v_asset.blocks.add(video_block)
            print(f"  + Attached Educational YouTube Video: {vid_url}")

    print("\n" + "=" * 80)
    print("Topic 10 Visual Enrichment Completed Successfully!")
    print("=" * 80)

if __name__ == "__main__":
    enrich_topic_10()
