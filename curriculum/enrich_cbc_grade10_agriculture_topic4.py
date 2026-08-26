"""
VLearn CBC Grade 10 Agriculture — Topic 4: Field Management Practices
Visual Enrichment Engine (Phase 2: Vector SVGs, Verified Photos & Asset Persistence)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Field Management Practices (Order: 4)

Attaches:
  - 10 First-Card Photographic Visual Hooks (100% Tested HTTP 200 Direct Wikimedia URLs)
  - 8 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - 2 Verified Educational YouTube Videos (Lesson 2 Card 4 & Lesson 7 Card 4)
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade10_agriculture_topic4.py
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
# 8 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 4: FIELD MANAGEMENT
# =============================================================================

# SVG 1: The 6 Pillars of Post-Planting Field Management (Lesson 1, Page 3)
SVG_FIELD_MANAGEMENT_PILLARS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 6 Core Pillars of Post-Planting Field Management</text>

  <!-- Central Hub: Maximum Yield Potential -->
  <circle cx="400" cy="240" r="65" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
  <text x="400" y="230" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">MAXIMUM</text>
  <text x="400" y="248" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">YIELD</text>
  <text x="400" y="265" font-size="10" fill="#86efac" text-anchor="middle">&amp; GRADE 1 QUALITY</text>

  <!-- Pillar 1: Gapping & Thinning (Top Left) -->
  <g transform="translate(45, 75)">
    <rect x="0" y="0" width="205" height="95" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <text x="102" y="24" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">1. GAPPING &amp; THINNING</text>
    <text x="10" y="48" font-size="10" fill="#cbd5e1">• Replant failed spots</text>
    <text x="10" y="68" font-size="10" fill="#cbd5e1">• Remove crowded seedlings</text>
    <text x="10" y="85" font-size="9" fill="#94a3b8">Optimizes plant population</text>
  </g>
  <line x1="250" y1="125" x2="345" y2="200" stroke="#eab308" stroke-width="2" stroke-dasharray="3,3"/>

  <!-- Pillar 2: Weeding (Top Right) -->
  <g transform="translate(550, 75)">
    <rect x="0" y="0" width="205" height="95" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="102" y="24" font-size="11" font-weight="bold" fill="#fca5a5" text-anchor="middle">2. WEED ERADICATION</text>
    <text x="10" y="48" font-size="10" fill="#cbd5e1">• Stops water/nutrient theft</text>
    <text x="10" y="68" font-size="10" fill="#cbd5e1">• Eliminates pest breeding hosts</text>
    <text x="10" y="85" font-size="9" fill="#94a3b8">First 30 days critical window</text>
  </g>
  <line x1="550" y1="125" x2="455" y2="200" stroke="#ef4444" stroke-width="2" stroke-dasharray="3,3"/>

  <!-- Pillar 3: Pruning (Mid Left) -->
  <g transform="translate(35, 195)">
    <rect x="0" y="0" width="205" height="95" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="102" y="24" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">3. STRATEGIC PRUNING</text>
    <text x="10" y="48" font-size="10" fill="#cbd5e1">• Pinch lateral axil suckers</text>
    <text x="10" y="68" font-size="10" fill="#cbd5e1">• Clear lower stems to Y-fork</text>
    <text x="10" y="85" font-size="9" fill="#94a3b8">Maximizes large fruit size</text>
  </g>
  <line x1="240" y1="240" x2="335" y2="240" stroke="#22c55e" stroke-width="2"/>

  <!-- Pillar 4: Top-Dressing (Mid Right) -->
  <g transform="translate(560, 195)">
    <rect x="0" y="0" width="205" height="95" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
    <text x="102" y="24" font-size="11" font-weight="bold" fill="#67e8f9" text-anchor="middle">4. TOP-DRESSING (N)</text>
    <text x="10" y="48" font-size="10" fill="#cbd5e1">• Apply CAN / Liquid Manure</text>
    <text x="10" y="68" font-size="10" fill="#cbd5e1">• Knee-high &amp; flowering timing</text>
    <text x="10" y="85" font-size="9" fill="#94a3b8">Fuels chlorophyll &amp; canopy</text>
  </g>
  <line x1="560" y1="240" x2="465" y2="240" stroke="#06b6d4" stroke-width="2"/>

  <!-- Pillar 5: Staking & Trellising (Bottom Left) -->
  <g transform="translate(45, 315)">
    <rect x="0" y="0" width="205" height="95" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="102" y="24" font-size="11" font-weight="bold" fill="#d8b4fe" text-anchor="middle">5. STAKING &amp; TRELLISING</text>
    <text x="10" y="48" font-size="10" fill="#cbd5e1">• Lift vines off wet soil</text>
    <text x="10" y="68" font-size="10" fill="#cbd5e1">• Prevents fruit rotting &amp; slugs</text>
    <text x="10" y="85" font-size="9" fill="#94a3b8">Supports heavy fruit load</text>
  </g>
  <line x1="250" y1="355" x2="345" y2="280" stroke="#a855f7" stroke-width="2" stroke-dasharray="3,3"/>

  <!-- Pillar 6: Mulching (Bottom Right) -->
  <g transform="translate(550, 315)">
    <rect x="0" y="0" width="205" height="95" rx="8" fill="#0f172a" stroke="#ca8a04" stroke-width="1.5"/>
    <text x="102" y="24" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">6. ORGANIC MULCHING</text>
    <text x="10" y="48" font-size="10" fill="#cbd5e1">• Retains 70% soil moisture</text>
    <text x="10" y="68" font-size="10" fill="#cbd5e1">• Smothers weed seed germination</text>
    <text x="10" y="85" font-size="9" fill="#94a3b8">Regulates root temperature</text>
  </g>
  <line x1="550" y1="355" x2="455" y2="280" stroke="#ca8a04" stroke-width="2" stroke-dasharray="3,3"/>
</svg>
""")

# SVG 2: Capsicum Plant Pruning Architecture: Base Y-Fork Clearance (Lesson 2, Page 3)
SVG_CAPSICUM_PRUNING = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Capsicum Plant Pruning Architecture: Base Y-Fork Clearance</text>

  <!-- Left: Anatomical Diagram Graphic -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    
    <!-- Soil Line -->
    <line x1="20" y1="300" x2="320" y2="300" stroke="#78350f" stroke-width="4"/>
    <text x="170" y="325" font-size="11" fill="#ca8a04" text-anchor="middle">Damp Soil Surface (Pathogen Zone)</text>

    <!-- Main Stem Up to Y-Fork -->
    <line x1="170" y1="300" x2="170" y2="180" stroke="#15803d" stroke-width="10"/>
    
    <!-- Y-Fork Split -->
    <line x1="170" y1="180" x2="100" y2="75" stroke="#22c55e" stroke-width="8"/>
    <line x1="170" y1="180" x2="240" y2="75" stroke="#22c55e" stroke-width="8"/>
    
    <!-- Crown Flower in Center -->
    <circle cx="170" cy="175" r="7" fill="#eab308"/>
    <text x="170" y="160" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">Crown Flower (Pinch Off)</text>

    <!-- Upper Peppers -->
    <rect x="85" y="85" width="25" height="35" rx="6" fill="#ef4444"/>
    <rect x="230" y="85" width="25" height="35" rx="6" fill="#22c55e"/>

    <!-- Clear Base Zone Indicator -->
    <rect x="30" y="200" width="105" height="75" rx="6" fill="#1e293b" stroke="#ef4444" stroke-dasharray="3,3"/>
    <text x="82" y="225" font-size="9" font-weight="bold" fill="#fca5a5" text-anchor="middle">CLEAR BASE ZONE</text>
    <text x="82" y="245" font-size="8" fill="#cbd5e1" text-anchor="middle">15–20 cm Height</text>
    <text x="82" y="260" font-size="8" fill="#f87171" text-anchor="middle">Remove all suckers</text>
    <line x1="135" y1="235" x2="165" y2="235" stroke="#ef4444" stroke-width="2"/>
  </g>

  <!-- Right: 3 Rules of Capsicum Pruning -->
  <g transform="translate(415, 65)">
    <!-- Rule 1 -->
    <rect x="0" y="0" width="345" height="95" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="15" y="25" font-size="12" font-weight="bold" fill="#38bdf8">1. Clear Base Below Y-Fork (15–20 cm)</text>
    <text x="15" y="48" font-size="11" fill="#cbd5e1">• Strips all lower leaves and side suckers</text>
    <text x="15" y="68" font-size="11" fill="#cbd5e1">• Stops soil-borne fungal splash (Bacterial spot)</text>
    <text x="15" y="85" font-size="10" fill="#86efac">Provides vital under-canopy ventilation</text>

    <!-- Rule 2 -->
    <rect x="0" y="115" width="345" height="95" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <text x="15" y="25" font-size="12" font-weight="bold" fill="#fde047">2. Select 2 to 4 Frame Branches</text>
    <text x="15" y="48" font-size="11" fill="#cbd5e1">• Train strong outward-growing main branches</text>
    <text x="15" y="68" font-size="11" fill="#cbd5e1">• Pinch weak, inward-pointing crossing shoots</text>
    <text x="15" y="85" font-size="10" fill="#86efac">Concentrates sugars into large thick-walled fruit</text>

    <!-- Rule 3 -->
    <rect x="0" y="230" width="345" height="115" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="15" y="25" font-size="12" font-weight="bold" fill="#4ade80">3. Sanitize Tools &amp; Remove Crown Flower</text>
    <text x="15" y="48" font-size="11" fill="#cbd5e1">• Dip secateurs in 10% bleach / methylated spirit</text>
    <text x="15" y="68" font-size="11" fill="#cbd5e1">• Prevents TMV / PVY viral sap transmission</text>
    <text x="15" y="88" font-size="11" fill="#cbd5e1">• Pinch crown flower in Y-fork to build bush vigor</text>
    <text x="15" y="105" font-size="10" fill="#94a3b8">Compost prunings away from field</text>
  </g>
</svg>
""")

# SVG 3: Tomato Leaf Axil Anatomy: Sucker Identification & Pinching (Lesson 3, Page 3)
SVG_TOMATO_SUCKER_ANATOMY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Tomato Leaf Axil Anatomy: Sucker Identification &amp; Removal</text>

  <!-- Left: Botanical Axil Diagram -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="345" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    
    <!-- Central Main Stem -->
    <line x1="170" y1="320" x2="170" y2="30" stroke="#15803d" stroke-width="14"/>
    <text x="170" y="20" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">Central Main Stem</text>

    <!-- Leaf Petiole Branching at 45° -->
    <line x1="170" y1="200" x2="280" y2="120" stroke="#16a34a" stroke-width="9"/>
    <ellipse cx="295" cy="110" rx="18" ry="10" fill="#22c55e"/>
    <text x="295" y="90" font-size="10" font-weight="bold" fill="#86efac" text-anchor="middle">Leaf Petiole</text>

    <!-- Lateral Sucker in the V-Axil -->
    <line x1="170" y1="195" x2="215" y2="105" stroke="#eab308" stroke-width="6"/>
    <ellipse cx="220" cy="95" rx="10" ry="7" fill="#fde047"/>
    <text x="235" y="80" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">Lateral Sucker</text>

    <!-- Highlighted V-Axil -->
    <circle cx="178" cy="190" r="18" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="3,3"/>
    <text x="110" y="225" font-size="10" font-weight="bold" fill="#fca5a5" text-anchor="middle">V-Shaped Leaf Axil</text>
    <line x1="110" y1="210" x2="160" y2="195" stroke="#ef4444" stroke-width="1.5"/>

    <rect x="20" y="280" width="300" height="45" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="300" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Target: Remove when 5–10 cm long</text>
    <text x="170" y="315" font-size="9" fill="#cbd5e1" text-anchor="middle">Prevents large open wounds and nutrient diversion</text>
  </g>

  <!-- Right: The Pinch-and-Twist Technique -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#15803d"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">THE PINCH-AND-TWIST PROTOCOL</text>

    <g transform="translate(15, 45)">
      <text x="0" y="20" font-size="12" font-weight="bold" fill="#fde047">Step 1: Grip Sucker Base</text>
      <text x="0" y="38" font-size="11" fill="#cbd5e1">Hold firmly between thumb and index finger</text>

      <text x="0" y="70" font-size="12" font-weight="bold" fill="#fde047">Step 2: Snap Sideways (90°)</text>
      <text x="0" y="88" font-size="11" fill="#cbd5e1">Bend sucker sharply sideways until it snaps clean</text>

      <text x="0" y="120" font-size="12" font-weight="bold" fill="#ef4444">CRITICAL WARNING: Never Pull Downward!</text>
      <text x="0" y="138" font-size="11" fill="#fca5a5">Pulling downward tears stem skin, inviting blight!</text>

      <text x="0" y="170" font-size="12" font-weight="bold" fill="#86efac">Step 3: Morning Pruning Rule</text>
      <text x="0" y="188" font-size="11" fill="#cbd5e1">Prune on sunny mornings so wounds callus quickly</text>
    </g>

    <rect x="15" y="275" width="315" height="55" rx="6" fill="#1e293b" stroke="#22c55e"/>
    <text x="172" y="295" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Result: Premium Grade 1 Fruit Size</text>
    <text x="172" y="313" font-size="9" fill="#86efac" text-anchor="middle">100% of sugars directed into central fruit trusses</text>
  </g>
</svg>
""")

# SVG 4: Single-Stem vs Multiple-Stem Tomato Architecture (Lesson 4, Page 3)
SVG_TOMATO_SYSTEMS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Tomato Pruning Architecture: Single-Stem vs Two-Stem System</text>

  <!-- Left: Single-Stem (Greenhouse) -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="335" height="345" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="335" height="32" rx="10" fill="#0284c7"/>
    <text x="167" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. SINGLE-STEM (GREENHOUSE)</text>

    <!-- Single Stem Graphic -->
    <line x1="167" y1="310" x2="167" y2="55" stroke="#38bdf8" stroke-width="7"/>
    <!-- Large Fruits -->
    <circle cx="140" cy="120" r="14" fill="#ef4444"/><circle cx="195" cy="180" r="14" fill="#ef4444"/>
    <circle cx="140" cy="240" r="14" fill="#ef4444"/>
    <text x="167" y="50" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Single Vertical Leader</text>

    <g transform="translate(15, 275)">
      <text x="0" y="15" font-size="10" font-weight="bold" fill="#38bdf8">• Spacing: 30–45 cm (High Density)</text>
      <text x="0" y="30" font-size="10" fill="#cbd5e1">• Fruit Size: Extra Large (Grade 1)</text>
      <text x="0" y="45" font-size="9" fill="#f87171">• High sunscald risk in open fields</text>
    </g>
  </g>

  <!-- Right: Two-Stem (Open-Field) -->
  <g transform="translate(420, 65)">
    <rect x="0" y="0" width="335" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="335" height="32" rx="10" fill="#15803d"/>
    <text x="167" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. TWO-STEM (OPEN-FIELD)</text>

    <!-- Two-Stem Graphic -->
    <line x1="167" y1="310" x2="167" y2="210" stroke="#22c55e" stroke-width="7"/>
    <!-- Branching below first flower -->
    <line x1="167" y1="210" x2="105" y2="55" stroke="#22c55e" stroke-width="6"/>
    <line x1="167" y1="210" x2="230" y2="55" stroke="#22c55e" stroke-width="6"/>
    <!-- First Flower Cluster Anchor -->
    <circle cx="167" cy="205" r="6" fill="#eab308"/>
    <text x="167" y="225" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">1st Flower Truss Split</text>
    <!-- Medium Fruits -->
    <circle cx="90" cy="110" r="10" fill="#ef4444"/><circle cx="245" cy="110" r="10" fill="#ef4444"/>

    <g transform="translate(15, 275)">
      <text x="0" y="15" font-size="10" font-weight="bold" fill="#4ade80">• Spacing: 60–75 cm (Wide Rows)</text>
      <text x="0" y="30" font-size="10" fill="#cbd5e1">• Fruit Count: Higher total per plant</text>
      <text x="0" y="45" font-size="9" fill="#86efac">• Dense canopy stops solar sunscald</text>
    </g>
  </g>
</svg>
""")

# SVG 5: Perennial Crop Pruning: Capping vs Multiple-Stem vs Cutting Back (Lesson 5, Page 3)
SVG_PERENNIAL_PRUNING = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Perennial Tree Systems: Capping vs Multiple-Stem vs Cutting Back</text>

  <!-- 1. Single-Stem Capped -->
  <g transform="translate(35, 65)">
    <rect x="0" y="0" width="225" height="345" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="225" height="30" rx="10" fill="#0284c7"/>
    <text x="112" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. SINGLE-STEM CAPPED</text>

    <!-- Tree Graphic -->
    <line x1="112" y1="280" x2="112" y2="130" stroke="#78350f" stroke-width="12"/>
    <!-- Capping Cut -->
    <line x1="95" y1="130" x2="130" y2="130" stroke="#ef4444" stroke-width="3"/>
    <text x="112" y="115" font-size="9" font-weight="bold" fill="#fca5a5" text-anchor="middle">Capped @ 1.5–1.8 m</text>
    <!-- Lateral Spreading Canopy -->
    <line x1="112" y1="160" x2="45" y2="180" stroke="#15803d" stroke-width="6"/>
    <line x1="112" y1="160" x2="180" y2="180" stroke="#15803d" stroke-width="6"/>

    <g transform="translate(10, 210)">
      <text x="0" y="15" font-size="10" font-weight="bold" fill="#38bdf8">• Easy ground harvesting</text>
      <text x="0" y="32" font-size="9" fill="#cbd5e1">• High wind resistance</text>
      <text x="0" y="49" font-size="9" fill="#cbd5e1">• Compact bush framework</text>
    </g>
    <rect x="10" y="295" width="205" height="35" rx="4" fill="#0c4a6e"/>
    <text x="112" y="316" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Easy Harvest Architecture</text>
  </g>

  <!-- 2. Multiple-Stem -->
  <g transform="translate(285, 65)">
    <rect x="0" y="0" width="225" height="345" rx="10" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect x="0" y="0" width="225" height="30" rx="10" fill="#ca8a04"/>
    <text x="112" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. MULTIPLE-STEM</text>

    <!-- Tree Graphic -->
    <line x1="112" y1="280" x2="60" y2="100" stroke="#78350f" stroke-width="8"/>
    <line x1="112" y1="280" x2="112" y2="90" stroke="#78350f" stroke-width="8"/>
    <line x1="112" y1="280" x2="165" y2="100" stroke="#78350f" stroke-width="8"/>
    <text x="112" y="75" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">2–4 Vertical Stems</text>

    <g transform="translate(10, 210)">
      <text x="0" y="15" font-size="10" font-weight="bold" fill="#fde047">• High early crop tonnage</text>
      <text x="0" y="32" font-size="9" fill="#cbd5e1">• Cyclic stem replacement</text>
      <text x="0" y="49" font-size="9" fill="#cbd5e1">• Rotational 4–6 yr cycles</text>
    </g>
    <rect x="10" y="295" width="205" height="35" rx="4" fill="#78350f"/>
    <text x="112" y="316" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">Cyclic Yield Maximizer</text>
  </g>

  <!-- 3. Cutting Back (Rejuvenation) -->
  <g transform="translate(535, 65)">
    <rect x="0" y="0" width="230" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="230" height="30" rx="10" fill="#15803d"/>
    <text x="115" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. CUTTING BACK (REJUVENATE)</text>

    <!-- Stump Graphic -->
    <line x1="115" y1="280" x2="115" y2="200" stroke="#78350f" stroke-width="20"/>
    <!-- 45° Angled Saw Cut -->
    <line x1="95" y1="210" x2="135" y2="190" stroke="#ef4444" stroke-width="4"/>
    <text x="115" y="180" font-size="9" font-weight="bold" fill="#fca5a5" text-anchor="middle">Cut @ 15–30 cm (45°)</text>
    <!-- Fresh Flush of Suckers -->
    <line x1="105" y1="200" x2="80" y2="120" stroke="#22c55e" stroke-width="5"/>
    <line x1="125" y1="200" x2="150" y2="120" stroke="#22c55e" stroke-width="5"/>
    <text x="115" y="105" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">Fresh Root-Crown Suckers</text>

    <g transform="translate(10, 210)">
      <text x="0" y="15" font-size="10" font-weight="bold" fill="#4ade80">• Restores 15+ yr old trees</text>
      <text x="0" y="32" font-size="9" fill="#cbd5e1">• Uses existing root network</text>
      <text x="0" y="49" font-size="9" fill="#cbd5e1">• Zero replanting cost</text>
    </g>
    <rect x="10" y="295" width="210" height="35" rx="4" fill="#14532d"/>
    <text x="115" y="316" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">Old Tree Regeneration</text>
  </g>
</svg>
""")

# SVG 6: Fertilizer Ring Application Diagram at Crop Drip Line (Lesson 7, Page 2)
SVG_RING_APPLICATION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Precision Fertilizer Ring Application at the Crop Drip Line</text>

  <!-- Overhead Schematic (Left) -->
  <g transform="translate(50, 65)">
    <rect x="0" y="0" width="340" height="345" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>

    <!-- Outer Leaf Canopy Perimeter (Drip Line) -->
    <circle cx="170" cy="170" r="120" fill="#14532d" opacity="0.4" stroke="#22c55e" stroke-width="2" stroke-dasharray="4,4"/>
    <text x="170" y="40" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Outer Leaf Drip Line (Root Zone)</text>

    <!-- Ring Trench with Fertilizer Granules -->
    <circle cx="170" cy="170" r="95" fill="none" stroke="#eab308" stroke-width="8"/>
    <text x="170" y="90" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">3 cm Circular Trench (Covered)</text>

    <!-- Stem Safety Buffer Zone -->
    <circle cx="170" cy="170" r="45" fill="#1e293b" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="2,2"/>
    <text x="170" y="145" font-size="8" font-weight="bold" fill="#fca5a5" text-anchor="middle">NO-FERTILIZER ZONE</text>

    <!-- Central Main Stem -->
    <circle cx="170" cy="170" r="14" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
    <text x="170" y="174" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">STEM</text>

    <rect x="20" y="295" width="300" height="35" rx="4" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="316" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Feeder Root Absorption Perimeter: 8–15 cm</text>
  </g>

  <!-- Right: 4-Step Rules of Application -->
  <g transform="translate(420, 65)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#15803d"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">4 RULES FOR RING TOP-DRESSING</text>

    <g transform="translate(15, 45)">
      <text x="0" y="20" font-size="12" font-weight="bold" fill="#fde047">1. Place Exactly at Drip Line (8–15 cm)</text>
      <text x="0" y="38" font-size="11" fill="#cbd5e1">Aligns with water-absorbing root hairs underground</text>

      <text x="0" y="70" font-size="12" font-weight="bold" fill="#ef4444">2. Zero Contact with Main Stem!</text>
      <text x="0" y="88" font-size="11" fill="#fca5a5">Stem contact causes lethal chemical 'fertilizer burn'</text>

      <text x="0" y="120" font-size="12" font-weight="bold" fill="#86efac">3. Cover with Soil Immediately</text>
      <text x="0" y="138" font-size="11" fill="#cbd5e1">Stops nitrogen volatilization into ammonia gas</text>

      <text x="0" y="170" font-size="12" font-weight="bold" fill="#38bdf8">4. Water / Irrigate Post-Application</text>
      <text x="0" y="188" font-size="11" fill="#cbd5e1">Dissolves mineral ions directly into root capillary zone</text>
    </g>

    <rect x="15" y="275" width="315" height="55" rx="6" fill="#1e293b" stroke="#22c55e"/>
    <text x="172" y="295" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">100% Nutrient Uptake Efficiency</text>
    <text x="172" y="313" font-size="9" fill="#86efac" text-anchor="middle">Zero atmospheric gas loss &amp; zero storm runoff</text>
  </g>
</svg>
""")

# SVG 7: Nitrogen Deficiency Leaf Chlorosis Diagnostic Progression (Lesson 8, Page 2)
SVG_NITROGEN_DEFICIENCY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Nitrogen Deficiency Leaf Chlorosis Diagnostic Progression</text>

  <!-- Stage 1: Healthy Leaf -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="220" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="30" rx="10" fill="#15803d"/>
    <text x="110" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. HEALTHY LEAF</text>

    <!-- Leaf Graphic -->
    <path d="M 110 50 Q 180 140 110 230 Q 40 140 110 50 Z" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
    <line x1="110" y1="50" x2="110" y2="230" stroke="#86efac" stroke-width="3"/>
    <text x="110" y="255" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Dark Green Color</text>
    <text x="110" y="275" font-size="9" fill="#cbd5e1" text-anchor="middle">100% Chlorophyll density</text>
    <text x="110" y="295" font-size="9" fill="#cbd5e1" text-anchor="middle">Peak photosynthesis</text>
  </g>

  <!-- Stage 2: Early Mobile Deficiency -->
  <g transform="translate(290, 65)">
    <rect x="0" y="0" width="220" height="345" rx="10" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="30" rx="10" fill="#ca8a04"/>
    <text x="110" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. EARLY CHLOROSIS</text>

    <!-- Leaf Graphic -->
    <path d="M 110 50 Q 180 140 110 230 Q 40 140 110 50 Z" fill="#a16207" stroke="#eab308" stroke-width="2"/>
    <line x1="110" y1="50" x2="110" y2="230" stroke="#fde047" stroke-width="3"/>
    <!-- Yellow Tip -->
    <polygon points="110,50 130,100 90,100" fill="#eab308"/>
    <text x="110" y="255" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">Pale Yellowing at Tip</text>
    <text x="110" y="275" font-size="9" fill="#cbd5e1" text-anchor="middle">Appears on older leaves</text>
    <text x="110" y="295" font-size="9" fill="#cbd5e1" text-anchor="middle">Nitrogen moving to shoot</text>
  </g>

  <!-- Stage 3: Classic V-Shaped Pattern -->
  <g transform="translate(535, 65)">
    <rect x="0" y="0" width="220" height="345" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="30" rx="10" fill="#991b1b"/>
    <text x="110" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. SEVERE V-SHAPE (MAIZE)</text>

    <!-- Leaf Graphic -->
    <path d="M 110 50 Q 180 140 110 230 Q 40 140 110 50 Z" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
    <!-- V-Shaped Yellow Midrib -->
    <polygon points="110,50 140,160 110,190 80,160" fill="#eab308" stroke="#fde047" stroke-width="1.5"/>
    <text x="110" y="255" font-size="10" font-weight="bold" fill="#fca5a5" text-anchor="middle">V-Shaped Midrib Yellowing</text>
    <text x="110" y="275" font-size="9" fill="#cbd5e1" text-anchor="middle">Tip &amp; midrib turn yellow</text>
    <text x="110" y="295" font-size="9" fill="#f87171" text-anchor="middle">Emergency CAN required</text>
  </g>
</svg>
""")

# SVG 8: Agricultural Nitrogen Runoff & Aquatic Eutrophication Chain (Lesson 9, Page 3)
SVG_EUTROPHICATION_CHAIN = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Agricultural Nitrogen Runoff &amp; Aquatic Eutrophication Chain</text>

  <!-- Step 1: Farm Runoff -->
  <g transform="translate(35, 65)">
    <rect x="0" y="0" width="165" height="345" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <rect x="0" y="0" width="165" height="30" rx="8" fill="#ca8a04"/>
    <text x="82" y="20" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">1. FERTILIZER RUNOFF</text>
    <text x="10" y="55" font-size="10" fill="#cbd5e1">• Excessive broadcast</text>
    <text x="10" y="75" font-size="10" fill="#cbd5e1">• Uncovered granules</text>
    <text x="10" y="95" font-size="10" fill="#cbd5e1">• Heavy storm rain</text>
    <text x="10" y="115" font-size="9" fill="#fde047">N washes into river</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <line x1="205" y1="240" x2="225" y2="240" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="225,235 235,240 225,245" fill="#38bdf8"/>

  <!-- Step 2: Algal Bloom -->
  <g transform="translate(225, 65)">
    <rect x="0" y="0" width="165" height="345" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="165" height="30" rx="8" fill="#15803d"/>
    <text x="82" y="20" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">2. ALGAL BLOOM</text>
    <text x="10" y="55" font-size="10" fill="#cbd5e1">• Nutrient overload</text>
    <text x="10" y="75" font-size="10" fill="#cbd5e1">• Explosive algae mat</text>
    <text x="10" y="95" font-size="10" fill="#cbd5e1">• Blocks sunlight</text>
    <text x="10" y="115" font-size="9" fill="#86efac">Underwater plants die</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <line x1="395" y1="240" x2="415" y2="240" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="415,235 425,240 415,245" fill="#38bdf8"/>

  <!-- Step 3: Decomposition -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="165" height="345" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="0" y="0" width="165" height="30" rx="8" fill="#7e22ce"/>
    <text x="82" y="20" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">3. DECOMPOSITION</text>
    <text x="10" y="55" font-size="10" fill="#cbd5e1">• Billions of algae die</text>
    <text x="10" y="75" font-size="10" fill="#cbd5e1">• Aerobic bacteria feed</text>
    <text x="10" y="95" font-size="10" fill="#cbd5e1">• Consume dissolved O₂</text>
    <text x="10" y="115" font-size="9" fill="#d8b4fe">Water turns anoxic</text>
  </g>

  <!-- Arrow 3 -> 4 -->
  <line x1="585" y1="240" x2="605" y2="240" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="605,235 615,240 605,245" fill="#38bdf8"/>

  <!-- Step 4: Dead Zones -->
  <g transform="translate(605, 65)">
    <rect x="0" y="0" width="160" height="345" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="160" height="30" rx="8" fill="#991b1b"/>
    <text x="80" y="20" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">4. DEAD ZONE / FISH KILL</text>
    <text x="10" y="55" font-size="10" fill="#cbd5e1">• Zero oxygen (Anoxia)</text>
    <text x="10" y="75" font-size="10" fill="#cbd5e1">• Fish suffocate en masse</text>
    <text x="10" y="95" font-size="10" fill="#cbd5e1">• Foul water odor</text>
    <text x="10" y="115" font-size="9" fill="#fca5a5">Destroys fisheries</text>
  </g>
</svg>
""")

SVG_MAP = {
    1: {"page": 3, "svg": SVG_FIELD_MANAGEMENT_PILLARS, "title": "The 6 Core Pillars of Post-Planting Field Management"},
    2: {"page": 3, "svg": SVG_CAPSICUM_PRUNING, "title": "Capsicum Plant Pruning Architecture: Base Y-Fork Clearance"},
    3: {"page": 3, "svg": SVG_TOMATO_SUCKER_ANATOMY, "title": "Tomato Leaf Axil Anatomy: Sucker Identification & Removal"},
    4: {"page": 3, "svg": SVG_TOMATO_SYSTEMS, "title": "Tomato Pruning Architecture: Single-Stem vs Two-Stem System"},
    5: {"page": 3, "svg": SVG_PERENNIAL_PRUNING, "title": "Perennial Tree Systems: Capping vs Multiple-Stem vs Cutting Back"},
    7: {"page": 2, "svg": SVG_RING_APPLICATION, "title": "Precision Fertilizer Ring Application at the Crop Drip Line"},
    8: {"page": 2, "svg": SVG_NITROGEN_DEFICIENCY, "title": "Nitrogen Deficiency Leaf Chlorosis Diagnostic Progression"},
    9: {"page": 3, "svg": SVG_EUTROPHICATION_CHAIN, "title": "Agricultural Nitrogen Runoff & Aquatic Eutrophication Chain"}
}

def enrich_grade10_topic4():
    """Injects verified photos, responsive vector SVGs, YouTube embeds, and creates LessonAssets."""
    print("=" * 80)
    print("STARTING ENRICHMENT: CBC Grade 10 Agriculture — Topic 4: Field Management Practices")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()
    topic = Topic.objects.filter(subject=subject, name="Field Management Practices").first()

    assert topic, "Topic 'Field Management Practices' not found!"

    images_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grade10_topic4_verified_images.json")
    with open(images_path, "r", encoding="utf-8") as f:
        verified_images = json.load(f)

    lessons = list(topic.lessons.all().order_by("learning_unit__order"))
    LessonAsset.objects.filter(lesson__in=lessons).delete()

    total_images_attached = 0
    total_svgs_attached = 0
    total_videos_attached = 0
    total_assets_persisted = 0

    for lesson in lessons:
        u_order = lesson.learning_unit.order
        u_str = str(u_order)

        # ---------------------------------------------------------------------
        # 1. First-Card Visual Hook (Photographic Wikimedia URL)
        # ---------------------------------------------------------------------
        hook_block = LessonBlock.objects.filter(
            lesson=lesson,
            page_number=1,
            block_type="suggested_image"
        ).first()

        if hook_block and u_str in verified_images:
            img_data = verified_images[u_str]
            content = hook_block.content or {}
            content["resolved_image_url"] = img_data["url"]
            content["url"] = img_data["url"]
            content["attribution"] = f"Photo by {img_data.get('author', 'Wikimedia Commons')} ({img_data.get('licensing', 'CC')})"
            content["commons_url"] = img_data.get("commons_url", "")
            hook_block.content = content
            hook_block.save()
            total_images_attached += 1

            asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="image",
                source_type="external",
                storage_type="url",
                status="attached",
                title=f"Lesson {u_order} Visual Hook: {hook_block.title}",
                description=content.get("caption", hook_block.title),
                url=img_data["url"],
                metadata={
                    "topic_order": 4,
                    "unit_order": u_order,
                    "card": 1,
                    "author": img_data.get("author", "Wikimedia Commons"),
                    "licensing": img_data.get("licensing", "CC"),
                    "commons_url": img_data.get("commons_url", "")
                }
            )
            hook_block.assets.add(asset)
            total_assets_persisted += 1
            print(f"  [Image Hook Attached] Lesson {u_order}: {img_data['title'][:50]}...")

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
                diag_block.save()
                total_svgs_attached += 1

                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    asset_type="diagram",
                    source_type="ai_generated",
                    storage_type="embed",
                    status="attached",
                    title=f"Lesson {u_order} Diagram: {svg_def['title']}",
                    description=diag_content.get("caption", svg_def["title"]),
                    metadata={
                        "topic_order": 4,
                        "unit_order": u_order,
                        "page": svg_def["page"],
                        "svg_content": svg_def["svg"]
                    }
                )
                diag_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [Vector SVG Attached] Lesson {u_order}: {svg_def['title']}")

        # ---------------------------------------------------------------------
        # 3. Educational YouTube Videos (Lesson 2 & Lesson 7)
        # ---------------------------------------------------------------------
        video_blocks = LessonBlock.objects.filter(
            lesson=lesson,
            block_type="suggested_video"
        )
        for v_block in video_blocks:
            v_content = v_block.content or {}
            v_url = v_content.get("url", "")
            if v_url:
                total_videos_attached += 1
                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    asset_type="youtube",
                    source_type="external",
                    storage_type="url",
                    status="attached",
                    title=f"Lesson {u_order} Video: {v_block.title}",
                    description=v_content.get("description", v_block.title),
                    url=v_url,
                    metadata={
                        "topic_order": 4,
                        "unit_order": u_order,
                        "youtube_url": v_url
                    }
                )
                v_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [YouTube Video Attached] Lesson {u_order}: {v_block.title}")

    print("=" * 80)
    print(f"ENRICHMENT COMPLETE: Topic 4 '{topic.name}'")
    print(f"  Photographic Hooks: {total_images_attached} / 10")
    print(f"  Vector SVGs:        {total_svgs_attached} / 8")
    print(f"  YouTube Videos:     {total_videos_attached} / 2")
    print(f"  LessonAssets:       {total_assets_persisted}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic4()
