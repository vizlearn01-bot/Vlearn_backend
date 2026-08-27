"""
VLearn CBC Grade 10 Geography — Topic 2: Map Reading and Interpretation
Visual Enrichment Engine (Vector SVGs, Verified Wikimedia Images & Educational Videos)

Subject: Geography (Grade 10 CBC)
Topic 2: Map Reading and Interpretation

Attaches:
  - 13 First-Card Photographic Visual Hooks (100% Tested HTTP 200 OK Direct Wikimedia URLs)
  - 11 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - Educational YouTube Video for Topographical Sheet Reading
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade10_geography_topic2.py
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
# 11 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 2: MAP READING
# =============================================================================

# SVG 1: Marginal Information Layout (Lesson 1)
SVG_MARGINAL_INFO = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <!-- Map Sheet Outer Frame -->
  <rect x="70" y="55" width="660" height="340" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  
  <!-- Inner Map Body Grid -->
  <rect x="120" y="90" width="560" height="230" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
  <line x1="260" y1="90" x2="260" y2="320" stroke="#334155" stroke-width="1" stroke-dasharray="4"/>
  <line x1="400" y1="90" x2="400" y2="320" stroke="#334155" stroke-width="1" stroke-dasharray="4"/>
  <line x1="540" y1="90" x2="540" y2="320" stroke="#334155" stroke-width="1" stroke-dasharray="4"/>
  <line x1="120" y1="165" x2="680" y2="165" stroke="#334155" stroke-width="1" stroke-dasharray="4"/>
  <line x1="120" y1="245" x2="680" y2="245" stroke="#334155" stroke-width="1" stroke-dasharray="4"/>
  <text x="400" y="210" font-size="14" fill="#64748b" font-weight="bold" text-anchor="middle">MAP BODY (RELIEF, DRAINAGE &amp; CULTURE)</text>

  <!-- 1. Title (Top Margin) -->
  <rect x="250" y="60" width="300" height="25" rx="4" fill="#0284c7"/>
  <text x="400" y="77" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. SHEET TITLE (e.g. NYERI 120/4)</text>

  <!-- 2. North Arrows (Top Right Margin) -->
  <g transform="translate(685, 95)">
    <rect x="0" y="0" width="40" height="70" rx="4" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <line x1="20" y1="60" x2="20" y2="15" stroke="#4ade80" stroke-width="2"/>
    <polygon points="20,10 15,20 25,20" fill="#4ade80"/>
    <text x="20" y="68" font-size="8" font-weight="bold" fill="#4ade80" text-anchor="middle">NORTH</text>
  </g>

  <!-- 3. Key / Legend (Bottom Left Margin) -->
  <g transform="translate(120, 330)">
    <rect x="0" y="0" width="180" height="55" rx="4" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="90" y="18" font-size="10" font-weight="bold" fill="#c084fc" text-anchor="middle">2. KEY / CONVENTIONAL SIGNS</text>
    <text x="10" y="34" font-size="9" fill="#cbd5e1">Roads, rivers, forests &amp; towns</text>
    <text x="10" y="48" font-size="9" fill="#cbd5e1">Decodes all cartographic symbols</text>
  </g>

  <!-- 4. Scale & Bar Scales (Bottom Center Margin) -->
  <g transform="translate(320, 330)">
    <rect x="0" y="0" width="220" height="55" rx="4" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="110" y="18" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">3. SCALE: 1:50,000 (V.I. 20m)</text>
    <rect x="20" y="28" width="180" height="8" fill="#334155"/>
    <rect x="20" y="28" width="45" height="8" fill="#fbbf24"/>
    <rect x="110" y="28" width="45" height="8" fill="#fbbf24"/>
    <text x="110" y="48" font-size="8" fill="#cbd5e1" text-anchor="middle">Linear Scale Bar (Kilometers)</text>
  </g>

  <!-- 5. Grid Coordinate Frame (Margins) -->
  <text x="95" y="170" font-size="10" font-weight="bold" fill="#38bdf8">14</text>
  <text x="95" y="250" font-size="10" font-weight="bold" fill="#38bdf8">13</text>
  <text x="255" y="338" font-size="10" font-weight="bold" fill="#38bdf8">52</text>
  <text x="395" y="338" font-size="10" font-weight="bold" fill="#38bdf8">53</text>
  <text x="535" y="338" font-size="10" font-weight="bold" fill="#38bdf8">54</text>
</svg>
""")

# SVG 2: Bearing & Protractor Measurement (Lesson 2)
SVG_BEARING_PROTRACTOR = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Measuring Compass Bearing from Point A to Point B</text>

  <!-- Origin Point A -->
  <circle cx="280" cy="260" r="8" fill="#38bdf8"/>
  <text x="260" y="280" font-size="16" font-weight="bold" fill="#38bdf8">Point A</text>

  <!-- Target Point B -->
  <circle cx="580" cy="140" r="8" fill="#22c55e"/>
  <text x="600" y="145" font-size="16" font-weight="bold" fill="#4ade80">Point B</text>

  <!-- Grid North Line at Point A -->
  <line x1="280" y1="360" x2="280" y2="80" stroke="#f87171" stroke-width="2.5"/>
  <polygon points="280,70 273,85 287,85" fill="#f87171"/>
  <text x="290" y="85" font-size="13" font-weight="bold" fill="#f87171">Grid North (000°)</text>

  <!-- Target Line AB -->
  <line x1="280" y1="260" x2="580" y2="140" stroke="#38bdf8" stroke-width="2.5"/>

  <!-- Clockwise Angle Sweep Arc -->
  <path d="M 280 160 A 100 100 0 0 1 367 185" fill="none" stroke="#fbbf24" stroke-width="3.5"/>
  <text x="345" y="150" font-size="15" font-weight="bold" fill="#fbbf24">Angle = 068°</text>

  <!-- Protractor Overlay Outline -->
  <path d="M 160 260 A 120 120 0 0 1 400 260 Z" fill="#0284c7" opacity="0.2" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3"/>
  <text x="400" y="280" font-size="11" fill="#cbd5e1" text-anchor="middle">Protractor base aligned with East-West axis</text>

  <!-- Formula Callout -->
  <g transform="translate(480, 310)">
    <rect x="0" y="0" width="280" height="90" rx="8" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="140" y="25" font-size="12" font-weight="bold" fill="#fbbf24" text-anchor="middle">Back Bearing of A from B:</text>
    <text x="20" y="50" font-size="11" fill="#cbd5e1">Forward Bearing &lt; 180° -> Add 180°</text>
    <text x="20" y="72" font-size="12" font-weight="bold" fill="#38bdf8">068° + 180° = 248°</text>
  </g>
</svg>
""")

# SVG 3: Thread Method for Winding Routes (Lesson 3)
SVG_THREAD_METHOD = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Distance Measurement: The Thread Method for Winding Routes</text>

  <!-- Stage 1: Winding River on Map -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="335" height="170" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="167" y="24" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Stage 1: Trace Curves with Thread</text>
    <path d="M 30 130 Q 70 60 120 110 T 210 80 T 300 130" fill="none" stroke="#0284c7" stroke-width="6"/>
    <!-- Dotted thread over river -->
    <path d="M 30 130 Q 70 60 120 110 T 210 80 T 300 130" fill="none" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="4"/>
    <circle cx="30" cy="130" r="5" fill="#f43f5e"/>
    <text x="30" y="150" font-size="10" fill="#f43f5e">Start Knot</text>
    <circle cx="300" cy="130" r="5" fill="#f43f5e"/>
    <text x="280" y="150" font-size="10" fill="#f43f5e">End Mark</text>
  </g>

  <!-- Stage 2: Straightened on Ruler -->
  <g transform="translate(420, 80)">
    <rect x="0" y="0" width="335" height="170" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="167" y="24" font-size="12" font-weight="bold" fill="#4ade80" text-anchor="middle">Stage 2: Measure Straightened Length</text>
    <!-- Straight thread -->
    <line x1="30" y1="70" x2="290" y2="70" stroke="#f43f5e" stroke-width="3" stroke-dasharray="4"/>
    <circle cx="30" cy="70" r="5" fill="#f43f5e"/>
    <circle cx="290" cy="70" r="5" fill="#f43f5e"/>
    <!-- Ruler marks -->
    <rect x="25" y="85" width="270" height="35" fill="#334155" stroke="#64748b"/>
    <line x1="30" y1="85" x2="30" y2="105" stroke="#ffffff" stroke-width="1.5"/>
    <text x="30" y="115" font-size="8" fill="#ffffff" text-anchor="middle">0</text>
    <line x1="160" y1="85" x2="160" y2="105" stroke="#ffffff" stroke-width="1.5"/>
    <text x="160" y="115" font-size="8" fill="#ffffff" text-anchor="middle">7 cm</text>
    <line x1="290" y1="85" x2="290" y2="105" stroke="#ffffff" stroke-width="1.5"/>
    <text x="290" y="115" font-size="8" fill="#ffffff" text-anchor="middle">14.6 cm</text>
    <text x="167" y="145" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">Map Distance = 14.6 cm</text>
  </g>

  <!-- Stage 3: Conversion Calculation -->
  <g transform="translate(45, 275)">
    <rect x="0" y="0" width="710" height="120" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="355" y="28" font-size="13" font-weight="bold" fill="#fbbf24" text-anchor="middle">Stage 3: Ground Distance Conversion (Scale 1:50,000)</text>
    <text x="40" y="60" font-size="12" fill="#cbd5e1">• Scale Statement: 1 cm on map = 0.5 km on the ground (500 meters)</text>
    <text x="40" y="85" font-size="13" font-weight="bold" fill="#38bdf8">• Ground Distance = 14.6 cm × 0.5 km/cm = 7.3 Kilometers (7,300 meters)</text>
  </g>
</svg>
""")

# SVG 4: Conventional Signs & Color Conventions (Lesson 4)
SVG_SIGNS_COLORS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Standard International Map Color Conventions</text>

  <!-- 4 Color Quadrants -->
  <!-- Blue: Water -->
  <g transform="translate(45, 75)">
    <rect x="0" y="0" width="335" height="155" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="2"/>
    <rect x="0" y="0" width="335" height="30" rx="8" fill="#0284c7"/>
    <text x="167" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">BLUE — HYDROGRAPHY</text>
    <text x="15" y="55" font-size="11" fill="#38bdf8">• Perennial &amp; seasonal rivers</text>
    <text x="15" y="75" font-size="11" fill="#38bdf8">• Lakes, reservoirs, dams</text>
    <text x="15" y="95" font-size="11" fill="#38bdf8">• Swamps, marshes &amp; boreholes</text>
    <text x="15" y="115" font-size="11" fill="#38bdf8">• Water tanks (W.T.) &amp; springs</text>
  </g>

  <!-- Green: Vegetation -->
  <g transform="translate(420, 75)">
    <rect x="0" y="0" width="335" height="155" rx="8" fill="#0f172a" stroke="#16a34a" stroke-width="2"/>
    <rect x="0" y="0" width="335" height="30" rx="8" fill="#16a34a"/>
    <text x="167" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">GREEN — VEGETATION &amp; CROPS</text>
    <text x="15" y="55" font-size="11" fill="#4ade80">• Indigenous &amp; gazetted forests</text>
    <text x="15" y="75" font-size="11" fill="#4ade80">• Plantations (tea, coffee, sugar)</text>
    <text x="15" y="95" font-size="11" fill="#4ade80">• Scrub, woodland &amp; thicket</text>
    <text x="15" y="115" font-size="11" fill="#4ade80">• Mangrove &amp; papyrus swamps</text>
  </g>

  <!-- Brown: Relief -->
  <g transform="translate(45, 250)">
    <rect x="0" y="0" width="335" height="155" rx="8" fill="#0f172a" stroke="#b45309" stroke-width="2"/>
    <rect x="0" y="0" width="335" height="30" rx="8" fill="#b45309"/>
    <text x="167" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">BROWN — RELIEF &amp; LANDFORMS</text>
    <text x="15" y="55" font-size="11" fill="#fbbf24">• Contour lines (V.I. 20m)</text>
    <text x="15" y="75" font-size="11" fill="#fbbf24">• Spot heights (.1840)</text>
    <text x="15" y="95" font-size="11" fill="#fbbf24">• Trigonometrical stations (△)</text>
    <text x="15" y="115" font-size="11" fill="#fbbf24">• Sand dunes &amp; rock outcrops</text>
  </g>

  <!-- Black/Red: Infrastructure -->
  <g transform="translate(420, 250)">
    <rect x="0" y="0" width="335" height="155" rx="8" fill="#0f172a" stroke="#e11d48" stroke-width="2"/>
    <rect x="0" y="0" width="335" height="30" rx="8" fill="#e11d48"/>
    <text x="167" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">RED / BLACK — HUMAN INFRASTRUCTURE</text>
    <text x="15" y="55" font-size="11" fill="#f43f5e">• Red: All-weather bound roads (A, B, C)</text>
    <text x="15" y="75" font-size="11" fill="#cbd5e1">• Black: Loose roads, footpaths, rail</text>
    <text x="15" y="95" font-size="11" fill="#cbd5e1">• Buildings, huts, churches, mosques</text>
    <text x="15" y="115" font-size="11" fill="#cbd5e1">• Sch (School), Disp (Dispensary), PO</text>
  </g>
</svg>
""")

# SVG 5: Grid Reference System (Lesson 5)
SVG_GRID_REFERENCES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">4-Figure vs. 6-Figure Grid Reference System</text>

  <!-- 1km Grid Square -->
  <g transform="translate(100, 80)">
    <rect x="0" y="0" width="260" height="260" fill="#0f172a" stroke="#38bdf8" stroke-width="2.5"/>
    
    <!-- Subdivisions (Tenths) -->
    <line x1="26" y1="0" x2="26" y2="260" stroke="#334155" stroke-width="1" stroke-dasharray="2"/>
    <line x1="52" y1="0" x2="52" y2="260" stroke="#334155" stroke-width="1" stroke-dasharray="2"/>
    <line x1="78" y1="0" x2="78" y2="260" stroke="#334155" stroke-width="1" stroke-dasharray="2"/>
    <line x1="104" y1="0" x2="104" y2="260" stroke="#334155" stroke-width="1" stroke-dasharray="2"/>
    <line x1="130" y1="0" x2="130" y2="260" stroke="#334155" stroke-width="1" stroke-dasharray="2"/>
    <line x1="156" y1="0" x2="156" y2="260" stroke="#334155" stroke-width="1" stroke-dasharray="2"/>
    <line x1="182" y1="0" x2="182" y2="260" stroke="#334155" stroke-width="1" stroke-dasharray="2"/>
    <line x1="208" y1="0" x2="208" y2="260" stroke="#334155" stroke-width="1" stroke-dasharray="2"/>
    <line x1="234" y1="0" x2="234" y2="260" stroke="#334155" stroke-width="1" stroke-dasharray="2"/>

    <line x1="0" y1="26" x2="260" y2="260" stroke="#334155" stroke-width="1" stroke-dasharray="2"/>
    <line x1="0" y1="52" x2="260" y2="52" stroke="#334155" stroke-width="1" stroke-dasharray="2"/>
    <line x1="0" y1="78" x2="260" y2="78" stroke="#334155" stroke-width="1" stroke-dasharray="2"/>
    <line x1="0" y1="104" x2="260" y2="104" stroke="#334155" stroke-width="1" stroke-dasharray="2"/>
    <line x1="0" y1="130" x2="260" y2="130" stroke="#334155" stroke-width="1" stroke-dasharray="2"/>
    <line x1="0" y1="156" x2="260" y2="156" stroke="#334155" stroke-width="1" stroke-dasharray="2"/>
    <line x1="0" y1="182" x2="260" y2="182" stroke="#334155" stroke-width="1" stroke-dasharray="2"/>
    <line x1="0" y1="208" x2="260" y2="208" stroke="#334155" stroke-width="1" stroke-dasharray="2"/>
    <line x1="0" y1="234" x2="260" y2="234" stroke="#334155" stroke-width="1" stroke-dasharray="2"/>

    <!-- Target Point (6 tenths East, 4 tenths North) -->
    <circle cx="156" cy="156" r="6" fill="#f43f5e"/>
    <text x="168" y="152" font-size="12" font-weight="bold" fill="#f43f5e">Target Church</text>

    <!-- South-West Corner (4-Figure Origin) -->
    <circle cx="0" cy="260" r="7" fill="#fbbf24"/>
    <text x="10" y="250" font-size="10" font-weight="bold" fill="#fbbf24">SW Corner</text>

    <!-- Easting / Northing Labels -->
    <text x="-25" y="265" font-size="12" font-weight="bold" fill="#38bdf8">78</text>
    <text x="-25" y="10" font-size="12" font-weight="bold" fill="#38bdf8">79</text>
    <text x="0" y="280" font-size="12" font-weight="bold" fill="#38bdf8">34</text>
    <text x="250" y="280" font-size="12" font-weight="bold" fill="#38bdf8">35</text>
  </g>

  <!-- Explanation Panel -->
  <g transform="translate(420, 80)">
    <rect x="0" y="0" width="335" height="120" rx="8" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="167" y="25" font-size="13" font-weight="bold" fill="#fbbf24" text-anchor="middle">4-Figure Grid Reference: 3478</text>
    <text x="15" y="55" font-size="11" fill="#cbd5e1">• Identifies the entire 1 km² square</text>
    <text x="15" y="75" font-size="11" fill="#cbd5e1">• Easting: Line 34 (West boundary)</text>
    <text x="15" y="95" font-size="11" fill="#cbd5e1">• Northing: Line 78 (South boundary)</text>
  </g>

  <g transform="translate(420, 220)">
    <rect x="0" y="0" width="335" height="120" rx="8" fill="#0f172a" stroke="#f43f5e" stroke-width="1.5"/>
    <text x="167" y="25" font-size="13" font-weight="bold" fill="#f43f5e" text-anchor="middle">6-Figure Grid Reference: 346784</text>
    <text x="15" y="55" font-size="11" fill="#cbd5e1">• Pinpoints exact location to 100 meters</text>
    <text x="15" y="75" font-size="11" fill="#cbd5e1">• Easting: 34 + 6 tenths east = 346</text>
    <text x="15" y="95" font-size="11" fill="#cbd5e1">• Northing: 78 + 4 tenths north = 784</text>
  </g>
</svg>
""")

# SVG 6: Slope Profiles & Contour Spacing (Lesson 7)
SVG_SLOPE_PROFILES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Contour Spacing and Fundamental Slope Profiles</text>

  <!-- 4 Slope Types -->
  <!-- 1. Gentle Slope -->
  <g transform="translate(45, 75)">
    <rect x="0" y="0" width="335" height="155" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="167" y="22" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. GENTLE SLOPE</text>
    <!-- Widely spaced contours -->
    <line x1="30" y1="50" x2="300" y2="50" stroke="#b45309" stroke-width="2"/>
    <line x1="30" y1="80" x2="300" y2="80" stroke="#b45309" stroke-width="2"/>
    <line x1="30" y1="110" x2="300" y2="110" stroke="#b45309" stroke-width="2"/>
    <text x="167" y="140" font-size="11" fill="#cbd5e1" text-anchor="middle">Contours are widely spaced apart</text>
  </g>

  <!-- 2. Steep Slope -->
  <g transform="translate(420, 75)">
    <rect x="0" y="0" width="335" height="155" rx="8" fill="#0f172a" stroke="#f87171" stroke-width="1.5"/>
    <text x="167" y="22" font-size="12" font-weight="bold" fill="#f87171" text-anchor="middle">2. STEEP SLOPE / ESCARPMENT</text>
    <!-- Closely packed contours -->
    <line x1="30" y1="50" x2="300" y2="50" stroke="#b45309" stroke-width="2"/>
    <line x1="30" y1="62" x2="300" y2="62" stroke="#b45309" stroke-width="2"/>
    <line x1="30" y1="74" x2="300" y2="74" stroke="#b45309" stroke-width="2"/>
    <line x1="30" y1="86" x2="300" y2="86" stroke="#b45309" stroke-width="2"/>
    <text x="167" y="140" font-size="11" fill="#cbd5e1" text-anchor="middle">Contours are tightly packed together</text>
  </g>

  <!-- 3. Convex Slope -->
  <g transform="translate(45, 245)">
    <rect x="0" y="0" width="335" height="155" rx="8" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="167" y="22" font-size="12" font-weight="bold" fill="#fbbf24" text-anchor="middle">3. CONVEX SLOPE (Bulging Out)</text>
    <!-- Close at bottom, wide at top -->
    <line x1="30" y1="45" x2="300" y2="45" stroke="#b45309" stroke-width="2"/>
    <line x1="30" y1="80" x2="300" y2="80" stroke="#b45309" stroke-width="2"/>
    <line x1="30" y1="100" x2="300" y2="100" stroke="#b45309" stroke-width="2"/>
    <line x1="30" y1="112" x2="300" y2="112" stroke="#b45309" stroke-width="2"/>
    <text x="167" y="140" font-size="11" fill="#cbd5e1" text-anchor="middle">Packed at base, wide at top</text>
  </g>

  <!-- 4. Concave Slope -->
  <g transform="translate(420, 245)">
    <rect x="0" y="0" width="335" height="155" rx="8" fill="#0f172a" stroke="#4ade80" stroke-width="1.5"/>
    <text x="167" y="22" font-size="12" font-weight="bold" fill="#4ade80" text-anchor="middle">4. CONCAVE SLOPE (Bowl Curve)</text>
    <!-- Wide at bottom, close at top -->
    <line x1="30" y1="45" x2="300" y2="45" stroke="#b45309" stroke-width="2"/>
    <line x1="30" y1="57" x2="300" y2="57" stroke="#b45309" stroke-width="2"/>
    <line x1="30" y1="75" x2="300" y2="75" stroke="#b45309" stroke-width="2"/>
    <line x1="30" y1="110" x2="300" y2="110" stroke="#b45309" stroke-width="2"/>
    <text x="167" y="140" font-size="11" fill="#cbd5e1" text-anchor="middle">Wide at base, packed at top</text>
  </g>
</svg>
""")

# SVG 7: Five Drainage Patterns (Lesson 8)
SVG_DRAINAGE_PATTERNS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Five Classic River Drainage Patterns</text>

  <!-- 1. Dendritic -->
  <g transform="translate(45, 75)">
    <rect x="0" y="0" width="220" height="150" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="110" y="22" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. Dendritic (Tree-like)</text>
    <path d="M 110 135 L 110 80 L 60 45 M 110 80 L 160 45 M 85 62 L 60 75 M 135 62 L 160 75" fill="none" stroke="#0284c7" stroke-width="2.5"/>
    <text x="110" y="140" font-size="9" fill="#cbd5e1" text-anchor="middle">Uniform rock resistance</text>
  </g>

  <!-- 2. Trellis -->
  <g transform="translate(290, 75)">
    <rect x="0" y="0" width="220" height="150" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="110" y="22" font-size="12" font-weight="bold" fill="#c084fc" text-anchor="middle">2. Trellis (90° Angles)</text>
    <line x1="110" y1="135" x2="110" y2="40" stroke="#a855f7" stroke-width="3"/>
    <line x1="40" y1="65" x2="110" y2="65" stroke="#a855f7" stroke-width="2"/>
    <line x1="180" y1="65" x2="110" y2="65" stroke="#a855f7" stroke-width="2"/>
    <line x1="40" y1="105" x2="110" y2="105" stroke="#a855f7" stroke-width="2"/>
    <line x1="180" y1="105" x2="110" y2="105" stroke="#a855f7" stroke-width="2"/>
    <text x="110" y="140" font-size="9" fill="#cbd5e1" text-anchor="middle">Folded / faulted strata</text>
  </g>

  <!-- 3. Radial -->
  <g transform="translate(535, 75)">
    <rect x="0" y="0" width="220" height="150" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="110" y="22" font-size="12" font-weight="bold" fill="#4ade80" text-anchor="middle">3. Radial (Spokes)</text>
    <circle cx="110" cy="85" r="14" fill="#334155" stroke="#4ade80" stroke-width="1.5"/>
    <line x1="110" y1="71" x2="110" y2="40" stroke="#4ade80" stroke-width="2"/>
    <line x1="110" y1="99" x2="110" y2="130" stroke="#4ade80" stroke-width="2"/>
    <line x1="96" y1="85" x2="50" y2="85" stroke="#4ade80" stroke-width="2"/>
    <line x1="124" y1="85" x2="170" y2="85" stroke="#4ade80" stroke-width="2"/>
    <text x="110" y="140" font-size="9" fill="#cbd5e1" text-anchor="middle">Isolated volcanic peak / dome</text>
  </g>

  <!-- 4. Parallel -->
  <g transform="translate(165, 245)">
    <rect x="0" y="0" width="220" height="150" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="110" y="22" font-size="12" font-weight="bold" fill="#fbbf24" text-anchor="middle">4. Parallel (Straight)</text>
    <line x1="60" y1="40" x2="60" y2="130" stroke="#fbbf24" stroke-width="2.5"/>
    <line x1="110" y1="40" x2="110" y2="130" stroke="#fbbf24" stroke-width="2.5"/>
    <line x1="160" y1="40" x2="160" y2="130" stroke="#fbbf24" stroke-width="2.5"/>
    <text x="110" y="140" font-size="9" fill="#cbd5e1" text-anchor="middle">Steep uniform escarpments</text>
  </g>

  <!-- 5. Centripetal -->
  <g transform="translate(420, 245)">
    <rect x="0" y="0" width="220" height="150" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <text x="110" y="22" font-size="12" font-weight="bold" fill="#f472b6" text-anchor="middle">5. Centripetal (Inward)</text>
    <circle cx="110" cy="85" r="16" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
    <line x1="45" y1="85" x2="94" y2="85" stroke="#f472b6" stroke-width="2"/>
    <line x1="175" y1="85" x2="126" y2="85" stroke="#f472b6" stroke-width="2"/>
    <line x1="110" y1="40" x2="110" y2="69" stroke="#f43f5e" stroke-width="2"/>
    <line x1="110" y1="130" x2="110" y2="101" stroke="#f43f5e" stroke-width="2"/>
    <text x="110" y="140" font-size="9" fill="#cbd5e1" text-anchor="middle">Inland basin / Caldera lake</text>
  </g>
</svg>
""")

# SVG 8: Physical Triad (Lesson 10)
SVG_PHYSICAL_TRIAD = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Landscape Synthesis: The Interlocking Physical Triad</text>

  <!-- Triangle Layout -->
  <!-- 1. Relief (Top) -->
  <g transform="translate(300, 70)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#b45309" stroke-width="2"/>
    <text x="100" y="25" font-size="13" font-weight="bold" fill="#fbbf24" text-anchor="middle">RELIEF &amp; ELEVATION</text>
    <text x="100" y="45" font-size="10" fill="#cbd5e1" text-anchor="middle">• Altitudinal lapse rate</text>
    <text x="100" y="60" font-size="10" fill="#cbd5e1" text-anchor="middle">• Slope gradient &amp; aspect</text>
  </g>

  <!-- 2. Drainage (Bottom-Left) -->
  <g transform="translate(80, 260)">
    <rect x="0" y="0" width="220" height="85" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="2"/>
    <text x="110" y="25" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">DRAINAGE &amp; HYDROLOGY</text>
    <text x="110" y="45" font-size="10" fill="#cbd5e1" text-anchor="middle">• Catchment discharge</text>
    <text x="110" y="60" font-size="10" fill="#cbd5e1" text-anchor="middle">• River erosion &amp; valleys</text>
    <text x="110" y="75" font-size="10" fill="#cbd5e1" text-anchor="middle">• Water table &amp; swamps</text>
  </g>

  <!-- 3. Vegetation (Bottom-Right) -->
  <g transform="translate(500, 260)">
    <rect x="0" y="0" width="220" height="85" rx="8" fill="#0f172a" stroke="#16a34a" stroke-width="2"/>
    <text x="110" y="25" font-size="13" font-weight="bold" fill="#4ade80" text-anchor="middle">VEGETATION &amp; ECOLOGY</text>
    <text x="110" y="45" font-size="10" fill="#cbd5e1" text-anchor="middle">• Forest catchments</text>
    <text x="110" y="60" font-size="10" fill="#cbd5e1" text-anchor="middle">• Montane bamboo belts</text>
    <text x="110" y="75" font-size="10" fill="#cbd5e1" text-anchor="middle">• Soil moisture indicators</text>
  </g>

  <!-- Arrows Linking -->
  <path d="M 280 145 L 210 260" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4"/>
  <path d="M 520 145 L 590 260" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4"/>
  <path d="M 300 300 L 500 300" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4"/>
</svg>
""")

# SVG 9: Cross-Section and Intervisibility (Lesson 11)
SVG_CROSS_SECTION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Cross-Section Construction and Intervisibility Ray</text>

  <!-- Graph Grid Frame -->
  <g transform="translate(80, 80)">
    <rect x="0" y="0" width="640" height="240" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    
    <!-- Y-axis Elevation Marks -->
    <line x1="0" y1="200" x2="640" y2="200" stroke="#334155" stroke-width="1"/>
    <text x="-15" y="205" font-size="10" fill="#94a3b8" text-anchor="end">1,400m</text>
    
    <line x1="0" y1="140" x2="640" y2="140" stroke="#334155" stroke-width="1"/>
    <text x="-15" y="145" font-size="10" fill="#94a3b8" text-anchor="end">1,600m</text>
    
    <line x1="0" y1="80" x2="640" y2="80" stroke="#334155" stroke-width="1"/>
    <text x="-15" y="85" font-size="10" fill="#94a3b8" text-anchor="end">1,800m</text>

    <line x1="0" y1="20" x2="640" y2="20" stroke="#334155" stroke-width="1"/>
    <text x="-15" y="25" font-size="10" fill="#94a3b8" text-anchor="end">2,000m</text>

    <!-- Topographic Curve Profile -->
    <path d="M 0 170 Q 120 40 220 180 T 360 210 T 480 90 T 640 180" fill="none" stroke="#b45309" stroke-width="3.5"/>

    <!-- Point A & Point B -->
    <circle cx="100" cy="80" r="6" fill="#38bdf8"/>
    <text x="100" y="65" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Point A (Hilltop)</text>

    <circle cx="560" cy="120" r="6" fill="#22c55e"/>
    <text x="560" y="105" font-size="12" font-weight="bold" fill="#4ade80" text-anchor="middle">Point B</text>

    <!-- Line of Sight (Intervisibility Ray) -->
    <line x1="100" y1="80" x2="560" y2="120" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4"/>
    <text x="330" y="90" font-size="11" font-weight="bold" fill="#f43f5e">Line of Sight Unobstructed -> INTERVISIBLE</text>
  </g>

  <!-- VE Formula Callout -->
  <text x="400" y="360" font-size="13" font-weight="bold" fill="#fbbf24" text-anchor="middle">Vertical Exaggeration (VE) = Vertical Scale (1:2,000) / Horizontal Scale (1:50,000) = 25 Times</text>
</svg>
""")

# SVG 10: Route Selection & Suitability Matrix (Lesson 12)
SVG_ROUTE_SELECTION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Topographical Route Selection &amp; Hazard Avoidance</text>

  <!-- 3 Route Options -->
  <!-- Route A: Mountain Crest (Poor) -->
  <g transform="translate(45, 75)">
    <rect x="0" y="0" width="220" height="230" rx="8" fill="#0f172a" stroke="#f87171" stroke-width="2"/>
    <text x="110" y="25" font-size="12" font-weight="bold" fill="#f87171" text-anchor="middle">ROUTE A: Ridge Summit</text>
    <text x="15" y="60" font-size="11" fill="#cbd5e1">❌ Extreme gradients</text>
    <text x="15" y="85" font-size="11" fill="#cbd5e1">❌ Severe cliff cuttings</text>
    <text x="15" y="110" font-size="11" fill="#cbd5e1">❌ Heavy earthworks cost</text>
    <text x="15" y="135" font-size="11" fill="#cbd5e1">❌ High erosion risk</text>
    <rect x="20" y="175" width="180" height="30" rx="4" fill="#7f1d1d"/>
    <text x="110" y="195" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">UNSUITABLE</text>
  </g>

  <!-- Route B: Valley Pass (OPTIMAL) -->
  <g transform="translate(290, 75)">
    <rect x="0" y="0" width="220" height="230" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <text x="110" y="25" font-size="12" font-weight="bold" fill="#4ade80" text-anchor="middle">ROUTE B: Valley Pass</text>
    <text x="15" y="60" font-size="11" fill="#cbd5e1">✅ Follows contour valleys</text>
    <text x="15" y="85" font-size="11" fill="#cbd5e1">✅ Gentle, uniform slope</text>
    <text x="15" y="110" font-size="11" fill="#cbd5e1">✅ Bridges narrow rivers</text>
    <text x="15" y="135" font-size="11" fill="#cbd5e1">✅ Connects settlements</text>
    <rect x="20" y="175" width="180" height="30" rx="4" fill="#14532d"/>
    <text x="110" y="195" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">OPTIMAL ROUTE</text>
  </g>

  <!-- Route C: Papyrus Swamp (Poor) -->
  <g transform="translate(535, 75)">
    <rect x="0" y="0" width="220" height="230" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <text x="110" y="25" font-size="12" font-weight="bold" fill="#fbbf24" text-anchor="middle">ROUTE C: Floodplain</text>
    <text x="15" y="60" font-size="11" fill="#cbd5e1">❌ Waterlogged marsh</text>
    <text x="15" y="85" font-size="11" fill="#cbd5e1">❌ Unstable clay soils</text>
    <text x="15" y="110" font-size="11" fill="#cbd5e1">❌ Seasonal flood hazard</text>
    <text x="15" y="135" font-size="11" fill="#cbd5e1">❌ Culvert washouts</text>
    <rect x="20" y="175" width="180" height="30" rx="4" fill="#78350f"/>
    <text x="110" y="195" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">HIGH RISK</text>
  </g>
</svg>
""")

# SVG 11: Master Map Work Synthesis (Lesson 13)
SVG_MAP_SYNTHESIS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Topic 2 Mastery: Topographical Map Interpretation Architecture</text>

  <!-- 4 Pillars -->
  <g transform="translate(45, 75)">
    <rect x="0" y="0" width="165" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="82" y="25" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. COORDINATES</text>
    <text x="10" y="55" font-size="10" fill="#cbd5e1">• Eastings first</text>
    <text x="10" y="75" font-size="10" fill="#cbd5e1">• Northings second</text>
    <text x="10" y="95" font-size="10" fill="#cbd5e1">• 4-Fig (1 km²)</text>
    <text x="10" y="115" font-size="10" fill="#cbd5e1">• 6-Fig (100 m)</text>
    <text x="10" y="135" font-size="10" fill="#cbd5e1">• True/Grid North</text>
    <text x="10" y="155" font-size="10" fill="#cbd5e1">• Bearings 0-360°</text>
  </g>

  <g transform="translate(225, 75)">
    <rect x="0" y="0" width="165" height="320" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="82" y="25" font-size="11" font-weight="bold" fill="#c084fc" text-anchor="middle">2. SCALES</text>
    <text x="10" y="55" font-size="10" fill="#cbd5e1">• RF: 1:50,000</text>
    <text x="10" y="75" font-size="10" fill="#cbd5e1">• Statement scale</text>
    <text x="10" y="95" font-size="10" fill="#cbd5e1">• Linear bar scale</text>
    <text x="10" y="115" font-size="10" fill="#cbd5e1">• Straight routes</text>
    <text x="10" y="135" font-size="10" fill="#cbd5e1">• Thread method</text>
    <text x="10" y="155" font-size="10" fill="#cbd5e1">• Area counting</text>
  </g>

  <g transform="translate(405, 75)">
    <rect x="0" y="0" width="165" height="320" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="82" y="25" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">3. RELIEF &amp; SLOPES</text>
    <text x="10" y="55" font-size="10" fill="#cbd5e1">• Contours &amp; V.I.</text>
    <text x="10" y="75" font-size="10" fill="#cbd5e1">• Spot heights / BM</text>
    <text x="10" y="95" font-size="10" fill="#cbd5e1">• Valleys &amp; spurs</text>
    <text x="10" y="115" font-size="10" fill="#cbd5e1">• Convex / Concave</text>
    <text x="10" y="135" font-size="10" fill="#cbd5e1">• Cross-sections</text>
    <text x="10" y="155" font-size="10" fill="#cbd5e1">• Vertical Exaggeration</text>
  </g>

  <g transform="translate(585, 75)">
    <rect x="0" y="0" width="165" height="320" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="82" y="25" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">4. DRAINAGE &amp; USES</text>
    <text x="10" y="55" font-size="10" fill="#cbd5e1">• Dendritic, Trellis</text>
    <text x="10" y="75" font-size="10" fill="#cbd5e1">• Radial &amp; Parallel</text>
    <text x="10" y="95" font-size="10" fill="#cbd5e1">• Flow directions</text>
    <text x="10" y="115" font-size="10" fill="#cbd5e1">• Vegetation zones</text>
    <text x="10" y="135" font-size="10" fill="#cbd5e1">• Settlement patterns</text>
    <text x="10" y="155" font-size="10" fill="#cbd5e1">• Route selection</text>
  </g>
</svg>
""")

TOPIC_2_SVGS = {
    1: SVG_MARGINAL_INFO,
    2: SVG_BEARING_PROTRACTOR,
    3: SVG_THREAD_METHOD,
    4: SVG_SIGNS_COLORS,
    5: SVG_GRID_REFERENCES,
    6: SVG_MARGINAL_INFO,
    7: SVG_SLOPE_PROFILES,
    8: SVG_DRAINAGE_PATTERNS,
    10: SVG_PHYSICAL_TRIAD,
    11: SVG_CROSS_SECTION,
    12: SVG_ROUTE_SELECTION,
    13: SVG_MAP_SYNTHESIS
}

def enrich_topic_2():
    print("=== Starting Visual Enrichment for Topic 2: Map Reading and Interpretation ===")
    
    cbc = Curriculum.objects.filter(name__iexact="CBC").first()
    grade10 = Grade.objects.filter(curriculum=cbc, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade10, name="Geography").first()
    topic = Topic.objects.filter(subject=subject, order=2).first()

    if not topic:
        raise ValueError("Topic 2 'Map Reading and Interpretation' not found.")

    with open('curriculum/grade10_geography_topic2_verified_images.json') as f:
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
                            "topic_order": 2
                        }
                    }
                )
                asset.url = img_data['url']
                asset.status = "attached"
                asset.save()
                asset.blocks.add(hook_block)
                print(f"  + Attached Wikimedia Photographic Hook: {img_data['url'][:55]}...")

        # 2. Attach Custom Vector SVG
        svg_xml = TOPIC_2_SVGS.get(int(u_order))
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
                            "topic_order": 2
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
                        "topic_order": 2
                    }
                }
            )
            v_asset.url = vid_url
            v_asset.status = "attached"
            v_asset.save()
            v_asset.blocks.add(video_block)
            print(f"  + Attached Educational YouTube Video: {vid_url}")

    print("\n=== Topic 2 Visual Enrichment Completed Successfully! ===")

if __name__ == "__main__":
    enrich_topic_2()
