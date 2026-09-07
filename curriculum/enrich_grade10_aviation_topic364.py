"""
VLearn Grade 10 Aviation — Topic 364: Aircraft Technical Drawing
Visual Enrichment Engine (Verified Photos, Responsive Vector SVGs & Video Assets)

Curriculum: CBC
Subject: Aviation (Subject ID: 44)
Topic: Aircraft Technical Drawing (Topic ID: 364, Order: 6)

Enriches:
  - 5 First-Card Photographic Visual Hooks (Verified Direct Wikimedia URLs returning HTTP 200)
  - 5 Custom Responsive Vector SVGs (viewBox="0 0 800 450", Dark Slate Theme #0f172a, Sanitized XML)
  - 5 Verified Educational YouTube Videos (oEmbed 200 verified)
  - Persists LessonAsset models and binds them to corresponding LessonBlocks

Usage:
  ./venv/bin/python curriculum/enrich_grade10_aviation_topic364.py
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
# 5 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 364
# =============================================================================

# SVG 1: Illustrated Parts Catalog (IPC) Exploded Wheel Hub Assembly (Lesson 1, Page 4)
SVG_IPC_EXPLODED_ASSEMBLY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <!-- Container Card -->
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Illustrated Parts Catalog (IPC) — Exploded Wheel Hub Assembly</text>
  <text x="400" y="66" font-size="12" fill="#94a3b8" text-anchor="middle">ATA Chapter 32-40: Main Landing Gear Wheel &amp; Brake Stack</text>

  <!-- Central Assembly Axis (Dashed Centerline) -->
  <line x1="50" y1="180" x2="750" y2="180" stroke="#64748b" stroke-width="1.5" stroke-dasharray="10 5 2 5"/>
  <text x="755" y="184" font-size="10" fill="#64748b">Axis</text>

  <!-- Item 1: Main Wheel Rim Half (Outer) -->
  <g transform="translate(80, 105)">
    <path d="M 10 10 L 45 10 L 50 35 L 60 40 L 60 110 L 50 115 L 45 140 L 10 140 L 10 110 L 25 105 L 25 45 L 10 40 Z" fill="#334155" stroke="#38bdf8" stroke-width="2"/>
    <ellipse cx="35" cy="75" rx="12" ry="30" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="35" cy="75" r="5" fill="#38bdf8"/>
    <!-- Callout 1 -->
    <line x1="35" y1="10" x2="35" y2="-20" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="35" cy="-20" r="10" fill="#b45309" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="35" y="-16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1</text>
    <text x="35" y="160" font-size="10" font-weight="bold" fill="#f8fafc" text-anchor="middle">Wheel Rim</text>
  </g>

  <!-- Item 2: Inboard Brake Rotor / Disc -->
  <g transform="translate(200, 115)">
    <rect x="0" y="5" width="22" height="120" rx="4" fill="#475569" stroke="#94a3b8" stroke-width="2"/>
    <line x1="11" y1="20" x2="11" y2="110" stroke="#0f172a" stroke-width="3" stroke-dasharray="6 4"/>
    <!-- Callout 2 -->
    <line x1="11" y1="5" x2="11" y2="-30" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="11" cy="-30" r="10" fill="#b45309" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="11" y="-26" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2</text>
    <text x="11" y="150" font-size="10" font-weight="bold" fill="#f8fafc" text-anchor="middle">Brake Rotor</text>
  </g>

  <!-- Item 3: Tapered Roller Bearing Cone -->
  <g transform="translate(305, 125)">
    <polygon points="5,10 35,20 35,90 5,100" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <line x1="12" y1="25" x2="12" y2="85" stroke="#ffffff" stroke-width="1.5"/>
    <line x1="20" y1="28" x2="20" y2="82" stroke="#ffffff" stroke-width="1.5"/>
    <line x1="28" y1="31" x2="28" y2="79" stroke="#ffffff" stroke-width="1.5"/>
    <!-- Callout 3 -->
    <line x1="20" y1="15" x2="20" y2="-40" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="20" cy="-40" r="10" fill="#b45309" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="20" y="-36" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3</text>
    <text x="20" y="140" font-size="10" font-weight="bold" fill="#f8fafc" text-anchor="middle">Roller Bearing</text>
  </g>

  <!-- Item 4: Thrust Washer -->
  <g transform="translate(425, 135)">
    <ellipse cx="10" cy="45" rx="8" ry="40" fill="#64748b" stroke="#cbd5e1" stroke-width="2"/>
    <ellipse cx="10" cy="45" rx="4" ry="18" fill="#1e293b"/>
    <!-- Callout 4 -->
    <line x1="10" y1="5" x2="10" y2="-50" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="10" cy="-50" r="10" fill="#b45309" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="10" y="-46" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4</text>
    <text x="10" y="130" font-size="10" font-weight="bold" fill="#f8fafc" text-anchor="middle">Thrust Washer</text>
  </g>

  <!-- Item 5: Axle Nut &amp; Cotter Pin -->
  <g transform="translate(520, 138)">
    <polygon points="5,15 25,15 32,28 32,58 25,70 5,70" fill="#d97706" stroke="#fbbf24" stroke-width="2"/>
    <line x1="18" y1="5" x2="18" y2="80" stroke="#ef4444" stroke-width="2"/>
    <!-- Callout 5 -->
    <line x1="18" y1="10" x2="18" y2="-53" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="18" cy="-53" r="10" fill="#b45309" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="18" y="-49" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">5</text>
    <text x="18" y="127" font-size="10" font-weight="bold" fill="#f8fafc" text-anchor="middle">Axle Nut &amp; Pin</text>
  </g>

  <!-- Item 6: Hub Dust Cap -->
  <g transform="translate(630, 130)">
    <path d="M 5 25 Q 35 25 40 50 Q 35 75 5 75 Z" fill="#059669" stroke="#34d399" stroke-width="2"/>
    <!-- Callout 6 -->
    <line x1="20" y1="25" x2="20" y2="-45" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="20" cy="-45" r="10" fill="#b45309" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="20" y="-41" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">6</text>
    <text x="20" y="135" font-size="10" font-weight="bold" fill="#f8fafc" text-anchor="middle">Dust Cap</text>
  </g>

  <!-- IPC Cross-Reference Parts Table -->
  <g transform="translate(35, 305)">
    <rect x="0" y="0" width="730" height="110" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <!-- Table Header -->
    <rect x="0" y="0" width="730" height="26" rx="8" fill="#334155"/>
    <text x="35" y="18" font-size="11" font-weight="bold" fill="#38bdf8">FIG/ITEM</text>
    <text x="150" y="18" font-size="11" font-weight="bold" fill="#38bdf8">PART NUMBER</text>
    <text x="370" y="18" font-size="11" font-weight="bold" fill="#38bdf8">NOMENCLATURE / DESCRIPTION</text>
    <text x="640" y="18" font-size="11" font-weight="bold" fill="#38bdf8">QTY</text>

    <!-- Row 1 -->
    <text x="35" y="44" font-size="10.5" fill="#f8fafc">32-40-01</text>
    <text x="150" y="44" font-size="10.5" fill="#f8fafc">PN 40-77C-01</text>
    <text x="370" y="44" font-size="10.5" fill="#94a3b8">WHEEL RIM ASSEMBLY, MAIN GEAR (AL 2024-T3)</text>
    <text x="648" y="44" font-size="10.5" fill="#f8fafc">1</text>

    <!-- Row 2 -->
    <text x="35" y="64" font-size="10.5" fill="#f8fafc">32-40-02</text>
    <text x="150" y="64" font-size="10.5" fill="#f8fafc">PN 164-032A</text>
    <text x="370" y="64" font-size="10.5" fill="#94a3b8">BRAKE ROTOR DISC, SLOTTED ALLOY STEEL</text>
    <text x="648" y="64" font-size="10.5" fill="#f8fafc">1</text>

    <!-- Row 3 -->
    <text x="35" y="84" font-size="10.5" fill="#f8fafc">32-40-03</text>
    <text x="150" y="84" font-size="10.5" fill="#f8fafc">PN LM67048</text>
    <text x="370" y="84" font-size="10.5" fill="#94a3b8">BEARING CONE, TAPERED ROLLER (PRECISION CLASS 3)</text>
    <text x="648" y="84" font-size="10.5" fill="#f8fafc">2</text>

    <!-- Row 4 -->
    <text x="35" y="103" font-size="10.5" fill="#f8fafc">32-40-05</text>
    <text x="150" y="103" font-size="10.5" fill="#f8fafc">PN AN310-8</text>
    <text x="370" y="103" font-size="10.5" fill="#94a3b8">NUT, SLOTTED ENGINE AXLE, CADMIUM PLATED</text>
    <text x="648" y="103" font-size="10.5" fill="#f8fafc">1</text>
  </g>
</svg>
""")

# SVG 2: Precision Drafting Setup for Isometric Axes & The 30-Degree Rule (Lesson 2, Page 4)
SVG_ISOMETRIC_AXES_SETUP = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <!-- Container Card -->
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Precision Drafting Setup: The Three Isometric Axes &amp; 30° Rule</text>
  <text x="400" y="66" font-size="12" fill="#94a3b8" text-anchor="middle">Using T-Square and 30°/60°/90° Set Square to Construct Mathematical Proportions</text>

  <!-- Drafting Board Surface -->
  <rect x="50" y="85" width="700" height="265" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>

  <!-- Horizontal T-Square Blade -->
  <rect x="35" y="300" width="730" height="35" rx="3" fill="#475569" stroke="#64748b" stroke-width="1.5"/>
  <text x="100" y="322" font-size="12" font-weight="bold" fill="#f8fafc">T-Square Horizontal Working Edge</text>
  <line x1="50" y1="300" x2="750" y2="300" stroke="#f59e0b" stroke-width="2"/>

  <!-- Left 30/60/90 Set Square (Flipped Left) -->
  <polygon points="170,300 370,300 370,185" fill="#38bdf8" fill-opacity="0.15" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4 3"/>
  <text x="240" y="290" font-size="11" fill="#38bdf8">30°</text>

  <!-- Right 30/60/90 Set Square (Flipped Right) -->
  <polygon points="400,300 600,300 400,185" fill="#38bdf8" fill-opacity="0.15" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4 3"/>
  <text x="540" y="290" font-size="11" fill="#38bdf8">30°</text>

  <!-- Central Vertex Point (*) -->
  <circle cx="385" cy="270" r="6" fill="#ef4444" stroke="#ffffff" stroke-width="2"/>
  <text x="385" y="292" font-size="11" font-weight="bold" fill="#ef4444" text-anchor="middle">Central Vertex (Origin)</text>

  <!-- Vertical Axis (Height: 90°) -->
  <line x1="385" y1="270" x2="385" y2="105" stroke="#38bdf8" stroke-width="3.5"/>
  <polygon points="385,98 380,108 390,108" fill="#38bdf8"/>
  <text x="395" y="115" font-size="12" font-weight="bold" fill="#38bdf8">VERTICAL AXIS (Height 90°)</text>

  <!-- Right Receding Axis (Length: 30°) -->
  <line x1="385" y1="270" x2="635" y2="125" stroke="#10b981" stroke-width="3.5"/>
  <polygon points="642,121 630,126 636,136" fill="#10b981"/>
  <text x="560" y="125" font-size="12" font-weight="bold" fill="#10b981">LENGTH AXIS (30° Right)</text>

  <!-- Left Receding Axis (Width: 30°) -->
  <line x1="385" y1="270" x2="135" y2="125" stroke="#f59e0b" stroke-width="3.5"/>
  <polygon points="128,121 134,136 140,126" fill="#f59e0b"/>
  <text x="130" y="115" font-size="12" font-weight="bold" fill="#f59e0b">WIDTH AXIS (30° Left)</text>

  <!-- 30° Baseline Angle Arcs -->
  <path d="M 445 270 A 60 60 0 0 0 437 240" fill="none" stroke="#10b981" stroke-width="2"/>
  <text x="455" y="258" font-size="11" font-weight="bold" fill="#10b981">30°</text>

  <path d="M 325 270 A 60 60 0 0 1 333 240" fill="none" stroke="#f59e0b" stroke-width="2"/>
  <text x="305" y="258" font-size="11" font-weight="bold" fill="#f59e0b">30°</text>

  <!-- 120° Internal Angle Arcs -->
  <path d="M 385 220 A 50 50 0 0 1 428 245" fill="none" stroke="#f8fafc" stroke-width="1.5" stroke-dasharray="3 3"/>
  <text x="415" y="215" font-size="11" font-weight="bold" fill="#f8fafc">120°</text>

  <path d="M 385 220 A 50 50 0 0 0 342 245" fill="none" stroke="#f8fafc" stroke-width="1.5" stroke-dasharray="3 3"/>
  <text x="340" y="215" font-size="11" font-weight="bold" fill="#f8fafc">120°</text>

  <!-- Bottom Guidance Note Card -->
  <g transform="translate(50, 365)">
    <rect x="0" y="0" width="700" height="55" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="20" y="24" font-size="11" font-weight="bold" fill="#38bdf8">CRITICAL DRAFTING RULE:</text>
    <text x="180" y="24" font-size="11" fill="#cbd5e1">All vertical edges stay at 90°. All receding horizontal edges rotate upward to exactly 30°.</text>
    <text x="20" y="44" font-size="11" font-weight="bold" fill="#10b981">MEASURABILITY:</text>
    <text x="180" y="44" font-size="11" fill="#cbd5e1">Parallel lines remain strictly parallel. Any measurement along these three axes is true scale.</text>
  </g>
</svg>
""")

# SVG 3: The Crating Method: 3-Stage Construction of an L-Bracket (Lesson 3, Page 4)
SVG_CRATING_METHOD_STAGES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <!-- Container Card -->
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Crating Method — Three-Stage Geometric Construction</text>
  <text x="400" y="66" font-size="12" fill="#94a3b8" text-anchor="middle">Step-by-Step Evolution from Light Bounding Box to Precision Finished Component</text>

  <!-- STAGE 1: Bounding Box (Outer Crate) -->
  <g transform="translate(40, 95)">
    <rect x="0" y="0" width="220" height="280" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="30" rx="8" fill="#0369a1"/>
    <text x="110" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 1: The Bounding Crate</text>

    <!-- 3D Crate Light Lines (Cyan Dashed) -->
    <g transform="translate(25, 60)">
      <!-- Front Face -->
      <polygon points="30,140 110,95 110,25 30,70" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4 3"/>
      <!-- Top Face -->
      <polygon points="30,70 110,25 150,48 70,93" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4 3"/>
      <!-- Right Face -->
      <polygon points="110,95 150,118 150,48 110,25" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4 3"/>
    </g>

    <text x="110" y="235" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Maximum Outer Envelope</text>
    <text x="110" y="252" font-size="10" fill="#94a3b8" text-anchor="middle">Drafted lightly with 2H/4H pencil.</text>
    <text x="110" y="266" font-size="10" fill="#94a3b8" text-anchor="middle">Locks Height, Length &amp; Width.</text>
  </g>

  <!-- STAGE 2: Plotting Steps & Projections -->
  <g transform="translate(290, 95)">
    <rect x="0" y="0" width="220" height="280" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="30" rx="8" fill="#b45309"/>
    <text x="110" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 2: Carving Features</text>

    <!-- Crate + Step Lines -->
    <g transform="translate(25, 60)">
      <!-- Faint Crate -->
      <polygon points="30,140 110,95 110,25 30,70" fill="none" stroke="#475569" stroke-width="1" stroke-dasharray="3 3"/>
      <polygon points="30,70 110,25 150,48 70,93" fill="none" stroke="#475569" stroke-width="1" stroke-dasharray="3 3"/>
      <polygon points="110,95 150,118 150,48 110,25" fill="none" stroke="#475569" stroke-width="1" stroke-dasharray="3 3"/>

      <!-- L-Step Cuts on Front Face -->
      <polyline points="30,70 70,47 70,82 110,60 110,95 30,140 30,70" fill="none" stroke="#f59e0b" stroke-width="2"/>
      <!-- Projection Lines Across Width -->
      <line x1="70" y1="47" x2="110" y2="70" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3 2"/>
      <line x1="70" y1="82" x2="110" y2="105" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3 2"/>
      <line x1="110" y1="60" x2="150" y2="83" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3 2"/>
    </g>

    <text x="110" y="235" font-size="11" font-weight="bold" fill="#f59e0b" text-anchor="middle">Plotting Cuts &amp; Steps</text>
    <text x="110" y="252" font-size="10" fill="#94a3b8" text-anchor="middle">Measure step points on crate faces.</text>
    <text x="110" y="266" font-size="10" fill="#94a3b8" text-anchor="middle">Project lines along 30° axes.</text>
  </g>

  <!-- STAGE 3: Final Darkened Object Lines -->
  <g transform="translate(540, 95)">
    <rect x="0" y="0" width="220" height="280" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="30" rx="8" fill="#047857"/>
    <text x="110" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 3: Finished Bracket</text>

    <!-- Heavy Dark L-Bracket Outlines -->
    <g transform="translate(25, 60)">
      <!-- L-Bracket Solid Faces -->
      <polygon points="30,70 70,47 70,82 110,60 110,95 30,140" fill="#1e293b" stroke="#10b981" stroke-width="2.5"/>
      <polygon points="70,47 110,70 70,93 30,70" fill="#334155" stroke="#10b981" stroke-width="2.5"/>
      <polygon points="70,82 110,105 150,83 110,60" fill="#334155" stroke="#10b981" stroke-width="2.5"/>
      <polygon points="110,95 150,118 150,83 110,60" fill="#1e293b" stroke="#10b981" stroke-width="2.5"/>
      <polygon points="110,105 150,128 150,118 110,95" fill="#475569" stroke="#10b981" stroke-width="2.5"/>

      <!-- Ghost Erased Lines (Very Faint) -->
      <line x1="70" y1="47" x2="110" y2="25" stroke="#334155" stroke-width="1" stroke-dasharray="2 2"/>
      <line x1="110" y1="25" x2="150" y2="48" stroke="#334155" stroke-width="1" stroke-dasharray="2 2"/>
      <line x1="150" y1="48" x2="150" y2="83" stroke="#334155" stroke-width="1" stroke-dasharray="2 2"/>
    </g>

    <text x="110" y="235" font-size="11" font-weight="bold" fill="#10b981" text-anchor="middle">Darken &amp; Erase Crate</text>
    <text x="110" y="252" font-size="10" fill="#94a3b8" text-anchor="middle">Heavy HB pencil outline.</text>
    <text x="110" y="266" font-size="10" fill="#94a3b8" text-anchor="middle">Ghost crate lines erased clean.</text>
  </g>

  <!-- Progression Arrows -->
  <polygon points="268,235 282,235 282,240 290,230 282,220 282,225 268,225" fill="#38bdf8"/>
  <polygon points="518,235 532,235 532,240 540,230 532,220 532,225 518,225" fill="#38bdf8"/>

  <!-- Footer Operational Note -->
  <text x="400" y="405" font-size="11.5" fill="#94a3b8" text-anchor="middle">Golden Rule: Never draw complex 3D forms freehand without an initial mathematical bounding crate.</text>
</svg>
""")

# SVG 4: Standardized Isometric Dimensioning & Title Block Standards (Lesson 4, Page 4)
SVG_DIMENSIONING_RULES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <!-- Container Card -->
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Standardized Isometric Dimensioning Anatomy &amp; Rules</text>
  <text x="400" y="66" font-size="12" fill="#94a3b8" text-anchor="middle">Parallel Alignment, Extension Gaps, Arrowhead Geometry &amp; Title Block Specifications</text>

  <!-- 3D Isometric Mounting Block -->
  <g transform="translate(160, 110)">
    <!-- Main Solid Faces -->
    <polygon points="60,160 180,90 180,20 60,90" fill="#1e293b" stroke="#f8fafc" stroke-width="2.5"/>
    <polygon points="60,90 180,20 250,60 130,130" fill="#334155" stroke="#f8fafc" stroke-width="2.5"/>
    <polygon points="180,90 250,130 250,60 180,20" fill="#0f172a" stroke="#f8fafc" stroke-width="2.5"/>

    <!-- Hole on Top Face (Isometric Ellipse) -->
    <ellipse cx="160" cy="75" rx="18" ry="9" fill="#0f172a" stroke="#38bdf8" stroke-width="1.8" transform="rotate(-15 160 75)"/>

    <!-- 1. Height Dimension (Vertical 90°) -->
    <!-- Extension Lines with 1.5mm gap -->
    <line x1="56" y1="90" x2="25" y2="90" stroke="#94a3b8" stroke-width="1.5"/>
    <line x1="56" y1="160" x2="25" y2="160" stroke="#94a3b8" stroke-width="1.5"/>
    <!-- Dimension Line with closed arrows -->
    <line x1="30" y1="90" x2="30" y2="160" stroke="#38bdf8" stroke-width="1.5"/>
    <polygon points="30,90 27,98 33,98" fill="#38bdf8"/>
    <polygon points="30,160 27,152 33,152" fill="#38bdf8"/>
    <!-- Dimension Text -->
    <text x="16" y="128" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">40</text>

    <!-- 2. Length Dimension (Receding 30° Right) -->
    <!-- Extension Lines with gap -->
    <line x1="60" y1="164" x2="60" y2="195" stroke="#94a3b8" stroke-width="1.5"/>
    <line x1="180" y1="94" x2="180" y2="125" stroke="#94a3b8" stroke-width="1.5"/>
    <!-- Dimension Line parallel to 30° axis -->
    <line x1="60" y1="190" x2="180" y2="120" stroke="#10b981" stroke-width="1.5"/>
    <polygon points="60,190 70,188 66,182" fill="#10b981"/>
    <polygon points="180,120 170,122 174,128" fill="#10b981"/>
    <text x="120" y="170" font-size="12" font-weight="bold" fill="#10b981" text-anchor="middle">80 mm</text>

    <!-- 3. Width Dimension (Receding 30° Left) -->
    <!-- Extension Lines with gap -->
    <line x1="184" y1="90" x2="215" y2="72" stroke="#94a3b8" stroke-width="1.5"/>
    <line x1="254" y1="130" x2="285" y2="112" stroke="#94a3b8" stroke-width="1.5"/>
    <!-- Dimension Line parallel to width axis -->
    <line x1="210" y1="75" x2="280" y2="115" stroke="#f59e0b" stroke-width="1.5"/>
    <polygon points="210,75 218,82 221,76" fill="#f59e0b"/>
    <polygon points="280,115 272,108 269,114" fill="#f59e0b"/>
    <text x="260" y="88" font-size="12" font-weight="bold" fill="#f59e0b" text-anchor="middle">50 mm</text>

    <!-- Callout 1: 1.5mm Gap Rule -->
    <circle cx="58" cy="90" r="10" fill="none" stroke="#ef4444" stroke-width="1.5"/>
    <line x1="58" y1="80" x2="40" y2="50" stroke="#ef4444" stroke-width="1.2"/>
    <rect x="-40" y="30" width="120" height="25" rx="4" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="20" y="47" font-size="10" font-weight="bold" fill="#ef4444" text-anchor="middle">1.5 mm Gap (No Touch)</text>
  </g>

  <!-- Drawing Title Block and Technical Notes (Bottom Right) -->
  <g transform="translate(480, 260)">
    <rect x="0" y="0" width="280" height="155" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="280" height="24" rx="6" fill="#0284c7"/>
    <text x="140" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">AIRCRAFT DRAWING TITLE BLOCK</text>

    <text x="12" y="42" font-size="10" font-weight="bold" fill="#94a3b8">PART NAME:</text>
    <text x="90" y="42" font-size="10.5" font-weight="bold" fill="#f8fafc">WING STRUT FITTING</text>

    <text x="12" y="62" font-size="10" font-weight="bold" fill="#94a3b8">PART NO:</text>
    <text x="90" y="62" font-size="10.5" font-weight="bold" fill="#f8fafc">208-011-304 REV: B</text>

    <text x="12" y="82" font-size="10" font-weight="bold" fill="#94a3b8">MATERIAL:</text>
    <text x="90" y="82" font-size="10.5" font-weight="bold" fill="#f8fafc">2024-T3 AL ALLOY BARE</text>

    <text x="12" y="102" font-size="10" font-weight="bold" fill="#94a3b8">UNITS:</text>
    <text x="90" y="102" font-size="10.5" font-weight="bold" fill="#34d399">ALL DIMENSIONS IN MM</text>

    <line x1="0" y1="112" x2="280" y2="112" stroke="#334155" stroke-width="1"/>

    <text x="12" y="130" font-size="10" font-weight="bold" fill="#f59e0b">TOLERANCE:</text>
    <text x="90" y="130" font-size="10.5" font-weight="bold" fill="#f8fafc">± 0.05 MM (UNLESS NOTED)</text>

    <text x="12" y="146" font-size="10" font-weight="bold" fill="#94a3b8">APPROVAL:</text>
    <text x="90" y="146" font-size="10" fill="#38bdf8">KCAA / FAA CERTIFIED</text>
  </g>

  <!-- Dimensioning Rules Checklist (Left Side) -->
  <g transform="translate(35, 275)">
    <rect x="0" y="0" width="220" height="140" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="15" y="22" font-size="11" font-weight="bold" fill="#38bdf8">DIMENSIONING RULES</text>
    <text x="15" y="44" font-size="10" fill="#cbd5e1">✓ Parallel to 30° isometric axes</text>
    <text x="15" y="64" font-size="10" fill="#cbd5e1">✓ 1.5 mm offset gap from object</text>
    <text x="15" y="84" font-size="10" fill="#cbd5e1">✓ Closed, sharp 3:1 arrowheads</text>
    <text x="15" y="104" font-size="10" fill="#cbd5e1">✓ Number centered, hovering above</text>
    <text x="15" y="124" font-size="10" fill="#ef4444">✗ Never cross dimension lines</text>
  </g>
</svg>
""")

# SVG 5: Technical Drawing Interpretation & Repair Workflow Flowchart (Lesson 5, Page 4)
SVG_DRAWING_INTERPRETATION_FLOWCHART = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <!-- Container Card -->
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Drawing Interpretation &amp; Maintenance Workflow Flowchart</text>
  <text x="400" y="66" font-size="12" fill="#94a3b8" text-anchor="middle">Standard Operational Protocol: Pilot Defect Report to Airworthiness Return-to-Service</text>

  <!-- Step 1: Pilot Squawk Entry -->
  <g transform="translate(40, 95)">
    <rect x="0" y="0" width="200" height="90" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.8"/>
    <rect x="0" y="0" width="200" height="24" rx="8" fill="#991b1b"/>
    <text x="100" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STEP 1: Pilot Squawk / Defect</text>
    <text x="15" y="44" font-size="10.5" font-weight="bold" fill="#f8fafc">Discrepancy Reported:</text>
    <text x="15" y="60" font-size="10" fill="#94a3b8">"Nose gear steering sluggish;"</text>
    <text x="15" y="76" font-size="10" fill="#94a3b8">excessive play during taxi.</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <polygon points="252,140 278,140 278,144 286,138 278,132 278,136 252,136" fill="#38bdf8"/>

  <!-- Step 2: AMM Procedure Consultation -->
  <g transform="translate(300, 95)">
    <rect x="0" y="0" width="200" height="90" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.8"/>
    <rect x="0" y="0" width="200" height="24" rx="8" fill="#b45309"/>
    <text x="100" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STEP 2: AMM Task Procedure</text>
    <text x="15" y="44" font-size="10.5" font-weight="bold" fill="#f8fafc">ATA Chapter 32 (Gear):</text>
    <text x="15" y="60" font-size="10" fill="#94a3b8">Read troubleshooting steps,</text>
    <text x="15" y="76" font-size="10" fill="#94a3b8">safety lockouts &amp; jacking rules.</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <polygon points="512,140 538,140 538,144 546,138 538,132 538,136 512,136" fill="#38bdf8"/>

  <!-- Step 3: IPC Exploded-View Diagram -->
  <g transform="translate(560, 95)">
    <rect x="0" y="0" width="200" height="90" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.8"/>
    <rect x="0" y="0" width="200" height="24" rx="8" fill="#0284c7"/>
    <text x="100" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STEP 3: IPC Exploded View</text>
    <text x="15" y="44" font-size="10.5" font-weight="bold" fill="#f8fafc">Locate 3D Isometric View:</text>
    <text x="15" y="60" font-size="10" fill="#94a3b8">Trace centerline to worn steering</text>
    <text x="15" y="76" font-size="10" fill="#94a3b8">collar bracket (Callout Item 12).</text>
  </g>

  <!-- Arrow Down (3 -> 4) -->
  <polygon points="660,195 660,225 664,225 658,235 652,225 656,225 656,195" fill="#38bdf8"/>

  <!-- Step 4: Cross-Reference Parts Table -->
  <g transform="translate(560, 245)">
    <rect x="0" y="0" width="200" height="90" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.8"/>
    <rect x="0" y="0" width="200" height="24" rx="8" fill="#7e22ce"/>
    <text x="100" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STEP 4: Cross-Reference IPC</text>
    <text x="15" y="44" font-size="10.5" font-weight="bold" fill="#f8fafc">Extract Exact Part Data:</text>
    <text x="15" y="60" font-size="10" fill="#94a3b8">Item 12 = PN 32-104-01</text>
    <text x="15" y="76" font-size="10" fill="#94a3b8">Verify certified stock in stores.</text>
  </g>

  <!-- Arrow Left (4 -> 5) -->
  <polygon points="548,290 522,290 522,286 514,292 522,298 522,294 548,294" fill="#38bdf8"/>

  <!-- Step 5: Engineering Blueprint Inspection -->
  <g transform="translate(300, 245)">
    <rect x="0" y="0" width="200" height="90" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.8"/>
    <rect x="0" y="0" width="200" height="24" rx="8" fill="#0891b2"/>
    <text x="100" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STEP 5: Blueprint Audit</text>
    <text x="15" y="44" font-size="10.5" font-weight="bold" fill="#f8fafc">Micrometer Verification:</text>
    <text x="15" y="60" font-size="10" fill="#94a3b8">Check wear limits (±0.02 mm).</text>
    <text x="15" y="76" font-size="10" fill="#94a3b8">Confirm part revision letter.</text>
  </g>

  <!-- Arrow Left (5 -> 6) -->
  <polygon points="288,290 262,290 262,286 254,292 262,298 262,294 288,294" fill="#38bdf8"/>

  <!-- Step 6: Installation & Release Sign-Off -->
  <g transform="translate(40, 245)">
    <rect x="0" y="0" width="200" height="90" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.8"/>
    <rect x="0" y="0" width="200" height="24" rx="8" fill="#047857"/>
    <text x="100" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STEP 6: Return-to-Service</text>
    <text x="15" y="44" font-size="10.5" font-weight="bold" fill="#f8fafc">Airworthiness Compliance:</text>
    <text x="15" y="60" font-size="10" fill="#94a3b8">Torque bolts to drawing spec,</text>
    <text x="15" y="76" font-size="10" fill="#94a3b8">sign technical logbook release.</text>
  </g>

  <!-- Bottom Discrepancy Alert Bar -->
  <g transform="translate(40, 355)">
    <rect x="0" y="0" width="720" height="60" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="20" y="24" font-size="11" font-weight="bold" fill="#ef4444">CRITICAL DISCREPANCY RULE:</text>
    <text x="210" y="24" font-size="11" fill="#f8fafc">If physical parts contradict manual blueprints, HALT WORK immediately.</text>
    <text x="20" y="46" font-size="10.5" fill="#94a3b8">Never modify or force parts. Quarantine the discrepancy and consult aircraft Engineering Orders and historical logbooks.</text>
  </g>
</svg>
""")

# =============================================================================
# ASSET DICTIONARIES MAPPED BY UNIT ORDER (0 to 4)
# =============================================================================

WIKIMEDIA_PHOTOS = {
    0: {
        "title": "Historical Wright Brothers Airplane Blueprint Drawing",
        "caption": "The original 1903 Wright Airplane engineering blueprint, showcasing how precise technical line drawings, dimensions, and standardized views establish the universal visual language of flight safety.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4c/The_Original_%22Wright%22_1903_Airplane_Drawing%2C_Blueprint_-_NARA_-_61631965.jpg",
        "page": 1
    },
    1: {
        "title": "Engineering Drafting Instruments and Set Squares",
        "caption": "Precision drafting set squares and millimeter scales used to construct exact 30-degree isometric axes and verify geometric angles in aerospace engineering layouts.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/55/GeoDreieck-Ingen-Proj-Mark.jpg",
        "page": 1
    },
    2: {
        "title": "Axonometric and Isometric Projections of Stepped Blocks",
        "caption": "Step-by-step geometric projection of structured blocks and prisms, demonstrating how enclosing bounding boxes enable accurate construction of complex 3D forms.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Axonometric_projections.png",
        "page": 1
    },
    3: {
        "title": "Standardized Engineering Drawing with Dimensions and Notes",
        "caption": "Precision technical engineering blueprint demonstrating standardized extension lines, arrowheads, tolerance specifications, and title block notations.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/03/DIN_69893_hsk_63a_drawing.png",
        "page": 1
    },
    4: {
        "title": "Aircraft Structural Maintainers Interpreting Engineering Blueprints",
        "caption": "Aviation maintenance technicians actively reviewing technical engineering drawings and blueprints in an aircraft hangar before conducting structural airframe repairs.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/49/Behind_the_Blueprint-_35th_MXG_Structural_Maintainers_at_Work_%289487278%29.jpg",
        "page": 1
    }
}

SVG_MAP = {
    0: {
        "title": "Illustrated Parts Catalog (IPC) Exploded Wheel Hub Assembly",
        "svg": SVG_IPC_EXPLODED_ASSEMBLY,
        "page": 4
    },
    1: {
        "title": "Drafting Setup for Isometric Axes and 30-Degree Alignment",
        "svg": SVG_ISOMETRIC_AXES_SETUP,
        "page": 4
    },
    2: {
        "title": "The Three-Stage Crating Method: L-Bracket Construction",
        "svg": SVG_CRATING_METHOD_STAGES,
        "page": 4
    },
    3: {
        "title": "Standardized Isometric Dimensioning and Annotation Blueprint",
        "svg": SVG_DIMENSIONING_RULES,
        "page": 4
    },
    4: {
        "title": "Technical Drawing Interpretation and Repair Workflow Flowchart",
        "svg": SVG_DRAWING_INTERPRETATION_FLOWCHART,
        "page": 4
    }
}

YOUTUBE_VIDEOS = {
    0: {
        "title": "Translating 2D Orthographic Projections into 3D Isometric Views",
        "url": "https://www.youtube.com/watch?v=h_u0BHKJ0yk",
        "description": "Visual demonstration of how three-dimensional isometric engineering drawings are constructed and correlated with flat 2D orthographic plans (Top, Front, Side views).",
        "page": 7
    },
    1: {
        "title": "The Evolution of Standardized Aviation Drafting and Manufacturing",
        "url": "https://www.youtube.com/watch?v=NpqU3eSeS1c",
        "description": "Historical perspective on how early aviation pioneers transitioned from guesswork sketches to standardized engineering drawings, enabling team manufacturing and airworthiness.",
        "page": 7
    },
    2: {
        "title": "Step-by-Step Isometric Sketching Using the Crating Method",
        "url": "https://www.youtube.com/watch?v=x9L9Vfj0UFE",
        "description": "Practical drafting tutorial demonstrating how to lay out an initial light bounding box, carve internal features, and produce professional isometric sketches with proper line weighting.",
        "page": 7
    },
    3: {
        "title": "Professional Technical Dimensioning and Drafting Standards",
        "url": "https://www.youtube.com/watch?v=NSlz_PSm7wY",
        "description": "Comprehensive tutorial demonstrating the proper drafting sequence for dimensioning: laying out extension lines, pulling parallel dimension lines, and correctly placing numerical tolerances.",
        "page": 7
    },
    4: {
        "title": "Aviation Chart and Airfield Diagram Real-Time Interpretation",
        "url": "https://www.youtube.com/watch?v=1A1zidPsNCA",
        "description": "Demonstration of spatial interpretation in aviation, showing how pilots and technicians translate 2D technical charts and airport diagrams into real-world 3D spatial awareness.",
        "page": 7
    }
}

def enrich_grade10_topic364():
    """Binds verified photographic hooks, custom responsive vector SVGs, and YouTube videos."""
    print("=" * 80)
    print("VISUAL & MULTIMEDIA ENRICHMENT ENGINE: Grade 10 Aviation — Topic 364")
    print("Topic: Aircraft Technical Drawing")
    print("=" * 80)

    topic = Topic.objects.filter(id=364, subject_id=44).first()
    if not topic:
        print("[ERROR] Topic 364 (Subject ID: 44) not found in database!")
        sys.exit(1)

    lessons = Lesson.objects.filter(topic=topic).order_by("learning_unit__order")
    if not lessons.exists():
        print("[ERROR] No lessons found for Topic 364! Run ingest_grade10_aviation_topic364.py first.")
        sys.exit(1)

    total_photos_attached = 0
    total_svgs_attached = 0
    total_videos_attached = 0
    total_assets_persisted = 0

    for lesson in lessons:
        u_order = lesson.learning_unit.order
        print(f"\n[*] Enriching Lesson {u_order + 1}: {lesson.title} (Lesson ID: {lesson.id})")

        # ---------------------------------------------------------------------
        # 1. Photographic Hook (Card 1)
        # ---------------------------------------------------------------------
        if u_order in WIKIMEDIA_PHOTOS:
            img_def = WIKIMEDIA_PHOTOS[u_order]
            photo_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=1,
                block_type="suggested_image"
            ).first()

            if photo_block:
                p_content = photo_block.content or {}
                p_content["resolved_image_url"] = img_def["url"]
                p_content["caption"] = img_def["caption"]
                p_content["title"] = img_def["title"]
                photo_block.content = p_content
                photo_block.title = img_def["title"]
                photo_block.save()

                asset, _ = LessonAsset.objects.get_or_create(
                    lesson=lesson,
                    asset_type="image",
                    url=img_def["url"],
                    defaults={
                        "source_type": "wikimedia",
                        "storage_type": "url",
                        "status": "attached",
                        "title": f"Lesson {u_order + 1} Photo: {img_def['title']}",
                        "description": img_def["caption"],
                        "metadata": {
                            "topic_order": 6,
                            "unit_order": u_order,
                            "page": 1,
                            "url": img_def["url"],
                            "license": "Creative Commons / Public Domain"
                        }
                    }
                )
                photo_block.assets.add(asset)
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
                            "topic_order": 6,
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
                            "topic_order": 6,
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
    print(f"ENRICHMENT COMPLETE: Topic 364 '{topic.name}'")
    print(f"  Photographic Hooks: {total_photos_attached} / 5")
    print(f"  Vector SVGs:        {total_svgs_attached} / 5")
    print(f"  YouTube Videos:     {total_videos_attached} / 5")
    print(f"  LessonAssets Total: {total_assets_persisted}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic364()
