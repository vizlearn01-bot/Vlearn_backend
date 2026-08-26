"""
VLearn CBC Grade 10 Agriculture — Topic 17: Composting
Visual Enrichment Engine (Phase 2: Vector SVGs, Verified Photos & Asset Persistence)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Composting (Order: 17)

Attaches:
  - 10 First-Card Photographic Visual Hooks (100% Tested HTTP 200 Direct Wikimedia URLs)
  - 8 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - 2 Verified Educational YouTube Videos (Lesson 4 Card 3 & Lesson 7 Card 3)
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade10_agriculture_topic17.py
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
# 8 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 17: COMPOSTING
# =============================================================================

# SVG 1: Physical Indicators of Fully Mature Compost (Lesson 1, Page 2)
SVG_COMPOST_MATURITY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Physical Indicators of Fully Mature Organic Compost</text>

  <!-- Central Hub: Mature Compost Sample -->
  <circle cx="400" cy="225" r="75" fill="#0f172a" stroke="#22c55e" stroke-width="3"/>
  <text x="400" y="215" font-size="12" font-weight="bold" fill="#4ade80" text-anchor="middle">MATURE</text>
  <text x="400" y="235" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">ORGANIC</text>
  <text x="400" y="255" font-size="11" font-weight="bold" fill="#86efac" text-anchor="middle">COMPOST</text>

  <!-- 4 Diagnostic Indicators -->
  <!-- 1. Color (Top-Left) -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="220" height="110" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="110" y="25" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. RICH DARK COLOR</text>
    <text x="15" y="52" font-size="9" fill="#cbd5e1">• Deep dark brown to jet black</text>
    <text x="15" y="72" font-size="9" fill="#cbd5e1">• Resembles fertile forest humus</text>
    <text x="15" y="92" font-size="9" font-weight="bold" fill="#67e8f9">• Zero raw un-rotted plant colors</text>
  </g>
  <line x1="265" y1="120" x2="335" y2="185" stroke="#38bdf8" stroke-width="2"/>

  <!-- 2. Texture (Top-Right) -->
  <g transform="translate(535, 65)">
    <rect x="0" y="0" width="220" height="110" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="110" y="25" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">2. CRUMBLY TEXTURE</text>
    <text x="15" y="52" font-size="9" fill="#cbd5e1">• Fine, loose, homogeneous structure</text>
    <text x="15" y="72" font-size="9" fill="#cbd5e1">• Individual scraps indistinguishable</text>
    <text x="15" y="92" font-size="9" font-weight="bold" fill="#86efac">• Crumbles smoothly in hand</text>
  </g>
  <line x1="535" y1="120" x2="465" y2="185" stroke="#22c55e" stroke-width="2"/>

  <!-- 3. Odor (Bottom-Left) -->
  <g transform="translate(45, 275)">
    <rect x="0" y="0" width="220" height="110" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <text x="110" y="25" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">3. EARTHY ODOR</text>
    <text x="15" y="52" font-size="9" fill="#cbd5e1">• Pleasant, sweet forest floor aroma</text>
    <text x="15" y="72" font-size="9" fill="#cbd5e1">• Zero ammonia or vinegar sharpness</text>
    <text x="15" y="92" font-size="9" font-weight="bold" fill="#fef08a">• Zero rotten egg (H2S) smell</text>
  </g>
  <line x1="265" y1="330" x2="335" y2="265" stroke="#eab308" stroke-width="2"/>

  <!-- 4. Temperature (Bottom-Right) -->
  <g transform="translate(535, 275)">
    <rect x="0" y="0" width="220" height="110" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="110" y="25" font-size="11" font-weight="bold" fill="#d8b4fe" text-anchor="middle">4. COOL TEMPERATURE</text>
    <text x="15" y="52" font-size="9" fill="#cbd5e1">• Ambient air temperature (~20-25°C)</text>
    <text x="15" y="72" font-size="9" fill="#cbd5e1">• Thermophilic heating has ended</text>
    <text x="15" y="92" font-size="9" font-weight="bold" fill="#e9d5ff">• Safe for root contact without burn</text>
  </g>
  <line x1="535" y1="330" x2="465" y2="265" stroke="#a855f7" stroke-width="2"/>

  <!-- Bottom Synthesis Banner -->
  <g transform="translate(45, 395)">
    <rect x="0" y="0" width="710" height="30" rx="6" fill="#0f172a" stroke="#22c55e"/>
    <text x="355" y="20" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Safe for Seedbeds: Completely stable, nutrient-dense humus ready for crop absorption</text>
  </g>
</svg>
""")

# SVG 2: Factors Determining Quality (Lesson 2, Page 2)
SVG_QUALITY_FACTORS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Key Factors Determining Compost Quality &amp; Microbial Activity</text>

  <!-- 4 Core Columns -->
  <!-- 1. C:N Balance -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="165" height="260" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="165" height="28" rx="8" fill="#0284c7"/>
    <text x="82" y="19" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">1. C:N RATIO (30:1)</text>
    <text x="10" y="50" font-size="8" font-weight="bold" fill="#38bdf8">• 30:1 Golden Rule</text>
    <text x="10" y="68" font-size="8" fill="#cbd5e1">• Browns (Carbon):</text>
    <text x="10" y="84" font-size="8" fill="#cbd5e1">  Dry stalks, straw</text>
    <text x="10" y="106" font-size="8" fill="#cbd5e1">• Greens (Nitrogen):</text>
    <text x="10" y="122" font-size="8" fill="#cbd5e1">  Fresh weeds, dung</text>
    <rect x="10" y="195" width="145" height="50" rx="4" fill="#1e293b" stroke="#38bdf8"/>
    <text x="82" y="216" font-size="8" font-weight="bold" fill="#67e8f9" text-anchor="middle">High C = Slow decay</text>
    <text x="82" y="232" font-size="8" font-weight="bold" fill="#f87171" text-anchor="middle">High N = Ammonia loss</text>
  </g>

  <!-- 2. Moisture Control -->
  <g transform="translate(225, 65)">
    <rect x="0" y="0" width="165" height="260" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
    <rect x="0" y="0" width="165" height="28" rx="8" fill="#0891b2"/>
    <text x="82" y="19" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">2. MOISTURE (50-60%)</text>
    <text x="10" y="50" font-size="8" font-weight="bold" fill="#67e8f9">• Sponge Standard</text>
    <text x="10" y="68" font-size="8" fill="#cbd5e1">• Damp to touch</text>
    <text x="10" y="84" font-size="8" fill="#cbd5e1">• 1-2 drops under grip</text>
    <text x="10" y="106" font-size="8" fill="#cbd5e1">• Water film feeds</text>
    <text x="10" y="122" font-size="8" fill="#cbd5e1">  microbial life</text>
    <rect x="10" y="195" width="145" height="50" rx="4" fill="#1e293b" stroke="#06b6d4"/>
    <text x="82" y="216" font-size="8" font-weight="bold" fill="#f87171" text-anchor="middle">&lt;30% = Dormancy</text>
    <text x="82" y="232" font-size="8" font-weight="bold" fill="#f87171" text-anchor="middle">&gt;70% = Waterlogged</text>
  </g>

  <!-- 3. Aeration & Turning -->
  <g transform="translate(405, 65)">
    <rect x="0" y="0" width="165" height="260" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="165" height="28" rx="8" fill="#15803d"/>
    <text x="82" y="19" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">3. AERATION (OXYGEN)</text>
    <text x="10" y="50" font-size="8" font-weight="bold" fill="#4ade80">• Aerobic Respiration</text>
    <text x="10" y="68" font-size="8" fill="#cbd5e1">• Regular turning</text>
    <text x="10" y="84" font-size="8" fill="#cbd5e1">  introduces fresh O2</text>
    <text x="10" y="106" font-size="8" fill="#cbd5e1">• Coarse base prevents</text>
    <text x="10" y="122" font-size="8" fill="#cbd5e1">  bottom compaction</text>
    <rect x="10" y="195" width="145" height="50" rx="4" fill="#1e293b" stroke="#22c55e"/>
    <text x="82" y="216" font-size="8" font-weight="bold" fill="#4ade80" text-anchor="middle">Aerobic = Odor-free</text>
    <text x="82" y="232" font-size="8" font-weight="bold" fill="#f87171" text-anchor="middle">Anaerobic = Foul H2S</text>
  </g>

  <!-- 4. Thermophilic Temperature -->
  <g transform="translate(585, 65)">
    <rect x="0" y="0" width="165" height="260" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <rect x="0" y="0" width="165" height="28" rx="8" fill="#ca8a04"/>
    <text x="82" y="19" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">4. TEMP (55-65°C)</text>
    <text x="10" y="50" font-size="8" font-weight="bold" fill="#fde047">• Sanitizing Hot Zone</text>
    <text x="10" y="68" font-size="8" fill="#cbd5e1">• Kills weed seeds</text>
    <text x="10" y="84" font-size="8" fill="#cbd5e1">• Destroys pathogens</text>
    <text x="10" y="100" font-size="8" fill="#cbd5e1">  (e.g., blight, E. coli)</text>
    <text x="10" y="122" font-size="8" fill="#cbd5e1">• Must stay &lt;70°C</text>
    <rect x="10" y="195" width="145" height="50" rx="4" fill="#1e293b" stroke="#eab308"/>
    <text x="82" y="216" font-size="8" font-weight="bold" fill="#4ade80" text-anchor="middle">Pasteurizes Waste</text>
    <text x="82" y="232" font-size="8" font-weight="bold" fill="#fef08a" text-anchor="middle">pH 6.0-7.0 Buffered</text>
  </g>

  <!-- Bottom Synthesis Banner -->
  <g transform="translate(45, 340)">
    <rect x="0" y="0" width="705" height="70" rx="8" fill="#0f172a" stroke="#38bdf8"/>
    <text x="352" y="26" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Composting Formula: Biological Balance Multiplies Soil Wealth</text>
    <text x="352" y="50" font-size="9" fill="#cbd5e1" text-anchor="middle">Proper management of C:N, moisture, oxygen, and temperature guarantees pathogen-free, highly fertile manure in 8-12 weeks.</text>
  </g>
</svg>
""")

# SVG 3: Four-Pit System Layout (Lesson 4, Page 2)
SVG_FOUR_PIT_LAYOUT = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Four-Pit Composting System Layout &amp; Directional Flow</text>

  <!-- 4 Sequential Pits (1.2m x 1.2m x 1.2m) -->
  <!-- Pit 1 -->
  <g transform="translate(45, 75)">
    <rect x="0" y="0" width="150" height="190" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="150" height="28" rx="8" fill="#991b1b"/>
    <text x="75" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">PIT 1: LAYERING</text>
    <text x="10" y="48" font-size="8" fill="#cbd5e1">• Fresh Raw Waste</text>
    <text x="10" y="65" font-size="8" fill="#cbd5e1">• Sequential Layers:</text>
    <text x="10" y="80" font-size="8" fill="#cbd5e1">  15cm Coarse Base</text>
    <text x="10" y="95" font-size="8" fill="#cbd5e1">  10cm Browns &amp; Greens</text>
    <text x="10" y="110" font-size="8" fill="#cbd5e1">  5cm Dung &amp; Ash</text>
    <text x="10" y="125" font-size="8" fill="#cbd5e1">  2cm Topsoil + Water</text>
    <rect x="10" y="145" width="130" height="35" rx="4" fill="#1e293b" stroke="#ef4444"/>
    <text x="75" y="167" font-size="9" font-weight="bold" fill="#f87171" text-anchor="middle">Weeks 1 - 3 (Heat 1)</text>
  </g>
  <line x1="195" y1="170" x2="235" y2="170" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="225,165 235,170 225,175" fill="#38bdf8"/>

  <!-- Pit 2 -->
  <g transform="translate(235, 75)">
    <rect x="0" y="0" width="150" height="190" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <rect x="0" y="0" width="150" height="28" rx="8" fill="#ca8a04"/>
    <text x="75" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">PIT 2: FIRST TURN</text>
    <text x="10" y="48" font-size="8" fill="#cbd5e1">• Shifted from Pit 1</text>
    <text x="10" y="65" font-size="8" fill="#cbd5e1">• Re-aeration of core</text>
    <text x="10" y="82" font-size="8" fill="#cbd5e1">• Second Heat Cycle</text>
    <text x="10" y="100" font-size="8" fill="#cbd5e1">• Volume reduces by 30%</text>
    <rect x="10" y="145" width="130" height="35" rx="4" fill="#1e293b" stroke="#eab308"/>
    <text x="75" y="167" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">Weeks 4 - 6 (Heat 2)</text>
  </g>
  <line x1="385" y1="170" x2="425" y2="170" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="415,165 425,170 415,175" fill="#38bdf8"/>

  <!-- Pit 3 -->
  <g transform="translate(425, 75)">
    <rect x="0" y="0" width="150" height="190" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="150" height="28" rx="8" fill="#0284c7"/>
    <text x="75" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">PIT 3: SECOND TURN</text>
    <text x="10" y="48" font-size="8" fill="#cbd5e1">• Shifted from Pit 2</text>
    <text x="10" y="65" font-size="8" fill="#cbd5e1">• Deep fiber breakdown</text>
    <text x="10" y="82" font-size="8" fill="#cbd5e1">• Actinomycete colonization</text>
    <text x="10" y="100" font-size="8" fill="#cbd5e1">• Color turns dark brown</text>
    <rect x="10" y="145" width="130" height="35" rx="4" fill="#1e293b" stroke="#38bdf8"/>
    <text x="75" y="167" font-size="9" font-weight="bold" fill="#67e8f9" text-anchor="middle">Weeks 7 - 9 (Curing)</text>
  </g>
  <line x1="575" y1="170" x2="615" y2="170" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="605,165 615,170 605,175" fill="#38bdf8"/>

  <!-- Pit 4 -->
  <g transform="translate(615, 75)">
    <rect x="0" y="0" width="140" height="190" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="140" height="28" rx="8" fill="#15803d"/>
    <text x="70" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">PIT 4: HARVEST</text>
    <text x="10" y="48" font-size="8" fill="#cbd5e1">• Mature Humus</text>
    <text x="10" y="65" font-size="8" fill="#cbd5e1">• Cool &amp; Crumbly</text>
    <text x="10" y="82" font-size="8" fill="#cbd5e1">• Earthy Forest Smell</text>
    <text x="10" y="100" font-size="8" fill="#cbd5e1">• Ready for Fields</text>
    <rect x="10" y="145" width="120" height="35" rx="4" fill="#1e293b" stroke="#22c55e"/>
    <text x="70" y="167" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">Weeks 10 - 12</text>
  </g>

  <!-- Bottom Dimensions & Operational Guidance -->
  <g transform="translate(45, 280)">
    <rect x="0" y="0" width="710" height="135" rx="8" fill="#0f172a" stroke="#334155"/>
    <text x="20" y="25" font-size="10" font-weight="bold" fill="#38bdf8">Engineering Dimensions &amp; Continuous Production Logic:</text>
    <text x="20" y="48" font-size="9" fill="#cbd5e1">• Pit Dimensions: Exactly 1.2 meters wide x 1.2 meters long x 1.2 meters deep, spaced 0.5 meters apart.</text>
    <text x="20" y="68" font-size="9" fill="#cbd5e1">• Continuous Supply: When Pit 1 is emptied into Pit 2 at Week 4, Pit 1 is immediately reloaded with fresh waste.</text>
    <text x="20" y="88" font-size="9" fill="#cbd5e1">• By Week 12, a farm harvests 1.5 to 2.0 tonnes of mature compost every 3 weeks continuously!</text>
    <text x="20" y="112" font-size="9" font-weight="bold" fill="#4ade80">Saves up to 100% of Farm Synthetic Fertilizer Expenditure Annually</text>
  </g>
</svg>
""")

# SVG 4: Shifting Schedule (Lesson 5, Page 2)
SVG_SHIFTING_SCHEDULE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Chronological Shifting Schedule of the Four-Pit System</text>

  <!-- Timeline Flow Across 12 Weeks -->
  <g transform="translate(45, 65)">
    <!-- Stage 1: Weeks 1-3 -->
    <rect x="0" y="0" width="710" height="70" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="15" y="24" font-size="10" font-weight="bold" fill="#f87171">STAGE 1 (WEEKS 1 - 3): INITIAL FILLING &amp; FIRST HEAT CYCLE</text>
    <text x="15" y="48" font-size="9" fill="#cbd5e1">Pit 1 is loaded with raw layered wastes. Internal thermophilic temperature surges to 60°C.</text>
    <rect x="580" y="15" width="115" height="40" rx="4" fill="#1e293b" stroke="#ef4444"/>
    <text x="637" y="39" font-size="9" font-weight="bold" fill="#f87171" text-anchor="middle">Pit 1 Active</text>
  </g>

  <g transform="translate(45, 145)">
    <!-- Stage 2: Weeks 4-6 -->
    <rect x="0" y="0" width="710" height="70" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <text x="15" y="24" font-size="10" font-weight="bold" fill="#fde047">STAGE 2 (WEEKS 4 - 6): FIRST SHIFT (PIT 1 -> PIT 2)</text>
    <text x="15" y="48" font-size="9" fill="#cbd5e1">Contents of Pit 1 shoveled into Pit 2 (aerating core). Pit 1 is reloaded with new batch of farm wastes.</text>
    <rect x="580" y="15" width="115" height="40" rx="4" fill="#1e293b" stroke="#eab308"/>
    <text x="637" y="39" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">Pit 1 &amp; 2 Active</text>
  </g>

  <g transform="translate(45, 225)">
    <!-- Stage 3: Weeks 7-9 -->
    <rect x="0" y="0" width="710" height="70" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="15" y="24" font-size="10" font-weight="bold" fill="#38bdf8">STAGE 3 (WEEKS 7 - 9): SECOND SHIFT (PIT 2 -> PIT 3, PIT 1 -> PIT 2)</text>
    <text x="15" y="48" font-size="9" fill="#cbd5e1">Batch 1 moves into Pit 3. Batch 2 moves into Pit 2. Pit 1 is reloaded with Batch 3.</text>
    <rect x="580" y="15" width="115" height="40" rx="4" fill="#1e293b" stroke="#38bdf8"/>
    <text x="637" y="39" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Pits 1, 2, 3 Active</text>
  </g>

  <g transform="translate(45, 305)">
    <!-- Stage 4: Weeks 10-12 -->
    <rect x="0" y="0" width="710" height="70" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <text x="15" y="24" font-size="10" font-weight="bold" fill="#4ade80">STAGE 4 (WEEKS 10 - 12): THIRD SHIFT &amp; MATURE HARVEST (PIT 4)</text>
    <text x="15" y="48" font-size="9" fill="#cbd5e1">Batch 1 reaches Pit 4: cool, dark, crumbly manure harvested for field application. Pipeline repeats indefinitely!</text>
    <rect x="580" y="15" width="115" height="40" rx="4" fill="#1e293b" stroke="#22c55e"/>
    <text x="637" y="39" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">Pit 4 Harvest!</text>
  </g>

  <!-- Bottom Synthesis Banner -->
  <g transform="translate(45, 390)">
    <text x="355" y="20" font-size="10" font-weight="bold" fill="#86efac" text-anchor="middle">Turning every 3-4 weeks aerates the core, pasteurizes weeds, and guarantees uniform decay</text>
  </g>
</svg>
""")

# SVG 5: Above-Ground Stack Architecture (Lesson 6, Page 2)
SVG_HEAP_STACK = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Step-by-Step Above-Ground Compost Heap Architecture</text>

  <!-- Stack Diagram Cross-Section -->
  <g transform="translate(100, 70)">
    <!-- Base Ground Line -->
    <line x1="0" y1="280" x2="600" y2="280" stroke="#94a3b8" stroke-width="3"/>
    <text x="300" y="305" font-size="9" fill="#cbd5e1" text-anchor="middle">Level, Well-Drained Soil Base (1.0m x 1.0m)</text>

    <!-- Layer 1: Coarse Base (20cm) -->
    <rect x="80" y="235" width="440" height="45" fill="#78350f" stroke="#92400e"/>
    <text x="300" y="262" font-size="9" font-weight="bold" fill="#fef3c7" text-anchor="middle">1. COARSE BASE (15-20cm): Woody Twigs &amp; Maize Stalks (Air Ventilator)</text>

    <!-- Layer 2: Carbon Browns (10cm) -->
    <rect x="100" y="195" width="400" height="40" fill="#92400e" stroke="#b45309"/>
    <text x="300" y="220" font-size="9" fill="#fef3c7" text-anchor="middle">2. CARBON BROWNS (10cm): Dry Grass, Straw, Dry Leaves</text>

    <!-- Layer 3: Nitrogen Greens (10cm) -->
    <rect x="120" y="155" width="360" height="40" fill="#15803d" stroke="#16a34a"/>
    <text x="300" y="180" font-size="9" fill="#ffffff" text-anchor="middle">3. NITROGEN GREENS (10cm): Fresh Weeds &amp; Kitchen Scraps</text>

    <!-- Layer 4: Dung & Ash (5cm) -->
    <rect x="140" y="125" width="320" height="30" fill="#3f3f46" stroke="#52525b"/>
    <text x="300" y="145" font-size="8" font-weight="bold" fill="#e4e4e7" text-anchor="middle">4. ANIMAL DUNG (5cm) + WOOD ASH DUSTING (Potassium/Buffer)</text>

    <!-- Layer 5: Topsoil Inoculant (2cm) -->
    <rect x="160" y="105" width="280" height="20" fill="#1c1917" stroke="#292524"/>
    <text x="300" y="119" font-size="8" fill="#a8a29e" text-anchor="middle">5. FERTILE TOPSOIL (2cm): Active Microbial Inoculant</text>

    <!-- Protective Top Cover (Gunny Sacks / Dry Grass) -->
    <path d="M 160 105 Q 300 65 440 105" fill="none" stroke="#22c55e" stroke-width="4"/>
    <text x="300" y="85" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">PROTECTIVE COVER: Old Gunny Sacks / Dry Grass (Retains Moisture &amp; Heat)</text>

    <!-- Central Monitoring Stick -->
    <line x1="300" y1="50" x2="300" y2="245" stroke="#ef4444" stroke-width="3" stroke-dasharray="4,4"/>
    <text x="310" y="65" font-size="8" font-weight="bold" fill="#f87171">Diagnostic Stick</text>
  </g>

  <!-- Bottom Synthesis Banner -->
  <g transform="translate(45, 385)">
    <rect x="0" y="0" width="710" height="40" rx="6" fill="#0f172a" stroke="#22c55e"/>
    <text x="355" y="24" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Above-Ground Heaps excel in wet climates: Superior aeration, easy turning, and zero waterlogging!</text>
  </g>
</svg>
""")

# SVG 6: Vermicomposting Bin Ecosystem (Lesson 7, Page 2)
SVG_VERMICOMPOST_BIN = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Vermicomposting Bin Ecosystem (Red Wigglers &amp; Castings)</text>

  <!-- Vermi-Bin Container Architecture -->
  <g transform="translate(60, 65)">
    <rect x="0" y="0" width="360" height="270" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>

    <!-- Lid with Air Vents -->
    <rect x="10" y="10" width="340" height="35" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <circle cx="50" cy="27" r="4" fill="#38bdf8"/>
    <circle cx="100" cy="27" r="4" fill="#38bdf8"/>
    <circle cx="150" cy="27" r="4" fill="#38bdf8"/>
    <circle cx="200" cy="27" r="4" fill="#38bdf8"/>
    <circle cx="250" cy="27" r="4" fill="#38bdf8"/>
    <circle cx="300" cy="27" r="4" fill="#38bdf8"/>
    <text x="175" y="22" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">LID WITH TOP AIR VENTILATION HOLES</text>

    <!-- Layer 1: Food Scrap Feeding Zone -->
    <rect x="15" y="55" width="330" height="50" rx="4" fill="#166534" stroke="#22c55e"/>
    <text x="180" y="85" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">FOOD SCRAPS: Fruit &amp; Veg Peels (No Citrus / Onions!)</text>

    <!-- Layer 2: Moist Shredded Bedding with Worms -->
    <rect x="15" y="115" width="330" height="75" rx="4" fill="#854d0e" stroke="#ca8a04"/>
    <text x="180" y="145" font-size="9" font-weight="bold" fill="#fef08a" text-anchor="middle">MOIST BEDDING: Shredded Paper / Coir (Wrung-out Sponge)</text>
    <text x="180" y="165" font-size="9" font-weight="bold" fill="#f87171" text-anchor="middle">Red Wiggler Earthworms (Eisenia fetida)</text>

    <!-- Layer 3: Pure Worm Castings Base -->
    <rect x="15" y="200" width="330" height="50" rx="4" fill="#18181b" stroke="#3f3f46"/>
    <text x="180" y="230" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">PURE WORM CASTINGS (Granular Black Biofertilizer)</text>

    <!-- Base Drainage Holes -->
    <circle cx="60" cy="260" r="3" fill="#38bdf8"/>
    <circle cx="120" cy="260" r="3" fill="#38bdf8"/>
    <circle cx="180" cy="260" r="3" fill="#38bdf8"/>
    <circle cx="240" cy="260" r="3" fill="#38bdf8"/>
    <circle cx="300" cy="260" r="3" fill="#38bdf8"/>
  </g>

  <!-- Right Features & Nutritional Metrics -->
  <g transform="translate(450, 65)">
    <rect x="0" y="0" width="295" height="270" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="147" y="28" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">Why Worm Castings Outperform Topsoil</text>
    <text x="15" y="60" font-size="9" fill="#cbd5e1">• 5x More Plant-Available Nitrogen</text>
    <text x="15" y="85" font-size="9" fill="#cbd5e1">• 7x More Soluble Available Phosphorus</text>
    <text x="15" y="110" font-size="9" fill="#cbd5e1">• 11x More Soluble Exchangeable Potassium</text>
    <text x="15" y="135" font-size="9" fill="#cbd5e1">• Rich in Root Growth Hormones (Auxins)</text>
    <text x="15" y="160" font-size="9" fill="#cbd5e1">• 100% Odorless &amp; Compact for Urban Balconies</text>
    <rect x="15" y="195" width="265" height="55" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="147" y="218" font-size="8" font-weight="bold" fill="#f87171" text-anchor="middle">BANNED IN VERMICOMPOSTING:</text>
    <text x="147" y="235" font-size="8" fill="#cbd5e1" text-anchor="middle">Citrus (Limonin), Onions, Garlic, Meat, Dairy</text>
  </g>

  <!-- Bottom Synthesis Banner -->
  <g transform="translate(45, 350)">
    <rect x="0" y="0" width="710" height="70" rx="8" fill="#0f172a" stroke="#38bdf8"/>
    <text x="355" y="28" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Harvest via Lateral Food Migration Method</text>
    <text x="355" y="50" font-size="9" fill="#cbd5e1" text-anchor="middle">Feed only one side of the bin for 5 days; all worms migrate over, allowing 100% pure castings to be scooped from the other side!</text>
  </g>
</svg>
""")

# SVG 7: Soil Structure Transformation (Lesson 9, Page 2)
SVG_SOIL_TRANSFORMATION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Soil Structure Transformation: Before vs. After Compost Addition</text>

  <!-- Split Screen: Before vs After -->
  <!-- Left Side: BEFORE COMPOST -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="260" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="28" rx="8" fill="#991b1b"/>
    <text x="170" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">BEFORE COMPOST (DEGRADED SOIL)</text>

    <!-- Dense Clay & Leaching Sand Visual -->
    <text x="15" y="55" font-size="9" font-weight="bold" fill="#f87171">Heavy Compact Clay:</text>
    <text x="15" y="73" font-size="8" fill="#cbd5e1">• Tiny pores, zero root oxygen, waterlogged in rain</text>
    <text x="15" y="88" font-size="8" fill="#cbd5e1">• Cracks into hard bricks during dry spells</text>

    <text x="15" y="115" font-size="9" font-weight="bold" fill="#f87171">Loose Droughty Sand:</text>
    <text x="15" y="133" font-size="8" fill="#cbd5e1">• Huge pores, zero water retention (drains instantly)</text>
    <text x="15" y="148" font-size="8" fill="#cbd5e1">• Low CEC: Nutrients leach away into groundwater</text>

    <rect x="15" y="180" width="310" height="60" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="170" y="205" font-size="9" font-weight="bold" fill="#fca5a5" text-anchor="middle">Result: Stunted Crop Roots &amp; High Fertilizer Waste</text>
    <text x="170" y="225" font-size="8" fill="#cbd5e1" text-anchor="middle">Chemical shocks destroy natural earthworms and microbes</text>
  </g>

  <!-- Right Side: AFTER COMPOST -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="340" height="260" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="28" rx="8" fill="#15803d"/>
    <text x="170" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">AFTER COMPOST (LIVING FERTILE SOIL)</text>

    <!-- Humus Aggregates Visual -->
    <text x="15" y="55" font-size="9" font-weight="bold" fill="#4ade80">Porous Crumbly Aggregates:</text>
    <text x="15" y="73" font-size="8" fill="#cbd5e1">• Clay opened up: Aeration + healthy drainage</text>
    <text x="15" y="88" font-size="8" fill="#cbd5e1">• Sand bound: Humus sponge boosts water retention +300%</text>

    <text x="15" y="115" font-size="9" font-weight="bold" fill="#4ade80">High Cation Exchange Capacity (CEC):</text>
    <text x="15" y="133" font-size="8" fill="#cbd5e1">• Negative charges magnetically hold K+, Ca2+, Mg2+</text>
    <text x="15" y="148" font-size="8" fill="#cbd5e1">• Neutral pH buffering (6.0-7.0) unlocks Phosphorus</text>

    <rect x="15" y="180" width="310" height="60" rx="6" fill="#1e293b" stroke="#22c55e"/>
    <text x="170" y="205" font-size="9" font-weight="bold" fill="#86efac" text-anchor="middle">Result: Massive Deep Roots &amp; Drought Resilience</text>
    <text x="170" y="225" font-size="8" fill="#cbd5e1" text-anchor="middle">Abundant earthworms &amp; mycorrhizal symbiotic fungal networks</text>
  </g>

  <!-- Bottom Synthesis Banner -->
  <g transform="translate(45, 340)">
    <rect x="0" y="0" width="710" height="70" rx="8" fill="#0f172a" stroke="#38bdf8"/>
    <text x="355" y="26" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Feed the Soil, and the Soil Will Feed the Crop</text>
    <text x="355" y="50" font-size="9" fill="#cbd5e1" text-anchor="middle">Organic compost transforms dead dirt into a self-sustaining, nutrient-rich biological ecosystem.</text>
  </g>
</svg>
""")

# SVG 8: Master Composting Lifecycle (Lesson 10, Page 2)
SVG_MASTER_COMPOSTING = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Master Composting Techniques &amp; Organic Soil Management Lifecycle</text>

  <!-- 6 Ring Stages -->
  <!-- 1. Waste Segregation -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="100" y="22" font-size="10" font-weight="bold" fill="#f87171" text-anchor="middle">1. WASTE SORTING</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Segregate browns &amp; greens</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Ban meats, dairy &amp; weeds</text>
  </g>
  <line x1="245" y1="102" x2="345" y2="200" stroke="#ef4444" stroke-width="2" stroke-dasharray="2,2"/>

  <!-- 2. Quality Optimization -->
  <g transform="translate(555, 65)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="100" y="22" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">2. 30:1 C:N BALANCING</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• 50-60% Sponge moisture</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Ash dusting &amp; soil inoculant</text>
  </g>
  <line x1="555" y1="102" x2="455" y2="200" stroke="#38bdf8" stroke-width="2" stroke-dasharray="2,2"/>

  <!-- 3. Method Selection -->
  <g transform="translate(35, 195)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <text x="100" y="22" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">3. METHOD DEPLOYMENT</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Four-Pit / Heap Stack</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Vermicompost / Tumblers</text>
  </g>
  <line x1="235" y1="240" x2="345" y2="240" stroke="#eab308" stroke-width="2"/>

  <!-- 4. Aerobic Pasteurization -->
  <g transform="translate(565, 195)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="100" y="22" font-size="10" font-weight="bold" fill="#d8b4fe" text-anchor="middle">4. THERMOPHILIC HEAT</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• 55-65°C kills pathogens</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Turning every 3-4 weeks</text>
  </g>
  <line x1="565" y1="240" x2="455" y2="240" stroke="#a855f7" stroke-width="2"/>

  <!-- 5. Maturity Verification -->
  <g transform="translate(130, 335)">
    <rect x="0" y="0" width="220" height="75" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
    <text x="110" y="22" font-size="10" font-weight="bold" fill="#67e8f9" text-anchor="middle">5. MATURITY AUDIT</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Dark black &amp; crumbly</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Sweet earthy forest scent</text>
  </g>
  <line x1="350" y1="350" x2="390" y2="298" stroke="#06b6d4" stroke-width="2"/>

  <!-- 6. Field Application -->
  <g transform="translate(450, 335)">
    <rect x="0" y="0" width="220" height="75" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <text x="110" y="22" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">6. FIELD APPLICATION</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Incorporation (5-10 kg/m2)</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Sidedressing &amp; 1:2:1 Blends</text>
  </g>
  <line x1="450" y1="350" x2="410" y2="298" stroke="#22c55e" stroke-width="2"/>

  <!-- Central Hub: Soil Stewardship -->
  <circle cx="400" cy="240" r="55" fill="#0f172a" stroke="#22c55e" stroke-width="3"/>
  <text x="400" y="235" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">CIRCULAR</text>
  <text x="400" y="252" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STEWARDSHIP</text>
</svg>
""")

SVG_MAP = {
    1: {"page": 2, "svg": SVG_COMPOST_MATURITY, "title": "Physical Indicators of Fully Mature Compost"},
    2: {"page": 2, "svg": SVG_QUALITY_FACTORS, "title": "Key Factors Determining Compost Quality & Microbial Activity"},
    4: {"page": 2, "svg": SVG_FOUR_PIT_LAYOUT, "title": "Four-Pit Composting System Layout & Directional Flow"},
    5: {"page": 2, "svg": SVG_SHIFTING_SCHEDULE, "title": "Chronological Shifting Schedule of the Four-Pit System"},
    6: {"page": 2, "svg": SVG_HEAP_STACK, "title": "Step-by-Step Above-Ground Compost Heap Architecture"},
    7: {"page": 2, "svg": SVG_VERMICOMPOST_BIN, "title": "Vermicomposting Bin Ecosystem (Red Wigglers & Castings)"},
    9: {"page": 2, "svg": SVG_SOIL_TRANSFORMATION, "title": "Soil Structure Transformation: Before vs After Compost Addition"},
    10: {"page": 2, "svg": SVG_MASTER_COMPOSTING, "title": "Master Composting Techniques & Organic Soil Management Lifecycle"}
}

def enrich_grade10_topic17():
    """Injects verified photos, responsive vector SVGs, YouTube embeds, and creates LessonAssets."""
    print("=" * 80)
    print("STARTING ENRICHMENT: CBC Grade 10 Agriculture — Topic 17: Composting")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()
    topic = Topic.objects.filter(subject=subject, name="Composting").first()

    assert topic, "Topic 'Composting' not found!"

    images_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grade10_topic17_verified_images.json")
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
                    "topic_order": 17,
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
                        "topic_order": 17,
                        "unit_order": u_order,
                        "page": svg_def["page"],
                        "svg_content": svg_def["svg"]
                    }
                )
                diag_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [Vector SVG Attached] Lesson {u_order}: {svg_def['title']}")

        # ---------------------------------------------------------------------
        # 3. Educational YouTube Videos (Lesson 4 & Lesson 7)
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
                        "topic_order": 17,
                        "unit_order": u_order,
                        "youtube_url": v_url
                    }
                )
                v_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [YouTube Video Attached] Lesson {u_order}: {v_block.title}")

    print("=" * 80)
    print(f"ENRICHMENT COMPLETE: Topic 17 '{topic.name}'")
    print(f"  Photographic Hooks: {total_images_attached} / 10")
    print(f"  Vector SVGs:        {total_svgs_attached} / 8")
    print(f"  YouTube Videos:     {total_videos_attached} / 2")
    print(f"  LessonAssets:       {total_assets_persisted}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic17()
