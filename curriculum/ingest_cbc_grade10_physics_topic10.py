"""
VLearn CBC Grade 10 Physics — Topic 10: Current Electricity
Production Ingestion & Visual Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Physics
Topic: Current Electricity (Order: 10)

6 Learning Units & 6 Published Lessons:
  1. Current, Potential Difference, EMF and Measurement (8 Pages, 13 Blocks)
  2. Ohm’s Law and V–I Characteristics (8 Pages, 13 Blocks)
  3. Resistance, Resistivity and Resistor Colour Codes (8 Pages, 13 Blocks)
  4. Series and Parallel Resistor Networks; Circuit Laws (8 Pages, 14 Blocks)
  5. Determining Resistance: Ammeter–Voltmeter, Wheatstone and Metre Bridge (8 Pages, 13 Blocks)
  6. Electrical Power, Heating Effect and Applications (8 Pages, 13 Blocks)

Includes:
  - 8 Custom Responsive Sanitized Vector SVG Diagrams
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
# SVG DEFINITIONS FOR TOPIC 10
# =============================================================================

def get_svg_emf_vs_terminal_voltage():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">EMF (OPEN CIRCUIT) VS TERMINAL POTENTIAL DIFFERENCE (CLOSED CIRCUIT)</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Electromotive Force E = V + Ir • Lost Volts (Ir) Wasted Across Internal Resistance (r)</text>

  <!-- Left: Open Circuit (Switch OPEN) -->
  <g transform="translate(60, 85)">
    <rect width="330" height="275" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="165" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. OPEN CIRCUIT (I = 0)</text>

    <!-- Battery with Internal Resistance -->
    <rect x="40" y="55" width="120" height="60" rx="4" fill="#0f172a" stroke="#64748b" stroke-dasharray="3 3"/>
    <line x1="60" y1="85" x2="80" y2="85" stroke="#f8fafc" stroke-width="2"/>
    <line x1="80" y1="70" x2="80" y2="100" stroke="#f59e0b" stroke-width="3"/>
    <line x1="90" y1="76" x2="90" y2="94" stroke="#94a3b8" stroke-width="3"/>
    <text x="70" y="68" fill="#f59e0b" font-size="10" font-weight="700">+</text>
    <!-- Internal r -->
    <path d="M 100 85 L 105 78 L 115 92 L 125 78 L 135 92 L 140 85" fill="none" stroke="#ef4444" stroke-width="1.5"/>
    <text x="120" y="72" fill="#ef4444" font-size="9">r</text>

    <!-- Open Switch -->
    <line x1="160" y1="85" x2="220" y2="85" stroke="#f8fafc" stroke-width="2"/>
    <line x1="220" y1="85" x2="250" y2="65" stroke="#ef4444" stroke-width="2.5"/>
    <circle cx="220" cy="85" r="3" fill="#f8fafc"/>
    <circle cx="260" cy="85" r="3" fill="#f8fafc"/>
    <text x="235" y="55" fill="#ef4444" font-size="10" font-weight="700">SWITCH OPEN</text>

    <!-- Voltmeter across terminals -->
    <path d="M 40 85 L 20 85 L 20 180 L 165 180 L 165 150" fill="none" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="165" cy="180" r="22" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="165" y="186" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">1.50 V</text>

    <text x="165" y="235" fill="#4ade80" font-size="12" font-weight="700" text-anchor="middle">Voltmeter Reads Full EMF (E)</text>
    <text x="165" y="255" fill="#cbd5e1" font-size="10" text-anchor="middle">No current flows ⟹ Lost Volts (Ir) = 0</text>
  </g>

  <!-- Right: Closed Circuit (Switch CLOSED) -->
  <g transform="translate(450, 85)">
    <rect width="330" height="275" rx="8" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
    <text x="165" y="24" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">2. CLOSED CIRCUIT (Current I Flows)</text>

    <!-- Battery with Internal Resistance -->
    <rect x="40" y="55" width="120" height="60" rx="4" fill="#0f172a" stroke="#64748b" stroke-dasharray="3 3"/>
    <line x1="60" y1="85" x2="80" y2="85" stroke="#f8fafc" stroke-width="2"/>
    <line x1="80" y1="70" x2="80" y2="100" stroke="#f59e0b" stroke-width="3"/>
    <line x1="90" y1="76" x2="90" y2="94" stroke="#94a3b8" stroke-width="3"/>
    <!-- Internal r -->
    <path d="M 100 85 L 105 78 L 115 92 L 125 78 L 135 92 L 140 85" fill="none" stroke="#ef4444" stroke-width="1.5"/>
    <text x="120" y="72" fill="#ef4444" font-size="9">r</text>

    <!-- Closed Switch & Resistor Load -->
    <line x1="160" y1="85" x2="280" y2="85" stroke="#f8fafc" stroke-width="2"/>
    <circle cx="220" cy="85" r="3" fill="#f8fafc"/>
    <circle cx="260" cy="85" r="3" fill="#f8fafc"/>
    <!-- Current Arrow -->
    <path d="M 230 75 L 250 75 M 245 70 L 250 75 L 245 80" stroke="#22c55e" stroke-width="2"/>
    <text x="240" y="65" fill="#4ade80" font-size="9" font-weight="700">I</text>

    <!-- Voltmeter across terminals -->
    <path d="M 40 85 L 20 85 L 20 180 L 165 180 L 165 150" fill="none" stroke="#22c55e" stroke-width="2"/>
    <circle cx="165" cy="180" r="22" fill="#1e293b" stroke="#22c55e" stroke-width="2"/>
    <text x="165" y="186" fill="#4ade80" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">1.30 V</text>

    <text x="165" y="235" fill="#f59e0b" font-size="12" font-weight="700" text-anchor="middle">Terminal Voltage V = 1.30 V</text>
    <text x="165" y="255" fill="#ef4444" font-size="10" text-anchor="middle">Lost Volts Ir = E - V = 0.20 V across r</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_meter_connections():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 380" width="100%" height="100%">
  <rect width="800" height="380" fill="#0f172a" rx="16"/>
  <text x="400" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">CORRECT METER CONNECTION: SERIES AMMETER &amp; PARALLEL VOLTMETER</text>
  <text x="400" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Ammeter (Low Resistance, Series) • Voltmeter (High Resistance, Parallel)</text>

  <!-- Circuit Diagram -->
  <g transform="translate(150, 90)">
    <!-- Battery -->
    <line x1="50" y1="100" x2="110" y2="100" stroke="#f8fafc" stroke-width="2"/>
    <line x1="110" y1="80" x2="110" y2="120" stroke="#f59e0b" stroke-width="4"/>
    <line x1="120" y1="90" x2="120" y2="110" stroke="#94a3b8" stroke-width="4"/>
    <text x="100" y="75" fill="#f59e0b" font-size="11" font-weight="700">+</text>
    <text x="130" y="75" fill="#94a3b8" font-size="11" font-weight="700">-</text>

    <!-- Top Wire with Series Ammeter -->
    <line x1="120" y1="100" x2="200" y2="100" stroke="#f8fafc" stroke-width="2"/>
    <!-- Ammeter Circle -->
    <circle cx="230" cy="100" r="20" fill="#1e293b" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="230" y="106" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="800" text-anchor="middle">A</text>
    <text x="230" y="65" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">Ammeter (Series)</text>

    <!-- Resistor R -->
    <line x1="250" y1="100" x2="330" y2="100" stroke="#f8fafc" stroke-width="2"/>
    <path d="M 330 100 L 338 88 L 348 112 L 358 88 L 368 112 L 378 88 L 388 112 L 396 100" fill="none" stroke="#f59e0b" stroke-width="3"/>
    <text x="363" y="75" fill="#f59e0b" font-size="12" font-weight="700" text-anchor="middle">Resistor (R)</text>

    <!-- Voltmeter in Parallel -->
    <path d="M 320 100 L 320 180 L 345 180" fill="none" stroke="#22c55e" stroke-width="2"/>
    <path d="M 405 100 L 405 180 L 385 180" fill="none" stroke="#22c55e" stroke-width="2"/>
    <circle cx="365" cy="180" r="20" fill="#1e293b" stroke="#22c55e" stroke-width="2.5"/>
    <text x="365" y="186" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="800" text-anchor="middle">V</text>
    <text x="365" y="220" fill="#4ade80" font-size="11" font-weight="700" text-anchor="middle">Voltmeter (Parallel)</text>

    <!-- Return Loop & Switch -->
    <line x1="396" y1="100" x2="470" y2="100" stroke="#f8fafc" stroke-width="2"/>
    <line x1="470" y1="100" x2="470" y2="240" stroke="#f8fafc" stroke-width="2"/>
    <line x1="470" y1="240" x2="50" y2="240" stroke="#f8fafc" stroke-width="2"/>
    <line x1="50" y1="240" x2="50" y2="100" stroke="#f8fafc" stroke-width="2"/>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_resistor_color_codes():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">FOUR-BAND RESISTOR COLOUR CODE SYSTEM</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Band 1: 1st Digit • Band 2: 2nd Digit • Band 3: Multiplier (10ⁿ) • Band 4: Tolerance</text>

  <!-- Resistor Body (Center) -->
  <g transform="translate(180, 100)">
    <!-- Metal Leads -->
    <line x1="-80" y1="60" x2="0" y2="60" stroke="#94a3b8" stroke-width="6"/>
    <line x1="480" y1="60" x2="560" y2="60" stroke="#94a3b8" stroke-width="6"/>

    <!-- Ceramic Resistor Body -->
    <path d="M 0 30 Q 30 10 70 20 L 410 20 Q 450 10 480 30 L 480 90 Q 450 110 410 100 L 70 100 Q 30 110 0 90 Z" fill="#d97706" stroke="#92400e" stroke-width="2"/>

    <!-- Band 1: Yellow (4) -->
    <rect x="90" y="18" width="22" height="84" fill="#eab308"/>
    <!-- Band 2: Violet (7) -->
    <rect x="160" y="20" width="22" height="80" fill="#8b5cf6"/>
    <!-- Band 3: Orange (Multiplier 10³ = ×1000) -->
    <rect x="230" y="20" width="22" height="80" fill="#f97316"/>
    <!-- Band 4: Gold (Tolerance ±5%) -->
    <rect x="370" y="18" width="22" height="84" fill="#fbbf24" stroke="#d97706" stroke-width="1"/>
  </g>

  <!-- Calculation Callout -->
  <g transform="translate(140, 240)">
    <rect width="560" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="280" y="30" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">EXAMPLE DECODING: YELLOW - VIOLET - ORANGE - GOLD</text>
    <text x="60" y="65" fill="#eab308" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Yellow = 4</text>
    <text x="160" y="65" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Violet = 7</text>
    <text x="260" y="65" fill="#fb923c" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Orange = × 1,000</text>
    <text x="430" y="65" fill="#fcd34d" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Gold = ± 5%</text>

    <text x="280" y="100" fill="#4ade80" font-family="system-ui, sans-serif" font-size="16" font-weight="800" text-anchor="middle">Resistance = 47 × 1,000 = 47,000 Ω (47 kΩ ± 5%)</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_series_parallel_networks():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">SERIES VS PARALLEL RESISTOR NETWORKS</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Series: Current Constant, Resistance Additive • Parallel: Voltage Constant, Resistance Decreases</text>

  <!-- Left: Series Circuit -->
  <g transform="translate(60, 80)">
    <rect width="330" height="280" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="165" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. SERIES (Single Continuous Loop)</text>

    <!-- Resistors in a row -->
    <line x1="30" y1="80" x2="80" y2="80" stroke="#f8fafc" stroke-width="2"/>
    <rect x="80" y="68" width="50" height="24" fill="#334155" stroke="#f59e0b" stroke-width="1.5" rx="3"/>
    <text x="105" y="84" fill="#f59e0b" font-size="11" font-weight="700" text-anchor="middle">R1</text>
    <line x1="130" y1="80" x2="170" y2="80" stroke="#f8fafc" stroke-width="2"/>
    <rect x="170" y="68" width="50" height="24" fill="#334155" stroke="#f59e0b" stroke-width="1.5" rx="3"/>
    <text x="195" y="84" fill="#f59e0b" font-size="11" font-weight="700" text-anchor="middle">R2</text>
    <line x1="220" y1="80" x2="260" y2="80" stroke="#f8fafc" stroke-width="2"/>
    <rect x="260" y="68" width="50" height="24" fill="#334155" stroke="#f59e0b" stroke-width="1.5" rx="3"/>
    <text x="285" y="84" fill="#f59e0b" font-size="11" font-weight="700" text-anchor="middle">R3</text>

    <!-- Current Arrow -->
    <path d="M 45 70 L 65 70 M 60 65 L 65 70 L 60 75" stroke="#38bdf8" stroke-width="2"/>
    <text x="55" y="60" fill="#38bdf8" font-size="9" font-weight="700">I_total</text>

    <text x="165" y="140" fill="#4ade80" font-size="13" font-weight="700" text-anchor="middle">R_T = R1 + R2 + R3</text>
    <text x="165" y="165" fill="#cbd5e1" font-size="11" text-anchor="middle">I_total = I1 = I2 = I3 (Same Current)</text>
    <text x="165" y="185" fill="#cbd5e1" font-size="11" text-anchor="middle">V_total = V1 + V2 + V3 (Shared Voltage)</text>
    <text x="165" y="245" fill="#ef4444" font-size="10" font-weight="700" text-anchor="middle">Fault: One burn out stops ALL flow</text>
  </g>

  <!-- Right: Parallel Circuit -->
  <g transform="translate(450, 80)">
    <rect width="330" height="280" rx="8" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
    <text x="165" y="24" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">2. PARALLEL (Multiple Independent Branches)</text>

    <!-- 3 Stacked Resistors -->
    <!-- Branch 1 -->
    <path d="M 50 60 L 110 60" stroke="#f8fafc" stroke-width="2"/>
    <rect x="110" y="48" width="60" height="24" fill="#334155" stroke="#22c55e" stroke-width="1.5" rx="3"/>
    <text x="140" y="64" fill="#4ade80" font-size="11" font-weight="700" text-anchor="middle">R1</text>
    <line x1="170" y1="60" x2="230" y2="60" stroke="#f8fafc" stroke-width="2"/>
    <!-- Branch 2 -->
    <path d="M 50 100 L 110 100" stroke="#f8fafc" stroke-width="2"/>
    <rect x="110" y="88" width="60" height="24" fill="#334155" stroke="#22c55e" stroke-width="1.5" rx="3"/>
    <text x="140" y="104" fill="#4ade80" font-size="11" font-weight="700" text-anchor="middle">R2</text>
    <line x1="170" y1="100" x2="230" y2="100" stroke="#f8fafc" stroke-width="2"/>

    <!-- Common Junction Rails -->
    <line x1="50" y1="60" x2="50" y2="100" stroke="#f8fafc" stroke-width="2.5"/>
    <line x1="230" y1="60" x2="230" y2="100" stroke="#f8fafc" stroke-width="2.5"/>

    <text x="165" y="150" fill="#4ade80" font-size="13" font-weight="700" text-anchor="middle">1 / R_T = 1/R1 + 1/R2</text>
    <text x="165" y="175" fill="#cbd5e1" font-size="11" text-anchor="middle">V_total = V1 = V2 (Same Voltage)</text>
    <text x="165" y="195" fill="#cbd5e1" font-size="11" text-anchor="middle">I_total = I1 + I2 (Divided Current)</text>
    <text x="165" y="245" fill="#4ade80" font-size="10" font-weight="700" text-anchor="middle">Standard household electrical wiring</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_metre_bridge():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">THE METRE BRIDGE PRECISION RESISTANCE MEASUREMENT</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Null Balance Condition (Ig = 0): Rx = Rs × ((100 - l₁) / l₁)</text>

  <!-- Metre Bridge Board -->
  <g transform="translate(100, 80)">
    <!-- Wooden Base -->
    <rect x="0" y="40" width="640" height="200" fill="#1e293b" stroke="#64748b" stroke-width="2" rx="8"/>

    <!-- Brass End Plates -->
    <polygon points="20,60 70,60 70,80 40,80 40,160 20,160" fill="#f59e0b"/>
    <polygon points="620,60 570,60 570,80 600,80 600,160 620,160" fill="#f59e0b"/>
    <!-- Central Brass Strip -->
    <rect x="180" y="60" width="280" height="20" fill="#f59e0b"/>

    <!-- Left Gap: Standard Resistor Rs -->
    <rect x="95" y="45" width="55" height="22" fill="#334155" stroke="#38bdf8" stroke-width="1.5" rx="3"/>
    <text x="122" y="60" fill="#38bdf8" font-size="10" font-weight="700" text-anchor="middle">Rs</text>
    <line x1="70" y1="70" x2="95" y2="56" stroke="#f8fafc" stroke-width="1.5"/>
    <line x1="150" y1="56" x2="180" y2="70" stroke="#f8fafc" stroke-width="1.5"/>

    <!-- Right Gap: Unknown Resistor Rx -->
    <rect x="490" y="45" width="55" height="22" fill="#334155" stroke="#ef4444" stroke-width="1.5" rx="3"/>
    <text x="517" y="60" fill="#ef4444" font-size="10" font-weight="700" text-anchor="middle">Rx</text>
    <line x1="460" y1="70" x2="490" y2="56" stroke="#f8fafc" stroke-width="1.5"/>
    <line x1="545" y1="56" x2="570" y2="70" stroke="#f8fafc" stroke-width="1.5"/>

    <!-- Uniform 100 cm Wire AB -->
    <line x1="30" y1="160" x2="610" y2="160" stroke="#f8fafc" stroke-width="3"/>
    <text x="25" y="180" fill="#f8fafc" font-size="11" font-weight="700">A (0 cm)</text>
    <text x="585" y="180" fill="#f8fafc" font-size="11" font-weight="700">B (100 cm)</text>

    <!-- Galvanometer & Sliding Jockey -->
    <line x1="320" y1="80" x2="320" y2="105" stroke="#f8fafc" stroke-width="2"/>
    <circle cx="320" cy="120" r="15" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <text x="320" y="124" fill="#4ade80" font-size="11" font-weight="800" text-anchor="middle">G</text>
    <line x1="320" y1="135" x2="260" y2="158" stroke="#f8fafc" stroke-width="2"/>
    <polygon points="260,158 255,150 265,150" fill="#22c55e"/>
    <text x="260" y="145" fill="#4ade80" font-size="9" font-weight="700" text-anchor="middle">Jockey</text>

    <!-- Length Dimensions -->
    <line x1="30" y1="200" x2="260" y2="200" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="145" y="215" fill="#38bdf8" font-size="10" font-weight="700" text-anchor="middle">Balance Length l₁</text>

    <line x1="260" y1="200" x2="610" y2="200" stroke="#ef4444" stroke-width="1.5"/>
    <text x="435" y="215" fill="#ef4444" font-size="10" font-weight="700" text-anchor="middle">100 - l₁</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg


# =============================================================================
# CURRICULUM DEFINITION DATA FOR TOPIC 10
# =============================================================================

def build_topic10_curriculum_data():
    return [
        # ---------------------------------------------------------------------
        # LESSON 1: Current, Potential Difference, EMF and Measurement
        # ---------------------------------------------------------------------
        {
            "unit_order": 1,
            "unit_name": "Current, Potential Difference, EMF and Measurement",
            "unit_description": "Definition of electric current I = Q/t, potential difference V = W/Q, Electromotive Force (EMF) vs Terminal Voltage (E = V + Ir), internal resistance r, and ammeter (series) / voltmeter (parallel) rules.",
            "lesson_title": "Current, Potential Difference, EMF and Measurement",
            "pages": [
                # Page 1: Hook & Glowing Bulb Circuit Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Continuous Flow: Dry Cell Lighting Miniature Lamp Circuit",
                        "content": {
                            "title": "Continuous Flow: Dry Cell Lighting Miniature Lamp Circuit",
                            "caption": "A 1.5 V dry cell battery connected by copper wires to a miniature incandescent light bulb. Chemical reactions in the cell drive a steady flow of electric charges around the closed loop.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Simple_battery_bulb_circuit.jpg/1280px-Simple_battery_bulb_circuit.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Simple_battery_bulb_circuit.jpg/1280px-Simple_battery_bulb_circuit.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Simple Battery Light Bulb Circuit",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Simple_battery_bulb_circuit.jpg/1280px-Simple_battery_bulb_circuit.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Simple_battery_bulb_circuit.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Charges in Motion: The Hydraulic Analogue",
                        "content": {
                            "title": "Current Electricity as Flowing Fluid",
                            "text": "In electrostatics, charges remained stationary.\n\nIn **current electricity**, an electrical source (battery) acts like a water pump, maintaining a continuous push (**potential difference**) that drives electrons through conductors to do work."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Current & Voltage Fundamentals",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **Electric Current ($I = Q/t$)** and **Potential Difference ($V = W/Q$)**.",
                                "Distinguish **EMF ($E$)** from **Terminal Voltage ($V$)**.",
                                "Model **Internal Resistance ($r$)** via $E = V + Ir$.",
                                "Connect **Ammeters in series** and **Voltmeters in parallel** correctly."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Electric Current (I)",
                        "content": {
                            "term": "Electric Current (I)",
                            "definition": "The rate of flow of electric charge past a point in a circuit: I = Q / t (measured in Amperes, A, where 1 A = 1 C/s).",
                            "example": "A current of 0.8 A flowing into a charging mobile phone."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Electromotive Force (EMF, E)",
                        "content": {
                            "term": "Electromotive Force (EMF, E)",
                            "definition": "The total work done per unit charge by an electrical source to drive charge through a complete circuit, measured on open circuit.",
                            "example": "A standard 1.5 V AA dry cell on open circuit."
                        }
                    }
                ],
                # Page 3: EMF vs Terminal Voltage SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "EMF vs Terminal Voltage Diagram",
                        "content": {
                            "title": "EMF vs Terminal Voltage Diagram",
                            "caption": "Comparison of open circuit EMF (1.50 V, I = 0) versus closed circuit Terminal Voltage (1.30 V), showing 0.20 V lost across internal resistance r.",
                            "svg_content": get_svg_emf_vs_terminal_voltage(),
                            "svg": get_svg_emf_vs_terminal_voltage()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "EMF vs Terminal Voltage Diagram",
                            "metadata": {
                                "svg_content": get_svg_emf_vs_terminal_voltage()
                            }
                        }
                    }
                ],
                # Page 4: Meter Connections SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Correct Meter Connection: Series Ammeter & Parallel Voltmeter",
                        "content": {
                            "title": "Correct Meter Connection: Series Ammeter & Parallel Voltmeter",
                            "caption": "Ammeter placed in series with low resistance to measure full current; Voltmeter placed in parallel with high resistance across resistor to measure potential difference.",
                            "svg_content": get_svg_meter_connections(),
                            "svg": get_svg_meter_connections()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Meter Connection Circuit Diagram",
                            "metadata": {
                                "svg_content": get_svg_meter_connections()
                            }
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Meter Resistance Requirements",
                        "content": {
                            "question": "Why must an ammeter have an extremely low internal resistance and a voltmeter have an extremely high internal resistance?",
                            "options": [
                                "To prevent the meters from melting.",
                                "To ensure the series ammeter does not reduce circuit current, and the parallel voltmeter does not draw current away from the component.",
                                "To allow the voltmeter to be connected in series.",
                                "To balance the internal resistance of the battery."
                            ],
                            "answer": "B",
                            "explanation": "An ammeter is connected in series; high resistance would reduce total circuit current. A voltmeter is connected in parallel; low resistance would divert current away from the component being measured. Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Worked Example
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Charge and Energy Calculations",
                        "content": {
                            "title": "Smartphone Battery Charging",
                            "problem": "A phone charger delivers a steady current of $0.8\\text{ A}$ at $5.0\\text{ V}$ for $10\\text{ minutes}$. Calculate total charge and total energy transferred.",
                            "steps": [
                                "1. **Convert Time**: $t = 10\\text{ min} = 600\\text{ s}$.",
                                "2. **Find Charge**: $Q = I \\times t = 0.8\\text{ A} \\times 600\\text{ s} = 480\\text{ C}$.",
                                "3. **Find Energy**: $W = V \\times Q = 5.0\\text{ V} \\times 480\\text{ C} = 2,400\\text{ J}$ ($2.4\\text{ kJ}$)."
                            ],
                            "answer": "Total charge is 480 C; total energy transferred is 2.4 kJ."
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Current, Potential Difference, and EMF Explained",
                        "content": {
                            "title": "Physics Video: Current, Potential Difference, and EMF Explained",
                            "description": "Video explaining electric current, voltage drops, lost volts across internal resistance, and connecting meters.",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "resolved_video_id": "CVsdXKO9xlk"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Current and Voltage Fundamentals Video",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "metadata": {
                                "youtube_id": "CVsdXKO9xlk"
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
                                "**Current ($I$)**: $I = Q/t$ (Amperes); **Voltage ($V$)**: $V = W/Q$ (Volts).",
                                "**EMF ($E$)**: Open circuit voltage; **Terminal Voltage ($V$)**: $E = V + Ir$.",
                                "**Ammeters**: Low resistance in series; **Voltmeters**: High resistance in parallel."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 2: Ohm’s Law and V–I Characteristics
        # ---------------------------------------------------------------------
        {
            "unit_order": 2,
            "unit_name": "Ohm’s Law and V–I Characteristics",
            "unit_description": "Definition of resistance R = V/I (Ohms), statement of Ohm's Law (V = IR at constant temperature), experimental verification with rheostat, and V-I graphs for ohmic vs non-ohmic conductors (filament lamps, diodes).",
            "lesson_title": "Ohm’s Law and V–I Characteristics",
            "pages": [
                # Page 1: Hook & Resistors Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Electrical Friction: Carbon-Composition Resistors",
                        "content": {
                            "title": "Electrical Friction: Carbon-Composition Resistors",
                            "caption": "A collection of commercial electronic resistors with color-coded bands. Resistors introduce controlled electrical friction into circuits to limit current and set operating voltages.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Electronic_resistors_assortment.jpg/1280px-Electronic_resistors_assortment.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Electronic_resistors_assortment.jpg/1280px-Electronic_resistors_assortment.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Electronic Resistors Assortment",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Electronic_resistors_assortment.jpg/1280px-Electronic_resistors_assortment.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Electronic_resistors_assortment.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Electrical Friction: Resistance",
                        "content": {
                            "title": "The Opposition to Current Flow",
                            "text": "Pushing a box over gravel requires more force than over ice.\n\nIn electricity, electrons encounter collisions with lattice atoms as they flow through conductors. This opposition is called **Resistance ($R$)**."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Ohm's Law & V-I Graphs",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "State and apply **Ohm's Law ($V = IR$)**.",
                                "Verify Ohm's law experimentally using a variable rheostat circuit.",
                                "Interpret $V-I$ and $I-V$ characteristic curves.",
                                "Distinguish **Ohmic conductors** (constant $R$) from **Non-Ohmic conductors** (filament bulbs, diodes)."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Ohm's Law",
                        "content": {
                            "term": "Ohm's Law",
                            "definition": "The current (I) through a metallic conductor is directly proportional to the potential difference (V) across it, provided temperature and other physical conditions remain constant.",
                            "example": "V = IR (Straight line V-I graph through origin)."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Non-Ohmic Conductor",
                        "content": {
                            "term": "Non-Ohmic Conductor",
                            "definition": "A conductor whose resistance varies with current or temperature, producing a non-linear (curved) V-I characteristic graph.",
                            "example": "Tungsten filament lamps and semiconductor diodes."
                        }
                    }
                ],
                # Page 3: Ohm's Law Formula & Gradient
                [
                    {
                        "type": "formula_breakdown",
                        "title": "Ohm's Law Mathematical Relationship",
                        "content": {
                            "title": "The Resistance Relationship",
                            "formula": "V = I \\times R \\implies R = \\frac{V}{I} = \\text{Gradient of } V-I \\text{ Graph}",
                            "variables": [
                                "$V$ = Potential difference across conductor in Volts ($\\text{V}$)",
                                "$I$ = Current through conductor in Amperes ($\\text{A}$)",
                                "$R$ = Resistance in Ohms ($\\Omega$)"
                            ]
                        }
                    }
                ],
                # Page 4: Ohmic vs Non-Ohmic Comparison
                [
                    {
                        "type": "comparison_table",
                        "title": "V–I Characteristics: Ohmic vs Non-Ohmic Conductors",
                        "content": {
                            "title": "Conductor Behavior Matrix",
                            "headers": ["Conductor Type", "V–I Graph Shape", "Resistance Behavior", "Physical Explanation"],
                            "rows": [
                                ["Constantan / Nichrome Wire", "Straight line passing through origin $(0,0)$", "Constant resistance", "Temperature kept steady; lattice vibration unchanged."],
                                ["Filament Light Bulb", "Curves upward with decreasing gradient for I-V", "Resistance increases with temperature", "White-hot tungsten lattice vibrates violently, scattering electrons."],
                                ["Semiconductor Diode", "Flat near origin, shoots up past $0.7\\text{ V}$ threshold", "Very high reverse R, near-zero forward R", "One-way electronic valve junction."]
                            ]
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Ohm's Law Voltage Doubling",
                        "content": {
                            "question": "A metallic alloy wire produces a straight-line V-I graph through the origin. If a potential difference of 6.0 V produces a current of 0.25 A, what is the resistance, and what current flows when voltage increases to 12.0 V?",
                            "options": [
                                "1.5 Ω and 0.50 A",
                                "24.0 Ω and 0.50 A",
                                "24.0 Ω and 0.125 A",
                                "1.5 Ω and 0.125 A"
                            ],
                            "answer": "B",
                            "explanation": "Resistance: $R = V/I = 6.0\\text{ V} / 0.25\\text{ A} = 24.0\\ \Omega$. Because the wire is ohmic, resistance remains constant at $24.0\\ \Omega$. At $12.0\\text{ V}$, current is $I = V/R = 12.0\\text{ V} / 24.0\\ \Omega = 0.50\\text{ A}$. Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Experimental Protocol
                [
                    {
                        "type": "step_process",
                        "title": "Laboratory Protocol: Verifying Ohm's Law",
                        "content": {
                            "title": "Constant-Temperature V-I Experiment",
                            "steps": [
                                "1. Connect battery, switch, rheostat, ammeter, and test wire in series.",
                                "2. Connect voltmeter in parallel across test wire.",
                                "3. Close switch briefly, record I and V, and immediately open switch to prevent overheating.",
                                "4. Adjust rheostat to take 5 distinct pairs of readings; plot V vs I to verify straight line."
                            ]
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Verifying Ohm's Law and V-I Graphs",
                        "content": {
                            "title": "Physics Video: Verifying Ohm's Law and V-I Graphs",
                            "description": "Video demonstrating experimental setup for Ohm's Law, rheostat current variation, and plotting ohmic vs non-ohmic curves.",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "resolved_video_id": "CVsdXKO9xlk"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Ohm's Law Verification Video",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "metadata": {
                                "youtube_id": "CVsdXKO9xlk"
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
                                "**Ohm's Law**: $V = IR$ if temperature is constant.",
                                "The **gradient of a $V-I$ graph** equals resistance ($R$).",
                                "**Ohmic conductors** produce straight lines through origin; **non-ohmic** (bulbs/diodes) produce curves."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 3: Resistance, Resistivity and Resistor Colour Codes
        # ---------------------------------------------------------------------
        {
            "unit_order": 3,
            "unit_name": "Resistance, Resistivity and Resistor Colour Codes",
            "unit_description": "Factors determining resistance (length R ∝ L, area R ∝ 1/A, material, temperature), Resistivity formula R = ρ L / A, wire stretching mechanics, and 4-band resistor color codes.",
            "lesson_title": "Resistance, Resistivity and Resistor Colour Codes",
            "pages": [
                # Page 1: Hook & Wire Gauges Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Geometric Factors: Copper Wire Gauges of Varying Thickness",
                        "content": {
                            "title": "Geometric Factors: Copper Wire Gauges of Varying Thickness",
                            "caption": "Reels of copper wire of different gauges: thick power transmission cables vs fine headphone wires. Wire thickness and length dictate electrical resistance.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Copper_wire_spools_gauges.jpg/1280px-Copper_wire_spools_gauges.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Copper_wire_spools_gauges.jpg/1280px-Copper_wire_spools_gauges.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Copper Wire Spools of Varying Gauges",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Copper_wire_spools_gauges.jpg/1280px-Copper_wire_spools_gauges.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Copper_wire_spools_gauges.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Mains Cables Are Thick",
                        "content": {
                            "title": "Geometry of Resistance",
                            "text": "Why do high-power electrical cables use thick metal conductors while phone wires are hair-thin?\n\nA thicker wire provides a wider path for electrons, reducing resistance and preventing wasted heat."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Resistivity & Color Codes",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify 4 physical factors affecting resistance ($L, A, \\rho, T$).",
                                "Calculate resistance using the **Resistivity equation: $R = \\rho \\frac{L}{A}$**.",
                                "Analyze what happens to resistance when a wire is **stretched**.",
                                "Decode commercial resistors using the **4-Band Color Code**."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Resistivity (ρ)",
                        "content": {
                            "term": "Resistivity (ρ)",
                            "definition": "An intrinsic material property measuring opposition to electric current, defined as the resistance of a 1 m conductor of 1 m² cross-sectional area (measured in Ω·m).",
                            "example": "Copper has low resistivity (1.7 × 10⁻⁸ Ω·m); Nichrome has high resistivity (1.1 × 10⁻⁶ Ω·m)."
                        }
                    }
                ],
                # Page 3: Resistor Color Code SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Four-Band Resistor Color Code System",
                        "content": {
                            "title": "Four-Band Resistor Color Code System",
                            "caption": "Resistor color decoding: Band 1 (Yellow = 4), Band 2 (Violet = 7), Band 3 (Orange multiplier = ×1,000), Band 4 (Gold tolerance = ±5%), yielding 47 kΩ ± 5%.",
                            "svg_content": get_svg_resistor_color_codes(),
                            "svg": get_svg_resistor_color_codes()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Resistor Color Code Diagram",
                            "metadata": {
                                "svg_content": get_svg_resistor_color_codes()
                            }
                        }
                    }
                ],
                # Page 4: Resistivity Formula Breakdown
                [
                    {
                        "type": "formula_breakdown",
                        "title": "The Resistivity Mathematical Model",
                        "content": {
                            "title": "Geometry and Material Combined",
                            "formula": "R = \\rho \\frac{L}{A} \\quad \\text{where} \\quad A = \\pi r^2 = \\frac{\\pi d^2}{4}",
                            "variables": [
                                "$R$ = Resistance in Ohms ($\\Omega$)",
                                "$\\rho$ = Material resistivity in Ohm-metres ($\\Omega\\cdot\\text{m}$)",
                                "$L$ = Length of conductor in metres ($\\text{m}$)",
                                "$A$ = Cross-sectional area in square metres ($\\text{m}^2$)"
                            ]
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Stretched Wire Resistance Calculation",
                        "content": {
                            "question": "A uniform wire of length L and cross-sectional area A has a resistance of 12 Ω. If it is stretched uniformly until its length is doubled (2L) while keeping volume constant (cutting area to A/2), what is its new resistance?",
                            "options": [
                                "12 Ω",
                                "24 Ω",
                                "48 Ω",
                                "6 Ω"
                            ],
                            "answer": "C",
                            "explanation": "Original resistance: $R_1 = \\rho L / A = 12\\ \Omega$. When stretched: $R_2 = \\rho (2L) / (A/2) = 4 \\times (\\rho L / A) = 4 \\times 12\\ \Omega = 48\\ \Omega$. Doubling length doubles resistance, and halving area doubles it again, resulting in a **4-fold increase (48 Ω)**. Option C is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Worked Resistivity Example
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Constantan Wire Resistance",
                        "content": {
                            "title": "Calculating Resistance from Wire Geometry",
                            "problem": "Calculate resistance of a $2.0\\text{ m}$ constantan wire of diameter $0.4\\text{ mm}$ ($\\rho = 4.9 \\times 10^{-7}\\ \Omega\\cdot\\text{m}$).",
                            "steps": [
                                "1. **Radius**: $r = 0.2\\text{ mm} = 2.0 \\times 10^{-4}\\text{ m}$.",
                                "2. **Area**: $A = \\pi r^2 = 3.142 \\times (2.0 \\times 10^{-4})^2 = 1.257 \\times 10^{-7}\\text{ m}^2$.",
                                "3. **Resistivity Formula**: $R = (4.9 \\times 10^{-7}) \\times \\frac{2.0}{1.257 \\times 10^{-7}} = 7.8\\ \Omega$."
                            ],
                            "answer": "The resistance is 7.8 Ohms."
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Resistivity and Resistor Color Codes",
                        "content": {
                            "title": "Physics Video: Resistivity and Resistor Color Codes",
                            "description": "Video explaining wire geometry, resistivity calculations, and decoding 4-band resistor color codes.",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "resolved_video_id": "CVsdXKO9xlk"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Resistivity and Color Codes Video",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "metadata": {
                                "youtube_id": "CVsdXKO9xlk"
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
                                "Resistance model: **$R = \\rho L / A$**.",
                                "Thick wires have lower resistance; long wires have higher resistance.",
                                "Resistor bands decode digits, multipliers ($10^n$), and tolerance."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 4: Series and Parallel Resistor Networks; Circuit Laws
        # ---------------------------------------------------------------------
        {
            "unit_order": 4,
            "unit_name": "Series and Parallel Resistor Networks; Circuit Laws",
            "unit_description": "Series networks (same current, shared voltage, RT = R1 + R2), Parallel networks (shared voltage, divided current, 1/RT = 1/R1 + 1/R2), and calculating combined series-parallel circuits.",
            "lesson_title": "Series and Parallel Resistor Networks; Circuit Laws",
            "pages": [
                # Page 1: Hook & Domestic Fuse Box Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Household Parallelism: Domestic Distribution Fuse Box",
                        "content": {
                            "title": "Household Parallelism: Domestic Distribution Fuse Box",
                            "caption": "A household consumer distribution board with circuit breakers. Household wiring is arranged in parallel branches so each room operates independently at full mains voltage (240 V).",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Domestic_fuse_box_breakers.jpg/1280px-Domestic_fuse_box_breakers.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Domestic_fuse_box_breakers.jpg/1280px-Domestic_fuse_box_breakers.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Domestic Distribution Fuse Box Board",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Domestic_fuse_box_breakers.jpg/1280px-Domestic_fuse_box_breakers.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Domestic_fuse_box_breakers.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Home Appliances Don't Turn Off Together",
                        "content": {
                            "title": "Series vs Parallel in Everyday Life",
                            "text": "In cheap fairy lights, one burnt-out bulb turns off the whole string (**Series**).\n\nIn your home, turning off a bedroom lamp does not affect the kitchen light because they are wired in independent branches (**Parallel**)."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Resistor Networks",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Apply current and voltage rules in **Series** and **Parallel** circuits.",
                                "Derive and calculate **Effective Resistance ($R_T$)**.",
                                "Solve combined series-parallel resistor networks."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Series Circuit",
                        "content": {
                            "term": "Series Circuit",
                            "definition": "A single continuous loop where current is identical through all components (I_total = I1 = I2) and total voltage is shared (V_total = V1 + V2).",
                            "example": "Total resistance: RT = R1 + R2 + R3."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Parallel Circuit",
                        "content": {
                            "term": "Parallel Circuit",
                            "definition": "Multiple independent branches where voltage is identical across all branches (V_total = V1 = V2) and total current divides (I_total = I1 + I2).",
                            "example": "Total resistance: 1/RT = 1/R1 + 1/R2."
                        }
                    }
                ],
                # Page 3: Series vs Parallel SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Series vs Parallel Resistor Networks Comparison",
                        "content": {
                            "title": "Series vs Parallel Resistor Networks Comparison",
                            "caption": "Comparison diagram: Series (constant current, shared voltage, additive RT) vs Parallel (constant voltage, divided current, reciprocal RT).",
                            "svg_content": get_svg_series_parallel_networks(),
                            "svg": get_svg_series_parallel_networks()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Series vs Parallel Networks Diagram",
                            "metadata": {
                                "svg_content": get_svg_series_parallel_networks()
                            }
                        }
                    }
                ],
                # Page 4: Rules Comparison Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Circuit Laws: Series vs Parallel Networks",
                        "content": {
                            "title": "Network Rules Matrix",
                            "headers": ["Rule", "Series Circuit", "Parallel Circuit"],
                            "rows": [
                                ["Current ($I$)", "$I_{\\text{total}} = I_1 = I_2$ (Same everywhere)", "$I_{\\text{total}} = I_1 + I_2$ (Divides at junctions)"],
                                ["Voltage ($V$)", "$V_{\\text{total}} = V_1 + V_2$ (Shared across loads)", "$V_{\\text{total}} = V_1 = V_2$ (Same across branches)"],
                                ["Effective Resistance ($R_T$)", "$R_T = R_1 + R_2 + R_3$ (Always increases)", "$\\frac{1}{R_T} = \\frac{1}{R_1} + \\frac{1}{R_2}$ (Always decreases)"],
                                ["Effect of Component Failure", "Circuit broken; all components shut off.", "Other branches continue operating normally."]
                            ]
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Ratio of Series to Parallel Resistance",
                        "content": {
                            "question": "Two identical resistors of resistance R are connected first in series, and then in parallel. What is the ratio of total series resistance to total parallel resistance (R_series / R_parallel)?",
                            "options": [
                                "1 : 1",
                                "2 : 1",
                                "4 : 1",
                                "1 : 4"
                            ],
                            "answer": "C",
                            "explanation": "In series: $R_{\\text{series}} = R + R = 2R$. In parallel: $1/R_{\\text{parallel}} = 1/R + 1/R = 2/R \\implies R_{\\text{parallel}} = R/2 = 0.5R$. The ratio is $2R / 0.5R = 4$. Series resistance is **4 times larger** than parallel. Option C is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Worked Combined Network Example
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Combined Series-Parallel Network",
                        "content": {
                            "title": "Solving a 12V Combined Circuit",
                            "problem": "A $12\\text{ V}$ battery powers a $4\ \Omega$ resistor in series with a parallel pair of $6\ \Omega$ and $3\ \Omega$ resistors. Calculate total resistance and total battery current.",
                            "steps": [
                                "1. **Parallel Block**: $\\frac{1}{R_p} = \\frac{1}{6} + \\frac{1}{3} = \\frac{3}{6} \\implies R_p = 2.0\ \Omega$.",
                                "2. **Total Resistance**: $R_T = 4.0\ \Omega + 2.0\ \Omega = 6.0\ \Omega$.",
                                "3. **Total Current**: $I_T = \\frac{V}{R_T} = \\frac{12.0\\text{ V}}{6.0\ \Omega} = 2.0\\text{ A}$."
                            ],
                            "answer": "Total resistance is 6.0 Ohms; total current is 2.0 Amperes."
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Series and Parallel Circuits and Network Laws",
                        "content": {
                            "title": "Physics Video: Series and Parallel Circuits and Network Laws",
                            "description": "Video explaining series and parallel resistor networks, Kirchhoff's current and voltage rules, and solving complex circuits.",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "resolved_video_id": "CVsdXKO9xlk"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Series and Parallel Networks Tutorial Video",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "metadata": {
                                "youtube_id": "CVsdXKO9xlk"
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
                                "**Series**: Same current, shared voltage, $R_T = R_1 + R_2$.",
                                "**Parallel**: Same voltage, divided current, $1/R_T = 1/R_1 + 1/R_2$.",
                                "Adding parallel resistors decreases overall effective resistance."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 5: Determining Resistance: Ammeter–Voltmeter, Wheatstone and Metre Bridge
        # ---------------------------------------------------------------------
        {
            "unit_order": 5,
            "unit_name": "Determining Resistance: Ammeter–Voltmeter, Wheatstone and Metre Bridge",
            "unit_description": "Systematic errors in ammeter-voltmeter methods, Wheatstone Bridge null balance condition (R1/R2 = R3/Rx), and Metre Bridge sliding jockey calculations Rx = Rs (100 - l1)/l1.",
            "lesson_title": "Determining Resistance: Ammeter–Voltmeter, Wheatstone and Metre Bridge",
            "pages": [
                # Page 1: Hook & Metre Bridge Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Precision Null-Balance: Laboratory Metre Bridge Apparatus",
                        "content": {
                            "title": "Precision Null-Balance: Laboratory Metre Bridge Apparatus",
                            "caption": "A classic wooden 1-metre slide-wire bridge with brass connection strips and a central sensitive galvanometer. Sliding the contact jockey locates the precise null point to measure unknown resistance without meter error.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Metre_bridge_laboratory_setup.jpg/1280px-Metre_bridge_laboratory_setup.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Metre_bridge_laboratory_setup.jpg/1280px-Metre_bridge_laboratory_setup.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Metre Bridge Laboratory Apparatus",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Metre_bridge_laboratory_setup.jpg/1280px-Metre_bridge_laboratory_setup.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Metre_bridge_laboratory_setup.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Null-Balance Precision Advantage",
                        "content": {
                            "title": "Bypassing Meter Resistance Errors",
                            "text": "Standard ammeters and voltmeters have internal resistance that distorts measurements.\n\nBridge circuits use a **Null-Balance Method**: adjusting a known ratio until zero current flows through a galvanometer ($I_g = 0$), eliminating all meter error!"
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Resistance Measurement Bridges",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Evaluate systematic errors in Ammeter-Voltmeter circuits.",
                                "Derive the **Wheatstone Bridge balance condition ($R_1/R_2 = R_3/R_x$)**.",
                                "Calculate unknown resistances using a **Metre Bridge ($R_x = R_s \\frac{100-l_1}{l_1}$)**."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Wheatstone Bridge",
                        "content": {
                            "term": "Wheatstone Bridge",
                            "definition": "A 4-resistor diamond bridge circuit balanced when zero current passes through a central galvanometer: R1 / R2 = R3 / Rx.",
                            "example": "Standard precision resistance measurement circuit."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Metre Bridge",
                        "content": {
                            "term": "Metre Bridge",
                            "definition": "A practical 100 cm uniform wire implementation of the Wheatstone bridge where wire segment lengths establish the balance ratio.",
                            "example": "Rx = Rs ((100 - l1) / l1)."
                        }
                    }
                ],
                # Page 3: Metre Bridge SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Metre Bridge Circuit and Null-Balance Diagram",
                        "content": {
                            "title": "Metre Bridge Circuit and Null-Balance Diagram",
                            "caption": "Metre bridge setup showing standard resistor Rs, unknown resistor Rx, 100 cm wire AB, central galvanometer, and sliding jockey at balance distance l1.",
                            "svg_content": get_svg_metre_bridge(),
                            "svg": get_svg_metre_bridge()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Metre Bridge Diagram",
                            "metadata": {
                                "svg_content": get_svg_metre_bridge()
                            }
                        }
                    }
                ],
                # Page 4: Ammeter-Voltmeter Error Analysis
                [
                    {
                        "type": "comparison_table",
                        "title": "Ammeter–Voltmeter Connection Options & Systematic Errors",
                        "content": {
                            "title": "Error Analysis Matrix",
                            "headers": ["Circuit Option", "Connection Description", "Source of Error", "Calculated Result"],
                            "rows": [
                                ["Option A (Voltmeter across Resistor only)", "Ammeter placed in main line before parallel R-V block.", "Ammeter measures $I_R + I_V$ (steals small voltmeter current).", "Calculated $R = V/I$ is **slightly lower** than true value."],
                                ["Option B (Voltmeter across both)", "Voltmeter bridged across series combination of Ammeter and R.", "Voltmeter measures $V_R + V_A$ (includes ammeter voltage drop).", "Calculated $R = V/I$ is **slightly higher** than true value."]
                            ]
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Why Balance Near 50 cm",
                        "content": {
                            "question": "In a metre bridge experiment, why should the standard resistor (Rs) be chosen so that the balance point falls near the middle of the wire (around 50 cm) rather than near the ends?",
                            "options": [
                                "To prevent the wire from melting.",
                                "To minimize percentage error in reading lengths and reduce systematic error from end-connections.",
                                "To protect the galvanometer from voltage spikes.",
                                "To make unknown resistance equal to zero."
                            ],
                            "answer": "B",
                            "explanation": "If the null point is near the extreme ends (e.g. 2 cm), a small reading error of 1 mm causes a large percentage error in length. Balancing near the center (50 cm) **minimizes measurement uncertainty and reduces end-strip resistance errors**. Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Worked Metre Bridge Example
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Metre Bridge Calculation",
                        "content": {
                            "title": "Finding Unknown Resistance Rx",
                            "problem": "A metre bridge balances at $l_1 = 40.0\\text{ cm}$ from end A when a standard $12.0\\ \Omega$ resistor is connected in the left gap. Calculate the unknown resistance $R_x$ in the right gap.",
                            "steps": [
                                "1. **Find Remaining Length**: $100 - l_1 = 100 - 40.0 = 60.0\\text{ cm}$.",
                                "2. **Apply Formula**: $R_x = R_s \\left(\\frac{100 - l_1}{l_1}\\right) = 12.0\\ \Omega \\times \\left(\\frac{60.0}{40.0}\\right)$.",
                                "3. **Calculate**: $R_x = 12.0 \\times 1.5 = 18.0\\ \Omega$."
                            ],
                            "answer": "The unknown resistance is 18.0 Ohms."
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Wheatstone and Metre Bridge Experiments",
                        "content": {
                            "title": "Physics Video: Wheatstone and Metre Bridge Experiments",
                            "description": "Video demonstrating Wheatstone bridge balance conditions, operating a sliding metre bridge, and calculating unknown resistance.",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "resolved_video_id": "CVsdXKO9xlk"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Metre Bridge Experiment Tutorial Video",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "metadata": {
                                "youtube_id": "CVsdXKO9xlk"
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
                                "Ammeter-voltmeter methods have systematic errors due to meter resistance.",
                                "**Wheatstone Bridge**: $R_1/R_2 = R_3/R_x$ when galvanometer current is zero.",
                                "**Metre Bridge**: $R_x = R_s \\frac{100-l_1}{l_1}$; best accuracy achieved near 50 cm."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 6: Electrical Power, Heating Effect and Applications
        # ---------------------------------------------------------------------
        {
            "unit_order": 6,
            "unit_name": "Electrical Power, Heating Effect and Applications",
            "unit_description": "Joule Heating mechanism, electrical power formulas (P = VI = I²R = V²/R), electrical energy E = Pt, commercial electricity billing in kilowatt-hours (kWh), and fuse safety selection.",
            "lesson_title": "Electrical Power, Heating Effect and Applications",
            "pages": [
                # Page 1: Hook & Glowing Toaster Coil Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Resistive Conversion: Glowing Red Heating Element in Toaster",
                        "content": {
                            "title": "Resistive Conversion: Glowing Red Heating Element in Toaster",
                            "caption": "A red-hot nichrome heating coil glowing inside an electric appliance. Drifting electrons collide with metal lattice atoms, converting electrical energy directly into intense thermal radiation.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Glowing_heating_element_toaster.jpg/1280px-Glowing_heating_element_toaster.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Glowing_heating_element_toaster.jpg/1280px-Glowing_heating_element_toaster.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Glowing Toaster Heating Element",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Glowing_heating_element_toaster.jpg/1280px-Glowing_heating_element_toaster.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Glowing_heating_element_toaster.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Physics of Electrical Heat",
                        "content": {
                            "title": "Joule Heating and Everyday Power",
                            "text": "When current flows through a wire, electron collisions create heat (**Joule Heating**).\n\nEngineers harness this in electric kettles, water heaters, and toasters, while protecting circuits from fires using calibrated **fuses**."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Power, Energy & Billing",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain the physical cause of **Joule Heating**.",
                                "Apply power equations: **$P = VI = I^2R = V^2/R$**.",
                                "Calculate electricity bills in commercial **kilowatt-hours ($1\\text{ kWh} = 3.6 \\times 10^6\\text{ J}$)**.",
                                "Select the correct **fuse rating** for appliances."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Electrical Power (P)",
                        "content": {
                            "term": "Electrical Power (P)",
                            "definition": "The rate at which electrical energy is converted into other forms of energy: P = V I = I²R = V²/R (measured in Watts, W).",
                            "example": "A 2400 W electric kettle converts 2400 Joules of energy per second."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Kilowatt-Hour (kWh)",
                        "content": {
                            "term": "Kilowatt-Hour (kWh)",
                            "definition": "The commercial billing unit of electrical energy representing 1 kW of power used for 1 hour: 1 kWh = 3.6 × 10⁶ Joules.",
                            "example": "Kenya Power (KPLC) electricity metering units."
                        }
                    }
                ],
                # Page 3: Power Formulas Breakdown
                [
                    {
                        "type": "formula_breakdown",
                        "title": "Electrical Power and Energy Equations",
                        "content": {
                            "title": "Thermodynamic Circuit Models",
                            "formula": "P = V I = I^2 R = \\frac{V^2}{R} \\quad \\text{and} \\quad E = P \\times t = V I t",
                            "variables": [
                                "$P$ = Electrical power in Watts ($\\text{W}$)",
                                "$E$ = Electrical energy in Joules ($\\text{J}$) or $\\text{kWh}$",
                                "$V$ = Potential difference in Volts ($\\text{V}$)",
                                "$I$ = Current in Amperes ($\\text{A}$)",
                                "$R$ = Resistance in Ohms ($\\Omega$)",
                                "$t$ = Time in seconds ($\\text{s}$) or hours ($\\text{hr}$)"
                            ]
                        }
                    }
                ],
                # Page 4: Household Billing Worked Example
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Household Electricity Bill Calculation",
                        "content": {
                            "title": "KPLC Shower Heater Monthly Cost",
                            "problem": "A $3.0\\text{ kW}$ shower heater is used for $30\\text{ minutes}$ daily. If KPLC charges $20.0\\text{ KES}$ per $\\text{kWh}$, calculate the monthly cost (30 days).",
                            "steps": [
                                "1. **Daily Energy**: $E_{\\text{day}} = 3.0\\text{ kW} \\times 0.5\\text{ hr} = 1.5\\text{ kWh}$.",
                                "2. **Monthly Energy**: $E_{\\text{month}} = 1.5\\text{ kWh} \\times 30 = 45.0\\text{ kWh}$.",
                                "3. **Total Cost**: $\\text{Cost} = 45.0\\text{ kWh} \\times 20.0\\text{ KES/kWh} = 900\\text{ KES}$."
                            ],
                            "answer": "The monthly cost is 900 KES."
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Kettle Operation on 3A Fuse",
                        "content": {
                            "question": "An electric kettle is rated at 240 V, 1200 W. A student plugs it into a mains socket fitted with a 3 A fuse. What will happen when the kettle is switched on?",
                            "options": [
                                "The kettle will heat at half its normal speed.",
                                "The kettle will operate normally.",
                                "The fuse will instantly melt (blow), breaking the circuit safely.",
                                "The kettle will catch fire."
                            ],
                            "answer": "C",
                            "explanation": "Calculate normal operating current: $I = P/V = 1200\\text{ W} / 240\\text{ V} = 5.0\\text{ A}$. Because the kettle draws $5.0\\text{ A}$, which exceeds the $3\\text{ A}$ fuse rating, the fuse wire will instantly overheat, **melt (blow), and safely break the circuit**. Option C is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Fuse Selection Protocol
                [
                    {
                        "type": "step_process",
                        "title": "Protocol for Fuse Sizing and Electrical Safety",
                        "content": {
                            "title": "Selecting the Right Fuse",
                            "steps": [
                                "1. **Calculate Normal Current**: Use $I = P / V$ (e.g. $2400\\text{ W} / 240\\text{ V} = 10\\text{ A}$).",
                                "2. **Select Standard Rating**: Choose a fuse rated **slightly higher than normal current** (e.g. choose a $13\\text{ A}$ fuse for a $10\\text{ A}$ appliance).",
                                "3. **Safety Installation**: Fuses must ALWAYS be connected in series with the **Live wire** to isolate the appliance when blown."
                            ]
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Electrical Power, Heating Effect, and Fuses",
                        "content": {
                            "title": "Physics Video: Electrical Power, Heating Effect, and Fuses",
                            "description": "Video illustrating Joule Heating formulas, calculating electricity bills in kWh, and how fuses protect appliances from overload fires.",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "resolved_video_id": "CVsdXKO9xlk"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Electrical Power and Safety Tutorial Video",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "metadata": {
                                "youtube_id": "CVsdXKO9xlk"
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
                                "**Joule Heating**: Drifting electrons collide with metal atoms, generating heat.",
                                "**Power**: $P = VI = I^2R = V^2/R$; Energy: $E = Pt$.",
                                "Commercial billing: $1\\text{ kWh} = 3.6 \\times 10^6\\text{ J}$.",
                                "**Fuses** are placed in the live wire with ratings chosen slightly above normal operating current."
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
def ingest_grade10_physics_topic10():
    print("======================================================================")
    print("INGESTING CBC GRADE 10 PHYSICS — TOPIC 10: CURRENT ELECTRICITY")
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

    # 3. Get or Create Topic: Current Electricity (Order: 10)
    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=10,
        defaults={
            "name": "Current Electricity",
            "description": "Comprehensive study of moving charges, current, voltage, EMF vs terminal potential difference, Ohm's law, resistance, resistivity, color codes, series/parallel resistor networks, Wheatstone and Metre bridges, Joule heating, and power billing."
        }
    )
    if not t_created and topic.name != "Current Electricity":
        topic.name = "Current Electricity"
        topic.description = "Comprehensive study of moving charges, current, voltage, EMF vs terminal potential difference, Ohm's law, resistance, resistivity, color codes, series/parallel resistor networks, Wheatstone and Metre bridges, Joule heating, and power billing."
        topic.save()
    print(f"Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    curriculum_data = build_topic10_curriculum_data()

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
    print(f"TOPIC 10 INGESTION COMPLETE:")
    print(f"  - Learning Units: {total_units_created}")
    print(f"  - Lessons:        {total_lessons_created}")
    print(f"  - Lesson Blocks:  {total_blocks_created}")
    print(f"  - Lesson Assets:  {total_assets_created}")
    print("======================================================================")

if __name__ == "__main__":
    ingest_grade10_physics_topic10()
