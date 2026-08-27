"""
VLearn CBC Grade 10 Geography — Topic 6: Earth Movements
Visual Enrichment Engine (Vector SVGs, Verified Wikimedia Images & Educational Videos)

Subject: Geography (Grade 10 CBC, Subject ID: 37)
Topic 6: Earth Movements

Attaches:
  - 6 First-Card Photographic Visual Hooks (100% Tested HTTP 200 OK Direct Wikimedia URLs)
  - 6 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - Educational YouTube Video for Mantle Convection & Tectonic Plates
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade10_geography_topic6.py
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
# 6 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 6: EARTH MOVEMENTS
# =============================================================================

# SVG 1: Endogenic vs Exogenic Forces Dynamic (Lesson 1)
SVG_FORCES_DYNAMIC = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">ENDOGENIC VS. EXOGENIC FORCE DYNAMIC</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Internal Constructional Forces vs. External Denudation &amp; Leveling Processes</text>

  <!-- Left Panel: Endogenic Forces -->
  <g transform="translate(35, 85)">
    <rect x="0" y="0" width="345" height="330" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="36" rx="10" fill="#b91c1c"/>
    <text x="172" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">1. ENDOGENIC (INTERNAL) FORCES</text>

    <!-- Mountain Peak Rising -->
    <path d="M 40 210 L 120 100 L 190 210 Z" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
    <path d="M 100 128 L 120 100 L 140 128 Z" fill="#ffffff"/>
    <path d="M 160 210 L 230 120 L 300 210 Z" fill="#334155" stroke="#64748b" stroke-width="1.5"/>

    <!-- Upward Forces / Magma Arrows -->
    <polygon points="120,240 110,260 116,260 116,280 124,280 124,260 130,260" fill="#f87171"/>
    <polygon points="230,240 220,260 226,260 226,280 234,280 234,260 240,260" fill="#f87171"/>
    <text x="172" y="275" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">Geothermal Heat &amp; Magma Uplift</text>

    <!-- Crustal base -->
    <rect x="20" y="210" width="305" height="15" fill="#78350f" rx="3"/>

    <!-- Key Bullet Points -->
    <text x="30" y="295" font-size="10.5" font-weight="bold" fill="#fca5a5">• Constructional Processes:</text>
    <text x="40" y="310" font-size="9.5" fill="#cbd5e1">- Orogenesis (Horizontal Folding &amp; Mountain Building)</text>
    <text x="40" y="323" font-size="9.5" fill="#cbd5e1">- Epeirogenesis (Broad Vertical Uplift &amp; Subsidence)</text>
  </g>

  <!-- Right Panel: Exogenic Forces -->
  <g transform="translate(420, 85)">
    <rect x="0" y="0" width="345" height="330" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="36" rx="10" fill="#0284c7"/>
    <text x="172" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">2. EXOGENIC (EXTERNAL) FORCES</text>

    <!-- Sun & Rain Clouds -->
    <circle cx="60" cy="70" r="16" fill="#f59e0b"/>
    <path d="M 230 65 Q 245 50 265 60 Q 285 50 295 65 Q 305 75 295 90 L 235 90 Q 220 80 230 65 Z" fill="#94a3b8"/>
    <!-- Rain lines -->
    <line x1="245" y1="95" x2="240" y2="110" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="2,2"/>
    <line x1="265" y1="95" x2="260" y2="110" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="2,2"/>
    <line x1="285" y1="95" x2="280" y2="110" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="2,2"/>

    <!-- Eroding Mountain Slope & River -->
    <path d="M 40 210 Q 120 140 180 180 T 310 210" fill="none" stroke="#64748b" stroke-width="2"/>
    <path d="M 120 160 Q 180 190 280 210" fill="none" stroke="#38bdf8" stroke-width="3"/>
    
    <!-- Leveling Arrows (Downwards) -->
    <polygon points="120,135 115,120 125,120" fill="#38bdf8"/>
    <line x1="120" y1="105" x2="120" y2="125" stroke="#38bdf8" stroke-width="2"/>
    <text x="172" y="135" font-size="10" font-weight="bold" fill="#38bdf8">Erosion &amp; Weathering</text>

    <!-- Deposition Basin -->
    <rect x="250" y="200" width="65" height="15" fill="#fef08a" rx="2"/>
    <text x="282" y="212" font-size="8.5" font-weight="bold" fill="#78350f" text-anchor="middle">Sediment</text>

    <!-- Crustal base -->
    <rect x="20" y="215" width="305" height="10" fill="#78350f" rx="3"/>

    <!-- Key Bullet Points -->
    <text x="30" y="250" font-size="10.5" font-weight="bold" fill="#7dd3fc">• Denudation &amp; Leveling Processes:</text>
    <text x="40" y="266" font-size="9.5" fill="#cbd5e1">- Weathering (In situ rock breakdown)</text>
    <text x="40" y="280" font-size="9.5" fill="#cbd5e1">- Erosion (Removal &amp; transport by water/wind)</text>
    <text x="40" y="294" font-size="9.5" fill="#cbd5e1">- Mass Wasting (Downslope gravity creep/slides)</text>
    <text x="40" y="308" font-size="9.5" fill="#cbd5e1">- Deposition (Sediment accumulation in basins)</text>
  </g>
</svg>
""")

# SVG 2: Tectonic Plate Driving Forces (Lesson 2)
SVG_MANTLE_CONVECTION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">TECTONIC PLATE DRIVING MECHANISMS</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Mantle Convection Cells, Mid-Ocean Ridge Push, and Subduction Trench Slab Pull</text>

  <!-- Asthenosphere / Mantle Region -->
  <rect x="40" y="140" width="720" height="230" fill="#7f1d1d" rx="6"/>
  <text x="400" y="260" font-size="16" font-weight="bold" fill="#fca5a5" fill-opacity="0.3" text-anchor="middle">SEMI-PLASTIC ASTHENOSPHERE / MANTLE</text>

  <!-- Core Boundary at bottom -->
  <rect x="40" y="370" width="720" height="45" fill="#e11d48" rx="4"/>
  <text x="400" y="398" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">HOT EARTH CORE (Radioactive Decay &amp; Primordial Heat Engine)</text>

  <!-- Left Convection Cell -->
  <g transform="translate(220, 250)">
    <circle cx="0" cy="0" r="55" fill="none" stroke="#f87171" stroke-width="4" stroke-dasharray="8,5"/>
    <!-- Arrows on circle (Clockwise) -->
    <polygon points="55,-5 63,-5 55,-20" fill="#fca5a5"/>
    <polygon points="-55,5 -63,5 -55,20" fill="#fca5a5"/>
    <text x="0" y="5" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Convection</text>
    <text x="0" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Cell A</text>
  </g>

  <!-- Right Convection Cell -->
  <g transform="translate(480, 250)">
    <circle cx="0" cy="0" r="55" fill="none" stroke="#f87171" stroke-width="4" stroke-dasharray="8,5"/>
    <!-- Arrows on circle (Counter-Clockwise) -->
    <polygon points="-55,-5 -63,-5 -55,-20" fill="#fca5a5"/>
    <polygon points="55,5 63,5 55,20" fill="#fca5a5"/>
    <text x="0" y="5" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Convection</text>
    <text x="0" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Cell B</text>
  </g>

  <!-- Rising Magma Plume / Mid-Ocean Ridge in Center -->
  <path d="M 320 370 Q 350 200 350 120 L 370 120 Q 370 200 400 370 Z" fill="#ef4444" opacity="0.85"/>
  <polygon points="360,105 348,125 372,125" fill="#fbbf24"/>
  <text x="360" y="98" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">RIDGE PUSH</text>

  <!-- Continental & Oceanic Plates -->
  <!-- Left Plate moving left -->
  <rect x="80" y="115" width="260" height="25" fill="#334155" stroke="#64748b" stroke-width="2" rx="3"/>
  <text x="210" y="132" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Tectonic Plate 1 (&lt;-- Divergence)</text>
  <polygon points="120,100 100,100 110,90" fill="#38bdf8"/>
  <line x1="100" y1="100" x2="160" y2="100" stroke="#38bdf8" stroke-width="2"/>

  <!-- Right Plate moving right and subducting -->
  <path d="M 380 115 L 620 115 L 680 240 L 655 250 L 605 140 L 380 140 Z" fill="#1e293b" stroke="#0284c7" stroke-width="2"/>
  <text x="500" y="132" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Oceanic Plate 2 (--&gt; Subduction)</text>
  
  <!-- Slab Pull annotation -->
  <g transform="translate(685, 230)">
    <polygon points="15,25 0,15 10,10" fill="#22c55e"/>
    <text x="25" y="15" font-size="11" font-weight="bold" fill="#4ade80">SLAB PULL</text>
    <text x="25" y="30" font-size="9" fill="#cbd5e1">Cold dense slab</text>
    <text x="25" y="42" font-size="9" fill="#cbd5e1">sinks into mantle</text>
  </g>
</svg>
""")

# SVG 3: Horizontal vs Vertical Crustal Movements (Lesson 3)
SVG_CRUSTAL_STRESSES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">TYPES OF CRUSTAL MOVEMENTS &amp; STRESSES</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Horizontal Orogenesis (Tension &amp; Compression) vs. Vertical Epeirogenesis</text>

  <!-- Panel 1: Tensional Stress (Left) -->
  <g transform="translate(35, 85)">
    <rect x="0" y="0" width="225" height="330" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="225" height="32" rx="10" fill="#d97706"/>
    <text x="112" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. TENSION (OROGENIC)</text>

    <!-- Pulling Arrows -->
    <polygon points="25,60 40,50 40,70" fill="#f59e0b"/>
    <line x1="40" y1="60" x2="80" y2="60" stroke="#f59e0b" stroke-width="3"/>
    <polygon points="200,60 185,50 185,70" fill="#f59e0b"/>
    <line x1="185" y1="60" x2="145" y2="60" stroke="#f59e0b" stroke-width="3"/>
    <text x="112" y="65" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">PULLING APART</text>

    <!-- Fracturing Block -->
    <g transform="translate(25, 90)">
      <polygon points="0,0 80,0 60,80 0,80" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
      <polygon points="95,0 175,0 175,80 75,80" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
      <line x1="80" y1="0" x2="60" y2="80" stroke="#ef4444" stroke-width="2" stroke-dasharray="3,3"/>
      <text x="68" y="45" font-size="9" fill="#ef4444" font-weight="bold">Fault</text>
    </g>

    <!-- Key Landforms -->
    <text x="15" y="205" font-size="10.5" font-weight="bold" fill="#fbbf24">• Resulting Landforms:</text>
    <text x="25" y="223" font-size="9.5" fill="#cbd5e1">- Fault Scarps &amp; Fractures</text>
    <text x="25" y="238" font-size="9.5" fill="#cbd5e1">- Rift Valleys (Grabens)</text>
    <text x="25" y="253" font-size="9.5" fill="#cbd5e1">- Block Mountains (Horsts)</text>
    <text x="15" y="280" font-size="9.5" font-weight="bold" fill="#94a3b8">Example: Kerio Escarpment</text>
  </g>

  <!-- Panel 2: Compressional Stress (Center) -->
  <g transform="translate(285, 85)">
    <rect x="0" y="0" width="225" height="330" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="225" height="32" rx="10" fill="#b91c1c"/>
    <text x="112" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. COMPRESSION (OROGENIC)</text>

    <!-- Pushing Arrows -->
    <polygon points="75,60 60,50 60,70" fill="#ef4444"/>
    <line x1="25" y1="60" x2="60" y2="60" stroke="#ef4444" stroke-width="3"/>
    <polygon points="150,60 165,50 165,70" fill="#ef4444"/>
    <line x1="200" y1="60" x2="165" y2="60" stroke="#ef4444" stroke-width="3"/>
    <text x="112" y="65" font-size="10" font-weight="bold" fill="#fca5a5" text-anchor="middle">SQUEEZING IN</text>

    <!-- Folded Strata -->
    <g transform="translate(25, 90)">
      <path d="M 0 50 Q 40 10 85 50 T 175 50" fill="none" stroke="#38bdf8" stroke-width="5"/>
      <path d="M 0 65 Q 40 25 85 65 T 175 65" fill="none" stroke="#22c55e" stroke-width="5"/>
      <path d="M 0 80 Q 40 40 85 80 T 175 80" fill="none" stroke="#eab308" stroke-width="5"/>
      <text x="45" y="15" font-size="8.5" fill="#38bdf8" font-weight="bold">Anticline (Crest)</text>
      <text x="130" y="80" font-size="8.5" fill="#eab308" font-weight="bold">Syncline (Trough)</text>
    </g>

    <!-- Key Landforms -->
    <text x="15" y="205" font-size="10.5" font-weight="bold" fill="#fca5a5">• Resulting Landforms:</text>
    <text x="25" y="223" font-size="9.5" fill="#cbd5e1">- Fold Mountain Belts</text>
    <text x="25" y="238" font-size="9.5" fill="#cbd5e1">- Anticlines &amp; Synclines</text>
    <text x="25" y="253" font-size="9.5" fill="#cbd5e1">- Overthrust Nappes</text>
    <text x="15" y="280" font-size="9.5" font-weight="bold" fill="#94a3b8">Example: Himalayas, Atlas</text>
  </g>

  <!-- Panel 3: Vertical Movements (Right) -->
  <g transform="translate(535, 85)">
    <rect x="0" y="0" width="230" height="330" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="32" rx="10" fill="#15803d"/>
    <text x="115" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. VERTICAL (EPEIROGENIC)</text>

    <!-- Up/Down Arrows -->
    <polygon points="60,45 50,55 70,55" fill="#22c55e"/>
    <line x1="60" y1="55" x2="60" y2="75" stroke="#22c55e" stroke-width="2"/>
    <text x="60" y="87" font-size="8.5" fill="#4ade80" font-weight="bold" text-anchor="middle">Uplift</text>

    <polygon points="170,75 160,65 180,65" fill="#38bdf8"/>
    <line x1="170" y1="45" x2="170" y2="65" stroke="#38bdf8" stroke-width="2"/>
    <text x="170" y="87" font-size="8.5" fill="#38bdf8" font-weight="bold" text-anchor="middle">Subsidence</text>

    <!-- Broad Plateau / Basin Block -->
    <g transform="translate(20, 100)">
      <!-- Plateau -->
      <polygon points="0,30 75,30 75,70 0,70" fill="#334155" stroke="#22c55e" stroke-width="1.5"/>
      <text x="37" y="52" font-size="8" fill="#ffffff" font-weight="bold" text-anchor="middle">Plateau</text>
      <!-- Basin -->
      <polygon points="115,50 190,50 190,70 115,70" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="152" y="62" font-size="8" fill="#ffffff" font-weight="bold" text-anchor="middle">Basin</text>
    </g>

    <!-- Key Landforms -->
    <text x="15" y="205" font-size="10.5" font-weight="bold" fill="#86efac">• Resulting Landforms:</text>
    <text x="25" y="223" font-size="9.5" fill="#cbd5e1">- Elevated Flat Plateaus</text>
    <text x="25" y="238" font-size="9.5" fill="#cbd5e1">- Coastal Emergence (Cliffs)</text>
    <text x="25" y="253" font-size="9.5" fill="#cbd5e1">- Downwarped Crustal Basins</text>
    <text x="15" y="280" font-size="9.5" font-weight="bold" fill="#94a3b8">Example: Yatta Plateau, Lake Victoria</text>
  </g>
</svg>
""")

# SVG 4: Elastic Rebound Theory (Lesson 4)
SVG_ELASTIC_REBOUND = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">ELASTIC REBOUND THEORY &amp; SEISMIC RELEASE</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">How Centuries of Slow Tectonic Strain Discharge in Seconds of Rapid Earthquake Motion</text>

  <!-- Stage 1: Unstressed Original State -->
  <g transform="translate(40, 95)">
    <rect x="0" y="0" width="220" height="300" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="34" rx="10" fill="#0284c7"/>
    <text x="110" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 1: UNSTRESSED</text>

    <!-- Block with straight reference line -->
    <rect x="25" y="60" width="80" height="110" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
    <rect x="115" y="60" width="80" height="110" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
    <line x1="105" y1="50" x2="105" y2="180" stroke="#ef4444" stroke-width="2" stroke-dasharray="3,3"/>
    <text x="105" y="45" font-size="9" fill="#ef4444" font-weight="bold" text-anchor="middle">Fault Plane</text>
    
    <!-- Straight line across -->
    <line x1="25" y1="115" x2="195" y2="115" stroke="#22c55e" stroke-width="3"/>
    <circle cx="65" cy="115" r="4" fill="#22c55e"/>
    <circle cx="155" cy="115" r="4" fill="#22c55e"/>
    <text x="110" y="135" font-size="9" fill="#86efac" text-anchor="middle">Straight Reference Line</text>

    <text x="110" y="210" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Frictional Equilibrium</text>
    <text x="110" y="230" font-size="9.5" fill="#cbd5e1" text-anchor="middle">No accumulated shear stress.</text>
    <text x="110" y="245" font-size="9.5" fill="#cbd5e1" text-anchor="middle">Rocks in relaxed state.</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <polygon points="268,245 288,245 288,240 298,250 288,260 288,255 268,255" fill="#f59e0b"/>

  <!-- Stage 2: Strain Accumulation -->
  <g transform="translate(290, 95)">
    <rect x="0" y="0" width="220" height="300" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="34" rx="10" fill="#d97706"/>
    <text x="110" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 2: ELASTIC STRAIN</text>

    <!-- Block flexing elastically under friction lock -->
    <g transform="translate(25, 60)">
      <polygon points="0,0 80,10 80,120 0,110" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
      <polygon points="90,10 170,0 170,110 90,120" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
      <!-- Curved bent line -->
      <path d="M 0 55 Q 60 65 80 75" fill="none" stroke="#f59e0b" stroke-width="3"/>
      <path d="M 90 45 Q 110 55 170 65" fill="none" stroke="#f59e0b" stroke-width="3"/>
      <line x1="85" y1="0" x2="85" y2="130" stroke="#ef4444" stroke-width="2" stroke-dasharray="3,3"/>
      <!-- Stress arrows -->
      <polygon points="20,15 10,25 30,25" fill="#f59e0b"/>
      <polygon points="150,105 160,95 140,95" fill="#f59e0b"/>
    </g>

    <text x="110" y="210" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">Friction-Locked Fault</text>
    <text x="110" y="230" font-size="9.5" fill="#cbd5e1" text-anchor="middle">Slow drift (cm/yr) bends rock</text>
    <text x="110" y="245" font-size="9.5" fill="#cbd5e1" text-anchor="middle">Storing massive elastic strain.</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <polygon points="518,245 538,245 538,240 548,250 538,260 538,255 518,255" fill="#ef4444"/>

  <!-- Stage 3: Rupture & Earthquake -->
  <g transform="translate(540, 95)">
    <rect x="0" y="0" width="220" height="300" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="34" rx="10" fill="#b91c1c"/>
    <text x="110" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 3: SUDDEN RUPTURE</text>

    <!-- Displaced offset blocks with radiating waves -->
    <g transform="translate(25, 60)">
      <rect x="0" y="0" width="80" height="110" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
      <rect x="90" y="20" width="80" height="110" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
      <!-- Offset straight lines -->
      <line x1="0" y1="55" x2="80" y2="55" stroke="#22c55e" stroke-width="3"/>
      <line x1="90" y1="75" x2="170" y2="75" stroke="#22c55e" stroke-width="3"/>
      <line x1="85" y1="0" x2="85" y2="135" stroke="#ef4444" stroke-width="2"/>
      <!-- Radiating seismic circles -->
      <circle cx="85" cy="65" r="12" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="2,2"/>
      <circle cx="85" cy="65" r="24" fill="none" stroke="#f87171" stroke-width="1.5" stroke-dasharray="3,3"/>
      <circle cx="85" cy="65" r="36" fill="none" stroke="#fca5a5" stroke-width="1.5" stroke-dasharray="4,4"/>
    </g>

    <text x="110" y="210" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">Rapid Seismic Discharge</text>
    <text x="110" y="230" font-size="9.5" fill="#cbd5e1" text-anchor="middle">Frictional lock breaks in seconds.</text>
    <text x="110" y="245" font-size="9.5" fill="#cbd5e1" text-anchor="middle">Stored energy radiates as waves!</text>
  </g>
</svg>
""")

# SVG 5: Three Fault Types and Crustal Blocks (Lesson 5)
SVG_FAULT_TYPES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="42" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">THREE PRIMARY FAULT TYPES &amp; CRUSTAL BLOCKS</text>
  <text x="400" y="60" font-size="11" fill="#94a3b8" text-anchor="middle">Structural Displacement Governed by Tectonic Tension, Compression, and Shear Stresses</text>

  <!-- Panel 1: Normal Fault (Tension) -->
  <g transform="translate(30, 75)">
    <rect x="0" y="0" width="230" height="195" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="115" y="20" font-size="11.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. NORMAL FAULT (Tension)</text>
    
    <!-- Block Diagram -->
    <g transform="translate(25, 35)">
      <!-- Footwall (Left, higher) -->
      <polygon points="0,15 80,15 50,110 0,110" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
      <text x="30" y="70" font-size="9" fill="#ffffff" font-weight="bold">Footwall</text>
      <!-- Hanging Wall (Right, dropped) -->
      <polygon points="90,45 170,45 170,110 60,110" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
      <text x="125" y="85" font-size="9" fill="#ffffff" font-weight="bold">Hanging Wall</text>
      <!-- Fault Scarp highlight -->
      <line x1="80" y1="15" x2="90" y2="45" stroke="#ef4444" stroke-width="3"/>
      <!-- Pulling arrows -->
      <polygon points="10,5 0,10 0,0" fill="#38bdf8"/>
      <polygon points="160,5 170,10 170,0" fill="#38bdf8"/>
    </g>
    <text x="115" y="165" font-size="9.5" fill="#cbd5e1" text-anchor="middle">Hanging wall drops relative to footwall</text>
    <text x="115" y="180" font-size="9" font-weight="bold" fill="#f87171" text-anchor="middle">Creates: Rift Valleys &amp; Escarpments</text>
  </g>

  <!-- Panel 2: Reverse Fault (Compression) -->
  <g transform="translate(285, 75)">
    <rect x="0" y="0" width="230" height="195" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="115" y="20" font-size="11.5" font-weight="bold" fill="#f87171" text-anchor="middle">2. REVERSE FAULT (Compression)</text>
    
    <!-- Block Diagram -->
    <g transform="translate(25, 35)">
      <!-- Footwall (Left, lower) -->
      <polygon points="0,45 80,45 50,110 0,110" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
      <text x="25" y="85" font-size="9" fill="#ffffff" font-weight="bold">Footwall</text>
      <!-- Hanging Wall (Right, pushed UP) -->
      <polygon points="90,15 170,15 170,110 60,110" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
      <text x="115" y="65" font-size="9" fill="#ffffff" font-weight="bold">Hanging Wall</text>
      <!-- Fault Scarp -->
      <line x1="90" y1="15" x2="80" y2="45" stroke="#ef4444" stroke-width="3"/>
      <!-- Pushing arrows -->
      <polygon points="20,5 30,0 30,10" fill="#ef4444"/>
      <polygon points="150,5 140,0 140,10" fill="#ef4444"/>
    </g>
    <text x="115" y="165" font-size="9.5" fill="#cbd5e1" text-anchor="middle">Hanging wall pushed UP over footwall</text>
    <text x="115" y="180" font-size="9" font-weight="bold" fill="#fca5a5" text-anchor="middle">Creates: Crustal Shortening &amp; Thrusts</text>
  </g>

  <!-- Panel 3: Strike-Slip Fault (Shear) -->
  <g transform="translate(540, 75)">
    <rect x="0" y="0" width="230" height="195" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="115" y="20" font-size="11.5" font-weight="bold" fill="#4ade80" text-anchor="middle">3. STRIKE-SLIP FAULT (Shear)</text>
    
    <!-- Block Diagram (Lateral sliding) -->
    <g transform="translate(25, 35)">
      <polygon points="10,25 85,10 85,95 10,110" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
      <polygon points="85,35 160,20 160,105 85,120" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
      <line x1="85" y1="10" x2="85" y2="120" stroke="#ef4444" stroke-width="2.5"/>
      <!-- Shear arrows -->
      <polygon points="40,2 55,2 45,-8" fill="#22c55e"/>
      <polygon points="130,128 115,128 125,138" fill="#22c55e"/>
    </g>
    <text x="115" y="165" font-size="9.5" fill="#cbd5e1" text-anchor="middle">Lateral horizontal sliding (no vertical offset)</text>
    <text x="115" y="180" font-size="9" font-weight="bold" fill="#86efac" text-anchor="middle">Example: San Andreas Fault</text>
  </g>

  <!-- Bottom Panel: Horst and Graben Architecture -->
  <g transform="translate(30, 280)">
    <rect x="0" y="0" width="740" height="140" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="370" y="20" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">CRUSTAL BLOCK LANDFORMS: HORST (BLOCK MOUNTAIN) &amp; GRABEN (RIFT VALLEY)</text>
    
    <!-- Blocks geometry -->
    <g transform="translate(80, 30)">
      <!-- Left Side Block -->
      <polygon points="0,20 110,20 85,85 0,85" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
      
      <!-- Center Graben (Dropped) -->
      <polygon points="120,45 280,45 255,85 145,85" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
      <text x="200" y="65" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">GRABEN (Rift Valley Floor)</text>
      
      <!-- Right Horst (Elevated Block) -->
      <polygon points="290,5 420,5 445,85 315,85" fill="#475569" stroke="#f59e0b" stroke-width="2"/>
      <text x="365" y="35" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">HORST (Block Mountain)</text>
      
      <!-- Far Right Block -->
      <polygon points="455,20 580,20 580,85 480,85" fill="#334155" stroke="#64748b" stroke-width="1.5"/>

      <!-- Normal fault lines -->
      <line x1="110" y1="20" x2="145" y2="85" stroke="#ef4444" stroke-width="2" stroke-dasharray="3,3"/>
      <line x1="280" y1="45" x2="315" y2="85" stroke="#ef4444" stroke-width="2" stroke-dasharray="3,3"/>
      <line x1="420" y1="5" x2="455" y2="85" stroke="#ef4444" stroke-width="2" stroke-dasharray="3,3"/>
    </g>
    <text x="370" y="125" font-size="10" fill="#94a3b8" text-anchor="middle">Gregory Rift Valley (Graben) bordered by Aberdare/Mau Escarpments and Ruwenzori (Horst)</text>
  </g>
</svg>
""")

# SVG 6: The Earth System Cascade (Lesson 6)
SVG_EARTH_CASCADE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="42" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">THE COMPLETE EARTH SYSTEM CASCADE</text>
  <text x="400" y="60" font-size="11" fill="#94a3b8" text-anchor="middle">Tracing the Flow from Deep Geothermal Heat to Topography, Drainage &amp; Human Life</text>

  <!-- Flow Boxes: 6 Steps in 2 Rows -->

  <!-- Step 1: Deep Core Heat & Radioactivity -->
  <g transform="translate(35, 75)">
    <rect x="0" y="0" width="220" height="135" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="26" rx="8" fill="#b91c1c"/>
    <text x="110" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. INTERNAL HEAT ENGINE</text>
    <text x="15" y="50" font-size="9.5" fill="#fca5a5" font-weight="bold">• Core Primordial Heat</text>
    <text x="15" y="68" font-size="9.5" fill="#cbd5e1">• Radioactive Decay (U, Th, K)</text>
    <text x="15" y="86" font-size="9.5" fill="#cbd5e1">• Generates immense thermal energy</text>
    <text x="15" y="104" font-size="9.5" fill="#cbd5e1">• Liquefies outer core, heats mantle</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <polygon points="265,140 280,140 280,135 288,145 280,155 280,150 265,150" fill="#ef4444"/>

  <!-- Step 2: Mantle Convection -->
  <g transform="translate(290, 75)">
    <rect x="0" y="0" width="220" height="135" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="26" rx="8" fill="#d97706"/>
    <text x="110" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. MANTLE CONVECTION</text>
    <text x="15" y="50" font-size="9.5" fill="#fbbf24" font-weight="bold">• Thermal Circulation Cells</text>
    <text x="15" y="68" font-size="9.5" fill="#cbd5e1">• Hot plastic mantle rocks rise</text>
    <text x="15" y="86" font-size="9.5" fill="#cbd5e1">• Lateral asthenospheric drag</text>
    <text x="15" y="104" font-size="9.5" fill="#cbd5e1">• Drives plate tectonics engine</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <polygon points="520,140 535,140 535,135 543,145 535,155 535,150 520,150" fill="#f59e0b"/>

  <!-- Step 3: Crustal Stresses -->
  <g transform="translate(545, 75)">
    <rect x="0" y="0" width="220" height="135" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="26" rx="8" fill="#7e22ce"/>
    <text x="110" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. CRUSTAL STRESSES</text>
    <text x="15" y="50" font-size="9.5" fill="#c084fc" font-weight="bold">• Lateral Tension (Pulling apart)</text>
    <text x="15" y="68" font-size="9.5" fill="#cbd5e1">• Compression (Squeezing together)</text>
    <text x="15" y="86" font-size="9.5" fill="#cbd5e1">• Shear (Transform sliding)</text>
    <text x="15" y="104" font-size="9.5" fill="#cbd5e1">• Vertical Isostatic readjustment</text>
  </g>

  <!-- Downward Arrow Row 1 -> Row 2 -->
  <polygon points="655,220 655,235 660,235 650,245 640,235 645,235 645,220" fill="#38bdf8"/>

  <!-- Step 4: Geological Processes (Bottom Right) -->
  <g transform="translate(545, 255)">
    <rect x="0" y="0" width="220" height="155" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="26" rx="8" fill="#0369a1"/>
    <text x="110" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4. DEFORMATION PROCESSES</text>
    <text x="15" y="50" font-size="9.5" fill="#38bdf8" font-weight="bold">• Orogenic Folding</text>
    <text x="15" y="68" font-size="9.5" fill="#cbd5e1">• Faulting &amp; Rifting</text>
    <text x="15" y="86" font-size="9.5" fill="#cbd5e1">• Volcanism &amp; Magma Outpourings</text>
    <text x="15" y="104" font-size="9.5" fill="#cbd5e1">• Sudden Seismic Elastic Rebound</text>
  </g>

  <!-- Arrow 4 -> 5 (Leftwards) -->
  <polygon points="535,330 520,330 520,325 512,335 520,345 520,340 535,340" fill="#0284c7"/>

  <!-- Step 5: Surface Landforms & Drainage (Bottom Center) -->
  <g transform="translate(290, 255)">
    <rect x="0" y="0" width="220" height="155" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="26" rx="8" fill="#047857"/>
    <text x="110" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">5. LANDFORMS &amp; DRAINAGE</text>
    <text x="15" y="50" font-size="9.5" fill="#4ade80" font-weight="bold">• Rift Valleys &amp; Escarpments</text>
    <text x="15" y="68" font-size="9.5" fill="#cbd5e1">• Downwarped Lakes (Lake Victoria)</text>
    <text x="15" y="86" font-size="9.5" fill="#cbd5e1">• Fault-Guided Straight Rivers</text>
    <text x="15" y="104" font-size="9.5" fill="#cbd5e1">• Volcanic Mountains (Mt. Kenya)</text>
    <text x="15" y="122" font-size="9.5" fill="#cbd5e1">• Ongoing Denudation Sculpting</text>
  </g>

  <!-- Arrow 5 -> 6 (Leftwards) -->
  <polygon points="280,330 265,330 265,325 257,335 265,345 265,340 280,340" fill="#10b981"/>

  <!-- Step 6: Human Ecosystems & Resources (Bottom Left) -->
  <g transform="translate(35, 255)">
    <rect x="0" y="0" width="220" height="155" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="26" rx="8" fill="#16a34a"/>
    <text x="110" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">6. HUMAN ENVIRONMENT</text>
    <text x="15" y="48" font-size="9.5" fill="#86efac" font-weight="bold">• Fertile Volcanic Soils (Farming)</text>
    <text x="15" y="66" font-size="9.5" fill="#cbd5e1">• Geothermal Power (Olkaria)</text>
    <text x="15" y="84" font-size="9.5" fill="#cbd5e1">• Tourism (Alkaline Rift Lakes)</text>
    <text x="15" y="102" font-size="9.5" fill="#f87171">• Earthquake &amp; Landslide Hazards</text>
    <text x="15" y="120" font-size="9.5" fill="#cbd5e1">• Renewal of Continental Land</text>
  </g>
</svg>
""")

TOPIC_6_SVGS = {
    1: SVG_FORCES_DYNAMIC,
    2: SVG_MANTLE_CONVECTION,
    3: SVG_CRUSTAL_STRESSES,
    4: SVG_ELASTIC_REBOUND,
    5: SVG_FAULT_TYPES,
    6: SVG_EARTH_CASCADE,
}

# =============================================================================
# ENRICHMENT EXECUTION RUNNER
# =============================================================================
def enrich_topic_6():
    print("=" * 80)
    print("VLearn Visual Enrichment Engine: Grade 10 Geography — Topic 6: Earth Movements")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(id=37).first() or Subject.objects.filter(grade=grade, name="Geography").first()
    topic = Topic.objects.filter(subject=subject, order=6).first()

    if not topic:
        raise RuntimeError("Topic 6 'Earth Movements' not found in database!")

    verified_images_path = os.path.join(os.path.dirname(__file__), 'grade10_geography_topic6_verified_images.json')
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
                            "topic_order": 6
                        }
                    }
                )
                asset.url = img_data['url']
                asset.status = "attached"
                asset.save()
                asset.blocks.add(hook_block)
                print(f"  + Attached Wikimedia Photographic Hook: {img_data['url'][:55]}...")

        # 2. Attach Custom Vector SVG
        svg_xml = TOPIC_6_SVGS.get(int(u_order))
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
                            "topic_order": 6
                        }
                    }
                )
                svg_asset.metadata["svg_content"] = svg_xml
                svg_asset.status = "attached"
                svg_asset.save()
                svg_asset.blocks.add(diagram_block)
                print(f"  + Attached Custom Responsive Vector SVG to block '{diagram_block.title}'")

        # 3. Attach YouTube Video if present (Lesson 2)
        video_block = LessonBlock.objects.filter(
            lesson=lesson,
            block_type="video"
        ).first()

        if video_block:
            c = video_block.content or {}
            vid_url = c.get("url") or "https://www.youtube.com/watch?v=ryrXAGY1lAA"
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
                        "topic_order": 6
                    }
                }
            )
            v_asset.url = vid_url
            v_asset.status = "attached"
            v_asset.save()
            v_asset.blocks.add(video_block)
            print(f"  + Attached Educational YouTube Video: {vid_url}")

    print("\n" + "=" * 80)
    print("Topic 6 Visual Enrichment Completed Successfully!")
    print("=" * 80)

if __name__ == "__main__":
    enrich_topic_6()
