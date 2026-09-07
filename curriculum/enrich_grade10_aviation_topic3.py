"""
VLearn Grade 10 Aviation — Topic 3: Aircraft Components and Construction (Topic ID: 249)
Visual Enrichment Engine (Verified Photos, Responsive Vector SVGs & Video Assets)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Aviation (Subject ID: 44)
Topic: Aircraft Components and Construction (Topic ID: 249, Order: 2)

Enriches:
  - 3 First-Card Photographic Visual Hooks (Verified Direct Wikimedia URLs)
  - 3 Custom Responsive Vector SVGs (viewBox="0 0 800 450", Dark Slate Theme #0f172a, Sanitized XML)
  - 3 Verified Educational YouTube Videos (Anatomy 3D, Flight controls, How airplanes work)
  - Persists LessonAsset models and binds them to corresponding LessonBlocks

Usage:
  ./venv/bin/python curriculum/enrich_grade10_aviation_topic3.py
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
# 3 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 249
# =============================================================================

# SVG 1: Aircraft Structural Anatomy (Lesson 1, Page 4)
SVG_AIRCRAFT_ANATOMY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="44" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Aircraft Structural Anatomy &amp; Construction</text>
  <text x="400" y="63" font-size="12" fill="#94a3b8" text-anchor="middle">Semi-Monocoque Fuselage, Internal Wing Framework, Empennage &amp; Undercarriage</text>

  <!-- Left: Semi-Monocoque Fuselage Cutaway -->
  <g transform="translate(35, 80)">
    <rect x="0" y="0" width="350" height="235" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="350" height="32" rx="10" fill="#0284c7"/>
    <text x="175" y="21" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">FUSELAGE: SEMI-MONOCOQUE ARCHITECTURE</text>

    <!-- Cylinder / Frame Diagram -->
    <ellipse cx="65" cy="115" rx="35" ry="60" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <ellipse cx="140" cy="115" rx="35" ry="60" fill="none" stroke="#60a5fa" stroke-width="2" stroke-dasharray="4,4"/>
    <ellipse cx="215" cy="115" rx="35" ry="60" fill="none" stroke="#60a5fa" stroke-width="2" stroke-dasharray="4,4"/>
    <ellipse cx="290" cy="115" rx="35" ry="60" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>

    <!-- Longitudinal Stringers -->
    <line x1="65" y1="55" x2="290" y2="55" stroke="#f59e0b" stroke-width="3"/>
    <line x1="65" y1="85" x2="290" y2="85" stroke="#f59e0b" stroke-width="2"/>
    <line x1="65" y1="145" x2="290" y2="145" stroke="#f59e0b" stroke-width="2"/>
    <line x1="65" y1="175" x2="290" y2="175" stroke="#f59e0b" stroke-width="3"/>

    <!-- Skin Cutaway Representation -->
    <path d="M 170 55 C 230 55 260 75 290 85 L 290 175 C 250 175 210 160 170 145 Z" fill="#0369a1" fill-opacity="0.35" stroke="#38bdf8" stroke-width="1.5"/>

    <!-- Labels -->
    <text x="75" y="195" font-size="10" font-weight="bold" fill="#60a5fa">• Circular Frames / Bulkheads</text>
    <text x="75" y="210" font-size="10" font-weight="bold" fill="#f59e0b">• Longitudinal Stringers</text>
    <text x="75" y="225" font-size="10" font-weight="bold" fill="#38bdf8">• Stressed Riveted Aluminum Skin</text>
  </g>

  <!-- Right: Wing Internal Framework (Spars & Ribs) -->
  <g transform="translate(415, 80)">
    <rect x="0" y="0" width="350" height="235" rx="10" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect x="0" y="0" width="350" height="32" rx="10" fill="#059669"/>
    <text x="175" y="21" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">WING SKELETON: SPARS, RIBS &amp; SKIN</text>

    <!-- Wing Outline -->
    <path d="M 30 75 L 320 95 L 315 160 L 30 180 Z" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>

    <!-- Main Front Spar -->
    <line x1="30" y1="100" x2="318" y2="115" stroke="#f59e0b" stroke-width="5"/>
    <text x="35" y="93" font-size="10" font-weight="bold" fill="#f59e0b">Front Main Spar (Bending Loads)</text>

    <!-- Rear Spar -->
    <line x1="30" y1="145" x2="316" y2="148" stroke="#f59e0b" stroke-width="4"/>
    <text x="35" y="160" font-size="9" fill="#f59e0b">Rear Spar</text>

    <!-- Transverse Ribs -->
    <path d="M 70 78 C 85 90 85 155 70 177" stroke="#34d399" stroke-width="2.5" fill="none"/>
    <path d="M 120 81 C 135 95 135 152 120 173" stroke="#34d399" stroke-width="2.5" fill="none"/>
    <path d="M 170 85 C 185 98 185 150 170 170" stroke="#34d399" stroke-width="2.5" fill="none"/>
    <path d="M 220 88 C 235 101 235 148 220 167" stroke="#34d399" stroke-width="2.5" fill="none"/>
    <path d="M 270 92 C 285 105 285 145 270 163" stroke="#34d399" stroke-width="2.5" fill="none"/>

    <text x="140" y="200" font-size="10" font-weight="bold" fill="#34d399">• Transverse Airfoil Ribs (Shape &amp; Skin Support)</text>
    <text x="140" y="215" font-size="10" fill="#94a3b8">Carries aerodynamic pressure directly to heavy spars</text>
    <text x="40" y="125" font-size="10" font-weight="bold" fill="#cbd5e1">Wing Root</text>
    <text x="265" y="120" font-size="10" font-weight="bold" fill="#cbd5e1">Wing Tip</text>
  </g>

  <!-- Bottom: Empennage & Tricycle Landing Gear Badges -->
  <g transform="translate(35, 330)">
    <!-- Empennage Component Card -->
    <rect x="0" y="0" width="350" height="85" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="15" y="22" font-size="12" font-weight="bold" fill="#c084fc">EMPENNAGE (Tail Assembly)</text>
    <text x="15" y="42" font-size="11" fill="#f8fafc">• <tspan font-weight="bold">Vertical Stabilizer:</tspan> Directional trim, prevents yaw drift</text>
    <text x="15" y="58" font-size="11" fill="#f8fafc">• <tspan font-weight="bold">Horizontal Stabilizer:</tspan> Longitudinal trim, prevents pitch bobbing</text>
    <text x="15" y="74" font-size="10" fill="#94a3b8">Acts like dart feathers ensuring straight, balanced forward flight</text>
  </g>

  <g transform="translate(415, 330)">
    <!-- Landing Gear Component Card -->
    <rect x="0" y="0" width="350" height="85" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <text x="15" y="22" font-size="12" font-weight="bold" fill="#f472b6">LANDING GEAR (Tricycle Undercarriage)</text>
    <text x="15" y="42" font-size="11" fill="#f8fafc">• <tspan font-weight="bold">Steerable Nosewheel:</tspan> Direct ground steering, prevents nose-over</text>
    <text x="15" y="58" font-size="11" fill="#f8fafc">• <tspan font-weight="bold">Oleo Shock Struts:</tspan> Nitrogen gas and metered hydraulic fluid</text>
    <text x="15" y="74" font-size="10" fill="#94a3b8">Absorbs high vertical impact energy on touchdown to protect spars</text>
  </g>
</svg>
""")

# SVG 2: Three Flight Axes & Flight Control Surfaces (Lesson 2, Page 4)
SVG_FLIGHT_AXES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="44" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Three Flight Axes &amp; Primary Control Surfaces</text>
  <text x="400" y="63" font-size="12" fill="#94a3b8" text-anchor="middle">Rotational Dynamics Passing Through the Center of Gravity (CG)</text>

  <!-- Central Aircraft Representation & Axes Coordinates -->
  <g id="axes_center">
    <!-- Fuselage Center Silhouette -->
    <ellipse cx="400" cy="190" rx="20" ry="12" fill="#334155" stroke="#64748b" stroke-width="1.5"/>

    <!-- LATERAL AXIS (Pitch) - Amber -->
    <line x1="80" y1="190" x2="720" y2="190" stroke="#f59e0b" stroke-width="3" stroke-dasharray="8,4"/>
    <text x="730" y="194" font-size="11" font-weight="bold" fill="#f59e0b">Lateral Axis (Pitch)</text>

    <!-- LONGITUDINAL AXIS (Roll) - Cyan -->
    <line x1="200" y1="80" x2="600" y2="300" stroke="#38bdf8" stroke-width="3"/>
    <text x="610" y="306" font-size="11" font-weight="bold" fill="#38bdf8">Longitudinal Axis (Roll)</text>

    <!-- VERTICAL AXIS (Yaw) - Emerald -->
    <line x1="400" y1="80" x2="400" y2="295" stroke="#34d399" stroke-width="3" stroke-dasharray="8,4"/>
    <text x="410" y="95" font-size="11" font-weight="bold" fill="#34d399">Vertical Axis (Yaw)</text>

    <!-- Center of Gravity Marker -->
    <circle cx="400" cy="190" r="14" fill="#f59e0b" fill-opacity="0.3"/>
    <circle cx="400" cy="190" r="7" fill="#facc15" stroke="#0f172a" stroke-width="2"/>
    <text x="400" y="215" font-size="10" font-weight="bold" fill="#facc15" text-anchor="middle">CG</text>

    <!-- Roll Curved Arrows (Longitudinal) -->
    <path d="M 520 230 A 28 28 0 1 1 540 265" fill="none" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow_cyan)"/>
    <text x="560" y="250" font-size="10" font-weight="bold" fill="#38bdf8">ROLL</text>

    <!-- Pitch Curved Arrows (Lateral) -->
    <path d="M 180 170 A 25 25 0 1 1 180 210" fill="none" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#arrow_amber)"/>
    <text x="140" y="175" font-size="10" font-weight="bold" fill="#f59e0b">PITCH</text>

    <!-- Yaw Curved Arrows (Vertical) -->
    <path d="M 370 120 A 30 30 0 1 1 430 120" fill="none" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrow_emerald)"/>
    <text x="400" y="145" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">YAW</text>
  </g>

  <!-- Markers -->
  <defs>
    <marker id="arrow_cyan" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#38bdf8"/>
    </marker>
    <marker id="arrow_amber" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#f59e0b"/>
    </marker>
    <marker id="arrow_emerald" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#34d399"/>
    </marker>
  </defs>

  <!-- Bottom Three Detailed Info Cards -->
  <!-- Card 1: ROLL / AILERONS -->
  <g transform="translate(35, 310)">
    <rect x="0" y="0" width="230" height="105" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="26" rx="8" fill="#0284c7"/>
    <text x="115" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">ROLL -> AILERONS</text>
    <text x="12" y="44" font-size="10" fill="#f8fafc">• <tspan font-weight="bold">Axis:</tspan> Longitudinal (Nose to Tail)</text>
    <text x="12" y="60" font-size="10" fill="#f8fafc">• <tspan font-weight="bold">Surface:</tspan> Wingtip Ailerons</text>
    <text x="12" y="76" font-size="10" fill="#94a3b8">• <tspan font-weight="bold">Motion:</tspan> Opposite (one up, one down)</text>
    <text x="12" y="94" font-size="10" fill="#38bdf8">• <tspan font-weight="bold">Input:</tspan> Turn yoke / wheel left or right</text>
  </g>

  <!-- Card 2: PITCH / ELEVATORS -->
  <g transform="translate(285, 310)">
    <rect x="0" y="0" width="230" height="105" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="26" rx="8" fill="#d97706"/>
    <text x="115" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">PITCH -> ELEVATORS</text>
    <text x="12" y="44" font-size="10" fill="#f8fafc">• <tspan font-weight="bold">Axis:</tspan> Lateral (Wingtip to Wingtip)</text>
    <text x="12" y="60" font-size="10" fill="#f8fafc">• <tspan font-weight="bold">Surface:</tspan> Horizontal Tail Elevators</text>
    <text x="12" y="76" font-size="10" fill="#94a3b8">• <tspan font-weight="bold">Motion:</tspan> Symmetrical (both up/down)</text>
    <text x="12" y="94" font-size="10" fill="#f59e0b">• <tspan font-weight="bold">Input:</tspan> Push yoke fwd / Pull yoke back</text>
  </g>

  <!-- Card 3: YAW / RUDDER -->
  <g transform="translate(535, 310)">
    <rect x="0" y="0" width="230" height="105" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="26" rx="8" fill="#059669"/>
    <text x="115" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">YAW -> RUDDER</text>
    <text x="12" y="44" font-size="10" fill="#f8fafc">• <tspan font-weight="bold">Axis:</tspan> Vertical (Through CG)</text>
    <text x="12" y="60" font-size="10" fill="#f8fafc">• <tspan font-weight="bold">Surface:</tspan> Vertical Fin Rudder</text>
    <text x="12" y="76" font-size="10" fill="#94a3b8">• <tspan font-weight="bold">Motion:</tspan> Swings lateral (left / right)</text>
    <text x="12" y="94" font-size="10" fill="#34d399">• <tspan font-weight="bold">Input:</tspan> Depress left or right foot pedals</text>
  </g>
</svg>
""")

# SVG 3: Fixed-Wing vs Rotary-Wing Functional Comparison & Helicopter Torque Balance (Lesson 3, Page 4)
SVG_COMPARISON_TORQUE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Fixed-Wing vs. Rotary-Wing Architecture &amp; Anti-Torque Physics</text>
  <text x="400" y="61" font-size="12" fill="#94a3b8" text-anchor="middle">Structural Functional Families &amp; Newton's Third Law Torque Balance</text>

  <!-- Left: Fixed-Wing Airplane Characteristics -->
  <g transform="translate(35, 75)">
    <rect x="0" y="0" width="350" height="215" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="350" height="30" rx="10" fill="#0284c7"/>
    <text x="175" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">FIXED-WING (AIRPLANE) DESIGN</text>

    <!-- Schematic features list -->
    <g transform="translate(15, 45)">
      <circle cx="8" cy="8" r="5" fill="#38bdf8"/>
      <text x="22" y="12" font-size="11" font-weight="bold" fill="#f8fafc">Lift: Rigid Stationary Wings</text>
      <text x="22" y="27" font-size="10" fill="#94a3b8">Requires continuous forward airspeed to generate lift</text>
    </g>

    <g transform="translate(15, 85)">
      <circle cx="8" cy="8" r="5" fill="#38bdf8"/>
      <text x="22" y="12" font-size="11" font-weight="bold" fill="#f8fafc">Propulsion: Engine &amp; Propeller / Jet</text>
      <text x="22" y="27" font-size="10" fill="#94a3b8">Produces forward thrust to move wings through air</text>
    </g>

    <g transform="translate(15, 125)">
      <circle cx="8" cy="8" r="5" fill="#38bdf8"/>
      <text x="22" y="12" font-size="11" font-weight="bold" fill="#f8fafc">Stability &amp; Yaw: Empennage &amp; Rudder</text>
      <text x="22" y="27" font-size="10" fill="#94a3b8">Fixed tail fin provides directional flight alignment</text>
    </g>

    <g transform="translate(15, 165)">
      <circle cx="8" cy="8" r="5" fill="#38bdf8"/>
      <text x="22" y="12" font-size="11" font-weight="bold" fill="#f8fafc">Ground Support: Wheeled Undercarriage</text>
      <text x="22" y="27" font-size="10" fill="#94a3b8">Tricycle or tailwheel gear for runway takeoff roll</text>
    </g>
  </g>

  <!-- Right: Rotary-Wing Helicopter Characteristics -->
  <g transform="translate(415, 75)">
    <rect x="0" y="0" width="350" height="215" rx="10" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect x="0" y="0" width="350" height="30" rx="10" fill="#059669"/>
    <text x="175" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">ROTARY-WING (HELICOPTER) DESIGN</text>

    <!-- Schematic features list -->
    <g transform="translate(15, 45)">
      <circle cx="8" cy="8" r="5" fill="#34d399"/>
      <text x="22" y="12" font-size="11" font-weight="bold" fill="#f8fafc">Lift &amp; Thrust: Spinning Main Rotor</text>
      <text x="22" y="27" font-size="10" fill="#94a3b8">Rotating blades act as flying airfoils; allows hover</text>
    </g>

    <g transform="translate(15, 85)">
      <circle cx="8" cy="8" r="5" fill="#34d399"/>
      <text x="22" y="12" font-size="11" font-weight="bold" fill="#f8fafc">Yaw &amp; Anti-Torque: Tail Rotor</text>
      <text x="22" y="27" font-size="10" fill="#94a3b8">Pushes sideways to counteract engine torque reaction</text>
    </g>

    <g transform="translate(15, 125)">
      <circle cx="8" cy="8" r="5" fill="#34d399"/>
      <text x="22" y="12" font-size="11" font-weight="bold" fill="#f8fafc">Takeoff Profile: True Vertical (VTOL)</text>
      <text x="22" y="27" font-size="10" fill="#94a3b8">Zero runway required; operates in confined clearings</text>
    </g>

    <g transform="translate(15, 165)">
      <circle cx="8" cy="8" r="5" fill="#34d399"/>
      <text x="22" y="12" font-size="11" font-weight="bold" fill="#f8fafc">Ground Support: Tubular Landing Skids</text>
      <text x="22" y="27" font-size="10" fill="#94a3b8">Rugged, lightweight, safe on unpaved bush mud/rocks</text>
    </g>
  </g>

  <!-- Bottom: Newton's Third Law Torque Balance Diagram -->
  <g transform="translate(35, 305)">
    <rect x="0" y="0" width="730" height="115" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="20" y="24" font-size="12" font-weight="bold" fill="#facc15">NEWTON'S THIRD LAW &amp; HELICOPTER TORQUE BALANCE</text>

    <!-- Visual Representation of Forces -->
    <!-- Top-Down View Miniature Helicopter -->
    <g transform="translate(140, 68)">
      <!-- Fuselage -->
      <ellipse cx="0" cy="0" rx="35" ry="16" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
      <!-- Tail Boom -->
      <line x1="-35" y1="0" x2="-100" y2="0" stroke="#94a3b8" stroke-width="3"/>
      <!-- Tail Rotor -->
      <line x1="-100" y1="-12" x2="-100" y2="12" stroke="#34d399" stroke-width="3"/>

      <!-- Main Rotor Blade -->
      <line x1="-65" y1="-5" x2="65" y2="5" stroke="#38bdf8" stroke-width="3"/>
      <!-- Main Rotor Rotation Arrow (Clockwise) -->
      <path d="M -40 -18 A 45 45 0 0 1 40 -18" fill="none" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow_rotor)"/>
      <text x="0" y="-24" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Main Rotor Spin (Clockwise)</text>

      <!-- Fuselage Reaction Torque Arrow (Counter-Clockwise) -->
      <path d="M 20 18 A 24 24 0 0 1 -20 18" fill="none" stroke="#f87171" stroke-width="2" marker-end="url(#arrow_torque)"/>
      <text x="0" y="32" font-size="9" font-weight="bold" fill="#f87171" text-anchor="middle">Fuselage Torque Reaction (CCW)</text>

      <!-- Tail Rotor Sideways Thrust Arrow -->
      <line x1="-100" y1="0" x2="-100" y2="-28" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrow_tail)"/>
      <text x="-105" y="-32" font-size="9" font-weight="bold" fill="#34d399" text-anchor="middle">Tail Rotor Thrust</text>
    </g>

    <!-- Text Explanation on Right Side -->
    <g transform="translate(290, 42)">
      <text x="0" y="12" font-size="11" fill="#f8fafc">• <tspan font-weight="bold">Action:</tspan> The engine twists the main rotor clockwise to create lift.</text>
      <text x="0" y="30" font-size="11" fill="#f8fafc">• <tspan font-weight="bold">Reaction:</tspan> Equal and opposite torque tries to spin the fuselage counter-clockwise.</text>
      <text x="0" y="48" font-size="11" fill="#f8fafc">• <tspan font-weight="bold">Correction:</tspan> The tail rotor pushes sideways to cancel torque and maintain heading.</text>
      <text x="0" y="65" font-size="10" fill="#94a3b8">Varying tail rotor pitch via pedals allows the pilot to yaw left or right during hover.</text>
    </g>

    <defs>
      <marker id="arrow_rotor" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
        <path d="M 0 0 L 10 5 L 0 10 z" fill="#38bdf8"/>
      </marker>
      <marker id="arrow_torque" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
        <path d="M 0 0 L 10 5 L 0 10 z" fill="#f87171"/>
      </marker>
      <marker id="arrow_tail" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
        <path d="M 0 0 L 10 5 L 0 10 z" fill="#34d399"/>
      </marker>
    </defs>
  </g>
</svg>
""")

# =============================================================================
# ENRICHMENT ASSET REGISTRY
# =============================================================================

PHOTO_HOOKS = {
    0: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/51/Cessna_172_Skyhawk%2C_S2-AFH.jpg",
        "title": "A Cessna 172 Skyhawk on the Apron",
        "caption": "A classic high-wing light training aircraft displaying the fundamental structural components: semi-monocoque fuselage, high wing, empennage, and fixed tricycle landing gear.",
        "author": "Shadman Samee",
        "license": "Creative Commons Attribution-Share Alike 2.0 Generic"
    },
    1: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/6e/C-141C_Glass_Cockpit_Upgrade.JPEG",
        "title": "Advanced Aircraft Flight Deck and Control Systems",
        "caption": "A modernized multi-engine cockpit displaying the primary flight yokes, rudder pedals, engine throttles, and glass avionics displays that command flight control surfaces.",
        "author": "US Air Force",
        "license": "Public Domain"
    },
    2: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/78/Bell_206L-4_LongRanger_IV_over_Botafogo_Bay%2C_Rio_de_Janeiro.jpg",
        "title": "A Bell 206L LongRanger Rotary-Wing Aircraft in Flight",
        "caption": "A light turbine utility helicopter demonstrating key rotary-wing structural features: spinning overhead main rotor, anti-torque tail rotor on the tail boom, and tubular landing skids.",
        "author": "Renato Spilimbergo",
        "license": "Creative Commons Attribution-Share Alike 4.0 International"
    }
}

SVG_MAP = {
    0: {
        "svg": SVG_AIRCRAFT_ANATOMY,
        "title": "Aircraft Structural Anatomy: Framework & Components",
        "page": 4
    },
    1: {
        "svg": SVG_FLIGHT_AXES,
        "title": "Three Flight Axes and Primary Control Surface Deflections",
        "page": 4
    },
    2: {
        "svg": SVG_COMPARISON_TORQUE,
        "title": "Fixed-Wing vs Rotary-Wing Functional Comparison and Torque Balance",
        "page": 4
    }
}

YOUTUBE_VIDEOS = {
    0: {
        "url": "https://www.youtube.com/watch?v=_x5RhNQZrrg",
        "title": "Aircraft Components and Primary Structure Walkthrough",
        "description": "Examine the three-dimensional relationship between the semi-monocoque fuselage, wing internal spars and ribs, empennage stabilizers, and landing gear layout."
    },
    1: {
        "url": "https://www.youtube.com/watch?v=CAl3PayUW0M",
        "title": "Flight Controls and Aircraft Axes in Motion",
        "description": "Observe physical control surfaces deflecting on an active training aircraft as the pilot moves the cockpit yoke and rudder pedals through their full range of motion."
    },
    2: {
        "url": "https://www.youtube.com/watch?v=g9oVFRG1PGQ",
        "title": "How Aircraft Work: Aerodynamics and Propulsion",
        "description": "Explore the physical mechanisms of airflow over fixed wings versus rotating blades, illustrating how pressure differentials produce flight."
    }
}

def enrich_grade10_topic3():
    """Enriches Grade 10 Aviation Topic 249 with photographic hooks, SVGs, and videos."""
    print("=" * 80)
    print("VLEARN VISUAL ENRICHMENT: Grade 10 Aviation — Topic 3 (ID: 249)")
    print("Aircraft Components and Construction")
    print("=" * 80)

    curriculum = Curriculum.objects.get(id=5)
    grade = Grade.objects.get(id=5, level=10)
    subject = Subject.objects.get(id=44, grade=grade)
    topic = Topic.objects.get(id=249, subject=subject)

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
                            "topic_order": 2,
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
                            "topic_order": 2,
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
                            "topic_order": 2,
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
    print(f"ENRICHMENT COMPLETE: Topic 249 '{topic.name}'")
    print(f"  Photographic Hooks: {total_photos_attached} / 3")
    print(f"  Vector SVGs:        {total_svgs_attached} / 3")
    print(f"  YouTube Videos:     {total_videos_attached} / 3")
    print(f"  LessonAssets Total: {total_assets_persisted}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic3()
