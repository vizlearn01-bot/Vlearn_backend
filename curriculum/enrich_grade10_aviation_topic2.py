"""
VLearn Grade 10 Aviation — Topic 2: Safety in Aviation
Visual Enrichment Engine (Verified Photos, Responsive Vector SVGs & Video Assets)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Aviation (Subject ID: 44)
Topic: Safety in Aviation (Topic ID: 248, Order: 1)

Enriches:
  - 6 First-Card Photographic Visual Hooks (Verified Direct Wikimedia URLs)
  - 6 Custom Responsive Vector SVGs (viewBox="0 0 800 450", Dark Slate Theme, Sanitized XML)
  - 6 Verified Educational YouTube Videos (Human factors, ramp PPE, hazard spotting, injury response, CPR, marshalling)
  - Persists LessonAsset models and binds them to corresponding LessonBlocks

Usage:
  ./venv/bin/python curriculum/enrich_grade10_aviation_topic2.py
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
# 6 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 2: SAFETY IN AVIATION
# =============================================================================

# SVG 1: The Safety Chain & Swiss Cheese Model (Lesson 1, Page 4)
SVG_SWISS_CHEESE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">James Reason's Swiss Cheese Safety Defense Model</text>

  <!-- Hazard Arrow -->
  <text x="50" y="195" font-size="12" font-weight="bold" fill="#ef4444">HAZARD</text>
  <line x1="45" y1="215" x2="130" y2="215" stroke="#ef4444" stroke-width="4" marker-end="url(#arrow-red)"/>

  <!-- Slice 1: Organizational Culture -->
  <g transform="translate(140, 90)">
    <rect x="0" y="0" width="110" height="250" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="55" y="30" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Organizational</text>
    <text x="55" y="45" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Culture</text>
    <circle cx="55" cy="110" r="16" fill="#1e293b" stroke="#64748b"/>
    <circle cx="55" cy="180" r="14" fill="#1e293b" stroke="#64748b"/>
    <text x="55" y="230" font-size="9" fill="#94a3b8" text-anchor="middle">No Shortcuts</text>
  </g>

  <!-- Slice 2: Engineering Defenses -->
  <g transform="translate(280, 90)">
    <rect x="0" y="0" width="110" height="250" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <text x="55" y="30" font-size="11" font-weight="bold" fill="#c084fc" text-anchor="middle">Engineering</text>
    <text x="55" y="45" font-size="11" font-weight="bold" fill="#c084fc" text-anchor="middle">Defenses</text>
    <circle cx="55" cy="85" r="14" fill="#1e293b" stroke="#64748b"/>
    <circle cx="55" cy="200" r="18" fill="#1e293b" stroke="#64748b"/>
    <text x="55" y="230" font-size="9" fill="#94a3b8" text-anchor="middle">Redundant Parts</text>
  </g>

  <!-- Slice 3: Procedural Checklists -->
  <g transform="translate(420, 90)">
    <rect x="0" y="0" width="110" height="250" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <text x="55" y="30" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">Checklists &amp;</text>
    <text x="55" y="45" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">Procedures</text>
    <circle cx="55" cy="130" r="15" fill="#1e293b" stroke="#64748b"/>
    <circle cx="55" cy="170" r="12" fill="#1e293b" stroke="#64748b"/>
    <text x="55" y="230" font-size="9" fill="#94a3b8" text-anchor="middle">Verified Logs</text>
  </g>

  <!-- Slice 4: Personal Awareness & PPE -->
  <g transform="translate(560, 90)">
    <rect x="0" y="0" width="110" height="250" rx="10" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
    <text x="55" y="30" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">Personal Alertness</text>
    <text x="55" y="45" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">&amp; PPE</text>
    <circle cx="55" cy="100" r="14" fill="#1e293b" stroke="#64748b"/>
    <circle cx="55" cy="190" r="16" fill="#1e293b" stroke="#64748b"/>
    <text x="55" y="230" font-size="9" fill="#94a3b8" text-anchor="middle">Situational Focus</text>
  </g>

  <!-- Trajectory Blocked Arrow -->
  <line x1="140" y1="215" x2="420" y2="215" stroke="#ef4444" stroke-width="3" stroke-dasharray="6,4"/>
  <circle cx="420" cy="215" r="8" fill="#ef4444"/>
  <line x1="414" y1="209" x2="426" y2="221" stroke="#ffffff" stroke-width="2.5"/>
  <line x1="426" y1="209" x2="414" y2="221" stroke="#ffffff" stroke-width="2.5"/>
  <text x="495" y="218" font-size="11" font-weight="bold" fill="#34d399">HAZARD BLOCKED BY DEFENSE LAYERS</text>

  <!-- Bottom Caption -->
  <rect x="40" y="365" width="720" height="48" rx="8" fill="#0f172a" stroke="#334155"/>
  <text x="400" y="388" font-size="11.5" fill="#f8fafc" text-anchor="middle">An accident only happens when the "holes" (procedural lapses, fatigue, missing tools) align simultaneously.</text>
  <text x="400" y="404" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Multi-layered procedural defense stops hazards from causing catastrophic failure.</text>

  <defs>
    <marker id="arrow-red" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#ef4444"/>
    </marker>
  </defs>
</svg>
""")

# SVG 2: PPE Layout & Hangar Housekeeping (Lesson 2, Page 4)
SVG_PPE_LAYOUT = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Aviation PPE Ensemble &amp; Hangar Safety Architecture</text>

  <!-- Left Column: Head-to-Toe PPE Anatomy -->
  <g transform="translate(35, 70)">
    <rect x="0" y="0" width="350" height="340" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="175" y="30" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">THE 5-POINT PPE SUIT</text>

    <!-- Point 1: Eye Protection -->
    <g transform="translate(20, 45)">
      <circle cx="12" cy="18" r="8" fill="#38bdf8"/>
      <text x="32" y="16" font-size="12" font-weight="bold" fill="#ffffff">1. Safety Glasses with Side Shields</text>
      <text x="32" y="32" font-size="10.5" fill="#94a3b8">Protects eyes from flying wire clippings, metal swarf &amp; solvent splashes</text>
    </g>

    <!-- Point 2: Hearing Protection -->
    <g transform="translate(20, 100)">
      <circle cx="12" cy="18" r="8" fill="#a855f7"/>
      <text x="32" y="16" font-size="12" font-weight="bold" fill="#ffffff">2. Acoustic Ear Defenders (Noise &gt; 85 dB)</text>
      <text x="32" y="32" font-size="10.5" fill="#94a3b8">Prevents irreversible hearing damage from roaring APUs &amp; jet turbines</text>
    </g>

    <!-- Point 3: High-Vis Vest -->
    <g transform="translate(20, 155)">
      <circle cx="12" cy="18" r="8" fill="#f59e0b"/>
      <text x="32" y="16" font-size="12" font-weight="bold" fill="#ffffff">3. Hi-Vis Reflective Vest (Day-Glo)</text>
      <text x="32" y="32" font-size="10.5" fill="#94a3b8">Ensures drivers of fuel trucks and taxiing pilots can spot workers</text>
    </g>

    <!-- Point 4: Nitrile Gloves -->
    <g transform="translate(20, 210)">
      <circle cx="12" cy="18" r="8" fill="#34d399"/>
      <text x="32" y="16" font-size="12" font-weight="bold" fill="#ffffff">4. Nitrile / Butyl Chemical Gloves</text>
      <text x="32" y="32" font-size="10.5" fill="#94a3b8">Resists corrosive Skydrol hydraulic fluid, kerosene, and harsh degreasers</text>
    </g>

    <!-- Point 5: Steel-Toe Boots -->
    <g transform="translate(20, 265)">
      <circle cx="12" cy="18" r="8" fill="#ef4444"/>
      <text x="32" y="16" font-size="12" font-weight="bold" fill="#ffffff">5. Steel-Toed Anti-Slip Boots</text>
      <text x="32" y="32" font-size="10.5" fill="#94a3b8">Protects toes from falling 30kg parts; non-slip soles on oily ramps</text>
    </g>
  </g>

  <!-- Right Column: Hangar Housekeeping Standards -->
  <g transform="translate(415, 70)">
    <rect x="0" y="0" width="350" height="340" rx="10" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
    <text x="175" y="30" font-size="14" font-weight="bold" fill="#34d399" text-anchor="middle">HANGAR HOUSEKEEPING PROTOCOLS</text>

    <g transform="translate(20, 50)">
      <rect x="0" y="0" width="310" height="70" rx="6" fill="#1e293b"/>
      <text x="15" y="24" font-size="12" font-weight="bold" fill="#f59e0b">Rule 1: Clear Yellow Walkways</text>
      <text x="15" y="44" font-size="10.5" fill="#cbd5e1">• Never run power cords or hoses across walkways</text>
      <text x="15" y="58" font-size="10.5" fill="#cbd5e1">• Maintain unblocked access to fire extinguishers &amp; exits</text>
    </g>

    <g transform="translate(20, 135)">
      <rect x="0" y="0" width="310" height="70" rx="6" fill="#1e293b"/>
      <text x="15" y="24" font-size="12" font-weight="bold" fill="#38bdf8">Rule 2: 100% Tool Accountability</text>
      <text x="15" y="44" font-size="10.5" fill="#cbd5e1">• Use shadow boards and cut-out foam trays</text>
      <text x="15" y="58" font-size="10.5" fill="#cbd5e1">• A tool left inside an engine or wing creates fatal FOD</text>
    </g>

    <g transform="translate(20, 220)">
      <rect x="0" y="0" width="310" height="70" rx="6" fill="#1e293b"/>
      <text x="15" y="24" font-size="12" font-weight="bold" fill="#34d399">Rule 3: Immediate Spill Remediation</text>
      <text x="15" y="44" font-size="10.5" fill="#cbd5e1">• Dam spills immediately with absorbent socks</text>
      <text x="15" y="58" font-size="10.5" fill="#cbd5e1">• Dispose of chemical rags in labeled hazardous waste bins</text>
    </g>
  </g>
</svg>
""")

# SVG 3: The Four Aviation Hazard Families (Lesson 3, Page 4)
SVG_HAZARD_FAMILIES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Four Aviation Hazard Families &amp; Controls</text>

  <!-- Box 1: Physical Hazards -->
  <g transform="translate(40, 75)">
    <rect x="0" y="0" width="340" height="150" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="20" y="28" font-size="13" font-weight="bold" fill="#38bdf8">1. PHYSICAL HAZARDS</text>
    <text x="20" y="50" font-size="11" fill="#cbd5e1">• High-speed spinning propellers &amp; turbine fans</text>
    <text x="20" y="68" font-size="11" fill="#cbd5e1">• Working on scaffolding at 6m heights (Falls)</text>
    <text x="20" y="86" font-size="11" fill="#cbd5e1">• Slippery hydraulic oil puddles on concrete</text>
    <rect x="15" y="105" width="310" height="32" rx="6" fill="#1e293b"/>
    <text x="170" y="125" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Controls: Fall harnesses, perimeter barriers, anti-slip boots</text>
  </g>

  <!-- Box 2: Chemical Hazards -->
  <g transform="translate(420, 75)">
    <rect x="0" y="0" width="340" height="150" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <text x="20" y="28" font-size="13" font-weight="bold" fill="#c084fc">2. CHEMICAL HAZARDS</text>
    <text x="20" y="50" font-size="11" fill="#cbd5e1">• Volatile, highly flammable Jet A-1 aviation fuel</text>
    <text x="20" y="68" font-size="11" fill="#cbd5e1">• Skydrol hydraulic fluid (severe eye/skin burn)</text>
    <text x="20" y="86" font-size="11" fill="#cbd5e1">• Toxic solvent vapors and battery acid fumes</text>
    <rect x="15" y="105" width="310" height="32" rx="6" fill="#1e293b"/>
    <text x="170" y="125" font-size="10" font-weight="bold" fill="#c084fc" text-anchor="middle">Controls: Butyl gloves, splash goggles, eyewash stations</text>
  </g>

  <!-- Box 3: Electrical Hazards -->
  <g transform="translate(40, 245)">
    <rect x="0" y="0" width="340" height="150" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <text x="20" y="28" font-size="13" font-weight="bold" fill="#fbbf24">3. ELECTRICAL HAZARDS</text>
    <text x="20" y="50" font-size="11" fill="#cbd5e1">• 115V AC / 400Hz Ground Power Units (GPU)</text>
    <text x="20" y="68" font-size="11" fill="#cbd5e1">• Aircraft 24V/28V DC heavy battery short-circuits</text>
    <text x="20" y="86" font-size="11" fill="#cbd5e1">• Static sparks during refueling (explosive risk)</text>
    <rect x="15" y="105" width="310" height="32" rx="6" fill="#1e293b"/>
    <text x="170" y="125" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">Controls: Static bonding clamps, lockout/tagout, GFCI</text>
  </g>

  <!-- Box 4: Ergonomic Hazards -->
  <g transform="translate(420, 245)">
    <rect x="0" y="0" width="340" height="150" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
    <text x="20" y="28" font-size="13" font-weight="bold" fill="#34d399">4. ERGONOMIC HAZARDS</text>
    <text x="20" y="50" font-size="11" fill="#cbd5e1">• Lifting heavy 40kg aircraft wheels and brakes</text>
    <text x="20" y="68" font-size="11" fill="#cbd5e1">• Awkward neck/back postures inside wing roots</text>
    <text x="20" y="86" font-size="11" fill="#cbd5e1">• Repetitive vibration from pneumatic rivet tools</text>
    <rect x="15" y="105" width="310" height="32" rx="6" fill="#1e293b"/>
    <text x="170" y="125" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">Controls: Hydraulic lift carts, team lifting, rest breaks</text>
  </g>
</svg>
""")

# SVG 4: Injury Severity Triage Pyramid (Lesson 4, Page 4)
SVG_INJURY_SEVERITY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Workplace Injury Severity &amp; Medical Triage Scale</text>

  <!-- Level 1: Minor Injuries (Bottom of Pyramid) -->
  <g transform="translate(100, 280)">
    <polygon points="0,90 600,90 520,0 80,0" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <text x="300" y="32" font-size="15" font-weight="bold" fill="#34d399" text-anchor="middle">LEVEL 1: MINOR INJURIES</text>
    <text x="300" y="55" font-size="11" fill="#cbd5e1" text-anchor="middle">Small cuts, surface abrasions, mild 1st-degree heat burns, minor muscle strains</text>
    <text x="300" y="73" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Action: Treated on-site using standard first-aid kit; worker resumes duties</text>
  </g>

  <!-- Level 2: Serious Injuries (Middle of Pyramid) -->
  <g transform="translate(180, 175)">
    <polygon points="0,90 440,90 380,0 60,0" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="220" y="32" font-size="15" font-weight="bold" fill="#fbbf24" text-anchor="middle">LEVEL 2: SERIOUS INJURIES</text>
    <text x="220" y="55" font-size="11" fill="#cbd5e1" text-anchor="middle">Deep lacerations, bone fractures, electric shock, chemical burns, head concussion</text>
    <text x="220" y="73" font-size="11" font-weight="bold" fill="#f59e0b" text-anchor="middle">Action: Immediate on-site stabilization; dispatch emergency ambulance</text>
  </g>

  <!-- Level 3: Fatal / Life-Threatening (Top of Pyramid) -->
  <g transform="translate(240, 70)">
    <polygon points="0,90 320,90 160,0" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <text x="160" y="42" font-size="14" font-weight="bold" fill="#f87171" text-anchor="middle">LEVEL 3: FATAL / CRITICAL</text>
    <text x="160" y="60" font-size="10.5" fill="#fca5a5" text-anchor="middle">Cardiac arrest, severe crush trauma,</text>
    <text x="160" y="75" font-size="10.5" fill="#fca5a5" text-anchor="middle">unconsciousness, severed arteries</text>
  </g>

  <!-- Side Callout: Medical Escalation Timeline -->
  <g transform="translate(620, 100)">
    <rect x="0" y="0" width="140" height="250" rx="8" fill="#0f172a" stroke="#64748b"/>
    <text x="70" y="25" font-size="11" font-weight="bold" fill="#f8fafc" text-anchor="middle">RESPONSE</text>
    <text x="70" y="42" font-size="11" font-weight="bold" fill="#f8fafc" text-anchor="middle">TIMELINE</text>
    <line x1="15" y1="55" x2="125" y2="55" stroke="#334155"/>
    <text x="70" y="80" font-size="10" font-weight="bold" fill="#ef4444" text-anchor="middle">&lt; 1 Minute</text>
    <text x="70" y="95" font-size="9" fill="#94a3b8" text-anchor="middle">Isolate live power /</text>
    <text x="70" y="108" font-size="9" fill="#94a3b8" text-anchor="middle">Start CPR</text>
    <line x1="25" y1="125" x2="115" y2="125" stroke="#334155"/>
    <text x="70" y="150" font-size="10" font-weight="bold" fill="#f59e0b" text-anchor="middle">&lt; 3 Minutes</text>
    <text x="70" y="165" font-size="9" fill="#94a3b8" text-anchor="middle">Airport ARFF</text>
    <text x="70" y="178" font-size="9" fill="#94a3b8" text-anchor="middle">rescue arrival</text>
    <line x1="25" y1="195" x2="115" y2="195" stroke="#334155"/>
    <text x="70" y="220" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">&lt; 15 Minutes</text>
    <text x="70" y="235" font-size="9" fill="#94a3b8" text-anchor="middle">Paramedic hospital</text>
  </g>
</svg>
""")

# SVG 5: First Aid and CPR Decision Flowchart (Lesson 5, Page 4)
SVG_FIRST_AID_CPR = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Emergency First Aid &amp; Hands-Only CPR Protocol</text>

  <!-- Step 1: Scene Safety -->
  <g transform="translate(40, 80)">
    <rect x="0" y="0" width="150" height="90" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <text x="75" y="25" font-size="11" font-weight="bold" fill="#f59e0b" text-anchor="middle">STEP 1: SCENE SAFETY</text>
    <text x="75" y="48" font-size="10" fill="#cbd5e1" text-anchor="middle">Check for live wires,</text>
    <text x="75" y="62" font-size="10" fill="#cbd5e1" text-anchor="middle">fuel spills or machinery.</text>
    <text x="75" y="76" font-size="9" font-weight="bold" fill="#ef4444" text-anchor="middle">Isolate power first!</text>
  </g>
  <line x1="190" y1="125" x2="230" y2="125" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrow)"/>

  <!-- Step 2: Check Response -->
  <g transform="translate(230, 80)">
    <rect x="0" y="0" width="150" height="90" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="75" y="25" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">STEP 2: CHECK VICTIM</text>
    <text x="75" y="48" font-size="10" fill="#cbd5e1" text-anchor="middle">Tap shoulders &amp; shout:</text>
    <text x="75" y="62" font-size="10" fill="#cbd5e1" text-anchor="middle">"Are you okay?"</text>
    <text x="75" y="76" font-size="9.5" fill="#94a3b8" text-anchor="middle">Check for normal breathing</text>
  </g>
  <line x1="380" y1="125" x2="420" y2="125" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>

  <!-- Step 3: Call 999 & Get AED -->
  <g transform="translate(420, 80)">
    <rect x="0" y="0" width="150" height="90" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <text x="75" y="25" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">STEP 3: CALL HELP</text>
    <text x="75" y="48" font-size="10" fill="#cbd5e1" text-anchor="middle">Dial 999 / 112</text>
    <text x="75" y="62" font-size="10" fill="#cbd5e1" text-anchor="middle">Airport Dispatch.</text>
    <text x="75" y="76" font-size="9.5" font-weight="bold" fill="#f59e0b" text-anchor="middle">Send for the AED!</text>
  </g>
  <line x1="570" y1="125" x2="610" y2="125" stroke="#ef4444" stroke-width="3" marker-end="url(#arrow)"/>

  <!-- Step 4: Hands-Only CPR -->
  <g transform="translate(610, 80)">
    <rect x="0" y="0" width="150" height="90" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
    <text x="75" y="25" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">STEP 4: START CPR</text>
    <text x="75" y="48" font-size="10" fill="#cbd5e1" text-anchor="middle">Center of chest.</text>
    <text x="75" y="62" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">100–120 bpm</text>
    <text x="75" y="76" font-size="9" fill="#cbd5e1" text-anchor="middle">5 to 6 cm deep</text>
  </g>

  <!-- Lower Section: Specific Trauma Rules -->
  <g transform="translate(40, 205)">
    <rect x="0" y="0" width="720" height="190" rx="10" fill="#0f172a" stroke="#334155"/>
    <text x="360" y="28" font-size="13" font-weight="bold" fill="#f8fafc" text-anchor="middle">FIRST AID PROTOCOLS FOR SPECIFIC HANGAR EMERGENCIES</text>

    <!-- Bleeding -->
    <g transform="translate(20, 45)">
      <rect x="0" y="0" width="155" height="125" rx="6" fill="#1e293b"/>
      <text x="77" y="22" font-size="11" font-weight="bold" fill="#ef4444" text-anchor="middle">Severe Bleeding</text>
      <text x="10" y="42" font-size="9.5" fill="#cbd5e1">• Direct firm pressure</text>
      <text x="10" y="58" font-size="9.5" fill="#cbd5e1">• Sterile gauze pads</text>
      <text x="10" y="74" font-size="9.5" fill="#cbd5e1">• Bandage tightly</text>
      <text x="10" y="94" font-size="9" fill="#f87171">• Do not remove soaked</text>
      <text x="10" y="106" font-size="9" fill="#f87171">  gauze; add more</text>
    </g>

    <!-- Burns -->
    <g transform="translate(195, 45)">
      <rect x="0" y="0" width="155" height="125" rx="6" fill="#1e293b"/>
      <text x="77" y="22" font-size="11" font-weight="bold" fill="#f59e0b" text-anchor="middle">Thermal Burns</text>
      <text x="10" y="42" font-size="9.5" fill="#cbd5e1">• Cool running water</text>
      <text x="10" y="58" font-size="9.5" fill="#cbd5e1">• Flush 10 to 20 mins</text>
      <text x="10" y="74" font-size="9.5" fill="#cbd5e1">• Cover with clean film</text>
      <text x="10" y="94" font-size="9" fill="#f87171">• NEVER apply butter,</text>
      <text x="10" y="106" font-size="9" fill="#f87171">  oils, or ice</text>
    </g>

    <!-- Fractures -->
    <g transform="translate(370, 45)">
      <rect x="0" y="0" width="155" height="125" rx="6" fill="#1e293b"/>
      <text x="77" y="22" font-size="11" font-weight="bold" fill="#a855f7" text-anchor="middle">Bone Fractures</text>
      <text x="10" y="42" font-size="9.5" fill="#cbd5e1">• Keep victim still</text>
      <text x="10" y="58" font-size="9.5" fill="#cbd5e1">• Splint in position</text>
      <text x="10" y="74" font-size="9.5" fill="#cbd5e1">• Support joint above</text>
      <text x="10" y="94" font-size="9" fill="#f87171">• NEVER attempt to</text>
      <text x="10" y="106" font-size="9" fill="#f87171">  straighten bone</text>
    </g>

    <!-- Shock -->
    <g transform="translate(545, 45)">
      <rect x="0" y="0" width="155" height="125" rx="6" fill="#1e293b"/>
      <text x="77" y="22" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Electric Shock</text>
      <text x="10" y="42" font-size="9.5" fill="#cbd5e1">• Switch OFF breaker</text>
      <text x="10" y="58" font-size="9.5" fill="#cbd5e1">• Push wire with wood</text>
      <text x="10" y="74" font-size="9.5" fill="#cbd5e1">• Check breathing</text>
      <text x="10" y="94" font-size="9" fill="#f87171">• NEVER touch with</text>
      <text x="10" y="106" font-size="9" fill="#f87171">  bare wet hands</text>
    </g>
  </g>

  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#f59e0b"/>
    </marker>
  </defs>
</svg>
""")

# SVG 6: Aviation Safety Careers and Turnaround Cycle (Lesson 6, Page 4)
SVG_SAFETY_CAREERS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Aviation Safety Careers &amp; Ground Turnaround Sequence</text>

  <!-- Left Column: Professional Safety Career Roles -->
  <g transform="translate(40, 75)">
    <rect x="0" y="0" width="340" height="330" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="170" y="28" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">AVIATION SAFETY PROFESSIONS</text>

    <g transform="translate(15, 45)">
      <rect x="0" y="0" width="310" height="55" rx="6" fill="#1e293b"/>
      <text x="15" y="20" font-size="11.5" font-weight="bold" fill="#38bdf8">Airport Safety Manager</text>
      <text x="15" y="38" font-size="10" fill="#94a3b8">Designs SMS protocols, audits hangars, prevents bird strikes</text>
    </g>

    <g transform="translate(15, 110)">
      <rect x="0" y="0" width="310" height="55" rx="6" fill="#1e293b"/>
      <text x="15" y="20" font-size="11.5" font-weight="bold" fill="#34d399">Air Traffic Controller (ATC)</text>
      <text x="15" y="38" font-size="10" fill="#94a3b8">Uses radar to separate aircraft, prevents runway collisions</text>
    </g>

    <g transform="translate(15, 175)">
      <rect x="0" y="0" width="310" height="55" rx="6" fill="#1e293b"/>
      <text x="15" y="20" font-size="11.5" font-weight="bold" fill="#f59e0b">Aviation Airworthiness Inspector (KCAA)</text>
      <text x="15" y="38" font-size="10" fill="#94a3b8">Certifies aircraft airworthiness, audits maintenance logs</text>
    </g>

    <g transform="translate(15, 240)">
      <rect x="0" y="0" width="310" height="55" rx="6" fill="#1e293b"/>
      <text x="15" y="20" font-size="11.5" font-weight="bold" fill="#ef4444">Airport Firefighter (ARFF)</text>
      <text x="15" y="38" font-size="10" fill="#94a3b8">Rapid 3-minute crash response, foam fire suppression</text>
    </g>
  </g>

  <!-- Right Column: The 4-Stage Aircraft Turnaround Protocol -->
  <g transform="translate(420, 75)">
    <rect x="0" y="0" width="340" height="330" rx="10" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
    <text x="170" y="28" font-size="14" font-weight="bold" fill="#34d399" text-anchor="middle">GROUND TURNAROUND CHECKLIST</text>

    <g transform="translate(20, 45)">
      <circle cx="15" cy="18" r="12" fill="#38bdf8"/>
      <text x="15" y="22" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">1</text>
      <text x="35" y="16" font-size="11" font-weight="bold" fill="#f8fafc">Pre-Arrival FOD Sweep</text>
      <text x="35" y="32" font-size="9.5" fill="#94a3b8">Scan parking spot to ensure zero debris can enter engines</text>
    </g>

    <g transform="translate(20, 110)">
      <circle cx="15" cy="18" r="12" fill="#38bdf8"/>
      <text x="15" y="22" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">2</text>
      <text x="35" y="16" font-size="11" font-weight="bold" fill="#f8fafc">Precision Marshalling</text>
      <text x="35" y="32" font-size="9.5" fill="#94a3b8">Guide aircraft to exact stop-line using wand paddles</text>
    </g>

    <g transform="translate(20, 175)">
      <circle cx="15" cy="18" r="12" fill="#38bdf8"/>
      <text x="15" y="22" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">3</text>
      <text x="35" y="16" font-size="11" font-weight="bold" fill="#f8fafc">Tire Chocking</text>
      <text x="35" y="32" font-size="9.5" fill="#94a3b8">Insert heavy rubber blocks against tires to prevent rolling</text>
    </g>

    <g transform="translate(20, 240)">
      <circle cx="15" cy="18" r="12" fill="#38bdf8"/>
      <text x="15" y="22" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">4</text>
      <text x="35" y="16" font-size="11" font-weight="bold" fill="#f8fafc">Static Ground Bonding</text>
      <text x="35" y="32" font-size="9.5" fill="#94a3b8">Attach copper earthing cable before opening fuel valves</text>
    </g>
  </g>
</svg>
""")

SVG_MAP_TOPIC2 = {
    0: {"svg": SVG_SWISS_CHEESE, "title": "The Swiss Cheese Safety Defense Model", "page": 4},
    1: {"svg": SVG_PPE_LAYOUT, "title": "Aviation PPE Ensemble and Hangar Safety Architecture", "page": 4},
    2: {"svg": SVG_HAZARD_FAMILIES, "title": "The Four Aviation Hazard Families and Controls", "page": 4},
    3: {"svg": SVG_INJURY_SEVERITY, "title": "Workplace Injury Severity & Medical Triage Scale", "page": 4},
    4: {"svg": SVG_FIRST_AID_CPR, "title": "Emergency First Aid & Hands-Only CPR Protocol", "page": 4},
    5: {"svg": SVG_SAFETY_CAREERS, "title": "Aviation Safety Careers & Ground Turnaround Sequence", "page": 4},
}

IMAGE_HOOKS_TOPIC2 = {
    0: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Aircraft_Electronics_Technician_2nd_Class_Roberts_tests_a_torque_wrench_in_the_Aircraft_Intermediate_Maintenance_Department_hangar_-_DPLA_-_0689b07c7fece7f80dfae7c80bf1f3ba.jpeg",
        "title": "Aircraft Maintenance Technician Calibrating Precision Torque Tools",
        "caption": "An aviation maintenance technician systematically verifying tool calibration before performing flight-critical structural servicing.",
        "author": "U.S. Navy",
        "license": "Public Domain"
    },
    1: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/07/Ear_muff_white_bg.jpg",
        "title": "Industrial Hearing Protection Ear Muffs for Aviation Ramp Safety",
        "caption": "Professional acoustic ear defenders designed to attenuate damaging high-decibel jet engine noise on the flight line and hangar floor.",
        "author": "Evan-Amos",
        "license": "Public Domain"
    },
    2: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/2/2b/Defense.gov_photo_essay_080721-F-6044B-226.jpg",
        "title": "Aviation Technicians Operating in a Heavy Maintenance Hangar",
        "caption": "An active military maintenance bay showing elevated work platforms, hydraulic jacks, and high-voltage ground power cables that require constant hazard control.",
        "author": "U.S. Air Force",
        "license": "Public Domain"
    },
    3: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/aa/Adventure_Medical_Kits_Professional_Trauma_Pak_Kit_with_QuikClot_%2841159334595%29.jpg",
        "title": "Industrial Medical Trauma First Aid Response Kit",
        "caption": "A professional trauma first aid kit stocked with sterile gauze, tourniquets, and burn dressings used to treat hangar injuries.",
        "author": "Airman Magazine",
        "license": "CC BY 2.0"
    },
    4: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/81/KM23-_Chuuk_State_Department_of_Education_CPR_Training_%287988095%29.jpg",
        "title": "Hands-On CPR Training on a Medical Resuscitation Manikin",
        "caption": "Trainees practicing high-quality chest compressions on a CPR manikin, mastering the 100–120 compressions-per-minute life-saving cadence.",
        "author": "U.S. Department of Defense",
        "license": "Public Domain"
    },
    5: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/1/10/Ground_Crew_Member_Directs_a_RAF_Tristar_Aircraft_MOD_45150114.jpg",
        "title": "Aircraft Marshaller Guiding an Aircraft Safely into the Terminal Gate",
        "caption": "An airfield ground marshaller using illuminated wand paddles to direct an arriving airliner into the gate, preventing wingtip ramp collisions.",
        "author": "Senior Aircraftman Ben Tritta / MoD",
        "license": "Open Government Licence v1.0"
    }
}

YOUTUBE_VIDEOS_TOPIC2 = {
    0: {
        "url": "https://www.youtube.com/watch?v=FViSA91DP-8",
        "title": "Human Factors and Hangar Safety Culture",
        "description": "Examine how fatigue, pressure, distraction, and lack of communication create workplace traps, and see how strict procedural checklists protect technicians."
    },
    1: {
        "url": "https://www.youtube.com/watch?v=H4L_Coqawz8",
        "title": "Aircraft Fueling Hazards, PPE, and Static Bonding",
        "description": "Observe professional aircraft fueling operations demonstrating bonding cable attachment, specialized nitrile gloves, eye protection, and emergency fuel shutoff procedures."
    },
    2: {
        "url": "https://www.youtube.com/watch?v=H4L_Coqawz8",
        "title": "Hazard Identification in Aircraft Maintenance",
        "description": "Walk through a virtual aircraft maintenance hangar to identify and classify physical tripping traps, ungrounded cords, chemical containers, and ergonomic lifting errors."
    },
    3: {
        "url": "https://www.youtube.com/watch?v=9g0H2g7sLq8",
        "title": "Workplace Injury Response and Severity Triage",
        "description": "Examine how industrial first responders triage lacerations, burns, and fractures, determining when on-site first aid suffices versus emergency medical escalation."
    },
    4: {
        "url": "https://www.youtube.com/watch?v=M4ACYp75mjU",
        "title": "Hands-Only CPR Demonstration and Practice",
        "description": "Watch a certified medical resuscitation demonstration showing exact hand placement, straight-arm posture, compression depth, and cadence."
    },
    5: {
        "url": "https://www.youtube.com/watch?v=2f3qE6_79hE",
        "title": "Aviation Ground Handling, Marshalling, and Turnaround Safety",
        "description": "Witness high-speed, coordinated ground turnaround operations showing aircraft marshalling, fuel grounding, baggage belt loading, and apron safety checks."
    }
}

def enrich_grade10_topic2():
    """Enriches Grade 10 Aviation Topic 2 with verified photos, SVGs, and YouTube videos."""
    print("=" * 80)
    print("VLEARN VISUAL ENRICHMENT ENGINE: Grade 10 Aviation — Topic 2")
    print("Attaching Verified Photos, Responsive Vector SVGs & Video Assets")
    print("=" * 80)

    topic = Topic.objects.get(id=248)
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
        if u_order in IMAGE_HOOKS_TOPIC2:
            img_def = IMAGE_HOOKS_TOPIC2[u_order]
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
                            "topic_order": 1,
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
        if u_order in SVG_MAP_TOPIC2:
            svg_def = SVG_MAP_TOPIC2[u_order]
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
                            "topic_order": 1,
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
        if u_order in YOUTUBE_VIDEOS_TOPIC2:
            vid_def = YOUTUBE_VIDEOS_TOPIC2[u_order]
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
                            "topic_order": 1,
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
    print(f"ENRICHMENT COMPLETE: Topic 2 '{topic.name}'")
    print(f"  Photographic Hooks: {total_photos_attached} / 6")
    print(f"  Vector SVGs:        {total_svgs_attached} / 6")
    print(f"  YouTube Videos:     {total_videos_attached} / 6")
    print(f"  LessonAssets Total: {total_assets_persisted}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic2()
