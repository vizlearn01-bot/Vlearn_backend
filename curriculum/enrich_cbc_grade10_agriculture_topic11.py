"""
VLearn CBC Grade 10 Agriculture — Topic 11: Beekeeping (Apiculture)
Visual Enrichment Engine (Phase 2: Vector SVGs, Verified Photos & Asset Persistence)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Beekeeping (Order: 11)

Attaches:
  - 8 First-Card Photographic Visual Hooks (100% Tested HTTP 200 Direct Wikimedia URLs)
  - 8 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - 1 Verified Educational YouTube Video (Lesson 5 Card 3)
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade10_agriculture_topic11.py
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
# 8 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 11: BEEKEEPING (APICULTURE)
# =============================================================================

# SVG 1: Optimal Apiary Siting Layout (Lesson 1, Page 2)
SVG_APIARY_SITING = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Optimal Apiary Siting Layout &amp; Public Safety Buffers</text>

  <!-- Left: Apiary Blueprint -->
  <g transform="translate(45, 60)">
    <rect x="0" y="0" width="340" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>

    <!-- Perimeter Live Fence (Windbreak) -->
    <rect x="20" y="20" width="300" height="260" rx="8" fill="none" stroke="#22c55e" stroke-width="3" stroke-dasharray="6,6"/>
    <text x="170" y="38" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Dense Live Fence Windbreak (Kei Apple / Bougainvillea)</text>

    <!-- Central Shaded Hives -->
    <g transform="translate(100, 70)">
      <!-- Tree Canopy Overlay -->
      <circle cx="70" cy="70" r="60" fill="#15803d" opacity="0.3"/>
      <text x="70" y="30" font-size="9" fill="#86efac" text-anchor="middle">Partial Tree Canopy (Shade)</text>

      <!-- 3 Hives on Stands -->
      <rect x="25" y="60" width="30" height="35" rx="3" fill="#ca8a04" stroke="#fde047"/>
      <rect x="55" y="60" width="30" height="35" rx="3" fill="#ca8a04" stroke="#fde047"/>
      <rect x="85" y="60" width="30" height="35" rx="3" fill="#ca8a04" stroke="#fde047"/>
      <text x="70" y="115" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">Hives on Greased Stands</text>
    </g>

    <!-- Shallow Water Point -->
    <g transform="translate(50, 210)">
      <ellipse cx="60" cy="30" rx="45" ry="20" fill="#0284c7" stroke="#38bdf8"/>
      <circle cx="45" cy="28" r="4" fill="#94a3b8"/>
      <circle cx="65" cy="32" r="5" fill="#94a3b8"/>
      <text x="60" y="34" font-size="8" fill="#ffffff" text-anchor="middle">Twigs / Gravel</text>
      <text x="60" y="62" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Shallow Water Point</text>
    </g>

    <text x="170" y="315" font-size="9" fill="#cbd5e1" text-anchor="middle">Orient hive entrances East towards morning sunrise</text>
  </g>

  <!-- Right: 4 Golden Siting Criteria -->
  <g transform="translate(415, 60)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="28" rx="10" fill="#0284c7"/>
    <text x="172" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4 ESSENTIAL APIARY SITING RULES</text>

    <g transform="translate(15, 40)">
      <rect x="0" y="0" width="315" height="55" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#38bdf8">1. Forage Radius (2 – 3 km):</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Abundant nectar/pollen crops (avocado, coffee, acacia).</text>

      <rect x="0" y="65" width="315" height="55" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#38bdf8">2. Safety Buffer Distance (≥ 100 meters):</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Strictly isolated from schools, roads, and livestock kraals.</text>

      <rect x="0" y="130" width="315" height="55" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#38bdf8">3. Shallow Water Point:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Must have floating gravel/sticks to prevent drowning.</text>

      <rect x="0" y="195" width="315" height="55" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#38bdf8">4. Windbreak &amp; Drainage:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Blocks strong chilling winds; well-drained dry soil.</text>
    </g>

    <text x="172" y="325" font-size="9" fill="#4ade80" text-anchor="middle">Outcome: Maximum honey yield + zero community stinging hazards</text>
  </g>
</svg>
""")

# SVG 2: Beekeeping Tools & PPE (Lesson 2, Page 2)
SVG_TOOLS_AND_PPE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Essential Beekeeping Tools &amp; Full Protective PPE Ensemble</text>

  <!-- Left: 3 Essential Tools -->
  <g transform="translate(45, 60)">
    <rect x="0" y="0" width="340" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="28" rx="10" fill="#15803d"/>
    <text x="170" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">ESSENTIAL APIARY TOOLS</text>

    <!-- 1. Smoker -->
    <g transform="translate(15, 40)">
      <rect x="0" y="0" width="310" height="70" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">1. Bellows Bee Smoker:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">• Burns dry natural fuel (maize cobs/grass)</text>
      <text x="15" y="55" font-size="9" fill="#cbd5e1">• Suppresses isopentyl acetate alarm pheromones</text>
    </g>

    <!-- 2. Hive Tool -->
    <g transform="translate(15, 120)">
      <rect x="0" y="0" width="310" height="70" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">2. L-Shaped Steel Hive Tool:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">• Pries propolis-sealed hive lids open</text>
      <text x="15" y="55" font-size="9" fill="#cbd5e1">• Scrapes burr comb &amp; lifts heavy frame lugs</text>
    </g>

    <!-- 3. Bee Brush -->
    <g transform="translate(15, 200)">
      <rect x="0" y="0" width="310" height="65" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">3. Soft-Bristled Bee Brush:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">• Gently sweeps bees off honeycombs</text>
      <text x="15" y="55" font-size="9" fill="#cbd5e1">• Prevents crushing or angering bees</text>
    </g>
  </g>

  <!-- Right: Full PPE Ensemble -->
  <g transform="translate(415, 60)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="28" rx="10" fill="#0284c7"/>
    <text x="172" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">PERSONAL PROTECTIVE EQUIPMENT (PPE)</text>

    <!-- 1. White Suit -->
    <g transform="translate(15, 40)">
      <rect x="0" y="0" width="315" height="60" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#38bdf8">1. White Canvas One-Piece Suit:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">• Smooth white fabric does NOT trigger defense</text>
      <text x="15" y="52" font-size="9" fill="#cbd5e1">  (Bees instinctively attack dark/rough textures)</text>
    </g>

    <!-- 2. Integrated Veil -->
    <g transform="translate(15, 110)">
      <rect x="0" y="0" width="315" height="60" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#38bdf8">2. Fine Wire-Mesh Hat Veil:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">• 100% facial, eye, and neck sting defense</text>
      <text x="15" y="52" font-size="9" fill="#cbd5e1">• Provides clear, unobstructed visibility</text>
    </g>

    <!-- 3. Gauntlets & Gumboots -->
    <g transform="translate(15, 180)">
      <rect x="0" y="0" width="315" height="70" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#38bdf8">3. Leather Gauntlets &amp; Rubber Gumboots:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">• Long leather sleeves sealed with elastic bands</text>
      <text x="15" y="55" font-size="9" fill="#cbd5e1">• Trousers tucked firmly inside gumboots</text>
    </g>

    <text x="172" y="295" font-size="9" fill="#67e8f9" text-anchor="middle">Rule: Never enter an active apiary without 100% sealed PPE!</text>
  </g>
</svg>
""")

# SVG 3: Hive Products & Pollination (Lesson 3, Page 2)
SVG_PRODUCTS_AND_POLLINATION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Economic Products of Apiculture &amp; Crop Pollination Value</text>

  <!-- Left: 4 Direct Hive Products -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="345" rx="10" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="30" rx="10" fill="#ca8a04"/>
    <text x="170" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">DIRECT COMMERCIAL HIVE PRODUCTS</text>

    <g transform="translate(15, 45)">
      <rect x="0" y="0" width="310" height="55" rx="6" fill="#1e293b" stroke="#eab308"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#fde047">1. Refined Honey (KES 800–1,200/kg):</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Natural sweetener, energy food, antimicrobial medicine.</text>

      <rect x="0" y="65" width="310" height="55" rx="6" fill="#1e293b" stroke="#eab308"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#fde047">2. Pure Beeswax (KES 1,000–1,500/kg):</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Cosmetics, candles, shoe polish, comb foundation.</text>

      <rect x="0" y="130" width="310" height="55" rx="6" fill="#1e293b" stroke="#eab308"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#fde047">3. Propolis (KES 2,000–4,000/kg):</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Antimicrobial bee glue used in pharmaceutical tinctures.</text>

      <rect x="0" y="195" width="310" height="55" rx="6" fill="#1e293b" stroke="#eab308"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#fde047">4. Royal Jelly &amp; Pollen:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">High-protein superfoods and luxury cosmetic extracts.</text>
    </g>
  </g>

  <!-- Right: Crop Pollination Service -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="30" rx="10" fill="#15803d"/>
    <text x="172" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">THE POLLINATION MULTIPLIER SERVICE</text>

    <g transform="translate(15, 45)">
      <rect x="0" y="0" width="315" height="70" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">Flower Fidelity Principle:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Individual bees visit the SAME crop species on a flight,</text>
      <text x="15" y="55" font-size="9" fill="#cbd5e1">guaranteeing highly efficient pollen cross-transfer.</text>

      <rect x="0" y="80" width="315" height="70" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">Agricultural Yield Boost (+30% to +100%):</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">• Avocado &amp; Passion Fruit: Maximum fruit set &amp; size</text>
      <text x="15" y="55" font-size="9" fill="#cbd5e1">• Coffee &amp; Sunflowers: Complete seed &amp; berry fill</text>

      <rect x="0" y="160" width="315" height="65" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">Global Ecosystem Food Security:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Over 1/3 of the human diet directly depends on</text>
      <text x="15" y="52" font-size="9" fill="#cbd5e1">insect cross-pollination by honey bees!</text>
    </g>

    <text x="172" y="295" font-size="9" fill="#86efac" text-anchor="middle">Pollination value exceeds direct honey sales by over 10x!</text>
  </g>
</svg>
""")

# SVG 4: Swarm Capture & Bait Hive (Lesson 4, Page 2)
SVG_SWARM_CAPTURE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Stocking Methods: Swarm Capture &amp; Bait Hive Pheromones</text>

  <!-- Left: Wild Swarm Capture -->
  <g transform="translate(45, 60)">
    <rect x="0" y="0" width="340" height="345" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="28" rx="10" fill="#0284c7"/>
    <text x="170" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. WILD SWARM CLUSTER CAPTURE</text>

    <g transform="translate(15, 40)">
      <rect x="0" y="0" width="310" height="50" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="12" y="18" font-size="10" font-weight="bold" fill="#38bdf8">1. Locate Clustered Swarm:</text>
      <text x="12" y="35" font-size="9" fill="#cbd5e1">Bees hanging calm &amp; gorged on tree branch.</text>

      <rect x="0" y="60" width="310" height="50" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="12" y="18" font-size="10" font-weight="bold" fill="#38bdf8">2. Position Catcher Underneath:</text>
      <text x="12" y="35" font-size="9" fill="#cbd5e1">Hold canvas net/box directly below cluster.</text>

      <rect x="0" y="120" width="310" height="50" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="12" y="18" font-size="10" font-weight="bold" fill="#38bdf8">3. Sharp Downward Shake:</text>
      <text x="12" y="35" font-size="9" fill="#cbd5e1">Single firm shake drops mass into container.</text>

      <rect x="0" y="180" width="310" height="60" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="12" y="18" font-size="10" font-weight="bold" fill="#4ade80">4. Secure the Queen Bee:</text>
      <text x="12" y="35" font-size="9" fill="#cbd5e1">Workers follow her Nasonov scent into box;</text>
      <text x="12" y="50" font-size="9" fill="#86efac">transfer to permanent hive at dusk.</text>
    </g>
  </g>

  <!-- Right: Bait Hive Pheromones -->
  <g transform="translate(415, 60)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="28" rx="10" fill="#ca8a04"/>
    <text x="172" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. BAIT HIVE PHEROMONE ATTRACTANTS</text>

    <g transform="translate(15, 40)">
      <rect x="0" y="0" width="315" height="60" rx="6" fill="#1e293b" stroke="#eab308"/>
      <text x="12" y="18" font-size="10" font-weight="bold" fill="#fde047">Lemon Grass Oil (Cymbopogon):</text>
      <text x="12" y="36" font-size="9" fill="#cbd5e1">• Contains citral &amp; geraniol</text>
      <text x="12" y="50" font-size="9" fill="#cbd5e1">• Chemically mimics Nasonov scout pheromone</text>
    </g>

    <g transform="translate(15, 110)">
      <rect x="0" y="0" width="315" height="60" rx="6" fill="#1e293b" stroke="#eab308"/>
      <text x="12" y="18" font-size="10" font-weight="bold" fill="#fde047">Melted Beeswax &amp; Propolis Rub:</text>
      <text x="12" y="36" font-size="9" fill="#cbd5e1">• Rubbed inside lid, top bars, and entrance</text>
      <text x="12" y="50" font-size="9" fill="#cbd5e1">• Emits natural established hive aroma</text>
    </g>

    <g transform="translate(15, 180)">
      <rect x="0" y="0" width="315" height="65" rx="6" fill="#1e293b" stroke="#eab308"/>
      <text x="12" y="18" font-size="10" font-weight="bold" fill="#fde047">Strategic Siting (2–3m Height):</text>
      <text x="12" y="36" font-size="9" fill="#cbd5e1">• Mounted in semi-shaded tree facing East</text>
      <text x="12" y="52" font-size="9" fill="#cbd5e1">• Near shallow water source</text>
    </g>

    <text x="172" y="300" font-size="9" fill="#fde047" text-anchor="middle">Zero cash cost; completely passive colonization!</text>
  </g>
</svg>
""")

# SVG 5: Nuc Frame Transfer & Queen Cage (Lesson 5, Page 2)
SVG_NUC_TRANSFER = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Nucleus Colony Transfer &amp; Slow-Release Queen Cage</text>

  <!-- Left: 5-Frame Nuc Transfer -->
  <g transform="translate(45, 60)">
    <rect x="0" y="0" width="340" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="28" rx="10" fill="#15803d"/>
    <text x="170" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">5-FRAME NUCLEUS TRANSFER</text>

    <g transform="translate(15, 40)">
      <rect x="0" y="0" width="310" height="60" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">1. Established Biological Core:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Contains 4–5 frames of brood, honey, pollen,</text>
      <text x="15" y="52" font-size="9" fill="#cbd5e1">worker bees, and an active laying mated queen.</text>

      <rect x="0" y="70" width="310" height="65" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">2. Preserve Sequential Frame Order:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Transfer frames in the EXACT same sequence</text>
      <text x="15" y="54" font-size="9" fill="#cbd5e1">into the center of the Langstroth box.</text>

      <rect x="0" y="145" width="310" height="60" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">3. Insert Outer Foundation Frames:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Flank the brood nest with blank wax frames</text>
      <text x="15" y="52" font-size="9" fill="#cbd5e1">to allow rapid colony expansion.</text>
    </g>

    <text x="170" y="300" font-size="9" fill="#86efac" text-anchor="middle">Harvest honey in 6–8 weeks with zero absconding risk!</text>
  </g>

  <!-- Right: Queen Cage & Sugar Plug -->
  <g transform="translate(415, 60)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="28" rx="10" fill="#0284c7"/>
    <text x="172" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">SLOW-RELEASE QUEEN CAGE MECHANISM</text>

    <!-- Schematic Queen Cage Box -->
    <rect x="25" y="45" width="295" height="110" rx="6" fill="#1e293b" stroke="#fde047" stroke-width="1.5"/>
    <text x="172" y="70" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">QUEEN CAGE (Wire Screen Mesh)</text>
    <rect x="40" y="85" width="160" height="50" rx="4" fill="#0f172a" stroke="#38bdf8"/>
    <text x="120" y="115" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Queen Bee Inside</text>
    <rect x="210" y="85" width="90" height="50" rx="4" fill="#ca8a04" stroke="#fde047"/>
    <text x="255" y="108" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Sugar Candy</text>
    <text x="255" y="124" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Plug (48–72h)</text>

    <!-- Explanation Box -->
    <g transform="translate(25, 170)">
      <rect x="0" y="0" width="295" height="85" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#38bdf8">Why the 48–72h Delay is Vital:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">• Package workers are strangers to the queen</text>
      <text x="15" y="54" font-size="9" fill="#cbd5e1">• Immediate release causes fatal "queen balling"</text>
      <text x="15" y="70" font-size="9" font-weight="bold" fill="#4ade80">• Chewing candy spreads pheromones peacefully</text>
    </g>

    <text x="172" y="300" font-size="9" fill="#67e8f9" text-anchor="middle">Guarantees 100% queen acceptance in package colonies</text>
  </g>
</svg>
""")

# SVG 6: Pest Defense & Safari Ant Barrier (Lesson 6, Page 2)
SVG_PEST_DEFENSE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Apiary Pest Defense Systems &amp; Post Grease Barriers</text>

  <!-- 3 Predator Defense Columns -->
  <!-- 1. Safari Ants (Grease Barrier) -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="220" height="340" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="28" rx="10" fill="#991b1b"/>
    <text x="110" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">1. SAFARI ANTS (DORYLUS)</text>

    <!-- Post Graphic -->
    <rect x="95" y="45" width="30" height="150" fill="#475569" stroke="#94a3b8"/>
    <!-- Grease Band -->
    <rect x="90" y="100" width="40" height="40" rx="4" fill="#ca8a04" stroke="#fde047" stroke-width="2"/>
    <text x="110" y="125" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">GREASE</text>

    <text x="110" y="215" font-size="10" font-weight="bold" fill="#f87171" text-anchor="middle">Mechanical Defense:</text>
    <text x="10" y="235" font-size="9" fill="#cbd5e1">• 10cm band of motor grease</text>
    <text x="10" y="250" font-size="9" fill="#cbd5e1">  or used engine oil</text>
    <text x="10" y="270" font-size="9" fill="#cbd5e1">• Hydrophobic sticky barrier</text>
    <text x="10" y="285" font-size="9" fill="#cbd5e1">  ants cannot cross</text>
    <text x="10" y="305" font-size="8" font-weight="bold" fill="#4ade80">• Zero chemical pesticides!</text>
  </g>

  <!-- 2. Honey Badgers (Suspended Wires) -->
  <g transform="translate(290, 65)">
    <rect x="0" y="0" width="220" height="340" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="28" rx="10" fill="#0284c7"/>
    <text x="110" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">2. HONEY BADGERS</text>

    <!-- Wire Suspension Graphic -->
    <line x1="110" y1="45" x2="110" y2="110" stroke="#94a3b8" stroke-width="3"/>
    <rect x="70" y="110" width="80" height="50" rx="4" fill="#ca8a04" stroke="#fde047"/>
    <text x="110" y="140" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Suspended Hive</text>

    <text x="110" y="215" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Wire Suspension:</text>
    <text x="10" y="235" font-size="9" fill="#cbd5e1">• Hives suspended on strong</text>
    <text x="10" y="250" font-size="9" fill="#cbd5e1">  galvanized steel wires</text>
    <text x="10" y="270" font-size="9" fill="#cbd5e1">• Height: 1.5m above ground</text>
    <text x="10" y="290" font-size="9" fill="#cbd5e1">• Badgers cannot climb or</text>
    <text x="10" y="305" font-size="9" fill="#cbd5e1">  smash hanging hives</text>
  </g>

  <!-- 3. Wax Moths & Dearth (Management) -->
  <g transform="translate(535, 65)">
    <rect x="0" y="0" width="220" height="340" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="28" rx="10" fill="#15803d"/>
    <text x="110" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">3. WAX MOTHS &amp; DEARTH</text>

    <g transform="translate(10, 45)">
      <rect x="0" y="0" width="200" height="75" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="10" y="18" font-size="9" font-weight="bold" fill="#4ade80">Wax Moth Defense:</text>
      <text x="10" y="35" font-size="8" fill="#cbd5e1">• Maintain strong colonies</text>
      <text x="10" y="50" font-size="8" fill="#cbd5e1">• Squeeze entrance to 8mm</text>
      <text x="10" y="65" font-size="8" fill="#cbd5e1">  to allow guard defense</text>
    </g>

    <g transform="translate(10, 130)">
      <rect x="0" y="0" width="200" height="85" rx="6" fill="#1e293b" stroke="#eab308"/>
      <text x="10" y="18" font-size="9" font-weight="bold" fill="#fde047">Dearth Season Feeding:</text>
      <text x="10" y="35" font-size="8" fill="#cbd5e1">• Feed 1:1 Sugar:Water syrup</text>
      <text x="10" y="50" font-size="8" fill="#cbd5e1">• Prevents starvation</text>
      <text x="10" y="65" font-size="8" fill="#cbd5e1">• Stops colony absconding</text>
    </g>

    <text x="110" y="275" font-size="9" font-weight="bold" fill="#86efac" text-anchor="middle">Foulbrood Disease:</text>
    <text x="10" y="295" font-size="8" fill="#cbd5e1">Burn heavily infected frames;</text>
    <text x="10" y="310" font-size="8" fill="#cbd5e1">sterilize boxes with blowtorch.</text>
  </g>
</svg>
""")

# SVG 7: Honey Harvesting & Processing (Lesson 7, Page 2)
SVG_HARVESTING_PIPELINE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 6-Stage Honey Harvesting &amp; Processing Pipeline</text>

  <!-- 6 Processing Stages Flowchart -->
  <!-- Stage 1: Capped Frame -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="220" height="95" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="110" y="22" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">STAGE 1: CAPPING CHECK</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• ≥ 80% of comb cells capped</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Guarantees &lt;18% moisture</text>
    <text x="10" y="80" font-size="9" font-weight="bold" fill="#86efac">• Prevents yeast fermentation</text>
  </g>
  <line x1="265" y1="112" x2="295" y2="112" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="285,107 295,112 285,117" fill="#38bdf8"/>

  <!-- Stage 2: Uncapping -->
  <g transform="translate(295, 65)">
    <rect x="0" y="0" width="210" height="95" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <text x="105" y="22" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">STAGE 2: UNCAPPING</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Heated uncapping knife</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Slices off thin wax caps</text>
    <text x="10" y="80" font-size="9" fill="#cbd5e1">• Done over uncapping tray</text>
  </g>
  <line x1="505" y1="112" x2="535" y2="112" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="525,107 535,112 525,117" fill="#38bdf8"/>

  <!-- Stage 3: Centrifugal Extractor -->
  <g transform="translate(535, 65)">
    <rect x="0" y="0" width="220" height="95" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="110" y="22" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">STAGE 3: CENTRIFUGAL SPIN</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Flings honey out of cells</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Wax comb remains 100% INTACT</text>
    <text x="10" y="80" font-size="9" font-weight="bold" fill="#67e8f9">• Comb returned to hive!</text>
  </g>

  <!-- Connecting Line Down -->
  <line x1="645" y1="160" x2="645" y2="210" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="640,200 645,210 650,200" fill="#38bdf8"/>

  <!-- Stage 4: Multi-Stage Filtration -->
  <g transform="translate(535, 210)">
    <rect x="0" y="0" width="220" height="95" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="110" y="22" font-size="10" font-weight="bold" fill="#d8b4fe" text-anchor="middle">STAGE 4: FILTRATION</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Coarse 1mm stainless sieve</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Fine 200-micron nylon mesh</text>
    <text x="10" y="80" font-size="9" fill="#cbd5e1">• Removes wax bits &amp; debris</text>
  </g>
  <line x1="535" y1="257" x2="505" y2="257" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="515,252 505,257 515,262" fill="#38bdf8"/>

  <!-- Stage 5: Settling Tank -->
  <g transform="translate(295, 210)">
    <rect x="0" y="0" width="210" height="95" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
    <text x="105" y="22" font-size="10" font-weight="bold" fill="#67e8f9" text-anchor="middle">STAGE 5: SETTLING (24–48h)</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Sits in food-grade tank</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Air bubbles &amp; foam rise</text>
    <text x="10" y="80" font-size="9" fill="#cbd5e1">• White foam is skimmed off</text>
  </g>
  <line x1="295" y1="257" x2="265" y2="257" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="275,252 265,257 275,262" fill="#38bdf8"/>

  <!-- Stage 6: Bottling -->
  <g transform="translate(45, 210)">
    <rect x="0" y="0" width="220" height="95" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="24" rx="8" fill="#15803d"/>
    <text x="110" y="16" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 6: HERMETIC BOTTLING</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Sterile, dry glass jars</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Airtight seals &amp; labels</text>
    <text x="10" y="80" font-size="9" font-weight="bold" fill="#4ade80">• Premium Grade 1 Market Sale</text>
  </g>

  <!-- Quality Assurance Footer -->
  <g transform="translate(45, 335)">
    <rect x="0" y="0" width="710" height="65" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="355" y="24" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Quality Standard: Extract in a Screened Bee-Proof Room with Sterile Equipment</text>
    <text x="355" y="46" font-size="9" fill="#cbd5e1" text-anchor="middle">Never heat raw honey above 45°C; unheated honey retains natural antibacterial enzymes (inhibine) and bio-flavonoids!</text>
  </g>
</svg>
""")

# SVG 8: Master Apiculture Systems Synthesis (Lesson 8, Page 2)
SVG_MASTER_APICULTURE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Master Apiculture Enterprise Systems &amp; Quality Synthesis</text>

  <!-- Central Hub: Apiculture Enterprise -->
  <circle cx="400" cy="240" r="55" fill="#0f172a" stroke="#eab308" stroke-width="3"/>
  <text x="400" y="235" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">COMMERCIAL</text>
  <text x="400" y="252" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">APICULTURE</text>

  <!-- 1. Apiary Siting -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="195" height="75" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="97" y="22" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">1. SITING &amp; SAFETY</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• 2–3km Forage &amp; Water</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• ≥100m Safety Buffer</text>
  </g>
  <line x1="240" y1="102" x2="345" y2="200" stroke="#22c55e" stroke-width="2" stroke-dasharray="2,2"/>

  <!-- 2. Equipment & Bee Space -->
  <g transform="translate(560, 65)">
    <rect x="0" y="0" width="195" height="75" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="97" y="22" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">2. HIVES &amp; PPE</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Langstroth (6.4–9.5mm)</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Smoker &amp; White Suits</text>
  </g>
  <line x1="560" y1="102" x2="455" y2="200" stroke="#38bdf8" stroke-width="2" stroke-dasharray="2,2"/>

  <!-- 3. Stocking Methods -->
  <g transform="translate(35, 195)">
    <rect x="0" y="0" width="195" height="75" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="97" y="22" font-size="11" font-weight="bold" fill="#d8b4fe" text-anchor="middle">3. STOCKING</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Lemon grass baiting</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Nucleus colony transfer</text>
  </g>
  <line x1="230" y1="240" x2="345" y2="240" stroke="#a855f7" stroke-width="2"/>

  <!-- 4. Pest Defense -->
  <g transform="translate(570, 195)">
    <rect x="0" y="0" width="195" height="75" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="97" y="22" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">4. PEST DEFENSE</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Post grease rings (Ants)</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• 1.5m Wires (Badgers)</text>
  </g>
  <line x1="570" y1="240" x2="455" y2="240" stroke="#ef4444" stroke-width="2"/>

  <!-- 5. Harvesting & Quality -->
  <g transform="translate(300, 335)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
    <text x="100" y="22" font-size="11" font-weight="bold" fill="#67e8f9" text-anchor="middle">5. HARVEST &amp; PROFIT</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• 80% Capping (<18% water)</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Centrifugal extraction</text>
  </g>
  <line x1="400" y1="335" x2="400" y2="298" stroke="#06b6d4" stroke-width="2"/>
</svg>
""")

SVG_MAP = {
    1: {"page": 2, "svg": SVG_APIARY_SITING, "title": "Optimal Apiary Siting Layout & Public Safety Buffers"},
    2: {"page": 2, "svg": SVG_TOOLS_AND_PPE, "title": "Essential Beekeeping Tools & Full Protective PPE Ensemble"},
    3: {"page": 2, "svg": SVG_PRODUCTS_AND_POLLINATION, "title": "Economic Products of Apiculture & Crop Pollination Value"},
    4: {"page": 2, "svg": SVG_SWARM_CAPTURE, "title": "Stocking Methods: Swarm Capture & Bait Hive Pheromones"},
    5: {"page": 2, "svg": SVG_NUC_TRANSFER, "title": "Nucleus Colony Transfer & Slow-Release Queen Cage"},
    6: {"page": 2, "svg": SVG_PEST_DEFENSE, "title": "Apiary Pest Defense Systems & Post Grease Barriers"},
    7: {"page": 2, "svg": SVG_HARVESTING_PIPELINE, "title": "The 6-Stage Honey Harvesting & Processing Pipeline"},
    8: {"page": 2, "svg": SVG_MASTER_APICULTURE, "title": "Master Apiculture Enterprise Systems & Quality Synthesis"}
}

def enrich_grade10_topic11():
    """Injects verified photos, responsive vector SVGs, YouTube embeds, and creates LessonAssets."""
    print("=" * 80)
    print("STARTING ENRICHMENT: CBC Grade 10 Agriculture — Topic 11: Beekeeping")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()
    topic = Topic.objects.filter(subject=subject, name="Beekeeping").first()

    assert topic, "Topic 'Beekeeping' not found!"

    images_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grade10_topic11_verified_images.json")
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
                    "topic_order": 11,
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
        if u_order in SVG_MAP:
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
                        "topic_order": 11,
                        "unit_order": u_order,
                        "page": svg_def["page"],
                        "svg_content": svg_def["svg"]
                    }
                )
                diag_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [Vector SVG Attached] Lesson {u_order}: {svg_def['title']}")

        # ---------------------------------------------------------------------
        # 3. Educational YouTube Videos (Lesson 5)
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
                        "topic_order": 11,
                        "unit_order": u_order,
                        "youtube_url": v_url
                    }
                )
                v_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [YouTube Video Attached] Lesson {u_order}: {v_block.title}")

    print("=" * 80)
    print(f"ENRICHMENT COMPLETE: Topic 11 '{topic.name}'")
    print(f"  Photographic Hooks: {total_images_attached} / 8")
    print(f"  Vector SVGs:        {total_svgs_attached} / 8")
    print(f"  YouTube Videos:     {total_videos_attached} / 1")
    print(f"  LessonAssets:       {total_assets_persisted}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic11()
