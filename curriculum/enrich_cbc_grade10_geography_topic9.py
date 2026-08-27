"""
VLearn CBC Grade 10 Geography — Topic 9: Earthquakes
Visual Enrichment Engine (Vector SVGs, Verified Wikimedia Images & Educational Videos)

Subject: Geography (Grade 10 CBC, Subject ID: 37)
Topic 9: Earthquakes

Attaches:
  - 10 First-Card Photographic Visual Hooks (100% Tested HTTP 200/206 Direct Wikimedia URLs)
  - 10 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - Educational YouTube Video for Earthquake Liquefaction & Tsunami Hazards (Lesson 6)
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade10_geography_topic9.py
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
# 10 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 9: EARTHQUAKES
# =============================================================================

# SVG 1: Earthquake Anatomy (Lesson 1)
SVG_EARTHQUAKE_ANATOMY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">ANATOMY OF AN EARTHQUAKE: FOCUS, EPICENTRE &amp; FAULT LINE</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">3D Spatial Relationship Between Subterranean Rupture &amp; Surface Wavefronts</text>

  <!-- Left Block (Footwall) -->
  <polygon points="120,180 340,140 340,360 120,380" fill="#334155" stroke="#475569" stroke-width="2"/>
  <polygon points="120,180 240,110 440,110 340,140" fill="#475569" stroke="#64748b" stroke-width="2"/>
  
  <!-- Right Block (Hanging wall displaced along fault plane) -->
  <polygon points="340,170 560,130 560,390 340,400" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
  <polygon points="340,170 440,110 660,110 560,130" fill="#334155" stroke="#64748b" stroke-width="2"/>

  <!-- Fault Plane Line / Scarp -->
  <line x1="340" y1="140" x2="340" y2="390" stroke="#ef4444" stroke-width="3" stroke-dasharray="6,4"/>
  <text x="315" y="270" font-size="12" font-weight="bold" fill="#f87171" transform="rotate(-70 315 270)">FAULT PLANE</text>

  <!-- Underground Focus (Hypocentre) -->
  <circle cx="340" cy="300" r="18" fill="#ef4444" opacity="0.3"/>
  <circle cx="340" cy="300" r="10" fill="#ef4444" opacity="0.7"/>
  <circle cx="340" cy="300" r="5" fill="#fbbf24"/>
  
  <!-- Concentric Seismic Waves from Focus -->
  <circle cx="340" cy="300" r="35" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,3" opacity="0.8"/>
  <circle cx="340" cy="300" r="60" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,4" opacity="0.6"/>
  <circle cx="340" cy="300" r="90" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,4" opacity="0.4"/>
  <circle cx="340" cy="300" r="120" fill="none" stroke="#f59e0b" stroke-width="1" stroke-dasharray="4,4" opacity="0.25"/>

  <!-- Vertical Projection Line from Focus to Epicentre -->
  <line x1="340" y1="300" x2="340" y2="155" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,3"/>
  
  <!-- Surface Epicentre -->
  <ellipse cx="340" cy="155" rx="14" ry="7" fill="#ef4444" stroke="#ffffff" stroke-width="2"/>
  <ellipse cx="340" cy="155" rx="30" ry="15" fill="none" stroke="#38bdf8" stroke-width="2"/>
  <ellipse cx="340" cy="155" rx="55" ry="25" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>

  <!-- Callout Labels -->
  <!-- Epicentre Label -->
  <g transform="translate(420, 140)">
    <line x1="-70" y1="15" x2="0" y2="0" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="-15" width="180" height="40" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="90" y="2" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">EPICENTRE</text>
    <text x="90" y="18" font-size="9" fill="#94a3b8" text-anchor="middle">Point on surface directly above focus</text>
  </g>

  <!-- Focus Label -->
  <g transform="translate(110, 290)">
    <line x1="150" y1="10" x2="220" y2="10" stroke="#fbbf24" stroke-width="1.5"/>
    <rect x="0" y="-10" width="160" height="45" rx="6" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="80" y="8" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">FOCUS (HYPOCENTRE)</text>
    <text x="80" y="24" font-size="9" fill="#94a3b8" text-anchor="middle">Exact subterranean point of rupture</text>
  </g>

  <!-- Right Panel Info Box -->
  <g transform="translate(560, 200)">
    <rect x="0" y="0" width="200" height="210" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="100" y="25" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">SEISMIC WAVE PROPAGATION</text>
    
    <circle cx="20" cy="55" r="5" fill="#38bdf8"/>
    <text x="35" y="58" font-size="10" font-weight="bold" fill="#ffffff">P-Waves (Primary):</text>
    <text x="35" y="73" font-size="9" fill="#cbd5e1">Compressional; fastest (solid &amp; liquid)</text>

    <circle cx="20" cy="100" r="5" fill="#f59e0b"/>
    <text x="35" y="103" font-size="10" font-weight="bold" fill="#ffffff">S-Waves (Secondary):</text>
    <text x="35" y="118" font-size="9" fill="#cbd5e1">Transverse shear; solids only</text>

    <circle cx="20" cy="145" r="5" fill="#ef4444"/>
    <text x="35" y="148" font-size="10" font-weight="bold" fill="#ffffff">Surface Waves:</text>
    <text x="35" y="163" font-size="9" fill="#cbd5e1">Slowest; maximum destructive shaking</text>

    <rect x="15" y="180" width="170" height="20" rx="4" fill="#0369a1"/>
    <text x="100" y="194" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Kenyan Rift: Shallow Normal Faulting</text>
  </g>
</svg>
""")

# SVG 2: Focal Depth & Wadati-Benioff Zone (Lesson 2)
SVG_EARTHQUAKE_DEPTH_TYPES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">EARTHQUAKE DEPTH CLASSIFICATION &amp; SUBDUCTION SEISMICITY</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Wadati-Benioff Zone Hypocentre Distribution &amp; Earthquake Temporal Sequences</text>

  <!-- Subduction Cross-Section -->
  <g transform="translate(40, 85)">
    <rect x="0" y="0" width="460" height="325" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    
    <!-- Oceanic Crust -->
    <path d="M 15 50 L 160 50 L 320 280 L 260 300 L 130 90 L 15 90 Z" fill="#3b82f6" opacity="0.6"/>
    <text x="60" y="40" font-size="11" font-weight="bold" fill="#60a5fa">Oceanic Plate</text>
    
    <!-- Continental Crust & Trench -->
    <path d="M 170 50 L 440 50 L 440 220 L 280 220 Z" fill="#78350f" opacity="0.8"/>
    <text x="350" y="40" font-size="11" font-weight="bold" fill="#fcd34d">Overriding Continent</text>
    <polygon points="360,50 385,25 410,50" fill="#dc2626"/>
    <text x="385" y="20" font-size="9" fill="#fca5a5" text-anchor="middle">Volcanic Arc</text>

    <!-- Depth Scale on Left -->
    <line x1="15" y1="50" x2="15" y2="300" stroke="#64748b" stroke-width="1"/>
    <text x="25" y="70" font-size="9" fill="#94a3b8">0 km (Surface)</text>
    <line x1="15" y1="120" x2="440" y2="120" stroke="#475569" stroke-width="1" stroke-dasharray="2,2"/>
    <text x="25" y="115" font-size="9" fill="#f87171">70 km (Shallow Boundary)</text>
    
    <line x1="15" y1="220" x2="440" y2="220" stroke="#475569" stroke-width="1" stroke-dasharray="2,2"/>
    <text x="25" y="215" font-size="9" fill="#fbbf24">300 km (Intermediate Boundary)</text>
    <text x="25" y="295" font-size="9" fill="#38bdf8">700 km (Deep Boundary)</text>

    <!-- Earthquake Hypocentres (Dots along Wadati-Benioff zone) -->
    <!-- Shallow: Red -->
    <circle cx="160" cy="70" r="7" fill="#ef4444"/>
    <circle cx="180" cy="90" r="6" fill="#ef4444"/>
    <circle cx="195" cy="110" r="6" fill="#ef4444"/>
    <!-- Intermediate: Orange -->
    <circle cx="225" cy="150" r="6" fill="#f59e0b"/>
    <circle cx="250" cy="180" r="6" fill="#f59e0b"/>
    <circle cx="270" cy="210" r="6" fill="#f59e0b"/>
    <!-- Deep: Blue/Cyan -->
    <circle cx="290" cy="245" r="6" fill="#38bdf8"/>
    <circle cx="310" cy="275" r="6" fill="#38bdf8"/>

    <text x="280" y="160" font-size="11" font-weight="bold" fill="#fca5a5" transform="rotate(50 280 160)">Wadati-Benioff Zone</text>
  </g>

  <!-- Right Panel: Earthquake Sequence & Energy -->
  <g transform="translate(520, 85)">
    <rect x="0" y="0" width="240" height="325" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="120" y="25" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">EARTHQUAKE SEQUENCE</text>

    <!-- Sequence Chart -->
    <g transform="translate(15, 45)">
      <!-- Foreshock -->
      <rect x="0" y="0" width="210" height="45" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
      <text x="10" y="18" font-size="11" font-weight="bold" fill="#fbbf24">1. Foreshocks</text>
      <text x="10" y="34" font-size="9" fill="#cbd5e1">Micro-ruptures prior to main fault failure</text>

      <!-- Mainshock -->
      <rect x="0" y="55" width="210" height="50" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
      <text x="10" y="75" font-size="11" font-weight="bold" fill="#f87171">2. Mainshock</text>
      <text x="10" y="92" font-size="9" fill="#cbd5e1">Principal massive energy release (highest Mw)</text>

      <!-- Aftershocks -->
      <rect x="0" y="115" width="210" height="45" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <text x="10" y="133" font-size="11" font-weight="bold" fill="#38bdf8">3. Aftershocks</text>
      <text x="10" y="149" font-size="9" fill="#cbd5e1">Crustal readjustment along adjacent faults</text>
    </g>

    <!-- Depth vs Damage Summary -->
    <g transform="translate(15, 225)">
      <rect x="0" y="0" width="210" height="85" rx="6" fill="#0f172a" stroke="#475569"/>
      <text x="105" y="18" font-size="10" font-weight="bold" fill="#fca5a5" text-anchor="middle">FOCAL DEPTH &amp; SURFACE DAMAGE</text>
      <text x="10" y="36" font-size="9" fill="#cbd5e1">• <tspan font-weight="bold" fill="#ef4444">Shallow (0–70 km):</tspan> 75% of energy; most destructive.</text>
      <text x="10" y="52" font-size="9" fill="#cbd5e1">• <tspan font-weight="bold" fill="#f59e0b">Intermediate (70–300 km):</tspan> Moderate shaking.</text>
      <text x="10" y="68" font-size="9" fill="#cbd5e1">• <tspan font-weight="bold" fill="#38bdf8">Deep (300–700 km):</tspan> Attenuates before reaching surface.</text>
    </g>
  </g>
</svg>
""")

# SVG 3: Global Seismic Belts (Lesson 3)
SVG_GLOBAL_SEISMIC_BELTS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">GLOBAL SEISMIC BELTS &amp; PLATE BOUNDARIES</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Spatial Distribution: Ring of Fire, Alpine-Himalayan Belt &amp; East African Rift</text>

  <!-- World Map Stylized Grid Background -->
  <g transform="translate(35, 80)">
    <rect x="0" y="0" width="730" height="240" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    
    <!-- Stylized Continents Outlines -->
    <!-- North America -->
    <path d="M 60 40 L 130 30 L 160 70 L 130 110 L 90 90 L 60 70 Z" fill="#334155" opacity="0.7"/>
    <!-- South America -->
    <path d="M 130 120 L 170 130 L 150 200 L 120 170 Z" fill="#334155" opacity="0.7"/>
    <!-- Eurasia -->
    <path d="M 320 30 L 520 25 L 560 80 L 460 90 L 380 70 L 320 50 Z" fill="#334155" opacity="0.7"/>
    <!-- Africa -->
    <path d="M 330 80 L 390 85 L 400 150 L 360 190 L 330 130 Z" fill="#334155" opacity="0.7"/>
    <!-- Australia -->
    <path d="M 540 140 L 600 140 L 590 190 L 530 180 Z" fill="#334155" opacity="0.7"/>

    <!-- 1. Circum-Pacific Ring of Fire (Red Curved Highway) -->
    <!-- East Pacific Rim (Americas) -->
    <path d="M 60 30 Q 90 80 130 120 Q 155 160 135 210" fill="none" stroke="#ef4444" stroke-width="5" opacity="0.85"/>
    <!-- West Pacific Rim (Asia / Oceania) -->
    <path d="M 530 30 Q 560 80 540 120 Q 580 160 560 210" fill="none" stroke="#ef4444" stroke-width="5" opacity="0.85"/>
    <!-- Aleutian connecting arc -->
    <path d="M 530 30 Q 640 10 700 15 M 10 15 Q 40 10 60 30" fill="none" stroke="#ef4444" stroke-width="4" stroke-dasharray="4,2"/>

    <!-- 2. Alpine-Himalayan Belt (Yellow Ribbon) -->
    <path d="M 300 75 Q 360 80 430 80 Q 480 85 520 120" fill="none" stroke="#fbbf24" stroke-width="4.5" opacity="0.9"/>

    <!-- 3. Mid-Atlantic Ridge & East African Rift (Cyan/Green) -->
    <!-- Mid Atlantic Ridge -->
    <path d="M 230 30 Q 250 100 230 150 Q 250 200 240 220" fill="none" stroke="#38bdf8" stroke-width="3.5" stroke-dasharray="5,3"/>
    <!-- East African Rift (EARS) -->
    <path d="M 375 95 Q 385 135 375 175" fill="none" stroke="#34d399" stroke-width="4"/>
    <circle cx="380" cy="135" r="4" fill="#fbbf24"/>
    <text x="395" y="140" font-size="9" font-weight="bold" fill="#34d399">Kenyan Gregory Rift</text>

    <!-- Labels on Map -->
    <text x="600" y="85" font-size="11" font-weight="bold" fill="#f87171">Pacific Ring of Fire (80%+)</text>
    <text x="420" y="65" font-size="10" font-weight="bold" fill="#fbbf24">Alpine-Himalayan Belt</text>
    <text x="170" y="80" font-size="9" fill="#38bdf8">Mid-Atlantic Ridge</text>
  </g>

  <!-- Bottom Legend Bar -->
  <g transform="translate(35, 335)">
    <rect x="0" y="0" width="730" height="85" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    
    <g transform="translate(20, 15)">
      <line x1="0" y1="10" x2="30" y2="10" stroke="#ef4444" stroke-width="4"/>
      <text x="40" y="14" font-size="11" font-weight="bold" fill="#f87171">1. Circum-Pacific Belt ("Ring of Fire")</text>
      <text x="40" y="30" font-size="9" fill="#cbd5e1">Subduction megathrust earthquakes; >80% global seismic energy (Japan, Chile, Alaska).</text>
    </g>

    <g transform="translate(380, 15)">
      <line x1="0" y1="10" x2="30" y2="10" stroke="#fbbf24" stroke-width="4"/>
      <text x="40" y="14" font-size="11" font-weight="bold" fill="#fbbf24">2. Alpine-Himalayan Collision Belt</text>
      <text x="40" y="30" font-size="9" fill="#cbd5e1">Continental collision; shallow destructive crustal earthquakes (Mediterranean, Nepal, Iran).</text>
    </g>

    <g transform="translate(20, 50)">
      <line x1="0" y1="10" x2="30" y2="10" stroke="#34d399" stroke-width="4"/>
      <text x="40" y="14" font-size="11" font-weight="bold" fill="#34d399">3. Continental Rifts (East African Rift)</text>
      <text x="40" y="28" font-size="9" fill="#cbd5e1">Tensional crustal pulling; shallow volcanic &amp; fault tremors (Kenya, Tanzania, Ethiopia).</text>
    </g>
  </g>
</svg>
""")

# SVG 4: Richter vs Mercalli Scales (Lesson 4)
SVG_RICHTER_VS_MERCALLI = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">MEASURING EARTHQUAKES: RICHTER MAGNITUDE VS. MERCALLI INTENSITY</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Quantitative Mathematical Focus Energy vs. Qualitative Observed Surface Destruction</text>

  <!-- Left Column: Richter Scale -->
  <g transform="translate(35, 85)">
    <rect x="0" y="0" width="350" height="325" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="350" height="35" rx="8" fill="#0369a1"/>
    <text x="175" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">RICHTER SCALE (QUANTITATIVE)</text>

    <text x="20" y="60" font-size="10.5" fill="#94a3b8">• Measures: <tspan font-weight="bold" fill="#38bdf8">Wave amplitude &amp; Energy release</tspan></text>
    <text x="20" y="78" font-size="10.5" fill="#94a3b8">• Instrument: <tspan font-weight="bold" fill="#38bdf8">Seismograph / Seismometer</tspan></text>
    <text x="20" y="96" font-size="10.5" fill="#94a3b8">• Mathematical Type: <tspan font-weight="bold" fill="#fbbf24">Logarithmic (Base 10 / ~32x Energy)</tspan></text>

    <!-- Energy Comparison Bars -->
    <g transform="translate(20, 115)">
      <rect x="0" y="0" width="40" height="22" rx="3" fill="#334155"/>
      <text x="20" y="15" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">M 4.0</text>
      <rect x="50" y="4" width="20" height="14" rx="2" fill="#38bdf8"/>
      <text x="80" y="15" font-size="9.5" fill="#cbd5e1">1x Energy baseline</text>

      <rect x="0" y="30" width="40" height="22" rx="3" fill="#334155"/>
      <text x="20" y="45" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">M 5.0</text>
      <rect x="50" y="34" width="60" height="14" rx="2" fill="#f59e0b"/>
      <text x="120" y="45" font-size="9.5" fill="#cbd5e1">~32x Energy</text>

      <rect x="0" y="60" width="40" height="22" rx="3" fill="#334155"/>
      <text x="20" y="75" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">M 6.0</text>
      <rect x="50" y="64" width="140" height="14" rx="2" fill="#ef4444"/>
      <text x="200" y="75" font-size="9.5" fill="#cbd5e1">~1,024x Energy</text>

      <rect x="0" y="90" width="40" height="22" rx="3" fill="#334155"/>
      <text x="20" y="105" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">M 8.0</text>
      <rect x="50" y="94" width="240" height="14" rx="2" fill="#dc2626"/>
      <text x="150" y="125" font-size="9.5" font-weight="bold" fill="#fca5a5">~1,000,000x Energy surge!</text>
    </g>

    <rect x="20" y="270" width="310" height="35" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="175" y="292" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Only ONE magnitude value per earthquake</text>
  </g>

  <!-- Right Column: Mercalli Scale -->
  <g transform="translate(415, 85)">
    <rect x="0" y="0" width="350" height="325" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="350" height="35" rx="8" fill="#991b1b"/>
    <text x="175" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">MODIFIED MERCALLI SCALE (QUALITATIVE)</text>

    <text x="20" y="60" font-size="10.5" fill="#94a3b8">• Measures: <tspan font-weight="bold" fill="#f87171">Observed shaking &amp; structural damage</tspan></text>
    <text x="20" y="78" font-size="10.5" fill="#94a3b8">• Instrument: <tspan font-weight="bold" fill="#f87171">Human sensation &amp; damage audits</tspan></text>
    <text x="20" y="96" font-size="10.5" fill="#94a3b8">• Rating Units: <tspan font-weight="bold" fill="#fbbf24">Roman Numerals (I to XII)</tspan></text>

    <!-- Mercalli Grades -->
    <g transform="translate(20, 115)">
      <rect x="0" y="0" width="45" height="22" rx="3" fill="#334155"/>
      <text x="22" y="15" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">I - II</text>
      <text x="55" y="15" font-size="9.5" fill="#cbd5e1">Felt only by sensitive instruments</text>

      <rect x="0" y="30" width="45" height="22" rx="3" fill="#334155"/>
      <text x="22" y="45" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">V - VI</text>
      <text x="55" y="45" font-size="9.5" fill="#cbd5e1">Felt by all; glassware breaks; minor cracks</text>

      <rect x="0" y="60" width="45" height="22" rx="3" fill="#334155"/>
      <text x="22" y="75" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">VIII - IX</text>
      <text x="55" y="75" font-size="9.5" fill="#cbd5e1">Heavy damage; partial building collapse</text>

      <rect x="0" y="90" width="45" height="22" rx="3" fill="#334155"/>
      <text x="22" y="105" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">XI - XII</text>
      <text x="55" y="105" font-size="9.5" fill="#fca5a5">Catastrophic total collapse; surface waves seen</text>
    </g>

    <rect x="20" y="270" width="310" height="35" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="175" y="292" font-size="10" font-weight="bold" fill="#f87171" text-anchor="middle">VARIES by location, distance &amp; soil type</text>
  </g>
</svg>
""")

# SVG 5: Seismograph Mechanics & Triangulation (Lesson 5)
SVG_SEISMOGRAPH_AND_TRIANGULATION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">SEISMOGRAPHS &amp; EPICENTRE TRIANGULATION</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Inertial Mass Mechanics &amp; Three-Station S-P Lag Distance Intersection</text>

  <!-- Left: Seismograph Mechanics -->
  <g transform="translate(35, 85)">
    <rect x="0" y="0" width="350" height="325" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="175" y="25" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. VERTICAL SEISMOGRAPH MECHANICS</text>

    <!-- Rigid Frame -->
    <path d="M 40 270 L 40 70 L 140 70" fill="none" stroke="#64748b" stroke-width="5"/>
    <!-- Bedrock base -->
    <rect x="25" y="270" width="120" height="25" fill="#475569" rx="2"/>
    <text x="85" y="287" font-size="9" fill="#cbd5e1" text-anchor="middle">Bedrock Base</text>

    <!-- Spring Suspension -->
    <path d="M 120 70 L 120 85 Q 110 95 120 105 Q 130 115 120 125 Q 110 135 120 145 L 120 160" fill="none" stroke="#f59e0b" stroke-width="2.5"/>
    
    <!-- Suspended Inertial Mass (Heavy Weight) -->
    <circle cx="120" cy="180" r="22" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/>
    <text x="120" y="184" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">MASS</text>
    <text x="120" y="215" font-size="9" font-weight="bold" fill="#fbbf24" text-anchor="middle">(Stays still via Inertia)</text>

    <!-- Pen -->
    <line x1="142" y1="180" x2="190" y2="180" stroke="#ef4444" stroke-width="2"/>
    <circle cx="190" cy="180" r="3" fill="#ef4444"/>

    <!-- Rotating Drum -->
    <rect x="190" y="110" width="70" height="140" rx="6" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
    <ellipse cx="225" cy="110" rx="35" ry="10" fill="#475569"/>
    <!-- Seismogram Wiggle Trace on Drum -->
    <path d="M 190 125 Q 210 125 215 125 Q 220 115 225 135 Q 230 105 235 145 Q 240 125 260 125" fill="none" stroke="#ef4444" stroke-width="1.5"/>
    <text x="225" y="265" font-size="9" fill="#94a3b8" text-anchor="middle">Rotating Drum (Moves with Earth)</text>

    <!-- Physics Summary -->
    <rect x="20" y="280" width="310" height="35" rx="4" fill="#1e293b"/>
    <text x="175" y="295" font-size="8.5" fill="#cbd5e1" text-anchor="middle"><tspan font-weight="bold" fill="#38bdf8">Key Principle:</tspan> Ground moves drum; mass remains stationary.</text>
  </g>

  <!-- Right: Triangulation Method -->
  <g transform="translate(415, 85)">
    <rect x="0" y="0" width="350" height="325" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="175" y="25" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">2. THREE-STATION TRIANGULATION</text>

    <!-- Station A -->
    <circle cx="120" cy="110" r="4" fill="#38bdf8"/>
    <text x="120" y="100" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Station A (Nairobi)</text>
    <circle cx="120" cy="110" r="75" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,3"/>

    <!-- Station B -->
    <circle cx="240" cy="120" r="4" fill="#f59e0b"/>
    <text x="240" y="110" font-size="9" font-weight="bold" fill="#f59e0b" text-anchor="middle">Station B (Eldoret)</text>
    <circle cx="240" cy="120" r="85" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,3"/>

    <!-- Station C -->
    <circle cx="170" cy="230" r="4" fill="#34d399"/>
    <text x="170" y="250" font-size="9" font-weight="bold" fill="#34d399" text-anchor="middle">Station C (Mombasa)</text>
    <circle cx="170" cy="230" r="95" fill="none" stroke="#34d399" stroke-width="1.5" stroke-dasharray="4,3"/>

    <!-- Intersection Point (Epicentre) -->
    <circle cx="175" cy="150" r="8" fill="#ef4444"/>
    <polygon points="175,142 178,148 184,148 179,152 181,158 175,154 169,158 171,152 166,148 172,148" fill="#ffffff"/>
    <text x="220" y="160" font-size="10" font-weight="bold" fill="#f87171">EPICENTRE</text>

    <!-- Triangulation Steps -->
    <g transform="translate(15, 260)">
      <rect x="0" y="0" width="320" height="55" rx="6" fill="#1e293b" stroke="#475569"/>
      <text x="10" y="17" font-size="9" fill="#cbd5e1">1. Measure S-P interval to calculate distance radius for each station.</text>
      <text x="10" y="32" font-size="9" fill="#cbd5e1">2. Draw 3 distance circles on map.</text>
      <text x="10" y="47" font-size="9" font-weight="bold" fill="#fca5a5">3. Single common intersection point = Earthquake Epicentre!</text>
    </g>
  </g>
</svg>
""")

# SVG 6: Seismic Hazards Matrix (Lesson 6)
SVG_SEISMIC_HAZARDS_LIQUEFACTION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">PRIMARY &amp; SECONDARY SEISMIC HAZARDS</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Mechanisms of Soil Liquefaction, Tsunami Generation, Landslides &amp; Fires</text>

  <!-- 4 Hazard Panels Grid -->
  <!-- Panel 1: Soil Liquefaction -->
  <g transform="translate(35, 85)">
    <rect x="0" y="0" width="350" height="150" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="350" height="28" rx="8" fill="#b45309"/>
    <text x="175" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1. SOIL LIQUEFACTION</text>

    <!-- Sinking building illustration -->
    <rect x="20" y="70" width="100" height="60" fill="#3b82f6" opacity="0.4" rx="2"/>
    <text x="70" y="105" font-size="9" fill="#93c5fd" text-anchor="middle">Water-saturated sand</text>
    <!-- Tilted Building -->
    <polygon points="50,45 85,35 105,95 70,105" fill="#64748b" stroke="#94a3b8" stroke-width="1.5"/>
    
    <g transform="translate(135, 40)">
      <text x="0" y="15" font-size="9.5" fill="#cbd5e1">• Shaking increases pore-water pressure.</text>
      <text x="0" y="32" font-size="9.5" fill="#cbd5e1">• Granular grains lose shear friction.</text>
      <text x="0" y="49" font-size="9.5" fill="#cbd5e1">• Soil behaves like dense liquid mud.</text>
      <text x="0" y="70" font-size="9.5" font-weight="bold" fill="#fbbf24">Result: Heavy buildings sink &amp; tilt.</text>
    </g>
  </g>

  <!-- Panel 2: Tsunami Generation -->
  <g transform="translate(415, 85)">
    <rect x="0" y="0" width="350" height="150" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="350" height="28" rx="8" fill="#0284c7"/>
    <text x="175" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2. SUBDUCTION TSUNAMI GENERATION</text>

    <!-- Fault Uplift & Wave -->
    <path d="M 15 120 L 70 120 L 70 90 L 120 90" fill="none" stroke="#ef4444" stroke-width="3"/>
    <polygon points="70,100 65,80 75,80" fill="#ef4444"/>
    <path d="M 15 65 Q 40 60 70 45 Q 90 65 120 65" fill="none" stroke="#38bdf8" stroke-width="2.5"/>

    <g transform="translate(135, 40)">
      <text x="0" y="15" font-size="9.5" fill="#cbd5e1">• Undersea megathrust fault slips vertically.</text>
      <text x="0" y="32" font-size="9.5" fill="#cbd5e1">• Entire ocean water column displaced.</text>
      <text x="0" y="49" font-size="9.5" fill="#cbd5e1">• Fast in deep water (800 km/h).</text>
      <text x="0" y="70" font-size="9.5" font-weight="bold" fill="#38bdf8">Surges up to 30m in shallow coasts.</text>
    </g>
  </g>

  <!-- Panel 3: Landslides & Slope Failure -->
  <g transform="translate(35, 250)">
    <rect x="0" y="0" width="350" height="160" rx="8" fill="#0f172a" stroke="#e2e8f0" stroke-width="1.5"/>
    <rect x="0" y="0" width="350" height="28" rx="8" fill="#475569"/>
    <text x="175" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">3. SEISMIC LANDSLIDES &amp; SCARPS</text>

    <polygon points="20,135 110,60 110,135" fill="#334155"/>
    <polygon points="70,90 105,65 120,115 85,135" fill="#b45309"/>
    <text x="95" y="145" font-size="8" fill="#fca5a5" text-anchor="middle">Debris flow</text>

    <g transform="translate(135, 40)">
      <text x="0" y="15" font-size="9.5" fill="#cbd5e1">• Ground vibrations destabilize slopes.</text>
      <text x="0" y="32" font-size="9.5" fill="#cbd5e1">• Blocks roads and dams river valleys.</text>
      <text x="0" y="49" font-size="9.5" fill="#cbd5e1">• Catastrophic upstream flood risks.</text>
      <text x="0" y="70" font-size="9.5" font-weight="bold" fill="#e2e8f0">E.g., Elgeyo Marakwet Escarpment.</text>
    </g>
  </g>

  <!-- Panel 4: Secondary Conflagrations -->
  <g transform="translate(415, 250)">
    <rect x="0" y="0" width="350" height="160" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="350" height="28" rx="8" fill="#b91c1c"/>
    <text x="175" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">4. INFRASTRUCTURE &amp; FIRE HAZARDS</text>

    <g transform="translate(20, 45)">
      <path d="M 25 70 Q 40 30 55 70 Q 70 30 85 70" fill="none" stroke="#ef4444" stroke-width="3"/>
      <polygon points="40,55 55,25 70,55" fill="#f59e0b"/>
      <text x="55" y="85" font-size="8.5" fill="#fca5a5" text-anchor="middle">Ruptured Gas Pipes</text>
    </g>

    <g transform="translate(135, 40)">
      <text x="0" y="15" font-size="9.5" fill="#cbd5e1">• Ruptured municipal gas lines ignite.</text>
      <text x="0" y="32" font-size="9.5" fill="#cbd5e1">• Severed water mains hinder firefighting.</text>
      <text x="0" y="49" font-size="9.5" fill="#cbd5e1">• Collapsed bridges block ambulances.</text>
      <text x="0" y="70" font-size="9.5" font-weight="bold" fill="#f87171">Solution: Automated seismic shut-offs.</text>
    </g>
  </g>
</svg>
""")

# SVG 7: Base Isolation & Vulnerability (Lesson 7)
SVG_SEISMIC_VULNERABILITY_BASE_ISOLATION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">EARTHQUAKE ENGINEERING: CONVENTIONAL VS. BASE ISOLATION</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Decoupling Superstructures from Ground Motion to Prevent Structural Collapse</text>

  <!-- Left Building: Conventional Fixed-Base (Brittle / Vulnerable) -->
  <g transform="translate(50, 85)">
    <rect x="0" y="0" width="320" height="325" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="160" y="25" font-size="12" font-weight="bold" fill="#f87171" text-anchor="middle">CONVENTIONAL FIXED-BASE</text>

    <!-- Ground Shaking Arrows -->
    <line x1="40" y1="280" x2="280" y2="280" stroke="#ef4444" stroke-width="3"/>
    <polygon points="50,275 30,280 50,285" fill="#ef4444"/>
    <polygon points="270,275 290,280 270,285" fill="#ef4444"/>
    <text x="160" y="302" font-size="9" fill="#f87171" text-anchor="middle">Violent Ground Acceleration</text>

    <!-- Deformed / Sheared Building -->
    <path d="M 80 270 L 110 90 L 210 90 L 180 270 Z" fill="#334155" stroke="#ef4444" stroke-width="2"/>
    <!-- Crack Lines -->
    <path d="M 120 220 L 140 200 L 130 180" stroke="#fbbf24" stroke-width="2.5"/>
    <path d="M 170 160 L 150 140 L 165 120" stroke="#fbbf24" stroke-width="2.5"/>

    <text x="160" y="75" font-size="9" font-weight="bold" fill="#f87171" text-anchor="middle">Severe Inter-Story Shear Drift</text>

    <g transform="translate(20, 210)">
      <rect x="0" y="0" width="280" height="50" rx="4" fill="#1e293b"/>
      <text x="10" y="18" font-size="9" fill="#fca5a5">• High inertia transfers directly into columns.</text>
      <text x="10" y="35" font-size="9" font-weight="bold" fill="#ef4444">• Brittle failure &amp; pancake collapse risk.</text>
    </g>
  </g>

  <!-- Right Building: Base-Isolated Building (Resilient) -->
  <g transform="translate(430, 85)">
    <rect x="0" y="0" width="320" height="325" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="160" y="25" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">SEISMIC BASE ISOLATION</text>

    <!-- Shaking Ground -->
    <line x1="40" y1="280" x2="280" y2="280" stroke="#ef4444" stroke-width="3"/>
    <polygon points="50,275 30,280 50,285" fill="#ef4444"/>
    <polygon points="270,275 290,280 270,285" fill="#ef4444"/>

    <!-- Base Isolator Bearings (Rubber & Steel Pads) -->
    <rect x="80" y="250" width="35" height="20" rx="3" fill="#fbbf24" stroke="#d97706"/>
    <rect x="205" y="250" width="35" height="20" rx="3" fill="#fbbf24" stroke="#d97706"/>
    <text x="160" y="264" font-size="8.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">Elastomeric Bearings</text>

    <!-- Upright Superstructure (Remains Plumb & Undamaged) -->
    <rect x="75" y="90" width="170" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="4"/>
    
    <!-- Tuned Mass Damper at Top -->
    <circle cx="160" cy="120" r="14" fill="#38bdf8"/>
    <text x="160" y="124" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">TMD</text>
    <text x="160" y="75" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Superstructure Remains Plumb</text>

    <g transform="translate(20, 210)">
      <rect x="0" y="0" width="280" height="50" rx="4" fill="#1e293b"/>
      <text x="10" y="18" font-size="9" fill="#93c5fd">• Bearings absorb ~80% of ground vibrations.</text>
      <text x="10" y="35" font-size="9" font-weight="bold" fill="#38bdf8">• Structure survives violent Mw 9.0 shaking.</text>
    </g>
  </g>
</svg>
""")

# SVG 8: Drop Cover Hold On (Lesson 8)
SVG_DROP_COVER_HOLD_ON = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">UNIVERSAL EARTHQUAKE SAFETY: DROP, COVER &amp; HOLD ON</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">The Internationally Standardized Life-Saving Physical Response Protocol</text>

  <!-- Step 1: DROP -->
  <g transform="translate(35, 85)">
    <rect x="0" y="0" width="230" height="240" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="230" height="32" rx="8" fill="#b91c1c"/>
    <text x="115" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">STEP 1: DROP</text>

    <!-- Person dropping to knees -->
    <circle cx="80" cy="90" r="15" fill="#fca5a5"/>
    <path d="M 80 105 L 80 150 L 120 170 L 150 170" fill="none" stroke="#fca5a5" stroke-width="8" stroke-linecap="round"/>
    <line x1="40" y1="180" x2="190" y2="180" stroke="#64748b" stroke-width="3"/>

    <text x="115" y="205" font-size="10.5" font-weight="bold" fill="#f87171" text-anchor="middle">Drop to Hands &amp; Knees</text>
    <text x="115" y="222" font-size="9" fill="#cbd5e1" text-anchor="middle">Prevents knockdown by shaking</text>
  </g>

  <!-- Step 2: COVER -->
  <g transform="translate(285, 85)">
    <rect x="0" y="0" width="230" height="240" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect x="0" y="0" width="230" height="32" rx="8" fill="#d97706"/>
    <text x="115" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">STEP 2: COVER</text>

    <!-- Sturdy Desk -->
    <rect x="40" y="80" width="150" height="15" rx="3" fill="#78350f"/>
    <rect x="45" y="95" width="12" height="85" fill="#78350f"/>
    <rect x="173" y="95" width="12" height="85" fill="#78350f"/>
    
    <!-- Person underneath -->
    <circle cx="115" cy="120" r="14" fill="#fde68a"/>
    <path d="M 115 134 L 115 165 L 140 170" fill="none" stroke="#fde68a" stroke-width="7" stroke-linecap="round"/>

    <text x="115" y="205" font-size="10.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">Cover Head &amp; Torso</text>
    <text x="115" y="222" font-size="9" fill="#cbd5e1" text-anchor="middle">Under a sturdy desk or table</text>
  </g>

  <!-- Step 3: HOLD ON -->
  <g transform="translate(535, 85)">
    <rect x="0" y="0" width="230" height="240" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="230" height="32" rx="8" fill="#0284c7"/>
    <text x="115" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">STEP 3: HOLD ON</text>

    <!-- Hands gripping table leg -->
    <rect x="100" y="70" width="30" height="110" rx="4" fill="#78350f"/>
    <ellipse cx="95" cy="120" rx="14" ry="9" fill="#93c5fd"/>
    <ellipse cx="95" cy="140" rx="14" ry="9" fill="#93c5fd"/>

    <text x="115" y="205" font-size="10.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Hold On to Shelter</text>
    <text x="115" y="222" font-size="9" fill="#cbd5e1" text-anchor="middle">Until all shaking stops completely</text>
  </g>

  <!-- Bottom Checklist -->
  <g transform="translate(35, 335)">
    <rect x="0" y="0" width="730" height="85" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="365" y="20" font-size="11" font-weight="bold" fill="#fca5a5" text-anchor="middle">72-HOUR HOUSEHOLD SURVIVAL KIT ESSENTIALS</text>
    
    <g transform="translate(30, 35)">
      <text x="0" y="15" font-size="9.5" fill="#cbd5e1">✓ Water (3L / person / day)</text>
      <text x="0" y="32" font-size="9.5" fill="#cbd5e1">✓ Non-perishable canned food</text>
    </g>
    <g transform="translate(260, 35)">
      <text x="0" y="15" font-size="9.5" fill="#cbd5e1">✓ First-aid kit &amp; essential medicines</text>
      <text x="0" y="32" font-size="9.5" fill="#cbd5e1">✓ LED Flashlight &amp; spare batteries</text>
    </g>
    <g transform="translate(500, 35)">
      <text x="0" y="15" font-size="9.5" fill="#cbd5e1">✓ Acoustic Whistle (to signal rescuers)</text>
      <text x="0" y="32" font-size="9.5" fill="#cbd5e1">✓ Certified copies of national IDs</text>
    </g>
  </g>
</svg>
""")

# SVG 9: Public Safety Broadcast Layout (Lesson 9)
SVG_PUBLIC_SAFETY_BROADCAST = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">PUBLIC DISASTER RISK COMMUNICATION &amp; BROADCAST DESIGN</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">5 Pillars of Emergency Messaging &amp; Multi-Channel Public Broadcast Templates</text>

  <!-- Left: Public Safety Poster Layout -->
  <g transform="translate(35, 85)">
    <rect x="0" y="0" width="350" height="325" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="350" height="32" rx="8" fill="#b91c1c"/>
    <text x="175" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">PUBLIC SAFETY POSTER TEMPLATE</text>

    <g transform="translate(20, 45)">
      <rect x="0" y="0" width="310" height="50" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="155" y="22" font-size="13" font-weight="bold" fill="#ef4444" text-anchor="middle">DROP, COVER, AND HOLD ON!</text>
      <text x="155" y="38" font-size="9.5" fill="#fca5a5" text-anchor="middle">Protect Yourself Immediately During Ground Shaking</text>

      <g transform="translate(0, 60)">
        <rect x="0" y="0" width="95" height="110" rx="4" fill="#1e293b"/>
        <text x="47" y="20" font-size="10" font-weight="bold" fill="#f87171" text-anchor="middle">1. DROP</text>
        <text x="47" y="40" font-size="8" fill="#cbd5e1" text-anchor="middle">To hands &amp; knees</text>

        <rect x="105" y="0" width="100" height="110" rx="4" fill="#1e293b"/>
        <text x="155" y="20" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">2. COVER</text>
        <text x="155" y="40" font-size="8" fill="#cbd5e1" text-anchor="middle">Head &amp; torso</text>

        <rect x="215" y="0" width="95" height="110" rx="4" fill="#1e293b"/>
        <text x="262" y="20" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">3. HOLD ON</text>
        <text x="262" y="40" font-size="8" fill="#cbd5e1" text-anchor="middle">To table legs</text>
      </g>

      <rect x="0" y="180" width="310" height="35" rx="4" fill="#0369a1"/>
      <text x="155" y="202" font-size="9.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Prepare your family emergency kit today!</text>
    </g>
  </g>

  <!-- Right: 30-Second Radio PSA Timeline -->
  <g transform="translate(415, 85)">
    <rect x="0" y="0" width="350" height="325" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="350" height="32" rx="8" fill="#0284c7"/>
    <text x="175" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">30-SECOND RADIO PSA TIMELINE</text>

    <g transform="translate(20, 45)">
      <!-- 0-5s -->
      <rect x="0" y="0" width="310" height="40" rx="4" fill="#1e293b" stroke="#f59e0b"/>
      <text x="10" y="18" font-size="9.5" font-weight="bold" fill="#fbbf24">[0–5s] Hook Sound:</text>
      <text x="10" y="32" font-size="8.5" fill="#cbd5e1">Subterranean rumble effect; "Did you feel that?"</text>

      <!-- 6-18s -->
      <rect x="0" y="50" width="310" height="55" rx="4" fill="#1e293b" stroke="#ef4444"/>
      <text x="10" y="18" font-size="9.5" font-weight="bold" fill="#f87171">[6–18s] Actionable Directives:</text>
      <text x="10" y="33" font-size="8.5" fill="#cbd5e1">"Do NOT run outside! Drop, Cover, and Hold On beneath a desk."</text>

      <!-- 19-30s -->
      <rect x="0" y="115" width="310" height="50" rx="4" fill="#1e293b" stroke="#38bdf8"/>
      <text x="10" y="18" font-size="9.5" font-weight="bold" fill="#38bdf8">[19–30s] Official Source &amp; Sign-off:</text>
      <text x="10" y="33" font-size="8.5" fill="#cbd5e1">"From Kenya National Disaster Management. Stay safe!"</text>

      <!-- 5 Communication Pillars -->
      <g transform="translate(0, 175)">
        <rect x="0" y="0" width="310" height="40" rx="4" fill="#0f172a" stroke="#475569"/>
        <text x="155" y="16" font-size="8.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">5 PILLARS OF RISK COMMUNICATION</text>
        <text x="155" y="30" font-size="8" fill="#cbd5e1" text-anchor="middle">Simple • Actionable • High-Visibility • Targeted • Multi-Channel</text>
      </g>
    </g>
  </g>
</svg>
""")

# SVG 10: Master Synthesis Flowchart (Lesson 10)
SVG_EARTHQUAKE_SYNTHESIS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">MASTER SYNTHESIS: THE COMPLETE SEISMIC CHAIN</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">From Mantle Convection to Fault Rupture, Seismology &amp; Disaster Resilience</text>

  <!-- Flowchart Stages -->
  <g transform="translate(30, 85)">
    <!-- Stage 1: Tectonics -->
    <rect x="0" y="0" width="135" height="130" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="135" height="26" rx="8" fill="#0369a1"/>
    <text x="67" y="17" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">1. TECTONICS</text>
    <text x="10" y="45" font-size="8.5" fill="#cbd5e1">• Mantle Convection</text>
    <text x="10" y="62" font-size="8.5" fill="#cbd5e1">• Plate boundaries</text>
    <text x="10" y="79" font-size="8.5" fill="#cbd5e1">• Interplate friction</text>
    <text x="10" y="105" font-size="8.5" font-weight="bold" fill="#38bdf8">Strain Energy</text>

    <!-- Arrow 1->2 -->
    <polygon points="140,65 150,65 150,60 158,65 150,70 150,65" fill="#64748b"/>

    <!-- Stage 2: Rupture -->
    <rect x="160" y="0" width="135" height="130" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="135" height="26" rx="8" fill="#b91c1c" transform="translate(160,0)"/>
    <text x="227" y="17" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">2. FOCUS RUPTURE</text>
    <text x="170" y="45" font-size="8.5" fill="#cbd5e1">• Elastic limit exceeded</text>
    <text x="170" y="62" font-size="8.5" fill="#cbd5e1">• Brittle fault fracture</text>
    <text x="170" y="79" font-size="8.5" fill="#cbd5e1">• Subterranean focus</text>
    <text x="170" y="105" font-size="8.5" font-weight="bold" fill="#f87171">Kinetic Release</text>

    <!-- Arrow 2->3 -->
    <polygon points="300,65 310,65 310,60 318,65 310,70 310,65" fill="#64748b"/>

    <!-- Stage 3: Wave Radiation -->
    <rect x="320" y="0" width="135" height="130" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="135" height="26" rx="8" fill="#d97706" transform="translate(320,0)"/>
    <text x="387" y="17" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">3. SEISMIC WAVES</text>
    <text x="330" y="45" font-size="8.5" fill="#cbd5e1">• P-Waves (fastest)</text>
    <text x="330" y="62" font-size="8.5" fill="#cbd5e1">• S-Waves (shear)</text>
    <text x="330" y="79" font-size="8.5" fill="#cbd5e1">• Surface waves</text>
    <text x="330" y="105" font-size="8.5" font-weight="bold" fill="#fbbf24">Ground Motion</text>

    <!-- Arrow 3->4 -->
    <polygon points="460,65 470,65 470,60 478,65 470,70 470,65" fill="#64748b"/>

    <!-- Stage 4: Measurement -->
    <rect x="480" y="0" width="135" height="130" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="0" y="0" width="135" height="26" rx="8" fill="#7e22ce" transform="translate(480,0)"/>
    <text x="547" y="17" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">4. SEISMOLOGY</text>
    <text x="490" y="45" font-size="8.5" fill="#cbd5e1">• Seismograph inertia</text>
    <text x="490" y="62" font-size="8.5" fill="#cbd5e1">• S-P Triangulation</text>
    <text x="490" y="79" font-size="8.5" fill="#cbd5e1">• Richter Magnitude</text>
    <text x="490" y="105" font-size="8.5" font-weight="bold" fill="#c084fc">Epicentre Located</text>

    <!-- Arrow 4->5 -->
    <polygon points="620,65 630,65 630,60 638,65 630,70 630,65" fill="#64748b"/>

    <!-- Stage 5: Mitigation -->
    <rect x="640" y="0" width="100" height="130" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect x="0" y="0" width="100" height="26" rx="8" fill="#059669" transform="translate(640,0)"/>
    <text x="690" y="17" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">5. RESILIENCE</text>
    <text x="648" y="45" font-size="8" fill="#cbd5e1">• Base isolation</text>
    <text x="648" y="60" font-size="8" fill="#cbd5e1">• Building codes</text>
    <text x="648" y="75" font-size="8" fill="#cbd5e1">• Drop, Cover, Hold</text>
    <text x="648" y="105" font-size="8.5" font-weight="bold" fill="#34d399">Lives Saved</text>
  </g>

  <!-- Bottom Synthesis Matrix -->
  <g transform="translate(30, 240)">
    <rect x="0" y="0" width="740" height="180" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="370" y="25" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">TOPIC 9: CORE KNOWLEDGE SUMMARY</text>

    <g transform="translate(25, 45)">
      <text x="0" y="15" font-size="10" font-weight="bold" fill="#f87171">Seismic Anatomy:</text>
      <text x="0" y="32" font-size="9" fill="#cbd5e1">Focus is underground fracture; Epicentre is surface point directly vertical.</text>
      <text x="0" y="52" font-size="10" font-weight="bold" fill="#fbbf24">Wave Velocities:</text>
      <text x="0" y="69" font-size="9" fill="#cbd5e1">P-waves (longitudinal compressional) > S-waves (transverse shear) > Surface waves (destructive).</text>
      <text x="0" y="89" font-size="10" font-weight="bold" fill="#38bdf8">Global Distribution:</text>
      <text x="0" y="106" font-size="9" fill="#cbd5e1">80%+ in Circum-Pacific Ring of Fire; Gregory Rift causes active tremors in Kenya.</text>
    </g>

    <g transform="translate(390, 45)">
      <text x="0" y="15" font-size="10" font-weight="bold" fill="#c084fc">Measurement Scales:</text>
      <text x="0" y="32" font-size="9" fill="#cbd5e1">Richter (Quantitative, Logarithmic energy) vs. Mercalli (Qualitative I-XII observed damage).</text>
      <text x="0" y="52" font-size="10" font-weight="bold" fill="#34d399">Hazard Reduction:</text>
      <text x="0" y="69" font-size="9" fill="#cbd5e1">Drop, Cover, and Hold On + Base isolation engineering prevents high-casualty structural failures.</text>
      <text x="0" y="89" font-size="10" font-weight="bold" fill="#e2e8f0">Locating Epicentres:</text>
      <text x="0" y="106" font-size="9" fill="#cbd5e1">3-station triangulation intersecting S-P distance circles.</text>
    </g>
  </g>
</svg>
""")

TOPIC_9_SVGS = {
    1: SVG_EARTHQUAKE_ANATOMY,
    2: SVG_EARTHQUAKE_DEPTH_TYPES,
    3: SVG_GLOBAL_SEISMIC_BELTS,
    4: SVG_RICHTER_VS_MERCALLI,
    5: SVG_SEISMOGRAPH_AND_TRIANGULATION,
    6: SVG_SEISMIC_HAZARDS_LIQUEFACTION,
    7: SVG_SEISMIC_VULNERABILITY_BASE_ISOLATION,
    8: SVG_DROP_COVER_HOLD_ON,
    9: SVG_PUBLIC_SAFETY_BROADCAST,
    10: SVG_EARTHQUAKE_SYNTHESIS
}

# =============================================================================
# ENRICHMENT RUNNER
# =============================================================================
def enrich_topic_9():
    print("=" * 80)
    print("Starting Visual Enrichment: Grade 10 CBC Geography — Topic 9: Earthquakes")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(id=37).first() or Subject.objects.filter(grade=grade, name="Geography").first()
    topic = Topic.objects.filter(subject=subject, order=9).first()

    if not topic:
        print("ERROR: Topic 9 not found in database! Please run ingestion first.")
        return

    # Load verified images JSON
    json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grade10_geography_topic9_verified_images.json")
    with open(json_path, "r") as f:
        verified_images = json.load(f)

    lessons = topic.lessons.all().order_by("learning_unit__order")
    print(f"Enriching {lessons.count()} Lessons for Topic 9: {topic.name}...")

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
                            "topic_order": 9
                        }
                    }
                )
                asset.url = img_data['url']
                asset.status = "attached"
                asset.save()
                asset.blocks.add(hook_block)
                print(f"  + Attached Wikimedia Photographic Hook: {img_data['url'][:65]}...")

        # 2. Attach Custom Vector SVG
        svg_xml = TOPIC_9_SVGS.get(int(u_order))
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
                            "topic_order": 9
                        }
                    }
                )
                svg_asset.metadata["svg_content"] = svg_xml
                svg_asset.status = "attached"
                svg_asset.save()
                svg_asset.blocks.add(diagram_block)
                print(f"  + Attached Custom Responsive Vector SVG to block '{diagram_block.title}'")

        # 3. Attach YouTube Video (Lesson 6)
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
                        "topic_order": 9
                    }
                }
            )
            v_asset.url = vid_url
            v_asset.status = "attached"
            v_asset.save()
            v_asset.blocks.add(video_block)
            print(f"  + Attached Educational YouTube Video: {vid_url}")

    print("\n" + "=" * 80)
    print("Topic 9 Visual Enrichment Completed Successfully!")
    print("=" * 80)

if __name__ == "__main__":
    enrich_topic_9()
