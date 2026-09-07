"""
VLearn Grade 10 Aviation — Topic 363: Aircraft Tools and Materials
Visual Enrichment Engine (Verified Photos, Responsive Vector SVGs & Video Assets)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Aviation (Subject ID: 44)
Topic: Aircraft Tools and Materials (Topic ID: 363, Order: 5)

Enriches:
  - 5 First-Card Photographic Visual Hooks (Verified Direct Wikimedia URLs)
  - 5 Custom Responsive Vector SVGs (viewBox="0 0 800 450", Dark Slate Theme, Sanitized XML)
  - 5 Verified Educational YouTube Videos (Metals, composites, hand tools, vernier calipers, human factors)
  - Persists LessonAsset models and binds them to corresponding LessonBlocks

Usage:
  ./venv/bin/python curriculum/enrich_grade10_aviation_topic363.py
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
# 5 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 363
# =============================================================================

# SVG 1: Aerospace Metals Distribution (Lesson 1, Page 4)
SVG_METALS_DISTRIBUTION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <!-- Outer Card Frame -->
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Aircraft Structural Metallurgy: Materials Distribution &amp; Applications</text>

  <!-- Left: Airframe Zones Schema -->
  <g transform="translate(35, 70)">
    <!-- Schematic Airframe Box -->
    <rect x="0" y="0" width="370" height="235" rx="10" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <text x="185" y="24" font-size="12" font-weight="bold" fill="#94a3b8" text-anchor="middle">STRUCTURAL AIRFRAME METAL ZONES</text>

    <!-- Aircraft Silhouette Graphic -->
    <path d="M 40 120 L 120 100 L 180 35 L 210 35 L 215 100 L 320 105 L 345 75 L 355 75 L 350 120 L 355 125 L 345 125 L 320 115 L 215 120 L 210 185 L 180 185 L 120 120 Z" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>

    <!-- Wing & Skin: Aluminum (Blue) -->
    <circle cx="165" cy="70" r="14" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="165" y="74" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Al</text>
    <line x1="179" y1="70" x2="230" y2="60" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="230" y="48" width="125" height="24" rx="4" fill="#0369a1"/>
    <text x="292" y="64" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Aluminum (Skins/Ribs)</text>

    <!-- Engine & Firewall: Titanium (Orange) -->
    <circle cx="170" cy="110" r="14" fill="#ea580c" stroke="#fb923c" stroke-width="1.5"/>
    <text x="170" y="114" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Ti</text>
    <line x1="184" y1="110" x2="230" y2="110" stroke="#fb923c" stroke-width="1.5"/>
    <rect x="230" y="98" width="125" height="24" rx="4" fill="#c2410c"/>
    <text x="292" y="114" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Titanium (Firewall/Pylon)</text>

    <!-- Landing Gear: Steel (Red) -->
    <circle cx="130" cy="140" r="14" fill="#b91c1c" stroke="#f87171" stroke-width="1.5"/>
    <text x="130" y="144" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">St</text>
    <line x1="130" y1="154" x2="130" y2="175" stroke="#f87171" stroke-width="1.5"/>
    <rect x="68" y="175" width="125" height="24" rx="4" fill="#991b1b"/>
    <text x="130" y="191" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Steel (Gear/Axles)</text>

    <!-- Accessory Gearbox: Magnesium (Yellow) -->
    <circle cx="90" cy="105" r="12" fill="#ca8a04" stroke="#fde047" stroke-width="1.5"/>
    <text x="90" y="109" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Mg</text>
    <line x1="90" y1="93" x2="90" y2="60" stroke="#fde047" stroke-width="1.5"/>
    <rect x="30" y="48" width="115" height="24" rx="4" fill="#a16207"/>
    <text x="87" y="64" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Magnesium (Gearbox)</text>
  </g>

  <!-- Right: Properties Comparison Matrix -->
  <g transform="translate(425, 70)">
    <rect x="0" y="0" width="340" height="235" rx="10" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <text x="170" y="24" font-size="12" font-weight="bold" fill="#94a3b8" text-anchor="middle">METALLURGICAL PERFORMANCE COMPARISON</text>

    <!-- Item 1: Aluminum -->
    <g transform="translate(15, 40)">
      <rect x="0" y="0" width="310" height="38" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <text x="12" y="18" font-size="11" font-weight="bold" fill="#38bdf8">Aluminum Alloy 2024 / 7075</text>
      <text x="12" y="32" font-size="9.5" fill="#cbd5e1">Density: 2.7 g/cm³ | High strength-to-weight | Alclad protected</text>
    </g>

    <!-- Item 2: Steel -->
    <g transform="translate(15, 85)">
      <rect x="0" y="0" width="310" height="38" rx="6" fill="#1e293b" stroke="#f87171" stroke-width="1"/>
      <text x="12" y="18" font-size="11" font-weight="bold" fill="#f87171">High-Tensile Steel (Chrome-Moly)</text>
      <text x="12" y="32" font-size="9.5" fill="#cbd5e1">Density: 7.8 g/cm³ | Extreme yield strength &amp; hardness</text>
    </g>

    <!-- Item 3: Titanium -->
    <g transform="translate(15, 130)">
      <rect x="0" y="0" width="310" height="38" rx="6" fill="#1e293b" stroke="#fb923c" stroke-width="1"/>
      <text x="12" y="18" font-size="11" font-weight="bold" fill="#fb923c">Titanium Alloy (Ti-6Al-4V)</text>
      <text x="12" y="32" font-size="9.5" fill="#cbd5e1">Density: 4.5 g/cm³ | Strong to 600°C | Complete rust immunity</text>
    </g>

    <!-- Item 4: Magnesium -->
    <g transform="translate(15, 175)">
      <rect x="0" y="0" width="310" height="38" rx="6" fill="#1e293b" stroke="#fde047" stroke-width="1"/>
      <text x="12" y="18" font-size="11" font-weight="bold" fill="#fde047">Magnesium Alloy</text>
      <text x="12" y="32" font-size="9.5" fill="#cbd5e1">Density: 1.7 g/cm³ | Ultra-light non-structural casting</text>
    </g>
  </g>

  <!-- Bottom: Galvanic Isolation Rule Banner -->
  <g transform="translate(35, 320)">
    <rect x="0" y="0" width="730" height="95" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <text x="20" y="24" font-size="12" font-weight="bold" fill="#fde047">GALVANIC ISOLATION SAFETY PROTOCOL</text>
    <text x="20" y="45" font-size="10.5" fill="#e2e8f0">• Never install bare steel fasteners directly into aluminum airframe skins: dissimilar metal contact creates an active galvanic battery.</text>
    <text x="20" y="63" font-size="10.5" fill="#e2e8f0">• Aluminum acts as the sacrificial anode and corrodes into powdery oxide, destroying the structural joint.</text>
    <text x="20" y="81" font-size="10.5" fill="#38bdf8">• MANDATORY: Apply zinc-chromate or polysulfide barrier sealant to insulate dissimilar metals in all joints.</text>
  </g>
</svg>
""")

# SVG 2: Composite Laminate Architecture (Lesson 2, Page 4)
SVG_COMPOSITE_LAMINATE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <!-- Container Card -->
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Advanced Composite Laminate Architecture: Fibers, Matrix &amp; Plies</text>

  <!-- Left: Exploded Ply Layup Diagram -->
  <g transform="translate(35, 68)">
    <rect x="0" y="0" width="370" height="240" rx="10" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <text x="185" y="22" font-size="11" font-weight="bold" fill="#94a3b8" text-anchor="middle">QUASI-ISOTROPIC PLY STACK (CUTAWAY)</text>

    <!-- Ply 1: 0 Degrees (Cyan) -->
    <g transform="translate(25, 40)">
      <polygon points="40,0 290,0 260,35 10,35" fill="#0891b2" stroke="#22d3ee" stroke-width="1.5"/>
      <!-- Fiber orientation lines -->
      <line x1="70" y1="0" x2="40" y2="35" stroke="#cffafe" stroke-width="1" stroke-dasharray="2,2"/>
      <line x1="120" y1="0" x2="90" y2="35" stroke="#cffafe" stroke-width="1" stroke-dasharray="2,2"/>
      <line x1="170" y1="0" x2="140" y2="35" stroke="#cffafe" stroke-width="1" stroke-dasharray="2,2"/>
      <line x1="220" y1="0" x2="190" y2="35" stroke="#cffafe" stroke-width="1" stroke-dasharray="2,2"/>
      <text x="298" y="22" font-size="10" font-weight="bold" fill="#22d3ee">0° Ply (Span Tension)</text>
    </g>

    <!-- Ply 2: +45 Degrees (Purple) -->
    <g transform="translate(25, 80)">
      <polygon points="40,0 290,0 260,35 10,35" fill="#7c3aed" stroke="#c084fc" stroke-width="1.5"/>
      <line x1="60" y1="0" x2="120" y2="35" stroke="#f3e8ff" stroke-width="1" stroke-dasharray="2,2"/>
      <line x1="120" y1="0" x2="180" y2="35" stroke="#f3e8ff" stroke-width="1" stroke-dasharray="2,2"/>
      <line x1="180" y1="0" x2="240" y2="35" stroke="#f3e8ff" stroke-width="1" stroke-dasharray="2,2"/>
      <text x="298" y="22" font-size="10" font-weight="bold" fill="#c084fc">+45° Ply (Torsion)</text>
    </g>

    <!-- Ply 3: 90 Degrees (Emerald) -->
    <g transform="translate(25, 120)">
      <polygon points="40,0 290,0 260,35 10,35" fill="#059669" stroke="#34d399" stroke-width="1.5"/>
      <line x1="30" y1="18" x2="275" y2="18" stroke="#d1fae5" stroke-width="1" stroke-dasharray="3,3"/>
      <text x="298" y="22" font-size="10" font-weight="bold" fill="#34d399">90° Ply (Chord Tension)</text>
    </g>

    <!-- Cured Epoxy Matrix Base -->
    <g transform="translate(25, 160)">
      <polygon points="40,0 290,0 260,35 10,35" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
      <text x="150" y="22" font-size="10" font-weight="bold" fill="#f1f5f9" text-anchor="middle">Thermoset Epoxy Resin Matrix (Binder)</text>
      <text x="298" y="22" font-size="10" font-weight="bold" fill="#94a3b8">Matrix Phase</text>
    </g>
  </g>

  <!-- Right: Material System Comparison -->
  <g transform="translate(425, 68)">
    <rect x="0" y="0" width="340" height="240" rx="10" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <text x="170" y="22" font-size="11" font-weight="bold" fill="#94a3b8" text-anchor="middle">ADVANCED COMPOSITE MATERIALS MATRIX</text>

    <!-- Carbon Fiber Box -->
    <g transform="translate(15, 35)">
      <rect x="0" y="0" width="310" height="42" rx="6" fill="#1e293b" stroke="#06b6d4" stroke-width="1"/>
      <text x="10" y="16" font-size="11" font-weight="bold" fill="#22d3ee">Carbon Fiber Reinforced Polymer (CFRP)</text>
      <text x="10" y="32" font-size="9.5" fill="#cbd5e1">Wing skins, fuselage barrels | Zero fatigue | High stiffness</text>
    </g>

    <!-- Fiberglass Box -->
    <g transform="translate(15, 83)">
      <rect x="0" y="0" width="310" height="42" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
      <text x="10" y="16" font-size="11" font-weight="bold" fill="#34d399">Fiberglass (GFRP)</text>
      <text x="10" y="32" font-size="9.5" fill="#cbd5e1">Nose radomes, fairings | Dielectric (radar transparent)</text>
    </g>

    <!-- Kevlar Box -->
    <g transform="translate(15, 131)">
      <rect x="0" y="0" width="310" height="42" rx="6" fill="#1e293b" stroke="#eab308" stroke-width="1"/>
      <text x="10" y="16" font-size="11" font-weight="bold" fill="#fde047">Kevlar (Aramid Fiber)</text>
      <text x="10" y="32" font-size="9.5" fill="#cbd5e1">Engine containment rings, cargo floor | High impact &amp; puncture</text>
    </g>

    <!-- Wood / Fabric Box -->
    <g transform="translate(15, 179)">
      <rect x="0" y="0" width="310" height="42" rx="6" fill="#1e293b" stroke="#f97316" stroke-width="1"/>
      <text x="10" y="16" font-size="11" font-weight="bold" fill="#fb923c">Sitka Spruce &amp; Polyester Fabric</text>
      <text x="10" y="32" font-size="9.5" fill="#cbd5e1">Vintage &amp; glider structures | High flexibility | Vulnerable to rot</text>
    </g>
  </g>

  <!-- Bottom: Delamination Hazard Warning -->
  <g transform="translate(35, 320)">
    <rect x="0" y="0" width="730" height="95" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="20" y="24" font-size="12" font-weight="bold" fill="#f87171">CRITICAL HAZARD: BARELY VISIBLE IMPACT DAMAGE (BVID) &amp; DELAMINATION</text>
    <text x="20" y="45" font-size="10.5" fill="#e2e8f0">• Composites bounce back elastically after low-velocity impact (e.g. baggage cart bump), leaving outer paint unblemished.</text>
    <text x="20" y="63" font-size="10.5" fill="#e2e8f0">• Beneath the surface, internal fiber plies tear free from the matrix, creating an invisible structural hollow pocket.</text>
    <text x="20" y="81" font-size="10.5" fill="#38bdf8">• MANDATORY: Always conduct ultrasonic scanning or acoustic tap testing following any reported ground impact.</text>
  </g>
</svg>
""")

# SVG 3: Aircraft Hand Tools: Cutting, Striking & Holding (Lesson 3, Page 4)
SVG_HAND_TOOLS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <!-- Outer Card Frame -->
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Sheet Metal Assembly: Cleco Clamping, Aviation Snips &amp; Mallet Forming</text>

  <!-- Left: Cleco Clamping Assembly Cross-Section -->
  <g transform="translate(35, 68)">
    <rect x="0" y="0" width="370" height="240" rx="10" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <text x="185" y="22" font-size="11" font-weight="bold" fill="#94a3b8" text-anchor="middle">SHEET METAL JOINT CLAMPING (CROSS-SECTION)</text>

    <!-- Aluminum Skin 1 (Top) -->
    <rect x="40" y="100" width="290" height="12" fill="#38bdf8" stroke="#0284c7" stroke-width="1"/>
    <text x="280" y="93" font-size="9" fill="#38bdf8">Upper Skin (2024-T3)</text>

    <!-- Aluminum Skin 2 (Bottom) -->
    <rect x="60" y="112" width="270" height="12" fill="#0284c7" stroke="#0369a1" stroke-width="1"/>
    <text x="280" y="137" font-size="9" fill="#0284c7">Lower Skin (Alclad)</text>

    <!-- Cleco Fastener 1 (Clamped) -->
    <g transform="translate(100, 45)">
      <!-- Body -->
      <rect x="12" y="0" width="16" height="48" rx="3" fill="#d97706" stroke="#b45309" stroke-width="1"/>
      <rect x="15" y="48" width="10" height="8" fill="#94a3b8"/>
      <!-- Expanding Pin Through Sheets -->
      <rect x="17" y="55" width="6" height="32" fill="#e2e8f0"/>
      <!-- Bottom Step Clamp -->
      <polygon points="15,87 25,87 28,92 12,92" fill="#f59e0b"/>
      <text x="20" y="-8" font-size="9.5" font-weight="bold" fill="#f59e0b" text-anchor="middle">Cleco Fastener</text>
      <text x="20" y="28" font-size="8" fill="#ffffff" text-anchor="middle">1/8"</text>
    </g>

    <!-- Open Drilled Hole Ready for Rivet -->
    <g transform="translate(190, 95)">
      <rect x="0" y="5" width="14" height="24" fill="#0f172a" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="2,2"/>
      <text x="7" y="45" font-size="8.5" fill="#f87171" text-anchor="middle">Drilled Hole</text>
    </g>

    <!-- Permanent Solid Rivet Installed -->
    <g transform="translate(250, 95)">
      <ellipse cx="8" cy="5" rx="9" ry="4" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1"/>
      <rect x="4" y="5" width="8" height="24" fill="#94a3b8"/>
      <ellipse cx="8" cy="29" rx="8" ry="5" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1"/>
      <text x="8" y="48" font-size="8.5" fill="#94a3b8" text-anchor="middle">Driven Rivet</text>
    </g>

    <!-- Cleco Rule Note -->
    <rect x="25" y="180" width="320" height="42" rx="6" fill="#1e293b"/>
    <text x="185" y="197" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Cleco Deployment Rule:</text>
    <text x="185" y="212" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Insert Cleco in every 3rd or 4th hole to prevent skin slipping</text>
  </g>

  <!-- Right: Aviation Snips & Striking Tools -->
  <g transform="translate(425, 68)">
    <rect x="0" y="0" width="340" height="240" rx="10" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <text x="170" y="22" font-size="11" font-weight="bold" fill="#94a3b8" text-anchor="middle">AVIATION SNIP DECODING &amp; STRIKING TOOLS</text>

    <!-- Red Snip -->
    <g transform="translate(15, 35)">
      <rect x="0" y="0" width="310" height="34" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
      <rect x="8" y="7" width="20" height="20" rx="3" fill="#ef4444"/>
      <text x="36" y="16" font-size="10.5" font-weight="bold" fill="#f87171">RED HANDLES: Cuts Left (Counter-Clockwise)</text>
      <text x="36" y="28" font-size="8.5" fill="#cbd5e1">Waste scrap rolls away to the right; keeps main panel flat</text>
    </g>

    <!-- Green Snip -->
    <g transform="translate(15, 75)">
      <rect x="0" y="0" width="310" height="34" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
      <rect x="8" y="7" width="20" height="20" rx="3" fill="#10b981"/>
      <text x="36" y="16" font-size="10.5" font-weight="bold" fill="#34d399">GREEN HANDLES: Cuts Right (Clockwise)</text>
      <text x="36" y="28" font-size="8.5" fill="#cbd5e1">Waste scrap rolls away to the left; prevents stock binding</text>
    </g>

    <!-- Yellow Snip -->
    <g transform="translate(15, 115)">
      <rect x="0" y="0" width="310" height="34" rx="6" fill="#1e293b" stroke="#eab308" stroke-width="1.5"/>
      <rect x="8" y="7" width="20" height="20" rx="3" fill="#eab308"/>
      <text x="36" y="16" font-size="10.5" font-weight="bold" fill="#fde047">YELLOW HANDLES: Cuts Straight Lines</text>
      <text x="36" y="28" font-size="8.5" fill="#cbd5e1">Wide radius curves and straight boundary shearing</text>
    </g>

    <!-- Striking Tools Comparison -->
    <g transform="translate(15, 158)">
      <rect x="0" y="0" width="150" height="68" rx="6" fill="#1e293b" stroke="#f87171" stroke-width="1"/>
      <text x="75" y="18" font-size="9.5" font-weight="bold" fill="#f87171" text-anchor="middle">Ball-Peen Hammer</text>
      <text x="75" y="34" font-size="8" fill="#e2e8f0" text-anchor="middle">• For driving steel punches</text>
      <text x="75" y="47" font-size="8" fill="#e2e8f0" text-anchor="middle">• Hand-forming solid rivets</text>
      <text x="75" y="60" font-size="8" fill="#ef4444" text-anchor="middle">NEVER strike skin panel</text>
    </g>

    <g transform="translate(175, 158)">
      <rect x="0" y="0" width="150" height="68" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <text x="75" y="18" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Soft-Faced Mallet</text>
      <text x="75" y="34" font-size="8" fill="#e2e8f0" text-anchor="middle">• Rubber / plastic / brass</text>
      <text x="75" y="47" font-size="8" fill="#e2e8f0" text-anchor="middle">• Forms curves over wood</text>
      <text x="75" y="60" font-size="8" fill="#34d399" text-anchor="middle">Protects Alclad coating</text>
    </g>
  </g>

  <!-- Bottom: Stress Riser Prevention Protocol -->
  <g transform="translate(35, 320)">
    <rect x="0" y="0" width="730" height="95" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="20" y="24" font-size="12" font-weight="bold" fill="#38bdf8">AIRCRAFT HAND TOOL PRECISION RULES</text>
    <text x="20" y="45" font-size="10.5" fill="#e2e8f0">• HACKSAW PITCH: Ensure at least TWO teeth contact the metal thickness at all times to prevent tooth stripping.</text>
    <text x="20" y="63" font-size="10.5" fill="#e2e8f0">• FILING DIRECTION: Push files forward ONLY. Dragging in reverse rolls cutting teeth over and destroys the tool.</text>
    <text x="20" y="81" font-size="10.5" fill="#f87171">• NO SERRATED PLIERS: Tooth marks on aluminum linkages create stress risers that fracture under engine vibration.</text>
  </g>
</svg>
""")

# SVG 4: Marking, Measuring & Powered Tools (Lesson 4, Page 4)
SVG_MEASURING_POWERED = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <!-- Outer Card Frame -->
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Precision Measuring Instruments &amp; Spark-Free Pneumatics</text>

  <!-- Left: Vernier Caliper & Micrometer -->
  <g transform="translate(35, 68)">
    <rect x="0" y="0" width="370" height="240" rx="10" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <text x="185" y="22" font-size="11" font-weight="bold" fill="#94a3b8" text-anchor="middle">PRECISION MEASURING INSTRUMENTS</text>

    <!-- Caliper Diagram Graphic -->
    <g transform="translate(20, 35)">
      <!-- Main Beam -->
      <rect x="30" y="20" width="290" height="18" fill="#cbd5e1" stroke="#64748b" stroke-width="1"/>
      <!-- Fixed Outside Jaw -->
      <path d="M 30 20 L 30 75 L 42 75 L 42 20 Z" fill="#94a3b8" stroke="#475569" stroke-width="1"/>
      <!-- Fixed Inside Nib -->
      <path d="M 30 20 L 30 0 L 40 0 L 40 20 Z" fill="#94a3b8" stroke="#475569" stroke-width="1"/>

      <!-- Sliding Jaw -->
      <g transform="translate(65, 0)">
        <rect x="0" y="16" width="45" height="26" fill="#e2e8f0" stroke="#475569" stroke-width="1"/>
        <path d="M 0 20 L 0 75 L 12 75 L 12 20 Z" fill="#94a3b8" stroke="#475569" stroke-width="1"/>
        <path d="M 0 20 L 0 0 L 10 0 L 10 20 Z" fill="#94a3b8" stroke="#475569" stroke-width="1"/>
        <text x="22" y="32" font-size="7.5" fill="#0f172a" font-weight="bold" text-anchor="middle">Vernier</text>
      </g>

      <!-- Depth Rod -->
      <line x1="320" y1="29" x2="335" y2="29" stroke="#94a3b8" stroke-width="3"/>
      <text x="180" y="85" font-size="9" fill="#38bdf8" text-anchor="middle">Vernier Caliper: Outer Jaws | Inner Nibs | Depth Rod (0.02 mm)</text>
    </g>

    <!-- Micrometer Graphic -->
    <g transform="translate(20, 135)">
      <!-- C Frame -->
      <path d="M 60 40 A 35 35 0 0 1 60 -10 L 80 -10 L 80 40 Z" fill="none" stroke="#64748b" stroke-width="10"/>
      <!-- Anvil -->
      <rect x="75" y="10" width="8" height="10" fill="#cbd5e1"/>
      <!-- Spindle -->
      <rect x="95" y="10" width="22" height="10" fill="#e2e8f0"/>
      <!-- Barrel / Sleeve -->
      <rect x="117" y="6" width="45" height="18" fill="#94a3b8" stroke="#475569" stroke-width="1"/>
      <!-- Thimble -->
      <rect x="162" y="3" width="45" height="24" rx="2" fill="#cbd5e1" stroke="#475569" stroke-width="1"/>
      <!-- Ratchet Stop -->
      <rect x="207" y="8" width="18" height="14" rx="2" fill="#64748b"/>
      <text x="180" y="70" font-size="9" fill="#fde047" text-anchor="middle">Outside Micrometer: Spindle + Thimble + Ratchet Stop (0.001 mm)</text>
    </g>
  </g>

  <!-- Right: Pneumatic Spark-Free Power Tools -->
  <g transform="translate(425, 68)">
    <rect x="0" y="0" width="340" height="240" rx="10" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <text x="170" y="22" font-size="11" font-weight="bold" fill="#94a3b8" text-anchor="middle">PNEUMATIC (AIR) TOOLS VS. ELECTRIC TOOLS</text>

    <!-- Comparison 1: Spark Hazard -->
    <g transform="translate(15, 38)">
      <rect x="0" y="0" width="310" height="52" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
      <text x="10" y="18" font-size="11" font-weight="bold" fill="#34d399">100% Spark-Free Safety</text>
      <text x="10" y="32" font-size="9" fill="#e2e8f0">Air motors contain NO carbon brushes or commutators.</text>
      <text x="10" y="44" font-size="9" fill="#38bdf8">Eliminates explosion hazards in fuel cell bays and paint hangars.</text>
    </g>

    <!-- Comparison 2: Weight & Ergonomics -->
    <g transform="translate(15, 98)">
      <rect x="0" y="0" width="310" height="52" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="10" y="18" font-size="11" font-weight="bold" fill="#38bdf8">Lightweight Ergonomic Handling</text>
      <text x="10" y="32" font-size="9" fill="#e2e8f0">No heavy iron stator or copper electrical windings.</text>
      <text x="10" y="44" font-size="9" fill="#cbd5e1">60% lighter; eliminates arm fatigue during overhead drilling.</text>
    </g>

    <!-- Comparison 3: Power Versatility -->
    <g transform="translate(15, 158)">
      <rect x="0" y="0" width="310" height="65" rx="6" fill="#1e293b" stroke="#eab308" stroke-width="1.5"/>
      <text x="10" y="18" font-size="11" font-weight="bold" fill="#fde047">Aviation Pneumatic Tool Family</text>
      <text x="10" y="32" font-size="9" fill="#e2e8f0">• Air Drills: High-speed (up to 4,000 RPM) match drilling</text>
      <text x="10" y="45" font-size="9" fill="#e2e8f0">• Rivet Guns: 2X, 3X, 4X cyclic pulse driving</text>
      <text x="10" y="58" font-size="9" fill="#e2e8f0">• Die Grinders: Precision weld and fastener smoothing</text>
    </g>
  </g>

  <!-- Bottom: Layout Marking Safety Rule -->
  <g transform="translate(35, 320)">
    <rect x="0" y="0" width="730" height="95" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="20" y="24" font-size="12" font-weight="bold" fill="#f87171">STRICT PROHIBITION: NEVER USE HARDENED STEEL SCRIBES ON AIRFRAMES</text>
    <text x="20" y="45" font-size="10.5" fill="#e2e8f0">• Scratching aluminum with a steel point creates a microscopic sharp groove known as a stress riser.</text>
    <text x="20" y="63" font-size="10.5" fill="#e2e8f0">• Cyclic flight vibrations cause structural fatigue cracks to rapidly grow from the root of the scribe scratch.</text>
    <text x="20" y="81" font-size="10.5" fill="#34d399">• APPROVED PRACTICE: Use soft graphite pencils, fine felt-tip markers, or layout dye only.</text>
  </g>
</svg>
""")

# SVG 5: Tool Care, Shadow Board & FOD Prevention (Lesson 5, Page 4)
SVG_SHADOW_BOARD_FOD = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <!-- Outer Frame -->
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Aviation Tool Control: Foam Shadow Drawer &amp; FOD Prevention Protocol</text>

  <!-- Left: High-Contrast Foam Shadow Drawer -->
  <g transform="translate(35, 68)">
    <!-- Drawer Casing -->
    <rect x="0" y="0" width="370" height="240" rx="10" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <text x="185" y="22" font-size="11" font-weight="bold" fill="#94a3b8" text-anchor="middle">TWO-COLOR FOAM SHADOW DRAWER (BLACK / NEON RED)</text>

    <!-- Slot 1: Torque Wrench (Present) -->
    <g transform="translate(25, 38)">
      <rect x="0" y="0" width="320" height="34" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <!-- Torque Wrench Shape Inside -->
      <rect x="15" y="12" width="220" height="10" rx="2" fill="#94a3b8"/>
      <rect x="235" y="7" width="50" height="20" rx="4" fill="#64748b"/>
      <text x="150" y="22" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Micrometer Torque Wrench (Present)</text>
      <circle cx="300" cy="17" r="7" fill="#10b981"/>
      <text x="300" y="20" font-size="8" fill="#ffffff" font-weight="bold" text-anchor="middle">✓</text>
    </g>

    <!-- Slot 2: Duckbill Pliers (Present) -->
    <g transform="translate(25, 80)">
      <rect x="0" y="0" width="320" height="34" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <path d="M 20 17 L 90 10 L 160 17 L 90 24 Z" fill="#94a3b8"/>
      <rect x="160" y="11" width="100" height="12" rx="3" fill="#3b82f6"/>
      <text x="160" y="22" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Duckbill Smooth-Jaw Pliers (Present)</text>
      <circle cx="300" cy="17" r="7" fill="#10b981"/>
      <text x="300" y="20" font-size="8" fill="#ffffff" font-weight="bold" text-anchor="middle">✓</text>
    </g>

    <!-- Slot 3: MISSING TOOL SLOT (Neon Yellow / Red Flashing) -->
    <g transform="translate(25, 122)">
      <!-- Neon High-Contrast Floor Exposed -->
      <rect x="0" y="0" width="320" height="42" rx="6" fill="#fde047" stroke="#ef4444" stroke-width="2"/>
      <rect x="15" y="8" width="180" height="26" rx="4" fill="#eab308" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="3,3"/>
      <text x="105" y="25" font-size="10" font-weight="bold" fill="#7f1d1d" text-anchor="middle">[EMPTY CUTOUT]</text>
      <rect x="210" y="8" width="100" height="26" rx="4" fill="#b91c1c"/>
      <text x="260" y="24" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">MISSING: 3/8" Ratchet</text>
    </g>

    <!-- Alert Banner Inside Drawer -->
    <g transform="translate(25, 175)">
      <rect x="0" y="0" width="320" height="50" rx="6" fill="#7f1d1d" stroke="#ef4444" stroke-width="1.5"/>
      <text x="160" y="20" font-size="10" font-weight="bold" fill="#fca5a5" text-anchor="middle">FOD ALERT: AIRFRAME GROUNDED</text>
      <text x="160" y="38" font-size="8.5" fill="#fecaca" text-anchor="middle">No aircraft may be released until missing tool is found</text>
    </g>
  </g>

  <!-- Right: 5-Step Maintenance Sign-Off Protocol -->
  <g transform="translate(425, 68)">
    <rect x="0" y="0" width="340" height="240" rx="10" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <text x="170" y="22" font-size="11" font-weight="bold" fill="#94a3b8" text-anchor="middle">5-STEP MAINTENANCE SIGN-OFF PROCEDURE</text>

    <!-- Step 1 -->
    <g transform="translate(15, 35)">
      <circle cx="14" cy="14" r="10" fill="#3b82f6"/>
      <text x="14" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">1</text>
      <text x="32" y="14" font-size="10" font-weight="bold" fill="#e2e8f0">Cease Maintenance Work</text>
      <text x="32" y="25" font-size="8.5" fill="#94a3b8">Clean workpiece and bag scrap hardware</text>
    </g>

    <!-- Step 2 -->
    <g transform="translate(15, 75)">
      <circle cx="14" cy="14" r="10" fill="#3b82f6"/>
      <text x="14" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">2</text>
      <text x="32" y="14" font-size="10" font-weight="bold" fill="#e2e8f0">FOD Area Inspection</text>
      <text x="32" y="25" font-size="8.5" fill="#94a3b8">Sweep bay, verify no sockets or rags in cavities</text>
    </g>

    <!-- Step 3 -->
    <g transform="translate(15, 115)">
      <circle cx="14" cy="14" r="10" fill="#3b82f6"/>
      <text x="14" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">3</text>
      <text x="32" y="14" font-size="10" font-weight="bold" fill="#e2e8f0">Shadow Drawer Audit</text>
      <text x="32" y="25" font-size="8.5" fill="#94a3b8">Visual scan: confirm every foam slot is filled</text>
    </g>

    <!-- Step 4 -->
    <g transform="translate(15, 155)">
      <circle cx="14" cy="14" r="10" fill="#3b82f6"/>
      <text x="14" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">4</text>
      <text x="32" y="14" font-size="10" font-weight="bold" fill="#e2e8f0">Logbook Sign-Off</text>
      <text x="32" y="25" font-size="8.5" fill="#94a3b8">Record: "Tool accountability checked; 100% accounted for"</text>
    </g>

    <!-- Step 5 -->
    <g transform="translate(15, 195)">
      <circle cx="14" cy="14" r="10" fill="#10b981"/>
      <text x="14" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">5</text>
      <text x="32" y="14" font-size="10" font-weight="bold" fill="#34d399">Release to Service (CRS)</text>
      <text x="32" y="25" font-size="8.5" fill="#94a3b8">Inspector certifies airframe airworthy for flight</text>
    </g>
  </g>

  <!-- Bottom: Torque Wrench Storage Protocol -->
  <g transform="translate(35, 320)">
    <rect x="0" y="0" width="730" height="95" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <text x="20" y="24" font-size="12" font-weight="bold" fill="#fde047">TORQUE WRENCH CALIBRATION PRESERVATION RULE</text>
    <text x="20" y="45" font-size="10.5" fill="#e2e8f0">• Always dial micrometer torque wrenches back to the lowest graduation mark prior to storing in toolbox cases.</text>
    <text x="20" y="63" font-size="10.5" fill="#e2e8f0">• Storing under tension compresses the internal calibrated spring, causing permanent micro-structural creep.</text>
    <text x="20" y="81" font-size="10.5" fill="#38bdf8">• A crept spring clicks prematurely, leaving critical engine cylinder and landing gear bolts dangerously under-torqued.</text>
  </g>
</svg>
""")

# =============================================================================
# ENRICHMENT DATA STRUCTURES
# =============================================================================

PHOTO_HOOKS = {
    0: {
        "title": "All-Metal Aircraft Airframe Architecture",
        "caption": "A light aircraft featuring an all-metal semi-monocoque aluminum alloy fuselage skin and wing assembly riveted to internal structural bulkheads and ribs.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/51/Cessna_172_Skyhawk%2C_S2-AFH.jpg",
        "page": 1
    },
    1: {
        "title": "Advanced Composite Commercial Airliner Airframe",
        "caption": "A Boeing 787 Dreamliner featuring an airframe structure constructed with over 50% advanced carbon fiber reinforced polymer composites for superior fuel efficiency and fatigue life.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/55/Saudi_Arabian_Airlines_Boeing_787-10_Dreamliner_London_Gatwick_Airport.jpg",
        "page": 1
    },
    2: {
        "title": "Aircraft Sheet Metal Cleco Fasteners",
        "caption": "Spring-loaded Cleco temporary sheet metal fasteners used by aircraft structural mechanics to clamp pre-drilled aluminum skin panels into precise alignment prior to permanent riveting.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/57/Cleco_3.2_and_4.8mm_temporary_fasteners.jpg",
        "page": 1
    },
    3: {
        "title": "Precision Metric Vernier Caliper",
        "caption": "A precision stainless steel vernier caliper equipped with external measuring jaws, internal measuring nibs, and a sliding depth rod for verifying micro-tolerances in aviation manufacturing.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/c2/Mahr_MarCal_16_N_vernier_caliper.png",
        "page": 1
    },
    4: {
        "title": "Aviation Maintenance Technician Testing a Torque Wrench",
        "caption": "An aviation maintenance technician conducting calibration testing and inspection of a precision torque wrench in an aircraft intermediate maintenance department hangar.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Aircraft_Electronics_Technician_2nd_Class_Roberts_tests_a_torque_wrench_in_the_Aircraft_Intermediate_Maintenance_Department_hangar_-_DPLA_-_0689b07c7fece7f80dfae7c80bf1f3ba.jpeg",
        "page": 1
    }
}

SVG_MAP = {
    0: {
        "title": "Aircraft Structural Metal Distribution Blueprint",
        "svg": SVG_METALS_DISTRIBUTION,
        "page": 4
    },
    1: {
        "title": "Carbon Fiber Composite Laminate Ply Architecture",
        "svg": SVG_COMPOSITE_LAMINATE,
        "page": 4
    },
    2: {
        "title": "Sheet Metal Assembly and Tool Operations Blueprint",
        "svg": SVG_HAND_TOOLS,
        "page": 4
    },
    3: {
        "title": "Vernier Caliper and Outside Micrometer Anatomy Blueprint",
        "svg": SVG_MEASURING_POWERED,
        "page": 4
    },
    4: {
        "title": "Aviation Tool Control Shadow Drawer and Sign-Off Workflow",
        "svg": SVG_SHADOW_BOARD_FOD,
        "page": 4
    }
}

YOUTUBE_VIDEOS = {
    0: {
        "title": "Materials in Aerospace: Aluminum, Titanium & Composites",
        "description": "Visual breakdown of crystal structures, yield strength tests, and high-temperature performance of aerospace aluminum, titanium, and modern alloys.",
        "url": "https://www.youtube.com/watch?v=CGiR4LxaLO0",
        "page": 7
    },
    1: {
        "title": "From Metals to Composites: Decoding Aircraft Materials",
        "description": "Visual guide demonstrating how dry carbon fiber weaves are molded, vacuum-bagged, and cured under high pressure in industrial autoclaves.",
        "url": "https://www.youtube.com/watch?v=2Q5MFjibiX0",
        "page": 7
    },
    2: {
        "title": "Aircraft Hand Tools and Measuring Devices",
        "description": "Practical demonstration of aviation snips, hacksaw pitch selection, Cleco fastener insertion pliers, and proper edge deburring technique.",
        "url": "https://www.youtube.com/watch?v=NSlz_PSm7wY",
        "page": 7
    },
    3: {
        "title": "How to Read a Metric Vernier Caliper",
        "description": "Step-by-step visual instruction on reading main beam millimeter graduations and aligning Vernier scale divisions down to 0.02 mm accuracy.",
        "url": "https://www.youtube.com/watch?v=vkPlzmalvN4",
        "page": 7
    },
    4: {
        "title": "The Human Factors in Aircraft Maintenance",
        "description": "Exploration of cognitive fatigue, rushing, and procedural discipline in aviation maintenance hangars, illustrating how tool control checklists prevent accidents.",
        "url": "https://www.youtube.com/watch?v=FViSA91DP-8",
        "page": 7
    }
}

def enrich_grade10_topic363():
    """Binds verified Wikimedia photos, custom vector SVGs, and YouTube videos to Topic 363."""
    print("=" * 80)
    print("ENRICHING: Grade 10 Aviation — Topic 363 (Aircraft Tools and Materials)")
    print("=" * 80)

    subject = Subject.objects.get(id=44)
    topic = Topic.objects.get(id=363, subject=subject)
    lessons = Lesson.objects.filter(topic=topic).order_by("learning_unit__order")

    if not lessons.exists():
        print("[ERROR] No lessons found under Topic 363. Run ingest script first.")
        sys.exit(1)

    total_photos_attached = 0
    total_svgs_attached = 0
    total_videos_attached = 0
    total_assets_persisted = 0

    for lesson in lessons:
        u_order = lesson.learning_unit.order
        print(f"\nProcessing Unit {u_order + 1}: {lesson.title} (Lesson ID: {lesson.id})")

        # ---------------------------------------------------------------------
        # 1. Card 1 Photographic Visual Hook
        # ---------------------------------------------------------------------
        if u_order in PHOTO_HOOKS:
            img_def = PHOTO_HOOKS[u_order]
            photo_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=1,
                block_type="suggested_image"
            ).first()

            if photo_block:
                p_content = photo_block.content or {}
                p_content["resolved_image_url"] = img_def["url"]
                p_content["title"] = img_def["title"]
                p_content["caption"] = img_def["caption"]
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
                        "title": f"Lesson {u_order + 1} Photo Hook: {img_def['title']}",
                        "description": img_def["caption"],
                        "metadata": {
                            "topic_order": 5,
                            "unit_order": u_order,
                            "page": 1,
                            "source_url": img_def["url"]
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
                            "topic_order": 5,
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
                            "topic_order": 5,
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
    print(f"ENRICHMENT COMPLETE: Topic 363 '{topic.name}'")
    print(f"  Photographic Hooks: {total_photos_attached} / 5")
    print(f"  Vector SVGs:        {total_svgs_attached} / 5")
    print(f"  YouTube Videos:     {total_videos_attached} / 5")
    print(f"  LessonAssets Total: {total_assets_persisted}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic363()
