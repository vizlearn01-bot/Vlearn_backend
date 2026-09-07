"""
VLearn Grade 10 Aviation — Topic 250: Flight Operations: Aviation Weather
Visual Enrichment Engine (Verified Photos, Responsive Vector SVGs & Video Assets)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Aviation (Subject ID: 44)
Topic: Flight Operations: Aviation Weather (Topic ID: 250, Order: 3)

Enriches:
  - 5 First-Card Photographic Visual Hooks (Verified Direct Wikimedia URLs)
  - 5 Custom Responsive Vector SVGs (viewBox="0 0 800 450", Dark Slate Theme, Sanitized XML)
  - 5 Verified Educational YouTube Videos (Meteorology, atmospheric strata, clouds, altimetry, weather hazards)
  - Persists LessonAsset models and binds them to corresponding LessonBlocks

Usage:
  ./venv/bin/python curriculum/enrich_grade10_aviation_topic250.py
"""

import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Topic, Lesson, LessonBlock, LessonAsset
)

def sanitize_svg(svg: str) -> str:
    """Ensures SVG is clean, responsive, and stripped of unneeded XML/DOCTYPE headers."""
    svg = re.sub(r'<\?xml.*?\?>', '', svg)
    svg = re.sub(r'<!DOCTYPE.*?>', '', svg)
    return svg.strip()

# =============================================================================
# 5 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 250
# =============================================================================

# SVG 1: Weather Elements & Aerodynamic Density Dynamics (Lesson 1, Page 4)
SVG_WEATHER_ELEMENTS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <!-- Outer Card -->
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Aviation Weather Elements &amp; Aerodynamic Air Density</text>

  <!-- Left Panel: Air Density Comparison -->
  <g transform="translate(35, 65)">
    <rect x="0" y="0" width="355" height="345" rx="10" fill="#0f172a" stroke="#3b82f6" stroke-width="1.5"/>
    <rect x="0" y="0" width="355" height="35" rx="10" fill="#1d4ed8"/>
    <text x="177" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">AIR DENSITY &amp; TEMPERATURE EFFECT</text>

    <!-- Cold Air Box -->
    <g transform="translate(15, 48)">
      <rect x="0" y="0" width="155" height="180" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
      <text x="77" y="20" font-size="11" font-weight="bold" fill="#10b981" text-anchor="middle">COLD AIR (Dense)</text>
      <!-- Densely packed dots -->
      <g fill="#38bdf8">
        <circle cx="25" cy="40" r="3.5"/><circle cx="50" cy="40" r="3.5"/><circle cx="75" cy="40" r="3.5"/><circle cx="100" cy="40" r="3.5"/><circle cx="125" cy="40" r="3.5"/>
        <circle cx="35" cy="58" r="3.5"/><circle cx="60" cy="58" r="3.5"/><circle cx="85" cy="58" r="3.5"/><circle cx="110" cy="58" r="3.5"/><circle cx="135" cy="58" r="3.5"/>
        <circle cx="25" cy="76" r="3.5"/><circle cx="50" cy="76" r="3.5"/><circle cx="75" cy="76" r="3.5"/><circle cx="100" cy="76" r="3.5"/><circle cx="125" cy="76" r="3.5"/>
        <circle cx="35" cy="94" r="3.5"/><circle cx="60" cy="94" r="3.5"/><circle cx="85" cy="94" r="3.5"/><circle cx="110" cy="94" r="3.5"/><circle cx="135" cy="94" r="3.5"/>
        <circle cx="25" cy="112" r="3.5"/><circle cx="50" cy="112" r="3.5"/><circle cx="75" cy="112" r="3.5"/><circle cx="100" cy="112" r="3.5"/><circle cx="125" cy="112" r="3.5"/>
      </g>
      <!-- Airfoil shape in cold air -->
      <path d="M 25 145 C 55 130 115 135 135 145 C 100 148 55 148 25 145 Z" fill="#64748b" stroke="#94a3b8" stroke-width="1.5"/>
      <text x="77" y="165" font-size="9.5" font-weight="bold" fill="#10b981" text-anchor="middle">&#8593; High Lift / High Thrust</text>
    </g>

    <!-- Hot Air Box -->
    <g transform="translate(185, 48)">
      <rect x="0" y="0" width="155" height="180" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
      <text x="77" y="20" font-size="11" font-weight="bold" fill="#ef4444" text-anchor="middle">HOT AIR (Thin)</text>
      <!-- Sparsely packed dots -->
      <g fill="#f87171">
        <circle cx="35" cy="45" r="3.5"/><circle cx="95" cy="42" r="3.5"/><circle cx="135" cy="50" r="3.5"/>
        <circle cx="65" cy="75" r="3.5"/><circle cx="115" cy="80" r="3.5"/>
        <circle cx="30" cy="105" r="3.5"/><circle cx="85" cy="110" r="3.5"/><circle cx="130" cy="105" r="3.5"/>
      </g>
      <!-- Airfoil shape in hot air -->
      <path d="M 25 145 C 55 130 115 135 135 145 C 100 148 55 148 25 145 Z" fill="#64748b" stroke="#94a3b8" stroke-width="1.5"/>
      <text x="77" y="165" font-size="9.5" font-weight="bold" fill="#ef4444" text-anchor="middle">&#8595; Low Lift / Low Thrust</text>
    </g>

    <!-- Operational Bullet Summary -->
    <g transform="translate(15, 240)">
      <rect x="0" y="0" width="325" height="92" rx="6" fill="#1e293b"/>
      <text x="12" y="22" font-size="10" fill="#f8fafc">&#8226; <tspan font-weight="bold" fill="#38bdf8">Cold Air:</tspan> Molecules packed close &#8594; Shorter takeoff run</text>
      <text x="12" y="44" font-size="10" fill="#f8fafc">&#8226; <tspan font-weight="bold" fill="#f87171">Hot Air:</tspan> Molecules expand &#8594; Longer runway needed</text>
      <text x="12" y="66" font-size="10" fill="#f8fafc">&#8226; <tspan font-weight="bold" fill="#f59e0b">High Altitude:</tspan> Elevation + Heat = High Density Altitude</text>
      <text x="12" y="84" font-size="9" fill="#94a3b8">  (e.g., Wilson Airport, Nairobi: 5,500 ft elevation)</text>
    </g>
  </g>

  <!-- Right Panel: Wind Vectors on Active Runway -->
  <g transform="translate(410, 65)">
    <rect x="0" y="0" width="355" height="345" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect x="0" y="0" width="355" height="35" rx="10" fill="#047857"/>
    <text x="177" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">RUNWAY WIND VECTOR DYNAMICS</text>

    <!-- Runway Illustration -->
    <g transform="translate(110, 48)">
      <!-- Asphalt Runway -->
      <rect x="35" y="0" width="65" height="210" rx="4" fill="#334155" stroke="#475569" stroke-width="1.5"/>
      <!-- Runway Centerline Dashes -->
      <line x1="67" y1="15" x2="67" y2="40" stroke="#ffffff" stroke-width="3" stroke-dasharray="8,6"/>
      <line x1="67" y1="50" x2="67" y2="155" stroke="#ffffff" stroke-width="3" stroke-dasharray="12,8"/>
      <text x="67" y="195" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">06</text>

      <!-- Aircraft on Runway -->
      <g transform="translate(67, 120)">
        <polygon points="0,-18 -15,12 0,6 15,12" fill="#38bdf8" stroke="#ffffff" stroke-width="1"/>
      </g>
    </g>

    <!-- Headwind Vector (Green, from Top) -->
    <g transform="translate(177, 45)">
      <line x1="0" y1="0" x2="0" y2="28" stroke="#10b981" stroke-width="3" marker-end="url(#arrow)"/>
      <polygon points="0,32 -5,22 5,22" fill="#10b981"/>
    </g>
    <text x="177" y="42" font-size="10.5" font-weight="bold" fill="#10b981" text-anchor="middle">HEADWIND (Desired)</text>
    <text x="177" y="54" font-size="9" fill="#94a3b8" text-anchor="middle">Extra lift / Shorter ground roll</text>

    <!-- Tailwind Vector (Red, from Bottom) -->
    <g transform="translate(177, 265)">
      <line x1="0" y1="20" x2="0" y2="-8" stroke="#ef4444" stroke-width="3"/>
      <polygon points="0,-12 -5,-2 5,-2" fill="#ef4444"/>
    </g>
    <text x="177" y="278" font-size="10.5" font-weight="bold" fill="#ef4444" text-anchor="middle">TAILWIND (Hazardous on Landing)</text>
    <text x="177" y="290" font-size="9" fill="#94a3b8" text-anchor="middle">High ground speed / Long rollout</text>

    <!-- Crosswind Vector (Amber, from Left) -->
    <g transform="translate(45, 155)">
      <line x1="0" y1="0" x2="55" y2="0" stroke="#f59e0b" stroke-width="3"/>
      <polygon points="60,0 50,-5 50,5" fill="#f59e0b"/>
      <text x="25" y="-8" font-size="10.5" font-weight="bold" fill="#f59e0b" text-anchor="middle">CROSSWIND</text>
      <text x="25" y="16" font-size="8.5" fill="#94a3b8" text-anchor="middle">Drift sideways</text>
    </g>

    <!-- Legend box -->
    <g transform="translate(15, 298)">
      <rect x="0" y="0" width="325" height="38" rx="6" fill="#1e293b"/>
      <text x="12" y="16" font-size="9.5" fill="#f8fafc"><tspan font-weight="bold" fill="#10b981">Headwind:</tspan> Increases airspeed without increasing ground roll.</text>
      <text x="12" y="30" font-size="9.5" fill="#f8fafc"><tspan font-weight="bold" fill="#f59e0b">Crosswind:</tspan> Max demonstrated limit ~15 kt for light aircraft.</text>
    </g>
  </g>
</svg>
""")

# SVG 2: Lower Atmosphere Thermal Structure & Flight Corridor (Lesson 2, Page 4)
SVG_ATMOSPHERE_LAYERS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <!-- Outer Card -->
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Lower Atmosphere Vertical Structure &amp; Aviation Flight Regimes</text>

  <!-- Left: Altitude vs Temperature Profile Chart -->
  <g transform="translate(45, 65)">
    <!-- Chart Background -->
    <rect x="50" y="20" width="320" height="310" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- Stratosphere Zone Fill (Top) -->
    <rect x="51" y="21" width="318" height="179" fill="#1e1b4b" opacity="0.6"/>
    <!-- Troposphere Zone Fill (Bottom) -->
    <rect x="51" y="210" width="318" height="119" fill="#0c4a6e" opacity="0.5"/>
    <!-- Tropopause Band -->
    <rect x="51" y="195" width="318" height="20" fill="#475569" opacity="0.8"/>
    <text x="210" y="209" font-size="9.5" font-weight="bold" fill="#f8fafc" text-anchor="middle">TROPOPAUSE BOUNDARY (11 km / ~36,000 ft, -56.5&#176;C)</text>

    <!-- Axes -->
    <line x1="50" y1="330" x2="370" y2="330" stroke="#94a3b8" stroke-width="1.5"/>
    <line x1="50" y1="20" x2="50" y2="330" stroke="#94a3b8" stroke-width="1.5"/>

    <!-- Y-Axis Ticks & Labels (Altitude km) -->
    <text x="42" y="333" font-size="10" fill="#94a3b8" text-anchor="end">0</text>
    <text x="42" y="215" font-size="10" fill="#38bdf8" text-anchor="end">11 km</text>
    <text x="42" y="125" font-size="10" fill="#94a3b8" text-anchor="end">30 km</text>
    <text x="42" y="25" font-size="10" fill="#c084fc" text-anchor="end">50 km</text>
    <text x="12" y="175" font-size="11" font-weight="bold" fill="#94a3b8" transform="rotate(-90 12 175)" text-anchor="middle">Altitude (km)</text>

    <!-- X-Axis Labels (Temperature °C) -->
    <text x="70" y="348" font-size="9.5" fill="#94a3b8">-60&#176;C</text>
    <text x="170" y="348" font-size="9.5" fill="#94a3b8">-30&#176;C</text>
    <text x="270" y="348" font-size="9.5" fill="#94a3b8">0&#176;C</text>
    <text x="340" y="348" font-size="9.5" fill="#94a3b8">+15&#176;C</text>
    <text x="210" y="362" font-size="10" font-weight="bold" fill="#94a3b8" text-anchor="middle">Temperature (&#176;C)</text>

    <!-- Red Temperature Profile Line -->
    <!-- Surface (+15°C, 0km) -> Tropopause (-56°C, 11km) -> Stratopause (0°C, 50km) -->
    <path d="M 345 330 L 80 205 L 80 195 L 270 25" fill="none" stroke="#ef4444" stroke-width="3"/>
    <circle cx="345" cy="330" r="4" fill="#ef4444"/>
    <circle cx="80" cy="205" r="4" fill="#ef4444"/>
    <circle cx="270" cy="25" r="4" fill="#ef4444"/>

    <!-- Lapse Rate Label in Troposphere -->
    <path d="M 230 280 L 175 250" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
    <text x="240" y="285" font-size="9.5" font-weight="bold" fill="#38bdf8">Lapse Rate: -2&#176;C / 1,000 ft</text>

    <!-- Ozone Warming Label in Stratosphere -->
    <path d="M 140 100 L 195 115" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3,3"/>
    <text x="120" y="95" font-size="9.5" font-weight="bold" fill="#f59e0b">Ozone (O&#8323;) UV Heating</text>
    <text x="120" y="108" font-size="8.5" fill="#94a3b8">Temperature increases</text>
  </g>

  <!-- Right: Operational Aviation Comparison -->
  <g transform="translate(440, 65)">
    <!-- Troposphere Card -->
    <rect x="0" y="180" width="315" height="150" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
    <rect x="0" y="180" width="315" height="28" rx="8" fill="#0369a1"/>
    <text x="157" y="199" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">TROPOSPHERE (The Weather Realm)</text>
    <g transform="translate(15, 218)">
      <circle cx="5" cy="5" r="4" fill="#38bdf8"/>
      <text x="18" y="9" font-size="10" fill="#f8fafc">Contains 99% of atmospheric water vapor</text>
      <circle cx="5" cy="27" r="4" fill="#38bdf8"/>
      <text x="18" y="31" font-size="10" fill="#f8fafc">Site of all clouds, rain, turbulence &amp; icing</text>
      <circle cx="5" cy="49" r="4" fill="#38bdf8"/>
      <text x="18" y="53" font-size="10" fill="#f8fafc">Standard lapse rate: 2&#176;C loss per 1,000 ft</text>
      <circle cx="5" cy="71" r="4" fill="#38bdf8"/>
      <text x="18" y="75" font-size="10" fill="#f8fafc">Light propeller aircraft cruise altitude</text>
      <circle cx="5" cy="93" r="4" fill="#38bdf8"/>
      <text x="18" y="97" font-size="10" fill="#f8fafc">Ceiling: 8 km (poles) to 18 km (equator)</text>
    </g>

    <!-- Stratosphere Card -->
    <rect x="0" y="0" width="315" height="165" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="0" y="0" width="315" height="28" rx="8" fill="#7e22ce"/>
    <text x="157" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">STRATOSPHERE (Commercial Jet Realm)</text>
    <g transform="translate(15, 38)">
      <!-- Commercial Jet Graphic -->
      <g transform="translate(230, 15)">
        <path d="M 0 0 L 25 -5 L 30 0 L 25 3 L 8 2 L -8 18 L -14 18 L -6 2 L -20 1 L -25 8 L -28 8 L -26 0 L -28 -8 L -25 -8 L -20 -1 Z" fill="#38bdf8"/>
        <text x="0" y="32" font-size="8" fill="#38bdf8" text-anchor="middle">FL390 Jet</text>
      </g>
      <circle cx="5" cy="5" r="4" fill="#c084fc"/>
      <text x="18" y="9" font-size="10" fill="#f8fafc">Extremely dry with zero convective storms</text>
      <circle cx="5" cy="27" r="4" fill="#c084fc"/>
      <text x="18" y="31" font-size="10" fill="#f8fafc">Smooth laminar air: zero weather turbulence</text>
      <circle cx="5" cy="49" r="4" fill="#c084fc"/>
      <text x="18" y="53" font-size="10" fill="#f8fafc">Thin air drastically cuts aircraft aerodynamic drag</text>
      <circle cx="5" cy="71" r="4" fill="#c084fc"/>
      <text x="18" y="75" font-size="10" fill="#f8fafc">Contains protective Ozone Layer (O&#8323;)</text>
      <circle cx="5" cy="93" r="4" fill="#c084fc"/>
      <text x="18" y="97" font-size="10" fill="#f8fafc">Max fuel efficiency for commercial airliners</text>
      <circle cx="5" cy="115" r="4" fill="#c084fc"/>
      <text x="18" y="119" font-size="9" fill="#94a3b8">Requires cabin pressurization (human physiology)</text>
    </g>
  </g>
</svg>
""")

# SVG 3: Cloud Classification Matrix & Severe Thunderstorm Anatomy (Lesson 3, Page 4)
SVG_CLOUD_MATRIX = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <!-- Outer Card -->
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Cloud Altitude Classification &amp; Thunderstorm (CB) Hazard Anatomy</text>

  <!-- Left Side: Altitude Tiers Diagram -->
  <g transform="translate(35, 65)">
    <!-- Altitude Backdrop -->
    <rect x="45" y="0" width="370" height="345" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- Y-Axis Altitude scale -->
    <line x1="45" y1="0" x2="45" y2="345" stroke="#64748b" stroke-width="1.5"/>
    <text x="38" y="15" font-size="9" fill="#94a3b8" text-anchor="end">40,000 ft</text>
    <text x="38" y="95" font-size="9" fill="#38bdf8" text-anchor="end">20,000 ft</text>
    <text x="38" y="210" font-size="9" fill="#f59e0b" text-anchor="end">6,500 ft</text>
    <text x="38" y="340" font-size="9" fill="#10b981" text-anchor="end">Surface</text>

    <!-- High Level Band (Cirrus) -->
    <rect x="46" y="0" width="368" height="95" fill="#1e1b4b" opacity="0.4"/>
    <line x1="45" y1="95" x2="415" y2="95" stroke="#38bdf8" stroke-width="1" stroke-dasharray="4,4"/>
    <!-- Cirrus wisps -->
    <path d="M 70 35 Q 120 20 180 32 T 260 25" fill="none" stroke="#e2e8f0" stroke-width="2" stroke-linecap="round"/>
    <path d="M 120 55 Q 180 40 240 50 T 320 42" fill="none" stroke="#e2e8f0" stroke-width="2" stroke-linecap="round"/>
    <text x="330" y="35" font-size="11" font-weight="bold" fill="#38bdf8">CIRRUS (Ci)</text>
    <text x="330" y="50" font-size="9" fill="#cbd5e1">100% Ice crystals</text>
    <text x="330" y="63" font-size="8.5" fill="#94a3b8">Approaching fronts</text>

    <!-- Mid Level Band (Altocumulus) -->
    <rect x="46" y="95" width="368" height="115" fill="#0f2a4a" opacity="0.4"/>
    <line x1="45" y1="210" x2="415" y2="210" stroke="#f59e0b" stroke-width="1" stroke-dasharray="4,4"/>
    <!-- Altocumulus patches -->
    <ellipse cx="90" cy="145" rx="18" ry="10" fill="#94a3b8" opacity="0.8"/>
    <ellipse cx="125" cy="142" rx="20" ry="11" fill="#cbd5e1" opacity="0.8"/>
    <ellipse cx="160" cy="146" rx="16" ry="9" fill="#94a3b8" opacity="0.8"/>
    <ellipse cx="195" cy="143" rx="19" ry="10" fill="#cbd5e1" opacity="0.8"/>
    <text x="330" y="135" font-size="11" font-weight="bold" fill="#f59e0b">ALTOCUMULUS (Ac)</text>
    <text x="330" y="150" font-size="9" fill="#cbd5e1">Mixed ice &amp; water</text>
    <text x="330" y="163" font-size="8.5" fill="#ef4444">&#9888; Airframe Icing Risk</text>

    <!-- Low Level Band (Stratus & Cumulus) -->
    <rect x="46" y="210" width="368" height="135" fill="#0c4a6e" opacity="0.3"/>
    <!-- Stratus sheet -->
    <rect x="60" y="235" width="180" height="22" rx="4" fill="#64748b" opacity="0.75"/>
    <text x="250" y="245" font-size="10.5" font-weight="bold" fill="#94a3b8">STRATUS (St)</text>
    <text x="250" y="258" font-size="8.5" fill="#cbd5e1">Low ceiling / Fog / Zero bumps</text>

    <!-- Cumulus puffy cloud -->
    <path d="M 70 315 C 65 305 75 295 90 295 C 95 285 110 282 120 290 C 130 280 150 285 155 295 C 165 295 175 305 170 315 Z" fill="#e2e8f0"/>
    <line x1="68" y1="315" x2="172" y2="315" stroke="#94a3b8" stroke-width="2"/>
    <text x="250" y="305" font-size="10.5" font-weight="bold" fill="#10b981">CUMULUS (Cu)</text>
    <text x="250" y="318" font-size="8.5" fill="#cbd5e1">Puffy / Flat base / Thermal bumps</text>
  </g>

  <!-- Right Side: Cumulonimbus (CB) Severe Storm Anatomy -->
  <g transform="translate(460, 65)">
    <rect x="0" y="0" width="305" height="345" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="305" height="32" rx="8" fill="#b91c1c"/>
    <text x="152" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">&#9888; CUMULONIMBUS (The Storm Giant)</text>

    <!-- Towering CB Cloud Silhouette -->
    <!-- Massive Anvil Top at 38,000 ft, narrow trunk, rain core -->
    <g transform="translate(15, 42)">
      <!-- Anvil Flat Top -->
      <path d="M 15 25 Q 135 15 255 20 C 275 22 270 35 245 40 C 205 45 185 55 175 80 L 170 170 C 185 175 195 195 185 205 L 85 205 C 75 195 85 175 100 170 L 95 80 C 85 55 65 45 25 40 C 5 35 0 25 15 25 Z" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
      <text x="135" y="35" font-size="11" font-weight="bold" fill="#f8fafc" text-anchor="middle">ANVIL DOME (~40,000 ft)</text>

      <!-- Updraft Vector (Red Up) -->
      <line x1="120" y1="180" x2="120" y2="85" stroke="#ef4444" stroke-width="3"/>
      <polygon points="120,78 114,90 126,90" fill="#ef4444"/>
      <text x="82" y="130" font-size="9" font-weight="bold" fill="#ef4444">Updraft &gt; 50 kt</text>

      <!-- Downdraft / Rain Shaft (Blue Down) -->
      <line x1="155" y1="95" x2="155" y2="185" stroke="#38bdf8" stroke-width="3"/>
      <polygon points="155,192 149,180 161,180" fill="#38bdf8"/>
      <text x="188" y="135" font-size="9" font-weight="bold" fill="#38bdf8">Microburst</text>

      <!-- Rain / Hail Striations -->
      <g stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3">
        <line x1="105" y1="210" x2="95" y2="238"/>
        <line x1="125" y1="210" x2="115" y2="238"/>
        <line x1="145" y1="210" x2="135" y2="238"/>
        <line x1="165" y1="210" x2="155" y2="238"/>
      </g>

      <!-- Lightning Bolt -->
      <polygon points="140,110 130,135 138,135 128,165 146,138 138,138" fill="#facc15" stroke="#eab308" stroke-width="0.5"/>

      <!-- Ground Line -->
      <line x1="10" y1="240" x2="265" y2="240" stroke="#64748b" stroke-width="2"/>
    </g>

    <!-- Hazard Warning Banner -->
    <g transform="translate(12, 290)">
      <rect x="0" y="0" width="280" height="45" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
      <text x="140" y="18" font-size="10.5" font-weight="bold" fill="#ef4444" text-anchor="middle">MANDATORY RULE: 20 NM CLEARANCE</text>
      <text x="140" y="34" font-size="9" fill="#f8fafc" text-anchor="middle">Never penetrate, fly under, or skirt near a CB!</text>
    </g>
  </g>
</svg>
""")

# SVG 4: Aerodrome Meteorological Sensors & Windsock Speed Analysis (Lesson 4, Page 4)
SVG_INSTRUMENT_SUITE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <!-- Outer Card -->
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Aerodrome Meteorological Sensors &amp; Windsock Speed Analysis</text>

  <!-- Left: Airport Sensor Kit (4-Box Grid) -->
  <g transform="translate(35, 65)">
    <!-- Box 1: Anemometer & Vane -->
    <rect x="0" y="0" width="170" height="160" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="26" rx="8" fill="#0284c7"/>
    <text x="85" y="18" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">ANEMOMETER &amp; VANE</text>
    <!-- Vector Graphic: 3 Cups and Vane -->
    <g transform="translate(85, 80)">
      <line x1="0" y1="25" x2="0" y2="-10" stroke="#94a3b8" stroke-width="2.5"/>
      <circle cx="0" cy="-10" r="4" fill="#f8fafc"/>
      <line x1="-25" y1="-10" x2="25" y2="-10" stroke="#94a3b8" stroke-width="2"/>
      <circle cx="-25" cy="-10" r="7" fill="#38bdf8"/>
      <circle cx="25" cy="-10" r="7" fill="#38bdf8"/>
      <!-- Fin -->
      <polygon points="0,-10 18,-18 15,-10" fill="#f59e0b"/>
    </g>
    <text x="85" y="132" font-size="9.5" font-weight="bold" fill="#f8fafc" text-anchor="middle">Measures: Wind Speed &amp; Heading</text>
    <text x="85" y="146" font-size="8.5" fill="#94a3b8" text-anchor="middle">Unit: Knots / Magnetic Degrees</text>

    <!-- Box 2: Barometer & Altimeter Link -->
    <rect x="185" y="0" width="170" height="160" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect x="185" y="0" width="170" height="26" rx="8" fill="#047857"/>
    <text x="270" y="18" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">BAROMETER &amp; ALTIMETER</text>
    <!-- Vector Graphic: Aneroid Capsule & Gauge -->
    <g transform="translate(270, 80)">
      <circle cx="0" cy="0" r="26" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
      <line x1="0" y1="0" x2="12" y2="-15" stroke="#ef4444" stroke-width="2"/>
      <circle cx="0" cy="0" r="3" fill="#ffffff"/>
      <text x="0" y="16" font-size="8" font-weight="bold" fill="#10b981" text-anchor="middle">QNH 1013</text>
    </g>
    <text x="270" y="132" font-size="9.5" font-weight="bold" fill="#f8fafc" text-anchor="middle">Calibrates Cockpit Altimeter</text>
    <text x="270" y="146" font-size="8.5" fill="#94a3b8" text-anchor="middle">Unit: hPa / Inches of Hg</text>

    <!-- Box 3: Stevenson Screen (Thermometer & Hygrometer) -->
    <rect x="0" y="175" width="355" height="165" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="175" width="355" height="26" rx="8" fill="#b45309"/>
    <text x="177" y="193" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">STEVENSON SCREEN: THERMOMETER &amp; HYGROMETER</text>
    <!-- Graphic representation -->
    <g transform="translate(25, 215)">
      <!-- Screen Box -->
      <rect x="0" y="0" width="70" height="55" rx="4" fill="#334155" stroke="#f8fafc" stroke-width="1.5"/>
      <line x1="0" y1="12" x2="70" y2="12" stroke="#64748b"/>
      <line x1="0" y1="24" x2="70" y2="24" stroke="#64748b"/>
      <line x1="0" y1="36" x2="70" y2="36" stroke="#64748b"/>
      <!-- Mast Legs -->
      <line x1="15" y1="55" x2="10" y2="95" stroke="#94a3b8" stroke-width="2"/>
      <line x1="55" y1="55" x2="60" y2="95" stroke="#94a3b8" stroke-width="2"/>
    </g>
    <g transform="translate(110, 215)">
      <text x="0" y="15" font-size="10" font-weight="bold" fill="#f59e0b">&#8226; Airfield Thermometer (&#176;C):</text>
      <text x="12" y="30" font-size="9" fill="#f8fafc">Calculates density altitude and takeoff roll distance.</text>
      <text x="0" y="52" font-size="10" font-weight="bold" fill="#38bdf8">&#8226; Hygrometer / Dewpoint Sensor (%):</text>
      <text x="12" y="67" font-size="9" fill="#f8fafc">Determines relative humidity, carb icing, and fog potential.</text>
      <text x="0" y="88" font-size="10" font-weight="bold" fill="#10b981">&#8226; Rain Gauge (mm):</text>
      <text x="12" y="103" font-size="9" fill="#f8fafc">Monitors runway standing water depth to avoid aquaplaning.</text>
    </g>
  </g>

  <!-- Right: 3-Stage Runway Windsock Speed Chart -->
  <g transform="translate(420, 65)">
    <rect x="0" y="0" width="345" height="340" rx="8" fill="#0f172a" stroke="#f97316" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="32" rx="8" fill="#c2410c"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">RUNWAY WINDSOCK SPEED DECODER</text>

    <!-- Stage 1: Flaccid / Hanging (< 3 kt) -->
    <g transform="translate(25, 45)">
      <line x1="15" y1="10" x2="15" y2="65" stroke="#94a3b8" stroke-width="3"/>
      <!-- Drooping sock -->
      <path d="M 15 15 C 25 15 30 25 30 35 C 30 55 22 65 20 70 L 16 70 C 18 60 22 45 22 35 C 22 25 18 20 15 20 Z" fill="#ea580c" stroke="#ffffff" stroke-width="1"/>
      <text x="80" y="32" font-size="11" font-weight="bold" fill="#10b981">STAGE 1: LIMP / HANGING</text>
      <text x="80" y="48" font-size="10" fill="#f8fafc">Speed: &lt; 3 Knots (Calm air)</text>
      <text x="80" y="62" font-size="9" fill="#94a3b8">Negligible crosswind impact on runway</text>
    </g>

    <!-- Stage 2: Half-Inflated / Angled (~ 7 to 10 kt) -->
    <g transform="translate(25, 135)">
      <line x1="15" y1="10" x2="15" y2="65" stroke="#94a3b8" stroke-width="3"/>
      <!-- 45-deg angled sock -->
      <path d="M 15 15 L 45 35 C 55 42 58 48 55 52 L 48 56 C 42 48 38 42 32 35 L 15 22 Z" fill="#ea580c" stroke="#ffffff" stroke-width="1"/>
      <text x="80" y="32" font-size="11" font-weight="bold" fill="#f59e0b">STAGE 2: HALF-INFLATED (45&#176;)</text>
      <text x="80" y="48" font-size="10" fill="#f8fafc">Speed: ~ 7 to 10 Knots (Breeze)</text>
      <text x="80" y="62" font-size="9" fill="#94a3b8">Active rudder corrections needed</text>
    </g>

    <!-- Stage 3: Fully Horizontal / Stiff (> 15 kt) -->
    <g transform="translate(25, 225)">
      <line x1="15" y1="10" x2="15" y2="65" stroke="#94a3b8" stroke-width="3"/>
      <!-- Fully horizontal sock -->
      <polygon points="15,15 70,22 70,30 15,37" fill="#ea580c" stroke="#ffffff" stroke-width="1"/>
      <line x1="33" y1="17" x2="33" y2="35" stroke="#ffffff" stroke-width="3"/>
      <line x1="51" y1="19" x2="51" y2="33" stroke="#ffffff" stroke-width="3"/>
      <text x="80" y="30" font-size="11" font-weight="bold" fill="#ef4444">STAGE 3: HORIZONTAL &amp; STIFF</text>
      <text x="80" y="46" font-size="10" fill="#f8fafc">Speed: &#8805; 15 Knots (Brisk wind)</text>
      <text x="80" y="60" font-size="9" fill="#94a3b8">Significant crosswind drift hazard</text>
    </g>

    <!-- Footer Note -->
    <rect x="15" y="300" width="315" height="30" rx="4" fill="#1e293b"/>
    <text x="172" y="319" font-size="9.5" fill="#f8fafc" text-anchor="middle"><tspan font-weight="bold" fill="#f97316">Orientation:</tspan> Wind blows IN wide mouth, exits tail (downwind).</text>
  </g>
</svg>
""")

# SVG 5: Flight Weather Safety Ecosystem & Aquaplaning Dynamics (Lesson 5, Page 4)
SVG_SAFETY_ECOSYSTEM = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <!-- Outer Card -->
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Aviation Weather Safety Chain &amp; Runway Aquaplaning Physics</text>

  <!-- Left: Dynamic Runway Aquaplaning Diagram -->
  <g transform="translate(35, 65)">
    <rect x="0" y="0" width="350" height="345" rx="8" fill="#0f172a" stroke="#3b82f6" stroke-width="1.5"/>
    <rect x="0" y="0" width="350" height="30" rx="8" fill="#1d4ed8"/>
    <text x="175" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">RUNWAY AQUAPLANING (HYDROPLANING)</text>

    <!-- Case A: Normal Dry Braking -->
    <g transform="translate(20, 45)">
      <rect x="0" y="0" width="145" height="170" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
      <text x="72" y="18" font-size="10.5" font-weight="bold" fill="#10b981" text-anchor="middle">DRY RUNWAY</text>
      <!-- Tire on Asphalt -->
      <ellipse cx="72" cy="75" rx="22" ry="38" fill="#334155" stroke="#f8fafc" stroke-width="2"/>
      <ellipse cx="72" cy="75" rx="12" ry="22" fill="#64748b"/>
      <!-- Runway Asphalt line -->
      <line x1="10" y1="113" x2="135" y2="113" stroke="#94a3b8" stroke-width="3"/>
      <rect x="45" y="110" width="55" height="6" fill="#10b981"/>
      <text x="72" y="135" font-size="9" font-weight="bold" fill="#10b981" text-anchor="middle">Mechanical Grip</text>
      <text x="72" y="152" font-size="8.5" fill="#f8fafc" text-anchor="middle">&#10004; 100% Braking Traction</text>
    </g>

    <!-- Case B: Dynamic Aquaplaning on Water Film -->
    <g transform="translate(185, 45)">
      <rect x="0" y="0" width="145" height="170" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
      <text x="72" y="18" font-size="10.5" font-weight="bold" fill="#ef4444" text-anchor="middle">FLOODED RUNWAY</text>
      <!-- Tire Riding on Water Wedge -->
      <ellipse cx="72" cy="70" rx="22" ry="38" fill="#334155" stroke="#f8fafc" stroke-width="2"/>
      <ellipse cx="72" cy="70" rx="12" ry="22" fill="#64748b"/>
      <!-- Water Layer -->
      <rect x="10" y="105" width="125" height="10" fill="#38bdf8" opacity="0.8"/>
      <!-- Water Wedge under tire -->
      <polygon points="45,108 85,102 105,108" fill="#60a5fa"/>
      <!-- Runway line below water -->
      <line x1="10" y1="115" x2="135" y2="115" stroke="#94a3b8" stroke-width="3"/>
      <text x="72" y="135" font-size="9" font-weight="bold" fill="#ef4444" text-anchor="middle">Riding on Water Film</text>
      <text x="72" y="152" font-size="8.5" fill="#fca5a5" text-anchor="middle">&#10008; ZERO Braking Traction</text>
    </g>

    <!-- Aquaplaning Formula & Safety Rules -->
    <g transform="translate(20, 230)">
      <rect x="0" y="0" width="310" height="98" rx="6" fill="#1e293b"/>
      <text x="12" y="20" font-size="10" font-weight="bold" fill="#38bdf8">&#8226; Hydroplaning Speed Formula: <tspan fill="#f8fafc">Vp &#8776; 9 &#215; &#8730;(Tire PSI)</tspan></text>
      <text x="12" y="40" font-size="9.5" fill="#f8fafc">&#8226; High forward speed forces water wedge beneath tire.</text>
      <text x="12" y="58" font-size="9.5" fill="#f8fafc">&#8226; Wheel ceases spinning; wheel brakes fail completely.</text>
      <text x="12" y="78" font-size="9.5" fill="#10b981">&#10004; Countermeasures: <tspan fill="#94a3b8">Grooved runways, spoilers, thrust reversers.</tspan></text>
    </g>
  </g>

  <!-- Right: 4-Stage Aviation Weather Safety Chain -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="350" height="345" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect x="0" y="0" width="350" height="30" rx="8" fill="#047857"/>
    <text x="175" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">FOUR-PILLAR WEATHER SAFETY ECOSYSTEM</text>

    <!-- Pillar 1: Meteorologist -->
    <g transform="translate(20, 42)">
      <rect x="0" y="0" width="310" height="58" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <circle cx="25" cy="29" r="14" fill="#0284c7"/>
      <text x="25" y="34" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1</text>
      <text x="50" y="22" font-size="10.5" font-weight="bold" fill="#38bdf8">METEOROLOGIST (The Forecaster)</text>
      <text x="50" y="38" font-size="9" fill="#f8fafc">Collects radar/satellite data; issues METARs, TAFs &amp; SIGMETs.</text>
      <text x="50" y="50" font-size="8.5" fill="#94a3b8">Predicts storm tracks, microbursts &amp; freezing levels.</text>
    </g>

    <!-- Pillar 2: Flight Dispatcher -->
    <g transform="translate(20, 112)">
      <rect x="0" y="0" width="310" height="58" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
      <circle cx="25" cy="29" r="14" fill="#b45309"/>
      <text x="25" y="34" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2</text>
      <text x="50" y="22" font-size="10.5" font-weight="bold" fill="#f59e0b">FLIGHT DISPATCHER (The Planner)</text>
      <text x="50" y="38" font-size="9" fill="#f8fafc">Designs flight plan detour routes around active storms.</text>
      <text x="50" y="50" font-size="8.5" fill="#94a3b8">Calculates required contingency fuel &amp; alternate aerodromes.</text>
    </g>

    <!-- Pillar 3: Air Traffic Controller (ATC) -->
    <g transform="translate(20, 182)">
      <rect x="0" y="0" width="310" height="58" rx="6" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
      <circle cx="25" cy="29" r="14" fill="#7e22ce"/>
      <text x="25" y="34" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3</text>
      <text x="50" y="22" font-size="10.5" font-weight="bold" fill="#c084fc">AIR TRAFFIC CONTROLLER (The Director)</text>
      <text x="50" y="38" font-size="9" fill="#f8fafc">Broadcasts live wind shear alerts &amp; runway water depths.</text>
      <text x="50" y="50" font-size="8.5" fill="#94a3b8">Vectors arriving aircraft away from convective cloud cells.</text>
    </g>

    <!-- Pillar 4: Pilot in Command -->
    <g transform="translate(20, 252)">
      <rect x="0" y="0" width="310" height="78" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
      <circle cx="25" cy="39" r="14" fill="#047857"/>
      <text x="25" y="44" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">4</text>
      <text x="50" y="22" font-size="10.5" font-weight="bold" fill="#10b981">PILOT IN COMMAND (The Decision-Maker)</text>
      <text x="50" y="38" font-size="9" fill="#f8fafc">Final pre-flight briefing &amp; onboard weather radar scan.</text>
      <text x="50" y="52" font-size="8.5" fill="#f8fafc">Absolute authority to execute a <tspan font-weight="bold" fill="#facc15">GO-AROUND</tspan> or divert.</text>
      <text x="50" y="66" font-size="8" fill="#94a3b8">Never compromise safety to maintain schedule.</text>
    </g>
  </g>
</svg>
""")

# =============================================================================
# ASSET DICTIONARIES
# =============================================================================

WIKIMEDIA_PHOTOS = {
    0: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b1/Air_Nelson_Q300_crosswind_landing_at_Tauranga_Airport.jpg",
        "title": "Dash 8 Q300 Turboprop Performing a Crosswind Landing",
        "caption": "A commercial turboprop aircraft executing a crab-angle approach in gusty crosswinds, demonstrating the critical influence of atmospheric wind vectors on runway alignment and flight control.",
        "author": "Wikimedia Commons",
        "license": "Creative Commons Attribution-Share Alike"
    },
    1: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/53/Fiery_South_Atlantic_Sunset.jpg",
        "title": "Stratosphere and Troposphere Layers Viewed from Orbit",
        "caption": "The distinct illuminated stratifications of the Earth's lower atmosphere captured from the International Space Station, showing the dense, cloud-filled troposphere beneath the clear, stable stratosphere.",
        "author": "NASA / Wikimedia Commons",
        "license": "Public Domain"
    },
    2: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d7/Anvil_of_a_Thunderstorm_Cloud.jpg",
        "title": "Massive Cumulonimbus Thunderstorm Cloud with Anvil Top",
        "caption": "A fully developed cumulonimbus incus storm cloud towering through the troposphere, exhibiting the iconic flattened anvil dome produced by violent vertical thermal updrafts.",
        "author": "Wikimedia Commons",
        "license": "Creative Commons Attribution-Share Alike"
    },
    3: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/2/2a/Marshland_Airport_windsock_and_runway_-_geograph.org.uk_-_656276.jpg",
        "title": "Calibrated Airfield Windsock Station Beside an Active Runway",
        "caption": "An illuminated international orange and white windsock providing instantaneous visual verification of wind direction and surface gust velocity adjacent to the touchdown zone.",
        "author": "Geograph.org.uk / Wikimedia Commons",
        "license": "Creative Commons Attribution-Share Alike"
    },
    4: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Landing_on_a_very_wet_runway_at_St._John%27s_Nfl_%2827595229845%29.jpg",
        "title": "Commercial Jet Touching Down on a Rain-Soaked Runway",
        "caption": "A twin-engine passenger jet landing on a wet runway, dispersing standing surface water while operating under strict crosswind and hydroplaning safety limits.",
        "author": "Wikimedia Commons",
        "license": "Creative Commons Attribution-Share Alike"
    }
}

SVG_MAP = {
    0: {
        "svg": SVG_WEATHER_ELEMENTS,
        "title": "Aviation Weather Elements & Aerodynamic Air Density",
        "page": 4
    },
    1: {
        "svg": SVG_ATMOSPHERE_LAYERS,
        "title": "Lower Atmosphere Vertical Structure & Aviation Flight Regimes",
        "page": 4
    },
    2: {
        "svg": SVG_CLOUD_MATRIX,
        "title": "Cloud Altitude Classification & Thunderstorm (CB) Hazard Anatomy",
        "page": 4
    },
    3: {
        "svg": SVG_INSTRUMENT_SUITE,
        "title": "Aerodrome Meteorological Sensors & Windsock Speed Analysis",
        "page": 4
    },
    4: {
        "svg": SVG_SAFETY_ECOSYSTEM,
        "title": "Aviation Weather Safety Chain & Runway Aquaplaning Physics",
        "page": 4
    }
}

YOUTUBE_VIDEOS = {
    0: {
        "url": "https://www.youtube.com/watch?v=G5rCZSQo44A",
        "title": "Atmosphere & Temperature in Aviation Meteorology",
        "description": "Expert flight instructor explains atmospheric physics, air density effects on aircraft performance, and how temperature variations dictate takeoff performance."
    },
    1: {
        "url": "https://www.youtube.com/watch?v=Id1AGMA0o_c",
        "title": "PPGS Lesson 11.1 | Weather: Atmospheric Layers",
        "description": "Private Pilot Ground School lecture explaining atmospheric composition, vertical temperature profiles, and operational altitude planning for pilots."
    },
    2: {
        "url": "https://www.youtube.com/watch?v=41BirFo_0UE",
        "title": "Clouds & Moisture Basics Explained in Flight Theory",
        "description": "Aviation weather tutorial covering moisture condensation, dew point spread, cloud base calculation, and the operational hazards associated with various cloud formations."
    },
    3: {
        "url": "https://www.youtube.com/watch?v=nS0N69snh14",
        "title": "PPGS Lesson 7.3 | Aircraft Instruments: Altimeter",
        "description": "Flight training tutorial detailing how atmospheric pressure governs the aneroid altimeter mechanism, subscale calibration, and operational altimetry errors."
    },
    4: {
        "url": "https://www.youtube.com/watch?v=9JeBd7TntfE",
        "title": "Instrument Weather Theory & Operational Hazard Analysis",
        "description": "Comprehensive flight training video examining frontal systems, convective hazard development, turbulence mechanisms, and tactical weather decision-making in airline operations."
    }
}

def enrich_grade10_topic250():
    """Enriches Topic 250 lessons with verified photos, vector SVGs, and educational videos."""
    print("=" * 80)
    print("VLearn Visual Enrichment Engine: Grade 10 Aviation — Topic 250")
    print("=" * 80)

    topic = Topic.objects.filter(id=250, subject_id=44).first()
    if not topic:
        print("[ERROR] Topic 250 not found!")
        sys.exit(1)

    lessons = Lesson.objects.filter(topic=topic).order_by("learning_unit__order")
    print(f"[*] Found {lessons.count()} lessons under Topic 250: '{topic.name}'.")

    total_photos_attached = 0
    total_svgs_attached = 0
    total_videos_attached = 0
    total_assets_persisted = 0

    for lesson in lessons:
        u_order = lesson.learning_unit.order
        print(f"\n[+] Processing Lesson {u_order + 1}: {lesson.title}")

        # ---------------------------------------------------------------------
        # 1. First-Card Photographic Visual Hooks
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
                        "source_type": "wikimedia",
                        "storage_type": "url",
                        "status": "attached",
                        "title": img_def["title"],
                        "description": img_def["caption"],
                        "metadata": {
                            "author": img_def["author"],
                            "license": img_def["license"],
                            "topic_order": 3,
                            "unit_order": u_order
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
                            "topic_order": 3,
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
                            "topic_order": 3,
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
    print(f"ENRICHMENT COMPLETE: Topic 250 '{topic.name}'")
    print(f"  Photographic Hooks: {total_photos_attached} / 5")
    print(f"  Vector SVGs:        {total_svgs_attached} / 5")
    print(f"  YouTube Videos:     {total_videos_attached} / 5")
    print(f"  LessonAssets Total: {total_assets_persisted}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic250()
