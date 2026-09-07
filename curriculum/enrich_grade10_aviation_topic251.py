"""
VLearn Grade 10 Aviation — Topic 251: Airport Safety and Operations
Visual Enrichment Engine (Verified Photos, Responsive Vector SVGs & Video Assets)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Aviation (Subject ID: 44)
Topic: Airport Safety and Operations (Topic ID: 251, Order: 4)

Enriches:
  - 5 First-Card Photographic Visual Hooks (Verified Direct Wikimedia URLs)
  - 5 Custom Responsive Vector SVGs (viewBox="0 0 800 450", Dark Slate Theme, Sanitized XML)
  - 5 Verified Educational YouTube Videos (Airport zones, fueling safety, airfield signs, CPR, human factors)
  - Persists LessonAsset models and binds them to corresponding LessonBlocks

Usage:
  ./venv/bin/python curriculum/enrich_grade10_aviation_topic251.py
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
# 5 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 251
# =============================================================================

# SVG 1: Airport 3-Zone Architecture (Lesson 1, Page 4)
SVG_AIRPORT_3_ZONES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <!-- Container Card -->
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Airport Three-Zone Security &amp; Operational Architecture</text>
  
  <!-- Zone 1: Landside (Green) -->
  <g transform="translate(35, 70)">
    <rect x="0" y="0" width="225" height="290" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <rect x="0" y="0" width="225" height="40" rx="10" fill="#047857"/>
    <text x="112" y="26" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">1. LANDSIDE (Public)</text>
    
    <g transform="translate(15, 55)">
      <circle cx="8" cy="8" r="5" fill="#10b981"/>
      <text x="22" y="12" font-size="11" font-weight="bold" fill="#f8fafc">Public Roadways</text>
      <text x="22" y="27" font-size="10" fill="#94a3b8">Curbside taxi &amp; bus drops</text>
    </g>
    
    <g transform="translate(15, 100)">
      <circle cx="8" cy="8" r="5" fill="#10b981"/>
      <text x="22" y="12" font-size="11" font-weight="bold" fill="#f8fafc">Vehicle Screening</text>
      <text x="22" y="27" font-size="10" fill="#94a3b8">Outer gate security checks</text>
    </g>

    <g transform="translate(15, 145)">
      <circle cx="8" cy="8" r="5" fill="#10b981"/>
      <text x="22" y="12" font-size="11" font-weight="bold" fill="#f8fafc">Public Car Parks</text>
      <text x="22" y="27" font-size="10" fill="#94a3b8">Short &amp; long term garages</text>
    </g>

    <g transform="translate(15, 190)">
      <circle cx="8" cy="8" r="5" fill="#10b981"/>
      <text x="22" y="12" font-size="11" font-weight="bold" fill="#f8fafc">Unrestricted Entry</text>
      <text x="22" y="27" font-size="10" fill="#94a3b8">No ticket or badge required</text>
    </g>
    
    <rect x="15" y="245" width="195" height="30" rx="6" fill="#1e293b"/>
    <text x="112" y="265" font-size="10" font-weight="bold" fill="#10b981" text-anchor="middle">Access: General Public</text>
  </g>

  <!-- Zone 2: Terminal Building (Amber) -->
  <g transform="translate(285, 70)">
    <rect x="0" y="0" width="230" height="290" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect x="0" y="0" width="230" height="40" rx="10" fill="#b45309"/>
    <text x="115" y="26" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">2. TERMINAL (Transition)</text>
    
    <g transform="translate(15, 55)">
      <circle cx="8" cy="8" r="5" fill="#f59e0b"/>
      <text x="22" y="12" font-size="11" font-weight="bold" fill="#f8fafc">Check-In Hall</text>
      <text x="22" y="27" font-size="10" fill="#94a3b8">Ticketing &amp; hold baggage</text>
    </g>
    
    <g transform="translate(15, 100)">
      <circle cx="8" cy="8" r="5" fill="#f59e0b"/>
      <text x="22" y="12" font-size="11" font-weight="bold" fill="#f8fafc">Security Filter</text>
      <text x="22" y="27" font-size="10" fill="#94a3b8">Metal detectors &amp; X-ray</text>
    </g>

    <g transform="translate(15, 145)">
      <circle cx="8" cy="8" r="5" fill="#f59e0b"/>
      <text x="22" y="12" font-size="11" font-weight="bold" fill="#f8fafc">Immigration &amp; Customs</text>
      <text x="22" y="27" font-size="10" fill="#94a3b8">Passport &amp; border control</text>
    </g>

    <g transform="translate(15, 190)">
      <circle cx="8" cy="8" r="5" fill="#f59e0b"/>
      <text x="22" y="12" font-size="11" font-weight="bold" fill="#f8fafc">Departure Lounges</text>
      <text x="22" y="27" font-size="10" fill="#94a3b8">Screened boarding gates</text>
    </g>
    
    <rect x="15" y="245" width="200" height="30" rx="6" fill="#1e293b"/>
    <text x="115" y="265" font-size="10" font-weight="bold" fill="#f59e0b" text-anchor="middle">Access: Ticketed / Screened</text>
  </g>

  <!-- Zone 3: Airside (Red) -->
  <g transform="translate(540, 70)">
    <rect x="0" y="0" width="225" height="290" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="225" height="40" rx="10" fill="#b91c1c"/>
    <text x="112" y="26" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">3. AIRSIDE (Restricted)</text>
    
    <g transform="translate(15, 55)">
      <circle cx="8" cy="8" r="5" fill="#ef4444"/>
      <text x="22" y="12" font-size="11" font-weight="bold" fill="#f8fafc">Aircraft Parking Apron</text>
      <text x="22" y="27" font-size="10" fill="#94a3b8">Refueling, loading, catering</text>
    </g>
    
    <g transform="translate(15, 100)">
      <circle cx="8" cy="8" r="5" fill="#ef4444"/>
      <text x="22" y="12" font-size="11" font-weight="bold" fill="#f8fafc">Active Taxiways</text>
      <text x="22" y="27" font-size="10" fill="#94a3b8">Surface maneuvering paths</text>
    </g>

    <g transform="translate(15, 145)">
      <circle cx="8" cy="8" r="5" fill="#ef4444"/>
      <text x="22" y="12" font-size="11" font-weight="bold" fill="#f8fafc">Active Runways</text>
      <text x="22" y="27" font-size="10" fill="#94a3b8">High-speed takeoff / landing</text>
    </g>

    <g transform="translate(15, 190)">
      <circle cx="8" cy="8" r="5" fill="#ef4444"/>
      <text x="22" y="12" font-size="11" font-weight="bold" fill="#f8fafc">Hangars &amp; Fuel Farm</text>
      <text x="22" y="27" font-size="10" fill="#94a3b8">Heavy aircraft maintenance</text>
    </g>
    
    <rect x="15" y="245" width="195" height="30" rx="6" fill="#1e293b"/>
    <text x="112" y="265" font-size="10" font-weight="bold" fill="#ef4444" text-anchor="middle">Access: Authorized Personnel Only</text>
  </g>

  <!-- Flow Arrows between Zones -->
  <path d="M 265 210 L 280 210" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)" fill="none"/>
  <path d="M 520 210 L 535 210" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)" fill="none"/>

  <!-- Bottom Physical Security Perimeter Banner -->
  <g transform="translate(35, 375)">
    <rect x="0" y="0" width="730" height="42" rx="8" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
    <text x="365" y="18" font-size="11" font-weight="bold" fill="#e2e8f0" text-anchor="middle">Physical Security Perimeter: High-Tensile Steel Security Fence, CCTV Coverage &amp; Guarded Gates</text>
    <text x="365" y="33" font-size="10" fill="#94a3b8" text-anchor="middle">Strict One-Way Passenger Flow | Unaccompanied Airside Trespass is a Severe Aviation Crime</text>
  </g>
</svg>
""")

# SVG 2: FOD Turbine Ingestion Vector & Refueling Grounding Circuit (Lesson 2, Page 4)
SVG_FOD_AND_REFUELING = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Airside Hazards: FOD Engine Ingestion &amp; Refueling Static Bonding</text>

  <!-- Left Half: FOD Ingestion Vector -->
  <g transform="translate(35, 70)">
    <rect x="0" y="0" width="350" height="340" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="350" height="38" rx="10" fill="#991b1b"/>
    <text x="175" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">FOD TURBINE INGESTION VECTOR</text>

    <!-- Jet Engine Nacelle Cross Section -->
    <path d="M 40 100 Q 140 85 240 95 L 240 210 Q 140 220 40 205 Z" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
    <!-- Spinner & Fan Blades -->
    <ellipse cx="140" cy="150" rx="18" ry="45" fill="#475569" stroke="#38bdf8" stroke-width="2"/>
    <path d="M 140 150 L 110 120 M 140 150 L 110 180 M 140 150 L 170 120 M 140 150 L 170 180" stroke="#38bdf8" stroke-width="3"/>
    <text x="140" y="80" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Turbofan Intake (15,000 RPM)</text>

    <!-- Intake Air Vortex -->
    <path d="M 30 130 C 70 140 90 148 130 150" stroke="#0ea5e9" stroke-width="2" stroke-dasharray="4,3" fill="none"/>
    <path d="M 30 170 C 70 160 90 152 130 150" stroke="#0ea5e9" stroke-width="2" stroke-dasharray="4,3" fill="none"/>

    <!-- Loose Debris (FOD Bolt) -->
    <g transform="translate(50, 240)">
      <rect x="0" y="0" width="16" height="8" rx="2" fill="#f59e0b"/>
      <rect x="16" y="2" width="14" height="4" fill="#d97706"/>
      <text x="40" y="8" font-size="10" font-weight="bold" fill="#f59e0b">Loose Bolt / Stone (FOD)</text>
    </g>
    <!-- Ingestion Trajectory Arrow -->
    <path d="M 70 235 Q 100 180 130 155" stroke="#ef4444" stroke-width="3" stroke-dasharray="4,2" fill="none"/>
    
    <!-- Impact Fracture Explosion Icon -->
    <circle cx="140" cy="150" r="14" fill="#dc2626" opacity="0.8"/>
    <text x="140" y="154" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">X</text>

    <!-- Hazard Outcome Box -->
    <rect x="15" y="270" width="320" height="55" rx="6" fill="#1e293b"/>
    <text x="25" y="290" font-size="11" font-weight="bold" fill="#fca5a5">Catastrophic Consequence:</text>
    <text x="25" y="306" font-size="10" fill="#cbd5e1">Compressor blade fragmentation -> In-flight flameout</text>
    <text x="25" y="320" font-size="10" fill="#94a3b8">Defense: Daily mandatory walk-downs &amp; magnetic sweeps</text>
  </g>

  <!-- Right Half: Fueling Grounding Circuit -->
  <g transform="translate(415, 70)">
    <rect x="0" y="0" width="350" height="340" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <rect x="0" y="0" width="350" height="38" rx="10" fill="#065f46"/>
    <text x="175" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">REFUELING STATIC BONDING CIRCUIT</text>

    <!-- Aircraft Wing Schematic -->
    <path d="M 40 100 L 200 100 L 220 125 L 40 125 Z" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
    <text x="120" y="92" font-size="10" font-weight="bold" fill="#e2e8f0" text-anchor="middle">Aircraft Fuel Tank (Wing)</text>

    <!-- Fuel Truck Schematic -->
    <rect x="230" y="170" width="90" height="50" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="250" cy="225" r="10" fill="#475569"/>
    <circle cx="300" cy="225" r="10" fill="#475569"/>
    <text x="275" y="200" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Fuel Bowser</text>

    <!-- Fuel Delivery Hose -->
    <path d="M 230 190 Q 180 180 160 125" stroke="#475569" stroke-width="6" fill="none"/>
    <text x="195" y="165" font-size="9" fill="#94a3b8">Fuel Hose</text>

    <!-- Static Bonding Wire (Truck to Airframe) -->
    <path d="M 240 170 Q 200 145 180 125" stroke="#eab308" stroke-width="2.5" stroke-dasharray="6,3" fill="none"/>
    <circle cx="180" cy="125" r="4" fill="#eab308"/>
    <circle cx="240" cy="170" r="4" fill="#eab308"/>
    <text x="190" y="140" font-size="9" font-weight="bold" fill="#facc15">Bonding Wire</text>

    <!-- Earth Ground Stake & Concrete Pad -->
    <rect x="20" y="240" width="310" height="15" fill="#334155"/>
    <text x="175" y="252" font-size="9" fill="#94a3b8" text-anchor="middle">Apron Concrete Pad</text>
    <line x1="120" y1="240" x2="120" y2="265" stroke="#10b981" stroke-width="4"/>
    <!-- Ground Stake Cable to Truck -->
    <path d="M 270 220 Q 200 240 120 242" stroke="#10b981" stroke-width="2.5" fill="none"/>
    <text x="135" y="235" font-size="9" font-weight="bold" fill="#34d399">Earth Ground Stake</text>

    <!-- Safety Mechanism Box -->
    <rect x="15" y="270" width="320" height="55" rx="6" fill="#1e293b"/>
    <text x="25" y="290" font-size="11" font-weight="bold" fill="#86efac">Electrostatic Discharge Circuit:</text>
    <text x="25" y="306" font-size="10" fill="#cbd5e1">Equalizes potential across wing, bowser, and earth.</text>
    <text x="25" y="320" font-size="10" fill="#94a3b8">Bleeds friction charges before fuel vapor can ignite.</text>
  </g>
</svg>
""")

# SVG 3: Airfield Universal Sign Matrix (Lesson 3, Page 4)
SVG_AIRFIELD_SIGN_MATRIX = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Airfield Universal Signage &amp; Pavement Markings Matrix</text>

  <!-- Quadrant 1: Mandatory Sign (Red/White) -->
  <g transform="translate(40, 65)">
    <rect x="0" y="0" width="340" height="155" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="15" y="15" width="130" height="60" rx="6" fill="#dc2626" stroke="#ffffff" stroke-width="2"/>
    <text x="80" y="55" font-size="24" font-weight="bold" fill="#ffffff" text-anchor="middle">15-33</text>
    
    <text x="160" y="32" font-size="13" font-weight="bold" fill="#ef4444">MANDATORY SIGN</text>
    <text x="160" y="50" font-size="11" fill="#e2e8f0">Red background, White text</text>
    <text x="160" y="68" font-size="11" font-weight="bold" fill="#fca5a5">MUST STOP! Do not cross</text>
    
    <rect x="15" y="90" width="310" height="50" rx="4" fill="#1e293b"/>
    <text x="25" y="110" font-size="10" fill="#cbd5e1">Marks runway entrance &amp; holding positions.</text>
    <text x="25" y="126" font-size="10" fill="#94a3b8">Requires explicit verbal clearance from ATC Tower.</text>
  </g>

  <!-- Quadrant 2: Location Sign (Black/Yellow) -->
  <g transform="translate(420, 65)">
    <rect x="0" y="0" width="340" height="155" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <rect x="15" y="15" width="70" height="60" rx="6" fill="#020617" stroke="#eab308" stroke-width="3"/>
    <text x="50" y="56" font-size="28" font-weight="bold" fill="#facc15" text-anchor="middle">B</text>
    
    <text x="105" y="32" font-size="13" font-weight="bold" fill="#facc15">LOCATION SIGN</text>
    <text x="105" y="50" font-size="11" fill="#e2e8f0">Black square, Yellow text/border</text>
    <text x="105" y="68" font-size="11" font-weight="bold" fill="#fde047">"Black square, you're there"</text>
    
    <rect x="15" y="90" width="310" height="50" rx="4" fill="#1e293b"/>
    <text x="25" y="110" font-size="10" fill="#cbd5e1">Confirms the taxiway currently being navigated.</text>
    <text x="25" y="126" font-size="10" fill="#94a3b8">Example: Vehicle is presently on Taxiway Bravo.</text>
  </g>

  <!-- Quadrant 3: Direction Sign (Yellow/Black) -->
  <g transform="translate(40, 240)">
    <rect x="0" y="0" width="340" height="175" rx="8" fill="#0f172a" stroke="#ca8a04" stroke-width="1.5"/>
    <rect x="15" y="15" width="110" height="60" rx="6" fill="#facc15" stroke="#000000" stroke-width="2"/>
    <text x="70" y="54" font-size="24" font-weight="bold" fill="#000000" text-anchor="middle">A &#8594;</text>
    
    <text x="140" y="32" font-size="13" font-weight="bold" fill="#facc15">DIRECTION SIGN</text>
    <text x="140" y="50" font-size="11" fill="#e2e8f0">Yellow background, Black text</text>
    <text x="140" y="68" font-size="11" font-weight="bold" fill="#fde047">"Yellow array points the way"</text>
    
    <rect x="15" y="90" width="310" height="65" rx="4" fill="#1e293b"/>
    <text x="25" y="110" font-size="10" fill="#cbd5e1">Indicates direction to intersecting taxiways.</text>
    <text x="25" y="126" font-size="10" fill="#94a3b8">Example: Turning right leads onto Taxiway Alpha.</text>
    <text x="25" y="142" font-size="10" fill="#38bdf8">Essential for navigating complex aerodrome routes.</text>
  </g>

  <!-- Quadrant 4: Pavement Hold Short Marking -->
  <g transform="translate(420, 240)">
    <rect x="0" y="0" width="340" height="175" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    
    <!-- Pavement Road with Hold Short Lines -->
    <rect x="15" y="15" width="120" height="65" rx="4" fill="#1e293b"/>
    <!-- Two Solid Lines -->
    <line x1="50" y1="18" x2="50" y2="77" stroke="#facc15" stroke-width="4"/>
    <line x1="60" y1="18" x2="60" y2="77" stroke="#facc15" stroke-width="4"/>
    <!-- Two Dashed Lines -->
    <line x1="72" y1="18" x2="72" y2="77" stroke="#facc15" stroke-width="4" stroke-dasharray="8,6"/>
    <line x1="82" y1="18" x2="82" y2="77" stroke="#facc15" stroke-width="4" stroke-dasharray="8,6"/>
    
    <text x="150" y="32" font-size="13" font-weight="bold" fill="#38bdf8">HOLD SHORT LINE</text>
    <text x="150" y="50" font-size="11" fill="#e2e8f0">Pavement Paint Geometry</text>
    <text x="150" y="68" font-size="11" font-weight="bold" fill="#93c5fd">Solid side = Halt; Dashed = Exit</text>

    <rect x="15" y="90" width="310" height="65" rx="4" fill="#1e293b"/>
    <text x="25" y="110" font-size="10" fill="#cbd5e1">Two solid yellow lines face approaching aircraft.</text>
    <text x="25" y="126" font-size="10" fill="#cbd5e1">Never cross solid lines without ATC radio clearance.</text>
    <text x="25" y="142" font-size="10" fill="#fca5a5">Crossing without authorization = Runway Incursion.</text>
  </g>
</svg>
""")

# SVG 4: Passenger Security Screening Sequence & Emergency Evacuation Flowchart (Lesson 4, Page 4)
SVG_SCREENING_AND_EVACUATION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Terminal Safety: Security Screening Chain &amp; Emergency Evacuation Flow</text>

  <!-- Top Half: 5-Step Security Screening Process -->
  <g transform="translate(30, 60)">
    <rect x="0" y="0" width="740" height="150" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="20" y="24" font-size="12" font-weight="bold" fill="#38bdf8">1. PASSENGER SECURITY SCREENING CHAIN (Sequential Flow)</text>
    
    <!-- Step 1 -->
    <g transform="translate(15, 38)">
      <rect x="0" y="0" width="130" height="95" rx="6" fill="#1e293b" stroke="#64748b" stroke-width="1"/>
      <circle cx="20" cy="20" r="12" fill="#0284c7"/>
      <text x="20" y="24" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1</text>
      <text x="40" y="22" font-size="11" font-weight="bold" fill="#e2e8f0">ID &amp; Ticket</text>
      <text x="10" y="50" font-size="9" fill="#cbd5e1">Boarding pass &amp;</text>
      <text x="10" y="65" font-size="9" fill="#cbd5e1">passport identity</text>
      <text x="10" y="80" font-size="9" fill="#94a3b8">verification</text>
    </g>

    <!-- Arrow 1 -> 2 -->
    <path d="M 148 85 L 158 85" stroke="#38bdf8" stroke-width="2"/>

    <!-- Step 2 -->
    <g transform="translate(160, 38)">
      <rect x="0" y="0" width="130" height="95" rx="6" fill="#1e293b" stroke="#64748b" stroke-width="1"/>
      <circle cx="20" cy="20" r="12" fill="#0284c7"/>
      <text x="20" y="24" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2</text>
      <text x="40" y="22" font-size="11" font-weight="bold" fill="#e2e8f0">Divestment</text>
      <text x="10" y="50" font-size="9" fill="#cbd5e1">Empty pockets,</text>
      <text x="10" y="65" font-size="9" fill="#cbd5e1">belt, jacket &amp; large</text>
      <text x="10" y="80" font-size="9" fill="#94a3b8">electronics in trays</text>
    </g>

    <!-- Arrow 2 -> 3 -->
    <path d="M 293 85 L 303 85" stroke="#38bdf8" stroke-width="2"/>

    <!-- Step 3 -->
    <g transform="translate(305, 38)">
      <rect x="0" y="0" width="130" height="95" rx="6" fill="#1e293b" stroke="#64748b" stroke-width="1"/>
      <circle cx="20" cy="20" r="12" fill="#0284c7"/>
      <text x="20" y="24" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3</text>
      <text x="40" y="22" font-size="11" font-weight="bold" fill="#e2e8f0">X-Ray Scan</text>
      <text x="10" y="50" font-size="9" fill="#cbd5e1">Dual-energy X-ray</text>
      <text x="10" y="65" font-size="9" fill="#cbd5e1">screens carry-on</text>
      <text x="10" y="80" font-size="9" fill="#94a3b8">bags for weapons</text>
    </g>

    <!-- Arrow 3 -> 4 -->
    <path d="M 438 85 L 448 85" stroke="#38bdf8" stroke-width="2"/>

    <!-- Step 4 -->
    <g transform="translate(450, 38)">
      <rect x="0" y="0" width="130" height="95" rx="6" fill="#1e293b" stroke="#64748b" stroke-width="1"/>
      <circle cx="20" cy="20" r="12" fill="#0284c7"/>
      <text x="20" y="24" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4</text>
      <text x="40" y="22" font-size="11" font-weight="bold" fill="#e2e8f0">Body Scan</text>
      <text x="10" y="50" font-size="9" fill="#cbd5e1">Walk-through</text>
      <text x="10" y="65" font-size="9" fill="#cbd5e1">metal detector or</text>
      <text x="10" y="80" font-size="9" fill="#94a3b8">millimeter scanner</text>
    </g>

    <!-- Arrow 4 -> 5 -->
    <path d="M 583 85 L 593 85" stroke="#38bdf8" stroke-width="2"/>

    <!-- Step 5 -->
    <g transform="translate(595, 38)">
      <rect x="0" y="0" width="130" height="95" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
      <circle cx="20" cy="20" r="12" fill="#059669"/>
      <text x="20" y="24" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">5</text>
      <text x="40" y="22" font-size="11" font-weight="bold" fill="#86efac">Secure Gate</text>
      <text x="10" y="50" font-size="9" fill="#cbd5e1">Collect items or</text>
      <text x="10" y="65" font-size="9" fill="#cbd5e1">secondary check;</text>
      <text x="10" y="80" font-size="9" fill="#86efac">Enter airside lounge</text>
    </g>
  </g>

  <!-- Bottom Half: Emergency Evacuation Flowchart -->
  <g transform="translate(30, 225)">
    <rect x="0" y="0" width="740" height="190" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="20" y="24" font-size="12" font-weight="bold" fill="#f87171">2. TERMINAL EMERGENCY EVACUATION PROTOCOL (Alarm to Assembly)</text>

    <!-- Box 1: Alarm -->
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="130" height="60" rx="6" fill="#dc2626"/>
      <text x="65" y="25" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">AUDIBLE ALARM</text>
      <text x="65" y="44" font-size="9" fill="#fecaca" text-anchor="middle">Horns &amp; Strobes active</text>
    </g>

    <!-- Connector -->
    <path d="M 148 72 L 160 72" stroke="#ef4444" stroke-width="2"/>

    <!-- Box 2: Halt Action -->
    <g transform="translate(160, 42)">
      <rect x="0" y="0" width="130" height="60" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
      <text x="65" y="25" font-size="10" font-weight="bold" fill="#f59e0b" text-anchor="middle">HALT COMMERCE</text>
      <text x="65" y="44" font-size="9" fill="#cbd5e1" text-anchor="middle">Cease check-in &amp; retail</text>
    </g>

    <!-- Connector -->
    <path d="M 293 72 L 305 72" stroke="#ef4444" stroke-width="2"/>

    <!-- Box 3: Follow Signs -->
    <g transform="translate(305, 42)">
      <rect x="0" y="0" width="130" height="60" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
      <text x="65" y="25" font-size="10" font-weight="bold" fill="#10b981" text-anchor="middle">EXIT ROUTE</text>
      <text x="65" y="44" font-size="9" fill="#cbd5e1" text-anchor="middle">Follow green exit signs</text>
    </g>

    <!-- Connector -->
    <path d="M 438 72 L 450 72" stroke="#ef4444" stroke-width="2"/>

    <!-- Box 4: No Backtracking -->
    <g transform="translate(450, 42)">
      <rect x="0" y="0" width="130" height="60" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
      <text x="65" y="25" font-size="10" font-weight="bold" fill="#f87171" text-anchor="middle">NO LUGGAGE</text>
      <text x="65" y="44" font-size="9" fill="#cbd5e1" text-anchor="middle">Do not backtrack</text>
    </g>

    <!-- Connector -->
    <path d="M 583 72 L 595 72" stroke="#ef4444" stroke-width="2"/>

    <!-- Box 5: Assembly Field -->
    <g transform="translate(595, 42)">
      <rect x="0" y="0" width="130" height="60" rx="6" fill="#047857"/>
      <text x="65" y="25" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">MUSTER FIELD</text>
      <text x="65" y="44" font-size="9" fill="#d1fae5" text-anchor="middle">Roll call &amp; triage</text>
    </g>

    <!-- Bottom Evacuation Rules Banner -->
    <rect x="15" y="120" width="710" height="50" rx="6" fill="#1e293b"/>
    <text x="365" y="140" font-size="11" font-weight="bold" fill="#facc15" text-anchor="middle">CRITICAL EVACUATION RULE: Human Life Always Precedes Material Assets</text>
    <text x="365" y="156" font-size="10" fill="#94a3b8" text-anchor="middle">Never use elevators | Maintain calm pacing | Keep airside runways completely clear of evacuees</text>
  </g>
</svg>
""")

# SVG 5: Airport Safety Team Ecosystem (Lesson 5, Page 4)
SVG_SAFETY_TEAM_ECOSYSTEM = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Airport Safety Team Ecosystem &amp; SMS Integration</text>

  <!-- Central Hub: Airport Safety Manager (SMS System Core) -->
  <g transform="translate(290, 160)">
    <rect x="0" y="0" width="220" height="110" rx="12" fill="#1e1b4b" stroke="#818cf8" stroke-width="2.5"/>
    <text x="110" y="30" font-size="12" font-weight="bold" fill="#c7d2fe" text-anchor="middle">SAFETY MANAGER</text>
    <text x="110" y="46" font-size="10" fill="#a5b4fc" text-anchor="middle">SMS Framework Overseer</text>
    <line x1="20" y1="56" x2="200" y2="56" stroke="#4338ca" stroke-width="1"/>
    <text x="110" y="74" font-size="9" fill="#e0e7ff" text-anchor="middle">&#8226; Risk Matrices &amp; Audits</text>
    <text x="110" y="90" font-size="9" fill="#e0e7ff" text-anchor="middle">&#8226; Non-Punitive Hazard Reporting</text>
  </g>

  <!-- Node 1: Air Traffic Controller (ATC) - Top Left -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="210" height="90" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="210" height="28" rx="10" fill="#0284c7"/>
    <text x="105" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">AIR TRAFFIC CONTROLLER (ATC)</text>
    <text x="15" y="46" font-size="9" fill="#cbd5e1">&#8226; Location: Aerodrome Control Tower</text>
    <text x="15" y="60" font-size="9" fill="#cbd5e1">&#8226; Separation: Runways &amp; Taxiways</text>
    <text x="15" y="74" font-size="9" fill="#38bdf8">&#8226; Tools: VHF Radio &amp; Ground Radar</text>
  </g>

  <!-- Node 2: Aviation Security (AVSEC) - Top Right -->
  <g transform="translate(545, 65)">
    <rect x="0" y="0" width="210" height="90" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect x="0" y="0" width="210" height="28" rx="10" fill="#d97706"/>
    <text x="105" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">SECURITY OFFICER (AVSEC)</text>
    <text x="15" y="46" font-size="9" fill="#cbd5e1">&#8226; Location: Terminal &amp; Access Gates</text>
    <text x="15" y="60" font-size="9" fill="#cbd5e1">&#8226; Mission: Intercept Prohibited Items</text>
    <text x="15" y="74" font-size="9" fill="#f59e0b">&#8226; Tools: X-Ray, Metal Detectors, CCTV</text>
  </g>

  <!-- Node 3: Ground Handling Specialist - Bottom Left -->
  <g transform="translate(45, 275)">
    <rect x="0" y="0" width="210" height="90" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <rect x="0" y="0" width="210" height="28" rx="10" fill="#059669"/>
    <text x="105" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">GROUND HANDLING AGENT</text>
    <text x="15" y="46" font-size="9" fill="#cbd5e1">&#8226; Location: Active Apron / Ramp</text>
    <text x="15" y="60" font-size="9" fill="#cbd5e1">&#8226; Duties: Chocking, Fuel Bonding, FOD</text>
    <text x="15" y="74" font-size="9" fill="#10b981">&#8226; Tools: Wands, Chocks, Ear Defenders</text>
  </g>

  <!-- Node 4: Airport Firefighter (ARFF) - Bottom Right -->
  <g transform="translate(545, 275)">
    <rect x="0" y="0" width="210" height="90" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="210" height="28" rx="10" fill="#dc2626"/>
    <text x="105" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">ARFF AIRPORT FIREFIGHTER</text>
    <text x="15" y="46" font-size="9" fill="#cbd5e1">&#8226; Location: Airside Fire Station</text>
    <text x="15" y="60" font-size="9" fill="#cbd5e1">&#8226; Mission: 3-Minute Runway Response</text>
    <text x="15" y="74" font-size="9" fill="#f87171">&#8226; Tools: Panther Crash Tenders &amp; Foam</text>
  </g>

  <!-- Communication / Reporting Connectors to Central Hub -->
  <line x1="255" y1="130" x2="300" y2="170" stroke="#818cf8" stroke-width="2" stroke-dasharray="4,2"/>
  <line x1="545" y1="130" x2="500" y2="170" stroke="#818cf8" stroke-width="2" stroke-dasharray="4,2"/>
  <line x1="255" y1="295" x2="300" y2="255" stroke="#818cf8" stroke-width="2" stroke-dasharray="4,2"/>
  <line x1="545" y1="295" x2="500" y2="255" stroke="#818cf8" stroke-width="2" stroke-dasharray="4,2"/>

  <!-- Connecting Banner at Bottom -->
  <g transform="translate(45, 380)">
    <rect x="0" y="0" width="710" height="38" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
    <text x="355" y="17" font-size="10" font-weight="bold" fill="#e2e8f0" text-anchor="middle">COLLABORATIVE SAFETY CULTURE: Zero-Blame Incident Reporting &amp; Rapid Emergency Mobilization</text>
    <text x="355" y="30" font-size="9" fill="#94a3b8" text-anchor="middle">If one link in the safety chain breaks, the integrity of the entire airfield is compromised.</text>
  </g>
</svg>
""")

# =============================================================================
# ENRICHMENT ASSETS CONFIGURATION FOR TOPIC 251
# =============================================================================

WIKIMEDIA_PHOTOS = {
    0: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/61/Jomo_Kenyatta_International_Airport_terminal_building.jpg",
        "title": "Jomo Kenyatta International Airport Terminal Architecture",
        "caption": "The exterior terminal building at Jomo Kenyatta International Airport (JKIA) in Nairobi, illustrating the architectural boundary between public landside areas and secure operational aviation zones.",
        "author": "Wikimedia Commons",
        "license": "Creative Commons Attribution-Share Alike"
    },
    1: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/8f/US_Navy_030309-N-9964S-019_Crew_members_gather_on_the_ship%27s_bow_to_participate_in_a_foreign_object_damage_%28FOD%29_walk-down.jpg",
        "title": "Flight Deck Personnel Conducting a Coordinated FOD Walk-Down",
        "caption": "Aviation crew members walking in a coordinated line to inspect the surface and collect loose debris, preventing catastrophic foreign object ingestion by high-thrust aircraft turbine engines.",
        "author": "US Navy / Wikimedia Commons",
        "license": "Public Domain"
    },
    2: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b1/Taxiway_8255.JPG",
        "title": "Airfield Taxiway Guidance Signs and Pavement Markings",
        "caption": "Standardized black location signs and yellow direction indicators positioned along an active airfield taxiway, providing unambiguous navigation guidance to pilots and ground vehicle operators.",
        "author": "Wikimedia Commons",
        "license": "Creative Commons Attribution-Share Alike"
    },
    3: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/9b/Security_screening_selectee.jpg",
        "title": "Passenger Security Screening Checkpoint in an International Terminal",
        "caption": "Aviation security personnel conducting non-intrusive personal screening at a secure terminal checkpoint to prevent unauthorized weapons, liquids, or prohibited items from entering restricted airside areas.",
        "author": "Wikimedia Commons",
        "license": "Public Domain"
    },
    4: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/f/fc/Airport_crash_tender_-_Rosenbauer_Panther_-_Airport_Budapest_%289437%29.jpg",
        "title": "Rosenbauer Panther Aircraft Rescue and Firefighting (ARFF) Crash Tender",
        "caption": "A specialized heavy ARFF crash vehicle stationed on an airport ramp, engineered for high-speed acceleration and massive chemical foam delivery to suppress intense aircraft jet fuel fires.",
        "author": "Wikimedia Commons",
        "license": "Creative Commons Attribution-Share Alike"
    }
}

SVG_MAP = {
    0: {
        "svg": SVG_AIRPORT_3_ZONES,
        "title": "Airport 3-Zone Architecture: Landside, Terminal, and Airside",
        "page": 4
    },
    1: {
        "svg": SVG_FOD_AND_REFUELING,
        "title": "FOD Turbine Ingestion Vector & Refueling Grounding Circuit",
        "page": 4
    },
    2: {
        "svg": SVG_AIRFIELD_SIGN_MATRIX,
        "title": "Airfield Universal Sign Matrix & Pavement Markings",
        "page": 4
    },
    3: {
        "svg": SVG_SCREENING_AND_EVACUATION,
        "title": "Passenger Security Screening Sequence & Emergency Evacuation Flowchart",
        "page": 4
    },
    4: {
        "svg": SVG_SAFETY_TEAM_ECOSYSTEM,
        "title": "Airport Safety Team Ecosystem & Operational Integration",
        "page": 4
    }
}

YOUTUBE_VIDEOS = {
    0: {
        "url": "https://www.youtube.com/watch?v=B0Ar5WsUhWs",
        "title": "Airport Operations: Aerodrome, Airport, Landside, Terminal, and Airside",
        "description": "Visual walkthrough of real airport physical layouts, illustrating the spatial and regulatory distinctions between landside public roadways, passenger terminals, and airside aircraft operational aprons."
    },
    1: {
        "url": "https://www.youtube.com/watch?v=H4L_Coqawz8",
        "title": "Jet Fuel Safety: Hazards, PPE, and Grounding Protocols",
        "description": "Demonstrates the vital procedures for handling volatile aviation jet fuels, highlighting static electrical bonding cables, grounding stakes, exclusion zones, and protective equipment."
    },
    2: {
        "url": "https://www.youtube.com/watch?v=Yacx4jNQlgo",
        "title": "Airport Signs, Markings, and Lighting Explained",
        "description": "An in-depth cockpit and ground-level perspective explaining how runway markings, taxiway centerlines, illuminated signage, and hold-short lines direct pilots safely across active aerodromes."
    },
    3: {
        "url": "https://www.youtube.com/watch?v=hblmFtbyYKQ",
        "title": "Emergency Medical Response: Hands-Only CPR in Aviation Terminals",
        "description": "Demonstrates the vital lifesaving technique of Hands-Only CPR, highlighting chest compression rate and rhythm (100–120 bpm) essential for medical first responders in crowded airport passenger concourses."
    },
    4: {
        "url": "https://www.youtube.com/watch?v=FViSA91DP-8",
        "title": "Human Factors in Aviation Safety and Maintenance",
        "description": "Explores how psychological awareness, fatigue management, clear communication, and structured safety checklists prevent critical human errors in aviation operations."
    }
}

def enrich_grade10_topic251():
    """Enriches Topic 251 lessons with verified photos, vector SVGs, and educational videos."""
    print("=" * 80)
    print("VLearn Visual Enrichment Engine: Grade 10 Aviation — Topic 251")
    print("=" * 80)

    topic = Topic.objects.filter(id=251, subject_id=44).first()
    if not topic:
        print("[ERROR] Topic 251 not found!")
        sys.exit(1)

    lessons = Lesson.objects.filter(topic=topic).order_by("learning_unit__order")
    print(f"[*] Found {lessons.count()} lessons under Topic 251: '{topic.name}'.")

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
                            "licensing": img_def["license"],
                            "topic_order": 4,
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
                            "topic_order": 4,
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
                            "topic_order": 4,
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
    print(f"ENRICHMENT COMPLETE: Topic 251 '{topic.name}'")
    print(f"  Photographic Hooks: {total_photos_attached} / 5")
    print(f"  Vector SVGs:        {total_svgs_attached} / 5")
    print(f"  YouTube Videos:     {total_videos_attached} / 5")
    print(f"  LessonAssets Total: {total_assets_persisted}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic251()
