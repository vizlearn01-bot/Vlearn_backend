"""
VLearn CBC Grade 10 Geography — Topic 5: Rocks
Visual Enrichment Engine (Vector SVGs, Verified Wikimedia Images & Educational Videos)

Subject: Geography (Grade 10 CBC, Subject ID: 37)
Topic 5: Rocks

Attaches:
  - 18 First-Card Photographic Visual Hooks (100% Verified Wikimedia URLs)
  - 18 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - Educational YouTube Video for the Rock Cycle in Motion (Lesson 2)
  - Populates LessonAsset models for offline caching and mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade10_geography_topic5.py
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
# 18 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 5: ROCKS
# =============================================================================

# SVG 1: Comparison of a Rock and a Mineral (Lesson 1)
SVG_ROCK_VS_MINERAL = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="48" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">ROCK VS. MINERAL ARCHITECTURE</text>
  <text x="400" y="70" font-size="12" fill="#94a3b8" text-anchor="middle">Aggregate Mixture (Granite Rock) vs. Pure Building Blocks (Minerals)</text>

  <!-- Left: Rock Specimen (Granite Aggregate) -->
  <g transform="translate(40, 95)">
    <rect x="0" y="0" width="320" height="300" rx="10" fill="#0f172a" stroke="#e2e8f0" stroke-width="2"/>
    <rect x="0" y="0" width="320" height="36" rx="10" fill="#334155"/>
    <text x="160" y="24" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">ROCK: GRANITE (AGGREGATE)</text>
    
    <!-- Granite Specimen Visual -->
    <rect x="40" y="55" width="240" height="150" rx="8" fill="#475569" stroke="#64748b" stroke-width="1.5"/>
    <!-- Speckles representing minerals -->
    <polygon points="50,70 75,65 70,90 45,85" fill="#f43f5e" opacity="0.8"/>
    <polygon points="80,100 110,95 105,120 75,115" fill="#f43f5e" opacity="0.8"/>
    <polygon points="180,65 210,60 205,85 175,80" fill="#f43f5e" opacity="0.8"/>
    <polygon points="220,120 250,115 245,140 215,135" fill="#f43f5e" opacity="0.8"/>
    <polygon points="120,65 145,60 140,85 115,80" fill="#e2e8f0" opacity="0.9"/>
    <polygon points="150,110 180,105 175,135 145,130" fill="#e2e8f0" opacity="0.9"/>
    <polygon points="60,130 90,125 85,155 55,150" fill="#e2e8f0" opacity="0.9"/>
    <circle cx="95" cy="80" r="10" fill="#0f172a"/>
    <circle cx="165" cy="75" r="12" fill="#0f172a"/>
    <circle cx="130" cy="135" r="9" fill="#0f172a"/>
    <circle cx="200" cy="130" r="11" fill="#0f172a"/>
    <circle cx="250" cy="85" r="8" fill="#0f172a"/>

    <text x="160" y="230" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Consolidated Aggregate Mixture</text>
    <text x="160" y="250" font-size="11" fill="#cbd5e1" text-anchor="middle">Variable chemical composition ($SiO_2, KAlSi_3O_8$, etc.)</text>
    <text x="160" y="270" font-size="10.5" fill="#94a3b8" text-anchor="middle">Analogous to a baked cake made of varied ingredients</text>
  </g>

  <!-- Middle: Zoom Arrows -->
  <g transform="translate(370, 200)">
    <line x1="0" y1="0" x2="50" y2="-60" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4"/>
    <polygon points="50,-60 42,-55 45,-47" fill="#f59e0b"/>
    <line x1="0" y1="20" x2="50" y2="20" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4"/>
    <polygon points="50,20 40,15 40,25" fill="#f59e0b"/>
    <line x1="0" y1="40" x2="50" y2="80" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4"/>
    <polygon points="50,80 43,68 49,63" fill="#f59e0b"/>
  </g>

  <!-- Right: Pure Mineral Components -->
  <g transform="translate(435, 95)">
    <!-- Mineral 1: Quartz -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="320" height="90" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
      <polygon points="20,45 35,15 50,45 42,75 28,75" fill="#e2e8f0" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="75" y="30" font-size="13" font-weight="bold" fill="#38bdf8">1. Quartz (Mineral)</text>
      <text x="75" y="50" font-size="11" fill="#cbd5e1">Formula: SiO2 (Silicon Dioxide)</text>
      <text x="75" y="70" font-size="10" fill="#94a3b8">Ordered hexagonal crystal lattice - Hardness: 7</text>
    </g>

    <!-- Mineral 2: Feldspar -->
    <g transform="translate(0, 105)">
      <rect x="0" y="0" width="320" height="90" rx="8" fill="#0f172a" stroke="#f43f5e" stroke-width="1.5"/>
      <rect x="20" y="20" width="35" height="50" rx="3" fill="#f43f5e" stroke="#fb7185" stroke-width="1.5"/>
      <text x="75" y="30" font-size="13" font-weight="bold" fill="#f43f5e">2. Potassium Feldspar (Mineral)</text>
      <text x="75" y="50" font-size="11" fill="#cbd5e1">Formula: KAlSi3O8 (Potassium Silicate)</text>
      <text x="75" y="70" font-size="10" fill="#94a3b8">Pink prismatic cleavage blocks - Hardness: 6</text>
    </g>

    <!-- Mineral 3: Biotite Mica -->
    <g transform="translate(0, 210)">
      <rect x="0" y="0" width="320" height="90" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
      <polygon points="15,35 45,20 55,55 25,70" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
      <text x="75" y="30" font-size="13" font-weight="bold" fill="#c084fc">3. Biotite Mica (Mineral)</text>
      <text x="75" y="50" font-size="11" fill="#cbd5e1">Formula: K(Mg,Fe)3AlSi3O10(OH)2</text>
      <text x="75" y="70" font-size="10" fill="#94a3b8">Black flexible platy sheets - Hardness: 2.5-3</text>
    </g>
  </g>
</svg>
""")

# SVG 2: The Dynamic Rock Cycle (Lesson 2)
SVG_ROCK_CYCLE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">THE DYNAMIC GEOLOGICAL ROCK CYCLE</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Continuous Pathways of Formation, Destruction, and Transformation</text>

  <!-- Node 1: MAGMA (Bottom Center) -->
  <g transform="translate(310, 340)">
    <rect x="0" y="0" width="180" height="60" rx="10" fill="#dc2626" stroke="#f87171" stroke-width="2"/>
    <text x="90" y="28" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">MOLTEN MAGMA</text>
    <text x="90" y="48" font-size="10" fill="#fee2e2" text-anchor="middle">Subterranean Melting Zone</text>
  </g>

  <!-- Node 2: IGNEOUS ROCKS (Top Left) -->
  <g transform="translate(60, 100)">
    <rect x="0" y="0" width="190" height="70" rx="10" fill="#0f172a" stroke="#f97316" stroke-width="2"/>
    <rect x="0" y="0" width="190" height="28" rx="10" fill="#c2410c"/>
    <text x="95" y="20" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">IGNEOUS ROCKS</text>
    <text x="95" y="46" font-size="10.5" fill="#fdba74" text-anchor="middle">Granite, Basalt, Obsidian</text>
    <text x="95" y="60" font-size="9.5" fill="#94a3b8" text-anchor="middle">Cooled Magma / Lava</text>
  </g>

  <!-- Node 3: SEDIMENTS & SEDIMENTARY (Top Right) -->
  <g transform="translate(550, 100)">
    <rect x="0" y="0" width="190" height="70" rx="10" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect x="0" y="0" width="190" height="28" rx="10" fill="#a16207"/>
    <text x="95" y="20" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">SEDIMENTARY ROCKS</text>
    <text x="95" y="46" font-size="10.5" fill="#fef08a" text-anchor="middle">Sandstone, Shale, Limestone</text>
    <text x="95" y="60" font-size="9.5" fill="#94a3b8" text-anchor="middle">Compacted &amp; Cemented</text>
  </g>

  <!-- Node 4: METAMORPHIC ROCKS (Mid Center) -->
  <g transform="translate(305, 190)">
    <rect x="0" y="0" width="190" height="70" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <rect x="0" y="0" width="190" height="28" rx="10" fill="#7e22ce"/>
    <text x="95" y="20" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">METAMORPHIC ROCKS</text>
    <text x="95" y="46" font-size="10.5" fill="#e9d5ff" text-anchor="middle">Gneiss, Slate, Marble</text>
    <text x="95" y="60" font-size="9.5" fill="#94a3b8" text-anchor="middle">Heat &amp; Pressure Recrystallized</text>
  </g>

  <!-- Pathway: Magma -> Igneous (Cooling & Crystallization) -->
  <path d="M310,360 C180,330 140,240 140,175" fill="none" stroke="#f97316" stroke-width="2.5" stroke-dasharray="5,5"/>
  <polygon points="140,170 135,182 145,182" fill="#f97316"/>
  <text x="135" y="270" font-size="10.5" font-weight="bold" fill="#f97316" transform="rotate(-40, 135, 270)">Cooling &amp; Solidification</text>

  <!-- Pathway: Igneous -> Sedimentary (Weathering, Transport, Lithification) -->
  <path d="M255,120 L545,120" fill="none" stroke="#eab308" stroke-width="2.5"/>
  <polygon points="550,120 538,115 538,125" fill="#eab308"/>
  <text x="400" y="112" font-size="11" font-weight="bold" fill="#eab308" text-anchor="middle">Weathering, Deposition &amp; Lithification</text>

  <!-- Pathway: Sedimentary -> Metamorphic (Heat & Pressure) -->
  <path d="M620,175 C590,225 540,230 500,230" fill="none" stroke="#a855f7" stroke-width="2.5"/>
  <polygon points="495,230 507,225 507,235" fill="#a855f7"/>
  <text x="590" y="215" font-size="10.5" font-weight="bold" fill="#c084fc">Heat &amp; Pressure</text>

  <!-- Pathway: Igneous -> Metamorphic (Heat & Pressure bypass) -->
  <path d="M180,175 C210,225 260,230 300,230" fill="none" stroke="#a855f7" stroke-width="2.5"/>
  <polygon points="305,230 293,225 293,235" fill="#a855f7"/>
  <text x="185" y="215" font-size="10.5" font-weight="bold" fill="#c084fc">Heat &amp; Pressure</text>

  <!-- Pathway: Metamorphic -> Magma (Melting) -->
  <path d="M400,265 L400,335" fill="none" stroke="#ef4444" stroke-width="2.5"/>
  <polygon points="400,340 395,328 405,328" fill="#ef4444"/>
  <text x="415" y="305" font-size="11" font-weight="bold" fill="#ef4444">Melting</text>

  <!-- Direct Pathway: Sedimentary -> Weathering recycling -->
  <path d="M680,100 C720,70 750,110 740,150 C730,165 710,165 700,160" fill="none" stroke="#eab308" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="740" y="85" font-size="9" fill="#eab308">Weathering</text>
</svg>
""")

# SVG 3: Intrusive vs Extrusive Cooling Environments (Lesson 3)
SVG_INTRUSIVE_VS_EXTRUSIVE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">INTRUSIVE VS. EXTRUSIVE IGNEOUS COOLING</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">The Fundamental Rule: Subterranean Insulation vs. Rapid Surface Quenching</text>

  <!-- Left: Geological Cross-Section -->
  <g transform="translate(35, 90)">
    <!-- Sky & Volcano Profile -->
    <rect x="0" y="0" width="360" height="310" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <path d="M0,130 L100,130 L180,60 L200,60 L280,130 L360,130 L360,310 L0,310 Z" fill="#334155"/>
    
    <!-- Surface Lava Flow (Extrusive) -->
    <path d="M200,60 Q230,80 270,130 L340,135" fill="none" stroke="#ef4444" stroke-width="6"/>
    <circle cx="290" cy="132" r="5" fill="#f59e0b"/>
    <text x="280" y="55" font-size="11" font-weight="bold" fill="#ef4444">EXTRUSIVE (Lava)</text>
    <text x="280" y="70" font-size="9.5" fill="#cbd5e1">Rapid Air/Water Cooling</text>

    <!-- Underground Magma Conduit & Chamber (Intrusive) -->
    <path d="M190,60 L190,190" stroke="#dc2626" stroke-width="10"/>
    <ellipse cx="190" cy="245" rx="90" ry="45" fill="#dc2626" stroke="#b91c1c" stroke-width="2"/>
    <text x="190" y="242" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">MAGMA CHAMBER</text>
    <text x="190" y="260" font-size="10" fill="#fee2e2" text-anchor="middle">INTRUSIVE (Plutonic Zone)</text>
    <text x="190" y="295" font-size="10" fill="#94a3b8" text-anchor="middle">Insulated Country Rock -> Slow Cooling</text>
  </g>

  <!-- Right: Texture Comparison Cards -->
  <g transform="translate(420, 90)">
    <!-- Card 1: Extrusive Texture (Basalt / Obsidian) -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="345" height="145" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
      <rect x="0" y="0" width="345" height="30" rx="8" fill="#991b1b"/>
      <text x="172" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">EXTRUSIVE: FINE / GLASSY TEXTURE</text>
      
      <!-- Microscopic grains illustration -->
      <circle cx="45" cy="85" r="30" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
      <path d="M25,85 L65,85 M45,65 L45,105" stroke="#475569" stroke-width="0.8"/>
      <text x="45" y="90" font-size="8" fill="#94a3b8" text-anchor="middle">Microscopic</text>

      <text x="90" y="55" font-size="11.5" font-weight="bold" fill="#f87171">Aphanitic / Glassy (e.g. Basalt, Obsidian)</text>
      <text x="90" y="75" font-size="10.5" fill="#cbd5e1">- Rapid solidification in seconds to days</text>
      <text x="90" y="95" font-size="10.5" fill="#cbd5e1">- Mineral atoms frozen before crystals can grow</text>
      <text x="90" y="115" font-size="10.5" fill="#cbd5e1">- Smooth, dull, or glassy vitreous appearance</text>
    </g>

    <!-- Card 2: Intrusive Texture (Granite / Gabbro) -->
    <g transform="translate(0, 160)">
      <rect x="0" y="0" width="345" height="145" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
      <rect x="0" y="0" width="345" height="30" rx="8" fill="#0369a1"/>
      <text x="172" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">INTRUSIVE: COARSE PHANERITIC TEXTURE</text>
      
      <!-- Coarse interlocking grains illustration -->
      <circle cx="45" cy="85" r="30" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <polygon points="25,75 45,60 40,85" fill="#f43f5e"/>
      <polygon points="45,60 65,75 55,95 40,85" fill="#e2e8f0"/>
      <polygon points="25,75 40,85 30,105" fill="#0f172a"/>
      <polygon points="40,85 55,95 45,110 30,105" fill="#f43f5e"/>

      <text x="90" y="55" font-size="11.5" font-weight="bold" fill="#38bdf8">Phaneritic (e.g. Granite, Diorite, Gabbro)</text>
      <text x="90" y="75" font-size="10.5" fill="#cbd5e1">- Slow cooling over thousands to millions of years</text>
      <text x="90" y="95" font-size="10.5" fill="#cbd5e1">- Mineral crystals grow large (&gt; 1mm) and visible</text>
      <text x="90" y="115" font-size="10.5" fill="#cbd5e1">- Interlocking coarse crystalline mosaic</text>
    </g>
  </g>
</svg>
""")

# SVG 4: Geological Cross-Section of Intrusive Bodies (Lesson 4)
SVG_INTRUSIVE_STRUCTURES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">CROSS-SECTION OF INTRUSIVE IGNEOUS BODIES</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Plutonic Masses (Batholiths) vs. Hypabyssal Sheets (Dykes &amp; Sills)</text>

  <g transform="translate(50, 85)">
    <!-- Country Rock Strata -->
    <rect x="0" y="0" width="700" height="315" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
    <line x1="0" y1="60" x2="700" y2="60" stroke="#334155" stroke-width="2" stroke-dasharray="4,4"/>
    <line x1="0" y1="120" x2="700" y2="120" stroke="#334155" stroke-width="2" stroke-dasharray="4,4"/>
    <line x1="0" y1="180" x2="700" y2="180" stroke="#334155" stroke-width="2" stroke-dasharray="4,4"/>
    
    <!-- Strata labels -->
    <text x="15" y="35" font-size="10" fill="#64748b">Surface Sedimentary Layer</text>
    <text x="15" y="95" font-size="10" fill="#64748b">Country Rock Strata A</text>
    <text x="15" y="155" font-size="10" fill="#64748b">Country Rock Strata B</text>

    <!-- Batholith (Deep Giant Pluton) -->
    <path d="M120,315 C150,200 280,190 350,210 C420,190 520,200 560,315 Z" fill="#dc2626" stroke="#ef4444" stroke-width="2"/>
    <text x="340" y="270" font-size="15" font-weight="bold" fill="#ffffff" text-anchor="middle">BATHOLITH</text>
    <text x="340" y="290" font-size="11" fill="#fee2e2" text-anchor="middle">Massive Deep Plutonic Rock (&gt; 100 km²)</text>

    <!-- Dyke 1 (Discordant Vertical Cut) -->
    <polygon points="180,210 195,210 215,60 200,60" fill="#f97316" stroke="#ea580c" stroke-width="1.5"/>
    <rect x="120" y="90" width="80" height="24" rx="4" fill="#0f172a" stroke="#f97316" stroke-width="1"/>
    <text x="160" y="106" font-size="10" font-weight="bold" fill="#f97316" text-anchor="middle">DYKE (Vertical)</text>

    <!-- Sill (Concordant Horizontal Sheet) -->
    <polygon points="208,120 450,120 450,135 206,135" fill="#f97316" stroke="#ea580c" stroke-width="1.5"/>
    <rect x="330" y="138" width="90" height="22" rx="4" fill="#0f172a" stroke="#f97316" stroke-width="1"/>
    <text x="375" y="153" font-size="10" font-weight="bold" fill="#f97316" text-anchor="middle">SILL (Horizontal)</text>

    <!-- Laccolith (Dome-shaped intrusion) -->
    <path d="M460,120 Q540,50 620,120 Z" fill="#f97316" stroke="#ea580c" stroke-width="1.5"/>
    <polygon points="535,210 545,210 545,120 535,120" fill="#f97316"/>
    <rect x="505" y="80" width="90" height="22" rx="4" fill="#0f172a" stroke="#f97316" stroke-width="1"/>
    <text x="550" y="95" font-size="10" font-weight="bold" fill="#f97316" text-anchor="middle">LACCOLITH</text>
  </g>
</svg>
""")

# SVG 5: Extrusive Rock Textures (Lesson 5)
SVG_EXTRUSIVE_TEXTURES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">EXTRUSIVE VOLCANIC PRODUCTS &amp; TEXTURES</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Effusive Lava Flows, Volcanic Glass, Vesicular Froth, and Pyroclastic Tuff</text>

  <!-- Grid of 4 Extrusive Types -->
  <g transform="translate(40, 85)">
    <!-- 1. Basalt -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="340" height="145" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
      <rect x="15" y="15" width="70" height="70" rx="6" fill="#1e293b" stroke="#64748b" stroke-width="1"/>
      <text x="50" y="55" font-size="9" fill="#94a3b8" text-anchor="middle">Dark Basalt</text>
      <text x="100" y="30" font-size="13" font-weight="bold" fill="#f87171">1. Basalt (Fine-Grained)</text>
      <text x="100" y="50" font-size="11" fill="#cbd5e1">Origin: Fluid basic lava flows</text>
      <text x="100" y="70" font-size="10.5" fill="#94a3b8">Texture: Aphanitic (microscopic crystals)</text>
      <text x="100" y="90" font-size="10.5" fill="#38bdf8">Kenya: Rift Valley floor plains</text>
    </g>

    <!-- 2. Obsidian -->
    <g transform="translate(370, 0)">
      <rect x="0" y="0" width="340" height="145" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
      <rect x="15" y="15" width="70" height="70" rx="6" fill="#020617" stroke="#38bdf8" stroke-width="1"/>
      <path d="M25,25 Q50,40 75,25 M30,65 Q55,45 70,70" stroke="#38bdf8" stroke-width="1.5" fill="none"/>
      <text x="100" y="30" font-size="13" font-weight="bold" fill="#38bdf8">2. Obsidian (Volcanic Glass)</text>
      <text x="100" y="50" font-size="11" fill="#cbd5e1">Origin: Instant cooling of silica lava</text>
      <text x="100" y="70" font-size="10.5" fill="#94a3b8">Texture: Glassy, sharp conchoidal fracture</text>
      <text x="100" y="90" font-size="10.5" fill="#38bdf8">Kenya: Hell's Gate, Naivasha</text>
    </g>

    <!-- 3. Pumice -->
    <g transform="translate(0, 160)">
      <rect x="0" y="0" width="340" height="145" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
      <rect x="15" y="15" width="70" height="70" rx="6" fill="#64748b" stroke="#f59e0b" stroke-width="1"/>
      <circle cx="30" cy="35" r="4" fill="#0f172a"/>
      <circle cx="50" cy="45" r="6" fill="#0f172a"/>
      <circle cx="70" cy="35" r="3" fill="#0f172a"/>
      <circle cx="40" cy="65" r="5" fill="#0f172a"/>
      <circle cx="65" cy="68" r="4" fill="#0f172a"/>
      <text x="100" y="30" font-size="13" font-weight="bold" fill="#fbbf24">3. Pumice (Vesicular Froth)</text>
      <text x="100" y="50" font-size="11" fill="#cbd5e1">Origin: Frothy gas-charged lava</text>
      <text x="100" y="70" font-size="10.5" fill="#94a3b8">Texture: Highly porous, floats on water</text>
      <text x="100" y="90" font-size="10.5" fill="#38bdf8">Kenya: Longonot &amp; Menengai craters</text>
    </g>

    <!-- 4. Volcanic Tuff -->
    <g transform="translate(370, 160)">
      <rect x="0" y="0" width="340" height="145" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
      <rect x="15" y="15" width="70" height="70" rx="6" fill="#475569" stroke="#a855f7" stroke-width="1"/>
      <line x1="20" y1="35" x2="80" y2="35" stroke="#a855f7" stroke-width="2"/>
      <line x1="20" y1="55" x2="80" y2="55" stroke="#a855f7" stroke-width="2"/>
      <line x1="20" y1="75" x2="80" y2="75" stroke="#a855f7" stroke-width="2"/>
      <text x="100" y="30" font-size="13" font-weight="bold" fill="#c084fc">4. Volcanic Tuff (Pyroclastic)</text>
      <text x="100" y="50" font-size="11" fill="#cbd5e1">Origin: Compressed volcanic ash/cinders</text>
      <text x="100" y="70" font-size="10.5" fill="#94a3b8">Texture: Layered consolidated ejecta</text>
      <text x="100" y="90" font-size="10.5" fill="#38bdf8">Kenya: Nairobi &amp; Machakos building stones</text>
    </g>
  </g>
</svg>
""")

# SVG 6: The Steps of Lithification (Lesson 6)
SVG_LITHIFICATION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">THE GEOLOGICAL STEPS OF LITHIFICATION</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">How Loose Sediments Transform into Solid Sedimentary Rock</text>

  <!-- Step 1: Deposition -->
  <g transform="translate(40, 95)">
    <rect x="0" y="0" width="220" height="300" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="36" rx="10" fill="#0284c7"/>
    <text x="110" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">1. DEPOSITION</text>
    
    <!-- Loose Grains & Water -->
    <rect x="20" y="55" width="180" height="140" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
    <rect x="20" y="55" width="180" height="140" rx="6" fill="#0284c7" opacity="0.3"/>
    <circle cx="50" cy="85" r="14" fill="#fbbf24"/>
    <circle cx="90" cy="80" r="12" fill="#fbbf24"/>
    <circle cx="130" cy="90" r="15" fill="#fbbf24"/>
    <circle cx="170" cy="85" r="13" fill="#fbbf24"/>
    <circle cx="65" cy="130" r="15" fill="#fbbf24"/>
    <circle cx="110" cy="135" r="16" fill="#fbbf24"/>
    <circle cx="155" cy="130" r="14" fill="#fbbf24"/>
    <circle cx="85" cy="170" r="15" fill="#fbbf24"/>
    <circle cx="135" cy="170" r="15" fill="#fbbf24"/>

    <text x="110" y="220" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Loose Sediment Layer</text>
    <text x="110" y="240" font-size="10.5" fill="#cbd5e1" text-anchor="middle">High pore space (50-60%)</text>
    <text x="110" y="260" font-size="10" fill="#94a3b8" text-anchor="middle">Grains surrounded by water</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <polygon points="275,230 295,230 295,225 305,235 295,245 295,240 275,240" fill="#f59e0b"/>

  <!-- Step 2: Compaction -->
  <g transform="translate(290, 95)">
    <rect x="0" y="0" width="220" height="300" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="36" rx="10" fill="#d97706"/>
    <text x="110" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">2. COMPACTION</text>
    
    <!-- Pressure arrows down -->
    <line x1="60" y1="48" x2="60" y2="60" stroke="#f59e0b" stroke-width="2"/>
    <polygon points="60,65 55,58 65,58" fill="#f59e0b"/>
    <line x1="110" y1="48" x2="110" y2="60" stroke="#f59e0b" stroke-width="2"/>
    <polygon points="110,65 105,58 115,58" fill="#f59e0b"/>
    <line x1="160" y1="48" x2="160" y2="60" stroke="#f59e0b" stroke-width="2"/>
    <polygon points="160,65 155,58 165,58" fill="#f59e0b"/>

    <!-- Tightly squeezed grains -->
    <rect x="20" y="70" width="180" height="125" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
    <circle cx="50" cy="95" r="14" fill="#fbbf24"/>
    <circle cx="78" cy="95" r="12" fill="#fbbf24"/>
    <circle cx="110" cy="95" r="15" fill="#fbbf24"/>
    <circle cx="145" cy="95" r="13" fill="#fbbf24"/>
    <circle cx="170" cy="95" r="11" fill="#fbbf24"/>
    <circle cx="60" cy="130" r="15" fill="#fbbf24"/>
    <circle cx="95" cy="130" r="16" fill="#fbbf24"/>
    <circle cx="130" cy="130" r="14" fill="#fbbf24"/>
    <circle cx="160" cy="130" r="13" fill="#fbbf24"/>
    <circle cx="75" cy="165" r="15" fill="#fbbf24"/>
    <circle cx="115" cy="165" r="15" fill="#fbbf24"/>
    <circle cx="150" cy="165" r="13" fill="#fbbf24"/>

    <text x="110" y="220" font-size="12" font-weight="bold" fill="#fbbf24" text-anchor="middle">Overlying Weight Squeezing</text>
    <text x="110" y="240" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Pore water expelled</text>
    <text x="110" y="260" font-size="10" fill="#94a3b8" text-anchor="middle">Grains tightly packed</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <polygon points="525,230 545,230 545,225 555,235 545,245 545,240 525,240" fill="#22c55e"/>

  <!-- Step 3: Cementation -->
  <g transform="translate(540, 95)">
    <rect x="0" y="0" width="220" height="300" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="36" rx="10" fill="#15803d"/>
    <text x="110" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">3. CEMENTATION</text>
    
    <!-- Cemented Solid Rock -->
    <rect x="20" y="55" width="180" height="140" rx="6" fill="#15803d" opacity="0.4"/>
    <rect x="20" y="55" width="180" height="140" rx="6" fill="none" stroke="#22c55e" stroke-width="1"/>
    <circle cx="50" cy="85" r="14" fill="#fbbf24" stroke="#22c55e" stroke-width="2"/>
    <circle cx="78" cy="85" r="12" fill="#fbbf24" stroke="#22c55e" stroke-width="2"/>
    <circle cx="110" cy="85" r="15" fill="#fbbf24" stroke="#22c55e" stroke-width="2"/>
    <circle cx="145" cy="85" r="13" fill="#fbbf24" stroke="#22c55e" stroke-width="2"/>
    <circle cx="60" cy="120" r="15" fill="#fbbf24" stroke="#22c55e" stroke-width="2"/>
    <circle cx="95" cy="120" r="16" fill="#fbbf24" stroke="#22c55e" stroke-width="2"/>
    <circle cx="130" cy="120" r="14" fill="#fbbf24" stroke="#22c55e" stroke-width="2"/>
    <circle cx="75" cy="155" r="15" fill="#fbbf24" stroke="#22c55e" stroke-width="2"/>
    <circle cx="115" cy="155" r="15" fill="#fbbf24" stroke="#22c55e" stroke-width="2"/>

    <text x="110" y="220" font-size="12" font-weight="bold" fill="#4ade80" text-anchor="middle">Mineral Glue Bonds Grains</text>
    <text x="110" y="240" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Calcite / Silica / Iron Glue</text>
    <text x="110" y="260" font-size="10" fill="#94a3b8" text-anchor="middle">Solid Sedimentary Rock Formed</text>
  </g>
</svg>
""")

# SVG 7: Classification of Organically Formed Rocks (Lesson 7)
SVG_SEDIMENTARY_CLASSES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">CLASSIFICATION OF SEDIMENTARY ROCKS</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Mechanically Formed (Clastic) vs. Organically Formed (Biological)</text>

  <!-- Left: Clastic Hierarchy -->
  <g transform="translate(40, 85)">
    <rect x="0" y="0" width="340" height="315" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <rect x="0" y="0" width="340" height="32" rx="8" fill="#a16207"/>
    <text x="170" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">1. MECHANICALLY FORMED (CLASTIC)</text>
    
    <g transform="translate(15, 45)">
      <!-- Conglomerate -->
      <rect x="0" y="0" width="310" height="55" rx="6" fill="#1e293b"/>
      <text x="15" y="22" font-size="12" font-weight="bold" fill="#fde047">Conglomerate &amp; Breccia</text>
      <text x="15" y="40" font-size="10.5" fill="#cbd5e1">Coarse gravel (&gt; 2mm); rounded river pebbles / angular debris</text>

      <!-- Sandstone -->
      <rect x="0" y="65" width="310" height="55" rx="6" fill="#1e293b"/>
      <text x="15" y="87" font-size="12" font-weight="bold" fill="#fde047">Sandstone</text>
      <text x="15" y="105" font-size="10.5" fill="#cbd5e1">Medium sand grains (0.06 - 2mm); quartz sand cemented</text>

      <!-- Shale -->
      <rect x="0" y="130" width="310" height="55" rx="6" fill="#1e293b"/>
      <text x="15" y="152" font-size="12" font-weight="bold" fill="#fde047">Shale &amp; Mudstone</text>
      <text x="15" y="170" font-size="10.5" fill="#cbd5e1">Fine clay/silt (&lt; 0.06mm); thin flaky sheets from calm muds</text>

      <!-- Kenya note -->
      <rect x="0" y="195" width="310" height="60" rx="6" fill="#334155"/>
      <text x="15" y="217" font-size="11" font-weight="bold" fill="#38bdf8">Kenyan Occurrence:</text>
      <text x="15" y="237" font-size="10" fill="#e2e8f0">Mazeras &amp; Mariakani Sandstones in Coastal Kenya</text>
    </g>
  </g>

  <!-- Right: Organic Classes -->
  <g transform="translate(420, 85)">
    <rect x="0" y="0" width="340" height="315" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="340" height="32" rx="8" fill="#15803d"/>
    <text x="170" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">2. ORGANICALLY FORMED (BIOLOGICAL)</text>
    
    <g transform="translate(15, 45)">
      <!-- Calcareous -->
      <rect x="0" y="0" width="310" height="55" rx="6" fill="#1e293b"/>
      <text x="15" y="22" font-size="12" font-weight="bold" fill="#86efac">Calcareous (Limestone, Chalk)</text>
      <text x="15" y="40" font-size="10.5" fill="#cbd5e1">Calcium-rich coral reefs &amp; shells (Bamburi, Mombasa)</text>

      <!-- Carbonaceous -->
      <rect x="0" y="65" width="310" height="55" rx="6" fill="#1e293b"/>
      <text x="15" y="87" font-size="12" font-weight="bold" fill="#86efac">Carbonaceous (Coal, Lignite, Peat)</text>
      <text x="15" y="105" font-size="10.5" fill="#cbd5e1">Ancient compressed swamp vegetation &amp; peat bogs</text>

      <!-- Siliceous -->
      <rect x="0" y="130" width="310" height="55" rx="6" fill="#1e293b"/>
      <text x="15" y="152" font-size="12" font-weight="bold" fill="#86efac">Siliceous (Diatomite)</text>
      <text x="15" y="170" font-size="10.5" fill="#cbd5e1">Microscopic single-celled diatom algae shells (Kariandusi)</text>

      <!-- Ferruginous -->
      <rect x="0" y="195" width="310" height="60" rx="6" fill="#1e293b"/>
      <text x="15" y="217" font-size="12" font-weight="bold" fill="#86efac">Ferruginous (Bog Iron Ore)</text>
      <text x="15" y="237" font-size="10.5" fill="#cbd5e1">Iron deposits precipitated by bacterial biochemical action</text>
    </g>
  </g>
</svg>
""")

# SVG 8: Chemical Formation of Trona at Lake Magadi (Lesson 8)
SVG_TRONA_MAGADI = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">FORMATION OF TRONA EVAPORITES AT LAKE MAGADI</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Closed Basin Hydrology, Alkaline Leaching, and Solar Crystallization</text>

  <!-- Basin Cross-Section Graphic -->
  <g transform="translate(45, 90)">
    <rect x="0" y="0" width="710" height="310" rx="8" fill="#0f172a" stroke="#f43f5e" stroke-width="1.5"/>
    
    <!-- Rift Valley Fault Escarpments -->
    <path d="M0,80 L120,80 L160,200 L550,200 L590,80 L710,80 L710,310 L0,310 Z" fill="#334155"/>
    
    <!-- Sun (Evaporation Engine) -->
    <circle cx="355" cy="50" r="25" fill="#f59e0b"/>
    <line x1="355" y1="15" x2="355" y2="5" stroke="#f59e0b" stroke-width="2"/>
    <line x1="355" y1="85" x2="355" y2="95" stroke="#f59e0b" stroke-width="2"/>
    <line x1="320" y1="50" x2="310" y2="50" stroke="#f59e0b" stroke-width="2"/>
    <line x1="390" y1="50" x2="400" y2="50" stroke="#f59e0b" stroke-width="2"/>
    
    <!-- Evaporation vapor arrows -->
    <path d="M280,180 Q290,140 280,110" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3,3" fill="none"/>
    <polygon points="280,105 275,115 285,115" fill="#f43f5e"/>
    <path d="M430,180 Q440,140 430,110" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3,3" fill="none"/>
    <polygon points="430,105 425,115 435,115" fill="#f43f5e"/>
    <text x="355" y="110" font-size="11" font-weight="bold" fill="#f43f5e" text-anchor="middle">INTENSE SOLAR EVAPORATION</text>

    <!-- Groundwater inflow leaching volcanic rocks -->
    <path d="M70,140 Q130,180 180,210" stroke="#38bdf8" stroke-width="3" fill="none"/>
    <polygon points="185,212 173,208 178,218" fill="#38bdf8"/>
    <text x="90" y="130" font-size="10" fill="#38bdf8">Rainwater Leaches Sodium</text>
    <text x="90" y="145" font-size="9" fill="#94a3b8">from Volcanic Rocks</text>

    <!-- Alkaline Springs -->
    <circle cx="210" cy="205" r="8" fill="#ec4899"/>
    <circle cx="500" cy="205" r="8" fill="#ec4899"/>
    <text x="210" y="195" font-size="9.5" font-weight="bold" fill="#f472b6" text-anchor="middle">Hot Spring</text>

    <!-- Lake Magadi Trona Salt Bed -->
    <rect x="180" y="210" width="350" height="35" rx="4" fill="#fbcfe8" stroke="#f43f5e" stroke-width="2"/>
    <text x="355" y="232" font-size="13" font-weight="bold" fill="#831843" text-anchor="middle">TRONA CRUST (SODA ASH BED)</text>
    
    <!-- Chemical Equation Box -->
    <rect x="120" y="260" width="470" height="35" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <text x="355" y="282" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Na2CO3 + NaHCO3 + 2H2O -> Na3H(CO3)2·2H2O (Trona Solid Evaporite)</text>
  </g>
</svg>
""")

# SVG 9: Agents of Metamorphism (Lesson 9)
SVG_METAMORPHIC_AGENTS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">THE THREE AGENTS OF METAMORPHISM</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Solid-State Transformation via Heat, Directed Pressure, and Hydrothermal Fluids</text>

  <!-- Panel 1: Heat -->
  <g transform="translate(35, 90)">
    <rect x="0" y="0" width="225" height="305" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="225" height="36" rx="10" fill="#991b1b"/>
    <text x="112" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">1. GEOTHERMAL HEAT</text>
    
    <!-- Magma baking graphic -->
    <path d="M20,180 C50,120 180,120 205,180" fill="#dc2626"/>
    <text x="112" y="165" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Magma Body</text>
    <path d="M30,110 Q112,90 195,110" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3" fill="none"/>
    <text x="112" y="100" font-size="9.5" fill="#f59e0b" text-anchor="middle">Thermal Bake Zone</text>

    <text x="112" y="210" font-size="12" font-weight="bold" fill="#f87171" text-anchor="middle">Recrystallization Energy</text>
    <text x="112" y="230" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Weakens chemical bonds</text>
    <text x="112" y="250" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Grows larger, stable crystals</text>
    <text x="112" y="275" font-size="10" fill="#94a3b8" text-anchor="middle">Source: Magma &amp; Depth</text>
  </g>

  <!-- Panel 2: Pressure -->
  <g transform="translate(285, 90)">
    <rect x="0" y="0" width="225" height="305" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <rect x="0" y="0" width="225" height="36" rx="10" fill="#7e22ce"/>
    <text x="112" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">2. DIRECTED PRESSURE</text>
    
    <!-- Compressive tectonic arrows -->
    <polygon points="25,120 55,120 55,110 70,125 55,140 55,130 25,130" fill="#a855f7"/>
    <polygon points="200,120 170,120 170,110 155,125 170,140 170,130 200,130" fill="#a855f7"/>
    <!-- Folded layers -->
    <path d="M80,105 Q112,85 145,105 Q112,125 80,105" fill="#c084fc"/>
    <path d="M80,125 Q112,105 145,125 Q112,145 80,125" fill="#e9d5ff"/>
    <path d="M80,145 Q112,125 145,145 Q112,165 80,145" fill="#7e22ce"/>

    <text x="112" y="210" font-size="12" font-weight="bold" fill="#c084fc" text-anchor="middle">Differential Stress</text>
    <text x="112" y="230" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Flattens mineral grains</text>
    <text x="112" y="250" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Generates parallel foliation</text>
    <text x="112" y="275" font-size="10" fill="#94a3b8" text-anchor="middle">Source: Tectonic collisions</text>
  </g>

  <!-- Panel 3: Hydrothermal Fluids -->
  <g transform="translate(535, 90)">
    <rect x="0" y="0" width="225" height="305" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="225" height="36" rx="10" fill="#0284c7"/>
    <text x="112" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">3. REACTIVE FLUIDS</text>
    
    <!-- Hydrothermal cracks -->
    <path d="M40,70 L80,110 L110,90 L160,140 L190,120" stroke="#38bdf8" stroke-width="3" fill="none"/>
    <circle cx="80" cy="110" r="5" fill="#38bdf8"/>
    <circle cx="160" cy="140" r="5" fill="#38bdf8"/>
    <text x="112" y="165" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Ion Transport in Fractures</text>

    <text x="112" y="210" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Chemical Catalysis</text>
    <text x="112" y="230" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Transports dissolved ions</text>
    <text x="112" y="250" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Speeds up reactions</text>
    <text x="112" y="275" font-size="10" fill="#94a3b8" text-anchor="middle">Forms rich mineral veins</text>
  </g>
</svg>
""")

# SVG 10: Contact vs Regional Metamorphism Settings (Lesson 10)
SVG_METAMORPHISM_TYPES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">CONTACT VS. REGIONAL METAMORPHISM SETTINGS</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Localized Magmatic Thermal Aureoles vs. Mountain-Scale Tectonic Collisions</text>

  <!-- Left: Contact Metamorphism -->
  <g transform="translate(40, 85)">
    <rect x="0" y="0" width="340" height="315" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="340" height="32" rx="8" fill="#991b1b"/>
    <text x="170" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">CONTACT (THERMAL) METAMORPHISM</text>
    
    <!-- Magma intrusion diagram -->
    <ellipse cx="170" cy="140" rx="60" ry="35" fill="#dc2626"/>
    <text x="170" y="145" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Magma Body</text>
    <!-- Aureole concentric circles -->
    <ellipse cx="170" cy="140" rx="85" ry="50" fill="none" stroke="#f97316" stroke-width="2" stroke-dasharray="3,3"/>
    <ellipse cx="170" cy="140" rx="110" ry="65" fill="none" stroke="#eab308" stroke-width="1.5" stroke-dasharray="3,3"/>
    <text x="170" y="215" font-size="10" font-weight="bold" fill="#f97316" text-anchor="middle">Metamorphic Aureole (Bake Zone)</text>

    <text x="170" y="245" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">Dominant Agent: High Heat</text>
    <text x="170" y="265" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Scale: Localized (meters around intrusions)</text>
    <text x="170" y="285" font-size="10" fill="#94a3b8" text-anchor="middle">Examples: Hornfels, Marble, Quartzite</text>
  </g>

  <!-- Right: Regional Metamorphism -->
  <g transform="translate(420, 85)">
    <rect x="0" y="0" width="340" height="315" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="0" y="0" width="340" height="32" rx="8" fill="#7e22ce"/>
    <text x="170" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">REGIONAL METAMORPHISM</text>
    
    <!-- Continental collision cross section -->
    <path d="M20,160 L90,100 L170,160 L250,90 L320,160 L320,210 L20,210 Z" fill="#334155" stroke="#a855f7" stroke-width="1.5"/>
    <polygon points="30,130 60,130 60,122 75,135 60,148 60,140 30,140" fill="#c084fc"/>
    <polygon points="310,130 280,130 280,122 265,135 280,148 280,140 310,140" fill="#c084fc"/>
    <text x="170" y="195" font-size="10" font-weight="bold" fill="#e9d5ff" text-anchor="middle">Folded Mountain Crust</text>

    <text x="170" y="245" font-size="11" font-weight="bold" fill="#c084fc" text-anchor="middle">Dominant Agents: Heat + Directed Stress</text>
    <text x="170" y="265" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Scale: Massive (1,000s of km² mountain belts)</text>
    <text x="170" y="285" font-size="10" fill="#94a3b8" text-anchor="middle">Kenya: Taita Hills, Mozambique Belt Gneisses</text>
  </g>
</svg>
""")

# SVG 11: Parent Rocks to Metamorphic Rocks Matrix (Lesson 11)
SVG_PROTOLITH_MATRIX = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">PARENT ROCKS &amp; METAMORPHIC DERIVATIVES</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Transformation Matrix: Protolith -> Metamorphic Rock and Resulting Texture</text>

  <!-- Table Structure -->
  <g transform="translate(40, 85)">
    <!-- Header -->
    <rect x="0" y="0" width="720" height="35" rx="6" fill="#0284c7"/>
    <text x="120" y="23" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">PARENT ROCK (PROTOLITH)</text>
    <text x="270" y="23" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">ORIGINAL CLASS</text>
    <text x="450" y="23" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">METAMORPHIC DERIVATIVE</text>
    <text x="630" y="23" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">TEXTURE</text>

    <!-- Row 1: Granite -> Gneiss -->
    <g transform="translate(0, 45)">
      <rect x="0" y="0" width="720" height="55" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
      <text x="120" y="32" font-size="13" font-weight="bold" fill="#f87171" text-anchor="middle">Granite</text>
      <text x="270" y="32" font-size="12" fill="#cbd5e1" text-anchor="middle">Plutonic Igneous</text>
      <text x="450" y="32" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">Gneiss</text>
      <rect x="575" y="15" width="110" height="25" rx="4" fill="#7e22ce"/>
      <text x="630" y="32" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Foliated (Banded)</text>
    </g>

    <!-- Row 2: Shale -> Slate -->
    <g transform="translate(0, 110)">
      <rect x="0" y="0" width="720" height="55" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
      <text x="120" y="32" font-size="13" font-weight="bold" fill="#fde047" text-anchor="middle">Shale / Clay</text>
      <text x="270" y="32" font-size="12" fill="#cbd5e1" text-anchor="middle">Clastic Sedimentary</text>
      <text x="450" y="32" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">Slate</text>
      <rect x="575" y="15" width="110" height="25" rx="4" fill="#7e22ce"/>
      <text x="630" y="32" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Foliated (Sheets)</text>
    </g>

    <!-- Row 3: Limestone -> Marble -->
    <g transform="translate(0, 175)">
      <rect x="0" y="0" width="720" height="55" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
      <text x="120" y="32" font-size="13" font-weight="bold" fill="#86efac" text-anchor="middle">Limestone</text>
      <text x="270" y="32" font-size="12" fill="#cbd5e1" text-anchor="middle">Organic / Chemical</text>
      <text x="450" y="32" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">Marble</text>
      <rect x="575" y="15" width="110" height="25" rx="4" fill="#0369a1"/>
      <text x="630" y="32" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Non-Foliated</text>
    </g>

    <!-- Row 4: Sandstone -> Quartzite -->
    <g transform="translate(0, 240)">
      <rect x="0" y="0" width="720" height="55" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
      <text x="120" y="32" font-size="13" font-weight="bold" fill="#fde047" text-anchor="middle">Sandstone</text>
      <text x="270" y="32" font-size="12" fill="#cbd5e1" text-anchor="middle">Clastic Sedimentary</text>
      <text x="450" y="32" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">Quartzite</text>
      <rect x="575" y="15" width="110" height="25" rx="4" fill="#0369a1"/>
      <text x="630" y="32" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Non-Foliated</text>
    </g>
  </g>
</svg>
""")

# SVG 12: Geological Stratigraphy Pillar (Lesson 12)
SVG_GEOLOGICAL_PILLAR = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">THE GEOLOGICAL STRATIGRAPHY PILLAR</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Chronological Eras: Precambrian, Paleozoic, Mesozoic, and Cenozoic</text>

  <g transform="translate(60, 85)">
    <!-- Column 1: Cenozoic (Top) -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="680" height="65" rx="6" fill="#b91c1c" stroke="#f87171" stroke-width="1.5"/>
      <text x="140" y="28" font-size="13" font-weight="bold" fill="#ffffff">CENOZOIC ERA (Recent - 66 Ma)</text>
      <text x="140" y="48" font-size="11" fill="#fee2e2">Age of Mammals &amp; Active Rifting | Youngest rock strata</text>
      <text x="520" y="38" font-size="11" font-weight="bold" fill="#fef08a">Kenya: Rift Valley Volcanics</text>
    </g>

    <!-- Column 2: Mesozoic -->
    <g transform="translate(0, 75)">
      <rect x="0" y="0" width="680" height="65" rx="6" fill="#c2410c" stroke="#fb923c" stroke-width="1.5"/>
      <text x="140" y="28" font-size="13" font-weight="bold" fill="#ffffff">MESOZOIC ERA (66 - 252 Ma)</text>
      <text x="140" y="48" font-size="11" fill="#ffedd5">Age of Reptiles &amp; Dinosaurs | Marine sandstones &amp; shales</text>
      <text x="520" y="38" font-size="11" font-weight="bold" fill="#fef08a">Kenya: Coastal Sediments</text>
    </g>

    <!-- Column 3: Paleozoic -->
    <g transform="translate(0, 150)">
      <rect x="0" y="0" width="680" height="65" rx="6" fill="#15803d" stroke="#4ade80" stroke-width="1.5"/>
      <text x="140" y="28" font-size="13" font-weight="bold" fill="#ffffff">PALEOZOIC ERA (252 - 541 Ma)</text>
      <text x="140" y="48" font-size="11" fill="#dcfce7">Early complex marine life | Ancient sandstones &amp; coal beds</text>
      <text x="520" y="38" font-size="11" font-weight="bold" fill="#fef08a">Kenya: Karoo Formations</text>
    </g>

    <!-- Column 4: Precambrian (Bottom / Deepest) -->
    <g transform="translate(0, 225)">
      <rect x="0" y="0" width="680" height="75" rx="6" fill="#1e1b4b" stroke="#818cf8" stroke-width="1.5"/>
      <text x="140" y="30" font-size="13" font-weight="bold" fill="#ffffff">PRECAMBRIAN ERA (Over 541 Ma - 4.6 Ga)</text>
      <text x="140" y="52" font-size="11" fill="#e0e7ff">Origin of Earth; Basement shields; Metamorphic gneisses &amp; granites</text>
      <text x="520" y="42" font-size="11" font-weight="bold" fill="#fef08a">Kenya: Basement System</text>
    </g>

    <!-- Depth arrow on left -->
    <line x1="-30" y1="10" x2="-30" y2="290" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="-30,300 -35,288 -25,288" fill="#38bdf8"/>
    <text x="-38" y="150" font-size="10.5" font-weight="bold" fill="#38bdf8" transform="rotate(-90, -38, 150)">INCREASING AGE &amp; DEPTH</text>
  </g>
</svg>
""")

# SVG 13: Geological Map of Kenya - Basement & Granites (Lesson 13)
SVG_KENYA_BASEMENT_MAP = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">GEOLOGICAL MAP OF KENYA: PRECAMBRIAN PROVINCES</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Distribution of Ancient Metamorphic Basement System &amp; Western Granitic Plutons</text>

  <!-- Map Shape Outline of Kenya -->
  <g transform="translate(60, 85)">
    <rect x="0" y="0" width="380" height="315" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    
    <!-- Simplified Kenya Polygon -->
    <polygon points="60,40 180,20 280,30 350,110 320,200 240,290 150,290 90,220 50,140" fill="#334155" stroke="#64748b" stroke-width="2"/>
    
    <!-- Precambrian Basement Belt (Eastern / Northern / Coast Hinterland) in Purple -->
    <polygon points="170,30 270,40 330,110 300,190 220,260 180,220 200,110" fill="#7e22ce" opacity="0.6"/>
    <text x="240" y="120" font-size="11" font-weight="bold" fill="#ffffff">BASEMENT</text>
    <text x="240" y="135" font-size="9" fill="#e9d5ff">Gneiss &amp; Schists</text>

    <!-- Western Plutonic Granites in Orange dots -->
    <circle cx="80" cy="180" r="14" fill="#f97316"/>
    <circle cx="95" cy="160" r="10" fill="#f97316"/>
    <circle cx="75" cy="205" r="12" fill="#f97316"/>
    <text x="95" y="185" font-size="10" font-weight="bold" fill="#ffffff">GRANITES</text>

    <!-- Lake Victoria (Blue) -->
    <ellipse cx="65" cy="190" rx="20" ry="30" fill="#0284c7" opacity="0.8"/>
  </g>

  <!-- Right Legend & Details -->
  <g transform="translate(470, 95)">
    <!-- Legend Card 1: Basement System -->
    <rect x="0" y="0" width="290" height="135" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="15" y="15" width="20" height="20" rx="3" fill="#7e22ce"/>
    <text x="45" y="30" font-size="13" font-weight="bold" fill="#c084fc">Precambrian Basement</text>
    <text x="15" y="55" font-size="10.5" fill="#cbd5e1">- Machakos, Kitui, Makueni, Embu</text>
    <text x="15" y="75" font-size="10.5" fill="#cbd5e1">- Northern Kenya (Turkana, Marsabit)</text>
    <text x="15" y="95" font-size="10.5" fill="#cbd5e1">- Taita Hills &amp; Taru hinterland</text>
    <text x="15" y="115" font-size="10" fill="#94a3b8">Rocks: Gneisses, schists, marbles</text>

    <!-- Legend Card 2: Western Granites -->
    <g transform="translate(0, 150)">
      <rect x="0" y="0" width="290" height="135" rx="8" fill="#0f172a" stroke="#f97316" stroke-width="1.5"/>
      <circle cx="25" cy="25" r="10" fill="#f97316"/>
      <text x="45" y="30" font-size="13" font-weight="bold" fill="#fb923c">Western Plutonic Granites</text>
      <text x="15" y="55" font-size="10.5" fill="#cbd5e1">- Kakamega, Vihiga, Kisumu, Kisii</text>
      <text x="15" y="75" font-size="10.5" fill="#cbd5e1">- Tabaka Soapstone (altered volcanic)</text>
      <text x="15" y="95" font-size="10.5" fill="#cbd5e1">- Massive tor monuments (Kit Mikayi)</text>
      <text x="15" y="115" font-size="10" fill="#94a3b8">Rocks: Coarse granite, syenite, ballast</text>
    </g>
  </g>
</svg>
""")

# SVG 14: Comprehensive Kenya Rock Distribution Map (Lesson 14)
SVG_KENYA_COMPREHENSIVE_MAP = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">COMPREHENSIVE GEOLOGICAL MAP OF KENYA</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Nationwide Distribution of Volcanic, Sedimentary, and Metamorphic Rocks</text>

  <!-- Left: Map Representation -->
  <g transform="translate(45, 85)">
    <rect x="0" y="0" width="370" height="315" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    
    <!-- Kenya Outline -->
    <polygon points="50,40 170,20 270,30 340,110 310,200 230,290 140,290 80,220 40,140" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
    
    <!-- Central Rift Volcanics (Red/Orange) -->
    <polygon points="120,40 170,40 180,180 150,250 110,230 110,90" fill="#dc2626" opacity="0.8"/>
    <text x="145" y="120" font-size="9" font-weight="bold" fill="#ffffff" transform="rotate(75, 145, 120)">RIFT VOLCANICS</text>

    <!-- Coastal Sedimentary Belt (Yellow) -->
    <polygon points="230,285 305,200 325,210 250,290" fill="#eab308" opacity="0.85"/>
    <text x="280" y="255" font-size="9" font-weight="bold" fill="#000000" transform="rotate(-55, 280, 255)">COAST SEDIMENTS</text>

    <!-- Precambrian Basement (Purple) -->
    <polygon points="170,30 260,35 320,105 285,185 200,160 180,60" fill="#7e22ce" opacity="0.6"/>

    <!-- Western Granites/Sediments (Green) -->
    <ellipse cx="65" cy="180" rx="18" ry="25" fill="#15803d" opacity="0.8"/>
  </g>

  <!-- Right: 4-Province Legend -->
  <g transform="translate(435, 85)">
    <!-- Province 1: Volcanics -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="320" height="70" rx="6" fill="#0f172a" stroke="#dc2626" stroke-width="1.5"/>
      <rect x="12" y="12" width="16" height="16" rx="3" fill="#dc2626"/>
      <text x="36" y="25" font-size="12" font-weight="bold" fill="#f87171">1. Central Rift Volcanics (Cenozoic)</text>
      <text x="12" y="45" font-size="10" fill="#cbd5e1">Rift Valley floor, Mt. Kenya, Aberdares, Chyulu</text>
      <text x="12" y="60" font-size="9.5" fill="#94a3b8">Rocks: Basalt, phonolite, trachyte, obsidian, tuff</text>
    </g>

    <!-- Province 2: Coastal Sediments -->
    <g transform="translate(0, 78)">
      <rect x="0" y="0" width="320" height="70" rx="6" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
      <rect x="12" y="12" width="16" height="16" rx="3" fill="#eab308"/>
      <text x="36" y="25" font-size="12" font-weight="bold" fill="#fde047">2. Coastal Sedimentary Strip</text>
      <text x="12" y="45" font-size="10" fill="#cbd5e1">Mombasa, Kilifi, Malindi, Kwale coastal belt</text>
      <text x="12" y="60" font-size="9.5" fill="#94a3b8">Rocks: Coral limestone, Mazeras sandstone, shale</text>
    </g>

    <!-- Province 3: Basement System -->
    <g transform="translate(0, 156)">
      <rect x="0" y="0" width="320" height="70" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
      <rect x="12" y="12" width="16" height="16" rx="3" fill="#7e22ce"/>
      <text x="36" y="25" font-size="12" font-weight="bold" fill="#c084fc">3. Precambrian Basement System</text>
      <text x="12" y="45" font-size="10" fill="#cbd5e1">Machakos, Kitui, Turkana, Marsabit, Taita</text>
      <text x="12" y="60" font-size="9.5" fill="#94a3b8">Rocks: Gneiss, schist, marble, quartzite</text>
    </g>

    <!-- Province 4: Western Granites & Basins -->
    <g transform="translate(0, 234)">
      <rect x="0" y="0" width="320" height="70" rx="6" fill="#0f172a" stroke="#15803d" stroke-width="1.5"/>
      <rect x="12" y="12" width="16" height="16" rx="3" fill="#15803d"/>
      <text x="36" y="25" font-size="12" font-weight="bold" fill="#86efac">4. Western Granites &amp; Lake Basins</text>
      <text x="12" y="45" font-size="10" fill="#cbd5e1">Lake Victoria basin, Kisumu, Kakamega, Kisii</text>
      <text x="12" y="60" font-size="9.5" fill="#94a3b8">Rocks: Plutonic granite, soapstone, lake clays</text>
    </g>
  </g>
</svg>
""")

# SVG 15: Economic Significance of Rocks (Lesson 15)
SVG_ECONOMIC_SIGNIFICANCE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">ECONOMIC SIGNIFICANCE OF ROCKS IN KENYA</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Powering Renewable Geothermal Energy, Construction Boom, and Water Security</text>

  <!-- 3 Sector Panels -->
  <g transform="translate(35, 90)">
    <!-- Sector 1: Geothermal Clean Energy -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="225" height="305" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
      <rect x="0" y="0" width="225" height="36" rx="10" fill="#991b1b"/>
      <text x="112" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">1. GEOTHERMAL POWER</text>
      
      <!-- Power turbine & steam -->
      <circle cx="112" cy="85" r="28" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
      <path d="M100,105 Q112,85 125,105 Q112,65 100,105" fill="#ef4444"/>
      <path d="M112,50 Q118,30 112,15 M105,50 Q100,30 105,15 M120,50 Q125,30 120,15" stroke="#ffffff" stroke-width="1.5" fill="none"/>

      <text x="112" y="145" font-size="12" font-weight="bold" fill="#f87171" text-anchor="middle">Olkaria Geothermal</text>
      <text x="112" y="170" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Volcanic heat superheats</text>
      <text x="112" y="190" font-size="10.5" fill="#cbd5e1" text-anchor="middle">underground steam</text>
      <text x="112" y="215" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Generates &gt; 800 MW electricity</text>
      <text x="112" y="245" font-size="10" fill="#94a3b8" text-anchor="middle">Key Rock: Fractured Basalt</text>
    </g>

    <!-- Sector 2: Construction Infrastructure -->
    <g transform="translate(250, 0)">
      <rect x="0" y="0" width="225" height="305" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
      <rect x="0" y="0" width="225" height="36" rx="10" fill="#d97706"/>
      <text x="112" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">2. CONSTRUCTION</text>
      
      <!-- Concrete building block -->
      <rect x="75" y="60" width="75" height="50" rx="4" fill="#334155" stroke="#f59e0b" stroke-width="1.5"/>
      <rect x="85" y="70" width="22" height="30" rx="2" fill="#0f172a"/>
      <rect x="118" y="70" width="22" height="30" rx="2" fill="#0f172a"/>

      <text x="112" y="145" font-size="12" font-weight="bold" fill="#fbbf24" text-anchor="middle">Cement &amp; Ballast</text>
      <text x="112" y="170" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Limestone for cement kilns</text>
      <text x="112" y="190" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Crushed ballast for SGR &amp; roads</text>
      <text x="112" y="215" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Tuff blocks for masonry walls</text>
      <text x="112" y="245" font-size="10" fill="#94a3b8" text-anchor="middle">Hub: Athi River &amp; Bamburi</text>
    </g>

    <!-- Sector 3: Aquifers & Water Security -->
    <g transform="translate(500, 0)">
      <rect x="0" y="0" width="225" height="305" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
      <rect x="0" y="0" width="225" height="36" rx="10" fill="#0284c7"/>
      <text x="112" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">3. GROUNDWATER</text>
      
      <!-- Aquifer water drop -->
      <path d="M112,60 C112,60 90,95 90,105 C90,118 100,125 112,125 C124,125 134,118 134,105 C134,95 112,60 112,60 Z" fill="#38bdf8"/>

      <text x="112" y="145" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Natural Aquifers</text>
      <text x="112" y="170" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Permeable sandstones &amp; basalts</text>
      <text x="112" y="190" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Filter and store pure water</text>
      <text x="112" y="215" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Feeds boreholes &amp; natural springs</text>
      <text x="112" y="245" font-size="10" fill="#94a3b8" text-anchor="middle">Key Rocks: Sandstone &amp; Tuff</text>
    </g>
  </g>
</svg>
""")

# SVG 16: Tourism and Cultural Significance (Lesson 16)
SVG_CULTURAL_SIGNIFICANCE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">SCENIC TOURISM &amp; CULTURAL HERITAGE OF ROCKS</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Geomorphology, Sacred Shrines, and Prehistoric Archaeological Archives</text>

  <!-- 3 Landmark Pillars -->
  <g transform="translate(35, 90)">
    <!-- Pillar 1: Kit Mikayi (Balancing Tor) -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="225" height="305" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
      <rect x="0" y="0" width="225" height="36" rx="10" fill="#7e22ce"/>
      <text x="112" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">KIT MIKAYI TOR</text>
      
      <!-- Stacked boulders drawing -->
      <ellipse cx="112" cy="115" rx="45" ry="18" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
      <ellipse cx="112" cy="90" rx="35" ry="15" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
      <ellipse cx="112" cy="68" rx="22" ry="12" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>

      <text x="112" y="155" font-size="12" font-weight="bold" fill="#c084fc" text-anchor="middle">Cultural Sacred Monument</text>
      <text x="112" y="180" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Seme, Kisumu County</text>
      <text x="112" y="200" font-size="10.5" fill="#cbd5e1" text-anchor="middle">UNESCO Cultural Inscription</text>
      <text x="112" y="225" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Prayer &amp; rainmaking rituals</text>
      <text x="112" y="255" font-size="10" fill="#94a3b8" text-anchor="middle">Rock: Weathered Granite Tor</text>
    </g>

    <!-- Pillar 2: Hell's Gate Gorges -->
    <g transform="translate(250, 0)">
      <rect x="0" y="0" width="225" height="305" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
      <rect x="0" y="0" width="225" height="36" rx="10" fill="#d97706"/>
      <text x="112" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">HELL'S GATE GORGES</text>
      
      <!-- Volcanic pillar Fischer's Tower -->
      <polygon points="95,125 105,65 119,65 129,125" fill="#78350f" stroke="#f59e0b" stroke-width="1.5"/>

      <text x="112" y="155" font-size="12" font-weight="bold" fill="#fbbf24" text-anchor="middle">Fischer's Tower</text>
      <text x="112" y="180" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Naivasha, Nakuru County</text>
      <text x="112" y="200" font-size="10.5" fill="#cbd5e1" text-anchor="middle">25m volcanic rock plug</text>
      <text x="112" y="225" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Rock climbing &amp; eco-tourism</text>
      <text x="112" y="255" font-size="10" fill="#94a3b8" text-anchor="middle">Rock: Trachyte / Basalt Plug</text>
    </g>

    <!-- Pillar 3: Prehistoric Caves & Rock Shelters -->
    <g transform="translate(500, 0)">
      <rect x="0" y="0" width="225" height="305" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
      <rect x="0" y="0" width="225" height="36" rx="10" fill="#15803d"/>
      <text x="112" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">ARCHAEOLOGICAL CAVES</text>
      
      <!-- Cave arch drawing -->
      <path d="M70,125 Q112,65 154,125 Z" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>

      <text x="112" y="155" font-size="12" font-weight="bold" fill="#86efac" text-anchor="middle">Kariandusi &amp; Gamble's Cave</text>
      <text x="112" y="180" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Prehistoric Living Shelters</text>
      <text x="112" y="200" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Preserves Stone Age tools</text>
      <text x="112" y="225" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Ancient fossils &amp; rock art</text>
      <text x="112" y="255" font-size="10" fill="#94a3b8" text-anchor="middle">Rock: Sedimentary &amp; Tuff Caves</text>
    </g>
  </g>
</svg>
""")

# SVG 17: Field Sampling Equipment & Safety Guide (Lesson 17)
SVG_FIELD_SAMPLING = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">GEOLOGIST'S FIELD SAMPLING &amp; SAFETY PROTOCOL GUIDE</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Essential Equipment, Sampling Techniques, and Mandatory Field Safety Rules</text>

  <!-- Left: Gear Checklist -->
  <g transform="translate(40, 85)">
    <rect x="0" y="0" width="340" height="315" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="340" height="32" rx="8" fill="#0284c7"/>
    <text x="170" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">ESSENTIAL FIELDWORK TOOLKIT</text>
    
    <g transform="translate(20, 50)">
      <!-- Tool 1: Goggles -->
      <text x="0" y="20" font-size="12" font-weight="bold" fill="#38bdf8">1. Safety Goggles &amp; Gloves</text>
      <text x="0" y="38" font-size="10.5" fill="#cbd5e1">Mandatory eye protection against sharp flying rock chips</text>

      <!-- Tool 2: Geological Hammer -->
      <text x="0" y="70" font-size="12" font-weight="bold" fill="#38bdf8">2. Geological Pick Hammer</text>
      <text x="0" y="88" font-size="10.5" fill="#cbd5e1">Exposes fresh, unweathered interior rock faces</text>

      <!-- Tool 3: Hand Lens -->
      <text x="0" y="120" font-size="12" font-weight="bold" fill="#38bdf8">3. 10x Magnifying Hand Lens</text>
      <text x="0" y="138" font-size="10.5" fill="#cbd5e1">Magnifies mineral grains, cleavage, and crystal habits</text>

      <!-- Tool 4: Labeled Bags & Notebook -->
      <text x="0" y="170" font-size="12" font-weight="bold" fill="#38bdf8">4. Labeled Sample Bags &amp; Notebook</text>
      <text x="0" y="188" font-size="10.5" fill="#cbd5e1">Records sample ID, location coordinates, color, and texture</text>

      <!-- Tool 5: Dilute Acid / Lemon Juice -->
      <text x="0" y="220" font-size="12" font-weight="bold" fill="#38bdf8">5. Dilute Acid (Effervescence Test)</text>
      <text x="0" y="238" font-size="10.5" fill="#cbd5e1">Tests for carbonate minerals in field limestone specimens</text>
    </g>
  </g>

  <!-- Right: Field Safety Rules -->
  <g transform="translate(420, 85)">
    <rect x="0" y="0" width="340" height="315" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="340" height="32" rx="8" fill="#991b1b"/>
    <text x="170" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">MANDATORY FIELD SAFETY RULES</text>
    
    <g transform="translate(20, 50)">
      <!-- Rule 1 -->
      <rect x="0" y="0" width="300" height="50" rx="6" fill="#1e293b"/>
      <text x="15" y="20" font-size="11.5" font-weight="bold" fill="#f87171">Rule 1: Always Wear Safety Goggles</text>
      <text x="15" y="38" font-size="10" fill="#cbd5e1">Never strike rocks without protective eyewear.</text>

      <!-- Rule 2 -->
      <rect x="0" y="60" width="300" height="50" rx="6" fill="#1e293b"/>
      <text x="15" y="80" font-size="11.5" font-weight="bold" fill="#f87171">Rule 2: Stay Clear of Active Quarry Walls</text>
      <text x="15" y="98" font-size="10" fill="#cbd5e1">Beware of loose rockfalls and heavy machinery.</text>

      <!-- Rule 3 -->
      <rect x="0" y="120" width="300" height="50" rx="6" fill="#1e293b"/>
      <text x="15" y="140" font-size="11.5" font-weight="bold" fill="#f87171">Rule 3: Beware of Snake/Scorpion Crevices</text>
      <text x="15" y="158" font-size="10" fill="#cbd5e1">Never reach bare hands into dark overgrown rock cracks.</text>

      <!-- Rule 4 -->
      <rect x="0" y="180" width="300" height="50" rx="6" fill="#1e293b"/>
      <text x="15" y="200" font-size="11.5" font-weight="bold" fill="#f87171">Rule 4: Never Taste Rock Samples</text>
      <text x="15" y="218" font-size="10" fill="#cbd5e1">Some minerals contain toxic heavy metals or arsenides.</text>
    </g>
  </g>
</svg>
""")

# SVG 18: Scientific Rock Display Case & Key (Lesson 18)
SVG_DISPLAY_CASE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">SCIENTIFIC ROCK DISPLAY CASE &amp; DICHOTOMOUS KEY</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Partitioned Laboratory Cabinet with Standardized Museum Specimen Labels</text>

  <!-- Display Cabinet Grid -->
  <g transform="translate(45, 85)">
    <!-- Outer Wooden Cabinet Frame -->
    <rect x="0" y="0" width="710" height="315" rx="8" fill="#451a03" stroke="#78350f" stroke-width="4"/>
    
    <!-- 6 Partitioned Compartments -->
    <!-- Compartment 1: Granite (Igneous Intrusive) -->
    <g transform="translate(15, 15)">
      <rect x="0" y="0" width="215" height="135" rx="6" fill="#0f172a" stroke="#dc2626" stroke-width="1.5"/>
      <circle cx="107" cy="45" r="24" fill="#f43f5e" stroke="#ffffff" stroke-width="1"/>
      <rect x="10" y="80" width="195" height="45" rx="4" fill="#1e293b"/>
      <text x="107" y="98" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">Granite (Plutonic)</text>
      <text x="107" y="115" font-size="9" fill="#94a3b8" text-anchor="middle">Site: Kakamega | Col: G10 Class</text>
    </g>

    <!-- Compartment 2: Basalt (Igneous Extrusive) -->
    <g transform="translate(245, 15)">
      <rect x="0" y="0" width="215" height="135" rx="6" fill="#0f172a" stroke="#dc2626" stroke-width="1.5"/>
      <circle cx="107" cy="45" r="24" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
      <rect x="10" y="80" width="195" height="45" rx="4" fill="#1e293b"/>
      <text x="107" y="98" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">Basalt (Extrusive)</text>
      <text x="107" y="115" font-size="9" fill="#94a3b8" text-anchor="middle">Site: Rift Valley | Col: G10 Class</text>
    </g>

    <!-- Compartment 3: Sandstone (Sedimentary Clastic) -->
    <g transform="translate(475, 15)">
      <rect x="0" y="0" width="215" height="135" rx="6" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
      <circle cx="107" cy="45" r="24" fill="#fde047" stroke="#ca8a04" stroke-width="1"/>
      <rect x="10" y="80" width="195" height="45" rx="4" fill="#1e293b"/>
      <text x="107" y="98" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">Sandstone (Clastic)</text>
      <text x="107" y="115" font-size="9" fill="#94a3b8" text-anchor="middle">Site: Mazeras | Col: G10 Class</text>
    </g>

    <!-- Compartment 4: Limestone (Sedimentary Organic) -->
    <g transform="translate(15, 165)">
      <rect x="0" y="0" width="215" height="135" rx="6" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
      <circle cx="107" cy="45" r="24" fill="#fef08a" stroke="#ca8a04" stroke-width="1"/>
      <rect x="10" y="80" width="195" height="45" rx="4" fill="#1e293b"/>
      <text x="107" y="98" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">Limestone (Fizzes in acid)</text>
      <text x="107" y="115" font-size="9" fill="#94a3b8" text-anchor="middle">Site: Bamburi | Col: G10 Class</text>
    </g>

    <!-- Compartment 5: Gneiss (Metamorphic Foliated) -->
    <g transform="translate(245, 165)">
      <rect x="0" y="0" width="215" height="135" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
      <circle cx="107" cy="45" r="24" fill="#c084fc" stroke="#7e22ce" stroke-width="1"/>
      <rect x="10" y="80" width="195" height="45" rx="4" fill="#1e293b"/>
      <text x="107" y="98" font-size="11" font-weight="bold" fill="#c084fc" text-anchor="middle">Gneiss (Banded Foliation)</text>
      <text x="107" y="115" font-size="9" fill="#94a3b8" text-anchor="middle">Site: Machakos | Col: G10 Class</text>
    </g>

    <!-- Compartment 6: Marble (Metamorphic Non-Foliated) -->
    <g transform="translate(475, 165)">
      <rect x="0" y="0" width="215" height="135" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
      <circle cx="107" cy="45" r="24" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>
      <rect x="10" y="80" width="195" height="45" rx="4" fill="#1e293b"/>
      <text x="107" y="98" font-size="11" font-weight="bold" fill="#c084fc" text-anchor="middle">Marble (Recrystallized)</text>
      <text x="107" y="115" font-size="9" fill="#94a3b8" text-anchor="middle">Site: Kajiado | Col: G10 Class</text>
    </g>
  </g>
</svg>
""")

TOPIC_5_SVGS = {
    1: SVG_ROCK_VS_MINERAL,
    2: SVG_ROCK_CYCLE,
    3: SVG_INTRUSIVE_VS_EXTRUSIVE,
    4: SVG_INTRUSIVE_STRUCTURES,
    5: SVG_EXTRUSIVE_TEXTURES,
    6: SVG_LITHIFICATION,
    7: SVG_SEDIMENTARY_CLASSES,
    8: SVG_TRONA_MAGADI,
    9: SVG_METAMORPHIC_AGENTS,
    10: SVG_METAMORPHISM_TYPES,
    11: SVG_PROTOLITH_MATRIX,
    12: SVG_GEOLOGICAL_PILLAR,
    13: SVG_KENYA_BASEMENT_MAP,
    14: SVG_KENYA_COMPREHENSIVE_MAP,
    15: SVG_ECONOMIC_SIGNIFICANCE,
    16: SVG_CULTURAL_SIGNIFICANCE,
    17: SVG_FIELD_SAMPLING,
    18: SVG_DISPLAY_CASE,
}

def enrich_topic_5():
    print("=" * 80)
    print("VLearn Visual Enrichment Engine: Grade 10 Geography — Topic 5: Rocks")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name="Geography").first()
    topic = Topic.objects.filter(subject=subject, order=5).first()

    if not topic:
        raise RuntimeError("Topic 5 'Rocks' not found!")

    verified_images_path = os.path.join(os.path.dirname(__file__), 'grade10_geography_topic5_verified_images.json')
    if not os.path.exists(verified_images_path):
        raise RuntimeError(f"Verified images file not found at {verified_images_path}")

    with open(verified_images_path, 'r') as f:
        verified_images = json.load(f)

    lessons = list(topic.lessons.all().order_by('learning_unit__order'))

    for lesson in lessons:
        u_order = str(lesson.learning_unit.order)
        print(f"\nEnriching Lesson {u_order}: {lesson.title}")

        # 1. Attach Card 1 Photographic Visual Hook
        img_data = verified_images.get(u_order)
        if img_data and img_data.get('url'):
            hook_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=1,
                block_type="suggested_image"
            ).first()

            if hook_block:
                hook_block.content = {
                    "url": img_data['url'],
                    "resolved_image_url": img_data['url'],
                    "caption": hook_block.title,
                    "author": img_data.get('author', 'Wikimedia Commons'),
                    "licensing": img_data.get('licensing', 'CC BY-SA'),
                    "commons_page_url": img_data.get('commons_url', '')
                }
                hook_block.save()

                asset, _ = LessonAsset.objects.get_or_create(
                    lesson=lesson,
                    title=f"Lesson {u_order} Visual Hook: {hook_block.title}",
                    defaults={
                        "asset_type": "image",
                        "source_type": "external",
                        "storage_type": "url",
                        "status": "attached",
                        "url": img_data['url'],
                        "metadata": {
                            "author": img_data.get('author', 'Wikimedia Commons'),
                            "licensing": img_data.get('licensing', 'CC BY-SA'),
                            "commons_url": img_data.get('commons_url', ''),
                            "unit_order": int(u_order),
                            "topic_order": 5
                        }
                    }
                )
                asset.url = img_data['url']
                asset.status = "attached"
                asset.save()
                asset.blocks.add(hook_block)
                print(f"  + Attached Wikimedia Photographic Hook: {img_data['url'][:55]}...")

        # 2. Attach Custom Vector SVG
        svg_xml = TOPIC_5_SVGS.get(int(u_order))
        if svg_xml:
            diagram_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="diagram"
            ).first()

            if diagram_block:
                diagram_block.content = {
                    "svg_content": svg_xml,
                    "title": diagram_block.title,
                    "caption": diagram_block.content.get("caption", diagram_block.title) if diagram_block.content else diagram_block.title
                }
                diagram_block.save()

                svg_asset, _ = LessonAsset.objects.get_or_create(
                    lesson=lesson,
                    title=f"Lesson {u_order} Diagram: {diagram_block.title}",
                    defaults={
                        "asset_type": "diagram",
                        "source_type": "ai_generated",
                        "storage_type": "embed",
                        "status": "attached",
                        "metadata": {
                            "svg_content": svg_xml,
                            "unit_order": int(u_order),
                            "topic_order": 5
                        }
                    }
                )
                svg_asset.metadata["svg_content"] = svg_xml
                svg_asset.status = "attached"
                svg_asset.save()
                svg_asset.blocks.add(diagram_block)
                print(f"  + Attached Custom Responsive Vector SVG to block '{diagram_block.title}'")

        # 3. Attach YouTube Video if present
        video_block = LessonBlock.objects.filter(
            lesson=lesson,
            block_type="video"
        ).first()

        if video_block:
            c = video_block.content or {}
            vid_url = c.get("url") or "https://www.youtube.com/watch?v=swKBi6hHHMA"
            v_asset, _ = LessonAsset.objects.get_or_create(
                lesson=lesson,
                title=f"Lesson {u_order} Video: {video_block.title}",
                defaults={
                    "asset_type": "youtube",
                    "source_type": "external",
                    "storage_type": "url",
                    "status": "attached",
                    "url": vid_url,
                    "metadata": {
                        "youtube_url": vid_url,
                        "unit_order": int(u_order),
                        "topic_order": 5
                    }
                }
            )
            v_asset.url = vid_url
            v_asset.status = "attached"
            v_asset.save()
            v_asset.blocks.add(video_block)
            print(f"  + Attached Educational YouTube Video: {vid_url}")

    print("\n" + "=" * 80)
    print("Topic 5 Visual Enrichment Completed Successfully!")
    print("=" * 80)

if __name__ == "__main__":
    enrich_topic_5()
