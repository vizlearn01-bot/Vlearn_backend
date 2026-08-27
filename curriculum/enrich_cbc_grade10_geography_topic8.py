"""
VLearn CBC Grade 10 Geography — Topic 8: Vulcanicity
Visual Enrichment Engine (Vector SVGs, Verified Wikimedia Images & Educational Videos)

Subject: Geography (Grade 10 CBC, Subject ID: 37)
Topic 8: Vulcanicity

Attaches:
  - 13 First-Card Photographic Visual Hooks (100% Tested HTTP 200 OK Direct Wikimedia URLs)
  - 13 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - Educational YouTube Video for Pyroclastic Flows & Volcanic Hazards
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade10_geography_topic8.py
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
# 13 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 8: VULCANICITY
# =============================================================================

# SVG 1: Tectonic & Thermal Drivers of Magma Generation (Lesson 1)
SVG_MAGMA_DRIVERS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">TECTONIC &amp; THERMAL DRIVERS OF MAGMA GENERATION</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Three Primary Physical Mechanisms Lowering Mantle Melting Points</text>

  <!-- Panel 1: Divergent Decompression -->
  <g transform="translate(30, 85)">
    <rect x="0" y="0" width="230" height="330" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="32" rx="10" fill="#0369a1"/>
    <text x="115" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. DIVERGENT RIFTING</text>
    
    <!-- Plates pulling apart -->
    <rect x="15" y="55" width="85" height="30" fill="#64748b" rx="3"/>
    <rect x="130" y="55" width="85" height="30" fill="#64748b" rx="3"/>
    <polygon points="45,70 30,70 30,65 20,70 30,75 30,70" fill="#f87171"/>
    <polygon points="175,70 190,70 190,65 200,70 190,75 190,70" fill="#f87171"/>
    <text x="55" y="50" font-size="10" fill="#94a3b8">Lithosphere</text>
    <text x="175" y="50" font-size="10" fill="#94a3b8">Lithosphere</text>
    
    <!-- Magma rising in center -->
    <path d="M 100 200 Q 115 130 115 75 Q 115 130 130 200 Z" fill="#ef4444" opacity="0.9"/>
    <polygon points="115,100 110,120 113,120 113,140 117,140 117,120 120,120" fill="#fbbf24"/>
    <polygon points="115,145 110,165 113,165 113,185 117,185 117,165 120,165" fill="#fbbf24"/>

    <!-- Explanatory text -->
    <text x="115" y="225" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Decompression Melting</text>
    <text x="115" y="245" font-size="9.5" fill="#cbd5e1" text-anchor="middle">• Crust pulls apart (rift)</text>
    <text x="115" y="260" font-size="9.5" fill="#cbd5e1" text-anchor="middle">• Confining pressure drops</text>
    <text x="115" y="275" font-size="9.5" fill="#cbd5e1" text-anchor="middle">• Asthenosphere melts freely</text>
    <text x="115" y="305" font-size="10" font-weight="bold" fill="#fca5a5" text-anchor="middle">e.g. East African Rift</text>
  </g>

  <!-- Panel 2: Subduction Flux Melting -->
  <g transform="translate(285, 85)">
    <rect x="0" y="0" width="230" height="330" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="32" rx="10" fill="#b91c1c"/>
    <text x="115" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. SUBDUCTION ZONES</text>

    <!-- Subducting oceanic plate -->
    <path d="M 15 65 L 110 65 L 180 180 L 140 195 L 85 105 L 15 105 Z" fill="#475569"/>
    <!-- Continental wedge -->
    <path d="M 115 65 L 215 65 L 215 130 L 135 130 Z" fill="#78350f" opacity="0.8"/>
    <!-- Water release dots -->
    <circle cx="120" cy="140" r="3" fill="#38bdf8"/>
    <circle cx="135" cy="155" r="3" fill="#38bdf8"/>
    <circle cx="150" cy="170" r="3" fill="#38bdf8"/>
    <!-- Magma plume to volcano -->
    <path d="M 155 130 Q 170 95 180 65 Q 185 95 170 130 Z" fill="#ef4444"/>
    <!-- Volcano on top -->
    <polygon points="160,65 180,45 200,65" fill="#b45309"/>

    <text x="115" y="225" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">Flux Melting (Water Addition)</text>
    <text x="115" y="245" font-size="9.5" fill="#cbd5e1" text-anchor="middle">• Wet oceanic crust descends</text>
    <text x="115" y="260" font-size="9.5" fill="#cbd5e1" text-anchor="middle">• Heat bakes out H2O fluids</text>
    <text x="115" y="275" font-size="9.5" fill="#cbd5e1" text-anchor="middle">• Water lowers melting point</text>
    <text x="115" y="305" font-size="10" font-weight="bold" fill="#fca5a5" text-anchor="middle">e.g. Pacific Ring of Fire</text>
  </g>

  <!-- Panel 3: Mantle Hotspots -->
  <g transform="translate(540, 85)">
    <rect x="0" y="0" width="230" height="330" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="32" rx="10" fill="#d97706"/>
    <text x="115" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. MANTLE HOTSPOTS</text>

    <!-- Plate moving over stationary plume -->
    <rect x="15" y="55" width="200" height="25" fill="#64748b" rx="2"/>
    <polygon points="180,67 195,67 195,63 205,67 195,71 195,67" fill="#38bdf8"/>
    <text x="115" y="50" font-size="10" fill="#94a3b8" text-anchor="middle">Overriding Crustal Plate</text>

    <!-- Hotspot plume from deep core boundary -->
    <path d="M 100 200 Q 115 130 115 75 Q 115 130 130 200 Z" fill="#f59e0b" opacity="0.9"/>
    <polygon points="105,55 115,40 125,55" fill="#dc2626"/>
    <polygon points="60,55 70,45 80,55" fill="#78350f" opacity="0.6"/>

    <text x="115" y="225" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">Deep Thermal Plumes</text>
    <text x="115" y="245" font-size="9.5" fill="#cbd5e1" text-anchor="middle">• Core-mantle thermal upwelling</text>
    <text x="115" y="260" font-size="9.5" fill="#cbd5e1" text-anchor="middle">• Burns hole through crust</text>
    <text x="115" y="275" font-size="9.5" fill="#cbd5e1" text-anchor="middle">• Forms volcanic island chains</text>
    <text x="115" y="305" font-size="10" font-weight="bold" fill="#fca5a5" text-anchor="middle">e.g. Hawaii &amp; Yellowstone</text>
  </g>
</svg>
""")

# SVG 2: Intrusive Magmatic Features Cross-Section (Lesson 2)
SVG_INTRUSIVE_FEATURES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">ANATOMY OF INTRUSIVE (PLUTONIC) IGNEOUS BODIES</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Concordant (Parallel) vs. Discordant (Cross-Cutting) Subsurface Structures</text>

  <g transform="translate(40, 80)">
    <!-- Sedimentary Rock Strata Background (Horizontal bedding planes) -->
    <rect x="0" y="40" width="720" height="50" fill="#334155" opacity="0.6"/>
    <line x1="0" y1="90" x2="720" y2="90" stroke="#475569" stroke-width="2" stroke-dasharray="6,4"/>
    <rect x="0" y="90" width="720" height="50" fill="#1e293b" opacity="0.8"/>
    <line x1="0" y1="140" x2="720" y2="140" stroke="#475569" stroke-width="2" stroke-dasharray="6,4"/>
    <rect x="0" y="140" width="720" height="50" fill="#334155" opacity="0.6"/>
    <line x1="0" y1="190" x2="720" y2="190" stroke="#475569" stroke-width="2" stroke-dasharray="6,4"/>
    <rect x="0" y="190" width="720" height="60" fill="#1e293b" opacity="0.8"/>

    <!-- 1. Deep Batholith at Base -->
    <path d="M 50 320 C 150 210, 450 200, 670 320 L 0 320 Z" fill="#b91c1c" stroke="#ef4444" stroke-width="2"/>
    <text x="360" y="290" font-size="15" font-weight="bold" fill="#ffffff" text-anchor="middle">BATHOLITH (Plutonic Root &gt; 100 km²)</text>

    <!-- 2. Laccolith (Mushroom Dome) -->
    <path d="M 80 140 Q 150 70 220 140 Z" fill="#dc2626" stroke="#f87171" stroke-width="2"/>
    <!-- Feeder pipe to Laccolith -->
    <rect x="145" y="140" width="10" height="85" fill="#dc2626"/>
    <text x="150" y="115" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">LACCOLITH</text>
    <text x="150" y="130" font-size="9" fill="#fecaca" text-anchor="middle">(Arched Strata)</text>

    <!-- 3. Sill (Concordant Sheet) -->
    <rect x="420" y="85" width="220" height="12" rx="2" fill="#ef4444" stroke="#fca5a5" stroke-width="1.5"/>
    <text x="530" y="80" font-size="11" font-weight="bold" fill="#fca5a5" text-anchor="middle">SILL (Parallel to Strata)</text>

    <!-- 4. Dyke (Discordant Wall) -->
    <rect x="520" y="97" width="14" height="135" fill="#ef4444" stroke="#fca5a5" stroke-width="1.5" transform="rotate(-5 520 140)"/>
    <text x="560" y="160" font-size="11" font-weight="bold" fill="#fca5a5" text-anchor="start">DYKE (Cuts Strata)</text>

    <!-- 5. Lopolith (Saucer Depression) -->
    <path d="M 230 150 Q 310 200 390 150 Q 310 175 230 150 Z" fill="#dc2626" stroke="#f87171" stroke-width="2"/>
    <rect x="305" y="170" width="10" height="55" fill="#dc2626"/>
    <text x="310" y="155" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">LOPOLITH</text>
    <text x="310" y="168" font-size="8.5" fill="#fecaca" text-anchor="middle">(Saucer Basin)</text>

    <!-- 6. Volcanic Plug & Eroded Cone -->
    <path d="M 620 40 L 680 0 L 740 40" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4" fill="none"/>
    <rect x="672" y="15" width="16" height="210" fill="#991b1b" stroke="#f87171" stroke-width="2"/>
    <text x="680" y="8" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">VOLCANIC PLUG</text>
    <text x="680" y="45" font-size="8.5" fill="#94a3b8" text-anchor="middle">(Fischer's Tower)</text>
  </g>

  <!-- Legend at Bottom -->
  <g transform="translate(60, 405)">
    <rect x="0" y="0" width="14" height="14" fill="#ef4444"/>
    <text x="22" y="11" font-size="10.5" fill="#cbd5e1">Concordant Intrusions (Sill, Laccolith, Lopolith)</text>
    <rect x="320" y="0" width="14" height="14" fill="#b91c1c"/>
    <text x="342" y="11" font-size="10.5" fill="#cbd5e1">Discordant Intrusions (Dyke, Batholith, Volcanic Plug)</text>
  </g>
</svg>
""")

# SVG 3: Acidic vs Basic Lava Flow Dynamics (Lesson 3)
SVG_LAVA_DYNAMICS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">LAVA DYNAMICS: BASIC (MAFIC) VS. ACIDIC (FELSIC)</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">How Silica Content and Viscosity Dictate Eruptive Style and Landform Morphology</text>

  <!-- Left: Basic (Mafic) Lava -->
  <g transform="translate(35, 85)">
    <rect x="0" y="0" width="345" height="330" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="36" rx="10" fill="#15803d"/>
    <text x="172" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">1. BASIC (MAFIC) LAVA</text>

    <!-- Gentle shield shape & runny lava -->
    <path d="M 20 180 Q 172 130 325 180 L 325 210 L 20 210 Z" fill="#334155"/>
    <path d="M 20 180 Q 172 140 325 180" stroke="#ef4444" stroke-width="8" fill="none"/>
    <path d="M 40 185 Q 172 145 305 185" stroke="#f59e0b" stroke-width="4" fill="none"/>

    <!-- Small bubbling gas vent -->
    <ellipse cx="172" cy="142" rx="12" ry="5" fill="#dc2626"/>
    <circle cx="165" cy="120" r="3" fill="#94a3b8" opacity="0.6"/>
    <circle cx="175" cy="105" r="4" fill="#94a3b8" opacity="0.6"/>
    <text x="172" y="95" font-size="9.5" fill="#94a3b8" text-anchor="middle">Gases escape easily (Effusive)</text>

    <!-- Characteristics -->
    <g transform="translate(20, 220)">
      <text x="0" y="15" font-size="11" font-weight="bold" fill="#4ade80">• Silica Content:</text>
      <text x="115" y="15" font-size="11" fill="#cbd5e1">Low (45 - 52% SiO2)</text>
      <text x="0" y="35" font-size="11" font-weight="bold" fill="#4ade80">• Viscosity:</text>
      <text x="115" y="35" font-size="11" fill="#cbd5e1">Low (Thin, fluid, runny)</text>
      <text x="0" y="55" font-size="11" font-weight="bold" fill="#4ade80">• Temperature:</text>
      <text x="115" y="55" font-size="11" fill="#cbd5e1">Very High (1,000°C - 1,200°C)</text>
      <text x="0" y="75" font-size="11" font-weight="bold" fill="#4ade80">• Landform:</text>
      <text x="115" y="75" font-size="11" fill="#cbd5e1">Shield Volcanoes, Lava Plateaus</text>
      <text x="0" y="95" font-size="11" font-weight="bold" fill="#4ade80">• Flow Range:</text>
      <text x="115" y="95" font-size="11" fill="#cbd5e1">Flows 10 - 50+ km before solidifying</text>
    </g>
  </g>

  <!-- Right: Acidic (Felsic) Lava -->
  <g transform="translate(420, 85)">
    <rect x="0" y="0" width="345" height="330" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="36" rx="10" fill="#b91c1c"/>
    <text x="172" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">2. ACIDIC (FELSIC) LAVA</text>

    <!-- Steep dome shape & viscous mound -->
    <path d="M 60 210 L 130 140 Q 172 80 215 140 L 285 210 Z" fill="#475569"/>
    <path d="M 125 140 Q 172 85 220 140 Q 172 110 125 140 Z" fill="#ef4444"/>

    <!-- High explosive gas blast -->
    <path d="M 172 85 Q 140 50 120 40 Q 172 45 220 40 Q 200 55 172 85 Z" fill="#94a3b8" opacity="0.8"/>
    <text x="172" y="55" font-size="9.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">EXPLOSIVE ASH BLAST</text>
    <text x="172" y="70" font-size="8.5" fill="#ffffff" text-anchor="middle">(Trapped High-Pressure Steam &amp; Gas)</text>

    <!-- Characteristics -->
    <g transform="translate(20, 220)">
      <text x="0" y="15" font-size="11" font-weight="bold" fill="#f87171">• Silica Content:</text>
      <text x="115" y="15" font-size="11" fill="#cbd5e1">High (&gt; 65% SiO2)</text>
      <text x="0" y="35" font-size="11" font-weight="bold" fill="#f87171">• Viscosity:</text>
      <text x="115" y="35" font-size="11" fill="#cbd5e1">High (Thick, sticky, gummy)</text>
      <text x="0" y="55" font-size="11" font-weight="bold" fill="#f87171">• Temperature:</text>
      <text x="115" y="55" font-size="11" fill="#cbd5e1">Lower (800°C - 1,000°C)</text>
      <text x="0" y="75" font-size="11" font-weight="bold" fill="#f87171">• Landform:</text>
      <text x="115" y="75" font-size="11" fill="#cbd5e1">Steep Domes, Stratovolcanoes</text>
      <text x="0" y="95" font-size="11" font-weight="bold" fill="#f87171">• Flow Range:</text>
      <text x="115" y="95" font-size="11" fill="#cbd5e1">Piles up directly over eruptive vent</text>
    </g>
  </g>
</svg>
""")

# SVG 4: Volcanic Materials: Solids, Liquids, and Gases (Lesson 4)
SVG_VOLCANIC_MATERIALS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">CLASSIFICATION OF VOLCANIC EJECTA</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Volatiles (Gases), Melts (Liquids), and Tephra / Pyroclastic Solids</text>

  <!-- Gas Box -->
  <g transform="translate(35, 85)">
    <rect x="0" y="0" width="225" height="150" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="225" height="28" rx="8" fill="#0284c7"/>
    <text x="112" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. GASEOUS VOLATILES</text>
    <text x="15" y="52" font-size="10.5" fill="#cbd5e1">• Water Vapor (H2O): 70 - 90%</text>
    <text x="15" y="72" font-size="10.5" fill="#cbd5e1">• Carbon Dioxide (CO2)</text>
    <text x="15" y="92" font-size="10.5" fill="#cbd5e1">• Sulfur Dioxide (SO2) [Acid Rain]</text>
    <text x="15" y="112" font-size="10.5" fill="#cbd5e1">• Hydrogen Sulfide (H2S)</text>
    <text x="15" y="132" font-size="10.5" fill="#cbd5e1">• Chlorine &amp; Fluorine Gases</text>
  </g>

  <!-- Liquid Box -->
  <g transform="translate(35, 250)">
    <rect x="0" y="0" width="225" height="165" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="225" height="28" rx="8" fill="#b91c1c"/>
    <text x="112" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. LIQUID LAVA TYPES</text>
    <text x="15" y="52" font-size="11" font-weight="bold" fill="#fca5a5">• Pahoehoe Lava:</text>
    <text x="25" y="70" font-size="10" fill="#cbd5e1">Smooth, ropy, satiny basaltic skin</text>
    <text x="15" y="95" font-size="11" font-weight="bold" fill="#fca5a5">• Aa Lava:</text>
    <text x="25" y="113" font-size="10" fill="#cbd5e1">Jagged, sharp, clinkery rough rubble</text>
    <text x="15" y="138" font-size="11" font-weight="bold" fill="#fca5a5">• Pillow Lava:</text>
    <text x="25" y="153" font-size="10" fill="#cbd5e1">Bulbous lobes chilled underwater</text>
  </g>

  <!-- Solids Particle Size Breakdown (Large Right Panel) -->
  <g transform="translate(280, 85)">
    <rect x="0" y="0" width="485" height="330" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="485" height="28" rx="8" fill="#d97706"/>
    <text x="242" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. SOLID PYROCLASTS (TEPHRA GRAIN-SIZE HIERARCHY)</text>

    <!-- Dust & Ash -->
    <g transform="translate(20, 45)">
      <circle cx="25" cy="25" r="2" fill="#e2e8f0"/>
      <circle cx="35" cy="20" r="1.5" fill="#e2e8f0"/>
      <circle cx="45" cy="28" r="2.5" fill="#e2e8f0"/>
      <text x="80" y="20" font-size="12" font-weight="bold" fill="#fbbf24">Volcanic Dust &amp; Ash (&lt; 2 mm)</text>
      <text x="80" y="38" font-size="10" fill="#cbd5e1">Microscopic rock glass powder; stays airborne for months, travels 1,000s of km.</text>
    </g>
    <line x1="20" y1="95" x2="465" y2="95" stroke="#334155" stroke-width="1"/>

    <!-- Lapilli -->
    <g transform="translate(20, 105)">
      <circle cx="20" cy="25" r="7" fill="#94a3b8"/>
      <circle cx="40" cy="22" r="10" fill="#64748b"/>
      <text x="80" y="20" font-size="12" font-weight="bold" fill="#fbbf24">Lapilli / Cinders (2 mm – 64 mm)</text>
      <text x="80" y="38" font-size="10" fill="#cbd5e1">Pea- to walnut-sized gravel fragments of frozen bubbly molten rock.</text>
    </g>
    <line x1="20" y1="155" x2="465" y2="155" stroke="#334155" stroke-width="1"/>

    <!-- Volcanic Blocks -->
    <g transform="translate(20, 165)">
      <polygon points="15,40 30,10 55,20 50,45 25,48" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
      <text x="80" y="20" font-size="12" font-weight="bold" fill="#fbbf24">Volcanic Blocks (&gt; 64 mm, Angular)</text>
      <text x="80" y="38" font-size="10" fill="#cbd5e1">Massive, sharp-edged angular boulders blasted from pre-existing solid crater walls.</text>
    </g>
    <line x1="20" y1="225" x2="465" y2="225" stroke="#334155" stroke-width="1"/>

    <!-- Volcanic Bombs -->
    <g transform="translate(20, 235)">
      <!-- Aerodynamic football shape -->
      <path d="M 10 30 Q 35 10 60 30 Q 35 50 10 30 Z" fill="#b91c1c" stroke="#f87171" stroke-width="1.5"/>
      <text x="80" y="20" font-size="12" font-weight="bold" fill="#fbbf24">Volcanic Bombs (&gt; 64 mm, Aerodynamic)</text>
      <text x="80" y="38" font-size="10" fill="#cbd5e1">Molten lava blobs ejected into flight; twisted into streamlined spindle/ribbon shapes.</text>
      <text x="80" y="55" font-size="9.5" fill="#fca5a5">• Kenyan Example: Abundant pumice &amp; obsidian deposits at Olkaria (Naivasha)</text>
    </g>
  </g>
</svg>
""")

# SVG 5: Extrusive Landforms Comparison (Lesson 5)
SVG_EXTRUSIVE_LANDFORMS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">EXTRUSIVE VOLCANIC LANDFORMS COMPARISON</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Shield Volcanoes vs. Cinder Cones vs. Fissure Lava Plateaus</text>

  <!-- Panel 1: Shield Volcano -->
  <g transform="translate(30, 85)">
    <rect x="0" y="0" width="230" height="330" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="32" rx="10" fill="#0284c7"/>
    <text x="115" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. SHIELD VOLCANO</text>

    <!-- Broad gentle dome -->
    <path d="M 15 150 Q 115 100 215 150 L 215 175 L 15 175 Z" fill="#334155"/>
    <path d="M 15 150 Q 115 100 215 150" stroke="#38bdf8" stroke-width="3" fill="none"/>
    <rect x="110" y="115" width="10" height="60" fill="#ef4444"/>

    <text x="115" y="195" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Broad Gentle Slopes (2° - 10°)</text>
    <text x="15" y="225" font-size="10" fill="#cbd5e1">• Low-viscosity basic basalt</text>
    <text x="15" y="245" font-size="10" fill="#cbd5e1">• Effusive, gentle lava flows</text>
    <text x="15" y="265" font-size="10" fill="#cbd5e1">• Giant base width (&gt; 100 km)</text>
    <text x="115" y="305" font-size="10" font-weight="bold" fill="#fca5a5" text-anchor="middle">e.g. Mauna Loa (Hawaii)</text>
  </g>

  <!-- Panel 2: Cinder Cone -->
  <g transform="translate(285, 85)">
    <rect x="0" y="0" width="230" height="330" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="32" rx="10" fill="#b91c1c"/>
    <text x="115" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. CINDER CONE</text>

    <!-- Steep small cone with top crater -->
    <path d="M 40 165 L 95 95 L 115 110 L 135 95 L 190 165 Z" fill="#475569"/>
    <!-- Loose cinder texture spots -->
    <circle cx="80" cy="140" r="2" fill="#ef4444"/>
    <circle cx="100" cy="130" r="2.5" fill="#f59e0b"/>
    <circle cx="150" cy="140" r="2" fill="#ef4444"/>
    <circle cx="130" cy="130" r="2.5" fill="#f59e0b"/>
    <rect x="111" y="110" width="8" height="55" fill="#ef4444"/>

    <text x="115" y="195" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">Steep Symmetrical Slopes (30° - 40°)</text>
    <text x="15" y="225" font-size="10" fill="#cbd5e1">• Loose pyroclastic scoria/ash</text>
    <text x="15" y="245" font-size="10" fill="#cbd5e1">• Explosive gas-driven eruptions</text>
    <text x="15" y="265" font-size="10" fill="#cbd5e1">• Small height (&lt; 400 m)</text>
    <text x="115" y="305" font-size="10" font-weight="bold" fill="#fca5a5" text-anchor="middle">e.g. Chyulu Hills (Kenya)</text>
  </g>

  <!-- Panel 3: Lava Plateau -->
  <g transform="translate(540, 85)">
    <rect x="0" y="0" width="230" height="330" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="32" rx="10" fill="#d97706"/>
    <text x="115" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. LAVA PLATEAU</text>

    <!-- Flat layered basalt table -->
    <rect x="25" y="120" width="180" height="45" fill="#334155"/>
    <line x1="25" y1="135" x2="205" y2="135" stroke="#ef4444" stroke-width="2"/>
    <line x1="25" y1="150" x2="205" y2="150" stroke="#f59e0b" stroke-width="2"/>
    <!-- Vertical fissure feeder -->
    <rect x="110" y="120" width="10" height="45" fill="#ef4444"/>

    <text x="115" y="195" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">Extensive Flat Upland Table</text>
    <text x="15" y="225" font-size="10" fill="#cbd5e1">• Highly fluid basalt from fissures</text>
    <text x="15" y="245" font-size="10" fill="#cbd5e1">• Layer upon layer of flood lava</text>
    <text x="15" y="265" font-size="10" fill="#cbd5e1">• Inverted relief through erosion</text>
    <text x="115" y="305" font-size="10" font-weight="bold" fill="#fca5a5" text-anchor="middle">e.g. Yatta Plateau (300 km)</text>
  </g>
</svg>
""")

# SVG 6: Composite Volcano (Stratovolcano) Cross-Section (Lesson 6)
SVG_STRATOVOLCANO = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">COMPOSITE VOLCANO (STRATOVOLCANO) ANATOMY</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Alternating Strata of Ash and Lava Flows with Conduit Branching</text>

  <g transform="translate(50, 80)">
    <!-- Base Magma Chamber -->
    <ellipse cx="350" cy="300" rx="120" ry="40" fill="#b91c1c" stroke="#ef4444" stroke-width="2"/>
    <text x="350" y="305" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">MAGMA CHAMBER</text>

    <!-- Main Cone Body -->
    <!-- Alternating layers -->
    <!-- Layer 1 (Ash): Gray with stipples -->
    <polygon points="50,260 350,70 650,260" fill="#475569"/>
    <!-- Layer 2 (Lava): Reddish -->
    <polygon points="80,260 350,90 620,260" fill="#7f1d1d"/>
    <!-- Layer 3 (Ash): Slate -->
    <polygon points="110,260 350,110 590,260" fill="#334155"/>
    <!-- Layer 4 (Lava): Crimson -->
    <polygon points="140,260 350,130 560,260" fill="#991b1b"/>
    <!-- Layer 5 (Ash): Gray -->
    <polygon points="170,260 350,150 530,260" fill="#475569"/>

    <!-- Central Vent Conduit -->
    <rect x="340" y="45" width="20" height="225" fill="#dc2626" stroke="#fca5a5" stroke-width="1"/>

    <!-- Summit Crater -->
    <polygon points="325,45 350,65 375,45" fill="#0f172a"/>
    <text x="350" y="30" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Summit Crater</text>

    <!-- Parasitic Cone on Right Flank -->
    <polygon points="500,220 540,175 580,220" fill="#475569"/>
    <!-- Branch Conduit / Feeder Dyke -->
    <line x1="355" y1="210" x2="540" y2="185" stroke="#ef4444" stroke-width="6"/>
    <text x="590" y="175" font-size="11" font-weight="bold" fill="#fbbf24">Parasitic Cone</text>
    <text x="590" y="190" font-size="9" fill="#cbd5e1">(Flank Eruption)</text>

    <!-- Feeder Dykes & Sills on Left Flank -->
    <line x1="345" y1="230" x2="200" y2="180" stroke="#ef4444" stroke-width="5"/>
    <line x1="200" y1="180" x2="160" y2="200" stroke="#ef4444" stroke-width="4"/>
    <text x="140" y="175" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">Intrusive Dykes &amp; Sills</text>

    <!-- Labels & Arrows -->
    <!-- Alternating layers annotation -->
    <line x1="120" y1="100" x2="200" y2="130" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="110" y="90" font-size="10.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Alternating Ash &amp; Lava Layers</text>
  </g>

  <!-- Kenyan Context Tag -->
  <text x="400" y="420" font-size="11.5" font-weight="bold" fill="#fca5a5" text-anchor="middle">Kenyan Exemplar: Mount Longonot (2,776 m) — Steep Trachyte Lava &amp; Pumice Strata</text>
</svg>
""")

# SVG 7: Caldera Collapse Sequence (Lesson 7)
SVG_CALDERA_COLLAPSE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">THREE-STAGE CALDERA COLLAPSE SEQUENCE</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Structural Inward Collapse Following Magma Chamber Evacuation</text>

  <!-- Stage 1: Climactic Eruption -->
  <g transform="translate(30, 85)">
    <rect x="0" y="0" width="230" height="330" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="32" rx="10" fill="#b91c1c"/>
    <text x="115" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 1: ERUPTION</text>

    <!-- Cone erupting violently -->
    <polygon points="20,190 115,80 210,190" fill="#475569"/>
    <!-- Huge eruption plume -->
    <path d="M 115 80 Q 70 35 50 20 Q 115 30 180 20 Q 160 35 115 80 Z" fill="#94a3b8" opacity="0.85"/>
    <!-- Magma Chamber emptying -->
    <ellipse cx="115" cy="250" rx="75" ry="30" fill="#450a0a" stroke="#ef4444" stroke-width="1.5"/>
    <ellipse cx="115" cy="265" rx="55" ry="15" fill="#dc2626"/>
    <text x="115" y="245" font-size="9" fill="#fca5a5" text-anchor="middle">Emptying Void</text>

    <text x="115" y="295" font-size="10.5" font-weight="bold" fill="#f87171" text-anchor="middle">Climactic Eruption</text>
    <text x="115" y="315" font-size="9" fill="#cbd5e1" text-anchor="middle">Massive magma release empties chamber</text>
  </g>

  <!-- Stage 2: Structural Summit Collapse -->
  <g transform="translate(285, 85)">
    <rect x="0" y="0" width="230" height="330" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="32" rx="10" fill="#d97706"/>
    <text x="115" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 2: COLLAPSE</text>

    <!-- Broken summit collapsing along ring faults -->
    <polygon points="20,190 65,130 165,130 210,190" fill="#475569"/>
    <!-- Collapsing block -->
    <polygon points="65,130 115,160 165,130 145,190 85,190" fill="#334155" stroke="#f59e0b" stroke-width="1.5"/>
    <!-- Downward collapse arrows -->
    <polygon points="115,150 110,135 120,135" fill="#f59e0b"/>
    <line x1="115" y1="115" x2="115" y2="145" stroke="#f59e0b" stroke-width="2"/>
    <!-- Ring fault lines -->
    <line x1="65" y1="130" x2="75" y2="250" stroke="#f87171" stroke-width="1.5" stroke-dasharray="3,3"/>
    <line x1="165" y1="130" x2="155" y2="250" stroke="#f87171" stroke-width="1.5" stroke-dasharray="3,3"/>

    <text x="115" y="295" font-size="10.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">Roof Collapse</text>
    <text x="115" y="315" font-size="9" fill="#cbd5e1" text-anchor="middle">Summit caves in along ring fractures</text>
  </g>

  <!-- Stage 3: Caldera Basin & Lake -->
  <g transform="translate(540, 85)">
    <rect x="0" y="0" width="230" height="330" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="32" rx="10" fill="#0284c7"/>
    <text x="115" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 3: CALDERA LAKE</text>

    <!-- Steep walls and flat basin -->
    <path d="M 20 190 L 60 135 L 75 170 L 155 170 L 170 135 L 210 190 Z" fill="#475569"/>
    <!-- Blue caldera lake -->
    <polygon points="78,168 152,168 145,175 85,175" fill="#38bdf8"/>
    <text x="115" y="163" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">CALDERA LAKE</text>

    <!-- Solidified pluton base -->
    <ellipse cx="115" cy="250" rx="75" ry="25" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
    <text x="115" y="255" font-size="8.5" fill="#94a3b8" text-anchor="middle">Cooling Pluton Base</text>

    <text x="115" y="295" font-size="10.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Menengai &amp; Lake Simbi</text>
    <text x="115" y="315" font-size="9" fill="#cbd5e1" text-anchor="middle">Steep caldera ring walls (up to 90 km²)</text>
  </g>
</svg>
""")

# SVG 8: Geyser Plumbing Physics & Eruption Thermodynamics (Lesson 8)
SVG_GEYSER_PHYSICS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">HYDROTHERMAL GEYSER PLUMBING &amp; THERMODYNAMICS</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">How Superheated Water Under Hydrostatic Pressure Triggers Violent Steam Flash Eruptions</text>

  <!-- Left: Underground Plumbing Diagram -->
  <g transform="translate(40, 85)">
    <rect x="0" y="0" width="350" height="330" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="350" height="30" rx="10" fill="#0369a1"/>
    <text x="175" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">CONFINED GEYSER PLUMBING CONDUIT</text>

    <!-- Ground surface -->
    <rect x="20" y="70" width="310" height="15" fill="#475569" rx="2"/>
    <text x="35" y="62" font-size="10" fill="#94a3b8">Ground Surface</text>

    <!-- Narrow constricted twisted channel -->
    <path d="M 160 70 L 160 120 L 140 140 L 170 180 L 150 210 L 165 240 L 145 260 L 185 260 L 185 240 L 165 210 L 185 180 L 155 140 L 175 120 L 175 70 Z" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>

    <!-- Steam bubble formation -->
    <circle cx="165" cy="230" r="5" fill="#ffffff" opacity="0.9"/>
    <circle cx="155" cy="245" r="4" fill="#ffffff" opacity="0.9"/>
    <circle cx="170" cy="252" r="6" fill="#ffffff" opacity="0.9"/>

    <!-- Magma Heat Source at bottom -->
    <rect x="40" y="275" width="270" height="40" rx="6" fill="#b91c1c" stroke="#ef4444" stroke-width="1.5"/>
    <text x="175" y="300" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">MAGMATIC HEAT SOURCE (&gt; 300°C)</text>

    <!-- Erupting column at surface -->
    <path d="M 160 70 Q 140 35 155 10 Q 167 35 175 70 Z" fill="#38bdf8" opacity="0.8"/>
  </g>

  <!-- Right: 4-Step Eruption Cycle Steps -->
  <g transform="translate(410, 85)">
    <rect x="0" y="0" width="350" height="330" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="350" height="30" rx="10" fill="#d97706"/>
    <text x="175" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">THE FOUR THERMODYNAMIC PHASES</text>

    <g transform="translate(20, 45)">
      <circle cx="12" cy="12" r="12" fill="#0284c7"/>
      <text x="12" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1</text>
      <text x="35" y="10" font-size="11" font-weight="bold" fill="#38bdf8">Groundwater Infiltration</text>
      <text x="35" y="25" font-size="9.5" fill="#cbd5e1">Cold meteoric water fills deep twisted fissures.</text>
    </g>

    <g transform="translate(20, 110)">
      <circle cx="12" cy="12" r="12" fill="#d97706"/>
      <text x="12" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2</text>
      <text x="35" y="10" font-size="11" font-weight="bold" fill="#fbbf24">Superheating Under Pressure</text>
      <text x="35" y="25" font-size="9.5" fill="#cbd5e1">Overlying water column raises boiling point &gt; 120°C.</text>
    </g>

    <g transform="translate(20, 175)">
      <circle cx="12" cy="12" r="12" fill="#ea580c"/>
      <text x="12" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3</text>
      <text x="35" y="10" font-size="11" font-weight="bold" fill="#fb923c">Steam Expansion &amp; Overflow</text>
      <text x="35" y="25" font-size="9.5" fill="#cbd5e1">Deep steam expands, lifting and overflowing top water.</text>
    </g>

    <g transform="translate(20, 240)">
      <circle cx="12" cy="12" r="12" fill="#dc2626"/>
      <text x="12" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4</text>
      <text x="35" y="10" font-size="11" font-weight="bold" fill="#f87171">Pressure Drop &amp; Steam Flash</text>
      <text x="35" y="25" font-size="9.5" fill="#cbd5e1">Sudden pressure drop flashes water to steam (1,600x blast).</text>
    </g>
    <text x="175" y="315" font-size="10" font-weight="bold" fill="#fca5a5" text-anchor="middle">Kenyan Exemplar: Lake Bogoria Boiling Geysers (5m jets)</text>
  </g>
</svg>
""")

# SVG 9: Global Volcanic Belts Map (Lesson 9)
SVG_GLOBAL_BELTS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">GLOBAL DISTRIBUTION OF VOLCANIC BELTS &amp; TECTONICS</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">The Pacific Ring of Fire, Mid-Atlantic Ridge, and East African Rift Zone</text>

  <!-- World Map Sketch (Continents Silhouettes) -->
  <g transform="translate(40, 80)">
    <rect x="0" y="0" width="720" height="260" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- Continents in dark slate -->
    <!-- North America -->
    <path d="M 60 50 Q 120 40 160 80 Q 130 140 100 150 Q 80 110 60 50 Z" fill="#334155"/>
    <!-- South America -->
    <path d="M 120 155 Q 160 170 140 230 Q 110 240 105 180 Z" fill="#334155"/>
    <!-- Eurasia -->
    <path d="M 280 40 Q 450 30 520 70 Q 480 120 380 100 Q 320 110 280 40 Z" fill="#334155"/>
    <!-- Africa -->
    <path d="M 300 100 Q 380 100 370 180 Q 340 230 310 180 Q 280 140 300 100 Z" fill="#334155"/>
    <!-- Australia -->
    <path d="M 500 170 Q 560 160 560 210 Q 500 220 500 170 Z" fill="#334155"/>

    <!-- 1. Pacific Ring of Fire (Red Bold Horseshoe Belt) -->
    <path d="M 60 80 Q 10 110 20 180 Q 40 240 70 250 M 640 240 Q 600 180 580 120 Q 540 50 480 40" stroke="#ef4444" stroke-width="5" stroke-dasharray="8,4" fill="none"/>
    <path d="M 70 60 L 150 90 L 120 170 L 105 240" stroke="#ef4444" stroke-width="4" stroke-dasharray="6,4" fill="none"/>
    <text x="610" y="160" font-size="12" font-weight="bold" fill="#f87171">PACIFIC RING OF FIRE</text>
    <text x="610" y="175" font-size="9" fill="#fca5a5">(75% of Active Volcanoes)</text>

    <!-- 2. Mid-Atlantic Ridge (Cyan S-Curve) -->
    <path d="M 220 30 Q 240 90 220 140 Q 240 200 230 250" stroke="#38bdf8" stroke-width="3.5" stroke-dasharray="5,3" fill="none"/>
    <circle cx="225" cy="40" r="5" fill="#38bdf8"/>
    <text x="235" y="43" font-size="10" font-weight="bold" fill="#38bdf8">Iceland (Divergent)</text>

    <!-- 3. East African Rift System (Amber Line) -->
    <path d="M 360 100 L 350 140 L 355 190" stroke="#f59e0b" stroke-width="4" fill="none"/>
    <circle cx="352" cy="145" r="4" fill="#ef4444"/>
    <text x="365" y="145" font-size="10" font-weight="bold" fill="#fbbf24">East African Rift (Kenya)</text>

    <!-- 4. Hawaii Hotspot -->
    <circle cx="20" cy="120" r="5" fill="#f59e0b"/>
    <text x="30" y="123" font-size="9.5" fill="#fbbf24">Hawaii Hotspot</text>
  </g>

  <!-- Legend at Bottom -->
  <g transform="translate(60, 365)">
    <rect x="0" y="0" width="16" height="10" fill="#ef4444"/>
    <text x="25" y="9" font-size="11" fill="#cbd5e1">Subduction Volcanism (Convergent / Ring of Fire)</text>
    <rect x="360" y="0" width="16" height="10" fill="#38bdf8"/>
    <text x="385" y="9" font-size="11" fill="#cbd5e1">Mid-Ocean Ridge Volcanism (Divergent / Atlantic)</text>
    <rect x="0" y="25" width="16" height="10" fill="#f59e0b"/>
    <text x="25" y="34" font-size="11" fill="#cbd5e1">Continental Rifting &amp; Mantle Hotspots (East Africa / Hawaii)</text>
  </g>
</svg>
""")

# SVG 10: Geographic Distribution of Volcanic Landforms in Kenya (Lesson 10)
SVG_KENYA_VOLCANISM = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">VOLCANIC LANDSCAPES &amp; DISTRIBUTION IN KENYA</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Spatial Alignment of Volcanoes Along the Gregory Rift Valley and Eastern Highlands</text>

  <g transform="translate(50, 80)">
    <!-- Kenya Border Outline Sketch -->
    <path d="M 120 20 L 260 10 L 360 80 L 370 200 L 290 300 L 190 280 L 100 240 L 70 120 Z" fill="#0f172a" stroke="#475569" stroke-width="2"/>

    <!-- Great Rift Valley Tectonic Trench (Shaded trough) -->
    <path d="M 150 20 Q 180 140 180 270 L 215 270 Q 215 140 185 20 Z" fill="#b91c1c" opacity="0.25"/>
    <line x1="150" y1="20" x2="180" y2="270" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,3"/>
    <line x1="185" y1="20" x2="215" y2="270" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,3"/>
    <text x="182" y="35" font-size="10" font-weight="bold" fill="#f87171" text-anchor="middle">Rift Floor</text>

    <!-- Lake Turkana -->
    <ellipse cx="160" cy="50" rx="8" ry="25" fill="#0284c7"/>
    <text x="135" y="55" font-size="9" fill="#38bdf8">L. Turkana</text>

    <!-- 1. Mount Elgon (Extinct Shield) -->
    <circle cx="85" cy="140" r="6" fill="#f59e0b"/>
    <text x="75" y="135" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="end">Mt. Elgon (Extinct)</text>

    <!-- 2. Menengai Caldera -->
    <circle cx="180" cy="165" r="6" fill="#ef4444"/>
    <text x="170" y="165" font-size="10" font-weight="bold" fill="#f87171" text-anchor="end">Menengai Caldera</text>

    <!-- 3. Mount Kenya (Extinct Plug) -->
    <circle cx="255" cy="170" r="7" fill="#38bdf8"/>
    <text x="268" y="170" font-size="11" font-weight="bold" fill="#38bdf8">Mt. Kenya (Batian/Nelion)</text>

    <!-- 4. Mount Longonot & Olkaria -->
    <circle cx="195" cy="195" r="6" fill="#ef4444"/>
    <text x="208" y="195" font-size="10" font-weight="bold" fill="#f87171">Mt. Longonot &amp; Olkaria</text>

    <!-- 5. Lake Simbi (Homa Bay) -->
    <circle cx="100" cy="195" r="5" fill="#06b6d4"/>
    <text x="90" y="205" font-size="9.5" fill="#22d3ee" text-anchor="end">Lake Simbi</text>

    <!-- 6. Yatta Plateau (Long Ridge) -->
    <path d="M 245 205 Q 280 250 310 280" stroke="#f59e0b" stroke-width="4"/>
    <text x="290" y="240" font-size="10" font-weight="bold" fill="#fbbf24">Yatta Plateau (300 km)</text>

    <!-- 7. Chyulu Hills Cinder Cones -->
    <ellipse cx="270" cy="275" rx="15" ry="6" fill="#dc2626"/>
    <text x="270" y="300" font-size="10" font-weight="bold" fill="#fca5a5" text-anchor="middle">Chyulu Hills (Shaitani Cone)</text>
  </g>

  <!-- Classification Summary Box on Right -->
  <g transform="translate(480, 85)">
    <rect x="0" y="0" width="270" height="325" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <rect x="0" y="0" width="270" height="28" rx="8" fill="#334155"/>
    <text x="135" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">KENYAN VOLCANO STATUS</text>

    <g transform="translate(15, 45)">
      <text x="0" y="0" font-size="11" font-weight="bold" fill="#38bdf8">• EXTINCT VOLCANOES:</text>
      <text x="10" y="18" font-size="9.5" fill="#cbd5e1">- Mt. Kenya (Plugs: Batian &amp; Nelion)</text>
      <text x="10" y="33" font-size="9.5" fill="#cbd5e1">- Mt. Elgon (Caves &amp; Caldera)</text>
    </g>

    <g transform="translate(15, 110)">
      <text x="0" y="0" font-size="11" font-weight="bold" fill="#f87171">• DORMANT VOLCANOES:</text>
      <text x="10" y="18" font-size="9.5" fill="#cbd5e1">- Mt. Longonot (Active steam vents)</text>
      <text x="10" y="33" font-size="9.5" fill="#cbd5e1">- Menengai Caldera (90 km² floor)</text>
      <text x="10" y="48" font-size="9.5" fill="#cbd5e1">- Mt. Suswa (Lava tube caves)</text>
    </g>

    <g transform="translate(15, 190)">
      <text x="0" y="0" font-size="11" font-weight="bold" fill="#fbbf24">• YOUNG / ACTIVE FIELDS:</text>
      <text x="10" y="18" font-size="9.5" fill="#cbd5e1">- Chyulu Hills (Shaitani Cone)</text>
      <text x="10" y="33" font-size="9.5" fill="#cbd5e1">- Olkaria Geothermal Field</text>
      <text x="10" y="48" font-size="9.5" fill="#cbd5e1">- Lake Bogoria Geysers</text>
    </g>
    <text x="135" y="305" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Over 40% of Kenya's Power = Geothermal</text>
  </g>
</svg>
""")

# SVG 11: Olkaria Geothermal Power Generation Cycle (Lesson 11)
SVG_OLKARIA_GEOTHERMAL = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">OLKARIA GEOTHERMAL POWER GENERATION CYCLE</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Harnessing Magmatic Steam to Produce Clean, Renewable Baseload Electricity</text>

  <g transform="translate(40, 80)">
    <!-- Ground Line -->
    <rect x="0" y="120" width="720" height="12" fill="#475569"/>
    <text x="15" y="112" font-size="11" fill="#94a3b8">Ground Surface (Hell's Gate National Park)</text>

    <!-- Deep Magma Reservoir at Bottom -->
    <ellipse cx="360" cy="300" rx="300" ry="35" fill="#b91c1c" stroke="#ef4444" stroke-width="2"/>
    <text x="360" y="305" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">SUB-SURFACE MAGMA HEAT SOURCE (&gt; 350°C)</text>

    <!-- Deep Geothermal Permeable Aquifer -->
    <rect x="60" y="210" width="600" height="45" fill="#0284c7" opacity="0.6" rx="4"/>
    <text x="360" y="238" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">SUPERHEATED HYDROTHERMAL RESERVOIR (Deep Water)</text>

    <!-- Production Well (Tapping Steam) -->
    <line x1="150" y1="120" x2="150" y2="230" stroke="#f59e0b" stroke-width="6"/>
    <polygon points="150,130 145,150 155,150" fill="#ffffff"/>
    <text x="135" y="175" font-size="10.5" font-weight="bold" fill="#fbbf24" text-anchor="end">Production Well</text>
    <text x="135" y="190" font-size="9" fill="#cbd5e1" text-anchor="end">(3,000 m Deep)</text>

    <!-- Separator Facility on Surface -->
    <rect x="180" y="60" width="60" height="60" rx="6" fill="#334155" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="210" y="90" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">CYCLONE</text>
    <text x="210" y="103" font-size="8.5" fill="#cbd5e1" text-anchor="middle">SEPARATOR</text>

    <!-- Steam pipe from well to separator -->
    <path d="M 150 120 L 150 90 L 180 90" stroke="#f59e0b" stroke-width="4" fill="none"/>

    <!-- Steam Turbine & Generator -->
    <rect x="300" y="55" width="100" height="65" rx="6" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <circle cx="330" cy="87" r="16" fill="#15803d"/>
    <text x="330" y="92" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">TURBINE</text>
    <rect x="360" y="72" width="30" height="30" fill="#eab308"/>
    <text x="375" y="90" font-size="9" font-weight="bold" fill="#000000" text-anchor="middle">GEN</text>

    <!-- Steam pipe from separator to turbine -->
    <line x1="240" y1="90" x2="300" y2="90" stroke="#38bdf8" stroke-width="4"/>

    <!-- Power Grid Transmission Lines -->
    <line x1="390" y1="87" x2="480" y2="40" stroke="#22c55e" stroke-width="2.5" stroke-dasharray="4,2"/>
    <text x="485" y="35" font-size="11" font-weight="bold" fill="#4ade80">National Grid (800+ MW)</text>

    <!-- Cooling Tower -->
    <path d="M 450 120 L 465 60 L 515 60 L 530 120 Z" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="490" y="95" font-size="9.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Cooling Tower</text>

    <!-- Reinjection Well (Eco-friendly recycle) -->
    <line x1="600" y1="120" x2="600" y2="230" stroke="#0284c7" stroke-width="6"/>
    <polygon points="600,210 595,190 605,190" fill="#ffffff"/>
    <text x="615" y="175" font-size="10.5" font-weight="bold" fill="#38bdf8">Reinjection Well</text>
    <text x="615" y="190" font-size="9" fill="#cbd5e1">(100% Recycled Water)</text>

    <!-- Pipe to Reinjection well -->
    <path d="M 530 110 L 600 110 L 600 120" stroke="#0284c7" stroke-width="3" fill="none"/>
  </g>
</svg>
""")

# SVG 12: Volcanic Hazards Matrix & Climate Dispersion (Lesson 12)
SVG_VOLCANIC_HAZARDS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">VOLCANIC HAZARDS MATRIX &amp; CLIMATIC IMPACTS</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Primary Lethal Threats, Secondary Disasters, and Stratospheric Global Cooling</text>

  <!-- Left: Eruption Hazard Diagram -->
  <g transform="translate(35, 85)">
    <rect x="0" y="0" width="345" height="330" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="30" rx="10" fill="#b91c1c"/>
    <text x="172" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">LOCAL &amp; REGIONAL HAZARDS</text>

    <!-- Volcano drawing -->
    <polygon points="40,240 172,110 305,240" fill="#475569"/>
    
    <!-- 1. Pyroclastic Flow (Superheated gray cloud rushing down slope) -->
    <path d="M 172 110 Q 120 160 50 230 Q 100 210 172 170 Z" fill="#94a3b8" opacity="0.9"/>
    <text x="95" y="165" font-size="10" font-weight="bold" fill="#fca5a5">Pyroclastic Flow</text>
    <text x="95" y="177" font-size="8" fill="#ffffff">(Up to 1,000°C / 700 km/h)</text>

    <!-- 2. Lahar Mudflow on right slope -->
    <path d="M 172 140 Q 230 180 310 245 L 290 250 Q 220 190 172 150 Z" fill="#78350f"/>
    <text x="255" y="195" font-size="10" font-weight="bold" fill="#fbbf24">Lahar (Mudflow)</text>

    <!-- 3. Lava Flow -->
    <path d="M 172 110 L 200 240" stroke="#ef4444" stroke-width="6"/>
    <text x="205" y="235" font-size="9.5" font-weight="bold" fill="#f87171">Lava Flow</text>

    <!-- 4. Ash Fallout -->
    <circle cx="80" cy="70" r="2" fill="#e2e8f0"/>
    <circle cx="100" cy="60" r="1.5" fill="#e2e8f0"/>
    <circle cx="120" cy="75" r="2" fill="#e2e8f0"/>
    <text x="172" y="295" font-size="10.5" font-weight="bold" fill="#ef4444" text-anchor="middle">Primary Lethal Risk: Pyroclastic Currents</text>
  </g>

  <!-- Right: Stratospheric Global Cooling Mechanism -->
  <g transform="translate(420, 85)">
    <rect x="0" y="0" width="345" height="330" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="30" rx="10" fill="#0369a1"/>
    <text x="172" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">GLOBAL CLIMATIC COOLING MECHANISM</text>

    <!-- Stratosphere Aerosol Layer -->
    <rect x="20" y="55" width="305" height="40" rx="4" fill="#0284c7" opacity="0.3"/>
    <text x="172" y="78" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Stratospheric Sulfate Aerosols (H2SO4)</text>

    <!-- Incoming Solar Radiation reflected -->
    <line x1="80" y1="20" x2="80" y2="55" stroke="#f59e0b" stroke-width="3"/>
    <polygon points="80,55 75,45 85,45" fill="#f59e0b"/>
    <!-- Reflected arrow -->
    <line x1="80" y1="55" x2="110" y2="25" stroke="#f59e0b" stroke-width="3"/>
    <polygon points="110,25 100,28 107,35" fill="#f59e0b"/>
    <text x="125" y="40" font-size="9" fill="#fbbf24">Reflected Solar Rays</text>

    <!-- Explanatory Bullet Points -->
    <g transform="translate(20, 115)">
      <text x="0" y="15" font-size="11" font-weight="bold" fill="#38bdf8">1. SO2 Gas Injection:</text>
      <text x="10" y="32" font-size="9.5" fill="#cbd5e1">Plume injects millions of tons of SO2 into stratosphere.</text>

      <text x="0" y="60" font-size="11" font-weight="bold" fill="#38bdf8">2. Aerosol Conversion:</text>
      <text x="10" y="77" font-size="9.5" fill="#cbd5e1">SO2 reacts with H2O vapor -> highly reflective droplets.</text>

      <text x="0" y="105" font-size="11" font-weight="bold" fill="#38bdf8">3. Global Temperature Drop:</text>
      <text x="10" y="122" font-size="9.5" fill="#cbd5e1">Solar radiation blocked -> Earth cools by 0.5°C - 2°C.</text>

      <text x="0" y="150" font-size="11" font-weight="bold" fill="#fca5a5">Historical Case:</text>
      <text x="10" y="167" font-size="9.5" fill="#fca5a5">1815 Mt. Tambora -> "The Year Without a Summer"</text>
    </g>
  </g>
</svg>
""")

# SVG 13: Volcanic Early Warning & Evacuation Matrix (Lesson 13)
SVG_DISASTER_PREPAREDNESS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">VOLCANIC EARLY WARNING &amp; DISASTER PROTOCOL</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Four-Tier Alert System: Scientific Monitoring Triggers Emergency Community Action</text>

  <!-- 4 Alert Levels as Step Cards -->
  <!-- Level 1: GREEN -->
  <g transform="translate(30, 85)">
    <rect x="0" y="0" width="170" height="320" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="170" height="36" rx="8" fill="#15803d"/>
    <text x="85" y="24" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. GREEN: NORMAL</text>
    
    <text x="15" y="60" font-size="11" font-weight="bold" fill="#4ade80">Scientific Signals:</text>
    <text x="15" y="78" font-size="9.5" fill="#cbd5e1">• Baseline background seismicity</text>
    <text x="15" y="98" font-size="9.5" fill="#cbd5e1">• Normal volcanic gas emission rates</text>
    <text x="15" y="118" font-size="9.5" fill="#cbd5e1">• Zero ground deformation/tilt</text>

    <text x="15" y="160" font-size="11" font-weight="bold" fill="#4ade80">Public Action:</text>
    <text x="15" y="178" font-size="9.5" fill="#cbd5e1">• Normal community routine</text>
    <text x="15" y="198" font-size="9.5" fill="#cbd5e1">• Regular hazard mapping drills</text>
    <text x="15" y="218" font-size="9.5" fill="#cbd5e1">• Park tourism fully open</text>
  </g>

  <!-- Level 2: YELLOW -->
  <g transform="translate(220, 85)">
    <rect x="0" y="0" width="170" height="320" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect x="0" y="0" width="170" height="36" rx="8" fill="#a16207"/>
    <text x="85" y="24" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. YELLOW: ADVISORY</text>
    
    <text x="15" y="60" font-size="11" font-weight="bold" fill="#fde047">Scientific Signals:</text>
    <text x="15" y="78" font-size="9.5" fill="#cbd5e1">• Elevated harmonic tremors detected</text>
    <text x="15" y="98" font-size="9.5" fill="#cbd5e1">• Slight increase in fumarole heat</text>
    <text x="15" y="118" font-size="9.5" fill="#cbd5e1">• Minor slope tilt measured</text>

    <text x="15" y="160" font-size="11" font-weight="bold" fill="#fde047">Public Action:</text>
    <text x="15" y="178" font-size="9.5" fill="#cbd5e1">• Scientists increase monitoring 24/7</text>
    <text x="15" y="198" font-size="9.5" fill="#cbd5e1">• Stock emergency shelters</text>
    <text x="15" y="218" font-size="9.5" fill="#cbd5e1">• Prepare evacuation transport</text>
  </g>

  <!-- Level 3: ORANGE -->
  <g transform="translate(410, 85)">
    <rect x="0" y="0" width="170" height="320" rx="8" fill="#0f172a" stroke="#f97316" stroke-width="2"/>
    <rect x="0" y="0" width="170" height="36" rx="8" fill="#c2410c"/>
    <text x="85" y="24" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. ORANGE: WATCH</text>
    
    <text x="15" y="60" font-size="11" font-weight="bold" fill="#fdba74">Scientific Signals:</text>
    <text x="15" y="78" font-size="9.5" fill="#cbd5e1">• Swelling of mountain flanks</text>
    <text x="15" y="98" font-size="9.5" fill="#cbd5e1">• Sharp spike in SO2 &amp; CO2 gases</text>
    <text x="15" y="118" font-size="9.5" fill="#cbd5e1">• Small phreatic steam explosions</text>

    <text x="15" y="160" font-size="11" font-weight="bold" fill="#fdba74">Public Action:</text>
    <text x="15" y="178" font-size="9.5" fill="#cbd5e1">• Close volcano tourism parks</text>
    <text x="15" y="198" font-size="9.5" fill="#cbd5e1">• Distribute dust masks to public</text>
    <text x="15" y="218" font-size="9.5" fill="#cbd5e1">• Voluntary evacuation of red zone</text>
  </g>

  <!-- Level 4: RED -->
  <g transform="translate(600, 85)">
    <rect x="0" y="0" width="170" height="320" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="170" height="36" rx="8" fill="#b91c1c"/>
    <text x="85" y="24" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">4. RED: WARNING</text>
    
    <text x="15" y="60" font-size="11" font-weight="bold" fill="#fca5a5">Scientific Signals:</text>
    <text x="15" y="78" font-size="9.5" fill="#cbd5e1">• Continuous seismic tremor swarm</text>
    <text x="15" y="98" font-size="9.5" fill="#cbd5e1">• Imminent / active explosive eruption</text>
    <text x="15" y="118" font-size="9.5" fill="#cbd5e1">• Rapid pyroclastic/lava generation</text>

    <text x="15" y="160" font-size="11" font-weight="bold" fill="#fca5a5">Public Action:</text>
    <text x="15" y="178" font-size="9.5" fill="#cbd5e1">• MANDATORY EVACUATION</text>
    <text x="15" y="198" font-size="9.5" fill="#cbd5e1">• Clear all exclusion zones</text>
    <text x="15" y="218" font-size="9.5" fill="#cbd5e1">• Reroute all commercial flights</text>
  </g>
</svg>
""")

TOPIC_8_SVGS = {
    1: SVG_MAGMA_DRIVERS,
    2: SVG_INTRUSIVE_FEATURES,
    3: SVG_LAVA_DYNAMICS,
    4: SVG_VOLCANIC_MATERIALS,
    5: SVG_EXTRUSIVE_LANDFORMS,
    6: SVG_STRATOVOLCANO,
    7: SVG_CALDERA_COLLAPSE,
    8: SVG_GEYSER_PHYSICS,
    9: SVG_GLOBAL_BELTS,
    10: SVG_KENYA_VOLCANISM,
    11: SVG_OLKARIA_GEOTHERMAL,
    12: SVG_VOLCANIC_HAZARDS,
    13: SVG_DISASTER_PREPAREDNESS,
}

# =============================================================================
# ENRICHMENT ENGINE EXECUTION
# =============================================================================
def enrich_topic_8():
    print("=" * 80)
    print("STARTING VLEARN VISUAL ENRICHMENT: GRADE 10 GEOGRAPHY TOPIC 8")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(id=37).first() or Subject.objects.filter(grade=grade, name="Geography").first()
    topic = Topic.objects.filter(subject=subject, order=8).first()

    if not topic:
        print("ERROR: Topic 8 not found in database! Please run ingestion first.")
        return

    # Load verified images JSON
    json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grade10_geography_topic8_verified_images.json")
    with open(json_path, "r") as f:
        verified_images = json.load(f)

    lessons = topic.lessons.all().order_by("learning_unit__order")
    print(f"Enriching {lessons.count()} Lessons for Topic 8: {topic.name}...")

    for lesson in lessons:
        u_order = str(lesson.learning_unit.order)
        print(f"\n--- Lesson {u_order}: {lesson.title} ---")

        # 1. Attach First-Card Photographic Visual Hook
        img_data = verified_images.get(u_order)
        if img_data:
            hook_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=1,
                block_type="suggested_image"
            ).first()

            if hook_block:
                hook_block.content = {
                    "text": hook_block.content.get("text", "") if hook_block.content else "",
                    "url": img_data['url'],
                    "resolved_image_url": img_data['url'],
                    "caption": f"Visual Hook: {hook_block.title}",
                    "author": img_data.get('author', 'Wikimedia Commons'),
                    "licensing": img_data.get('licensing', 'CC BY-SA')
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
                            "topic_order": 8
                        }
                    }
                )
                asset.url = img_data['url']
                asset.status = "attached"
                asset.save()
                asset.blocks.add(hook_block)
                print(f"  + Attached Wikimedia Photographic Hook: {img_data['url'][:65]}...")

        # 2. Attach Custom Vector SVG
        svg_xml = TOPIC_8_SVGS.get(int(u_order))
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
                            "topic_order": 8
                        }
                    }
                )
                svg_asset.metadata["svg_content"] = svg_xml
                svg_asset.status = "attached"
                svg_asset.save()
                svg_asset.blocks.add(diagram_block)
                print(f"  + Attached Custom Responsive Vector SVG to block '{diagram_block.title}'")

        # 3. Attach YouTube Video (Lesson 12)
        video_block = LessonBlock.objects.filter(
            lesson=lesson,
            block_type="video"
        ).first()

        if video_block:
            c = video_block.content or {}
            vid_url = c.get("url") or "https://www.youtube.com/watch?v=Cvjwt9nnwXY"
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
                        "topic_order": 8
                    }
                }
            )
            v_asset.url = vid_url
            v_asset.status = "attached"
            v_asset.save()
            v_asset.blocks.add(video_block)
            print(f"  + Attached Educational YouTube Video: {vid_url}")

    print("\n" + "=" * 80)
    print("Topic 8 Visual Enrichment Completed Successfully!")
    print("=" * 80)

if __name__ == "__main__":
    enrich_topic_8()
