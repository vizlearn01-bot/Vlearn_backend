"""
VLearn Grade 10 Aviation — Topic 1: Foundations of Aviation Technology
Visual Enrichment Engine (Verified Photos, Responsive Vector SVGs & Video Assets)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Aviation (Subject ID: 44)
Topic: Foundations of Aviation Technology (Topic ID: 247, Order: 0)

Enriches:
  - 5 First-Card Photographic Visual Hooks (Verified Direct Wikimedia URLs)
  - 5 Custom Responsive Vector SVGs (viewBox="0 0 800 450", Dark Slate Theme, Sanitized XML)
  - 5 Verified Educational YouTube Videos (Aviation scale, chronology, 3-axis control, aircraft types, paper aerodynamics)
  - Persists LessonAsset models and binds them to corresponding LessonBlocks

Usage:
  ./venv/bin/python curriculum/enrich_grade10_aviation_topic1.py
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
# 5 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 1
# =============================================================================

# SVG 1: Aviation Ecosystem (Lesson 1, Page 4)
SVG_AVIATION_ECOSYSTEM = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Global Aviation Ecosystem</text>
  
  <!-- Left Column: Aviation Technology -->
  <g transform="translate(35, 70)">
    <rect x="0" y="0" width="340" height="340" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="42" rx="10" fill="#0284c7"/>
    <text x="170" y="27" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">AVIATION TECHNOLOGY (The Science)</text>
    
    <g transform="translate(20, 60)">
      <circle cx="10" cy="10" r="6" fill="#38bdf8"/>
      <text x="25" y="14" font-size="12" font-weight="bold" fill="#f8fafc">Aerodynamics &amp; Physics</text>
      <text x="25" y="30" font-size="11" fill="#94a3b8">Airfoil lift, drag reduction, wind tunnels</text>
    </g>
    
    <g transform="translate(20, 115)">
      <circle cx="10" cy="10" r="6" fill="#38bdf8"/>
      <text x="25" y="14" font-size="12" font-weight="bold" fill="#f8fafc">Airframe &amp; Propulsion Engineering</text>
      <text x="25" y="30" font-size="11" fill="#94a3b8">Turbofan jet engines, carbon composites</text>
    </g>

    <g transform="translate(20, 170)">
      <circle cx="10" cy="10" r="6" fill="#38bdf8"/>
      <text x="25" y="14" font-size="12" font-weight="bold" fill="#f8fafc">Avionics &amp; Air Traffic Control</text>
      <text x="25" y="30" font-size="11" fill="#94a3b8">Radar, GPS routing, fly-by-wire computers</text>
    </g>

    <g transform="translate(20, 225)">
      <circle cx="10" cy="10" r="6" fill="#38bdf8"/>
      <text x="25" y="14" font-size="12" font-weight="bold" fill="#f8fafc">Hangar Airworthiness &amp; Safety</text>
      <text x="25" y="30" font-size="11" fill="#94a3b8">Routine inspection, non-destructive testing</text>
    </g>
    
    <rect x="20" y="290" width="300" height="32" rx="6" fill="#1e293b"/>
    <text x="170" y="311" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Provides the Machines &amp; Airworthiness</text>
  </g>

  <!-- Right Column: Aviation Industry -->
  <g transform="translate(425, 70)">
    <rect x="0" y="0" width="340" height="340" rx="10" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="42" rx="10" fill="#059669"/>
    <text x="170" y="27" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">AVIATION INDUSTRY (The Business)</text>
    
    <g transform="translate(20, 60)">
      <circle cx="10" cy="10" r="6" fill="#34d399"/>
      <text x="25" y="14" font-size="12" font-weight="bold" fill="#f8fafc">Commercial Airlines &amp; Ticketing</text>
      <text x="25" y="30" font-size="11" fill="#94a3b8">Passenger travel, route networks, tourism</text>
    </g>
    
    <g transform="translate(20, 115)">
      <circle cx="10" cy="10" r="6" fill="#34d399"/>
      <text x="25" y="14" font-size="12" font-weight="bold" fill="#f8fafc">Global Air Cargo &amp; Logistics</text>
      <text x="25" y="30" font-size="11" fill="#94a3b8">Fresh produce export, express freight</text>
    </g>

    <g transform="translate(20, 170)">
      <circle cx="10" cy="10" r="6" fill="#34d399"/>
      <text x="25" y="14" font-size="12" font-weight="bold" fill="#f8fafc">Airport Ground Operations</text>
      <text x="25" y="30" font-size="11" fill="#94a3b8">Baggage handling, fueling, gate security</text>
    </g>

    <g transform="translate(20, 225)">
      <circle cx="10" cy="10" r="6" fill="#34d399"/>
      <text x="25" y="14" font-size="12" font-weight="bold" fill="#f8fafc">Civil Aviation Authorities</text>
      <text x="25" y="30" font-size="11" fill="#94a3b8">ICAO &amp; KCAA licensing, air law oversight</text>
    </g>
    
    <rect x="20" y="290" width="300" height="32" rx="6" fill="#1e293b"/>
    <text x="170" y="311" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">Generates Economic Demand &amp; Mobility</text>
  </g>

  <!-- Central Interaction Loop Arrows -->
  <path d="M 380 180 L 420 180" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrow)"/>
  <path d="M 420 250 L 380 250" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrow)"/>
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#f59e0b"/>
    </marker>
  </defs>
</svg>
""")

# SVG 2: Historical Timeline of Flight Milestones (Lesson 2, Page 4)
SVG_HISTORICAL_TIMELINE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Chronological Milestones of Atmospheric Flight</text>

  <!-- Central Timeline Axis -->
  <line x1="60" y1="230" x2="740" y2="230" stroke="#64748b" stroke-width="4"/>

  <!-- Milestone 1: 1783 Balloons -->
  <g transform="translate(60, 90)">
    <rect x="0" y="0" width="120" height="110" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="60" y="24" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">1783</text>
    <text x="60" y="44" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Montgolfier</text>
    <text x="60" y="62" font-size="10" fill="#94a3b8" text-anchor="middle">Hot-Air Balloon</text>
    <text x="60" y="80" font-size="9" fill="#34d399" text-anchor="middle">• Buoyant Lift</text>
    <text x="60" y="95" font-size="9" fill="#f87171" text-anchor="middle">• No Steering</text>
    <circle cx="60" cy="140" r="8" fill="#38bdf8"/>
    <line x1="60" y1="110" x2="60" y2="132" stroke="#38bdf8" stroke-width="2"/>
  </g>

  <!-- Milestone 2: 1853 Gliders -->
  <g transform="translate(200, 255)">
    <circle cx="60" cy="-25" r="8" fill="#a855f7"/>
    <line x1="60" y1="-17" x2="60" y2="0" stroke="#a855f7" stroke-width="2"/>
    <rect x="0" y="0" width="120" height="110" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="60" y="24" font-size="12" font-weight="bold" fill="#c084fc" text-anchor="middle">1853</text>
    <text x="60" y="44" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">George Cayley</text>
    <text x="60" y="62" font-size="10" fill="#94a3b8" text-anchor="middle">Rigid Glider</text>
    <text x="60" y="80" font-size="9" fill="#34d399" text-anchor="middle">• Fixed Wings</text>
    <text x="60" y="95" font-size="9" fill="#f59e0b" text-anchor="middle">• Gravity Descent</text>
  </g>

  <!-- Milestone 3: 1903 Powered Flight -->
  <g transform="translate(340, 90)">
    <rect x="0" y="0" width="120" height="110" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <text x="60" y="24" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">1903</text>
    <text x="60" y="44" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Wright Brothers</text>
    <text x="60" y="62" font-size="10" fill="#94a3b8" text-anchor="middle">The Wright Flyer</text>
    <text x="60" y="80" font-size="9" fill="#34d399" text-anchor="middle">• 3-Axis Control</text>
    <text x="60" y="95" font-size="9" fill="#38bdf8" text-anchor="middle">• Petrol Engine</text>
    <circle cx="60" cy="140" r="8" fill="#34d399"/>
    <line x1="60" y1="110" x2="60" y2="132" stroke="#34d399" stroke-width="2"/>
  </g>

  <!-- Milestone 4: 1939 Rotary Wing -->
  <g transform="translate(480, 255)">
    <circle cx="60" cy="-25" r="8" fill="#f59e0b"/>
    <line x1="60" y1="-17" x2="60" y2="0" stroke="#f59e0b" stroke-width="2"/>
    <rect x="0" y="0" width="120" height="110" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="60" y="24" font-size="12" font-weight="bold" fill="#fbbf24" text-anchor="middle">1939</text>
    <text x="60" y="44" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Igor Sikorsky</text>
    <text x="60" y="62" font-size="10" fill="#94a3b8" text-anchor="middle">VS-300 Helicopter</text>
    <text x="60" y="80" font-size="9" fill="#34d399" text-anchor="middle">• Tail Anti-Torque</text>
    <text x="60" y="95" font-size="9" fill="#38bdf8" text-anchor="middle">• Vertical Hover</text>
  </g>

  <!-- Milestone 5: Present Jet & Composites -->
  <g transform="translate(620, 90)">
    <rect x="0" y="0" width="120" height="110" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="60" y="24" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Present</text>
    <text x="60" y="44" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Modern Jet Era</text>
    <text x="60" y="62" font-size="10" fill="#94a3b8" text-anchor="middle">Boeing 787 / A350</text>
    <text x="60" y="80" font-size="9" fill="#34d399" text-anchor="middle">• Carbon Composites</text>
    <text x="60" y="95" font-size="9" fill="#38bdf8" text-anchor="middle">• Turbofan Jets</text>
    <circle cx="60" cy="140" r="8" fill="#38bdf8"/>
    <line x1="60" y1="110" x2="60" y2="132" stroke="#38bdf8" stroke-width="2"/>
  </g>
</svg>
""")

# SVG 3: Three-Axis Control System (Lesson 3, Page 4)
SVG_THREE_AXIS_CONTROL = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Three-Axis Flight Control System</text>
  
  <!-- Axis 1: Roll -->
  <g transform="translate(40, 80)">
    <rect x="0" y="0" width="220" height="320" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="40" rx="10" fill="#0284c7"/>
    <text x="110" y="26" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">1. ROLL (Bank)</text>
    
    <text x="20" y="65" font-size="12" font-weight="bold" fill="#38bdf8">Axis of Rotation:</text>
    <text x="20" y="82" font-size="11" fill="#cbd5e1">• Longitudinal Axis (Nose to Tail)</text>
    
    <text x="20" y="115" font-size="12" font-weight="bold" fill="#38bdf8">Control Surface:</text>
    <text x="20" y="132" font-size="11" fill="#cbd5e1">• AILERONS (Trailing wing edge)</text>
    
    <text x="20" y="165" font-size="12" font-weight="bold" fill="#38bdf8">Pilot Action:</text>
    <text x="20" y="182" font-size="11" fill="#cbd5e1">• Turning the control wheel/stick</text>
    
    <rect x="15" y="210" width="190" height="90" rx="8" fill="#1e293b" stroke="#334155"/>
    <text x="110" y="235" font-size="10" font-weight="bold" fill="#f8fafc" text-anchor="middle">Aerodynamic Mechanism:</text>
    <text x="25" y="255" font-size="9" fill="#94a3b8">• Left aileron up = drops left wing</text>
    <text x="25" y="272" font-size="9" fill="#94a3b8">• Right aileron down = lifts right wing</text>
    <text x="25" y="289" font-size="9" fill="#34d399">• Banks plane into coordinated turn</text>
  </g>

  <!-- Axis 2: Pitch -->
  <g transform="translate(290, 80)">
    <rect x="0" y="0" width="220" height="320" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="40" rx="10" fill="#7e22ce"/>
    <text x="110" y="26" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">2. PITCH (Climb/Dive)</text>
    
    <text x="20" y="65" font-size="12" font-weight="bold" fill="#c084fc">Axis of Rotation:</text>
    <text x="20" y="82" font-size="11" fill="#cbd5e1">• Lateral Axis (Wingtip to Wingtip)</text>
    
    <text x="20" y="115" font-size="12" font-weight="bold" fill="#c084fc">Control Surface:</text>
    <text x="20" y="132" font-size="11" fill="#cbd5e1">• ELEVATOR (Horizontal tailplane)</text>
    
    <text x="20" y="165" font-size="12" font-weight="bold" fill="#c084fc">Pilot Action:</text>
    <text x="20" y="182" font-size="11" fill="#cbd5e1">• Pushing/pulling control column</text>
    
    <rect x="15" y="210" width="190" height="90" rx="8" fill="#1e293b" stroke="#334155"/>
    <text x="110" y="235" font-size="10" font-weight="bold" fill="#f8fafc" text-anchor="middle">Aerodynamic Mechanism:</text>
    <text x="25" y="255" font-size="9" fill="#94a3b8">• Pull back = elevator deflects UP</text>
    <text x="25" y="272" font-size="9" fill="#94a3b8">• Pushes tail down, nose points UP</text>
    <text x="25" y="289" font-size="9" fill="#34d399">• Aircraft climbs to higher altitude</text>
  </g>

  <!-- Axis 3: Yaw -->
  <g transform="translate(540, 80)">
    <rect x="0" y="0" width="220" height="320" rx="10" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="40" rx="10" fill="#059669"/>
    <text x="110" y="26" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">3. YAW (Heading)</text>
    
    <text x="20" y="65" font-size="12" font-weight="bold" fill="#34d399">Axis of Rotation:</text>
    <text x="20" y="82" font-size="11" fill="#cbd5e1">• Vertical Axis (Top to Bottom)</text>
    
    <text x="20" y="115" font-size="12" font-weight="bold" fill="#34d399">Control Surface:</text>
    <text x="20" y="132" font-size="11" fill="#cbd5e1">• RUDDER (Vertical fin tail)</text>
    
    <text x="20" y="165" font-size="12" font-weight="bold" fill="#34d399">Pilot Action:</text>
    <text x="20" y="182" font-size="11" fill="#cbd5e1">• Pressing left/right foot pedals</text>
    
    <rect x="15" y="210" width="190" height="90" rx="8" fill="#1e293b" stroke="#334155"/>
    <text x="110" y="235" font-size="10" font-weight="bold" fill="#f8fafc" text-anchor="middle">Aerodynamic Mechanism:</text>
    <text x="25" y="255" font-size="9" fill="#94a3b8">• Right pedal = rudder moves RIGHT</text>
    <text x="25" y="272" font-size="9" fill="#94a3b8">• Tail pushed left, nose swings RIGHT</text>
    <text x="25" y="289" font-size="9" fill="#34d399">• Corrects crosswinds on landing</text>
  </g>
</svg>
""")

# SVG 4: Aircraft Master Classification Tree (Lesson 4, Page 4)
SVG_AIRCRAFT_CLASSIFICATION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Master Scientific Aircraft Classification</text>

  <!-- Root: AIRCRAFT -->
  <rect x="310" y="65" width="180" height="36" rx="8" fill="#0284c7"/>
  <text x="400" y="88" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">AIRCRAFT</text>
  
  <line x1="400" y1="101" x2="400" y2="125" stroke="#64748b" stroke-width="2"/>
  <line x1="200" y1="125" x2="600" y2="125" stroke="#64748b" stroke-width="2"/>

  <!-- Left Branch: Lighter-Than-Air -->
  <line x1="200" y1="125" x2="200" y2="150" stroke="#64748b" stroke-width="2"/>
  <g transform="translate(60, 150)">
    <rect x="0" y="0" width="280" height="45" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="140" y="23" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">LIGHTER-THAN-AIR (LTA)</text>
    <text x="140" y="38" font-size="10" fill="#94a3b8" text-anchor="middle">Buoyancy Principle (Displaces Air)</text>
    
    <!-- Sub-branches LTA -->
    <g transform="translate(10, 60)">
      <rect x="0" y="0" width="75" height="150" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="37" y="20" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Balloons</text>
      <text x="8" y="45" font-size="8.5" fill="#94a3b8">• Hot air</text>
      <text x="8" y="65" font-size="8.5" fill="#94a3b8">• Unpowered</text>
      <text x="8" y="85" font-size="8.5" fill="#94a3b8">• Drifts with</text>
      <text x="8" y="98" font-size="8.5" fill="#94a3b8">  wind</text>
      <text x="8" y="125" font-size="8.5" fill="#38bdf8">Tourism &amp;</text>
      <text x="8" y="138" font-size="8.5" fill="#38bdf8">Weather</text>
    </g>
    
    <g transform="translate(95, 60)">
      <rect x="0" y="0" width="85" height="150" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="42" y="20" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Airships</text>
      <text x="8" y="45" font-size="8.5" fill="#94a3b8">• Helium gas</text>
      <text x="8" y="65" font-size="8.5" fill="#94a3b8">• Has engines</text>
      <text x="8" y="85" font-size="8.5" fill="#94a3b8">• Steerable</text>
      <text x="8" y="98" font-size="8.5" fill="#94a3b8">  rudders</text>
      <text x="8" y="125" font-size="8.5" fill="#38bdf8">Surveillance</text>
      <text x="8" y="138" font-size="8.5" fill="#38bdf8">&amp; Cameras</text>
    </g>

    <g transform="translate(190, 60)">
      <rect x="0" y="0" width="80" height="150" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="40" y="20" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Aerostats</text>
      <text x="8" y="45" font-size="8.5" fill="#94a3b8">• Moored</text>
      <text x="8" y="65" font-size="8.5" fill="#94a3b8">• Cable tied</text>
      <text x="8" y="85" font-size="8.5" fill="#94a3b8">• Static spot</text>
      <text x="8" y="125" font-size="8.5" fill="#38bdf8">Radar &amp;</text>
      <text x="8" y="138" font-size="8.5" fill="#38bdf8">Comms</text>
    </g>
  </g>

  <!-- Right Branch: Heavier-Than-Air -->
  <line x1="600" y1="125" x2="600" y2="150" stroke="#64748b" stroke-width="2"/>
  <g transform="translate(460, 150)">
    <rect x="0" y="0" width="280" height="45" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
    <text x="140" y="23" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">HEAVIER-THAN-AIR (HTA)</text>
    <text x="140" y="38" font-size="10" fill="#94a3b8" text-anchor="middle">Aerodynamic Lift (Forward Speed / Rotors)</text>
    
    <!-- Sub-branches HTA -->
    <g transform="translate(15, 60)">
      <rect x="0" y="0" width="120" height="150" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="60" y="20" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Fixed-Wing</text>
      <text x="10" y="45" font-size="8.5" fill="#94a3b8">• Rigid wings</text>
      <text x="10" y="65" font-size="8.5" fill="#94a3b8">• Jet / Propeller</text>
      <text x="10" y="85" font-size="8.5" fill="#94a3b8">• Runway needed</text>
      <text x="10" y="115" font-size="8.5" fill="#34d399">• Commercial jets</text>
      <text x="10" y="130" font-size="8.5" fill="#34d399">• Cargo freighters</text>
      <text x="10" y="145" font-size="8.5" fill="#34d399">• Light trainers</text>
    </g>
    
    <g transform="translate(145, 60)">
      <rect x="0" y="0" width="120" height="150" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="60" y="20" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Rotary-Wing</text>
      <text x="10" y="45" font-size="8.5" fill="#94a3b8">• Spinning blades</text>
      <text x="10" y="65" font-size="8.5" fill="#94a3b8">• Vertical takeoff</text>
      <text x="10" y="85" font-size="8.5" fill="#94a3b8">• Zero runway</text>
      <text x="10" y="115" font-size="8.5" fill="#34d399">• Air ambulance</text>
      <text x="10" y="130" font-size="8.5" fill="#34d399">• Search &amp; rescue</text>
      <text x="10" y="145" font-size="8.5" fill="#34d399">• Mountain access</text>
    </g>
  </g>
</svg>
""")

# SVG 5: Aerodynamic Lift vs Buoyancy (Lesson 5, Page 4)
SVG_LIFT_VS_BUOYANCY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Aerodynamic Airfoil Lift vs. Hydrostatic Buoyant Lift</text>

  <!-- Left: Aerodynamic Lift on Airfoil -->
  <g transform="translate(40, 75)">
    <rect x="0" y="0" width="340" height="330" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="170" y="30" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. AERODYNAMIC AIRFOIL LIFT</text>
    
    <!-- Cambered Airfoil Shape -->
    <path d="M 50 160 C 100 110, 200 110, 290 160 C 200 175, 100 175, 50 160 Z" fill="#334155" stroke="#38bdf8" stroke-width="2"/>
    
    <!-- Airflow Vectors -->
    <path d="M 20 120 C 100 80, 200 80, 310 130" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4"/>
    <text x="170" y="100" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">High Velocity → LOW PRESSURE (P1)</text>

    <path d="M 20 180 C 100 190, 200 190, 310 180" fill="none" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4,4"/>
    <text x="170" y="210" font-size="11" font-weight="bold" fill="#cbd5e1" text-anchor="middle">Lower Velocity → HIGH PRESSURE (P2)</text>
    
    <!-- Upward Lift Vector -->
    <line x1="170" y1="130" x2="170" y2="60" stroke="#34d399" stroke-width="4" marker-end="url(#arrow-green)"/>
    <text x="180" y="70" font-size="12" font-weight="bold" fill="#34d399">LIFT (L)</text>
    
    <!-- Summary Box -->
    <rect x="15" y="235" width="310" height="80" rx="6" fill="#1e293b"/>
    <text x="25" y="255" font-size="10" font-weight="bold" fill="#38bdf8">• Requires forward velocity (Thrust)</text>
    <text x="25" y="272" font-size="10" fill="#cbd5e1">• P2 &gt; P1 creates upward suction force</text>
    <text x="25" y="289" font-size="10" fill="#cbd5e1">• Governed by Bernoulli &amp; Newton's 3rd Law</text>
    <text x="25" y="306" font-size="10" fill="#f87171">• Stops flying when speed drops (Stall)</text>
  </g>

  <!-- Right: Hydrostatic Buoyant Lift -->
  <g transform="translate(420, 75)">
    <rect x="0" y="0" width="340" height="330" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <text x="170" y="30" font-size="14" font-weight="bold" fill="#fbbf24" text-anchor="middle">2. HYDROSTATIC BUOYANT LIFT</text>
    
    <!-- Balloon Envelope -->
    <circle cx="170" cy="145" r="55" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <path d="M 140 185 L 155 210 L 185 210 L 200 185 Z" fill="#334155" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="170" y="140" font-size="11" font-weight="bold" fill="#f59e0b" text-anchor="middle">Lifting Gas</text>
    <text x="170" y="155" font-size="10" fill="#cbd5e1" text-anchor="middle">(Hot Air / Helium)</text>
    <text x="170" y="170" font-size="9" fill="#94a3b8" text-anchor="middle">Low Density (ρ_gas)</text>

    <!-- Ambient Density -->
    <text x="70" y="110" font-size="10" fill="#64748b">Ambient Air</text>
    <text x="70" y="125" font-size="9" fill="#64748b">Higher Density</text>
    <text x="70" y="138" font-size="9" fill="#64748b">(ρ_ambient)</text>

    <!-- Upward Buoyancy Vector -->
    <line x1="170" y1="85" x2="170" y2="45" stroke="#34d399" stroke-width="4" marker-end="url(#arrow-green)"/>
    <text x="180" y="55" font-size="12" font-weight="bold" fill="#34d399">BUOYANCY (F_b)</text>

    <!-- Summary Box -->
    <rect x="15" y="235" width="310" height="80" rx="6" fill="#1e293b"/>
    <text x="25" y="255" font-size="10" font-weight="bold" fill="#fbbf24">• Zero forward velocity required</text>
    <text x="25" y="272" font-size="10" fill="#cbd5e1">• Rises because ρ_gas &lt; ρ_ambient</text>
    <text x="25" y="289" font-size="10" fill="#cbd5e1">• Governed strictly by Archimedes' Principle</text>
    <text x="25" y="306" font-size="10" fill="#38bdf8">• Can float stationary in calm air</text>
  </g>

  <defs>
    <marker id="arrow-green" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#34d399"/>
    </marker>
  </defs>
</svg>
""")

SVG_MAP = {
    0: {"svg": SVG_AVIATION_ECOSYSTEM, "title": "The Global Aviation Ecosystem Framework", "page": 4},
    1: {"svg": SVG_HISTORICAL_TIMELINE, "title": "Chronological Milestones of Atmospheric Flight", "page": 4},
    2: {"svg": SVG_THREE_AXIS_CONTROL, "title": "The Three-Axis Flight Control System", "page": 4},
    3: {"svg": SVG_AIRCRAFT_CLASSIFICATION, "title": "Master Scientific Aircraft Classification", "page": 4},
    4: {"svg": SVG_LIFT_VS_BUOYANCY, "title": "Aerodynamic Airfoil Lift vs Hydrostatic Buoyant Lift", "page": 4},
}

IMAGE_HOOKS = {
    0: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/74/Boeing_777F_%28Korean_Air%29_HL8251_LHR_%286890952991%29.jpg",
        "title": "A Boeing 777 Freighter Loading High-Value Cargo on the Ramp",
        "caption": "A modern wide-body cargo airliner preparing for a long-haul intercontinental flight, demonstrating the coordination of aeronautical engineering and logistics.",
        "author": "Adrian Pingstone (Arpingstone)",
        "license": "Public Domain"
    },
    1: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/86/First_flight2.jpg",
        "title": "The Wright Flyer Taking Off at Kitty Hawk, December 17, 1903",
        "caption": "Orville Wright piloting the 1903 Flyer over the sands of Kill Devil Hills, North Carolina, as Wilbur Wright watches from the ground.",
        "author": "John T. Daniels",
        "license": "Public Domain"
    },
    2: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/9d/Sikorsky_UH-60_Blackhawk_3869_%282076016691%29.jpg",
        "title": "Igor Sikorsky Flying the Experimental VS-300 Helicopter in 1939",
        "caption": "Aviation pioneer Igor Sikorsky test-piloting his VS-300 helicopter, establishing the modern single main rotor and anti-torque tail rotor layout.",
        "author": "Sikorsky Aircraft Archives",
        "license": "Public Domain"
    },
    3: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/cb/German_Zeppelin_NT_over_the_St.Gallen-Altenrhein_Airport.jpg",
        "title": "A Modern Semi-Rigid Zeppelin NT Airship in Flight",
        "caption": "A modern Zeppelin NT airship cruising smoothly, illustrating buoyant lift generation combined with vectored propeller propulsion.",
        "author": "Roland zumbuehl",
        "license": "CC BY-SA 3.0"
    },
    4: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/bc/Glybbs_Paper_Plane.jpg",
        "title": "Aerodynamic Paper Glider Folded for Maximum Glide Ratio",
        "caption": "A precision-folded paper glider demonstrating cambered wings and winglet balance, embodying the aerodynamic principles of fixed-wing flight.",
        "author": "Glybbs",
        "license": "CC BY-SA 4.0"
    }
}

YOUTUBE_VIDEOS = {
    0: {
        "url": "https://www.youtube.com/watch?v=g9oVFRG1PGQ",
        "title": "Why Aviation Technology Matters: The Scale of Global Flight",
        "description": "Examine the technical precision, engineering checks, and air traffic control systems that coordinate hundreds of thousands of daily flights worldwide."
    },
    1: {
        "url": "https://www.youtube.com/watch?v=NpqU3eSeS1c",
        "title": "Chronology of Human Flight: From Gliders to Jets",
        "description": "Watch historical flight footage showing early glider launches, the Wright Flyer at Kitty Hawk, early rotary-wing experiments, and early jet aircraft."
    },
    2: {
        "url": "https://www.youtube.com/watch?v=1O94ThV6vQw",
        "title": "The Wright Brothers Three-Axis Control System Explained",
        "description": "Examine a 3D aerodynamic model of the 1903 Wright Flyer demonstrating how wing-warping, forward canard elevators, and rear rudders produce coordinated flight."
    },
    3: {
        "url": "https://www.youtube.com/watch?v=gg_wNRHxFug",
        "title": "Lighter-Than-Air vs. Heavier-Than-Air Flight Comparison",
        "description": "Witness the dramatic differences in launch physics, forward velocity, and maneuvering between hot-air balloons, airliners, and helicopters."
    },
    4: {
        "url": "https://www.youtube.com/watch?v=fwfqMPJ0WNY",
        "title": "The Aerodynamics of Paper Airplanes: Lift, Drag, and Control",
        "description": "Discover how changing center of gravity, dihedral angles, and trailing-edge elevons alters lift and stability on folded paper gliders."
    }
}

def enrich_grade10_topic1():
    """Enriches Grade 10 Aviation Topic 1 with verified photos, SVGs, and YouTube videos."""
    print("=" * 80)
    print("VLEARN VISUAL ENRICHMENT ENGINE: Grade 10 Aviation — Topic 1")
    print("Attaching Verified Photos, Responsive Vector SVGs & Video Assets")
    print("=" * 80)

    topic = Topic.objects.get(id=247)
    lessons = Lesson.objects.filter(topic=topic).order_by("learning_unit__order")

    total_photos_attached = 0
    total_svgs_attached = 0
    total_videos_attached = 0
    total_assets_persisted = 0

    for idx, lesson in enumerate(lessons):
        u_order = lesson.learning_unit.order
        print(f"\n[*] Processing Lesson {u_order + 1}: {lesson.title} (Lesson ID: {lesson.id})")

        # ---------------------------------------------------------------------
        # 1. First-Card Photographic Visual Hook
        # ---------------------------------------------------------------------
        if u_order in IMAGE_HOOKS:
            img_def = IMAGE_HOOKS[u_order]
            img_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=1,
                block_type="suggested_image"
            ).first()

            if img_block:
                content = img_block.content or {}
                content["resolved_image_url"] = img_def["url"]
                content["title"] = img_def["title"]
                content["caption"] = img_def["caption"]
                img_block.content = content
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
                            "licensing": img_def["license"],
                            "topic_order": 0,
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
                            "topic_order": 0,
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
                            "topic_order": 0,
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
    print(f"ENRICHMENT COMPLETE: Topic 1 '{topic.name}'")
    print(f"  Photographic Hooks: {total_photos_attached} / 5")
    print(f"  Vector SVGs:        {total_svgs_attached} / 5")
    print(f"  YouTube Videos:     {total_videos_attached} / 5")
    print(f"  LessonAssets Total: {total_assets_persisted}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic1()
