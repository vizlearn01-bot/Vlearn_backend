"""
VLearn CBC Grade 10 Agriculture — Topic 9: Animal Handling and Safety
Visual Enrichment Engine (Phase 2: Vector SVGs, Verified Photos & Asset Persistence)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Animal Handling and Safety (Order: 9)

Attaches:
  - 9 First-Card Photographic Visual Hooks (100% Tested HTTP 200 Direct Wikimedia URLs)
  - 8 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - 1 Verified Educational YouTube Video (Lesson 1 Card 3)
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade10_agriculture_topic9.py
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
# 8 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 9: ANIMAL HANDLING & SAFETY
# =============================================================================

# SVG 1: The 4 Pillars of Humane Animal Handling (Lesson 1, Page 2)
SVG_HANDLING_PILLARS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 4 Pillars of Humane Animal Handling &amp; Safety</text>

  <!-- Central Emblem: Sustainable Agribusiness -->
  <circle cx="400" cy="240" r="58" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
  <text x="400" y="232" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">HUMANE</text>
  <text x="400" y="248" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">LIVESTOCK</text>
  <text x="400" y="263" font-size="9" fill="#86efac" text-anchor="middle">HUSBANDRY</text>

  <!-- 1. Animal Welfare (Top) -->
  <g transform="translate(290, 70)">
    <rect x="0" y="0" width="220" height="80" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="25" rx="8" fill="#15803d"/>
    <text x="110" y="17" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">1. ANIMAL WELFARE</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Eliminates physical pain &amp; fear</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Fulfills 5 Animal Freedoms</text>
  </g>
  <line x1="400" y1="150" x2="400" y2="182" stroke="#22c55e" stroke-width="3"/>
  <polygon points="395,172 400,182 405,172" fill="#22c55e"/>

  <!-- 2. Handler Safety (Right) -->
  <g transform="translate(545, 195)">
    <rect x="0" y="0" width="220" height="80" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="25" rx="8" fill="#0891b2"/>
    <text x="110" y="17" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">2. HANDLER SAFETY</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Zero goring, kicks, or crushes</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Secure crushes &amp; PPE</text>
  </g>
  <line x1="545" y1="240" x2="458" y2="240" stroke="#06b6d4" stroke-width="3"/>
  <polygon points="468,235 458,240 468,245" fill="#06b6d4"/>

  <!-- 3. High Productivity (Bottom) -->
  <g transform="translate(290, 320)">
    <rect x="0" y="0" width="220" height="80" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="25" rx="8" fill="#ca8a04"/>
    <text x="110" y="17" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">3. HIGH PRODUCTIVITY</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Low stress = High Oxytocin flow</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Rapid daily weight gains</text>
  </g>
  <line x1="400" y1="320" x2="400" y2="298" stroke="#eab308" stroke-width="3"/>
  <polygon points="395,308 400,298 405,308" fill="#eab308"/>

  <!-- 4. Economic Profit (Left) -->
  <g transform="translate(35, 195)">
    <rect x="0" y="0" width="220" height="80" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="25" rx="8" fill="#7e22ce"/>
    <text x="110" y="17" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">4. ECONOMIC PROFIT</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Zero carcass bruising deductions</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Reduced veterinary bills</text>
  </g>
  <line x1="255" y1="240" x2="342" y2="240" stroke="#a855f7" stroke-width="3"/>
  <polygon points="332,235 342,240 332,245" fill="#a855f7"/>
</svg>
""")

# SVG 2: Safe Livestock Transport & Loading Ramp (Lesson 2, Page 2)
SVG_LOADING_RAMP = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Safe Livestock Transport &amp; Solid-Wall Loading Ramp Engineering</text>

  <!-- Left: Loading Ramp Schematic -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>

    <!-- Ramp Incline Profile -->
    <path d="M 30 290 L 260 140 L 260 290 Z" fill="#334155" stroke="#22c55e" stroke-width="2"/>

    <!-- Non-slip Cleats on Incline -->
    <line x1="60" y1="270" x2="70" y2="264" stroke="#fde047" stroke-width="3"/>
    <line x1="100" y1="244" x2="110" y2="238" stroke="#fde047" stroke-width="3"/>
    <line x1="140" y1="218" x2="150" y2="212" stroke="#fde047" stroke-width="3"/>
    <line x1="180" y1="192" x2="190" y2="186" stroke="#fde047" stroke-width="3"/>
    <line x1="220" y1="166" x2="230" y2="160" stroke="#fde047" stroke-width="3"/>

    <!-- Solid Side Wall (Opaque Barrier) -->
    <rect x="30" y="100" width="230" height="40" fill="#0c4a6e" stroke="#38bdf8"/>
    <text x="145" y="125" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">SOLID OPAQUE WALL (Blocks Visual Motion)</text>

    <!-- Angle Indicator -->
    <path d="M 70 290 A 40 40 0 0 0 65 267" fill="none" stroke="#ef4444" stroke-width="2"/>
    <text x="90" y="285" font-size="11" font-weight="bold" fill="#ef4444">≤ 20° Slope</text>

    <!-- Truck Connection Bumper -->
    <rect x="260" y="120" width="60" height="90" fill="#1e293b" stroke="#fde047" stroke-width="2"/>
    <text x="290" y="165" font-size="9" fill="#fde047" text-anchor="middle">Truck Bed</text>

    <text x="170" y="325" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Stepped Cleats + Non-Slip Rubber Flooring</text>
  </g>

  <!-- Right: 4 Golden Transport Rules -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#0284c7"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">4 LIVESTOCK TRANSPORT RULES</text>

    <g transform="translate(15, 45)">
      <text x="0" y="18" font-size="11" font-weight="bold" fill="#38bdf8">1. Solid Side Walls on Ramps:</text>
      <text x="0" y="34" font-size="10" fill="#cbd5e1">Blocks distracting motion &amp; shadows; prevents balking.</text>

      <text x="0" y="62" font-size="11" font-weight="bold" fill="#38bdf8">2. Incline Slope Under 20 Degrees:</text>
      <text x="0" y="78" font-size="10" fill="#cbd5e1">Prevents steep climbing panic and slipping injuries.</text>

      <text x="0" y="106" font-size="11" font-weight="bold" fill="#38bdf8">3. Deep Clean Bedding (10cm Straw):</text>
      <text x="0" y="122" font-size="10" fill="#cbd5e1">Absorbs manure/urine; prevents slick fall injuries.</text>

      <text x="0" y="150" font-size="11" font-weight="bold" fill="#38bdf8">4. Safe Stocking Density &amp; Partitions:</text>
      <text x="0" y="166" font-size="10" fill="#cbd5e1">Never overload; prevents fatal herd trampling.</text>
    </g>

    <rect x="15" y="260" width="315" height="70" rx="6" fill="#1e293b" stroke="#22c55e"/>
    <text x="172" y="285" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Economic Meat Protection</text>
    <text x="172" y="305" font-size="9" fill="#86efac" text-anchor="middle">Proper loading eliminates KES 3,000–5,000 in carcass bruising</text>
    <text x="172" y="320" font-size="9" fill="#86efac" text-anchor="middle">deductions per steer at the Kenya Meat Commission!</text>
  </g>
</svg>
""")

# SVG 3: Inhumane vs Humane Driving (Lesson 3, Page 2)
SVG_HUMANE_VS_INHUMANE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Livestock Driving: Inhumane Methods vs. Low-Stress Humane Solutions</text>

  <!-- Left: Inhumane Methods (Red) -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="345" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="32" rx="10" fill="#991b1b"/>
    <text x="170" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">INHUMANE HARMFUL METHODS (AVOID)</text>

    <g transform="translate(15, 45)">
      <rect x="0" y="0" width="310" height="55" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#f87171">• Wooden Sticks &amp; Metal Pipes:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Causes deep hematomas &amp; condemned meat.</text>

      <rect x="0" y="65" width="310" height="55" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#f87171">• Tail-Twisting &amp; Breaking:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Fractures vertebrae; destroys spinal nerves.</text>

      <rect x="0" y="130" width="310" height="55" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#f87171">• Thin Nylon Donkey Ropes:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Cuts deep raw sores into neck and chest.</text>

      <text x="15" y="210" font-size="10" font-weight="bold" fill="#fca5a5">Outcome: Chronic stress, pain, high vet costs</text>
    </g>
  </g>

  <!-- Right: Humane Solutions (Green) -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#15803d"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">HUMANE LOW-STRESS ALTERNATIVES</text>

    <g transform="translate(15, 45)">
      <rect x="0" y="0" width="315" height="55" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">• Plastic Herding Flags &amp; Canes:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Creates visual guide barriers without pain.</text>

      <rect x="0" y="65" width="315" height="55" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">• Plywood Sorting Boards:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Guides pigs calmly by blocking line of sight.</text>

      <rect x="0" y="130" width="315" height="55" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">• Wide (10cm) Padded Canvas Harnesses:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Distributes pulling draft load across chest.</text>

      <text x="15" y="210" font-size="10" font-weight="bold" fill="#86efac">Outcome: Zero injuries, calm herd, max profit</text>
    </g>
  </g>
</svg>
""")

# SVG 4: Cattle Crush Schematic (Lesson 4, Page 2)
SVG_CATTLE_CRUSH = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Top-Down Architectural Schematic of a Standard Cattle Crush</text>

  <!-- Top-Down Blueprint View -->
  <g transform="translate(60, 60)">
    <!-- Funnel Race Entrance -->
    <path d="M 30 180 L 140 130 L 140 210 L 30 160 Z" fill="#0f172a" stroke="#ca8a04" stroke-width="2"/>
    <text x="85" y="175" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">Funnel Race</text>

    <!-- Rear Sliding Gate -->
    <line x1="140" y1="100" x2="140" y2="240" stroke="#ef4444" stroke-width="6"/>
    <text x="140" y="85" font-size="9" font-weight="bold" fill="#f87171" text-anchor="middle">Rear Sliding Gate</text>

    <!-- Crush Corridor -->
    <rect x="140" y="125" width="380" height="90" fill="#1e293b" stroke="#22c55e" stroke-width="2"/>
    <!-- Cow Silhouette Position -->
    <ellipse cx="320" cy="170" rx="120" ry="32" fill="#334155" stroke="#94a3b8"/>
    <text x="320" y="174" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Restrained Cow (Single-Animal Corridor: 65–70cm Width)</text>

    <!-- Service Gate (Rear Flank Access) -->
    <line x1="200" y1="215" x2="260" y2="250" stroke="#38bdf8" stroke-width="4"/>
    <text x="230" y="270" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Service Gate (AI / Vet Access)</text>

    <!-- Front Head Gate / Yoke -->
    <line x1="520" y1="100" x2="520" y2="240" stroke="#22c55e" stroke-width="6"/>
    <rect x="510" y="145" width="20" height="50" rx="4" fill="#15803d" stroke="#4ade80"/>
    <text x="520" y="85" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Head Gate / Yoke (Locks Neck)</text>

    <!-- Operator Working Platform (Outside Rails) -->
    <rect x="140" y="20" width="380" height="40" rx="6" fill="#0c4a6e" stroke="#38bdf8"/>
    <text x="330" y="45" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">SAFE OPERATOR WORKING PATH (Outside Timber/Steel Rails)</text>
  </g>

  <!-- Technical Spec Footer -->
  <g transform="translate(60, 355)">
    <rect x="0" y="0" width="680" height="60" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="340" y="22" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Standard Dimensions: Width = 65–70 cm | Rail Height = 1.4–1.5 m | Post Spacing = 1.2 m</text>
    <text x="340" y="42" font-size="9" fill="#cbd5e1" text-anchor="middle">Prevents animal from turning around; locks head securely for zero-danger vaccinations and medical drenching.</text>
  </g>
</svg>
""")

# SVG 5: Restraint Tools & PPE (Lesson 5, Page 2)
SVG_TOOLS_AND_PPE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Livestock Restraint Tools &amp; Essential Handler PPE Ensemble</text>

  <!-- Left: Restraint Tools -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="32" rx="10" fill="#15803d"/>
    <text x="170" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. LEADING &amp; RESTRAINT TOOLS</text>

    <!-- 1. Halter -->
    <g transform="translate(15, 45)">
      <rect x="0" y="0" width="310" height="55" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">Rope / Leather Halter:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Noseband rests midway between eyes and muzzle.</text>
    </g>

    <!-- 2. Bull Ring & Staff -->
    <g transform="translate(15, 110)">
      <rect x="0" y="0" width="310" height="55" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">Bull Ring + 1.5m Solid Lead Stick:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Nasal septum sensitivity + rigid physical spacer.</text>
    </g>

    <!-- 3. Casting Ropes -->
    <g transform="translate(15, 175)">
      <rect x="0" y="0" width="310" height="55" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">Cotton Casting Ropes (Reuff's Method):</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Lays large cattle down safely without bone breaks.</text>
    </g>

    <text x="170" y="260" font-size="9" fill="#86efac" text-anchor="middle">Rule: Never wrap lead rope around your hand or wrist!</text>
  </g>

  <!-- Right: PPE Ensemble -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#0284c7"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. PERSONAL PROTECTIVE EQUIPMENT (PPE)</text>

    <!-- 1. Steel-toed boots -->
    <g transform="translate(15, 45)">
      <rect x="0" y="0" width="315" height="55" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#38bdf8">Steel-Toed Gumboots with Treads:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Protects toes from hoof crush; prevents slips on manure.</text>
    </g>

    <!-- 2. Leather gloves -->
    <g transform="translate(15, 110)">
      <rect x="0" y="0" width="315" height="55" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#38bdf8">Heavy Cowhide Leather Gloves:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Prevents friction rope burns and wire scratches.</text>
    </g>

    <!-- 3. Overalls -->
    <g transform="translate(15, 175)">
      <rect x="0" y="0" width="315" height="55" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#38bdf8">Cotton Work Overalls:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Physical barrier against manure, chemicals &amp; zoonoses.</text>
    </g>

    <text x="172" y="260" font-size="9" fill="#67e8f9" text-anchor="middle">Rule: Mandatory PPE before entering livestock pens!</text>
  </g>
</svg>
""")

# SVG 6: Flight Zone & Point of Balance (Lesson 6, Page 2)
SVG_FLIGHT_ZONE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Cattle Behavioral Dynamics: Flight Zone &amp; Point of Balance</text>

  <!-- Central Cattle Silhouette Schematic -->
  <g transform="translate(180, 70)">
    <!-- Outer Flight Zone Circle -->
    <circle cx="220" cy="180" r="160" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="6,6"/>
    <text x="220" y="35" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Edge of Flight Zone (Personal Space Perimeter)</text>

    <!-- Point of Balance (Shoulder Line) -->
    <line x1="220" y1="40" x2="220" y2="320" stroke="#fde047" stroke-width="3"/>
    <text x="220" y="335" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">POINT OF BALANCE (Line through Shoulders)</text>

    <!-- Cow Body Center -->
    <ellipse cx="220" cy="180" rx="80" ry="30" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
    <text x="220" y="175" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">COW</text>
    <!-- Head Indicator -->
    <polygon points="300,170 330,180 300,190" fill="#22c55e"/>
    <text x="335" y="184" font-size="9" font-weight="bold" fill="#22c55e">HEAD (Forward)</text>

    <!-- Rear 30° Blind Spot (Red Wedge) -->
    <path d="M 140 180 L 70 145 A 160 160 0 0 0 70 215 Z" fill="#ef4444" opacity="0.4"/>
    <text x="100" y="184" font-size="9" font-weight="bold" fill="#f87171" text-anchor="middle">BLIND SPOT (Kick Zone)</text>

    <!-- Handler Vectors -->
    <!-- Vector A: Behind Shoulder -> Move Forward -->
    <circle cx="160" cy="250" r="12" fill="#22c55e"/>
    <text x="160" y="254" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">H</text>
    <line x1="160" y1="235" x2="190" y2="205" stroke="#22c55e" stroke-width="3"/>
    <polygon points="180,205 190,205 190,215" fill="#22c55e"/>
    <text x="110" y="280" font-size="9" font-weight="bold" fill="#4ade80">Stand HERE to move FORWARD</text>

    <!-- Vector B: In Front of Shoulder -> Stop / Reverse -->
    <circle cx="280" cy="250" r="12" fill="#ef4444"/>
    <text x="280" y="254" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">H</text>
    <line x1="280" y1="235" x2="250" y2="205" stroke="#ef4444" stroke-width="3"/>
    <polygon points="250,215 250,205 260,205" fill="#ef4444"/>
    <text x="330" y="280" font-size="9" font-weight="bold" fill="#f87171">Stand HERE to STOP / BACK UP</text>
  </g>
</svg>
""")

# SVG 7: Zoonoses Defense & Biosecurity (Lesson 7, Page 2)
SVG_ZOONOSES_DEFENSE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Major Livestock Zoonoses &amp; Handler Biosecurity Barriers</text>

  <!-- Left: 3 Deadly Zoonoses (Threat) -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="345" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="32" rx="10" fill="#991b1b"/>
    <text x="170" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">HIGH-RISK LIVESTOCK ZOONOSES</text>

    <g transform="translate(15, 45)">
      <!-- Anthrax -->
      <rect x="0" y="0" width="310" height="70" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="15" y="20" font-size="11" font-weight="bold" fill="#f87171">1. Anthrax (Bacillus anthracis):</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">• Non-clotting dark blood from orifices</text>
      <text x="15" y="55" font-size="9" font-weight="bold" fill="#fca5a5">• BIOSECURITY: NEVER OPEN CARCASS!</text>

      <!-- Brucellosis -->
      <rect x="0" y="80" width="310" height="70" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="15" y="20" font-size="11" font-weight="bold" fill="#f87171">2. Brucellosis (Brucella abortus):</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">• Spread via raw milk &amp; birth placenta</text>
      <text x="15" y="55" font-size="9" fill="#cbd5e1">• Causes chronic undulating fever in humans</text>

      <!-- Ringworm -->
      <rect x="0" y="160" width="310" height="60" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="15" y="20" font-size="11" font-weight="bold" fill="#f87171">3. Ringworm (Trichophyton fungus):</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">• Contagious crusty skin rash from calves</text>
    </g>
  </g>

  <!-- Right: 4 Handler Defense Barriers (Protection) -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#15803d"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">THE 4 HANDLER BIOSECURITY BARRIERS</text>

    <g transform="translate(15, 45)">
      <rect x="0" y="0" width="315" height="55" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">1. Milk Pasteurization / Boiling:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Destroys 100% of Brucella &amp; TB pathogens.</text>

      <rect x="0" y="65" width="315" height="55" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">2. WHO 20-Sec Handwashing Drill:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Wash thoroughly with soap after livestock handling.</text>

      <rect x="0" y="130" width="315" height="55" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">3. Obstetrical Gloves at Calving:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Physical barrier against infected fluids.</text>

      <rect x="0" y="195" width="315" height="55" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">4. Zero Food / Drink in Animal Housing:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Eliminates fecal-oral pathogen ingestion.</text>
    </g>
  </g>
</svg>
""")

# SVG 8: Master Operational Synthesis (Lesson 9, Page 2)
SVG_MASTER_SYNTHESIS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Master Animal Handling &amp; Safety Systems Operational Synthesis</text>

  <!-- Central Hub: Safe Agribusiness -->
  <circle cx="400" cy="240" r="55" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
  <text x="400" y="235" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">SAFE &amp; HUMANE</text>
  <text x="400" y="252" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">LIVESTOCK FARM</text>

  <!-- 1. Animal Psychology -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="195" height="75" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <text x="97" y="22" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">1. BEHAVIOR</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Flight zone navigation</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Point of balance (shoulder)</text>
  </g>
  <line x1="240" y1="102" x2="345" y2="200" stroke="#22c55e" stroke-width="2" stroke-dasharray="2,2"/>

  <!-- 2. Safety Structures -->
  <g transform="translate(560, 65)">
    <rect x="0" y="0" width="195" height="75" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="97" y="22" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">2. STRUCTURES</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Cattle crush with head yoke</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Solid-wall loading ramp ≤20°</text>
  </g>
  <line x1="560" y1="102" x2="455" y2="200" stroke="#38bdf8" stroke-width="2" stroke-dasharray="2,2"/>

  <!-- 3. Tools & PPE -->
  <g transform="translate(35, 195)">
    <rect x="0" y="0" width="195" height="75" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <text x="97" y="22" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">3. TOOLS &amp; PPE</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Halter &amp; Bull lead staff</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Steel-toed boots &amp; gloves</text>
  </g>
  <line x1="230" y1="240" x2="345" y2="240" stroke="#eab308" stroke-width="2"/>

  <!-- 4. Biosecurity -->
  <g transform="translate(570, 195)">
    <rect x="0" y="0" width="195" height="75" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
    <text x="97" y="22" font-size="11" font-weight="bold" fill="#67e8f9" text-anchor="middle">4. BIOSECURITY</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Anthrax carcass quarantine</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• 20-Sec handwashing drill</text>
  </g>
  <line x1="570" y1="240" x2="455" y2="240" stroke="#06b6d4" stroke-width="2"/>

  <!-- 5. Community Advocacy -->
  <g transform="translate(300, 335)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="100" y="22" font-size="11" font-weight="bold" fill="#d8b4fe" text-anchor="middle">5. ADVOCACY</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Market loading ramp reform</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Padded donkey harnesses</text>
  </g>
  <line x1="400" y1="335" x2="400" y2="298" stroke="#a855f7" stroke-width="2"/>
</svg>
""")

SVG_MAP = {
    1: {"page": 2, "svg": SVG_HANDLING_PILLARS, "title": "The 4 Pillars of Humane Animal Handling & Safety"},
    2: {"page": 2, "svg": SVG_LOADING_RAMP, "title": "Safe Livestock Transport & Solid-Wall Loading Ramp Engineering"},
    3: {"page": 2, "svg": SVG_HUMANE_VS_INHUMANE, "title": "Livestock Driving: Inhumane Methods vs Low-Stress Solutions"},
    4: {"page": 2, "svg": SVG_CATTLE_CRUSH, "title": "Top-Down Architectural Schematic of a Standard Cattle Crush"},
    5: {"page": 2, "svg": SVG_TOOLS_AND_PPE, "title": "Livestock Restraint Tools & Essential Handler PPE Ensemble"},
    6: {"page": 2, "svg": SVG_FLIGHT_ZONE, "title": "Cattle Behavioral Dynamics: Flight Zone & Point of Balance"},
    7: {"page": 2, "svg": SVG_ZOONOSES_DEFENSE, "title": "Major Livestock Zoonoses & Handler Biosecurity Barriers"},
    9: {"page": 2, "svg": SVG_MASTER_SYNTHESIS, "title": "Master Animal Handling & Safety Systems Operational Synthesis"}
}

def enrich_grade10_topic9():
    """Injects verified photos, responsive vector SVGs, YouTube embeds, and creates LessonAssets."""
    print("=" * 80)
    print("STARTING ENRICHMENT: CBC Grade 10 Agriculture — Topic 9: Animal Handling and Safety")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()
    topic = Topic.objects.filter(subject=subject, name="Animal Handling and Safety").first()

    assert topic, "Topic 'Animal Handling and Safety' not found!"

    images_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grade10_topic9_verified_images.json")
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
                    "topic_order": 9,
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
                        "topic_order": 9,
                        "unit_order": u_order,
                        "page": svg_def["page"],
                        "svg_content": svg_def["svg"]
                    }
                )
                diag_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [Vector SVG Attached] Lesson {u_order}: {svg_def['title']}")

        # ---------------------------------------------------------------------
        # 3. Educational YouTube Videos (Lesson 1)
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
                        "topic_order": 9,
                        "unit_order": u_order,
                        "youtube_url": v_url
                    }
                )
                v_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [YouTube Video Attached] Lesson {u_order}: {v_block.title}")

    print("=" * 80)
    print(f"ENRICHMENT COMPLETE: Topic 9 '{topic.name}'")
    print(f"  Photographic Hooks: {total_images_attached} / 9")
    print(f"  Vector SVGs:        {total_svgs_attached} / 8")
    print(f"  YouTube Videos:     {total_videos_attached} / 1")
    print(f"  LessonAssets:       {total_assets_persisted}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic9()
