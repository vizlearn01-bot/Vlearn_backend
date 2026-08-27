"""
VLearn CBC Grade 10 Physics — Topic 5: Moments and Equilibrium
Production Ingestion & Visual Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Physics
Topic: Moments and Equilibrium (Order: 5)

6 Learning Units & 6 Published Lessons:
  1. Centre of Gravity and Centre of Mass Indicators (8 Pages, 13 Blocks)
  2. Moment of a Force About a Point (8 Pages, 13 Blocks)
  3. Principle of Moments and Equilibrium (8 Pages, 14 Blocks)
  4. Torque, Couples and Moments About Two Supports (8 Pages, 13 Blocks)
  5. Resolution of Forces and Stability (8 Pages, 14 Blocks)
  6. Applications and Design of Stable Structures (8 Pages, 13 Blocks)

Includes:
  - 10 Custom Responsive Sanitized Vector SVG Diagrams
  - 6 Verified Wikimedia Commons Photographic Assets
  - 6 Verified Educational YouTube Video Integrations
  - 6 Formative Scenario-Based MCQs with 4 Options and Pedagogical Feedback
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
# SVG DEFINITIONS FOR TOPIC 5
# =============================================================================

def get_svg_cog_regular_laminas():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">CENTRE OF GRAVITY (C.O.G.) IN UNIFORM REGULAR LAMINAS</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Symmetrical Geometric Shapes • C.O.G. Coincides with Geometric Centroid</text>

  <!-- 1. Rectangle (Diagonals) -->
  <g transform="translate(50, 80)">
    <rect width="210" height="260" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="105" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">RECTANGLE / SQUARE</text>

    <!-- Rectangular Cardboard -->
    <rect x="35" y="60" width="140" height="100" fill="#0284c722" stroke="#38bdf8" stroke-width="2"/>
    <line x1="35" y1="60" x2="175" y2="160" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 3"/>
    <line x1="35" y1="160" x2="175" y2="60" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 3"/>

    <!-- C.O.G. Point & Weight Vector -->
    <circle cx="105" cy="110" r="5" fill="#ef4444"/>
    <path d="M 105 110 L 105 150 M 99 142 L 105 150 L 111 142" stroke="#ef4444" stroke-width="2.5"/>
    <text x="115" y="140" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700">W</text>

    <text x="105" y="195" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Diagonal Intersection</text>
    <text x="105" y="215" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Midpoint of width & length</text>
  </g>

  <!-- 2. Circle (Diameters) -->
  <g transform="translate(315, 80)">
    <rect width="210" height="260" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="105" y="28" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">CIRCULAR DISC</text>

    <!-- Circular Plate -->
    <circle cx="105" cy="110" r="55" fill="#d9770622" stroke="#f59e0b" stroke-width="2"/>
    <line x1="50" y1="110" x2="160" y2="110" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 3"/>
    <line x1="105" y1="55" x2="105" y2="165" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 3"/>

    <!-- C.O.G. Point & Weight Vector -->
    <circle cx="105" cy="110" r="5" fill="#ef4444"/>
    <path d="M 105 110 L 105 150 M 99 142 L 105 150 L 111 142" stroke="#ef4444" stroke-width="2.5"/>
    <text x="115" y="140" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700">W</text>

    <text x="105" y="195" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Center of Circle</text>
    <text x="105" y="215" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Intersection of all diameters</text>
  </g>

  <!-- 3. Triangle (Medians) -->
  <g transform="translate(580, 80)">
    <rect width="210" height="260" rx="10" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
    <text x="105" y="28" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">TRIANGLE (CENTROID)</text>

    <!-- Triangular Plate -->
    <polygon points="105,55 45,155 165,155" fill="#16a34a22" stroke="#22c55e" stroke-width="2"/>
    <line x1="105" y1="55" x2="105" y2="155" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 3"/>
    <line x1="45" y1="155" x2="135" y2="105" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 3"/>
    <line x1="165" y1="155" x2="75" y2="105" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 3"/>

    <!-- Centroid C.O.G. Point & Weight Vector -->
    <circle cx="105" cy="122" r="5" fill="#ef4444"/>
    <path d="M 105 122 L 105 160 M 99 152 L 105 160 L 111 152" stroke="#ef4444" stroke-width="2.5"/>
    <text x="115" y="148" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700">W</text>

    <text x="105" y="195" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Intersection of Medians</text>
    <text x="105" y="215" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">1/3 height from base</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_cog_irregular_plumb_line():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%">
  <rect width="820" height="440" fill="#0f172a" rx="16"/>
  <text x="410" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">EXPERIMENT: DETERMINING C.O.G. OF AN IRREGULAR LAMINA</text>
  <text x="410" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Suspension & Plumb Line Method • Lines of Action from Pivot Points Intersect at C.O.G.</text>

  <!-- Retort Stand & Apparatus -->
  <g transform="translate(80, 80)">
    <!-- Stand Base -->
    <rect x="0" y="320" width="140" height="20" fill="#334155" rx="3"/>
    <!-- Vertical Rod -->
    <rect x="60" y="0" width="12" height="320" fill="#64748b"/>
    <!-- Clamp & Horizontal Pin -->
    <rect x="60" y="30" width="120" height="12" fill="#475569"/>
    <circle cx="170" cy="36" r="4" fill="#f59e0b"/> <!-- Pin pivot A -->
  </g>

  <!-- Irregular Cardboard Lamina Suspended from Hole A -->
  <g transform="translate(250, 110)">
    <!-- Asymmetrical Lamina Shape -->
    <path d="M 0 6 Q 120 -40 220 30 Q 300 120 250 220 Q 150 280 40 240 Q -50 180 0 6 Z" fill="#0284c722" stroke="#38bdf8" stroke-width="2.5"/>

    <!-- Hole A (Pivot) -->
    <circle cx="0" cy="6" r="5" fill="#f59e0b"/>
    <text x="-15" y="10" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Hole A</text>

    <!-- Hole B -->
    <circle cx="210" cy="40" r="5" fill="#38bdf8"/>
    <text x="225" y="45" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Hole B</text>

    <!-- Hole C -->
    <circle cx="50" cy="235" r="5" fill="#38bdf8"/>
    <text x="35" y="255" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Hole C</text>

    <!-- Line from Hole A (Vertical Plumb Line) -->
    <line x1="0" y1="6" x2="150" y2="260" stroke="#f59e0b" stroke-width="2" stroke-dasharray="5 3"/>
    
    <!-- Line from Hole B -->
    <line x1="210" y1="40" x2="-20" y2="170" stroke="#38bdf8" stroke-width="2" stroke-dasharray="5 3"/>

    <!-- Line from Hole C -->
    <line x1="50" y1="235" x2="160" y2="10" stroke="#22c55e" stroke-width="2" stroke-dasharray="5 3"/>

    <!-- Intersection C.O.G. Point -->
    <circle cx="88" cy="115" r="7" fill="#ef4444"/>
    <text x="100" y="115" fill="#ef4444" font-family="system-ui, sans-serif" font-size="13" font-weight="700">C.O.G. (Intersection)</text>

    <!-- Plumb Line Lead Bob Hanging in Front -->
    <line x1="0" y1="6" x2="0" y2="280" stroke="#f8fafc" stroke-width="1.5"/>
    <polygon points="-8,280 8,280 0,295" fill="#94a3b8" stroke="#f8fafc" stroke-width="1"/>
    <text x="12" y="290" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="10">Plumb Line Bob</text>
  </g>

  <!-- Explanatory Box on Right -->
  <g transform="translate(560, 95)">
    <rect width="220" height="200" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="110" y="26" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">PHYSICS PRINCIPLE</text>
    <text x="15" y="55" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">1. When freely suspended, an object rotates until its C.O.G. lies vertically below the pivot.</text>
    <text x="15" y="110" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">2. Plumb lines from 3 holes (A, B, C) intersect at a single unique balance point.</text>
    <text x="15" y="165" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3. Cardboard will balance on a pencil tip at C.O.G.!</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_moment_definition():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 400" width="100%" height="100%">
  <rect width="820" height="400" fill="#0f172a" rx="16"/>
  <text x="410" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">MOMENT OF A FORCE: TURNING EFFECT ABOUT A PIVOT</text>
  <text x="410" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Moment (M) = Force (F) × Perpendicular Distance (d) • SI Unit: Newton-meter (N m)</text>

  <!-- Horizontal Lever Bar -->
  <g transform="translate(100, 160)">
    <!-- Fixed Pivot Triangle at Left -->
    <polygon points="40,30 20,70 60,70" fill="#64748b" stroke="#94a3b8" stroke-width="1.5"/>
    <circle cx="40" cy="30" r="5" fill="#f59e0b"/>
    <text x="40" y="90" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Pivot (P)</text>

    <!-- Horizontal Beam -->
    <rect x="40" y="20" width="500" height="20" rx="3" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>

    <!-- Applied Downward Force F at Right End -->
    <path d="M 540 30 L 540 140 M 530 128 L 540 140 L 550 128" stroke="#ef4444" stroke-width="4"/>
    <text x="560" y="100" fill="#ef4444" font-family="system-ui, sans-serif" font-size="15" font-weight="700">Force F (N)</text>

    <!-- Perpendicular Distance Dimension Bracket -->
    <line x1="40" y1="-20" x2="540" y2="-20" stroke="#f59e0b" stroke-width="2"/>
    <path d="M 40 -26 L 40 -14 M 540 -26 L 540 -14" stroke="#f59e0b" stroke-width="2"/>
    <text x="290" y="-30" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Perpendicular Distance (d)</text>

    <!-- Curved Clockwise Moment Arrow -->
    <path d="M 80 -10 Q 120 -30 140 10" fill="none" stroke="#38bdf8" stroke-width="3"/>
    <polygon points="140,10 145,0 135,2" fill="#38bdf8"/>
    <text x="130" y="-15" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Clockwise Moment</text>
  </g>

  <!-- Formula Callout Box -->
  <g transform="translate(180, 290)">
    <rect width="460" height="75" rx="10" fill="#1e293b" stroke="#22c55e" stroke-width="2"/>
    <text x="230" y="32" fill="#4ade80" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">M = F × d</text>
    <text x="230" y="55" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Doubling distance (d) doubles turning effect with the exact same effort force</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_seesaw_moments():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">THE PRINCIPLE OF MOMENTS: ROTATIONAL EQUILIBRIUM</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Sum of Clockwise Moments = Sum of Anticlockwise Moments (Σ M_cw = Σ M_acw)</text>

  <!-- Balanced Meter Rule Seesaw -->
  <g transform="translate(100, 150)">
    <!-- Central Pivot Triangle -->
    <polygon points="320,40 300,90 340,90" fill="#64748b" stroke="#94a3b8" stroke-width="1.5"/>
    <circle cx="320" cy="40" r="5" fill="#f59e0b"/>
    <text x="320" y="110" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Pivot (50 cm)</text>

    <!-- Horizontal Balanced Beam -->
    <rect x="20" y="30" width="600" height="20" rx="3" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>

    <!-- Left Load: 50 N at 40 cm distance (10 cm mark) -->
    <rect x="65" y="50" width="30" height="25" rx="3" fill="#38bdf8" stroke="#0284c7" stroke-width="1.5"/>
    <text x="80" y="67" fill="#000000" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">50 N</text>
    <path d="M 80 75 L 80 115 M 74 107 L 80 115 L 86 107" stroke="#38bdf8" stroke-width="3"/>
    
    <line x1="80" y1="10" x2="320" y2="10" stroke="#38bdf8" stroke-width="1.5"/>
    <path d="M 80 6 L 80 14 M 320 6 L 320 14" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="200" y="0" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">d1 = 40 cm (0.40 m)</text>

    <!-- Right Load: 100 N at 20 cm distance (70 cm mark) -->
    <rect x="425" y="50" width="30" height="35" rx="3" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
    <text x="440" y="72" fill="#000000" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">100 N</text>
    <path d="M 440 85 L 440 125 M 434 117 L 440 125 L 446 117" stroke="#f59e0b" stroke-width="3"/>

    <line x1="320" y1="10" x2="440" y2="10" stroke="#f59e0b" stroke-width="1.5"/>
    <path d="M 320 6 L 320 14 M 440 6 L 440 14" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="380" y="0" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">d2 = 20 cm (0.20 m)</text>
  </g>

  <!-- Equilibrium Proof Calculation Box -->
  <g transform="translate(140, 290)">
    <rect width="560" height="85" rx="10" fill="#1e293b" stroke="#22c55e" stroke-width="2"/>
    <text x="140" y="32" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Anticlockwise Moment:</text>
    <text x="140" y="58" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">50 N × 0.40 m = 20 N m</text>

    <text x="280" y="45" fill="#4ade80" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">=</text>

    <text x="420" y="32" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Clockwise Moment:</text>
    <text x="420" y="58" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">100 N × 0.20 m = 20 N m</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_couple_torque():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 420" width="100%" height="100%">
  <rect width="820" height="420" fill="#0f172a" rx="16"/>
  <text x="410" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">TORQUE OF A COUPLE: PURE ROTATION WITHOUT TRANSLATION</text>
  <text x="410" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Two Equal, Opposite, Parallel Forces • Torque (T) = Force (F) × Perpendicular Separation (s)</text>

  <!-- Steering Wheel Schematic -->
  <g transform="translate(230, 90)">
    <!-- Outer Wheel Rim -->
    <circle cx="180" cy="130" r="110" fill="#1e293b" stroke="#94a3b8" stroke-width="16"/>
    <!-- Central Hub -->
    <circle cx="180" cy="130" r="25" fill="#334155" stroke="#38bdf8" stroke-width="2"/>
    <!-- Spokes -->
    <line x1="180" y1="45" x2="180" y2="215" stroke="#64748b" stroke-width="6"/>
    <line x1="95" y1="130" x2="265" y2="130" stroke="#64748b" stroke-width="6"/>

    <!-- Left Force: 30 N Upward -->
    <path d="M 70 130 L 70 40 M 64 50 L 70 40 L 76 50" stroke="#38bdf8" stroke-width="4"/>
    <text x="50" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700">F = 30 N (Up)</text>

    <!-- Right Force: 30 N Downward -->
    <path d="M 290 130 L 290 220 M 284 210 L 290 220 L 296 210" stroke="#f59e0b" stroke-width="4"/>
    <text x="305" y="235" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="700">F = 30 N (Down)</text>

    <!-- Separation s Dimension Line -->
    <line x1="70" y1="130" x2="290" y2="130" stroke="#22c55e" stroke-width="2" stroke-dasharray="4 3"/>
    <text x="180" y="120" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Separation s = 0.40 m</text>
  </g>

  <!-- Calculation Banner -->
  <g transform="translate(150, 320)">
    <rect width="520" height="70" rx="8" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
    <text x="260" y="28" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">T = F × s = 30 N × 0.40 m = 12 N m (Clockwise)</text>
    <text x="260" y="52" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Resultant linear force = 30 N - 30 N = 0 N (No stress on central steering bearing!)</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_bridge_supports():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">MOMENTS ON TWO SUPPORTS: REACTION FORCES (BRIDGES)</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Conditions of Equilibrium: Upward Forces = Downward Forces • Sum of Moments About Pivot = 0</text>

  <!-- Supported Bridge Beam Schematic -->
  <g transform="translate(100, 130)">
    <!-- Support Pillar A (Left) -->
    <rect x="30" y="60" width="40" height="70" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
    <path d="M 50 60 L 50 10 M 44 20 L 50 10 L 56 20" stroke="#38bdf8" stroke-width="4"/>
    <text x="50" y="0" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">RA = 550 N</text>

    <!-- Support Pillar B (Right) -->
    <rect x="570" y="60" width="40" height="70" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
    <path d="M 590 60 L 590 10 M 584 20 L 590 10 L 596 20" stroke="#f59e0b" stroke-width="4"/>
    <text x="590" y="0" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">RB = 250 N</text>

    <!-- Horizontal Bridge Plank (4.0 m) -->
    <rect x="30" y="45" width="580" height="20" rx="3" fill="#1e293b" stroke="#f8fafc" stroke-width="2"/>

    <!-- Load 1: Painter (600 N at 1.0 m from A) -->
    <path d="M 185 45 L 185 125 M 179 115 L 185 125 L 191 115" stroke="#ef4444" stroke-width="3"/>
    <text x="185" y="145" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Painter = 600 N</text>

    <!-- Load 2: Plank Weight (200 N at center 2.0 m from A) -->
    <path d="M 320 45 L 320 115 M 314 105 L 320 115 L 326 105" stroke="#ef4444" stroke-width="2.5"/>
    <text x="320" y="135" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">W_plank = 200 N</text>
  </g>

  <!-- Equilibrium Balance Equation Box -->
  <g transform="translate(120, 285)">
    <rect width="600" height="85" rx="10" fill="#1e293b" stroke="#22c55e" stroke-width="2"/>
    <text x="300" y="28" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. Moments about A: RB × 4.0 m = (600 N × 1.0 m) + (200 N × 2.0 m) = 1000 N m ⟹ RB = 250 N</text>
    <text x="300" y="55" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">2. Vertical Forces: RA + RB = 600 N + 200 N = 800 N ⟹ RA = 550 N</text>
    <text x="300" y="74" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Support A carries a larger share of weight because the painter is closer to it.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_equilibrium_states():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">THE THREE STATES OF EQUILIBRIUM: STABLE, UNSTABLE, NEUTRAL</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Behavior Under Small Angular Displacement • Height Change of Centre of Gravity</text>

  <!-- 1. Stable Equilibrium -->
  <g transform="translate(50, 80)">
    <rect width="210" height="285" rx="10" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
    <text x="105" y="28" fill="#22c55e" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">1. STABLE</text>

    <!-- Cone resting on broad base -->
    <polygon points="105,70 50,170 160,170" fill="#16a34a33" stroke="#22c55e" stroke-width="2"/>
    <circle cx="105" cy="140" r="5" fill="#ef4444"/>
    <text x="105" y="130" fill="#ef4444" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">C.O.G.</text>

    <text x="105" y="200" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Returns to Base</text>
    <text x="105" y="220" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">When tilted slightly:</text>
    <text x="105" y="240" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">C.O.G. RISES</text>
    <text x="105" y="260" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Restoring moment pulls it back</text>
  </g>

  <!-- 2. Unstable Equilibrium -->
  <g transform="translate(315, 80)">
    <rect width="210" height="285" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="105" y="28" fill="#ef4444" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">2. UNSTABLE</text>

    <!-- Cone balanced on sharp tip -->
    <polygon points="105,170 50,70 160,70" fill="#ef444433" stroke="#ef4444" stroke-width="2"/>
    <circle cx="105" cy="100" r="5" fill="#ef4444"/>
    <text x="105" y="90" fill="#ef4444" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">C.O.G.</text>

    <text x="105" y="200" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Topples Over</text>
    <text x="105" y="220" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">When tilted slightly:</text>
    <text x="105" y="240" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">C.O.G. FALLS</text>
    <text x="105" y="260" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Overturning moment accelerates fall</text>
  </g>

  <!-- 3. Neutral Equilibrium -->
  <g transform="translate(580, 80)">
    <rect width="210" height="285" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="105" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">3. NEUTRAL</text>

    <!-- Cone lying on sloped side -->
    <polygon points="50,170 160,170 135,100" fill="#0284c733" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="115" cy="147" r="5" fill="#ef4444"/>
    <text x="115" y="137" fill="#ef4444" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">C.O.G.</text>

    <text x="105" y="200" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Stays in New Position</text>
    <text x="105" y="220" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">When rolled or pushed:</text>
    <text x="105" y="240" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">C.O.G. HEIGHT UNCHANGED</text>
    <text x="105" y="260" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Zero restoring or toppling moment</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_crane_moments():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 420" width="100%" height="100%">
  <rect width="840" height="420" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">TOWER CRANE COUNTERWEIGHT MOMENT BALANCING SCHEMATIC</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Balancing Moments to Prevent Toppling • Counterweight Moment = Maximum Safe Load Moment</text>

  <!-- Crane Structure -->
  <g transform="translate(100, 80)">
    <!-- Base Foundation -->
    <rect x="180" y="230" width="100" height="20" fill="#334155" stroke="#94a3b8" stroke-width="1.5" rx="3"/>
    <!-- Vertical Mast -->
    <rect x="220" y="40" width="20" height="190" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>

    <!-- Horizontal Jib Beam -->
    <rect x="40" y="40" width="580" height="15" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>

    <!-- Left: Short Counterweight Arm (10 m) -->
    <rect x="40" y="55" width="50" height="40" fill="#64748b" stroke="#94a3b8" stroke-width="1.5" rx="3"/>
    <text x="65" y="78" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">100,000 N</text>
    <path d="M 65 95 L 65 140 M 59 130 L 65 140 L 71 130" stroke="#38bdf8" stroke-width="3"/>

    <line x1="65" y1="20" x2="230" y2="20" stroke="#38bdf8" stroke-width="1.5"/>
    <path d="M 65 16 L 65 24 M 230 16 L 230 24" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="145" y="12" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">d_C = 10 m</text>

    <!-- Right: Long Load Jib (40 m) -->
    <rect x="580" y="55" width="25" height="25" fill="#ef4444" stroke="#dc2626" stroke-width="1.5" rx="2"/>
    <text x="592" y="72" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">W</text>
    <path d="M 592 80 L 592 140 M 586 130 L 592 140 L 598 130" stroke="#ef4444" stroke-width="3"/>

    <line x1="230" y1="20" x2="592" y2="20" stroke="#ef4444" stroke-width="1.5"/>
    <path d="M 230 16 L 230 24 M 592 16 L 592 24" stroke="#ef4444" stroke-width="1.5"/>
    <text x="410" y="12" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">d_L = 40 m</text>
  </g>

  <!-- Crane Moment Equilibrium Equation Box -->
  <g transform="translate(100, 310)">
    <rect width="640" height="75" rx="8" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
    <text x="320" y="28" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Counterweight Moment (Anticlockwise) = Maximum Safe Load Moment (Clockwise)</text>
    <text x="320" y="50" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">100,000 N × 10 m = W × 40 m ⟹ 1,000,000 N m = 40 W ⟹ Maximum Safe Load W = 25,000 N</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg


# =============================================================================
# CURRICULUM DEFINITION DATA FOR TOPIC 5
# =============================================================================

def build_topic5_curriculum_data():
    return [
        # ---------------------------------------------------------------------
        # LESSON 1: Centre of Gravity and Centre of Mass Indicators
        # ---------------------------------------------------------------------
        {
            "unit_order": 1,
            "unit_name": "Centre of Gravity and Centre of Mass Indicators",
            "unit_description": "Definition of Centre of Gravity (C.O.G.) and Centre of Mass, finding C.O.G. in regular symmetrical laminas and irregular laminas using the plumb line suspension method, and vehicle stability.",
            "lesson_title": "Centre of Gravity and Centre of Mass Indicators",
            "pages": [
                # Page 1: Hook & Gymnast Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Athletic Equilibrium: Gymnast Aligning C.O.G. on Narrow Beam",
                        "content": {
                            "title": "Athletic Equilibrium: Gymnast Aligning C.O.G. on Narrow Beam",
                            "caption": "A gymnast executing a handstand balance on a narrow beam. The athlete maintains stability by aligning her Centre of Gravity directly vertically above the narrow contact base.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Gymnast_handstand_balance.jpg/1280px-Gymnast_handstand_balance.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Gymnast_handstand_balance.jpg/1280px-Gymnast_handstand_balance.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Gymnast Balance and Centre of Gravity",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Gymnast_handstand_balance.jpg/1280px-Gymnast_handstand_balance.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Gymnast_handstand_balance.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Magic Balance Point of Objects",
                        "content": {
                            "title": "Balancing on a Single Point",
                            "text": "Have you ever tried balancing a meter rule on your fingertip?\n\n- If your finger is near one end, the rule falls instantly.\n- But if you place your finger precisely under the $50\\text{ cm}$ midpoint, the entire rule balances effortlessly!\n\nThis single point through which the entire weight of the body acts is the **Centre of Gravity (C.O.G.)**."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Centre of Gravity",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **Centre of Gravity (C.O.G.)** and **Centre of Mass**.",
                                "Locate the C.O.G. of **regular symmetrical laminas** (rectangles, circles, triangles).",
                                "Determine the C.O.G. of an **irregular lamina** experimentally using the plumb line suspension method.",
                                "Explain how C.O.G. height affects vehicle rollover stability."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Centre of Gravity (C.O.G.)",
                        "content": {
                            "term": "Centre of Gravity (C.O.G.)",
                            "definition": "The single point through which the entire gravitational weight of an object appears to act, regardless of its orientation.",
                            "example": "The C.O.G. of a uniform meter rule is located at its 50 cm geometric midpoint."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Centre of Mass",
                        "content": {
                            "term": "Centre of Mass",
                            "definition": "The unique point where the entire mass of an object is concentrated. In uniform gravity on Earth, it coincides exactly with the Centre of Gravity.",
                            "example": "A spinning hammer rotates around its centre of mass as it flies through the air."
                        }
                    }
                ],
                # Page 3: C.O.G. of Regular Laminas SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Centre of Gravity in Uniform Regular Symmetrical Laminas",
                        "content": {
                            "title": "Centre of Gravity in Uniform Regular Symmetrical Laminas",
                            "caption": "Geometric centroids representing C.O.G. in a rectangle (diagonal intersection), circle (center of diameters), and triangle (median intersection at 1/3 height from base).",
                            "svg_content": get_svg_cog_regular_laminas(),
                            "svg": get_svg_cog_regular_laminas()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Regular Laminas Centre of Gravity Diagram",
                            "metadata": {
                                "svg_content": get_svg_cog_regular_laminas()
                            }
                        }
                    }
                ],
                # Page 4: Plumb Line Experiment & SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Suspension Method for Irregular Laminas",
                        "content": {
                            "title": "Suspension Method for Irregular Laminas",
                            "caption": "Irregular cardboard lamina freely suspended from pin hole A with a plumb line. Vertical balance lines drawn from holes A, B, and C intersect at the unique Centre of Gravity.",
                            "svg_content": get_svg_cog_irregular_plumb_line(),
                            "svg": get_svg_cog_irregular_plumb_line()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Irregular Lamina Plumb Line Experiment Diagram",
                            "metadata": {
                                "svg_content": get_svg_cog_irregular_plumb_line()
                            }
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Laboratory Protocol: Finding C.O.G. of an Irregular Lamina",
                        "content": {
                            "title": "Plumb Line Suspension Method Protocol",
                            "steps": [
                                "1. Punch 3 small, clean holes (A, B, C) near the outer edges of the irregular cardboard.",
                                "2. Suspend the cardboard freely from hole A on a horizontal pin clamped to a retort stand.",
                                "3. Hang a plumb line from the same pin so it hangs vertically in front of the cardboard.",
                                "4. Draw a straight pencil line along the plumb line string from hole A.",
                                "5. Repeat from hole B and hole C. The point where all 3 lines intersect is the **Centre of Gravity**.",
                                "6. **Verification**: Place the cardboard horizontally on a pencil tip at the intersection point; it balances in equilibrium!"
                            ]
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Friction in the Suspension Method",
                        "content": {
                            "question": "When finding the Centre of Gravity of an irregular cardboard sheet using the plumb line suspension method, why is it essential that the cardboard can swing completely freely on the pivot pin?",
                            "options": [
                                "To allow the cardboard to accelerate rapidly under gravity.",
                                "To ensure friction does not prevent the cardboard from rotating until its C.O.G. is directly vertically below the pivot.",
                                "To prevent the retort stand from tipping over.",
                                "To allow the plumb line bob to touch the floor."
                            ],
                            "answer": "B",
                            "explanation": "When an object hangs freely from a pivot, gravity pulls downward on its C.O.G., generating a turning moment until the C.O.G. is aligned **directly below the pivot pin**. If there is friction, the cardboard will get stuck prematurely before reaching true vertical alignment. Therefore, Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Real-World Vehicle Stability
                [
                    {
                        "type": "real_world_connection",
                        "title": "Real-World Engineering: Load Distribution and C.O.G. in Vehicles",
                        "content": {
                            "title": "Preventing Rollover Accidents in Matatus and Lorries",
                            "text": "- **Luggage Placement**: Heavy cargo in buses and matatus must always be placed in low under-floor luggage lockers rather than high roof racks. Placing heavy loads on roof racks elevates the vehicle's C.O.G., making it dangerously prone to toppling on sharp bends.\n- **Sailboat Keels**: Sailing boats have heavy lead keels at the bottom of the hull, keeping the C.O.G. low so the boat rights itself automatically when tilted by strong winds."
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Finding Centre of Gravity and Vehicle Rollover Safety",
                        "content": {
                            "title": "Physics Video: Finding Centre of Gravity and Vehicle Rollover Safety",
                            "description": "Demonstration of the plumb line method for irregular laminas, centroid geometry, and automotive tilt table rollover testing.",
                            "url": "https://www.youtube.com/watch?v=XQnOq7U4cWc",
                            "resolved_video_id": "XQnOq7U4cWc"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Centre of Gravity and Vehicle Rollover Video",
                            "url": "https://www.youtube.com/watch?v=XQnOq7U4cWc",
                            "metadata": {
                                "youtube_id": "XQnOq7U4cWc"
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
                                "**Centre of Gravity (C.O.G.)** is the point through which the entire weight of a body acts.",
                                "For **uniform symmetrical objects**, C.O.G. is at the geometric centroid.",
                                "For **irregular laminas**, C.O.G. is found at the intersection of lines from the **suspension method**.",
                                "Lowering the C.O.G. improves the stability of vehicles and structures."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 2: Moment of a Force About a Point
        # ---------------------------------------------------------------------
        {
            "unit_order": 2,
            "unit_name": "Moment of a Force About a Point",
            "unit_description": "Defining the turning effect of a force, mathematical formula M = F × d, perpendicular distance from pivot, SI unit Newton-meter (N m), and spanner leverage.",
            "lesson_title": "Moment of a Force About a Point",
            "pages": [
                # Page 1: Hook & Spanner Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Leverage in Mechanical Work: Loosening Lug Nuts with a Long Spanner",
                        "content": {
                            "title": "Leverage in Mechanical Work: Loosening Lug Nuts with a Long Spanner",
                            "caption": "A vehicle mechanic using a long steel spanner to loosen a tight wheel nut. Applying force far from the nut pivot maximizes the turning moment with minimal effort.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Wrench_tightening_lug_nut.jpg/1280px-Wrench_tightening_lug_nut.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Wrench_tightening_lug_nut.jpg/1280px-Wrench_tightening_lug_nut.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Mechanic Using Long Spanner for Turning Moment",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Wrench_tightening_lug_nut.jpg/1280px-Wrench_tightening_lug_nut.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Wrench_tightening_lug_nut.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Are Door Handles Placed Far From Hinges?",
                        "content": {
                            "title": "The Turning Effect of Forces",
                            "text": "Try pushing a heavy door open by pressing right next to its hinges:\n\n- It requires immense muscular effort to budge.\n- But push near the outer edge by the door handle, and the door opens effortlessly!\n\nThe turning effect produced by a force is called its **Moment**."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Moments",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define the **Moment of a force** and state its SI unit (**Newton-meter, N m**).",
                                "Apply the mathematical formula $M = F \\times d$ using perpendicular distance.",
                                "Explain why forces passing directly through a pivot produce zero moment.",
                                "Solve real-world problems involving door handles, spanners, and levers."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Moment of a Force",
                        "content": {
                            "term": "Moment of a Force",
                            "definition": "The measure of the turning or rotational effect of a force about a pivot point ($M = F \\times d$).",
                            "example": "A 25 N force applied 0.8 m from hinges produces a 20 N m moment."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Perpendicular Distance (d)",
                        "content": {
                            "term": "Perpendicular Distance (d)",
                            "definition": "The shortest straight-line distance from the pivot point to the line of action of the applied force.",
                            "example": "Measured at a 90° right angle from the pivot to the force vector line."
                        }
                    }
                ],
                # Page 3: Moment Formula & SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Moment of a Force About a Pivot Diagram",
                        "content": {
                            "title": "Moment of a Force About a Pivot Diagram",
                            "caption": "Horizontal lever bar showing pivot P, downward force F, perpendicular distance d, and clockwise moment M = F × d.",
                            "svg_content": get_svg_moment_definition(),
                            "svg": get_svg_moment_definition()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Moment of a Force Formula Diagram",
                            "metadata": {
                                "svg_content": get_svg_moment_definition()
                            }
                        }
                    },
                    {
                        "type": "formula_breakdown",
                        "title": "Moment Equation",
                        "content": {
                            "title": "The Turning Effect Equation",
                            "formula": "M = F \\times d",
                            "variables": [
                                "$M$ = Moment in Newton-meters ($\\text{N m}$)",
                                "$F$ = Applied Force in Newtons ($\\text{N}$)",
                                "$d$ = Perpendicular distance from pivot in metres ($\\text{m}$)"
                            ],
                            "rules": [
                                "**Unit Caution**: Do NOT write $\\text{N m}$ as Joules ($\\text{J}$); Joules are strictly reserved for work and energy.",
                                "**Zero Moment**: A force acting directly through the pivot ($d = 0$) creates zero turning effect."
                            ]
                        }
                    }
                ],
                # Page 4: Worked Examples
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Door Handle & Spanner Moments",
                        "content": {
                            "title": "Calculating Turning Moments",
                            "problem": "1. A person pushes a door handle located $0.8\\text{ m}$ from the hinges with a perpendicular force of $25\\text{ N}$. Calculate the moment.\n2. A mechanic uses a $25\\text{ cm}$ spanner with an $80\\text{ N}$ force. Calculate the moment exerted on the nut.",
                            "steps": [
                                "1. **Door Handle**: $M = F \\times d = 25\\text{ N} \\times 0.8\\text{ m} = 20\\text{ N m}$.",
                                "2. **Spanner Conversion**: Convert $25\\text{ cm}$ to metres: $d = 0.25\\text{ m}$.",
                                "3. **Spanner Moment**: $M = 80\\text{ N} \\times 0.25\\text{ m} = 20\\text{ N m}$."
                            ],
                            "answer": "Both produce a turning moment of 20 N m."
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Spanner Leverage",
                        "content": {
                            "question": "A student applies a perpendicular force of $50\\text{ N}$ to a spanner at a distance of $10\\text{ cm}$ from a tight nut, producing a moment of $5\\text{ N m}$. If they slide their hand back to $20\\text{ cm}$ from the nut and pull with the same $50\\text{ N}$ force, how does the turning moment change?",
                            "options": [
                                "The moment remains 5 N m because the force is unchanged.",
                                "The moment decreases to 2.5 N m.",
                                "The moment doubles to 10 N m, making it twice as effective.",
                                "The moment quadruples to 20 N m."
                            ],
                            "answer": "C",
                            "explanation": "Moment is directly proportional to perpendicular distance ($M = F \\times d$). Doubling the distance from $0.10\\text{ m}$ to $0.20\\text{ m}$ doubles the turning moment from $5\\text{ N m}$ to $10\\text{ N m}$ ($50 \\times 0.20 = 10\\text{ N m}$). Therefore, Option C is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Daily Turning Applications
                [
                    {
                        "type": "real_world_connection",
                        "title": "Everyday Turning Moments",
                        "content": {
                            "title": "Moments in Everyday Mechanisms",
                            "text": "- **Steering Wheel**: Turning the large outer rim applies force at radius $R$ from the steering column pivot.\n- **Bicycle Pedals**: Pushing down on the pedal rotates the chain ring around the bottom bracket axle.\n- **Wheelbarrow**: Lifting the long handles applies upward effort far from the front wheel pivot to raise heavy loads easily."
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Moments, Levers, and Turning Effects",
                        "content": {
                            "title": "Physics Video: Moments, Levers, and Turning Effects",
                            "description": "Visual lesson explaining the physics of moments, perpendicular distance, and practical lever applications in construction and daily life.",
                            "url": "https://www.youtube.com/watch?v=kYJvI8oE2yA",
                            "resolved_video_id": "kYJvI8oE2yA"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Moments and Turning Effects Physics Video",
                            "url": "https://www.youtube.com/watch?v=kYJvI8oE2yA",
                            "metadata": {
                                "youtube_id": "kYJvI8oE2yA"
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
                                "A **Moment** is the turning effect of a force: **$M = F \\times d$** (SI unit: $\\text{N m}$).",
                                "Distance $d$ must be **perpendicular** from the pivot to the line of action of the force.",
                                "Increasing distance from the pivot produces greater turning effect with the same force."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 3: Principle of Moments and Equilibrium
        # ---------------------------------------------------------------------
        {
            "unit_order": 3,
            "unit_name": "Principle of Moments and Equilibrium",
            "unit_description": "Rotational equilibrium, clockwise and anticlockwise moments, the Principle of Moments (Σ M_cw = Σ M_acw), meter rule balance investigations, and non-uniform beam calculations.",
            "lesson_title": "Principle of Moments and Equilibrium",
            "pages": [
                # Page 1: Hook & Market Scale Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Precision Balance: Dual-Pan Market Scale in Rotational Equilibrium",
                        "content": {
                            "title": "Precision Balance: Dual-Pan Market Scale in Rotational Equilibrium",
                            "caption": "A dual-pan beam balance scale used in a market. When the clockwise moment from brass weights equals the anticlockwise moment from dry goods, the beam settles in horizontal equilibrium.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Traditional_balance_scale.jpg/1280px-Traditional_balance_scale.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Traditional_balance_scale.jpg/1280px-Traditional_balance_scale.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Dual Pan Balance Scale in Equilibrium",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Traditional_balance_scale.jpg/1280px-Traditional_balance_scale.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Traditional_balance_scale.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "How a Light Person Balances a Heavy Person on a Seesaw",
                        "content": {
                            "title": "Balancing Turning Effects",
                            "text": "Have you ever played on a seesaw with a friend much heavier than you?\n\n- If you both sit at the same distance, the seesaw tilts to their side.\n- But if your heavier friend slides closer to the center pivot, suddenly the seesaw balances horizontally!\n\nThis is governed by the **Principle of Moments**."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Principle of Moments",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "State the **Principle of Moments** for a body in rotational equilibrium.",
                                "Distinguish between **clockwise** and **anticlockwise** moments.",
                                "Verify the Principle of Moments experimentally using a suspended meter rule.",
                                "Solve quantitative equilibrium problems, including accounting for the beam's own weight at its C.O.G."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Rotational Equilibrium",
                        "content": {
                            "term": "Rotational Equilibrium",
                            "definition": "The state of a body where the sum of clockwise moments about any point equals the sum of anticlockwise moments about that same point ($\\sum M_{\\text{cw}} = \\sum M_{\\text{acw}}$).",
                            "example": "A balanced horizontal seesaw or weighing scale."
                        }
                    }
                ],
                # Page 3: Principle of Moments Formula & Seesaw SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Principle of Moments on a Balanced Seesaw",
                        "content": {
                            "title": "The Principle of Moments on a Balanced Seesaw",
                            "caption": "Balanced meter rule showing 50 N at 40 cm (anticlockwise 20 N m) balanced by 100 N at 20 cm (clockwise 20 N m), proving Σ M_cw = Σ M_acw.",
                            "svg_content": get_svg_seesaw_moments(),
                            "svg": get_svg_seesaw_moments()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Principle of Moments Seesaw Diagram",
                            "metadata": {
                                "svg_content": get_svg_seesaw_moments()
                            }
                        }
                    },
                    {
                        "type": "formula_breakdown",
                        "title": "The Principle of Moments",
                        "content": {
                            "title": "Law of Rotational Balance",
                            "formula": "\\sum M_{\\text{clockwise}} = \\sum M_{\\text{anticlockwise}} \\implies F_1 \\times d_1 = F_2 \\times d_2",
                            "variables": [
                                "$F_1, F_2$ = Opposing forces in Newtons ($\\text{N}$)",
                                "$d_1, d_2$ = Respective perpendicular distances from the pivot in metres ($\\text{m}$)"
                            ],
                            "rules": [
                                "**Law Statement**: When a body is in rotational equilibrium, the total clockwise moments about any pivot point equal the total anticlockwise moments about that same point."
                            ]
                        }
                    }
                ],
                # Page 4: Worked Example (Factoring in Beam Weight)
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Finding the Weight of a Uniform Rod",
                        "content": {
                            "title": "Factoring in Beam Weight at C.O.G.",
                            "problem": "A uniform half-meter rod ($50\\text{ cm}$ long) balances at its $25\\text{ cm}$ mark. When a weight of $12\\text{ N}$ is hung at the $10\\text{ cm}$ mark, the rod balances on a pivot placed at the $20\\text{ cm}$ mark. Calculate the weight ($W$) of the rod.",
                            "steps": [
                                "1. **Left Anticlockwise Force**: $F_1 = 12\\text{ N}$ at $10\\text{ cm}$ mark (distance to pivot $d_1 = 20 - 10 = 10\\text{ cm} = 0.10\\text{ m}$).",
                                "2. **Right Clockwise Force (Rod Weight)**: Weight $W$ acts at $25\\text{ cm}$ C.O.G. (distance to pivot $d_w = 25 - 20 = 5\\text{ cm} = 0.05\\text{ m}$).",
                                "3. **Set Up Moments Equation**: $\\text{Anticlockwise Moments} = \\text{Clockwise Moments} \\implies 12\\text{ N} \\times 0.10\\text{ m} = W \\times 0.05\\text{ m}$.",
                                "4. **Solve for W**: $1.2 = 0.05W \\implies W = \\frac{1.2}{0.05} = 24\\text{ N}$."
                            ],
                            "answer": "The weight of the rod is 24 N."
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Predicting Beam Tilt",
                        "content": {
                            "question": "A uniform $1\\text{ m}$ ruler is pivoted at its $50\\text{ cm}$ center. A $2\\text{ N}$ weight is placed at the $10\\text{ cm}$ mark (distance $40\\text{ cm}$ from pivot), and a $3\\text{ N}$ weight is placed at the $80\\text{ cm}$ mark (distance $30\\text{ cm}$ from pivot). What will happen to the ruler?",
                            "options": [
                                "It remains in horizontal equilibrium.",
                                "It tilts anticlockwise because the 2 N weight is further from the pivot.",
                                "It tilts clockwise because the clockwise moment (0.9 N m) is greater than the anticlockwise moment (0.8 N m).",
                                "It accelerates upward off the pivot."
                            ],
                            "answer": "C",
                            "explanation": "Calculate moments about the 50 cm pivot: Anticlockwise moment = $2\\text{ N} \\times 0.40\\text{ m} = 0.8\\text{ N m}$. Clockwise moment = $3\\text{ N} \\times 0.30\\text{ m} = 0.9\\text{ N m}$. Since clockwise moment ($0.9\\text{ N m}$) exceeds anticlockwise moment ($0.8\\text{ N m}$), the ruler tilts **clockwise**. Option C is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Practical Investigation
                [
                    {
                        "type": "mini_activity",
                        "title": "Laboratory Investigation: Verifying Principle of Moments",
                        "content": {
                            "title": "Balancing Slotted Masses on a Meter Rule",
                            "task": "Balance a meter rule at its 50 cm mark. Hang a $1\\text{ N}$ mass at $30\\text{ cm}$ from pivot (left) and slide a $2\\text{ N}$ mass along the right side until horizontal balance is restored (observed at $15\\text{ cm}$ from pivot). Verify $1\\text{ N} \\times 0.30\\text{ m} = 2\\text{ N} \\times 0.15\\text{ m} = 0.30\\text{ N m}$."
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Demonstration Video: The Principle of Moments in Equilibrium",
                        "content": {
                            "title": "Demonstration Video: The Principle of Moments in Equilibrium",
                            "description": "Laboratory tutorial demonstrating rotational equilibrium, balancing suspended weights, and calculating beam weights.",
                            "url": "https://www.youtube.com/watch?v=0kF41E_2i1c",
                            "resolved_video_id": "0kF41E_2i1c"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Principle of Moments Demonstration Video",
                            "url": "https://www.youtube.com/watch?v=0kF41E_2i1c",
                            "metadata": {
                                "youtube_id": "0kF41E_2i1c"
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
                                "**Principle of Moments**: For equilibrium, $\\sum M_{\\text{cw}} = \\sum M_{\\text{acw}}$.",
                                "When a beam is not pivoted at its center, its **own weight acts at the C.O.G.**",
                                "Always calculate distances **from the pivot point**."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 4: Torque, Couples and Moments About Two Supports
        # ---------------------------------------------------------------------
        {
            "unit_order": 4,
            "unit_name": "Torque, Couples and Moments About Two Supports",
            "unit_description": "Definition of torque and couples (two equal, opposite, parallel forces), torque formula T = F × s, steering wheels and tap handles, and calculating reaction forces on supported beams and bridges.",
            "lesson_title": "Torque, Couples and Moments About Two Supports",
            "pages": [
                # Page 1: Hook & Steering Wheel Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Pure Rotation: Hands Gripping Opposite Sides of a Steering Wheel",
                        "content": {
                            "title": "Pure Rotation: Hands Gripping Opposite Sides of a Steering Wheel",
                            "caption": "A driver gripping a steering wheel with both hands on opposite sides. Applying two equal and opposite forces forms a couple, rotating the wheel smoothly without sideways bearing wear.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Steering_wheel_hands.jpg/1280px-Steering_wheel_hands.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Steering_wheel_hands.jpg/1280px-Steering_wheel_hands.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Steering Wheel Couple Application",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Steering_wheel_hands.jpg/1280px-Steering_wheel_hands.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Steering_wheel_hands.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Two Hands Turn Better Than One",
                        "content": {
                            "title": "The Physics of a Couple",
                            "text": "Try turning a stiff vehicle steering wheel or opening a tight water tap with just one finger:\n\n- It pushes the axle sideways, generating heavy friction on the bearings.\n- But use two hands on opposite sides—one pulling down while the other pushes up—and the wheel spins smoothly!\n\nThis pair of forces is called a **Couple**, and its turning effect is **Torque**."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Couples & Bridge Supports",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define a **Couple** and **Torque**.",
                                "Calculate the torque of a couple using $T = F \\times s$.",
                                "Explain why couples produce **pure rotation** with zero net linear force.",
                                "Calculate support reaction forces ($R_A, R_B$) for beams and bridges on two supports."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Couple",
                        "content": {
                            "term": "Couple",
                            "definition": "A pair of parallel forces of equal magnitude, acting in opposite directions, whose lines of action do not coincide.",
                            "example": "Turning a water tap or rotating a vehicle steering wheel."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Torque of a Couple",
                        "content": {
                            "term": "Torque of a Couple",
                            "definition": "The rotational effect produced by a couple, calculated by multiplying one force by the perpendicular separation between them ($T = F \\times s$).",
                            "example": "Applying 30 N at 0.40 m separation generates 12 N m of torque."
                        }
                    }
                ],
                # Page 3: Couple SVG & Formula
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Torque of a Couple on a Steering Wheel",
                        "content": {
                            "title": "Torque of a Couple on a Steering Wheel",
                            "caption": "Opposing 30 N forces separated by wheel diameter s = 0.40 m creating 12 N m of clockwise torque with zero net linear force.",
                            "svg_content": get_svg_couple_torque(),
                            "svg": get_svg_couple_torque()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Torque of a Couple Diagram",
                            "metadata": {
                                "svg_content": get_svg_couple_torque()
                            }
                        }
                    }
                ],
                # Page 4: Bridge Reactions SVG & Method
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Moments on Two Supports: Bridge Reaction Forces",
                        "content": {
                            "title": "Moments on Two Supports: Bridge Reaction Forces",
                            "caption": "Supported horizontal plank showing upward reaction forces RA and RB balancing a painter (600 N) and plank weight (200 N).",
                            "svg_content": get_svg_bridge_supports(),
                            "svg": get_svg_bridge_supports()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Bridge Reaction Forces Diagram",
                            "metadata": {
                                "svg_content": get_svg_bridge_supports()
                            }
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Method for Solving Two-Support Beam Problems",
                        "content": {
                            "title": "Two Equilibrium Conditions",
                            "steps": [
                                "1. **Rotational Balance**: Choose one support (e.g. Support A) as your pivot. This eliminates $R_A$ ($R_A \\times 0 = 0$).",
                                "2. **Equate Moments about A**: $\\text{Clockwise Moments} = \\text{Anticlockwise Moments} \\implies (W_{\\text{painter}} \\times d_1) + (W_{\\text{beam}} \\times d_2) = R_B \\times L$. Solve for $R_B$.",
                                "3. **Translational Balance**: Equate total upward and downward forces: $R_A + R_B = W_{\\text{total}}$. Solve for $R_A$."
                            ]
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Steering Wheel Couple Torque",
                        "content": {
                            "question": "A motorist applies a couple of forces of $30\\text{ N}$ each to opposite sides of a steering wheel of diameter $40\\text{ cm}$. What is the resulting torque exerted on the steering wheel?",
                            "options": [
                                "1.2 N m",
                                "12 N m",
                                "24 N m",
                                "1,200 N m"
                            ],
                            "answer": "B",
                            "explanation": "Convert diameter to metres: $s = 40\\text{ cm} = 0.40\\text{ m}$. Using the couple torque formula: $$T = F \\times s = 30\\text{ N} \\times 0.40\\text{ m} = 12\\text{ N m}$$ Therefore, Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Worked Example (Supported Plank)
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Supported Scaffolding Plank",
                        "content": {
                            "title": "Calculating Reaction Forces",
                            "problem": "A uniform plank of length $4.0\\text{ m}$ and weight $200\\text{ N}$ rests on supports A and B at its ends. A $600\\text{ N}$ painter stands $1.0\\text{ m}$ from A. Calculate $R_A$ and $R_B$.",
                            "steps": [
                                "1. **Moments about A**: $R_B \\times 4.0 = (600 \\times 1.0) + (200 \\times 2.0) = 600 + 400 = 1000\\text{ N m}$.",
                                "2. **Solve for $R_B$**: $R_B = \\frac{1000}{4.0} = 250\\text{ N}$.",
                                "3. **Force Balance**: $R_A + R_B = 600 + 200 = 800\\text{ N} \\implies R_A = 800 - 250 = 550\\text{ N}$."
                            ],
                            "answer": "Support A carries 550 N and Support B carries 250 N."
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Torque of Couples and Beam Reaction Forces",
                        "content": {
                            "title": "Physics Video: Torque of Couples and Beam Reaction Forces",
                            "description": "Tutorial covering couples, torque calculation, and step-by-step solutions for bridge support reactions.",
                            "url": "https://www.youtube.com/watch?v=kYJvI8oE2yA",
                            "resolved_video_id": "kYJvI8oE2yA"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Couples and Bridge Reactions Video",
                            "url": "https://www.youtube.com/watch?v=kYJvI8oE2yA",
                            "metadata": {
                                "youtube_id": "kYJvI8oE2yA"
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
                                "A **Couple** consists of two equal, opposite parallel forces producing pure rotation: **$T = F \\times s$**.",
                                "For **supported beams**, solve reaction forces using moment balance about one support followed by vertical force balance."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 5: Resolution of Forces and Stability
        # ---------------------------------------------------------------------
        {
            "unit_order": 5,
            "unit_name": "Resolution of Forces and Stability",
            "unit_description": "Resolving angled forces into perpendicular components (Fx = F cos θ, Fy = F sin θ), three states of equilibrium (stable, unstable, neutral), and the mechanics of toppling (base area vs C.O.G. height).",
            "lesson_title": "Resolution of Forces and Stability",
            "pages": [
                # Page 1: Hook & Excavator Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Heavy Plant Engineering: Excavator Wide Steel Tracks for Incline Stability",
                        "content": {
                            "title": "Heavy Plant Engineering: Excavator Wide Steel Tracks for Incline Stability",
                            "caption": "A construction excavator operating on a steep hillside. Its wide steel tracks expand its base support area and low heavy chassis keeps the C.O.G. low to prevent toppling.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Excavator_working_on_slope.jpg/1280px-Excavator_working_on_slope.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Excavator_working_on_slope.jpg/1280px-Excavator_working_on_slope.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Excavator Stability on Inclined Slope",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Excavator_working_on_slope.jpg/1280px-Excavator_working_on_slope.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Excavator_working_on_slope.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Physics of Toppling Over",
                        "content": {
                            "title": "Why Do Some Objects Tip Easily?",
                            "text": "Why do high-chassis lorries topple over easily on steep corners, while low racing cars never flip?\n\nStability is determined by the relationship between the **Centre of Gravity height** and the **Base Area of Support**."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Resolution & Stability",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Resolve force vectors into horizontal ($F_x = F\\cos\\theta$) and vertical ($F_y = F\\sin\\theta$) components.",
                                "Classify the **3 states of equilibrium**: **Stable, Unstable**, and **Neutral**.",
                                "Explain the condition for **toppling** (line of action of C.O.G. falling outside base area).",
                                "Identify the two golden rules for maximizing stability (wide base and low C.O.G.)."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Resolution of Forces",
                        "content": {
                            "term": "Resolution of Forces",
                            "definition": "The mathematical process of splitting a single force vector into two perpendicular components (horizontal and vertical).",
                            "example": "Pulling a suitcase at 30° creates horizontal pulling force and vertical lifting force."
                        }
                    }
                ],
                # Page 3: 3 States of Equilibrium SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Three States of Equilibrium",
                        "content": {
                            "title": "The Three States of Equilibrium",
                            "caption": "Cone illustrations showing Stable (C.O.G. rises, returns to base), Unstable (C.O.G. falls, topples over), and Neutral (C.O.G. height unchanged, stays in new position).",
                            "svg_content": get_svg_equilibrium_states(),
                            "svg": get_svg_equilibrium_states()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Three States of Equilibrium Diagram",
                            "metadata": {
                                "svg_content": get_svg_equilibrium_states()
                            }
                        }
                    }
                ],
                # Page 4: Vector Resolution & Stability Rules
                [
                    {
                        "type": "formula_breakdown",
                        "title": "Force Vector Resolution",
                        "content": {
                            "title": "Resolving Angled Vectors",
                            "formula": "F_x = F \\cos(\\theta) \\quad \\text{and} \\quad F_y = F \\sin(\\theta)",
                            "variables": [
                                "$F$ = Magnitude of applied force ($\\text{N}$)",
                                "$\\theta$ = Angle of the force relative to horizontal ($^\\circ$)",
                                "$F_x$ = Horizontal component ($\\text{N}$)",
                                "$F_y$ = Vertical component ($\\text{N}$)"
                            ]
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "The Three States of Physical Balance",
                        "content": {
                            "title": "Equilibrium Comparison",
                            "headers": ["Equilibrium State", "Response to Tilt", "C.O.G. Height Shift", "Physical Example"],
                            "rows": [
                                ["Stable", "Returns to original position.", "C.O.G. rises slightly.", "Cone resting on broad circular base."],
                                ["Unstable", "Topples further away from original state.", "C.O.G. falls immediately.", "Pencil balanced on its sharp tip."],
                                ["Neutral", "Remains at rest in its new position.", "C.O.G. height is unchanged.", "Soccer ball rolling on flat ground."]
                            ]
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Ramp Incline Stability",
                        "content": {
                            "question": "A uniform wooden block is placed on an adjustable ramp. If a heavy metal block is glued to the top of the wooden block, how does this affect the block's stability against toppling?",
                            "options": [
                                "It becomes more stable because the block is now heavier.",
                                "It becomes less stable because raising the C.O.G. causes its vertical weight line to fall outside the base at a smaller tilt angle.",
                                "Stability remains unchanged because the contact area is the same.",
                                "It enters neutral equilibrium."
                            ],
                            "answer": "B",
                            "explanation": "Adding weight to the top elevates the overall **Centre of Gravity**. A higher C.O.G. means that when tilted on a ramp, the vertical line of action of weight passes outside the base area at a much lower angle of incline, making the object **less stable and prone to toppling**. Therefore, Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Golden Rules for Stability
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Two Golden Rules of Structural Stability",
                        "content": {
                            "title": "How Engineers Maximize Stability",
                            "text": "1. **Keep the Centre of Gravity as low as possible**: Low C.O.G. means a greater angle of tilt is required before the weight line falls outside the support base.\n2. **Make the Base Area as wide as possible**: Wide base area expands the support polygon, ensuring the weight vector line remains within the base during tilting."
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: States of Equilibrium and Toppling Mechanics",
                        "content": {
                            "title": "Physics Video: States of Equilibrium and Toppling Mechanics",
                            "description": "Video illustrating stable, unstable, and neutral equilibrium, toppling angles, and base area optimization.",
                            "url": "https://www.youtube.com/watch?v=kYJvI8oE2yA",
                            "resolved_video_id": "kYJvI8oE2yA"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Equilibrium States and Toppling Video",
                            "url": "https://www.youtube.com/watch?v=kYJvI8oE2yA",
                            "metadata": {
                                "youtube_id": "kYJvI8oE2yA"
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
                                "Forces resolve into **$F_x = F\\cos\\theta$** and **$F_y = F\\sin\\theta$**.",
                                "The 3 equilibrium states are **stable** (C.O.G. rises), **unstable** (C.O.G. falls), and **neutral** (C.O.G. unchanged).",
                                "An object topples when its C.O.G. weight line falls **outside its base area**.",
                                "Maximize stability with a **wide base** and a **low C.O.G.**"
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 6: Applications and Design of Stable Structures
        # ---------------------------------------------------------------------
        {
            "unit_order": 6,
            "unit_name": "Applications and Design of Stable Structures",
            "unit_description": "Integration of moments, C.O.G., and stability in engineering structures: tower crane counterweights, bridge foundations, and the newspaper tower design challenge.",
            "lesson_title": "Applications and Design of Stable Structures",
            "pages": [
                # Page 1: Hook & Tower Crane Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Construction Engineering: Nairobi High-Rise Tower Crane",
                        "content": {
                            "title": "Construction Engineering: Nairobi High-Rise Tower Crane",
                            "caption": "A towering construction crane operating on a Nairobi skyscraper. Its long lifting jib is counterbalanced by heavy concrete blocks at the short end to prevent forward tipping.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Tower_crane_Nairobi.jpg/1280px-Tower_crane_Nairobi.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Tower_crane_Nairobi.jpg/1280px-Tower_crane_Nairobi.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Construction Tower Crane in Nairobi",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Tower_crane_Nairobi.jpg/1280px-Tower_crane_Nairobi.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 4.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Tower_crane_Nairobi.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Engineering Towers That Never Tip",
                        "content": {
                            "title": "How Cranes Lift Massive Loads Without Tipping",
                            "text": "How does a slender crane lift several tonnes of steel at the tip of its 40-metre arm without toppling forward?\n\nStructural engineers balance moments by placing massive concrete **counterweights** on the short arm behind the mast."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Structural Design & Stability",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Integrate C.O.G., moments, and stability in structural analysis.",
                                "Calculate balancing moments for **tower crane counterweights** ($L \\times d_L = C \\times d_C$).",
                                "Evaluate bridge foundations and high-rise structural stability.",
                                "Design and prototype a stable structural tower model."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Counterweight",
                        "content": {
                            "term": "Counterweight",
                            "definition": "A heavy mass placed on the opposite side of a pivot to generate an opposing balancing moment, neutralizing tipping forces.",
                            "example": "Concrete blocks on crane jibs and elevator counterweights."
                        }
                    }
                ],
                # Page 3: Tower Crane Moments SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Tower Crane Counterweight Moment Balancing Schematic",
                        "content": {
                            "title": "Tower Crane Counterweight Moment Balancing Schematic",
                            "caption": "Crane schematic: 100,000 N counterweight at 10 m (anticlockwise 1,000,000 N m) balancing a maximum safe load of 25,000 N at 40 m (clockwise 1,000,000 N m).",
                            "svg_content": get_svg_crane_moments(),
                            "svg": get_svg_crane_moments()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Tower Crane Moment Balancing Diagram",
                            "metadata": {
                                "svg_content": get_svg_crane_moments()
                            }
                        }
                    }
                ],
                # Page 4: Tower Crane Worked Calculation
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Calculating Maximum Safe Crane Load",
                        "content": {
                            "title": "Crane Load Limit Calculation",
                            "problem": "A tower crane has a counterweight of $100,000\\text{ N}$ located $10.0\\text{ m}$ to the left of the mast pivot. Calculate the maximum safe load ($W$) that can be lifted at the end of the $40.0\\text{ m}$ right jib without tipping the crane.",
                            "steps": [
                                "1. **Anticlockwise Counterweight Moment**: $M_{\\text{anti}} = 100,000\\text{ N} \\times 10.0\\text{ m} = 1,000,000\\text{ N m}$.",
                                "2. **Set Up Clockwise Load Moment**: $M_{\\text{clock}} = W \\times 40.0\\text{ m}$.",
                                "3. **Equate for Balance**: $1,000,000 = 40.0 W \\implies W = \\frac{1,000,000}{40.0} = 25,000\\text{ N}$."
                            ],
                            "answer": "The maximum safe load at 40 m is 25,000 N (equivalent to 2.5 tonnes)."
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Improving Structural Tower Stability",
                        "content": {
                            "question": "A student group builds a newspaper model tower. When a 100 g mass is placed on top, the tower immediately tilts and topples. Which modification will most effectively prevent toppling?",
                            "options": [
                                "Add extra tape to the top joints to make them stiffer.",
                                "Shorten the legs to lower the overall Centre of Gravity and widen the leg span.",
                                "Make the tower taller using extra newspaper rolled loosely.",
                                "Remove the base supports."
                            ],
                            "answer": "B",
                            "explanation": "Toppling occurs when the C.O.G. is too high or the base is too narrow. Shortening the legs lowers the heavy load (lowering C.O.G.) and widening the leg span increases base area, greatly improving stability. Adding tape/height to the top raises C.O.G. and worsens instability. Therefore, Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Design Challenge
                [
                    {
                        "type": "mini_activity",
                        "title": "Engineering Challenge: Stable Tower Prototype",
                        "content": {
                            "title": "The Newspaper Tower Challenge",
                            "task": "Construct a freestanding stable tower using 20 sheets of newspaper and masking tape that supports a $100\\text{ g}$ load at its peak for 1 minute:\n\n1. Form a wide tripod/pyramid base to maximize base area.\n2. Keep upper rolled tubes lightweight to avoid raising the C.O.G.\n3. Test the structure and calculate the maximum tipping angle."
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Engineering Video: Tower Crane Physics and Structural Stability",
                        "content": {
                            "title": "Engineering Video: Tower Crane Physics and Structural Stability",
                            "description": "Video explaining tower crane counterweight dynamics, wind load mitigation, and foundation anchoring in high-rise construction.",
                            "url": "https://www.youtube.com/watch?v=kYJvI8oE2yA",
                            "resolved_video_id": "kYJvI8oE2yA"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Tower Crane Stability Physics Video",
                            "url": "https://www.youtube.com/watch?v=kYJvI8oE2yA",
                            "metadata": {
                                "youtube_id": "kYJvI8oE2yA"
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
                                "**Tower Cranes** use counterweights to neutralize overturning moments ($L \\times d_L = C \\times d_C$).",
                                "Structural stability is achieved by keeping the **weight line of action inside the base area**."
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
def ingest_grade10_physics_topic5():
    print("======================================================================")
    print("INGESTING CBC GRADE 10 PHYSICS — TOPIC 5: MOMENTS AND EQUILIBRIUM")
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

    # 3. Get or Create Topic: Moments and Equilibrium (Order: 5)
    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=5,
        defaults={
            "name": "Moments and Equilibrium",
            "description": "Exploration of Centre of Gravity, Moment of a Force (M = F×d), Principle of Moments (Σ M_cw = Σ M_acw), torque of couples, force resolution, and structural stability."
        }
    )
    if not t_created and topic.name != "Moments and Equilibrium":
        topic.name = "Moments and Equilibrium"
        topic.description = "Exploration of Centre of Gravity, Moment of a Force (M = F×d), Principle of Moments (Σ M_cw = Σ M_acw), torque of couples, force resolution, and structural stability."
        topic.save()
    print(f"Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    curriculum_data = build_topic5_curriculum_data()

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
    print(f"TOPIC 5 INGESTION COMPLETE:")
    print(f"  - Learning Units: {total_units_created}")
    print(f"  - Lessons:        {total_lessons_created}")
    print(f"  - Lesson Blocks:  {total_blocks_created}")
    print(f"  - Lesson Assets:  {total_assets_created}")
    print("======================================================================")

if __name__ == "__main__":
    ingest_grade10_physics_topic5()
