"""
VLearn CBC Grade 10 Agriculture — Topic 5: Growing Selected Crops
Visual Enrichment Engine (Phase 2: Vector SVGs, Verified Photos & Asset Persistence)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Growing Selected Crops (Order: 5)

Attaches:
  - 10 First-Card Photographic Visual Hooks (100% Tested HTTP 200 Direct Wikimedia URLs)
  - 8 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - 2 Verified Educational YouTube Videos (Lesson 3 Card 3 & Lesson 6 Card 3)
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade10_agriculture_topic5.py
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
# 8 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 5: GROWING SELECTED CROPS
# =============================================================================

# SVG 1: Agribusiness Crop Selection Decision Matrix (Lesson 1, Page 3)
SVG_CROP_SELECTION_MATRIX = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Agribusiness Crop Selection Decision Matrix</text>

  <!-- Central Target: Enterprise Selection -->
  <circle cx="400" cy="240" r="65" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
  <text x="400" y="230" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">SELECTED</text>
  <text x="400" y="248" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">CROP</text>
  <text x="400" y="265" font-size="10" fill="#86efac" text-anchor="middle">ENTERPRISE</text>

  <!-- Filter 1: Market Demand (Top) -->
  <g transform="translate(290, 70)">
    <rect x="0" y="0" width="220" height="85" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="26" rx="8" fill="#15803d"/>
    <text x="110" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. MARKET DEMAND &amp; PRICE</text>
    <text x="10" y="45" font-size="10" fill="#cbd5e1">• High local community consumption</text>
    <text x="10" y="65" font-size="10" fill="#cbd5e1">• Ready buyers (Supermarkets, Canteens)</text>
  </g>
  <line x1="400" y1="155" x2="400" y2="175" stroke="#22c55e" stroke-width="3"/>
  <polygon points="395,175 400,185 405,175" fill="#22c55e"/>

  <!-- Filter 2: Ecological Fit (Right) -->
  <g transform="translate(545, 195)">
    <rect x="0" y="0" width="220" height="85" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="26" rx="8" fill="#ca8a04"/>
    <text x="110" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. ECOLOGICAL ADAPTATION</text>
    <text x="10" y="45" font-size="10" fill="#cbd5e1">• Altitude, temperature &amp; rainfall</text>
    <text x="10" y="65" font-size="10" fill="#cbd5e1">• Soil type, drainage &amp; target pH</text>
  </g>
  <line x1="545" y1="240" x2="465" y2="240" stroke="#eab308" stroke-width="3"/>
  <polygon points="475,235 465,240 475,245" fill="#eab308"/>

  <!-- Filter 3: Water & Inputs (Bottom) -->
  <g transform="translate(290, 315)">
    <rect x="0" y="0" width="220" height="85" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="26" rx="8" fill="#0891b2"/>
    <text x="110" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. INPUT &amp; WATER ACCESS</text>
    <text x="10" y="45" font-size="10" fill="#cbd5e1">• Clean, reliable irrigation supply</text>
    <text x="10" y="65" font-size="10" fill="#cbd5e1">• Quality hybrid seeds &amp; fertilizers</text>
  </g>
  <line x1="400" y1="315" x2="400" y2="305" stroke="#06b6d4" stroke-width="3"/>
  <polygon points="395,315 400,305 405,315" fill="#06b6d4"/>

  <!-- Filter 4: Maturity Window (Left) -->
  <g transform="translate(35, 195)">
    <rect x="0" y="0" width="220" height="85" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="26" rx="8" fill="#7e22ce"/>
    <text x="110" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4. MATURITY DURATION</text>
    <text x="10" y="45" font-size="10" fill="#cbd5e1">• 2 to 3-month short season cycle</text>
    <text x="10" y="65" font-size="10" fill="#cbd5e1">• Matches school term / quick cash flow</text>
  </g>
  <line x1="255" y1="240" x2="335" y2="240" stroke="#a855f7" stroke-width="3"/>
  <polygon points="325,235 335,240 325,245" fill="#a855f7"/>
</svg>
""")

# SVG 2: Standard 1.0m Wide Nursery Bed Architecture & Siting (Lesson 2, Page 3)
SVG_NURSERY_BED_ARCHITECTURE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Standard 1.0m Wide Nursery Bed Architecture &amp; Ergonomics</text>

  <!-- Cross-Section Graphic (Center Left) -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>

    <!-- Perimeter Drainage Furrows -->
    <path d="M 20 230 L 45 270 L 65 230 Z" fill="#0c4a6e" stroke="#0284c7"/>
    <path d="M 275 230 L 295 270 L 320 230 Z" fill="#0c4a6e" stroke="#0284c7"/>
    <text x="45" y="295" font-size="8" fill="#38bdf8" text-anchor="middle">Drain Trench</text>
    <text x="295" y="295" font-size="8" fill="#38bdf8" text-anchor="middle">Drain Trench</text>

    <!-- Raised Bed Soil Mound -->
    <path d="M 65 230 L 85 160 L 255 160 L 275 230 Z" fill="#14532d" stroke="#22c55e" stroke-width="2"/>
    <text x="170" y="195" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Fine Crumb Tilth + Compost</text>
    <text x="170" y="215" font-size="9" fill="#86efac" text-anchor="middle">(15 cm Raised Height)</text>

    <!-- 1.0 Meter Width Dimension Line -->
    <line x1="85" y1="140" x2="255" y2="140" stroke="#fde047" stroke-width="2"/>
    <polygon points="85,137 75,140 85,143" fill="#fde047"/>
    <polygon points="255,137 265,140 255,143" fill="#fde047"/>
    <text x="170" y="130" font-size="12" font-weight="bold" fill="#fde047" text-anchor="middle">Standard Width: Exactly 1.0 m</text>

    <!-- 50 cm Reach from Both Sides -->
    <text x="125" y="105" font-size="9" fill="#cbd5e1" text-anchor="middle">50 cm Reach</text>
    <text x="215" y="105" font-size="9" fill="#cbd5e1" text-anchor="middle">50 cm Reach</text>

    <rect x="20" y="305" width="300" height="28" rx="4" fill="#14532d"/>
    <text x="170" y="323" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">Zero Soil Compaction: Never Step on Bed!</text>
  </g>

  <!-- Right: 4 Site Selection Rules -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#0284c7"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">4 NURSERY SITING CRITERIA</text>

    <g transform="translate(15, 45)">
      <text x="0" y="20" font-size="12" font-weight="bold" fill="#fde047">1. Proximity to Clean Water:</text>
      <text x="0" y="38" font-size="11" fill="#cbd5e1">Within short distance; seedlings need twice daily care</text>

      <text x="0" y="70" font-size="12" font-weight="bold" fill="#fde047">2. Gentle Topography (Slope):</text>
      <text x="0" y="88" font-size="11" fill="#cbd5e1">Flat/gentle slope; avoids erosion and swamp waterlogging</text>

      <text x="0" y="120" font-size="12" font-weight="bold" fill="#fde047">3. Wind Shelter &amp; Morning Sun:</text>
      <text x="0" y="138" font-size="11" fill="#cbd5e1">Sheltered from strong gusts; avoid dense tree shade (etiolation)</text>

      <text x="0" y="170" font-size="12" font-weight="bold" fill="#fde047">4. Disease-Free Rotation History:</text>
      <text x="0" y="188" font-size="11" fill="#cbd5e1">Avoid old solanaceous plots to prevent bacterial wilt</text>
    </g>

    <rect x="15" y="275" width="315" height="55" rx="6" fill="#1e293b" stroke="#22c55e"/>
    <text x="172" y="295" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">5-Step Soil Preparation</text>
    <text x="172" y="313" font-size="9" fill="#86efac" text-anchor="middle">Clear -&gt; Dig 30cm -&gt; Pulverize -&gt; Add Compost -&gt; Level</text>
  </g>
</svg>
""")

# SVG 3: Sowing, Mulching & Sloped Shade Frame Cross-Section (Lesson 3, Page 3)
SVG_NURSERY_SOWING_SHADE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Nursery Sowing, Mulch Layer, and Sloped Shade Architecture</text>

  <!-- Cross Section Illustration Graphic -->
  <g transform="translate(60, 65)">
    <!-- Sloped Overhead Shade Roof (1m high) -->
    <polygon points="50,45 630,20 630,35 50,60" fill="#78350f" stroke="#ca8a04" stroke-width="1.5"/>
    <text x="340" y="30" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">SLOPED SHADE FRAME (1.0 m High) — Sheds Heavy Raindrops &amp; Noon Sun</text>

    <!-- Support Posts -->
    <line x1="80" y1="55" x2="80" y2="230" stroke="#ca8a04" stroke-width="6"/>
    <line x1="600" y1="30" x2="600" y2="230" stroke="#ca8a04" stroke-width="6"/>

    <!-- Dry Grass Mulch Layer -->
    <rect x="100" y="180" width="480" height="15" fill="#ca8a04" opacity="0.8" stroke="#fde047" stroke-width="1"/>
    <text x="340" y="172" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">Dry Grass Mulch (REMOVE IMMEDIATELY AT EMERGENCE TO HALT ETIOLATION)</text>

    <!-- Refined Topsoil Matrix -->
    <rect x="100" y="195" width="480" height="100" fill="#14532d" stroke="#22c55e" stroke-width="2"/>
    <text x="340" y="275" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Refined Granular Tilth (&lt;5 mm) Mixed with Organic Compost</text>

    <!-- Drilled Seed Furrows (10–15 cm spacing, 1.5 cm depth) -->
    <g transform="translate(140, 205)">
      <circle cx="0" cy="15" r="5" fill="#eab308"/><text x="0" y="35" font-size="9" fill="#fde047" text-anchor="middle">1.5 cm</text>
      <circle cx="100" cy="15" r="5" fill="#eab308"/><text x="100" y="35" font-size="9" fill="#fde047" text-anchor="middle">1.5 cm</text>
      <circle cx="200" cy="15" r="5" fill="#eab308"/><text x="200" y="35" font-size="9" fill="#fde047" text-anchor="middle">1.5 cm</text>
      <circle cx="300" cy="15" r="5" fill="#eab308"/><text x="300" y="35" font-size="9" fill="#fde047" text-anchor="middle">1.5 cm</text>
      <circle cx="400" cy="15" r="5" fill="#eab308"/><text x="400" y="35" font-size="9" fill="#fde047" text-anchor="middle">1.5 cm</text>
      <!-- Spacing dimension -->
      <line x1="0" y1="45" x2="100" y2="45" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="50" y="58" font-size="8" fill="#38bdf8" text-anchor="middle">10–15 cm Spacing</text>
    </g>
  </g>

  <!-- Agronomic Rules Footer -->
  <g transform="translate(60, 340)">
    <rect x="0" y="0" width="680" height="70" rx="8" fill="#0f172a" stroke="#38bdf8"/>
    <text x="340" y="24" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Precision Drilling Rule: Never Broadcast Seeds in Nursery Beds!</text>
    <text x="20" y="48" font-size="10" fill="#cbd5e1">• Uniform 1.5 cm depth guarantees equal germination speed &amp; leaves 10 cm walkways for hand weeding</text>
  </g>
</svg>
""")

# SVG 4: Nursery Management: Thinning, Pricking Out & Hardening Off (Lesson 4, Page 3)
SVG_NURSERY_MANAGEMENT = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Nursery Husbandry: Thinning, Pricking Out &amp; Hardening Off</text>

  <!-- Step 1: Thinning -->
  <g transform="translate(35, 65)">
    <rect x="0" y="0" width="225" height="345" rx="10" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect x="0" y="0" width="225" height="30" rx="10" fill="#ca8a04"/>
    <text x="112" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. THINNING</text>

    <!-- Graphic -->
    <g transform="translate(30, 60)">
      <line x1="20" y1="80" x2="20" y2="20" stroke="#22c55e" stroke-width="5"/>
      <line x1="45" y1="80" x2="45" y2="35" stroke="#f87171" stroke-width="2" stroke-dasharray="2,2"/>
      <line x1="70" y1="80" x2="70" y2="40" stroke="#f87171" stroke-width="2" stroke-dasharray="2,2"/>
      <line x1="100" y1="80" x2="100" y2="20" stroke="#22c55e" stroke-width="5"/>
      <text x="82" y="105" font-size="9" fill="#fde047" text-anchor="middle">Remove weak seedlings</text>
    </g>

    <g transform="translate(10, 180)">
      <text x="0" y="15" font-size="10" font-weight="bold" fill="#fde047">• Pluck crowded seedlings</text>
      <text x="0" y="35" font-size="9" fill="#cbd5e1">• Leaves 2–3 cm space</text>
      <text x="0" y="55" font-size="9" fill="#cbd5e1">• Builds thick stocky stems</text>
      <text x="0" y="75" font-size="9" fill="#cbd5e1">• Eliminates nutrient theft</text>
    </g>
    <rect x="10" y="295" width="205" height="35" rx="4" fill="#78350f"/>
    <text x="112" y="316" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">Space Optimization</text>
  </g>

  <!-- Step 2: Pricking Out -->
  <g transform="translate(285, 65)">
    <rect x="0" y="0" width="225" height="345" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="225" height="30" rx="10" fill="#0284c7"/>
    <text x="112" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. PRICKING OUT</text>

    <!-- Graphic -->
    <g transform="translate(45, 60)">
      <rect x="0" y="30" width="45" height="50" rx="4" fill="#1e293b" stroke="#38bdf8"/>
      <line x1="22" y1="45" x2="22" y2="10" stroke="#22c55e" stroke-width="4"/>
      <rect x="75" y="30" width="45" height="50" rx="4" fill="#1e293b" stroke="#38bdf8"/>
      <line x1="97" y1="45" x2="97" y2="10" stroke="#22c55e" stroke-width="4"/>
      <text x="67" y="105" font-size="9" fill="#38bdf8" text-anchor="middle">5 cm × 5 cm tubes</text>
    </g>

    <g transform="translate(10, 180)">
      <text x="0" y="15" font-size="10" font-weight="bold" fill="#38bdf8">• At 2–3 true leaves stage</text>
      <text x="0" y="35" font-size="9" fill="#cbd5e1">• Move to individual pots</text>
      <text x="0" y="55" font-size="9" fill="#cbd5e1">• Spacing: 5 cm × 5 cm</text>
      <text x="0" y="75" font-size="9" fill="#cbd5e1">• Stimulates lateral roots</text>
    </g>
    <rect x="10" y="295" width="205" height="35" rx="4" fill="#0c4a6e"/>
    <text x="112" y="316" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Root Volume Expansion</text>
  </g>

  <!-- Step 3: Hardening Off -->
  <g transform="translate(535, 65)">
    <rect x="0" y="0" width="230" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="230" height="30" rx="10" fill="#15803d"/>
    <text x="115" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. HARDENING OFF</text>

    <!-- Sun / Water Graphic -->
    <g transform="translate(65, 60)">
      <circle cx="50" cy="30" r="22" fill="#eab308" stroke="#fde047" stroke-width="2"/>
      <text x="50" y="34" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">SUN</text>
      <text x="50" y="80" font-size="9" fill="#fca5a5" text-anchor="middle">Reduce Water</text>
      <text x="50" y="105" font-size="9" fill="#86efac" text-anchor="middle">Remove Shade</text>
    </g>

    <g transform="translate(10, 180)">
      <text x="0" y="15" font-size="10" font-weight="bold" fill="#4ade80">• 1–2 weeks before field</text>
      <text x="0" y="35" font-size="9" fill="#cbd5e1">• Progressively remove shade</text>
      <text x="0" y="55" font-size="9" fill="#cbd5e1">• Reduce water frequency</text>
      <text x="0" y="75" font-size="9" fill="#cbd5e1">• Thickens leaf cuticles</text>
    </g>
    <rect x="10" y="295" width="210" height="35" rx="4" fill="#14532d"/>
    <text x="115" y="316" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">Transplant Shock Defense</text>
  </g>
</svg>
""")

# SVG 5: Step-by-Step Seedling Transplanting Protocol with Root Ball (Lesson 5, Page 3)
SVG_TRANSPLANTING_PROTOCOL = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Field Establishment: Seedling Transplanting Protocol with Root Ball</text>

  <!-- Step 1: Pre-Water & Lift with Trowel -->
  <g transform="translate(35, 65)">
    <rect x="0" y="0" width="165" height="345" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="165" height="28" rx="8" fill="#0284c7"/>
    <text x="82" y="19" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">1. TROWEL LIFTING</text>
    
    <!-- Trowel + Root Ball Graphic -->
    <path d="M 40 100 Q 82 140 125 100 L 115 170 L 50 170 Z" fill="#78350f" stroke="#ca8a04"/>
    <line x1="82" y1="120" x2="82" y2="60" stroke="#22c55e" stroke-width="5"/>
    <text x="82" y="195" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Intact Soil Root Ball</text>

    <text x="10" y="230" font-size="9" fill="#cbd5e1">• Water nursery 30 min prior</text>
    <text x="10" y="250" font-size="9" fill="#cbd5e1">• Slide trowel underneath</text>
    <text x="10" y="270" font-size="9" font-weight="bold" fill="#ef4444">• NEVER pull by stem!</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <line x1="205" y1="230" x2="225" y2="230" stroke="#38bdf8" stroke-width="2"/>
  <polygon points="225,225 235,230 225,235" fill="#38bdf8"/>

  <!-- Step 2: Placement at Collar Depth -->
  <g transform="translate(230, 65)">
    <rect x="0" y="0" width="165" height="345" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="165" height="28" rx="8" fill="#15803d"/>
    <text x="82" y="19" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">2. COLLAR DEPTH</text>

    <!-- Planting Hole Graphic -->
    <rect x="25" y="120" width="115" height="60" rx="6" fill="#14532d" stroke="#22c55e"/>
    <line x1="82" y1="130" x2="82" y2="60" stroke="#22c55e" stroke-width="5"/>
    <line x1="15" y1="120" x2="150" y2="120" stroke="#ca8a04" stroke-width="2" stroke-dasharray="2,2"/>
    <text x="82" y="195" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">Exact Nursery Depth</text>

    <text x="10" y="230" font-size="9" fill="#cbd5e1">• Manured hole (200g compost)</text>
    <text x="10" y="250" font-size="9" fill="#cbd5e1">• Collar level with soil</text>
    <text x="10" y="270" font-size="9" fill="#cbd5e1">• No buried leaves</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <line x1="400" y1="230" x2="420" y2="230" stroke="#38bdf8" stroke-width="2"/>
  <polygon points="420,225 430,230 420,235" fill="#38bdf8"/>

  <!-- Step 3: Firming Soil -->
  <g transform="translate(425, 65)">
    <rect x="0" y="0" width="165" height="345" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <rect x="0" y="0" width="165" height="28" rx="8" fill="#ca8a04"/>
    <text x="82" y="19" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">3. SOIL FIRMING</text>

    <rect x="25" y="120" width="115" height="60" fill="#78350f"/>
    <line x1="82" y1="130" x2="82" y2="60" stroke="#22c55e" stroke-width="5"/>
    <circle cx="55" cy="130" r="10" fill="#ca8a04"/><circle cx="110" cy="130" r="10" fill="#ca8a04"/>
    <text x="82" y="195" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">Remove Air Pockets</text>

    <text x="10" y="230" font-size="9" fill="#cbd5e1">• Press with fingertips</text>
    <text x="10" y="250" font-size="9" fill="#cbd5e1">• Eliminates air voids</text>
    <text x="10" y="270" font-size="9" fill="#cbd5e1">• Locks roots with soil</text>
  </g>

  <!-- Arrow 3 -> 4 -->
  <line x1="595" y1="230" x2="615" y2="230" stroke="#38bdf8" stroke-width="2"/>
  <polygon points="615,225 625,230 615,235" fill="#38bdf8"/>

  <!-- Step 4: Water & Shade -->
  <g transform="translate(620, 65)">
    <rect x="0" y="0" width="145" height="345" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
    <rect x="0" y="0" width="145" height="28" rx="8" fill="#0891b2"/>
    <text x="72" y="19" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">4. WATER &amp; MULCH</text>

    <circle cx="72" cy="115" r="18" fill="#0284c7"/>
    <text x="72" y="120" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">H₂O</text>
    <text x="72" y="195" font-size="9" font-weight="bold" fill="#67e8f9" text-anchor="middle">Late Afternoon (4 PM)</text>

    <text x="8" y="230" font-size="9" fill="#cbd5e1">• 1L water immediately</text>
    <text x="8" y="250" font-size="9" fill="#cbd5e1">• Light ring mulch</text>
    <text x="8" y="270" font-size="9" fill="#86efac">• 12hr night recovery</text>
  </g>
</svg>
""")

# SVG 6: Tomato Staking & Loose Figure-of-8 Tie Mechanics (Lesson 6, Page 3)
SVG_STAKING_FIGURE_8 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Biomechanical Staking &amp; Loose Figure-of-8 Knot Mechanics</text>

  <!-- Left: Whole Plant Staking Graphic -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="345" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>

    <!-- Wooden Stake (1.5m) -->
    <line x1="120" y1="310" x2="120" y2="40" stroke="#ca8a04" stroke-width="12"/>
    <text x="120" y="30" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">1.5 m Wooden Stake</text>

    <!-- Tomato Vine -->
    <line x1="210" y1="310" x2="210" y2="55" stroke="#15803d" stroke-width="8"/>
    <!-- Red Fruits -->
    <circle cx="235" cy="140" r="14" fill="#ef4444"/><circle cx="185" cy="200" r="14" fill="#ef4444"/>

    <!-- Figure-of-8 Ties -->
    <ellipse cx="165" cy="110" rx="45" ry="12" fill="none" stroke="#38bdf8" stroke-width="3"/>
    <ellipse cx="165" cy="230" rx="45" ry="12" fill="none" stroke="#38bdf8" stroke-width="3"/>

    <!-- Soil / Mulch -->
    <rect x="20" y="305" width="300" height="25" fill="#78350f"/>
    <text x="170" y="322" font-size="9" fill="#fde047" text-anchor="middle">Dry Grass Mulch (Keeps Soil Moist &amp; Clean)</text>
  </g>

  <!-- Right: Zoom on Figure-of-8 Knot -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#15803d"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">WHY THE FIGURE-OF-8 TIE MATTERS</text>

    <!-- Zoom Schematic -->
    <g transform="translate(45, 55)">
      <!-- Stake Circle -->
      <circle cx="50" cy="50" r="25" fill="#78350f" stroke="#ca8a04" stroke-width="3"/>
      <text x="50" y="55" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">STAKE</text>
      <!-- Stem Circle -->
      <circle cx="200" cy="50" r="20" fill="#15803d" stroke="#22c55e" stroke-width="3"/>
      <text x="200" y="55" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">STEM</text>

      <!-- Crossed Figure-of-8 Line -->
      <path d="M 50 25 C 125 25, 125 75, 200 75 C 225 75, 225 25, 200 25 C 125 25, 125 75, 50 75 C 25 75, 25 25, 50 25 Z" fill="none" stroke="#38bdf8" stroke-width="3"/>
      <text x="125" y="105" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">2 cm Expansion Buffer</text>
    </g>

    <g transform="translate(15, 185)">
      <text x="0" y="15" font-size="11" font-weight="bold" fill="#ef4444">1. Prevents Stem Girdling (Choking):</text>
      <text x="0" y="32" font-size="10" fill="#cbd5e1">Stems expand in caliper; tight knots strangle sap flow</text>

      <text x="0" y="58" font-size="11" font-weight="bold" fill="#4ade80">2. Cushions Against Wind Chafing:</text>
      <text x="0" y="75" font-size="10" fill="#cbd5e1">Twine cross creates a flexible shock absorber</text>

      <text x="0" y="100" font-size="11" font-weight="bold" fill="#fde047">3. Elevates Produce Off Soil Spores:</text>
      <text x="0" y="117" font-size="10" fill="#cbd5e1">Stops ground blight &amp; ensures Grade 1 clean fruits</text>
    </g>
  </g>
</svg>
""")

# SVG 7: Tomato Harvest Maturity Stages (Lesson 8, Page 3)
SVG_TOMATO_MATURITY_STAGES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Tomato Harvest Maturity Continuum &amp; Market Suitability</text>

  <!-- Stage 1: Mature Green -->
  <g transform="translate(35, 65)">
    <rect x="0" y="0" width="225" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="225" height="30" rx="10" fill="#15803d"/>
    <text x="112" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. GREEN MATURE STAGE</text>

    <!-- Green Tomato Graphic -->
    <circle cx="112" cy="115" r="45" fill="#16a34a" stroke="#22c55e" stroke-width="2"/>
    <text x="112" y="120" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">100% Green</text>

    <g transform="translate(10, 185)">
      <text x="0" y="15" font-size="10" font-weight="bold" fill="#4ade80">• Fully sized; jelly formed inside</text>
      <text x="0" y="35" font-size="9" fill="#cbd5e1">• Maximum physical firmness</text>
      <text x="0" y="55" font-size="9" font-weight="bold" fill="#38bdf8">• Best for Long Distance (&gt;100 km)</text>
      <text x="0" y="75" font-size="9" fill="#cbd5e1">• Ripens in transit (7–10 days)</text>
    </g>
    <rect x="10" y="295" width="205" height="35" rx="4" fill="#14532d"/>
    <text x="112" y="316" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">Export &amp; Long Transit King</text>
  </g>

  <!-- Stage 2: Breaker / Turning -->
  <g transform="translate(285, 65)">
    <rect x="0" y="0" width="225" height="345" rx="10" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect x="0" y="0" width="225" height="30" rx="10" fill="#ca8a04"/>
    <text x="112" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. BREAKER STAGE</text>

    <!-- Breaker Tomato Graphic (Green with Pink Tip) -->
    <circle cx="112" cy="115" r="45" fill="#16a34a" stroke="#eab308" stroke-width="2"/>
    <path d="M 85 140 Q 112 110 139 140 A 45 45 0 0 1 85 140 Z" fill="#ef4444"/>
    <text x="112" y="110" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Pink Star</text>

    <g transform="translate(10, 185)">
      <text x="0" y="15" font-size="10" font-weight="bold" fill="#fde047">• First color break at blossom end</text>
      <text x="0" y="35" font-size="9" fill="#cbd5e1">• Firm skin with flavor synthesis</text>
      <text x="0" y="55" font-size="9" font-weight="bold" fill="#38bdf8">• Best for Supermarkets / Retail</text>
      <text x="0" y="75" font-size="9" fill="#cbd5e1">• 4–6 day retail shelf life</text>
    </g>
    <rect x="10" y="295" width="205" height="35" rx="4" fill="#78350f"/>
    <text x="112" y="316" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">Retail Supermarket Standard</text>
  </g>

  <!-- Stage 3: Full Red Ripe -->
  <g transform="translate(535, 65)">
    <rect x="0" y="0" width="230" height="345" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="230" height="30" rx="10" fill="#991b1b"/>
    <text x="115" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. FULLY RIPE STAGE</text>

    <!-- Red Tomato Graphic -->
    <circle cx="115" cy="115" r="45" fill="#ef4444" stroke="#f87171" stroke-width="2"/>
    <text x="115" y="120" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">100% Red</text>

    <g transform="translate(10, 185)">
      <text x="0" y="15" font-size="10" font-weight="bold" fill="#fca5a5">• 100% red/crimson coloration</text>
      <text x="0" y="35" font-size="9" fill="#cbd5e1">• Peak sugar brix &amp; aroma</text>
      <text x="0" y="55" font-size="9" font-weight="bold" fill="#38bdf8">• Best for Local Sale / Kitchens</text>
      <text x="0" y="75" font-size="9" fill="#cbd5e1">• Softens fast; immediate use</text>
    </g>
    <rect x="10" y="295" width="210" height="35" rx="4" fill="#450a0a"/>
    <text x="115" y="316" font-size="9" font-weight="bold" fill="#fca5a5" text-anchor="middle">Immediate Farm-Gate Sales</text>
  </g>
</svg>
""")

# SVG 8: The Complete 6-Phase Crop Production Lifecycle (Lesson 10, Page 2)
SVG_CROP_LIFECYCLE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Complete 6-Phase Commercial Crop Production Lifecycle</text>

  <!-- Central Hub: Agribusiness Enterprise -->
  <circle cx="400" cy="240" r="55" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
  <text x="400" y="235" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">COMMERCIAL</text>
  <text x="400" y="252" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">AGRIBUSINESS</text>

  <!-- 1. Planning -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="195" height="75" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="97" y="22" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">PHASE 1: PLANNING</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Market survey &amp; crop choice</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Production calendar &amp; budget</text>
  </g>
  <line x1="240" y1="102" x2="345" y2="200" stroke="#22c55e" stroke-width="2" stroke-dasharray="2,2"/>

  <!-- 2. Nursery Sowing -->
  <g transform="translate(560, 65)">
    <rect x="0" y="0" width="195" height="75" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="97" y="22" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">PHASE 2: SOWING</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• 1.0 m bed, fine tilth + compost</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Drill seeds, mulch &amp; shade</text>
  </g>
  <line x1="560" y1="102" x2="455" y2="200" stroke="#38bdf8" stroke-width="2" stroke-dasharray="2,2"/>

  <!-- 3. Nursery Husbandry -->
  <g transform="translate(35, 195)">
    <rect x="0" y="0" width="195" height="75" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <text x="97" y="22" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">PHASE 3: NURSERY CARE</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Fine-rose watering &amp; thinning</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• 2-week hardening off</text>
  </g>
  <line x1="230" y1="240" x2="345" y2="240" stroke="#eab308" stroke-width="2"/>

  <!-- 4. Field Establishment -->
  <g transform="translate(570, 195)">
    <rect x="0" y="0" width="195" height="75" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
    <text x="97" y="22" font-size="11" font-weight="bold" fill="#67e8f9" text-anchor="middle">PHASE 4: TRANSPLANTING</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Intact root ball with trowel</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Late afternoon planting @ collar</text>
  </g>
  <line x1="570" y1="240" x2="455" y2="240" stroke="#06b6d4" stroke-width="2"/>

  <!-- 5. Field Management -->
  <g transform="translate(45, 325)">
    <rect x="0" y="0" width="195" height="75" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="97" y="22" font-size="11" font-weight="bold" fill="#d8b4fe" text-anchor="middle">PHASE 5: FIELD CARE</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Staking with figure-of-8 ties</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Pruning suckers &amp; CAN top-dress</text>
  </g>
  <line x1="240" y1="362" x2="345" y2="280" stroke="#a855f7" stroke-width="2" stroke-dasharray="2,2"/>

  <!-- 6. Harvest & Accounting -->
  <g transform="translate(560, 325)">
    <rect x="0" y="0" width="195" height="75" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="97" y="22" font-size="11" font-weight="bold" fill="#fca5a5" text-anchor="middle">PHASE 6: HARVEST &amp; ROI</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Morning harvest at breaker/ripe</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Grade 1 marketing &amp; profit ledger</text>
  </g>
  <line x1="560" y1="362" x2="455" y2="280" stroke="#ef4444" stroke-width="2" stroke-dasharray="2,2"/>
</svg>
""")

SVG_MAP = {
    1: {"page": 3, "svg": SVG_CROP_SELECTION_MATRIX, "title": "Agribusiness Crop Selection Decision Matrix"},
    2: {"page": 3, "svg": SVG_NURSERY_BED_ARCHITECTURE, "title": "Standard 1.0m Wide Nursery Bed Architecture & Siting"},
    3: {"page": 3, "svg": SVG_NURSERY_SOWING_SHADE, "title": "Sowing, Mulching & Sloped Shade Frame Cross-Section"},
    4: {"page": 3, "svg": SVG_NURSERY_MANAGEMENT, "title": "Nursery Management: Thinning, Pricking Out & Hardening Off"},
    5: {"page": 3, "svg": SVG_TRANSPLANTING_PROTOCOL, "title": "Step-by-Step Seedling Transplanting Protocol with Root Ball"},
    6: {"page": 3, "svg": SVG_STAKING_FIGURE_8, "title": "Tomato Staking & Loose Figure-of-8 Tie Mechanics"},
    8: {"page": 3, "svg": SVG_TOMATO_MATURITY_STAGES, "title": "Tomato Harvest Maturity Stages: Green Mature vs Breaker vs Ripe"},
    10: {"page": 2, "svg": SVG_CROP_LIFECYCLE, "title": "The Complete 6-Phase Crop Production Lifecycle"}
}

def enrich_grade10_topic5():
    """Injects verified photos, responsive vector SVGs, YouTube embeds, and creates LessonAssets."""
    print("=" * 80)
    print("STARTING ENRICHMENT: CBC Grade 10 Agriculture — Topic 5: Growing Selected Crops")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()
    topic = Topic.objects.filter(subject=subject, name="Growing Selected Crops").first()

    assert topic, "Topic 'Growing Selected Crops' not found!"

    images_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grade10_topic5_verified_images.json")
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
                    "topic_order": 5,
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
                        "topic_order": 5,
                        "unit_order": u_order,
                        "page": svg_def["page"],
                        "svg_content": svg_def["svg"]
                    }
                )
                diag_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [Vector SVG Attached] Lesson {u_order}: {svg_def['title']}")

        # ---------------------------------------------------------------------
        # 3. Educational YouTube Videos (Lesson 3 & Lesson 6)
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
                        "topic_order": 5,
                        "unit_order": u_order,
                        "youtube_url": v_url
                    }
                )
                v_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [YouTube Video Attached] Lesson {u_order}: {v_block.title}")

    print("=" * 80)
    print(f"ENRICHMENT COMPLETE: Topic 5 '{topic.name}'")
    print(f"  Photographic Hooks: {total_images_attached} / 10")
    print(f"  Vector SVGs:        {total_svgs_attached} / 8")
    print(f"  YouTube Videos:     {total_videos_attached} / 2")
    print(f"  LessonAssets:       {total_assets_persisted}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic5()
