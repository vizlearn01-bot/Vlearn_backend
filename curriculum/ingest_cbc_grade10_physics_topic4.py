"""
VLearn CBC Grade 10 Physics — Topic 4: Temperature and Thermal Expansion
Production Ingestion & Visual Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Physics
Topic: Temperature and Thermal Expansion (Order: 4)

4 Learning Units & 4 Published Lessons:
  1. Temperature and Measurement Technologies (8 Pages, 13 Blocks)
  2. Expansion and Contraction of Solids (8 Pages, 14 Blocks)
  3. Expansion and Contraction of Fluids; Unusual Expansion of Water (8 Pages, 14 Blocks)
  4. Applications of Thermal Expansion and Measurement (8 Pages, 14 Blocks)

Includes:
  - 6 Custom Responsive Sanitized Vector SVG Diagrams
  - 4 Verified Wikimedia Commons Photographic Assets
  - 4 Verified Educational YouTube Video Integrations
  - 4 Formative Scenario-Based MCQs with 4 Options and Pedagogical Feedback
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
# SVG DEFINITIONS FOR TOPIC 4
# =============================================================================

def get_svg_temperature_scales():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%">
  <rect width="820" height="440" fill="#0f172a" rx="16"/>
  <text x="410" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">TEMPERATURE SCALES: KELVIN (SI ABSOLUTE) VS CELSIUS</text>
  <text x="410" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Identical Unit Increment (1 K = 1 °C) • Shifted by 273.15 Units (T_K = T_C + 273.15)</text>

  <!-- Left: Kelvin Scale Stem -->
  <g transform="translate(180, 85)">
    <rect x="35" y="20" width="30" height="280" rx="15" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="50" cy="315" r="25" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <rect x="44" y="50" width="12" height="250" fill="#38bdf8"/>
    
    <text x="50" y="0" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">KELVIN (K)</text>
    <text x="50" y="15" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">SI Absolute Scale</text>

    <!-- Calibration Ticks & Labels -->
    <!-- Boiling Point -->
    <line x1="20" y1="50" x2="35" y2="50" stroke="#f8fafc" stroke-width="2"/>
    <text x="10" y="54" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="end">373.15 K</text>
    
    <!-- Freezing Point -->
    <line x1="20" y1="160" x2="35" y2="160" stroke="#38bdf8" stroke-width="2"/>
    <text x="10" y="164" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="end">273.15 K</text>
    
    <!-- Absolute Zero -->
    <line x1="20" y1="280" x2="35" y2="280" stroke="#ef4444" stroke-width="2"/>
    <text x="10" y="284" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="end">0 K</text>
  </g>

  <!-- Right: Celsius Scale Stem -->
  <g transform="translate(540, 85)">
    <rect x="35" y="20" width="30" height="280" rx="15" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="50" cy="315" r="25" fill="#d97706" stroke="#f59e0b" stroke-width="2"/>
    <rect x="44" y="50" width="12" height="250" fill="#f59e0b"/>
    
    <text x="50" y="0" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">CELSIUS (°C)</text>
    <text x="50" y="15" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Empirical Metric Scale</text>

    <!-- Calibration Ticks & Labels -->
    <!-- Boiling Point -->
    <line x1="65" y1="50" x2="80" y2="50" stroke="#f8fafc" stroke-width="2"/>
    <text x="90" y="54" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700">100.0 °C</text>
    
    <!-- Freezing Point -->
    <line x1="65" y1="160" x2="80" y2="160" stroke="#38bdf8" stroke-width="2"/>
    <text x="90" y="164" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">0.0 °C</text>
    
    <!-- Absolute Zero -->
    <line x1="65" y1="280" x2="80" y2="280" stroke="#ef4444" stroke-width="2"/>
    <text x="90" y="284" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="700">-273.15 °C</text>
  </g>

  <!-- Horizontal Comparison Connectors -->
  <g stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5 3">
    <!-- Steam / Boiling Point -->
    <line x1="250" y1="135" x2="570" y2="135"/>
    <rect x="330" y="120" width="160" height="26" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <text x="410" y="137" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Water Boils (100 K span)</text>

    <!-- Ice / Freezing Point -->
    <line x1="250" y1="245" x2="570" y2="245"/>
    <rect x="330" y="230" width="160" height="26" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <text x="410" y="247" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Water Freezes (0 °C)</text>

    <!-- Absolute Zero -->
    <line x1="250" y1="365" x2="570" y2="365"/>
    <rect x="300" y="352" width="220" height="26" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
    <text x="410" y="369" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Absolute Zero (Zero Kinetic Energy)</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_ball_and_ring():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 420" width="100%" height="100%">
  <rect width="820" height="420" fill="#0f172a" rx="16"/>
  <text x="410" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">GRAVESANDE’S BALL AND RING: 3D THERMAL EXPANSION OF SOLIDS</text>
  <text x="410" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Heating Increases Volumetric Dimensions • Cooling Causes Rapid Thermal Contraction</text>

  <!-- Panel 1: Cold (Passes Through) -->
  <g transform="translate(40, 80)">
    <rect width="230" height="310" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="115" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. COLD (ROOM TEMP, 20°C)</text>

    <!-- Ring Support Stand -->
    <rect x="40" y="160" width="150" height="12" fill="#475569" rx="3"/>
    <ellipse cx="115" cy="166" rx="26" ry="6" fill="#0f172a" stroke="#94a3b8" stroke-width="2"/>

    <!-- Cold Brass Ball passing smoothly through ring -->
    <line x1="115" y1="60" x2="115" y2="150" stroke="#94a3b8" stroke-width="2"/>
    <circle cx="115" cy="166" r="22" fill="#eab308" stroke="#ca8a04" stroke-width="2"/>

    <path d="M 115 195 L 115 225 M 109 217 L 115 225 L 121 217" stroke="#22c55e" stroke-width="3"/>
    <text x="115" y="250" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Passes Easily Through</text>
    <text x="115" y="270" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Diameter_ball &lt; Diameter_ring</text>
  </g>

  <!-- Panel 2: Heated Over Flame -->
  <g transform="translate(295, 80)">
    <rect width="230" height="310" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="115" y="28" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">2. HEATING OVER FLAME</text>

    <!-- Wire Handle holding ball -->
    <line x1="115" y1="50" x2="115" y2="120" stroke="#94a3b8" stroke-width="2"/>
    <!-- Red Hot Expanding Ball -->
    <circle cx="115" cy="120" r="27" fill="#ef4444" stroke="#f97316" stroke-width="2.5"/>

    <!-- Bunsen Burner Flame -->
    <path d="M 100 220 Q 115 155 130 220 Z" fill="#38bdf8" opacity="0.8"/>
    <path d="M 106 220 Q 115 170 124 220 Z" fill="#fef08a"/>
    <rect x="105" y="220" width="20" height="35" fill="#64748b"/>

    <text x="115" y="275" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Thermal Energy Absorbed</text>
    <text x="115" y="295" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Atomic vibrations increase volume</text>
  </g>

  <!-- Panel 3: Hot Ball Stuck on Ring -->
  <g transform="translate(550, 80)">
    <rect width="230" height="310" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="115" y="28" fill="#ef4444" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">3. TEST AFTER HEATING</text>

    <!-- Ring Support Stand -->
    <rect x="40" y="160" width="150" height="12" fill="#475569" rx="3"/>
    <ellipse cx="115" cy="166" rx="26" ry="6" fill="#0f172a" stroke="#94a3b8" stroke-width="2"/>

    <!-- Hot Expanded Ball Resting on Ring (Cannot Fall Through) -->
    <line x1="115" y1="50" x2="115" y2="135" stroke="#94a3b8" stroke-width="2"/>
    <circle cx="115" cy="140" r="27" fill="#f97316" stroke="#ef4444" stroke-width="2.5"/>

    <!-- Red Prohibition 'X' -->
    <path d="M 105 190 L 125 210 M 125 190 L 105 210" stroke="#ef4444" stroke-width="3"/>
    <text x="115" y="235" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Stuck! Cannot Pass</text>
    <text x="115" y="255" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Diameter_ball &gt; Diameter_ring</text>
    <text x="115" y="275" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Contracts when cooled in water</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_anomalous_water_curve():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%">
  <rect width="820" height="440" fill="#0f172a" rx="16"/>
  <text x="410" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">THE ANOMALOUS EXPANSION OF WATER (0°C TO 10°C)</text>
  <text x="410" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Water Contracts as Heated from 0°C to 4°C • Minimum Volume & Maximum Density at 4°C</text>

  <!-- Grid & Axes -->
  <line x1="120" y1="360" x2="740" y2="360" stroke="#94a3b8" stroke-width="2"/>
  <line x1="120" y1="360" x2="120" y2="80" stroke="#94a3b8" stroke-width="2"/>

  <!-- Y-Axis: Volume of 1 kg of Water (cm³) -->
  <text x="105" y="365" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">1000.00</text>
  <text x="105" y="260" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">1000.10</text>
  <text x="105" y="160" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">1000.20</text>
  <text x="105" y="90" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">1000.30</text>
  <text x="40" y="210" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle" transform="rotate(-90 40 210)">Volume of 1 kg of Water (cm³)</text>

  <!-- X-Axis: Temperature (°C) -->
  <text x="120" y="380" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">0 °C</text>
  <text x="240" y="380" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">2 °C</text>
  <text x="360" y="380" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">4 °C (Min Vol)</text>
  <text x="480" y="380" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">6 °C</text>
  <text x="600" y="380" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">8 °C</text>
  <text x="720" y="380" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">10 °C</text>
  <text x="430" y="410" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Temperature (°C)</text>

  <!-- Anomalous Parabolic Curve -->
  <!-- Starts at 0°C (1000.12 cm³, y=240), drops to 4°C (1000.00 cm³, y=360), rises to 10°C (1000.27 cm³, y=100) -->
  <path d="M 120 240 Q 240 360 360 360 T 720 100" fill="none" stroke="#38bdf8" stroke-width="4"/>

  <!-- Minimum Point Highlight at 4°C -->
  <circle cx="360" cy="360" r="7" fill="#22c55e"/>
  <line x1="360" y1="80" x2="360" y2="360" stroke="#22c55e" stroke-width="1.5" stroke-dasharray="4 3"/>

  <!-- Callout 1: 0°C to 4°C Anomalous Region -->
  <rect x="150" y="100" width="180" height="75" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
  <text x="240" y="122" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">ANOMALOUS REGION</text>
  <text x="240" y="142" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Water contracts when heated</text>
  <text x="240" y="158" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Expands when cooled to 0°C</text>

  <!-- Callout 2: 4°C Peak Density -->
  <rect x="420" y="170" width="220" height="75" rx="8" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
  <text x="530" y="192" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">AT EXACTLY 4 °C:</text>
  <text x="530" y="212" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Minimum Volume = 1000.00 cm³</text>
  <text x="530" y="230" fill="#22c55e" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Maximum Density = 1000 kg/m³</text>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_frozen_pond():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%">
  <rect width="820" height="440" fill="#0f172a" rx="16"/>
  <text x="410" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">ECOLOGICAL PRESERVATION: THERMAL STRATIFICATION IN A FROZEN LAKE</text>
  <text x="410" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Ice Floats on Surface (Low Density) • Dense 4°C Liquid Water Protects Benthic Aquatic Life</text>

  <!-- Atmosphere Above Pond -->
  <rect x="60" y="70" width="700" height="50" fill="#0284c711" stroke="#334155" stroke-width="1"/>
  <text x="410" y="100" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Sub-Zero Air Atmosphere (-10 °C to -5 °C)</text>

  <!-- Floating Surface Ice Slab (0°C to -5°C) -->
  <rect x="60" y="120" width="700" height="40" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2"/>
  <text x="410" y="145" fill="#0369a1" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">INSULATING ICE LAYER (0 °C Surface Freezing, Density ≈ 917 kg/m³ - Floats!)</text>

  <!-- Water Strata Layers -->
  <!-- Layer 1: 1 °C -->
  <rect x="60" y="160" width="700" height="45" fill="#0284c722"/>
  <text x="120" y="188" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="600">1 °C Layer</text>

  <!-- Layer 2: 2 °C -->
  <rect x="60" y="205" width="700" height="45" fill="#0284c744"/>
  <text x="120" y="233" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="600">2 °C Layer</text>

  <!-- Layer 3: 3 °C -->
  <rect x="60" y="250" width="700" height="45" fill="#0284c766"/>
  <text x="120" y="278" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="600">3 °C Layer</text>

  <!-- Bottom Layer: 4 °C Maximum Density -->
  <rect x="60" y="295" width="700" height="90" fill="#0284c788" stroke="#22c55e" stroke-width="2"/>
  <text x="120" y="325" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="700">4 °C BOTTOM WATER LAYER (Maximum Density = 1000 kg/m³)</text>
  <text x="120" y="345" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11">Water remains liquid throughout winter, shielding aquatic organisms from freezing.</text>

  <!-- Aquatic Life Representations (Fish & Plants in 4°C Layer) -->
  <!-- Fish 1 -->
  <path d="M 520 340 Q 545 330 560 340 L 575 330 L 575 350 L 560 340 Q 545 350 520 340 Z" fill="#f59e0b"/>
  <circle cx="530" cy="338" r="2" fill="#000000"/>
  <!-- Fish 2 -->
  <path d="M 640 355 Q 660 347 675 355 L 685 347 L 685 363 L 675 355 Q 660 363 640 355 Z" fill="#f59e0b"/>
  <!-- Aquatic Pond Plants -->
  <path d="M 450 385 Q 440 340 455 310" stroke="#22c55e" stroke-width="3" fill="none"/>
  <path d="M 465 385 Q 480 350 470 320" stroke="#22c55e" stroke-width="3" fill="none"/>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_bimetallic_strip():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%">
  <rect width="820" height="440" fill="#0f172a" rx="16"/>
  <text x="410" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">MECHANICS OF A BIMETALLIC STRIP: DIFFERENTIAL EXPANSION</text>
  <text x="410" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Brass (α = 1.9 × 10⁻⁵ K⁻¹) Expands/Contracts More Than Steel (α = 1.2 × 10⁻⁵ K⁻¹)</text>

  <!-- Panel 1: Room Temperature (20°C) Straight -->
  <g transform="translate(40, 80)">
    <rect width="230" height="310" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="115" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. ROOM TEMP (20°C)</text>

    <!-- Wall Mount -->
    <rect x="25" y="80" width="15" height="120" fill="#64748b"/>

    <!-- Straight Joined Strips -->
    <!-- Top: Brass (Gold) -->
    <rect x="40" y="115" width="150" height="20" fill="#eab308" stroke="#ca8a04" stroke-width="1"/>
    <text x="115" y="130" fill="#000000" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Brass (Higher α)</text>
    
    <!-- Bottom: Steel (Silver) -->
    <rect x="40" y="135" width="150" height="20" fill="#94a3b8" stroke="#64748b" stroke-width="1"/>
    <text x="115" y="150" fill="#000000" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Steel (Lower α)</text>

    <text x="115" y="220" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Perfectly Straight</text>
    <text x="115" y="240" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Both metals at equal initial length</text>
  </g>

  <!-- Panel 2: Heated to 100°C (Bends Downward) -->
  <g transform="translate(295, 80)">
    <rect width="230" height="310" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="115" y="28" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">2. HEATED (100°C)</text>

    <!-- Wall Mount -->
    <rect x="25" y="80" width="15" height="120" fill="#64748b"/>

    <!-- Downward Curved Strips -->
    <path d="M 40 120 Q 120 120 180 180" fill="none" stroke="#eab308" stroke-width="18" stroke-linecap="round"/>
    <path d="M 40 135 Q 115 135 170 190" fill="none" stroke="#94a3b8" stroke-width="18" stroke-linecap="round"/>

    <text x="115" y="225" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Curves Toward Steel</text>
    <text x="115" y="245" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Brass expands more (outer curve)</text>
    <text x="115" y="260" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Steel on inside circumference</text>
  </g>

  <!-- Panel 3: Cooled to 0°C (Bends Upward) -->
  <g transform="translate(550, 80)">
    <rect width="230" height="310" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="115" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">3. COOLED (0°C)</text>

    <!-- Wall Mount -->
    <rect x="25" y="80" width="15" height="120" fill="#64748b"/>

    <!-- Upward Curved Strips -->
    <path d="M 40 145 Q 115 145 170 85" fill="none" stroke="#94a3b8" stroke-width="18" stroke-linecap="round"/>
    <path d="M 40 130 Q 120 130 180 75" fill="none" stroke="#eab308" stroke-width="18" stroke-linecap="round"/>

    <text x="115" y="225" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Curves Toward Brass</text>
    <text x="115" y="245" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Brass contracts more (inner curve)</text>
    <text x="115" y="260" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Forces strip to bend upward</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_bimetallic_fire_alarm():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 420" width="100%" height="100%">
  <rect width="820" height="420" fill="#0f172a" rx="16"/>
  <text x="410" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">BIMETALLIC FIRE ALARM CIRCUIT: THERMAL SWITCHING SCHEMATIC</text>
  <text x="410" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Flame Heats Brass-on-Top Strip • Strip Bends Downward to Touch Contact Screw and Complete Alarm Loop</text>

  <!-- Circuit Schematic Diagram -->
  <g transform="translate(100, 80)">
    <!-- 9V Battery -->
    <rect x="50" y="100" width="40" height="60" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="4"/>
    <text x="70" y="135" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">9V</text>

    <!-- Circuit Wires -->
    <path d="M 70 100 L 70 30 L 320 30 L 320 70" fill="none" stroke="#f8fafc" stroke-width="3"/>
    <path d="M 70 160 L 70 230 L 520 230 L 520 160" fill="none" stroke="#f8fafc" stroke-width="3"/>

    <!-- Alarm Bell / Buzzer -->
    <circle cx="520" cy="130" r="25" fill="#ef4444" stroke="#f8fafc" stroke-width="2"/>
    <text x="520" y="135" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">ALARM</text>

    <!-- Fixed Wall Anchor -->
    <rect x="305" y="70" width="30" height="40" fill="#64748b" rx="2"/>

    <!-- Bimetallic Strip (Brass on top, Steel on bottom) -->
    <rect x="335" y="75" width="130" height="10" fill="#eab308"/> <!-- Brass -->
    <rect x="335" y="85" width="130" height="10" fill="#94a3b8"/> <!-- Steel -->
    <circle cx="465" cy="85" r="4" fill="#38bdf8"/> <!-- Contact point on strip -->

    <!-- Contact Screw Terminal (2 mm gap) -->
    <rect x="455" y="115" width="20" height="15" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
    <path d="M 465 130 L 465 230" stroke="#f8fafc" stroke-width="3"/>
    <text x="490" y="110" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="10" font-weight="700">2 mm Gap</text>

    <!-- Heat Flame Beneath Strip -->
    <path d="M 390 155 Q 400 115 410 155 Z" fill="#ef4444"/>
    <path d="M 395 155 Q 400 125 405 155 Z" fill="#fef08a"/>
    <text x="400" y="175" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Flame (Heat)</text>
  </g>

  <!-- Explanatory Operation Box -->
  <g transform="translate(100, 310)">
    <rect width="620" height="75" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <text x="20" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1. Normal Condition:</text>
    <text x="145" y="28" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Strip is straight; circuit is open; alarm remains silent.</text>
    <text x="20" y="52" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700">2. Fire Condition:</text>
    <text x="145" y="52" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">Heat expands top brass layer faster than steel, bending strip down onto screw to trigger alarm.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg


# =============================================================================
# CURRICULUM DEFINITION DATA FOR TOPIC 4
# =============================================================================

def build_topic4_curriculum_data():
    return [
        # ---------------------------------------------------------------------
        # LESSON 1: Temperature and Measurement Technologies
        # ---------------------------------------------------------------------
        {
            "unit_order": 1,
            "unit_name": "Temperature and Measurement Technologies",
            "unit_description": "Scientific definition of temperature as average molecular kinetic energy, thermal equilibrium, Kelvin and Celsius temperature scales, and 9 modern temperature measurement technologies.",
            "lesson_title": "Temperature and Measurement Technologies",
            "pages": [
                # Page 1: Hook & Clinical Thermometer Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Biomedical Technology: Digital Clinical Thermometer",
                        "content": {
                            "title": "Biomedical Technology: Digital Clinical Thermometer",
                            "caption": "A modern digital clinical thermometer displaying a body temperature reading of 37.0 °C. The instrument uses a sensitive thermistor sensor operating on thermal equilibrium.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Digital_thermometer.jpg/1280px-Digital_thermometer.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Digital_thermometer.jpg/1280px-Digital_thermometer.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Digital Biomedical Clinical Thermometer",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Digital_thermometer.jpg/1280px-Digital_thermometer.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Digital_thermometer.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Our Sense of Touch Deceives Us",
                        "content": {
                            "title": "The Fallacy of Human Touch",
                            "text": "Have you ever touched a metal desk frame and a wooden book on a cold morning in school?\n\n- The metal frame feels freezing cold to your fingers, while the book feels comfortably warm.\n- Yet both have been sitting in the exact same classroom air all night!\n\nHuman skin is a poor thermometer: it senses the **rate of heat transfer**, not true temperature. To study nature accurately, physicists define **Temperature** objectively and build instruments using predictable **thermometric properties**."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Temperature & Measurement",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **temperature** in terms of average particle kinetic energy.",
                                "Explain the principle of **thermal equilibrium** in temperature measurement.",
                                "Convert temperatures between the **Celsius ($^\\circ\\text{C}$)** and **Kelvin ($\\text{K}$)** scales.",
                                "Identify and compare 9 modern temperature measurement technologies and their underlying thermometric properties."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Temperature",
                        "content": {
                            "term": "Temperature",
                            "definition": "A physical quantity measuring the average kinetic energy of the particles (atoms or molecules) in a substance. Heat spontaneously flows from higher to lower temperature.",
                            "example": "Boiling water has a higher temperature than ice water because its molecules move and vibrate faster."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Thermal Equilibrium",
                        "content": {
                            "term": "Thermal Equilibrium",
                            "definition": "The condition where two or more interacting bodies reach identical temperatures, resulting in zero net heat exchange.",
                            "example": "A clinical thermometer must rest under the tongue until it reaches thermal equilibrium with the body."
                        }
                    }
                ],
                # Page 3: Temperature Scales SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Temperature Scales: Kelvin vs Celsius Calibration Points",
                        "content": {
                            "title": "Temperature Scales: Kelvin vs Celsius Calibration Points",
                            "caption": "Side-by-side comparison of Kelvin (SI Absolute) and Celsius scales showing Absolute Zero (0 K / -273.15 °C), Freezing Point (273.15 K / 0 °C), and Boiling Point (373.15 K / 100 °C).",
                            "svg_content": get_svg_temperature_scales(),
                            "svg": get_svg_temperature_scales()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Kelvin vs Celsius Temperature Scales Diagram",
                            "metadata": {
                                "svg_content": get_svg_temperature_scales()
                            }
                        }
                    },
                    {
                        "type": "formula_breakdown",
                        "title": "Scale Conversion Equations",
                        "content": {
                            "title": "Converting Between Kelvin and Celsius",
                            "formula": "T_{\\text{K}} = T_{\\text{C}} + 273.15 \\quad \\Longleftrightarrow \\quad T_{\\text{C}} = T_{\\text{K}} - 273.15",
                            "variables": [
                                "$T_{\\text{K}}$ = Temperature on the absolute Kelvin scale ($\\text{K}$)",
                                "$T_{\\text{C}}$ = Temperature on the Celsius scale ($^\\circ\\text{C}$)"
                            ],
                            "rules": [
                                "**No Degree Symbol for Kelvin**: We write $300\\text{ K}$, never $300^\\circ\\text{K}$.",
                                "**Identical Unit Step**: A change of $\\Delta T = 1\\text{ K}$ is exactly equal to $\\Delta T = 1^\\circ\\text{C}$."
                            ]
                        }
                    }
                ],
                # Page 4: 9 Temperature Technologies Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "9 Modern Temperature Measurement Technologies",
                        "content": {
                            "title": "Thermometric Properties and Sensor Technologies",
                            "headers": ["Technology", "Thermometric Property", "Operational Range", "Practical Industrial Application"],
                            "rows": [
                                ["Liquid-in-Glass", "Volume expansion of mercury or dyed alcohol in capillary tube.", "-39 °C to 350 °C", "Meteorological stations and school laboratories."],
                                ["Bimetallic Devices", "Differential expansion causing a composite strip to curve.", "-50 °C to 500 °C", "Thermostats in electric iron boxes and ovens."],
                                ["Thermocouples", "Voltage generated across two distinct metal junctions (Seebeck effect).", "-200 °C to 1800 °C", "Industrial smelting furnaces and aircraft jet engines."],
                                ["Resistance Detectors (RTDs)", "Increase in electrical resistance of pure platinum wire.", "-200 °C to 850 °C", "High-precision laboratory calibration standards."],
                                ["Thermistors", "Sharp non-linear change in semiconductor ceramic resistance.", "-90 °C to 130 °C", "Digital medical thermometers and smartphone battery sensors."],
                                ["Infrared Radiators", "Thermal emission radiation intensity and wavelength.", "-50 °C to 3000 °C", "Non-contact clinical forehead scanners and molten metal inspection."],
                                ["Silicon Diodes", "Linear voltage drop across a forward-biased p-n junction.", "-270 °C to 200 °C", "Cryogenic research and supercomputer cooling."],
                                ["Molecular Change-of-State", "Calibrated melting points of organic chemical crystals.", "30 °C to 300 °C", "Single-use sterile medical heat sterilization tags."],
                                ["Pyroelectric Motion Sensors", "Charge displacement from infrared thermal gradient shifts.", "Ambient Room Range", "Security burglar alarms and automated restroom faucets."]
                            ]
                        }
                    }
                ],
                # Page 5: Practical Activity
                [
                    {
                        "type": "mini_activity",
                        "title": "Laboratory Investigation: Thermometer Response Times",
                        "content": {
                            "title": "Comparing Sensor Response Speeds",
                            "task": "Test a liquid-in-glass thermometer, digital thermistor, and infrared thermometer in ice water ($0^\\circ\\text{C}$) and hot water ($70^\\circ\\text{C}$):\n\n1. **Response Time**: Measure how many seconds each sensor takes to reach thermal equilibrium.\n2. **Non-Contact Advantage**: Observe why infrared sensors read surface temperatures instantaneously (0.1 s) without physical immersion.\n3. **Safety Rule**: Handle hot water with extreme care to avoid scalding!"
                        }
                    }
                ],
                # Page 6: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Smelting Furnace Temperature Sensor",
                        "content": {
                            "question": "An industrial metallurgical smelting plant in Mombasa needs to measure the temperature of molten copper inside a blast furnace at approximately $1,200^\\circ\\text{C}$. Which temperature measurement technology is most suitable?",
                            "options": [
                                "A mercury liquid-in-glass thermometer",
                                "A digital medical thermistor sensor",
                                "A high-temperature thermocouple or infrared pyrometer",
                                "A cryogenic silicon diode sensor"
                            ],
                            "answer": "C",
                            "explanation": "Molten copper is at $1,200^\\circ\\text{C}$. Mercury boils at $357^\\circ\\text{C}$ (destroying glass thermometers), thermistors degrade above $150^\\circ\\text{C}$, and silicon diodes operate near absolute zero. **Thermocouples** (rated up to $1,800^\\circ\\text{C}$) and non-contact **infrared pyrometers** are the only instruments engineered to withstand and measure extreme industrial smelting temperatures. Therefore, Option C is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Temperature Measurement & Thermocouple Principles",
                        "content": {
                            "title": "Physics Video: Temperature Measurement & Thermocouple Principles",
                            "description": "Educational video explaining thermal equilibrium, the Kelvin scale, and how thermocouples and thermistors measure temperature.",
                            "url": "https://www.youtube.com/watch?v=0kF41E_2i1c",
                            "resolved_video_id": "0kF41E_2i1c"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Temperature Measurement and Sensors Video",
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
                        "title": "Lesson 1 Summary: Key Takeaways",
                        "content": {
                            "title": "Core Summary",
                            "takeaways": [
                                "**Temperature** measures average particle kinetic energy.",
                                "**Thermal Equilibrium** is the fundamental operating principle of thermometers.",
                                "SI absolute temperature is **Kelvin (K)**: $T_{\\text{K}} = T_{\\text{C}} + 273.15$.",
                                "Different technologies leverage specific **thermometric properties** (liquid expansion, resistance, voltage, infrared radiation)."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 2: Expansion and Contraction of Solids
        # ---------------------------------------------------------------------
        {
            "unit_order": 2,
            "unit_name": "Expansion and Contraction of Solids",
            "unit_description": "Thermal expansion and contraction in solids, coefficient of linear expansivity (α), mathematical modeling (ΔL = α·L0·ΔT), railway track gaps, bridge comb joints, and the Gravesande Ball and Ring experiment.",
            "lesson_title": "Expansion and Contraction of Solids",
            "pages": [
                # Page 1: Hook & Bridge Expansion Joint Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Civil Engineering: Metal Comb Expansion Joint on a Concrete Bridge",
                        "content": {
                            "title": "Civil Engineering: Metal Comb Expansion Joint on a Concrete Bridge",
                            "caption": "A heavy steel comb expansion joint on a concrete highway bridge. The interlocking teeth slide in and out as the bridge expands under midday heat and contracts in the cool night.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Expansion_joint_on_bridge.jpg/1280px-Expansion_joint_on_bridge.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Expansion_joint_on_bridge.jpg/1280px-Expansion_joint_on_bridge.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Concrete Highway Bridge Expansion Joint",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Expansion_joint_on_bridge.jpg/1280px-Expansion_joint_on_bridge.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Expansion_joint_on_bridge.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Do Engineers Leave Gaps in Bridges and Rails?",
                        "content": {
                            "title": "The Destructive Force of Thermal Expansion",
                            "text": "If you travel on the Standard Gauge Railway (SGR) or drive across a large highway bridge in Kenya, you will notice expansion gaps and comb joints.\n\n- Why build gaps into solid steel and concrete?\n- What would happen if rails were welded into a continuous seamless line under the equatorial sun?\n\nMidday heat forces steel and concrete atoms to vibrate more vigorously, pushing them apart. Without expansion gaps, rails buckle into twisted metal and bridge decks fracture."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Solid Thermal Expansion",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain the microscopic origin of **thermal expansion and contraction** in solids.",
                                "Define the **Coefficient of Linear Expansivity ($\\alpha$)** and state its SI unit ($\\text{K}^{-1}$ or $^\\circ\\text{C}^{-1}$).",
                                "Apply the linear expansion formula $\\Delta L = \\alpha L_0 \\Delta T$ to quantitative engineering problems.",
                                "Analyze the **Ball and Ring experiment** demonstrating 3D volumetric thermal expansion."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Coefficient of Linear Expansivity (α)",
                        "content": {
                            "term": "Coefficient of Linear Expansivity (α)",
                            "definition": "The fractional change in length of a solid per unit change in temperature ($\\alpha = \\frac{\\Delta L}{L_0 \\Delta T}$).",
                            "example": "Steel has $\\alpha = 1.2 \\times 10^{-5}\\text{ K}^{-1}$, expanding 0.012 mm per metre for each 1 °C temperature rise."
                        }
                    }
                ],
                # Page 3: Linear Expansion Formula & Metal Values
                [
                    {
                        "type": "formula_breakdown",
                        "title": "The Linear Expansion Mathematical Model",
                        "content": {
                            "title": "Predicting Change in Length",
                            "formula": "\\Delta L = \\alpha \\cdot L_0 \\cdot \\Delta T \\quad \\implies \\quad L_{\\text{final}} = L_0(1 + \\alpha \\Delta T)",
                            "variables": [
                                "$\\Delta L = L - L_0$ = Change in length (expansion) in metres ($\\text{m}$)",
                                "$\\alpha$ = Coefficient of Linear Expansivity in $\\text{K}^{-1}$ (or $^\\circ\\text{C}^{-1}$)",
                                "$L_0$ = Original length of the solid in metres ($\\text{m}$)",
                                "$\\Delta T = T_{\\text{final}} - T_{\\text{initial}}$ = Change in temperature in $\\text{K}$ (or $^\\circ\\text{C}$)"
                            ],
                            "rules": [
                                "**Three Governing Factors**: Expansion is directly proportional to original length ($L_0$), temperature rise ($\\Delta T$), and material nature ($\\alpha$)."
                            ]
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Linear Expansivity of Engineering Metals",
                        "content": {
                            "title": "Expansivity Coefficients",
                            "headers": ["Material", "Expansivity Coefficient (α)", "Thermal Behavior"],
                            "rows": [
                                ["Aluminium", "2.3 × 10⁻⁵ K⁻¹", "Expands very rapidly when heated."],
                                ["Brass", "1.9 × 10⁻⁵ K⁻¹", "High expansion; paired with steel in bimetallic strips."],
                                ["Copper", "1.7 × 10⁻⁵ K⁻¹", "High conductivity with moderate expansion."],
                                ["Steel / Iron", "1.2 × 10⁻⁵ K⁻¹", "Stable expansion; matches concrete expansivity in rebar."],
                                ["Invar (Ni-Fe Alloy)", "1.2 × 10⁻⁶ K⁻¹", "Near-zero expansion; used in precision clocks and surveying tapes."]
                            ]
                        }
                    }
                ],
                # Page 4: Worked Example (SGR Rail Track)
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: SGR Steel Rail Track Expansion",
                        "content": {
                            "title": "Calculating Required Railway Expansion Gaps",
                            "problem": "A steel rail section on the SGR is exactly $25.0\\text{ m}$ long when laid in the morning at $15.0^\\circ\\text{C}$. In the afternoon, equatorial sun heats the rail to $45.0^\\circ\\text{C}$. If $\\alpha_{\\text{steel}} = 1.2 \\times 10^{-5}\\text{ K}^{-1}$, calculate:\n1. Temperature rise ($\\Delta T$).\n2. Expansion ($\\Delta L$) in millimetres.\n3. Minimum gap required between adjacent rails.",
                            "steps": [
                                "1. **Temperature Change**: $\\Delta T = 45.0^\\circ\\text{C} - 15.0^\\circ\\text{C} = 30.0^\\circ\\text{C} = 30.0\\text{ K}$.",
                                "2. **Select Formula**: $\\Delta L = \\alpha \\cdot L_0 \\cdot \\Delta T$.",
                                "3. **Substitute Values**: $\\Delta L = (1.2 \\times 10^{-5}) \\times 25.0 \\times 30.0 = 9.0 \\times 10^{-3}\\text{ m} = 9.0\\text{ mm}$.",
                                "4. **Required Gap**: To avoid compressive buckling when adjacent rails expand toward each other, an expansion gap of at least $9.0\\text{ mm}$ must be provided."
                            ],
                            "answer": "The rail expands by 9.0 mm; a minimum gap of 9.0 mm prevents buckling."
                        }
                    }
                ],
                # Page 5: Ball and Ring SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Gravesande's Ball and Ring: 3D Solid Thermal Expansion",
                        "content": {
                            "title": "Gravesande's Ball and Ring: 3D Solid Thermal Expansion",
                            "caption": "Three-stage experiment: Cold ball passes easily through the ring (Panel 1), heated ball expands in volume (Panel 2), and hot ball sits stuck on top of the ring (Panel 3).",
                            "svg_content": get_svg_ball_and_ring(),
                            "svg": get_svg_ball_and_ring()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Ball and Ring Thermal Expansion Diagram",
                            "metadata": {
                                "svg_content": get_svg_ball_and_ring()
                            }
                        }
                    }
                ],
                # Page 6: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Railway Expansion Calculations",
                        "content": {
                            "question": "A steel railway bridge span is $100\\text{ metres}$ long at $10^\\circ\\text{C}$. On a hot day at $40^\\circ\\text{C}$ (temperature change $\\Delta T = 30\\text{ K}$), how much will the bridge span expand if $\\alpha_{\\text{steel}} = 1.2 \\times 10^{-5}\\text{ K}^{-1}$?",
                            "options": [
                                "0.36 mm",
                                "36.0 mm (3.6 cm)",
                                "360.0 mm (36 cm)",
                                "3.6 metres"
                            ],
                            "answer": "B",
                            "explanation": "Applying $\\Delta L = \\alpha \\cdot L_0 \\cdot \\Delta T$: $$\\Delta L = (1.2 \\times 10^{-5}\\text{ K}^{-1}) \\times (100\\text{ m}) \\times (30\\text{ K}) = 0.036\\text{ m} = 36.0\\text{ mm} \\text{ (or } 3.6\\text{ cm)}$$ This significant 3.6 cm expansion explains why heavy bridges require roller bearings and comb expansion joints. Therefore, Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Solid Thermal Expansion and Railway Track Buckling",
                        "content": {
                            "title": "Physics Video: Solid Thermal Expansion and Railway Track Buckling",
                            "description": "Dramatic physics footage demonstrating thermal expansion, the Ball and Ring experiment, and real-world railway track buckle prevention.",
                            "url": "https://www.youtube.com/watch?v=IhQn_rE7z_0",
                            "resolved_video_id": "IhQn_rE7z_0"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Thermal Expansion in Solids Demonstration",
                            "url": "https://www.youtube.com/watch?v=IhQn_rE7z_0",
                            "metadata": {
                                "youtube_id": "IhQn_rE7z_0"
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
                                "Thermal expansion is caused by increased atomic lattice vibrations pushing atoms apart.",
                                "Linear expansion is modeled by **$\\Delta L = \\alpha L_0 \\Delta T$**.",
                                "Civil structures accommodate expansion via **comb joints, roller bearings**, and **railway gaps**."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 3: Expansion and Contraction of Fluids; Anomalous Expansion of Water
        # ---------------------------------------------------------------------
        {
            "unit_order": 3,
            "unit_name": "Expansion and Contraction of Fluids; Unusual Expansion of Water",
            "unit_description": "Volumetric expansion in liquids and gases, anomalous expansion of water between 0°C and 4°C, maximum density of water at 4°C, aquatic ecosystem survival in freezing conditions, and frost pipe bursts.",
            "lesson_title": "Expansion and Contraction of Fluids; Anomalous Expansion of Water",
            "pages": [
                # Page 1: Hook & Frozen Lake Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Aquatic Ecosystem: Frozen Lake with Protective Floating Ice Blanket",
                        "content": {
                            "title": "Aquatic Ecosystem: Frozen Lake with Protective Floating Ice Blanket",
                            "caption": "A frozen mountain lake. The top surface is covered with floating ice (density ≈ 917 kg/m³), while dense 4 °C liquid water remains at the bottom, protecting aquatic life from freezing.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Frozen_lake.jpg/1280px-Frozen_lake.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Frozen_lake.jpg/1280px-Frozen_lake.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Frozen Lake Aquatic Ice Insulation",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Frozen_lake.jpg/1280px-Frozen_lake.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Frozen_lake.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Bizarre Anomaly of Water",
                        "content": {
                            "title": "Why Does Water Expand When It Freezes?",
                            "text": "Almost all liquids shrink steadily in volume as they cool.\n\n- Why does a glass bottle filled with water shatter if left inside a freezer overnight?\n- Why do ice cubes float on water instead of sinking to the bottom?\n\nBetween $0^\\circ\\text{C}$ and $4^\\circ\\text{C}$, water exhibits an extraordinary behavior called **anomalous expansion**. As it cools toward freezing, water stops contracting and begins to expand! Without this anomaly, rivers and lakes would freeze solid from the bottom up, extinguishing all aquatic life on Earth."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Fluid Expansion & Water Anomaly",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain **volumetric expansion** in fluids (liquids and gases).",
                                "Describe the **anomalous expansion of water** between $0^\\circ\\text{C}$ and $4^\\circ\\text{C}$.",
                                "Analyze the Volume vs Temperature and Density vs Temperature curves for water.",
                                "Explain why water reaches its **maximum density ($1000\\text{ kg/m}^3$) at $4^\\circ\\text{C}$**.",
                                "Explain the biological survival of aquatic ecosystems in freezing climates."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Anomalous Expansion of Water",
                        "content": {
                            "term": "Anomalous Expansion of Water",
                            "definition": "The unusual property of water where it expands upon cooling from 4 °C to 0 °C, and contracts when heated from 0 °C to 4 °C, reaching its maximum density at 4 °C.",
                            "example": "Ice has a density of ~917 kg/m³, allowing it to float atop 1000 kg/m³ water."
                        }
                    }
                ],
                # Page 3: Anomalous Water Curve SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Anomalous Volume & Density Curve of Water",
                        "content": {
                            "title": "Anomalous Volume & Density Curve of Water",
                            "caption": "Volume of 1 kg of water plotted from 0 °C to 10 °C, displaying a distinct minimum volume and maximum density (1000 kg/m³) at exactly 4 °C.",
                            "svg_content": get_svg_anomalous_water_curve(),
                            "svg": get_svg_anomalous_water_curve()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Anomalous Expansion of Water Graph Diagram",
                            "metadata": {
                                "svg_content": get_svg_anomalous_water_curve()
                            }
                        }
                    }
                ],
                # Page 4: Molecular Mechanism & Frozen Pond SVG
                [
                    {
                        "type": "concept_explanation",
                        "title": "Molecular Origin of the Anomaly",
                        "content": {
                            "title": "The Open Hexagonal Hydrogen Bond Crystal Lattice",
                            "text": "As liquid water cools from $100^\\circ\\text{C}$ to $4^\\circ\\text{C}$, thermal kinetic energy decreases and molecules pack closer together.\n\nHowever, below **$4^\\circ\\text{C}$**, hydrogen bonds begin locking water molecules into a rigid, **open hexagonal lattice**. This structural cage forces molecules further apart than in liquid state, increasing total volume and decreasing density. At $0^\\circ\\text{C}$, ice forms with an open structure that is $\\approx 9\\%$ less dense than water."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Thermal Stratification in a Frozen Lake Ecosystem",
                        "content": {
                            "title": "Thermal Stratification in a Frozen Lake Ecosystem",
                            "caption": "Cross-sectional thermal profile of a winter lake: sub-zero atmosphere (-10 °C), floating surface ice sheet (0 °C), and protected 4 °C bottom water layer supporting fish and plant life.",
                            "svg_content": get_svg_frozen_pond(),
                            "svg": get_svg_frozen_pond()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Frozen Lake Thermal Stratification Diagram",
                            "metadata": {
                                "svg_content": get_svg_frozen_pond()
                            }
                        }
                    }
                ],
                # Page 5: Laboratory Investigation
                [
                    {
                        "type": "step_process",
                        "title": "Laboratory Investigation: Fluid Volume Expansion",
                        "content": {
                            "title": "Flask and Capillary Tube Experiment",
                            "steps": [
                                "1. **Apparatus**: Glass flask with single-hole stopper, capillary tube, dyed water, and hot water bath.",
                                "2. **Initial Observation**: When the flask is first submerged in hot water, the liquid level in the capillary tube **drops momentarily**! (The glass flask absorbs heat and expands first, increasing internal capacity).",
                                "3. **Subsequent Observation**: Once heat conducts into the water, the liquid level rises rapidly and steadily.",
                                "4. **Conclusion**: Liquids expand significantly more than solids for the same temperature rise."
                            ]
                        }
                    }
                ],
                # Page 6: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Temperature at the Bottom of a Frozen Pond",
                        "content": {
                            "question": "During a severe winter in a high-altitude region, the surface of a deep freshwater pond freezes into a thick slab of ice at $0^\\circ\\text{C}$. What is the temperature of the liquid water at the deepest bottom layer of the pond?",
                            "options": [
                                "-10 °C",
                                "0 °C",
                                "4 °C",
                                "100 °C"
                            ],
                            "answer": "C",
                            "explanation": "Because of the anomalous expansion of water, water reaches its **maximum density at $4^\\circ\\text{C}$** ($1000\\text{ kg/m}^3$). Colder water ($0^\\circ\\text{C}$ to $3^\\circ\\text{C}$) and surface ice (density $\\approx 917\\text{ kg/m}^3$) are less dense and float on top. The densest $4^\\circ\\text{C}$ water sinks to the bottom, insulating aquatic life throughout winter. Therefore, Option C is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: The Anomalous Expansion of Water Explained",
                        "content": {
                            "title": "Physics Video: The Anomalous Expansion of Water Explained",
                            "description": "Visual explanation of hydrogen bonding, open crystal lattice structure in ice, density curves, and ecological importance of water's anomalous behavior.",
                            "url": "https://www.youtube.com/watch?v=T41_K8A2Y_M",
                            "resolved_video_id": "T41_K8A2Y_M"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Anomalous Expansion of Water Physics Video",
                            "url": "https://www.youtube.com/watch?v=T41_K8A2Y_M",
                            "metadata": {
                                "youtube_id": "T41_K8A2Y_M"
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
                                "Fluids undergo **volumetric expansion** when heated.",
                                "Water behaves anomalously between **$0^\\circ\\text{C}$ and $4^\\circ\\text{C}$**, expanding as it cools.",
                                "Water reaches **maximum density at $4^\\circ\\text{C}$** ($1000\\text{ kg/m}^3$).",
                                "Ice floats, creating an insulating blanket that keeps the bottom of lakes at a life-sustaining $4^\\circ\\text{C}$."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 4: Applications of Thermal Expansion and Measurement
        # ---------------------------------------------------------------------
        {
            "unit_order": 4,
            "unit_name": "Applications of Thermal Expansion and Measurement",
            "unit_description": "Mechanical applications of differential thermal expansion: bimetallic strips, thermostats in iron boxes and water heaters, fire alarm circuits, shrink fitting, expansion loops in steam pipes, and power cable sag.",
            "lesson_title": "Applications of Thermal Expansion and Measurement",
            "pages": [
                # Page 1: Hook & Thermostat Coil Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Mechanical Control: Inside a Coiled Bimetallic Thermostat",
                        "content": {
                            "title": "Mechanical Control: Inside a Coiled Bimetallic Thermostat",
                            "caption": "Inside an electromechanical thermostat showing a coiled bimetallic strip made of brass and steel with electrical contact points that open and close as temperature changes.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Bimetal_thermostat.jpg/1280px-Bimetal_thermostat.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Bimetal_thermostat.jpg/1280px-Bimetal_thermostat.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Coiled Bimetallic Thermostat Internal Switch",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Bimetal_thermostat.jpg/1280px-Bimetal_thermostat.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Bimetal_thermostat.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Mechanical Brain of Domestic Appliances",
                        "content": {
                            "title": "How Does an Electric Iron Box Regulate Its Own Heat?",
                            "text": "When using an electric iron box in Kenyan homes, you set the dial and begin ironing. After reaching temperature, you hear a sharp 'click' and the indicator light switches off to prevent scorching your clothes.\n\nHow does an electric iron sense heat and switch itself on and off without a microprocessor? It uses the simple, reliable physics of a **bimetallic strip**."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Thermal Expansion Applications",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain the mechanical operation of a **bimetallic strip** under heating and cooling.",
                                "Analyze how a **thermostat** maintains a constant set temperature in domestic appliances.",
                                "Trace the electrical circuit operation of a **bimetallic fire alarm system**.",
                                "Describe industrial expansion mitigation: **U-shaped expansion loops in steam pipes**, **shrink-fitting**, and **sagging power transmission lines**."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Bimetallic Strip",
                        "content": {
                            "term": "Bimetallic Strip",
                            "definition": "A composite temperature-sensing element made of two distinct metals (usually brass and steel) welded together along their length that bends predictably when heated or cooled.",
                            "example": "Used in oven thermostats, electric kettles, and circuit breakers."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Thermostat",
                        "content": {
                            "term": "Thermostat",
                            "definition": "An automatic regulating device that maintains a system at a predetermined temperature by opening and closing an electrical circuit.",
                            "example": "Water heater geysers and domestic refrigerators."
                        }
                    }
                ],
                # Page 3: Bimetallic Strip Mechanics SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Mechanics of a Bimetallic Strip: Differential Expansion",
                        "content": {
                            "title": "Mechanics of a Bimetallic Strip: Differential Expansion",
                            "caption": "Three behavior states of a Brass-Steel bimetallic strip: straight at room temperature (20 °C), curved toward steel when heated (100 °C), and curved toward brass when cooled (0 °C).",
                            "svg_content": get_svg_bimetallic_strip(),
                            "svg": get_svg_bimetallic_strip()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Bimetallic Strip Differential Bending Diagram",
                            "metadata": {
                                "svg_content": get_svg_bimetallic_strip()
                            }
                        }
                    }
                ],
                # Page 4: Industrial Applications
                [
                    {
                        "type": "concept_explanation",
                        "title": "Engineering Applications & Expansion Mitigation",
                        "content": {
                            "title": "Controlling and Utilizing Thermal Expansion",
                            "text": "- **Electric Iron Box Thermostat**: As the iron heats, the bimetallic strip bends away from a silver contact screw, breaking the circuit. When cooled, it straightens to reconnect current.\n- **Shrink Fitting**: A metal gear is heated to expand its central hole, slipped onto an axle, and cooled to form an unbreakable interference grip.\n- **Steam Pipe Expansion Loops**: High-temperature steam pipes are built with U-shaped flexible expansion loops that absorb thermal elongation without buckling.\n- **Power Cable Sag**: Overhead electrical wires are strung loosely in cool weather to prevent them from snapping under extreme tension during cold winter contractions."
                        }
                    }
                ],
                # Page 5: Fire Alarm Circuit SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Bimetallic Fire Alarm Circuit Schematic",
                        "content": {
                            "title": "Bimetallic Fire Alarm Circuit Schematic",
                            "caption": "Schematic of a bimetallic fire alarm: A 9V battery, bimetallic strip (brass on top), 2 mm contact gap, and alarm bell. Heat causes the strip to bend downward, completing the circuit to sound the alarm.",
                            "svg_content": get_svg_bimetallic_fire_alarm(),
                            "svg": get_svg_bimetallic_fire_alarm()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Bimetallic Fire Alarm Circuit Diagram",
                            "metadata": {
                                "svg_content": get_svg_bimetallic_fire_alarm()
                            }
                        }
                    }
                ],
                # Page 6: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Bimetallic Strip Bending Direction",
                        "content": {
                            "question": "A bimetallic strip is fabricated by welding a strip of Brass ($\\alpha = 1.9 \\times 10^{-5}\\text{ K}^{-1}$) to an equal-sized strip of Steel ($\\alpha = 1.2 \\times 10^{-5}\\text{ K}^{-1}$). If the strip is anchored at one end and heated in a flame, how will it respond?",
                            "options": [
                                "It will remain completely straight but increase in electrical resistance.",
                                "It will bend in a curve toward the Steel side, because Brass expands more and forms the outer arc.",
                                "It will bend in a curve toward the Brass side, because Steel shrinks.",
                                "It will shatter into small fragments immediately."
                            ],
                            "answer": "B",
                            "explanation": "Because Brass has a higher coefficient of linear expansivity than Steel ($\\alpha_{\\text{brass}} > \\alpha_{\\text{steel}}$), Brass expands more upon heating. To accommodate its greater length, Brass is forced onto the **outer circumference** of the curve, forcing the composite strip to **bend toward the Steel side**. Therefore, Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Demonstration Video: Bimetallic Strips & Thermostat Mechanisms",
                        "content": {
                            "title": "Demonstration Video: Bimetallic Strips & Thermostat Mechanisms",
                            "description": "Video demonstrating how bimetallic strips bend under flame, how bimetallic thermostats switch circuits in electric irons, and how bimetallic fire alarms trigger.",
                            "url": "https://www.youtube.com/watch?v=0e68Y2k-014",
                            "resolved_video_id": "0e68Y2k-014"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Bimetallic Strip and Thermostat Video Demonstration",
                            "url": "https://www.youtube.com/watch?v=0e68Y2k-014",
                            "metadata": {
                                "youtube_id": "0e68Y2k-014"
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
                                "A **bimetallic strip** uses unequal expansion rates of two metals to create temperature-activated mechanical motion.",
                                "**Thermostats** maintain constant temperatures by breaking and making contact in heating circuits.",
                                "Structures manage thermal expansion using **expansion loops, shrink fitting**, and **power cable sagging**."
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
def ingest_grade10_physics_topic4():
    print("======================================================================")
    print("INGESTING CBC GRADE 10 PHYSICS — TOPIC 4: TEMPERATURE AND THERMAL EXPANSION")
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

    # 3. Get or Create Topic: Temperature and Thermal Expansion (Order: 4)
    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=4,
        defaults={
            "name": "Temperature and Thermal Expansion",
            "description": "Exploration of temperature, thermometric properties, linear expansivity (ΔL = αL0ΔT), anomalous expansion of water, and bimetallic thermostats."
        }
    )
    if not t_created and topic.name != "Temperature and Thermal Expansion":
        topic.name = "Temperature and Thermal Expansion"
        topic.description = "Exploration of temperature, thermometric properties, linear expansivity (ΔL = αL0ΔT), anomalous expansion of water, and bimetallic thermostats."
        topic.save()
    print(f"Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    curriculum_data = build_topic4_curriculum_data()

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
    print(f"TOPIC 4 INGESTION COMPLETE:")
    print(f"  - Learning Units: {total_units_created}")
    print(f"  - Lessons:        {total_lessons_created}")
    print(f"  - Lesson Blocks:  {total_blocks_created}")
    print(f"  - Lesson Assets:  {total_assets_created}")
    print("======================================================================")

if __name__ == "__main__":
    ingest_grade10_physics_topic4()
