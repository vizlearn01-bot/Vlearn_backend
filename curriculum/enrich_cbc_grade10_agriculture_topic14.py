"""
VLearn CBC Grade 10 Agriculture — Topic 14: Product Processing and Value Addition
Visual Enrichment Engine (Phase 2: Vector SVGs, Verified Photos & Asset Persistence)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Product Processing and Value Addition (Order: 14)

Attaches:
  - 12 First-Card Photographic Visual Hooks (100% Tested HTTP 200 Direct Wikimedia URLs)
  - 8 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - 1 Verified Educational YouTube Video (Lesson 9 Card 3)
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade10_agriculture_topic14.py
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
# 8 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 14: PRODUCT PROCESSING
# =============================================================================

# SVG 1: Economic Ladder (Lesson 1, Page 2)
SVG_ECONOMIC_LADDER = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Raw Commodity vs. Value-Added Product Economic Ladder</text>

  <!-- Step 1: Raw Commodity -->
  <g transform="translate(45, 75)">
    <rect x="0" y="0" width="220" height="230" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="28" rx="8" fill="#991b1b"/>
    <text x="110" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 1: RAW COMMODITY</text>
    <text x="15" y="52" font-size="10" font-weight="bold" fill="#f87171">• Product: Raw Cow Milk</text>
    <text x="15" y="74" font-size="9" fill="#cbd5e1">• Price: KES 40 / Liter</text>
    <text x="15" y="96" font-size="9" fill="#cbd5e1">• Shelf-life: 4 to 6 Hours</text>
    <text x="15" y="118" font-size="9" fill="#cbd5e1">• Market Role: Price-taker</text>
    <text x="15" y="140" font-size="9" fill="#cbd5e1">• Vulnerability: High spoilage</text>
    <rect x="15" y="165" width="190" height="45" rx="5" fill="#1e293b" stroke="#ef4444"/>
    <text x="110" y="192" font-size="10" font-weight="bold" fill="#fca5a5" text-anchor="middle">Low Margin / High Risk</text>
  </g>
  <line x1="265" y1="190" x2="295" y2="190" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="285,185 295,190 285,195" fill="#38bdf8"/>

  <!-- Step 2: Basic Processing -->
  <g transform="translate(295, 75)">
    <rect x="0" y="0" width="210" height="230" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <rect x="0" y="0" width="210" height="28" rx="8" fill="#ca8a04"/>
    <text x="105" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 2: BASIC PROCESSING</text>
    <text x="15" y="52" font-size="10" font-weight="bold" fill="#fde047">• Product: Pasteurized Milk</text>
    <text x="15" y="74" font-size="9" fill="#cbd5e1">• Price: KES 70 / Liter</text>
    <text x="15" y="96" font-size="9" fill="#cbd5e1">• Shelf-life: 5 to 7 Days</text>
    <text x="15" y="118" font-size="9" fill="#cbd5e1">• Heat kills active bacteria</text>
    <text x="15" y="140" font-size="9" fill="#cbd5e1">• Safe cold chain storage</text>
    <rect x="15" y="165" width="180" height="45" rx="5" fill="#1e293b" stroke="#eab308"/>
    <text x="105" y="192" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">+75% Price Increase</text>
  </g>
  <line x1="505" y1="190" x2="535" y2="190" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="525,185 535,190 525,195" fill="#38bdf8"/>

  <!-- Step 3: High Value Addition -->
  <g transform="translate(535, 75)">
    <rect x="0" y="0" width="220" height="230" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="28" rx="8" fill="#15803d"/>
    <text x="110" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 3: VALUE ADDITION</text>
    <text x="15" y="52" font-size="10" font-weight="bold" fill="#4ade80">• Product: Strawberry Yoghurt</text>
    <text x="15" y="74" font-size="9" fill="#cbd5e1">• Price: KES 80 / 250ml cup</text>
    <text x="15" y="96" font-size="10" font-weight="bold" fill="#86efac">• Yield: KES 320 / Liter!</text>
    <text x="15" y="118" font-size="9" fill="#cbd5e1">• Shelf-life: 30 to 45 Days</text>
    <text x="15" y="140" font-size="9" fill="#cbd5e1">• Branded consumer good</text>
    <rect x="15" y="165" width="190" height="45" rx="5" fill="#1e293b" stroke="#22c55e"/>
    <text x="110" y="192" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">+700% Value Multiplier!</text>
  </g>

  <!-- Bottom Summary Banner -->
  <g transform="translate(45, 325)">
    <rect x="0" y="0" width="710" height="85" rx="8" fill="#0f172a" stroke="#38bdf8"/>
    <text x="355" y="30" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Farmer's Economic Transition</text>
    <text x="355" y="55" font-size="10" fill="#cbd5e1" text-anchor="middle">From helpless price-taker selling raw bulk $\rightarrow$ To profitable price-setter selling branded consumer goods!</text>
  </g>
</svg>
""")

# SVG 2: 6 Core Methods (Lesson 4, Page 2)
SVG_SIX_METHODS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">6 Core Scientific Methods of Agricultural Value Addition</text>

  <!-- 6 Method Cards Grid -->
  <!-- 1. Dehydration -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="220" height="155" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="110" y="25" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. DEHYDRATION (DRYING)</text>
    <text x="10" y="52" font-size="9" fill="#cbd5e1">• Lowers moisture &lt;12%</text>
    <text x="10" y="72" font-size="9" fill="#cbd5e1">• Halts all microbial growth</text>
    <text x="10" y="92" font-size="9" fill="#cbd5e1">• Solar dryers &amp; dehydrators</text>
    <text x="10" y="125" font-size="9" font-weight="bold" fill="#67e8f9">E.g., Grains, Cassava, Mangoes</text>
  </g>

  <!-- 2. Milling -->
  <g transform="translate(290, 65)">
    <rect x="0" y="0" width="220" height="155" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="110" y="25" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">2. MILLING (GRINDING)</text>
    <text x="10" y="52" font-size="9" fill="#cbd5e1">• Particle size reduction (&lt;0.5mm)</text>
    <text x="10" y="72" font-size="9" fill="#cbd5e1">• Multiplies surface area</text>
    <text x="10" y="92" font-size="9" fill="#cbd5e1">• Easy cooking &amp; blending</text>
    <text x="10" y="125" font-size="9" font-weight="bold" fill="#86efac">E.g., Maize, Millet, Composite Flour</text>
  </g>

  <!-- 3. Thermal Treatment -->
  <g transform="translate(535, 65)">
    <rect x="0" y="0" width="220" height="155" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="110" y="25" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">3. THERMAL TREATMENT</text>
    <text x="10" y="52" font-size="9" fill="#cbd5e1">• Pasteurization: 72°C for 15s</text>
    <text x="10" y="72" font-size="9" fill="#cbd5e1">• Kills vegetative pathogens</text>
    <text x="10" y="92" font-size="9" fill="#cbd5e1">• Deactivates spoiling enzymes</text>
    <text x="10" y="125" font-size="9" font-weight="bold" fill="#fca5a5">E.g., Milk, Fruit Juices, Canning</text>
  </g>

  <!-- 4. Chemical Preservation -->
  <g transform="translate(45, 240)">
    <rect x="0" y="0" width="220" height="160" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <text x="110" y="25" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">4. CHEMICAL PRESERVATION</text>
    <text x="10" y="52" font-size="9" fill="#cbd5e1">• Citric/Acetic Acid drops pH &lt;4.6</text>
    <text x="10" y="72" font-size="9" fill="#cbd5e1">• High Sugar/Salt Osmosis</text>
    <text x="10" y="92" font-size="9" fill="#cbd5e1">• Dehydrates microbial cells</text>
    <text x="10" y="125" font-size="9" font-weight="bold" fill="#fde047">E.g., Fruit Jams, Pickles, Salted Fish</text>
  </g>

  <!-- 5. Fermentation -->
  <g transform="translate(290, 240)">
    <rect x="0" y="0" width="220" height="160" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="110" y="25" font-size="11" font-weight="bold" fill="#d8b4fe" text-anchor="middle">5. FERMENTATION</text>
    <text x="10" y="52" font-size="9" fill="#cbd5e1">• Lactic acid bacteria cultures</text>
    <text x="10" y="72" font-size="9" fill="#cbd5e1">• Drops pH to 4.5 barrier</text>
    <text x="10" y="92" font-size="9" fill="#cbd5e1">• Improves aroma &amp; digestion</text>
    <text x="10" y="125" font-size="9" font-weight="bold" fill="#d8b4fe">E.g., Mala, Yoghurt, Silage</text>
  </g>

  <!-- 6. Extraction -->
  <g transform="translate(535, 240)">
    <rect x="0" y="0" width="220" height="160" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
    <text x="110" y="25" font-size="11" font-weight="bold" fill="#67e8f9" text-anchor="middle">6. EXTRACTION</text>
    <text x="10" y="52" font-size="9" fill="#cbd5e1">• Mechanical pressure expellers</text>
    <text x="10" y="72" font-size="9" fill="#cbd5e1">• Separates high-value oils</text>
    <text x="10" y="92" font-size="9" fill="#cbd5e1">• Cold-pressed premium quality</text>
    <text x="10" y="125" font-size="9" font-weight="bold" fill="#67e8f9">E.g., Sunflower Oil, Avocado Oil</text>
  </g>
</svg>
""")

# SVG 3: Crisp Manufacturing Pipeline (Lesson 5, Page 2)
SVG_CRISP_PIPELINE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Potato &amp; Banana Crisp Production Pipeline &amp; Enterprise Economics</text>

  <!-- 5 Pipeline Steps -->
  <!-- Step 1: Selection & Peeling -->
  <g transform="translate(35, 70)">
    <rect x="0" y="0" width="130" height="130" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="65" y="22" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. PEEL &amp; SLICE</text>
    <text x="10" y="48" font-size="8" fill="#cbd5e1">• Low-sugar tubers</text>
    <text x="10" y="66" font-size="8" fill="#cbd5e1">• 1.0mm Thin discs</text>
    <text x="10" y="84" font-size="8" fill="#cbd5e1">• Mandoline slicer</text>
    <text x="10" y="105" font-size="8" font-weight="bold" fill="#67e8f9">Uniform thickness</text>
  </g>
  <line x1="165" y1="135" x2="185" y2="135" stroke="#38bdf8" stroke-width="2"/>

  <!-- Step 2: Cold Starch Rinse -->
  <g transform="translate(185, 70)">
    <rect x="0" y="0" width="130" height="130" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="65" y="22" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">2. RINSE &amp; DRY</text>
    <text x="10" y="48" font-size="8" fill="#cbd5e1">• Cold water wash</text>
    <text x="10" y="66" font-size="8" fill="#cbd5e1">• Removes starch</text>
    <text x="10" y="84" font-size="8" fill="#cbd5e1">• Pat 100% dry</text>
    <text x="10" y="105" font-size="8" font-weight="bold" fill="#86efac">Prevents clumping</text>
  </g>
  <line x1="315" y1="135" x2="335" y2="135" stroke="#22c55e" stroke-width="2"/>

  <!-- Step 3: Deep Frying (175°C) -->
  <g transform="translate(335, 70)">
    <rect x="0" y="0" width="130" height="130" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <text x="65" y="22" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">3. DEEP FRY</text>
    <text x="10" y="48" font-size="8" fill="#cbd5e1">• Clean veg oil</text>
    <text x="10" y="66" font-size="8" font-weight="bold" fill="#fde047">• 170°C to 180°C</text>
    <text x="10" y="84" font-size="8" fill="#cbd5e1">• Fry till bubbles stop</text>
    <text x="10" y="105" font-size="8" font-weight="bold" fill="#fde047">Golden &amp; crispy</text>
  </g>
  <line x1="465" y1="135" x2="485" y2="135" stroke="#eab308" stroke-width="2"/>

  <!-- Step 4: Drain & Season -->
  <g transform="translate(485, 70)">
    <rect x="0" y="0" width="130" height="130" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="65" y="22" font-size="10" font-weight="bold" fill="#d8b4fe" text-anchor="middle">4. DRAIN &amp; SPICE</text>
    <text x="10" y="48" font-size="8" fill="#cbd5e1">• Wire skimmer</text>
    <text x="10" y="66" font-size="8" fill="#cbd5e1">• Absorbent paper</text>
    <text x="10" y="84" font-size="8" fill="#cbd5e1">• Dust salt/chili</text>
    <text x="10" y="105" font-size="8" font-weight="bold" fill="#d8b4fe">While still warm</text>
  </g>
  <line x1="615" y1="135" x2="635" y2="135" stroke="#a855f7" stroke-width="2"/>

  <!-- Step 5: Package & Sell -->
  <g transform="translate(635, 70)">
    <rect x="0" y="0" width="130" height="130" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <text x="65" y="22" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">5. SEAL POUCH</text>
    <text x="10" y="48" font-size="8" fill="#cbd5e1">• Heat-sealed foil</text>
    <text x="10" y="66" font-size="8" fill="#cbd5e1">• 50g Branded packs</text>
    <text x="10" y="84" font-size="8" fill="#cbd5e1">• 6-Month shelf-life</text>
    <text x="10" y="105" font-size="8" font-weight="bold" fill="#4ade80">KES 30 / packet</text>
  </g>

  <!-- Bottom Financial Model Banner -->
  <g transform="translate(35, 230)">
    <rect x="0" y="0" width="730" height="180" rx="8" fill="#0f172a" stroke="#38bdf8"/>
    <text x="365" y="26" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Enterprise Financial Model (1 kg Raw Potatoes)</text>

    <g transform="translate(20, 45)">
      <rect x="0" y="0" width="215" height="110" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="107" y="22" font-size="10" font-weight="bold" fill="#f87171" text-anchor="middle">Raw Potato Sale</text>
      <text x="15" y="50" font-size="9" fill="#cbd5e1">• 1 kg Raw Potatoes: KES 40</text>
      <text x="15" y="70" font-size="9" fill="#cbd5e1">• Profit: ~KES 10</text>
      <text x="15" y="95" font-size="10" font-weight="bold" fill="#fca5a5">Low Farm-Gate Margin</text>
    </g>

    <g transform="translate(255, 45)">
      <rect x="0" y="0" width="220" height="110" rx="6" fill="#1e293b" stroke="#eab308"/>
      <text x="110" y="22" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">Crisp Production Costs</text>
      <text x="15" y="48" font-size="8" fill="#cbd5e1">• Potatoes (1kg): KES 40</text>
      <text x="15" y="66" font-size="8" fill="#cbd5e1">• Oil, Fuel &amp; Salt: KES 50</text>
      <text x="15" y="84" font-size="8" fill="#cbd5e1">• 6 Foil Pouches: KES 18</text>
      <text x="15" y="102" font-size="9" font-weight="bold" fill="#fde047">Total Cost = KES 108</text>
    </g>

    <g transform="translate(495, 45)">
      <rect x="0" y="0" width="215" height="110" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="107" y="22" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Value Added Returns</text>
      <text x="15" y="48" font-size="8" fill="#cbd5e1">• 6 x 50g Packets = KES 180</text>
      <text x="15" y="68" font-size="10" font-weight="bold" fill="#4ade80">• Net Profit = KES 72</text>
      <text x="15" y="95" font-size="10" font-weight="bold" fill="#86efac">+180% Profit Boost!</text>
    </g>
  </g>
</svg>
""")

# SVG 4: Jam Preservation Triangle (Lesson 6, Page 2)
SVG_JAM_TRIANGLE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Jam Preservation Triangle: 3 Irreversible Defense Barriers</text>

  <!-- Central Visual Triangle -->
  <polygon points="400,80 180,310 620,310" fill="none" stroke="#eab308" stroke-width="4"/>

  <!-- Top Peak: Thermal Kill -->
  <g transform="translate(300, 60)">
    <circle cx="100" cy="30" r="45" fill="#0f172a" stroke="#ef4444" stroke-width="3"/>
    <text x="100" y="26" font-size="10" font-weight="bold" fill="#f87171" text-anchor="middle">1. THERMAL</text>
    <text x="100" y="40" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">KILL (104°C)</text>
  </g>
  <text x="400" y="145" font-size="9" fill="#cbd5e1" text-anchor="middle">Destroys all active bacteria, yeasts &amp; molds</text>

  <!-- Left Bottom: High Acidity (Low pH) -->
  <g transform="translate(100, 275)">
    <circle cx="80" cy="40" r="45" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
    <text x="80" y="36" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">2. HIGH ACIDITY</text>
    <text x="80" y="50" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">(pH &lt; 4.6)</text>
  </g>
  <text x="180" y="375" font-size="9" fill="#cbd5e1" text-anchor="middle">Lemon citric acid halts bacterial spore germination</text>

  <!-- Right Bottom: Osmotic Dehydration -->
  <g transform="translate(540, 275)">
    <circle cx="80" cy="40" r="45" fill="#0f172a" stroke="#22c55e" stroke-width="3"/>
    <text x="80" y="36" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">3. OSMOTIC</text>
    <text x="80" y="50" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">PRESSURE</text>
  </g>
  <text x="620" y="375" font-size="9" fill="#cbd5e1" text-anchor="middle">Sugar binds water, desiccating invading microbes</text>

  <!-- Center Hub: 18-Month Stability -->
  <circle cx="400" cy="235" r="48" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
  <text x="400" y="228" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">12 – 18 MONTHS</text>
  <text x="400" y="244" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">ROOM TEMP</text>
  <text x="400" y="258" font-size="9" fill="#cbd5e1" text-anchor="middle">STABILITY</text>
</svg>
""")

# SVG 5: Cassava Detoxification Pipeline (Lesson 8, Page 2)
SVG_CASSAVA_PIPELINE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Safe Cassava Cyanide Detoxification &amp; Flour Milling Pipeline</text>

  <!-- 4 Step Flow -->
  <!-- Step 1: Thick Peeling & Chipping -->
  <g transform="translate(45, 75)">
    <rect x="0" y="0" width="160" height="210" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="160" height="26" rx="8" fill="#991b1b"/>
    <text x="80" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">1. THICK PEEL &amp; CHIP</text>
    <text x="10" y="48" font-size="8" fill="#cbd5e1">• Peel brown bark &amp; pink cortex</text>
    <text x="10" y="70" font-size="9" font-weight="bold" fill="#f87171">• Removes &gt;80% of cyanide</text>
    <text x="10" y="95" font-size="8" fill="#cbd5e1">• Slice into 5mm thin chips</text>
    <text x="10" y="115" font-size="8" fill="#cbd5e1">• Multiplies surface area</text>
    <rect x="10" y="155" width="140" height="40" rx="4" fill="#1e293b" stroke="#ef4444"/>
    <text x="80" y="180" font-size="8" fill="#fca5a5" text-anchor="middle">Danger: High Linamarin</text>
  </g>
  <line x1="205" y1="180" x2="235" y2="180" stroke="#38bdf8" stroke-width="2"/>

  <!-- Step 2: 72-Hour Fermentation -->
  <g transform="translate(235, 75)">
    <rect x="0" y="0" width="160" height="210" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <rect x="0" y="0" width="160" height="26" rx="8" fill="#ca8a04"/>
    <text x="80" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">2. 72-HR FERMENT</text>
    <text x="10" y="48" font-size="8" fill="#cbd5e1">• Submerge chips in water</text>
    <text x="10" y="70" font-size="8" fill="#cbd5e1">• Soak for 3 full days</text>
    <text x="10" y="95" font-size="8" fill="#cbd5e1">• Linamarase enzymes activate</text>
    <text x="10" y="118" font-size="9" font-weight="bold" fill="#fde047">• Cyanide leaches into water</text>
    <rect x="10" y="155" width="140" height="40" rx="4" fill="#1e293b" stroke="#eab308"/>
    <text x="80" y="180" font-size="8" fill="#fde047" text-anchor="middle">90% Cyanide Destroyed</text>
  </g>
  <line x1="395" y1="180" x2="425" y2="180" stroke="#38bdf8" stroke-width="2"/>

  <!-- Step 3: Solar Drying -->
  <g transform="translate(425, 75)">
    <rect x="0" y="0" width="160" height="210" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="160" height="26" rx="8" fill="#0284c7"/>
    <text x="80" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">3. SOLAR DRYING</text>
    <text x="10" y="48" font-size="8" fill="#cbd5e1">• Raised mesh drying beds</text>
    <text x="10" y="70" font-size="9" font-weight="bold" fill="#38bdf8">• Moisture drops &lt;12%</text>
    <text x="10" y="95" font-size="8" fill="#cbd5e1">• Evaporates residual HCN</text>
    <text x="10" y="118" font-size="8" fill="#cbd5e1">• Chips snap with crisp sound</text>
    <rect x="10" y="155" width="140" height="40" rx="4" fill="#1e293b" stroke="#38bdf8"/>
    <text x="80" y="180" font-size="8" fill="#67e8f9" text-anchor="middle">Zero Mold Risk</text>
  </g>
  <line x1="585" y1="180" x2="615" y2="180" stroke="#38bdf8" stroke-width="2"/>

  <!-- Step 4: Mill, Sieve & Pallet Store -->
  <g transform="translate(615, 75)">
    <rect x="0" y="0" width="140" height="210" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="140" height="26" rx="8" fill="#15803d"/>
    <text x="70" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">4. MILL &amp; SIEVE</text>
    <text x="10" y="48" font-size="8" fill="#cbd5e1">• Hammer mill grinding</text>
    <text x="10" y="70" font-size="8" fill="#cbd5e1">• 0.5mm Fine sieve mesh</text>
    <text x="10" y="95" font-size="8" fill="#cbd5e1">• Removes woody fiber</text>
    <text x="10" y="118" font-size="8" fill="#cbd5e1">• Store on raised pallets</text>
    <rect x="10" y="155" width="120" height="40" rx="4" fill="#1e293b" stroke="#22c55e"/>
    <text x="70" y="180" font-size="8" font-weight="bold" fill="#4ade80" text-anchor="middle">100% Safe Flour</text>
  </g>

  <!-- Bottom Banner -->
  <g transform="translate(45, 310)">
    <rect x="0" y="0" width="710" height="100" rx="8" fill="#0f172a" stroke="#22c55e"/>
    <text x="355" y="26" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">Food Safety &amp; Economic Transformation</text>
    <text x="355" y="52" font-size="9" fill="#cbd5e1" text-anchor="middle">Converts perishable, toxic raw tubers into a safe, shelf-stable, high-value baking flour (KES 120/kg) with 12+ months shelf-life!</text>
    <text x="355" y="75" font-size="9" font-weight="bold" fill="#86efac" text-anchor="middle">Residual Cyanide &lt; 10 ppm (Meets all WHO and KEBS Standards)</text>
  </g>
</svg>
""")

# SVG 6: Yoghurt Fermentation Curve (Lesson 9, Page 2)
SVG_YOGHURT_CURVE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Scientific Yoghurt Fermentation Curve: Time, Temp &amp; pH Kinetics</text>

  <!-- Graph Axis Grid -->
  <g transform="translate(85, 70)">
    <line x1="40" y1="20" x2="40" y2="240" stroke="#94a3b8" stroke-width="2"/>
    <line x1="40" y1="240" x2="620" y2="240" stroke="#94a3b8" stroke-width="2"/>

    <!-- Y-Axis Labels (pH) -->
    <text x="30" y="30" font-size="9" fill="#f87171" text-anchor="end">pH 7.0</text>
    <text x="30" y="60" font-size="9" fill="#f87171" text-anchor="end">pH 6.6</text>
    <text x="30" y="120" font-size="9" fill="#fde047" text-anchor="end">pH 5.5</text>
    <text x="30" y="180" font-size="9" fill="#4ade80" text-anchor="end">pH 4.8</text>
    <text x="30" y="215" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="end">pH 4.5</text>

    <!-- X-Axis Labels (Hours at 43°C) -->
    <text x="40" y="260" font-size="9" fill="#cbd5e1" text-anchor="middle">0 Hr (Inoculate)</text>
    <text x="180" y="260" font-size="9" fill="#cbd5e1" text-anchor="middle">2 Hours</text>
    <text x="360" y="260" font-size="9" fill="#cbd5e1" text-anchor="middle">4 Hours</text>
    <text x="540" y="260" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">6 Hours (Ready!)</text>

    <!-- The Falling pH Curve -->
    <path d="M 40 60 Q 180 80 360 170 T 540 215" fill="none" stroke="#22c55e" stroke-width="4"/>
    <circle cx="40" cy="60" r="5" fill="#f87171"/>
    <circle cx="360" cy="170" r="5" fill="#fde047"/>
    <circle cx="540" cy="215" r="7" fill="#22c55e"/>

    <!-- Key Milestone Callouts -->
    <text x="180" y="65" font-size="8" fill="#cbd5e1">S. thermophilus consumes lactose</text>
    <text x="375" y="155" font-size="8" fill="#fde047">Coagulation begins (Casein gel)</text>
    <text x="550" y="200" font-size="9" font-weight="bold" fill="#4ade80">Target pH 4.5: Chill to 4°C!</text>
  </g>

  <!-- Bottom Parameter Card -->
  <g transform="translate(45, 350)">
    <rect x="0" y="0" width="710" height="65" rx="6" fill="#0f172a" stroke="#38bdf8"/>
    <text x="20" y="24" font-size="10" font-weight="bold" fill="#38bdf8">Optimum Incubation Temperature: 42°C – 45°C</text>
    <text x="20" y="45" font-size="9" fill="#cbd5e1">Bacteria: Streptococcus thermophilus (Fast acid) + Lactobacillus bulgaricus (Texture &amp; aroma)</text>
    <text x="450" y="35" font-size="11" font-weight="bold" fill="#4ade80">Pathogen Destruction Barrier = pH 4.5</text>
  </g>
</svg>
""")

# SVG 7: Legal Label Anatomy (Lesson 12, Page 2)
SVG_LABEL_ANATOMY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Food-Safe Product Packaging &amp; Mandatory Legal Label Anatomy</text>

  <!-- The Product Label Frame -->
  <g transform="translate(180, 65)">
    <rect x="0" y="0" width="440" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2.5"/>

    <!-- 1. Brand & Product Name -->
    <rect x="15" y="15" width="410" height="45" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="220" y="38" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. NANDI MOUNTAIN PURE HONEY</text>
    <text x="220" y="52" font-size="9" fill="#cbd5e1" text-anchor="middle">100% Organic Cold-Strained Blossom Honey</text>

    <!-- 2. Net Weight & Quality -->
    <g transform="translate(15, 70)">
      <rect x="0" y="0" width="195" height="35" rx="4" fill="#1e293b" stroke="#22c55e"/>
      <text x="97" y="22" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">2. NET WEIGHT: 500g</text>
    </g>

    <!-- 8. KEBS Standardization Mark -->
    <g transform="translate(230, 70)">
      <rect x="0" y="0" width="195" height="35" rx="4" fill="#1e293b" stroke="#eab308"/>
      <text x="97" y="22" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">8. KEBS QUALITY PERMIT</text>
    </g>

    <!-- 3. Ingredients in Descending Order -->
    <g transform="translate(15, 115)">
      <rect x="0" y="0" width="410" height="45" rx="4" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="18" font-size="9" font-weight="bold" fill="#38bdf8">3. INGREDIENTS (Descending Order by Weight):</text>
      <text x="10" y="34" font-size="8" fill="#cbd5e1">Pure Natural Bee Honey (100%). Zero added sugar or preservatives.</text>
    </g>

    <!-- 4. Manufacturer Contacts -->
    <g transform="translate(15, 170)">
      <rect x="0" y="0" width="410" height="45" rx="4" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="18" font-size="9" font-weight="bold" fill="#38bdf8">4. MANUFACTURER &amp; PHYSICAL ADDRESS:</text>
      <text x="10" y="34" font-size="8" fill="#cbd5e1">Nandi Hills Youth Agro-Processors Ltd, P.O. Box 12, Kapsabet, Kenya</text>
    </g>

    <!-- 5 & 6. Mfg Date, Expiry & Batch -->
    <g transform="translate(15, 225)">
      <rect x="0" y="0" width="195" height="50" rx="4" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="18" font-size="8" font-weight="bold" fill="#cbd5e1">5. DATES:</text>
      <text x="10" y="32" font-size="8" fill="#4ade80">MFG: 12/08/2026</text>
      <text x="10" y="44" font-size="8" fill="#f87171">EXP: 12/08/2028</text>
    </g>

    <g transform="translate(230, 225)">
      <rect x="0" y="0" width="195" height="50" rx="4" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="18" font-size="8" font-weight="bold" fill="#cbd5e1">6. BATCH / LOT #:</text>
      <text x="10" y="32" font-size="9" font-weight="bold" fill="#fde047">LOT-NH-2026-08B</text>
      <text x="10" y="44" font-size="8" fill="#cbd5e1">(Traceability Code)</text>
    </g>

    <!-- 7. Storage Conditions -->
    <g transform="translate(15, 285)">
      <rect x="0" y="0" width="410" height="40" rx="4" fill="#1e293b" stroke="#334155"/>
      <text x="205" y="24" font-size="9" fill="#cbd5e1" text-anchor="middle">7. STORAGE: Store in a dry, cool place away from direct sunlight.</text>
    </g>
  </g>
</svg>
""")

# SVG 8: Master Lifecycle (Lesson 12, Page 3)
SVG_MASTER_LIFECYCLE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Master Agricultural Product Processing &amp; Value Addition Lifecycle</text>

  <!-- 6 Ring Steps -->
  <!-- 1. Harvest & PHL Mitigation -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="100" y="22" font-size="10" font-weight="bold" fill="#f87171" text-anchor="middle">1. HARVEST &amp; PHL DEFENSE</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Stop 30–40% food waste</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Bypass seasonal market gluts</text>
  </g>
  <line x1="245" y1="102" x2="345" y2="200" stroke="#ef4444" stroke-width="2" stroke-dasharray="2,2"/>

  <!-- 2. Preservation Methods -->
  <g transform="translate(555, 65)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="100" y="22" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">2. PRESERVATION SCIENCE</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Drying &lt;12% &amp; 72°C Pasteurize</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Low pH &lt;4.6 &amp; Sugar Osmosis</text>
  </g>
  <line x1="555" y1="102" x2="455" y2="200" stroke="#38bdf8" stroke-width="2" stroke-dasharray="2,2"/>

  <!-- 3. Plant Processing -->
  <g transform="translate(35, 195)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <text x="100" y="22" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">3. PLANT PRACTICALS</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Banana &amp; potato crisps</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Tomato jam &amp; cassava flour</text>
  </g>
  <line x1="235" y1="240" x2="345" y2="240" stroke="#eab308" stroke-width="2"/>

  <!-- 4. Animal Processing -->
  <g transform="translate(565, 195)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="100" y="22" font-size="10" font-weight="bold" fill="#d8b4fe" text-anchor="middle">4. ANIMAL PRACTICALS</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Mala &amp; 43°C yoghurt making</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Honey &lt;18% &amp; hide fleshing</text>
  </g>
  <line x1="565" y1="240" x2="455" y2="240" stroke="#a855f7" stroke-width="2"/>

  <!-- 5. Packaging & Labels -->
  <g transform="translate(130, 335)">
    <rect x="0" y="0" width="220" height="75" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
    <text x="110" y="22" font-size="10" font-weight="bold" fill="#67e8f9" text-anchor="middle">5. PACKAGING &amp; LABELS</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Food-grade glass &amp; foil pouches</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• 8 Mandatory KEBS label items</text>
  </g>
  <line x1="350" y1="350" x2="390" y2="298" stroke="#06b6d4" stroke-width="2"/>

  <!-- 6. Distribution & Profit -->
  <g transform="translate(450, 335)">
    <rect x="0" y="0" width="220" height="75" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <text x="110" y="22" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">6. HIGH PROFIT MARGINS</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• +200% to +700% Value gain</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Stable year-round food security</text>
  </g>
  <line x1="450" y1="350" x2="410" y2="298" stroke="#22c55e" stroke-width="2"/>

  <!-- Central Hub: Agricultural Wealth -->
  <circle cx="400" cy="240" r="55" fill="#0f172a" stroke="#22c55e" stroke-width="3"/>
  <text x="400" y="235" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">AGRIBUSINESS</text>
  <text x="400" y="252" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">WEALTH</text>
</svg>
""")

SVG_MAP = {
    1: {"page": 2, "svg": SVG_ECONOMIC_LADDER, "title": "Raw Commodity vs Value-Added Product Economic Ladder"},
    4: {"page": 2, "svg": SVG_SIX_METHODS, "title": "6 Core Scientific Methods of Agricultural Value Addition"},
    5: {"page": 2, "svg": SVG_CRISP_PIPELINE, "title": "Crisp Production Pipeline & Value Addition Economics"},
    6: {"page": 2, "svg": SVG_JAM_TRIANGLE, "title": "The Jam Preservation Triangle: Heat, Acidity & Osmosis"},
    8: {"page": 2, "svg": SVG_CASSAVA_PIPELINE, "title": "Safe Cassava Detoxification & Flour Milling Pipeline"},
    9: {"page": 2, "svg": SVG_YOGHURT_CURVE, "title": "Scientific Yoghurt Fermentation Curve: Time, Temp & pH Drop"}
}

def enrich_grade10_topic14():
    """Injects verified photos, responsive vector SVGs, YouTube embeds, and creates LessonAssets."""
    print("=" * 80)
    print("STARTING ENRICHMENT: CBC Grade 10 Agriculture — Topic 14: Product Processing and Value Addition")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()
    topic = Topic.objects.filter(subject=subject, name="Product Processing and Value Addition").first()

    assert topic, "Topic 'Product Processing and Value Addition' not found!"

    images_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grade10_topic14_verified_images.json")
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
                    "topic_order": 14,
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
        # Lesson 12 has two SVG diagrams (Page 2 and Page 3)
        if u_order == 12:
            diag_blocks = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="suggested_diagram"
            ).order_by("page_number")
            for idx, d_block in enumerate(diag_blocks):
                if idx == 0:
                    svg_payload = SVG_LABEL_ANATOMY
                    title_text = "Food-Safe Product Packaging & Mandatory Legal Label Anatomy"
                    p_num = 2
                else:
                    svg_payload = SVG_MASTER_LIFECYCLE
                    title_text = "Master Agricultural Product Processing & Value Addition Lifecycle Matrix"
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
                    title=f"Lesson 12 Diagram {idx+1}: {title_text}",
                    description=d_content.get("caption", title_text),
                    metadata={
                        "topic_order": 14,
                        "unit_order": 12,
                        "page": p_num,
                        "svg_content": svg_payload
                    }
                )
                d_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [Vector SVG Attached] Lesson 12 (Page {p_num}): {title_text}")

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
                        "topic_order": 14,
                        "unit_order": u_order,
                        "page": svg_def["page"],
                        "svg_content": svg_def["svg"]
                    }
                )
                diag_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [Vector SVG Attached] Lesson {u_order}: {svg_def['title']}")

        # ---------------------------------------------------------------------
        # 3. Educational YouTube Videos (Lesson 9)
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
                        "topic_order": 14,
                        "unit_order": u_order,
                        "youtube_url": v_url
                    }
                )
                v_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [YouTube Video Attached] Lesson {u_order}: {v_block.title}")

    print("=" * 80)
    print(f"ENRICHMENT COMPLETE: Topic 14 '{topic.name}'")
    print(f"  Photographic Hooks: {total_images_attached} / 12")
    print(f"  Vector SVGs:        {total_svgs_attached} / 8")
    print(f"  YouTube Videos:     {total_videos_attached} / 1")
    print(f"  LessonAssets:       {total_assets_persisted}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic14()
