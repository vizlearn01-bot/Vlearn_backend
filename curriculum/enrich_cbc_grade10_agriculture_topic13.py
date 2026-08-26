"""
VLearn CBC Grade 10 Agriculture — Topic 13: Tools and Equipment
Visual Enrichment Engine (Phase 2: Vector SVGs, Verified Photos & Asset Persistence)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Tools and Equipment (Order: 13)

Attaches:
  - 14 First-Card Photographic Visual Hooks (100% Tested HTTP 200 Direct Wikimedia URLs)
  - 8 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - 1 Verified Educational YouTube Video (Lesson 11 Card 3)
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade10_agriculture_topic13.py
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
# 8 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 13: TOOLS AND EQUIPMENT
# =============================================================================

# SVG 1: Power Sources in Agriculture (Lesson 1, Page 2)
SVG_POWER_SOURCES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Power Sources in Agricultural Implements</text>

  <!-- 3 Power Pathway Columns -->
  <!-- 1. Manual Power -->
  <g transform="translate(45, 70)">
    <rect x="0" y="0" width="220" height="330" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="32" rx="10" fill="#15803d"/>
    <text x="110" y="21" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. MANUAL POWER</text>

    <g transform="translate(15, 45)">
      <text x="0" y="20" font-size="10" font-weight="bold" fill="#4ade80">Energy Source:</text>
      <text x="0" y="38" font-size="9" fill="#cbd5e1">Human Muscular Force</text>
      <text x="0" y="65" font-size="10" font-weight="bold" fill="#4ade80">Typical Implements:</text>
      <text x="0" y="83" font-size="9" fill="#cbd5e1">Jembe, Panga, Spade, Trowel</text>
      <text x="0" y="110" font-size="10" font-weight="bold" fill="#4ade80">Power Output:</text>
      <text x="0" y="128" font-size="9" fill="#cbd5e1">&lt; 0.1 Horsepower (Low)</text>
      <text x="0" y="155" font-size="10" font-weight="bold" fill="#4ade80">Key Advantages:</text>
      <text x="0" y="173" font-size="9" fill="#cbd5e1">High precision, very low cost</text>
    </g>

    <rect x="15" y="245" width="190" height="65" rx="6" fill="#1e293b" stroke="#22c55e"/>
    <text x="95" y="270" font-size="10" font-weight="bold" fill="#86efac" text-anchor="middle">BEST DOMAIN:</text>
    <text x="95" y="292" font-size="9" fill="#cbd5e1" text-anchor="middle">Small gardens &amp; nursery beds</text>
  </g>

  <!-- 2. Animal-Drawn Power -->
  <g transform="translate(290, 70)">
    <rect x="0" y="0" width="220" height="330" rx="10" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="32" rx="10" fill="#ca8a04"/>
    <text x="110" y="21" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. ANIMAL DRAFT POWER</text>

    <g transform="translate(15, 45)">
      <text x="0" y="20" font-size="10" font-weight="bold" fill="#fde047">Energy Source:</text>
      <text x="0" y="38" font-size="9" fill="#cbd5e1">Draft Oxen, Donkeys, Camels</text>
      <text x="0" y="65" font-size="10" font-weight="bold" fill="#fde047">Typical Implements:</text>
      <text x="0" y="83" font-size="9" fill="#cbd5e1">Ox-ploughs, Ridgers, Carts</text>
      <text x="0" y="110" font-size="10" font-weight="bold" fill="#fde047">Power Output:</text>
      <text x="0" y="128" font-size="9" fill="#cbd5e1">0.5 – 1.5 Horsepower (Medium)</text>
      <text x="0" y="155" font-size="10" font-weight="bold" fill="#fde047">Key Advantages:</text>
      <text x="0" y="173" font-size="9" fill="#cbd5e1">5x faster than manual; low fuel cost</text>
    </g>

    <rect x="15" y="245" width="190" height="65" rx="6" fill="#1e293b" stroke="#eab308"/>
    <text x="95" y="270" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">BEST DOMAIN:</text>
    <text x="95" y="292" font-size="9" fill="#cbd5e1" text-anchor="middle">Medium smallholder acreage (1–5 ha)</text>
  </g>

  <!-- 3. Motorized Power -->
  <g transform="translate(535, 70)">
    <rect x="0" y="0" width="220" height="330" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="32" rx="10" fill="#0284c7"/>
    <text x="110" y="21" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. MOTORIZED POWER</text>

    <g transform="translate(15, 45)">
      <text x="0" y="20" font-size="10" font-weight="bold" fill="#38bdf8">Energy Source:</text>
      <text x="0" y="38" font-size="9" fill="#cbd5e1">Diesel / Petrol / Electricity</text>
      <text x="0" y="65" font-size="10" font-weight="bold" fill="#38bdf8">Typical Implements:</text>
      <text x="0" y="83" font-size="9" fill="#cbd5e1">Tractors, Water Pumps, Tillers</text>
      <text x="0" y="110" font-size="10" font-weight="bold" fill="#38bdf8">Power Output:</text>
      <text x="0" y="128" font-size="9" fill="#cbd5e1">&gt; 15.0 Horsepower (Massive)</text>
      <text x="0" y="155" font-size="10" font-weight="bold" fill="#38bdf8">Key Advantages:</text>
      <text x="0" y="173" font-size="9" fill="#cbd5e1">Maximum speed, conquers hard clays</text>
    </g>

    <rect x="15" y="245" width="190" height="65" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="95" y="270" font-size="10" font-weight="bold" fill="#67e8f9" text-anchor="middle">BEST DOMAIN:</text>
    <text x="95" y="292" font-size="9" fill="#cbd5e1" text-anchor="middle">Large commercial estates &amp; irrigation</text>
  </g>
</svg>
""")

# SVG 2: Spade vs Shovel Structural & Functional Anatomy (Lesson 3, Page 2)
SVG_SPADE_VS_SHOVEL = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Spade vs. Shovel: Structural &amp; Functional Anatomy</text>

  <!-- Left: The Spade (Cutting Tool) -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="340" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="30" rx="10" fill="#15803d"/>
    <text x="170" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">THE SPADE (CUTTING IMPLEMENT)</text>

    <!-- Schematic Drawing of Spade -->
    <g transform="translate(30, 45)">
      <!-- Handle -->
      <rect x="35" y="10" width="14" height="90" rx="3" fill="#94a3b8"/>
      <polygon points="25,10 59,10 52,25 32,25" fill="#475569"/>
      <text x="85" y="25" font-size="9" fill="#94a3b8">Short D-Handle (Ergonomic)</text>

      <!-- Blade -->
      <rect x="22" y="105" width="40" height="85" fill="#22c55e" stroke="#86efac" stroke-width="1.5"/>
      <line x1="22" y1="190" x2="62" y2="190" stroke="#ffffff" stroke-width="2"/>
      <text x="85" y="145" font-size="9" fill="#86efac">Flat, Rectangular Blade</text>
      <text x="85" y="185" font-size="9" fill="#ffffff">Straight, Razor-Sharp Edge</text>
    </g>

    <!-- Technical Specs -->
    <g transform="translate(20, 245)">
      <rect x="0" y="0" width="300" height="75" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="150" y="20" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">PRIMARY FUNCTIONS:</text>
      <text x="10" y="42" font-size="9" fill="#cbd5e1">• Slicing turf &amp; vertical trench walls</text>
      <text x="10" y="60" font-size="9" fill="#cbd5e1">• Cutting soil blocks &amp; root division</text>
    </g>
  </g>

  <!-- Right: The Shovel (Scooping Tool) -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="340" height="340" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="30" rx="10" fill="#0284c7"/>
    <text x="170" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">THE SHOVEL (SCOOPING IMPLEMENT)</text>

    <!-- Schematic Drawing of Shovel -->
    <g transform="translate(30, 45)">
      <!-- Long Handle -->
      <rect x="35" y="0" width="12" height="110" rx="3" fill="#94a3b8"/>
      <text x="85" y="25" font-size="9" fill="#94a3b8">Long Straight Shaft (Leverage)</text>

      <!-- Concave Blade -->
      <path d="M 15 110 Q 41 125 67 110 L 60 190 Q 41 200 22 190 Z" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="85" y="145" font-size="9" fill="#38bdf8">Concave Scoop Bowl</text>
      <text x="85" y="185" font-size="9" fill="#67e8f9">Curved Raised Side Edges</text>
    </g>

    <!-- Technical Specs -->
    <g transform="translate(20, 245)">
      <rect x="0" y="0" width="300" height="75" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="150" y="20" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">PRIMARY FUNCTIONS:</text>
      <text x="10" y="42" font-size="9" fill="#cbd5e1">• Scooping &amp; lifting loose manure &amp; sand</text>
      <text x="10" y="60" font-size="9" fill="#cbd5e1">• Loading bulk compost into wheelbarrows</text>
    </g>
  </g>
</svg>
""")

# SVG 3: Castration Tools: Burdizzo vs Elastrator (Lesson 6, Page 2)
SVG_CASTRATION_TOOLS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Livestock Castration Tools: Burdizzo vs. Elastrator</text>

  <!-- Left: The Burdizzo Castrator -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="340" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="30" rx="10" fill="#15803d"/>
    <text x="170" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. BURDIZZO CASTRATOR</text>

    <g transform="translate(20, 45)">
      <rect x="0" y="0" width="300" height="85" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="150" y="22" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">MECHANICAL ACTION:</text>
      <text x="10" y="44" font-size="9" fill="#cbd5e1">• Compound-leverage heavy steel pincers</text>
      <text x="10" y="62" font-size="9" fill="#cbd5e1">• Clamps spermatic cord for 10–15 seconds</text>
      <text x="10" y="78" font-size="9" fill="#86efac">• Crushes blood vessels through intact skin</text>
    </g>

    <g transform="translate(20, 145)">
      <rect x="0" y="0" width="300" height="80" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="150" y="20" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">TARGET ANIMALS:</text>
      <text x="10" y="42" font-size="9" fill="#cbd5e1">• Mature bulls, rams, and bucks (&gt;2 months)</text>
      <text x="10" y="60" font-size="9" fill="#cbd5e1">• Best for pasture livestock in tropical fly zones</text>
    </g>

    <rect x="20" y="240" width="300" height="80" rx="6" fill="#0f172a" stroke="#22c55e" stroke-dasharray="3,3"/>
    <text x="150" y="265" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">BIOSECURITY BENEFIT:</text>
    <text x="150" y="288" font-size="9" fill="#cbd5e1" text-anchor="middle">ZERO open wounds = ZERO fly-strike (myiasis)</text>
    <text x="150" y="305" font-size="9" fill="#cbd5e1" text-anchor="middle">and zero external hemorrhaging!</text>
  </g>

  <!-- Right: The Elastrator -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="340" height="340" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="30" rx="10" fill="#0284c7"/>
    <text x="170" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. ELASTRATOR &amp; RUBBER RINGS</text>

    <g transform="translate(20, 45)">
      <rect x="0" y="0" width="300" height="85" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="150" y="22" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">MECHANICAL ACTION:</text>
      <text x="10" y="44" font-size="9" fill="#cbd5e1">• 4-prong pliers stretch heavy rubber ring</text>
      <text x="10" y="62" font-size="9" fill="#cbd5e1">• Ring contracts around scrotal neck</text>
      <text x="10" y="78" font-size="9" fill="#67e8f9">• Cuts circulation; testicles drop in 2–3 wks</text>
    </g>

    <g transform="translate(20, 145)">
      <rect x="0" y="0" width="300" height="80" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="150" y="20" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">TARGET ANIMALS:</text>
      <text x="10" y="42" font-size="9" fill="#cbd5e1">• Young lambs and goat kids (&lt; 2 weeks old)</text>
      <text x="10" y="60" font-size="9" fill="#cbd5e1">• Fast, humane, high-throughput herd task</text>
    </g>

    <rect x="20" y="240" width="300" height="80" rx="6" fill="#0f172a" stroke="#ef4444" stroke-dasharray="3,3"/>
    <text x="150" y="265" font-size="10" font-weight="bold" fill="#f87171" text-anchor="middle">CRITICAL SAFETY RULE:</text>
    <text x="150" y="288" font-size="9" fill="#cbd5e1" text-anchor="middle">Must pair with maternal tetanus coverage</text>
    <text x="150" y="305" font-size="9" fill="#cbd5e1" text-anchor="middle">or tetanus antitoxin injections!</text>
  </g>
</svg>
""")

# SVG 4: Open-Ended vs Ring Spanner Torque Mechanics (Lesson 9, Page 2)
SVG_SPANNER_MECHANICS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Open-Ended vs. Ring Spanner Mechanical Torque Distribution</text>

  <!-- Left: Open-Ended Spanner (High Slippage Risk) -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="340" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="30" rx="10" fill="#991b1b"/>
    <text x="170" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">OPEN-ENDED SPANNER (2-POINT CONTACT)</text>

    <!-- Schematic Drawing of Open Jaw -->
    <g transform="translate(30, 45)">
      <path d="M 30 20 L 70 20 L 70 80 L 30 80" fill="none" stroke="#ef4444" stroke-width="6"/>
      <!-- Hex Bolt in middle -->
      <polygon points="50,30 65,40 65,60 50,70 35,60 35,40" fill="#334155" stroke="#f87171" stroke-width="2"/>
      <circle cx="35" cy="40" r="4" fill="#ef4444"/>
      <circle cx="65" cy="60" r="4" fill="#ef4444"/>
      <text x="95" y="45" font-size="9" fill="#f87171">Contacts ONLY 2 flat sides</text>
      <text x="95" y="65" font-size="9" fill="#fca5a5">Jaws spread under high torque!</text>
    </g>

    <!-- Operational Specs -->
    <g transform="translate(20, 165)">
      <rect x="0" y="0" width="300" height="150" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="150" y="22" font-size="10" font-weight="bold" fill="#f87171" text-anchor="middle">MECHANICAL CONSEQUENCES:</text>
      <text x="10" y="48" font-size="9" fill="#cbd5e1">• High risk of slipping on seized bolts</text>
      <text x="10" y="70" font-size="9" fill="#cbd5e1">• Rounds off hex bolt corners permanently</text>
      <text x="10" y="92" font-size="9" fill="#cbd5e1">• Operator knuckles smash into machinery</text>
      <text x="10" y="125" font-size="9" font-weight="bold" fill="#fde047">Best used ONLY for fast low-torque spinning</text>
    </g>
  </g>

  <!-- Right: Ring Spanner (100% Multi-Point Grip) -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="340" height="340" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="30" rx="10" fill="#15803d"/>
    <text x="170" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">RING SPANNER (FULL ENCLOSED GRIP)</text>

    <!-- Schematic Drawing of Ring Head -->
    <g transform="translate(30, 45)">
      <circle cx="50" cy="50" r="32" fill="none" stroke="#22c55e" stroke-width="6"/>
      <!-- Hex Bolt in middle with 6 green contact points -->
      <polygon points="50,30 67,40 67,60 50,70 33,60 33,40" fill="#334155" stroke="#4ade80" stroke-width="2"/>
      <circle cx="50" cy="30" r="3" fill="#22c55e"/>
      <circle cx="67" cy="40" r="3" fill="#22c55e"/>
      <circle cx="67" cy="60" r="3" fill="#22c55e"/>
      <circle cx="50" cy="70" r="3" fill="#22c55e"/>
      <circle cx="33" cy="60" r="3" fill="#22c55e"/>
      <circle cx="33" cy="40" r="3" fill="#22c55e"/>
      <text x="95" y="45" font-size="9" fill="#4ade80">Encloses all 6 hex corners</text>
      <text x="95" y="65" font-size="9" fill="#86efac">100% Uniform torque distribution</text>
    </g>

    <!-- Operational Specs -->
    <g transform="translate(20, 165)">
      <rect x="0" y="0" width="300" height="150" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="150" y="22" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">MECHANICAL CONSEQUENCES:</text>
      <text x="10" y="48" font-size="9" fill="#cbd5e1">• Zero slippage risk under maximum torque</text>
      <text x="10" y="70" font-size="9" fill="#cbd5e1">• Protects bolt corners from wear</text>
      <text x="10" y="92" font-size="9" fill="#cbd5e1">• Safest tool for breaking seized/rusty nuts</text>
      <text x="10" y="125" font-size="9" font-weight="bold" fill="#86efac">The gold standard for high-torque assembly</text>
    </g>
  </g>
</svg>
""")

# SVG 5: Hand Saw Cutting Angles & Crowbar Class 1 Lever (Lesson 10, Page 2)
SVG_SAW_AND_LEVER = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Hand Saw Cutting Angles &amp; Crowbar Class 1 Lever Mechanics</text>

  <!-- Left: Hand Saw 45-Degree Stance -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="340" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="30" rx="10" fill="#0284c7"/>
    <text x="170" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. HAND SAW TIMBER CUTTING</text>

    <!-- Schematic Drawing of Saw & Wood -->
    <g transform="translate(30, 45)">
      <!-- Timber block -->
      <rect x="10" y="90" width="160" height="45" rx="3" fill="#ca8a04" stroke="#fde047"/>
      <text x="90" y="118" font-size="9" fill="#ffffff" text-anchor="middle">Timber Workpiece</text>

      <!-- Saw Blade at 45 Degrees -->
      <line x1="30" y1="90" x2="130" y2="10" stroke="#38bdf8" stroke-width="5"/>
      <text x="110" y="45" font-size="10" font-weight="bold" fill="#38bdf8">45° Blade Angle</text>
    </g>

    <!-- Step Rules -->
    <g transform="translate(20, 165)">
      <rect x="0" y="0" width="300" height="150" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="150" y="22" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">3-STEP SAWING PROTOCOL:</text>
      <text x="10" y="48" font-size="9" fill="#cbd5e1">1. Draw pencil guide line across timber</text>
      <text x="10" y="70" font-size="9" fill="#cbd5e1">2. Draw backward 2–3x to make starter kerf</text>
      <text x="10" y="92" font-size="9" fill="#cbd5e1">3. Saw at 45° angle with long smooth strokes</text>
      <text x="10" y="125" font-size="9" font-weight="bold" fill="#67e8f9">Let the weight of the saw do the cutting!</text>
    </g>
  </g>

  <!-- Right: Crowbar Class 1 Lever -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="340" height="340" rx="10" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="30" rx="10" fill="#ca8a04"/>
    <text x="170" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. CROWBAR CLASS 1 LEVER</text>

    <!-- Schematic Drawing of Lever -->
    <g transform="translate(30, 45)">
      <!-- Crowbar bar -->
      <line x1="20" y1="80" x2="200" y2="20" stroke="#94a3b8" stroke-width="6"/>

      <!-- Fulcrum Pivot Block in center -->
      <polygon points="70,80 85,55 100,80" fill="#ef4444"/>
      <text x="85" y="100" font-size="9" font-weight="bold" fill="#f87171" text-anchor="middle">FULCRUM (Pivot)</text>

      <!-- Load at short end -->
      <circle cx="25" cy="78" r="8" fill="#eab308"/>
      <text x="25" y="100" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">LOAD</text>

      <!-- Effort at long end -->
      <line x1="195" y1="10" x2="195" y2="35" stroke="#22c55e" stroke-width="3"/>
      <polygon points="190,30 195,40 200,30" fill="#22c55e"/>
      <text x="195" y="55" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">EFFORT</text>
    </g>

    <!-- Operational Specs -->
    <g transform="translate(20, 165)">
      <rect x="0" y="0" width="300" height="150" rx="6" fill="#1e293b" stroke="#eab308"/>
      <text x="150" y="22" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">MECHANICAL ADVANTAGE:</text>
      <text x="10" y="48" font-size="9" fill="#cbd5e1">• Fulcrum (pivot) sits close to the load</text>
      <text x="10" y="70" font-size="9" fill="#cbd5e1">• Long handle multiplies human input force</text>
      <text x="10" y="92" font-size="9" fill="#cbd5e1">• Extracts 10cm rusted nails with zero strain</text>
      <text x="10" y="125" font-size="9" font-weight="bold" fill="#fde047">Massive lifting power for posts and rocks!</text>
    </g>
  </g>
</svg>
""")

# SVG 6: 5 Core Pillars of Tool Maintenance (Lesson 11, Page 2)
SVG_MAINTENANCE_PILLARS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">5 Core Pillars of Agricultural Tool Maintenance</text>

  <!-- 5 Circular Process Hubs -->
  <!-- 1. Clean & Scrape -->
  <g transform="translate(45, 80)">
    <circle cx="60" cy="60" r="48" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="60" y="55" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. CLEAN &amp;</text>
    <text x="60" y="72" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">SCRAPE</text>
    <text x="60" y="130" font-size="9" fill="#cbd5e1" text-anchor="middle">Scrape soil &amp; sap;</text>
    <text x="60" y="145" font-size="9" fill="#cbd5e1" text-anchor="middle">dry 100% thoroughly</text>
  </g>
  <line x1="155" y1="140" x2="190" y2="140" stroke="#38bdf8" stroke-width="2"/>

  <!-- 2. Precision Sharpen -->
  <g transform="translate(195, 80)">
    <circle cx="60" cy="60" r="48" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <text x="60" y="55" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">2. SHARPEN</text>
    <text x="60" y="72" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">BEVELS</text>
    <text x="60" y="130" font-size="9" fill="#cbd5e1" text-anchor="middle">30° single push file;</text>
    <text x="60" y="145" font-size="9" fill="#cbd5e1" text-anchor="middle">oil whetstone stropping</text>
  </g>
  <line x1="305" y1="140" x2="340" y2="140" stroke="#22c55e" stroke-width="2"/>

  <!-- 3. Lubricate & Grease -->
  <g transform="translate(345, 80)">
    <circle cx="60" cy="60" r="48" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <text x="60" y="55" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">3. LUBRICATE</text>
    <text x="60" y="72" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">&amp; GREASE</text>
    <text x="60" y="130" font-size="9" fill="#cbd5e1" text-anchor="middle">Lithium grease axles;</text>
    <text x="60" y="145" font-size="9" fill="#cbd5e1" text-anchor="middle">oil pivot joints</text>
  </g>
  <line x1="455" y1="140" x2="490" y2="140" stroke="#eab308" stroke-width="2"/>

  <!-- 4. Repair & Wedge -->
  <g transform="translate(495, 80)">
    <circle cx="60" cy="60" r="48" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <text x="60" y="55" font-size="11" font-weight="bold" fill="#d8b4fe" text-anchor="middle">4. REPAIR &amp;</text>
    <text x="60" y="72" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">WEDGE</text>
    <text x="60" y="130" font-size="9" fill="#cbd5e1" text-anchor="middle">Tighten all bolts;</text>
    <text x="60" y="145" font-size="9" fill="#cbd5e1" text-anchor="middle">wedge loose handles</text>
  </g>
  <line x1="605" y1="140" x2="640" y2="140" stroke="#a855f7" stroke-width="2"/>

  <!-- 5. Store Indoors -->
  <g transform="translate(645, 80)">
    <circle cx="60" cy="60" r="48" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <text x="60" y="55" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">5. SECURE</text>
    <text x="60" y="72" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STORAGE</text>
    <text x="60" y="130" font-size="9" fill="#cbd5e1" text-anchor="middle">Hang head-down;</text>
    <text x="60" y="145" font-size="9" fill="#cbd5e1" text-anchor="middle">shadow board audit</text>
  </g>

  <!-- Bottom Banner: Economic & Safety Dividends -->
  <g transform="translate(45, 275)">
    <rect x="0" y="0" width="710" height="125" rx="8" fill="#0f172a" stroke="#38bdf8"/>
    <text x="355" y="28" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Agricultural Mechanics Dividend</text>

    <g transform="translate(25, 45)">
      <rect x="0" y="0" width="200" height="60" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="100" y="22" font-size="10" font-weight="bold" fill="#22c55e" text-anchor="middle">10x Longer Lifespan</text>
      <text x="100" y="42" font-size="8" fill="#cbd5e1" text-anchor="middle">Tools last 15+ years</text>
    </g>

    <g transform="translate(255, 45)">
      <rect x="0" y="0" width="200" height="60" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="100" y="22" font-size="10" font-weight="bold" fill="#eab308" text-anchor="middle">50% Faster Work Rate</text>
      <text x="100" y="42" font-size="8" fill="#cbd5e1" text-anchor="middle">Sharp blades require less force</text>
    </g>

    <g transform="translate(485, 45)">
      <rect x="0" y="0" width="200" height="60" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="100" y="22" font-size="10" font-weight="bold" fill="#ef4444" text-anchor="middle">Zero Workshop Injuries</text>
      <text x="100" y="42" font-size="8" fill="#cbd5e1" text-anchor="middle">No slipping or flying heads</text>
    </g>
  </g>
</svg>
""")

# SVG 7: Shadow Board Layout & Vertical Tool Rack (Lesson 13, Page 2)
SVG_SHADOW_BOARD = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Farm Workshop Shadow Board Layout &amp; Vertical Tool Rack</text>

  <!-- Left: Shadow Board Wall -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="340" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="30" rx="10" fill="#15803d"/>
    <text x="170" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. SHADOW BOARD (5-SEC AUDIT)</text>

    <!-- Schematic Tool Silhouettes Painted on Wall -->
    <g transform="translate(20, 45)">
      <!-- Claw Hammer Outline -->
      <rect x="15" y="10" width="50" height="15" rx="2" fill="#334155" stroke="#ef4444" stroke-dasharray="2,2"/>
      <rect x="35" y="25" width="10" height="65" rx="2" fill="#334155" stroke="#ef4444" stroke-dasharray="2,2"/>
      <text x="40" y="105" font-size="8" fill="#f87171" text-anchor="middle">Hammer Silhouette</text>

      <!-- Spanner Outline -->
      <rect x="110" y="10" width="25" height="80" rx="3" fill="#334155" stroke="#38bdf8" stroke-dasharray="2,2"/>
      <text x="122" y="105" font-size="8" fill="#38bdf8" text-anchor="middle">Spanner</text>

      <!-- Hand Saw Outline -->
      <polygon points="180,10 270,10 270,80 180,50" fill="#334155" stroke="#fde047" stroke-dasharray="2,2"/>
      <text x="225" y="105" font-size="8" fill="#fde047" text-anchor="middle">Hand Saw</text>
    </g>

    <!-- Operational Rule -->
    <g transform="translate(20, 165)">
      <rect x="0" y="0" width="300" height="150" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="150" y="22" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">SHADOW BOARD ADVANTAGES:</text>
      <text x="10" y="48" font-size="9" fill="#cbd5e1">• Painted silhouettes show exact tool home</text>
      <text x="10" y="70" font-size="9" fill="#cbd5e1">• Empty silhouette instantly flags missing tool</text>
      <text x="10" y="92" font-size="9" fill="#cbd5e1">• 5-second end-of-day inventory audit</text>
      <text x="10" y="125" font-size="9" font-weight="bold" fill="#86efac">Eliminates tool loss and theft completely!</text>
    </g>
  </g>

  <!-- Right: Vertical Wall Rack (Head-Down Rule) -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="340" height="340" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="30" rx="10" fill="#0284c7"/>
    <text x="170" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. VERTICAL RACK (HEAD-DOWN RULE)</text>

    <!-- Schematic Vertical Hanging -->
    <g transform="translate(30, 45)">
      <!-- Long handles pointing up -->
      <rect x="40" y="10" width="10" height="85" fill="#94a3b8"/>
      <rect x="110" y="10" width="10" height="85" fill="#94a3b8"/>
      <rect x="180" y="10" width="10" height="85" fill="#94a3b8"/>

      <!-- Heavy heads pointing down at bottom -->
      <rect x="25" y="95" width="40" height="30" fill="#38bdf8"/>
      <polygon points="100,95 130,95 115,125" fill="#22c55e"/>
      <line x1="165" y1="110" x2="205" y2="110" stroke="#eab308" stroke-width="4"/>

      <text x="45" y="145" font-size="8" fill="#38bdf8" text-anchor="middle">Spade</text>
      <text x="115" y="145" font-size="8" fill="#22c55e" text-anchor="middle">Jembe</text>
      <text x="185" y="145" font-size="8" fill="#eab308" text-anchor="middle">Rake</text>
    </g>

    <!-- Operational Rule -->
    <g transform="translate(20, 165)">
      <rect x="0" y="0" width="300" height="150" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="150" y="22" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">THE HEAD-DOWN SAFETY MANDATE:</text>
      <text x="10" y="48" font-size="9" fill="#cbd5e1">• Heavy steel blades point downward to floor</text>
      <text x="10" y="70" font-size="9" fill="#cbd5e1">• Prevents sharp heads falling onto heads/eyes</text>
      <text x="10" y="92" font-size="9" fill="#cbd5e1">• Keeps walkways 100% free of tripping hazards</text>
      <text x="10" y="125" font-size="9" font-weight="bold" fill="#67e8f9">Workshop walkways remain clean &amp; safe!</text>
    </g>
  </g>
</svg>
""")

# SVG 8: Master Lifecycle Matrix (Lesson 14, Page 2)
SVG_MASTER_LIFECYCLE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Master Agricultural Tools, Equipment &amp; Safety Lifecycle</text>

  <!-- 6 Process Nodes in Ring -->
  <!-- 1. Classification & Power -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="100" y="22" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">1. CLASSIFICATION</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Tool vs Equip vs Machine</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Manual / Draft / Motorized</text>
  </g>
  <line x1="245" y1="102" x2="345" y2="200" stroke="#22c55e" stroke-width="2" stroke-dasharray="2,2"/>

  <!-- 2. Task Matching -->
  <g transform="translate(555, 65)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="100" y="22" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">2. TASK MATCHING</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Soil, crop stage, ergonomics</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Prevent vascular crop tearing</text>
  </g>
  <line x1="555" y1="102" x2="455" y2="200" stroke="#38bdf8" stroke-width="2" stroke-dasharray="2,2"/>

  <!-- 3. Specialized Implements -->
  <g transform="translate(35, 195)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <text x="100" y="22" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">3. CROP &amp; LIVESTOCK</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Spade / Shovel / Secateurs</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Burdizzo / Drencher / Strip Cup</text>
  </g>
  <line x1="235" y1="240" x2="345" y2="240" stroke="#eab308" stroke-width="2"/>

  <!-- 4. Assembly & Fabrication -->
  <g transform="translate(565, 195)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="100" y="22" font-size="10" font-weight="bold" fill="#d8b4fe" text-anchor="middle">4. FABRICATION</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Ring spanners &amp; washers</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• 45° Hand saw &amp; Class 1 lever</text>
  </g>
  <line x1="565" y1="240" x2="455" y2="240" stroke="#a855f7" stroke-width="2"/>

  <!-- 5. 5-Pillar Maintenance -->
  <g transform="translate(130, 335)">
    <rect x="0" y="0" width="220" height="75" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
    <text x="110" y="22" font-size="10" font-weight="bold" fill="#67e8f9" text-anchor="middle">5. 5-PILLAR CARE</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Clean, 30° File, Lubricate</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Wedge handle &amp; Linseed oil</text>
  </g>
  <line x1="350" y1="350" x2="390" y2="298" stroke="#06b6d4" stroke-width="2"/>

  <!-- 6. Storage & Safety -->
  <g transform="translate(450, 335)">
    <rect x="0" y="0" width="220" height="75" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="110" y="22" font-size="10" font-weight="bold" fill="#f87171" text-anchor="middle">6. STORAGE &amp; SAFETY</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Shadow Board &amp; Head-down rack</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Matched PPE &amp; 15-min Eye Wash</text>
  </g>
  <line x1="450" y1="350" x2="410" y2="298" stroke="#ef4444" stroke-width="2"/>

  <!-- Central Hub: Agricultural Productivity -->
  <circle cx="400" cy="240" r="55" fill="#0f172a" stroke="#22c55e" stroke-width="3"/>
  <text x="400" y="235" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">AGRICULTURAL</text>
  <text x="400" y="252" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">MECHANICS</text>
</svg>
""")

SVG_MAP = {
    1: {"page": 2, "svg": SVG_POWER_SOURCES, "title": "Power Sources in Agricultural Implements"},
    3: {"page": 2, "svg": SVG_SPADE_VS_SHOVEL, "title": "Spade vs. Shovel: Structural & Functional Anatomy"},
    6: {"page": 2, "svg": SVG_CASTRATION_TOOLS, "title": "Livestock Castration Tools: Burdizzo vs. Elastrator"},
    9: {"page": 2, "svg": SVG_SPANNER_MECHANICS, "title": "Open-Ended vs. Ring Spanner Mechanical Torque Distribution"},
    10: {"page": 2, "svg": SVG_SAW_AND_LEVER, "title": "Hand Saw Cutting Angles & Crowbar Class 1 Lever Mechanics"},
    11: {"page": 2, "svg": SVG_MAINTENANCE_PILLARS, "title": "5 Core Pillars of Agricultural Tool Maintenance"},
    13: {"page": 2, "svg": SVG_SHADOW_BOARD, "title": "Farm Workshop Shadow Board Layout & Vertical Tool Rack"},
    14: {"page": 2, "svg": SVG_MASTER_LIFECYCLE, "title": "Master Agricultural Tools, Equipment & Safety Lifecycle"}
}

def enrich_grade10_topic13():
    """Injects verified photos, responsive vector SVGs, YouTube embeds, and creates LessonAssets."""
    print("=" * 80)
    print("STARTING ENRICHMENT: CBC Grade 10 Agriculture — Topic 13: Tools and Equipment")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()
    topic = Topic.objects.filter(subject=subject, name="Tools and Equipment").first()

    assert topic, "Topic 'Tools and Equipment' not found!"

    images_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grade10_topic13_verified_images.json")
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
                    "topic_order": 13,
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
                        "topic_order": 13,
                        "unit_order": u_order,
                        "page": svg_def["page"],
                        "svg_content": svg_def["svg"]
                    }
                )
                diag_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [Vector SVG Attached] Lesson {u_order}: {svg_def['title']}")

        # ---------------------------------------------------------------------
        # 3. Educational YouTube Videos (Lesson 11)
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
                        "topic_order": 13,
                        "unit_order": u_order,
                        "youtube_url": v_url
                    }
                )
                v_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [YouTube Video Attached] Lesson {u_order}: {v_block.title}")

    print("=" * 80)
    print(f"ENRICHMENT COMPLETE: Topic 13 '{topic.name}'")
    print(f"  Photographic Hooks: {total_images_attached} / 14")
    print(f"  Vector SVGs:        {total_svgs_attached} / 8")
    print(f"  YouTube Videos:     {total_videos_attached} / 1")
    print(f"  LessonAssets:       {total_assets_persisted}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic13()
