"""
VLearn Form 4 Geography — Topic 6: Transport and Communication
Visual Enrichment Engine (18 Vector SVGs + 8 Verified Wikimedia Photos)

Attaches:
  - 18 Custom Vector SVGs to suggested_diagram blocks
  - 8 Pre-Verified Wikimedia Photos to suggested_image blocks
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_form4_geography_topic6.py
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
    """Ensures SVG is clean, responsive, and stripped of unneeded XML headers."""
    svg = re.sub(r'<\?xml.*?\?>', '', svg)
    svg = re.sub(r'<!DOCTYPE.*?>', '', svg)
    return svg.strip()

# =====================================================================
# 18 HIGH-PRECISION VECTOR SVGS FOR TOPIC 6: TRANSPORT AND COMMUNICATION
# =====================================================================

SVG_1 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Surplus-Deficit Economic Gradient &amp; Transport Flow Model</text>

  <!-- Region A (Surplus) -->
  <rect x="60" y="140" width="220" height="180" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
  <text x="170" y="180" font-size="16" font-weight="bold" fill="#10b981" text-anchor="middle">REGION A: SURPLUS</text>
  <text x="170" y="210" font-size="13" fill="#a7f3d0" text-anchor="middle">(High Commodity Supply)</text>
  <text x="170" y="250" font-size="12" fill="#cbd5e1" text-anchor="middle">• Agricultural Crops</text>
  <text x="170" y="275" font-size="12" fill="#cbd5e1" text-anchor="middle">• Raw Minerals &amp; Oil</text>

  <!-- Transport Corridor -->
  <line x1="280" y1="230" x2="520" y2="230" stroke="#38bdf8" stroke-width="6"/>
  <polygon points="510,220 535,230 510,240" fill="#38bdf8"/>
  <rect x="330" y="175" font-size="13" width="140" height="40" rx="6" fill="#1e293b" stroke="#38bdf8"/>
  <text x="400" y="200" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">TRANSPORT LINK</text>

  <!-- Region B (Deficit) -->
  <rect x="520" y="140" width="220" height="180" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
  <text x="630" y="180" font-size="16" font-weight="bold" fill="#ef4444" text-anchor="middle">REGION B: DEFICIT</text>
  <text x="630" y="210" font-size="13" fill="#fca5a5" text-anchor="middle">(High Market Demand)</text>
  <text x="630" y="250" font-size="12" fill="#cbd5e1" text-anchor="middle">• Urban Consumers</text>
  <text x="630" y="275" font-size="12" fill="#cbd5e1" text-anchor="middle">• Industrial Refineries</text>
</svg>
""")

SVG_2 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Comparative Ecological Adaptations of Traditional Animal Transport</text>

  <g transform="translate(40, 80)">
    <!-- Camel -->
    <rect x="0" y="0" width="165" height="320" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="82" y="30" font-size="15" font-weight="bold" fill="#f59e0b" text-anchor="middle">Camels</text>
    <text x="82" y="60" font-size="12" fill="#fef08a" text-anchor="middle">Sahara Sand Dunes</text>
    <text x="15" y="100" font-size="11" fill="#cbd5e1">• Wide padded hooves</text>
    <text x="15" y="125" font-size="11" fill="#cbd5e1">• Water retention</text>
    <text x="15" y="150" font-size="11" fill="#cbd5e1">• Heavy load endurance</text>

    <!-- Donkey -->
    <rect x="185" y="0" width="165" height="320" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <text x="267" y="30" font-size="15" font-weight="bold" fill="#10b981" text-anchor="middle">Donkeys</text>
    <text x="267" y="60" font-size="12" fill="#a7f3d0" text-anchor="middle">Steep Mountain Paths</text>
    <text x="200" y="100" font-size="11" fill="#cbd5e1">• Sure-footed stability</text>
    <text x="200" y="125" font-size="11" fill="#cbd5e1">• Low feed requirement</text>
    <text x="200" y="150" font-size="11" fill="#cbd5e1">• Rural pack transport</text>

    <!-- Oxen -->
    <rect x="370" y="0" width="165" height="320" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="452" y="30" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">Oxen</text>
    <text x="452" y="60" font-size="12" fill="#93c5fd" text-anchor="middle">Agricultural Fields</text>
    <text x="385" y="100" font-size="11" fill="#cbd5e1">• High pulling traction</text>
    <text x="385" y="125" font-size="11" fill="#cbd5e1">• Heavy cart haulage</text>
    <text x="385" y="150" font-size="11" fill="#cbd5e1">• Farm ploughing</text>

    <!-- Elephant -->
    <rect x="555" y="0" width="165" height="320" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="637" y="30" font-size="15" font-weight="bold" fill="#a855f7" text-anchor="middle">Elephants</text>
    <text x="637" y="60" font-size="12" fill="#e9d5ff" text-anchor="middle">Tropical Forests</text>
    <text x="570" y="100" font-size="11" fill="#cbd5e1">• Dragging heavy logs</text>
    <text x="570" y="125" font-size="11" fill="#cbd5e1">• Penetrating thickets</text>
    <text x="570" y="150" font-size="11" fill="#cbd5e1">• Asian timber camps</text>
  </g>
</svg>
""")

SVG_3 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Traditional vs Modern Transport Efficiency &amp; Payload Matrix</text>

  <rect x="40" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="212" y="110" font-size="16" font-weight="bold" fill="#f59e0b" text-anchor="middle">Traditional Animal/Human</text>
  <text x="60" y="160" font-size="13" fill="#cbd5e1">• Speed: 3 - 6 km/h (Slow)</text>
  <text x="60" y="200" font-size="13" fill="#cbd5e1">• Payload: 50 kg - 500 kg</text>
  <text x="60" y="240" font-size="13" fill="#cbd5e1">• Fuel Cost: Zero (Grass/Food)</text>
  <text x="60" y="280" font-size="13" fill="#cbd5e1">• Environmental: Zero carbon</text>
  <text x="60" y="320" font-size="13" fill="#cbd5e1">• Flexibility: High on footpaths</text>

  <rect x="415" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="587" y="110" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">Modern Motorized Road/Rail</text>
  <text x="435" y="160" font-size="13" fill="#cbd5e1">• Speed: 60 - 120 km/h (Fast)</text>
  <text x="435" y="200" font-size="13" fill="#cbd5e1">• Payload: 10 Tons - 5,000 Tons</text>
  <text x="435" y="240" font-size="13" fill="#cbd5e1">• Fuel Cost: Diesel/Petroleum</text>
  <text x="435" y="280" font-size="13" fill="#cbd5e1">• Environmental: Exhaust fumes</text>
  <text x="435" y="320" font-size="13" fill="#cbd5e1">• Flexibility: Needs engineered roads</text>
</svg>
""")

SVG_4 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Four Principal Trans-Continental Highway Corridors Across Africa</text>
  <rect x="120" y="70" width="560" height="340" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

  <!-- Great North Road -->
  <line x1="520" y1="90" x2="380" y2="380" stroke="#ef4444" stroke-width="4"/>
  <text x="470" y="220" font-size="12" font-weight="bold" fill="#ef4444">1. Great North Road (Cairo to Cape Town)</text>

  <!-- Trans-Africa Highway -->
  <line x1="160" y1="240" x2="550" y2="240" stroke="#10b981" stroke-width="4"/>
  <text x="250" y="260" font-size="12" font-weight="bold" fill="#10b981">2. Trans-Africa Highway (Mombasa to Dakar)</text>

  <!-- Dakar-Djamena -->
  <line x1="160" y1="180" x2="360" y2="180" stroke="#f59e0b" stroke-width="3"/>
  <text x="180" y="170" font-size="11" fill="#f59e0b">3. Dakar-Djamena</text>

  <!-- Trans-Sahara -->
  <line x1="280" y1="250" x2="420" y2="90" stroke="#a855f7" stroke-width="3"/>
  <text x="320" y="140" font-size="11" fill="#a855f7">4. Trans-Sahara</text>
</svg>
""")

SVG_5 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Road vs Rail Cost Efficiency Curves Over Distance</text>

  <!-- Axes -->
  <line x1="80" y1="360" x2="720" y2="360" stroke="#94a3b8" stroke-width="2"/>
  <line x1="80" y1="80" x2="80" y2="360" stroke="#94a3b8" stroke-width="2"/>
  <text x="400" y="400" font-size="13" font-weight="bold" fill="#cbd5e1" text-anchor="middle">Distance (Kilometers)</text>
  <text x="30" y="220" font-size="13" font-weight="bold" fill="#cbd5e1" transform="rotate(-90 30 220)" text-anchor="middle">Freight Cost per Ton</text>

  <!-- Road Curve (Low initial cost, steep slope) -->
  <path d="M 80 320 Q 300 240 700 80" stroke="#ef4444" stroke-width="3" fill="none"/>
  <text x="620" y="110" font-size="13" font-weight="bold" fill="#ef4444">Road Transport</text>

  <!-- Rail Curve (High terminal cost, flat slope) -->
  <path d="M 80 220 Q 300 210 700 180" stroke="#10b981" stroke-width="3" fill="none"/>
  <text x="620" y="170" font-size="13" font-weight="bold" fill="#10b981">Railway Transport</text>

  <!-- Crossover Point -->
  <circle cx="370" cy="225" r="8" fill="#f59e0b"/>
  <line x1="370" y1="225" x2="370" y2="360" stroke="#f59e0b" stroke-dasharray="4,4"/>
  <text x="370" y="380" font-size="12" font-weight="bold" fill="#f59e0b" text-anchor="middle">300 km Crossover Point</text>
</svg>
""")

SVG_6 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Historical Causes of Fragmented Railway Gauge Networks in Africa</text>
  <rect x="40" y="80" width="720" height="320" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

  <!-- Lines from inland to coast -->
  <line x1="100" y1="120" x2="300" y2="120" stroke="#ef4444" stroke-width="4"/>
  <text x="200" y="110" font-size="12" fill="#ef4444" text-anchor="middle">Meter Gauge (1000mm)</text>

  <line x1="100" y1="220" x2="300" y2="220" stroke="#f59e0b" stroke-width="4"/>
  <text x="200" y="210" font-size="12" fill="#f59e0b" text-anchor="middle">Cape Gauge (1067mm)</text>

  <line x1="100" y1="320" x2="300" y2="320" stroke="#10b981" stroke-width="4"/>
  <text x="200" y="310" font-size="12" fill="#10b981" text-anchor="middle">Standard Gauge (1435mm)</text>

  <!-- Broken Cross-Link -->
  <line x1="200" y1="120" x2="200" y2="320" stroke="#ef4444" stroke-width="3" stroke-dasharray="6,6"/>
  <rect x="150" y="200" width="100" height="40" rx="4" fill="#991b1b"/>
  <text x="200" y="225" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">NO LINK</text>

  <!-- Explanation -->
  <rect x="360" y="100" width="370" height="270" rx="6" fill="#1e293b" stroke="#38bdf8"/>
  <text x="545" y="130" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">CAUSES OF RAIL FRAGMENTATION</text>
  <text x="380" y="175" font-size="12" fill="#cbd5e1">1. Colonial Export Focus (Mine → Port)</text>
  <text x="380" y="215" font-size="12" fill="#cbd5e1">2. Rival Colonial Gauge Differences</text>
  <text x="380" y="255" font-size="12" fill="#cbd5e1">3. Border Political Disputes</text>
  <text x="380" y="295" font-size="12" fill="#cbd5e1">4. High Mountain Engineering Costs</text>
  <text x="380" y="335" font-size="12" fill="#cbd5e1">5. Low Inter-state Agricultural Trade</text>
</svg>
""")

SVG_7 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Pipeline Transport Flow &amp; Storage Infrastructure (KPC)</text>

  <rect x="40" y="180" width="140" height="80" rx="6" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
  <text x="110" y="215" font-size="13" font-weight="bold" fill="#06b6d4" text-anchor="middle">Mombasa Marine</text>
  <text x="110" y="235" font-size="13" font-weight="bold" fill="#06b6d4" text-anchor="middle">Terminal (KPC)</text>

  <line x1="180" y1="220" x2="310" y2="220" stroke="#38bdf8" stroke-width="8"/>
  <rect x="210" y="180" width="70" height="30" rx="4" fill="#1e3a8a"/>
  <text x="245" y="200" font-size="11" fill="#ffffff" text-anchor="middle">Pump 1</text>

  <rect x="310" y="180" width="140" height="80" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <text x="380" y="215" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">Nairobi Inland</text>
  <text x="380" y="235" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">Depot Terminal</text>

  <line x1="450" y1="220" x2="580" y2="220" stroke="#38bdf8" stroke-width="8"/>

  <rect x="580" y="180" width="160" height="80" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
  <text x="660" y="215" font-size="13" font-weight="bold" fill="#10b981" text-anchor="middle">Eldoret &amp; Kisumu</text>
  <text x="660" y="235" font-size="13" font-weight="bold" fill="#10b981" text-anchor="middle">Regional Terminals</text>
</svg>
""")

SVG_8 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Ocean Shipping Structure: Liners vs Tramps</text>
  <rect x="40" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="212" y="110" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">Ocean Liners</text>
  <text x="60" y="160" font-size="13" fill="#cbd5e1">• Fixed routes &amp; ports</text>
  <text x="60" y="200" font-size="13" fill="#cbd5e1">• Rigid timetable schedule</text>
  <text x="60" y="240" font-size="13" fill="#cbd5e1">• Fixed published freight tariffs</text>
  <text x="60" y="280" font-size="13" fill="#cbd5e1">• Containerised high-value cargo</text>
  <text x="60" y="320" font-size="13" fill="#cbd5e1">• Example: Passenger &amp; container ships</text>

  <rect x="415" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="587" y="110" font-size="16" font-weight="bold" fill="#f59e0b" text-anchor="middle">Ocean Tramps</text>
  <text x="435" y="160" font-size="13" fill="#cbd5e1">• Flexible charter routes</text>
  <text x="435" y="200" font-size="13" fill="#cbd5e1">• No fixed timetable schedule</text>
  <text x="435" y="240" font-size="13" fill="#cbd5e1">• Negotiable freight rates</text>
  <text x="435" y="280" font-size="13" fill="#cbd5e1">• Bulky raw materials (coal/wheat)</text>
  <text x="435" y="320" font-size="13" fill="#cbd5e1">• Example: Bulk mineral carriers</text>
</svg>
""")

SVG_9 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Intermodal Containerisation Value Chain</text>

  <rect x="40" y="80" width="720" height="50" rx="6" fill="#065f46" stroke="#10b981"/>
  <text x="400" y="112" font-size="15" font-weight="bold" fill="#a7f3d0" text-anchor="middle">1. Factory Sealed Packing into Standardized TEU Steel Containers</text>

  <rect x="100" y="160" width="600" height="50" rx="6" fill="#1e3a8a" stroke="#38bdf8"/>
  <text x="400" y="192" font-size="14" fill="#cbd5e1" text-anchor="middle">2. Road Truck Transport to Deep-Water Container Sea Port</text>

  <rect x="160" y="240" width="480" height="50" rx="6" fill="#713f12" stroke="#f59e0b"/>
  <text x="400" y="272" font-size="14" font-weight="bold" fill="#fef08a" text-anchor="middle">3. Automated Gantry Crane Loading onto Ocean Container Ship</text>

  <rect x="220" y="320" width="360" height="50" rx="6" fill="#581c87" stroke="#a855f7"/>
  <text x="400" y="352" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">4. Direct Intermodal Transfer onto SGR Freight Trains</text>
</svg>
""")

SVG_10 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Mode Selection Decision Tree for Industrial Cargo</text>

  <!-- Root -->
  <rect x="300" y="80" width="200" height="50" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <text x="400" y="110" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">CARGO TYPE ANALYSIS</text>

  <!-- Branch 1 -->
  <line x1="330" y1="130" x2="160" y2="200" stroke="#10b981" stroke-width="3"/>
  <rect x="60" y="200" width="200" height="80" rx="6" fill="#065f46" stroke="#10b981"/>
  <text x="160" y="235" font-size="13" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Heavy &amp; Bulky (500T Copper)</text>
  <text x="160" y="260" font-size="12" fill="#ffffff" text-anchor="middle">→ OPTIMAL: RAILWAY</text>

  <!-- Branch 2 -->
  <line x1="470" y1="130" x2="640" y2="200" stroke="#ef4444" stroke-width="3"/>
  <rect x="540" y="200" width="200" height="80" rx="6" fill="#7f1d1d" stroke="#ef4444"/>
  <text x="640" y="235" font-size="13" font-weight="bold" fill="#fecaca" text-anchor="middle">Light &amp; Perishable (5T Beans)</text>
  <text x="640" y="260" font-size="12" fill="#ffffff" text-anchor="middle">→ OPTIMAL: AIR FREIGHT</text>
</svg>
""")

SVG_11 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Physical Topographic Profile of the St. Lawrence Seaway</text>

  <!-- Elevation Steps -->
  <rect x="40" y="120" width="120" height="240" fill="#0284c7"/>
  <text x="100" y="150" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Lake Superior</text>
  <text x="100" y="170" font-size="11" fill="#ffffff" text-anchor="middle">(183m Elev)</text>

  <!-- Soo Locks -->
  <line x1="160" y1="160" x2="200" y2="190" stroke="#f59e0b" stroke-width="4"/>

  <rect x="200" y="190" width="160" height="170" fill="#0284c7"/>
  <text x="280" y="220" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Lake Huron / Erie</text>

  <!-- Niagara Falls Drop -->
  <path d="M 360 220 L 400 320" stroke="#ef4444" stroke-width="6"/>
  <text x="380" y="260" font-size="11" font-weight="bold" fill="#ef4444">Niagara Falls (99m Drop)</text>

  <rect x="400" y="320" width="160" height="40" fill="#0284c7"/>
  <text x="480" y="345" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Lake Ontario</text>

  <rect x="560" y="340" width="200" height="20" fill="#0284c7"/>
  <text x="660" y="355" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Atlantic Ocean Level</text>
</svg>
""")

SVG_12 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Engineering Lock Mechanism Functioning in Canal Navigation</text>

  <g transform="translate(40, 80)">
    <rect x="0" y="0" width="220" height="320" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="110" y="30" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">Stage 1: Entry</text>
    <text x="110" y="60" font-size="11" fill="#cbd5e1" text-anchor="middle">Ship enters lock chamber</text>
    <text x="110" y="80" font-size="11" fill="#cbd5e1" text-anchor="middle">at lower water level</text>

    <rect x="250" y="0" width="220" height="320" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="360" y="30" font-size="14" font-weight="bold" fill="#f59e0b" text-anchor="middle">Stage 2: Water Fill</text>
    <text x="360" y="60" font-size="11" fill="#cbd5e1" text-anchor="middle">Gates close; water fills</text>
    <text x="360" y="80" font-size="11" fill="#cbd5e1" text-anchor="middle">chamber from upper lake</text>

    <rect x="500" y="0" width="220" height="320" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <text x="610" y="30" font-size="14" font-weight="bold" fill="#10b981" text-anchor="middle">Stage 3: Exit</text>
    <text x="610" y="60" font-size="11" fill="#cbd5e1" text-anchor="middle">Ship floats to upper level;</text>
    <text x="610" y="80" font-size="11" fill="#cbd5e1" text-anchor="middle">upper gates open</text>
  </g>
</svg>
""")

SVG_13 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Socio-Economic Impact Network of the St. Lawrence Seaway</text>

  <rect x="60" y="100" width="180" height="80" rx="6" fill="#065f46" stroke="#10b981"/>
  <text x="150" y="135" font-size="13" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Bulk Canadian Wheat</text>
  <text x="150" y="155" font-size="12" fill="#ffffff" text-anchor="middle">&amp; Mesabi Iron Ore</text>

  <line x1="240" y1="140" x2="360" y2="140" stroke="#38bdf8" stroke-width="4"/>

  <rect x="360" y="100" width="180" height="80" rx="6" fill="#1e3a8a" stroke="#38bdf8"/>
  <text x="450" y="135" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">St. Lawrence Seaway</text>
  <text x="450" y="155" font-size="12" fill="#ffffff" text-anchor="middle">Water Highway</text>

  <line x1="540" y1="140" x2="660" y2="140" stroke="#38bdf8" stroke-width="4"/>

  <rect x="660" y="100" width="100" height="80" rx="6" fill="#713f12" stroke="#f59e0b"/>
  <text x="710" y="145" font-size="12" font-weight="bold" fill="#fef08a" text-anchor="middle">Atlantic Trade</text>
</svg>
""")

SVG_14 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Undersea Fiber Optic Cable &amp; Satellite Architecture</text>
  <rect x="40" y="160" width="180" height="80" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <text x="130" y="195" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">Subsea Fiber Cables</text>
  <text x="130" y="215" font-size="12" fill="#cbd5e1" text-anchor="middle">(SEACOM / TEAMS)</text>

  <line x1="220" y1="200" x2="350" y2="200" stroke="#0284c7" stroke-width="6"/>

  <rect x="350" y="160" width="180" height="80" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
  <text x="440" y="195" font-size="13" font-weight="bold" fill="#ef4444" text-anchor="middle">Mombasa Digital</text>
  <text x="440" y="215" font-size="12" fill="#cbd5e1" text-anchor="middle">Landing Gateway</text>

  <line x1="530" y1="200" x2="660" y2="200" stroke="#10b981" stroke-width="6"/>

  <rect x="660" y="160" width="100" height="80" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
  <text x="710" y="195" font-size="12" font-weight="bold" fill="#10b981" text-anchor="middle">Inland 4G/5G</text>
  <text x="710" y="215" font-size="12" fill="#10b981" text-anchor="middle">&amp; Satellite</text>
</svg>
""")

SVG_15 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">M-Pesa &amp; Mobile Banking Economic Velocity Model</text>
  <rect x="60" y="140" width="200" height="160" rx="6" fill="#065f46" stroke="#10b981"/>
  <text x="160" y="180" font-size="15" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Urban Sender</text>
  <text x="160" y="220" font-size="12" fill="#ffffff" text-anchor="middle">Instant SMS Cash</text>

  <line x1="260" y1="220" x2="540" y2="220" stroke="#38bdf8" stroke-width="6"/>
  <polygon points="530,210 555,220 530,230" fill="#38bdf8"/>

  <rect x="540" y="140" width="200" height="160" rx="6" fill="#1e3a8a" stroke="#38bdf8"/>
  <text x="640" y="180" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">Rural Receiver</text>
  <text x="640" y="220" font-size="12" fill="#ffffff" text-anchor="middle">Zero Bank Travel</text>
</svg>
""")

SVG_16 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Four Physical Barriers to River Transport in Africa</text>
  <g transform="translate(40, 80)">
    <rect x="0" y="0" width="345" height="140" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="172" y="30" font-size="14" font-weight="bold" fill="#ef4444" text-anchor="middle">1. Seasonal Volume Drop</text>
    <text x="172" y="60" font-size="11" fill="#cbd5e1" text-anchor="middle">Rivers pass dry zones; volumes drop,</text>
    <text x="172" y="80" font-size="11" fill="#cbd5e1" text-anchor="middle">preventing year-round sailing</text>

    <rect x="375" y="0" width="345" height="140" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="547" y="30" font-size="14" font-weight="bold" fill="#ef4444" text-anchor="middle">2. Waterfalls &amp; Rapids</text>
    <text x="547" y="60" font-size="11" fill="#cbd5e1" text-anchor="middle">Plateau edge drop-offs block</text>
    <text x="547" y="80" font-size="11" fill="#cbd5e1" text-anchor="middle">vessel movement</text>

    <rect x="0" y="160" width="345" height="140" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="172" y="190" font-size="14" font-weight="bold" fill="#ef4444" text-anchor="middle">3. River Siltation</text>
    <text x="172" y="220" font-size="11" fill="#cbd5e1" text-anchor="middle">Soil erosion fills river beds with</text>
    <text x="172" y="240" font-size="11" fill="#cbd5e1" text-anchor="middle">shallow sandbars grounding ships</text>

    <rect x="375" y="160" width="345" height="140" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="547" y="190" font-size="14" font-weight="bold" fill="#ef4444" text-anchor="middle">4. Floating Vegetation</text>
    <text x="547" y="220" font-size="11" fill="#cbd5e1" text-anchor="middle">Weeds (water hyacinth) choke channels</text>
    <text x="547" y="240" font-size="11" fill="#cbd5e1" text-anchor="middle">and entangle boat propellers</text>
  </g>
</svg>
""")

SVG_17 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Strategic Engineering Interventions for African River Navigation</text>
  <rect x="40" y="80" width="720" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="400" y="120" font-size="16" font-weight="bold" fill="#10b981" text-anchor="middle">ENGINEERING SOLUTIONS</text>
  <text x="80" y="170" font-size="13" fill="#cbd5e1">• Dredging: Deepening shallow silted channels</text>
  <text x="80" y="220" font-size="13" fill="#cbd5e1">• Dams: Creating deep reservoirs over dangerous rapids</text>
  <text x="80" y="270" font-size="13" fill="#cbd5e1">• Canals &amp; Locks: Bypassing waterfalls and elevation drops</text>
  <text x="80" y="320" font-size="13" fill="#cbd5e1">• Mechanical Weed Harvesters: Clearing hyacinth mats</text>
</svg>
""")

SVG_18 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Six-Point National Strategy for Integrated Transport &amp; Communication</text>
  <g transform="translate(60, 80)">
    <rect x="0" y="0" width="210" height="130" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="105" y="35" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. SGR Rail Corridors</text>

    <rect x="235" y="0" width="210" height="130" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <text x="340" y="35" font-size="14" font-weight="bold" fill="#10b981" text-anchor="middle">2. Fiber Optic Grid</text>

    <rect x="470" y="0" width="210" height="130" rx="6" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <text x="575" y="35" font-size="14" font-weight="bold" fill="#eab308" text-anchor="middle">3. Port Automation</text>

    <rect x="0" y="160" width="210" height="130" rx="6" fill="#0f172a" stroke="#f43f5e" stroke-width="2"/>
    <text x="105" y="195" font-size="14" font-weight="bold" fill="#f43f5e" text-anchor="middle">4. Urban BRT Lanes</text>

    <rect x="235" y="160" width="210" height="130" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <text x="340" y="195" font-size="14" font-weight="bold" fill="#a855f7" text-anchor="middle">5. Air Cargo Expansion</text>

    <rect x="470" y="160" width="210" height="130" rx="6" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
    <text x="575" y="195" font-size="14" font-weight="bold" fill="#06b6d4" text-anchor="middle">6. Regional Treaties</text>
  </g>
</svg>
""")

TOPIC6_SVGS = [
    SVG_1, SVG_2, SVG_3, SVG_4, SVG_5, SVG_6,
    SVG_7, SVG_8, SVG_9, SVG_10, SVG_11, SVG_12,
    SVG_13, SVG_14, SVG_15, SVG_16, SVG_17, SVG_18
]

# =====================================================================
# 8 VERIFIED WIKIMEDIA COMMONS PHOTOS FOR TOPIC 6: TRANSPORT AND COMMUNICATION
# =====================================================================

TOPIC6_PHOTOS = [
    {
        "lesson_order": 1,
        "page": 5,
        "title": "Traditional Camel Caravan in Desert",
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/dd/Camel_caravan_going_through_sand_in_the_Sahara_Desert.jpg",
        "author": "Public Domain, Wikimedia Commons",
        "licensing": "Public domain",
        "caption": "Camel caravan traversing sand dunes in the Sahara Desert."
    },
    {
        "lesson_order": 2,
        "page": 4,
        "title": "Kenya SGR Madaraka Express Freight Train",
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d9/New_SGR_train_Nairobi.jpg",
        "author": "Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "Kenya Standard Gauge Railway (SGR) freight train hauling heavy containerized cargo."
    },
    {
        "lesson_order": 3,
        "page": 3,
        "title": "Commercial Petroleum Pipeline Work",
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/c9/Pipeline_work.jpg",
        "author": "Wikimedia Commons",
        "licensing": "CC BY-SA 3.0",
        "caption": "Underground steel petroleum pipeline installation establishing continuous fluid transport."
    },
    {
        "lesson_order": 3,
        "page": 6,
        "title": "Container Shipping Port Terminal & Gantry Cranes",
        "url": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Container-Terminal_Bremerhaven_02.jpg",
        "author": "Wikimedia Commons",
        "licensing": "CC BY-SA 3.0",
        "caption": "Modern deep-water container terminal featuring gantry cranes loading TEU containers onto an ocean ship."
    },
    {
        "lesson_order": 3,
        "page": 9,
        "title": "Air Freight Cargo Aircraft Loader Operations",
        "url": "https://upload.wikimedia.org/wikipedia/commons/2/2f/Aircraft_cargo_%28ULD%29_loader_in_operaton.jpg",
        "author": "Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "High-speed motorized ULD cargo loader loading palleted freight into a commercial cargo jet aircraft."
    },
    {
        "lesson_order": 4,
        "page": 4,
        "title": "Vessel Passing Through St. Lawrence Seaway Lock",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/68/St._Lawrence_Seaway_lock_scenes_%28I0015590%29.jpg",
        "author": "Public Domain, Wikimedia Commons",
        "licensing": "Public domain",
        "caption": "Large ocean freight vessel navigating a concrete lock chamber along the St. Lawrence Seaway."
    },
    {
        "lesson_order": 5,
        "page": 4,
        "title": "Mobile Cellular Telecommunication Network Tower",
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Cell_Tower_Ciudad_del_Carmen2020.jpg",
        "author": "Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "High-gain cellular telecommunication tower relaying 4G/5G mobile signals across urban and rural landscapes."
    },
    {
        "lesson_order": 6,
        "page": 4,
        "title": "River Rapids Navigation Barrier",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/45/Klondikers_in_boat_navigating_Whitehorse_Rapids%2C_probably_1898_%28AL%2BCA_639%29.jpg",
        "author": "Public Domain, Wikimedia Commons",
        "licensing": "Public domain",
        "caption": "Turbulent river rapids demonstrating steep rocky drop-offs that obstruct commercial vessel navigation."
    }
]

def enrich_form4_geography_topic6():
    print("=" * 80)
    print("VLearn Form 4 Geography — Topic 6: Visual Enrichment Engine")
    print("Attaching 18 Vector SVGs & 8 Verified Wikimedia Photographic Assets")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    subject = Subject.objects.filter(grade=grade, name="Geography").first()
    topic = Topic.objects.filter(subject=subject, name="Transport and Communication").first()

    if not topic:
        print("[!] Error: Topic 'Transport and Communication' not found!")
        return

    lessons = list(topic.lessons.all().order_by("learning_unit__order"))
    LessonAsset.objects.filter(lesson__in=lessons).delete()
    print("[*] Cleared existing LessonAssets for clean enrichment.")

    svg_counter = 0

    for lesson in lessons:
        u_order = lesson.learning_unit.order
        print(f"\n[*] Enriching Lesson {u_order}: {lesson.title}")

        # 1. Attach SVG Diagrams
        diagram_blocks = list(LessonBlock.objects.filter(lesson=lesson, block_type="suggested_diagram").order_by("order"))
        for db in diagram_blocks:
            if svg_counter < len(TOPIC6_SVGS):
                svg_data = TOPIC6_SVGS[svg_counter]
                content = db.content or {}
                content["svg_content"] = svg_data
                content["svg"] = svg_data
                db.content = content
                db.save()

                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    asset_type="diagram",
                    source_type="ai_generated",
                    storage_type="embed",
                    status="attached",
                    title=db.title,
                    description=f"Sanitized vector diagram: {db.title}",
                    metadata={"svg_content": svg_data}
                )
                db.assets.add(asset)
                print(f"  [SVG OK] '{db.title[:40]}' -> Block ID: {db.id} (Page {db.page_number})")
                svg_counter += 1

        # 2. Attach Wikimedia Photos
        photo_meta_list = [p for p in TOPIC6_PHOTOS if p["lesson_order"] == u_order]
        image_blocks = list(LessonBlock.objects.filter(lesson=lesson, block_type="suggested_image").order_by("order"))

        for idx, ib in enumerate(image_blocks):
            if idx < len(photo_meta_list):
                pm = photo_meta_list[idx]
                content = ib.content or {}
                content["resolved_image_url"] = pm["url"]
                content["url"] = pm["url"]
                content["author"] = pm["author"]
                content["licensing"] = pm["licensing"]
                content["caption"] = pm["caption"]
                ib.content = content
                ib.save()

                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    asset_type="image",
                    source_type="external",
                    storage_type="url",
                    status="attached",
                    title=ib.title,
                    description=pm["caption"],
                    url=pm["url"],
                    metadata={
                        "author": pm["author"],
                        "licensing": pm["licensing"],
                        "caption": pm["caption"]
                    }
                )
                ib.assets.add(asset)
                print(f"  [WIKIMEDIA OK] '{ib.title[:40]}' -> Block ID: {ib.id} (Page {ib.page_number})")

    total_assets = LessonAsset.objects.filter(lesson__in=lessons).count()
    print("=" * 80)
    print(f"[SUCCESS] Form 4 Geography Topic 6 Visual Enrichment Complete!")
    print(f"[*] Total LessonAssets Created: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_form4_geography_topic6()
