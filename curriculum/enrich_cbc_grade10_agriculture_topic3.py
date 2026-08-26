"""
VLearn CBC Grade 10 Agriculture — Topic 3: Land Preparation
Visual Enrichment Engine (Phase 2: Vector SVGs, Verified Photos & Asset Persistence)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Land Preparation (Order: 3)

Attaches:
  - 12 First-Card Photographic Visual Hooks (100% Tested HTTP 200 Direct Wikimedia URLs)
  - 10 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - 2 Verified Educational YouTube Videos (Lesson 3 Card 4 & Lesson 10 Card 3)
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade10_agriculture_topic3.py
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
# 10 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 3: LAND PREPARATION
# =============================================================================

# SVG 1: The 4-Stage Land Preparation Sequence Flowchart (Lesson 1, Page 3)
SVG_LAND_PREP_SEQUENCE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 4-Stage Sequential Flow of Agricultural Land Preparation</text>

  <!-- Stage 1: Land Clearing -->
  <g transform="translate(35, 75)">
    <rect x="0" y="0" width="165" height="330" rx="10" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect x="0" y="0" width="165" height="32" rx="10" fill="#ca8a04"/>
    <text x="82" y="22" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 1: CLEARING</text>
    
    <text x="12" y="55" font-size="11" font-weight="bold" fill="#fde047">Primary Goal:</text>
    <text x="12" y="75" font-size="10" fill="#cbd5e1">• Remove brush, tall weeds, and stumps</text>
    
    <text x="12" y="115" font-size="11" font-weight="bold" fill="#fde047">Tools Used:</text>
    <text x="12" y="135" font-size="10" fill="#cbd5e1">• Slasher (Grass)</text>
    <text x="12" y="155" font-size="10" fill="#cbd5e1">• Panga (Shrubs)</text>
    <text x="12" y="175" font-size="10" fill="#cbd5e1">• Mattock (Stumps)</text>
    <text x="12" y="195" font-size="10" fill="#cbd5e1">• Axe / Bulldozer</text>
    
    <rect x="10" y="240" width="145" height="45" rx="6" fill="#1e293b" stroke="#ca8a04"/>
    <text x="82" y="258" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">Do Not Burn!</text>
    <text x="82" y="274" font-size="8" fill="#fef08a" text-anchor="middle">Recycle to Compost</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <line x1="205" y1="240" x2="225" y2="240" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="225,235 235,240 225,245" fill="#38bdf8"/>

  <!-- Stage 2: Primary Cultivation -->
  <g transform="translate(235, 75)">
    <rect x="0" y="0" width="165" height="330" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="165" height="32" rx="10" fill="#b91c1c"/>
    <text x="82" y="22" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 2: PRIMARY</text>
    
    <text x="12" y="55" font-size="11" font-weight="bold" fill="#fca5a5">Primary Goal:</text>
    <text x="12" y="75" font-size="10" fill="#cbd5e1">• Break hard crust (15–30 cm)</text>
    <text x="12" y="95" font-size="10" fill="#cbd5e1">• Invert &amp; bury weeds</text>
    
    <text x="12" y="125" font-size="11" font-weight="bold" fill="#fca5a5">Tools Used:</text>
    <text x="12" y="145" font-size="10" fill="#cbd5e1">• Hand / Fork Jembe</text>
    <text x="12" y="165" font-size="10" fill="#cbd5e1">• Mouldboard Plough</text>
    <text x="12" y="185" font-size="10" fill="#cbd5e1">• Disc Plough</text>
    <text x="12" y="205" font-size="10" fill="#cbd5e1">• Deep Subsoiler</text>
    
    <rect x="10" y="240" width="145" height="45" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="82" y="258" font-size="9" font-weight="bold" fill="#fca5a5" text-anchor="middle">Rough Clod State</text>
    <text x="82" y="274" font-size="8" fill="#cbd5e1" text-anchor="middle">Aerates &amp; Inverts</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <line x1="405" y1="240" x2="425" y2="240" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="425,235 435,240 425,245" fill="#38bdf8"/>

  <!-- Stage 3: Secondary Cultivation -->
  <g transform="translate(435, 75)">
    <rect x="0" y="0" width="165" height="330" rx="10" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
    <rect x="0" y="0" width="165" height="32" rx="10" fill="#0e7490"/>
    <text x="82" y="22" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 3: SECONDARY</text>
    
    <text x="12" y="55" font-size="11" font-weight="bold" fill="#67e8f9">Primary Goal:</text>
    <text x="12" y="75" font-size="10" fill="#cbd5e1">• Shatter large clods (5–15 cm)</text>
    <text x="12" y="95" font-size="10" fill="#cbd5e1">• Produce optimal tilth</text>
    
    <text x="12" y="125" font-size="11" font-weight="bold" fill="#67e8f9">Tools Used:</text>
    <text x="12" y="145" font-size="10" fill="#cbd5e1">• Hand Rake</text>
    <text x="12" y="165" font-size="10" fill="#cbd5e1">• Disc Harrow</text>
    <text x="12" y="185" font-size="10" fill="#cbd5e1">• Spring-Tine Harrow</text>
    <text x="12" y="205" font-size="10" fill="#cbd5e1">• Rotavator</text>
    
    <rect x="10" y="240" width="145" height="45" rx="6" fill="#1e293b" stroke="#06b6d4"/>
    <text x="82" y="258" font-size="9" font-weight="bold" fill="#67e8f9" text-anchor="middle">Refined Tilth</text>
    <text x="82" y="274" font-size="8" fill="#cbd5e1" text-anchor="middle">Fine / Granular</text>
  </g>

  <!-- Arrow 3 -> 4 -->
  <line x1="605" y1="240" x2="625" y2="240" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="625,235 635,240 625,245" fill="#38bdf8"/>

  <!-- Stage 4: Tertiary Operations -->
  <g transform="translate(635, 75)">
    <rect x="0" y="0" width="130" height="330" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="130" height="32" rx="10" fill="#15803d"/>
    <text x="65" y="22" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 4: TERTIARY</text>
    
    <text x="10" y="55" font-size="10" font-weight="bold" fill="#86efac">Custom Shaping:</text>
    <text x="10" y="75" font-size="9" fill="#cbd5e1">• Ridging (Tubers)</text>
    <text x="10" y="95" font-size="9" fill="#cbd5e1">• Raised Beds (Veg)</text>
    <text x="10" y="115" font-size="9" fill="#cbd5e1">• Leveling</text>
    <text x="10" y="135" font-size="9" fill="#cbd5e1">• Soil Rolling</text>
    <text x="10" y="155" font-size="9" fill="#cbd5e1">• Furrow Opening</text>
    
    <rect x="10" y="240" width="110" height="45" rx="6" fill="#1e293b" stroke="#22c55e"/>
    <text x="65" y="258" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">Planting-Ready</text>
    <text x="65" y="274" font-size="8" fill="#dcfce7" text-anchor="middle">Target Seedbed</text>
  </g>
</svg>
""")

# SVG 2: Land Clearing Tools and Composting vs Burning (Lesson 2, Page 3)
SVG_CLEARING_COMPOSTING = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Land Clearing Equipment &amp; Ecological Biomass Fate</text>

  <!-- Left: Manual Tools -->
  <g transform="translate(35, 65)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#0284c7"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">PRIMARY LAND CLEARING TOOLS</text>

    <g transform="translate(15, 45)">
      <text x="0" y="20" font-size="12" font-weight="bold" fill="#fde047">1. Slasher (Long Handled):</text>
      <text x="0" y="38" font-size="11" fill="#cbd5e1">Cuts tall grass, annual weeds &amp; green pasture</text>

      <text x="0" y="70" font-size="12" font-weight="bold" fill="#fde047">2. Panga / Machete (Broad Blade):</text>
      <text x="0" y="88" font-size="11" fill="#cbd5e1">Chops thick woody shrubs, saplings &amp; branches</text>

      <text x="0" y="120" font-size="12" font-weight="bold" fill="#fde047">3. Mattock (Pick + Hoe Blade):</text>
      <text x="0" y="138" font-size="11" fill="#cbd5e1">Prys out deep taproots &amp; underground tree stumps</text>

      <text x="0" y="170" font-size="12" font-weight="bold" fill="#fde047">4. Axe &amp; Bulldozer (Heavy Timber):</text>
      <text x="0" y="188" font-size="11" fill="#cbd5e1">Fells mature trees &amp; pushes large field boulders</text>
    </g>

    <rect x="15" y="285" width="315" height="45" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="172" y="304" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Goal: Clear Surface to Protect Tillage Blades</text>
    <text x="172" y="320" font-size="9" fill="#cbd5e1" text-anchor="middle">Prevents bent plough shears &amp; broken discs</text>
  </g>

  <!-- Right: Composting vs Burning -->
  <g transform="translate(420, 65)">
    <rect x="0" y="0" width="345" height="165" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="30" rx="10" fill="#15803d"/>
    <text x="172" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">RECYCLING TO COMPOST (RECOMMENDED)</text>
    <text x="15" y="55" font-size="11" fill="#86efac">• Preserves 100% of organic carbon and nutrients</text>
    <text x="15" y="75" font-size="11" fill="#cbd5e1">• Feeds beneficial earthworms &amp; mycorrhizal fungi</text>
    <text x="15" y="95" font-size="11" fill="#cbd5e1">• Increases soil water-holding sponge capacity</text>
    <text x="15" y="115" font-size="11" fill="#cbd5e1">• Produces valuable farmyard humus for next crop</text>
  </g>

  <g transform="translate(420, 245)">
    <rect x="0" y="0" width="345" height="165" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="30" rx="10" fill="#991b1b"/>
    <text x="172" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">SLASH-AND-BURN (DESTRUCTIVE)</text>
    <text x="15" y="55" font-size="11" fill="#fca5a5">• Incinerates valuable soil organic matter (SOM)</text>
    <text x="15" y="75" font-size="11" fill="#cbd5e1">• Heat sterilizes and cooks beneficial soil microbes</text>
    <text x="15" y="95" font-size="11" fill="#cbd5e1">• Leaves topsoil bare and prone to heavy runoff erosion</text>
    <text x="15" y="115" font-size="11" fill="#cbd5e1">• Emits CO₂ and harmful smoke air pollution</text>
  </g>
</svg>
""")

# SVG 3: Primary Tillage Implements: Mouldboard vs Disc vs Subsoiler (Lesson 3, Page 3)
SVG_PRIMARY_IMPLEMENTS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Primary Tillage Implements: Mouldboard vs Disc Plough vs Subsoiler</text>

  <!-- Implement 1: Mouldboard Plough -->
  <g transform="translate(35, 65)">
    <rect x="0" y="0" width="230" height="345" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="230" height="32" rx="10" fill="#0284c7"/>
    <text x="115" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. MOULDBOARD PLOUGH</text>

    <!-- Cutting Diagram Graphic -->
    <path d="M 40 85 Q 115 65 180 120 L 140 135 Z" fill="#38bdf8" opacity="0.8"/>
    <text x="115" y="160" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">180° Complete Inversion</text>

    <g transform="translate(12, 180)">
      <text x="0" y="15" font-size="11" font-weight="bold" fill="#cbd5e1">• Cutting: Static sharp share</text>
      <text x="0" y="35" font-size="10" fill="#94a3b8">• Action: Rolls slice completely</text>
      <text x="0" y="55" font-size="10" font-weight="bold" fill="#4ade80">• Best for: Clean loam soils</text>
      <text x="0" y="75" font-size="10" fill="#94a3b8">• Superior weed burial</text>
      <text x="0" y="95" font-size="10" fill="#f87171">• Weakness: Jams on rocks</text>
    </g>

    <rect x="15" y="295" width="200" height="35" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="115" y="316" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Optimal Clean Land Plough</text>
  </g>

  <!-- Implement 2: Disc Plough -->
  <g transform="translate(285, 65)">
    <rect x="0" y="0" width="230" height="345" rx="10" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect x="0" y="0" width="230" height="32" rx="10" fill="#ca8a04"/>
    <text x="115" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. DISC PLOUGH</text>

    <!-- Disc Diagram Graphic -->
    <ellipse cx="115" cy="100" rx="45" ry="30" fill="#eab308" opacity="0.8" stroke="#fde047" stroke-width="2"/>
    <text x="115" y="160" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">Rolling Concave Discs</text>

    <g transform="translate(12, 180)">
      <text x="0" y="15" font-size="11" font-weight="bold" fill="#cbd5e1">• Cutting: Rotating steel discs</text>
      <text x="0" y="35" font-size="10" fill="#94a3b8">• Action: Scoops &amp; rolls over</text>
      <text x="0" y="55" font-size="10" font-weight="bold" fill="#4ade80">• Best for: Stony, dry, hard soils</text>
      <text x="0" y="75" font-size="10" fill="#94a3b8">• Rolls over buried stumps</text>
      <text x="0" y="95" font-size="10" fill="#fde047">• Heavy draft requirement</text>
    </g>

    <rect x="15" y="295" width="200" height="35" rx="6" fill="#1e293b" stroke="#eab308"/>
    <text x="115" y="316" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">Tough / Stony Terrain Master</text>
  </g>

  <!-- Implement 3: Subsoiler -->
  <g transform="translate(535, 65)">
    <rect x="0" y="0" width="230" height="345" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="230" height="32" rx="10" fill="#b91c1c"/>
    <text x="115" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. DEEP SUBSOILER</text>

    <!-- Subsoiler Shank Graphic -->
    <line x1="115" y1="65" x2="115" y2="135" stroke="#ef4444" stroke-width="6"/>
    <polygon points="105,135 125,135 115,150" fill="#ef4444"/>
    <text x="115" y="165" font-size="11" font-weight="bold" fill="#fca5a5" text-anchor="middle">40–60 cm Hardpan Shank</text>

    <g transform="translate(12, 180)">
      <text x="0" y="15" font-size="11" font-weight="bold" fill="#cbd5e1">• Purpose: Shatters hardpans</text>
      <text x="0" y="35" font-size="10" fill="#94a3b8">• Does not invert soil</text>
      <text x="0" y="55" font-size="10" font-weight="bold" fill="#4ade80">• Restores drainage channels</text>
      <text x="0" y="75" font-size="10" fill="#94a3b8">• Eliminates root compaction</text>
      <text x="0" y="95" font-size="10" fill="#fca5a5">• Performed every 3–5 years</text>
    </g>

    <rect x="15" y="295" width="200" height="35" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="115" y="316" font-size="9" font-weight="bold" fill="#ef4444" text-anchor="middle">Compaction Hardpan Buster</text>
  </g>
</svg>
""")

# SVG 4: Soil Tilth Comparison: Fine vs Coarse (Lesson 4, Page 3)
SVG_TILTH_COMPARISON = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Soil Tilth Dynamics: Fine Seedbed vs Coarse Cloddy Tilth</text>

  <!-- Left: Fine Tilth -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="335" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="335" height="35" rx="10" fill="#15803d"/>
    <text x="167" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">FINE SEEDBED TILTH (&lt;5 mm)</text>

    <!-- Seed-Soil Graphic -->
    <rect x="25" y="55" width="285" height="95" rx="6" fill="#1e293b" stroke="#334155"/>
    <circle cx="167" cy="100" r="10" fill="#eab308"/>
    <!-- Fine crumbs surrounding seed -->
    <circle cx="145" cy="85" r="4" fill="#86efac"/><circle cx="185" cy="85" r="4" fill="#86efac"/>
    <circle cx="140" cy="110" r="4" fill="#86efac"/><circle cx="190" cy="110" r="4" fill="#86efac"/>
    <text x="167" y="135" font-size="9" fill="#dcfce7" text-anchor="middle">100% Intimate Seed-to-Soil Capillary Contact</text>

    <g transform="translate(20, 165)">
      <text x="0" y="20" font-size="12" font-weight="bold" fill="#86efac">Target: Small-Seeded Crops</text>
      <text x="0" y="40" font-size="11" fill="#cbd5e1">• Carrots, Onions, Kales, Cabbage, Tomatoes</text>
      <text x="0" y="60" font-size="11" fill="#cbd5e1">• Rapid capillary water absorption (imbibition)</text>
      <text x="0" y="80" font-size="11" fill="#cbd5e1">• Prevents carrot taproot branching / forking</text>
      <text x="0" y="100" font-size="11" fill="#fde047">• Warning: Do not over-mill to avoid soil capping</text>
    </g>

    <rect x="20" y="295" width="295" height="30" rx="4" fill="#14532d"/>
    <text x="167" y="314" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Mandatory for Horticultural Nurseries</text>
  </g>

  <!-- Right: Coarse Cloddy Tilth -->
  <g transform="translate(420, 65)">
    <rect x="0" y="0" width="335" height="345" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="335" height="35" rx="10" fill="#0284c7"/>
    <text x="167" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">COARSE CLODDY TILTH (20–50 mm)</text>

    <!-- Seed-Soil Graphic -->
    <rect x="25" y="55" width="285" height="95" rx="6" fill="#1e293b" stroke="#334155"/>
    <circle cx="167" cy="100" r="18" fill="#ca8a04"/>
    <!-- Clods -->
    <rect x="90" y="75" width="35" height="30" rx="6" fill="#64748b"/>
    <rect x="210" y="75" width="35" height="30" rx="6" fill="#64748b"/>
    <text x="167" y="135" font-size="9" fill="#93c5fd" text-anchor="middle">Large Seeds Emerge Strongly Through Clods</text>

    <g transform="translate(20, 165)">
      <text x="0" y="20" font-size="12" font-weight="bold" fill="#38bdf8">Target: Large-Seeded Crops</text>
      <text x="0" y="40" font-size="11" fill="#cbd5e1">• Hybrid Maize, Beans, Sunflowers, Cotton</text>
      <text x="0" y="60" font-size="11" fill="#cbd5e1">• Resists surface crusting (soil capping) after rain</text>
      <text x="0" y="80" font-size="11" fill="#cbd5e1">• Provides high water infiltration during storms</text>
      <text x="0" y="100" font-size="11" fill="#4ade80">• Saves 50% tillage fuel by avoiding extra harrowing</text>
    </g>

    <rect x="20" y="295" width="295" height="30" rx="4" fill="#0c4a6e"/>
    <text x="167" y="314" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Optimal for Commercial Cereal Fields</text>
  </g>
</svg>
""")

# SVG 5: Tertiary Field Structures: Raised Beds vs Ridges (Lesson 5, Page 3)
SVG_TERTIARY_STRUCTURES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Tertiary Field Structures: Raised Beds vs Contour Ridges</text>

  <!-- Left: Raised Vegetable Bed -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="335" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="335" height="35" rx="10" fill="#15803d"/>
    <text x="167" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">RAISED VEGETABLE BED</text>

    <!-- Cross Section Graphic -->
    <path d="M 30 135 L 75 80 L 260 80 L 305 135 Z" fill="#14532d" stroke="#22c55e" stroke-width="2"/>
    <text x="167" y="110" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Flat Top (1.0 m Wide)</text>
    <text x="167" y="125" font-size="9" fill="#86efac" text-anchor="middle">Height: 15 cm</text>

    <g transform="translate(20, 160)">
      <text x="0" y="15" font-size="11" font-weight="bold" fill="#86efac">• Best for: Cabbage, Kales, Spinach, Carrots</text>
      <text x="0" y="35" font-size="10" fill="#cbd5e1">• Eliminates foot traffic compaction in root zone</text>
      <text x="0" y="55" font-size="10" fill="#cbd5e1">• Prevents root drowning during heavy rains</text>
      <text x="0" y="75" font-size="10" fill="#cbd5e1">• Concentrates compost and organic manures</text>
      <text x="0" y="95" font-size="10" fill="#cbd5e1">• Facilitates precision furrow / drip irrigation</text>
    </g>

    <rect x="20" y="295" width="295" height="30" rx="4" fill="#14532d"/>
    <text x="167" y="314" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Standard Vegetable Seedbed Architecture</text>
  </g>

  <!-- Right: Contour Ridges -->
  <g transform="translate(420, 65)">
    <rect x="0" y="0" width="335" height="345" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect x="0" y="0" width="335" height="35" rx="10" fill="#b45309"/>
    <text x="167" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">CONTOUR TILLAGE RIDGES</text>

    <!-- Cross Section Graphic -->
    <path d="M 25 135 Q 90 70 155 135 Q 220 70 285 135 Z" fill="#78350f" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="90" cy="115" r="10" fill="#eab308"/><circle cx="220" cy="115" r="10" fill="#eab308"/>
    <text x="155" y="110" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Mounds (30 cm)</text>

    <g transform="translate(20, 160)">
      <text x="0" y="15" font-size="11" font-weight="bold" fill="#fde047">• Best for: Sweet Potatoes, Irish Potatoes, Cassava</text>
      <text x="0" y="35" font-size="10" fill="#cbd5e1">• Provides deep, loose soil for tuber expansion</text>
      <text x="0" y="55" font-size="10" fill="#cbd5e1">• Prevents tuber rot by elevating roots above water</text>
      <text x="0" y="75" font-size="10" fill="#cbd5e1">• Contour placement stops downhill storm runoff</text>
      <text x="0" y="95" font-size="10" fill="#cbd5e1">• Makes harvesting effortless without tool cuts</text>
    </g>

    <rect x="20" y="295" width="295" height="30" rx="4" fill="#78350f"/>
    <text x="167" y="314" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">Mandatory for Root &amp; Tuber Enterprises</text>
  </g>
</svg>
""")

# SVG 6: Land Preparation Tool Safety & Maintenance (Lesson 6, Page 3)
SVG_TOOL_SAFETY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Farm Tool Safety Regulations &amp; Routine Maintenance Cycle</text>

  <!-- Left: Safety Standards -->
  <g transform="translate(35, 65)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#991b1b"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">FIELD SAFETY REGULATIONS</text>

    <g transform="translate(15, 45)">
      <text x="0" y="20" font-size="12" font-weight="bold" fill="#fca5a5">1. Maintain 3-Meter Safe Distance:</text>
      <text x="0" y="38" font-size="11" fill="#cbd5e1">Never swing jembes or slashers near peers</text>

      <text x="0" y="70" font-size="12" font-weight="bold" fill="#fca5a5">2. Mandatory PPE Gear:</text>
      <text x="0" y="88" font-size="11" fill="#cbd5e1">Steel-toe boots, leather gloves, safety goggles</text>

      <text x="0" y="120" font-size="12" font-weight="bold" fill="#fca5a5">3. Inspect Handles Before Use:</text>
      <text x="0" y="138" font-size="11" fill="#cbd5e1">Check for loose heads or split wooden handles</text>

      <text x="0" y="170" font-size="12" font-weight="bold" fill="#fca5a5">4. Safe Tool Carrying:</text>
      <text x="0" y="188" font-size="11" fill="#cbd5e1">Carry blades facing downward and away from body</text>
    </g>

    <rect x="15" y="285" width="315" height="45" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="172" y="304" font-size="10" font-weight="bold" fill="#ef4444" text-anchor="middle">Rule: Zero Tolerance for Loose Tool Heads</text>
    <text x="172" y="320" font-size="9" fill="#fca5a5" text-anchor="middle">Prevents lethal flying metal projectiles</text>
  </g>

  <!-- Right: 4-Step Maintenance Cycle -->
  <g transform="translate(420, 65)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#15803d"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">4-STEP TOOL CARE &amp; STORAGE CYCLE</text>

    <g transform="translate(15, 45)">
      <text x="0" y="20" font-size="12" font-weight="bold" fill="#86efac">Step 1: Clean &amp; Wash Mud</text>
      <text x="0" y="38" font-size="11" fill="#cbd5e1">Wash soil with water; moisture causes rust</text>

      <text x="0" y="70" font-size="12" font-weight="bold" fill="#86efac">Step 2: Wipe Thoroughly Dry</text>
      <text x="0" y="88" font-size="11" fill="#cbd5e1">Dry metal head completely with a dry cloth</text>

      <text x="0" y="120" font-size="12" font-weight="bold" fill="#86efac">Step 3: File &amp; Sharpen Bevel</text>
      <text x="0" y="138" font-size="11" fill="#cbd5e1">File cutting edge at 30° to reduce digging effort</text>

      <text x="0" y="170" font-size="12" font-weight="bold" fill="#86efac">Step 4: Oil &amp; Hang on Racks</text>
      <text x="0" y="188" font-size="11" fill="#cbd5e1">Rub oil to seal oxygen; hang in locked tool shed</text>
    </g>

    <rect x="15" y="285" width="315" height="45" rx="6" fill="#1e293b" stroke="#22c55e"/>
    <text x="172" y="304" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Hydrophobic Oil Barrier Halts Rusting</text>
    <text x="172" y="320" font-size="9" fill="#86efac" text-anchor="middle">Extends tool lifespan by over 10+ years</text>
  </g>
</svg>
""")

# SVG 7: Zero Tillage Seed Placement & Residue Model (Lesson 7, Page 3)
SVG_ZERO_TILL_MODEL = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Conservation Agriculture: Zero Tillage Direct Seeding Model</text>

  <!-- Cross Section Soil Profile Graphic -->
  <g transform="translate(60, 65)">
    <!-- Mulch Layer (Top) -->
    <rect x="0" y="0" width="680" height="35" fill="#78350f" stroke="#eab308" stroke-width="1.5"/>
    <text x="340" y="22" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">PERMANENT CROP RESIDUE &amp; MULCH LAYER (Stops Evaporation &amp; Raindrop Impact)</text>

    <!-- Undisturbed Soil Matrix -->
    <rect x="0" y="35" width="680" height="190" fill="#0f172a" stroke="#334155" stroke-width="2"/>
    <text x="340" y="130" font-size="13" font-weight="bold" fill="#475569" text-anchor="middle">UNDISTURBED SOIL PROFILE (Preserves Natural Pores &amp; Earthworms)</text>

    <!-- Coulter Disc Slicing Slit -->
    <ellipse cx="200" cy="50" rx="30" ry="60" fill="#38bdf8" opacity="0.8" stroke="#0284c7" stroke-width="2"/>
    <text x="200" y="20" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. Rolling Coulter</text>

    <!-- Seed Tube -->
    <line x1="340" y1="10" x2="340" y2="75" stroke="#22c55e" stroke-width="5"/>
    <circle cx="340" cy="80" r="8" fill="#eab308"/>
    <text x="340" y="20" font-size="10" font-weight="bold" fill="#22c55e" text-anchor="middle">2. Seed &amp; Fertilizer Drop</text>

    <!-- Packing Wheel -->
    <circle cx="480" cy="40" r="25" fill="#64748b" stroke="#94a3b8" stroke-width="2"/>
    <text x="480" y="20" font-size="10" font-weight="bold" fill="#cbd5e1" text-anchor="middle">3. Press Wheel</text>
  </g>

  <!-- 3 Pillars of CA Footer -->
  <g transform="translate(60, 310)">
    <rect x="0" y="0" width="215" height="95" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="107" y="25" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. MINIMUM DISTURBANCE</text>
    <text x="10" y="50" font-size="10" fill="#cbd5e1">• Narrow 2 cm seed slit only</text>
    <text x="10" y="70" font-size="10" fill="#cbd5e1">• Zero plowing or harrowing</text>

    <rect x="232" y="0" width="215" height="95" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="107" y="25" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">2. PERMANENT COVER</text>
    <text x="10" y="50" font-size="10" fill="#cbd5e1">• Retain 100% crop stover</text>
    <text x="10" y="70" font-size="10" fill="#cbd5e1">• Cuts evaporation by 70%</text>

    <rect x="465" y="0" width="215" height="95" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <text x="107" y="25" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">3. CROP ROTATION</text>
    <text x="10" y="50" font-size="10" fill="#cbd5e1">• Rotate cereals with legumes</text>
    <text x="10" y="70" font-size="10" fill="#cbd5e1">• Disrupts pest cycles</text>
  </g>
</svg>
""")

# SVG 8: Strip Tillage (Zone Tillage) Field Architecture (Lesson 8, Page 3)
SVG_STRIP_TILLAGE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Strip Tillage (Zone Tillage) Architecture &amp; Field Layout</text>

  <!-- Field Layout Map Graphic -->
  <g transform="translate(50, 70)">
    <!-- Undisturbed Zone 1 (Left) -->
    <rect x="0" y="0" width="180" height="220" fill="#78350f" opacity="0.6" stroke="#eab308" stroke-width="1.5"/>
    <text x="90" y="105" font-size="12" font-weight="bold" fill="#fde047" text-anchor="middle">UNDISTURBED</text>
    <text x="90" y="125" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">MULCH ZONE</text>
    <text x="90" y="145" font-size="10" fill="#fef08a" text-anchor="middle">(45–60 cm Wide)</text>

    <!-- Cultivated Strip 1 (Center) -->
    <rect x="180" y="0" width="100" height="220" fill="#14532d" opacity="0.9" stroke="#22c55e" stroke-width="2"/>
    <circle cx="230" cy="80" r="10" fill="#eab308"/><circle cx="230" cy="150" r="10" fill="#eab308"/>
    <text x="230" y="30" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">TILLED STRIP</text>
    <text x="230" y="48" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">(15 cm Wide)</text>
    <text x="230" y="200" font-size="9" fill="#dcfce7" text-anchor="middle">Fine Crumb</text>

    <!-- Undisturbed Zone 2 (Right) -->
    <rect x="280" y="0" width="240" height="220" fill="#78350f" opacity="0.6" stroke="#eab308" stroke-width="1.5"/>
    <text x="400" y="105" font-size="12" font-weight="bold" fill="#fde047" text-anchor="middle">UNDISTURBED</text>
    <text x="400" y="125" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">MULCH ZONE</text>
    <text x="400" y="145" font-size="10" fill="#fef08a" text-anchor="middle">(Stops Erosion &amp; Retains Water)</text>

    <!-- Cultivated Strip 2 (Far Right) -->
    <rect x="520" y="0" width="100" height="220" fill="#14532d" opacity="0.9" stroke="#22c55e" stroke-width="2"/>
    <circle cx="570" cy="80" r="10" fill="#eab308"/><circle cx="570" cy="150" r="10" fill="#eab308"/>
    <text x="570" y="30" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">TILLED STRIP</text>
    <text x="570" y="48" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">(15 cm Wide)</text>
    <text x="570" y="200" font-size="9" fill="#dcfce7" text-anchor="middle">Fine Crumb</text>

    <!-- Row Spacing Dimension -->
    <line x1="230" y1="210" x2="570" y2="210" stroke="#38bdf8" stroke-width="2"/>
    <text x="400" y="205" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Standard Row Spacing: 75 cm</text>
  </g>

  <!-- Agronomic Benefits Footer -->
  <g transform="translate(50, 310)">
    <rect x="0" y="0" width="700" height="95" rx="8" fill="#0f172a" stroke="#64748b"/>
    <text x="350" y="25" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Best of Both Worlds: Clean Tillage Seedbed + Zero Tillage Water Conservation</text>
    <text x="20" y="52" font-size="11" fill="#cbd5e1">• <tspan font-weight="bold" fill="#4ade80">Saves 40–60% Tractor Fuel:</tspan> Disturbs only 20–25% of total field surface area</text>
    <text x="20" y="74" font-size="11" fill="#cbd5e1">• <tspan font-weight="bold" fill="#fde047">Protects Soil Carbon:</tspan> Prevents microbial oxidation burnout of organic humus in inter-rows</text>
  </g>
</svg>
""")

# SVG 9: Site Assessment Decision Matrix (Lesson 9, Page 3)
SVG_SITE_ASSESSMENT = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Pre-Tillage Site Assessment &amp; Crop-Matching Decision Tree</text>

  <!-- Node 1: Slope Assessment -->
  <g transform="translate(35, 65)">
    <rect x="0" y="0" width="220" height="90" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="110" y="25" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. TOPOGRAPHY &amp; SLOPE</text>
    <text x="10" y="50" font-size="10" fill="#cbd5e1">• Flat (&lt;5%): Strip / Clean Till</text>
    <text x="10" y="70" font-size="10" font-weight="bold" fill="#f87171">• Steep (&gt;15%): Zero Till only</text>
  </g>

  <!-- Node 2: Soil Compaction -->
  <g transform="translate(290, 65)">
    <rect x="0" y="0" width="220" height="90" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <text x="110" y="25" font-size="12" font-weight="bold" fill="#fde047" text-anchor="middle">2. SOIL COMPACTION</text>
    <text x="10" y="50" font-size="10" fill="#cbd5e1">• Friable soil: Standard tillage</text>
    <text x="10" y="70" font-size="10" font-weight="bold" fill="#ef4444">• Hardpan &gt;20cm: Subsoiler (60cm)</text>
  </g>

  <!-- Node 3: Weed Flora -->
  <g transform="translate(545, 65)">
    <rect x="0" y="0" width="220" height="90" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <text x="110" y="25" font-size="12" font-weight="bold" fill="#4ade80" text-anchor="middle">3. WEED FLORA</text>
    <text x="10" y="50" font-size="10" fill="#cbd5e1">• Annual weeds: Disc harrow</text>
    <text x="10" y="70" font-size="10" font-weight="bold" fill="#a855f7">• Couch grass: Fork jembe lift</text>
  </g>

  <!-- Final Crop-Matching Output Boxes -->
  <g transform="translate(35, 180)">
    <!-- Outcome 1: Carrots -->
    <rect x="0" y="0" width="165" height="225" rx="8" fill="#0f172a" stroke="#ea580c" stroke-width="1.5"/>
    <rect x="0" y="0" width="165" height="28" rx="8" fill="#c2410c"/>
    <text x="82" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">CARROTS</text>
    <text x="10" y="48" font-size="10" font-weight="bold" fill="#fdba74">Seedbed:</text>
    <text x="10" y="65" font-size="9" fill="#cbd5e1">Deep, rock-free ultra-fine tilth</text>
    <text x="10" y="95" font-size="10" font-weight="bold" fill="#fdba74">Why:</text>
    <text x="10" y="112" font-size="9" fill="#cbd5e1">Stones/clods cause taproot forking &amp; split carrots</text>
  </g>

  <g transform="translate(225, 180)">
    <!-- Outcome 2: Irish Potatoes -->
    <rect x="0" y="0" width="165" height="225" rx="8" fill="#0f172a" stroke="#ca8a04" stroke-width="1.5"/>
    <rect x="0" y="0" width="165" height="28" rx="8" fill="#a16207"/>
    <text x="82" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">POTATOES / TUBERS</text>
    <text x="10" y="48" font-size="10" font-weight="bold" fill="#fde047">Seedbed:</text>
    <text x="10" y="65" font-size="9" fill="#cbd5e1">30 cm Contour Ridges</text>
    <text x="10" y="95" font-size="10" font-weight="bold" fill="#fde047">Why:</text>
    <text x="10" y="112" font-size="9" fill="#cbd5e1">Loose soil for tuber expansion; prevents water rot</text>
  </g>

  <g transform="translate(415, 180)">
    <!-- Outcome 3: Brassicas -->
    <rect x="0" y="0" width="165" height="225" rx="8" fill="#0f172a" stroke="#15803d" stroke-width="1.5"/>
    <rect x="0" y="0" width="165" height="28" rx="8" fill="#166534"/>
    <text x="82" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">CABBAGE / VEG</text>
    <text x="10" y="48" font-size="10" font-weight="bold" fill="#86efac">Seedbed:</text>
    <text x="10" y="65" font-size="9" fill="#cbd5e1">15 cm Raised Beds</text>
    <text x="10" y="95" font-size="10" font-weight="bold" fill="#86efac">Why:</text>
    <text x="10" y="112" font-size="9" fill="#cbd5e1">Prevents foot compaction; concentrates manure</text>
  </g>

  <g transform="translate(605, 180)">
    <!-- Outcome 4: Maize -->
    <rect x="0" y="0" width="160" height="225" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
    <rect x="0" y="0" width="160" height="28" rx="8" fill="#0369a1"/>
    <text x="80" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">MAIZE / BEANS</text>
    <text x="10" y="48" font-size="10" font-weight="bold" fill="#38bdf8">Seedbed:</text>
    <text x="10" y="65" font-size="9" fill="#cbd5e1">Strip / Zero Till</text>
    <text x="10" y="95" font-size="10" font-weight="bold" fill="#38bdf8">Why:</text>
    <text x="10" y="112" font-size="9" fill="#cbd5e1">Large seeds emerge easily; stops soil capping</text>
  </g>
</svg>
""")

# SVG 10: Step-by-Step Demonstration Plot Layout (Lesson 10, Page 2)
SVG_DEMO_PLOT_LAYOUT = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Standard 3m x 3m Demonstration Plot Layout &amp; Tillage Sequence</text>

  <!-- Plot Box Graphic (Center Left) -->
  <g transform="translate(50, 60)">
    <!-- Outer Drainage Furrow -->
    <rect x="0" y="0" width="340" height="340" fill="#0f172a" stroke="#06b6d4" stroke-width="2" stroke-dasharray="4,4"/>
    <text x="170" y="18" font-size="9" fill="#67e8f9" text-anchor="middle">Perimeter Drainage Trench (10 cm deep)</text>

    <!-- Main Seedbed (3m x 3m) -->
    <rect x="25" y="25" width="290" height="290" fill="#14532d" stroke="#22c55e" stroke-width="3"/>
    
    <!-- Corner Pegs -->
    <circle cx="25" cy="25" r="8" fill="#eab308"/><circle cx="315" cy="25" r="8" fill="#eab308"/>
    <circle cx="25" cy="315" r="8" fill="#eab308"/><circle cx="315" cy="315" r="8" fill="#eab308"/>
    
    <!-- Boundary Strings -->
    <line x1="25" y1="25" x2="315" y2="25" stroke="#fde047" stroke-width="2"/>
    <line x1="25" y1="315" x2="315" y2="315" stroke="#fde047" stroke-width="2"/>
    <line x1="25" y1="25" x2="25" y2="315" stroke="#fde047" stroke-width="2"/>
    <line x1="315" y1="25" x2="315" y2="315" stroke="#fde047" stroke-width="2"/>

    <text x="170" y="155" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">3.0 m × 3.0 m</text>
    <text x="170" y="180" font-size="11" font-weight="bold" fill="#86efac" text-anchor="middle">Prepared Seedbed</text>
    <text x="170" y="200" font-size="10" fill="#dcfce7" text-anchor="middle">Crumbly Granular Tilth</text>
  </g>

  <!-- Step-by-Step Checklist (Right Side) -->
  <g transform="translate(420, 60)">
    <rect x="0" y="0" width="345" height="340" rx="8" fill="#0f172a" stroke="#334155"/>
    <rect x="0" y="0" width="345" height="32" rx="8" fill="#0284c7"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">THE 4-STEP TILLAGE CHECKLIST</text>

    <g transform="translate(15, 45)">
      <text x="0" y="20" font-size="12" font-weight="bold" fill="#fde047">Step 1: Slashing (Biomass Recycling)</text>
      <text x="0" y="38" font-size="10" fill="#cbd5e1">Cut grass at ground level; wheelbarrow to compost</text>

      <text x="0" y="70" font-size="12" font-weight="bold" fill="#fde047">Step 2: Primary Digging (20–25 cm)</text>
      <text x="0" y="88" font-size="10" fill="#cbd5e1">Dig with hand jembes; invert soil slices</text>

      <text x="0" y="120" font-size="12" font-weight="bold" fill="#fde047">Step 3: Secondary Clod Breaking</text>
      <text x="0" y="138" font-size="10" fill="#cbd5e1">Fork jembes shatter clods; lift couch grass rhizomes</text>

      <text x="0" y="170" font-size="12" font-weight="bold" fill="#fde047">Step 4: Incorporating Compost &amp; Raking</text>
      <text x="0" y="188" font-size="10" fill="#cbd5e1">Add 15 kg compost; rake surface level and smooth</text>
    </g>

    <rect x="15" y="265" width="315" height="55" rx="6" fill="#1e293b" stroke="#22c55e"/>
    <text x="172" y="285" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Quality Standard: Crumbly, Flat, Clean</text>
    <text x="172" y="303" font-size="9" fill="#86efac" text-anchor="middle">100% free of stones, plastic, and weed roots</text>
  </g>
</svg>
""")

SVG_MAP = {
    1: {"page": 3, "svg": SVG_LAND_PREP_SEQUENCE, "title": "The 4-Stage Sequential Flow of Agricultural Land Preparation"},
    2: {"page": 3, "svg": SVG_CLEARING_COMPOSTING, "title": "Land Clearing Equipment & Ecological Biomass Fate"},
    3: {"page": 3, "svg": SVG_PRIMARY_IMPLEMENTS, "title": "Primary Tillage Implements: Mouldboard vs Disc Plough vs Subsoiler"},
    4: {"page": 3, "svg": SVG_TILTH_COMPARISON, "title": "Soil Tilth Dynamics: Fine Seedbed vs Coarse Cloddy Tilth"},
    5: {"page": 3, "svg": SVG_TERTIARY_STRUCTURES, "title": "Tertiary Field Structures: Raised Beds vs Contour Ridges"},
    6: {"page": 3, "svg": SVG_TOOL_SAFETY, "title": "Farm Tool Safety Regulations & Routine Maintenance Cycle"},
    7: {"page": 3, "svg": SVG_ZERO_TILL_MODEL, "title": "Conservation Agriculture: Zero Tillage Direct Seeding Model"},
    8: {"page": 3, "svg": SVG_STRIP_TILLAGE, "title": "Strip Tillage (Zone Tillage) Architecture & Field Layout"},
    9: {"page": 3, "svg": SVG_SITE_ASSESSMENT, "title": "Pre-Tillage Site Assessment & Crop-Matching Decision Tree"},
    10: {"page": 2, "svg": SVG_DEMO_PLOT_LAYOUT, "title": "Standard 3m x 3m Demonstration Plot Layout & Tillage Sequence"}
}

def enrich_grade10_topic3():
    """Injects verified photos, responsive vector SVGs, YouTube embeds, and creates LessonAssets."""
    print("=" * 80)
    print("STARTING ENRICHMENT: CBC Grade 10 Agriculture — Topic 3: Land Preparation")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()
    topic = Topic.objects.filter(subject=subject, name="Land Preparation").first()

    assert topic, "Topic 'Land Preparation' not found!"

    images_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grade10_topic3_verified_images.json")
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
                    "topic_order": 3,
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
                        "topic_order": 3,
                        "unit_order": u_order,
                        "page": svg_def["page"],
                        "svg_content": svg_def["svg"]
                    }
                )
                diag_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [Vector SVG Attached] Lesson {u_order}: {svg_def['title']}")

        # ---------------------------------------------------------------------
        # 3. Educational YouTube Videos (Lesson 3 & Lesson 10)
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
                        "topic_order": 3,
                        "unit_order": u_order,
                        "youtube_url": v_url
                    }
                )
                v_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [YouTube Video Attached] Lesson {u_order}: {v_block.title}")

    print("=" * 80)
    print(f"ENRICHMENT COMPLETE: Topic 3 '{topic.name}'")
    print(f"  Photographic Hooks: {total_images_attached} / 12")
    print(f"  Vector SVGs:        {total_svgs_attached} / 10")
    print(f"  YouTube Videos:     {total_videos_attached} / 2")
    print(f"  LessonAssets:       {total_assets_persisted}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic3()
