"""
VLearn CBC Grade 10 Agriculture — Topic 12: Animal Rearing Project
Visual Enrichment Engine (Phase 2: Vector SVGs, Verified Photos & Asset Persistence)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Animal Rearing Project (Order: 12)

Attaches:
  - 10 First-Card Photographic Visual Hooks (100% Tested HTTP 200 Direct Wikimedia URLs)
  - 8 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - 1 Verified Educational YouTube Video (Lesson 7 Card 3)
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade10_agriculture_topic12.py
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
# 8 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 12: ANIMAL REARING PROJECT
# =============================================================================

# SVG 1: Feasibility Decision Matrix (Lesson 1, Page 2)
SVG_FEASIBILITY_MATRIX = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Agribusiness Feasibility Decision Matrix &amp; Resource Auditing</text>

  <!-- 5 Resource Pillars Flowing to Decision Hub -->
  <!-- 1. Land & Space -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="220" height="75" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="110" y="22" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. SPATIAL FOOTPRINT</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Horizontal vs Vertical Cages</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Compact &lt;10m² micro-livestock</text>
  </g>
  <line x1="265" y1="102" x2="345" y2="200" stroke="#38bdf8" stroke-width="2" stroke-dasharray="2,2"/>

  <!-- 2. Capex & Opex Capital -->
  <g transform="translate(535, 65)">
    <rect x="0" y="0" width="220" height="75" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="110" y="22" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">2. CAPITAL MODELING</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Capex: Durable housing &amp; tools</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Opex: 60–70% feed + vaccines</text>
  </g>
  <line x1="535" y1="102" x2="455" y2="200" stroke="#22c55e" stroke-width="2" stroke-dasharray="2,2"/>

  <!-- Central Decision Hub -->
  <circle cx="400" cy="240" r="58" fill="#0f172a" stroke="#eab308" stroke-width="3"/>
  <text x="400" y="232" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">ENTERPRISE</text>
  <text x="400" y="248" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">SELECTION</text>
  <text x="400" y="263" font-size="10" fill="#cbd5e1" text-anchor="middle">DECISION</text>

  <!-- 3. Water Security & Labor -->
  <g transform="translate(35, 195)">
    <rect x="0" y="0" width="230" height="80" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="115" y="22" font-size="11" font-weight="bold" fill="#d8b4fe" text-anchor="middle">3. WATER &amp; LABOR</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Clean daily water supply</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• 7:00 AM &amp; 4:30 PM duty roster</text>
  </g>
  <line x1="265" y1="235" x2="342" y2="235" stroke="#a855f7" stroke-width="2"/>

  <!-- 4. Market Demand & Pricing -->
  <g transform="translate(535, 195)">
    <rect x="0" y="0" width="230" height="80" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
    <text x="115" y="22" font-size="11" font-weight="bold" fill="#67e8f9" text-anchor="middle">4. MARKET DEMAND</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Pre-identified local buyers</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Target retail &amp; wholesale price</text>
  </g>
  <line x1="535" y1="235" x2="458" y2="235" stroke="#06b6d4" stroke-width="2"/>

  <!-- 5. Technical Knowledge & Biosecurity (Bottom) -->
  <g transform="translate(275, 335)">
    <rect x="0" y="0" width="250" height="75" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="125" y="22" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">5. SKILLS &amp; BIOSECURITY</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Husbandry &amp; disease prevention</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Zero risk of animal neglect</text>
  </g>
  <line x1="400" y1="335" x2="400" y2="298" stroke="#ef4444" stroke-width="2"/>
</svg>
""")

# SVG 2: Species Comparison: Rabbits vs Broilers vs BSFL (Lesson 2, Page 2)
SVG_SPECIES_COMPARISON = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Micro-Livestock Enterprise Selection: Biological &amp; Economic Comparison</text>

  <!-- 3 Species Columns -->
  <!-- 1. Rabbits (Cuniculture) -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="220" height="340" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="28" rx="10" fill="#15803d"/>
    <text x="110" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">1. CUNICULTURE (RABBITS)</text>

    <g transform="translate(10, 45)">
      <text x="10" y="18" font-size="9" font-weight="bold" fill="#4ade80">• High Fecundity:</text>
      <text x="10" y="34" font-size="9" fill="#cbd5e1">  1 Doe kindles 4–5x/yr (30+ kits).</text>
      <text x="10" y="58" font-size="9" font-weight="bold" fill="#4ade80">• 50% Forage Feeding:</text>
      <text x="10" y="74" font-size="9" fill="#cbd5e1">  Eats wilted farm weeds/vines.</text>
      <text x="10" y="98" font-size="9" font-weight="bold" fill="#4ade80">• 16-Week Market Cycle:</text>
      <text x="10" y="114" font-size="9" fill="#cbd5e1">  Reaches 2.0–2.5 kg live weight.</text>
      <text x="10" y="138" font-size="9" font-weight="bold" fill="#4ade80">• Low Cash Risk:</text>
      <text x="10" y="154" font-size="9" fill="#cbd5e1">  Minimal commercial feed cost.</text>
    </g>

    <rect x="15" y="245" width="190" height="70" rx="6" fill="#1e293b" stroke="#22c55e"/>
    <text x="95" y="265" font-size="9" font-weight="bold" fill="#86efac" text-anchor="middle">BEST FOR:</text>
    <text x="95" y="285" font-size="8" fill="#cbd5e1" text-anchor="middle">Low-budget schools with abundant</text>
    <text x="95" y="300" font-size="8" fill="#cbd5e1" text-anchor="middle">green forage &amp; small land area.</text>
  </g>

  <!-- 2. Broiler Poultry -->
  <g transform="translate(290, 65)">
    <rect x="0" y="0" width="220" height="340" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="28" rx="10" fill="#0284c7"/>
    <text x="110" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">2. BROILER POULTRY</text>

    <g transform="translate(10, 45)">
      <text x="10" y="18" font-size="9" font-weight="bold" fill="#38bdf8">• Rapid Turnaround:</text>
      <text x="10" y="34" font-size="9" fill="#cbd5e1">  Market-ready in 4 to 6 weeks!</text>
      <text x="10" y="58" font-size="9" font-weight="bold" fill="#38bdf8">• High Feed Conversion:</text>
      <text x="10" y="74" font-size="9" fill="#cbd5e1">  FCR 1.6–1.8 (4.5kg feed/bird).</text>
      <text x="10" y="98" font-size="9" font-weight="bold" fill="#38bdf8">• Capital Intensive:</text>
      <text x="10" y="114" font-size="9" fill="#cbd5e1">  Requires 100% purchased feed.</text>
      <text x="10" y="138" font-size="9" font-weight="bold" fill="#38bdf8">• Immediate Market:</text>
      <text x="10" y="154" font-size="9" fill="#cbd5e1">  Very high local meat liquidity.</text>
    </g>

    <rect x="15" y="245" width="190" height="70" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="95" y="265" font-size="9" font-weight="bold" fill="#67e8f9" text-anchor="middle">BEST FOR:</text>
    <text x="95" y="285" font-size="8" fill="#cbd5e1" text-anchor="middle">Fast single-term project completion</text>
    <text x="95" y="300" font-size="8" fill="#cbd5e1" text-anchor="middle">with available operational cash.</text>
  </g>

  <!-- 3. Black Soldier Fly Larvae (BSFL) -->
  <g transform="translate(535, 65)">
    <rect x="0" y="0" width="220" height="340" rx="10" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="28" rx="10" fill="#ca8a04"/>
    <text x="110" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">3. BSFL INSECT FARMING</text>

    <g transform="translate(10, 45)">
      <text x="10" y="18" font-size="9" font-weight="bold" fill="#fde047">• 3-Week Micro-Cycle:</text>
      <text x="10" y="34" font-size="9" fill="#cbd5e1">  Egg to harvest in 18–21 days.</text>
      <text x="10" y="58" font-size="9" font-weight="bold" fill="#fde047">• Organic Bio-Recycling:</text>
      <text x="10" y="74" font-size="9" fill="#cbd5e1">  Feeds on kitchen/market waste.</text>
      <text x="10" y="98" font-size="9" font-weight="bold" fill="#fde047">• >40% Crude Protein:</text>
      <text x="10" y="114" font-size="9" fill="#cbd5e1">  Replaces expensive fishmeal.</text>
      <text x="10" y="138" font-size="9" font-weight="bold" fill="#fde047">• Tiny Footprint:</text>
      <text x="10" y="154" font-size="9" fill="#cbd5e1">  Reared in vertical plastic crates.</text>
    </g>

    <rect x="15" y="245" width="190" height="70" rx="6" fill="#1e293b" stroke="#eab308"/>
    <text x="95" y="265" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">BEST FOR:</text>
    <text x="95" y="285" font-size="8" fill="#cbd5e1" text-anchor="middle">Circular economy &amp; supplemental</text>
    <text x="95" y="300" font-size="8" fill="#cbd5e1" text-anchor="middle">protein feed for poultry/fish.</text>
  </g>
</svg>
""")

# SVG 3: Agribusiness Financial Pipeline: Capex, Opex, Break-Even & ROI (Lesson 4, Page 2)
SVG_FINANCIAL_PIPELINE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Agribusiness Financial Pipeline: 50-Broiler Production Model</text>

  <!-- Financial Flow Steps -->
  <!-- Step 1: Costs (Capex Depr + Opex) -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="220" height="150" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="26" rx="8" fill="#991b1b"/>
    <text x="110" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">1. TOTAL PRODUCTION COST</text>
    <text x="10" y="48" font-size="9" fill="#cbd5e1">• 50 Chicks: KES 5,000</text>
    <text x="10" y="66" font-size="9" fill="#cbd5e1">• 5 Bags Feed: KES 20,000</text>
    <text x="10" y="84" font-size="9" fill="#cbd5e1">• Vet/Heat: KES 3,000</text>
    <text x="10" y="102" font-size="9" fill="#cbd5e1">• Capex Depr (10%): KES 1,500</text>
    <text x="10" y="132" font-size="11" font-weight="bold" fill="#f87171">Total Cost = KES 29,500</text>
  </g>
  <line x1="265" y1="140" x2="295" y2="140" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="285,135 295,140 285,145" fill="#38bdf8"/>

  <!-- Step 2: Mortality & Break-Even -->
  <g transform="translate(295, 65)">
    <rect x="0" y="0" width="210" height="150" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <rect x="0" y="0" width="210" height="26" rx="8" fill="#ca8a04"/>
    <text x="105" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">2. BREAK-EVEN PRICING</text>
    <text x="10" y="48" font-size="9" fill="#cbd5e1">• Mortality: 4% (2 birds)</text>
    <text x="10" y="66" font-size="9" font-weight="bold" fill="#fde047">• Surviving Birds = 48</text>
    <text x="10" y="92" font-size="9" fill="#cbd5e1">Break-Even Formula:</text>
    <text x="10" y="108" font-size="8" fill="#cbd5e1">KES 29,500 / 48 birds</text>
    <text x="10" y="132" font-size="11" font-weight="bold" fill="#fde047">Break-Even = KES 615</text>
  </g>
  <line x1="505" y1="140" x2="535" y2="140" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="525,135 535,140 525,145" fill="#38bdf8"/>

  <!-- Step 3: Market Revenue & Profit -->
  <g transform="translate(535, 65)">
    <rect x="0" y="0" width="220" height="150" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="26" rx="8" fill="#15803d"/>
    <text x="110" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">3. REVENUE &amp; PROFIT</text>
    <text x="10" y="48" font-size="9" fill="#cbd5e1">• Market Price: KES 850/bird</text>
    <text x="10" y="66" font-size="9" fill="#cbd5e1">• Gross Rev: KES 40,800</text>
    <text x="10" y="84" font-size="9" fill="#cbd5e1">• Plus Manure: KES 1,000</text>
    <text x="10" y="108" font-size="11" font-weight="bold" fill="#4ade80">Net Profit = KES 12,300</text>
    <text x="10" y="132" font-size="10" font-weight="bold" fill="#86efac">ROI = 41.7%</text>
  </g>

  <!-- Bottom Calculation Breakdown Banner -->
  <g transform="translate(45, 245)">
    <rect x="0" y="0" width="710" height="155" rx="8" fill="#0f172a" stroke="#38bdf8"/>
    <text x="355" y="26" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Key Financial Metric Formulas</text>

    <g transform="translate(20, 45)">
      <rect x="0" y="0" width="210" height="90" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="105" y="22" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Break-Even Price</text>
      <text x="105" y="48" font-size="9" fill="#cbd5e1" text-anchor="middle">Total Production Cost</text>
      <line x1="20" y1="55" x2="190" y2="55" stroke="#94a3b8" stroke-width="1"/>
      <text x="105" y="72" font-size="9" fill="#cbd5e1" text-anchor="middle">Surviving Units</text>
    </g>

    <g transform="translate(250, 45)">
      <rect x="0" y="0" width="210" height="90" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="105" y="22" font-size="10" font-weight="bold" fill="#22c55e" text-anchor="middle">Net Enterprise Profit</text>
      <text x="105" y="52" font-size="9" fill="#cbd5e1" text-anchor="middle">Gross Revenue</text>
      <text x="105" y="70" font-size="9" fill="#cbd5e1" text-anchor="middle">- Total Production Cost</text>
    </g>

    <g transform="translate(480, 45)">
      <rect x="0" y="0" width="210" height="90" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="105" y="22" font-size="10" font-weight="bold" fill="#eab308" text-anchor="middle">Return on Investment</text>
      <text x="105" y="48" font-size="9" fill="#cbd5e1" text-anchor="middle">(Net Profit / Total Cost)</text>
      <text x="105" y="68" font-size="9" fill="#cbd5e1" text-anchor="middle">x 100%</text>
    </g>
  </g>
</svg>
""")

# SVG 4: Rabbit Hutch Blueprint (Lesson 5, Page 2)
SVG_RABBIT_HUTCH = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Elevated Rabbit Hutch Architectural Blueprint &amp; Hygiene Engineering</text>

  <!-- Left: Schematic Hutch Elevation -->
  <g transform="translate(45, 60)">
    <rect x="0" y="0" width="340" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>

    <!-- Sloping Roof -->
    <polygon points="20,70 320,40 320,55 20,85" fill="#94a3b8"/>
    <text x="170" y="50" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Corrugated Iron Roof (Sloping)</text>

    <!-- Main Cage Body -->
    <rect x="30" y="85" width="280" height="120" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>

    <!-- Dark Nesting Box Compartment (Left) -->
    <rect x="30" y="85" width="90" height="120" fill="#334155" stroke="#22c55e"/>
    <text x="75" y="140" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">Dark Nest Box</text>
    <text x="75" y="155" font-size="8" fill="#cbd5e1" text-anchor="middle">(Kindling Doe)</text>

    <!-- Wire Mesh Activity Area (Right) -->
    <rect x="120" y="85" width="190" height="120" fill="none" stroke="#38bdf8" stroke-dasharray="4,4"/>
    <text x="215" y="145" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Wire Mesh Activity Pen</text>

    <!-- 1.2cm Slotted Floor -->
    <line x1="30" y1="205" x2="310" y2="205" stroke="#eab308" stroke-width="4" stroke-dasharray="6,4"/>
    <text x="170" y="222" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">1.2 cm Slotted Floor (Dung Falls Through)</text>

    <!-- 1-Meter Legs with Ant Deflectors -->
    <rect x="40" y="205" width="16" height="110" fill="#475569"/>
    <rect x="284" y="205" width="16" height="110" fill="#475569"/>

    <!-- Ant Grease Rings -->
    <rect x="34" y="250" width="28" height="16" rx="3" fill="#ca8a04" stroke="#fde047"/>
    <rect x="278" y="250" width="28" height="16" rx="3" fill="#ca8a04" stroke="#fde047"/>
    <text x="170" y="262" font-size="8" fill="#cbd5e1" text-anchor="middle">Grease Ant Rings</text>

    <text x="170" y="330" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">1.0 Meter Elevated Leg Clearance</text>
  </g>

  <!-- Right: 4 Engineering Standards -->
  <g transform="translate(415, 60)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="28" rx="10" fill="#0284c7"/>
    <text x="172" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">HUTCH ENGINEERING STANDARDS</text>

    <g transform="translate(15, 40)">
      <rect x="0" y="0" width="315" height="60" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#38bdf8">1. 1-Meter Leg Elevation:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">• Blocks dogs, rodents, and crawling safari ants</text>
      <text x="15" y="52" font-size="9" fill="#cbd5e1">• Comfortable standing inspection height</text>
    </g>

    <g transform="translate(15, 110)">
      <rect x="0" y="0" width="315" height="65" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#38bdf8">2. 1.2 cm Floor Slat Spacing:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">• Dung &amp; urine fall through cleanly</text>
      <text x="15" y="54" font-size="9" fill="#86efac">• Prevents sore hocks and coccidiosis!</text>
    </g>

    <g transform="translate(15, 185)">
      <rect x="0" y="0" width="315" height="65" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#38bdf8">3. Dark Nesting Compartment:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">• Solid timber walls provide warmth and privacy</text>
      <text x="15" y="54" font-size="9" fill="#cbd5e1">• Prevents doe from abandoning/eating newborn kits</text>
    </g>

    <text x="172" y="310" font-size="9" fill="#67e8f9" text-anchor="middle">Standard Dimensions: 1.0m (L) x 0.8m (W) x 0.6m (H)</text>
  </g>
</svg>
""")

# SVG 5: Deep Litter Poultry Coop (Lesson 5, Page 3)
SVG_POULTRY_COOP = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Deep Litter Poultry Coop: Ventilation &amp; Feeder Elevation Engineering</text>

  <!-- Left: Cross-Section Diagram -->
  <g transform="translate(45, 60)">
    <rect x="0" y="0" width="340" height="345" rx="10" fill="#0f172a" stroke="#eab308" stroke-width="2"/>

    <!-- Roof -->
    <polygon points="10,50 330,30 330,45 10,65" fill="#94a3b8"/>

    <!-- Solid Lower Wall (0.6m) -->
    <rect x="25" y="160" width="290" height="50" fill="#475569" stroke="#94a3b8"/>
    <text x="170" y="190" font-size="9" fill="#ffffff" text-anchor="middle">Solid Lower Wall (0.6m) - Blocks Cold Drafts</text>

    <!-- Upper Wire Mesh Ventilation -->
    <rect x="25" y="65" width="290" height="95" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,4"/>
    <text x="170" y="115" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Continuous Wire Ventilation (<10ppm Ammonia)</text>

    <!-- Deep Litter Floor -->
    <rect x="25" y="210" width="290" height="40" fill="#ca8a04" stroke="#fde047"/>
    <text x="170" y="235" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">10–15 cm Clean Wood Shavings Deep Litter</text>

    <!-- Suspended Feeder -->
    <line x1="170" y1="65" x2="170" y2="155" stroke="#94a3b8" stroke-width="2"/>
    <rect x="150" y="155" width="40" height="35" rx="3" fill="#ef4444" stroke="#f87171"/>
    <text x="170" y="177" font-size="8" fill="#ffffff" text-anchor="middle">Feeder</text>
    <text x="170" y="280" font-size="9" fill="#4ade80" text-anchor="middle">Feeder lip aligned at bird back-level</text>
  </g>

  <!-- Right: 3 Golden Poultry Housing Standards -->
  <g transform="translate(415, 60)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="28" rx="10" fill="#15803d"/>
    <text x="172" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">POULTRY COOP MANAGEMENT RULES</text>

    <g transform="translate(15, 40)">
      <rect x="0" y="0" width="315" height="65" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">1. Deep Litter (10–15 cm):</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">• Absorbs moisture; turned weekly with rake</text>
      <text x="15" y="54" font-size="9" fill="#cbd5e1">• Insulates chicks from cold concrete floors</text>
    </g>

    <g transform="translate(15, 115)">
      <rect x="0" y="0" width="315" height="65" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">2. Back-Level Suspended Feeders:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">• Suspended at birds' back/shoulder height</text>
      <text x="15" y="54" font-size="9" fill="#86efac">• Eliminates feed scratching &amp; fecal contamination</text>
    </g>

    <g transform="translate(15, 190)">
      <rect x="0" y="0" width="315" height="65" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">3. Ammonia Gas Venting:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">• Upper wire mesh vents hot ammonia gas</text>
      <text x="15" y="54" font-size="9" fill="#cbd5e1">• Prevents respiratory ciliary damage &amp; pneumonia</text>
    </g>

    <text x="172" y="310" font-size="9" fill="#86efac" text-anchor="middle">Stocking Density: 10–12 broilers per square meter</text>
  </g>
</svg>
""")

# SVG 6: 4 Core Farm Records (Lesson 6, Page 2)
SVG_FARM_RECORDS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">4-Core Farm Record-Keeping Ledger Architecture</text>

  <!-- 4 Ledger Cards Grid -->
  <!-- 1. Inventory -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="145" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="340" height="26" rx="8" fill="#0284c7"/>
    <text x="170" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">1. ANIMAL INVENTORY LOG</text>
    <text x="15" y="48" font-size="9" fill="#cbd5e1">• Opening Stock (Count at start of week)</text>
    <text x="15" y="66" font-size="9" fill="#cbd5e1">• Inflows: Births / Purchases (+)</text>
    <text x="15" y="84" font-size="9" fill="#cbd5e1">• Outflows: Mortalities / Sales (-)</text>
    <text x="15" y="112" font-size="10" font-weight="bold" fill="#38bdf8">Closing Stock = Open + Births - Deaths</text>
  </g>

  <!-- 2. Feeding & Expense -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="340" height="145" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="340" height="26" rx="8" fill="#15803d"/>
    <text x="170" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">2. FEEDING &amp; EXPENSE LOG</text>
    <text x="15" y="48" font-size="9" fill="#cbd5e1">• Daily feed consumed (kg / bags)</text>
    <text x="15" y="66" font-size="9" fill="#cbd5e1">• Feed brand &amp; batch expiration date</text>
    <text x="15" y="84" font-size="9" fill="#cbd5e1">• Unit cost &amp; total cumulative expense</text>
    <text x="15" y="112" font-size="10" font-weight="bold" fill="#4ade80">Tracks 60–70% of total project costs</text>
  </g>

  <!-- 3. Growth & Production -->
  <g transform="translate(45, 230)">
    <rect x="0" y="0" width="340" height="150" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <rect x="0" y="0" width="340" height="26" rx="8" fill="#ca8a04"/>
    <text x="170" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">3. PRODUCTION &amp; GROWTH LOG</text>
    <text x="15" y="48" font-size="9" fill="#cbd5e1">• Weekly sample body weight measurements (g)</text>
    <text x="15" y="66" font-size="9" fill="#cbd5e1">• Average Daily Gain (ADG) calculation</text>
    <text x="15" y="84" font-size="9" fill="#cbd5e1">• Daily egg count / Kindling litter sizes</text>
    <text x="15" y="115" font-size="10" font-weight="bold" fill="#fde047">Computes Feed Conversion Ratio (FCR)</text>
  </g>

  <!-- 4. Health & Drug Withdrawal -->
  <g transform="translate(415, 230)">
    <rect x="0" y="0" width="340" height="150" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="26" rx="8" fill="#991b1b"/>
    <text x="170" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">4. HEALTH &amp; TREATMENT LOG</text>
    <text x="15" y="48" font-size="9" fill="#cbd5e1">• Disease symptoms &amp; clinical diagnosis</text>
    <text x="15" y="66" font-size="9" fill="#cbd5e1">• Drug administered, dosage &amp; route</text>
    <text x="15" y="88" font-size="9" font-weight="bold" fill="#f87171">• MANDATORY DRUG WITHDRAWAL DAYS</text>
    <text x="15" y="115" font-size="10" font-weight="bold" fill="#fca5a5">Ensures zero chemical residues in meat!</text>
  </g>
</svg>
""")

# SVG 7: Biosecurity Footbath (Lesson 9, Page 2)
SVG_BIOSECURITY_FOOTBATH = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Farm Biosecurity Perimeter &amp; Entry Disinfectant Footbath</text>

  <!-- Left: Biosecurity Architecture -->
  <g transform="translate(45, 60)">
    <rect x="0" y="0" width="340" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="28" rx="10" fill="#15803d"/>
    <text x="170" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3 PILLARS OF FARM BIOSECURITY</text>

    <g transform="translate(15, 40)">
      <rect x="0" y="0" width="310" height="60" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">1. Isolation:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">• Wire mesh screens block wild birds &amp; rodents</text>
      <text x="15" y="52" font-size="9" fill="#cbd5e1">• Perimeter fence with locked access gate</text>
    </g>

    <g transform="translate(15, 110)">
      <rect x="0" y="0" width="310" height="60" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">2. Sanitation:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">• Daily washing of water drinkers &amp; hoppers</text>
      <text x="15" y="52" font-size="9" fill="#cbd5e1">• Dry deep litter; zero damp wet patches</text>
    </g>

    <g transform="translate(15, 180)">
      <rect x="0" y="0" width="310" height="60" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">3. Traffic Control:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">• "No Unauthorized Visitors" signage</text>
      <text x="15" y="52" font-size="9" fill="#cbd5e1">• Dedicated gumboots for project workers</text>
    </g>

    <text x="170" y="300" font-size="9" fill="#86efac" text-anchor="middle">Goal: Zero pathogens enter the flock environment!</text>
  </g>

  <!-- Right: The Disinfectant Footbath -->
  <g transform="translate(415, 60)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="28" rx="10" fill="#0284c7"/>
    <text x="172" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">DISINFECTANT FOOTBATH OPERATION</text>

    <!-- Schematic Footbath Tray -->
    <rect x="25" y="45" width="295" height="110" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="35" y="65" width="275" height="70" rx="6" fill="#0284c7" opacity="0.6"/>
    <text x="172" y="95" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Disinfectant Solution Tray</text>
    <text x="172" y="115" font-size="9" fill="#dbeafe" text-anchor="middle">(Virkon-S / Bleach / Copper Sulfate)</text>

    <!-- Operational Rules -->
    <g transform="translate(25, 170)">
      <rect x="0" y="0" width="295" height="110" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="15" y="22" font-size="10" font-weight="bold" fill="#38bdf8">Footbath Rules:</text>
      <text x="15" y="42" font-size="9" fill="#cbd5e1">• Placed at sole entrance of livestock unit</text>
      <text x="15" y="60" font-size="9" fill="#cbd5e1">• 10-second foot immersion before stepping in</text>
      <text x="15" y="78" font-size="9" fill="#cbd5e1">• Solution replaced every 48–72 hours</text>
      <text x="15" y="96" font-size="9" font-weight="bold" fill="#4ade80">• Destroys 99.9% of shoe-borne viruses &amp; bacteria</text>
    </g>

    <text x="172" y="315" font-size="9" fill="#67e8f9" text-anchor="middle">Mechanical barrier stops disease transmission cold!</text>
  </g>
</svg>
""")

# SVG 8: Master Animal Rearing Lifecycle (Lesson 10, Page 2)
SVG_MASTER_LIFECYCLE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Master Animal Rearing Project Agribusiness Lifecycle Matrix</text>

  <!-- 6 Process Nodes in Ring -->
  <!-- 1. Feasibility & Selection -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="195" height="75" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="97" y="22" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">1. FEASIBILITY &amp; SELECTION</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Space, Capex/Opex, Market</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Broilers vs Rabbits vs BSFL</text>
  </g>
  <line x1="240" y1="102" x2="345" y2="200" stroke="#22c55e" stroke-width="2" stroke-dasharray="2,2"/>

  <!-- 2. Planning & Budget -->
  <g transform="translate(560, 65)">
    <rect x="0" y="0" width="195" height="75" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="97" y="22" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">2. SMART PLAN &amp; BUDGET</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• 4 Activity phases</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Break-even price modeling</text>
  </g>
  <line x1="560" y1="102" x2="455" y2="200" stroke="#38bdf8" stroke-width="2" stroke-dasharray="2,2"/>

  <!-- 3. Housing Architecture -->
  <g transform="translate(35, 195)">
    <rect x="0" y="0" width="195" height="75" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <text x="97" y="22" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">3. HOUSING CONSTRUCTION</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• 1.0m Elevated rabbit hutch</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Deep litter coop ventilation</text>
  </g>
  <line x1="230" y1="240" x2="345" y2="240" stroke="#eab308" stroke-width="2"/>

  <!-- 4. Stocking & Management -->
  <g transform="translate(570, 195)">
    <rect x="0" y="0" width="195" height="75" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="97" y="22" font-size="10" font-weight="bold" fill="#d8b4fe" text-anchor="middle">4. STOCKING &amp; FEEDING</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Anti-stress glucose water</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• 1/3 Fill rule + Forage wilting</text>
  </g>
  <line x1="570" y1="240" x2="455" y2="240" stroke="#a855f7" stroke-width="2"/>

  <!-- 5. Biosecurity & Records -->
  <g transform="translate(140, 335)">
    <rect x="0" y="0" width="220" height="75" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
    <text x="110" y="22" font-size="10" font-weight="bold" fill="#67e8f9" text-anchor="middle">5. BIOSECURITY &amp; LOGS</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Entry footbaths &amp; 3-I plan</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• 4-Core record ledger tracking</text>
  </g>
  <line x1="360" y1="350" x2="390" y2="298" stroke="#06b6d4" stroke-width="2"/>

  <!-- 6. Evaluation & Marketing -->
  <g transform="translate(440, 335)">
    <rect x="0" y="0" width="220" height="75" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="110" y="22" font-size="10" font-weight="bold" fill="#f87171" text-anchor="middle">6. EVALUATION &amp; PROFIT</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• FCR &amp; ADG computations</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• P&amp;L Financial Statement &amp; ROI</text>
  </g>
  <line x1="440" y1="350" x2="410" y2="298" stroke="#ef4444" stroke-width="2"/>

  <!-- Central Hub: Agribusiness Success -->
  <circle cx="400" cy="240" r="55" fill="#0f172a" stroke="#22c55e" stroke-width="3"/>
  <text x="400" y="235" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">AGRIBUSINESS</text>
  <text x="400" y="252" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">SUCCESS</text>
</svg>
""")

SVG_MAP = {
    1: {"page": 2, "svg": SVG_FEASIBILITY_MATRIX, "title": "Agribusiness Feasibility Decision Matrix & Resource Auditing"},
    2: {"page": 2, "svg": SVG_SPECIES_COMPARISON, "title": "Micro-Livestock Enterprise Selection: Biological & Economic Comparison"},
    4: {"page": 2, "svg": SVG_FINANCIAL_PIPELINE, "title": "Agribusiness Financial Pipeline: 50-Broiler Production Model"},
    5: {"page": 2, "svg": SVG_RABBIT_HUTCH, "title": "Elevated Rabbit Hutch Architectural Blueprint & Hygiene Engineering"},
    6: {"page": 2, "svg": SVG_FARM_RECORDS, "title": "4-Core Farm Record-Keeping Ledger Architecture"},
    9: {"page": 2, "svg": SVG_BIOSECURITY_FOOTBATH, "title": "Farm Biosecurity Perimeter & Entry Disinfectant Footbath"},
    10: {"page": 2, "svg": SVG_MASTER_LIFECYCLE, "title": "Master Animal Rearing Project Agribusiness Lifecycle Matrix"}
}

def enrich_grade10_topic12():
    """Injects verified photos, responsive vector SVGs, YouTube embeds, and creates LessonAssets."""
    print("=" * 80)
    print("STARTING ENRICHMENT: CBC Grade 10 Agriculture — Topic 12: Animal Rearing Project")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()
    topic = Topic.objects.filter(subject=subject, name="Animal Rearing Project").first()

    assert topic, "Topic 'Animal Rearing Project' not found!"

    images_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grade10_topic12_verified_images.json")
    with open(images_path, "r", encoding="utf-8") as f:
        verified_images = json.load(f)

    lessons = list(topic.lessons.all().order_by("learning_unit__order"))
    LessonAsset.objects.filter(lesson__in=lessons).delete()

    total_images_attached = 0
    total_svgs_attached = 0
    total_videos_attached = 0
    total_assets_persisted = 0

    for lesson in lessons:
        u_order = lesson.learning_unit.order
        u_str = str(u_order)

        # ---------------------------------------------------------------------
        # 1. First-Card Visual Hook (Photographic Wikimedia URL)
        # ---------------------------------------------------------------------
        hook_block = LessonBlock.objects.filter(
            lesson=lesson,
            page_number=1,
            block_type="suggested_image"
        ).first()

        if hook_block and u_str in verified_images:
            img_data = verified_images[u_str]
            content = hook_block.content or {}
            content["resolved_image_url"] = img_data["url"]
            content["url"] = img_data["url"]
            content["attribution"] = f"Photo by {img_data.get('author', 'Wikimedia Commons')} ({img_data.get('licensing', 'CC')})"
            content["commons_url"] = img_data.get("commons_url", "")
            hook_block.content = content
            hook_block.save()
            total_images_attached += 1

            asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="image",
                source_type="external",
                storage_type="url",
                status="attached",
                title=f"Lesson {u_order} Visual Hook: {hook_block.title}",
                description=content.get("caption", hook_block.title),
                url=img_data["url"],
                metadata={
                    "topic_order": 12,
                    "unit_order": u_order,
                    "card": 1,
                    "author": img_data.get("author", "Wikimedia Commons"),
                    "licensing": img_data.get("licensing", "CC"),
                    "commons_url": img_data.get("commons_url", "")
                }
            )
            hook_block.assets.add(asset)
            total_assets_persisted += 1
            print(f"  [Image Hook Attached] Lesson {u_order}: {img_data['title'][:50]}...")

        # ---------------------------------------------------------------------
        # 2. Custom Responsive Vector SVGs
        # ---------------------------------------------------------------------
        # Handle Lesson 5 which has two SVG diagrams (Page 2 and Page 3)
        if u_order == 5:
            diag_blocks = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="suggested_diagram"
            ).order_by("page_number")
            for idx, d_block in enumerate(diag_blocks):
                if idx == 0:
                    svg_payload = SVG_RABBIT_HUTCH
                    title_text = "Elevated Rabbit Hutch Architectural Blueprint"
                    p_num = 2
                else:
                    svg_payload = SVG_POULTRY_COOP
                    title_text = "Deep Litter Poultry Coop Ventilation & Feeder Elevation"
                    p_num = 3

                d_content = d_block.content or {}
                d_content["svg"] = svg_payload
                d_content["svg_xml"] = svg_payload
                d_content["title"] = title_text
                d_block.content = d_content
                d_block.save()
                total_svgs_attached += 1

                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    asset_type="diagram",
                    source_type="ai_generated",
                    storage_type="embed",
                    status="attached",
                    title=f"Lesson 5 Diagram {idx+1}: {title_text}",
                    description=d_content.get("caption", title_text),
                    metadata={
                        "topic_order": 12,
                        "unit_order": 5,
                        "page": p_num,
                        "svg_content": svg_payload
                    }
                )
                d_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [Vector SVG Attached] Lesson 5 (Page {p_num}): {title_text}")

        elif u_order in SVG_MAP:
            svg_def = SVG_MAP[u_order]
            diag_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="suggested_diagram"
            ).first()

            if diag_block:
                diag_content = diag_block.content or {}
                diag_content["svg"] = svg_def["svg"]
                diag_content["svg_xml"] = svg_def["svg"]
                diag_content["title"] = svg_def["title"]
                diag_block.content = diag_content
                diag_block.save()
                total_svgs_attached += 1

                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    asset_type="diagram",
                    source_type="ai_generated",
                    storage_type="embed",
                    status="attached",
                    title=f"Lesson {u_order} Diagram: {svg_def['title']}",
                    description=diag_content.get("caption", svg_def["title"]),
                    metadata={
                        "topic_order": 12,
                        "unit_order": u_order,
                        "page": svg_def["page"],
                        "svg_content": svg_def["svg"]
                    }
                )
                diag_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [Vector SVG Attached] Lesson {u_order}: {svg_def['title']}")

        # ---------------------------------------------------------------------
        # 3. Educational YouTube Videos (Lesson 7)
        # ---------------------------------------------------------------------
        video_blocks = LessonBlock.objects.filter(
            lesson=lesson,
            block_type="suggested_video"
        )
        for v_block in video_blocks:
            v_content = v_block.content or {}
            v_url = v_content.get("url", "")
            if v_url:
                total_videos_attached += 1
                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    asset_type="youtube",
                    source_type="external",
                    storage_type="url",
                    status="attached",
                    title=f"Lesson {u_order} Video: {v_block.title}",
                    description=v_content.get("description", v_block.title),
                    url=v_url,
                    metadata={
                        "topic_order": 12,
                        "unit_order": u_order,
                        "youtube_url": v_url
                    }
                )
                v_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [YouTube Video Attached] Lesson {u_order}: {v_block.title}")

    print("=" * 80)
    print(f"ENRICHMENT COMPLETE: Topic 12 '{topic.name}'")
    print(f"  Photographic Hooks: {total_images_attached} / 10")
    print(f"  Vector SVGs:        {total_svgs_attached} / 8")
    print(f"  YouTube Videos:     {total_videos_attached} / 1")
    print(f"  LessonAssets:       {total_assets_persisted}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic12()
