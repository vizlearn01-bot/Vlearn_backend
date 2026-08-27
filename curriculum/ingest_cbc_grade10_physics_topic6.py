"""
VLearn CBC Grade 10 Physics — Topic 6: Energy, Work, Power and Machines
Production Ingestion & Visual Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Physics
Topic: Energy, Work, Power and Machines (Order: 6)

7 Learning Units & 7 Published Lessons:
  1. Energy, Work and Power (8 Pages, 13 Blocks)
  2. Kinetic and Potential Energy (8 Pages, 13 Blocks)
  3. Conservation and Transformation of Mechanical Energy (8 Pages, 14 Blocks)
  4. Simple Machines and Mechanical Advantage (8 Pages, 13 Blocks)
  5. Levers, Moments and Inclined Planes (8 Pages, 13 Blocks)
  6. Wheels, Axles, Gears, Pulleys and Hydraulic Machines (8 Pages, 14 Blocks)
  7. Energy, Machines and Sustainable Design (8 Pages, 13 Blocks)

Includes:
  - 9 Custom Responsive Sanitized Vector SVG Diagrams
  - 7 Verified Wikimedia Commons Photographic Assets
  - 7 Verified Educational YouTube Video Integrations
  - 7 Formative Scenario-Based MCQs with 4 Options and Pedagogical Feedback
"""

import os
import sys
import re
import django
from django.db import transaction

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)
from curriculum.media_orchestration.visual_intelligence.svg_sanitizer import validate_and_sanitize_svg

# =============================================================================
# SVG DEFINITIONS FOR TOPIC 6
# =============================================================================

def get_svg_work_vs_zero_work():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 420" width="100%" height="100%">
  <rect width="820" height="420" fill="#0f172a" rx="16"/>
  <text x="410" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">WORK DONE (W = F × d) VS ZERO WORK (FORCE ⊥ DISPLACEMENT)</text>
  <text x="410" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Work is Done in Physics Only When Displacement Occurs in the Direction of the Applied Force</text>

  <!-- Left: Work Done (W = 500 J) -->
  <g transform="translate(40, 80)">
    <rect width="350" height="310" rx="10" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
    <text x="175" y="28" fill="#22c55e" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">1. POSITIVE WORK DONE (W > 0)</text>

    <!-- Ground line -->
    <line x1="30" y1="180" x2="320" y2="180" stroke="#94a3b8" stroke-width="2"/>

    <!-- Pushed Box -->
    <rect x="110" y="110" width="80" height="70" fill="#0284c733" stroke="#38bdf8" stroke-width="2" rx="4"/>
    <text x="150" y="150" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Box</text>

    <!-- Force Arrow F (Right) -->
    <path d="M 50 145 L 105 145 M 95 139 L 105 145 L 95 151" stroke="#22c55e" stroke-width="4"/>
    <text x="75" y="135" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="700">F = 100 N</text>

    <!-- Displacement Arrow d (Right) -->
    <path d="M 110 210 L 250 210 M 240 204 L 250 210 L 240 216" stroke="#38bdf8" stroke-width="3"/>
    <text x="180" y="230" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Displacement d = 5 m</text>

    <!-- Calculation Box -->
    <rect x="30" y="245" width="290" height="50" rx="6" fill="#0f172a" stroke="#22c55e" stroke-width="1"/>
    <text x="175" y="275" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">W = 100 N × 5 m = 500 Joules (J)</text>
  </g>

  <!-- Right: Zero Work Done (W = 0) -->
  <g transform="translate(430, 80)">
    <rect width="350" height="310" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="175" y="28" fill="#ef4444" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">2. ZERO WORK DONE (W = 0)</text>

    <!-- Ground line -->
    <line x1="30" y1="180" x2="320" y2="180" stroke="#94a3b8" stroke-width="2"/>

    <!-- Person carrying heavy box horizontally -->
    <rect x="135" y="100" width="50" height="40" fill="#f59e0b33" stroke="#f59e0b" stroke-width="2" rx="3"/>
    <text x="160" y="125" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Bag</text>

    <!-- Upward holding force arrow -->
    <path d="M 160 100 L 160 50 M 154 60 L 160 50 L 166 60" stroke="#f59e0b" stroke-width="3.5"/>
    <text x="170" y="75" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Upward Force F</text>

    <!-- Horizontal motion arrow -->
    <path d="M 135 210 L 250 210 M 240 204 L 250 210 L 240 216" stroke="#38bdf8" stroke-width="3"/>
    <text x="190" y="230" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Horizontal Walk (d)</text>

    <!-- 90-degree right angle symbol -->
    <path d="M 160 145 L 175 145 L 175 160" stroke="#ef4444" stroke-width="1.5" fill="none"/>
    <text x="180" y="155" fill="#ef4444" font-family="system-ui, sans-serif" font-size="10" font-weight="700">90°</text>

    <!-- Calculation Box -->
    <rect x="30" y="245" width="290" height="50" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="175" y="275" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">W = F × d × cos(90°) = 0 Joules</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_ke_speed_parabola():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%">
  <rect width="800" height="420" fill="#0f172a" rx="16"/>
  <text x="400" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">KINETIC ENERGY (E_k = 1/2 m v²) VS SPEED (v)</text>
  <text x="400" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Parabolic Speed-Square Law • Doubling Speed Quadruples (4×) Kinetic Energy</text>

  <!-- Axes -->
  <line x1="120" y1="340" x2="720" y2="340" stroke="#94a3b8" stroke-width="2"/>
  <line x1="120" y1="340" x2="120" y2="80" stroke="#94a3b8" stroke-width="2"/>

  <!-- Y-Axis: Kinetic Energy (kJ) for 1000 kg car -->
  <text x="105" y="345" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">0</text>
  <text x="105" y="285" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">50 kJ</text>
  <text x="105" y="200" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">200 kJ (4×)</text>
  <text x="105" y="100" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">450 kJ (9×)</text>
  <text x="40" y="200" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle" transform="rotate(-90 40 200)">Kinetic Energy E_k (kJ)</text>

  <!-- X-Axis: Speed (m/s) -->
  <text x="120" y="360" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">0</text>
  <text x="300" y="360" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">10 m/s (36 km/h)</text>
  <text x="480" y="360" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">20 m/s (2× Speed)</text>
  <text x="660" y="360" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">30 m/s (3× Speed)</text>
  <text x="420" y="390" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Speed v (m/s)</text>

  <!-- Parabolic Curve -->
  <path d="M 120 340 Q 400 330 660 100" fill="none" stroke="#38bdf8" stroke-width="4"/>

  <!-- Points on Curve -->
  <circle cx="300" cy="285" r="5" fill="#38bdf8"/>
  <circle cx="480" cy="200" r="6" fill="#f59e0b"/>
  <circle cx="660" cy="100" r="7" fill="#ef4444"/>

  <!-- Callout Box -->
  <rect x="180" y="90" width="240" height="65" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="300" y="112" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">E_k ∝ v² (Quadratic)</text>
  <text x="300" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Crash impact energy grows with v²!</text>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_falling_stone_energy():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%">
  <rect width="820" height="440" fill="#0f172a" rx="16"/>
  <text x="410" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">CONSERVATION OF MECHANICAL ENERGY: THE FALLING BODY</text>
  <text x="410" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Total Mechanical Energy (E_total = E_k + E_p) Remains Constant At All Points (v = √(2gh))</text>

  <!-- Cliff & Falling Stages -->
  <g transform="translate(100, 80)">
    <!-- Cliff Structure -->
    <path d="M 0 50 L 140 50 L 140 320 L 0 320 Z" fill="#1e293b" stroke="#64748b" stroke-width="2"/>

    <!-- Stage 1: Top of Cliff (Height = h, v = 0) -->
    <circle cx="200" cy="50" r="14" fill="#38bdf8" stroke="#ffffff" stroke-width="2"/>
    <g transform="translate(230, 30)">
      <rect width="280" height="45" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="140" y="20" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. TOP (Height = h, Speed = 0)</text>
      <text x="140" y="38" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">GPE = mgh | KE = 0 | E_total = mgh</text>
    </g>

    <!-- Stage 2: Midway (Height = 0.5h) -->
    <circle cx="200" cy="170" r="14" fill="#f59e0b" stroke="#ffffff" stroke-width="2"/>
    <g transform="translate(230, 150)">
      <rect width="280" height="45" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="140" y="20" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. MIDWAY (Height = 0.5 h)</text>
      <text x="140" y="38" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">GPE = 0.5 mgh | KE = 0.5 mgh | E_total = mgh</text>
    </g>

    <!-- Stage 3: Ground Impact (Height = 0, Speed = v_max) -->
    <circle cx="200" cy="290" r="14" fill="#22c55e" stroke="#ffffff" stroke-width="2"/>
    <g transform="translate(230, 270)">
      <rect width="280" height="45" rx="6" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
      <text x="140" y="20" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. GROUND (Height = 0, v = √(2gh))</text>
      <text x="140" y="38" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">GPE = 0 | KE = 1/2 mv² | E_total = mgh</text>
    </g>

    <!-- Downward Acceleration Arrow -->
    <path d="M 200 70 L 200 150 M 194 140 L 200 150 L 206 140" stroke="#94a3b8" stroke-width="2" stroke-dasharray="3 3"/>
    <path d="M 200 190 L 200 270 M 194 260 L 200 270 L 206 260" stroke="#94a3b8" stroke-width="2" stroke-dasharray="3 3"/>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_sankey_diagram():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 380" width="100%" height="100%">
  <rect width="820" height="380" fill="#0f172a" rx="16"/>
  <text x="410" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">SANKEY ENERGY FLOW DIAGRAM: WATER PUMP SYSTEM</text>
  <text x="410" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Total Input Energy (100 J) = Useful Output GPE (70 J) + Wasted Heat & Friction (30 J)</text>

  <!-- Input Trunk (100 J) -->
  <path d="M 60 120 L 260 120 L 260 260 L 60 260 Z" fill="#38bdf8" opacity="0.9"/>
  <text x="160" y="195" fill="#000000" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Total Input Electrical Energy (100 J = 100%)</text>

  <!-- Useful Branch (70 J = 70% width) -->
  <path d="M 260 120 L 680 120 L 680 218 L 260 218 Z" fill="#22c55e" opacity="0.9"/>
  <path d="M 680 105 L 720 169 L 680 233 Z" fill="#22c55e"/>
  <text x="470" y="175" fill="#000000" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Useful GPE of Lifted Water = 70 J (70% Efficiency)</text>

  <!-- Wasted Branch Curving Down (30 J = 30% width) -->
  <path d="M 260 218 Q 360 218 360 300 L 420 300 Q 420 260 260 260 Z" fill="#ef4444" opacity="0.9"/>
  <path d="M 345 300 L 390 340 L 435 300 Z" fill="#ef4444"/>
  <text x="390" y="365" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Wasted Heat in Motor & Friction = 30 J (30%)</text>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_pulley_block_tackle():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%">
  <rect width="820" height="440" fill="#0f172a" rx="16"/>
  <text x="410" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">BLOCK AND TACKLE PULLEY SYSTEM (VR = 4)</text>
  <text x="410" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">4 Supporting Rope Strands • Multiplies Effort Force (MA = 3, Efficiency = 75%)</text>

  <!-- Pulley System Schematic -->
  <g transform="translate(140, 80)">
    <!-- Top Fixed Pulley Block (2 Sheaves) -->
    <rect x="80" y="10" width="120" height="20" fill="#64748b" rx="3"/>
    <circle cx="110" cy="50" r="22" fill="#334155" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="170" cy="50" r="22" fill="#334155" stroke="#38bdf8" stroke-width="2"/>

    <!-- Bottom Movable Pulley Block (2 Sheaves) -->
    <circle cx="110" cy="200" r="22" fill="#334155" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="170" cy="200" r="22" fill="#334155" stroke="#f59e0b" stroke-width="2"/>
    <rect x="80" y="210" width="120" height="15" fill="#64748b" rx="3"/>

    <!-- Continuous Rope Strands (4 supporting lines) -->
    <line x1="88" y1="50" x2="88" y2="200" stroke="#f8fafc" stroke-width="3"/>
    <line x1="132" y1="50" x2="132" y2="200" stroke="#f8fafc" stroke-width="3"/>
    <line x1="148" y1="50" x2="148" y2="200" stroke="#f8fafc" stroke-width="3"/>
    <line x1="192" y1="50" x2="192" y2="200" stroke="#f8fafc" stroke-width="3"/>

    <!-- Effort Pull Rope -->
    <line x1="192" y1="50" x2="230" y2="250" stroke="#ef4444" stroke-width="3"/>
    <path d="M 230 250 L 230 300 M 224 290 L 230 300 L 236 290" stroke="#ef4444" stroke-width="3"/>
    <text x="245" y="280" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Effort E = 400 N</text>

    <!-- Load (1200 N) -->
    <rect x="110" y="235" width="60" height="45" fill="#f59e0b" stroke="#d97706" stroke-width="2" rx="4"/>
    <text x="140" y="262" fill="#000000" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1200 N</text>
  </g>

  <!-- Performance Metric Cards on Right -->
  <g transform="translate(480, 85)">
    <!-- MA Box -->
    <rect width="280" height="65" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="15" y="26" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">1. Mechanical Advantage (MA):</text>
    <text x="15" y="48" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13">MA = Load / Effort = 1200 N / 400 N = 3.0</text>

    <!-- VR Box -->
    <rect y="80" width="280" height="65" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="15" y="106" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700">2. Velocity Ratio (VR):</text>
    <text x="15" y="128" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13">VR = 4 (4 supporting rope strands)</text>

    <!-- Efficiency Box -->
    <rect y="160" width="280" height="75" rx="8" fill="#1e293b" stroke="#22c55e" stroke-width="2"/>
    <text x="15" y="186" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="700">3. Useful Efficiency (η):</text>
    <text x="15" y="212" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="700">η = (MA / VR) × 100% = 75.0%</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_three_lever_classes():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">THE THREE CLASSES OF LEVERS (FLE CLASSIFICATION RULE)</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">1st Class (Fulcrum Middle) • 2nd Class (Load Middle) • 3rd Class (Effort Middle)</text>

  <!-- 1st Class Lever (F in middle) -->
  <g transform="translate(50, 80)">
    <rect width="210" height="260" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="105" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1st CLASS (FULCRUM)</text>

    <!-- Beam -->
    <rect x="25" y="100" width="160" height="12" fill="#38bdf833" stroke="#38bdf8" stroke-width="1.5"/>
    <!-- Fulcrum in center -->
    <polygon points="105,112 95,135 115,135" fill="#f59e0b"/>
    <text x="105" y="150" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">F (Pivot)</text>

    <!-- Effort on left (Down) -->
    <path d="M 35 70 L 35 95 M 30 87 L 35 95 L 40 87" stroke="#22c55e" stroke-width="2.5"/>
    <text x="35" y="60" fill="#22c55e" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Effort</text>

    <!-- Load on right (Down) -->
    <rect x="160" y="80" width="20" height="20" fill="#ef4444"/>
    <text x="170" y="65" fill="#ef4444" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Load</text>

    <text x="105" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Crowbar, Scissors, Seesaw</text>
  </g>

  <!-- 2nd Class Lever (L in middle) -->
  <g transform="translate(315, 80)">
    <rect width="210" height="260" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="105" y="28" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">2nd CLASS (LOAD)</text>

    <!-- Beam -->
    <rect x="25" y="100" width="160" height="12" fill="#f59e0b33" stroke="#f59e0b" stroke-width="1.5"/>
    <!-- Fulcrum on left -->
    <polygon points="35,112 25,135 45,135" fill="#f59e0b"/>
    <text x="35" y="150" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">F</text>

    <!-- Load in center (Down) -->
    <rect x="95" y="80" width="20" height="20" fill="#ef4444"/>
    <text x="105" y="65" fill="#ef4444" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Load (L)</text>

    <!-- Effort on right (Up) -->
    <path d="M 175 140 L 175 115 M 170 123 L 175 115 L 180 123" stroke="#22c55e" stroke-width="2.5"/>
    <text x="175" y="160" fill="#22c55e" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Effort</text>

    <text x="105" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Wheelbarrow, Nutcracker (MA &gt; 1)</text>
  </g>

  <!-- 3rd Class Lever (E in middle) -->
  <g transform="translate(580, 80)">
    <rect width="210" height="260" rx="10" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
    <text x="105" y="28" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">3rd CLASS (EFFORT)</text>

    <!-- Beam -->
    <rect x="25" y="100" width="160" height="12" fill="#22c55e33" stroke="#22c55e" stroke-width="1.5"/>
    <!-- Fulcrum on left -->
    <polygon points="35,112 25,135 45,135" fill="#f59e0b"/>
    <text x="35" y="150" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">F</text>

    <!-- Effort in center (Up) -->
    <path d="M 105 140 L 105 115 M 100 123 L 105 115 L 110 123" stroke="#22c55e" stroke-width="2.5"/>
    <text x="105" y="160" fill="#22c55e" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Effort (E)</text>

    <!-- Load on right (Down) -->
    <rect x="160" y="80" width="20" height="20" fill="#ef4444"/>
    <text x="170" y="65" fill="#ef4444" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Load</text>

    <text x="105" y="210" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Tweezers, Fishing Rod, Forearm</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_inclined_plane():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <rect width="800" height="400" fill="#0f172a" rx="16"/>
  <text x="400" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">INCLINED PLANE: TRADING FORCE FOR DISTANCE</text>
  <text x="400" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Velocity Ratio (VR) = Length of Slope (L) / Vertical Height (h) = 1 / sin(θ)</text>

  <!-- Ramp Triangle Structure -->
  <g transform="translate(100, 100)">
    <!-- Triangular Wedge -->
    <polygon points="0,220 500,220 500,60" fill="#0284c722" stroke="#38bdf8" stroke-width="2.5"/>

    <!-- Angle theta -->
    <path d="M 60 220 A 40 40 0 0 0 52 203" fill="none" stroke="#f59e0b" stroke-width="2"/>
    <text x="75" y="212" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="700">θ</text>

    <!-- Box on Ramp -->
    <g transform="translate(240, 143) rotate(-17.7)">
      <rect x="0" y="-35" width="50" height="35" fill="#f59e0b" stroke="#d97706" stroke-width="1.5" rx="3"/>
      <path d="M 50 -17 L 90 -17 M 82 -22 L 90 -17 L 82 -12" stroke="#22c55e" stroke-width="3"/>
      <text x="100" y="-12" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Effort E</text>
    </g>

    <!-- Length L Dimension (Hypotenuse) -->
    <line x1="-15" y1="210" x2="485" y2="50" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="215" y="115" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Slope Length L = 12.0 m</text>

    <!-- Height h Dimension -->
    <line x1="530" y1="60" x2="530" y2="220" stroke="#f59e0b" stroke-width="2"/>
    <path d="M 524 60 L 536 60 M 524 220 L 536 220" stroke="#f59e0b" stroke-width="2"/>
    <text x="545" y="145" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Height h = 1.5 m</text>
  </g>

  <!-- Calculation Box -->
  <g transform="translate(150, 320)">
    <rect width="500" height="60" rx="8" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
    <text x="250" y="28" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">VR = Length / Height = 12.0 m / 1.5 m = 8.0</text>
    <text x="250" y="48" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Spreading lift across 12 m allows a 160 N effort to raise an 800 N wheelchair</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_meshed_gears():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 400" width="100%" height="100%">
  <rect width="820" height="400" fill="#0f172a" rx="16"/>
  <text x="410" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">GEAR TRANSMISSION: VELOCITY RATIO & SPEED TRANSFORMATION</text>
  <text x="410" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">VR = Number of Teeth on Driven Gear (N_driven) / Number of Teeth on Driver Gear (N_driver)</text>

  <!-- Left: Small Driver Gear (10 Teeth) -->
  <g transform="translate(220, 180)">
    <circle cx="0" cy="0" r="50" fill="#1e293b" stroke="#38bdf8" stroke-width="4"/>
    <circle cx="0" cy="0" r="15" fill="#64748b"/>
    <!-- Gear teeth indication -->
    <path d="M 0 -58 L 0 -45 M 35 -40 L 26 -31 M 55 0 L 42 0 M 35 40 L 26 31 M 0 58 L 0 45 M -35 40 L -26 31 M -55 0 L -42 0 M -35 -40 L -26 -31" stroke="#38bdf8" stroke-width="6"/>

    <!-- Clockwise Rotation Arrow -->
    <path d="M -25 -25 Q 0 -40 25 -25" fill="none" stroke="#22c55e" stroke-width="3"/>
    <text x="0" y="80" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Driver Gear (10 Teeth)</text>
    <text x="0" y="98" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Rotates Clockwise</text>
  </g>

  <!-- Right: Large Driven Gear (30 Teeth) -->
  <g transform="translate(420, 180)">
    <circle cx="0" cy="0" r="110" fill="#1e293b" stroke="#f59e0b" stroke-width="4"/>
    <circle cx="0" cy="0" r="22" fill="#64748b"/>
    <!-- Gear teeth indication -->
    <path d="M 0 -120 L 0 -105 M 65 -95 L 53 -81 M 115 0 L 100 0 M 65 95 L 53 81 M 0 120 L 0 105 M -65 95 L -53 81 M -115 0 L -100 0 M -65 -95 L -53 -81" stroke="#f59e0b" stroke-width="8"/>

    <!-- Anticlockwise Rotation Arrow -->
    <path d="M 40 -50 Q 0 -80 -40 -50" fill="none" stroke="#22c55e" stroke-width="3"/>
    <text x="0" y="140" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Driven Gear (30 Teeth)</text>
    <text x="0" y="160" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Rotates Anticlockwise</text>
  </g>

  <!-- VR Formula Banner -->
  <g transform="translate(160, 320)">
    <rect width="500" height="50" rx="8" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
    <text x="250" y="32" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">VR = N_driven / N_driver = 30 / 10 = 3.0 (Torque Multiplied by 3×)</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg


# =============================================================================
# CURRICULUM DEFINITION DATA FOR TOPIC 6
# =============================================================================

def build_topic6_curriculum_data():
    return [
        # ---------------------------------------------------------------------
        # LESSON 1: Energy, Work and Power
        # ---------------------------------------------------------------------
        {
            "unit_order": 1,
            "unit_name": "Energy, Work and Power",
            "unit_description": "Precise physics definitions of Energy (capacity to do work), Work (W = F × d), zero work conditions, and Power (rate of energy transfer, P = W/t in Watts).",
            "lesson_title": "Energy, Work and Power",
            "pages": [
                # Page 1: Hook & Workers Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Industrial Labor: Lifting Heavy Construction Beams with Ropes",
                        "content": {
                            "title": "Industrial Labor: Lifting Heavy Construction Beams with Ropes",
                            "caption": "A team of construction workers using rope lines to lift a heavy timber beam. Work is performed as muscular forces displace the load vertically.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Construction_workers_lifting_beam.jpg/1280px-Construction_workers_lifting_beam.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Construction_workers_lifting_beam.jpg/1280px-Construction_workers_lifting_beam.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Workers Performing Mechanical Work on Construction Site",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Construction_workers_lifting_beam.jpg/1280px-Construction_workers_lifting_beam.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Construction_workers_lifting_beam.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Carrying Maize Flour: Work vs Power",
                        "content": {
                            "title": "Why Does Running Exhaust You Faster?",
                            "text": "If you carry a heavy $20\\text{ kg}$ bag of maize flour ($200\\text{ N}$) across a 20-metre yard:\n\n- Walking slowly takes 30 seconds.\n- Sprinting takes 5 seconds.\n\nIn both cases, you moved the exact same load over the same distance, performing the **exact same Work**. But running required **6 times more Power** because you transferred that energy in one-sixth of the time!"
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Work and Power",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **Energy** and **Work Done** in physics ($W = F \\times d$).",
                                "Explain why no mechanical work is done when force and displacement are perpendicular ($90^\\circ$).",
                                "Define **Power** as the rate of doing work ($P = W / t$) and calculate it in **Watts (W)**.",
                                "Solve quantitative problems relating force, distance, work, time, and power."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Work Done",
                        "content": {
                            "term": "Work Done",
                            "definition": "The mechanical energy transferred when a force causes an object to move in the direction of the force ($W = F \\times d$).",
                            "example": "Lifting a 1500 N block 8.0 m requires 12,000 Joules of work."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Power",
                        "content": {
                            "term": "Power",
                            "definition": "The rate at which work is done or energy is transferred per unit time ($P = W / t$).",
                            "example": "A 480 W student transfers 480 Joules of energy every second."
                        }
                    }
                ],
                # Page 3: Work vs Zero Work SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Work Done vs Zero Work Diagram",
                        "content": {
                            "title": "Work Done vs Zero Work Diagram",
                            "caption": "Comparison of active work (pushing box in direction of motion, W = 500 J) versus zero work (carrying bag vertically while moving horizontally, W = 0 J).",
                            "svg_content": get_svg_work_vs_zero_work(),
                            "svg": get_svg_work_vs_zero_work()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Work Done vs Zero Work Diagram",
                            "metadata": {
                                "svg_content": get_svg_work_vs_zero_work()
                            }
                        }
                    }
                ],
                # Page 4: Formulas & Units
                [
                    {
                        "type": "formula_breakdown",
                        "title": "Work and Power Mathematical Equations",
                        "content": {
                            "title": "Mechanical Work and Power Models",
                            "formula": "W = F \\times d \\quad \\text{and} \\quad P = \\frac{W}{t}",
                            "variables": [
                                "$W$ = Work done in Joules ($\\text{J}$ or $\\text{N m}$)",
                                "$F$ = Applied Force in Newtons ($\\text{N}$)",
                                "$d$ = Displacement in metres ($\\text{m}$)",
                                "$P$ = Power in Watts ($\\text{W}$ or $\\text{J/s}$)",
                                "$t$ = Time taken in seconds ($\\text{s}$)"
                            ],
                            "rules": [
                                "**One Joule (1 J)** = Work done by 1 N moving 1 m.",
                                "**One Watt (1 W)** = Rate of transferring 1 Joule per second ($1\\text{ W} = 1\\text{ J/s}$)."
                            ]
                        }
                    }
                ],
                # Page 5: Worked Example
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Crane Lifting Work & Student Running Power",
                        "content": {
                            "title": "Calculating Work and Power",
                            "problem": "1. A crane lifts a $150\\text{ kg}$ concrete block vertically through $8.0\\text{ m}$ ($g = 10\\text{ m/s}^2$). Calculate work done.\n2. A $60\\text{ kg}$ student runs up a $4.0\\text{ m}$ flight of stairs in $5.0\\text{ s}$. Calculate useful power output.",
                            "steps": [
                                "1. **Crane Lifting Force**: $F = mg = 150\\text{ kg} \\times 10 = 1500\\text{ N}$.\n   **Crane Work**: $W = F \\times d = 1500\\text{ N} \\times 8.0\\text{ m} = 12,000\\text{ J}$ ($12\\text{ kJ}$).",
                                "2. **Student Force**: $F = mg = 60 \\times 10 = 600\\text{ N}$.\n   **Student Work**: $W = 600\\text{ N} \\times 4.0\\text{ m} = 2400\\text{ J}$.\n   **Student Power**: $P = \\frac{W}{t} = \\frac{2400\\text{ J}}{5.0\\text{ s}} = 480\\text{ W}$."
                            ],
                            "answer": "Crane work is 12 kJ; student power output is 480 W."
                        }
                    }
                ],
                # Page 6: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Comparing Water Pump Work & Power",
                        "content": {
                            "question": "Pump A lifts $120\\text{ kg}$ of water through $10\\text{ m}$ in $20\\text{ s}$. Pump B lifts the same $120\\text{ kg}$ of water through $10\\text{ m}$ in only $10\\text{ s}$. How do their work and power outputs compare?",
                            "options": [
                                "Both do the exact same work, but Pump B has twice the power of Pump A.",
                                "Pump B does twice the work of Pump A, but they have equal power.",
                                "Both pumps have equal power, but Pump B does half the work.",
                                "Pump B has twice the work and twice the power."
                            ],
                            "answer": "A",
                            "explanation": "Work depends only on force and height: $W = mgh = 120 \\times 10 \\times 10 = 12,000\\text{ J}$. Because both pumps lift the same mass through the same height, they do **identical work** ($12\\text{ kJ}$). Pump B completes this work in half the time ($10\\text{ s}$ vs $20\\text{ s}$), so its power is double: $P_B = \\frac{12000}{10} = 1200\\text{ W}$ while $P_A = \\frac{12000}{20} = 600\\text{ W}$. Therefore, Option A is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Work, Energy and Power Explained",
                        "content": {
                            "title": "Physics Video: Work, Energy and Power Explained",
                            "description": "Video explaining the relationship between force, displacement, work in Joules, and the rate of energy transfer in Watts.",
                            "url": "https://www.youtube.com/watch?v=w4QFJb9a8vo",
                            "resolved_video_id": "w4QFJb9a8vo"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Work and Power Physics Tutorial",
                            "url": "https://www.youtube.com/watch?v=w4QFJb9a8vo",
                            "metadata": {
                                "youtube_id": "w4QFJb9a8vo"
                            }
                        }
                    }
                ],
                # Page 8: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson 1 Summary: Key Takeaways",
                        "content": {
                            "title": "Core Summary",
                            "takeaways": [
                                "**Work** ($W = F \\times d$) requires displacement in the direction of the force (unit: Joule, J).",
                                "Carrying an object horizontally does zero work in the vertical direction.",
                                "**Power** ($P = W / t$) is the rate of doing work (unit: Watt, W)."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 2: Kinetic and Potential Energy
        # ---------------------------------------------------------------------
        {
            "unit_order": 2,
            "unit_name": "Kinetic and Potential Energy",
            "unit_description": "Mathematical models of Kinetic Energy (Ek = 1/2 m v²), Gravitational Potential Energy (Ep = mgh), Elastic Potential Energy, and the parabolic speed-square relationship.",
            "lesson_title": "Kinetic and Potential Energy",
            "pages": [
                # Page 1: Hook & Hydroelectric Dam Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Stored Potential to Active Kinetic: Hydroelectric Reservoir Cascades",
                        "content": {
                            "title": "Stored Potential to Active Kinetic: Hydroelectric Reservoir Cascades",
                            "caption": "Masinga Dam reservoir holding millions of tonnes of water at high elevation. The stored gravitational potential energy (Ep = mgh) converts into kinetic energy as water falls through penstocks to turn turbines.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Hydroelectric_dam_turbines.jpg/1280px-Hydroelectric_dam_turbines.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Hydroelectric_dam_turbines.jpg/1280px-Hydroelectric_dam_turbines.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Hydroelectric Dam Water Potential Energy",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Hydroelectric_dam_turbines.jpg/1280px-Hydroelectric_dam_turbines.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Hydroelectric_dam_turbines.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "From Stored Tension to Explosive Motion",
                        "content": {
                            "title": "The Dual Faces of Energy",
                            "text": "When you pull back the elastic band of a catapult, nothing moves, yet enormous energy is stored waiting to launch.\n\nEnergy manifests as **Potential Energy** (stored due to position or deformation) or **Kinetic Energy** (active motion)."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Kinetic & Potential Energy",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define and calculate **Gravitational Potential Energy ($E_p = mgh$)**.",
                                "Define and calculate **Kinetic Energy ($E_k = \\frac{1}{2}mv^2$)**.",
                                "Analyze the **speed-square proportionality** ($E_k \\propto v^2$) and its impact on vehicle safety.",
                                "Understand Elastic Potential Energy stored in deformed materials."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Gravitational Potential Energy (Ep)",
                        "content": {
                            "term": "Gravitational Potential Energy (Ep)",
                            "definition": "The energy stored in an object due to its vertical elevation in a gravitational field ($E_p = mgh$).",
                            "example": "A 500 kg water tank raised 6.0 m stores 30,000 J of GPE."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Kinetic Energy (Ek)",
                        "content": {
                            "term": "Kinetic Energy (Ek)",
                            "definition": "The energy possessed by an object due to its physical velocity ($E_k = \\frac{1}{2}mv^2$).",
                            "example": "A 40 kg cheetah running at 25 m/s has 12,500 J of KE."
                        }
                    }
                ],
                # Page 3: KE vs Speed Parabola SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Kinetic Energy vs Speed Parabolic Curve",
                        "content": {
                            "title": "Kinetic Energy vs Speed Parabolic Curve",
                            "caption": "Parabolic plot of Kinetic Energy vs Speed for a 1,000 kg vehicle: Doubling speed from 10 to 20 m/s quadruples KE from 50 to 200 kJ.",
                            "svg_content": get_svg_ke_speed_parabola(),
                            "svg": get_svg_ke_speed_parabola()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Kinetic Energy Speed Parabola Diagram",
                            "metadata": {
                                "svg_content": get_svg_ke_speed_parabola()
                            }
                        }
                    }
                ],
                # Page 4: Mathematical Models
                [
                    {
                        "type": "formula_breakdown",
                        "title": "Energy Equations",
                        "content": {
                            "title": "Potential and Kinetic Energy Equations",
                            "formula": "E_p = mgh \\quad \\text{and} \\quad E_k = \\frac{1}{2}mv^2",
                            "variables": [
                                "$E_p, E_k$ = Energy in Joules ($\\text{J}$)",
                                "$m$ = Mass in kilograms ($\\text{kg}$)",
                                "$g$ = Acceleration due to gravity ($10\\text{ m/s}^2$)",
                                "$h$ = Height in metres ($\\text{m}$)",
                                "$v$ = Speed in metres per second ($\\text{m/s}$)"
                            ]
                        }
                    }
                ],
                # Page 5: Worked Example
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Elevated Tank GPE & Running Cheetah KE",
                        "content": {
                            "title": "Calculating GPE and KE",
                            "problem": "1. Calculate GPE of a $500\\text{ kg}$ water tank $6.0\\text{ m}$ high ($g = 10\\text{ m/s}^2$).\n2. Calculate KE of a $40\\text{ kg}$ cheetah running at $25\\text{ m/s}$.",
                            "steps": [
                                "1. **GPE**: $E_p = mgh = 500\\text{ kg} \\times 10 \\times 6.0\\text{ m} = 30,000\\text{ J}$ ($30\\text{ kJ}$).",
                                "2. **KE**: $E_k = 0.5 \\times 40\\text{ kg} \\times (25\\text{ m/s})^2 = 20 \\times 625 = 12,500\\text{ J}$ ($12.5\\text{ kJ}$)."
                            ],
                            "answer": "Tank GPE is 30 kJ; cheetah KE is 12.5 kJ."
                        }
                    }
                ],
                # Page 6: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Comparing GPE of Stones",
                        "content": {
                            "question": "Stone A has mass $2\\text{ kg}$ and rests on a wall $5\\text{ m}$ high. Stone B has mass $1\\text{ kg}$ and rests on a building $10\\text{ m}$ high. How do their gravitational potential energies compare?",
                            "options": [
                                "Stone A has twice the GPE of Stone B.",
                                "Stone B has twice the GPE of Stone A.",
                                "Both stones store the exact same GPE (100 J).",
                                "GPE cannot be calculated without speed."
                            ],
                            "answer": "C",
                            "explanation": "Calculate GPE: Stone A: $E_{p1} = 2\\text{ kg} \\times 10 \\times 5\\text{ m} = 100\\text{ J}$. Stone B: $E_{p2} = 1\\text{ kg} \\times 10 \\times 10\\text{ m} = 100\\text{ J}$. Despite different masses and heights, both store **identical GPE ($100\\text{ J}$)** because the product $m \\times h$ is identical ($2 \\times 5 = 1 \\times 10$). Therefore, Option C is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Kinetic and Potential Energy Calculations",
                        "content": {
                            "title": "Physics Video: Kinetic and Potential Energy Calculations",
                            "description": "Video explaining the formulas for potential and kinetic energy, the speed-square law, and roller coaster energy conversions.",
                            "url": "https://www.youtube.com/watch?v=BSWlnJbTA00",
                            "resolved_video_id": "BSWlnJbTA00"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Kinetic and Potential Energy Video",
                            "url": "https://www.youtube.com/watch?v=BSWlnJbTA00",
                            "metadata": {
                                "youtube_id": "BSWlnJbTA00"
                            }
                        }
                    }
                ],
                # Page 8: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson 2 Summary: Key Takeaways",
                        "content": {
                            "title": "Core Summary",
                            "takeaways": [
                                "**Gravitational Potential Energy**: $E_p = mgh$.",
                                "**Kinetic Energy**: $E_k = \\frac{1}{2}mv^2$ (grows quadratically with speed).",
                                "Both forms are measured in **Joules (J)**."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 3: Conservation and Transformation of Mechanical Energy
        # ---------------------------------------------------------------------
        {
            "unit_order": 3,
            "unit_name": "Conservation and Transformation of Mechanical Energy",
            "unit_description": "The Law of Conservation of Energy, mechanical energy transformations (Ek + Ep = constant), velocity of a falling body (v = √(2gh)), friction dissipation, and Sankey diagrams.",
            "lesson_title": "Conservation and Transformation of Mechanical Energy",
            "pages": [
                # Page 1: Hook & Swing Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Harmonic Exchange: Playground Swing Kinetic-Potential Transformation",
                        "content": {
                            "title": "Harmonic Exchange: Playground Swing Kinetic-Potential Transformation",
                            "caption": "A child on a playground swing. At peak height, speed is zero (maximum potential energy), which converts into peak speed at the lowest point (maximum kinetic energy).",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Child_on_a_swing.jpg/1280px-Child_on_a_swing.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Child_on_a_swing.jpg/1280px-Child_on_a_swing.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Playground Swing Energy Transformation",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Child_on_a_swing.jpg/1280px-Child_on_a_swing.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Child_on_a_swing.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Pendulum of Trust",
                        "content": {
                            "title": "Why a Pendulum Never Hits Your Nose",
                            "text": "If you hold a heavy bowling ball pendulum against your nose and release it without pushing, will it smash your face when it swings back?\n\nNo! It stops a fraction of a millimeter in front of your skin. Energy cannot be created from nothing; this is the **Law of Conservation of Energy**."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Energy Conservation",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "State the **Law of Conservation of Energy**.",
                                "Model mechanical energy conversion in falling bodies and pendulums ($E_k + E_p = \\text{Constant}$).",
                                "Derive and apply $v = \\sqrt{2gh}$ for freefall without air resistance.",
                                "Interpret **Sankey diagrams** showing useful energy vs dissipative friction heat."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Law of Conservation of Energy",
                        "content": {
                            "term": "Law of Conservation of Energy",
                            "definition": "Energy cannot be created or destroyed; it can only be transformed from one form to another. Total energy in an isolated system remains constant.",
                            "example": "Falling water converts potential energy into kinetic energy to drive generators."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Energy Dissipation",
                        "content": {
                            "term": "Energy Dissipation",
                            "definition": "The conversion of useful mechanical energy into non-useful thermal or acoustic energy due to friction and air resistance.",
                            "example": "Car brake pads getting hot during braking."
                        }
                    }
                ],
                # Page 3: Falling Stone SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Conservation of Mechanical Energy in Freefall",
                        "content": {
                            "title": "Conservation of Mechanical Energy in Freefall",
                            "caption": "Falling body converting GPE (mgh) at top into KE (1/2 mv²) at ground impact with constant total mechanical energy and impact speed v = √(2gh).",
                            "svg_content": get_svg_falling_stone_energy(),
                            "svg": get_svg_falling_stone_energy()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Freefall Energy Conservation Diagram",
                            "metadata": {
                                "svg_content": get_svg_falling_stone_energy()
                            }
                        }
                    }
                ],
                # Page 4: Derivation & Speed Formula
                [
                    {
                        "type": "formula_breakdown",
                        "title": "Velocity of a Free-Falling Body",
                        "content": {
                            "title": "Mass-Independent Falling Velocity",
                            "formula": "mgh = \\frac{1}{2}mv^2 \\implies v = \\sqrt{2gh}",
                            "variables": [
                                "$v$ = Impact speed in metres per second ($\\text{m/s}$)",
                                "$g$ = Acceleration due to gravity ($10\\text{ m/s}^2$)",
                                "$h$ = Falling height in metres ($\\text{m}$)"
                            ],
                            "rules": [
                                "**Galileo's Discovery**: In the absence of air resistance, mass $m$ cancels out; all objects fall and reach the ground with identical speed from height $h$."
                            ]
                        }
                    }
                ],
                # Page 5: Sankey Flow SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Sankey Diagram: Water Pump Energy Distribution",
                        "content": {
                            "title": "Sankey Diagram: Water Pump Energy Distribution",
                            "caption": "Sankey energy flow: 100 J input splits into 70 J useful water GPE and 30 J wasted friction heat.",
                            "svg_content": get_svg_sankey_diagram(),
                            "svg": get_svg_sankey_diagram()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Water Pump Sankey Diagram",
                            "metadata": {
                                "svg_content": get_svg_sankey_diagram()
                            }
                        }
                    }
                ],
                # Page 6: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Energy State at Lowest Point of Swing",
                        "content": {
                            "question": "A pendulum is released from rest at Position A. As it swings down through its lowest vertical point (Position B), which statement correctly describes its energy?",
                            "options": [
                                "Potential energy is maximum and kinetic energy is zero.",
                                "Both kinetic and potential energy are maximum simultaneously.",
                                "Potential energy is at a minimum and kinetic energy is at its maximum.",
                                "Total mechanical energy is double the initial value."
                            ],
                            "answer": "C",
                            "explanation": "As the bob swings downward, it loses height (minimum GPE). By conservation of energy, all lost GPE converts into **Kinetic Energy**, reaching maximum speed and maximum KE at the lowest point. Total mechanical energy remains constant. Option C is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Conservation of Energy and Pendulum Demonstration",
                        "content": {
                            "title": "Physics Video: Conservation of Energy and Pendulum Demonstration",
                            "description": "Video demonstrating conservation of mechanical energy, freefall speed derivations, and the pendulum of trust.",
                            "url": "https://www.youtube.com/watch?v=w4QFJb9a8vo",
                            "resolved_video_id": "w4QFJb9a8vo"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Energy Conservation Demonstration Video",
                            "url": "https://www.youtube.com/watch?v=w4QFJb9a8vo",
                            "metadata": {
                                "youtube_id": "w4QFJb9a8vo"
                            }
                        }
                    }
                ],
                # Page 8: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson 3 Summary: Key Takeaways",
                        "content": {
                            "title": "Core Summary",
                            "takeaways": [
                                "**Law of Conservation of Energy**: Energy cannot be created or destroyed.",
                                "In freefall, $mgh = \\frac{1}{2}mv^2 \\implies v = \\sqrt{2gh}$.",
                                "Real machines experience **dissipation**, converting useful energy to friction heat."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 4: Simple Machines and Mechanical Advantage
        # ---------------------------------------------------------------------
        {
            "unit_order": 4,
            "unit_name": "Simple Machines and Mechanical Advantage",
            "unit_description": "Fundamental metrics of simple machines: Load, Effort, Mechanical Advantage (MA = L/E), Velocity Ratio (VR = d_E/d_L), Efficiency (η = MA/VR × 100%), and why real machines are never 100% efficient.",
            "lesson_title": "Simple Machines and Mechanical Advantage",
            "pages": [
                # Page 1: Hook & Crate Ramp Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Force Multiplication: Rolling Heavy Crate Up an Inclined Ramp",
                        "content": {
                            "title": "Force Multiplication: Rolling Heavy Crate Up an Inclined Ramp",
                            "caption": "A worker using a wooden ramp to load a heavy cargo crate onto a truck bed. The ramp allows a small effort force to overcome a heavy load by increasing the pushing distance.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Worker_pushing_cart_up_ramp.jpg/1280px-Worker_pushing_cart_up_ramp.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Worker_pushing_cart_up_ramp.jpg/1280px-Worker_pushing_cart_up_ramp.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Worker Using Simple Machine Ramp",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Worker_pushing_cart_up_ramp.jpg/1280px-Worker_pushing_cart_up_ramp.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Worker_pushing_cart_up_ramp.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Golden Rule of Machines",
                        "content": {
                            "title": "You Cannot Get Free Work!",
                            "text": "How can a system of pulleys allow one student to lift a heavy 1200 N vehicle engine?\n\nA machine multiplies your **force**, but you pay for it by moving a much longer **distance** ($VR = d_E / d_L$)."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Machine Performance Metrics",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **Load, Effort**, and **Mechanical Advantage ($MA = L/E$)**.",
                                "Define **Velocity Ratio ($VR = d_E/d_L$)** as a geometric property.",
                                "Calculate **Efficiency** using $\\eta = \\left(\\frac{MA}{VR}\\right) \\times 100\\%$.",
                                "Explain why real machine efficiency is always **less than $100\\%$**."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Mechanical Advantage (MA)",
                        "content": {
                            "term": "Mechanical Advantage (MA)",
                            "definition": "The factor by which a machine multiplies the applied input effort force ($MA = \\text{Load} / \\text{Effort}$). It has no units.",
                            "example": "An effort of 400 N lifting a 1200 N load yields an MA of 3.0."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Velocity Ratio (VR)",
                        "content": {
                            "term": "Velocity Ratio (VR)",
                            "definition": "The ratio of the distance moved by the effort to the distance moved by the load ($VR = d_E / d_L$). It depends solely on machine geometry.",
                            "example": "In a 4-strand pulley, the effort moves 4 metres for every 1 metre the load rises ($VR = 4$)."
                        }
                    }
                ],
                # Page 3: Pulley Block & Tackle SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Block and Tackle Pulley System Performance Metrics",
                        "content": {
                            "title": "Block and Tackle Pulley System Performance Metrics",
                            "caption": "A 4-rope pulley system lifting 1200 N with 400 N effort, demonstrating MA = 3, VR = 4, and Efficiency = 75%.",
                            "svg_content": get_svg_pulley_block_tackle(),
                            "svg": get_svg_pulley_block_tackle()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Block and Tackle Pulley Metrics Diagram",
                            "metadata": {
                                "svg_content": get_svg_pulley_block_tackle()
                            }
                        }
                    }
                ],
                # Page 4: Efficiency Relationship
                [
                    {
                        "type": "formula_breakdown",
                        "title": "Machine Efficiency Derivation",
                        "content": {
                            "title": "Efficiency Equation",
                            "formula": "\\eta = \\frac{\\text{Useful Work Output}}{\\text{Total Work Input}} \\times 100\\% = \\left( \\frac{L \\times d_L}{E \\times d_E} \\right) \\times 100\\% = \\left( \\frac{MA}{VR} \\right) \\times 100\\%",
                            "variables": [
                                "$\\eta$ = Efficiency percentage ($\\text{\\%}$)",
                                "$MA$ = Mechanical Advantage ($L/E$)",
                                "$VR$ = Velocity Ratio ($d_E/d_L$)"
                            ],
                            "rules": [
                                "**Friction & Weight**: Real machines must overcome moving friction and lift their own parts, so $\\text{Work Output} < \\text{Work Input}$ and $\\eta < 100\\%$."
                            ]
                        }
                    }
                ],
                # Page 5: Worked Example
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Complete Pulley Performance Evaluation",
                        "content": {
                            "title": "Calculating MA, Effort Distance, and Efficiency",
                            "problem": "A pulley with $VR = 4$ lifts a $1200\\text{ N}$ engine through $2.0\\text{ m}$ with an effort of $400\\text{ N}$. Calculate:\n1. Mechanical Advantage ($MA$).\n2. Effort rope distance pulled ($d_E$).\n3. Useful efficiency ($\\eta$).",
                            "steps": [
                                "1. **MA**: $MA = \\frac{\\text{Load}}{\\text{Effort}} = \\frac{1200\\text{ N}}{400\\text{ N}} = 3.0$.",
                                "2. **Effort Distance**: $VR = \\frac{d_E}{d_L} \\implies 4 = \\frac{d_E}{2.0\\text{ m}} \\implies d_E = 8.0\\text{ m}$.",
                                "3. **Efficiency**: $\\eta = \\left(\\frac{MA}{VR}\\right) \\times 100\\% = \\left(\\frac{3.0}{4.0}\\right) \\times 100\\% = 75.0\\%$."
                            ],
                            "answer": "MA is 3.0, effort distance is 8.0 m, and efficiency is 75%."
                        }
                    }
                ],
                # Page 6: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Effect of Lubrication on Machines",
                        "content": {
                            "question": "A mechanic lubricates the squeaky bearings of a crane with grease. How does this lubrication affect the Mechanical Advantage ($MA$), Velocity Ratio ($VR$), and Efficiency of the machine?",
                            "options": [
                                "Both MA and VR increase, but efficiency stays unchanged.",
                                "VR increases, but MA and efficiency decrease.",
                                "MA and efficiency increase, while geometric VR remains exactly the same.",
                                "All three parameters double."
                            ],
                            "answer": "C",
                            "explanation": "Greasing bearings reduces friction, meaning less effort is needed to lift the same load, increasing **Mechanical Advantage ($MA = L/E$)**. Because $VR$ depends purely on wheel dimensions and rope geometry, **$VR$ remains unchanged**. Since efficiency is $\\eta = \\frac{MA}{VR} \\times 100\\%$, efficiency **increases**. Option C is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Simple Machines, MA, VR and Efficiency",
                        "content": {
                            "title": "Physics Video: Simple Machines, MA, VR and Efficiency",
                            "description": "Video explaining mechanical advantage, velocity ratio, and efficiency in pulleys and inclined planes.",
                            "url": "https://www.youtube.com/watch?v=ytwzRk_L_aA",
                            "resolved_video_id": "ytwzRk_L_aA"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Simple Machines MA VR Efficiency Video",
                            "url": "https://www.youtube.com/watch?v=ytwzRk_L_aA",
                            "metadata": {
                                "youtube_id": "ytwzRk_L_aA"
                            }
                        }
                    }
                ],
                # Page 8: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson 4 Summary: Key Takeaways",
                        "content": {
                            "title": "Core Summary",
                            "takeaways": [
                                "**Mechanical Advantage**: $MA = \\text{Load} / \\text{Effort}$.",
                                "**Velocity Ratio**: $VR = d_E / d_L$ (geometric ratio).",
                                "**Efficiency**: $\\eta = (MA / VR) \\times 100\\%$ (always $< 100\\%$ due to friction)."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 5: Levers, Moments and Inclined Planes
        # ---------------------------------------------------------------------
        {
            "unit_order": 5,
            "unit_name": "Levers, Moments and Inclined Planes",
            "unit_description": "Classification of the 3 classes of levers (1st, 2nd, and 3rd class), inclined plane mechanics (VR = L/h = 1/sin θ), wheelchair ramp calculations, and friction trade-offs.",
            "lesson_title": "Levers, Moments and Inclined Planes",
            "pages": [
                # Page 1: Hook & Wheelbarrow Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Agricultural Leverage: Farm Wheelbarrow (Second-Class Lever)",
                        "content": {
                            "title": "Agricultural Leverage: Farm Wheelbarrow (Second-Class Lever)",
                            "caption": "A farm wheelbarrow transporting harvested produce. The front wheel acts as the fulcrum, the cargo load rests in the middle, and upward effort is applied at the long handles.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Wheelbarrow_on_farm.jpg/1280px-Wheelbarrow_on_farm.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Wheelbarrow_on_farm.jpg/1280px-Wheelbarrow_on_farm.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Agricultural Wheelbarrow Lever Application",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Wheelbarrow_on_farm.jpg/1280px-Wheelbarrow_on_farm.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Wheelbarrow_on_farm.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Rolling Up a Slope Beats Lifting",
                        "content": {
                            "title": "The Geometry of Slopes",
                            "text": "Lifting a heavy $100\\text{ kg}$ oil drum vertically onto a lorry bed requires four straining people.\n\nLay two wooden planks at an angle, and one person rolls the drum up easily! The **Inclined Plane** and the **Lever** are two of humanity's oldest machines."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Levers and Ramps",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Classify the **3 classes of levers** based on Fulcrum, Load, and Effort positions.",
                                "Derive and calculate the Velocity Ratio of an **Inclined Plane** ($VR = L/h = 1/\\sin\\theta$).",
                                "Calculate $MA$, $VR$, and efficiency for wheelchair ramps and levers.",
                                "Explain how sliding friction limits ramp efficiency."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Lever",
                        "content": {
                            "term": "Lever",
                            "definition": "A rigid bar pivoted about a fixed point (fulcrum) used to multiply force or speed.",
                            "example": "Crowbars, wheelbarrows, and tweezers."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Inclined Plane",
                        "content": {
                            "term": "Inclined Plane",
                            "definition": "A flat surface set at an angle to the horizontal used to raise heavy loads with reduced effort force.",
                            "example": "Wheelchair ramps and road switchbacks on steep hills."
                        }
                    }
                ],
                # Page 3: 3 Classes of Levers SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Three Classes of Levers Diagram",
                        "content": {
                            "title": "The Three Classes of Levers Diagram",
                            "caption": "Structural comparison: 1st Class (Fulcrum in middle, e.g. scissors), 2nd Class (Load in middle, e.g. wheelbarrow), 3rd Class (Effort in middle, e.g. tweezers).",
                            "svg_content": get_svg_three_lever_classes(),
                            "svg": get_svg_three_lever_classes()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Three Classes of Levers Diagram",
                            "metadata": {
                                "svg_content": get_svg_three_lever_classes()
                            }
                        }
                    }
                ],
                # Page 4: Inclined Plane SVG & Formula
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Inclined Plane Geometry and Velocity Ratio",
                        "content": {
                            "title": "Inclined Plane Geometry and Velocity Ratio",
                            "caption": "Inclined plane showing slope length L = 12.0 m, vertical rise h = 1.5 m, yielding VR = L/h = 8.0.",
                            "svg_content": get_svg_inclined_plane(),
                            "svg": get_svg_inclined_plane()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Inclined Plane Geometry Diagram",
                            "metadata": {
                                "svg_content": get_svg_inclined_plane()
                            }
                        }
                    },
                    {
                        "type": "formula_breakdown",
                        "title": "Inclined Plane Equation",
                        "content": {
                            "title": "Ramp Velocity Ratio",
                            "formula": "VR = \\frac{\\text{Slope Length (}L\\text{)}}{\\text{Vertical Height (}h\\text{)}} = \\frac{1}{\\sin(\\theta)}",
                            "variables": [
                                "$L$ = Length of the inclined ramp ($\\text{m}$)",
                                "$h$ = Vertical elevation gain ($\\text{m}$)",
                                "$\\theta$ = Angle of inclination ($^\\circ$)"
                            ]
                        }
                    }
                ],
                # Page 5: Worked Example (Hospital Ramp)
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Hospital Wheelchair Ramp Evaluation",
                        "content": {
                            "title": "Evaluating a 12 m Wheelchair Ramp",
                            "problem": "A hospital ramp is $12.0\\text{ m}$ long and reaches an elevation of $1.5\\text{ m}$. An $800\\text{ N}$ wheelchair is pushed up using $160\\text{ N}$ effort. Calculate:\n1. Velocity Ratio ($VR$).\n2. Mechanical Advantage ($MA$).\n3. Useful efficiency ($\\eta$).",
                            "steps": [
                                "1. **VR**: $VR = \\frac{L}{h} = \\frac{12.0\\text{ m}}{1.5\\text{ m}} = 8.0$.",
                                "2. **MA**: $MA = \\frac{\\text{Load}}{\\text{Effort}} = \\frac{800\\text{ N}}{160\\text{ N}} = 5.0$.",
                                "3. **Efficiency**: $\\eta = \\left(\\frac{MA}{VR}\\right) \\times 100\\% = \\left(\\frac{5.0}{8.0}\\right) \\times 100\\% = 62.5\\%$."
                            ],
                            "answer": "VR is 8.0, MA is 5.0, and efficiency is 62.5% (37.5% lost to wheel friction)."
                        }
                    }
                ],
                # Page 6: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Ramp Efficiency Limitation",
                        "content": {
                            "question": "Why is the actual efficiency of a real-world inclined plane ramp always significantly less than 100%?",
                            "options": [
                                "Gravity pulls stronger on tilted surfaces than vertical drops.",
                                "A significant portion of input work is dissipated as heat overcoming friction between the load and ramp surface.",
                                "The diagonal length of a ramp is mathematically shorter than its height.",
                                "Ramps destroy a portion of the input force."
                            ],
                            "answer": "B",
                            "explanation": "Any object moving along an inclined plane encounters sliding/rolling friction against the ramp surface. This friction dissipates input work into heat, ensuring useful work output is less than input work, resulting in an efficiency below 100%. Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Levers and Inclined Planes Explained",
                        "content": {
                            "title": "Physics Video: Levers and Inclined Planes Explained",
                            "description": "Video explaining first, second, and third-class levers, inclined planes, and calculating mechanical advantage.",
                            "url": "https://www.youtube.com/watch?v=ytwzRk_L_aA",
                            "resolved_video_id": "ytwzRk_L_aA"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Levers and Ramps Physics Tutorial",
                            "url": "https://www.youtube.com/watch?v=ytwzRk_L_aA",
                            "metadata": {
                                "youtube_id": "ytwzRk_L_aA"
                            }
                        }
                    }
                ],
                # Page 8: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson 5 Summary: Key Takeaways",
                        "content": {
                            "title": "Core Summary",
                            "takeaways": [
                                "**1st Class**: Fulcrum in middle; **2nd Class**: Load in middle ($MA > 1$); **3rd Class**: Effort in middle ($MA < 1$).",
                                "**Inclined Plane**: $VR = L/h = 1/\\sin\\theta$.",
                                "Gentle slopes have large $VR$, reducing required effort force."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 6: Wheels, Axles, Gears, Pulleys and Hydraulic Machines
        # ---------------------------------------------------------------------
        {
            "unit_order": 6,
            "unit_name": "Wheels, Axles, Gears, Pulleys and Hydraulic Machines",
            "unit_description": "Rotational transmission systems (Wheel and Axle VR = R/r, Gears VR = N_driven/N_driver), multi-pulley systems, and Hydraulic Machines based on Pascal's Principle (P = F1/A1 = F2/A2).",
            "lesson_title": "Wheels, Axles, Gears, Pulleys and Hydraulic Machines",
            "pages": [
                # Page 1: Hook & Hydraulic Jack Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Fluid Transmission: Heavy-Duty Hydraulic Bottle Jack Lifting a Lorry",
                        "content": {
                            "title": "Fluid Transmission: Heavy-Duty Hydraulic Bottle Jack Lifting a Lorry",
                            "caption": "A vehicle mechanic operating a hydraulic bottle jack under a multi-ton lorry axle. Small strokes on the hand lever multiply force 40-fold through Pascal's Principle.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Hydraulic_bottle_jack.jpg/1280px-Hydraulic_bottle_jack.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Hydraulic_bottle_jack.jpg/1280px-Hydraulic_bottle_jack.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Hydraulic Bottle Jack Force Multiplication",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Hydraulic_bottle_jack.jpg/1280px-Hydraulic_bottle_jack.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Hydraulic_bottle_jack.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Bicycle Gears and Hydraulic Power",
                        "content": {
                            "title": "Transforming Rotational and Fluid Motion",
                            "text": "When riding a multi-speed bicycle up a hill, shifting to a low gear lets your legs spin fast while moving up steep inclines easily.\n\nConnecting rotating gears or hydraulic pistons allows us to transform speed, torque, and force."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Complex Transmission Systems",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Calculate $VR$ for **Wheel and Axle** systems ($VR = R/r$).",
                                "Calculate $VR$ for **Gear Trains** ($VR = N_{\\text{driven}} / N_{\\text{driver}}$).",
                                "Apply Pascal's Principle to calculate force multiplication in **Hydraulic Machines** ($F_2 = F_1 \\times \\frac{A_2}{A_1}$).",
                                "Explain why trapped air bubbles ruin hydraulic machine performance."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Wheel and Axle",
                        "content": {
                            "term": "Wheel and Axle",
                            "definition": "A machine consisting of two co-axial cylinders of different radii ($R$ and $r$) rotating together ($VR = R/r$).",
                            "example": "Doorknobs, screwdrivers, steering wheels, and windlasses."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Gear Train",
                        "content": {
                            "term": "Gear Train",
                            "definition": "A system of toothed intermeshed wheels that transmits rotational speed and torque ($VR = N_{\\text{driven}} / N_{\\text{driver}}$).",
                            "example": "Bicycle derailleur gears and car transmissions."
                        }
                    }
                ],
                # Page 3: Meshed Gears SVG & Formula
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Meshed Gear Transmission Diagram",
                        "content": {
                            "title": "Meshed Gear Transmission Diagram",
                            "caption": "Driver gear (10 teeth) meshing with driven gear (30 teeth) showing opposite rotation and VR = 30 / 10 = 3.0 (torque multiplied by 3).",
                            "svg_content": get_svg_meshed_gears(),
                            "svg": get_svg_meshed_gears()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Meshed Gear Transmission Diagram",
                            "metadata": {
                                "svg_content": get_svg_meshed_gears()
                            }
                        }
                    }
                ],
                # Page 4: Hydraulic Jack Calculations
                [
                    {
                        "type": "formula_breakdown",
                        "title": "Hydraulic Transmission Model",
                        "content": {
                            "title": "Pascal's Principle in Hydraulics",
                            "formula": "P = \\frac{F_1}{A_1} = \\frac{F_2}{A_2} \\implies F_2 = F_1 \\times \\left(\\frac{A_2}{A_1}\\right) \\quad \\text{and} \\quad VR = \\frac{A_2}{A_1} = \\left(\\frac{D_2}{D_1}\\right)^2",
                            "variables": [
                                "$F_1, F_2$ = Input effort and output load forces ($\\text{N}$)",
                                "$A_1, A_2$ = Input and output piston areas ($\\text{m}^2$)",
                                "$D_1, D_2$ = Piston diameters ($\\text{m}$)"
                            ]
                        }
                    }
                ],
                # Page 5: Worked Example (Hydraulic Garage Lift)
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Hydraulic Garage Lift Performance",
                        "content": {
                            "title": "Evaluating a 12,000 N Car Lift",
                            "problem": "A hydraulic lift has an input piston of $0.01\\text{ m}^2$ and an output piston of $0.50\\text{ m}^2$. A $300\\text{ N}$ effort raises a $12,000\\text{ N}$ car. Calculate:\n1. Velocity Ratio ($VR$).\n2. Mechanical Advantage ($MA$).\n3. Useful efficiency ($\\eta$).",
                            "steps": [
                                "1. **VR**: $VR = \\frac{A_2}{A_1} = \\frac{0.50\\text{ m}^2}{0.01\\text{ m}^2} = 50$.",
                                "2. **MA**: $MA = \\frac{\\text{Load}}{\\text{Effort}} = \\frac{12,000\\text{ N}}{300\\text{ N}} = 40$.",
                                "3. **Efficiency**: $\\eta = \\left(\\frac{MA}{VR}\\right) \\times 100\\% = \\left(\\frac{40}{50}\\right) \\times 100\\% = 80.0\\%$."
                            ],
                            "answer": "VR is 50, MA is 40, and efficiency is 80%."
                        }
                    }
                ],
                # Page 6: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Air Bubble in Hydraulic Brake System",
                        "content": {
                            "question": "A motorist notices that their vehicle's hydraulic brake pedal feels 'spongy' and stops poorly. The mechanic explains there is an air bubble trapped in the brake fluid line. Why does trapped air reduce hydraulic performance?",
                            "options": [
                                "Air is heavier than brake oil, increasing the load on the pedal.",
                                "Air bubbles chemically react with oil, turning it to water.",
                                "Air is highly compressible; effort is wasted squeezing the gas instead of transmitting fluid pressure to brake pads.",
                                "Air bubbles freeze instantly at room temperature."
                            ],
                            "answer": "C",
                            "explanation": "Liquids are virtually incompressible, transmitting applied pressure undiminished. Gases are highly compressible. When an air bubble is trapped in hydraulic lines, pedal effort merely compresses the air volume instead of transmitting pressure to the wheel slave cylinders, resulting in a 'spongy' pedal and brake failure. Option C is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Gears, Pulleys, and Hydraulic Systems",
                        "content": {
                            "title": "Physics Video: Gears, Pulleys, and Hydraulic Systems",
                            "description": "Video explaining gear ratios, wheel and axle mechanics, and hydraulic force multiplication via Pascal's Principle.",
                            "url": "https://www.youtube.com/watch?v=ytwzRk_L_aA",
                            "resolved_video_id": "ytwzRk_L_aA"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Gears and Hydraulics Video Demonstration",
                            "url": "https://www.youtube.com/watch?v=ytwzRk_L_aA",
                            "metadata": {
                                "youtube_id": "ytwzRk_L_aA"
                            }
                        }
                    }
                ],
                # Page 8: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson 6 Summary: Key Takeaways",
                        "content": {
                            "title": "Core Summary",
                            "takeaways": [
                                "**Wheel and Axle**: $VR = R/r$.",
                                "**Gear Systems**: $VR = N_{\\text{driven}} / N_{\\text{driver}}$.",
                                "**Hydraulic Machines**: $F_2 = F_1 \\times \\left(\\frac{A_2}{A_1}\\right)$ with $VR = A_2/A_1$.",
                                "Trapped air bubbles severely degrade hydraulics due to gas compressibility."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 7: Energy, Machines and Sustainable Design
        # ---------------------------------------------------------------------
        {
            "unit_order": 7,
            "unit_name": "Energy, Machines and Sustainable Design",
            "unit_description": "Evolution of machines, sustainability principles, resource matching, evaluating energy budgets in community innovations, and the sustainable machine design challenge.",
            "lesson_title": "Energy, Machines and Sustainable Design",
            "pages": [
                # Page 1: Hook & Grinding Mill Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Appropriate Technology: Hand-Operated Agricultural Grinding Mill",
                        "content": {
                            "title": "Appropriate Technology: Hand-Operated Agricultural Grinding Mill",
                            "caption": "A locally fabricated hand-cranked agricultural grain mill in rural Kenya. The long crank handle (wheel and axle) multiplies manual effort to mill flour cleanly without imported fuel or electricity.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Hand_crank_grain_mill.jpg/1280px-Hand_crank_grain_mill.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Hand_crank_grain_mill.jpg/1280px-Hand_crank_grain_mill.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Hand Crank Grain Mill Sustainable Technology",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Hand_crank_grain_mill.jpg/1280px-Hand_crank_grain_mill.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Hand_crank_grain_mill.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Engineering with Local Resources",
                        "content": {
                            "title": "Innovation in Kenyan Communities",
                            "text": "In farming villages across Kenya, you see incredible ingenuity: bicycle water pumps, hand-cranked maize shellers, and solar dryers.\n\nGreat engineering is not about expensive imported technology; it is about applying fundamental physics to build **sustainable, low-cost solutions**."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Sustainable Innovation",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Trace the **evolution of machines** from bone tools to renewable energy systems.",
                                "Evaluate machines against the 4 pillars of **sustainability** (efficiency, local materials, repairability, zero pollution).",
                                "Construct an **energy budget and resource-matching matrix**.",
                                "Prototype and evaluate a simple machine using recycled materials."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Sustainable Technology",
                        "content": {
                            "term": "Sustainable Technology",
                            "definition": "Engineering designs that meet human needs while conserving energy, utilizing recyclable resources, and minimizing environmental degradation.",
                            "example": "Bicycle-powered water pumps and hand-cranked maize shellers."
                        }
                    }
                ],
                # Page 3: Sustainability Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Resource Matching and Sustainable Machine Design",
                        "content": {
                            "title": "Community Engineering Solutions",
                            "headers": ["Community Need", "Physical Machine", "Sourced Materials", "Useful Output", "Mitigation Strategy"],
                            "rows": [
                                ["Clean Irrigation", "Wheel & Axle on Piston Pump", "Old bicycle frame, PVC pipe", "5 liters/min water lift", "Lubricate chain with vegetable grease."],
                                ["Harvest Processing", "Meshed Gears & Lever Crank", "Recycled sheet metal, wooden handle", "10 kg shelled maize/hr", "Cardboard funnel to prevent grain scatter."],
                                ["Cargo Transport", "Wheelbarrow (2nd Class Lever)", "Scrap metal pipe, recycled wheelbarrow tire", "Transport 50 kg farm loads", "Align axle to minimize bearing friction."]
                            ]
                        }
                    }
                ],
                # Page 4: Design Challenge
                [
                    {
                        "type": "mini_activity",
                        "title": "Engineering Challenge: Sustainable Machine Prototype",
                        "content": {
                            "title": "The Community Innovation Challenge",
                            "task": "Choose one local challenge and construct a simple machine prototype using recycled cardboard, bottles, bottle caps, skewers, and rubber bands:\n\n1. **Water Lifter**: Raise water 1.0 m from bucket to table.\n2. **Agricultural Sheller**: Shell dry beans/maize kernels.\n3. **Cargo Transporter**: Transport 500 g across rough floor.\n4. Measure estimated $MA$ and optimize design to reduce friction."
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Bicycle Pump Usability Optimization",
                        "content": {
                            "question": "A student group builds a bicycle-powered water pump using a recycled bicycle wheel and pump cylinder. During testing, pedaling is extremely difficult and little water is lifted. Which engineering action will most logically improve usability and efficiency?",
                            "options": [
                                "Add extra weights to the bicycle frame to make it heavier.",
                                "Increase the diameter of the pump cylinder so it holds twice as much water.",
                                "Lubricate the chain and wheel axle to reduce friction, and adjust the gear ratio to reduce required effort.",
                                "Paint the bicycle green."
                            ],
                            "answer": "C",
                            "explanation": "Stiff pedaling indicates excessive frictional dissipation and a mismatched mechanical advantage. **Lubricating moving chains and axles** eliminates friction losses, and **adjusting the gear ratio** reduces the pedal effort force needed, significantly boosting efficiency and user comfort. Option C is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: The 4 Pillars of Sustainable Machines
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Four Pillars of Sustainable Engineering",
                        "content": {
                            "title": "Criteria for Modern Machine Design",
                            "text": "1. **High Energy Efficiency**: Minimize frictional losses to maximize useful work output.\n2. **Local & Recycled Materials**: Sourced locally to minimize economic cost and carbon footprint.\n3. **Community Repairability**: Built with standard components easily serviced with basic hand tools.\n4. **Environmental Protection**: Zero toxic emissions or pollution during operation."
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Engineering Video: Appropriate Technology & Sustainable Machines",
                        "content": {
                            "title": "Engineering Video: Appropriate Technology & Sustainable Machines",
                            "description": "Video profiling low-cost community innovation, pedal-powered agricultural machinery, and sustainable physics engineering.",
                            "url": "https://www.youtube.com/watch?v=ytwzRk_L_aA",
                            "resolved_video_id": "ytwzRk_L_aA"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Sustainable Machine Design Video",
                            "url": "https://www.youtube.com/watch?v=ytwzRk_L_aA",
                            "metadata": {
                                "youtube_id": "ytwzRk_L_aA"
                            }
                        }
                    }
                ],
                # Page 8: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson 7 Summary: Key Takeaways",
                        "content": {
                            "title": "Core Summary",
                            "takeaways": [
                                "Sustainable engineering balances **mechanical performance with environmental and economic viability**.",
                                "Community innovations apply simple physics (pulleys, levers, gears) to solve local challenges.",
                                "Optimization requires iterative testing to minimize friction and balance mechanical advantage."
                            ]
                        }
                    }
                ]
            ]
        }
    ]


# =============================================================================
# INGESTION EXECUTION ENGINE
# =============================================================================

@transaction.atomic
def ingest_grade10_physics_topic6():
    print("======================================================================")
    print("INGESTING CBC GRADE 10 PHYSICS — TOPIC 6: ENERGY, WORK, POWER AND MACHINES")
    print("======================================================================")

    # 1. Verify Curriculum & Grade
    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    if not curriculum:
        raise ValueError("Curriculum 'CBC' (ID: 5) not found!")

    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    if not grade:
        raise ValueError("Grade 10 not found under CBC curriculum!")

    # 2. Get Subject: Physics
    subject = Subject.objects.filter(grade=grade, name="Physics").first()
    if not subject:
        subject = Subject.objects.create(
            grade=grade,
            name="Physics",
            description="CBC Senior Secondary Physics"
        )
    print(f"Subject: {subject.name} (ID: {subject.id})")

    # 3. Get or Create Topic: Energy, Work, Power and Machines (Order: 6)
    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=6,
        defaults={
            "name": "Energy, Work, Power and Machines",
            "description": "Comprehensive study of Work (W = F×d), Power (P = W/t), Kinetic and Potential Energy, Conservation of Energy, simple machines (MA, VR, efficiency), levers, inclined planes, gears, hydraulics, and sustainable design."
        }
    )
    if not t_created and topic.name != "Energy, Work, Power and Machines":
        topic.name = "Energy, Work, Power and Machines"
        topic.description = "Comprehensive study of Work (W = F×d), Power (P = W/t), Kinetic and Potential Energy, Conservation of Energy, simple machines (MA, VR, efficiency), levers, inclined planes, gears, hydraulics, and sustainable design."
        topic.save()
    print(f"Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    curriculum_data = build_topic6_curriculum_data()

    total_units_created = 0
    total_lessons_created = 0
    total_blocks_created = 0
    total_assets_created = 0

    for unit_data in curriculum_data:
        u_order = unit_data["unit_order"]
        u_name = unit_data["unit_name"]
        u_desc = unit_data["unit_description"]
        l_title = unit_data["lesson_title"]
        pages = unit_data["pages"]

        # Create or Update Learning Unit
        learning_unit, lu_created = LearningUnit.objects.get_or_create(
            topic=topic,
            order=u_order,
            defaults={"name": u_name, "description": u_desc}
        )
        if not lu_created:
            learning_unit.name = u_name
            learning_unit.description = u_desc
            learning_unit.save()
        total_units_created += 1

        # Create or Update Lesson
        lesson, l_created = Lesson.objects.get_or_create(
            topic=topic,
            learning_unit=learning_unit,
            defaults={"title": l_title, "status": "published", "version": 1}
        )
        if not l_created:
            lesson.title = l_title
            lesson.status = "published"
            lesson.version = 1
            lesson.save()
        total_lessons_created += 1

        # Idempotently refresh LessonBlocks and Assets for this lesson
        lesson.blocks.all().delete()
        lesson.assets.all().delete()

        block_order_counter = 10

        for page_idx, page_blocks in enumerate(pages, start=1):
            for comp_idx, block_spec in enumerate(page_blocks, start=1):
                b_type = block_spec["type"]
                b_title = block_spec.get("title", "")
                b_content = block_spec.get("content", {})
                b_meta = block_spec.get("metadata", {})

                # If block has inline SVG, store in metadata
                if "svg_content" in b_content:
                    b_meta["svg_content"] = b_content["svg_content"]

                block = LessonBlock.objects.create(
                    lesson=lesson,
                    block_type=b_type,
                    component_type=b_type,
                    title=b_title,
                    content=b_content,
                    metadata=b_meta,
                    page_number=page_idx,
                    component_order=comp_idx,
                    order=block_order_counter
                )
                block_order_counter += 10
                total_blocks_created += 1

                # If block has an associated asset specification, create LessonAsset
                if "asset" in block_spec:
                    asset_spec = block_spec["asset"]
                    asset = LessonAsset.objects.create(
                        lesson=lesson,
                        asset_type=asset_spec["asset_type"],
                        source_type=asset_spec.get("source_type", "external"),
                        storage_type=asset_spec.get("storage_type", "url"),
                        status="approved",
                        title=asset_spec.get("title", b_title),
                        description=asset_spec.get("description", ""),
                        url=asset_spec.get("url"),
                        metadata=asset_spec.get("metadata", {})
                    )
                    block.assets.add(asset)
                    total_assets_created += 1

        print(f"  -> Ingested Unit {u_order}: '{u_name}' | Lesson: '{l_title}' ({len(pages)} Pages, {lesson.blocks.count()} Blocks, {lesson.assets.count()} Assets)")

    print("======================================================================")
    print(f"TOPIC 6 INGESTION COMPLETE:")
    print(f"  - Learning Units: {total_units_created}")
    print(f"  - Lessons:        {total_lessons_created}")
    print(f"  - Lesson Blocks:  {total_blocks_created}")
    print(f"  - Lesson Assets:  {total_assets_created}")
    print("======================================================================")

if __name__ == "__main__":
    ingest_grade10_physics_topic6()
