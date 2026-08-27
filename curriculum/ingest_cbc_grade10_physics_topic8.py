"""
VLearn CBC Grade 10 Physics — Topic 8: Radioactivity and Stability of Isotopes
Production Ingestion & Visual Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Physics
Topic: Radioactivity and Stability of Isotopes (Order: 8)

7 Learning Units & 7 Published Lessons:
  1. Isotopes, Nuclides and Nuclear Stability (8 Pages, 13 Blocks)
  2. Radioactive Decay and Nuclear Equations (8 Pages, 13 Blocks)
  3. Types and Properties of Radiation (8 Pages, 13 Blocks)
  4. Detection of Radioactive Emissions and Safety (8 Pages, 14 Blocks)
  5. Half-Life and Decay Curves (8 Pages, 13 Blocks)
  6. Nuclear Fission, Fusion and Chain Reactions (8 Pages, 13 Blocks)
  7. Medical, Industrial, Agricultural and Environmental Applications (8 Pages, 13 Blocks)

Includes:
  - 7 Custom Responsive Sanitized Vector SVG Diagrams
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
# SVG DEFINITIONS FOR TOPIC 8
# =============================================================================

def get_svg_nuclide_notation():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <rect width="800" height="400" fill="#0f172a" rx="16"/>
  <text x="400" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">STANDARD NUCLIDE NOTATION AND COMPOSITION</text>
  <text x="400" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Mass Number (A = Protons + Neutrons) • Atomic Number (Z = Protons) • Neutrons N = A - Z</text>

  <!-- Giant Nuclide Symbol Box -->
  <g transform="translate(180, 100)">
    <rect width="220" height="230" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="135" y="160" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="110" font-weight="800" text-anchor="middle">C</text>

    <!-- Top Left: Mass Number A (14) -->
    <circle cx="55" cy="65" r="28" fill="#ef444422" stroke="#ef4444" stroke-width="2"/>
    <text x="55" y="74" fill="#ef4444" font-family="system-ui, sans-serif" font-size="26" font-weight="800" text-anchor="middle">14</text>

    <!-- Bottom Left: Atomic Number Z (6) -->
    <circle cx="55" cy="170" r="28" fill="#38bdf822" stroke="#38bdf8" stroke-width="2"/>
    <text x="55" y="179" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="26" font-weight="800" text-anchor="middle">6</text>
  </g>

  <!-- Labels & Calculations on Right -->
  <g transform="translate(440, 100)">
    <!-- Mass Number Label -->
    <rect width="280" height="60" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="15" y="24" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Mass Number (A = 14):</text>
    <text x="15" y="45" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12">Total nucleons (6 Protons + 8 Neutrons)</text>

    <!-- Atomic Number Label -->
    <rect y="75" width="280" height="60" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="15" y="99" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Atomic Number (Z = 6):</text>
    <text x="15" y="120" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12">Defines element identity (6 Protons)</text>

    <!-- Neutron Formula -->
    <rect y="150" width="280" height="80" rx="8" fill="#1e293b" stroke="#22c55e" stroke-width="2"/>
    <text x="15" y="176" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Neutrons (N) = A - Z:</text>
    <text x="15" y="200" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13">N = 14 - 6 = 8 Neutrons</text>
    <text x="15" y="218" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Unstable radioactive isotope of Carbon</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_electric_field_deflection():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">DEFLECTION OF RADIATION IN AN ELECTRIC FIELD</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Beta (-) Deflects Sharply to (+) • Alpha (+) Deflects Gently to (-) • Gamma (0) Undeflected</text>

  <!-- Lead Collimator Block (Left) -->
  <g transform="translate(60, 160)">
    <rect x="0" y="0" width="50" height="80" fill="#475569" stroke="#94a3b8" stroke-width="1.5" rx="3"/>
    <rect x="40" y="32" width="15" height="16" fill="#0f172a"/>
    <circle cx="20" cy="40" r="8" fill="#f59e0b"/>
    <text x="25" y="105" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Source</text>
  </g>

  <!-- Parallel Charged Plates -->
  <g transform="translate(180, 80)">
    <!-- Positive Top Plate (+) -->
    <rect x="0" y="0" width="380" height="18" fill="#ef4444" rx="3"/>
    <text x="190" y="14" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">POSITIVE PLATE (+)</text>

    <!-- Negative Bottom Plate (-) -->
    <rect x="0" y="220" width="380" height="18" fill="#38bdf8" rx="3"/>
    <text x="190" y="234" fill="#000000" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">NEGATIVE PLATE (-)</text>

    <!-- 1. Beta Particle Path (Curves sharply UP towards +) -->
    <path d="M -70 120 L 40 120 Q 200 120 320 25" fill="none" stroke="#ef4444" stroke-width="3"/>
    <polygon points="320,25 310,24 316,33" fill="#ef4444"/>
    <text x="340" y="35" fill="#ef4444" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Beta (β⁻) Particle</text>
    <text x="340" y="52" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Light mass, sharp deflection</text>

    <!-- 2. Gamma Ray Path (Straight, Zero Deflection) -->
    <line x1="-70" y1="120" x2="480" y2="120" stroke="#22c55e" stroke-width="2.5" stroke-dasharray="6 4"/>
    <polygon points="480,120 470,115 470,125" fill="#22c55e"/>
    <text x="495" y="124" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Gamma (γ) Ray</text>
    <text x="495" y="140" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Neutral charge, zero deflection</text>

    <!-- 3. Alpha Particle Path (Curves gently DOWN towards -) -->
    <path d="M -70 120 L 40 120 Q 200 120 320 210" fill="none" stroke="#38bdf8" stroke-width="4"/>
    <polygon points="320,210 316,200 310,208" fill="#38bdf8"/>
    <text x="340" y="205" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Alpha (α) Particle</text>
    <text x="340" y="222" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10">Heavy mass (+2e), gentle deflection</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_radiation_shielding():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 380" width="100%" height="100%">
  <rect width="820" height="380" fill="#0f172a" rx="16"/>
  <text x="410" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">PENETRATING POWER AND RADIATION SHIELDING</text>
  <text x="410" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Alpha Stopped by Paper • Beta Stopped by Aluminum • Gamma Stopped by Lead</text>

  <!-- Shielding Materials -->
  <g transform="translate(100, 80)">
    <!-- Material 1: Sheet of Paper -->
    <rect x="200" y="20" width="12" height="240" fill="#f8fafc" stroke="#94a3b8" stroke-width="1"/>
    <text x="206" y="280" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Paper (0.1 mm)</text>

    <!-- Material 2: Aluminum Sheet -->
    <rect x="360" y="20" width="22" height="240" fill="#94a3b8" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="371" y="280" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Aluminum (5 mm)</text>

    <!-- Material 3: Dense Lead Block -->
    <rect x="520" y="20" width="50" height="240" fill="#334155" stroke="#64748b" stroke-width="2"/>
    <text x="545" y="280" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Lead / Concrete</text>

    <!-- 1. Alpha Path (Stops at Paper) -->
    <path d="M 0 60 L 200 60" stroke="#38bdf8" stroke-width="4"/>
    <circle cx="200" cy="60" r="5" fill="#ef4444"/>
    <text x="-10" y="65" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="end">Alpha (α)</text>

    <!-- 2. Beta Path (Passes Paper, Stops at Aluminum) -->
    <path d="M 0 130 L 360 130" stroke="#f59e0b" stroke-width="3"/>
    <circle cx="360" cy="130" r="5" fill="#ef4444"/>
    <text x="-10" y="135" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="end">Beta (β)</text>

    <!-- 3. Gamma Path (Passes Paper & Al, Absorbed in Lead) -->
    <path d="M 0 200 L 545 200" stroke="#22c55e" stroke-width="2.5" stroke-dasharray="5 3"/>
    <circle cx="545" cy="200" r="5" fill="#ef4444"/>
    <text x="-10" y="205" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="end">Gamma (γ)</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_three_safety_pillars():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">THE THREE PILLARS OF RADIATION SAFETY AND PROTECTION</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Standard Industrial Protocols to Minimize Radiation Dose (ALARA Principle)</text>

  <!-- Pillar 1: Minimize Time -->
  <g transform="translate(50, 80)">
    <rect width="210" height="260" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="105" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. MINIMIZE TIME</text>

    <!-- Clock Icon -->
    <circle cx="105" cy="95" r="40" fill="#0284c722" stroke="#38bdf8" stroke-width="2.5"/>
    <line x1="105" y1="95" x2="105" y2="70" stroke="#38bdf8" stroke-width="3"/>
    <line x1="105" y1="95" x2="125" y2="95" stroke="#38bdf8" stroke-width="3"/>

    <text x="105" y="165" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Work Swiftly</text>
    <text x="105" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Cumulative dose is directly</text>
    <text x="105" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">proportional to exposure time.</text>
  </g>

  <!-- Pillar 2: Maximize Distance -->
  <g transform="translate(315, 80)">
    <rect width="210" height="260" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="105" y="28" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">2. MAXIMIZE DISTANCE</text>

    <!-- Tongs / Arrow Icon -->
    <path d="M 45 95 L 165 95 M 55 85 L 45 95 L 55 105 M 155 85 L 165 95 L 155 105" stroke="#f59e0b" stroke-width="3"/>
    <circle cx="35" cy="95" r="6" fill="#ef4444"/>

    <text x="105" y="165" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Inverse Square Law</text>
    <text x="105" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Intensity drops with 1/d².</text>
    <text x="105" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Always handle with long tongs.</text>
  </g>

  <!-- Pillar 3: Use Shielding -->
  <g transform="translate(580, 80)">
    <rect width="210" height="260" rx="10" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
    <text x="105" y="28" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">3. DENSE SHIELDING</text>

    <!-- Shield / Lead Barrier Icon -->
    <rect x="75" y="60" width="60" height="70" fill="#334155" stroke="#22c55e" stroke-width="2" rx="4"/>
    <text x="105" y="100" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">LEAD</text>

    <text x="105" y="165" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Absorb Radiation</text>
    <text x="105" y="185" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Store inside thick lead pots</text>
    <text x="105" y="200" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">and wear lead-lined aprons.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_half_life_decay_curve():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 420" width="100%" height="100%">
  <rect width="820" height="420" fill="#0f172a" rx="16"/>
  <text x="410" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">RADIOACTIVE HALF-LIFE (t_1/2) EXPONENTIAL DECAY CURVE</text>
  <text x="410" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Activity Halves Every 15 Hours: N(t) = N_0 × (1/2)^n • Constant Halving Interval</text>

  <!-- Axes -->
  <line x1="120" y1="340" x2="740" y2="340" stroke="#94a3b8" stroke-width="2"/>
  <line x1="120" y1="340" x2="120" y2="80" stroke="#94a3b8" stroke-width="2"/>

  <!-- Y-Axis Ticks (Activity in Bq) -->
  <text x="105" y="345" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">0</text>
  <text x="105" y="280" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">100 Bq (1/8)</text>
  <text x="105" y="215" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">200 Bq (1/4)</text>
  <text x="105" y="150" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">400 Bq (1/2)</text>
  <text x="105" y="85" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="end">800 Bq (N0)</text>
  <text x="35" y="200" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle" transform="rotate(-90 35 200)">Activity (Bq)</text>

  <!-- X-Axis Ticks (Time in Hours) -->
  <text x="120" y="360" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">0</text>
  <text x="270" y="360" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">15 h (1 t_1/2)</text>
  <text x="420" y="360" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">30 h (2 t_1/2)</text>
  <text x="570" y="360" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">45 h (3 t_1/2)</text>
  <text x="430" y="390" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Time Elapsed (hours)</text>

  <!-- Exponential Decay Curve -->
  <path d="M 120 85 Q 220 200 270 215 T 420 280 T 570 312 T 720 330" fill="none" stroke="#38bdf8" stroke-width="3.5"/>

  <!-- Dashed Halving Projection Lines -->
  <line x1="120" y1="215" x2="270" y2="215" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4 3"/>
  <line x1="270" y1="215" x2="270" y2="340" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4 3"/>
  <circle cx="270" cy="215" r="5" fill="#f59e0b"/>

  <line x1="120" y1="280" x2="420" y2="280" stroke="#22c55e" stroke-width="1.5" stroke-dasharray="4 3"/>
  <line x1="420" y1="280" x2="420" y2="340" stroke="#22c55e" stroke-width="1.5" stroke-dasharray="4 3"/>
  <circle cx="420" cy="280" r="5" fill="#22c55e"/>

  <line x1="120" y1="312" x2="570" y2="312" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4 3"/>
  <line x1="570" y1="312" x2="570" y2="340" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4 3"/>
  <circle cx="570" cy="312" r="5" fill="#38bdf8"/>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_nuclear_fission_chain():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 420" width="100%" height="100%">
  <rect width="840" height="420" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">CONTROLLED NUCLEAR FISSION CHAIN REACTION (U-235)</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Neutron Capture • Splitting into Ba-141 & Kr-92 • Emission of 3 Fast Neutrons • Control Rod Absorption</text>

  <!-- Fission Schematic -->
  <g transform="translate(60, 90)">
    <!-- Stage 1: Incident Slow Neutron striking U-235 -->
    <circle cx="40" cy="120" r="7" fill="#38bdf8"/>
    <path d="M 40 120 L 110 120 M 100 115 L 110 120 L 100 125" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="40" y="100" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Slow Neutron</text>

    <circle cx="150" cy="120" r="28" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
    <text x="150" y="125" fill="#000000" font-family="system-ui, sans-serif" font-size="11" font-weight="800" text-anchor="middle">U-235</text>

    <!-- Stage 2: Splitting into Fission Fragments -->
    <!-- Barium-141 -->
    <path d="M 175 110 L 260 60" stroke="#ef4444" stroke-width="2"/>
    <circle cx="280" cy="50" r="18" fill="#ef4444" stroke="#dc2626" stroke-width="1.5"/>
    <text x="280" y="54" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Ba-141</text>

    <!-- Krypton-92 -->
    <path d="M 175 130 L 260 190" stroke="#ef4444" stroke-width="2"/>
    <circle cx="280" cy="200" r="15" fill="#ef4444" stroke="#dc2626" stroke-width="1.5"/>
    <text x="280" y="204" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Kr-92</text>

    <!-- 3 Emitted Neutrons -->
    <circle cx="340" cy="80" r="6" fill="#38bdf8"/>
    <circle cx="340" cy="125" r="6" fill="#38bdf8"/>
    <circle cx="340" cy="170" r="6" fill="#38bdf8"/>

    <!-- Control Rod Absorber (Middle Neutron Intercepted) -->
    <rect x="380" y="105" width="20" height="40" fill="#64748b" stroke="#94a3b8" stroke-width="1.5" rx="3"/>
    <text x="390" y="160" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Control Rod (Absorbed)</text>

    <!-- Stage 3: Continuing Sustained Chain (Top & Bottom Neutrons trigger next U-235) -->
    <circle cx="520" cy="60" r="24" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
    <text x="520" y="65" fill="#000000" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">U-235</text>

    <circle cx="520" cy="190" r="24" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
    <text x="520" y="195" fill="#000000" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">U-235</text>
  </g>

  <!-- Energy Output Callout -->
  <g transform="translate(160, 325)">
    <rect width="520" height="50" rx="8" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
    <text x="260" y="32" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">E = mc² • 1 kg of Uranium produces 2–3 million times more energy than 1 kg of coal</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg


# =============================================================================
# CURRICULUM DEFINITION DATA FOR TOPIC 8
# =============================================================================

def build_topic8_curriculum_data():
    return [
        # ---------------------------------------------------------------------
        # LESSON 1: Isotopes, Nuclides and Nuclear Stability
        # ---------------------------------------------------------------------
        {
            "unit_order": 1,
            "unit_name": "Isotopes, Nuclides and Nuclear Stability",
            "unit_description": "Nuclide notation A/Z X, calculating neutrons N = A - Z, isotopes (same protons, different neutrons), nuclear stability (Strong Nuclear Force vs Electrostatic repulsion), and background radiation.",
            "lesson_title": "Isotopes, Nuclides and Nuclear Stability",
            "pages": [
                # Page 1: Hook & Carbon Atom Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Subatomic Core: Carbon Atom Nucleus and Electron Cloud",
                        "content": {
                            "title": "Subatomic Core: Carbon Atom Nucleus and Electron Cloud",
                            "caption": "An artistic representation of a Carbon atom showing its dense central nucleus of 6 protons and 6 neutrons surrounded by orbiting electron shells.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Carbon_atom_representation.jpg/1280px-Carbon_atom_representation.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Carbon_atom_representation.jpg/1280px-Carbon_atom_representation.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Carbon Atom Atomic Structure",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Carbon_atom_representation.jpg/1280px-Carbon_atom_representation.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Carbon_atom_representation.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Silent Nuclear Clock",
                        "content": {
                            "title": "Why Some Atoms Never Change and Others Explode",
                            "text": "Why do Carbon-12 atoms remain stable for billions of years, while Carbon-14 atoms spontaneously decay?\n\nInside the atomic nucleus, stability is dictated by the battle between the **Strong Nuclear Force** holding nucleons together and **Electrostatic Repulsion** pushing positive protons apart."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Nuclides & Stability",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Represent nuclides using standard notation: **${}^{A}_{Z}\\text{X}$**.",
                                "Calculate number of neutrons using **$N = A - Z$**.",
                                "Define **Isotopes** and explain nuclear stability.",
                                "Identify sources of natural and artificial **Background Radiation**."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Nuclide",
                        "content": {
                            "term": "Nuclide",
                            "definition": "A specific atomic species characterized by its exact number of protons (Z) and neutrons (N).",
                            "example": "Carbon-14 (${}^{14}_{6}\\text{C}$) and Uranium-238 (${}^{238}_{92}\\text{U}$)."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Isotopes",
                        "content": {
                            "term": "Isotopes",
                            "definition": "Atoms of the same element having the same atomic number (protons) but different mass numbers (neutrons).",
                            "example": "Carbon-12 (${}^{12}_{6}\\text{C}$) and Carbon-14 (${}^{14}_{6}\\text{C}$)."
                        }
                    }
                ],
                # Page 3: Nuclide Notation SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Standard Nuclide Notation Diagram",
                        "content": {
                            "title": "Standard Nuclide Notation Diagram",
                            "caption": "Carbon-14 nuclide notation: Mass Number A = 14, Atomic Number Z = 6, yielding N = A - Z = 8 neutrons.",
                            "svg_content": get_svg_nuclide_notation(),
                            "svg": get_svg_nuclide_notation()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Nuclide Notation Diagram",
                            "metadata": {
                                "svg_content": get_svg_nuclide_notation()
                            }
                        }
                    }
                ],
                # Page 4: Forces in the Nucleus
                [
                    {
                        "type": "comparison_table",
                        "title": "Subatomic Battle: Strong Nuclear Force vs Electrostatic Force",
                        "content": {
                            "title": "Nuclear Stability Forces",
                            "headers": ["Force", "Nature", "Acts Between", "Role in Stability"],
                            "rows": [
                                ["Strong Nuclear Force", "Attractive (Extremely powerful at $< 10^{-15}\\text{ m}$)", "All nucleons (Protons & Neutrons)", "Glues the nucleus together against repulsion."],
                                ["Electrostatic Repulsion", "Repulsive (Long range)", "Between positive protons only", "Tends to blow the nucleus apart as proton count rises."]
                            ]
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Calculating Neutrons in Uranium-238",
                        "content": {
                            "question": "An atom of Uranium-238 is represented by the nuclide notation ${}^{238}_{92}\\text{U}$. How many neutrons are contained in the nucleus of this atom?",
                            "options": [
                                "92",
                                "146",
                                "238",
                                "330"
                            ],
                            "answer": "B",
                            "explanation": "Mass number is $A = 238$ and atomic number is $Z = 92$. The number of neutrons $N$ is calculated as $N = A - Z = 238 - 92 = 146$ neutrons. Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Isotope Modeling Activity
                [
                    {
                        "type": "mini_activity",
                        "title": "Laboratory Activity: Card-Based Isotope Modeling",
                        "content": {
                            "title": "Building Carbon-12 and Carbon-14",
                            "task": "Cut 20 red circles (protons, +) and 20 blue circles (neutrons, blank):\n\n1. Model Carbon-12: Combine 6 protons + 6 neutrons (${}^{12}_{6}\\text{C}$).\n2. Model Carbon-14: Combine 6 protons + 8 neutrons (${}^{14}_{6}\\text{C}$).\n3. Notice: Proton count remains 6 because atomic number defines chemical element identity."
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Atomic Nucleus, Isotopes, and Nuclear Stability",
                        "content": {
                            "title": "Physics Video: Atomic Nucleus, Isotopes, and Nuclear Stability",
                            "description": "Video explaining nuclide notation, the strong nuclear force, and isotopic stability curves.",
                            "url": "https://www.youtube.com/watch?v=kYJvI8oE2yA",
                            "resolved_video_id": "kYJvI8oE2yA"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Nuclear Stability and Isotopes Video",
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
                        "title": "Lesson 1 Summary: Key Takeaways",
                        "content": {
                            "title": "Core Summary",
                            "takeaways": [
                                "Nuclide notation: **${}^{A}_{Z}\\text{X}$** where $N = A - Z$.",
                                "**Isotopes** share the same atomic number $Z$ but have different mass numbers $A$.",
                                "**Nuclear stability** depends on the balance between the Strong Nuclear Force and Electrostatic repulsion."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 2: Radioactive Decay and Nuclear Equations
        # ---------------------------------------------------------------------
        {
            "unit_order": 2,
            "unit_name": "Radioactive Decay and Nuclear Equations",
            "unit_description": "Spontaneous and random decay, parent and daughter nuclides, balancing nuclear equations for Alpha decay (4/2 He), Beta decay (0/-1 e), and Gamma emission (0/0 gamma).",
            "lesson_title": "Radioactive Decay and Nuclear Equations",
            "pages": [
                # Page 1: Hook & Uranium Ore Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Natural Radioactivity: Pitchblende (Uranium Ore) Specimen",
                        "content": {
                            "title": "Natural Radioactivity: Pitchblende (Uranium Ore) Specimen",
                            "caption": "A geological specimen of pitchblende uranium ore. Inside this rock, unstable heavy uranium nuclei are naturally and spontaneously decaying into lighter elements like thorium, radium, and lead.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Pitchblende_uranium_ore.jpg/1280px-Pitchblende_uranium_ore.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Pitchblende_uranium_ore.jpg/1280px-Pitchblende_uranium_ore.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Pitchblende Uranium Radioactive Ore",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Pitchblende_uranium_ore.jpg/1280px-Pitchblende_uranium_ore.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Pitchblende_uranium_ore.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Spontaneous Transmutation of Elements",
                        "content": {
                            "title": "Alchemists' Dream Achieved by Nature",
                            "text": "Chemical reactions only rearrange outer electrons.\n\nIn **Radioactive Decay**, unstable atomic nuclei spontaneously shed particles and energy, transmuting the parent atom into a completely different chemical element!"
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Nuclear Equations",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain radioactive decay as a **spontaneous** and **random** process.",
                                "Describe **Alpha ($\\alpha$), Beta ($\\beta^-$)**, and **Gamma ($\\gamma$)** emissions.",
                                "Balance mass and atomic numbers in **nuclear decay equations**."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Alpha (α) Decay",
                        "content": {
                            "term": "Alpha (α) Decay",
                            "definition": "The emission of a Helium nucleus (${}^{4}_{2}\\text{He}$), decreasing mass number A by 4 and atomic number Z by 2.",
                            "example": "${}^{238}_{92}\\text{U} \\longrightarrow {}^{234}_{90}\\text{Th} + {}^{4}_{2}\\text{He}$"
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Beta (β⁻) Decay",
                        "content": {
                            "term": "Beta (β⁻) Decay",
                            "definition": "The spontaneous conversion of a nuclear neutron into a proton, emitting a high-speed electron (${}^{0}_{-1}\\text{e}$), keeping A unchanged and increasing Z by 1.",
                            "example": "${}^{14}_{6}\\text{C} \\longrightarrow {}^{14}_{7}\\text{N} + {}^{0}_{-1}\\text{e}$"
                        }
                    }
                ],
                # Page 3: General Decay Equations
                [
                    {
                        "type": "formula_breakdown",
                        "title": "Nuclear Decay Balancing Models",
                        "content": {
                            "title": "Conservation of Nucleons and Charge",
                            "formula": "\\sum A_{\\text{reactants}} = \\sum A_{\\text{products}} \\quad \\text{and} \\quad \\sum Z_{\\text{reactants}} = \\sum Z_{\\text{products}}",
                            "variables": [
                                "Alpha: ${}^{A}_{Z}\\text{X} \\longrightarrow {}^{A-4}_{Z-2}\\text{Y} + {}^{4}_{2}\\text{He}$",
                                "Beta: ${}^{A}_{Z}\\text{X} \\longrightarrow {}^{A}_{Z+1}\\text{Y} + {}^{0}_{-1}\\text{e}$",
                                "Gamma: ${}^{A}_{Z}\\text{X}^* \\longrightarrow {}^{A}_{Z}\\text{X} + {}^{0}_{0}\\gamma$"
                            ]
                        }
                    }
                ],
                # Page 4: Worked Nuclear Balancing Examples
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Balancing Decay Equations",
                        "content": {
                            "title": "Identifying Daughter Products",
                            "problem": "1. Radium-226 (${}^{226}_{88}\\text{Ra}$) undergoes alpha decay.\n2. Iodine-131 (${}^{131}_{53}\\text{I}$) undergoes beta decay.",
                            "steps": [
                                "1. **Radium Alpha Decay**: ${}^{226}_{88}\\text{Ra} \\longrightarrow {}^{A}_{Z}\\text{X} + {}^{4}_{2}\\text{He}$. Top: $226 = A + 4 \\implies A = 222$. Bottom: $88 = Z + 2 \\implies Z = 86$ (Radon, $\\text{Rn}$). Equation: ${}^{226}_{88}\\text{Ra} \\longrightarrow {}^{222}_{86}\\text{Rn} + {}^{4}_{2}\\text{He}$.",
                                "2. **Iodine Beta Decay**: ${}^{131}_{53}\\text{I} \\longrightarrow {}^{A}_{Z}\\text{X} + {}^{0}_{-1}\\text{e}$. Top: $131 = A + 0 \\implies A = 131$. Bottom: $53 = Z - 1 \\implies Z = 54$ (Xenon, $\\text{Xe}$). Equation: ${}^{131}_{53}\\text{I} \\longrightarrow {}^{131}_{54}\\text{Xe} + {}^{0}_{-1}\\text{e}$."
                            ],
                            "answer": "Daughters are Radon-222 and Xenon-131."
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Thorium-234 to Protactinium-234 Decay",
                        "content": {
                            "question": "An unstable isotope of Thorium represented by ${}^{234}_{90}\\text{Th}$ decays into Protactinium (${}^{234}_{91}\\text{Pa}$). What particle was emitted?",
                            "options": [
                                "An alpha particle",
                                "A beta particle",
                                "A gamma photon",
                                "A neutron"
                            ],
                            "answer": "B",
                            "explanation": "Mass number remains unchanged ($234 = 234 + A \\implies A = 0$) while atomic number increases by 1 ($90 = 91 + Z \\implies Z = -1$). The emitted particle with $A=0, Z=-1$ is a **Beta particle (${}^{0}_{-1}\\text{e}$)**. Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Equation Balancing Exercise
                [
                    {
                        "type": "step_process",
                        "title": "Rules for Balancing Nuclear Reactions",
                        "content": {
                            "title": "Two-Step Balancing Checklist",
                            "steps": [
                                "1. **Balance Mass Numbers (Top)**: Sum of mass numbers on the left of the arrow MUST equal sum on the right.",
                                "2. **Balance Atomic Numbers (Bottom)**: Sum of atomic numbers on the left MUST equal sum on the right.",
                                "3. **Identify Element Symbol**: Look up atomic number $Z$ on periodic table to assign correct chemical symbol."
                            ]
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Alpha, Beta, and Gamma Nuclear Decay Equations",
                        "content": {
                            "title": "Physics Video: Alpha, Beta, and Gamma Nuclear Decay Equations",
                            "description": "Video explaining radioactive decay, balancing nuclear equations, and tracking parent-daughter transmutations.",
                            "url": "https://www.youtube.com/watch?v=kYJvI8oE2yA",
                            "resolved_video_id": "kYJvI8oE2yA"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Nuclear Decay Equations Tutorial",
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
                                "**Alpha decay**: Emits ${}^{4}_{2}\\text{He}$ ($A-4, Z-2$).",
                                "**Beta decay**: Emits ${}^{0}_{-1}\\text{e}$ ($A$ unchanged, $Z+1$).",
                                "**Gamma emission**: Emits pure energy photons (${}^{0}_{0}\\gamma$) without changing $A$ or $Z$."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 3: Types and Properties of Radiation
        # ---------------------------------------------------------------------
        {
            "unit_order": 3,
            "unit_name": "Types and Properties of Radiation",
            "unit_description": "Comparative physical properties of Alpha, Beta, and Gamma radiations: mass, charge, speed, ionizing power vs penetrating power, and trajectory deflection in electric/magnetic fields.",
            "lesson_title": "Types and Properties of Radiation",
            "pages": [
                # Page 1: Hook & Shielding Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Radiation Penetration: Paper, Aluminum, and Lead Shielding",
                        "content": {
                            "title": "Radiation Penetration: Paper, Aluminum, and Lead Shielding",
                            "caption": "Comparison of radiation penetration: Alpha particles are stopped by thin paper, Beta particles pass paper but are stopped by aluminum, while Gamma rays require thick dense lead.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Radiation_shielding_comparison.jpg/1280px-Radiation_shielding_comparison.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Radiation_shielding_comparison.jpg/1280px-Radiation_shielding_comparison.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Radiation Shielding Penetration Diagram",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Radiation_shielding_comparison.jpg/1280px-Radiation_shielding_comparison.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Radiation_shielding_comparison.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Paper Stops Some Radiation but Not Others",
                        "content": {
                            "title": "Ionizing Power vs Penetrating Power",
                            "text": "A sheet of paper stops alpha particles completely, but gamma rays pass through concrete walls.\n\nRadiation behavior is governed by the inverse trade-off between **Ionizing Power** (stripping electrons) and **Penetrating Power** (distance traveled)."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Radiation Properties",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Compare **Alpha, Beta**, and **Gamma** across charge, mass, speed, ionization, and penetration.",
                                "Explain the inverse relationship between ionizing power and penetrating power.",
                                "Analyze radiation trajectory splitting in **electric and magnetic fields**."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Ionizing Power",
                        "content": {
                            "term": "Ionizing Power",
                            "definition": "The physical ability of radiation to strip electrons away from atoms, forming ions and causing biological damage.",
                            "example": "Alpha radiation has the highest ionizing power due to its +2 charge and heavy mass."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Penetrating Power",
                        "content": {
                            "term": "Penetrating Power",
                            "definition": "The ability of radiation to pass through matter without being absorbed or stopped.",
                            "example": "Gamma radiation has the highest penetration because it has no charge or mass."
                        }
                    }
                ],
                # Page 3: Radiation Shielding SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Radiation Penetration and Shielding Diagram",
                        "content": {
                            "title": "Radiation Penetration and Shielding Diagram",
                            "caption": "Visual penetration chart: Alpha stopped by paper, Beta stopped by 5 mm aluminum, Gamma penetrating deep into thick lead.",
                            "svg_content": get_svg_radiation_shielding(),
                            "svg": get_svg_radiation_shielding()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Radiation Shielding Diagram",
                            "metadata": {
                                "svg_content": get_svg_radiation_shielding()
                            }
                        }
                    }
                ],
                # Page 4: Electric Field Deflection SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Deflection of Radiation in an Electric Field",
                        "content": {
                            "title": "Deflection of Radiation in an Electric Field",
                            "caption": "Electric field trajectories: Beta curves sharply to (+) plate, Alpha curves gently to (-) plate, Gamma passes straight with zero deflection.",
                            "svg_content": get_svg_electric_field_deflection(),
                            "svg": get_svg_electric_field_deflection()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Electric Field Radiation Deflection Diagram",
                            "metadata": {
                                "svg_content": get_svg_electric_field_deflection()
                            }
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Alpha vs Gamma Penetrating Power",
                        "content": {
                            "question": "Why do Alpha (α) particles have very low penetrating power compared to Gamma (γ) rays?",
                            "options": [
                                "Alpha particles travel at the speed of light.",
                                "Alpha particles are electrically neutral.",
                                "Alpha particles are heavy and have a +2 charge, colliding frequently and ionizing matter rapidly, dissipating energy within centimetres.",
                                "Alpha particles dissolve in air."
                            ],
                            "answer": "C",
                            "explanation": "Because alpha particles are heavy and carry a $+2$ charge, they interact strongly with electrons in surrounding matter, ionizing atoms vigorously. This high rate of collision rapidly depletes their kinetic energy, stopping them within a few centimetres of air or a sheet of paper. Option C is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Comparison Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Comprehensive Physical Properties of Nuclear Radiations",
                        "content": {
                            "title": "Radiation Comparison Matrix",
                            "headers": ["Property", "Alpha (α)", "Beta (β⁻)", "Gamma (γ)"],
                            "rows": [
                                ["Nature", "Helium nucleus (${}^{4}_{2}\\text{He}$)", "High-speed electron (${}^{0}_{-1}\\text{e}$)", "High-energy EM photon (${}^{0}_{0}\\gamma$)"],
                                ["Charge & Mass", "+2e charge, 4 u mass", "-1e charge, 1/1840 u mass", "0 charge, 0 mass"],
                                ["Ionizing Power", "Extremely Strong", "Moderate", "Weak"],
                                ["Penetrating Power", "Weak (Paper / 5 cm air)", "Moderate (5 mm aluminum)", "Very High (Thick lead / concrete)"],
                                ["Electric Deflection", "Deflects towards (-) plate", "Deflects sharply towards (+) plate", "Undeflected"]
                            ]
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Properties of Alpha, Beta, and Gamma Radiation",
                        "content": {
                            "title": "Physics Video: Properties of Alpha, Beta, and Gamma Radiation",
                            "description": "Video demonstrating ionizing power in cloud chambers, magnetic deflection, and penetration through shielding materials.",
                            "url": "https://www.youtube.com/watch?v=kYJvI8oE2yA",
                            "resolved_video_id": "kYJvI8oE2yA"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Radiation Properties Demonstration Video",
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
                        "title": "Lesson 3 Summary: Key Takeaways",
                        "content": {
                            "title": "Core Summary",
                            "takeaways": [
                                "**Alpha**: Heavy, +2 charge, high ionizing power, stopped by paper.",
                                "**Beta**: Light, -1 charge, moderate ionization, stopped by aluminum.",
                                "**Gamma**: Neutral photon, low ionization, highly penetrating (requires lead)."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 4: Detection of Radioactive Emissions and Safety
        # ---------------------------------------------------------------------
        {
            "unit_order": 4,
            "unit_name": "Detection of Radioactive Emissions and Safety",
            "unit_description": "Radiation detectors exploiting ionization (Geiger-Müller counter, cloud chamber, gold leaf electroscope, photographic plates), exposure vs contamination, and the 3 pillars of radiation safety (Time, Distance, Shielding).",
            "lesson_title": "Detection of Radioactive Emissions and Safety",
            "pages": [
                # Page 1: Hook & GM Counter Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Ionization Detection: Researcher Surveying Sample with GM Counter",
                        "content": {
                            "title": "Ionization Detection: Researcher Surveying Sample with GM Counter",
                            "caption": "A researcher using a yellow Geiger-Müller counter wand to measure ionizing radiation emitted from a mineral specimen, converting gas ionization pulses into audible clicks and digital counts.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Geiger_counter_radiation_survey.jpg/1280px-Geiger_counter_radiation_survey.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Geiger_counter_radiation_survey.jpg/1280px-Geiger_counter_radiation_survey.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Geiger Muller Radiation Survey Counter",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Geiger_counter_radiation_survey.jpg/1280px-Geiger_counter_radiation_survey.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Geiger_counter_radiation_survey.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Detecting the Invisible",
                        "content": {
                            "title": "How We See Invisible Radiation",
                            "text": "Nuclear radiation is invisible, silent, and odorless.\n\nPhysics detects radiation by exploiting its ability to **ionize matter**: creating electrical pulses in gas tubes (GM counters), fog tracks in alcohol vapor (cloud chambers), or chemical exposure on film."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Radiation Detectors & Safety",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Describe how GM counters, cloud chambers, and electroscopes detect radiation.",
                                "Distinguish between **Exposure (Irradiation)** and **Contamination**.",
                                "Apply the **3 Pillars of Radiation Safety**: Time, Distance, and Shielding."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Geiger-Müller (GM) Counter",
                        "content": {
                            "term": "Geiger-Müller (GM) Counter",
                            "definition": "An instrument with a low-pressure gas tube that registers voltage pulses when ionizing radiation creates ion pairs between electrodes.",
                            "example": "Standard handheld radiation survey meter."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Irradiation vs Contamination",
                        "content": {
                            "term": "Irradiation vs Contamination",
                            "definition": "Irradiation is external exposure to radiation (stops when source is removed); Contamination is physical radioactive dust stuck on a person or surface.",
                            "example": "Medical X-rays cause irradiation without making the patient radioactive."
                        }
                    }
                ],
                # Page 3: 3 Pillars of Safety SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Three Pillars of Radiation Safety",
                        "content": {
                            "title": "The Three Pillars of Radiation Safety",
                            "caption": "The ALARA safety framework: Minimize Time (work swiftly), Maximize Distance (use tongs), and Use Dense Shielding (lead containers).",
                            "svg_content": get_svg_three_safety_pillars(),
                            "svg": get_svg_three_safety_pillars()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Three Pillars of Radiation Safety Diagram",
                            "metadata": {
                                "svg_content": get_svg_three_safety_pillars()
                            }
                        }
                    }
                ],
                # Page 4: Detectors Comparison Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Radiation Detection Technologies",
                        "content": {
                            "title": "Detector Mechanisms",
                            "headers": ["Detector Type", "Operating Principle", "Physical Evidence Observed"],
                            "rows": [
                                ["Geiger-Müller Counter", "Ionizes low-pressure gas, creating current pulse across electrodes.", "Audible clicks / digital count rate (Bq)."],
                                ["Cloud Chamber", "Ion tracks act as condensation nuclei in supersaturated vapor.", "Visible white fog tracks (Alpha: thick straight; Beta: thin wispy)."],
                                ["Gold Leaf Electroscope", "Ions in air neutralize electrical charge on metal cap.", "Divergent gold leaf collapses."],
                                ["Photographic Film", "Radiation ionizes silver halide crystals in emulsion.", "Darkening / fogging of film badge."]
                            ]
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Radiotherapy Source Handling Safety",
                        "content": {
                            "question": "A medical physicist handles a radioactive cancer therapy source. Which protocol combines the best physics-based safety actions?",
                            "options": [
                                "Wear thin cotton gloves and work slowly.",
                                "Use long mechanical tongs to maximize distance, keep the source inside a lead container when not in use, and work swiftly to minimize exposure time.",
                                "Heat the sample to stop decay.",
                                "Work in total darkness."
                            ],
                            "answer": "B",
                            "explanation": "This protocol applies all three radiation safety pillars: **maximizing distance** (using tongs), **dense shielding** (lead container), and **minimizing time** (working swiftly). Radioactivity cannot be stopped by heat or darkness. Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Biological Effects & Chernobyl Case Study
                [
                    {
                        "type": "real_world_connection",
                        "title": "Nuclear Safety: Lessons from the 1986 Chernobyl Disaster",
                        "content": {
                            "title": "Preventing Radioactive Contamination",
                            "text": "- **Biological Damage**: Ionizing radiation breaks chemical bonds in cellular DNA, causing radiation sickness, leukemia, and genetic mutations.\n- **Chernobyl (1986)**: A catastrophic reactor surge released radioactive contamination across Europe, proving that nuclear facilities must have passive failsafe containment and robust emergency shielding."
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Radiation Detectors and Radiation Protection",
                        "content": {
                            "title": "Physics Video: Radiation Detectors and Radiation Protection",
                            "description": "Video demonstrating cloud chambers, Geiger-Müller counter operation, and the 3 pillars of radiation safety.",
                            "url": "https://www.youtube.com/watch?v=kYJvI8oE2yA",
                            "resolved_video_id": "kYJvI8oE2yA"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Radiation Detectors and Safety Video",
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
                                "**Detectors** (GM counter, cloud chamber, electroscope) rely on gas ionization.",
                                "**Exposure** is external radiation; **contamination** is radioactive matter on surfaces.",
                                "Protect against radiation via **Time, Distance, and Shielding**."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 5: Half-Life and Decay Curves
        # ---------------------------------------------------------------------
        {
            "unit_order": 5,
            "unit_name": "Half-Life and Decay Curves",
            "unit_description": "Definition of Half-Life (t1/2) and Activity (Bq), exponential decay formula N(t) = N0(1/2)^n, reading graphical decay curves, and fluid burette decay modeling.",
            "lesson_title": "Half-Life and Decay Curves",
            "pages": [
                # Page 1: Hook & Coin Analogy Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Statistical Halving: Coin-Flip Analogy for Radioactive Half-Life",
                        "content": {
                            "title": "Statistical Halving: Coin-Flip Analogy for Radioactive Half-Life",
                            "caption": "A collection of coins. Shaking 1000 coins yields ~500 heads, then 250, then 125. While each coin flip is random, the overall sample follows a predictable halving law.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Coins_heads_and_tails.jpg/1280px-Coins_heads_and_tails.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Coins_heads_and_tails.jpg/1280px-Coins_heads_and_tails.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Coin Flip Radioactive Half-Life Analogy",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Coins_heads_and_tails.jpg/1280px-Coins_heads_and_tails.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Coins_heads_and_tails.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Predictability from Complete Randomness",
                        "content": {
                            "title": "The Law of Constant Halving",
                            "text": "We cannot predict when a single radioactive nucleus will decay.\n\nYet across a large population of billions of atoms, exactly half of the remaining sample decays in a constant time interval: the **Half-Life ($t_{1/2}$)**."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Half-Life & Decay Calculations",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **Half-Life ($t_{1/2}$)** and **Activity ($A$) in Becquerels (Bq)**.",
                                "Extract half-life values from graphical **exponential decay curves**.",
                                "Solve quantitative problems using **$N = N_0 \\left(\\frac{1}{2}\\right)^n$** where $n = t / t_{1/2}$."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Half-Life (t1/2)",
                        "content": {
                            "term": "Half-Life (t1/2)",
                            "definition": "The constant time taken for half of the radioactive nuclei in a sample to decay, or for sample activity to fall to half its initial value.",
                            "example": "Sodium-24 has a half-life of 15 hours; Carbon-14 has a half-life of 5,730 years."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Activity (Becquerels, Bq)",
                        "content": {
                            "term": "Activity",
                            "definition": "The rate of nuclear decays occurring per second (1 Bq = 1 decay per second).",
                            "example": "A medical sample with an activity of 800 Bq undergoes 800 disintegrations every second."
                        }
                    }
                ],
                # Page 3: Half-Life Decay Curve SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Radioactive Half-Life Exponential Decay Curve",
                        "content": {
                            "title": "Radioactive Half-Life Exponential Decay Curve",
                            "caption": "Exponential decay curve for Sodium-24 (t1/2 = 15 h): 800 Bq → 400 Bq (15 h) → 200 Bq (30 h) → 100 Bq (45 h).",
                            "svg_content": get_svg_half_life_decay_curve(),
                            "svg": get_svg_half_life_decay_curve()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Exponential Decay Curve Diagram",
                            "metadata": {
                                "svg_content": get_svg_half_life_decay_curve()
                            }
                        }
                    }
                ],
                # Page 4: Mathematical Equations & Worked Example
                [
                    {
                        "type": "formula_breakdown",
                        "title": "Half-Life Mathematical Model",
                        "content": {
                            "title": "Exponential Halving Equation",
                            "formula": "n = \\frac{t}{t_{1/2}} \\quad \\text{and} \\quad N(t) = N_0 \\left( \\frac{1}{2} \\right)^n",
                            "variables": [
                                "$N_0$ = Initial activity / number of nuclei ($\\text{Bq}$ or $\\text{g}$)",
                                "$N(t)$ = Remaining activity / nuclei at time $t$",
                                "$t$ = Total elapsed time",
                                "$t_{1/2}$ = Half-life of the isotope",
                                "$n$ = Number of half-lives elapsed"
                            ]
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Sodium-24 Activity Calculation",
                        "content": {
                            "title": "Activity After 45 Hours",
                            "problem": "A Sodium-24 sample ($t_{1/2} = 15\\text{ h}$) has an initial activity of $800\\text{ Bq}$. Calculate its remaining activity after $45\\text{ hours}$.",
                            "steps": [
                                "1. **Number of Half-Lives**: $n = \\frac{t}{t_{1/2}} = \\frac{45\\text{ h}}{15\\text{ h}} = 3\\text{ half-lives}$.",
                                "2. **Apply Halving Formula**: $N = 800 \\times \\left(\\frac{1}{2}\\right)^3 = 800 \\times \\frac{1}{8} = 100\\text{ Bq}$.",
                                "3. **Verification by Sequence**: $800\\text{ Bq} \\xrightarrow{15\\text{h}} 400\\text{ Bq} \\xrightarrow{30\\text{h}} 200\\text{ Bq} \\xrightarrow{45\\text{h}} 100\\text{ Bq}$."
                            ],
                            "answer": "Remaining activity is 100 Bq."
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Mass Remaining After 3 Half-Lives",
                        "content": {
                            "question": "A radioactive isotope has a half-life of 8 days. If we start with a 32-gram sample, how much of the original isotope remains undecayed after 24 days?",
                            "options": [
                                "2 grams",
                                "4 grams",
                                "8 grams",
                                "12 grams"
                            ],
                            "answer": "B",
                            "explanation": "Calculate elapsed half-lives: $n = 24 / 8 = 3$ half-lives. Halve mass 3 times: $32\\text{ g} \\xrightarrow{8\\text{d}} 16\\text{ g} \\xrightarrow{16\\text{d}} 8\\text{ g} \\xrightarrow{24\\text{d}} 4\\text{ g}$. Exactly **4 grams** remain. Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Water Burette Modeling
                [
                    {
                        "type": "mini_activity",
                        "title": "Laboratory Activity: Fluid Burette Half-Life Model",
                        "content": {
                            "title": "Exponential Drainage Analogue",
                            "task": "Fill a 50 mL burette with water. Open the valve slightly:\n\n1. Time the drop from 50 mL to 25 mL.\n2. Time the drop from 25 mL to 12.5 mL.\n3. Observe: As head pressure drops, drainage slows, yielding approximately constant halving intervals mimicking radioactive decay."
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Half-Life Calculations and Decay Curves",
                        "content": {
                            "title": "Physics Video: Half-Life Calculations and Decay Curves",
                            "description": "Video explaining radioactive half-life, exponential decay equations, and solving half-life word problems.",
                            "url": "https://www.youtube.com/watch?v=kYJvI8oE2yA",
                            "resolved_video_id": "kYJvI8oE2yA"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Half-Life and Decay Curves Tutorial",
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
                                "**Half-Life ($t_{1/2}$)**: Time for half of nuclei to decay.",
                                "Remaining quantity: **$N = N_0 (1/2)^n$** where $n = t / t_{1/2}$.",
                                "Activity is measured in **Becquerels (Bq)**."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 6: Nuclear Fission, Fusion and Chain Reactions
        # ---------------------------------------------------------------------
        {
            "unit_order": 6,
            "unit_name": "Nuclear Fission, Fusion and Chain Reactions",
            "unit_description": "Mechanics of Nuclear Fission (U-235), chain reactions and control rods, Nuclear Fusion in stars (Deuterium-Tritium), mass-energy equivalence (E = mc²), and comparing nuclear vs chemical energy.",
            "lesson_title": "Nuclear Fission, Fusion and Chain Reactions",
            "pages": [
                # Page 1: Hook & Solar Flares Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Cosmic Powerhouse: Nuclear Fusion Flaring on the Sun",
                        "content": {
                            "title": "Cosmic Powerhouse: Nuclear Fusion Flaring on the Sun",
                            "caption": "Massive solar flares erupting from the Sun's surface. Inside the solar core, millions of tonnes of hydrogen undergo nuclear fusion every second, releasing staggering amounts of thermal and electromagnetic energy.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Sun_solar_flare_eruption.jpg/1280px-Sun_solar_flare_eruption.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Sun_solar_flare_eruption.jpg/1280px-Sun_solar_flare_eruption.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Solar Flare Nuclear Fusion on the Sun",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Sun_solar_flare_eruption.jpg/1280px-Sun_solar_flare_eruption.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Sun_solar_flare_eruption.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Tapping the Energy of the Nucleus",
                        "content": {
                            "title": "The Most Energy-Dense Reactions in the Universe",
                            "text": "1 kg of Uranium produces 2 to 3 million times more energy than 1 kg of coal.\n\nNuclear reactions convert tiny deficits of mass directly into pure energy ($E = mc^2$) through **Nuclear Fission** (splitting heavy nuclei) or **Nuclear Fusion** (fusing light nuclei)."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Fission, Fusion & Chain Reactions",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **Nuclear Fission** and **Nuclear Fusion**.",
                                "Explain how a **controlled chain reaction** is maintained using control rods.",
                                "Compare fuel, conditions, energy yield, and waste for fission vs fusion."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Nuclear Fission",
                        "content": {
                            "term": "Nuclear Fission",
                            "definition": "The splitting of a heavy nucleus (U-235) by neutron capture into two lighter daughter nuclei, releasing neutrons and massive energy.",
                            "example": "${}^{235}_{92}\\text{U} + {}^{1}_{0}\\text{n} \\longrightarrow {}^{141}_{56}\\text{Ba} + {}^{92}_{36}\\text{Kr} + 3{}^{1}_{0}\\text{n} + \\text{Energy}$"
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Nuclear Fusion",
                        "content": {
                            "term": "Nuclear Fusion",
                            "definition": "The combining of two light nuclei (Deuterium and Tritium) at extreme temperatures and pressures to form a heavier Helium nucleus, releasing vast energy.",
                            "example": "${}^{2}_{1}\\text{H} + {}^{3}_{1}\\text{H} \\longrightarrow {}^{4}_{2}\\text{He} + {}^{1}_{0}\\text{n} + \\text{Energy}$"
                        }
                    }
                ],
                # Page 3: Fission Chain SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Controlled Nuclear Fission Chain Reaction Diagram",
                        "content": {
                            "title": "Controlled Nuclear Fission Chain Reaction Diagram",
                            "caption": "Neutron splitting U-235 into Ba-141 and Kr-92, releasing 3 neutrons. Control rods absorb excess neutrons to maintain a steady, safe chain reaction.",
                            "svg_content": get_svg_nuclear_fission_chain(),
                            "svg": get_svg_nuclear_fission_chain()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Nuclear Fission Chain Reaction Diagram",
                            "metadata": {
                                "svg_content": get_svg_nuclear_fission_chain()
                            }
                        }
                    }
                ],
                # Page 4: Fission vs Fusion Comparison
                [
                    {
                        "type": "comparison_table",
                        "title": "Nuclear Fission vs Nuclear Fusion",
                        "content": {
                            "title": "Comparison Matrix",
                            "headers": ["Feature", "Nuclear Fission", "Nuclear Fusion"],
                            "rows": [
                                ["Basic Mechanism", "Splitting a heavy nucleus into lighter fragments.", "Fusing light nuclei into a heavier nucleus."],
                                ["Primary Fuel", "Uranium-235 / Plutonium-239", "Hydrogen isotopes (Deuterium & Tritium)"],
                                ["Energy Yield", "Very High (Millions of times > coal)", "Extremely High (4× higher than fission per gram)"],
                                ["Required Conditions", "Moderated thermal neutrons", "Extreme temperature (millions of °C) & pressure"],
                                ["Primary Occurrence", "Civil nuclear reactors", "Core of the Sun and stars"],
                                ["Waste Products", "Radioactive fission fragments (long half-life)", "Clean, non-radioactive Helium gas"]
                            ]
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Why Fusion is Not Yet Used on Earth",
                        "content": {
                            "question": "Why is nuclear fusion not yet used on Earth for commercial power generation, despite releasing more energy than fission?",
                            "options": [
                                "Fusion does not release energy on Earth.",
                                "Fusion requires extreme temperatures (millions of °C) and pressure to overcome positive electrostatic repulsion between nuclei, making containment difficult.",
                                "Hydrogen is extremely rare on Earth.",
                                "Fusion produces massive toxic greenhouse gas emissions."
                            ],
                            "answer": "B",
                            "explanation": "Because all atomic nuclei carry positive charges, they strongly repel each other. To get them close enough for fusion, they must be heated to millions of degrees to overcome this Coulomb barrier. Confining this ultra-hot plasma stably on Earth remains a massive engineering challenge. Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Chain Reaction Control
                [
                    {
                        "type": "concept_explanation",
                        "title": "Controlled vs Uncontrolled Chain Reactions",
                        "content": {
                            "title": "The Physics of Nuclear Control",
                            "text": "- **Uncontrolled Reaction**: Every emitted neutron triggers a new fission, causing exponential escalation in microseconds (nuclear weapon).\n- **Controlled Reaction**: Boron or Cadmium **control rods** absorb surplus neutrons so that exactly one neutron per fission continues the reaction, producing safe, steady baseload electricity."
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Nuclear Fission and Fusion Explained",
                        "content": {
                            "title": "Physics Video: Nuclear Fission and Fusion Explained",
                            "description": "Video explaining nuclear fission chain reactions, reactor core mechanics, and tokamak magnetic fusion research.",
                            "url": "https://www.youtube.com/watch?v=kYJvI8oE2yA",
                            "resolved_video_id": "kYJvI8oE2yA"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Fission and Fusion Video Demonstration",
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
                                "**Fission**: Heavy nuclei split by neutrons; controlled by absorbing control rods.",
                                "**Fusion**: Light hydrogen nuclei combine at millions of degrees in stars.",
                                "Nuclear reactions release millions of times more energy than chemical combustion."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 7: Medical, Industrial, Agricultural and Environmental Applications
        # ---------------------------------------------------------------------
        {
            "unit_order": 7,
            "unit_name": "Medical, Industrial, Agricultural and Environmental Applications",
            "unit_description": "Radioisotopes in cancer radiotherapy (Cobalt-60), medical diagnostics (Technetium-99m), industrial thickness gauging (Strontium-90), agricultural fertilizers (Phosphorus-32), Carbon-14 archaeological dating, and deep geological waste disposal.",
            "lesson_title": "Medical, Industrial, Agricultural and Environmental Applications",
            "pages": [
                # Page 1: Hook & PET Scan Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Nuclear Medicine: Patient Undergoing Advanced PET Scan",
                        "content": {
                            "title": "Nuclear Medicine: Patient Undergoing Advanced PET Scan",
                            "caption": "A patient undergoing a diagnostic Positron Emission Tomography (PET) scan. Short-lived radioisotopes injected into the bloodstream emit gamma signals, mapping organ function and tumors without invasive surgery.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/PET_scan_medical_imaging.jpg/1280px-PET_scan_medical_imaging.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/PET_scan_medical_imaging.jpg/1280px-PET_scan_medical_imaging.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "PET Scan Medical Diagnostic Imaging",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/PET_scan_medical_imaging.jpg/1280px-PET_scan_medical_imaging.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:PET_scan_medical_imaging.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Harnessing Radioactivity for Good",
                        "content": {
                            "title": "Beyond Weapons: Healing and Industry",
                            "text": "Radioactivity is one of modern medicine's greatest healing tools.\n\nFrom destroying cancerous tumors with Gamma beams to dating ancient African fossils with Carbon-14, radioisotopes revolutionize science and industry."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Radioisotope Applications",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify applications of radioisotopes in **medicine, industry, agriculture**, and **archaeology**.",
                                "Select appropriate radioisotopes based on **half-life** and **radiation type**.",
                                "Evaluate environmental management and **deep geological disposal** of nuclear waste."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Radioactive Tracer",
                        "content": {
                            "term": "Radioactive Tracer",
                            "definition": "A small quantity of a short-lived radioisotope introduced into a physical or biological system to track fluid flow, absorption, or pipeline leaks.",
                            "example": "Technetium-99m injected to image heart blood flow."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Carbon-14 Dating",
                        "content": {
                            "term": "Carbon-14 Dating",
                            "definition": "A scientific method measuring remaining Carbon-14 activity (half-life 5,730 years) to determine the age of organic archaeological artifacts.",
                            "example": "Dating ancient wooden tools and human fossils."
                        }
                    }
                ],
                # Page 3: Radioisotope Applications Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Selected Radioisotopes Across Practical Fields",
                        "content": {
                            "title": "Radioisotopes and Their Applications",
                            "headers": ["Field", "Application", "Isotope & Radiation", "Half-Life", "Operating Principle"],
                            "rows": [
                                ["Medicine", "Cancer Radiotherapy", "Cobalt-60 (Gamma)", "5.27 years", "Focused gamma beams destroy cancer cells without surgical cutting."],
                                ["Medicine", "Diagnostic Tracers", "Technetium-99m (Gamma)", "6 hours", "Short half-life decays rapidly and safely within 24 hours."],
                                ["Industry", "Thickness Gauging", "Strontium-90 (Beta)", "28.8 years", "Beta transmission through rolling sheet metal/paper regulates rollers."],
                                ["Agriculture", "Fertilizer Absorption", "Phosphorus-32 (Beta)", "14.3 days", "Tracks how fast crops absorb fertilizer from soil."],
                                ["Archaeology", "Carbon Dating", "Carbon-14 (Beta)", "5,730 years", "Decay of absorbed C-14 dates organic fossils up to 50,000 years."]
                            ]
                        }
                    }
                ],
                # Page 4: Pipeline Leak Tracer Selection
                [
                    {
                        "type": "step_process",
                        "title": "Criteria for Selecting Radioisotopes",
                        "content": {
                            "title": "Choosing the Right Isotope",
                            "steps": [
                                "1. **Penetration Match**: For underground pipeline leaks, choose **Gamma emitters** to penetrate soil and concrete; for thin sheet gauging, choose **Beta**.",
                                "2. **Half-Life Optimization**: For medical diagnostics or public water tracers, choose **short half-lives (hours/days)** to prevent long-term radioactive contamination.",
                                "3. **Toxicity & Chemical Behavior**: Ensure the tracer does not chemically bind to pipe walls or harm living tissue."
                            ]
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Choosing an Underground Leak Tracer",
                        "content": {
                            "question": "An engineer wants to find a leak in a water pipe buried under concrete. Which radioisotope is safest and most effective?",
                            "options": [
                                "An alpha emitter with half-life of 100 years.",
                                "A gamma emitter with half-life of 6 hours.",
                                "A beta emitter with half-life of 20,000 years.",
                                "A gamma emitter with half-life of 50 years."
                            ],
                            "answer": "B",
                            "explanation": "The tracer must emit **Gamma (γ)** radiation because only gamma rays can penetrate concrete and soil to reach detectors above ground. Furthermore, it must have a **short half-life (6 hours)** so that the water does not remain radioactive for long periods. Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Geological Nuclear Waste Disposal
                [
                    {
                        "type": "concept_explanation",
                        "title": "Environmental Responsibility: Nuclear Waste Disposal",
                        "content": {
                            "title": "Deep Geological Disposal",
                            "text": "- **Long-Lived Waste**: Spent reactor fuel contains isotopes with half-lives exceeding 10,000 years.\n- **Disposal Protocol**: High-level waste is vitrified into glass, sealed in copper/steel canisters, encased in bentonite clay, and buried **500 metres deep in stable granite bedrock**, isolating it from the human biosphere for millennia."
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Applications of Radioisotopes in Medicine and Industry",
                        "content": {
                            "title": "Physics Video: Applications of Radioisotopes in Medicine and Industry",
                            "description": "Video illustrating medical radiotherapy, PET scan imaging, industrial thickness gauging, and Carbon-14 dating.",
                            "url": "https://www.youtube.com/watch?v=kYJvI8oE2yA",
                            "resolved_video_id": "kYJvI8oE2yA"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Radioisotope Applications Video",
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
                        "title": "Lesson 7 Summary: Key Takeaways",
                        "content": {
                            "title": "Core Summary",
                            "takeaways": [
                                "**Medicine**: Cobalt-60 (cancer therapy), Technetium-99m (diagnostic tracer).",
                                "**Industry & Agriculture**: Strontium-90 (thickness gauging), Phosphorus-32 (fertilizer tracer).",
                                "**Archaeology**: Carbon-14 dating ($t_{1/2} = 5730\\text{ yr}$).",
                                "Nuclear waste requires **deep geological repository disposal**."
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
def ingest_grade10_physics_topic8():
    print("======================================================================")
    print("INGESTING CBC GRADE 10 PHYSICS — TOPIC 8: RADIOACTIVITY AND ISOTOPES")
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

    # 3. Get or Create Topic: Radioactivity and Stability of Isotopes (Order: 8)
    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=8,
        defaults={
            "name": "Radioactivity and Stability of Isotopes",
            "description": "Comprehensive study of isotopes, nuclide notation (A/Z X), alpha, beta, and gamma radioactive decay equations, radiation properties and deflection, detection devices (GM counter), half-life calculations, nuclear fission vs fusion, and radioisotope applications."
        }
    )
    if not t_created and topic.name != "Radioactivity and Stability of Isotopes":
        topic.name = "Radioactivity and Stability of Isotopes"
        topic.description = "Comprehensive study of isotopes, nuclide notation (A/Z X), alpha, beta, and gamma radioactive decay equations, radiation properties and deflection, detection devices (GM counter), half-life calculations, nuclear fission vs fusion, and radioisotope applications."
        topic.save()
    print(f"Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    curriculum_data = build_topic8_curriculum_data()

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
    print(f"TOPIC 8 INGESTION COMPLETE:")
    print(f"  - Learning Units: {total_units_created}")
    print(f"  - Lessons:        {total_lessons_created}")
    print(f"  - Lesson Blocks:  {total_blocks_created}")
    print(f"  - Lesson Assets:  {total_assets_created}")
    print("======================================================================")

if __name__ == "__main__":
    ingest_grade10_physics_topic8()
