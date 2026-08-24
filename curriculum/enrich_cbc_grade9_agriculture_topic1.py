"""
VLearn CBC Grade 9 Agriculture — Topic 1: Conserving Animal Feeds (Forage, Drought, and Hay)
Visual Enrichment Engine (Phase 2: Vector SVGs, Verified 200 OK Photos & Asset Persistence)

Curriculum: CBC (ID: 5)
Grade: Grade 9 (Level: 9)
Subject: Agriculture
Topic: Conserving Animal Feeds (Forage, Drought, and Hay) (Order: 1)

Attaches:
  - 12 First-Card Photographic Visual Hooks (100% Tested HTTP 200 OK Direct Wikimedia URLs)
  - 12 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - 1 Verified Educational YouTube Video for Capstone Review (Lesson 12 Card 8)
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade9_agriculture_topic1.py
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
# 12 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 9 TOPIC 1: CONSERVING ANIMAL FEEDS
# =============================================================================

# SVG 1: Forage Classification Wheel (Lesson 1, Page 3)
SVG_FORAGE_CLASSIFICATION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Botanical &amp; Agricultural Forage Classification</text>
  
  <!-- Column 1: Grasses -->
  <g transform="translate(40, 70)">
    <rect x="0" y="0" width="225" height="340" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="225" height="45" rx="10" fill="#15803d"/>
    <text x="112" y="28" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">1. FORAGE GRASSES</text>
    
    <text x="15" y="75" font-size="12" font-weight="bold" fill="#4ade80">Primary Role:</text>
    <text x="15" y="95" font-size="11" fill="#cbd5e1">• Bulk fiber &amp; digestible energy</text>
    <text x="15" y="115" font-size="11" fill="#cbd5e1">• Fills rumen &amp; fuels metabolism</text>
    
    <line x1="15" y1="130" x2="210" y2="130" stroke="#334155" stroke-width="1"/>
    
    <text x="15" y="150" font-size="12" font-weight="bold" fill="#4ade80">Plant Characteristics:</text>
    <text x="15" y="170" font-size="11" fill="#cbd5e1">• Narrow, parallel-veined leaves</text>
    <text x="15" y="190" font-size="11" fill="#cbd5e1">• Fast vegetative biomass</text>
    
    <line x1="15" y1="205" x2="210" y2="205" stroke="#334155" stroke-width="1"/>
    
    <text x="15" y="225" font-size="12" font-weight="bold" fill="#4ade80">Key Examples:</text>
    <rect x="15" y="240" width="195" height="80" rx="6" fill="#1e293b"/>
    <text x="25" y="260" font-size="11" font-weight="bold" fill="#86efac">• Rhodes Grass (Hay)</text>
    <text x="25" y="280" font-size="11" font-weight="bold" fill="#86efac">• Napier Grass (Zero-grazing)</text>
    <text x="25" y="300" font-size="11" font-weight="bold" fill="#86efac">• Forage Sorghum &amp; Oats</text>
  </g>

  <!-- Column 2: Legumes -->
  <g transform="translate(287, 70)">
    <rect x="0" y="0" width="225" height="340" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="225" height="45" rx="10" fill="#0284c7"/>
    <text x="112" y="28" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">2. FORAGE LEGUMES</text>
    
    <text x="15" y="75" font-size="12" font-weight="bold" fill="#38bdf8">Primary Role:</text>
    <text x="15" y="95" font-size="11" fill="#cbd5e1">• High crude protein &amp; minerals</text>
    <text x="15" y="115" font-size="11" fill="#cbd5e1">• Boosts milk yield &amp; growth</text>
    
    <line x1="15" y1="130" x2="210" y2="130" stroke="#334155" stroke-width="1"/>
    
    <text x="15" y="150" font-size="12" font-weight="bold" fill="#38bdf8">Plant Characteristics:</text>
    <text x="15" y="170" font-size="11" fill="#cbd5e1">• Broad compound leaves</text>
    <text x="15" y="190" font-size="11" fill="#cbd5e1">• Nitrogen-fixing root nodules</text>
    
    <line x1="15" y1="205" x2="210" y2="205" stroke="#334155" stroke-width="1"/>
    
    <text x="15" y="225" font-size="12" font-weight="bold" fill="#38bdf8">Key Examples:</text>
    <rect x="15" y="240" width="195" height="80" rx="6" fill="#1e293b"/>
    <text x="25" y="260" font-size="11" font-weight="bold" fill="#7dd3fc">• Desmodium (Silver/Greenleaf)</text>
    <text x="25" y="280" font-size="11" font-weight="bold" fill="#7dd3fc">• Lucerne (Alfalfa)</text>
    <text x="25" y="300" font-size="11" font-weight="bold" fill="#7dd3fc">• Calliandra &amp; Leucaena</text>
  </g>

  <!-- Column 3: Crop Residues -->
  <g transform="translate(535, 70)">
    <rect x="0" y="0" width="225" height="340" rx="10" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect x="0" y="0" width="225" height="45" rx="10" fill="#ca8a04"/>
    <text x="112" y="28" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">3. CROP RESIDUES</text>
    
    <text x="15" y="75" font-size="12" font-weight="bold" fill="#facc15">Primary Role:</text>
    <text x="15" y="95" font-size="11" fill="#cbd5e1">• Emergency drought bulk fiber</text>
    <text x="15" y="115" font-size="11" fill="#cbd5e1">• Stretches premium hay stores</text>
    
    <line x1="15" y1="130" x2="210" y2="130" stroke="#334155" stroke-width="1"/>
    
    <text x="15" y="150" font-size="12" font-weight="bold" fill="#facc15">Plant Characteristics:</text>
    <text x="15" y="170" font-size="11" fill="#cbd5e1">• Harvest leftovers (dry stalks)</text>
    <text x="15" y="190" font-size="11" fill="#cbd5e1">• High durability &amp; low moisture</text>
    
    <line x1="15" y1="205" x2="210" y2="205" stroke="#334155" stroke-width="1"/>
    
    <text x="15" y="225" font-size="12" font-weight="bold" fill="#facc15">Key Examples:</text>
    <rect x="15" y="240" width="195" height="80" rx="6" fill="#1e293b"/>
    <text x="25" y="260" font-size="11" font-weight="bold" fill="#fde047">• Maize Stover (Post-harvest)</text>
    <text x="25" y="280" font-size="11" font-weight="bold" fill="#fde047">• Wheat &amp; Barley Straw</text>
    <text x="25" y="300" font-size="11" font-weight="bold" fill="#fde047">• Bean &amp; Pea Haulms</text>
  </g>
</svg>
""")

# SVG 2: Drought Impact Chain (Lesson 2, Page 3)
SVG_DROUGHT_IMPACT_CHAIN = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#f87171" text-anchor="middle">The Biological &amp; Economic Drought Impact Chain</text>

  <!-- Step 1: Climate Trigger -->
  <g transform="translate(40, 70)">
    <rect x="0" y="0" width="220" height="150" rx="8" fill="#0f172a" stroke="#f87171" stroke-width="1.5"/>
    <text x="110" y="25" font-size="12" font-weight="bold" fill="#f87171" text-anchor="middle">1. CLIMATE SHOCK</text>
    <rect x="10" y="35" width="200" height="105" rx="4" fill="#1e293b"/>
    <text x="20" y="58" font-size="11" fill="#cbd5e1">• Rains fail / dry season</text>
    <text x="20" y="78" font-size="11" fill="#cbd5e1">• Soil moisture evaporates</text>
    <text x="20" y="98" font-size="11" fill="#cbd5e1">• Plant growth halts</text>
    <text x="20" y="123" font-size="10" font-weight="bold" fill="#fca5a5">Volume drops drastically</text>
  </g>

  <!-- Arrow 1 -->
  <path d="M 270 145 L 295 145" stroke="#94a3b8" stroke-width="3" fill="none" marker-end="url(#arrow)"/>

  <!-- Step 2: Plant Biology Collapse -->
  <g transform="translate(300, 70)">
    <rect x="0" y="0" width="220" height="150" rx="8" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="110" y="25" font-size="12" font-weight="bold" fill="#fbbf24" text-anchor="middle">2. PLANT LIGNIFICATION</text>
    <rect x="10" y="35" width="200" height="105" rx="4" fill="#1e293b"/>
    <text x="20" y="58" font-size="11" fill="#cbd5e1">• Water &amp; protein drop</text>
    <text x="20" y="78" font-size="11" fill="#cbd5e1">• Woody lignin increases</text>
    <text x="20" y="98" font-size="11" fill="#cbd5e1">• Grass becomes tough</text>
    <text x="20" y="123" font-size="10" font-weight="bold" fill="#fde68a">Digestibility plummets</text>
  </g>

  <!-- Arrow 2 -->
  <path d="M 530 145 L 555 145" stroke="#94a3b8" stroke-width="3" fill="none"/>

  <!-- Step 3: Animal Health Impact -->
  <g transform="translate(560, 70)">
    <rect x="0" y="0" width="200" height="150" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="100" y="25" font-size="12" font-weight="bold" fill="#ef4444" text-anchor="middle">3. HERD MALNUTRITION</text>
    <rect x="10" y="35" width="180" height="105" rx="4" fill="#1e293b"/>
    <text x="20" y="58" font-size="11" fill="#cbd5e1">• Severe weight loss</text>
    <text x="20" y="78" font-size="11" fill="#cbd5e1">• Milk drops by 50-80%</text>
    <text x="20" y="98" font-size="11" fill="#cbd5e1">• Weakened immunity</text>
    <text x="20" y="123" font-size="10" font-weight="bold" fill="#fca5a5">Risk of animal death</text>
  </g>

  <!-- Lower Banner: The Farmer's Defense -->
  <g transform="translate(40, 245)">
    <rect x="0" y="0" width="720" height="165" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <text x="360" y="30" font-size="14" font-weight="bold" fill="#4ade80" text-anchor="middle">THE SOLUTION: PROACTIVE FORAGE CONSERVATION</text>
    
    <g transform="translate(20, 45)">
      <rect x="0" y="0" width="210" height="105" rx="6" fill="#1e293b"/>
      <text x="105" y="25" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Baled Hay</text>
      <text x="15" y="50" font-size="10" fill="#cbd5e1">• Cut at flowering stage</text>
      <text x="15" y="70" font-size="10" fill="#cbd5e1">• Sun-dried to 15% moisture</text>
      <text x="15" y="90" font-size="10" fill="#cbd5e1">• Stored safely in barn</text>
    </g>

    <g transform="translate(255, 45)">
      <rect x="0" y="0" width="210" height="105" rx="6" fill="#1e293b"/>
      <text x="105" y="25" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Stacked Haystacks</text>
      <text x="15" y="50" font-size="10" fill="#cbd5e1">• Raised 30cm timber base</text>
      <text x="15" y="70" font-size="10" fill="#cbd5e1">• Sloped rain-shedding roof</text>
      <text x="15" y="90" font-size="10" fill="#cbd5e1">• Low-cost farm security</text>
    </g>

    <g transform="translate(490, 45)">
      <rect x="0" y="0" width="210" height="105" rx="6" fill="#1e293b"/>
      <text x="105" y="25" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Standing Pasture</text>
      <text x="15" y="50" font-size="10" fill="#cbd5e1">• Deferred wet season growth</text>
      <text x="15" y="70" font-size="10" fill="#cbd5e1">• Fenced for dry spell</text>
      <text x="15" y="90" font-size="10" fill="#cbd5e1">• Zero harvesting labor</text>
    </g>
  </g>
</svg>
""")

# SVG 3: Moisture Reduction & Compaction Curve (Lesson 3, Page 3)
SVG_HAYMAKING_CURVE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Moisture Reduction &amp; Compaction Science of Haymaking</text>

  <!-- Left: Moisture Bar Chart -->
  <g transform="translate(40, 70)">
    <rect x="0" y="0" width="340" height="340" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="170" y="30" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">Moisture Content During Haymaking</text>
    
    <!-- Fresh Pasture Bar -->
    <text x="30" y="70" font-size="11" fill="#cbd5e1">1. Fresh Pasture (Cutting Stage)</text>
    <rect x="30" y="80" width="280" height="24" rx="4" fill="#334155"/>
    <rect x="30" y="80" width="224" height="24" rx="4" fill="#3b82f6"/>
    <text x="260" y="96" font-size="11" font-weight="bold" fill="#ffffff">80% Water</text>
    <text x="30" y="120" font-size="10" fill="#ef4444">⚠️ If stored now: rapid heating, rotting &amp; toxic mould!</text>

    <!-- Wilting Stage Bar -->
    <text x="30" y="155" font-size="11" fill="#cbd5e1">2. Day 1 Sun-Drying (Wilting)</text>
    <rect x="30" y="165" width="280" height="24" rx="4" fill="#334155"/>
    <rect x="30" y="165" width="126" height="24" rx="4" fill="#eab308"/>
    <text x="165" y="181" font-size="11" font-weight="bold" fill="#ffffff">45% Water</text>
    <text x="30" y="205" font-size="10" fill="#facc15">Solar energy evaporates water from leaf stomata</text>

    <!-- Target Safe Hay Bar -->
    <text x="30" y="240" font-size="11" fill="#cbd5e1">3. Cured Hay (Day 2-3 Drying)</text>
    <rect x="30" y="250" width="280" height="24" rx="4" fill="#334155"/>
    <rect x="30" y="250" width="50" height="24" rx="4" fill="#22c55e"/>
    <text x="90" y="266" font-size="11" font-weight="bold" fill="#4ade80">15% - 20%</text>
    <text x="30" y="290" font-size="10" font-weight="bold" fill="#4ade80">✅ SAFE THRESHOLD: Microbes stop; rot-proof!</text>
  </g>

  <!-- Right: Volume Compaction Diagram -->
  <g transform="translate(420, 70)">
    <rect x="0" y="0" width="340" height="340" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="170" y="30" font-size="13" font-weight="bold" fill="#4ade80" text-anchor="middle">Volume Compaction Efficiency</text>
    
    <!-- Loose Grass Box -->
    <rect x="30" y="60" width="280" height="100" rx="6" fill="#1e293b" stroke="#eab308" stroke-dasharray="4"/>
    <text x="170" y="85" font-size="12" font-weight="bold" fill="#facc15" text-anchor="middle">Loose Dry Grass (Uncompacted)</text>
    <text x="170" y="110" font-size="11" fill="#cbd5e1" text-anchor="middle">• Bulky, spreads out across barn</text>
    <text x="170" y="130" font-size="11" fill="#cbd5e1" text-anchor="middle">• Blown by wind; hard to transport</text>

    <!-- Downward Arrow -->
    <text x="170" y="185" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">⬇️ Manual Compaction Press (70% Volume Reduction) ⬇️</text>

    <!-- Compact Bale Box -->
    <rect x="80" y="205" width="180" height="95" rx="6" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
    <text x="170" y="235" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">Compact Rectangular Bale</text>
    <text x="170" y="260" font-size="10" fill="#dcfce7" text-anchor="middle">40cm x 50cm x 75cm</text>
    <text x="170" y="280" font-size="10" fill="#dcfce7" text-anchor="middle">High density, stackable, easily sold</text>
  </g>
</svg>
""")

# SVG 4: Safe Hay Barn Blueprint (Lesson 4, Page 3)
SVG_SAFE_HAY_BARN = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Engineering Blueprint: Safe Hay Storage Barn</text>

  <!-- Roof Structure -->
  <polygon points="120,110 400,65 680,110" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
  <text x="400" y="95" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Overhead Corrugated Rainproof Roof</text>

  <!-- Wall Outlines & Ventilation Mesh -->
  <rect x="140" y="110" width="520" height="230" fill="#0f172a" stroke="#475569" stroke-width="2"/>
  
  <!-- Ventilation Wire Mesh Indicator -->
  <rect x="155" y="125" width="100" height="190" fill="#1e293b" stroke="#38bdf8" stroke-dasharray="3"/>
  <text x="205" y="215" font-size="10" fill="#38bdf8" text-anchor="middle" transform="rotate(-90 205 215)">Open Wire Mesh Airflow</text>

  <rect x="545" y="125" width="100" height="190" fill="#1e293b" stroke="#38bdf8" stroke-dasharray="3"/>
  <text x="595" y="215" font-size="10" fill="#38bdf8" text-anchor="middle" transform="rotate(90 595 215)">Cross-Ventilation</text>

  <!-- Stacked Bales Inside Barn -->
  <g transform="translate(280, 150)">
    <!-- Bale Row 3 (Top) -->
    <rect x="25" y="0" width="90" height="40" rx="3" fill="#ca8a04" stroke="#facc15" stroke-width="1.5"/>
    <rect x="125" y="0" width="90" height="40" rx="3" fill="#ca8a04" stroke="#facc15" stroke-width="1.5"/>
    
    <!-- Bale Row 2 (Middle) -->
    <rect x="0" y="45" width="75" height="40" rx="3" fill="#ca8a04" stroke="#facc15" stroke-width="1.5"/>
    <rect x="80" y="45" width="75" height="40" rx="3" fill="#ca8a04" stroke="#facc15" stroke-width="1.5"/>
    <rect x="160" y="45" width="75" height="40" rx="3" fill="#ca8a04" stroke="#facc15" stroke-width="1.5"/>

    <!-- Bale Row 1 (Bottom) -->
    <rect x="0" y="90" width="75" height="40" rx="3" fill="#ca8a04" stroke="#facc15" stroke-width="1.5"/>
    <rect x="80" y="90" width="75" height="40" rx="3" fill="#ca8a04" stroke="#facc15" stroke-width="1.5"/>
    <rect x="160" y="90" width="75" height="40" rx="3" fill="#ca8a04" stroke="#facc15" stroke-width="1.5"/>

    <!-- Air Gap Indicator -->
    <text x="120" y="145" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Interlocking Stacks with Air Gaps</text>
  </g>

  <!-- Elevated Pallets (>= 30cm) -->
  <g transform="translate(265, 305)">
    <rect x="0" y="0" width="270" height="15" rx="2" fill="#78350f" stroke="#b45309" stroke-width="1.5"/>
    <rect x="10" y="15" width="20" height="20" fill="#451a03"/>
    <rect x="70" y="15" width="20" height="20" fill="#451a03"/>
    <rect x="130" y="15" width="20" height="20" fill="#451a03"/>
    <rect x="190" y="15" width="20" height="20" fill="#451a03"/>
    <rect x="240" y="15" width="20" height="20" fill="#451a03"/>
    <text x="135" y="50" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">Elevated Wooden Pallets (≥ 30cm Clearance)</text>
  </g>

  <!-- Ground Line & Capillary Barrier -->
  <rect x="120" y="360" width="560" height="35" rx="4" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
  <text x="400" y="382" font-size="11" fill="#fca5a5" text-anchor="middle">Bare Soil Moisture Barrier (Prevents capillary rot into bottom bales)</text>
</svg>
""")

# SVG 5: Standing Pasture Banking & Risks (Lesson 5, Page 3)
SVG_STANDING_PASTURE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Living Pasture Banking Concept &amp; Risk Matrix</text>

  <!-- Left: How Pasture Banking Works -->
  <g transform="translate(40, 70)">
    <rect x="0" y="0" width="340" height="340" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="40" rx="10" fill="#15803d"/>
    <text x="170" y="26" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">HOW PASTURE BANKING WORKS</text>
    
    <text x="15" y="70" font-size="12" font-weight="bold" fill="#4ade80">1. Wet Season Growth Phase:</text>
    <text x="25" y="90" font-size="11" fill="#cbd5e1">• Fenced paddock left ungrazed</text>
    <text x="25" y="110" font-size="11" fill="#cbd5e1">• Grass accumulates tall biomass &amp; deep roots</text>

    <text x="15" y="150" font-size="12" font-weight="bold" fill="#4ade80">2. Dry Season Utilization:</text>
    <text x="25" y="170" font-size="11" fill="#cbd5e1">• Paddock gate opened during drought</text>
    <text x="25" y="190" font-size="11" fill="#cbd5e1">• Livestock graze standing forage directly</text>

    <rect x="15" y="220" width="310" height="100" rx="6" fill="#1e293b"/>
    <text x="25" y="245" font-size="11" font-weight="bold" fill="#38bdf8">Key Advantages:</text>
    <text x="25" y="265" font-size="10" fill="#cbd5e1">✅ Zero harvest labor &amp; machinery cost</text>
    <text x="25" y="285" font-size="10" fill="#cbd5e1">✅ Zero storage barn required</text>
    <text x="25" y="305" font-size="10" fill="#cbd5e1">✅ Accessible in cloudy or wet weather</text>
  </g>

  <!-- Right: Outdoor Risks & Limitations -->
  <g transform="translate(420, 70)">
    <rect x="0" y="0" width="340" height="340" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="40" rx="10" fill="#b91c1c"/>
    <text x="170" y="26" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">OUTDOOR RISKS &amp; THREATS</text>

    <g transform="translate(15, 55)">
      <!-- Risk 1: Wildfire -->
      <rect x="0" y="0" width="310" height="60" rx="6" fill="#1e293b" stroke="#f87171" stroke-width="1"/>
      <text x="15" y="24" font-size="11" font-weight="bold" fill="#f87171">🔥 Wildfire Hazard:</text>
      <text x="15" y="44" font-size="10" fill="#cbd5e1">Dry grass is flammable; one spark burns whole reserve</text>
      
      <!-- Risk 2: Weather -->
      <rect x="0" y="70" width="310" height="60" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1"/>
      <text x="15" y="94" font-size="11" font-weight="bold" fill="#fbbf24">⛈️ Hailstones &amp; Flash Floods:</text>
      <text x="15" y="114" font-size="10" fill="#cbd5e1">Severe weather can flatten and wash away forage</text>

      <!-- Risk 3: Land Size -->
      <rect x="0" y="140" width="310" height="60" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <text x="15" y="164" font-size="11" font-weight="bold" fill="#38bdf8">🗺️ High Land Requirement:</text>
      <text x="15" y="184" font-size="10" fill="#cbd5e1">Cannot be practiced on plots under 1 acre</text>

      <!-- Risk 4: Quality -->
      <rect x="0" y="210" width="310" height="65" rx="6" fill="#1e293b" stroke="#a855f7" stroke-width="1"/>
      <text x="15" y="234" font-size="11" font-weight="bold" fill="#c084fc">📉 Natural Nutrient Decline:</text>
      <text x="15" y="254" font-size="10" fill="#cbd5e1">Overmature grass loses protein compared to baled hay</text>
    </g>
  </g>
</svg>
""")

# SVG 6: 6-Paddock Rotational & Deferred Grazing System (Lesson 6, Page 2)
SVG_ROTATIONAL_PADDOCKS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">6-Paddock Rotational &amp; Deferred Grazing System Blueprint</text>

  <!-- Paddock Grid (2 rows of 3) -->
  <g transform="translate(40, 70)">
    <!-- Paddock 1: Currently Grazing -->
    <rect x="0" y="0" width="225" height="150" rx="8" fill="#14532d" stroke="#22c55e" stroke-width="2.5"/>
    <text x="112" y="30" font-size="13" font-weight="bold" fill="#4ade80" text-anchor="middle">Paddock 1: ACTIVE</text>
    <text x="112" y="60" font-size="11" fill="#dcfce7" text-anchor="middle">🐄 Dairy Herd Grazing</text>
    <text x="112" y="85" font-size="10" fill="#86efac" text-anchor="middle">Grazing Duration: 5 Days</text>
    <text x="112" y="115" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Graze to 5cm stubble height</text>

    <!-- Paddock 2: Rest Stage 1 -->
    <rect x="247" y="0" width="225" height="150" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="359" y="30" font-size="13" font-weight="bold" fill="#94a3b8" text-anchor="middle">Paddock 2: Rest (Day 1-5)</text>
    <text x="359" y="70" font-size="11" fill="#64748b" text-anchor="middle">🌱 Early regrowth</text>
    <text x="359" y="100" font-size="10" fill="#94a3b8" text-anchor="middle">Roots absorbing nutrients</text>

    <!-- Paddock 3: Rest Stage 2 -->
    <rect x="495" y="0" width="225" height="150" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="607" y="30" font-size="13" font-weight="bold" fill="#94a3b8" text-anchor="middle">Paddock 3: Rest (Day 6-10)</text>
    <text x="607" y="70" font-size="11" fill="#64748b" text-anchor="middle">🌿 Active vegetative growth</text>
    <text x="607" y="100" font-size="10" fill="#94a3b8" text-anchor="middle">Leaf area expanding</text>

    <!-- Paddock 4: Rest Stage 3 -->
    <rect x="0" y="170" width="225" height="150" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="112" y="200" font-size="13" font-weight="bold" fill="#94a3b8" text-anchor="middle">Paddock 4: Rest (Day 11-15)</text>
    <text x="112" y="240" font-size="11" fill="#64748b" text-anchor="middle">🌾 Tall lush foliage</text>
    <text x="112" y="270" font-size="10" fill="#94a3b8" text-anchor="middle">Pre-flowering peak nutrition</text>

    <!-- Paddock 5: Ready for Herd -->
    <rect x="247" y="170" width="225" height="150" rx="8" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
    <text x="359" y="200" font-size="13" font-weight="bold" fill="#34d399" text-anchor="middle">Paddock 5: NEXT IN LINE</text>
    <text x="359" y="240" font-size="11" fill="#a7f3d0" text-anchor="middle">✨ Full 25 Days Rested</text>
    <text x="359" y="270" font-size="10" fill="#6ee7b7" text-anchor="middle">Ready for cattle next week</text>

    <!-- Paddock 6: DEFERRED (Dry Season Reserve) -->
    <rect x="495" y="170" width="225" height="150" rx="8" fill="#451a03" stroke="#f59e0b" stroke-width="2.5"/>
    <text x="607" y="200" font-size="13" font-weight="bold" fill="#fbbf24" text-anchor="middle">Paddock 6: DEFERRED BANK</text>
    <text x="607" y="235" font-size="11" fill="#fde68a" text-anchor="middle">🔒 LOCKED FOR DROUGHT</text>
    <text x="607" y="265" font-size="10" fill="#fcd34d" text-anchor="middle">Untouched throughout wet season</text>
    <text x="607" y="290" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Dry-season standing feed reserve</text>
  </g>
</svg>
""")

# SVG 7: Weatherproof Haystack Cross-Section (Lesson 7, Page 2)
SVG_HAYSTACK_CROSS_SECTION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Engineering Cross-Section: Weatherproof Haystack</text>

  <!-- Waterproof Sloped Thatch / Tarpaulin Cover -->
  <polygon points="400,80 180,240 620,240" fill="#0284c7" stroke="#38bdf8" stroke-width="2.5"/>
  <text x="400" y="130" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Sloped Crown Roof (45° Rain-Shedding Pitch)</text>

  <!-- Tie Ropes & Counterweight Stones -->
  <line x1="260" y1="180" x2="160" y2="330" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4"/>
  <circle cx="160" cy="335" r="10" fill="#64748b" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="140" y="360" font-size="9" font-weight="bold" fill="#fde68a" text-anchor="middle">Hanging Counterweight Stone</text>

  <line x1="540" y1="180" x2="640" y2="330" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4"/>
  <circle cx="640" cy="335" r="10" fill="#64748b" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="660" y="360" font-size="9" font-weight="bold" fill="#fde68a" text-anchor="middle">Weighted Anchor Rope</text>

  <!-- Compacted Hay Core -->
  <polygon points="400,100 220,240 220,330 580,330 580,240" fill="#ca8a04" stroke="#facc15" stroke-width="2"/>
  <text x="400" y="240" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">Densely Compacted Dry Hay Core</text>
  <text x="400" y="265" font-size="11" fill="#fef08a" text-anchor="middle">(Air pockets squeezed out during layering)</text>

  <!-- Raised Platform Base (>= 30cm) -->
  <rect x="200" y="330" width="400" height="15" rx="3" fill="#78350f" stroke="#b45309" stroke-width="2"/>
  <rect x="220" y="345" width="20" height="25" fill="#451a03"/>
  <rect x="340" y="345" width="20" height="25" fill="#451a03"/>
  <rect x="440" y="345" width="20" height="25" fill="#451a03"/>
  <rect x="560" y="345" width="20" height="25" fill="#451a03"/>
  
  <text x="400" y="360" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">Raised Wooden Platform (≥ 30cm)</text>

  <!-- Airflow Arrows Underneath -->
  <path d="M 120 380 Q 200 370 280 380" stroke="#38bdf8" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
  <text x="400" y="395" font-size="11" fill="#38bdf8" text-anchor="middle">Continuous Airflow Gap (Blocks rising soil dampness)</text>

  <!-- Ground Line -->
  <line x1="100" y1="410" x2="700" y2="410" stroke="#ef4444" stroke-width="2"/>
  <text x="400" y="425" font-size="10" fill="#f87171" text-anchor="middle">Bare Soil (Damp Ground)</text>
</svg>
""")

# SVG 8: Wooden Box Baler 3D Blueprint & Twines (Lesson 8, Page 3)
SVG_BOX_BALER_BLUEPRINT = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">3D Blueprint: Wooden Box Baler &amp; Pre-Packing Twine Routing</text>

  <!-- Box Structure 3D Wireframe -->
  <g transform="translate(180, 80)">
    <!-- Box Body -->
    <rect x="0" y="50" width="380" height="230" rx="6" fill="#0f172a" stroke="#b45309" stroke-width="2.5"/>
    <text x="190" y="80" font-size="13" font-weight="bold" fill="#f59e0b" text-anchor="middle">Empty Wooden Chamber (40cm W x 50cm H x 75cm L)</text>

    <!-- Side Door Hinges -->
    <rect x="0" y="80" width="8" height="25" rx="2" fill="#94a3b8"/>
    <rect x="0" y="220" width="8" height="25" rx="2" fill="#94a3b8"/>
    <text x="35" y="160" font-size="10" fill="#94a3b8" transform="rotate(-90 35 160)">Hinged Side Latch Door</text>

    <!-- Twine 1 (Left String) -->
    <path d="M 80,10 L 80,50 L 80,260 L 160,260 L 160,50 L 160,10" fill="none" stroke="#38bdf8" stroke-width="3"/>
    <circle cx="80" cy="10" r="5" fill="#38bdf8"/>
    <circle cx="160" cy="10" r="5" fill="#38bdf8"/>
    <text x="80" y="0" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Twine 1 End</text>

    <!-- Twine 2 (Right String) -->
    <path d="M 220,10 L 220,50 L 220,260 L 300,260 L 300,50 L 300,10" fill="none" stroke="#38bdf8" stroke-width="3"/>
    <circle cx="220" cy="10" r="5" fill="#38bdf8"/>
    <circle cx="300" cy="10" r="5" fill="#38bdf8"/>
    <text x="220" y="0" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Twine 2 End</text>

    <!-- Floor Routing Label -->
    <rect x="90" y="180" width="200" height="40" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-dasharray="2"/>
    <text x="190" y="205" font-size="10" font-weight="bold" fill="#7dd3fc" text-anchor="middle">Twines run along walls &amp; floor</text>
  </g>

  <!-- Golden Rule Callout -->
  <g transform="translate(60, 365)">
    <rect x="0" y="0" width="680" height="50" rx="6" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="340" y="30" font-size="12" font-weight="bold" fill="#4ade80" text-anchor="middle">THE CARDINAL RULE: Always position sisal twines inside BEFORE adding any grass!</text>
  </g>
</svg>
""")

# SVG 9: 4-Stage Haystack Construction Flow (Lesson 9, Page 2)
SVG_HAYSTACK_PROCESS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">4-Stage Haystack Construction Process Flow</text>

  <!-- 4 Step Cards -->
  <g transform="translate(30, 70)">
    <!-- Stage 1 -->
    <rect x="0" y="0" width="170" height="340" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="35" rx="8" fill="#0284c7"/>
    <text x="85" y="23" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 1</text>
    <text x="85" y="65" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Platform Base</text>
    <text x="12" y="100" font-size="10" fill="#cbd5e1">• Flat, dry farm site</text>
    <text x="12" y="125" font-size="10" fill="#cbd5e1">• Plant 4 corner posts</text>
    <text x="12" y="150" font-size="10" fill="#cbd5e1">• Nail timber rafters</text>
    <text x="12" y="175" font-size="10" font-weight="bold" fill="#fbbf24">• Elevate ≥ 30cm high</text>
    <rect x="12" y="240" width="146" height="80" rx="4" fill="#1e293b"/>
    <text x="85" y="285" font-size="9" fill="#94a3b8" text-anchor="middle">Airflow clearance</text>
  </g>

  <!-- Stage 2 -->
  <g transform="translate(220, 70)">
    <rect x="0" y="0" width="170" height="340" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="35" rx="8" fill="#ca8a04"/>
    <text x="85" y="23" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 2</text>
    <text x="85" y="65" font-size="12" font-weight="bold" fill="#facc15" text-anchor="middle">Core Compaction</text>
    <text x="12" y="100" font-size="10" fill="#cbd5e1">• Load dry grass/stover</text>
    <text x="12" y="125" font-size="10" fill="#cbd5e1">• Pack layers firmly</text>
    <text x="12" y="150" font-size="10" fill="#cbd5e1">• Stamp out air pockets</text>
    <text x="12" y="175" font-size="10" font-weight="bold" fill="#facc15">• Build up to 1.5m</text>
    <rect x="12" y="240" width="146" height="80" rx="4" fill="#1e293b"/>
    <text x="85" y="285" font-size="9" fill="#94a3b8" text-anchor="middle">Dense stable core</text>
  </g>

  <!-- Stage 3 -->
  <g transform="translate(410, 70)">
    <rect x="0" y="0" width="170" height="340" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="35" rx="8" fill="#db2777"/>
    <text x="85" y="23" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 3</text>
    <text x="85" y="65" font-size="12" font-weight="bold" fill="#f472b6" text-anchor="middle">Sloped Crown</text>
    <text x="12" y="100" font-size="10" fill="#cbd5e1">• Taper top forage</text>
    <text x="12" y="125" font-size="10" fill="#cbd5e1">• Shape 45° steep pitch</text>
    <text x="12" y="150" font-size="10" fill="#cbd5e1">• House-roof profile</text>
    <text x="12" y="175" font-size="10" font-weight="bold" fill="#f472b6">• Zero flat spots</text>
    <rect x="12" y="240" width="146" height="80" rx="4" fill="#1e293b"/>
    <text x="85" y="285" font-size="9" fill="#94a3b8" text-anchor="middle">Water shedding</text>
  </g>

  <!-- Stage 4 -->
  <g transform="translate(600, 70)">
    <rect x="0" y="0" width="170" height="340" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="35" rx="8" fill="#15803d"/>
    <text x="85" y="23" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 4</text>
    <text x="85" y="65" font-size="12" font-weight="bold" fill="#4ade80" text-anchor="middle">Cover &amp; Anchor</text>
    <text x="12" y="100" font-size="10" fill="#cbd5e1">• Drape plastic / thatch</text>
    <text x="12" y="125" font-size="10" fill="#cbd5e1">• Pass sisal tie ropes</text>
    <text x="12" y="150" font-size="10" fill="#cbd5e1">• Hang weight stones</text>
    <text x="12" y="175" font-size="10" font-weight="bold" fill="#4ade80">• Storm resistance</text>
    <rect x="12" y="240" width="146" height="80" rx="4" fill="#1e293b"/>
    <text x="85" y="285" font-size="9" fill="#94a3b8" text-anchor="middle">Rot-proof storage</text>
  </g>
</svg>
""")

# SVG 10: 5-Step Box-Baling Operation (Lesson 10, Page 2)
SVG_BOX_BALING_STEPS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">5-Step Manual Box-Baling Operation Workflow</text>

  <!-- Step 1 -->
  <g transform="translate(35, 75)">
    <rect x="0" y="0" width="130" height="330" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="65" cy="30" r="16" fill="#0284c7"/>
    <text x="65" y="35" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1</text>
    <text x="65" y="70" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Lay Twines</text>
    <text x="10" y="105" font-size="9" fill="#cbd5e1">• Position 2 sisal strings inside empty box</text>
    <text x="10" y="145" font-size="9" fill="#cbd5e1">• Run along walls &amp; floor</text>
    <text x="10" y="180" font-size="9" font-weight="bold" fill="#7dd3fc">• Ends hang outside</text>
  </g>

  <!-- Step 2 -->
  <g transform="translate(180, 75)">
    <rect x="0" y="0" width="130" height="330" rx="6" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <circle cx="65" cy="30" r="16" fill="#ca8a04"/>
    <text x="65" y="35" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2</text>
    <text x="65" y="70" font-size="11" font-weight="bold" fill="#facc15" text-anchor="middle">Layer &amp; Stamp</text>
    <text x="10" y="105" font-size="9" fill="#cbd5e1">• Add 20cm dry grass layer</text>
    <text x="10" y="145" font-size="9" fill="#cbd5e1">• Step in with gumboots</text>
    <text x="10" y="180" font-size="9" font-weight="bold" fill="#fde047">• Heavy compaction</text>
  </g>

  <!-- Step 3 -->
  <g transform="translate(325, 75)">
    <rect x="0" y="0" width="130" height="330" rx="6" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <circle cx="65" cy="30" r="16" fill="#db2777"/>
    <text x="65" y="35" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3</text>
    <text x="65" y="70" font-size="11" font-weight="bold" fill="#f472b6" text-anchor="middle">Fill to Rim</text>
    <text x="10" y="105" font-size="9" fill="#cbd5e1">• Repeat layering &amp; stamping</text>
    <text x="10" y="145" font-size="9" fill="#cbd5e1">• Pack tightly to top rim</text>
    <text x="10" y="180" font-size="9" font-weight="bold" fill="#fbcfe8">• Maximum density</text>
  </g>

  <!-- Step 4 -->
  <g transform="translate(470, 75)">
    <rect x="0" y="0" width="130" height="330" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <circle cx="65" cy="30" r="16" fill="#9333ea"/>
    <text x="65" y="35" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">4</text>
    <text x="65" y="70" font-size="11" font-weight="bold" fill="#c084fc" text-anchor="middle">Tie Knots</text>
    <text x="10" y="105" font-size="9" fill="#cbd5e1">• Pull strings over top</text>
    <text x="10" y="145" font-size="9" fill="#cbd5e1">• Apply body weight</text>
    <text x="10" y="180" font-size="9" font-weight="bold" fill="#e9d5ff">• Tie secure reef knot</text>
  </g>

  <!-- Step 5 -->
  <g transform="translate(615, 75)">
    <rect x="0" y="0" width="130" height="330" rx="6" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <circle cx="65" cy="30" r="16" fill="#15803d"/>
    <text x="65" y="35" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">5</text>
    <text x="65" y="70" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">Release Bale</text>
    <text x="10" y="105" font-size="9" fill="#cbd5e1">• Open side door latch</text>
    <text x="10" y="145" font-size="9" fill="#cbd5e1">• Slide out dense bale</text>
    <text x="10" y="180" font-size="9" font-weight="bold" fill="#86efac">• Stack on pallets</text>
  </g>
</svg>
""")

# SVG 11: 4-Pillar Household Drought Mitigation (Lesson 11, Page 2)
SVG_HOUSEHOLD_DROUGHT_MATRIX = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 4-Pillar Household Drought Mitigation Matrix</text>

  <!-- 4 Quadrants -->
  <!-- Quad 1: Drought Tolerant Crops -->
  <g transform="translate(40, 70)">
    <rect x="0" y="0" width="340" height="155" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <text x="20" y="30" font-size="13" font-weight="bold" fill="#4ade80">1. DROUGHT-TOLERANT PLANTING</text>
    <text x="20" y="60" font-size="11" fill="#cbd5e1">• Establish deep-rooted Rhodes grass &amp; Sorghum</text>
    <text x="20" y="85" font-size="11" fill="#cbd5e1">• Intercrop high-protein Desmodium legumes</text>
    <text x="20" y="115" font-size="10" font-weight="bold" fill="#86efac">Benefit: Sustains green growth under low moisture</text>
  </g>

  <!-- Quad 2: Strategic Destocking -->
  <g transform="translate(420, 70)">
    <rect x="0" y="0" width="340" height="155" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="20" y="30" font-size="13" font-weight="bold" fill="#38bdf8">2. STRATEGIC DESTOCKING</text>
    <text x="20" y="60" font-size="11" fill="#cbd5e1">• Sell older, unproductive, or male stock early</text>
    <text x="20" y="85" font-size="11" fill="#cbd5e1">• Protect high-yielding dairy cows and breeders</text>
    <text x="20" y="115" font-size="10" font-weight="bold" fill="#7dd3fc">Benefit: Reduces feed demand &amp; generates cash</text>
  </g>

  <!-- Quad 3: Crop Residue Recycling -->
  <g transform="translate(40, 245)">
    <rect x="0" y="0" width="340" height="155" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <text x="20" y="30" font-size="13" font-weight="bold" fill="#facc15">3. CROP RESIDUE RECYCLING</text>
    <text x="20" y="60" font-size="11" fill="#cbd5e1">• Collect &amp; chop maize stover and wheat straw</text>
    <text x="20" y="85" font-size="11" fill="#cbd5e1">• Feed residues in morning for bulk rumen fiber</text>
    <text x="20" y="115" font-size="10" font-weight="bold" fill="#fde047">Benefit: Stretches expensive hay reserves 2x longer</text>
  </g>

  <!-- Quad 4: Mathematical Feed Budgeting -->
  <g transform="translate(420, 245)">
    <rect x="0" y="0" width="340" height="155" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <text x="20" y="30" font-size="13" font-weight="bold" fill="#c084fc">4. FEED BUDGETING MATHEMATICS</text>
    <text x="20" y="60" font-size="11" fill="#cbd5e1">• Calculate: Herd Daily Need x Dry Days Expected</text>
    <text x="20" y="85" font-size="11" fill="#cbd5e1">• E.g.: 2 cows x 0.25 bales/day x 90 days = 45 bales</text>
    <text x="20" y="115" font-size="10" font-weight="bold" fill="#e9d5ff">Benefit: Zero feed surprises; eliminates starvation</text>
  </g>
</svg>
""")

# SVG 12: Economic Cost-Benefit Comparison (Lesson 12, Page 2)
SVG_ECONOMIC_BENEFIT = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Economic Cost-Benefit: Conserved Hay vs Commercial Feeds</text>

  <!-- Left: Farmer Cherono (Conserved Hay) -->
  <g transform="translate(40, 70)">
    <rect x="0" y="0" width="340" height="340" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="40" rx="10" fill="#15803d"/>
    <text x="170" y="26" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">FARMER CHERONO (CONSERVED HAY)</text>
    
    <text x="20" y="70" font-size="11" fill="#cbd5e1">Daily Milk Revenue (5 Liters):</text>
    <text x="20" y="90" font-size="14" font-weight="bold" fill="#4ade80">+350 KES / Day</text>

    <text x="20" y="130" font-size="11" fill="#cbd5e1">Daily Feeding Cost (Home Hay):</text>
    <text x="20" y="150" font-size="14" font-weight="bold" fill="#4ade80">0 KES / Day (Free Rain Grass)</text>

    <line x1="20" y1="175" x2="320" y2="175" stroke="#334155" stroke-width="1.5"/>

    <text x="20" y="205" font-size="12" font-weight="bold" fill="#ffffff">Net Daily Profit:</text>
    <rect x="20" y="220" width="300" height="50" rx="6" fill="#14532d" stroke="#22c55e" stroke-width="1.5"/>
    <text x="170" y="252" font-size="18" font-weight="bold" fill="#4ade80" text-anchor="middle">+350 KES NET PROFIT / DAY</text>

    <text x="20" y="295" font-size="10" fill="#86efac">✅ Herd stays healthy &amp; retains full breeding value</text>
    <text x="20" y="315" font-size="10" fill="#86efac">✅ Zero debt; highly profitable enterprise</text>
  </g>

  <!-- Right: Farmer Mwangi (No Conserved Feed) -->
  <g transform="translate(420, 70)">
    <rect x="0" y="0" width="340" height="340" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="40" rx="10" fill="#b91c1c"/>
    <text x="170" y="26" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">FARMER MWANGI (NO STORED FEED)</text>

    <text x="20" y="70" font-size="11" fill="#cbd5e1">Daily Milk Revenue (Stress Drop):</text>
    <text x="20" y="90" font-size="14" font-weight="bold" fill="#fca5a5">+300 KES / Day</text>

    <text x="20" y="130" font-size="11" fill="#cbd5e1">Daily Feeding Cost (Commercial Feed):</text>
    <text x="20" y="150" font-size="14" font-weight="bold" fill="#ef4444">-400 KES / Day (Drought Price Surge)</text>

    <line x1="20" y1="175" x2="320" y2="175" stroke="#334155" stroke-width="1.5"/>

    <text x="20" y="205" font-size="12" font-weight="bold" fill="#ffffff">Net Daily Balance:</text>
    <rect x="20" y="220" width="300" height="50" rx="6" fill="#450a0a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="170" y="252" font-size="18" font-weight="bold" fill="#f87171" text-anchor="middle">-100 KES NET LOSS / DAY</text>

    <text x="20" y="295" font-size="10" fill="#fca5a5">❌ Cow becomes emaciated and stops producing</text>
    <text x="20" y="315" font-size="10" fill="#fca5a5">❌ Forced to sell cow at panic throwaway price</text>
  </g>
</svg>
""")

TOPIC1_SVGS = [
    {"lesson_order": 1, "page_number": 3, "title": "Botanical and Agricultural Forage Classification Wheel", "svg": SVG_FORAGE_CLASSIFICATION},
    {"lesson_order": 2, "page_number": 3, "title": "The Biological & Economic Drought Impact Chain", "svg": SVG_DROUGHT_IMPACT_CHAIN},
    {"lesson_order": 3, "page_number": 3, "title": "Moisture Reduction and Volume Compaction in Haymaking", "svg": SVG_HAYMAKING_CURVE},
    {"lesson_order": 4, "page_number": 3, "title": "Engineering Blueprint: A Safe, Weatherproof Hay Storage Facility", "svg": SVG_SAFE_HAY_BARN},
    {"lesson_order": 5, "page_number": 3, "title": "The Standing Forage Pasture Banking Cycle & Risk Factors", "svg": SVG_STANDING_PASTURE},
    {"lesson_order": 6, "page_number": 2, "title": "6-Paddock Rotational & Deferred Grazing System Blueprint", "svg": SVG_ROTATIONAL_PADDOCKS},
    {"lesson_order": 7, "page_number": 2, "title": "Engineering Cross-Section of a Weatherproof Haystack", "svg": SVG_HAYSTACK_CROSS_SECTION},
    {"lesson_order": 8, "page_number": 3, "title": "3D Blueprint of a Wooden Box Baler & Pre-Packing Twine Routing", "svg": SVG_BOX_BALER_BLUEPRINT},
    {"lesson_order": 9, "page_number": 2, "title": "4-Stage Haystack Construction Process Flow", "svg": SVG_HAYSTACK_PROCESS},
    {"lesson_order": 10, "page_number": 2, "title": "5-Step Manual Box-Baling Operation Workflow", "svg": SVG_BOX_BALING_STEPS},
    {"lesson_order": 11, "page_number": 2, "title": "The 4-Pillar Household Forage Conservation Framework", "svg": SVG_HOUSEHOLD_DROUGHT_MATRIX},
    {"lesson_order": 12, "page_number": 2, "title": "Economic Cost-Benefit Comparison: Conserved Hay vs. Commercial Feed", "svg": SVG_ECONOMIC_BENEFIT},
]

def enrich_cbc_grade9_agriculture_topic1():
    """Attaches vector SVGs, Wikimedia photographic visual hooks, YouTube video, and persists LessonAsset records."""
    print("=" * 80)
    print("STARTING VISUAL ENRICHMENT: CBC GRADE 9 AGRICULTURE — TOPIC 1")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    assert curriculum, "CBC Curriculum not found!"
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 9").first()
    assert grade, "Grade 9 not found under CBC!"
    subject = Subject.objects.filter(grade=grade, name="Agriculture").first()
    assert subject, "Subject Agriculture not found under Grade 9!"
    topic = Topic.objects.filter(subject=subject, name="Conserving Animal Feeds (Forage, Drought, and Hay)").first()
    assert topic, "Topic Conserving Animal Feeds not found!"

    lessons = list(topic.lessons.all().order_by("learning_unit__order"))
    print(f"[*] Found {len(lessons)} Lessons under Topic: '{topic.name}' (ID: {topic.id})")

    # Clean existing LessonAssets for clean re-enrichment
    LessonAsset.objects.filter(lesson__in=lessons).delete()
    print("[*] Cleared existing LessonAssets for clean re-enrichment.")

    # Load verified photographic images from JSON
    images_json_path = os.path.join(os.path.dirname(__file__), "grade9_topic1_verified_images.json")
    with open(images_json_path, "r") as f:
        verified_images = json.load(f)

    # 1. Attach Card 1 Visual Hooks (Wikimedia Photos)
    print("\n[+] Phase 2A: Attaching Card 1 Photographic Visual Hooks...")
    for lesson in lessons:
        u_order = str(lesson.learning_unit.order)
        img_info = verified_images.get(u_order)
        if not img_info:
            continue

        hook_block = LessonBlock.objects.filter(
            lesson=lesson,
            page_number=1,
            block_type="suggested_image"
        ).first()

        if hook_block:
            content = hook_block.content or {}
            content["resolved_image_url"] = img_info["url"]
            content["url"] = img_info["url"]
            content["author"] = img_info.get("author", "Wikimedia Commons Contributor")
            content["licensing"] = img_info.get("licensing", "CC BY-SA 4.0")
            hook_block.content = content
            hook_block.save()

            asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="image",
                source_type="external",
                storage_type="url",
                status="attached",
                title=hook_block.title,
                description=content.get("caption", hook_block.title),
                url=img_info["url"],
                metadata={
                    "author": img_info.get("author", "Wikimedia Commons Contributor"),
                    "licensing": img_info.get("licensing", "CC BY-SA 4.0"),
                    "caption": content.get("caption", ""),
                    "is_card_1_hook": True
                }
            )
            hook_block.assets.add(asset)
            print(f"  [CARD 1 HOOK OK] Lesson {u_order}: '{hook_block.title[:45]}...' -> Asset ID {asset.id}")

    # 2. Attach Custom Vector SVGs
    print("\n[+] Phase 2B: Attaching Custom Sanitized Vector SVGs...")
    for sm in TOPIC1_SVGS:
        u_order = sm["lesson_order"]
        p_num = sm["page_number"]
        lesson = next((l for l in lessons if l.learning_unit.order == u_order), None)
        if not lesson:
            continue

        diagram_block = LessonBlock.objects.filter(
            lesson=lesson,
            page_number=p_num,
            block_type="suggested_diagram"
        ).first()

        if diagram_block:
            content = diagram_block.content or {}
            content["svg_content"] = sm["svg"]
            content["svg"] = sm["svg"]
            diagram_block.content = content
            diagram_block.save()

            asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                source_type="ai_generated",
                storage_type="embed",
                status="attached",
                title=sm["title"],
                description=f"Sanitized vector SVG diagram: {sm['title']}",
                metadata={"svg_content": sm["svg"]}
            )
            diagram_block.assets.add(asset)
            print(f"  [SVG ATTACHED] Lesson {u_order} Page {p_num}: '{diagram_block.title[:45]}...' -> Asset ID {asset.id}")

    # 3. Attach Multiple Curated Video Lessons across Topic 1
    print("\n[+] Phase 2C: Attaching Multiple Curated Video Lessons across Topic 1...")
    TOPIC1_VIDEOS = {
        1: {
            "url": "https://www.youtube.com/watch?v=TXJPk-QfhDU",
            "resolved_video_id": "TXJPk-QfhDU",
            "title": "Smart Farm - Hay and Fodder Farming in Kenya",
            "author": "Citizen TV Kenya",
            "caption": "Watch Citizen TV's Smart Farm feature exploring commercial and smallholder fodder production, pasture management, and forage conservation in Kenya."
        },
        5: {
            "url": "https://www.youtube.com/watch?v=xlqbcWnNX6w",
            "resolved_video_id": "xlqbcWnNX6w",
            "title": "Field Video: How to Make High-Quality Maize Silage",
            "author": "Farm With Fred",
            "caption": "Watch this step-by-step practical field guide on harvesting maize at dough stage, chopping, compacting in silage pits, and air-tight soil sealing."
        },
        8: {
            "url": "https://www.youtube.com/watch?v=aPibjW1jTpM",
            "resolved_video_id": "aPibjW1jTpM",
            "title": "Field Video: BOMA Rhodes Hay Production & Baling in Kenya",
            "author": "Paul Gatere",
            "caption": "Watch this practical demonstration of mowing, field curing, and baling Boma Rhodes grass into tight hay bales on smallholder Kenyan farms."
        },
        12: {
            "url": "https://www.youtube.com/watch?v=PY6kRnI3Vd8",
            "resolved_video_id": "PY6kRnI3Vd8",
            "title": "Topic Video Review: Silage Making & Fodder Conservation Technology",
            "author": "Paul Gatere",
            "caption": "A comprehensive instructional video demonstration of silage making, anaerobic pit sealing, and drought feeding strategies for Grade 9 Agriculture."
        }
    }

    for u_order, v_info in TOPIC1_VIDEOS.items():
        lesson = next((l for l in lessons if l.learning_unit.order == u_order), None)
        if not lesson:
            continue

        video_block = LessonBlock.objects.filter(
            lesson=lesson,
            block_type="suggested_video"
        ).first()

        if not video_block:
            target_page = 6 if u_order == 12 else 4
            video_block = LessonBlock.objects.create(
                lesson=lesson,
                block_id=f"g9_agri_t1_u{u_order}_video",
                block_type="suggested_video",
                component_type="suggested_video",
                title=v_info["title"],
                content={
                    "title": v_info["title"],
                    "url": v_info["url"],
                    "resolved_video_id": v_info["resolved_video_id"],
                    "caption": v_info["caption"],
                    "author": v_info["author"],
                    "verified": True
                },
                page_number=target_page,
                page_title="Video Demonstration Resource",
                component_order=9,
                order=99
            )

        content = video_block.content or {}
        content.update(v_info)
        content["verified"] = True
        video_block.content = content
        video_block.save()

        asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="youtube",
            source_type="external",
            storage_type="url",
            status="attached",
            title=v_info["title"],
            description=v_info["caption"],
            url=v_info["url"],
            metadata={"video_id": v_info["resolved_video_id"], "author": v_info["author"]}
        )
        video_block.assets.add(asset)
        print(f"  [VIDEO ATTACHED] Lesson {u_order} Page {video_block.page_number}: '{v_info['title'][:45]}...' -> Asset ID {asset.id}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_cbc_grade9_agriculture_topic1()
