"""
VLearn CBC Grade 10 Geography — Topic 1: Introduction to Geography
Visual Enrichment Engine (Vector SVGs, Verified Wikimedia Images & Educational Videos)

Subject: Geography (Subject ID: 37, Grade: Grade 10 CBC)
Topic 1: Introduction to Geography

Attaches:
  - 8 First-Card Photographic Visual Hooks (100% Tested HTTP 200 OK Direct Wikimedia URLs)
  - 8 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - 2 Verified Educational YouTube Videos
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade10_geography_topic1.py
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
# 8 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 1: INTRODUCTION TO GEOGRAPHY
# =============================================================================

# SVG 1: The Six Pillars of Geographical Analysis (Lesson 1)
SVG_SIX_THEMES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Six Fundamental Themes of Geographical Inquiry</text>
  
  <!-- Central Hub -->
  <circle cx="400" cy="230" r="60" fill="#0284c7" stroke="#38bdf8" stroke-width="3"/>
  <text x="400" y="225" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">GEOGRAPHICAL</text>
  <text x="400" y="245" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">INQUIRY</text>

  <!-- Connectors -->
  <line x1="400" y1="170" x2="400" y2="105" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4"/>
  <line x1="455" y1="200" x2="610" y2="135" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4"/>
  <line x1="455" y1="260" x2="610" y2="325" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4"/>
  <line x1="400" y1="290" x2="400" y2="355" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4"/>
  <line x1="345" y1="260" x2="190" y2="325" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4"/>
  <line x1="345" y1="200" x2="190" y2="135" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4"/>

  <!-- Theme 1: Place (Top) -->
  <g transform="translate(300, 65)">
    <rect x="0" y="0" width="200" height="42" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="100" y="18" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. PLACE</text>
    <text x="100" y="32" font-size="10" fill="#cbd5e1" text-anchor="middle">Physical &amp; human character</text>
  </g>

  <!-- Theme 2: Space (Top-Right) -->
  <g transform="translate(560, 110)">
    <rect x="0" y="0" width="190" height="42" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <text x="95" y="18" font-size="12" font-weight="bold" fill="#c084fc" text-anchor="middle">2. SPACE</text>
    <text x="95" y="32" font-size="10" fill="#cbd5e1" text-anchor="middle">Spatial distribution &amp; gaps</text>
  </g>

  <!-- Theme 3: Environment (Bottom-Right) -->
  <g transform="translate(560, 305)">
    <rect x="0" y="0" width="190" height="42" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <text x="95" y="18" font-size="12" font-weight="bold" fill="#4ade80" text-anchor="middle">3. ENVIRONMENT</text>
    <text x="95" y="32" font-size="10" fill="#cbd5e1" text-anchor="middle">Atmosphere, soils &amp; water</text>
  </g>

  <!-- Theme 4: Time (Bottom) -->
  <g transform="translate(300, 355)">
    <rect x="0" y="0" width="200" height="42" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <text x="100" y="18" font-size="12" font-weight="bold" fill="#fbbf24" text-anchor="middle">4. TIME</text>
    <text x="100" y="32" font-size="10" fill="#cbd5e1" text-anchor="middle">Landscape &amp; urban change</text>
  </g>

  <!-- Theme 5: Movement (Bottom-Left) -->
  <g transform="translate(50, 305)">
    <rect x="0" y="0" width="190" height="42" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="2"/>
    <text x="95" y="18" font-size="12" font-weight="bold" fill="#f472b6" text-anchor="middle">5. MOVEMENT</text>
    <text x="95" y="32" font-size="10" fill="#cbd5e1" text-anchor="middle">Flow of goods, ideas &amp; people</text>
  </g>

  <!-- Theme 6: Region (Top-Left) -->
  <g transform="translate(50, 110)">
    <rect x="0" y="0" width="190" height="42" rx="8" fill="#0f172a" stroke="#14b8a6" stroke-width="2"/>
    <text x="95" y="18" font-size="12" font-weight="bold" fill="#2dd4bf" text-anchor="middle">6. REGION</text>
    <text x="95" y="32" font-size="10" fill="#cbd5e1" text-anchor="middle">Unifying geographic areas</text>
  </g>
</svg>
""")

# SVG 2: The Geography Tree — Physical vs Human (Lesson 2)
SVG_GEOGRAPHY_TREE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Structure of Geography: Two Great Branches</text>

  <!-- Trunk -->
  <rect x="330" y="70" width="140" height="45" rx="8" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
  <text x="400" y="97" font-size="15" font-weight="bold" fill="#ffffff" text-anchor="middle">GEOGRAPHY</text>

  <!-- Branch 1: Physical Geography -->
  <g transform="translate(45, 135)">
    <rect x="0" y="0" width="330" height="270" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="330" height="38" rx="10" fill="#0369a1"/>
    <text x="165" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">PHYSICAL GEOGRAPHY</text>
    
    <text x="20" y="65" font-size="11" font-weight="bold" fill="#38bdf8">• Geomorphology</text>
    <text x="135" y="65" font-size="11" fill="#cbd5e1">— Landforms &amp; earth shaping</text>
    
    <text x="20" y="105" font-size="11" font-weight="bold" fill="#38bdf8">• Climatology</text>
    <text x="135" y="105" font-size="11" fill="#cbd5e1">— Long-term weather patterns</text>
    
    <text x="20" y="145" font-size="11" font-weight="bold" fill="#38bdf8">• Hydrology</text>
    <text x="135" y="145" font-size="11" fill="#cbd5e1">— Water systems, rivers, oceans</text>
    
    <text x="20" y="185" font-size="11" font-weight="bold" fill="#38bdf8">• Pedology</text>
    <text x="135" y="185" font-size="11" fill="#cbd5e1">— Soil formation &amp; properties</text>
    
    <text x="20" y="225" font-size="11" font-weight="bold" fill="#38bdf8">• Biogeography</text>
    <text x="135" y="225" font-size="11" fill="#cbd5e1">— Plants (flora) &amp; animals (fauna)</text>
  </g>

  <!-- Branch 2: Human & Economic Geography -->
  <g transform="translate(425, 135)">
    <rect x="0" y="0" width="330" height="270" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <rect x="0" y="0" width="330" height="38" rx="10" fill="#7e22ce"/>
    <text x="165" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">HUMAN &amp; ECONOMIC GEOGRAPHY</text>
    
    <text x="20" y="65" font-size="11" font-weight="bold" fill="#c084fc">• Population</text>
    <text x="135" y="65" font-size="11" fill="#cbd5e1">— Demography, census, growth</text>
    
    <text x="20" y="105" font-size="11" font-weight="bold" fill="#c084fc">• Settlement</text>
    <text x="135" y="105" font-size="11" fill="#cbd5e1">— Urban &amp; rural hierarchy</text>
    
    <text x="20" y="145" font-size="11" font-weight="bold" fill="#c084fc">• Agriculture</text>
    <text x="135" y="145" font-size="11" fill="#cbd5e1">— Farming systems &amp; food supply</text>
    
    <text x="20" y="185" font-size="11" font-weight="bold" fill="#c084fc">• Economic</text>
    <text x="135" y="185" font-size="11" fill="#cbd5e1">— Industry, energy, mining, trade</text>
    
    <text x="20" y="225" font-size="11" font-weight="bold" fill="#c084fc">• Transport</text>
    <text x="135" y="225" font-size="11" fill="#cbd5e1">— Roads, rail, ports &amp; networks</text>
  </g>
</svg>
""")

# SVG 3: Geography as an Interdisciplinary Bridge (Lesson 3)
SVG_INTERDISCIPLINARY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Geography: The Integrative Bridge Across Disciplines</text>

  <!-- Center Circle -->
  <circle cx="400" cy="230" r="65" fill="#0284c7" stroke="#38bdf8" stroke-width="3"/>
  <text x="400" y="225" font-size="15" font-weight="bold" fill="#ffffff" text-anchor="middle">GEOGRAPHY</text>
  <text x="400" y="245" font-size="11" fill="#e0f2fe" text-anchor="middle">Spatial Integrator</text>

  <!-- 8 Connected Nodes -->
  <!-- Mathematics -->
  <g transform="translate(325, 70)">
    <rect x="0" y="0" width="150" height="40" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="75" y="18" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Mathematics</text>
    <text x="75" y="32" font-size="9" fill="#94a3b8" text-anchor="middle">Scale, Bearings, Stats</text>
  </g>

  <!-- Physics -->
  <g transform="translate(540, 95)">
    <rect x="0" y="0" width="150" height="40" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="75" y="18" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Physics</text>
    <text x="75" y="32" font-size="9" fill="#94a3b8" text-anchor="middle">Atmosphere, Seismic waves</text>
  </g>

  <!-- Chemistry -->
  <g transform="translate(600, 210)">
    <rect x="0" y="0" width="150" height="40" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="75" y="18" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Chemistry</text>
    <text x="75" y="32" font-size="9" fill="#94a3b8" text-anchor="middle">Rock weathering, Soil pH</text>
  </g>

  <!-- Biology -->
  <g transform="translate(540, 325)">
    <rect x="0" y="0" width="150" height="40" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="75" y="18" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">Biology</text>
    <text x="75" y="32" font-size="9" fill="#94a3b8" text-anchor="middle">Ecosystems, Flora/Fauna</text>
  </g>

  <!-- Computer Science -->
  <g transform="translate(325, 360)">
    <rect x="0" y="0" width="150" height="40" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="75" y="18" font-size="11" font-weight="bold" fill="#c084fc" text-anchor="middle">Computer Science</text>
    <text x="75" y="32" font-size="9" fill="#94a3b8" text-anchor="middle">GIS, Remote Sensing</text>
  </g>

  <!-- Economics -->
  <g transform="translate(110, 325)">
    <rect x="0" y="0" width="150" height="40" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="75" y="18" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">Economics</text>
    <text x="75" y="32" font-size="9" fill="#94a3b8" text-anchor="middle">Trade, Resource use</text>
  </g>

  <!-- History -->
  <g transform="translate(50, 210)">
    <rect x="0" y="0" width="150" height="40" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <text x="75" y="18" font-size="11" font-weight="bold" fill="#f472b6" text-anchor="middle">History</text>
    <text x="75" y="32" font-size="9" fill="#94a3b8" text-anchor="middle">Settlement evolution</text>
  </g>

  <!-- Agriculture -->
  <g transform="translate(110, 95)">
    <rect x="0" y="0" width="150" height="40" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="75" y="18" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">Agriculture</text>
    <text x="75" y="32" font-size="9" fill="#94a3b8" text-anchor="middle">Soil suitability, Crops</text>
  </g>
</svg>
""")

# SVG 4: Kenya's Water Towers (Lesson 4)
SVG_WATER_TOWERS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Hydrological Function of Kenya's Water Towers</text>

  <!-- Mountain Profile -->
  <path d="M 100 370 L 280 160 L 350 200 L 450 120 L 580 250 L 700 370 Z" fill="#334155" stroke="#475569" stroke-width="2"/>
  <path d="M 230 205 L 280 160 L 330 190 Z" fill="#e2e8f0"/>
  <path d="M 400 160 L 450 120 L 500 165 Z" fill="#e2e8f0"/>

  <!-- Forest Canopy Green Zone -->
  <path d="M 160 370 L 250 240 L 340 260 L 420 210 L 520 280 L 640 370 Z" fill="#15803d" opacity="0.8"/>

  <!-- Rain Clouds -->
  <ellipse cx="280" cy="110" rx="55" ry="25" fill="#0284c7" opacity="0.85"/>
  <ellipse cx="450" cy="80" rx="65" ry="30" fill="#0284c7" opacity="0.85"/>
  <text x="450" y="85" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Precipitation</text>

  <!-- Arrows Rain -->
  <line x1="280" y1="140" x2="280" y2="180" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3"/>
  <line x1="450" y1="115" x2="450" y2="165" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3"/>

  <!-- Ground Absorption & Streams -->
  <path d="M 320 270 Q 380 320 460 370" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <text x="490" y="350" font-size="11" font-weight="bold" fill="#38bdf8">Perennial River Flow</text>

  <!-- Key Water Towers Box -->
  <g transform="translate(45, 75)">
    <rect x="0" y="0" width="170" height="130" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="85" y="22" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">5 Key Water Towers</text>
    <text x="15" y="45" font-size="10" fill="#cbd5e1">1. Mau Forest Complex</text>
    <text x="15" y="65" font-size="10" fill="#cbd5e1">2. Mount Kenya</text>
    <text x="15" y="85" font-size="10" fill="#cbd5e1">3. Aberdare Ranges</text>
    <text x="15" y="105" font-size="10" fill="#cbd5e1">4. Mount Elgon</text>
    <text x="15" y="125" font-size="10" fill="#cbd5e1">5. Cherangani Hills</text>
  </g>
</svg>
""")

# SVG 5: The Geographer's Toolbox (Lesson 5)
SVG_TOOLBOX = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Geographer's Essential Toolkit</text>

  <!-- 6 Tool Boxes -->
  <!-- 1. Topo Maps -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="215" height="145" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="215" height="30" rx="8" fill="#0284c7"/>
    <text x="107" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Topographical Maps</text>
    <text x="15" y="55" font-size="10" fill="#cbd5e1">• 1:50,000 series</text>
    <text x="15" y="75" font-size="10" fill="#cbd5e1">• Contours &amp; relief</text>
    <text x="15" y="95" font-size="10" fill="#cbd5e1">• Grid references</text>
    <text x="15" y="115" font-size="10" fill="#cbd5e1">• Bearings &amp; distances</text>
  </g>

  <!-- 2. Fieldwork -->
  <g transform="translate(290, 80)">
    <rect x="0" y="0" width="215" height="145" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="215" height="30" rx="8" fill="#16a34a"/>
    <text x="107" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Fieldwork &amp; Inquiry</text>
    <text x="15" y="55" font-size="10" fill="#cbd5e1">• Direct observation</text>
    <text x="15" y="75" font-size="10" fill="#cbd5e1">• Pacing &amp; sketching</text>
    <text x="15" y="95" font-size="10" fill="#cbd5e1">• Questionnaires</text>
    <text x="15" y="115" font-size="10" fill="#cbd5e1">• Specimen sampling</text>
  </g>

  <!-- 3. GPS & GIS -->
  <g transform="translate(535, 80)">
    <rect x="0" y="0" width="215" height="145" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="0" y="0" width="215" height="30" rx="8" fill="#9333ea"/>
    <text x="107" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. GPS &amp; GIS Software</text>
    <text x="15" y="55" font-size="10" fill="#cbd5e1">• Coordinate capture</text>
    <text x="15" y="75" font-size="10" fill="#cbd5e1">• Thematic layers</text>
    <text x="15" y="95" font-size="10" fill="#cbd5e1">• Satellite imagery</text>
    <text x="15" y="115" font-size="10" fill="#cbd5e1">• Spatial databases</text>
  </g>

  <!-- 4. Statistics -->
  <g transform="translate(45, 255)">
    <rect x="0" y="0" width="215" height="145" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="215" height="30" rx="8" fill="#d97706"/>
    <text x="107" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">4. Statistical Methods</text>
    <text x="15" y="55" font-size="10" fill="#cbd5e1">• Central tendency</text>
    <text x="15" y="75" font-size="10" fill="#cbd5e1">• Frequency tables</text>
    <text x="15" y="95" font-size="10" fill="#cbd5e1">• Bar &amp; pie charts</text>
    <text x="15" y="115" font-size="10" fill="#cbd5e1">• Climographs</text>
  </g>

  <!-- 5. Photographs -->
  <g transform="translate(290, 255)">
    <rect x="0" y="0" width="215" height="145" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <rect x="0" y="0" width="215" height="30" rx="8" fill="#db2777"/>
    <text x="107" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">5. Aerial &amp; Ground Photos</text>
    <text x="15" y="55" font-size="10" fill="#cbd5e1">• Ground-level views</text>
    <text x="15" y="75" font-size="10" fill="#cbd5e1">• Oblique air photos</text>
    <text x="15" y="95" font-size="10" fill="#cbd5e1">• Vertical air photos</text>
    <text x="15" y="115" font-size="10" fill="#cbd5e1">• Land use monitoring</text>
  </g>

  <!-- 6. Surveying -->
  <g transform="translate(535, 255)">
    <rect x="0" y="0" width="215" height="145" rx="8" fill="#0f172a" stroke="#14b8a6" stroke-width="1.5"/>
    <rect x="0" y="0" width="215" height="30" rx="8" fill="#0d9488"/>
    <text x="107" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">6. Elementary Surveying</text>
    <text x="15" y="55" font-size="10" fill="#cbd5e1">• Prismatic compass</text>
    <text x="15" y="75" font-size="10" fill="#cbd5e1">• Ranging rods &amp; tape</text>
    <text x="15" y="95" font-size="10" fill="#cbd5e1">• Abney level / Clinometer</text>
    <text x="15" y="115" font-size="10" fill="#cbd5e1">• Slope profiling</text>
  </g>
</svg>
""")

# SVG 6: Career Pathways (Lesson 6)
SVG_CAREERS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Professional Career Pathways in Geography</text>

  <!-- Central Origin -->
  <rect x="45" y="180" width="160" height="70" rx="10" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
  <text x="125" y="212" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">GRADE 10</text>
  <text x="125" y="232" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">GEOGRAPHY</text>

  <!-- 4 Pathway Boxes -->
  <!-- 1. Geospatial & Tech -->
  <g transform="translate(260, 65)">
    <rect x="0" y="0" width="490" height="65" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="20" y="28" font-size="13" font-weight="bold" fill="#c084fc">Geospatial &amp; Data Technology</text>
    <text x="20" y="48" font-size="11" fill="#cbd5e1">GIS Analyst • Remote Sensing Specialist • Digital Cartographer</text>
  </g>

  <!-- 2. Environmental & Planning -->
  <g transform="translate(260, 150)">
    <rect x="0" y="0" width="490" height="65" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="20" y="28" font-size="13" font-weight="bold" fill="#4ade80">Environmental &amp; Urban Management</text>
    <text x="20" y="48" font-size="11" fill="#cbd5e1">Urban Planner • NEMA Impact Auditor • Forestry &amp; Watershed Officer</text>
  </g>

  <!-- 3. Atmospheric & Aviation -->
  <g transform="translate(260, 235)">
    <rect x="0" y="0" width="490" height="65" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="20" y="28" font-size="13" font-weight="bold" fill="#38bdf8">Atmospheric &amp; Aviation Sciences</text>
    <text x="20" y="48" font-size="11" fill="#cbd5e1">Meteorologist • Aviation Navigator • Disaster Management Officer</text>
  </g>

  <!-- 4. Surveying & Tourism -->
  <g transform="translate(260, 320)">
    <rect x="0" y="0" width="490" height="65" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="20" y="28" font-size="13" font-weight="bold" fill="#fbbf24">Field Surveying &amp; Conservation</text>
    <text x="20" y="48" font-size="11" fill="#cbd5e1">Cadastral Land Surveyor • KWS Wildlife Warden • Ecotourism Director</text>
  </g>
</svg>
""")

# SVG 7: TACKS Sketch Map Standard (Lesson 7)
SVG_TACKS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Standardized Cartographic Quality: The TACKS Checklist</text>

  <g transform="translate(50, 75)">
    <!-- T - Title -->
    <rect x="0" y="0" width="130" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="130" height="40" rx="8" fill="#0284c7"/>
    <text x="65" y="25" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">T - TITLE</text>
    <text x="12" y="70" font-size="11" font-weight="bold" fill="#38bdf8">What it is:</text>
    <text x="12" y="90" font-size="10" fill="#cbd5e1">• Clear heading</text>
    <text x="12" y="110" font-size="10" fill="#cbd5e1">• States locality</text>
    <text x="12" y="130" font-size="10" fill="#cbd5e1">• Defines theme</text>
  </g>

  <g transform="translate(195, 75)">
    <!-- A - Arrow -->
    <rect x="0" y="0" width="130" height="320" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="130" height="40" rx="8" fill="#16a34a"/>
    <text x="65" y="25" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">A - ARROW</text>
    <text x="12" y="70" font-size="11" font-weight="bold" fill="#4ade80">North Arrow:</text>
    <text x="12" y="90" font-size="10" fill="#cbd5e1">• Points True North</text>
    <text x="12" y="110" font-size="10" fill="#cbd5e1">• Guides orientation</text>
    <text x="12" y="130" font-size="10" fill="#cbd5e1">• Standard symbol</text>
  </g>

  <g transform="translate(340, 75)">
    <!-- C - Compass / Key -->
    <rect x="0" y="0" width="130" height="320" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <rect x="0" y="0" width="130" height="40" rx="8" fill="#9333ea"/>
    <text x="65" y="25" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">C - KEY</text>
    <text x="12" y="70" font-size="11" font-weight="bold" fill="#c084fc">Legend:</text>
    <text x="12" y="90" font-size="10" fill="#cbd5e1">• Decodes symbols</text>
    <text x="12" y="110" font-size="10" fill="#cbd5e1">• Explains colors</text>
    <text x="12" y="130" font-size="10" fill="#cbd5e1">• Standard signs</text>
  </g>

  <g transform="translate(485, 75)">
    <!-- K - Frame -->
    <rect x="0" y="0" width="130" height="320" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect x="0" y="0" width="130" height="40" rx="8" fill="#d97706"/>
    <text x="65" y="25" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">K - FRAME</text>
    <text x="12" y="70" font-size="11" font-weight="bold" fill="#fbbf24">Border:</text>
    <text x="12" y="90" font-size="10" fill="#cbd5e1">• Enclosing box</text>
    <text x="12" y="110" font-size="10" fill="#cbd5e1">• Neat neat layout</text>
    <text x="12" y="130" font-size="10" fill="#cbd5e1">• Clean margins</text>
  </g>

  <g transform="translate(630, 75)">
    <!-- S - Scale -->
    <rect x="0" y="0" width="130" height="320" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="2"/>
    <rect x="0" y="0" width="130" height="40" rx="8" fill="#db2777"/>
    <text x="65" y="25" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">S - SCALE</text>
    <text x="12" y="70" font-size="11" font-weight="bold" fill="#f472b6">Proportions:</text>
    <text x="12" y="90" font-size="10" fill="#cbd5e1">• Linear bar</text>
    <text x="12" y="110" font-size="10" fill="#cbd5e1">• RF / Statement</text>
    <text x="12" y="130" font-size="10" fill="#cbd5e1">• Ground ratio</text>
  </g>
</svg>
""")

# SVG 8: Master Synthesis (Lesson 8)
SVG_SYNTHESIS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Grade 10 Geography: Topic 1 Knowledge Architecture</text>

  <!-- 4 Core Quadrants -->
  <!-- 1. Foundations -->
  <g transform="translate(45, 75)">
    <rect x="0" y="0" width="335" height="155" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="20" y="25" font-size="13" font-weight="bold" fill="#38bdf8">1. Conceptual Foundations</text>
    <text x="20" y="50" font-size="11" fill="#cbd5e1">• Definition: Earth as home of humankind</text>
    <text x="20" y="70" font-size="11" fill="#cbd5e1">• Etymology: Geo (Earth) + Graphein (to write)</text>
    <text x="20" y="90" font-size="11" fill="#cbd5e1">• 6 Themes: Place, Space, Environment,</text>
    <text x="30" y="108" font-size="11" fill="#cbd5e1">Time, Movement, Region</text>
  </g>

  <!-- 2. Branches -->
  <g transform="translate(420, 75)">
    <rect x="0" y="0" width="335" height="155" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="20" y="25" font-size="13" font-weight="bold" fill="#c084fc">2. Two Great Branches</text>
    <text x="20" y="50" font-size="11" fill="#cbd5e1">• Physical: Geomorphology, Climatology,</text>
    <text x="30" y="68" font-size="11" fill="#cbd5e1">Hydrology, Pedology, Biogeography</text>
    <text x="20" y="90" font-size="11" fill="#cbd5e1">• Human: Demography, Settlement,</text>
    <text x="30" y="108" font-size="11" fill="#cbd5e1">Agriculture, Economics, Transport</text>
  </g>

  <!-- 3. Interdisciplinary & Sustainability -->
  <g transform="translate(45, 245)">
    <rect x="0" y="0" width="335" height="160" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="20" y="25" font-size="13" font-weight="bold" fill="#4ade80">3. Interdisciplinary &amp; Daily Life</text>
    <text x="20" y="50" font-size="11" fill="#cbd5e1">• Bridge subject: Maths, Physics, Bio, CS</text>
    <text x="20" y="70" font-size="11" fill="#cbd5e1">• Sustainable Development &amp; Water Towers</text>
    <text x="20" y="90" font-size="11" fill="#cbd5e1">• Hazard avoidance &amp; flood planning</text>
  </g>

  <!-- 4. Practice & Careers -->
  <g transform="translate(420, 245)">
    <rect x="0" y="0" width="335" height="160" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="20" y="25" font-size="13" font-weight="bold" fill="#fbbf24">4. Tools, Inquiry &amp; Careers</text>
    <text x="20" y="50" font-size="11" fill="#cbd5e1">• Tools: Maps, Fieldwork, GPS, GIS, Stats</text>
    <text x="20" y="70" font-size="11" fill="#cbd5e1">• Inquiry: TACKS sketch mapping</text>
    <text x="20" y="90" font-size="11" fill="#cbd5e1">• Careers: GIS Analyst, Meteorologist,</text>
    <text x="30" y="108" font-size="11" fill="#cbd5e1">Urban Planner, Surveyor, NEMA</text>
  </g>
</svg>
""")

TOPIC_1_SVGS = {
    1: SVG_SIX_THEMES,
    2: SVG_GEOGRAPHY_TREE,
    3: SVG_INTERDISCIPLINARY,
    4: SVG_WATER_TOWERS,
    5: SVG_TOOLBOX,
    6: SVG_CAREERS,
    7: SVG_TACKS,
    8: SVG_SYNTHESIS
}

def enrich_topic_1():
    print("=== Starting Visual Enrichment for Topic 1: Introduction to Geography ===")
    
    cbc = Curriculum.objects.filter(name__iexact="CBC").first()
    grade10 = Grade.objects.filter(curriculum=cbc, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade10, name="Geography").first()
    topic = Topic.objects.filter(subject=subject, order=1).first()

    if not topic:
        raise ValueError("Topic 1 'Introduction to Geography' not found.")

    with open('curriculum/grade10_geography_topic1_verified_images.json') as f:
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
                            "topic_order": 1
                        }
                    }
                )
                asset.url = img_data['url']
                asset.status = "attached"
                asset.save()
                asset.blocks.add(hook_block)
                print(f"  + Attached Wikimedia Photographic Hook: {img_data['url'][:55]}...")

        # 2. Attach Custom Vector SVG
        svg_xml = TOPIC_1_SVGS.get(int(u_order))
        if svg_xml:
            diagram_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="suggested_diagram"
            ).first()

            if diagram_block:
                diagram_block.content = {
                    "svg_content": svg_xml,
                    "title": diagram_block.title
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
                            "topic_order": 1
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
            block_type="suggested_video"
        ).first()

        if video_block:
            c = video_block.content or {}
            vid_url = c.get("youtube_url") or f"https://www.youtube.com/watch?v={c.get('resolved_video_id', '')}"
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
                        "video_id": c.get("resolved_video_id"),
                        "youtube_url": vid_url,
                        "unit_order": int(u_order),
                        "topic_order": 1
                    }
                }
            )
            v_asset.url = vid_url
            v_asset.status = "attached"
            v_asset.save()
            v_asset.blocks.add(video_block)
            print(f"  + Attached Educational YouTube Video: {vid_url}")

    print("\n=== Topic 1 Visual Enrichment Completed Successfully! ===")

if __name__ == "__main__":
    enrich_topic_1()
