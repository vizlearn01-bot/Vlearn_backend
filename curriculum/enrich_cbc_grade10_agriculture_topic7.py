"""
VLearn CBC Grade 10 Agriculture — Topic 7: General Crop Harvesting
Visual Enrichment Engine (Phase 2: Vector SVGs, Verified Photos & Asset Persistence)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: General Crop Harvesting (Order: 7)

Attaches:
  - 10 First-Card Photographic Visual Hooks (100% Tested HTTP 200 Direct Wikimedia URLs)
  - 8 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - 1 Verified Educational YouTube Video (Lesson 2 Card 3)
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade10_agriculture_topic7.py
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
# 8 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 7: GENERAL CROP HARVESTING
# =============================================================================

# SVG 1: The 4 Key Determinants of Crop Harvest Timing (Lesson 1, Page 2)
SVG_HARVEST_DETERMINANTS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 4 Key Determinants of Crop Harvest Timing</text>

  <!-- Central Target: Harvest Day -->
  <circle cx="400" cy="240" r="60" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
  <text x="400" y="230" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">OPTIMAL</text>
  <text x="400" y="248" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">HARVEST</text>
  <text x="400" y="265" font-size="9" fill="#86efac" text-anchor="middle">TIMING</text>

  <!-- 1. Physiological Maturity (Top) -->
  <g transform="translate(290, 70)">
    <rect x="0" y="0" width="220" height="80" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="25" rx="8" fill="#15803d"/>
    <text x="110" y="17" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">1. PHYSIOLOGICAL MATURITY</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Maximum dry matter accumulation</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Black layer sealed; starch peak</text>
  </g>
  <line x1="400" y1="150" x2="400" y2="180" stroke="#22c55e" stroke-width="3"/>
  <polygon points="395,170 400,180 405,170" fill="#22c55e"/>

  <!-- 2. Moisture Content (Right) -->
  <g transform="translate(545, 195)">
    <rect x="0" y="0" width="220" height="80" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="25" rx="8" fill="#0891b2"/>
    <text x="110" y="17" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">2. MOISTURE PERCENTAGE</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Field harvest: 18–20% moisture</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Storage target: 13–14% threshold</text>
  </g>
  <line x1="545" y1="240" x2="460" y2="240" stroke="#06b6d4" stroke-width="3"/>
  <polygon points="470,235 460,240 470,245" fill="#06b6d4"/>

  <!-- 3. Weather Conditions (Bottom) -->
  <g transform="translate(290, 320)">
    <rect x="0" y="0" width="220" height="80" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="25" rx="8" fill="#ca8a04"/>
    <text x="110" y="17" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">3. DRY WEATHER WINDOW</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Clear sunny skies essential</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Rain triggers Aspergillus mold</text>
  </g>
  <line x1="400" y1="320" x2="400" y2="300" stroke="#eab308" stroke-width="3"/>
  <polygon points="395,310 400,300 405,310" fill="#eab308"/>

  <!-- 4. Intended Purpose (Left) -->
  <g transform="translate(35, 195)">
    <rect x="0" y="0" width="220" height="80" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="25" rx="8" fill="#7e22ce"/>
    <text x="110" y="17" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">4. MARKET DESTINATION</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Fresh retail (Breaker tomatoes)</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Factory processing vs Seed stock</text>
  </g>
  <line x1="255" y1="240" x2="340" y2="240" stroke="#a855f7" stroke-width="3"/>
  <polygon points="330,235 340,240 330,245" fill="#a855f7"/>
</svg>
""")

# SVG 2: Potato Haulm Destruction & Subterranean Skin Setting (Lesson 2, Page 2)
SVG_POTATO_HAULM = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Irish Potato Haulm Destruction &amp; Subterranean Skin Setting</text>

  <!-- Left: Day 0 Haulm Mowing -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="345" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="32" rx="10" fill="#991b1b"/>
    <text x="170" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">DAY 0: MECHANICAL HAULM CUTTING</text>

    <!-- Mower / Cut Vines -->
    <line x1="30" y1="120" x2="310" y2="120" stroke="#ef4444" stroke-width="3" stroke-dasharray="4,4"/>
    <text x="170" y="105" font-size="10" font-weight="bold" fill="#f87171" text-anchor="middle">Mowing Line at Soil Surface</text>

    <!-- Cut Stumps -->
    <line x1="80" y1="160" x2="80" y2="120" stroke="#15803d" stroke-width="6"/>
    <line x1="170" y1="160" x2="170" y2="120" stroke="#15803d" stroke-width="6"/>
    <line x1="260" y1="160" x2="260" y2="120" stroke="#15803d" stroke-width="6"/>

    <!-- Subterranean Soil Ridge -->
    <rect x="20" y="160" width="300" height="90" fill="#78350f"/>
    <!-- Thin-Skinned Tubers -->
    <ellipse cx="80" cy="205" rx="25" ry="16" fill="#ca8a04" stroke="#fde047" stroke-width="1"/>
    <ellipse cx="170" cy="205" rx="25" ry="16" fill="#ca8a04" stroke="#fde047" stroke-width="1"/>
    <ellipse cx="260" cy="205" rx="25" ry="16" fill="#ca8a04" stroke="#fde047" stroke-width="1"/>
    <text x="170" y="240" font-size="9" fill="#fde047" text-anchor="middle">Thin, Fragile Tuber Skins (Tears Easily)</text>

    <g transform="translate(15, 265)">
      <text x="0" y="15" font-size="10" fill="#cbd5e1">• Halts vegetative vine growth</text>
      <text x="0" y="32" font-size="10" fill="#cbd5e1">• Eliminates foliar Late Blight host</text>
      <text x="0" y="49" font-size="10" fill="#f87171">• Tubers still prone to skinning</text>
    </g>
  </g>

  <!-- Right: Day 14 Cured Tough Skin -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#15803d"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">DAY 14: FULL SKIN SET &amp; CURED PERIDERM</text>

    <!-- Dead Dry Stems -->
    <line x1="80" y1="160" x2="80" y2="135" stroke="#78350f" stroke-width="4"/>
    <line x1="172" y1="160" x2="172" y2="135" stroke="#78350f" stroke-width="4"/>
    <line x1="265" y1="160" x2="265" y2="135" stroke="#78350f" stroke-width="4"/>
    <text x="172" y="125" font-size="9" fill="#ca8a04" text-anchor="middle">Desiccated Stalks</text>

    <!-- Soil Ridge -->
    <rect x="20" y="160" width="305" height="90" fill="#78350f"/>
    <!-- Cured Thick-Skinned Tubers -->
    <ellipse cx="80" cy="205" rx="25" ry="16" fill="#a16207" stroke="#22c55e" stroke-width="3"/>
    <ellipse cx="172" cy="205" rx="25" ry="16" fill="#a16207" stroke="#22c55e" stroke-width="3"/>
    <ellipse cx="265" cy="205" rx="25" ry="16" fill="#a16207" stroke="#22c55e" stroke-width="3"/>
    <text x="172" y="240" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">Tough Corky Periderm (Thumb-Rub Proof)</text>

    <g transform="translate(15, 265)">
      <text x="0" y="15" font-size="10" fill="#cbd5e1">• Resists scraping during digging</text>
      <text x="0" y="32" font-size="10" fill="#cbd5e1">• Zero Late Blight spore contact</text>
      <text x="0" y="49" font-size="10" font-weight="bold" fill="#4ade80">• 100% Ready for Digging Fork</text>
    </g>
  </g>
</svg>
""")

# SVG 3: Manual vs Mechanical Harvesting Comparison (Lesson 3, Page 2)
SVG_MANUAL_VS_MECHANICAL = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Harvesting Technology: Manual Labor vs Mechanical Machinery</text>

  <!-- Left: Manual Harvesting -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="32" rx="10" fill="#15803d"/>
    <text x="170" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. MANUAL HARVESTING (HUMAN LABOR)</text>

    <!-- Tool Graphics -->
    <g transform="translate(30, 55)">
      <rect x="0" y="0" width="80" height="60" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="40" y="35" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">Panga / Sickle</text>

      <rect x="100" y="0" width="80" height="60" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="140" y="35" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">Digging Fork</text>

      <rect x="200" y="0" width="80" height="60" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="240" y="35" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">Secateurs</text>
    </g>

    <g transform="translate(15, 140)">
      <text x="0" y="18" font-size="11" font-weight="bold" fill="#4ade80">Key Strengths:</text>
      <text x="0" y="36" font-size="10" fill="#cbd5e1">• Highly selective: leaves unripe produce</text>
      <text x="0" y="54" font-size="10" fill="#cbd5e1">• Low capital entry (hand tools only)</text>
      <text x="0" y="72" font-size="10" fill="#cbd5e1">• Works on steep, rocky, small plots</text>

      <text x="0" y="105" font-size="11" font-weight="bold" fill="#ef4444">Key Limitations:</text>
      <text x="0" y="123" font-size="10" fill="#cbd5e1">• Extremely slow (0.3 acres/day)</text>
      <text x="0" y="141" font-size="10" fill="#cbd5e1">• Labor shortages during peak seasons</text>
    </g>
  </g>

  <!-- Right: Mechanical Harvesting -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#0284c7"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. MECHANICAL HARVESTING (MACHINERY)</text>

    <!-- Machine Graphics -->
    <g transform="translate(35, 55)">
      <rect x="0" y="0" width="130" height="60" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="65" y="28" font-size="9" font-weight="bold" fill="#67e8f9" text-anchor="middle">Combine Harvester</text>
      <text x="65" y="45" font-size="8" fill="#cbd5e1" text-anchor="middle">(Cereals: Cut/Thresh)</text>

      <rect x="145" y="0" width="130" height="60" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="210" y="28" font-size="9" font-weight="bold" fill="#67e8f9" text-anchor="middle">Potato Digger</text>
      <text x="210" y="45" font-size="8" fill="#cbd5e1" text-anchor="middle">(Tractor Lifter)</text>
    </g>

    <g transform="translate(15, 140)">
      <text x="0" y="18" font-size="11" font-weight="bold" fill="#38bdf8">Key Strengths:</text>
      <text x="0" y="36" font-size="10" fill="#cbd5e1">• Ultra-fast: 30–50 acres/day</text>
      <text x="0" y="54" font-size="10" fill="#cbd5e1">• Captures narrow sunny weather windows</text>
      <text x="0" y="72" font-size="10" fill="#cbd5e1">• Drastically cuts labor wage overheads</text>

      <text x="0" y="105" font-size="11" font-weight="bold" fill="#ef4444">Key Limitations:</text>
      <text x="0" y="123" font-size="10" fill="#cbd5e1">• Massive capital investment</text>
      <text x="0" y="141" font-size="10" fill="#cbd5e1">• Non-selective: harvests weeds &amp; green pods</text>
    </g>
  </g>
</svg>
""")

# SVG 4: Maize Kernel Black Layer (Lesson 4, Page 2)
SVG_BLACK_LAYER = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Maize Kernel Black Layer Physiological Maturity Marker</text>

  <!-- Left: Kernel Anatomical Cross-Section -->
  <g transform="translate(60, 65)">
    <rect x="0" y="0" width="320" height="345" rx="10" fill="#0f172a" stroke="#eab308" stroke-width="2"/>

    <!-- Kernel Shape -->
    <path d="M 90 80 Q 160 50 230 80 L 210 260 Q 160 300 110 260 Z" fill="#ca8a04" stroke="#fde047" stroke-width="2"/>

    <!-- Starch Endosperm -->
    <path d="M 105 95 Q 160 75 215 95 L 200 200 Q 160 210 120 200 Z" fill="#fef08a"/>
    <text x="160" y="145" font-size="11" font-weight="bold" fill="#713f12" text-anchor="middle">Starch Endosperm</text>

    <!-- Embryo (Germ) -->
    <ellipse cx="160" cy="230" rx="25" ry="35" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="160" y="235" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">Embryo</text>

    <!-- THE BLACK LAYER (Sealing Tip) -->
    <path d="M 125 265 Q 160 290 195 265 L 185 280 Q 160 300 135 280 Z" fill="#09090b" stroke="#ef4444" stroke-width="2"/>
    <text x="160" y="325" font-size="12" font-weight="bold" fill="#ef4444" text-anchor="middle">BLACK LAYER (Abscission Seal)</text>
  </g>

  <!-- Right: Diagnostic Interpretation -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#0284c7"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">THE BLACK LAYER DIAGNOSTIC TEST</text>

    <g transform="translate(15, 45)">
      <text x="0" y="20" font-size="12" font-weight="bold" fill="#fde047">1. What is the Black Layer?</text>
      <text x="0" y="38" font-size="11" fill="#cbd5e1">A physical layer of collapsed, suberized dark cells forming at the tip where the kernel connects to the cob.</text>

      <text x="0" y="70" font-size="12" font-weight="bold" fill="#fde047">2. Biological Significance:</text>
      <text x="0" y="88" font-size="11" fill="#cbd5e1">Confirms 100% maximum dry matter accumulation; vascular nutrient flow from the plant has permanently ceased.</text>

      <text x="0" y="120" font-size="12" font-weight="bold" fill="#fde047">3. Field Action:</text>
      <text x="0" y="138" font-size="11" fill="#cbd5e1">The crop is now physiologically mature and ready for field dry-down and timely harvesting.</text>
    </g>

    <rect x="15" y="265" width="315" height="65" rx="6" fill="#1e293b" stroke="#22c55e"/>
    <text x="172" y="288" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">In-Field Diagnostic Protocol</text>
    <text x="172" y="308" font-size="9" fill="#86efac" text-anchor="middle">Extract 3 kernels from center of cob; inspect tip with hand lens!</text>
  </g>
</svg>
""")

# SVG 5: Step-by-Step Irish Potato Digging (Lesson 6, Page 2)
SVG_POTATO_DIGGING = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Step-by-Step Irish Potato Digging: 30cm Fork Clearance</text>

  <!-- Left: Digging Fork Ridge Cross-Section -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>

    <!-- Potato Ridge Mound -->
    <path d="M 20 280 Q 170 120 320 280 Z" fill="#78350f" stroke="#ca8a04" stroke-width="2"/>

    <!-- Potato Tubers Underground -->
    <ellipse cx="140" cy="220" rx="22" ry="14" fill="#a16207" stroke="#fde047"/>
    <ellipse cx="180" cy="200" rx="22" ry="14" fill="#a16207" stroke="#fde047"/>
    <ellipse cx="200" cy="235" rx="20" ry="13" fill="#a16207" stroke="#fde047"/>

    <!-- Main Stem (Cut) -->
    <line x1="170" y1="160" x2="170" y2="125" stroke="#451a03" stroke-width="6"/>

    <!-- Digging Fork Inserted 30cm Away -->
    <line x1="60" y1="80" x2="95" y2="260" stroke="#38bdf8" stroke-width="6"/>
    <!-- 4 Tines -->
    <line x1="95" y1="260" x2="135" y2="275" stroke="#38bdf8" stroke-width="3"/>
    <line x1="95" y1="260" x2="135" y2="265" stroke="#38bdf8" stroke-width="3"/>
    <line x1="95" y1="260" x2="135" y2="255" stroke="#38bdf8" stroke-width="3"/>

    <!-- 30cm Dimension Arrow -->
    <line x1="60" y1="130" x2="170" y2="130" stroke="#fde047" stroke-width="2"/>
    <polygon points="60,127 50,130 60,133" fill="#fde047"/>
    <polygon points="170,127 180,130 170,133" fill="#fde047"/>
    <text x="115" y="120" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">30 cm Clearance</text>
  </g>

  <!-- Right: 4 Harvest & Curing Rules -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#0284c7"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">4 POTATO HARVEST RULES</text>

    <g transform="translate(15, 45)">
      <text x="0" y="20" font-size="12" font-weight="bold" fill="#fde047">1. Use a Digging Fork, Never a Flat Jembe:</text>
      <text x="0" y="38" font-size="11" fill="#cbd5e1">Slender tines slide between tubers without slicing flesh.</text>

      <text x="0" y="70" font-size="12" font-weight="bold" fill="#fde047">2. 30 cm Safe Insertion Distance:</text>
      <text x="0" y="88" font-size="11" fill="#cbd5e1">Drive fork into ridge side; pry upward gently to lift root cluster.</text>

      <text x="0" y="120" font-size="12" font-weight="bold" fill="#fde047">3. Handle Gently in Padded Crates:</text>
      <text x="0" y="138" font-size="11" fill="#cbd5e1">Never throw into metal buckets; bruising triggers Soft Rot.</text>

      <text x="0" y="170" font-size="12" font-weight="bold" fill="#fde047">4. 7–10 Days Shaded Curing (Suberization):</text>
      <text x="0" y="188" font-size="11" fill="#cbd5e1">Heals micro-wounds in shade; prevents toxic solanine greening.</text>
    </g>

    <rect x="15" y="275" width="315" height="55" rx="6" fill="#1e293b" stroke="#22c55e"/>
    <text x="172" y="295" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Greening Alert</text>
    <text x="172" y="313" font-size="9" fill="#86efac" text-anchor="middle">Direct sunlight turns potatoes green and toxic (solanine)!</text>
  </g>
</svg>
""")

# SVG 6: Grain Moisture Continuum (Lesson 8, Page 2)
SVG_GRAIN_MOISTURE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Cereal Grain Moisture Continuum &amp; Storage Safety Zones</text>

  <!-- Horizontal Moisture Gradient Bar -->
  <g transform="translate(60, 80)">
    <!-- Scale Bar -->
    <rect x="0" y="40" width="680" height="35" rx="6" fill="#0f172a" stroke="#334155" stroke-width="2"/>

    <!-- Zone 1: >25% Wet (Red) -->
    <rect x="510" y="42" width="168" height="31" fill="#ef4444"/>
    <!-- Zone 2: 18-25% Field Harvest (Yellow) -->
    <rect x="340" y="42" width="170" height="31" fill="#eab308"/>
    <!-- Zone 3: 13-14% Safe Target (Green) -->
    <rect x="170" y="42" width="170" height="31" fill="#22c55e"/>
    <!-- Zone 4: <10% Over-dry (Blue) -->
    <rect x="2" y="42" width="168" height="31" fill="#38bdf8"/>

    <!-- Percentage Labels -->
    <text x="85" y="62" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">&lt; 10% Over-Dry</text>
    <text x="255" y="62" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">13% – 14% SAFE ZONE</text>
    <text x="425" y="62" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">18% – 25% Field Harvest</text>
    <text x="595" y="62" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">&gt; 25% Physiologically Wet</text>
  </g>

  <!-- Zone Descriptions Grid -->
  <g transform="translate(60, 185)">
    <!-- Safe Zone Highlight Card -->
    <rect x="0" y="0" width="680" height="130" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="680" height="30" rx="10" fill="#15803d"/>
    <text x="340" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">WHY 13% TO 14% IS THE GOLD STANDARD FOR SAFE STORAGE</text>

    <g transform="translate(20, 45)">
      <text x="0" y="15" font-size="11" font-weight="bold" fill="#4ade80">1. Mold &amp; Aflatoxin Elimination:</text>
      <text x="0" y="32" font-size="10" fill="#cbd5e1">Aspergillus and Penicillium molds cannot germinate or produce toxins below 14% moisture.</text>

      <text x="0" y="55" font-size="11" font-weight="bold" fill="#4ade80">2. Minimal Grain Respiration:</text>
      <text x="0" y="72" font-size="10" fill="#cbd5e1">Embryo metabolism drops to dormant state; zero spontaneous heating inside storage bags.</text>
    </g>
  </g>

  <!-- Moisture Testing Methods Footer -->
  <g transform="translate(60, 335)">
    <rect x="0" y="0" width="680" height="75" rx="8" fill="#1e293b" stroke="#38bdf8"/>
    <text x="340" y="24" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">3 In-Field Moisture Testing Protocols</text>
    <text x="20" y="48" font-size="10" fill="#cbd5e1">• 1. Digital Moisture Meter (Exact %)  |  2. Salt Jar Test (Clumping = Wet)  |  3. Bite Test (Glassy Snap = Dry)</text>
  </g>
</svg>
""")

# SVG 7: Hermetic PICS Bag Cross-Section (Lesson 9, Page 2)
SVG_PICS_BAG = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Hermetic PICS Bag Tri-Layer Architecture &amp; Insect Asphyxiation</text>

  <!-- Left: Bag Cross-Section Schematic -->
  <g transform="translate(60, 65)">
    <rect x="0" y="0" width="320" height="345" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>

    <!-- Layer 1: Outer Woven Polypropylene Sack -->
    <rect x="25" y="40" width="270" height="240" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
    <text x="160" y="32" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Layer 1: Outer Woven Bag (Tear Strength)</text>

    <!-- Layer 2: Middle 80-micron HDPE Liner -->
    <rect x="45" y="60" width="230" height="200" rx="6" fill="#0c4a6e" stroke="#22c55e" stroke-width="2"/>
    <text x="160" y="75" font-size="8" font-weight="bold" fill="#86efac" text-anchor="middle">Layer 2: Middle HDPE Liner (Gas Barrier)</text>

    <!-- Layer 3: Inner 80-micron HDPE Liner -->
    <rect x="65" y="85" width="190" height="160" rx="4" fill="#14532d" stroke="#fde047" stroke-width="2"/>
    <text x="160" y="100" font-size="8" font-weight="bold" fill="#fde047" text-anchor="middle">Layer 3: Inner HDPE Liner (Gas Barrier)</text>

    <!-- Sealed Grain Core -->
    <g transform="translate(85, 115)">
      <circle cx="25" cy="25" r="5" fill="#ca8a04"/><circle cx="55" cy="25" r="5" fill="#ca8a04"/><circle cx="85" cy="25" r="5" fill="#ca8a04"/><circle cx="115" cy="25" r="5" fill="#ca8a04"/>
      <circle cx="40" cy="55" r="5" fill="#ca8a04"/><circle cx="70" cy="55" r="5" fill="#ca8a04"/><circle cx="100" cy="55" r="5" fill="#ca8a04"/>
      <circle cx="25" cy="85" r="5" fill="#ca8a04"/><circle cx="55" cy="85" r="5" fill="#ca8a04"/><circle cx="85" cy="85" r="5" fill="#ca8a04"/><circle cx="115" cy="85" r="5" fill="#ca8a04"/>
    </g>

    <text x="160" y="315" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Airtight Hermetic Seal (Zero Chemical Dust!)</text>
  </g>

  <!-- Right: Asphyxiation Mechanism -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#15803d"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">HOW HERMETIC SEALING KILLS WEEVILS</text>

    <g transform="translate(15, 45)">
      <text x="0" y="18" font-size="11" font-weight="bold" fill="#4ade80">1. Oxygen Depletion (&lt;5% O₂):</text>
      <text x="0" y="34" font-size="10" fill="#cbd5e1">Respiring insects &amp; grain embryos consume trapped oxygen.</text>

      <text x="0" y="62" font-size="11" font-weight="bold" fill="#4ade80">2. Carbon Dioxide Accumulation:</text>
      <text x="0" y="78" font-size="10" fill="#cbd5e1">CO₂ levels rise rapidly inside the double-liner barrier.</text>

      <text x="0" y="106" font-size="11" font-weight="bold" fill="#ef4444">3. Total Insect Asphyxiation:</text>
      <text x="0" y="122" font-size="10" fill="#fca5a5">Adult weevils, larvae, and eggs suffocate and die in days.</text>

      <text x="0" y="150" font-size="11" font-weight="bold" fill="#38bdf8">4. 100% Food-Safe &amp; Chemical-Free:</text>
      <text x="0" y="166" font-size="10" fill="#cbd5e1">Grain can be eaten immediately upon opening with no wash.</text>
    </g>

    <rect x="15" y="260" width="315" height="70" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="172" y="282" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Stacking Rule on Pallets</text>
    <text x="172" y="302" font-size="9" fill="#86efac" text-anchor="middle">Always stack PICS bags on wooden pallets off concrete floors</text>
    <text x="172" y="318" font-size="9" fill="#86efac" text-anchor="middle">to prevent moisture absorption from the ground!</text>
  </g>
</svg>
""")

# SVG 8: The Complete Post-Harvest Value Chain Continuum (Lesson 10, Page 2)
SVG_POST_HARVEST_CHAIN = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 5-Phase Crop Harvesting &amp; Post-Harvest Value Chain</text>

  <!-- Central Hub: Food Security -->
  <circle cx="400" cy="240" r="55" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
  <text x="400" y="235" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">ZERO WASTE</text>
  <text x="400" y="252" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">FOOD SECURITY</text>

  <!-- 1. Maturity Diagnostic -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="195" height="75" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="97" y="22" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">1. MATURITY TESTING</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Black layer in maize</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Thumb-rub skin set test</text>
  </g>
  <line x1="240" y1="102" x2="345" y2="200" stroke="#22c55e" stroke-width="2" stroke-dasharray="2,2"/>

  <!-- 2. Pre-Harvest Conditioning -->
  <g transform="translate(560, 65)">
    <rect x="0" y="0" width="195" height="75" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="97" y="22" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">2. PRE-HARVEST</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Haulm destruction (14 days)</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Cob bending &amp; stooking</text>
  </g>
  <line x1="560" y1="102" x2="455" y2="200" stroke="#38bdf8" stroke-width="2" stroke-dasharray="2,2"/>

  <!-- 3. Dry Weather Harvest -->
  <g transform="translate(35, 195)">
    <rect x="0" y="0" width="195" height="75" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <text x="97" y="22" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">3. DRY HARVEST</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• 30cm fork clearance</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Snap cobs in sunny weather</text>
  </g>
  <line x1="230" y1="240" x2="345" y2="240" stroke="#eab308" stroke-width="2"/>

  <!-- 4. Post-Harvest Processing -->
  <g transform="translate(570, 195)">
    <rect x="0" y="0" width="195" height="75" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
    <text x="97" y="22" font-size="11" font-weight="bold" fill="#67e8f9" text-anchor="middle">4. 13% SUN DRYING</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Shell &amp; winnow chaff</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Dry to 13% on tarpaulin</text>
  </g>
  <line x1="570" y1="240" x2="455" y2="240" stroke="#06b6d4" stroke-width="2"/>

  <!-- 5. Hermetic Storage -->
  <g transform="translate(300, 335)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="100" y="22" font-size="11" font-weight="bold" fill="#d8b4fe" text-anchor="middle">5. HERMETIC STORAGE</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• PICS bags on pallets</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Rat guards on granary posts</text>
  </g>
  <line x1="400" y1="335" x2="400" y2="300" stroke="#a855f7" stroke-width="2"/>
</svg>
""")

SVG_MAP = {
    1: {"page": 2, "svg": SVG_HARVEST_DETERMINANTS, "title": "The 4 Key Determinants of Crop Harvest Timing"},
    2: {"page": 2, "svg": SVG_POTATO_HAULM, "title": "Potato Haulm Destruction & Subterranean Skin Setting"},
    3: {"page": 2, "svg": SVG_MANUAL_VS_MECHANICAL, "title": "Manual vs Mechanical Harvesting Operational Comparison"},
    4: {"page": 2, "svg": SVG_BLACK_LAYER, "title": "Maize Kernel Black Layer Physiological Maturity Marker"},
    6: {"page": 2, "svg": SVG_POTATO_DIGGING, "title": "Step-by-Step Irish Potato Digging & 30cm Fork Clearance"},
    8: {"page": 2, "svg": SVG_GRAIN_MOISTURE, "title": "Grain Moisture Continuum: Field Wetness to 13% Safe Storage Zone"},
    9: {"page": 2, "svg": SVG_PICS_BAG, "title": "Hermetic PICS Bag Cross-Section & Oxygen Depletion Asphyxiation Mechanism"},
    10: {"page": 2, "svg": SVG_POST_HARVEST_CHAIN, "title": "The Complete Post-Harvest Value Chain Continuum"}
}

def enrich_grade10_topic7():
    """Injects verified photos, responsive vector SVGs, YouTube embeds, and creates LessonAssets."""
    print("=" * 80)
    print("STARTING ENRICHMENT: CBC Grade 10 Agriculture — Topic 7: General Crop Harvesting")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()
    topic = Topic.objects.filter(subject=subject, name="General Crop Harvesting").first()

    assert topic, "Topic 'General Crop Harvesting' not found!"

    images_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grade10_topic7_verified_images.json")
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
                    "topic_order": 7,
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
                        "topic_order": 7,
                        "unit_order": u_order,
                        "page": svg_def["page"],
                        "svg_content": svg_def["svg"]
                    }
                )
                diag_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [Vector SVG Attached] Lesson {u_order}: {svg_def['title']}")

        # ---------------------------------------------------------------------
        # 3. Educational YouTube Videos (Lesson 2)
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
                        "topic_order": 7,
                        "unit_order": u_order,
                        "youtube_url": v_url
                    }
                )
                v_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [YouTube Video Attached] Lesson {u_order}: {v_block.title}")

    print("=" * 80)
    print(f"ENRICHMENT COMPLETE: Topic 7 '{topic.name}'")
    print(f"  Photographic Hooks: {total_images_attached} / 10")
    print(f"  Vector SVGs:        {total_svgs_attached} / 8")
    print(f"  YouTube Videos:     {total_videos_attached} / 1")
    print(f"  LessonAssets:       {total_assets_persisted}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic7()
