"""
VLearn CBC Grade 10 Agriculture — Topic 2: Properties of Soil
Visual Enrichment Engine (Phase 2: Vector SVGs, Verified Photos & Asset Persistence)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Properties of Soil (Order: 2)

Attaches:
  - 12 First-Card Photographic Visual Hooks (100% Tested HTTP 200 OK Direct Wikimedia URLs)
  - 10 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - 2 Verified Educational YouTube Videos (Lesson 10 Card 3 & Lesson 12 Card 3)
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade10_agriculture_topic2.py
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
# 10 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 2: PROPERTIES OF SOIL
# =============================================================================

# SVG 1: Simplified USDA Soil Textural Triangle (Lesson 1, Page 4)
SVG_TEXTURAL_TRIANGLE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">USDA Soil Textural Triangle and Primary Textural Classes</text>

  <!-- Main Triangle Geometry -->
  <polygon points="400,80 180,360 620,360" fill="#0f172a" stroke="#64748b" stroke-width="3"/>

  <!-- Triangle Apex: Clay -->
  <circle cx="400" cy="80" r="18" fill="#ef4444"/>
  <text x="400" y="85" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">CLAY</text>
  <text x="400" y="60" font-size="12" font-weight="bold" fill="#f87171" text-anchor="middle">100% Clay (&lt;0.002 mm)</text>

  <!-- Bottom Left: Sand -->
  <circle cx="180" cy="360" r="18" fill="#eab308"/>
  <text x="180" y="365" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">SAND</text>
  <text x="180" y="395" font-size="12" font-weight="bold" fill="#fde047" text-anchor="middle">100% Sand (0.05–2.0 mm)</text>

  <!-- Bottom Right: Silt -->
  <circle cx="620" cy="360" r="18" fill="#06b6d4"/>
  <text x="620" y="365" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">SILT</text>
  <text x="620" y="395" font-size="12" font-weight="bold" fill="#67e8f9" text-anchor="middle">100% Silt (0.002–0.05 mm)</text>

  <!-- Internal Zones -->
  <!-- Heavy Clay Zone (Top) -->
  <polygon points="400,105 320,200 480,200" fill="#7f1d1d" opacity="0.7" stroke="#ef4444" stroke-width="1.5"/>
  <text x="400" y="160" font-size="12" font-weight="bold" fill="#fca5a5" text-anchor="middle">CLAYEY SOILS</text>
  <text x="400" y="178" font-size="10" fill="#fecaca" text-anchor="middle">&gt;40% Clay | High Water &amp; Nutrient Retention</text>

  <!-- Loam Zone (Center - Optimal) -->
  <polygon points="330,230 470,230 440,310 360,310" fill="#14532d" opacity="0.9" stroke="#22c55e" stroke-width="2"/>
  <text x="400" y="265" font-size="14" font-weight="bold" fill="#4ade80" text-anchor="middle">LOAM SOILS (OPTIMAL)</text>
  <text x="400" y="285" font-size="10" font-weight="bold" fill="#86efac" text-anchor="middle">40% Sand | 40% Silt | 20% Clay</text>

  <!-- Sandy Loam Zone (Left) -->
  <polygon points="210,350 310,215 350,310 240,350" fill="#713f12" opacity="0.6" stroke="#eab308" stroke-width="1.5"/>
  <text x="270" y="300" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">SANDY LOAM</text>
  <text x="270" y="315" font-size="9" fill="#fef08a" text-anchor="middle">High Aeration &amp; Drainage</text>

  <!-- Silt Loam Zone (Right) -->
  <polygon points="590,350 490,215 450,310 560,350" fill="#164e63" opacity="0.6" stroke="#06b6d4" stroke-width="1.5"/>
  <text x="530" y="300" font-size="11" font-weight="bold" fill="#67e8f9" text-anchor="middle">SILT LOAM</text>
  <text x="530" y="315" font-size="9" fill="#cffafe" text-anchor="middle">Silky / High Moisture</text>

  <!-- Info Callout Box -->
  <g transform="translate(40, 75)">
    <rect x="0" y="0" width="130" height="90" rx="8" fill="#0f172a" stroke="#334155"/>
    <text x="65" y="22" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Particle Sizes</text>
    <text x="10" y="42" font-size="9" fill="#cbd5e1">• Sand: 0.05–2.0 mm</text>
    <text x="10" y="60" font-size="9" fill="#cbd5e1">• Silt: 0.002–0.05 mm</text>
    <text x="10" y="78" font-size="9" fill="#cbd5e1">• Clay: &lt;0.002 mm</text>
  </g>
</svg>
""")

# SVG 2: Types of Soil Structure (Lesson 2, Page 3)
SVG_SOIL_STRUCTURE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Primary Types of Soil Structure Aggregates (Peds)</text>

  <!-- 1. Crumbly (Ideal) -->
  <g transform="translate(35, 65)">
    <rect x="0" y="0" width="230" height="165" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="230" height="32" rx="10" fill="#15803d"/>
    <text x="115" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. CRUMBLY (OPTIMAL)</text>
    <text x="12" y="55" font-size="11" font-weight="bold" fill="#86efac">• Shape: Small rounded, porous</text>
    <text x="12" y="75" font-size="10" fill="#cbd5e1">• Porosity: Highest internal voids</text>
    <text x="12" y="95" font-size="10" fill="#cbd5e1">• Root Growth: Deep and unhindered</text>
    <text x="12" y="115" font-size="10" fill="#cbd5e1">• Water: Excellent infiltration</text>
    <rect x="10" y="130" width="210" height="24" rx="4" fill="#14532d"/>
    <text x="115" y="146" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Best for All Crop Roots</text>
  </g>

  <!-- 2. Granular -->
  <g transform="translate(285, 65)">
    <rect x="0" y="0" width="230" height="165" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="32" rx="10" fill="#0369a1"/>
    <text x="115" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. GRANULAR</text>
    <text x="12" y="55" font-size="11" font-weight="bold" fill="#7dd3fc">• Shape: Small rounded, dense</text>
    <text x="12" y="75" font-size="10" fill="#cbd5e1">• Porosity: Good topsoil aeration</text>
    <text x="12" y="95" font-size="10" fill="#cbd5e1">• Occurrence: Cultivated topsoils</text>
    <text x="12" y="115" font-size="10" fill="#cbd5e1">• Water: Rapid infiltration</text>
    <rect x="10" y="130" width="210" height="24" rx="4" fill="#0c4a6e"/>
    <text x="115" y="146" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Common Garden Topsoil</text>
  </g>

  <!-- 3. Blocky -->
  <g transform="translate(535, 65)">
    <rect x="0" y="0" width="230" height="165" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="32" rx="10" fill="#b45309"/>
    <text x="115" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. BLOCKY</text>
    <text x="12" y="55" font-size="11" font-weight="bold" fill="#fde047">• Shape: Angular / subangular cubes</text>
    <text x="12" y="75" font-size="10" fill="#cbd5e1">• Size: 1.5 to 5.0 cm peds</text>
    <text x="12" y="95" font-size="10" fill="#cbd5e1">• Occurrence: Heavy B subsoils</text>
    <text x="12" y="115" font-size="10" fill="#cbd5e1">• Water: Drains along ped cracks</text>
    <rect x="10" y="130" width="210" height="24" rx="4" fill="#78350f"/>
    <text x="115" y="146" font-size="10" font-weight="bold" fill="#fcd34d" text-anchor="middle">Typical Subsoil Aggregate</text>
  </g>

  <!-- 4. Platy (Compacted) -->
  <g transform="translate(35, 250)">
    <rect x="0" y="0" width="230" height="165" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="230" height="32" rx="10" fill="#991b1b"/>
    <text x="115" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">4. PLATY (COMPACTED)</text>
    <text x="12" y="55" font-size="11" font-weight="bold" fill="#fca5a5">• Shape: Thin horizontal plates</text>
    <text x="12" y="75" font-size="10" fill="#cbd5e1">• Hazard: Plow pans &amp; crusts</text>
    <text x="12" y="95" font-size="10" fill="#cbd5e1">• Drainage: Severely blocked</text>
    <text x="12" y="115" font-size="10" fill="#cbd5e1">• Roots: Deflected horizontally</text>
    <rect x="10" y="130" width="210" height="24" rx="4" fill="#7f1d1d"/>
    <text x="115" y="146" font-size="10" font-weight="bold" fill="#ef4444" text-anchor="middle">Highly Undesirable (Pan)</text>
  </g>

  <!-- 5. Prismatic -->
  <g transform="translate(285, 250)">
    <rect x="0" y="0" width="230" height="165" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="32" rx="10" fill="#7e22ce"/>
    <text x="115" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">5. PRISMATIC</text>
    <text x="12" y="55" font-size="11" font-weight="bold" fill="#c084fc">• Shape: Tall vertical columns</text>
    <text x="12" y="75" font-size="10" fill="#cbd5e1">• Top: Flat, angular edges</text>
    <text x="12" y="95" font-size="10" fill="#cbd5e1">• Occurrence: Lower subsoils</text>
    <text x="12" y="115" font-size="10" fill="#cbd5e1">• Water: Vertical crack flow</text>
    <rect x="10" y="130" width="210" height="24" rx="4" fill="#581c87"/>
    <text x="115" y="146" font-size="10" font-weight="bold" fill="#c084fc" text-anchor="middle">Dense Lower Subsoil</text>
  </g>

  <!-- 6. Columnar -->
  <g transform="translate(535, 250)">
    <rect x="0" y="0" width="230" height="165" rx="10" fill="#0f172a" stroke="#e11d48" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="32" rx="10" fill="#9f1239"/>
    <text x="115" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">6. COLUMNAR</text>
    <text x="12" y="55" font-size="11" font-weight="bold" fill="#fda4af">• Shape: Vertical pillars</text>
    <text x="12" y="75" font-size="10" fill="#cbd5e1">• Top: Rounded, salt-capped</text>
    <text x="12" y="95" font-size="10" fill="#cbd5e1">• Occurrence: Saline-sodic soils</text>
    <text x="12" y="115" font-size="10" fill="#cbd5e1">• Hazard: Sodium dispersion</text>
    <rect x="10" y="130" width="210" height="24" rx="4" fill="#881337"/>
    <text x="115" y="146" font-size="10" font-weight="bold" fill="#f43f5e" text-anchor="middle">Sodic Soil Indicator</text>
  </g>
</svg>
""")

# SVG 3: Porosity and Bulk Density (Lesson 3, Page 4)
SVG_POROSITY_DENSITY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Soil Porosity &amp; Bulk Density: Loose vs Compacted State</text>

  <!-- Left: Loose Crumb Soil -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="335" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="335" height="35" rx="10" fill="#15803d"/>
    <text x="167" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">LOOSE, WELL-STRUCTURED SOIL</text>

    <!-- 50:50 Graphic Box -->
    <rect x="25" y="55" width="285" height="110" rx="6" fill="#1e293b" stroke="#334155"/>
    <rect x="25" y="55" width="142" height="110" fill="#15803d" opacity="0.8"/>
    <rect x="167" y="55" width="143" height="55" fill="#0284c7" opacity="0.8"/>
    <rect x="167" y="110" width="143" height="55" fill="#38bdf8" opacity="0.4"/>
    
    <text x="96" y="115" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">50% SOLID</text>
    <text x="96" y="130" font-size="9" fill="#dcfce7" text-anchor="middle">(45% Mineral + 5% SOM)</text>
    
    <text x="238" y="88" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">25% AIR (Macro)</text>
    <text x="238" y="142" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">25% WATER (Micro)</text>

    <g transform="translate(20, 185)">
      <text x="0" y="20" font-size="12" font-weight="bold" fill="#86efac">Bulk Density (Db): 1.10 – 1.30 g/cm³</text>
      <text x="0" y="42" font-size="11" fill="#cbd5e1">• Total Porosity: 50% to 58%</text>
      <text x="0" y="64" font-size="11" fill="#cbd5e1">• Abundant large macro-pores for oxygen</text>
      <text x="0" y="86" font-size="11" fill="#cbd5e1">• Deep, unhindered root expansion</text>
      <text x="0" y="108" font-size="11" fill="#cbd5e1">• Infiltration: Rapid (Zero surface runoff)</text>
    </g>

    <rect x="20" y="305" width="295" height="26" rx="4" fill="#14532d"/>
    <text x="167" y="322" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Optimal Health &amp; Crop Yields</text>
  </g>

  <!-- Right: Compacted Soil -->
  <g transform="translate(420, 65)">
    <rect x="0" y="0" width="335" height="345" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="335" height="35" rx="10" fill="#991b1b"/>
    <text x="167" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">COMPACTED SOIL (PLOW PAN)</text>

    <!-- Compacted Graphic Box -->
    <rect x="25" y="55" width="285" height="110" rx="6" fill="#1e293b" stroke="#334155"/>
    <rect x="25" y="55" width="200" height="110" fill="#991b1b" opacity="0.8"/>
    <rect x="225" y="55" width="85" height="35" fill="#0284c7" opacity="0.5"/>
    <rect x="225" y="90" width="85" height="75" fill="#38bdf8" opacity="0.4"/>
    
    <text x="125" y="115" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">70% SOLID MATTER</text>
    <text x="125" y="130" font-size="9" fill="#fecaca" text-anchor="middle">(Crushed Matrix)</text>
    
    <text x="267" y="78" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">5% AIR</text>
    <text x="267" y="132" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">25% WATER</text>

    <g transform="translate(20, 185)">
      <text x="0" y="20" font-size="12" font-weight="bold" fill="#fca5a5">Bulk Density (Db): 1.65 – 1.80 g/cm³</text>
      <text x="0" y="42" font-size="11" fill="#cbd5e1">• Total Porosity: Drops below 35%</text>
      <text x="0" y="64" font-size="11" fill="#cbd5e1">• Macro-pores crushed; oxygen starved</text>
      <text x="0" y="86" font-size="11" fill="#cbd5e1">• Roots physically stunted &amp; deflected</text>
      <text x="0" y="108" font-size="11" fill="#cbd5e1">• Infiltration: Sealed (Severe erosion runoff)</text>
    </g>

    <rect x="20" y="305" width="295" height="26" rx="4" fill="#7f1d1d"/>
    <text x="167" y="322" font-size="10" font-weight="bold" fill="#ef4444" text-anchor="middle">Critical Root Growth Restriction</text>
  </g>
</svg>
""")

# SVG 4: Soil Color Diagnostic Matrix (Lesson 4, Page 3)
SVG_SOIL_COLOR = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Soil Color Diagnostic Matrix &amp; Agricultural Indicators</text>

  <!-- Color 1: Dark Brown / Black -->
  <g transform="translate(35, 65)">
    <rect x="0" y="0" width="355" height="160" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="355" height="32" rx="10" fill="#15803d"/>
    <text x="177" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">DARK BROWN / JET BLACK</text>
    <text x="15" y="55" font-size="11" font-weight="bold" fill="#86efac">Agent: High Organic Matter (Humus)</text>
    <text x="15" y="75" font-size="10" fill="#cbd5e1">• Rich in decomposed plant residues and active microbes</text>
    <text x="15" y="95" font-size="10" fill="#cbd5e1">• High water-holding capacity &amp; massive CEC battery</text>
    <text x="15" y="115" font-size="10" fill="#cbd5e1">• Drainage: Excellent, highly aerated crumb topsoil</text>
    <rect x="15" y="125" width="325" height="24" rx="4" fill="#1e293b"/>
    <text x="177" y="141" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Prime Agricultural Topsoil (All Crops)</text>
  </g>

  <!-- Color 2: Bright Red / Orange -->
  <g transform="translate(410, 65)">
    <rect x="0" y="0" width="355" height="160" rx="10" fill="#0f172a" stroke="#f97316" stroke-width="2"/>
    <rect x="0" y="0" width="355" height="32" rx="10" fill="#c2410c"/>
    <text x="177" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">BRIGHT RED / DEEP ORANGE</text>
    <text x="15" y="55" font-size="11" font-weight="bold" fill="#fdba74">Agent: Oxidized Ferric Iron (Fe³⁺, Hematite)</text>
    <text x="15" y="75" font-size="10" fill="#cbd5e1">• Indicates continuous, excellent aeration and deep drainage</text>
    <text x="15" y="95" font-size="10" fill="#cbd5e1">• Unrestricted oxygen flow; zero waterlogging</text>
    <text x="15" y="115" font-size="10" fill="#cbd5e1">• Typical of volcanic highland soils (Kericho, Kiambu)</text>
    <rect x="15" y="125" width="325" height="24" rx="4" fill="#1e293b"/>
    <text x="177" y="141" font-size="10" font-weight="bold" fill="#fb923c" text-anchor="middle">Ideal for Deep Perennials (Tea, Coffee, Trees)</text>
  </g>

  <!-- Color 3: Dull Grey / Pale Blue (Gleying) -->
  <g transform="translate(35, 245)">
    <rect x="0" y="0" width="355" height="170" rx="10" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
    <rect x="0" y="0" width="355" height="32" rx="10" fill="#0e7490"/>
    <text x="177" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">DULL GREY / BLUISH (GLEYED)</text>
    <text x="15" y="55" font-size="11" font-weight="bold" fill="#67e8f9">Agent: Reduced Ferrous Iron (Fe²⁺, Anaerobic)</text>
    <text x="15" y="75" font-size="10" fill="#cbd5e1">• Chronic waterlogging; oxygen completely stripped</text>
    <text x="15" y="95" font-size="10" fill="#cbd5e1">• Toxic anaerobic root rots for upland crops</text>
    <text x="15" y="115" font-size="10" fill="#cbd5e1">• Found in low valley bottoms, swamps, and rice basins</text>
    <rect x="15" y="132" width="325" height="26" rx="4" fill="#1e293b"/>
    <text x="177" y="149" font-size="10" font-weight="bold" fill="#06b6d4" text-anchor="middle">Suited for Aquaculture &amp; Paddy Rice</text>
  </g>

  <!-- Color 4: Mottled (Grey with Red/Orange Spots) -->
  <g transform="translate(410, 245)">
    <rect x="0" y="0" width="355" height="170" rx="10" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect x="0" y="0" width="355" height="32" rx="10" fill="#854d0e"/>
    <text x="177" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">MOTTLED (SPOTTED RED / GREY)</text>
    <text x="15" y="55" font-size="11" font-weight="bold" fill="#fde047">Agent: Fluctuating Seasonal Water Table</text>
    <text x="15" y="75" font-size="10" fill="#cbd5e1">• Alternates between aerated (dry season) and flooded (wet season)</text>
    <text x="15" y="95" font-size="10" fill="#cbd5e1">• Warns farmer of seasonal root drownings</text>
    <text x="15" y="115" font-size="10" fill="#cbd5e1">• Requires raised planting beds and drainage furrows</text>
    <rect x="15" y="132" width="325" height="26" rx="4" fill="#1e293b"/>
    <text x="177" y="149" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">Requires Surface Drainage Intervention</text>
  </g>
</svg>
""")

# SVG 5: Step-by-Step Zigzag Soil Sampling Protocol (Lesson 5, Page 3)
SVG_SOIL_SAMPLING = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Field Soil Sampling Protocol: The 5-Step Zigzag Workflow</text>

  <!-- Step 1 -->
  <g transform="translate(35, 70)">
    <rect x="0" y="0" width="135" height="340" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="135" height="32" rx="8" fill="#0284c7"/>
    <text x="67" y="21" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STEP 1: FIELD WALK</text>
    <text x="10" y="55" font-size="10" font-weight="bold" fill="#38bdf8">• Walk Zigzag Path</text>
    <text x="10" y="75" font-size="9" fill="#cbd5e1">• Traverse across field uniformly</text>
    <text x="10" y="105" font-size="10" font-weight="bold" fill="#f87171">Avoid Anomalies:</text>
    <text x="10" y="122" font-size="9" fill="#cbd5e1">• Manure heaps</text>
    <text x="10" y="138" font-size="9" fill="#cbd5e1">• Charcoal ash</text>
    <text x="10" y="154" font-size="9" fill="#cbd5e1">• Fence lines</text>
    <text x="10" y="170" font-size="9" fill="#cbd5e1">• Big tree shade</text>
  </g>

  <!-- Step 2 -->
  <g transform="translate(185, 70)">
    <rect x="0" y="0" width="135" height="340" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="135" height="32" rx="8" fill="#0284c7"/>
    <text x="67" y="21" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STEP 2: CLEAR LITTER</text>
    <text x="10" y="55" font-size="10" font-weight="bold" fill="#38bdf8">• Scrape Surface</text>
    <text x="10" y="75" font-size="9" fill="#cbd5e1">• Brush away dry grass &amp; undecomposed mulch</text>
    <text x="10" y="115" font-size="10" font-weight="bold" fill="#fde047">Rule:</text>
    <text x="10" y="135" font-size="9" fill="#cbd5e1">Do not scrape away topsoil mineral layer</text>
  </g>

  <!-- Step 3 -->
  <g transform="translate(335, 70)">
    <rect x="0" y="0" width="135" height="340" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="135" height="32" rx="8" fill="#15803d"/>
    <text x="67" y="21" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STEP 3: V-HOLE SLICE</text>
    <text x="10" y="55" font-size="10" font-weight="bold" fill="#86efac">• Dig V-Hole 20cm</text>
    <text x="10" y="75" font-size="9" fill="#cbd5e1">• Cut 1.5 cm slice from flat side</text>
    <text x="10" y="105" font-size="10" font-weight="bold" fill="#86efac">• Trim Edges</text>
    <text x="10" y="125" font-size="9" fill="#cbd5e1">• Leave 2 cm center strip core</text>
    <text x="10" y="155" font-size="9" fill="#cbd5e1">• Collect 15–20 cores</text>
  </g>

  <!-- Step 4 -->
  <g transform="translate(485, 70)">
    <rect x="0" y="0" width="135" height="340" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="135" height="32" rx="8" fill="#0284c7"/>
    <text x="67" y="21" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STEP 4: COMPOSITE</text>
    <text x="10" y="55" font-size="10" font-weight="bold" fill="#38bdf8">• Clean Plastic Bucket</text>
    <text x="10" y="75" font-size="9" fill="#cbd5e1">• Thoroughly mix all 15–20 cores</text>
    <text x="10" y="110" font-size="10" font-weight="bold" fill="#38bdf8">• Extract 500g</text>
    <text x="10" y="130" font-size="9" fill="#cbd5e1">• Air-dry in shade</text>
    <text x="10" y="150" font-size="9" fill="#cbd5e1">(Never heat dry!)</text>
  </g>

  <!-- Step 5 -->
  <g transform="translate(635, 70)">
    <rect x="0" y="0" width="130" height="340" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="130" height="32" rx="8" fill="#0284c7"/>
    <text x="65" y="21" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STEP 5: DISPATCH</text>
    <text x="10" y="55" font-size="10" font-weight="bold" fill="#38bdf8">• Label Sample Bag</text>
    <text x="10" y="75" font-size="9" fill="#cbd5e1">• Farmer name</text>
    <text x="10" y="92" font-size="9" fill="#cbd5e1">• Field Block ID</text>
    <text x="10" y="109" font-size="9" fill="#cbd5e1">• Target crop</text>
    <text x="10" y="135" font-size="10" font-weight="bold" fill="#4ade80">• Ship to Lab</text>
    <text x="10" y="152" font-size="9" fill="#cbd5e1">For N, P, K, pH, CEC</text>
  </g>
</svg>
""")

# SVG 6: Soil pH and Nutrient Availability Scale (Lesson 6, Page 3)
SVG_SOIL_PH_SCALE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Soil pH Scale and Plant Nutrient Availability Bands</text>

  <!-- pH Axis Header -->
  <g transform="translate(50, 65)">
    <rect x="0" y="0" width="200" height="28" fill="#991b1b" rx="4"/>
    <text x="100" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STRONGLY ACIDIC (pH 4.0 - 5.5)</text>

    <rect x="210" y="0" width="280" height="28" fill="#15803d" rx="4"/>
    <text x="350" y="18" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">OPTIMAL ZONE (pH 6.0 - 7.0)</text>

    <rect x="500" y="0" width="200" height="28" fill="#0e7490" rx="4"/>
    <text x="600" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">ALKALINE (pH 7.5 - 9.0)</text>
  </g>

  <!-- Nutrient Band 1: Nitrogen -->
  <g transform="translate(50, 110)">
    <rect x="0" y="0" width="100" height="30" fill="#0f172a"/>
    <text x="0" y="20" font-size="12" font-weight="bold" fill="#ffffff">Nitrogen (N)</text>
    <path d="M 110 20 Q 210 15 350 5 Q 490 15 700 20" fill="none" stroke="#22c55e" stroke-width="8"/>
  </g>

  <!-- Nutrient Band 2: Phosphorus (Locked in Acid!) -->
  <g transform="translate(50, 155)">
    <rect x="0" y="0" width="100" height="30" fill="#0f172a"/>
    <text x="0" y="20" font-size="12" font-weight="bold" fill="#f87171">Phosphorus (P)</text>
    <path d="M 110 28 Q 200 26 350 5 Q 490 20 700 28" fill="none" stroke="#ef4444" stroke-width="10"/>
    <text x="150" y="12" font-size="9" fill="#fca5a5">Locked by Al/Fe</text>
    <text x="610" y="12" font-size="9" fill="#fca5a5">Locked by Ca</text>
  </g>

  <!-- Nutrient Band 3: Potassium -->
  <g transform="translate(50, 200)">
    <rect x="0" y="0" width="100" height="30" fill="#0f172a"/>
    <text x="0" y="20" font-size="12" font-weight="bold" fill="#ffffff">Potassium (K)</text>
    <path d="M 110 22 Q 210 16 350 6 Q 490 16 700 22" fill="none" stroke="#38bdf8" stroke-width="7"/>
  </g>

  <!-- Nutrient Band 4: Calcium & Magnesium -->
  <g transform="translate(50, 245)">
    <rect x="0" y="0" width="100" height="30" fill="#0f172a"/>
    <text x="0" y="20" font-size="12" font-weight="bold" fill="#ffffff">Ca &amp; Mg</text>
    <path d="M 110 25 Q 210 18 350 6 Q 490 12 700 8" fill="none" stroke="#a855f7" stroke-width="8"/>
  </g>

  <!-- Nutrient Band 5: Micronutrients (Fe, Zn, Mn) -->
  <g transform="translate(50, 290)">
    <rect x="0" y="0" width="100" height="30" fill="#0f172a"/>
    <text x="0" y="20" font-size="12" font-weight="bold" fill="#fde047">Fe, Zn, Mn</text>
    <path d="M 110 6 Q 210 8 350 15 Q 490 24 700 28" fill="none" stroke="#eab308" stroke-width="8"/>
    <text x="620" y="15" font-size="9" fill="#fef08a">Deficiency Lockup</text>
  </g>

  <!-- Remediation Footer -->
  <g transform="translate(50, 350)">
    <rect x="0" y="0" width="345" height="65" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="172" y="22" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">ACID REMEDY: AGRICULTURAL LIME (CaCO3)</text>
    <text x="172" y="45" font-size="10" fill="#cbd5e1" text-anchor="middle">Neutralizes H+ ions, raises pH, unlocks Phosphorus</text>

    <rect x="355" y="0" width="345" height="65" rx="6" fill="#1e293b" stroke="#06b6d4"/>
    <text x="527" y="22" font-size="11" font-weight="bold" fill="#67e8f9" text-anchor="middle">ALKALINE REMEDY: ELEMENTAL SULFUR / COMPOST</text>
    <text x="527" y="45" font-size="10" fill="#cbd5e1" text-anchor="middle">Acidifies soil, unlocks micronutrients (Fe, Zn)</text>
  </g>
</svg>
""")

# SVG 7: Cation Exchange Capacity (Lesson 7, Page 3)
SVG_CEC_MODEL = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Cation Exchange Capacity (CEC) &amp; Soil Colloid Chemistry</text>

  <!-- Colloid 1: Negatively Charged Clay / Humus Particle -->
  <g transform="translate(50, 75)">
    <rect x="0" y="0" width="280" height="260" rx="14" fill="#0284c7" stroke="#38bdf8" stroke-width="3"/>
    <text x="140" y="45" font-size="15" font-weight="bold" fill="#ffffff" text-anchor="middle">SOIL COLLOID</text>
    <text x="140" y="65" font-size="12" fill="#e0f2fe" text-anchor="middle">(Clay Mineral / Humus)</text>
    <text x="140" y="130" font-size="45" font-weight="bold" fill="#ffffff" opacity="0.3" text-anchor="middle">- - - - -</text>
    <text x="140" y="180" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">PERMANENT NEGATIVE</text>
    <text x="140" y="200" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">SURFACE CHARGE (-)</text>
    <text x="140" y="235" font-size="11" fill="#e0f2fe" text-anchor="middle">Humus CEC: 100–300 cmol/kg</text>
  </g>

  <!-- Adsorbed Cations Surrounding Colloid -->
  <g transform="translate(340, 80)">
    <!-- Ca2+ -->
    <rect x="10" y="10" width="80" height="40" rx="8" fill="#15803d" stroke="#4ade80" stroke-width="1.5"/>
    <text x="50" y="35" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">Ca²⁺</text>

    <!-- Mg2+ -->
    <rect x="10" y="65" width="80" height="40" rx="8" fill="#15803d" stroke="#4ade80" stroke-width="1.5"/>
    <text x="50" y="90" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">Mg²⁺</text>

    <!-- K+ -->
    <rect x="10" y="120" width="80" height="40" rx="8" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="50" y="145" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">K⁺</text>

    <!-- NH4+ -->
    <rect x="10" y="175" width="80" height="40" rx="8" fill="#7e22ce" stroke="#c084fc" stroke-width="1.5"/>
    <text x="50" y="200" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">NH₄⁺</text>
  </g>

  <!-- Plant Root Hair Exchanging H+ -->
  <g transform="translate(460, 75)">
    <rect x="0" y="0" width="280" height="260" rx="14" fill="#15803d" stroke="#22c55e" stroke-width="3"/>
    <text x="140" y="45" font-size="15" font-weight="bold" fill="#ffffff" text-anchor="middle">PLANT ROOT HAIR</text>
    <text x="140" y="75" font-size="11" fill="#dcfce7" text-anchor="middle">Secretes H⁺ ions into solution</text>
    
    <rect x="40" y="100" width="200" height="50" rx="8" fill="#1e293b"/>
    <text x="140" y="122" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">Cation Exchange Reaction:</text>
    <text x="140" y="138" font-size="10" fill="#cbd5e1" text-anchor="middle">2 H⁺ exchanged for 1 Ca²⁺ / K⁺</text>

    <text x="140" y="190" font-size="11" fill="#dcfce7" text-anchor="middle">• Absorbs nutrient cations</text>
    <text x="140" y="210" font-size="11" fill="#dcfce7" text-anchor="middle">• Powered by root respiration</text>
  </g>

  <!-- Explanation Banner -->
  <g transform="translate(50, 360)">
    <rect x="0" y="0" width="700" height="60" rx="8" fill="#0f172a" stroke="#64748b"/>
    <text x="350" y="25" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Electrostatic Retention: Negative charges prevent rainfall from leaching cations into groundwater</text>
    <text x="350" y="45" font-size="11" fill="#cbd5e1" text-anchor="middle">Low-CEC Sandy Soils: Lack negative charges $\rightarrow$ Require frequent 'spoon-fed' fertilizer doses</text>
  </g>
</svg>
""")

# SVG 8: Osmotic Root Flow Model: Normal vs Saline (Lesson 8, Page 4)
SVG_SALINITY_OSMOSIS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Soil Salinity: Osmotic Water Uptake vs Physiological Drought</text>

  <!-- Left: Normal Soil -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="335" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="335" height="35" rx="10" fill="#15803d"/>
    <text x="167" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">NORMAL SOIL (LOW SALINITY)</text>

    <g transform="translate(20, 55)">
      <rect x="0" y="0" width="130" height="110" rx="8" fill="#1e293b" stroke="#334155"/>
      <text x="65" y="25" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">SOIL WATER</text>
      <text x="65" y="55" font-size="10" fill="#cbd5e1">Low Salt Conc.</text>
      <text x="65" y="75" font-size="10" fill="#cbd5e1">(High Water Pot.)</text>
      
      <line x1="140" y1="55" x2="165" y2="55" stroke="#22c55e" stroke-width="4"/>
      <polygon points="165,50 175,55 165,60" fill="#22c55e"/>

      <rect x="175" y="0" width="120" height="110" rx="8" fill="#14532d" stroke="#22c55e"/>
      <text x="235" y="25" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">ROOT CELLS</text>
      <text x="235" y="55" font-size="10" fill="#dcfce7">High Solute Conc.</text>
      <text x="235" y="75" font-size="10" fill="#dcfce7">(Low Water Pot.)</text>
    </g>

    <g transform="translate(20, 185)">
      <text x="0" y="20" font-size="12" font-weight="bold" fill="#86efac">Osmosis Mechanism: NORMAL INFLOW</text>
      <text x="0" y="42" font-size="11" fill="#cbd5e1">• Water flows naturally from soil into roots</text>
      <text x="0" y="64" font-size="11" fill="#cbd5e1">• Cells stay turgid; transpiration active</text>
      <text x="0" y="86" font-size="11" fill="#cbd5e1">• Full nutrient transport to leaves</text>
    </g>

    <rect x="20" y="300" width="295" height="28" rx="4" fill="#14532d"/>
    <text x="167" y="318" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">Vibrant Growth &amp; High Yields</text>
  </g>

  <!-- Right: Saline Soil -->
  <g transform="translate(420, 65)">
    <rect x="0" y="0" width="335" height="345" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="335" height="35" rx="10" fill="#991b1b"/>
    <text x="167" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">SALINE SOIL (PHYSIOLOGICAL DROUGHT)</text>

    <g transform="translate(20, 55)">
      <rect x="0" y="0" width="130" height="110" rx="8" fill="#7f1d1d" stroke="#ef4444"/>
      <text x="65" y="25" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">SOIL WATER</text>
      <text x="65" y="55" font-size="10" fill="#fca5a5">Extreme Salt Conc.</text>
      <text x="65" y="75" font-size="10" fill="#fca5a5">(High Osmotic Pull)</text>
      
      <line x1="165" y1="55" x2="140" y2="55" stroke="#ef4444" stroke-width="4"/>
      <polygon points="140,50 130,55 140,60" fill="#ef4444"/>

      <rect x="175" y="0" width="120" height="110" rx="8" fill="#1e293b" stroke="#334155"/>
      <text x="235" y="25" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">ROOT CELLS</text>
      <text x="235" y="55" font-size="10" fill="#cbd5e1">Lower Solutes</text>
      <text x="235" y="75" font-size="10" fill="#cbd5e1">(Water Pulled Out)</text>
    </g>

    <g transform="translate(20, 185)">
      <text x="0" y="20" font-size="12" font-weight="bold" fill="#fca5a5">Osmosis Mechanism: REVERSED GRADIENT</text>
      <text x="0" y="42" font-size="11" fill="#cbd5e1">• Soil water chemically holds moisture tightly</text>
      <text x="0" y="64" font-size="11" fill="#cbd5e1">• Plant wilts and dehydrates in wet soil!</text>
      <text x="0" y="86" font-size="11" fill="#cbd5e1">• Toxic Na⁺/Cl⁻ burns leaf tips</text>
    </g>

    <rect x="20" y="300" width="295" height="28" rx="4" fill="#7f1d1d"/>
    <text x="167" y="318" font-size="11" font-weight="bold" fill="#ef4444" text-anchor="middle">Physiological Drought &amp; Crop Death</text>
  </g>
</svg>
""")

# SVG 9: The Triple Benefits of Humus (Lesson 9, Page 3)
SVG_HUMUS_TRIPLE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Triple Agricultural Power of Soil Humus</text>

  <!-- Central Hub: Humus -->
  <circle cx="400" cy="225" r="55" fill="#78350f" stroke="#eab308" stroke-width="3"/>
  <text x="400" y="220" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">STABLE</text>
  <text x="400" y="240" font-size="14" font-weight="bold" fill="#fde047" text-anchor="middle">HUMUS</text>

  <!-- Pillar 1: Physical Benefits (Top Left) -->
  <g transform="translate(35, 70)">
    <rect x="0" y="0" width="230" height="150" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="230" height="32" rx="10" fill="#15803d"/>
    <text x="115" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. PHYSICAL (THE SPONGE)</text>
    <text x="12" y="55" font-size="11" font-weight="bold" fill="#86efac">• Water Holding Capacity:</text>
    <text x="12" y="75" font-size="10" fill="#cbd5e1">Holds 6x its dry weight in water</text>
    <text x="12" y="100" font-size="11" font-weight="bold" fill="#86efac">• Crumb Ped Aggregation:</text>
    <text x="12" y="120" font-size="10" fill="#cbd5e1">Glues loose sand &amp; dense clay</text>
  </g>
  <line x1="265" y1="145" x2="350" y2="195" stroke="#22c55e" stroke-width="2" stroke-dasharray="4,4"/>

  <!-- Pillar 2: Chemical Benefits (Top Right) -->
  <g transform="translate(535, 70)">
    <rect x="0" y="0" width="230" height="150" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="230" height="32" rx="10" fill="#0284c7"/>
    <text x="115" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. CHEMICAL (THE BATTERY)</text>
    <text x="12" y="55" font-size="11" font-weight="bold" fill="#7dd3fc">• Massive CEC Capacity:</text>
    <text x="12" y="75" font-size="10" fill="#cbd5e1">100–300 cmol/kg negative charge</text>
    <text x="12" y="100" font-size="11" font-weight="bold" fill="#7dd3fc">• Slow-Release Nutrients:</text>
    <text x="12" y="120" font-size="10" fill="#cbd5e1">Steady release of N, P, S minerals</text>
  </g>
  <line x1="535" y1="145" x2="450" y2="195" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4"/>

  <!-- Pillar 3: Biological Benefits (Bottom Center) -->
  <g transform="translate(250, 290)">
    <rect x="0" y="0" width="300" height="135" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <rect x="0" y="0" width="300" height="32" rx="10" fill="#7e22ce"/>
    <text x="150" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. BIOLOGICAL (THE FOOD WEB FUEL)</text>
    <text x="15" y="55" font-size="11" font-weight="bold" fill="#c084fc">• Sustains Soil Biodiversity:</text>
    <text x="15" y="75" font-size="10" fill="#cbd5e1">Feeds billions of bacteria, mycorrhizae &amp; earthworms</text>
    <text x="15" y="98" font-size="11" font-weight="bold" fill="#c084fc">• Disease Suppression:</text>
    <text x="15" y="118" font-size="10" fill="#cbd5e1">Bio-control of fungal wilts and parasitic nematodes</text>
  </g>
  <line x1="400" y1="280" x2="400" y2="290" stroke="#a855f7" stroke-width="2"/>
</svg>
""")

# SVG 10: Vertical Soil Profile Horizons (Lesson 11, Page 3)
SVG_SOIL_PROFILE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Stratigraphic Horizons of a Mature Soil Profile (O, A, E, B, C, R)</text>

  <!-- Stratigraphic Column Graphic -->
  <g transform="translate(60, 55)">
    <!-- O Horizon -->
    <rect x="0" y="0" width="180" height="35" fill="#451a03" stroke="#78350f" stroke-width="1.5"/>
    <text x="90" y="22" font-size="12" font-weight="bold" fill="#fde047" text-anchor="middle">O HORIZON</text>

    <!-- A Horizon -->
    <rect x="0" y="35" width="180" height="70" fill="#1e293b" stroke="#22c55e" stroke-width="2"/>
    <text x="90" y="75" font-size="13" font-weight="bold" fill="#4ade80" text-anchor="middle">A HORIZON (TOPSOIL)</text>

    <!-- E Horizon -->
    <rect x="0" y="105" width="180" height="40" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="90" y="130" font-size="11" font-weight="bold" fill="#e2e8f0" text-anchor="middle">E HORIZON (ELUVIATED)</text>

    <!-- B Horizon -->
    <rect x="0" y="145" width="180" height="95" fill="#9a3412" stroke="#ea580c" stroke-width="2"/>
    <text x="90" y="195" font-size="13" font-weight="bold" fill="#fed7aa" text-anchor="middle">B HORIZON (SUBSOIL)</text>

    <!-- C Horizon -->
    <rect x="0" y="240" width="180" height="65" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
    <text x="90" y="275" font-size="12" font-weight="bold" fill="#cbd5e1" text-anchor="middle">C HORIZON (PARENT)</text>

    <!-- R Horizon -->
    <rect x="0" y="305" width="180" height="55" fill="#0f172a" stroke="#475569" stroke-width="2"/>
    <text x="90" y="340" font-size="12" font-weight="bold" fill="#94a3b8" text-anchor="middle">R HORIZON (BEDROCK)</text>
  </g>

  <!-- Descriptive Callouts (Right Side) -->
  <g transform="translate(265, 55)">
    <!-- O Callout -->
    <rect x="0" y="0" width="480" height="35" rx="6" fill="#0f172a" stroke="#78350f"/>
    <text x="15" y="22" font-size="11" fill="#fde047"><tspan font-weight="bold">O Layer:</tspan> Organic surface litter (undecomposed leaves, straw, twigs).</text>

    <!-- A Callout -->
    <rect x="0" y="42" width="480" height="60" rx="6" fill="#0f172a" stroke="#22c55e"/>
    <text x="15" y="62" font-size="11" font-weight="bold" fill="#4ade80">A Horizon (Topsoil / Feeder Zone):</text>
    <text x="15" y="80" font-size="10" fill="#cbd5e1">Rich in dark humus, active earthworms, and N, P, K nutrients. Primary root zone.</text>

    <!-- E Callout -->
    <rect x="0" y="108" width="480" height="35" rx="6" fill="#0f172a" stroke="#94a3b8"/>
    <text x="15" y="130" font-size="10" fill="#e2e8f0"><tspan font-weight="bold">E Horizon:</tspan> Leached sand layer where minerals have been washed downward.</text>

    <!-- B Callout -->
    <rect x="0" y="149" width="480" height="85" rx="6" fill="#0f172a" stroke="#ea580c"/>
    <text x="15" y="169" font-size="11" font-weight="bold" fill="#fdba74">B Horizon (Subsoil / Illuvial Accumulation):</text>
    <text x="15" y="187" font-size="10" fill="#cbd5e1">Dense clay and iron accumulation. Deep root anchoring and water storage.</text>
    <text x="15" y="205" font-size="10" font-weight="bold" fill="#fde047">Nutrient Pump: Deep tree roots pull leached minerals back to topsoil.</text>

    <!-- C Callout -->
    <rect x="0" y="240" width="480" height="55" rx="6" fill="#0f172a" stroke="#64748b"/>
    <text x="15" y="260" font-size="11" font-weight="bold" fill="#cbd5e1">C Horizon (Parent Material):</text>
    <text x="15" y="278" font-size="10" fill="#94a3b8">Weathered, fractured rock fragments lacking organic matter or soil structures.</text>

    <!-- R Callout -->
    <rect x="0" y="302" width="480" height="55" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="15" y="322" font-size="11" font-weight="bold" fill="#94a3b8">R Horizon (Solid Bedrock):</text>
    <text x="15" y="340" font-size="10" fill="#cbd5e1">Unweathered granite/basalt rock base. Sets physical limit of rooting depth.</text>
  </g>
</svg>
""")

SVG_MAP = {
    1: {"page": 4, "svg": SVG_TEXTURAL_TRIANGLE, "title": "Simplified USDA Soil Textural Triangle"},
    2: {"page": 3, "svg": SVG_SOIL_STRUCTURE, "title": "Primary Types of Soil Structure Aggregates"},
    3: {"page": 4, "svg": SVG_POROSITY_DENSITY, "title": "Soil Porosity & Bulk Density: Loose vs Compacted State"},
    4: {"page": 3, "svg": SVG_SOIL_COLOR, "title": "Soil Color Diagnostic Matrix & Agricultural Indicators"},
    5: {"page": 3, "svg": SVG_SOIL_SAMPLING, "title": "Field Soil Sampling Protocol: The 5-Step Zigzag Workflow"},
    6: {"page": 3, "svg": SVG_SOIL_PH_SCALE, "title": "Soil pH Scale and Plant Nutrient Availability Bands"},
    7: {"page": 3, "svg": SVG_CEC_MODEL, "title": "Cation Exchange Capacity (CEC) & Soil Colloid Chemistry"},
    8: {"page": 4, "svg": SVG_SALINITY_OSMOSIS, "title": "Soil Salinity: Osmotic Water Uptake vs Physiological Drought"},
    9: {"page": 3, "svg": SVG_HUMUS_TRIPLE, "title": "The Triple Agricultural Power of Soil Humus"},
    11: {"page": 3, "svg": SVG_SOIL_PROFILE, "title": "Stratigraphic Horizons of a Mature Soil Profile (O, A, E, B, C, R)"}
}

def enrich_grade10_topic2():
    """Injects verified photos, responsive vector SVGs, YouTube embeds, and creates LessonAssets."""
    print("=" * 80)
    print("STARTING ENRICHMENT: CBC Grade 10 Agriculture — Topic 2: Properties of Soil")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()
    topic = Topic.objects.filter(subject=subject, name="Properties of Soil").first()

    assert topic, "Topic 'Properties of Soil' not found!"

    images_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grade10_topic2_verified_images.json")
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
                    "topic_order": 2,
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
                        "topic_order": 2,
                        "unit_order": u_order,
                        "page": svg_def["page"],
                        "svg_content": svg_def["svg"]
                    }
                )
                diag_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [Vector SVG Attached] Lesson {u_order}: {svg_def['title']}")

        # ---------------------------------------------------------------------
        # 3. Educational YouTube Videos (Lesson 10 & Lesson 12)
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
                        "topic_order": 2,
                        "unit_order": u_order,
                        "youtube_url": v_url
                    }
                )
                v_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [YouTube Video Attached] Lesson {u_order}: {v_block.title}")

    print("=" * 80)
    print(f"ENRICHMENT COMPLETE: Topic 2 '{topic.name}'")
    print(f"  Photographic Hooks: {total_images_attached} / 12")
    print(f"  Vector SVGs:        {total_svgs_attached} / 10")
    print(f"  YouTube Videos:     {total_videos_attached} / 2")
    print(f"  LessonAssets:       {total_assets_persisted}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic2()
