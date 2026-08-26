"""
VLearn CBC Grade 10 Agriculture — Topic 6: Crop Protection
Visual Enrichment Engine (Phase 2: Vector SVGs, Verified Photos & Asset Persistence)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Crop Protection (Order: 6)

Attaches:
  - 14 First-Card Photographic Visual Hooks (100% Tested HTTP 200 Direct Wikimedia URLs)
  - 10 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - 2 Verified Educational YouTube Videos (Lesson 3 Card 3 & Lesson 12 Card 2)
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade10_agriculture_topic6.py
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
# 10 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 6: CROP PROTECTION
# =============================================================================

# SVG 1: Evolutionary Biology & Seed Bank Dynamics of Weeds (Lesson 1, Page 2)
SVG_WEED_ADAPTATIONS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 5 Evolutionary Superpowers of Agricultural Weeds</text>

  <!-- Central Hub: Weed Domination -->
  <circle cx="400" cy="240" r="60" fill="#0f172a" stroke="#ef4444" stroke-width="3"/>
  <text x="400" y="230" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">AGGRESSIVE</text>
  <text x="400" y="248" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">WEED</text>
  <text x="400" y="265" font-size="9" fill="#fca5a5" text-anchor="middle">COMPETITION</text>

  <!-- 1. Prolific Seeds (Top-Left) -->
  <g transform="translate(45, 75)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <text x="100" y="22" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">1. PROLIFIC SEEDS</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• 100,000+ seeds per plant</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Overwhelms crop stand</text>
  </g>
  <line x1="245" y1="120" x2="345" y2="200" stroke="#eab308" stroke-width="2"/>

  <!-- 2. Seed Dormancy (Top-Right) -->
  <g transform="translate(555, 75)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="100" y="22" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">2. SOIL SEED BANK</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Survives 20–50 years in soil</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Staggered germination</text>
  </g>
  <line x1="555" y1="120" x2="455" y2="200" stroke="#38bdf8" stroke-width="2"/>

  <!-- 3. Rapid Maturation (Middle-Left) -->
  <g transform="translate(35, 205)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="100" y="22" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">3. FAST MATURATION</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Seeds set in 3–4 weeks</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Outpaces crop canopy</text>
  </g>
  <line x1="235" y1="240" x2="340" y2="240" stroke="#22c55e" stroke-width="2"/>

  <!-- 4. Deep Rhizomes (Middle-Right) -->
  <g transform="translate(565, 205)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="100" y="22" font-size="11" font-weight="bold" fill="#d8b4fe" text-anchor="middle">4. RHIZOMES &amp; TUBERS</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Subterranean food reserve</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Sprouts after cutting</text>
  </g>
  <line x1="565" y1="240" x2="460" y2="240" stroke="#a855f7" stroke-width="2"/>

  <!-- 5. Specialized Dispersal (Bottom Center) -->
  <g transform="translate(300, 335)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
    <text x="100" y="22" font-size="11" font-weight="bold" fill="#67e8f9" text-anchor="middle">5. EPIZOOCHORY DISPERSAL</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Barbed hooks cling to fur</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Wind tufts &amp; water carried</text>
  </g>
  <line x1="400" y1="335" x2="400" y2="300" stroke="#06b6d4" stroke-width="2"/>
</svg>
""")

# SVG 2: Blackjack Barbed Seed Epizoochory Adaptation (Lesson 2, Page 2)
SVG_BLACKJACK_SEED = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Blackjack (Bidens pilosa) Barbed Seed Epizoochory Adaptation</text>

  <!-- Left: Seed Illustration -->
  <g transform="translate(60, 65)">
    <rect x="0" y="0" width="320" height="345" rx="10" fill="#0f172a" stroke="#eab308" stroke-width="2"/>

    <!-- Seed Body (Linear Cypsela) -->
    <rect x="145" y="150" width="30" height="150" rx="4" fill="#09090b" stroke="#71717a" stroke-width="2"/>
    <text x="160" y="230" font-size="10" font-weight="bold" fill="#ffffff" transform="rotate(-90 160 230)" text-anchor="middle">Cypsela (Seed Body)</text>

    <!-- 3 Barbed Pappus Awns -->
    <line x1="150" y1="150" x2="110" y2="60" stroke="#ca8a04" stroke-width="4"/>
    <line x1="160" y1="150" x2="160" y2="50" stroke="#ca8a04" stroke-width="4"/>
    <line x1="170" y1="150" x2="210" y2="60" stroke="#ca8a04" stroke-width="4"/>

    <!-- Backward-Pointing Barbs (Awn Hooks) -->
    <path d="M 125 100 L 115 110 M 135 120 L 125 130" stroke="#fde047" stroke-width="3"/>
    <path d="M 160 80 L 150 90 M 160 110 L 170 120" stroke="#fde047" stroke-width="3"/>
    <path d="M 195 100 L 205 110 M 185 120 L 195 130" stroke="#fde047" stroke-width="3"/>

    <text x="160" y="325" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">Retro-Barbed Awns (Pappi)</text>
  </g>

  <!-- Right: Functional Description -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#0284c7"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">EPIZOOCHORY DISPERSAL MECHANISM</text>

    <g transform="translate(15, 45)">
      <text x="0" y="20" font-size="12" font-weight="bold" fill="#fde047">1. Mechanical Hooking Action:</text>
      <text x="0" y="38" font-size="11" fill="#cbd5e1">The awns point backward like fishhooks, easily penetrating wool, fur, and clothing.</text>

      <text x="0" y="70" font-size="12" font-weight="bold" fill="#fde047">2. High Pull Resistance:</text>
      <text x="0" y="88" font-size="11" fill="#cbd5e1">Once hooked, the barbs resist pulling out; animals carry seeds kilometers away.</text>

      <text x="0" y="120" font-size="12" font-weight="bold" fill="#fde047">3. Extreme Fecundity:</text>
      <text x="0" y="138" font-size="11" fill="#cbd5e1">One plant produces 3,000–6,000 seeds that readily detach upon contact.</text>

      <text x="0" y="170" font-size="12" font-weight="bold" fill="#fde047">4. Agronomic Consequence:</text>
      <text x="0" y="188" font-size="11" fill="#cbd5e1">Contaminates sheep wool, lowering fleece market value; infests clean seedbeds.</text>
    </g>

    <rect x="15" y="275" width="315" height="55" rx="6" fill="#1e293b" stroke="#22c55e"/>
    <text x="172" y="295" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Control Recommendation</text>
    <text x="172" y="313" font-size="9" fill="#86efac" text-anchor="middle">Uproot or hoe Blackjack BEFORE yellow composite flowers turn into black barbed seeds!</text>
  </g>
</svg>
""")

# SVG 3: Standard Scientific Weed Herbarium Mounting & Label Sheet (Lesson 3, Page 2)
SVG_HERBARIUM_SHEET = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Standard Scientific Weed Herbarium Mounting &amp; Label Architecture</text>

  <!-- Left: A3 Herbarium Cardstock Sheet -->
  <g transform="translate(60, 65)">
    <rect x="0" y="0" width="280" height="345" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>

    <!-- Mounted Plant Specimen -->
    <!-- Roots -->
    <path d="M 140 280 Q 120 310 95 330 M 140 280 Q 150 315 140 335 M 140 280 Q 170 310 185 325" stroke="#78350f" stroke-width="2.5" fill="none"/>
    <text x="140" y="325" font-size="8" fill="#78350f" text-anchor="middle">Intact Roots</text>

    <!-- Stem & Leaves -->
    <line x1="140" y1="280" x2="140" y2="100" stroke="#15803d" stroke-width="4"/>
    <!-- Leaves -->
    <ellipse cx="110" cy="180" rx="25" ry="12" fill="#22c55e" stroke="#15803d"/>
    <ellipse cx="170" cy="160" rx="25" ry="12" fill="#22c55e" stroke="#15803d"/>
    <ellipse cx="115" cy="130" rx="20" ry="10" fill="#22c55e" stroke="#15803d"/>
    <ellipse cx="165" cy="110" rx="20" ry="10" fill="#22c55e" stroke="#15803d"/>

    <!-- Flowers / Seeds at Top -->
    <circle cx="140" cy="80" r="12" fill="#eab308" stroke="#ca8a04"/>
    <circle cx="125" cy="68" r="8" fill="#ffffff"/><circle cx="155" cy="68" r="8" fill="#ffffff"/>

    <!-- Bottom-Right Label Tag -->
    <rect x="135" y="245" width="140" height="95" rx="3" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
    <text x="205" y="260" font-size="7" font-weight="bold" fill="#0f172a" text-anchor="middle">HERBARIUM RECORD</text>
    <text x="140" y="275" font-size="6" fill="#334155">Name: Bidens pilosa</text>
    <text x="140" y="288" font-size="6" fill="#334155">Family: Asteraceae</text>
    <text x="140" y="301" font-size="6" fill="#334155">Loc: School Garden</text>
    <text x="140" y="314" font-size="6" fill="#334155">Date: 26/08/2026</text>
    <text x="140" y="327" font-size="6" fill="#334155">Col: Grade 10 Agri</text>
  </g>

  <!-- Right: 5-Step Botanical Protocol -->
  <g transform="translate(375, 65)">
    <rect x="0" y="0" width="380" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="380" height="32" rx="10" fill="#15803d"/>
    <text x="190" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">5-STEP HERBARIUM PROTOCOL</text>

    <g transform="translate(15, 45)">
      <text x="0" y="18" font-size="11" font-weight="bold" fill="#4ade80">1. Complete Collection with Roots:</text>
      <text x="0" y="34" font-size="10" fill="#cbd5e1">Lift whole plant using a trowel; wash soil from roots.</text>

      <text x="0" y="62" font-size="11" font-weight="bold" fill="#4ade80">2. Layout &amp; Pressing:</text>
      <text x="0" y="78" font-size="10" fill="#cbd5e1">Spread leaves &amp; roots flat between dry newspaper sheets.</text>

      <text x="0" y="106" font-size="11" font-weight="bold" fill="#4ade80">3. Daily Newspaper Changes (7–10 Days):</text>
      <text x="0" y="122" font-size="10" fill="#fde047">MANDATORY: Change paper daily to halt fungal rot &amp; mold.</text>

      <text x="0" y="150" font-size="11" font-weight="bold" fill="#4ade80">4. Mounting on Cardstock:</text>
      <text x="0" y="166" font-size="10" fill="#cbd5e1">Glue crisp dried specimen onto standard A3 (29x42cm) sheet.</text>

      <text x="0" y="194" font-size="11" font-weight="bold" fill="#4ade80">5. Bottom-Right Labeling:</text>
      <text x="0" y="210" font-size="10" fill="#cbd5e1">Botanical name, common name, habitat, date &amp; collector.</text>
    </g>

    <rect x="15" y="280" width="350" height="50" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="190" y="300" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Scientific Purpose</text>
    <text x="190" y="318" font-size="9" fill="#86efac" text-anchor="middle">Permanent diagnostic reference library for agricultural weed scouting.</text>
  </g>
</svg>
""")

# SVG 4: Morphological Stem Anatomy: Grass vs Sedge vs Broadleaf (Lesson 4, Page 2)
SVG_STEM_ANATOMY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Morphological Stem Anatomy &amp; Diagnostic Cross-Sections</text>

  <!-- Group 1: Broad-Leaved Dicots -->
  <g transform="translate(35, 65)">
    <rect x="0" y="0" width="225" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="225" height="30" rx="10" fill="#15803d"/>
    <text x="112" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. BROAD-LEAF (DICOT)</text>

    <!-- Cross Section: Solid Round/Square with Vascular Ring -->
    <g transform="translate(50, 45)">
      <circle cx="62" cy="62" r="50" fill="#14532d" stroke="#22c55e" stroke-width="3"/>
      <circle cx="62" cy="62" r="35" fill="#1e293b" stroke="#86efac" stroke-width="1.5" stroke-dasharray="3,3"/>
      <text x="62" y="67" font-size="9" font-weight="bold" fill="#86efac" text-anchor="middle">Solid Stem</text>
    </g>

    <g transform="translate(10, 180)">
      <text x="0" y="15" font-size="10" font-weight="bold" fill="#4ade80">• Net (Reticulate) Venation</text>
      <text x="0" y="35" font-size="9" fill="#cbd5e1">• Deep primary taproot</text>
      <text x="0" y="55" font-size="9" fill="#cbd5e1">• Solid branched stem</text>
      <text x="0" y="75" font-size="9" font-weight="bold" fill="#fde047">• Killed by 2,4-D in maize</text>
    </g>
    <rect x="10" y="295" width="205" height="35" rx="4" fill="#14532d"/>
    <text x="112" y="316" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">e.g. Blackjack, Pigweed</text>
  </g>

  <!-- Group 2: Grass Weeds (Poaceae) -->
  <g transform="translate(285, 65)">
    <rect x="0" y="0" width="225" height="345" rx="10" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect x="0" y="0" width="225" height="30" rx="10" fill="#ca8a04"/>
    <text x="112" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. GRASS WEED (POACEAE)</text>

    <!-- Cross Section: Round Hollow Culm -->
    <g transform="translate(50, 45)">
      <circle cx="62" cy="62" r="50" fill="#78350f" stroke="#ca8a04" stroke-width="3"/>
      <circle cx="62" cy="62" r="28" fill="#0f172a" stroke="#fde047" stroke-width="2"/>
      <text x="62" y="67" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">Hollow Culm</text>
    </g>

    <g transform="translate(10, 180)">
      <text x="0" y="15" font-size="10" font-weight="bold" fill="#fde047">• Parallel leaf venation</text>
      <text x="0" y="35" font-size="9" fill="#cbd5e1">• Round &amp; hollow stem</text>
      <text x="0" y="55" font-size="9" fill="#cbd5e1">• Swollen joints (nodes)</text>
      <text x="0" y="75" font-size="9" font-weight="bold" fill="#f87171">• Tolerant to 2,4-D</text>
    </g>
    <rect x="10" y="295" width="205" height="35" rx="4" fill="#78350f"/>
    <text x="112" y="316" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">e.g. Couch Grass, Kikuyu</text>
  </g>

  <!-- Group 3: Sedge Weeds (Cyperaceae) -->
  <g transform="translate(535, 65)">
    <rect x="0" y="0" width="230" height="345" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="230" height="30" rx="10" fill="#0284c7"/>
    <text x="115" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. SEDGE (CYPERACEAE)</text>

    <!-- Cross Section: Solid Triangle -->
    <g transform="translate(52, 45)">
      <polygon points="62,15 15,100 110,100" fill="#0c4a6e" stroke="#38bdf8" stroke-width="3"/>
      <text x="62" y="75" font-size="9" font-weight="bold" fill="#67e8f9" text-anchor="middle">Solid Triangle</text>
    </g>

    <g transform="translate(10, 180)">
      <text x="0" y="15" font-size="10" font-weight="bold" fill="#38bdf8">• Triangular solid stem</text>
      <text x="0" y="35" font-size="9" fill="#cbd5e1">• Completely lacks nodes</text>
      <text x="0" y="55" font-size="9" fill="#cbd5e1">• 3-ranked leaf rows</text>
      <text x="0" y="75" font-size="9" fill="#cbd5e1">• Basal tubers (nuts)</text>
    </g>
    <rect x="10" y="295" width="210" height="35" rx="4" fill="#0c4a6e"/>
    <text x="115" y="316" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">e.g. Nut Grass (Cyperus)</text>
  </g>
</svg>
""")

# SVG 5: Weed Life Cycle Horizons (Lesson 5, Page 2)
SVG_LIFECYCLES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Weed Life Cycle Horizons &amp; Strategic Management Windows</text>

  <!-- Annual Cycle (1 Season) -->
  <g transform="translate(35, 65)">
    <rect x="0" y="0" width="225" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="225" height="30" rx="10" fill="#15803d"/>
    <text x="112" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">ANNUAL WEEDS (&lt;1 YR)</text>

    <g transform="translate(20, 50)">
      <circle cx="92" cy="45" r="35" fill="none" stroke="#22c55e" stroke-width="3" stroke-dasharray="4,4"/>
      <text x="92" y="40" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Seed -&gt; Shoot</text>
      <text x="92" y="55" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">-&gt; Flower -&gt; Die</text>
    </g>

    <g transform="translate(10, 160)">
      <text x="0" y="15" font-size="10" font-weight="bold" fill="#4ade80">• 1 Season lifecycle</text>
      <text x="0" y="35" font-size="9" fill="#cbd5e1">• Reproduces via seeds</text>
      <text x="0" y="55" font-size="9" font-weight="bold" fill="#f87171">• CRITICAL: Hoe before flowering</text>
      <text x="0" y="75" font-size="9" fill="#cbd5e1">• e.g. Blackjack, Pigweed</text>
    </g>
    <rect x="10" y="295" width="205" height="35" rx="4" fill="#14532d"/>
    <text x="112" y="316" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">Controlled by Tillage</text>
  </g>

  <!-- Biennial Cycle (2 Years) -->
  <g transform="translate(285, 65)">
    <rect x="0" y="0" width="225" height="345" rx="10" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect x="0" y="0" width="225" height="30" rx="10" fill="#ca8a04"/>
    <text x="112" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">BIENNIAL WEEDS (2 YRS)</text>

    <g transform="translate(20, 50)">
      <rect x="15" y="15" width="70" height="60" rx="4" fill="#1e293b" stroke="#eab308"/>
      <text x="50" y="42" font-size="8" font-weight="bold" fill="#fde047" text-anchor="middle">Yr 1: Rosette</text>
      <rect x="95" y="15" width="70" height="60" rx="4" fill="#1e293b" stroke="#eab308"/>
      <text x="130" y="42" font-size="8" font-weight="bold" fill="#fde047" text-anchor="middle">Yr 2: Seed/Die</text>
    </g>

    <g transform="translate(10, 160)">
      <text x="0" y="15" font-size="10" font-weight="bold" fill="#fde047">• 2 Years lifecycle</text>
      <text x="0" y="35" font-size="9" fill="#cbd5e1">• Year 1: Stores root food</text>
      <text x="0" y="55" font-size="9" fill="#cbd5e1">• Year 2: Flowers &amp; seeds</text>
      <text x="0" y="75" font-size="9" fill="#cbd5e1">• e.g. Wild carrot, Thistle</text>
    </g>
    <rect x="10" y="295" width="205" height="35" rx="4" fill="#78350f"/>
    <text x="112" y="316" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">Taproot Severing in Yr 1</text>
  </g>

  <!-- Perennial Cycle (>2 Years) -->
  <g transform="translate(535, 65)">
    <rect x="0" y="0" width="230" height="345" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="230" height="30" rx="10" fill="#991b1b"/>
    <text x="115" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">PERENNIAL WEEDS (&gt;2 YRS)</text>

    <g transform="translate(20, 50)">
      <path d="M 20 60 Q 95 10 170 60 M 20 60 Q 95 110 170 60" fill="#450a0a" stroke="#ef4444" stroke-width="2"/>
      <text x="95" y="65" font-size="9" font-weight="bold" fill="#fca5a5" text-anchor="middle">Continuous Rhizomes</text>
    </g>

    <g transform="translate(10, 160)">
      <text x="0" y="15" font-size="10" font-weight="bold" fill="#fca5a5">• Indefinite survival</text>
      <text x="0" y="35" font-size="9" fill="#cbd5e1">• Subterranean rhizome net</text>
      <text x="0" y="55" font-size="9" fill="#f87171">• Surface hoeing FAILS</text>
      <text x="0" y="75" font-size="9" fill="#cbd5e1">• e.g. Couch grass, Nut grass</text>
    </g>
    <rect x="10" y="295" width="210" height="35" rx="4" fill="#450a0a"/>
    <text x="115" y="316" font-size="9" font-weight="bold" fill="#fca5a5" text-anchor="middle">Systemic Chemical / Solarize</text>
  </g>
</svg>
""")

# SVG 6: Cultural Weed Suppression (Lesson 7, Page 2)
SVG_CULTURAL_SUPPRESSION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Cultural Weed Suppression: Mulching &amp; Living Cover Crop Canopy</text>

  <!-- Left: Organic Mulching Mechanism -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="345" rx="10" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="32" rx="10" fill="#ca8a04"/>
    <text x="170" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. ORGANIC MULCH LIGHT-BLOCKING</text>

    <!-- Sun & Blocked Light -->
    <circle cx="170" cy="70" r="22" fill="#eab308" stroke="#fde047" stroke-width="2"/>
    <line x1="170" y1="95" x2="170" y2="135" stroke="#fde047" stroke-width="3" stroke-dasharray="3,3"/>

    <!-- Mulch Layer (7cm) -->
    <rect x="25" y="140" width="290" height="25" rx="4" fill="#78350f" stroke="#ca8a04"/>
    <text x="170" y="157" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">7 cm Dry Grass Mulch Layer (Blocks 95% Light)</text>

    <!-- Topsoil & Choked Weed Seeds -->
    <rect x="25" y="165" width="290" height="85" fill="#14532d"/>
    <circle cx="65" cy="205" r="5" fill="#f87171"/><text x="65" y="225" font-size="8" fill="#fca5a5" text-anchor="middle">Dormant</text>
    <circle cx="170" cy="205" r="5" fill="#f87171"/><text x="170" y="225" font-size="8" fill="#fca5a5" text-anchor="middle">Dormant</text>
    <circle cx="275" cy="205" r="5" fill="#f87171"/><text x="275" y="225" font-size="8" fill="#fca5a5" text-anchor="middle">Dormant</text>

    <g transform="translate(15, 260)">
      <text x="0" y="15" font-size="10" fill="#cbd5e1">• Weed seeds starved of solar energy</text>
      <text x="0" y="32" font-size="10" fill="#cbd5e1">• Conserves 70% soil moisture</text>
      <text x="0" y="49" font-size="10" fill="#4ade80">• Adds organic humus upon decay</text>
    </g>
  </g>

  <!-- Right: Living Cover Crop Canopy -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#15803d"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. LIVING COVER CROP CANOPY</text>

    <!-- Maize + Dense Cowpea Understory -->
    <!-- Maize Stalks -->
    <line x1="90" y1="180" x2="90" y2="70" stroke="#84cc16" stroke-width="6"/>
    <line x1="250" y1="180" x2="250" y2="70" stroke="#84cc16" stroke-width="6"/>
    <text x="90" y="60" font-size="9" fill="#a3e635" text-anchor="middle">Maize</text>
    <text x="250" y="60" font-size="9" fill="#a3e635" text-anchor="middle">Maize</text>

    <!-- Dense Cowpea Ground Blanket -->
    <ellipse cx="170" cy="170" rx="130" ry="20" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
    <text x="170" y="174" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Dense Cowpea / Desmodium Canopy</text>

    <!-- Soil Base -->
    <rect x="25" y="190" width="295" height="60" fill="#14532d"/>
    <text x="170" y="225" font-size="10" font-weight="bold" fill="#86efac" text-anchor="middle">Zero Sunlight Reaches Bare Soil</text>

    <g transform="translate(15, 260)">
      <text x="0" y="15" font-size="10" fill="#cbd5e1">• Outcompetes weeds for light &amp; space</text>
      <text x="0" y="32" font-size="10" fill="#cbd5e1">• Fixes atmospheric nitrogen gas</text>
      <text x="0" y="49" font-size="10" fill="#4ade80">• Push-pull suppresses Striga weed</text>
    </g>
  </g>
</svg>
""")

# SVG 7: Chemical Herbicide Action (Lesson 9, Page 2)
SVG_HERBICIDE_ACTION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Chemical Herbicide Dynamics: Contact vs Systemic Translocation</text>

  <!-- Left: Contact Herbicide Action -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="345" rx="10" fill="#0f172a" stroke="#f87171" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="32" rx="10" fill="#991b1b"/>
    <text x="170" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. CONTACT HERBICIDE (LEAVES ONLY)</text>

    <!-- Plant Graphic -->
    <!-- Scorch Marks on Leaves -->
    <ellipse cx="120" cy="100" rx="30" ry="15" fill="#78350f" stroke="#ef4444" stroke-width="2"/>
    <ellipse cx="220" cy="120" rx="30" ry="15" fill="#78350f" stroke="#ef4444" stroke-width="2"/>
    <line x1="170" y1="80" x2="170" y2="200" stroke="#ca8a04" stroke-width="5"/>
    <text x="170" y="70" font-size="9" fill="#f87171" text-anchor="middle">Foliar Scorch (Dead Tissue)</text>

    <!-- Underground Rhizome (ALIVE & SPROUTING) -->
    <rect x="25" y="200" width="290" height="50" fill="#14532d"/>
    <line x1="60" y1="225" x2="280" y2="225" stroke="#22c55e" stroke-width="6"/>
    <polygon points="270,215 285,225 270,235" fill="#22c55e"/>
    <text x="170" y="240" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">Rhizome SURVIVES and Resprouts!</text>

    <g transform="translate(15, 260)">
      <text x="0" y="15" font-size="10" fill="#fca5a5">• Destroys only contacted green cells</text>
      <text x="0" y="32" font-size="10" fill="#fca5a5">• Zero vascular movement inside plant</text>
      <text x="0" y="49" font-size="10" font-weight="bold" fill="#ef4444">• Ineffective against perennial weeds</text>
    </g>
  </g>

  <!-- Right: Systemic Herbicide Action -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#15803d"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. SYSTEMIC TRANSLOCATION (WHOLE PLANT)</text>

    <!-- Plant Graphic with Downward Arrows -->
    <ellipse cx="120" cy="100" rx="30" ry="15" fill="#14532d" stroke="#38bdf8" stroke-width="2"/>
    <ellipse cx="220" cy="120" rx="30" ry="15" fill="#14532d" stroke="#38bdf8" stroke-width="2"/>
    <line x1="170" y1="80" x2="170" y2="200" stroke="#0284c7" stroke-width="6"/>
    
    <!-- Phloem Downward Translocation Arrows -->
    <line x1="150" y1="110" x2="150" y2="180" stroke="#38bdf8" stroke-width="3"/>
    <polygon points="145,180 150,190 155,180" fill="#38bdf8"/>
    <line x1="190" y1="130" x2="190" y2="180" stroke="#38bdf8" stroke-width="3"/>
    <polygon points="185,180 190,190 195,180" fill="#38bdf8"/>

    <!-- Underground Rhizome (DESTROYED) -->
    <rect x="25" y="200" width="295" height="50" fill="#450a0a"/>
    <line x1="60" y1="225" x2="280" y2="225" stroke="#7f1d1d" stroke-width="6" stroke-dasharray="4,4"/>
    <text x="172" y="240" font-size="9" font-weight="bold" fill="#f87171" text-anchor="middle">Rhizome Destroyed at Growing Points</text>

    <g transform="translate(15, 260)">
      <text x="0" y="15" font-size="10" fill="#86efac">• Absorbed by leaves and translocated</text>
      <text x="0" y="32" font-size="10" fill="#86efac">• Moves via phloem to subterranean roots</text>
      <text x="0" y="49" font-size="10" font-weight="bold" fill="#4ade80">• Permanent eradication of Couch grass</text>
    </g>
  </g>
</svg>
""")

# SVG 8: National Plant Quarantine & Phytosanitary Barrier (Lesson 10, Page 2)
SVG_QUARANTINE_BARRIER = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">National Biosecurity: Plant Quarantine &amp; Phytosanitary Barrier</text>

  <!-- Step 1: Foreign Seed Shipments (Left) -->
  <g transform="translate(35, 75)">
    <rect x="0" y="0" width="180" height="330" rx="10" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect x="0" y="0" width="180" height="30" rx="10" fill="#ca8a04"/>
    <text x="90" y="20" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">IMPORTED SHIPMENTS</text>

    <rect x="25" y="55" width="130" height="60" rx="6" fill="#1e293b" stroke="#eab308"/>
    <text x="90" y="80" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">Foreign Grain</text>
    <text x="90" y="98" font-size="8" fill="#fca5a5" text-anchor="middle">+ Exotic Weed Seeds</text>

    <g transform="translate(10, 140)">
      <text x="0" y="15" font-size="9" fill="#cbd5e1">• Commercial seed lots</text>
      <text x="0" y="35" font-size="9" fill="#cbd5e1">• Air, sea &amp; land ports</text>
      <text x="0" y="55" font-size="9" fill="#cbd5e1">• Potential biosecurity risk</text>
    </g>
  </g>

  <!-- Arrow 1 -> 2 -->
  <line x1="215" y1="240" x2="265" y2="240" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="265,235 275,240 265,245" fill="#38bdf8"/>

  <!-- Step 2: KEPHIS Inspection Gateway (Center) -->
  <g transform="translate(280, 75)">
    <rect x="0" y="0" width="240" height="330" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="240" height="30" rx="10" fill="#0284c7"/>
    <text x="120" y="20" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">PHYTOSANITARY GATEWAY</text>

    <!-- Magnifier / Inspection Icon -->
    <circle cx="120" cy="90" r="30" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
    <line x1="140" y1="110" x2="165" y2="135" stroke="#38bdf8" stroke-width="5"/>
    <text x="120" y="95" font-size="8" font-weight="bold" fill="#67e8f9" text-anchor="middle">KEPHIS LAB</text>

    <!-- Branch A: Contaminated -> Destroyed -->
    <rect x="15" y="155" width="210" height="50" rx="4" fill="#450a0a" stroke="#ef4444"/>
    <text x="120" y="175" font-size="9" font-weight="bold" fill="#fca5a5" text-anchor="middle">NOXIOUS WEED DETECTED</text>
    <text x="120" y="192" font-size="8" fill="#ffffff" text-anchor="middle">Incinerated / Entry Rejected</text>

    <!-- Branch B: Clean -> Certified -->
    <rect x="15" y="220" width="210" height="50" rx="4" fill="#14532d" stroke="#22c55e"/>
    <text x="120" y="240" font-size="9" font-weight="bold" fill="#86efac" text-anchor="middle">PASSED PURITY TEST</text>
    <text x="120" y="257" font-size="8" fill="#ffffff" text-anchor="middle">Phytosanitary Certificate Issued</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <line x1="520" y1="240" x2="570" y2="240" stroke="#22c55e" stroke-width="3"/>
  <polygon points="570,235 580,240 570,245" fill="#22c55e"/>

  <!-- Step 3: Protected National Farms (Right) -->
  <g transform="translate(585, 75)">
    <rect x="0" y="0" width="180" height="330" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="180" height="30" rx="10" fill="#15803d"/>
    <text x="90" y="20" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">CLEAN ARABLE FARMS</text>

    <rect x="25" y="55" width="130" height="60" rx="6" fill="#14532d" stroke="#22c55e"/>
    <text x="90" y="80" font-size="10" font-weight="bold" fill="#86efac" text-anchor="middle">Healthy Crops</text>
    <text x="90" y="98" font-size="8" fill="#ffffff" text-anchor="middle">Zero Exotic Invasives</text>

    <g transform="translate(10, 140)">
      <text x="0" y="15" font-size="9" fill="#cbd5e1">• Free of Parthenium</text>
      <text x="0" y="35" font-size="9" fill="#cbd5e1">• Free of Striga seeds</text>
      <text x="0" y="55" font-size="9" fill="#4ade80">• National food security</text>
    </g>
  </g>
</svg>
""")

# SVG 9: The Integrated Weed Management (IWM) Control Pyramid (Lesson 11, Page 2)
SVG_IWM_PYRAMID = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Integrated Weed Management (IWM) Control Hierarchy</text>

  <!-- Left: Pyramid Schematic -->
  <g transform="translate(60, 65)">
    <!-- Level 4: Chemical (Peak) -->
    <polygon points="170,30 115,100 225,100" fill="#991b1b" stroke="#ef4444" stroke-width="2"/>
    <text x="170" y="80" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">TARGETED CHEMICAL</text>

    <!-- Level 3: Physical & Biological -->
    <polygon points="115,105 70,180 270,180 225,105" fill="#ca8a04" stroke="#eab308" stroke-width="2"/>
    <text x="170" y="148" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">PHYSICAL &amp; BIOLOGICAL</text>

    <!-- Level 2: Cultural Foundation -->
    <polygon points="70,185 25,260 315,260 270,185" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <text x="170" y="228" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">CULTURAL HUSBANDRY</text>

    <!-- Level 1: Prevention (Base) -->
    <polygon points="25,265 -15,335 355,335 315,265" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
    <text x="170" y="305" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">PREVENTION &amp; SANITATION (BASE)</text>
  </g>

  <!-- Right: Detail Description of the 4 Layers -->
  <g transform="translate(425, 65)">
    <rect x="0" y="0" width="335" height="345" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="335" height="30" rx="10" fill="#0284c7"/>
    <text x="167" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">IWM OPERATIONAL TIERS</text>

    <g transform="translate(15, 40)">
      <text x="0" y="15" font-size="10" font-weight="bold" fill="#ef4444">Tier 4: Targeted Chemical (Peak)</text>
      <text x="0" y="30" font-size="9" fill="#cbd5e1">Selective herbicides applied only on heavy hot-spots.</text>

      <text x="0" y="55" font-size="10" font-weight="bold" fill="#fde047">Tier 3: Physical &amp; Biological</text>
      <text x="0" y="70" font-size="9" fill="#cbd5e1">Hand-hoeing small weeds; natural insect predators.</text>

      <text x="0" y="95" font-size="10" font-weight="bold" fill="#38bdf8">Tier 2: Cultural Management</text>
      <text x="0" y="110" font-size="9" fill="#cbd5e1">Crop rotation, living cover crops, dry organic mulch.</text>

      <text x="0" y="135" font-size="10" font-weight="bold" fill="#4ade80">Tier 1: Prevention &amp; Sanitation (Base)</text>
      <text x="0" y="150" font-size="9" fill="#cbd5e1">Certified clean seeds, machinery wash-down, clean water.</text>
    </g>

    <rect x="15" y="255" width="305" height="75" rx="6" fill="#1e293b" stroke="#22c55e"/>
    <text x="152" y="275" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">The Golden Agronomic Maxim</text>
    <text x="152" y="295" font-size="9" fill="#86efac" text-anchor="middle">Combine multiple compatible tactics to prevent</text>
    <text x="152" y="310" font-size="9" fill="#86efac" text-anchor="middle">herbicide resistance and build living soil fertility!</text>
  </g>
</svg>
""")

# SVG 10: Couch Grass Rhizome Fragmentation Model (Lesson 14, Page 2)
SVG_COUCH_GRASS_FRAGMENTATION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Couch Grass (Digitaria abyssinica) Rhizome Fragmentation Model</text>

  <!-- Step 1: Single Continuous Rhizome Network -->
  <g transform="translate(35, 65)">
    <rect x="0" y="0" width="220" height="345" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="28" rx="8" fill="#15803d"/>
    <text x="110" y="19" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">1. INTACT RHIZOME NETWORK</text>

    <line x1="20" y1="120" x2="200" y2="120" stroke="#ca8a04" stroke-width="8"/>
    <!-- Nodes -->
    <circle cx="50" cy="120" r="7" fill="#eab308"/><circle cx="110" cy="120" r="7" fill="#eab308"/><circle cx="170" cy="120" r="7" fill="#eab308"/>
    <!-- Green Shoots -->
    <line x1="110" y1="120" x2="110" y2="60" stroke="#22c55e" stroke-width="4"/>
    <text x="110" y="155" font-size="9" fill="#fde047" text-anchor="middle">1 Plant with Dormant Nodes</text>

    <text x="10" y="200" font-size="9" fill="#cbd5e1">• Continuous subterranean stem</text>
    <text x="10" y="220" font-size="9" fill="#cbd5e1">• Apical dominance suppresses buds</text>
    <text x="10" y="240" font-size="9" fill="#cbd5e1">• Survives dry season in dormancy</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <line x1="260" y1="230" x2="280" y2="230" stroke="#ef4444" stroke-width="2"/>
  <polygon points="280,225 290,230 280,235" fill="#ef4444"/>

  <!-- Step 2: Disc Plow Chopping -->
  <g transform="translate(290, 65)">
    <rect x="0" y="0" width="220" height="345" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="28" rx="8" fill="#991b1b"/>
    <text x="110" y="19" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">2. MECHANICAL DISC PLOWING</text>

    <!-- Sliced Segments -->
    <line x1="20" y1="120" x2="65" y2="120" stroke="#ca8a04" stroke-width="6"/>
    <line x1="85" y1="120" x2="135" y2="120" stroke="#ca8a04" stroke-width="6"/>
    <line x1="155" y1="120" x2="200" y2="120" stroke="#ca8a04" stroke-width="6"/>

    <!-- Cut lines -->
    <line x1="75" y1="100" x2="75" y2="140" stroke="#ef4444" stroke-width="2" stroke-dasharray="2,2"/>
    <line x1="145" y1="100" x2="145" y2="140" stroke="#ef4444" stroke-width="2" stroke-dasharray="2,2"/>
    <text x="110" y="155" font-size="9" font-weight="bold" fill="#f87171" text-anchor="middle">Rhizomes Sliced into Pieces</text>

    <text x="10" y="200" font-size="9" fill="#cbd5e1">• Disc blades sever network</text>
    <text x="10" y="220" font-size="9" fill="#cbd5e1">• Breaks apical dominance</text>
    <text x="10" y="240" font-size="9" font-weight="bold" fill="#ef4444">• Spreads fragments across field</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <line x1="515" y1="230" x2="535" y2="230" stroke="#ef4444" stroke-width="2"/>
  <polygon points="535,225 545,230 535,235" fill="#ef4444"/>

  <!-- Step 3: Massive Re-growth Multiplying Infestation -->
  <g transform="translate(545, 65)">
    <rect x="0" y="0" width="220" height="345" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="28" rx="8" fill="#ca8a04"/>
    <text x="110" y="19" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">3. 10X WEED MULTIPLICATION</text>

    <!-- Multiple Shoots -->
    <line x1="45" y1="120" x2="45" y2="60" stroke="#22c55e" stroke-width="4"/>
    <line x1="110" y1="120" x2="110" y2="60" stroke="#22c55e" stroke-width="4"/>
    <line x1="175" y1="120" x2="175" y2="60" stroke="#22c55e" stroke-width="4"/>
    <text x="110" y="155" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">Each Node Becomes a New Plant!</text>

    <text x="10" y="200" font-size="9" fill="#cbd5e1">• Every fragment sprouts roots</text>
    <text x="10" y="220" font-size="9" fill="#cbd5e1">• Infestation multiplies 10-fold</text>
    <text x="10" y="240" font-size="9" font-weight="bold" fill="#fde047">• Chokes young maize crop</text>
  </g>
</svg>
""")

SVG_MAP = {
    1: {"page": 2, "svg": SVG_WEED_ADAPTATIONS, "title": "Evolutionary Biology & Seed Bank Dynamics of Weeds"},
    2: {"page": 2, "svg": SVG_BLACKJACK_SEED, "title": "Blackjack (Bidens pilosa) Barbed Seed Epizoochory Adaptation"},
    3: {"page": 2, "svg": SVG_HERBARIUM_SHEET, "title": "Standard Scientific Weed Herbarium Mounting & Label Sheet"},
    4: {"page": 2, "svg": SVG_STEM_ANATOMY, "title": "Morphological Stem Anatomy: Grass vs Sedge vs Broadleaf"},
    5: {"page": 2, "svg": SVG_LIFECYCLES, "title": "Weed Life Cycle Horizons: Annual vs Biennial vs Perennial"},
    7: {"page": 2, "svg": SVG_CULTURAL_SUPPRESSION, "title": "Cultural Weed Suppression: Mulching & Living Cover Crop Canopy"},
    9: {"page": 2, "svg": SVG_HERBICIDE_ACTION, "title": "Chemical Herbicide Action: Contact vs Systemic Translocation"},
    10: {"page": 2, "svg": SVG_QUARANTINE_BARRIER, "title": "National Plant Quarantine & Phytosanitary Inspection Barrier"},
    11: {"page": 2, "svg": SVG_IWM_PYRAMID, "title": "The Integrated Weed Management (IWM) Control Pyramid"},
    14: {"page": 2, "svg": SVG_COUCH_GRASS_FRAGMENTATION, "title": "Couch Grass (Digitaria abyssinica) Rhizome Fragmentation Model"}
}

def enrich_grade10_topic6():
    """Injects verified photos, responsive vector SVGs, YouTube embeds, and creates LessonAssets."""
    print("=" * 80)
    print("STARTING ENRICHMENT: CBC Grade 10 Agriculture — Topic 6: Crop Protection")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()
    topic = Topic.objects.filter(subject=subject, name="Crop Protection").first()

    assert topic, "Topic 'Crop Protection' not found!"

    images_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grade10_topic6_verified_images.json")
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
                    "topic_order": 6,
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
                        "topic_order": 6,
                        "unit_order": u_order,
                        "page": svg_def["page"],
                        "svg_content": svg_def["svg"]
                    }
                )
                diag_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [Vector SVG Attached] Lesson {u_order}: {svg_def['title']}")

        # ---------------------------------------------------------------------
        # 3. Educational YouTube Videos (Lesson 3 & Lesson 12)
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
                        "topic_order": 6,
                        "unit_order": u_order,
                        "youtube_url": v_url
                    }
                )
                v_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [YouTube Video Attached] Lesson {u_order}: {v_block.title}")

    print("=" * 80)
    print(f"ENRICHMENT COMPLETE: Topic 6 '{topic.name}'")
    print(f"  Photographic Hooks: {total_images_attached} / 14")
    print(f"  Vector SVGs:        {total_svgs_attached} / 10")
    print(f"  YouTube Videos:     {total_videos_attached} / 2")
    print(f"  LessonAssets:       {total_assets_persisted}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic6()
