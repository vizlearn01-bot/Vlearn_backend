"""
VLearn CBC Grade 10 Geography — Topic 4: Geographic Information System (GIS)
Visual Enrichment Engine (Vector SVGs, Verified Wikimedia Images & Educational Videos)

Subject: Geography (Grade 10 CBC, Subject ID: 37)
Topic 4: Geographic Information System (GIS)

Attaches:
  - 13 First-Card Photographic Visual Hooks (100% Tested HTTP 200 OK Direct Wikimedia URLs)
  - 13 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - Educational YouTube Video for Latitude & Longitude Coordinate Grids
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade10_geography_topic4.py
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
# 13 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 4: GIS
# =============================================================================

# SVG 1: Geospatial Pipeline (Lesson 1)
SVG_GEOSPATIAL_PIPELINE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="48" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">THE GEOSPATIAL WORKFLOW PIPELINE</text>
  <text x="400" y="70" font-size="12" fill="#94a3b8" text-anchor="middle">From Observation and Positioning to Spatial Analysis and Decision-Making</text>

  <!-- Panel 1: Remote Sensing -->
  <g transform="translate(35, 95)">
    <rect x="0" y="0" width="220" height="300" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="36" rx="10" fill="#0284c7"/>
    <text x="110" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">1. REMOTE SENSING (RS)</text>
    
    <!-- Satellite Icon -->
    <circle cx="110" cy="85" r="28" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="65" y="80" width="25" height="10" rx="2" fill="#38bdf8"/>
    <rect x="130" y="80" width="25" height="10" rx="2" fill="#38bdf8"/>
    <line x1="90" y1="85" x2="130" y2="85" stroke="#ffffff" stroke-width="2"/>
    
    <!-- Waves down -->
    <path d="M95 125 Q110 140 125 125" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3"/>
    <path d="M85 140 Q110 160 135 140" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3"/>
    <path d="M75 155 Q110 180 145 155" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3"/>
    
    <!-- Role text -->
    <text x="110" y="195" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">OBSERVATION</text>
    <text x="110" y="215" font-size="10" fill="#cbd5e1" text-anchor="middle">Captures aerial imagery</text>
    <text x="110" y="230" font-size="10" fill="#cbd5e1" text-anchor="middle">&amp; environmental data</text>
    <text x="110" y="250" font-size="10" fill="#94a3b8" text-anchor="middle">e.g. Flood extent in Kisumu</text>
    <rect x="25" y="265" width="170" height="22" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
    <text x="110" y="280" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">"WHAT IS HAPPENING?"</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <polygon points="265,245 285,245 285,240 295,250 285,260 285,255 265,255" fill="#f59e0b"/>

  <!-- Panel 2: GPS -->
  <g transform="translate(290, 95)">
    <rect x="0" y="0" width="220" height="300" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="36" rx="10" fill="#d97706"/>
    <text x="110" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">2. GLOBAL POSITIONING (GPS)</text>
    
    <!-- GPS Pin & Satellites -->
    <circle cx="110" cy="95" r="30" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="110" cy="90" r="10" fill="#ef4444"/>
    <polygon points="103,96 117,96 110,115" fill="#ef4444"/>
    <circle cx="110" cy="90" r="4" fill="#ffffff"/>
    
    <text x="110" y="195" font-size="12" font-weight="bold" fill="#fbbf24" text-anchor="middle">LOCATION</text>
    <text x="110" y="215" font-size="10" fill="#cbd5e1" text-anchor="middle">Pinpoints precise coordinates</text>
    <text x="110" y="230" font-size="10" fill="#cbd5e1" text-anchor="middle">(Latitude, Longitude, Altitude)</text>
    <text x="110" y="250" font-size="10" fill="#94a3b8" text-anchor="middle">e.g. Stranded village positions</text>
    <rect x="25" y="265" width="170" height="22" rx="4" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
    <text x="110" y="280" font-size="9.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">"WHERE IS IT LOCATED?"</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <polygon points="520,245 540,245 540,240 550,250 540,260 540,255 520,255" fill="#22c55e"/>

  <!-- Panel 3: GIS -->
  <g transform="translate(545, 95)">
    <rect x="0" y="0" width="220" height="300" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="36" rx="10" fill="#16a34a"/>
    <text x="110" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">3. GEOGRAPHIC INFO (GIS)</text>
    
    <!-- Layered Computer Display -->
    <rect x="70" y="60" width="80" height="55" rx="4" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
    <line x1="80" y1="75" x2="140" y2="75" stroke="#38bdf8" stroke-width="2"/>
    <line x1="80" y1="85" x2="140" y2="85" stroke="#fbbf24" stroke-width="2"/>
    <line x1="80" y1="95" x2="140" y2="95" stroke="#4ade80" stroke-width="2"/>
    <rect x="100" y="115" width="20" height="15" fill="#334155"/>
    <line x1="85" y1="130" x2="135" y2="130" stroke="#334155" stroke-width="3"/>
    
    <text x="110" y="195" font-size="12" font-weight="bold" fill="#4ade80" text-anchor="middle">INTEGRATION &amp; ANALYSIS</text>
    <text x="110" y="215" font-size="10" fill="#cbd5e1" text-anchor="middle">Layers imagery + GPS data</text>
    <text x="110" y="230" font-size="10" fill="#cbd5e1" text-anchor="middle">Models solutions &amp; routes</text>
    <text x="110" y="250" font-size="10" fill="#94a3b8" text-anchor="middle">e.g. Fastest evacuation paths</text>
    <rect x="25" y="265" width="170" height="22" rx="4" fill="#1e293b" stroke="#22c55e" stroke-width="1"/>
    <text x="110" y="280" font-size="9.5" font-weight="bold" fill="#4ade80" text-anchor="middle">"HOW DO WE ACT?"</text>
  </g>
</svg>
""")

# SVG 2: Exploded GIS Layer Stack (Lesson 2)
SVG_LAYER_STACK = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">EXPLODED 3D GIS LAYER STACK &amp; GEOMETRIES</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Multi-layered thematic integration anchored to a shared coordinate reference frame</text>

  <!-- Vertical Alignment Axis Line -->
  <line x1="380" y1="85" x2="380" y2="395" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,4"/>
  <circle cx="380" cy="115" r="4" fill="#ef4444"/>
  <circle cx="380" cy="195" r="4" fill="#ef4444"/>
  <circle cx="380" cy="275" r="4" fill="#ef4444"/>
  <circle cx="380" cy="355" r="4" fill="#ef4444"/>

  <!-- Level 4: Points Layer (Top) -->
  <g transform="translate(180, 85)">
    <polygon points="100,0 360,0 260,60 0,60" fill="#0284c7" fill-opacity="0.35" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="120" cy="30" r="5" fill="#ef4444"/>
    <circle cx="200" cy="30" r="5" fill="#ef4444"/>
    <circle cx="270" cy="20" r="5" fill="#ef4444"/>
    <text x="380" y="35" font-size="13" font-weight="bold" fill="#38bdf8">1. POINTS LAYER (0D Primitives)</text>
    <text x="380" y="52" font-size="10.5" fill="#cbd5e1">Boreholes, School Gates, Mountain Peaks, Clinics</text>
  </g>

  <!-- Level 3: Lines Layer -->
  <g transform="translate(180, 165)">
    <polygon points="100,0 360,0 260,60 0,60" fill="#d97706" fill-opacity="0.35" stroke="#fbbf24" stroke-width="2"/>
    <path d="M40 30 Q120 10 200 30 T320 25" fill="none" stroke="#fbbf24" stroke-width="3"/>
    <path d="M100 55 L220 10" fill="none" stroke="#ffffff" stroke-width="2" stroke-dasharray="3,3"/>
    <text x="380" y="35" font-size="13" font-weight="bold" fill="#fbbf24">2. LINES LAYER (1D Polylines)</text>
    <text x="380" y="52" font-size="10.5" fill="#cbd5e1">Rivers, Paved Highways, Pipelines, Power Grids</text>
  </g>

  <!-- Level 2: Polygons Layer -->
  <g transform="translate(180, 245)">
    <polygon points="100,0 360,0 260,60 0,60" fill="#16a34a" fill-opacity="0.35" stroke="#4ade80" stroke-width="2"/>
    <polygon points="60,35 150,20 180,45 90,50" fill="#22c55e" fill-opacity="0.6" stroke="#4ade80" stroke-width="1.5"/>
    <polygon points="190,20 300,15 270,45 200,45" fill="#15803d" fill-opacity="0.6" stroke="#4ade80" stroke-width="1.5"/>
    <text x="380" y="35" font-size="13" font-weight="bold" fill="#4ade80">3. POLYGONS LAYER (2D Areas)</text>
    <text x="380" y="52" font-size="10.5" fill="#cbd5e1">Forests, Farm Parcels, Lakes, Administrative Counties</text>
  </g>

  <!-- Level 1: Base Imagery (Bottom) -->
  <g transform="translate(180, 325)">
    <polygon points="100,0 360,0 260,60 0,60" fill="#475569" fill-opacity="0.5" stroke="#94a3b8" stroke-width="2"/>
    <rect x="80" y="15" width="200" height="30" fill="#334155" fill-opacity="0.7"/>
    <text x="180" y="35" font-size="10" fill="#94a3b8" text-anchor="middle">Raster Satellite / Aerial Orthophoto</text>
    <text x="380" y="35" font-size="13" font-weight="bold" fill="#e2e8f0">4. BASE IMAGERY (Raster Grid)</text>
    <text x="380" y="52" font-size="10.5" fill="#cbd5e1">Continuous Landsat/Sentinel Multispectral Pixels</text>
  </g>

  <!-- Alignment callout -->
  <rect x="35" y="210" width="130" height="60" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
  <text x="100" y="230" font-size="10" font-weight="bold" fill="#ef4444" text-anchor="middle">SPATIAL ALIGNMENT</text>
  <text x="100" y="245" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Common Coordinate</text>
  <text x="100" y="258" font-size="8.5" fill="#cbd5e1" text-anchor="middle">System (WGS84 / UTM)</text>
</svg>
""")

# SVG 3: 5 Components of GIS (Lesson 3)
SVG_5_COMPONENTS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">THE FIVE INTERACTING COMPONENTS OF GIS</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">A functional socio-technical system linking technology, spatial data, and human intelligence</text>

  <!-- Central Hub: GIS -->
  <circle cx="400" cy="245" r="55" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
  <text x="400" y="240" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">GIS</text>
  <text x="400" y="258" font-size="10" fill="#38bdf8" text-anchor="middle">SYSTEM CORE</text>

  <!-- Component 1: Hardware (Top) -->
  <g transform="translate(320, 85)">
    <rect x="0" y="0" width="160" height="65" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="80" y="24" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. HARDWARE</text>
    <text x="80" y="42" font-size="9.5" fill="#cbd5e1" text-anchor="middle">CPUs, GPUs, Servers,</text>
    <text x="80" y="55" font-size="9.5" fill="#cbd5e1" text-anchor="middle">GPS Units, Monitors</text>
  </g>
  <line x1="400" y1="150" x2="400" y2="190" stroke="#38bdf8" stroke-width="2"/>

  <!-- Component 2: Software (Top Right) -->
  <g transform="translate(560, 160)">
    <rect x="0" y="0" width="160" height="65" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <text x="80" y="24" font-size="12" font-weight="bold" fill="#c084fc" text-anchor="middle">2. SOFTWARE</text>
    <text x="80" y="42" font-size="9.5" fill="#cbd5e1" text-anchor="middle">QGIS, ArcGIS Pro,</text>
    <text x="80" y="55" font-size="9.5" fill="#cbd5e1" text-anchor="middle">PostGIS, Google Earth</text>
  </g>
  <line x1="560" y1="205" x2="455" y2="230" stroke="#a855f7" stroke-width="2"/>

  <!-- Component 3: Data (Bottom Right) -->
  <g transform="translate(520, 310)">
    <rect x="0" y="0" width="160" height="65" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <text x="80" y="24" font-size="12" font-weight="bold" fill="#4ade80" text-anchor="middle">3. DATA (THE FUEL)</text>
    <text x="80" y="42" font-size="9.5" fill="#cbd5e1" text-anchor="middle">Vector Layers, Rasters,</text>
    <text x="80" y="55" font-size="9.5" fill="#cbd5e1" text-anchor="middle">Tabular Attributes</text>
  </g>
  <line x1="520" y1="325" x2="445" y2="280" stroke="#22c55e" stroke-width="2"/>

  <!-- Component 4: People (Bottom Left) -->
  <g transform="translate(120, 310)">
    <rect x="0" y="0" width="160" height="65" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <text x="80" y="24" font-size="12" font-weight="bold" fill="#fbbf24" text-anchor="middle">4. PEOPLE</text>
    <text x="80" y="42" font-size="9.5" fill="#cbd5e1" text-anchor="middle">Analysts, Cartographers,</text>
    <text x="80" y="55" font-size="9.5" fill="#cbd5e1" text-anchor="middle">Urban Planners, Users</text>
  </g>
  <line x1="280" y1="325" x2="355" y2="280" stroke="#f59e0b" stroke-width="2"/>

  <!-- Component 5: Methods (Top Left) -->
  <g transform="translate(80, 160)">
    <rect x="0" y="0" width="160" height="65" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="2"/>
    <text x="80" y="24" font-size="12" font-weight="bold" fill="#f472b6" text-anchor="middle">5. METHODS</text>
    <text x="80" y="42" font-size="9.5" fill="#cbd5e1" text-anchor="middle">Spatial Algorithms,</text>
    <text x="80" y="55" font-size="9.5" fill="#cbd5e1" text-anchor="middle">Buffer/Overlay Workflows</text>
  </g>
  <line x1="240" y1="205" x2="345" y2="230" stroke="#ec4899" stroke-width="2"/>
</svg>
""")

# SVG 4: Latitude & Longitude Global Grid (Lesson 4)
SVG_GLOBAL_GRID = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">GEOGRAPHICAL COORDINATES: LATITUDE &amp; LONGITUDE</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Spherical coordinate framework for unique global positioning</text>

  <!-- Globe Outline -->
  <circle cx="280" cy="245" r="140" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  
  <!-- Parallels of Latitude -->
  <ellipse cx="280" cy="245" rx="140" ry="12" fill="none" stroke="#22c55e" stroke-width="3"/>
  <ellipse cx="280" cy="180" rx="123" ry="10" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4"/>
  <ellipse cx="280" cy="310" rx="123" ry="10" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4"/>
  <ellipse cx="280" cy="130" rx="85" ry="7" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4"/>
  <ellipse cx="280" cy="360" rx="85" ry="7" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4"/>

  <!-- Meridians of Longitude -->
  <ellipse cx="280" cy="245" rx="12" ry="140" fill="none" stroke="#f59e0b" stroke-width="3"/>
  <ellipse cx="280" cy="245" rx="65" ry="140" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4"/>
  <ellipse cx="280" cy="245" rx="115" ry="140" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4"/>

  <!-- Axis & Poles -->
  <line x1="280" y1="90" x2="280" y2="400" stroke="#ffffff" stroke-width="1" stroke-dasharray="2,2"/>
  <text x="280" y="98" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">NORTH POLE (90° N)</text>
  <text x="280" y="398" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">SOUTH POLE (90° S)</text>

  <!-- Labels on Globe -->
  <text x="125" y="240" font-size="11" font-weight="bold" fill="#22c55e">EQUATOR (0° LAT)</text>
  <text x="300" y="150" font-size="11" font-weight="bold" fill="#f59e0b">PRIME MERIDIAN (0° LONG)</text>

  <!-- Explanatory Box (Right) -->
  <g transform="translate(470, 95)">
    <rect x="0" y="0" width="280" height="135" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="20" y="25" font-size="13" font-weight="bold" fill="#4ade80">PARALLELS OF LATITUDE</text>
    <text x="20" y="48" font-size="10.5" fill="#cbd5e1">- Measures North/South of Equator</text>
    <text x="20" y="66" font-size="10.5" fill="#cbd5e1">- Range: 0° (Equator) to 90° (Poles)</text>
    <text x="20" y="84" font-size="10.5" fill="#cbd5e1">- Lines never intersect (True Parallels)</text>
    <text x="20" y="112" font-size="10" font-weight="bold" fill="#38bdf8">Kenya Example: Nairobi ≈ 1.29° S</text>
  </g>

  <g transform="translate(470, 245)">
    <rect x="0" y="0" width="280" height="135" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="20" y="25" font-size="13" font-weight="bold" fill="#fbbf24">MERIDIANS OF LONGITUDE</text>
    <text x="20" y="48" font-size="10.5" fill="#cbd5e1">- Measures East/West of Prime Meridian</text>
    <text x="20" y="66" font-size="10.5" fill="#cbd5e1">- Range: 0° (Greenwich) to 180° (Antimeridian)</text>
    <text x="20" y="84" font-size="10.5" fill="#cbd5e1">- Converge at North and South Poles</text>
    <text x="20" y="112" font-size="10" font-weight="bold" fill="#38bdf8">Kenya Example: Nairobi ≈ 36.82° E</text>
  </g>
</svg>
""")

# SVG 5: Coordinate Conversion Math (Lesson 5)
SVG_COORDINATE_CONVERSION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">COORDINATE CONVERSION: DECIMAL DEGREES &lt;=&gt; DMS</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Base-60 Sexagesimal Mathematical Subdivisions (1° = 60′ = 3600″)</text>

  <!-- Left: DD to DMS -->
  <g transform="translate(35, 85)">
    <rect x="0" y="0" width="345" height="320" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#0284c7"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">CONVERT: DD to DMS (e.g. 36.8245°)</text>

    <!-- Step 1 -->
    <rect x="15" y="45" width="315" height="60" rx="6" fill="#1e293b"/>
    <text x="25" y="65" font-size="11" font-weight="bold" fill="#38bdf8">1. Extract Whole Degrees:</text>
    <text x="25" y="85" font-size="11" fill="#cbd5e1">Integer part = <tspan font-weight="bold" fill="#ffffff">36°</tspan> | Remaining decimal = 0.8245</text>

    <!-- Step 2 -->
    <rect x="15" y="115" width="315" height="70" rx="6" fill="#1e293b"/>
    <text x="25" y="135" font-size="11" font-weight="bold" fill="#fbbf24">2. Calculate Minutes (× 60):</text>
    <text x="25" y="155" font-size="10.5" fill="#cbd5e1">0.8245 × 60 = <tspan font-weight="bold" fill="#fbbf24">49.47′</tspan></text>
    <text x="25" y="172" font-size="10.5" fill="#cbd5e1">Integer part = <tspan font-weight="bold" fill="#ffffff">49′</tspan> | Remaining decimal = 0.47</text>

    <!-- Step 3 -->
    <rect x="15" y="195" width="315" height="60" rx="6" fill="#1e293b"/>
    <text x="25" y="215" font-size="11" font-weight="bold" fill="#4ade80">3. Calculate Seconds (× 60):</text>
    <text x="25" y="235" font-size="10.5" fill="#cbd5e1">0.47 × 60 = <tspan font-weight="bold" fill="#4ade80">28.2″</tspan></text>

    <!-- Result -->
    <rect x="15" y="265" width="315" height="40" rx="6" fill="#0284c7" fill-opacity="0.3" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="172" y="290" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">RESULT: 36° 49′ 28.2″ E</text>
  </g>

  <!-- Right: DMS to DD -->
  <g transform="translate(420, 85)">
    <rect x="0" y="0" width="345" height="320" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#16a34a"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">CONVERT: DMS to DD (e.g. 1° 15′ 36″ S)</text>

    <!-- Formula -->
    <rect x="15" y="45" width="315" height="55" rx="6" fill="#1e293b"/>
    <text x="172" y="68" font-size="10.5" font-weight="bold" fill="#4ade80" text-anchor="middle">DD = Degrees + (Minutes / 60) + (Seconds / 3600)</text>
    <text x="172" y="88" font-size="9.5" fill="#94a3b8" text-anchor="middle">Inverse division restores decimal fraction</text>

    <!-- Step 1 -->
    <rect x="15" y="110" width="315" height="55" rx="6" fill="#1e293b"/>
    <text x="25" y="130" font-size="11" font-weight="bold" fill="#cbd5e1">Minutes Division: 15 / 60 = <tspan font-weight="bold" fill="#fbbf24">0.25°</tspan></text>
    <text x="25" y="150" font-size="11" font-weight="bold" fill="#cbd5e1">Seconds Division: 36 / 3600 = <tspan font-weight="bold" fill="#4ade80">0.01°</tspan></text>

    <!-- Step 2 -->
    <rect x="15" y="175" width="315" height="75" rx="6" fill="#1e293b"/>
    <text x="25" y="195" font-size="11" font-weight="bold" fill="#38bdf8">Sum All Components:</text>
    <text x="25" y="215" font-size="11" fill="#cbd5e1">DD = 1° + 0.25° + 0.01°</text>
    <text x="25" y="235" font-size="12" font-weight="bold" fill="#ffffff">DD = 1.26°</text>

    <!-- Result -->
    <rect x="15" y="265" width="315" height="40" rx="6" fill="#16a34a" fill-opacity="0.3" stroke="#22c55e" stroke-width="1.5"/>
    <text x="172" y="290" font-size="13" font-weight="bold" fill="#4ade80" text-anchor="middle">RESULT: 1.26° S (or -1.26°)</text>
  </g>
</svg>
""")

# SVG 6: GPS Satellite Trilateration (Lesson 6)
SVG_GPS_TRILATERATION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">GPS SATELLITE TRILATERATION GEOMETRY</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Calculating ground coordinates through intersecting time-delay distance spheres</text>

  <!-- Satellites -->
  <!-- Sat 1 (Top Left) -->
  <g transform="translate(140, 95)">
    <circle cx="0" cy="0" r="16" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <text x="0" y="5" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">SAT 1</text>
    <circle cx="0" cy="0" r="170" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.4"/>
  </g>

  <!-- Sat 2 (Top Right) -->
  <g transform="translate(660, 95)">
    <circle cx="0" cy="0" r="16" fill="#d97706" stroke="#fbbf24" stroke-width="2"/>
    <text x="0" y="5" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">SAT 2</text>
    <circle cx="0" cy="0" r="280" fill="none" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.4"/>
  </g>

  <!-- Sat 3 (Top Center) -->
  <g transform="translate(400, 80)">
    <circle cx="0" cy="0" r="16" fill="#16a34a" stroke="#4ade80" stroke-width="2"/>
    <text x="0" y="5" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">SAT 3</text>
    <circle cx="0" cy="0" r="185" fill="none" stroke="#4ade80" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.4"/>
  </g>

  <!-- Sat 4 (Far Left) -->
  <g transform="translate(60, 240)">
    <circle cx="0" cy="0" r="16" fill="#9333ea" stroke="#c084fc" stroke-width="2"/>
    <text x="0" y="5" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">SAT 4</text>
    <circle cx="0" cy="0" r="340" fill="none" stroke="#c084fc" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.3"/>
  </g>

  <!-- Receiver Intersection (Earth Surface) -->
  <g transform="translate(400, 265)">
    <!-- Signal rays -->
    <line x1="-260" y1="-170" x2="0" y2="0" stroke="#38bdf8" stroke-width="2"/>
    <line x1="260" y1="-170" x2="0" y2="0" stroke="#fbbf24" stroke-width="2"/>
    <line x1="0" y1="-185" x2="0" y2="0" stroke="#4ade80" stroke-width="2"/>
    <line x1="-340" y1="-25" x2="0" y2="0" stroke="#c084fc" stroke-width="2"/>

    <!-- Uncertainty Circle -->
    <circle cx="0" cy="0" r="28" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,4"/>
    
    <!-- User Point -->
    <circle cx="0" cy="0" r="8" fill="#ef4444" stroke="#ffffff" stroke-width="2"/>
    <text x="0" y="45" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">GPS RECEIVER (FIX)</text>
    <text x="0" y="60" font-size="9" fill="#94a3b8" text-anchor="middle">Lat: 1.29° S | Long: 36.82° E</text>
    <text x="0" y="73" font-size="9" fill="#38bdf8" text-anchor="middle">Alt: 1,680m (Accuracy ±3m)</text>
  </g>

  <!-- Explanation Bottom Left -->
  <g transform="translate(45, 335)">
    <rect x="0" y="0" width="250" height="85" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="15" y="20" font-size="11" font-weight="bold" fill="#38bdf8">CONSTELLATION REQUIREMENTS</text>
    <text x="15" y="38" font-size="10" fill="#cbd5e1">- 3 Satellites: 2D Fix (Latitude, Longitude)</text>
    <text x="15" y="55" font-size="10" fill="#4ade80">- 4 Satellites: 3D Fix (+ Altitude &amp; Clock Correction)</text>
    <text x="15" y="72" font-size="9" fill="#94a3b8">Distance = Speed of Light (c) × Time Delay (Δt)</text>
  </g>
</svg>
""")

# SVG 7: True Colour vs False Colour (Lesson 7)
SVG_REMOTE_SENSING_COMPOSITE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">REMOTE SENSING: TRUE-COLOUR VS FALSE-COLOUR (NIR)</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Near-Infrared (NIR) band converts plant chlorophyll reflectance into vibrant diagnostic red</text>

  <!-- Left: True Colour -->
  <g transform="translate(45, 85)">
    <rect x="0" y="0" width="335" height="250" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="335" height="30" rx="8" fill="#0284c7"/>
    <text x="167" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">TRUE-COLOUR COMPOSITE (RGB: 4, 3, 2)</text>

    <!-- Simulated Scene -->
    <rect x="15" y="40" width="305" height="195" fill="#1e293b"/>
    <!-- Water -->
    <polygon points="15,40 120,40 80,140 15,100" fill="#0f766e"/>
    <text x="45" y="75" font-size="9" fill="#99f6e4">Deep Lake (Dark Blue)</text>
    <!-- Forest -->
    <circle cx="230" cy="100" r="50" fill="#15803d"/>
    <text x="230" y="105" font-size="9" fill="#bbf7d0" text-anchor="middle">Healthy Forest (Green)</text>
    <!-- Urban/Soil -->
    <rect x="130" y="155" width="170" height="70" fill="#78716c"/>
    <text x="215" y="195" font-size="9" fill="#f5f5f4" text-anchor="middle">Urban Built-Up / Bare Soil (Grey/Tan)</text>
  </g>

  <!-- Right: False Colour -->
  <g transform="translate(420, 85)">
    <rect x="0" y="0" width="335" height="250" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="335" height="30" rx="8" fill="#dc2626"/>
    <text x="167" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">FALSE-COLOUR INFRARED (NIR-R-G: 5, 4, 3)</text>

    <!-- Simulated Scene -->
    <rect x="15" y="40" width="305" height="195" fill="#1e293b"/>
    <!-- Water -->
    <polygon points="15,40 120,40 80,140 15,100" fill="#020617"/>
    <text x="45" y="75" font-size="9" fill="#94a3b8">Water (Jet Black - Absorbs NIR)</text>
    <!-- Forest -->
    <circle cx="230" cy="100" r="50" fill="#ef4444"/>
    <text x="230" y="105" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Dense Forest (Bright Red - Reflects NIR)</text>
    <!-- Urban/Soil -->
    <rect x="130" y="155" width="170" height="70" fill="#0284c7" fill-opacity="0.8"/>
    <text x="215" y="195" font-size="9" fill="#ffffff" text-anchor="middle">Urban Concrete / Soil (Cyan / Blue-Grey)</text>
  </g>

  <!-- Bottom Takeaway Banner -->
  <rect x="45" y="355" width="710" height="65" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
  <text x="400" y="380" font-size="12" font-weight="bold" fill="#f59e0b" text-anchor="middle">KEY GEOGRAPHICAL INSIGHT</text>
  <text x="400" y="402" font-size="11" fill="#cbd5e1" text-anchor="middle">Healthy vegetation reflects near-infrared radiation intensely. False-colour mapping makes crop stress,</text>
  <text x="400" y="416" font-size="11" fill="#cbd5e1" text-anchor="middle">illegal deforestation, and water boundaries immediately distinguishable from soil and concrete.</text>
</svg>
""")

# SVG 8: On-Screen Vector Digitization (Lesson 8)
SVG_DIGITIZATION_WORKFLOW = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">DATA INPUT: HEADS-UP ON-SCREEN DIGITIZATION</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Transforming geo-referenced raster imagery into structured vector layers</text>

  <!-- GIS Software Viewport Frame -->
  <rect x="45" y="85" width="460" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <rect x="45" y="85" width="460" height="28" rx="8" fill="#0284c7"/>
  <text x="60" y="104" font-size="11" font-weight="bold" fill="#ffffff">QGIS / ArcGIS Digitizing Canvas — Geo-referenced Orthophoto</text>

  <!-- Background Raster Image -->
  <rect x="55" y="120" width="440" height="275" fill="#334155" fill-opacity="0.5"/>
  <circle cx="200" cy="220" r="60" fill="#15803d" fill-opacity="0.3"/>

  <!-- Digitized Vector Features -->
  <!-- 1. Polygon Digitizing -->
  <polygon points="150,180 260,190 240,270 140,250" fill="#22c55e" fill-opacity="0.4" stroke="#4ade80" stroke-width="2"/>
  <circle cx="150" cy="180" r="4" fill="#ffffff" stroke="#4ade80" stroke-width="1.5"/>
  <circle cx="260" cy="190" r="4" fill="#ffffff" stroke="#4ade80" stroke-width="1.5"/>
  <circle cx="240" cy="270" r="4" fill="#ffffff" stroke="#4ade80" stroke-width="1.5"/>
  <circle cx="140" cy="250" r="4" fill="#ffffff" stroke="#4ade80" stroke-width="1.5"/>
  <text x="200" y="235" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Forest Polygon Layer</text>

  <!-- 2. Polyline Digitizing -->
  <path d="M80 340 L180 310 L280 330 L450 300" fill="none" stroke="#fbbf24" stroke-width="3"/>
  <circle cx="80" cy="340" r="3.5" fill="#ffffff"/>
  <circle cx="180" cy="310" r="3.5" fill="#ffffff"/>
  <circle cx="280" cy="330" r="3.5" fill="#ffffff"/>
  <circle cx="450" cy="300" r="3.5" fill="#ffffff"/>
  <text x="360" y="310" font-size="10" font-weight="bold" fill="#fbbf24">Main Road Polyline</text>

  <!-- 3. Point Digitizing with Mouse Cursor -->
  <circle cx="340" cy="170" r="6" fill="#ef4444" stroke="#ffffff" stroke-width="1.5"/>
  <text x="350" y="160" font-size="9.5" font-weight="bold" fill="#ef4444">Clinic Point</text>
  <!-- Cursor pointer -->
  <polygon points="340,170 340,195 348,188 358,198 362,194 352,184 360,184" fill="#ffffff" stroke="#000000" stroke-width="1"/>

  <!-- Right Side: 3 Workflows Info -->
  <g transform="translate(530, 85)">
    <rect x="0" y="0" width="225" height="320" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="112" y="28" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">DATA INPUT METHODS</text>

    <rect x="15" y="45" width="195" height="75" rx="6" fill="#1e293b"/>
    <text x="25" y="65" font-size="11" font-weight="bold" fill="#38bdf8">1. Coordinate Entry</text>
    <text x="25" y="82" font-size="9.5" fill="#cbd5e1">Manual typing of (X, Y)</text>
    <text x="25" y="96" font-size="9.5" fill="#cbd5e1">into database tables.</text>

    <rect x="15" y="130" width="195" height="75" rx="6" fill="#1e293b"/>
    <text x="25" y="150" font-size="11" font-weight="bold" fill="#fbbf24">2. GPS File Import</text>
    <text x="25" y="167" font-size="9.5" fill="#cbd5e1">Direct upload of .gpx,</text>
    <text x="25" y="181" font-size="9.5" fill="#cbd5e1">.kml, or .geojson tracks.</text>

    <rect x="15" y="215" width="195" height="90" rx="6" fill="#1e293b"/>
    <text x="25" y="235" font-size="11" font-weight="bold" fill="#4ade80">3. Heads-Up Tracing</text>
    <text x="25" y="252" font-size="9.5" fill="#cbd5e1">Clicking vertices over</text>
    <text x="25" y="266" font-size="9.5" fill="#cbd5e1">geo-referenced rasters to</text>
    <text x="25" y="280" font-size="9.5" fill="#cbd5e1">create vector shapes.</text>
  </g>
</svg>
""")

# SVG 9: Map Layout & 6 Marginal Elements (Lesson 9)
SVG_MAP_LAYOUT_MARGINALS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <!-- Outer Map Neatline -->
  <rect x="40" y="35" width="720" height="380" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>

  <!-- 1. Map Title Banner (Top) -->
  <rect x="160" y="45" width="480" height="30" rx="4" fill="#0284c7"/>
  <text x="400" y="65" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">1. MAP TITLE: NAIROBI COUNTY LAND-USE &amp; ZONING (2026)</text>

  <!-- 2. Main Map Body Canvas -->
  <rect x="60" y="85" width="480" height="260" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
  <!-- Map Features -->
  <polygon points="100,120 220,100 240,180 120,200" fill="#15803d" fill-opacity="0.6" stroke="#4ade80" stroke-width="1.5"/>
  <text x="170" y="155" font-size="11" font-weight="bold" fill="#bbf7d0" text-anchor="middle">Forest Zone</text>
  
  <polygon points="260,110 480,100 460,250 250,220" fill="#78716c" fill-opacity="0.5" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="360" y="170" font-size="11" font-weight="bold" fill="#f5f5f4" text-anchor="middle">Urban Built-Up Area</text>

  <path d="M60 220 Q200 280 350 200 T540 240" fill="none" stroke="#38bdf8" stroke-width="3"/>
  <text x="180" y="275" font-size="10" fill="#38bdf8">Nairobi River</text>

  <circle cx="380" cy="140" r="6" fill="#ef4444"/>
  <text x="395" y="145" font-size="9.5" font-weight="bold" fill="#ef4444">City Hall</text>

  <!-- Coordinate Graticule Grid Ticks -->
  <text x="65" y="100" font-size="9" fill="#94a3b8">1°15'S, 36°48'E</text>
  <text x="470" y="340" font-size="9" fill="#94a3b8">1°20'S, 36°55'E</text>

  <!-- Right Margin Sidebar for Components -->
  <!-- 3. North Arrow -->
  <g transform="translate(620, 90)">
    <rect x="0" y="0" width="80" height="75" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <polygon points="40,10 32,38 40,32" fill="#ef4444"/>
    <polygon points="40,10 48,38 40,32" fill="#cbd5e1"/>
    <line x1="40" y1="32" x2="40" y2="55" stroke="#ffffff" stroke-width="2"/>
    <text x="40" y="68" font-size="10" font-weight="bold" fill="#ef4444" text-anchor="middle">TRUE NORTH</text>
  </g>

  <!-- 4. Key / Legend -->
  <g transform="translate(560, 175)">
    <rect x="0" y="0" width="185" height="170" rx="6" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <text x="92" y="20" font-size="11" font-weight="bold" fill="#c084fc" text-anchor="middle">2. KEY / LEGEND</text>
    
    <rect x="15" y="35" width="20" height="12" fill="#15803d" stroke="#4ade80"/>
    <text x="45" y="45" font-size="9.5" fill="#cbd5e1">Protected Forest</text>

    <rect x="15" y="55" width="20" height="12" fill="#78716c" stroke="#cbd5e1"/>
    <text x="45" y="65" font-size="9.5" fill="#cbd5e1">Commercial Zone</text>

    <line x1="15" y1="82" x2="35" y2="82" stroke="#38bdf8" stroke-width="3"/>
    <text x="45" y="86" font-size="9.5" fill="#cbd5e1">Permanent River</text>

    <circle cx="25" cy="102" r="5" fill="#ef4444"/>
    <text x="45" y="106" font-size="9.5" fill="#cbd5e1">Public Admin Centre</text>

    <line x1="15" y1="122" x2="35" y2="122" stroke="#fbbf24" stroke-width="2" stroke-dasharray="3,3"/>
    <text x="45" y="126" font-size="9.5" fill="#cbd5e1">Sub-County Border</text>

    <text x="92" y="155" font-size="8.5" fill="#94a3b8" text-anchor="middle">Decodes all thematic symbols</text>
  </g>

  <!-- Bottom Margin: 5. Scale & 6. Source -->
  <g transform="translate(60, 355)">
    <rect x="0" y="0" width="300" height="50" rx="4" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
    <text x="150" y="18" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">3. SCALE: 1:50,000 (1 cm = 500 m)</text>
    <!-- Scale Bar -->
    <rect x="30" y="26" width="60" height="8" fill="#ffffff"/>
    <rect x="90" y="26" width="60" height="8" fill="#fbbf24"/>
    <rect x="150" y="26" width="60" height="8" fill="#ffffff"/>
    <rect x="210" y="26" width="60" height="8" fill="#fbbf24"/>
    <text x="30" y="44" font-size="8" fill="#94a3b8">0</text>
    <text x="150" y="44" font-size="8" fill="#94a3b8">1 km</text>
    <text x="270" y="44" font-size="8" fill="#94a3b8">2 km</text>
  </g>

  <g transform="translate(380, 355)">
    <rect x="0" y="0" width="365" height="50" rx="4" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <text x="15" y="18" font-size="9.5" font-weight="bold" fill="#38bdf8">4. SOURCE ATTRIBUTION &amp; METADATA</text>
    <text x="15" y="32" font-size="8.5" fill="#cbd5e1">Data Source: Survey of Kenya, Landsat 9 OLI, OpenStreetMap</text>
    <text x="15" y="44" font-size="8.5" fill="#94a3b8">Projection: UTM Zone 37S, Datum: WGS84 | Author: Grade 10 GIS Lab</text>
  </g>
</svg>
""")

# SVG 10: Spatial Query & Buffering Analysis (Lesson 10)
SVG_SPATIAL_ANALYSIS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">SPATIAL ANALYSIS: BUFFERING &amp; OVERLAY SUITABILITY</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Executing mathematical proximity and multi-criteria overlay queries</text>

  <!-- Left Canvas: Proximity Buffer -->
  <g transform="translate(35, 85)">
    <rect x="0" y="0" width="345" height="320" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#0284c7"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">PROXIMITY ANALYSIS: 100m RIVER BUFFER</text>

    <!-- River Line -->
    <path d="M40 80 Q160 220 300 120" fill="none" stroke="#38bdf8" stroke-width="5"/>
    
    <!-- 100m Buffer Zone -->
    <path d="M40 80 Q160 220 300 120" fill="none" stroke="#38bdf8" stroke-width="45" stroke-opacity="0.25" stroke-linecap="round"/>
    <text x="170" y="180" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">100m Riparian Buffer Zone</text>

    <!-- Factory inside Buffer (Violation) -->
    <rect x="110" y="125" width="18" height="18" fill="#ef4444"/>
    <text x="120" y="160" font-size="9" font-weight="bold" fill="#ef4444" text-anchor="middle">Factory A (Illegal)</text>

    <!-- Factory outside Buffer (Compliant) -->
    <rect x="250" y="230" width="18" height="18" fill="#22c55e"/>
    <text x="260" y="260" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">Factory B (Compliant)</text>

    <rect x="15" y="275" width="315" height="35" rx="4" fill="#1e293b"/>
    <text x="172" y="297" font-size="10" fill="#cbd5e1" text-anchor="middle"><tspan fill="#ef4444" font-weight="bold">Query</tspan>: S_Distance(Factory, River) &lt; 100m</text>
  </g>

  <!-- Right Canvas: Multi-Layer Overlay -->
  <g transform="translate(420, 85)">
    <rect x="0" y="0" width="345" height="320" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#16a34a"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">OVERLAY ANALYSIS: TEA FARM SUITABILITY</text>

    <!-- Overlapping Venn-like Spatial Polygons -->
    <!-- Slope Layer -->
    <circle cx="140" cy="140" r="65" fill="#0284c7" fill-opacity="0.3" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="110" y="110" font-size="9.5" fill="#38bdf8">Gentle Slope (&lt;15°)</text>

    <!-- Soil Layer -->
    <circle cx="210" cy="140" r="65" fill="#f59e0b" fill-opacity="0.3" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="245" y="110" font-size="9.5" fill="#fbbf24">Volcanic Loam</text>

    <!-- Rainfall Layer -->
    <circle cx="175" cy="195" r="60" fill="#9333ea" fill-opacity="0.3" stroke="#c084fc" stroke-width="1.5"/>
    <text x="175" y="240" font-size="9.5" fill="#c084fc" text-anchor="middle">Rainfall &gt; 1,400mm</text>

    <!-- Intersection Center (Optimal Site) -->
    <circle cx="175" cy="160" r="18" fill="#22c55e" fill-opacity="0.8" stroke="#ffffff" stroke-width="2"/>
    <text x="175" y="164" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">OPTIMAL</text>

    <rect x="15" y="260" width="315" height="50" rx="4" fill="#1e293b"/>
    <text x="172" y="280" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Boolean Overlay Logic (INTERSECTION)</text>
    <text x="172" y="298" font-size="9" fill="#cbd5e1" text-anchor="middle">[Slope &lt; 15°] AND [Soil = Volcanic] AND [Rain &gt; 1400mm]</text>
  </g>
</svg>
""")

# SVG 11: Disaster Management Flood Model (Lesson 11)
SVG_DISASTER_MANAGEMENT = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">DISASTER MANAGEMENT GIS: BUDALANGI FLOOD EVACUATION MODEL</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Integrating Digital Elevation Models (DEM), River Discharge, and Safe Transport Corridors</text>

  <!-- Main Map Display -->
  <rect x="45" y="85" width="480" height="320" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
  
  <!-- Elevation Zones (DEM Contours) -->
  <!-- Highland Safe Zone (>1,200m) -->
  <polygon points="45,85 525,85 525,180 45,150" fill="#15803d" fill-opacity="0.4"/>
  <text x="280" y="115" font-size="12" font-weight="bold" fill="#4ade80" text-anchor="middle">HIGHLAND SAFE REFUGE (&gt; 1,200m ASL)</text>

  <!-- Lowland Flood Inundation Zone (<1,150m) -->
  <polygon points="45,150 525,180 525,405 45,405" fill="#0284c7" fill-opacity="0.3"/>
  <text x="280" y="375" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">LOWLAND INUNDATION HAZARD ZONE (RIVER NZOIA BASIN)</text>

  <!-- River Nzoia Bursting Banks -->
  <path d="M45 280 Q200 360 360 260 T525 320" fill="none" stroke="#38bdf8" stroke-width="12" stroke-opacity="0.7"/>
  <text x="360" y="300" font-size="10" font-weight="bold" fill="#ffffff">River Nzoia (Flood Stage)</text>

  <!-- Flooded Village (Marooned) -->
  <circle cx="180" cy="310" r="14" fill="#ef4444" stroke="#ffffff" stroke-width="2"/>
  <text x="180" y="338" font-size="9" font-weight="bold" fill="#ef4444" text-anchor="middle">Village A (Marooned)</text>

  <!-- Safe Shelter Camp -->
  <rect x="360" y="110" width="30" height="25" rx="4" fill="#22c55e" stroke="#ffffff" stroke-width="2"/>
  <text x="375" y="150" font-size="9.5" font-weight="bold" fill="#4ade80" text-anchor="middle">Emergency Shelter Camp</text>

  <!-- Evacuation Route (Network Path) -->
  <path d="M180 310 L260 240 L375 135" fill="none" stroke="#fbbf24" stroke-width="4" stroke-dasharray="6,4"/>
  <polygon points="370,140 375,135 370,132" fill="#fbbf24"/>
  <text x="290" y="210" font-size="10" font-weight="bold" fill="#fbbf24">Optimal Evacuation Path</text>

  <!-- Right Panel: Model Workflow -->
  <g transform="translate(545, 85)">
    <rect x="0" y="0" width="210" height="320" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="105" y="25" font-size="12" font-weight="bold" fill="#f87171" text-anchor="middle">GIS DISASTER PROTOCOL</text>

    <rect x="15" y="40" width="180" height="55" rx="4" fill="#1e293b"/>
    <text x="25" y="58" font-size="10" font-weight="bold" fill="#38bdf8">1. DEM Slope Analysis</text>
    <text x="25" y="73" font-size="8.5" fill="#cbd5e1">Predicts water pooling</text>
    <text x="25" y="85" font-size="8.5" fill="#cbd5e1">in low-lying terrain.</text>

    <rect x="15" y="105" width="180" height="55" rx="4" fill="#1e293b"/>
    <text x="25" y="123" font-size="10" font-weight="bold" fill="#fbbf24">2. GPS Victim Triangulation</text>
    <text x="25" y="138" font-size="8.5" fill="#cbd5e1">Pins stranded families</text>
    <text x="25" y="150" font-size="8.5" fill="#cbd5e1">for boat &amp; heli rescue.</text>

    <rect x="15" y="170" width="180" height="55" rx="4" fill="#1e293b"/>
    <text x="25" y="188" font-size="10" font-weight="bold" fill="#4ade80">3. Network Routing</text>
    <text x="25" y="203" font-size="8.5" fill="#cbd5e1">Calculates dry roads to</text>
    <text x="25" y="215" font-size="8.5" fill="#cbd5e1">highland relief camps.</text>

    <rect x="15" y="235" width="180" height="70" rx="4" fill="#7f1d1d" fill-opacity="0.5" stroke="#ef4444" stroke-width="1"/>
    <text x="105" y="258" font-size="10" font-weight="bold" fill="#fca5a5" text-anchor="middle">BUDALANGI IMPACT</text>
    <text x="105" y="276" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Early warnings save lives</text>
    <text x="105" y="290" font-size="8.5" fill="#cbd5e1" text-anchor="middle">before flood crests peak.</text>
  </g>
</svg>
""")

# SVG 12: Precision Agriculture NDVI & Forest Conservation (Lesson 12)
SVG_PRECISION_AGRI_ECOLOGY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">PRECISION AGRICULTURE (NDVI) &amp; FOREST CONSERVATION</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Harnessing drone multispectral indices and satellite change detection</text>

  <!-- Left: Precision Agriculture NDVI Farm Grid -->
  <g transform="translate(35, 85)">
    <rect x="0" y="0" width="345" height="320" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#16a34a"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">PRECISION AGRI: NDVI CROP HEALTH MAP</text>

    <!-- 4x4 Farm Parcel Grid with NDVI Colors -->
    <!-- High Vigour (Green) -->
    <rect x="25" y="45" width="70" height="50" fill="#15803d" stroke="#1e293b" stroke-width="2"/>
    <rect x="100" y="45" width="70" height="50" fill="#16a34a" stroke="#1e293b" stroke-width="2"/>
    <rect x="175" y="45" width="70" height="50" fill="#22c55e" stroke="#1e293b" stroke-width="2"/>
    <rect x="250" y="45" width="70" height="50" fill="#15803d" stroke="#1e293b" stroke-width="2"/>

    <!-- Moderate Stress (Yellow/Orange) -->
    <rect x="25" y="100" width="70" height="50" fill="#ca8a04" stroke="#1e293b" stroke-width="2"/>
    <rect x="100" y="100" width="70" height="50" fill="#eab308" stroke="#1e293b" stroke-width="2"/>
    <rect x="175" y="100" width="70" height="50" fill="#16a34a" stroke="#1e293b" stroke-width="2"/>
    <rect x="250" y="100" width="70" height="50" fill="#ca8a04" stroke="#1e293b" stroke-width="2"/>

    <!-- Severe Stress (Red/Brown) -->
    <rect x="25" y="155" width="70" height="50" fill="#dc2626" stroke="#1e293b" stroke-width="2"/>
    <rect x="100" y="155" width="70" height="50" fill="#ef4444" stroke="#1e293b" stroke-width="2"/>
    <rect x="175" y="155" width="70" height="50" fill="#ca8a04" stroke="#1e293b" stroke-width="2"/>
    <rect x="250" y="155" width="70" height="50" fill="#15803d" stroke="#1e293b" stroke-width="2"/>

    <text x="172" y="230" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">NDVI = (NIR - Red) / (NIR + Red)</text>
    
    <!-- Variable Rate Application Action -->
    <rect x="20" y="245" width="305" height="60" rx="6" fill="#1e293b"/>
    <text x="30" y="265" font-size="10" font-weight="bold" fill="#fbbf24">Variable Rate Technology (VRT):</text>
    <text x="30" y="280" font-size="9" fill="#cbd5e1">- Green patches: Zero extra fertilizer applied.</text>
    <text x="30" y="295" font-size="9" fill="#f87171">- Red patches: GPS tractor applies targeted fertilizer.</text>
  </g>

  <!-- Right: Mau Forest Deforestation Tracking -->
  <g transform="translate(420, 85)">
    <rect x="0" y="0" width="345" height="320" rx="10" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#0284c7"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">MAU FOREST COMPLEX: CANOPY CHANGE</text>

    <!-- Multi-temporal Satellite Comparison -->
    <!-- 2010 Canopy -->
    <g transform="translate(20, 45)">
      <rect x="0" y="0" width="145" height="150" fill="#1e293b" rx="4"/>
      <polygon points="10,20 135,20 120,130 25,120" fill="#15803d"/>
      <text x="72" y="145" font-size="9.5" font-weight="bold" fill="#4ade80" text-anchor="middle">Year 2010 (Intact)</text>
    </g>

    <!-- 2026 Canopy with Clearings -->
    <g transform="translate(180, 45)">
      <rect x="0" y="0" width="145" height="150" fill="#1e293b" rx="4"/>
      <polygon points="10,20 135,20 120,130 25,120" fill="#15803d"/>
      <!-- Deforested patches (red) -->
      <polygon points="40,40 80,45 70,80 30,70" fill="#ef4444"/>
      <polygon points="85,90 120,95 110,120 75,115" fill="#ef4444"/>
      <text x="72" y="145" font-size="9.5" font-weight="bold" fill="#f87171" text-anchor="middle">Year 2026 (Illegal Logging)</text>
    </g>

    <!-- Takeaway summary -->
    <rect x="20" y="210" width="305" height="95" rx="6" fill="#1e293b"/>
    <text x="30" y="230" font-size="10.5" font-weight="bold" fill="#38bdf8">KFS Conservation Monitoring:</text>
    <text x="30" y="248" font-size="9" fill="#cbd5e1">1. Temporal difference algorithm detects canopy drop.</text>
    <text x="30" y="263" font-size="9" fill="#cbd5e1">2. Generates real-time GPS coordinates of logging.</text>
    <text x="30" y="278" font-size="9" fill="#cbd5e1">3. Forest rangers deployed directly to coordinates.</text>
  </g>
</svg>
""")

# SVG 13: Locality Mapping 5-Step Workflow & QA Checklist (Lesson 13)
SVG_LOCALITY_MAPPING_QA = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">LOCALITY MAPPING PROJECT WORKFLOW &amp; QA AUDIT</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">End-to-end practical execution from field collection to cartographic quality control</text>

  <!-- 5 Sequential Workflow Stages (Top Half) -->
  <!-- Step 1 -->
  <g transform="translate(35, 85)">
    <rect x="0" y="0" width="130" height="110" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="65" cy="25" r="12" fill="#0284c7"/>
    <text x="65" y="29" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">1</text>
    <text x="65" y="55" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">PLANNING</text>
    <text x="65" y="72" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Define map scope</text>
    <text x="65" y="85" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&amp; asset themes</text>
  </g>
  <polygon points="172,140 182,140 182,136 188,143 182,150 182,146 172,146" fill="#64748b"/>

  <!-- Step 2 -->
  <g transform="translate(190, 85)">
    <rect x="0" y="0" width="130" height="110" rx="8" fill="#0f172a" stroke="#fbbf24" stroke-width="2"/>
    <circle cx="65" cy="25" r="12" fill="#d97706"/>
    <text x="65" y="29" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">2</text>
    <text x="65" y="55" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">FIELD SURVEY</text>
    <text x="65" y="72" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Record GPS points</text>
    <text x="65" y="85" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&amp; ground sketches</text>
  </g>
  <polygon points="327,140 337,140 337,136 343,143 337,150 337,146 327,146" fill="#64748b"/>

  <!-- Step 3 -->
  <g transform="translate(345, 85)">
    <rect x="0" y="0" width="130" height="110" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <circle cx="65" cy="25" r="12" fill="#9333ea"/>
    <text x="65" y="29" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">3</text>
    <text x="65" y="55" font-size="11" font-weight="bold" fill="#c084fc" text-anchor="middle">DATA ENTRY</text>
    <text x="65" y="72" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Import .gpx tracks</text>
    <text x="65" y="85" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&amp; heads-up trace</text>
  </g>
  <polygon points="482,140 492,140 492,136 498,143 492,150 492,146 482,146" fill="#64748b"/>

  <!-- Step 4 -->
  <g transform="translate(500, 85)">
    <rect x="0" y="0" width="130" height="110" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="2"/>
    <circle cx="65" cy="25" r="12" fill="#db2777"/>
    <text x="65" y="29" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">4</text>
    <text x="65" y="55" font-size="11" font-weight="bold" fill="#f472b6" text-anchor="middle">STYLING</text>
    <text x="65" y="72" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Standard colors,</text>
    <text x="65" y="85" font-size="8.5" fill="#cbd5e1" text-anchor="middle">icons &amp; hierarchy</text>
  </g>
  <polygon points="637,140 647,140 647,136 653,143 647,150 647,146 637,146" fill="#64748b"/>

  <!-- Step 5 -->
  <g transform="translate(655, 85)">
    <rect x="0" y="0" width="110" height="110" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <circle cx="55" cy="25" r="12" fill="#16a34a"/>
    <text x="55" y="29" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">5</text>
    <text x="55" y="55" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">PUBLISH</text>
    <text x="55" y="72" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Export final</text>
    <text x="55" y="85" font-size="8.5" fill="#cbd5e1" text-anchor="middle">thematic map</text>
  </g>

  <!-- Bottom Half: KICD Quality Control Audit Checklist -->
  <g transform="translate(35, 215)">
    <rect x="0" y="0" width="730" height="190" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="730" height="30" rx="10" fill="#0284c7"/>
    <text x="365" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">KICD QUALITY CONTROL &amp; CARTOGRAPHIC AUDIT CHECKLIST</text>

    <!-- Checklist Item 1 -->
    <g transform="translate(25, 45)">
      <circle cx="10" cy="15" r="8" fill="#22c55e"/>
      <text x="10" y="19" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">✓</text>
      <text x="25" y="18" font-size="11" font-weight="bold" fill="#4ade80">1. Positional Accuracy:</text>
      <text x="25" y="34" font-size="9.5" fill="#cbd5e1">Coordinates match true physical ground features within acceptable GPS error bounds (&lt; ±5m).</text>
    </g>

    <!-- Checklist Item 2 -->
    <g transform="translate(25, 90)">
      <circle cx="10" cy="15" r="8" fill="#22c55e"/>
      <text x="10" y="19" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">✓</text>
      <text x="25" y="18" font-size="11" font-weight="bold" fill="#fbbf24">2. Marginal Completeness:</text>
      <text x="25" y="34" font-size="9.5" fill="#cbd5e1">All 6 essentials present: Title, Key/Legend, Scale Bar, North Arrow, Coordinate Frame, and Source.</text>
    </g>

    <!-- Checklist Item 3 -->
    <g transform="translate(25, 135)">
      <circle cx="10" cy="15" r="8" fill="#22c55e"/>
      <text x="10" y="19" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">✓</text>
      <text x="25" y="18" font-size="11" font-weight="bold" fill="#38bdf8">3. Cartographic Legibility:</text>
      <text x="25" y="34" font-size="9.5" fill="#cbd5e1">Zero symbol collisions, intuitive colors (green forest, blue water), and balanced layout hierarchy.</text>
    </g>
  </g>
</svg>
""")

TOPIC_4_SVGS = {
    1: SVG_GEOSPATIAL_PIPELINE,
    2: SVG_LAYER_STACK,
    3: SVG_5_COMPONENTS,
    4: SVG_GLOBAL_GRID,
    5: SVG_COORDINATE_CONVERSION,
    6: SVG_GPS_TRILATERATION,
    7: SVG_REMOTE_SENSING_COMPOSITE,
    8: SVG_DIGITIZATION_WORKFLOW,
    9: SVG_MAP_LAYOUT_MARGINALS,
    10: SVG_SPATIAL_ANALYSIS,
    11: SVG_DISASTER_MANAGEMENT,
    12: SVG_PRECISION_AGRI_ECOLOGY,
    13: SVG_LOCALITY_MAPPING_QA,
}

def enrich_topic_4():
    print("=" * 80)
    print("VLearn Visual Enrichment Engine: Grade 10 Geography — Topic 4: GIS")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name="Geography").first()
    topic = Topic.objects.filter(subject=subject, order=4).first()

    if not topic:
        raise RuntimeError("Topic 4 'Geographic Information System (GIS)' not found!")

    verified_images_path = os.path.join(os.path.dirname(__file__), 'grade10_geography_topic4_verified_images.json')
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
                            "topic_order": 4
                        }
                    }
                )
                asset.url = img_data['url']
                asset.status = "attached"
                asset.save()
                asset.blocks.add(hook_block)
                print(f"  + Attached Wikimedia Photographic Hook: {img_data['url'][:55]}...")

        # 2. Attach Custom Vector SVG
        svg_xml = TOPIC_4_SVGS.get(int(u_order))
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
                            "topic_order": 4
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
                        "topic_order": 4
                    }
                }
            )
            v_asset.url = vid_url
            v_asset.status = "attached"
            v_asset.save()
            v_asset.blocks.add(video_block)
            print(f"  + Attached Educational YouTube Video: {vid_url}")

    print("\n" + "=" * 80)
    print("Topic 4 Visual Enrichment Completed Successfully!")
    print("=" * 80)

if __name__ == "__main__":
    enrich_topic_4()
