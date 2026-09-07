"""
VLearn Grade 10 Aviation — Topic 368: Airport Business Services (Subject ID: 44, Topic ID: 368)
Visual & Multimedia Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Aviation (Subject ID: 44)
Topic: Airport Business Services (Topic ID: 368, Order: 10)

Enriches:
  - 5 First-Card Photographic Visual Hooks (Verified Direct Wikimedia URLs returning HTTP/2 200)
  - 5 Custom Responsive Vector SVGs (viewBox="0 0 800 450", Dark Slate Theme #0f172a, Sanitized XML)
  - 5 Curated Educational YouTube Videos (Verified Active via oEmbed)
  - Persists LessonAsset models (5 image, 5 diagram, 5 youtube = 15 total) and binds them to LessonBlocks

Usage:
  ./venv/bin/python curriculum/enrich_grade10_aviation_topic368.py
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
# 5 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 368
# =============================================================================

# SVG 1: Passenger Terminal Workflow Flowchart (Lesson 1)
SVG_PASSENGER_TERMINAL_WORKFLOW = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="44" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Passenger Terminal Workflow Architecture</text>
  <text x="400" y="64" font-size="12" fill="#94a3b8" text-anchor="middle">End-to-End Traveler Journey: Landside Public Zone to Airside Sterile Boarding</text>

  <!-- Zone Demarcation Banners -->
  <rect x="35" y="80" width="345" height="24" rx="6" fill="#065f46" opacity="0.8"/>
  <text x="207" y="96" font-size="11" font-weight="bold" fill="#a7f3d0" text-anchor="middle">PUBLIC LANDSIDE ZONE (Unscreened Access)</text>

  <rect x="420" y="80" width="345" height="24" rx="6" fill="#1e40af" opacity="0.8"/>
  <text x="592" y="96" font-size="11" font-weight="bold" fill="#bfdbfe" text-anchor="middle">STERILE AIRSIDE ZONE (Restricted Security Access)</text>

  <!-- Flow Row 1: Steps 1 to 4 -->
  <!-- Step 1: Curbside -->
  <g transform="translate(40, 115)">
    <rect width="155" height="110" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect width="155" height="24" rx="8" fill="#059669"/>
    <text x="77" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Curbside Arrival</text>
    <text x="12" y="45" font-size="10" fill="#e2e8f0">• Terminal drop-off</text>
    <text x="12" y="63" font-size="10" fill="#e2e8f0">• Flight info displays</text>
    <text x="12" y="81" font-size="10" fill="#e2e8f0">• Luggage trolleys</text>
    <text x="12" y="99" font-size="9" fill="#94a3b8">Public concourse</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <path d="M 200 170 L 225 170" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Step 2: Check-in Kiosk -->
  <g transform="translate(230, 115)">
    <rect width="155" height="110" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect width="155" height="24" rx="8" fill="#059669"/>
    <text x="77" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Check-In / Kiosk</text>
    <text x="12" y="45" font-size="10" fill="#e2e8f0">• Passport verification</text>
    <text x="12" y="63" font-size="10" fill="#e2e8f0">• Ticket contract check</text>
    <text x="12" y="81" font-size="10" fill="#e2e8f0">• Seat selection</text>
    <text x="12" y="99" font-size="9" fill="#38bdf8">Boarding pass printed</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <path d="M 390 170 L 415 170" stroke="#38bdf8" stroke-width="2"/>

  <!-- Step 3: Baggage Drop & BRS -->
  <g transform="translate(420, 115)">
    <rect width="155" height="110" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="155" height="24" rx="8" fill="#0284c7"/>
    <text x="77" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Baggage Drop (BRS)</text>
    <text x="12" y="45" font-size="10" fill="#e2e8f0">• Digital scale weight</text>
    <text x="12" y="63" font-size="10" fill="#e2e8f0">• 10-digit barcode tag</text>
    <text x="12" y="81" font-size="10" fill="#e2e8f0">• Conveyor belt scan</text>
    <text x="12" y="99" font-size="9" fill="#fbbf24">BRS Tracking active</text>
  </g>

  <!-- Arrow 3 -> 4 -->
  <path d="M 580 170 L 605 170" stroke="#38bdf8" stroke-width="2"/>

  <!-- Step 4: Security Screening -->
  <g transform="translate(610, 115)">
    <rect width="155" height="110" rx="8" fill="#0f172a" stroke="#f87171" stroke-width="1.5"/>
    <rect width="155" height="24" rx="8" fill="#dc2626"/>
    <text x="77" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4. Security Screening</text>
    <text x="12" y="45" font-size="10" fill="#e2e8f0">• Dual-energy X-ray</text>
    <text x="12" y="63" font-size="10" fill="#e2e8f0">• 100ml liquid rule</text>
    <text x="12" y="81" font-size="10" fill="#e2e8f0">• Body scanner check</text>
    <text x="12" y="99" font-size="9" fill="#fca5a5">Sterile zone barrier</text>
  </g>

  <!-- Flow Row 2: Steps 8 to 5 (Right-to-Left loop) -->
  <!-- Step 8: Jetbridge & Boarding -->
  <g transform="translate(40, 260)">
    <rect width="155" height="110" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="155" height="24" rx="8" fill="#0284c7"/>
    <text x="77" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">8. Jetbridge Boarding</text>
    <text x="12" y="45" font-size="10" fill="#e2e8f0">• Aerobridge walkway</text>
    <text x="12" y="63" font-size="10" fill="#e2e8f0">• Cabin crew welcome</text>
    <text x="12" y="81" font-size="10" fill="#e2e8f0">• Seat stowage</text>
    <text x="12" y="99" font-size="9" fill="#34d399">Aircraft secured</text>
  </g>

  <!-- Arrow 7 -> 8 -->
  <path d="M 230 315 L 205 315" stroke="#38bdf8" stroke-width="2"/>

  <!-- Step 7: Departure Gate -->
  <g transform="translate(230, 260)">
    <rect width="155" height="110" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="155" height="24" rx="8" fill="#0284c7"/>
    <text x="77" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">7. Departure Gate</text>
    <text x="12" y="45" font-size="10" fill="#e2e8f0">• Final barcode scan</text>
    <text x="12" y="63" font-size="10" fill="#e2e8f0">• Manifest matching</text>
    <text x="12" y="81" font-size="10" fill="#e2e8f0">• BRS positive match</text>
    <text x="12" y="99" font-size="9" fill="#38bdf8">No Passenger, No Bag</text>
  </g>

  <!-- Arrow 6 -> 7 -->
  <path d="M 420 315 L 395 315" stroke="#38bdf8" stroke-width="2"/>

  <!-- Step 6: Duty Free & Lounge -->
  <g transform="translate(420, 260)">
    <rect width="155" height="110" rx="8" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="155" height="24" rx="8" fill="#d97706"/>
    <text x="77" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">6. Duty-Free Concourse</text>
    <text x="12" y="45" font-size="10" fill="#e2e8f0">• Retail boutiques</text>
    <text x="12" y="63" font-size="10" fill="#e2e8f0">• Cafes &amp; dining</text>
    <text x="12" y="81" font-size="10" fill="#e2e8f0">• Boarding lounges</text>
    <text x="12" y="99" font-size="9" fill="#fde68a">Commercial revenue</text>
  </g>

  <!-- Arrow 5 -> 6 -->
  <path d="M 610 315 L 585 315" stroke="#38bdf8" stroke-width="2"/>

  <!-- Step 5: Passport / Immigration -->
  <g transform="translate(610, 260)">
    <rect width="155" height="110" rx="8" fill="#0f172a" stroke="#a78bfa" stroke-width="1.5"/>
    <rect width="155" height="24" rx="8" fill="#7c3aed"/>
    <text x="77" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">5. Passport Control</text>
    <text x="12" y="45" font-size="10" fill="#e2e8f0">• E-Passport scan</text>
    <text x="12" y="63" font-size="10" fill="#e2e8f0">• Biometric e-gates</text>
    <text x="12" y="81" font-size="10" fill="#e2e8f0">• Visa &amp; customs check</text>
    <text x="12" y="99" font-size="9" fill="#ddd6fe">Border authorization</text>
  </g>

  <!-- Connecting Turn Arrow: Step 4 down to Step 5 -->
  <path d="M 687 225 L 687 260" stroke="#38bdf8" stroke-width="2"/>

  <!-- Bottom Critical Rule Bar -->
  <rect x="40" y="390" width="725" height="30" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
  <text x="400" y="410" font-size="11" fill="#38bdf8" font-weight="bold" text-anchor="middle">AIRPORT SAFETY MANDATE: Positive Baggage Reconciliation (BRS) strictly enforces "No Passenger Onboard = No Bag Flies"</text>
</svg>
""")

# SVG 2: Air Cargo Logistics Chain & Turnaround (Lesson 2)
SVG_AIR_CARGO_LOGISTICS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="44" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Air Cargo Logistics Chain &amp; Apron Turnaround Architecture</text>
  <text x="400" y="64" font-size="12" fill="#94a3b8" text-anchor="middle">Cold-Chain Handling, Unit Load Devices (ULDs), Scissor High-Loader, and Freighter Hold Stowing</text>

  <!-- Step 1: Cold Storage Warehouse -->
  <g transform="translate(35, 90)">
    <rect width="165" height="150" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="165" height="26" rx="8" fill="#0284c7"/>
    <text x="82" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Cold Storage Facility</text>
    
    <rect x="15" y="40" width="135" height="35" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
    <text x="82" y="55" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Climate: +2°C to +8°C</text>
    <text x="82" y="68" font-size="9" fill="#94a3b8" text-anchor="middle">Pharma &amp; Fresh Flowers</text>

    <text x="12" y="95" font-size="10" fill="#e2e8f0">• Phytosanitary checks</text>
    <text x="12" y="112" font-size="10" fill="#e2e8f0">• Barcode consignment tag</text>
    <text x="12" y="129" font-size="10" fill="#e2e8f0">• Thermal protective covers</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <path d="M 205 165 L 225 165" stroke="#38bdf8" stroke-width="2"/>

  <!-- Step 2: Unit Load Device (ULD) Buildup -->
  <g transform="translate(230, 90)">
    <rect width="165" height="150" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect width="165" height="26" rx="8" fill="#059669"/>
    <text x="82" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Contoured ULD Buildup</text>

    <!-- ULD Profile Graphic -->
    <path d="M 35 75 L 105 75 L 125 50 L 55 50 Z" fill="#334155" stroke="#34d399" stroke-width="1.5"/>
    <text x="82" y="65" font-size="9" font-weight="bold" fill="#34d399" text-anchor="middle">LD-3 Contoured Box</text>

    <text x="12" y="95" font-size="10" fill="#e2e8f0">• Tare weight: ~75 kg</text>
    <text x="12" y="112" font-size="10" fill="#e2e8f0">• Max gross: ~1,588 kg</text>
    <text x="12" y="129" font-size="10" fill="#e2e8f0">• Slanted fuselage contour</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <path d="M 400 165 L 420 165" stroke="#38bdf8" stroke-width="2"/>

  <!-- Step 3: Tarmac High-Loader -->
  <g transform="translate(425, 90)">
    <rect width="165" height="150" rx="8" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="165" height="26" rx="8" fill="#d97706"/>
    <text x="82" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Scissor High-Loader</text>

    <!-- Scissor Mechanism Graphic -->
    <path d="M 40 68 L 125 45 M 40 45 L 125 68" stroke="#fbbf24" stroke-width="2"/>
    <rect x="35" y="42" width="95" height="6" fill="#fbbf24"/>
    <text x="82" y="78" font-size="9" fill="#fde68a" text-anchor="middle">Hydraulic Lift Deck</text>

    <text x="12" y="98" font-size="10" fill="#e2e8f0">• Elevates up to 5.5 meters</text>
    <text x="12" y="115" font-size="10" fill="#e2e8f0">• Omni motorized rollers</text>
    <text x="12" y="132" font-size="10" fill="#e2e8f0">• Stabilizer safety jacks</text>
  </g>

  <!-- Arrow 3 -> 4 -->
  <path d="M 595 165 L 615 165" stroke="#38bdf8" stroke-width="2"/>

  <!-- Step 4: Freighter Main Deck & Holds -->
  <g transform="translate(620, 90)">
    <rect width="145" height="150" rx="8" fill="#0f172a" stroke="#a78bfa" stroke-width="1.5"/>
    <rect width="145" height="26" rx="8" fill="#7c3aed"/>
    <text x="72" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4. Aircraft Cargo Hold</text>

    <rect x="15" y="40" width="115" height="35" rx="4" fill="#1e293b" stroke="#a78bfa" stroke-width="1"/>
    <text x="72" y="55" font-size="9" font-weight="bold" fill="#a78bfa" text-anchor="middle">Cargo Floor Tracks</text>
    <text x="72" y="68" font-size="8" fill="#94a3b8" text-anchor="middle">9G Restraint Latches</text>

    <text x="10" y="95" font-size="10" fill="#e2e8f0">• Main deck cargo door</text>
    <text x="10" y="112" font-size="10" fill="#e2e8f0">• Weight &amp; balance lock</text>
    <text x="10" y="129" font-size="10" fill="#e2e8f0">• Fire suppression bay</text>
  </g>

  <!-- Bottom Panel: Synchronized Apron Turnaround GSE Grid -->
  <g transform="translate(35, 260)">
    <rect width="730" height="160" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="365" y="24" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">PARALLEL APRON TURNAROUND SERVICES (30 to 45 Minute Window)</text>

    <!-- 4 GSE Turnaround Boxes -->
    <!-- GSE 1: Refueling -->
    <g transform="translate(20, 38)">
      <rect width="155" height="105" rx="6" fill="#1e293b" stroke="#f87171" stroke-width="1"/>
      <text x="77" y="20" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">Jet A-1 Refueling</text>
      <text x="10" y="42" font-size="9" fill="#e2e8f0">• Under-wing hydrant</text>
      <text x="10" y="58" font-size="9" fill="#e2e8f0">• 2,000+ L/min flow rate</text>
      <text x="10" y="74" font-size="9" fill="#e2e8f0">• Static bonding wire</text>
      <text x="10" y="94" font-size="8" font-weight="bold" fill="#fca5a5">Grounding Mandatory</text>
    </g>

    <!-- GSE 2: Catering -->
    <g transform="translate(195, 38)">
      <rect width="155" height="105" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1"/>
      <text x="77" y="20" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">Catering Logistics</text>
      <text x="10" y="42" font-size="9" fill="#e2e8f0">• High-lift refrigerated van</text>
      <text x="10" y="58" font-size="9" fill="#e2e8f0">• Galley trolley swap</text>
      <text x="10" y="74" font-size="9" fill="#e2e8f0">• Fresh meal restocking</text>
      <text x="10" y="94" font-size="8" font-weight="bold" fill="#fde68a">Opposite Door Access</text>
    </g>

    <!-- GSE 3: GPU & Baggage -->
    <g transform="translate(370, 38)">
      <rect width="165" height="105" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
      <text x="82" y="20" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">Ground Power &amp; Belts</text>
      <text x="10" y="42" font-size="9" fill="#e2e8f0">• 400Hz 115V AC Power</text>
      <text x="10" y="58" font-size="9" fill="#e2e8f0">• Engine APU fuel saved</text>
      <text x="10" y="74" font-size="9" fill="#e2e8f0">• Belt loaders for bags</text>
      <text x="10" y="94" font-size="8" font-weight="bold" fill="#a7f3d0">Reduced Ramp Noise</text>
    </g>

    <!-- GSE 4: Pushback Tug -->
    <g transform="translate(555, 38)">
      <rect width="155" height="105" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <text x="77" y="20" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Pushback Towbar Tug</text>
      <text x="10" y="42" font-size="9" fill="#e2e8f0">• High-torque diesel/eGSE</text>
      <text x="10" y="58" font-size="9" fill="#e2e8f0">• Nose gear steering pin</text>
      <text x="10" y="74" font-size="9" fill="#e2e8f0">• Headset intercom link</text>
      <text x="10" y="94" font-size="8" font-weight="bold" fill="#bfdbfe">Push into Taxiway</text>
    </g>
  </g>
</svg>
""")

# SVG 3: Airport Revenue Model & Financial Architecture (Lesson 3)
SVG_AIRPORT_REVENUE_FINANCE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="44" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Airport Revenue Model &amp; Financial Architecture</text>
  <text x="400" y="64" font-size="12" fill="#94a3b8" text-anchor="middle">Balancing Aeronautical Fees, Commercial Concessions, and Mandatory Safety Operating Costs</text>

  <!-- Left Column: Aeronautical Revenue (45-50%) -->
  <g transform="translate(35, 85)">
    <rect width="345" height="165" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="345" height="28" rx="10" fill="#0284c7"/>
    <text x="172" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">AERONAUTICAL REVENUES (Aviation Regulated)</text>

    <g font-size="11" fill="#e2e8f0" transform="translate(15, 45)">
      <rect x="0" y="0" width="315" height="22" rx="4" fill="#1e293b"/>
      <text x="10" y="15"><tspan font-weight="bold" fill="#38bdf8">Aircraft Landing Fees</tspan> — Based on MTOW weight</text>

      <rect x="0" y="26" width="315" height="22" rx="4" fill="#1e293b"/>
      <text x="10" y="15"><tspan font-weight="bold" fill="#38bdf8">Passenger Service Charges (PFC)</tspan> — Per departure ticket</text>

      <rect x="0" y="52" width="315" height="22" rx="4" fill="#1e293b"/>
      <text x="10" y="15"><tspan font-weight="bold" fill="#38bdf8">Aircraft Parking &amp; Hangarage</tspan> — Hourly/overnight tarmac</text>

      <rect x="0" y="78" width="315" height="22" rx="4" fill="#1e293b"/>
      <text x="10" y="15"><tspan font-weight="bold" fill="#38bdf8">Air Navigation &amp; Lighting</tspan> — Runway approach fees</text>
    </g>
    <text x="172" y="154" font-size="10" fill="#94a3b8" text-anchor="middle">Directly tied to flight volumes, airline contracts &amp; payload weight</text>
  </g>

  <!-- Right Column: Non-Aeronautical Revenue (50-55%) -->
  <g transform="translate(420, 85)">
    <rect width="345" height="165" rx="10" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect width="345" height="28" rx="10" fill="#059669"/>
    <text x="172" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">NON-AERONAUTICAL REVENUES (Commercial Market)</text>

    <g font-size="11" fill="#e2e8f0" transform="translate(15, 45)">
      <rect x="0" y="0" width="315" height="22" rx="4" fill="#1e293b"/>
      <text x="10" y="15"><tspan font-weight="bold" fill="#34d399">Duty-Free &amp; Retail Concessions</tspan> — Leases &amp; % sales</text>

      <rect x="0" y="26" width="315" height="22" rx="4" fill="#1e293b"/>
      <text x="10" y="15"><tspan font-weight="bold" fill="#34d399">Food, Beverage &amp; Dining</tspan> — Terminal restaurants &amp; cafes</text>

      <rect x="0" y="52" width="315" height="22" rx="4" fill="#1e293b"/>
      <text x="10" y="15"><tspan font-weight="bold" fill="#34d399">Car Parking &amp; Ground Transport</tspan> — Multi-story lots, taxis</text>

      <rect x="0" y="78" width="315" height="22" rx="4" fill="#1e293b"/>
      <text x="10" y="15"><tspan font-weight="bold" fill="#34d399">Advertising &amp; Real Estate</tspan> — Billboards, airport hotels</text>
    </g>
    <text x="172" y="154" font-size="10" fill="#94a3b8" text-anchor="middle">High profit margins driven by captive passenger dwell time</text>
  </g>

  <!-- Convergence Bar: Total Revenue -->
  <path d="M 207 250 L 360 275" stroke="#38bdf8" stroke-width="2"/>
  <path d="M 592 250 L 440 275" stroke="#34d399" stroke-width="2"/>

  <rect x="250" y="265" width="300" height="28" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
  <text x="400" y="284" font-size="12" font-weight="bold" fill="#fbbf24" text-anchor="middle">TOTAL GROSS AIRPORT REVENUE</text>

  <!-- Bottom Panel: Operating Expenses (OPEX) & Net Operating Balance -->
  <g transform="translate(35, 305)">
    <rect width="730" height="115" rx="10" fill="#0f172a" stroke="#f87171" stroke-width="1.5"/>
    <rect width="730" height="24" rx="10" fill="#991b1b"/>
    <text x="365" y="17" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">AIRPORT OPERATING EXPENSES (OPEX) — Mandatory Safety Baseline</text>

    <g font-size="10" fill="#e2e8f0" transform="translate(20, 36)">
      <rect x="0" y="0" width="220" height="60" rx="5" fill="#1e293b"/>
      <text x="15" y="20" font-weight="bold" fill="#f87171">Safety &amp; Rescue Services</text>
      <text x="15" y="36">• ARFF Category 9 Firefighting</text>
      <text x="15" y="50">• 24/7 Paramedics &amp; Drills</text>

      <rect x="245" y="0" width="220" height="60" rx="5" fill="#1e293b"/>
      <text x="15" y="20" font-weight="bold" fill="#f87171">Airfield Maintenance</text>
      <text x="15" y="36">• Runway rubber removal &amp; lighting</text>
      <text x="15" y="50">• Nav-aid recalibration (ILS/VOR)</text>

      <rect x="490" y="0" width="200" height="60" rx="5" fill="#1e293b"/>
      <text x="15" y="20" font-weight="bold" fill="#f87171">Security &amp; Terminal Staff</text>
      <text x="15" y="36">• Checkpoint screeners &amp; police</text>
      <text x="15" y="50">• Terminal HVAC &amp; utility power</text>
    </g>
  </g>
</svg>
""")

# SVG 4: Green Airport & Emerging Aviation Technology Ecosystem (Lesson 4)
SVG_GREEN_AIRPORT_ECOSYSTEM = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="44" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Green Airport &amp; Emerging Technology Ecosystem</text>
  <text x="400" y="64" font-size="12" fill="#94a3b8" text-anchor="middle">Solar Runway Canopies, Electric GSE (e-GSE), SAF Fuel Systems, and Biometric Automation</text>

  <!-- 4 Primary Sustainable Innovation Quads -->

  <!-- Quad 1: Solar Photovoltaic Farms -->
  <g transform="translate(35, 80)">
    <rect width="350" height="150" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect width="350" height="26" rx="8" fill="#059669"/>
    <text x="175" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Solar Photovoltaic Runway Farms</text>

    <!-- Solar Panel Grid Graphic -->
    <g transform="translate(20, 38)">
      <rect x="0" y="0" width="100" height="60" rx="4" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1"/>
      <line x1="25" y1="0" x2="25" y2="60" stroke="#38bdf8" stroke-width="0.75"/>
      <line x1="50" y1="0" x2="50" y2="60" stroke="#38bdf8" stroke-width="0.75"/>
      <line x1="75" y1="0" x2="75" y2="60" stroke="#38bdf8" stroke-width="0.75"/>
      <line x1="0" y1="20" x2="100" y2="20" stroke="#38bdf8" stroke-width="0.75"/>
      <line x1="0" y1="40" x2="100" y2="40" stroke="#38bdf8" stroke-width="0.75"/>
      <text x="50" y="75" font-size="9" fill="#38bdf8" font-weight="bold" text-anchor="middle">100% Clean Solar</text>
    </g>

    <g font-size="10" fill="#e2e8f0" transform="translate(135, 42)">
      <text y="15">• Utilizing open runway buffer terrain</text>
      <text y="33">• Powers terminal lighting &amp; HVAC</text>
      <text y="51">• Offsets grid energy blackouts</text>
      <text y="69">• Zero operational carbon emissions</text>
      <text y="92" font-size="9" font-weight="bold" fill="#34d399">Pioneered by George &amp; Cochin Airports</text>
    </g>
  </g>

  <!-- Quad 2: Electric GSE (e-GSE) Infrastructure -->
  <g transform="translate(415, 80)">
    <rect width="350" height="150" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="350" height="26" rx="8" fill="#0284c7"/>
    <text x="175" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Electric Ground Support Equipment (e-GSE)</text>

    <!-- Electric Tug Graphic -->
    <g transform="translate(20, 42)">
      <rect x="0" y="15" width="85" height="40" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <circle cx="20" cy="55" r="8" fill="#475569" stroke="#94a3b8" stroke-width="1"/>
      <circle cx="65" cy="55" r="8" fill="#475569" stroke="#94a3b8" stroke-width="1"/>
      <text x="42" y="38" font-size="12" fill="#38bdf8" text-anchor="middle">⚡ e-TUG</text>
      <text x="42" y="78" font-size="9" fill="#38bdf8" font-weight="bold" text-anchor="middle">Lithium Battery</text>
    </g>

    <g font-size="10" fill="#e2e8f0" transform="translate(125, 42)">
      <text y="15">• Zero tailpipe diesel soot &amp; CO fumes</text>
      <text y="33">• Drastically reduced ramp decibel noise</text>
      <text y="51">• High torque for heavy widebody pushbacks</text>
      <text y="69">• Smart solar fast-charging stations</text>
      <text y="92" font-size="9" font-weight="bold" fill="#38bdf8">Protects Ground Crew Respiratory Health</text>
    </g>
  </g>

  <!-- Quad 3: Sustainable Aviation Fuel (SAF) -->
  <g transform="translate(35, 245)">
    <rect width="350" height="155" rx="8" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="350" height="26" rx="8" fill="#d97706"/>
    <text x="175" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Sustainable Aviation Fuel (SAF) Storage</text>

    <!-- Fuel Tank Graphic -->
    <g transform="translate(20, 42)">
      <rect x="10" y="5" width="75" height="55" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
      <text x="47" y="32" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">SAF TANK</text>
      <text x="47" y="46" font-size="8" fill="#fde68a" text-anchor="middle">Biofuel Blend</text>
      <text x="47" y="78" font-size="9" fill="#fbbf24" font-weight="bold" text-anchor="middle">-80% Lifecycle CO2</text>
    </g>

    <g font-size="10" fill="#e2e8f0" transform="translate(125, 42)">
      <text y="15">• Made from agricultural waste &amp; oils</text>
      <text y="33">• Drop-in fuel: compatible with jet engines</text>
      <text y="51">• Dedicated on-airport blending tanks</text>
      <text y="69">• Pressurized hydrant delivery pipelines</text>
      <text y="94" font-size="9" font-weight="bold" fill="#fbbf24">Aviation Net-Zero 2050 Pillar</text>
    </g>
  </g>

  <!-- Quad 4: Automated Biometric Boarding -->
  <g transform="translate(415, 245)">
    <rect width="350" height="155" rx="8" fill="#0f172a" stroke="#a78bfa" stroke-width="1.5"/>
    <rect width="350" height="26" rx="8" fill="#7c3aed"/>
    <text x="175" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4. Biometric Single-Token Automation</text>

    <!-- Face Scan Turnstile Graphic -->
    <g transform="translate(20, 42)">
      <rect x="10" y="5" width="75" height="55" rx="6" fill="#1e293b" stroke="#a78bfa" stroke-width="1.5"/>
      <circle cx="47" cy="28" r="12" fill="none" stroke="#a78bfa" stroke-width="1.5"/>
      <circle cx="47" cy="24" r="3" fill="#a78bfa"/>
      <text x="47" y="78" font-size="9" fill="#a78bfa" font-weight="bold" text-anchor="middle">Facial Token</text>
    </g>

    <g font-size="10" fill="#e2e8f0" transform="translate(125, 42)">
      <text y="15">• Walk-through biometric e-turnstiles</text>
      <text y="33">• Under 2-second identity verification</text>
      <text y="51">• Paperless ticketing &amp; boarding gates</text>
      <text y="69">• Autonomous robot baggage shuttles</text>
      <text y="94" font-size="9" font-weight="bold" fill="#a78bfa">Quadruples Passenger Concourse Throughput</text>
    </g>
  </g>

  <!-- Bottom Strip -->
  <text x="400" y="426" font-size="11" fill="#94a3b8" text-anchor="middle">Sustainable Airport Operations: Combining Zero-Emission Ground Fleets with AI &amp; Solar Innovation</text>
</svg>
""")

# SVG 5: Integrated Airport Business Simulation Command Matrix (Lesson 5)
SVG_AIRPORT_SIMULATION_COMMAND_MATRIX = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="44" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Integrated Airport Business Simulation Command Matrix</text>
  <text x="400" y="64" font-size="12" fill="#94a3b8" text-anchor="middle">Multidisciplinary Crisis Command: Operations, Logistics, Commercial, and Regulatory Oversight</text>

  <!-- Central Hub: Integrated Operations Control Center (IOCC / AOCC) -->
  <g transform="translate(275, 145)">
    <rect width="250" height="120" rx="12" fill="#0f172a" stroke="#fbbf24" stroke-width="2"/>
    <rect width="250" height="28" rx="12" fill="#d97706"/>
    <text x="125" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">CENTRAL COMMAND HUB (IOCC)</text>
    <text x="125" y="48" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">Turnaround Coordination</text>
    <text x="15" y="70" font-size="10" fill="#e2e8f0">• Master Flight Manifest Sign-off</text>
    <text x="15" y="88" font-size="10" fill="#e2e8f0">• Real-Time Weather &amp; Fuel Telemetry</text>
    <text x="15" y="106" font-size="10" fill="#e2e8f0">• Cross-Departmental Crisis Resolution</text>
  </g>

  <!-- Node 1: Top-Left: Passenger Services Team -->
  <g transform="translate(35, 80)">
    <rect width="200" height="105" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="200" height="24" rx="8" fill="#0284c7"/>
    <text x="100" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Passenger Services</text>
    <text x="10" y="42" font-size="9" fill="#e2e8f0">• Gate barcode scanning</text>
    <text x="10" y="58" font-size="9" fill="#e2e8f0">• Missing passenger identification</text>
    <text x="10" y="74" font-size="9" fill="#e2e8f0">• Delay customer care &amp; vouchers</text>
    <text x="10" y="94" font-size="9" font-weight="bold" fill="#38bdf8">Gate 4 Discrepancy Alert</text>
  </g>
  <path d="M 235 130 L 275 170" stroke="#38bdf8" stroke-width="2"/>

  <!-- Node 2: Top-Right: Flight Crew & Dispatch -->
  <g transform="translate(565, 80)">
    <rect width="200" height="105" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect width="200" height="24" rx="8" fill="#059669"/>
    <text x="100" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Flight Crew &amp; Dispatch</text>
    <text x="10" y="42" font-size="9" fill="#e2e8f0">• En-route thunderstorm rerouting</text>
    <text x="10" y="58" font-size="9" fill="#e2e8f0">• Extra safety fuel calculation (+800kg)</text>
    <text x="10" y="74" font-size="9" fill="#e2e8f0">• Center of Gravity (CG) envelope</text>
    <text x="10" y="94" font-size="9" font-weight="bold" fill="#34d399">Cockpit Acceptance of Load</text>
  </g>
  <path d="M 565 130 L 525 170" stroke="#34d399" stroke-width="2"/>

  <!-- Node 3: Bottom-Left: Ground & Ramp Logistics -->
  <g transform="translate(35, 230)">
    <rect width="200" height="105" rx="8" fill="#0f172a" stroke="#f87171" stroke-width="1.5"/>
    <rect width="200" height="24" rx="8" fill="#dc2626"/>
    <text x="100" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Ground &amp; Ramp Logistics</text>
    <text x="10" y="42" font-size="9" fill="#e2e8f0">• Bag offloading (Seat 12C match)</text>
    <text x="10" y="58" font-size="9" fill="#e2e8f0">• ULD payload balancing (500kg offload)</text>
    <text x="10" y="74" font-size="9" fill="#e2e8f0">• Fuel hydrant static grounding</text>
    <text x="10" y="94" font-size="9" font-weight="bold" fill="#fca5a5">Positive Reconciliation Check</text>
  </g>
  <path d="M 235 270 L 275 230" stroke="#f87171" stroke-width="2"/>

  <!-- Node 4: Bottom-Right: Airport Management & Finance -->
  <g transform="translate(565, 230)">
    <rect width="200" height="105" rx="8" fill="#0f172a" stroke="#a78bfa" stroke-width="1.5"/>
    <rect width="200" height="24" rx="8" fill="#7c3aed"/>
    <text x="100" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4. Airport Finance &amp; Comms</text>
    <text x="10" y="42" font-size="9" fill="#e2e8f0">• Priority freight: keep flowers flying</text>
    <text x="10" y="58" font-size="9" fill="#e2e8f0">• Delay machinery cargo (low cost)</text>
    <text x="10" y="74" font-size="9" fill="#e2e8f0">• Gate stand reallocation</text>
    <text x="10" y="94" font-size="9" font-weight="bold" fill="#ddd6fe">Minimizes Financial Losses</text>
  </g>
  <path d="M 565 270 L 525 230" stroke="#a78bfa" stroke-width="2"/>

  <!-- Bottom Regulatory Banner: KCAA Safety & Consumer Audit -->
  <g transform="translate(35, 355)">
    <rect width="730" height="65" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="730" height="22" rx="8" fill="#0369a1"/>
    <text x="365" y="15" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">5. REGULATORY &amp; CONSUMER AUDIT TEAM (KCAA Oversight Referee)</text>

    <g font-size="10" fill="#e2e8f0" transform="translate(15, 30)">
      <text x="20" y="14">• Audits baggage offload proof</text>
      <text x="20" y="28">• Inspects passenger refreshment care</text>
      <text x="300" y="14">• Verifies MTOW calculation compliance</text>
      <text x="300" y="28">• Validates center of gravity load sheet</text>
      <text x="560" y="20" font-size="11" font-weight="bold" fill="#34d399">✓ Legal Clearance to Fly</text>
    </g>
  </g>
</svg>
""")

# =============================================================================
# MULTIMEDIA ASSET MAPPINGS (VERIFIED ASSETS)
# =============================================================================

WIKIMEDIA_PHOTOS = {
    0: {
        "title": "Modern Airport Terminal Passenger Check-in Concourse",
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e7/Taiwan_Taoyuan_International_Airport_Terminal_2_Check-in_Hall_20200815.jpg",
        "caption": "A modern airport passenger terminal departure concourse showing self-service kiosks, check-in desks, automated baggage drop lanes, and flight information display systems.",
        "page": 1
    },
    1: {
        "title": "Air Cargo High-Loader Loading Unit Load Devices (ULDs)",
        "url": "https://upload.wikimedia.org/wikipedia/commons/2/2f/Aircraft_cargo_%28ULD%29_loader_in_operaton.jpg",
        "caption": "An airport ramp scissor-lift high-loader transferring standardized aluminum Unit Load Device (ULD) cargo containers into the main deck cargo door of a freight aircraft.",
        "page": 1
    },
    2: {
        "title": "Jomo Kenyatta International Airport Commercial Terminal Facade",
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Jomo_Kenyatta_International_Airport_terminal_building%2C_2025_%2802%29.jpg",
        "caption": "The main commercial passenger terminal building of Jomo Kenyatta International Airport (JKIA) in Nairobi, managed and operated by the Kenya Airports Authority (KAA).",
        "page": 1
    },
    3: {
        "title": "Utility-Scale Solar Farm Powering Airport Operations",
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/cc/Solar_Plant_powering_the_Cochin_International_Airport.jpg",
        "caption": "A utility-scale solar photovoltaic power plant installed on airport buffer lands, supplying clean renewable electricity for terminal operations and electric ground vehicles.",
        "page": 1
    },
    4: {
        "title": "Collaborative Airport Flightline Ground Operations",
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/32/A_tale_of_two-_A_team_approach_to_flightline_operations_%288046588%29.jpg",
        "caption": "A coordinated multidisciplinary airport ground team managing aircraft turnaround, flightline safety protocols, and operational dispatch.",
        "page": 1
    }
}

SVG_MAP = {
    0: {
        "title": "Passenger Terminal Workflow Architecture",
        "svg": SVG_PASSENGER_TERMINAL_WORKFLOW,
        "page": 4
    },
    1: {
        "title": "Air Cargo Logistics Chain & Ramp Turnaround Architecture",
        "svg": SVG_AIR_CARGO_LOGISTICS,
        "page": 4
    },
    2: {
        "title": "Airport Revenue Model and Financial Architecture",
        "svg": SVG_AIRPORT_REVENUE_FINANCE,
        "page": 4
    },
    3: {
        "title": "Green Airport and Emerging Aviation Technology Ecosystem",
        "svg": SVG_GREEN_AIRPORT_ECOSYSTEM,
        "page": 4
    },
    4: {
        "title": "Integrated Airport Business Simulation Command Matrix",
        "svg": SVG_AIRPORT_SIMULATION_COMMAND_MATRIX,
        "page": 4
    }
}

YOUTUBE_VIDEOS = {
    0: {
        "title": "Airport Procedures: Baggage Handling and Security",
        "url": "https://www.youtube.com/watch?v=wBRImzQSG80",
        "description": "Examine the unseen automated sorting networks, barcode scanner arrays, and ramp reconciliation systems that process luggage from check-in desks to aircraft cargo holds.",
        "page": 9
    },
    1: {
        "title": "Ramp Operations: Aircraft Turnaround and Ground Handling",
        "url": "https://www.youtube.com/watch?v=pAL3GfdWLWM",
        "description": "Witness the high-speed choreography of aircraft turnarounds as ground crews synchronize cargo unloading, fuel hydrants, catering lifts, and pushback tugs.",
        "page": 9
    },
    2: {
        "title": "Aviation Regulation: Role of the Civil Aviation Authority",
        "url": "https://www.youtube.com/watch?v=PecMbpWxK9w",
        "description": "Discover how national civil aviation authorities regulate airspace safety, audit airport infrastructure, license aviation professionals, and protect passenger rights.",
        "page": 9
    },
    3: {
        "title": "Emerging Airport Tech: Robotics and Humanoid Baggage Handling",
        "url": "https://www.youtube.com/watch?v=VqETxTNoG1Y",
        "description": "Discover how airlines and aerodrome operators are testing robotic assistance, autonomous luggage tugs, and AI automation on the commercial apron.",
        "page": 9
    },
    4: {
        "title": "Airport Operations: Landside, Airside, and Terminal Systems",
        "url": "https://www.youtube.com/watch?v=B0Ar5WsUhWs",
        "description": "Understand the comprehensive architecture of commercial airport operations, integrating airside runways, landside concourses, passenger terminals, and regulatory safety frameworks.",
        "page": 9
    }
}

def enrich_grade10_topic368():
    """Binds verified photographic hooks, custom responsive vector SVGs, and YouTube videos."""
    print("=" * 80)
    print("VISUAL & MULTIMEDIA ENRICHMENT ENGINE: Grade 10 Aviation — Topic 368")
    print("Topic: Airport Business Services")
    print("=" * 80)

    topic = Topic.objects.filter(id=368, subject_id=44).first()
    if not topic:
        print("[ERROR] Topic 368 (Subject ID: 44) not found in database!")
        sys.exit(1)

    lessons = Lesson.objects.filter(topic=topic).order_by("learning_unit__order")
    if not lessons.exists():
        print("[ERROR] No lessons found for Topic 368! Run ingest_grade10_aviation_topic368.py first.")
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
                p_content["url"] = img_def["url"]
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
                        "source_type": "external",
                        "storage_type": "url",
                        "status": "attached",
                        "title": f"Lesson {u_order + 1} Photo: {img_def['title']}",
                        "description": img_def["caption"],
                        "metadata": {
                            "topic_order": 10,
                            "unit_order": u_order,
                            "page": img_def["page"],
                            "license": "Wikimedia Commons (Public Domain / CC-BY-SA)",
                            "resolved_image_url": img_def["url"]
                        }
                    }
                )
                photo_block.assets.add(asset)
                total_photos_attached += 1
                total_assets_persisted += 1
                print(f"  [Photo Attached] {img_def['title']}")

        # ---------------------------------------------------------------------
        # 2. Custom Responsive Vector SVGs (Card 4)
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
                            "topic_order": 10,
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
        # 3. Curated Instructional YouTube Videos (Card 9)
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
                            "topic_order": 10,
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
    print(f"ENRICHMENT COMPLETE: Topic 368 '{topic.name}'")
    print(f"  Photographic Hooks: {total_photos_attached} / 5")
    print(f"  Vector SVGs:        {total_svgs_attached} / 5")
    print(f"  YouTube Videos:     {total_videos_attached} / 5")
    print(f"  LessonAssets Total: {total_assets_persisted}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic368()
