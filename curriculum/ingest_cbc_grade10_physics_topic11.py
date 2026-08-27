"""
VLearn CBC Grade 10 Physics — Topic 11: Introduction to Electronics
Production Ingestion & Visual Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Physics
Topic: Introduction to Electronics (Order: 11)

2 Learning Units & 2 Published Lessons:
  1. Conductors, Insulators, Semiconductors and Components (8 Pages, 13 Blocks)
  2. Basic Electronic Circuits and Digital Applications (8 Pages, 13 Blocks)

Includes:
  - 4 Custom Responsive Sanitized Vector SVG Diagrams
  - 2 Verified Wikimedia Commons Photographic Assets
  - 2 Verified Educational YouTube Video Integrations
  - 2 Formative Scenario-Based MCQs with 4 Options and Pedagogical Feedback
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
# SVG DEFINITIONS FOR TOPIC 11
# =============================================================================

def get_svg_energy_bands():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">ENERGY BAND THEORY: CONDUCTORS, INSULATORS &amp; SEMICONDUCTORS</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Valence Band (Bonded Electrons) • Conduction Band (Free Electrons) • Energy Gap (E_g)</text>

  <!-- 1. Conductor (Overlapping Bands) -->
  <g transform="translate(50, 85)">
    <rect width="210" height="275" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="105" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. CONDUCTOR (Metals)</text>

    <!-- Conduction Band -->
    <rect x="35" y="50" width="140" height="80" fill="#0284c7" rx="4"/>
    <text x="105" y="95" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Conduction Band</text>

    <!-- Valence Band (Overlapping) -->
    <rect x="35" y="100" width="140" height="80" fill="#ef4444" opacity="0.8" rx="4"/>
    <text x="105" y="150" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Valence Band</text>

    <text x="105" y="210" fill="#4ade80" font-size="12" font-weight="700" text-anchor="middle">No Band Gap (E_g = 0)</text>
    <text x="105" y="235" fill="#cbd5e1" font-size="10" text-anchor="middle">Bands overlap; electrons flow</text>
    <text x="105" y="250" fill="#cbd5e1" font-size="10" text-anchor="middle">freely at any temperature.</text>
  </g>

  <!-- 2. Insulator (Large Band Gap > 5 eV) -->
  <g transform="translate(315, 85)">
    <rect width="210" height="275" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="105" y="24" fill="#ef4444" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">2. INSULATOR (Rubber/Glass)</text>

    <!-- Conduction Band (Empty) -->
    <rect x="35" y="50" width="140" height="50" fill="#1e293b" stroke="#0284c7" stroke-width="1.5" rx="4"/>
    <text x="105" y="80" fill="#94a3b8" font-size="10" text-anchor="middle">Conduction (Empty)</text>

    <!-- Large Forbidden Gap -->
    <rect x="45" y="110" width="120" height="40" fill="#ef444422" stroke="#ef4444" stroke-dasharray="3 3" rx="3"/>
    <text x="105" y="135" fill="#ef4444" font-size="10" font-weight="700" text-anchor="middle">Large Gap (E_g &gt; 5 eV)</text>

    <!-- Valence Band (Full) -->
    <rect x="35" y="160" width="140" height="50" fill="#ef4444" rx="4"/>
    <text x="105" y="190" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Valence (Full)</text>

    <text x="105" y="235" fill="#cbd5e1" font-size="10" text-anchor="middle">Electrons cannot jump;</text>
    <text x="105" y="250" fill="#cbd5e1" font-size="10" text-anchor="middle">blocks all electric current.</text>
  </g>

  <!-- 3. Semiconductor (Narrow Band Gap ≈ 1 eV) -->
  <g transform="translate(580, 85)">
    <rect width="210" height="275" rx="8" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
    <text x="105" y="24" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">3. SEMICONDUCTOR (Silicon)</text>

    <!-- Conduction Band -->
    <rect x="35" y="50" width="140" height="50" fill="#0284c7" rx="4"/>
    <circle cx="105" cy="75" r="5" fill="#38bdf8"/>
    <text x="120" y="79" fill="#f8fafc" font-size="9">e⁻</text>

    <!-- Narrow Gap with Thermal Jump Arrow -->
    <line x1="105" y1="140" x2="105" y2="105" stroke="#f59e0b" stroke-width="2"/>
    <polygon points="105,105 101,113 109,113" fill="#f59e0b"/>
    <text x="105" y="125" fill="#f59e0b" font-size="9" font-weight="700" text-anchor="middle">E_g ≈ 1.1 eV</text>

    <!-- Valence Band -->
    <rect x="35" y="140" width="140" height="50" fill="#ef4444" rx="4"/>
    <circle cx="105" cy="165" r="5" fill="#0f172a" stroke="#f8fafc" stroke-width="1.5"/>
    <text x="120" y="169" fill="#f8fafc" font-size="9">Hole (+)</text>

    <text x="105" y="215" fill="#4ade80" font-size="11" font-weight="700" text-anchor="middle">Thermal Excitation</text>
    <text x="105" y="235" fill="#cbd5e1" font-size="10" text-anchor="middle">Room heat frees electrons &amp;</text>
    <text x="105" y="250" fill="#cbd5e1" font-size="10" text-anchor="middle">creates mobile holes!</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_diode_bias():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%">
  <rect width="840" height="380" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">SEMICONDUCTOR DIODE BIASING: FORWARD VS REVERSE BIAS</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Forward Bias: Current Flows, LED Lights • Reverse Bias: Depletion Layer Blocks Current</text>

  <!-- Left: Forward Bias -->
  <g transform="translate(60, 80)">
    <rect width="330" height="270" rx="8" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
    <text x="165" y="24" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. FORWARD BIAS (Conduction Mode)</text>

    <!-- Battery (Anode to Positive) -->
    <line x1="40" y1="70" x2="40" y2="90" stroke="#f59e0b" stroke-width="3"/>
    <line x1="50" y1="75" x2="50" y2="85" stroke="#94a3b8" stroke-width="3"/>
    <text x="35" y="65" fill="#f59e0b" font-size="10" font-weight="700">+</text>
    <text x="55" y="65" fill="#94a3b8" font-size="10" font-weight="700">-</text>

    <!-- Diode Symbol (Pointing Right: Forward) -->
    <polygon points="120,80 100,68 100,92" fill="#22c55e"/>
    <line x1="120" y1="68" x2="120" y2="92" stroke="#22c55e" stroke-width="3"/>
    <text x="110" y="110" fill="#4ade80" font-size="10" font-weight="700" text-anchor="middle">Diode (Anode → Cathode)</text>

    <!-- Resistor & LED -->
    <line x1="120" y1="80" x2="180" y2="80" stroke="#f8fafc" stroke-width="2"/>
    <circle cx="210" cy="80" r="14" fill="#eab308" stroke="#ca8a04" stroke-width="2"/>
    <!-- Glowing rays -->
    <line x1="210" y1="60" x2="210" y2="50" stroke="#eab308" stroke-width="2"/>
    <line x1="225" y1="65" x2="235" y2="55" stroke="#eab308" stroke-width="2"/>
    <text x="210" y="110" fill="#eab308" font-size="10" font-weight="700" text-anchor="middle">LED GLOWS</text>

    <!-- Loop completion -->
    <path d="M 224 80 L 290 80 L 290 150 L 20 150 L 20 80 L 40 80" fill="none" stroke="#22c55e" stroke-width="2"/>

    <text x="165" y="195" fill="#4ade80" font-size="12" font-weight="700" text-anchor="middle">Depletion Layer Shrinks ⟹ Low Resistance</text>
    <text x="165" y="220" fill="#cbd5e1" font-size="10" text-anchor="middle">Current flows freely through circuit.</text>
  </g>

  <!-- Right: Reverse Bias -->
  <g transform="translate(450, 80)">
    <rect width="330" height="270" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="165" y="24" fill="#ef4444" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">2. REVERSE BIAS (Blocking Mode)</text>

    <!-- Battery -->
    <line x1="40" y1="70" x2="40" y2="90" stroke="#f59e0b" stroke-width="3"/>
    <line x1="50" y1="75" x2="50" y2="85" stroke="#94a3b8" stroke-width="3"/>

    <!-- Diode Symbol (Flipped: Cathode to +) -->
    <polygon points="100,80 120,68 120,92" fill="#ef4444"/>
    <line x1="100" y1="68" x2="100" y2="92" stroke="#ef4444" stroke-width="3"/>
    <text x="110" y="110" fill="#ef4444" font-size="10" font-weight="700" text-anchor="middle">Diode (Reversed)</text>

    <!-- LED (Dark) -->
    <line x1="120" y1="80" x2="180" y2="80" stroke="#f8fafc" stroke-width="2"/>
    <circle cx="210" cy="80" r="14" fill="#334155" stroke="#64748b" stroke-width="2"/>
    <!-- Red X on LED -->
    <line x1="202" y1="72" x2="218" y2="88" stroke="#ef4444" stroke-width="2.5"/>
    <line x1="218" y1="72" x2="202" y2="88" stroke="#ef4444" stroke-width="2.5"/>
    <text x="210" y="110" fill="#94a3b8" font-size="10" font-weight="700" text-anchor="middle">LED DARK</text>

    <!-- Loop completion with block X -->
    <path d="M 224 80 L 290 80 L 290 150 L 20 150 L 20 80 L 40 80" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="4 4"/>

    <text x="165" y="195" fill="#ef4444" font-size="12" font-weight="700" text-anchor="middle">Depletion Layer Widens ⟹ Infinite Resistance</text>
    <text x="165" y="220" fill="#cbd5e1" font-size="10" text-anchor="middle">All current is blocked by p-n junction.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_half_wave_rectification():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">HALF-WAVE RECTIFICATION: AC TO PULSATING DC CONVERSION</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Diode Passes Positive Half-Cycles &amp; Blocks Negative Cycles</text>

  <!-- Left: Circuit Layout -->
  <g transform="translate(50, 80)">
    <rect width="320" height="280" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="160" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">RECTIFIER CIRCUIT</text>

    <!-- AC Source Symbol -->
    <circle cx="60" cy="110" r="22" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <path d="M 50 110 Q 55 100 60 110 T 70 110" fill="none" stroke="#f59e0b" stroke-width="2.5"/>
    <text x="60" y="150" fill="#f59e0b" font-size="10" font-weight="700" text-anchor="middle">AC Source (~)</text>

    <!-- Diode in series -->
    <line x1="82" y1="110" x2="140" y2="110" stroke="#f8fafc" stroke-width="2"/>
    <polygon points="160,110 140,98 140,122" fill="#22c55e"/>
    <line x1="160" y1="98" x2="160" y2="122" stroke="#22c55e" stroke-width="3"/>
    <text x="150" y="85" fill="#4ade80" font-size="10" font-weight="700" text-anchor="middle">Diode</text>

    <!-- Load Resistor (RL) -->
    <line x1="160" y1="110" x2="250" y2="110" stroke="#f8fafc" stroke-width="2"/>
    <rect x="235" y="130" width="30" height="60" fill="#334155" stroke="#f59e0b" stroke-width="1.5" rx="3"/>
    <text x="250" y="165" fill="#f59e0b" font-size="10" font-weight="700" text-anchor="middle">RL</text>

    <!-- Return wire -->
    <path d="M 250 110 L 250 130 M 250 190 L 250 220 L 60 220 L 60 132" stroke="#f8fafc" stroke-width="2"/>
  </g>

  <!-- Right: Input AC vs Output Pulsating DC Waveforms -->
  <g transform="translate(420, 80)">
    <rect width="370" height="280" rx="8" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
    <text x="185" y="24" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">WAVEFORM COMPARISON</text>

    <!-- 1. Input AC Wave (Sinusoidal) -->
    <text x="30" y="55" fill="#f59e0b" font-size="11" font-weight="700">1. Input AC Voltage (V_in)</text>
    <line x1="30" y1="90" x2="340" y2="90" stroke="#64748b" stroke-width="1"/>
    <path d="M 40 90 Q 75 40 110 90 T 180 90 T 250 90 T 320 90" fill="none" stroke="#f59e0b" stroke-width="2.5"/>

    <!-- 2. Output DC Wave (Half-Wave Rectified) -->
    <text x="30" y="165" fill="#4ade80" font-size="11" font-weight="700">2. Output Pulsating DC Voltage (V_out)</text>
    <line x1="30" y1="210" x2="340" y2="210" stroke="#64748b" stroke-width="1"/>
    <!-- Positive peaks passed, negative flat -->
    <path d="M 40 210 Q 75 160 110 210 L 180 210 Q 215 160 250 210 L 320 210" fill="none" stroke="#22c55e" stroke-width="3"/>
    <text x="145" y="235" fill="#94a3b8" font-size="9" text-anchor="middle">Blocked (0 V)</text>
    <text x="285" y="235" fill="#94a3b8" font-size="9" text-anchor="middle">Blocked (0 V)</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg


# =============================================================================
# CURRICULUM DEFINITION DATA FOR TOPIC 11
# =============================================================================

def build_topic11_curriculum_data():
    return [
        # ---------------------------------------------------------------------
        # LESSON 1: Conductors, Insulators, Semiconductors and Components
        # ---------------------------------------------------------------------
        {
            "unit_order": 1,
            "unit_name": "Conductors, Insulators, Semiconductors and Components",
            "unit_description": "Energy band theory (valence band, conduction band, band gap Eg), conductors vs insulators vs semiconductors vs superconductors, doping (n-type vs p-type), six fundamental electronic components, and diode/LED polarity testing.",
            "lesson_title": "Conductors, Insulators, Semiconductors and Components",
            "pages": [
                # Page 1: Hook & Silicon Wafer Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Solid-State Foundation: Silicon Wafer with Integrated Microchips",
                        "content": {
                            "title": "Solid-State Foundation: Silicon Wafer with Integrated Microchips",
                            "caption": "A polished silicon semiconductor wafer containing thousands of microscopic integrated circuit microchips. Controlling the energy band gap of silicon enables all modern computing and mobile electronics.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Silicon_wafer_integrated_circuits.jpg/1280px-Silicon_wafer_integrated_circuits.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Silicon_wafer_integrated_circuits.jpg/1280px-Silicon_wafer_integrated_circuits.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Silicon Wafer Microchip Foundation",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Silicon_wafer_integrated_circuits.jpg/1280px-Silicon_wafer_integrated_circuits.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Silicon_wafer_integrated_circuits.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Controlling Current Without Moving Parts",
                        "content": {
                            "title": "The Power of Semiconductors",
                            "text": "Inside smartphones and solar controllers, there are no mechanical levers or switches.\n\nBy manipulating subatomic energy levels in **semiconductors**, we create solid-state electronic components that direct and switch currents at microscopic scales."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Solid-State Physics",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain electrical conduction using **Energy Band Theory** (Valence band, Conduction band, Band gap $E_g$).",
                                "Distinguish **Conductors, Insulators, Semiconductors**, and **Superconductors**.",
                                "Explain **Doping** and contrast **n-type** with **p-type** semiconductors.",
                                "Identify 6 essential components and test **Diode / LED polarity**."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Band Gap (Energy Gap, Eg)",
                        "content": {
                            "term": "Band Gap (Energy Gap, Eg)",
                            "definition": "The forbidden energy zone between the valence band and the conduction band that electrons cannot occupy. Electrons must gain energy Eg to jump into the conduction band.",
                            "example": "Silicon has a narrow band gap of 1.1 eV; diamond insulator has a wide gap > 5 eV."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Doping",
                        "content": {
                            "term": "Doping",
                            "definition": "The deliberate addition of tiny, controlled amounts of impurity atoms to an intrinsic semiconductor to drastically increase its electrical conductivity.",
                            "example": "Doping silicon with phosphorus creates n-type material; doping with boron creates p-type."
                        }
                    }
                ],
                # Page 3: Energy Bands SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Energy Band Theory: Conductors, Insulators & Semiconductors",
                        "content": {
                            "title": "Energy Band Theory: Conductors, Insulators & Semiconductors",
                            "caption": "Comparison of energy band structures: Conductors (overlapping bands, Eg = 0), Insulators (large gap Eg > 5 eV), and Semiconductors (narrow gap Eg ≈ 1.1 eV allowing thermal excitation).",
                            "svg_content": get_svg_energy_bands(),
                            "svg": get_svg_energy_bands()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Energy Band Theory Diagram",
                            "metadata": {
                                "svg_content": get_svg_energy_bands()
                            }
                        }
                    }
                ],
                # Page 4: Diode Biasing SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Semiconductor Diode Biasing: Forward vs Reverse Bias",
                        "content": {
                            "title": "Semiconductor Diode Biasing: Forward vs Reverse Bias",
                            "caption": "Diode operation: Forward bias (Anode to +, Cathode to -) shrinks depletion layer and lights LED; Reverse bias widens depletion layer and blocks all current.",
                            "svg_content": get_svg_diode_bias(),
                            "svg": get_svg_diode_bias()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Diode Biasing Diagram",
                            "metadata": {
                                "svg_content": get_svg_diode_bias()
                            }
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Current-Limiting Resistor with LED",
                        "content": {
                            "question": "Why is a fixed current-limiting resistor always wired in series with a Light Emitting Diode (LED) in a low-voltage DC circuit?",
                            "options": [
                                "To convert DC battery voltage into AC.",
                                "To increase circuit resistance, preventing the low-resistance forward-biased LED from drawing excessive current and destroying its p-n junction.",
                                "To store electric charge like a capacitor.",
                                "To reverse the polarity of the LED."
                            ],
                            "answer": "B",
                            "explanation": "Once an LED is forward-biased beyond its threshold voltage (~2 V), its dynamic resistance drops to near-zero. Without a series resistor, excessive current would rush through the p-n junction, overheating and destroying the delicate semiconductor chip. Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Electronic Components Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Six Fundamental Electronic Components",
                        "content": {
                            "title": "Core Electronic Building Blocks",
                            "headers": ["Component", "Circuit Symbol", "Polarity", "Primary Function"],
                            "rows": [
                                ["Resistor", "Zig-zag / Rectangle", "Non-polar", "Limits current and divides circuit voltage."],
                                ["Capacitor", "Two parallel plates", "Polar (Electrolytic) / Non-polar", "Stores electrical charge and blocks steady DC."],
                                ["Semiconductor Diode", "Triangle pointing to bar", "Polar (Anode +, Cathode -)", "One-way valve; allows current in forward bias only."],
                                ["Light Emitting Diode (LED)", "Diode with outward arrows", "Polar (Long leg Anode +, Short leg -)", "Emits light when forward-biased."],
                                ["Transistor (NPN)", "Circle with Collector, Base, Emitter", "Polar", "Acts as solid-state automatic switch or amplifier."],
                                ["Switch", "Two terminals with hinged line", "Non-polar", "Manually opens or closes circuit loop."]
                            ]
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Semiconductors, Doping, Diodes, and LEDs",
                        "content": {
                            "title": "Physics Video: Semiconductors, Doping, Diodes, and LEDs",
                            "description": "Video explaining energy band theory, n-type vs p-type doping, p-n junction depletion layers, and diode circuits.",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "resolved_video_id": "CVsdXKO9xlk"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Semiconductor Physics Tutorial Video",
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
                                "**Band Theory**: Conductors (overlapping), Insulators (large gap $E_g > 5\\text{ eV}$), Semiconductors (narrow gap $E_g \\approx 1\\text{ eV}$).",
                                "**Doping**: Adding pentavalent atoms yields **n-type** (electrons); adding trivalent yields **p-type** (holes).",
                                "**Diodes**: Conduct when forward-biased; block current when reverse-biased.",
                                "Always use a current-limiting resistor with LEDs."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 2: Basic Electronic Circuits and Digital Applications
        # ---------------------------------------------------------------------
        {
            "unit_order": 2,
            "unit_name": "Basic Electronic Circuits and Digital Applications",
            "unit_description": "Half-wave rectification mechanics with single diode (AC to pulsating DC), NPN transistor operating as automatic solid-state switch (Vbe > 0.6 V threshold), light-sensing alarm circuit with LDR, and Input-Process-Output (I-P-O) digital model.",
            "lesson_title": "Basic Electronic Circuits and Digital Applications",
            "pages": [
                # Page 1: Hook & Phone Charger PCB Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Power Rectification: Open Phone Charger Printed Circuit Board",
                        "content": {
                            "title": "Power Rectification: Open Phone Charger Printed Circuit Board",
                            "caption": "An opened smartphone charger showing miniature rectifying semiconductor diodes and smoothing capacitors on a printed circuit board, converting 240 V AC mains into safe 5 V DC.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Phone_charger_circuit_board.jpg/1280px-Phone_charger_circuit_board.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Phone_charger_circuit_board.jpg/1280px-Phone_charger_circuit_board.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Phone Charger Rectifier PCB",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Phone_charger_circuit_board.jpg/1280px-Phone_charger_circuit_board.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Phone_charger_circuit_board.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Taming Wild Alternating Current",
                        "content": {
                            "title": "Why Rectification is Essential",
                            "text": "Mains electricity reverses direction 50 times every second ($50\\text{ Hz}$ AC).\n\nLithium phone batteries can only store Direct Current (DC). Semiconductor diodes perform **rectification**, converting AC into unidirectional DC."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Electronic Circuits & Systems",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain **Half-Wave Rectification** using a single diode.",
                                "Analyze how an **NPN Transistor** operates as an automatic electronic switch.",
                                "Build and calibrate a **light-sensing automatic switch** using an LDR and voltage divider.",
                                "Map electronic systems using the **Input–Process–Output (I-P-O) model**."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Rectification",
                        "content": {
                            "term": "Rectification",
                            "definition": "The conversion of Alternating Current (AC), which reverses periodically, into Direct Current (DC), which flows in one direction only.",
                            "example": "A diode bridge inside a laptop power adapter."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Transistor Switch",
                        "content": {
                            "term": "Transistor Switch",
                            "definition": "A solid-state switching configuration where a small base current/voltage (> 0.6 V) turns on a large collector-emitter current to power an output device.",
                            "example": "Automatic night-time solar street lighting."
                        }
                    }
                ],
                # Page 3: Half-Wave Rectification SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Half-Wave Rectification Circuit and Waveforms",
                        "content": {
                            "title": "Half-Wave Rectification Circuit and Waveforms",
                            "caption": "Half-wave rectifier: Single diode allows positive AC half-cycles to pass while blocking negative cycles, producing a pulsating DC output.",
                            "svg_content": get_svg_half_wave_rectification(),
                            "svg": get_svg_half_wave_rectification()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Half Wave Rectification Diagram",
                            "metadata": {
                                "svg_content": get_svg_half_wave_rectification()
                            }
                        }
                    }
                ],
                # Page 4: Input-Process-Output Framework
                [
                    {
                        "type": "comparison_table",
                        "title": "The Input–Process–Output (I-P-O) Model of Electronic Systems",
                        "content": {
                            "title": "System Architecture Matrix",
                            "headers": ["Stage", "Primary Function", "Example Components", "Real-World Application"],
                            "rows": [
                                ["Input Stage", "Sensors detecting physical changes and generating electrical signals.", "LDR (light), Thermistor (temp), Moisture probe, Switch.", "LDR sensing sunset darkness."],
                                ["Processing Stage", "Makes logical switching decisions by evaluating voltage thresholds.", "NPN Transistor, Microchip, Comparator.", "Transistor turning ON when base $V > 0.6\\text{ V}$."],
                                ["Output Stage", "Actuators converting control signals into physical action.", "LED (light), Buzzer (sound), Motor (motion), Relay.", "Buzzer sounding alarm / Streetlight turning on."]
                            ]
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Thermistor in Voltage Divider Circuit",
                        "content": {
                            "question": "If an NTC thermistor (whose resistance drops when heated and rises when cold) is placed at the bottom of a potential divider connected to the base of an NPN transistor switch, what environmental condition turns on the output LED?",
                            "options": [
                                "An increase in temperature (becoming hot).",
                                "A decrease in temperature (becoming cold).",
                                "An increase in light intensity.",
                                "A change in AC frequency."
                            ],
                            "answer": "B",
                            "explanation": "When temperature decreases (getting cold), the NTC thermistor's resistance rises. In a voltage divider where the thermistor is connected to ground, a high resistance pulls the midpoint base voltage UP. When base voltage crosses the $0.6\\text{ V}$ threshold, the transistor turns ON and lights the LED (acting as a freeze alarm). Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: LDR Switching Circuit Protocol
                [
                    {
                        "type": "step_process",
                        "title": "Laboratory Protocol: Light-Activated Automatic Alarm",
                        "content": {
                            "title": "Building a Transistor Night Light",
                            "steps": [
                                "1. Place NPN transistor (BC547) on breadboard (Emitter, Base, Collector).",
                                "2. Connect variable resistor to + rail and LDR to ground, forming a voltage divider.",
                                "3. Connect divider midpoint to Base (B); connect Emitter (E) directly to ground rail.",
                                "4. Connect Collector (C) to LED and current-limiting resistor to + rail.",
                                "5. Test: Cover LDR with hand; observe LED light up instantly as LDR resistance pulls base voltage > 0.6 V."
                            ]
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Rectification, Transistor Switching, and Sensors",
                        "content": {
                            "title": "Physics Video: Rectification, Transistor Switching, and Sensors",
                            "description": "Video explaining AC rectification with diodes, NPN transistor switching threshold mechanics, and LDR light alarms.",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "resolved_video_id": "CVsdXKO9xlk"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Electronics and Transistor Switching Video",
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
                                "**Rectification**: Diodes convert AC to DC by passing only forward half-cycles.",
                                "**Transistor switch**: Turns ON when base-emitter voltage exceeds $0.6\\text{ V}$.",
                                "**Voltage divider**: Pairs sensor (LDR/Thermistor) with resistor to automate switching.",
                                "Electronic systems follow the **Input–Process–Output (I-P-O)** framework."
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
def ingest_grade10_physics_topic11():
    print("======================================================================")
    print("INGESTING CBC GRADE 10 PHYSICS — TOPIC 11: INTRODUCTION TO ELECTRONICS")
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

    # 3. Get or Create Topic: Introduction to Electronics (Order: 11)
    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=11,
        defaults={
            "name": "Introduction to Electronics",
            "description": "Study of solid-state semiconductor physics, energy band theory, doping (n-type vs p-type), six fundamental components, diode/LED biasing, half-wave AC-DC rectification, NPN transistor automatic switching, and the Input-Process-Output framework."
        }
    )
    if not t_created and topic.name != "Introduction to Electronics":
        topic.name = "Introduction to Electronics"
        topic.description = "Study of solid-state semiconductor physics, energy band theory, doping (n-type vs p-type), six fundamental components, diode/LED biasing, half-wave AC-DC rectification, NPN transistor automatic switching, and the Input-Process-Output framework."
        topic.save()
    print(f"Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    curriculum_data = build_topic11_curriculum_data()

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
    print(f"TOPIC 11 INGESTION COMPLETE:")
    print(f"  - Learning Units: {total_units_created}")
    print(f"  - Lessons:        {total_lessons_created}")
    print(f"  - Lesson Blocks:  {total_blocks_created}")
    print(f"  - Lesson Assets:  {total_assets_created}")
    print("======================================================================")

if __name__ == "__main__":
    ingest_grade10_physics_topic11()
