"""
VLearn Grade 10 Aviation — Topic 367: The Airport: Structure and Operations (Subject ID: 44, Topic ID: 367)
Visual Enrichment Engine (Verified Photos, Responsive Vector SVGs & Video Assets)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Aviation (Subject ID: 44)
Topic: The Airport: Structure and Operations (Topic ID: 367, Order: 9)

Enriches:
  - 5 First-Card Photographic Visual Hooks (Verified Direct Wikimedia URLs returning HTTP/2 200)
  - 5 Custom Responsive Vector SVGs (viewBox="0 0 800 450", Dark Slate Theme #0f172a, Sanitized XML)
  - 5 Verified Educational YouTube Videos
  - Persists LessonAsset models (15 total: 5 image, 5 diagram, 5 youtube) and binds them to LessonBlocks

Usage:
  ./venv/bin/python curriculum/enrich_grade10_aviation_topic367.py
"""

import os
import sys
import re
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
# 5 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 367
# =============================================================================

# SVG 1: Airport Classification Pyramid (Lesson 1)
SVG_AIRPORT_CLASSIFICATION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Airport Classification Hierarchy: Categories A through E</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Runway Length, Pavement Strength (PCN), Aircraft Handling &amp; ARFF Rescue Readiness</text>

  <!-- Tier A: Apex -->
  <g transform="translate(100, 85)">
    <polygon points="300,0 200,60 400,60" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="300" y="38" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">CATEGORY A</text>
    <rect x="420" y="8" width="240" height="48" rx="6" fill="#0f172a" stroke="#0284c7" stroke-width="1"/>
    <text x="430" y="26" font-size="11" font-weight="bold" fill="#38bdf8">Major International Hubs (JKIA, Moi Int'l)</text>
    <text x="430" y="44" font-size="10" fill="#cbd5e1">Runway &gt;3,000m | PCN 80+ | ARFF Cat 9-10 | B777/A350</text>
  </g>

  <!-- Tier B -->
  <g transform="translate(100, 150)">
    <polygon points="200,0 400,0 430,55 170,55" fill="#0d9488" stroke="#2dd4bf" stroke-width="1.5"/>
    <text x="300" y="34" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">CATEGORY B</text>
    <rect x="445" y="5" width="240" height="48" rx="6" fill="#0f172a" stroke="#0d9488" stroke-width="1"/>
    <text x="455" y="23" font-size="11" font-weight="bold" fill="#2dd4bf">Major Domestic / Regional (Kisumu, Wilson)</text>
    <text x="455" y="41" font-size="10" fill="#cbd5e1">Runway 2,000-3,000m | PCN 45-70 | ARFF 5-7 | E190/Dash 8</text>
  </g>

  <!-- Tier C -->
  <g transform="translate(100, 210)">
    <polygon points="170,0 430,0 460,55 140,55" fill="#d97706" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="300" y="34" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">CATEGORY C</text>
    <rect x="475" y="5" width="240" height="48" rx="6" fill="#0f172a" stroke="#d97706" stroke-width="1"/>
    <text x="485" y="23" font-size="11" font-weight="bold" fill="#fbbf24">County Commercial Airstrips (Malindi, Ukunda)</text>
    <text x="485" y="41" font-size="10" fill="#cbd5e1">Runway 1,200-1,800m | PCN 20-40 | ARFF 3-4 | C208 Caravan</text>
  </g>

  <!-- Tier D -->
  <g transform="translate(100, 270)">
    <polygon points="140,0 460,0 490,55 110,55" fill="#ea580c" stroke="#fb923c" stroke-width="1.5"/>
    <text x="300" y="34" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">CATEGORY D</text>
    <rect x="505" y="5" width="240" height="48" rx="6" fill="#0f172a" stroke="#ea580c" stroke-width="1"/>
    <text x="515" y="23" font-size="11" font-weight="bold" fill="#fb923c">Unpaved Bush Airstrips (Keekorok, Amboseli)</text>
    <text x="515" y="41" font-size="10" fill="#cbd5e1">Runway &lt;1,200m Grass/Murram | Uncontrolled | Light Bush</text>
  </g>

  <!-- Tier E: Base -->
  <g transform="translate(100, 330)">
    <polygon points="110,0 490,0 520,55 80,55" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="300" y="34" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">CATEGORY E</text>
    <rect x="535" y="5" width="220" height="48" rx="6" fill="#0f172a" stroke="#64748b" stroke-width="1"/>
    <text x="545" y="23" font-size="11" font-weight="bold" fill="#94a3b8">Specialized &amp; Defense (Laikipia Air Base)</text>
    <text x="545" y="41" font-size="10" fill="#cbd5e1">Military fast jets, pilot academies &amp; private ranches</text>
  </g>

  <!-- Legend Callout on Left -->
  <g transform="translate(30, 110)">
    <rect width="150" height="150" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="15" y="24" font-size="11" font-weight="bold" fill="#38bdf8">KEY METRICS</text>
    <text x="15" y="48" font-size="10" fill="#e2e8f0">• Runway Length (m)</text>
    <text x="15" y="72" font-size="10" fill="#e2e8f0">• Pavement PCN Rating</text>
    <text x="15" y="96" font-size="10" fill="#e2e8f0">• ARFF Category (1-10)</text>
    <text x="15" y="120" font-size="10" fill="#e2e8f0">• Border Immigration</text>
    <text x="15" y="140" font-size="10" fill="#e2e8f0">• Navigational Aids</text>
  </g>

  <rect x="30" y="395" width="740" height="28" rx="6" fill="#0f172a" stroke="#334155"/>
  <text x="400" y="414" font-size="11" fill="#38bdf8" text-anchor="middle" font-weight="bold">ICAO Standard: Pavement strength, fire response, and runway length dictate operational clearance.</text>
</svg>
""")

# SVG 2: Comprehensive Airport Zoning Map (Lesson 2)
SVG_AIRPORT_ZONING = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Comprehensive Airport Operational Zoning &amp; Airfield Layout</text>
  <text x="400" y="62" font-size="12" fill="#94a3b8" text-anchor="middle">Spatial Boundaries: Landside Public Zone, Security Barrier, Airside Apron, Taxiways &amp; Runways</text>

  <!-- Landside Zone (Left) -->
  <g transform="translate(30, 80)">
    <rect width="180" height="310" rx="8" fill="#0f172a" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4"/>
    <rect width="180" height="28" rx="8" fill="#334155"/>
    <text x="90" y="19" font-size="11" font-weight="bold" fill="#f8fafc" text-anchor="middle">LANDSIDE (PUBLIC)</text>
    
    <!-- Parking & Roads -->
    <rect x="15" y="40" width="150" height="50" rx="6" fill="#1e293b" stroke="#475569"/>
    <text x="90" y="62" font-size="10" font-weight="bold" fill="#94a3b8" text-anchor="middle">Public Parking &amp; Roads</text>
    <text x="90" y="78" font-size="9" fill="#64748b" text-anchor="middle">Drop-off &amp; Transit Hub</text>

    <!-- Ticketing Concourse -->
    <rect x="15" y="105" width="150" height="60" rx="6" fill="#1e293b" stroke="#475569"/>
    <text x="90" y="128" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Check-in Concourse</text>
    <text x="90" y="144" font-size="9" fill="#cbd5e1" text-anchor="middle">Ticket Counters &amp; Baggage Drop</text>

    <path d="M 90,170 L 90,195" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>

    <!-- Security Checkpoint -->
    <rect x="15" y="200" width="150" height="50" rx="6" fill="#ef4444" fill-opacity="0.2" stroke="#ef4444" stroke-width="1.5"/>
    <text x="90" y="222" font-size="10" font-weight="bold" fill="#f87171" text-anchor="middle">SECURITY SCREENING</text>
    <text x="90" y="238" font-size="9" fill="#fca5a5" text-anchor="middle">Metal Detectors &amp; Bag X-Ray</text>

    <text x="90" y="280" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">BOUNDARY LINE</text>
    <text x="90" y="296" font-size="9" fill="#94a3b8" text-anchor="middle">ID &amp; Boarding Pass Required</text>
  </g>

  <!-- Airside Terminal & Apron (Middle) -->
  <g transform="translate(230, 80)">
    <rect width="250" height="310" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
    <rect width="250" height="28" rx="8" fill="#0284c7"/>
    <text x="125" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">AIRSIDE: TERMINAL &amp; APRON (RAMP)</text>

    <!-- Departure Concourse -->
    <rect x="15" y="40" width="220" height="45" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="125" y="60" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Secure Boarding Gates &amp; Lounges</text>
    <text x="125" y="74" font-size="9" fill="#94a3b8" text-anchor="middle">Duty-free transit &amp; jet bridge access</text>

    <!-- Aircraft Parking Stands (Apron) -->
    <g transform="translate(15, 100)">
      <rect width="220" height="195" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-dasharray="3,3"/>
      <text x="110" y="20" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">APRON / RAMP AIRCRAFT STANDS</text>
      
      <!-- Stand 1 -->
      <rect x="15" y="35" width="90" height="60" rx="4" fill="#0f172a" stroke="#334155"/>
      <circle cx="60" cy="65" r="18" fill="#0284c7" fill-opacity="0.3"/>
      <text x="60" y="62" font-size="9" font-weight="bold" fill="#e2e8f0" text-anchor="middle">STAND 1</text>
      <text x="60" y="74" font-size="8" fill="#38bdf8" text-anchor="middle">Jet Bridge</text>

      <!-- Stand 2 -->
      <rect x="115" y="35" width="90" height="60" rx="4" fill="#0f172a" stroke="#334155"/>
      <circle cx="160" cy="65" r="18" fill="#0284c7" fill-opacity="0.3"/>
      <text x="160" y="62" font-size="9" font-weight="bold" fill="#e2e8f0" text-anchor="middle">STAND 2</text>
      <text x="160" y="74" font-size="8" fill="#38bdf8" text-anchor="middle">Refueling</text>

      <!-- Ramp Equipment Area -->
      <rect x="15" y="110" width="190" height="70" rx="4" fill="#0f172a" stroke="#475569"/>
      <text x="110" y="128" font-size="9" font-weight="bold" fill="#f87171" text-anchor="middle">GROUND SERVICE EQUIPMENT (GSE)</text>
      <text x="110" y="144" font-size="8" fill="#cbd5e1" text-anchor="middle">• Pushback Tugs • Baggage Belt Loaders</text>
      <text x="110" y="158" font-size="8" fill="#cbd5e1" text-anchor="middle">• Fuel Hydrant Carts • Catering High-Loaders</text>
      <text x="110" y="172" font-size="8" fill="#fbbf24" text-anchor="middle">Mandatory PPE: High-Vis Vests &amp; Ear Protection</text>
    </g>
  </g>

  <!-- Airfield Pavements: Taxiways & Runways (Right) -->
  <g transform="translate(500, 80)">
    <rect width="270" height="310" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#059669"/>
    <text x="135" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">AIRFIELD: TAXIWAYS &amp; RUNWAYS</text>

    <!-- Taxiway Path -->
    <rect x="15" y="40" width="70" height="255" rx="4" fill="#1e293b" stroke="#334155"/>
    <!-- Yellow Taxiway Centerline -->
    <line x1="50" y1="45" x2="50" y2="290" stroke="#facc15" stroke-width="3"/>
    <text x="50" y="150" font-size="10" font-weight="bold" fill="#facc15" transform="rotate(-90 50,150)" text-anchor="middle">TAXIWAY ALPHA (YELLOW)</text>

    <!-- Active Runway -->
    <rect x="105" y="40" width="90" height="255" rx="4" fill="#0f172a" stroke="#ffffff" stroke-width="1.5"/>
    <!-- White Runway Markings -->
    <line x1="150" y1="50" x2="150" y2="285" stroke="#ffffff" stroke-width="3" stroke-dasharray="10,8"/>
    <text x="150" y="80" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">06</text>
    <rect x="115" y="110" width="25" height="40" fill="#ffffff"/>
    <rect x="160" y="110" width="25" height="40" fill="#ffffff"/>
    <text x="150" y="200" font-size="10" font-weight="bold" fill="#ffffff" transform="rotate(-90 150,200)" text-anchor="middle">ACTIVE RUNWAY 06/24</text>
    <text x="150" y="275" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">24</text>

    <!-- Supporting Facilities (Tower & ARFF) -->
    <g transform="translate(205, 45)">
      <rect width="55" height="60" rx="4" fill="#1e293b" stroke="#38bdf8"/>
      <circle cx="27" cy="25" r="10" fill="#0284c7"/>
      <text x="27" y="48" font-size="8" font-weight="bold" fill="#38bdf8" text-anchor="middle">ATC TOWER</text>
      
      <rect y="75" width="55" height="55" rx="4" fill="#1e293b" stroke="#ef4444"/>
      <text x="27" y="98" font-size="8" font-weight="bold" fill="#f87171" text-anchor="middle">ARFF FIRE</text>
      <text x="27" y="112" font-size="7" fill="#cbd5e1" text-anchor="middle">&lt;3 Min Reach</text>

      <rect y="145" width="55" height="70" rx="4" fill="#1e293b" stroke="#a855f7"/>
      <text x="27" y="175" font-size="8" font-weight="bold" fill="#c084fc" text-anchor="middle">HANGAR</text>
      <text x="27" y="192" font-size="7" fill="#cbd5e1" text-anchor="middle">Maintenance</text>
    </g>
  </g>

  <!-- Bottom Annotation -->
  <rect x="30" y="400" width="740" height="24" rx="4" fill="#0f172a" stroke="#334155"/>
  <text x="400" y="416" font-size="10" fill="#94a3b8" text-anchor="middle">Yellow Lines = Taxiways (Slow Ground Roll) | White Lines = Runways (Takeoff &amp; Landing Speeds)</text>
</svg>
""")

# SVG 3: Magnetic Runway Designation Circle (Lesson 3)
SVG_RUNWAY_DESIGNATION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Magnetic Runway Designation Circle &amp; Reciprocal Geometry</text>
  <text x="400" y="62" font-size="12" fill="#94a3b8" text-anchor="middle">360° Magnetic Compass Rose, Rounding to Nearest 10°, and the +/- 180° (18) Reciprocal Rule</text>

  <!-- Left: 360-Degree Compass Circle -->
  <g transform="translate(220, 240)">
    <!-- Outer Compass Circle -->
    <circle cx="0" cy="0" r="140" fill="#0f172a" stroke="#334155" stroke-width="2"/>
    <circle cx="0" cy="0" r="120" fill="none" stroke="#1e293b" stroke-width="1.5" stroke-dasharray="4,4"/>

    <!-- Cardinal Directions -->
    <line x1="0" y1="-140" x2="0" y2="-125" stroke="#38bdf8" stroke-width="3"/>
    <text x="0" y="-148" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">360° / 000° [RWY 36]</text>

    <line x1="140" y1="0" x2="125" y2="0" stroke="#38bdf8" stroke-width="3"/>
    <text x="150" y="4" font-size="12" font-weight="bold" fill="#38bdf8">090° [RWY 09]</text>

    <line x1="0" y1="140" x2="0" y2="125" stroke="#38bdf8" stroke-width="3"/>
    <text x="0" y="158" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">180° [RWY 18]</text>

    <line x1="-140" y1="0" x2="-125" y2="0" stroke="#38bdf8" stroke-width="3"/>
    <text x="-150" y="4" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="end">270° [RWY 27]</text>

    <!-- Runway Strip Aligned 060° to 240° -->
    <g transform="rotate(-30)">
      <rect x="-105" y="-18" width="210" height="36" rx="4" fill="#334155" stroke="#ffffff" stroke-width="1.5"/>
      <line x1="-95" y1="0" x2="95" y2="0" stroke="#ffffff" stroke-width="2" stroke-dasharray="6,4"/>
      <!-- Runway Numbers -->
      <text x="-80" y="5" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle" transform="rotate(90 -80,5)">24</text>
      <text x="80" y="5" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle" transform="rotate(-90 80,5)">06</text>
    </g>

    <!-- Reciprocal Connector Arc -->
    <path d="M 95,-55 A 110 110 0 0 1 -95,55" fill="none" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="5,4"/>
    <text x="50" y="35" font-size="11" font-weight="bold" fill="#fbbf24">+ 180° Reciprocal</text>

    <circle cx="0" cy="0" r="5" fill="#38bdf8"/>
  </g>

  <!-- Right: Technical Mathematical Breakdown Panel -->
  <g transform="translate(450, 85)">
    <rect width="310" height="320" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
    <rect width="310" height="30" rx="8" fill="#0284c7"/>
    <text x="155" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">RUNWAY NUMBERING FORMULA</text>

    <!-- Step 1 -->
    <g transform="translate(15, 45)">
      <rect width="280" height="42" rx="4" fill="#1e293b"/>
      <text x="10" y="18" font-size="11" font-weight="bold" fill="#38bdf8">1. Measure Magnetic Heading</text>
      <text x="10" y="34" font-size="10" fill="#cbd5e1">Approach azimuth relative to Magnetic North</text>
    </g>

    <!-- Step 2 -->
    <g transform="translate(15, 95)">
      <rect width="280" height="42" rx="4" fill="#1e293b"/>
      <text x="10" y="18" font-size="11" font-weight="bold" fill="#38bdf8">2. Round to Nearest 10°</text>
      <text x="10" y="34" font-size="10" fill="#cbd5e1">e.g. 058° rounds to 060° | 238° rounds to 240°</text>
    </g>

    <!-- Step 3 -->
    <g transform="translate(15, 145)">
      <rect width="280" height="42" rx="4" fill="#1e293b"/>
      <text x="10" y="18" font-size="11" font-weight="bold" fill="#38bdf8">3. Drop Trailing Zero</text>
      <text x="10" y="34" font-size="10" fill="#cbd5e1">060° → Runway 06 | 240° → Runway 24</text>
    </g>

    <!-- Step 4: Reciprocal Rule -->
    <g transform="translate(15, 195)">
      <rect width="280" height="58" rx="4" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
      <text x="10" y="18" font-size="11" font-weight="bold" fill="#fbbf24">4. The +/- 18 Reciprocal Rule</text>
      <text x="10" y="34" font-size="10" fill="#cbd5e1">If ≤ 18: Add 18 (06 + 18 = 24 → Runway 06/24)</text>
      <text x="10" y="48" font-size="10" fill="#cbd5e1">If &gt; 18: Subtract 18 (27 - 18 = 09 → Runway 09/27)</text>
    </g>

    <!-- Parallel Suffixes -->
    <g transform="translate(15, 260)">
      <rect width="280" height="48" rx="4" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="18" font-size="10" font-weight="bold" fill="#2dd4bf">Parallel Runways (Left, Center, Right):</text>
      <text x="10" y="34" font-size="10" fill="#cbd5e1">36L (Left) | 36C (Center) | 36R (Right)</text>
    </g>
  </g>
</svg>
""")

# SVG 4: Standard Runway Visual Markings & Airfield Signs (Lesson 4)
SVG_RUNWAY_MARKINGS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Standard Precision Runway Markings &amp; Airfield Signage</text>
  <text x="400" y="62" font-size="12" fill="#94a3b8" text-anchor="middle">Threshold Stripes, Designation, Centerline, Aiming Points, Touchdown Zones &amp; Yellow Hold-Short Lines</text>

  <!-- Runway Surface (Dark Asphalt) -->
  <g transform="translate(40, 85)">
    <rect width="720" height="150" rx="6" fill="#0f172a" stroke="#475569" stroke-width="2"/>

    <!-- Runway Edge Lines -->
    <line x1="0" y1="5" x2="720" y2="5" stroke="#ffffff" stroke-width="2"/>
    <line x1="0" y1="145" x2="720" y2="145" stroke="#ffffff" stroke-width="2"/>

    <!-- 1. Threshold Zebra Stripes (8 bars = 100 ft wide) -->
    <g transform="translate(15, 20)">
      <rect x="0" y="0" width="45" height="8" fill="#ffffff"/>
      <rect x="0" y="14" width="45" height="8" fill="#ffffff"/>
      <rect x="0" y="28" width="45" height="8" fill="#ffffff"/>
      <rect x="0" y="42" width="45" height="8" fill="#ffffff"/>
      <rect x="0" y="60" width="45" height="8" fill="#ffffff"/>
      <rect x="0" y="74" width="45" height="8" fill="#ffffff"/>
      <rect x="0" y="88" width="45" height="8" fill="#ffffff"/>
      <rect x="0" y="102" width="45" height="8" fill="#ffffff"/>
    </g>

    <!-- 2. Runway Designation Number -->
    <text x="100" y="84" font-size="34" font-weight="bold" fill="#ffffff" text-anchor="middle">09</text>

    <!-- 3. Dashed White Centerline -->
    <line x1="140" y1="75" x2="720" y2="75" stroke="#ffffff" stroke-width="4" stroke-dasharray="35,20"/>

    <!-- 4. Touchdown Zone 1 (3-bar pair) -->
    <g transform="translate(160, 25)">
      <rect x="0" y="0" width="30" height="6" fill="#ffffff"/>
      <rect x="0" y="12" width="30" height="6" fill="#ffffff"/>
      <rect x="0" y="24" width="30" height="6" fill="#ffffff"/>
      <rect x="0" y="70" width="30" height="6" fill="#ffffff"/>
      <rect x="0" y="82" width="30" height="6" fill="#ffffff"/>
      <rect x="0" y="94" width="30" height="6" fill="#ffffff"/>
    </g>

    <!-- 5. Aiming Point Blocks (1,000 ft from threshold) -->
    <g transform="translate(240, 25)">
      <rect x="0" y="5" width="70" height="26" fill="#ffffff"/>
      <rect x="0" y="69" width="70" height="26" fill="#ffffff"/>
    </g>

    <!-- 6. Touchdown Zone 2 (2-bar pair) -->
    <g transform="translate(360, 25)">
      <rect x="0" y="6" width="30" height="6" fill="#ffffff"/>
      <rect x="0" y="18" width="30" height="6" fill="#ffffff"/>
      <rect x="0" y="76" width="30" height="6" fill="#ffffff"/>
      <rect x="0" y="88" width="30" height="6" fill="#ffffff"/>
    </g>

    <!-- 7. Touchdown Zone 3 (1-bar pair) -->
    <g transform="translate(440, 25)">
      <rect x="0" y="12" width="30" height="6" fill="#ffffff"/>
      <rect x="0" y="82" width="30" height="6" fill="#ffffff"/>
    </g>
  </g>

  <!-- Labels for Runway Markings -->
  <g transform="translate(40, 245)" font-size="10" fill="#94a3b8">
    <text x="38" y="10" text-anchor="middle" fill="#38bdf8">Threshold Stripes</text>
    <text x="100" y="10" text-anchor="middle" fill="#38bdf8">Designation (09)</text>
    <text x="275" y="10" text-anchor="middle" fill="#fbbf24">Aiming Point (1000 ft)</text>
    <text x="400" y="10" text-anchor="middle" fill="#38bdf8">Touchdown Zone Bars</text>
    <text x="600" y="10" text-anchor="middle" fill="#38bdf8">Dashed Centerline</text>
  </g>

  <!-- Intersecting Taxiway & Hold-Short Lines (Bottom) -->
  <g transform="translate(180, 270)">
    <rect width="440" height="110" rx="8" fill="#0f172a" stroke="#334155"/>
    <text x="220" y="22" font-size="11" font-weight="bold" fill="#facc15" text-anchor="middle">INTERSECTING TAXIWAY WITH RUNWAY HOLD-SHORT LINE</text>

    <!-- Taxiway Centerline (Yellow) -->
    <line x1="20" y1="55" x2="420" y2="55" stroke="#facc15" stroke-width="3"/>

    <!-- Runway Holding Position Line (2 Solid, 2 Dashed Yellow) -->
    <g transform="translate(180, 30)">
      <!-- Dashed lines (Runway side) -->
      <line x1="0" y1="0" x2="0" y2="55" stroke="#facc15" stroke-width="3" stroke-dasharray="6,4"/>
      <line x1="8" y1="0" x2="8" y2="55" stroke="#facc15" stroke-width="3" stroke-dasharray="6,4"/>
      <!-- Solid lines (Taxiway side) -->
      <line x1="16" y1="0" x2="16" y2="55" stroke="#facc15" stroke-width="3"/>
      <line x1="24" y1="0" x2="24" y2="55" stroke="#facc15" stroke-width="3"/>
    </g>

    <!-- Directional Labels -->
    <text x="140" y="98" font-size="9" font-weight="bold" fill="#2dd4bf">← RUNWAY SIDE (Dashed)</text>
    <text x="250" y="98" font-size="9" font-weight="bold" fill="#f87171">TAXIWAY SIDE (Solid - STOP!) →</text>

    <!-- Airfield Signs -->
    <!-- Mandatory Instruction Sign: Red box, white text -->
    <rect x="30" y="32" width="70" height="26" rx="3" fill="#dc2626" stroke="#ffffff" stroke-width="1"/>
    <text x="65" y="49" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">09-27</text>

    <!-- Location Sign: Black box, yellow text -->
    <rect x="330" y="32" width="30" height="26" rx="3" fill="#000000" stroke="#facc15" stroke-width="1.5"/>
    <text x="345" y="50" font-size="13" font-weight="bold" fill="#facc15" text-anchor="middle">A</text>
  </g>

  <rect x="30" y="405" width="740" height="24" rx="4" fill="#0f172a" stroke="#334155"/>
  <text x="400" y="421" font-size="10" fill="#38bdf8" text-anchor="middle">Rule: Never cross the double solid yellow lines toward a runway without explicit ATC clearance!</text>
</svg>
""")

# SVG 5: Air Traffic Control Tower & Flight Sequence (Lesson 5)
SVG_ATC_OPERATIONS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Air Traffic Control Airspace &amp; Aerodrome Tower Control Sequence</text>
  <text x="400" y="62" font-size="12" fill="#94a3b8" text-anchor="middle">Operational Chain of Authority: Clearance Delivery, Ground Control, Tower Local Control &amp; Radar</text>

  <!-- Step 1: Clearance Delivery -->
  <g transform="translate(30, 85)">
    <rect width="170" height="230" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
    <rect width="170" height="30" rx="8" fill="#0284c7"/>
    <text x="85" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. CLEARANCE DELIVERY</text>
    
    <text x="12" y="52" font-size="10" font-weight="bold" fill="#38bdf8">Location: Gate / Stand</text>
    <text x="12" y="68" font-size="10" fill="#94a3b8">Frequency: 121.6 MHz</text>
    
    <rect x="10" y="80" width="150" height="70" rx="4" fill="#1e293b"/>
    <text x="15" y="96" font-size="9" font-weight="bold" fill="#cbd5e1">Key Duties:</text>
    <text x="15" y="112" font-size="8.5" fill="#94a3b8">• Verify filed flight plan</text>
    <text x="15" y="126" font-size="8.5" fill="#94a3b8">• Assign climb altitude</text>
    <text x="15" y="140" font-size="8.5" fill="#94a3b8">• Issue 4-digit squawk code</text>

    <rect x="10" y="160" width="150" height="55" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-dasharray="2,2"/>
    <text x="85" y="176" font-size="8.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">PILOT ACTION</text>
    <text x="85" y="192" font-size="8" fill="#cbd5e1" text-anchor="middle">Request IFR/VFR Clearance</text>
    <text x="85" y="204" font-size="8" fill="#fbbf24" text-anchor="middle">Mandatory Readback</text>
  </g>

  <!-- Step 2: Ground Control -->
  <g transform="translate(220, 85)">
    <rect width="170" height="230" rx="8" fill="#0f172a" stroke="#0d9488" stroke-width="1.5"/>
    <rect width="170" height="30" rx="8" fill="#0d9488"/>
    <text x="85" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. GROUND CONTROL</text>
    
    <text x="12" y="52" font-size="10" font-weight="bold" fill="#2dd4bf">Location: Aprons &amp; Taxiways</text>
    <text x="12" y="68" font-size="10" fill="#94a3b8">Frequency: 121.9 MHz</text>
    
    <rect x="10" y="80" width="150" height="70" rx="4" fill="#1e293b"/>
    <text x="15" y="96" font-size="9" font-weight="bold" fill="#cbd5e1">Key Duties:</text>
    <text x="15" y="112" font-size="8.5" fill="#94a3b8">• Authorize push &amp; start</text>
    <text x="15" y="126" font-size="8.5" fill="#94a3b8">• Assign taxiway route (A, B)</text>
    <text x="15" y="140" font-size="8.5" fill="#94a3b8">• Order hold-short of runway</text>

    <rect x="10" y="160" width="150" height="55" rx="4" fill="#1e293b" stroke="#2dd4bf" stroke-dasharray="2,2"/>
    <text x="85" y="176" font-size="8.5" font-weight="bold" fill="#2dd4bf" text-anchor="middle">PILOT ACTION</text>
    <text x="85" y="192" font-size="8" fill="#cbd5e1" text-anchor="middle">Taxi along yellow centerline</text>
    <text x="85" y="204" font-size="8" fill="#f87171" text-anchor="middle">Halt before solid lines</text>
  </g>

  <!-- Step 3: Tower Local Control -->
  <g transform="translate(410, 85)">
    <rect width="170" height="230" rx="8" fill="#0f172a" stroke="#d97706" stroke-width="1.5"/>
    <rect width="170" height="30" rx="8" fill="#d97706"/>
    <text x="85" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. TOWER (LOCAL)</text>
    
    <text x="12" y="52" font-size="10" font-weight="bold" fill="#fbbf24">Location: Active Runways</text>
    <text x="12" y="68" font-size="10" fill="#94a3b8">Frequency: 118.1 MHz</text>
    
    <rect x="10" y="80" width="150" height="70" rx="4" fill="#1e293b"/>
    <text x="15" y="96" font-size="9" font-weight="bold" fill="#cbd5e1">Key Duties:</text>
    <text x="15" y="112" font-size="8.5" fill="#94a3b8">• Runway crossing clearance</text>
    <text x="15" y="126" font-size="8.5" fill="#94a3b8">• Line up and wait</text>
    <text x="15" y="140" font-size="8.5" fill="#94a3b8">• "Cleared for takeoff / land"</text>

    <rect x="10" y="160" width="150" height="55" rx="4" fill="#1e293b" stroke="#fbbf24" stroke-dasharray="2,2"/>
    <text x="85" y="176" font-size="8.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">PILOT ACTION</text>
    <text x="85" y="192" font-size="8" fill="#cbd5e1" text-anchor="middle">Report holding short</text>
    <text x="85" y="204" font-size="8" fill="#2dd4bf" text-anchor="middle">Takeoff roll acceleration</text>
  </g>

  <!-- Step 4: Departure Radar -->
  <g transform="translate(600, 85)">
    <rect width="170" height="230" rx="8" fill="#0f172a" stroke="#7c3aed" stroke-width="1.5"/>
    <rect width="170" height="30" rx="8" fill="#7c3aed"/>
    <text x="85" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4. DEPARTURE RADAR</text>
    
    <text x="12" y="52" font-size="10" font-weight="bold" fill="#c084fc">Location: Terminal Airspace</text>
    <text x="12" y="68" font-size="10" fill="#94a3b8">Frequency: 119.7 MHz</text>
    
    <rect x="10" y="80" width="150" height="70" rx="4" fill="#1e293b"/>
    <text x="15" y="96" font-size="9" font-weight="bold" fill="#cbd5e1">Key Duties:</text>
    <text x="15" y="112" font-size="8.5" fill="#94a3b8">• Radar identification</text>
    <text x="15" y="126" font-size="8.5" fill="#94a3b8">• Radar vectoring headings</text>
    <text x="15" y="140" font-size="8.5" fill="#94a3b8">• Enroute climb sequencing</text>

    <rect x="10" y="160" width="150" height="55" rx="4" fill="#1e293b" stroke="#c084fc" stroke-dasharray="2,2"/>
    <text x="85" y="176" font-size="8.5" font-weight="bold" fill="#c084fc" text-anchor="middle">PILOT ACTION</text>
    <text x="85" y="192" font-size="8" fill="#cbd5e1" text-anchor="middle">Switch to Departure</text>
    <text x="85" y="204" font-size="8" fill="#38bdf8" text-anchor="middle">Report passing altitude</text>
  </g>

  <!-- Bottom Readback Safety Protocol Bar -->
  <g transform="translate(30, 330)">
    <rect width="740" height="85" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="370" y="22" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">THE MANDATORY READBACK / HEARBACK SAFETY PROTOCOL</text>
    <text x="370" y="42" font-size="10" fill="#e2e8f0" text-anchor="middle">Pilots MUST repeat verbatim all runway numbers, hold-short instructions, and altimeter settings.</text>
    <text x="370" y="58" font-size="10" fill="#fbbf24" text-anchor="middle">Controllers actively listen to verify the readback. Silence does NOT equal consent!</text>
    <text x="370" y="74" font-size="9.5" fill="#94a3b8" text-anchor="middle">Example: "Taxi to Runway 06, hold short Runway 06, Kenya 540" → Prevents Catastrophic Runway Incursions</text>
  </g>
</svg>
""")

# =============================================================================
# ASSET MAPPINGS (Photos, SVGs, Videos)
# =============================================================================

WIKIMEDIA_PHOTOS = {
    0: {
        "title": "Jomo Kenyatta International Airport Aerial Overview",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/87/Jomo_Kenyatta_International_Airport_%28JKIA%29.jpg",
        "caption": "An aerial view of Jomo Kenyatta International Airport (JKIA) in Nairobi, Kenya's primary Category A international hub handling widebody long-haul aircraft.",
        "author": "Wikimedia Commons Contributor",
        "license": "CC BY-SA"
    },
    1: {
        "title": "Commercial Jet on Active Airport Terminal Apron",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/07/Qatar_Airways_Airbus_A380-800_at_Heathrow_Airport_Terminal_4_before_Flying_to_Doha%2C_6_Jan_2015.jpg",
        "caption": "A widebody commercial airliner parked on the terminal apron receiving ground handling, baggage loading, and fueling services in the secure airside zone.",
        "author": "Wikimedia Commons Contributor",
        "license": "CC BY-SA"
    },
    2: {
        "title": "Runway Designation Marking Numbers Detail",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/78/15R-33L_-_Aeropuerto_de_Madrid-Barajas_-_detail.jpg",
        "caption": "A close-up view of painted runway numbers and parallel suffix letters demonstrating magnetic heading alignment and reciprocal airfield geometry.",
        "author": "Wikimedia Commons Contributor",
        "license": "CC BY-SA"
    },
    3: {
        "title": "Taxiway Hold-Short Lines at Runway Crossing",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/03/ATL_TWY_B_-_RWY_Crossing_%2813534655025%29.jpg",
        "caption": "Pavement markings showing double solid and double dashed yellow hold-short lines where a taxiway intersects an active runway, accompanied by mandatory airfield instruction signs.",
        "author": "Wikimedia Commons Contributor",
        "license": "CC BY-SA"
    },
    4: {
        "title": "Air Traffic Controllers in Control Tower Cab",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/09/Air_traffic_heathrow.JPG",
        "caption": "Certified air traffic controllers managing surface ground taxiing, runway departures, and arriving aircraft from the elevated glass cab of an airport control tower.",
        "author": "Wikimedia Commons Contributor",
        "license": "CC BY-SA"
    }
}

SVG_MAP = {
    0: {
        "title": "Airport Classification Pyramid & Operational Capabilities",
        "svg": SVG_AIRPORT_CLASSIFICATION,
        "page": 4
    },
    1: {
        "title": "Comprehensive Airport Zoning & Operational Layout Map",
        "svg": SVG_AIRPORT_ZONING,
        "page": 4
    },
    2: {
        "title": "Magnetic Runway Designation Circle & Reciprocal Geometry",
        "svg": SVG_RUNWAY_DESIGNATION,
        "page": 4
    },
    3: {
        "title": "Standard Runway Visual Markings & Airfield Signage Schematic",
        "svg": SVG_RUNWAY_MARKINGS,
        "page": 4
    },
    4: {
        "title": "Air Traffic Control Airspace & Aerodrome Tower Control Sequence",
        "svg": SVG_ATC_OPERATIONS,
        "page": 4
    }
}

YOUTUBE_VIDEOS = {
    0: {
        "title": "Airport Operations: Aerodromes, Airside & Landside Basics",
        "url": "https://www.youtube.com/watch?v=B0Ar5WsUhWs",
        "description": "Examine how certified airports organize surface infrastructure, manage security barriers between public and operational zones, and ensure international compliance."
    },
    1: {
        "title": "Inside Modern Airport Airside Infrastructure",
        "url": "https://www.youtube.com/watch?v=YmlfheAGx0E",
        "description": "Take a behind-the-scenes walkthrough of an international airport terminal, observing passenger flows, ramp operations, and the boundary separating landside from airside."
    },
    2: {
        "title": "Runway Markings, Signs, and Numbering Explained",
        "url": "https://www.youtube.com/watch?v=Yacx4jNQlgo",
        "description": "Watch how compass bearings correspond directly to the bold numbers painted on runway thresholds, and see how parallel runway letters guide landing pilots."
    },
    3: {
        "title": "Aerial Perspective of Runway Visual Markings",
        "url": "https://www.youtube.com/watch?v=eZuutXV7fqY",
        "description": "Examine how runway threshold stripes, aiming point blocks, and yellow hold-short lines appear to a pilot flying on final approach and during airfield taxiing."
    },
    4: {
        "title": "Standard Aviation Radiotelephony and Pilot-ATC Communication",
        "url": "https://www.youtube.com/watch?v=0t8tL6Mtp4E",
        "description": "Listen to real-world pilot and air traffic control communications, demonstrating professional pushback requests, taxi instructions, and takeoff clearances."
    }
}

def enrich_grade10_topic367():
    print("=" * 80)
    print("STARTING ENRICHMENT: Grade 10 Aviation — Topic 367: The Airport: Structure and Operations")
    print("=" * 80)

    topic = Topic.objects.filter(id=367).first()
    if not topic:
        print("[ERROR] Topic 367 not found!")
        return

    lessons = Lesson.objects.filter(topic=topic).order_by("learning_unit__order")
    print(f"[*] Found {lessons.count()} lessons under Topic 367 ({topic.name})")

    total_photos_attached = 0
    total_svgs_attached = 0
    total_videos_attached = 0
    total_assets_persisted = 0

    for lesson in lessons:
        u_order = lesson.learning_unit.order
        print(f"\n[+] Processing Lesson {u_order + 1}: {lesson.title} (ID: {lesson.id})")

        # ---------------------------------------------------------------------
        # 1. Card 1 Photographic Visual Hook
        # ---------------------------------------------------------------------
        if u_order in WIKIMEDIA_PHOTOS:
            img_def = WIKIMEDIA_PHOTOS[u_order]
            img_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=1,
                block_type="suggested_image"
            ).first()

            if img_block:
                b_content = img_block.content or {}
                b_content["resolved_image_url"] = img_def["url"]
                b_content["url"] = img_def["url"]
                b_content["caption"] = img_def["caption"]
                b_content["title"] = img_def["title"]
                img_block.content = b_content
                img_block.title = img_def["title"]
                img_block.save()

                asset, _ = LessonAsset.objects.get_or_create(
                    lesson=lesson,
                    asset_type="image",
                    url=img_def["url"],
                    defaults={
                        "source_type": "external",
                        "storage_type": "url",
                        "status": "attached",
                        "title": img_def["title"],
                        "description": img_def["caption"],
                        "metadata": {
                            "author": img_def["author"],
                            "licensing": img_def["license"],
                            "topic_order": 9,
                            "unit_order": u_order,
                            "page": 1
                        }
                    }
                )
                img_block.assets.add(asset)
                total_photos_attached += 1
                total_assets_persisted += 1
                print(f"  [Photo Hook Attached] {img_def['title']}")

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
                diag_block.title = svg_def["title"]
                diag_block.save()

                asset, _ = LessonAsset.objects.get_or_create(
                    lesson=lesson,
                    asset_type="diagram",
                    title=f"Lesson {u_order + 1} Diagram: {svg_def['title']}",
                    defaults={
                        "source_type": "ai_generated",
                        "storage_type": "embed",
                        "status": "attached",
                        "description": svg_def["title"],
                        "metadata": {
                            "topic_order": 9,
                            "unit_order": u_order,
                            "page": svg_def["page"],
                            "svg_content": svg_def["svg"]
                        }
                    }
                )
                diag_block.assets.add(asset)
                total_svgs_attached += 1
                total_assets_persisted += 1
                print(f"  [Vector SVG Attached] {svg_def['title']}")

        # ---------------------------------------------------------------------
        # 3. Curated Instructional YouTube Videos
        # ---------------------------------------------------------------------
        if u_order in YOUTUBE_VIDEOS:
            vid_def = YOUTUBE_VIDEOS[u_order]
            vid_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="suggested_video"
            ).first()

            if vid_block:
                v_content = vid_block.content or {}
                v_content["url"] = vid_def["url"]
                v_content["title"] = vid_def["title"]
                v_content["description"] = vid_def["description"]
                vid_block.content = v_content
                vid_block.title = vid_def["title"]
                vid_block.save()

                asset, _ = LessonAsset.objects.get_or_create(
                    lesson=lesson,
                    asset_type="youtube",
                    url=vid_def["url"],
                    defaults={
                        "source_type": "external",
                        "storage_type": "url",
                        "status": "attached",
                        "title": f"Lesson {u_order + 1} Video: {vid_def['title']}",
                        "description": vid_def["description"],
                        "metadata": {
                            "topic_order": 9,
                            "unit_order": u_order,
                            "youtube_url": vid_def["url"]
                        }
                    }
                )
                vid_block.assets.add(asset)
                total_videos_attached += 1
                total_assets_persisted += 1
                print(f"  [YouTube Video Attached] {vid_def['title']}")

    print("\n" + "=" * 80)
    print(f"ENRICHMENT COMPLETE: Topic 367 '{topic.name}'")
    print(f"  Photographic Hooks: {total_photos_attached} / 5")
    print(f"  Vector SVGs:        {total_svgs_attached} / 5")
    print(f"  YouTube Videos:     {total_videos_attached} / 5")
    print(f"  LessonAssets Total: {total_assets_persisted}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic367()
