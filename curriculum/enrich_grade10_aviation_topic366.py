"""
VLearn Grade 10 Aviation — Topic 366: Aerodynamics of Flight (Subject ID: 44, Topic ID: 366)
Visual Enrichment Engine (Verified Photos, Responsive Vector SVGs & Video Assets)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Aviation (Subject ID: 44)
Topic: Aerodynamics of Flight (Topic ID: 366, Order: 8)

Enriches:
  - 5 First-Card Photographic Visual Hooks (Verified Direct Wikimedia URLs)
  - 5 Custom Responsive Vector SVGs (viewBox="0 0 800 450", Dark Slate Theme #0f172a, Sanitized XML)
    * SVG 1: Airfoil geometry (camber, chord, leading/trailing edge, angle of attack, airflow velocity differential & Bernoulli pressure gradient).
    * SVG 2: The Four Forces of Flight in unaccelerated level flight (Lift, Weight, Thrust, Drag) with equilibrium vectors.
    * SVG 3: Aircraft 3 rotational axes (Longitudinal/Roll/Ailerons, Lateral/Pitch/Elevator, Vertical/Yaw/Rudder).
    * SVG 4: Stall dynamics: Increasing Angle of Attack past critical angle (15°-18°), boundary layer separation, turbulent wake, and loss of lift.
    * SVG 5: Wingtip vortices generation, circular spiral wake turbulence, and separation distance matrix.
  - 5 Verified Educational YouTube Videos
  - Persists LessonAsset models and binds them to corresponding LessonBlocks

Usage:
  ./venv/bin/python curriculum/enrich_grade10_aviation_topic366.py
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
# 5 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 366
# =============================================================================

# SVG 1: Airfoil Geometry, Flow Dynamics, and Bernoulli Pressure Gradient (Lesson 1)
SVG_AIRFOIL_GEOMETRY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="44" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Airfoil Geometry &amp; Aerodynamic Lift Generation</text>
  <text x="400" y="64" font-size="12" fill="#94a3b8" text-anchor="middle">Camber, Chord Line, Velocity Differential, Bernoulli Low Pressure &amp; Lift Vector</text>

  <!-- Aerodynamic Streamlines Above (Accelerated flow / Red-Orange) -->
  <g stroke="#f43f5e" stroke-width="2" fill="none" opacity="0.85">
    <path d="M 60 140 C 180 135 240 90 400 95 C 520 100 640 150 740 170"/>
    <path d="M 60 160 C 180 155 245 115 400 120 C 520 125 640 170 740 190"/>
    <path d="M 60 180 C 180 175 250 140 400 145 C 520 150 640 190 740 210"/>
  </g>

  <!-- Airfoil Profile -->
  <!-- Nose at (210, 240), Trailing edge at (610, 270) -->
  <path d="M 210 240 C 205 210 260 160 370 170 C 470 180 560 235 610 270 C 540 275 420 270 320 265 C 240 260 215 255 210 240 Z" 
        fill="#334155" stroke="#38bdf8" stroke-width="3"/>

  <!-- Chord Line (Dashed Orange) -->
  <line x1="170" y1="237" x2="650" y2="273" stroke="#f59e0b" stroke-width="2" stroke-dasharray="6,4"/>
  <circle cx="210" cy="240" r="4" fill="#f59e0b"/>
  <circle cx="610" cy="270" r="4" fill="#f59e0b"/>

  <!-- Relative Wind Vector (Incoming Blue Arrows from Left) -->
  <g stroke="#38bdf8" stroke-width="2.5">
    <line x1="50" y1="250" x2="160" y2="250"/>
    <polygon points="170,250 155,244 155,256" fill="#38bdf8"/>
    <line x1="50" y1="270" x2="160" y2="270"/>
    <polygon points="170,270 155,264 155,276" fill="#38bdf8"/>
    <line x1="50" y1="290" x2="160" y2="290"/>
    <polygon points="170,290 155,284 155,296" fill="#38bdf8"/>
  </g>
  <text x="105" y="235" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">RELATIVE WIND</text>

  <!-- Angle of Attack (AOA) Arc -->
  <path d="M 130 250 A 50 50 0 0 0 145 235" fill="none" stroke="#f59e0b" stroke-width="2"/>
  <text x="140" y="222" font-size="11" font-weight="bold" fill="#f59e0b">AOA (~8°)</text>

  <!-- Lower Streamlines (Slower flow / Blue) -->
  <g stroke="#0284c7" stroke-width="2" fill="none" opacity="0.8">
    <path d="M 60 280 C 200 280 320 285 450 290 C 560 295 650 290 740 285"/>
    <path d="M 60 310 C 200 310 320 315 450 315 C 560 315 650 310 740 305"/>
  </g>

  <!-- Center of Pressure & Lift Vector -->
  <!-- CP at (350, 200) -->
  <line x1="360" y1="210" x2="360" y2="85" stroke="#22c55e" stroke-width="4"/>
  <polygon points="360,75 350,95 370,95" fill="#22c55e"/>
  <circle cx="360" cy="210" r="5" fill="#22c55e"/>
  <rect x="375" y="90" width="135" height="32" rx="6" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
  <text x="442" y="111" font-size="13" font-weight="bold" fill="#22c55e" text-anchor="middle">LIFT FORCE (L)</text>

  <!-- Bernoulli Pressure Annotations -->
  <!-- Top Surface: Low Pressure -->
  <rect x="260" y="115" width="220" height="26" rx="5" fill="#1e293b" stroke="#f43f5e" stroke-width="1"/>
  <text x="370" y="132" font-size="10.5" font-weight="bold" fill="#fca5a5" text-anchor="middle">High Velocity ➔ LOW PRESSURE (Suction)</text>

  <!-- Bottom Surface: High Pressure -->
  <rect x="270" y="325" width="220" height="26" rx="5" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
  <text x="380" y="342" font-size="10.5" font-weight="bold" fill="#93c5fd" text-anchor="middle">Lower Velocity ➔ HIGH PRESSURE (Push)</text>

  <!-- Anatomy Labels -->
  <!-- Leading Edge -->
  <line x1="210" y1="240" x2="160" y2="185" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="155" y="180" font-size="10" font-weight="bold" fill="#e2e8f0" text-anchor="end">Leading Edge</text>

  <!-- Trailing Edge -->
  <line x1="610" y1="270" x2="660" y2="235" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="665" y="235" font-size="10" font-weight="bold" fill="#e2e8f0">Trailing Edge</text>

  <!-- Camber Label -->
  <line x1="370" y1="170" x2="370" y2="225" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="470" y="185" font-size="10" fill="#38bdf8">Upper Camber Profile</text>

  <!-- Downwash Arrows at Trailing Edge -->
  <g stroke="#38bdf8" stroke-width="2" fill="none">
    <path d="M 610 270 Q 670 290 710 330"/>
    <polygon points="716,337 703,330 712,321" fill="#38bdf8"/>
  </g>
  <text x="705" y="360" font-size="10" font-weight="bold" fill="#38bdf8">Downwash (Newton's 3rd Law)</text>

  <!-- Bottom Summary Legend -->
  <rect x="35" y="365" width="730" height="50" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="400" y="385" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">KEY FORMULA: Lift = 0.5 × Cl × ρ × V² × S</text>
  <text x="400" y="403" font-size="10" fill="#94a3b8" text-anchor="middle">Airfoil camber accelerates air over the top, dropping static pressure (Bernoulli) while deflecting mass downward (Newton).</text>
</svg>
""")

# SVG 2: The Four Forces of Flight in Equilibrium (Lesson 2)
SVG_FOUR_FORCES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="44" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Four Forces of Flight: Equilibrium in Level Flight</text>
  <text x="400" y="64" font-size="12" fill="#94a3b8" text-anchor="middle">Unaccelerated Straight-and-Level Cruise: Lift = Weight and Thrust = Drag</text>

  <!-- Aircraft Silhouette (Center) -->
  <!-- CG located at (400, 230) -->
  <g transform="translate(400, 230)">
    <!-- Horizontal Fuselage -->
    <path d="M -110 0 C -90 -12 60 -12 110 -2 C 120 0 120 4 110 6 C 60 12 -90 12 -110 0 Z" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
    <!-- Cabin Canopy -->
    <path d="M -40 -6 Q 0 -18 30 -6 Z" fill="#38bdf8" opacity="0.6"/>
    <!-- Main Wing Profile -->
    <path d="M -15 2 L -25 -42 L 5 -42 L 5 2 Z" fill="#64748b" stroke="#cbd5e1" stroke-width="1.5"/>
    <!-- Tail Fin (Vertical Stabilizer) -->
    <path d="M 85 -2 L 105 -32 L 118 -32 L 108 0 Z" fill="#64748b" stroke="#cbd5e1" stroke-width="1.5"/>
    <!-- Horizontal Tail -->
    <line x1="85" y1="2" x2="115" y2="2" stroke="#cbd5e1" stroke-width="3"/>
    <!-- Propeller Spinner / Nose -->
    <path d="M -110 -6 L -115 0 L -110 6 Z" fill="#f59e0b"/>
    <ellipse cx="-116" cy="0" rx="2" ry="18" fill="#e2e8f0" opacity="0.5"/>

    <!-- Center of Gravity (CG) Marker -->
    <circle cx="0" cy="0" r="10" fill="#0f172a" stroke="#ffffff" stroke-width="2"/>
    <path d="M 0 0 L 10 0 A 10 10 0 0 1 0 10 Z" fill="#ffffff"/>
    <path d="M 0 0 L -10 0 A 10 10 0 0 1 0 -10 Z" fill="#ffffff"/>
    <text x="14" y="-12" font-size="10" font-weight="bold" fill="#ffffff">CG</text>
  </g>

  <!-- 1. LIFT VECTOR (Upward Green Arrow) -->
  <line x1="400" y1="220" x2="400" y2="95" stroke="#22c55e" stroke-width="5"/>
  <polygon points="400,80 388,105 412,105" fill="#22c55e"/>
  <rect x="330" y="85" width="140" height="30" rx="6" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
  <text x="400" y="105" font-size="13" font-weight="bold" fill="#22c55e" text-anchor="middle">LIFT (L)</text>

  <!-- 2. WEIGHT VECTOR (Downward Blue Arrow) -->
  <line x1="400" y1="240" x2="400" y2="365" stroke="#3b82f6" stroke-width="5"/>
  <polygon points="400,380 388,355 412,355" fill="#3b82f6"/>
  <rect x="330" y="340" width="140" height="30" rx="6" fill="#0f172a" stroke="#3b82f6" stroke-width="2"/>
  <text x="400" y="360" font-size="13" font-weight="bold" fill="#60a5fa" text-anchor="middle">WEIGHT (W)</text>

  <!-- 3. THRUST VECTOR (Forward Red Arrow to Left) -->
  <line x1="390" y1="230" x2="230" y2="230" stroke="#ef4444" stroke-width="5"/>
  <polygon points="215,230 240,218 240,242" fill="#ef4444"/>
  <rect x="180" y="245" width="120" height="30" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
  <text x="240" y="265" font-size="13" font-weight="bold" fill="#f87171" text-anchor="middle">THRUST (T)</text>

  <!-- 4. DRAG VECTOR (Rearward Orange Arrow to Right) -->
  <line x1="410" y1="230" x2="570" y2="230" stroke="#f97316" stroke-width="5"/>
  <polygon points="585,230 560,218 560,242" fill="#f97316"/>
  <rect x="500" y="245" width="120" height="30" rx="6" fill="#0f172a" stroke="#f97316" stroke-width="2"/>
  <text x="560" y="265" font-size="13" font-weight="bold" fill="#fb923c" text-anchor="middle">DRAG (D)</text>

  <!-- Equilibrium Equality Badges -->
  <rect x="40" y="90" width="170" height="75" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="125" y="112" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">VERTICAL BALANCE</text>
  <text x="125" y="132" font-size="14" font-weight="bold" fill="#22c55e" text-anchor="middle">LIFT = WEIGHT</text>
  <text x="125" y="152" font-size="9.5" fill="#94a3b8" text-anchor="middle">Constant Altitude (Zero Climb)</text>

  <rect x="590" y="90" width="170" height="75" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="675" y="112" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">HORIZONTAL BALANCE</text>
  <text x="675" y="132" font-size="14" font-weight="bold" fill="#f87171" text-anchor="middle">THRUST = DRAG</text>
  <text x="675" y="152" font-size="9.5" fill="#94a3b8" text-anchor="middle">Constant Speed (Zero Accel)</text>

  <!-- Drag Breakdown Sub-box -->
  <g transform="translate(540, 310)">
    <rect x="0" y="0" width="220" height="70" rx="6" fill="#0f172a" stroke="#f97316" stroke-width="1"/>
    <text x="110" y="18" font-size="10" font-weight="bold" fill="#fb923c" text-anchor="middle">TOTAL DRAG EQUATION</text>
    <text x="110" y="36" font-size="9.5" fill="#ffffff" text-anchor="middle">Total Drag = Parasite + Induced</text>
    <text x="110" y="52" font-size="8.5" fill="#94a3b8" text-anchor="middle">Parasite (Skin/Form) ↑ with Speed²</text>
    <text x="110" y="64" font-size="8.5" fill="#94a3b8" text-anchor="middle">Induced (Lift byproduct) ↓ with Speed</text>
  </g>

  <!-- Bottom Principle Banner -->
  <rect x="35" y="390" width="730" height="30" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="400" y="410" font-size="10.5" fill="#e2e8f0" text-anchor="middle">When all four forces are equal, the net acceleration is zero. The plane is in straight, unaccelerated flight.</text>
</svg>
""")

# SVG 3: Aircraft Three Rotational Axes and Flight Controls (Lesson 3)
SVG_THREE_AXES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="44" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Three Axes of Rotation &amp; Primary Flight Control Surfaces</text>
  <text x="400" y="64" font-size="12" fill="#94a3b8" text-anchor="middle">Intersecting at the Center of Gravity (CG): Roll, Pitch, and Yaw Dynamics</text>

  <!-- Left Column: Longitudinal Axis (Roll / Ailerons) -->
  <g transform="translate(30, 80)">
    <rect x="0" y="0" width="230" height="330" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="30" rx="10" fill="#dc2626"/>
    <text x="115" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">LONGITUDINAL AXIS</text>

    <text x="115" y="55" font-size="15" font-weight="bold" fill="#f87171" text-anchor="middle">ROLL</text>
    <text x="115" y="72" font-size="10" fill="#94a3b8" text-anchor="middle">Tilting Wings Side to Side</text>

    <!-- Isometric Graphic -->
    <g transform="translate(115, 135)">
      <!-- Line of axis (Nose to Tail) -->
      <line x1="0" y1="-50" x2="0" y2="50" stroke="#ef4444" stroke-width="3" stroke-dasharray="4,4"/>
      <!-- Wings horizontal -->
      <line x1="-70" y1="0" x2="70" y2="0" stroke="#cbd5e1" stroke-width="6"/>
      <!-- Roll Curved Arrow -->
      <path d="M -40 -20 A 45 45 0 0 1 40 -20" fill="none" stroke="#f87171" stroke-width="2.5"/>
      <polygon points="45,-15 40,-25 32,-18" fill="#f87171"/>
      <circle cx="0" cy="0" r="5" fill="#ffffff"/>
      <!-- Ailerons highlighted on wingtips -->
      <rect x="-68" y="-4" width="20" height="8" rx="2" fill="#ef4444"/>
      <rect x="48" y="-4" width="20" height="8" rx="2" fill="#ef4444"/>
    </g>

    <rect x="12" y="205" width="206" height="110" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <text x="115" y="225" font-size="10.5" font-weight="bold" fill="#f87171" text-anchor="middle">PRIMARY CONTROL: AILERONS</text>
    <g font-size="9.5" fill="#e2e8f0" transform="translate(20, 245)">
      <text y="0">• Location: Outer wing trailing edge</text>
      <text y="16">• Motion: Move differentially (opposing)</text>
      <text y="32">• Input: Turn yoke or stick left / right</text>
      <text y="48">• Turn left: Left aileron UP, right DOWN</text>
    </g>
  </g>

  <!-- Middle Column: Lateral Axis (Pitch / Elevator) -->
  <g transform="translate(285, 80)">
    <rect x="0" y="0" width="230" height="330" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="30" rx="10" fill="#16a34a"/>
    <text x="115" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">LATERAL AXIS</text>

    <text x="115" y="55" font-size="15" font-weight="bold" fill="#4ade80" text-anchor="middle">PITCH</text>
    <text x="115" y="72" font-size="10" fill="#94a3b8" text-anchor="middle">Tilting Nose Up and Down</text>

    <!-- Isometric Graphic -->
    <g transform="translate(115, 135)">
      <!-- Line of axis (Wingtip to Wingtip) -->
      <line x1="-70" y1="0" x2="70" y2="0" stroke="#22c55e" stroke-width="3" stroke-dasharray="4,4"/>
      <!-- Fuselage vertical cross line -->
      <line x1="0" y1="-50" x2="0" y2="50" stroke="#cbd5e1" stroke-width="6"/>
      <!-- Pitch Curved Arrow -->
      <path d="M -20 -40 A 45 45 0 0 1 -20 40" fill="none" stroke="#4ade80" stroke-width="2.5"/>
      <polygon points="-15,45 -25,40 -18,32" fill="#4ade80"/>
      <circle cx="0" cy="0" r="5" fill="#ffffff"/>
      <!-- Elevator highlighted on horizontal tail -->
      <rect x="-25" y="42" width="50" height="8" rx="2" fill="#22c55e"/>
    </g>

    <rect x="12" y="205" width="206" height="110" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <text x="115" y="225" font-size="10.5" font-weight="bold" fill="#4ade80" text-anchor="middle">PRIMARY CONTROL: ELEVATOR</text>
    <g font-size="9.5" fill="#e2e8f0" transform="translate(20, 245)">
      <text y="0">• Location: Horizontal stabilizer tail</text>
      <text y="16">• Motion: Hinges up / down together</text>
      <text y="32">• Input: Pull yoke (UP) / Push yoke (DOWN)</text>
      <text y="48">• Up elevator forces tail down, nose UP</text>
    </g>
  </g>

  <!-- Right Column: Vertical Axis (Yaw / Rudder) -->
  <g transform="translate(540, 80)">
    <rect x="0" y="0" width="230" height="330" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="30" rx="10" fill="#0284c7"/>
    <text x="115" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">VERTICAL AXIS</text>

    <text x="115" y="55" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">YAW</text>
    <text x="115" y="72" font-size="10" fill="#94a3b8" text-anchor="middle">Swinging Nose Left and Right</text>

    <!-- Isometric Graphic -->
    <g transform="translate(115, 135)">
      <!-- Fuselage body -->
      <ellipse cx="0" cy="0" rx="55" ry="20" fill="#475569" stroke="#cbd5e1" stroke-width="2"/>
      <!-- Vertical axis passing straight down -->
      <line x1="0" y1="-55" x2="0" y2="55" stroke="#38bdf8" stroke-width="3" stroke-dasharray="4,4"/>
      <!-- Yaw Curved Arrow around center -->
      <path d="M -30 -15 A 35 15 0 0 1 30 -15" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
      <polygon points="35,-12 30,-20 23,-15" fill="#38bdf8"/>
      <circle cx="0" cy="0" r="5" fill="#ffffff"/>
      <!-- Rudder highlighted on vertical tail -->
      <rect x="42" y="-12" width="10" height="24" rx="2" fill="#38bdf8"/>
    </g>

    <rect x="12" y="205" width="206" height="110" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <text x="115" y="225" font-size="10.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">PRIMARY CONTROL: RUDDER</text>
    <g font-size="9.5" fill="#e2e8f0" transform="translate(20, 245)">
      <text y="0">• Location: Vertical stabilizer tail fin</text>
      <text y="16">• Motion: Hinges left / right</text>
      <text y="32">• Input: Push left or right rudder pedals</text>
      <text y="48">• Right pedal deflects rudder right, nose YAWS right</text>
    </g>
  </g>
</svg>
""")

# SVG 4: Stall Dynamics & Boundary Layer Separation (Lesson 4)
SVG_STALL_DYNAMICS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="44" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Aerodynamic Stall Dynamics: Critical Angle of Attack</text>
  <text x="400" y="64" font-size="12" fill="#94a3b8" text-anchor="middle">Comparison of Attached Laminar Flow (Normal) vs. Boundary Layer Separation (Stalled)</text>

  <!-- Left Side: Normal Flight (Attached Flow) -->
  <g transform="translate(35, 80)">
    <rect x="0" y="0" width="350" height="260" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="350" height="30" rx="10" fill="#15803d"/>
    <text x="175" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">NORMAL FLIGHT: ATTACHED AIRFLOW (AOA ~ 5°)</text>

    <!-- Smooth Blue Streamlines -->
    <g stroke="#38bdf8" stroke-width="2" fill="none" opacity="0.85">
      <path d="M 20 85 C 80 85 110 55 180 58 C 240 60 300 95 330 110"/>
      <path d="M 20 105 C 80 105 115 75 180 78 C 240 80 300 115 330 130"/>
      <path d="M 20 125 C 80 125 120 95 180 98 C 240 100 300 135 330 150"/>
      <path d="M 20 160 C 100 160 180 165 260 170 C 300 170 330 165 330 165"/>
    </g>

    <!-- Airfoil at low AOA (~5°) -->
    <!-- Nose at (90, 130), Trailing edge at (290, 150) -->
    <path d="M 90 130 C 85 110 120 75 185 82 C 240 88 280 130 290 150 C 250 152 180 148 130 145 Z" 
          fill="#334155" stroke="#4ade80" stroke-width="2"/>

    <!-- Chord Line -->
    <line x1="75" y1="128" x2="305" y2="152" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,3"/>

    <!-- High Lift Arrow -->
    <line x1="185" y1="110" x2="185" y2="40" stroke="#22c55e" stroke-width="3.5"/>
    <polygon points="185,30 178,45 192,45" fill="#22c55e"/>
    <text x="200" y="45" font-size="11" font-weight="bold" fill="#22c55e">High Lift</text>

    <!-- Status Box -->
    <rect x="20" y="195" width="310" height="50" rx="6" fill="#1e293b" stroke="#16a34a" stroke-width="1"/>
    <text x="175" y="214" font-size="10.5" font-weight="bold" fill="#4ade80" text-anchor="middle">Boundary Layer Fully Attached</text>
    <text x="175" y="232" font-size="9" fill="#cbd5e1" text-anchor="middle">Low Drag | Responsive Flight Controls | Stable Lift</text>
  </g>

  <!-- Right Side: Stalled Flight (Separated Flow) -->
  <g transform="translate(415, 80)">
    <rect x="0" y="0" width="350" height="260" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="350" height="30" rx="10" fill="#b91c1c"/>
    <text x="175" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">STALLED FLIGHT: AIRFLOW SEPARATION (AOA > 18°)</text>

    <!-- Separated Chaotic Red Eddies -->
    <g stroke="#ef4444" stroke-width="2" fill="none" opacity="0.9">
      <!-- Approaching air splits -->
      <path d="M 20 120 C 60 120 75 90 90 70 C 110 40 140 40 160 60 C 180 80 150 110 130 90"/>
      <!-- Swirling vortex 1 -->
      <circle cx="175" cy="75" r="14" stroke-dasharray="3,2"/>
      <polygon points="185,65 190,75 180,75" fill="#ef4444"/>
      <!-- Swirling vortex 2 -->
      <circle cx="235" cy="95" r="18" stroke-dasharray="4,2"/>
      <polygon points="250,85 255,97 243,95" fill="#ef4444"/>
      <!-- Swirling vortex 3 -->
      <circle cx="295" cy="115" r="15" stroke-dasharray="3,2"/>
      <!-- Lower airflow -->
      <path d="M 20 170 C 80 170 140 190 200 200 C 260 210 300 205 330 200" stroke="#38bdf8"/>
    </g>

    <!-- Airfoil at steep AOA (~22°) -->
    <!-- Nose at (90, 110), Trailing edge at (260, 185) -->
    <path d="M 90 110 C 90 85 130 65 185 95 C 230 120 250 170 260 185 C 220 180 150 150 120 135 Z" 
          fill="#334155" stroke="#ef4444" stroke-width="2"/>

    <!-- Chord line tilted steeply -->
    <line x1="70" y1="98" x2="275" y2="192" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,3"/>

    <!-- Collapsed Lift Arrow & Rapid Sink -->
    <line x1="175" y1="120" x2="175" y2="80" stroke="#ef4444" stroke-width="2" stroke-dasharray="2,2"/>
    <text x="185" y="75" font-size="11" font-weight="bold" fill="#ef4444">Lift Collapses (-75%)</text>
    
    <!-- Massive Drag Arrow -->
    <line x1="220" y1="140" x2="310" y2="140" stroke="#f97316" stroke-width="4"/>
    <polygon points="320,140 305,132 305,148" fill="#f97316"/>
    <text x="270" y="162" font-size="10" font-weight="bold" fill="#f97316">Massive Drag</text>

    <!-- Status Box -->
    <rect x="20" y="195" width="310" height="50" rx="6" fill="#1e293b" stroke="#dc2626" stroke-width="1"/>
    <text x="175" y="214" font-size="10.5" font-weight="bold" fill="#f87171" text-anchor="middle">Turbulent Boundary Layer Detachment</text>
    <text x="175" y="232" font-size="9" fill="#fca5a5" text-anchor="middle">Airframe Buffeting | Yoke Mushiness | Severe Altitude Sink</text>
  </g>

  <!-- Bottom Recovery Sequence Banner -->
  <g transform="translate(35, 350)">
    <rect x="0" y="0" width="730" height="70" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="365" y="22" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">UNIVERSAL 3-STEP STALL RECOVERY PROCEDURE</text>
    <g font-size="10" fill="#ffffff" transform="translate(20, 44)">
      <text x="0"><tspan font-weight="bold" fill="#f59e0b">1. PUSH YOKE FORWARD:</tspan> Reduce Angle of Attack below critical limit (Airflow reattaches instantly)</text>
      <text x="0" y="18"><tspan font-weight="bold" fill="#34d399">2. ROLL WINGS LEVEL:</tspan> Coordinate ailerons and rudder  |  <tspan font-weight="bold" fill="#38bdf8">3. MAXIMUM POWER:</tspan> Smoothly advance throttle to climb away</text>
    </g>
  </g>
</svg>
""")

# SVG 5: Wingtip Vortices Generation & Separation Matrix (Lesson 5)
SVG_WINGTIP_VORTICES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="44" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Wingtip Vortices &amp; Wake Turbulence Avoidance</text>
  <text x="400" y="64" font-size="12" fill="#94a3b8" text-anchor="middle">Pressure Equalization Curl, Sinking Wake Funnels, and Airport Separation Corridors</text>

  <!-- Aft View of Transport Aircraft Wing -->
  <!-- Left Wingtip at (120, 150), Fuselage at (400, 150), Right Wingtip at (680, 150) -->
  <g transform="translate(0, 0)">
    <!-- Main Wing Bar -->
    <path d="M 120 150 L 370 158 L 400 160 L 430 158 L 680 150 L 680 142 L 400 152 L 120 142 Z" fill="#64748b" stroke="#94a3b8" stroke-width="2"/>
    <!-- Fuselage Profile (Rear View) -->
    <ellipse cx="400" cy="155" rx="30" ry="32" fill="#334155" stroke="#cbd5e1" stroke-width="2"/>
    <!-- Vertical Tail Fin -->
    <path d="M 395 125 L 395 80 L 405 80 L 405 125 Z" fill="#475569" stroke="#cbd5e1" stroke-width="1.5"/>
    <!-- Jet Engines under wings -->
    <ellipse cx="280" cy="175" rx="14" ry="16" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <ellipse cx="520" cy="175" rx="14" ry="16" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>

    <!-- Pressure Labels across Wing -->
    <text x="400" y="138" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">LOW PRESSURE (Suction on Upper Camber)</text>
    <text x="400" y="198" font-size="10" font-weight="bold" fill="#f59e0b" text-anchor="middle">HIGH PRESSURE (Compression Under Wing)</text>
  </g>

  <!-- LEFT WINGTIP VORTEX (Clockwise curl / Orange-Red Spirals) -->
  <g transform="translate(120, 150)" stroke="#f97316" stroke-width="2" fill="none">
    <!-- Spiraling ellipses downward and inward -->
    <path d="M 0 10 C 25 15 35 40 25 60 C 15 80 -25 80 -35 50 C -45 20 -10 -20 30 -20 C 70 -20 80 40 60 80 C 40 120 -30 130 -60 90"/>
    <polygon points="-65,85 -62,98 -50,92" fill="#f97316"/>
  </g>
  <text x="80" y="240" font-size="11" font-weight="bold" fill="#f97316" text-anchor="middle">Clockwise Roll</text>
  <text x="80" y="255" font-size="9" fill="#94a3b8" text-anchor="middle">(Viewed from behind)</text>

  <!-- RIGHT WINGTIP VORTEX (Counter-Clockwise curl / Orange-Red Spirals) -->
  <g transform="translate(680, 150)" stroke="#f97316" stroke-width="2" fill="none">
    <!-- Spiraling ellipses downward and inward -->
    <path d="M 0 10 C -25 15 -35 40 -25 60 C -15 80 25 80 35 50 C 45 20 10 -20 -30 -20 C -70 -20 -80 40 -60 80 C -40 120 30 130 60 90"/>
    <polygon points="65,85 62,98 50,92" fill="#f97316"/>
  </g>
  <text x="720" y="240" font-size="11" font-weight="bold" fill="#f97316" text-anchor="middle">Counter-Clockwise</text>
  <text x="720" y="255" font-size="9" fill="#94a3b8" text-anchor="middle">(Viewed from behind)</text>

  <!-- Sinking Motion Indicator -->
  <g stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3">
    <line x1="200" y1="210" x2="200" y2="280"/>
    <line x1="600" y1="210" x2="600" y2="280"/>
  </g>
  <text x="400" y="245" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Vortices Sink at 400 - 500 ft/min</text>
  <text x="400" y="260" font-size="9.5" fill="#94a3b8" text-anchor="middle">Levels off 800 - 1,000 ft below flight path</text>

  <!-- Middle Box: Peak Hazard Configuration -->
  <rect x="230" y="275" width="340" height="42" rx="6" fill="#450a0a" stroke="#ef4444" stroke-width="1.5"/>
  <text x="400" y="293" font-size="11" font-weight="bold" fill="#fca5a5" text-anchor="middle">MAXIMUM VORTEX STRENGTH: HEAVY, CLEAN &amp; SLOW</text>
  <text x="400" y="308" font-size="9.5" fill="#ffffff" text-anchor="middle">High Mass + Flaps Retracted + High Angle of Attack</text>

  <!-- Bottom Panel: Takeoff & Landing Avoidance Matrix -->
  <g transform="translate(30, 330)">
    <rect x="0" y="0" width="740" height="95" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="740" height="22" rx="8" fill="#0284c7"/>
    <text x="370" y="15" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">RUNWAY AVOIDANCE PROCEDURES (LIGHT AIRCRAFT BEHIND HEAVY JET)</text>

    <!-- Takeoff Corridor -->
    <g transform="translate(20, 32)">
      <text x="0" y="12" font-size="10.5" font-weight="bold" fill="#34d399">TAKEOFF BEHIND HEAVY JET:</text>
      <text x="0" y="28" font-size="9.5" fill="#e2e8f0">• Rotate (lift off) <tspan font-weight="bold" fill="#34d399">BEFORE</tspan> the heavy jet's rotation point.</text>
      <text x="0" y="44" font-size="9.5" fill="#e2e8f0">• Climb <tspan font-weight="bold" fill="#34d399">ABOVE &amp; UPWIND</tspan> of the jet's climbing flight corridor.</text>
    </g>

    <!-- Landing Corridor -->
    <g transform="translate(400, 32)">
      <text x="0" y="12" font-size="10.5" font-weight="bold" fill="#f59e0b">LANDING BEHIND HEAVY JET:</text>
      <text x="0" y="28" font-size="9.5" fill="#e2e8f0">• Stay <tspan font-weight="bold" fill="#f59e0b">ABOVE</tspan> the jet's approach glide path.</text>
      <text x="0" y="44" font-size="9.5" fill="#e2e8f0">• Touch down <tspan font-weight="bold" fill="#f59e0b">BEYOND</tspan> the point where the jet's wheels landed.</text>
    </g>
  </g>
</svg>
""")

# =============================================================================
# ASSET DATA DEFINITIONS
# =============================================================================

PHOTO_HOOKS = {
    0: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Airfoil_lift_and_drag.jpg",
        "title": "Aerodynamic Airfoil Profile and Lift Streamlines",
        "caption": "A cross-sectional diagram and physical model of an asymmetric aerodynamic airfoil cutting through oncoming airflow to generate aerodynamic lift.",
        "author": "J Doug McLean",
        "license": "CC BY-SA 3.0"
    },
    1: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/84/Cessna_172_RG_in_flight_by_Don_Ramey_Logan.jpg",
        "title": "Light Aircraft Maintaining Stable Cruising Flight",
        "caption": "A light general aviation aircraft cruising in straight-and-level unaccelerated flight, maintaining balanced physical equilibrium among Lift, Weight, Thrust, and Drag.",
        "author": "Don Ramey Logan",
        "license": "CC BY 4.0"
    },
    2: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/02/Aircraft_controls_%2816436200715%29.jpg",
        "title": "Aircraft Primary Flight Control Surfaces and Cockpit Inputs",
        "caption": "A light aircraft showing hinged flight control surfaces (ailerons, elevator, and rudder) that deflect airflow to rotate the plane around its three axes.",
        "author": "US Air Force",
        "license": "Public Domain"
    },
    3: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a8/FA-18C_vapor_LEX_and_wingtip_1.jpg",
        "title": "High Angle of Attack Airflow Separation and Vapor Condensation",
        "caption": "A high-performance aircraft maneuvering at high Angle of Attack, showing intense boundary layer condensation and vortex separation across the lifting surfaces.",
        "author": "Jonathan Chandler / U.S. Navy",
        "license": "Public Domain"
    },
    4: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/f/fe/Airplane_vortex_edit.jpg",
        "title": "Wingtip Vortex Generation Trailing an Aircraft",
        "caption": "A flight demonstration revealing energetic counter-rotating wingtip vortices spiraling backward from the outer edges of the lifting wings.",
        "author": "NASA Langley Research Center / Fir0002",
        "license": "Public Domain"
    }
}

SVG_MAP = {
    0: {
        "title": "Airfoil Geometry, Flow Dynamics, and Pressure Gradient",
        "svg": SVG_AIRFOIL_GEOMETRY,
        "page": 4
    },
    1: {
        "title": "The Four Forces of Flight Vector Equilibrium Diagram",
        "svg": SVG_FOUR_FORCES,
        "page": 4
    },
    2: {
        "title": "Aircraft Rotational Axes and Primary Flight Control Surfaces",
        "svg": SVG_THREE_AXES,
        "page": 4
    },
    3: {
        "title": "Stall Dynamics: Increasing Angle of Attack & Airflow Separation",
        "svg": SVG_STALL_DYNAMICS,
        "page": 4
    },
    4: {
        "title": "Wingtip Vortices Formation, Wake Turbulence & Separation Matrix",
        "svg": SVG_WINGTIP_VORTICES,
        "page": 4
    }
}

YOUTUBE_VIDEOS = {
    0: {
        "url": "https://www.youtube.com/watch?v=dpNCU37z4vU",
        "title": "Airfoil Geometry and Aerodynamic Lift Generation",
        "description": "Watch how oncoming relative wind splits at the leading edge, and observe how velocity differentials, Bernoulli pressure gradients, and angle of attack combine to produce aerodynamic lift."
    },
    1: {
        "url": "https://www.youtube.com/watch?v=imDKWTt5cfk",
        "title": "The Four Forces of Flight Explained Simply",
        "description": "Examine how the four fundamental aerodynamic forces interact, observe animated vector balances during unaccelerated cruising flight, and see how thrust and drag shifts produce climbs and descents."
    },
    2: {
        "url": "https://www.youtube.com/watch?v=53rzgOpFnIs",
        "title": "The Three Axes of Rotation on an Aircraft",
        "description": "Watch real cockpit control inputs translate into external surface movements, showing how aileron, elevator, and rudder deflections rotate the airplane around its three axes."
    },
    3: {
        "url": "https://www.youtube.com/watch?v=xxLNVRxNJZA",
        "title": "Airflow Behavior During a Flight Stall Demonstration",
        "description": "Observe real-time tuft testing on an aircraft wing as increasing Angle of Attack leads to boundary layer detachment, wild tuft fluttering, and sudden loss of lift."
    },
    4: {
        "url": "https://www.youtube.com/watch?v=-34-Igi5UMc",
        "title": "Ground Effect and Wake Turbulence Explained",
        "description": "Watch smoke-visualization wind tunnel tests demonstrating wingtip vortex formation and see graphical animations showing safe takeoff and landing avoidance corridors."
    }
}

def enrich_grade10_topic366():
    """Enriches Grade 10 Aviation Topic 366 with photographic hooks, SVGs, and videos."""
    print("=" * 80)
    print("VLEARN VISUAL ENRICHMENT: Grade 10 Aviation — Topic 366 (ID: 366)")
    print("Aerodynamics of Flight")
    print("=" * 80)

    curriculum = Curriculum.objects.get(id=5)
    grade = Grade.objects.get(id=5, level=10)
    subject = Subject.objects.get(id=44, grade=grade)
    topic = Topic.objects.get(id=366, subject=subject)

    print(f"[*] Topic: {topic.name} (ID: {topic.id})")

    lessons = Lesson.objects.filter(topic=topic).order_by("learning_unit__order")
    print(f"[*] Found {lessons.count()} Lessons to enrich.")

    total_photos_attached = 0
    total_svgs_attached = 0
    total_videos_attached = 0
    total_assets_persisted = 0

    for lesson in lessons:
        u_order = lesson.learning_unit.order
        print(f"\n--- Processing Lesson {u_order + 1}: {lesson.title} (ID: {lesson.id}) ---")

        # ---------------------------------------------------------------------
        # 1. First-Card Photographic Visual Hooks
        # ---------------------------------------------------------------------
        if u_order in PHOTO_HOOKS:
            img_def = PHOTO_HOOKS[u_order]
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
                            "topic_order": 8,
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
                            "topic_order": 8,
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
                            "topic_order": 8,
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
    print("ENRICHMENT SUMMARY")
    print("=" * 80)
    print(f"Total Photos Attached: {total_photos_attached}/5")
    print(f"Total SVGs Attached:   {total_svgs_attached}/5")
    print(f"Total Videos Attached: {total_videos_attached}/5")
    print(f"Total LessonAssets:    {total_assets_persisted}/15")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic366()