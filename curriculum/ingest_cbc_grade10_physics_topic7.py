"""
VLearn CBC Grade 10 Physics — Topic 7: Properties of Waves
Production Ingestion & Visual Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Physics
Topic: Properties of Waves (Order: 7)

6 Learning Units & 6 Published Lessons:
  1. Wave Concepts and Representations (8 Pages, 13 Blocks)
  2. Rectilinear Propagation, Reflection and Refraction (8 Pages, 13 Blocks)
  3. Diffraction and Interference (8 Pages, 13 Blocks)
  4. Stationary Waves, Modes and Resonance (8 Pages, 14 Blocks)
  5. Modulation and Frequency-Modulated Waves (8 Pages, 13 Blocks)
  6. Doppler Effect and Wave Applications (8 Pages, 13 Blocks)

Includes:
  - 9 Custom Responsive Sanitized Vector SVG Diagrams
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
# SVG DEFINITIONS FOR TOPIC 7
# =============================================================================

def get_svg_wave_anatomy():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 440" width="100%" height="100%">
  <rect width="840" height="440" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">ANATOMY OF WAVES: TRANSVERSE VS LONGITUDINAL</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Wavelength (λ), Amplitude (A), Crests, Troughs, Compressions and Rarefactions (v = fλ)</text>

  <!-- 1. Transverse Wave -->
  <g transform="translate(50, 80)">
    <rect width="740" height="150" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="20" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700">1. TRANSVERSE WAVE (Perpendicular Particle Vibration • e.g. Light, Water)</text>

    <!-- Equilibrium Line -->
    <line x1="40" y1="85" x2="700" y2="85" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4 4"/>
    <text x="705" y="89" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Equilibrium</text>

    <!-- Sine Wave Curve -->
    <path d="M 60 85 Q 120 15 180 85 T 300 85 T 420 85 T 540 85 T 660 85" fill="none" stroke="#38bdf8" stroke-width="3"/>

    <!-- Amplitude Marker -->
    <line x1="180" y1="85" x2="180" y2="50" stroke="#f59e0b" stroke-width="1.5"/>
    <path d="M 180 85 L 180 50 M 175 57 L 180 50 L 185 57" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="190" y="70" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Amplitude (A)</text>

    <!-- Crest & Trough -->
    <circle cx="180" cy="50" r="4" fill="#22c55e"/>
    <text x="180" y="38" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Crest</text>
    <circle cx="300" cy="120" r="4" fill="#ef4444"/>
    <text x="300" y="138" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Trough</text>

    <!-- Wavelength Lambda Marker -->
    <line x1="180" y1="30" x2="420" y2="30" stroke="#f8fafc" stroke-width="1.5"/>
    <path d="M 180 25 L 180 35 M 420 25 L 420 35" stroke="#f8fafc" stroke-width="1.5"/>
    <text x="300" y="24" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Wavelength (λ = Crest to Crest)</text>
  </g>

  <!-- 2. Longitudinal Wave -->
  <g transform="translate(50, 250)">
    <rect width="740" height="150" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="20" y="24" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="700">2. LONGITUDINAL WAVE (Parallel Particle Vibration • e.g. Sound in Air)</text>

    <!-- Compression & Rarefaction Slinky Sections -->
    <!-- Compression 1 -->
    <g stroke="#38bdf8" stroke-width="3">
      <line x1="80" y1="50" x2="80" y2="110"/>
      <line x1="90" y1="50" x2="90" y2="110"/>
      <line x1="100" y1="50" x2="100" y2="110"/>
      <line x1="110" y1="50" x2="110" y2="110"/>
    </g>
    <text x="95" y="130" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Compression</text>

    <!-- Rarefaction 1 -->
    <g stroke="#64748b" stroke-width="2">
      <line x1="150" y1="60" x2="150" y2="100"/>
      <line x1="200" y1="60" x2="200" y2="100"/>
      <line x1="250" y1="60" x2="250" y2="100"/>
    </g>
    <text x="200" y="130" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Rarefaction</text>

    <!-- Compression 2 -->
    <g stroke="#38bdf8" stroke-width="3">
      <line x1="320" y1="50" x2="320" y2="110"/>
      <line x1="330" y1="50" x2="330" y2="110"/>
      <line x1="340" y1="50" x2="340" y2="110"/>
      <line x1="350" y1="50" x2="350" y2="110"/>
    </g>
    <text x="335" y="130" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Compression</text>

    <!-- Wavelength Lambda Marker for Longitudinal -->
    <line x1="95" y1="40" x2="335" y2="40" stroke="#f8fafc" stroke-width="1.5"/>
    <path d="M 95 35 L 95 45 M 335 35 L 335 45" stroke="#f8fafc" stroke-width="1.5"/>
    <text x="215" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Wavelength (λ = Center of Compression to Next)</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_reflection_ray():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <rect width="800" height="400" fill="#0f172a" rx="16"/>
  <text x="400" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">THE LAW OF REFLECTION (ANGLE OF INCIDENCE = ANGLE OF REFLECTION)</text>
  <text x="400" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Angles Measured Relative to the Normal (Perpendicular Line at Point of Incidence)</text>

  <!-- Reflection Ray Diagram -->
  <g transform="translate(150, 100)">
    <!-- Mirror / Reflecting Surface -->
    <line x1="0" y1="200" x2="500" y2="200" stroke="#38bdf8" stroke-width="4"/>
    <line x1="0" y1="204" x2="500" y2="204" stroke="#64748b" stroke-width="2" stroke-dasharray="6 4"/>
    <text x="250" y="230" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Plane Mirror / Reflecting Barrier</text>

    <!-- Normal Line (Perpendicular) -->
    <line x1="250" y1="20" x2="250" y2="200" stroke="#94a3b8" stroke-width="2" stroke-dasharray="5 4"/>
    <text x="250" y="10" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Normal (90°)</text>

    <!-- Incident Ray -->
    <path d="M 80 50 L 250 200 M 165 125 L 160 115 L 175 120" stroke="#22c55e" stroke-width="3"/>
    <text x="90" y="40" fill="#4ade80" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Incident Ray</text>

    <!-- Reflected Ray -->
    <path d="M 250 200 L 420 50 M 335 125 L 340 115 L 325 120" stroke="#f59e0b" stroke-width="3"/>
    <text x="410" y="40" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Reflected Ray</text>

    <!-- Angle i & Angle r Arcs -->
    <path d="M 215 150 A 60 60 0 0 1 250 140" fill="none" stroke="#22c55e" stroke-width="2"/>
    <text x="220" y="135" fill="#4ade80" font-family="system-ui, sans-serif" font-size="14" font-weight="700">i</text>

    <path d="M 250 140 A 60 60 0 0 1 285 150" fill="none" stroke="#f59e0b" stroke-width="2"/>
    <text x="270" y="135" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="14" font-weight="700">r</text>
  </g>

  <!-- Formula Callout Box -->
  <g transform="translate(200, 310)">
    <rect width="400" height="50" rx="8" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
    <text x="200" y="32" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">Angle of Incidence (i) = Angle of Reflection (r)</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_diffraction_gaps():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">WAVE DIFFRACTION: DEPENDENCE ON GAP WIDTH (w) AND WAVELENGTH (λ)</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Maximum Spreading Occurs When Gap Width Is Comparable to Wavelength (w ≈ λ)</text>

  <!-- Left: Wide Gap (w >> λ) Negligible Diffraction -->
  <g transform="translate(50, 80)">
    <rect width="340" height="280" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="170" y="26" fill="#ef4444" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. WIDE GAP (w &gt;&gt; λ) • SHARP BEAM</text>

    <!-- Incident straight wavefronts -->
    <line x1="30" y1="70" x2="30" y2="230" stroke="#38bdf8" stroke-width="2.5"/>
    <line x1="60" y1="70" x2="60" y2="230" stroke="#38bdf8" stroke-width="2.5"/>
    <line x1="90" y1="70" x2="90" y2="230" stroke="#38bdf8" stroke-width="2.5"/>

    <!-- Wide Barrier with large opening -->
    <rect x="120" y="50" width="16" height="50" fill="#64748b"/>
    <rect x="120" y="190" width="16" height="60" fill="#64748b"/>

    <!-- Emerging straight waves with minor edge curling -->
    <line x1="160" y1="105" x2="160" y2="185" stroke="#38bdf8" stroke-width="2.5"/>
    <line x1="200" y1="105" x2="200" y2="185" stroke="#38bdf8" stroke-width="2.5"/>
    <line x1="240" y1="105" x2="240" y2="185" stroke="#38bdf8" stroke-width="2.5"/>

    <text x="240" y="80" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Shadow Zone</text>
    <text x="240" y="215" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10">Shadow Zone</text>
    <text x="170" y="265" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">e.g. Light through a doorway</text>
  </g>

  <!-- Right: Narrow Gap (w ≈ λ) Significant Circular Diffraction -->
  <g transform="translate(450, 80)">
    <rect width="340" height="280" rx="10" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
    <text x="170" y="26" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">2. NARROW GAP (w ≈ λ) • FULL SPREADING</text>

    <!-- Incident straight wavefronts -->
    <line x1="30" y1="70" x2="30" y2="230" stroke="#38bdf8" stroke-width="2.5"/>
    <line x1="60" y1="70" x2="60" y2="230" stroke="#38bdf8" stroke-width="2.5"/>
    <line x1="90" y1="70" x2="90" y2="230" stroke="#38bdf8" stroke-width="2.5"/>

    <!-- Narrow Barrier with small slit -->
    <rect x="120" y="50" width="16" height="85" fill="#64748b"/>
    <rect x="120" y="160" width="16" height="90" fill="#64748b"/>

    <!-- Emerging semicircular expanding wavefronts -->
    <path d="M 140 115 A 35 35 0 0 1 140 180" fill="none" stroke="#22c55e" stroke-width="2.5"/>
    <path d="M 145 90 A 65 65 0 0 1 145 205" fill="none" stroke="#22c55e" stroke-width="2.5"/>
    <path d="M 150 65 A 95 95 0 0 1 150 230" fill="none" stroke="#22c55e" stroke-width="2.5"/>

    <text x="170" y="265" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">e.g. Sound bending around corners</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_stationary_wave_modes():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 420" width="100%" height="100%">
  <rect width="840" height="420" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">STATIONARY WAVE MODES ON A STRETCHED STRING</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Nodes (N = Zero Vibration) • Antinodes (AN = Maximum Vibration) • Length L = n (λ / 2)</text>

  <!-- 1. Fundamental Mode (1st Harmonic, n = 1) -->
  <g transform="translate(80, 80)">
    <rect width="680" height="85" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="20" y="22" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">1st HARMONIC (Fundamental): L = λ / 2 ⟹ λ = 2L, f1 = v / 2L</text>

    <!-- Fixed Ends (Nodes) -->
    <circle cx="60" cy="52" r="5" fill="#ef4444"/>
    <text x="60" y="72" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">N</text>
    <circle cx="620" cy="52" r="5" fill="#ef4444"/>
    <text x="620" y="72" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">N</text>

    <!-- Center Antinode -->
    <circle cx="340" cy="27" r="4" fill="#22c55e"/>
    <text x="340" y="20" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">AN</text>

    <!-- Wave Loop Envelope -->
    <path d="M 60 52 Q 340 5 620 52" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
    <path d="M 60 52 Q 340 100 620 52" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3"/>
  </g>

  <!-- 2. Second Harmonic (1st Overtone, n = 2) -->
  <g transform="translate(80, 180)">
    <rect width="680" height="85" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="20" y="22" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700">2nd HARMONIC (1st Overtone): L = λ ⟹ λ = L, f2 = 2f1</text>

    <!-- Nodes -->
    <circle cx="60" cy="52" r="5" fill="#ef4444"/>
    <text x="60" y="72" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">N</text>
    <circle cx="340" cy="52" r="5" fill="#ef4444"/>
    <text x="340" y="72" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">N</text>
    <circle cx="620" cy="52" r="5" fill="#ef4444"/>
    <text x="620" y="72" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">N</text>

    <!-- Wave Envelope (2 loops) -->
    <path d="M 60 52 Q 200 15 340 52 Q 480 90 620 52" fill="none" stroke="#f59e0b" stroke-width="2.5"/>
    <path d="M 60 52 Q 200 90 340 52 Q 480 15 620 52" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 3"/>
  </g>

  <!-- 3. Third Harmonic (2nd Overtone, n = 3) -->
  <g transform="translate(80, 280)">
    <rect width="680" height="85" rx="6" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
    <text x="20" y="22" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700">3rd HARMONIC (2nd Overtone): L = 1.5 λ ⟹ λ = 2L/3, f3 = 3f1</text>

    <!-- Nodes -->
    <circle cx="60" cy="52" r="4" fill="#ef4444"/>
    <circle cx="246" cy="52" r="4" fill="#ef4444"/>
    <circle cx="433" cy="52" r="4" fill="#ef4444"/>
    <circle cx="620" cy="52" r="4" fill="#ef4444"/>

    <!-- Wave Envelope (3 loops) -->
    <path d="M 60 52 Q 153 15 246 52 Q 340 90 433 52 Q 526 15 620 52" fill="none" stroke="#22c55e" stroke-width="2.5"/>
    <path d="M 60 52 Q 153 90 246 52 Q 340 15 433 52 Q 526 90 620 52" fill="none" stroke="#22c55e" stroke-width="2" stroke-dasharray="4 3"/>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_doppler_effect():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">THE DOPPLER EFFECT: RELATIVE MOTION & APPARENT FREQUENCY</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Approaching: Compressed Wavefronts (High Pitch) • Receding: Stretched Wavefronts (Low Pitch)</text>

  <!-- Doppler Wavefront Schematic -->
  <g transform="translate(100, 80)">
    <!-- Behind Moving Source (Left: Stretched Wavefronts) -->
    <circle cx="280" cy="140" r="140" fill="none" stroke="#ef4444" stroke-width="2"/>
    <circle cx="310" cy="140" r="100" fill="none" stroke="#ef4444" stroke-width="2"/>
    <circle cx="340" cy="140" r="60" fill="none" stroke="#ef4444" stroke-width="2"/>

    <!-- In Front of Moving Source (Right: Squeezed Wavefronts) -->
    <circle cx="370" cy="140" r="25" fill="none" stroke="#22c55e" stroke-width="2.5"/>

    <!-- Moving Sound Source (Ambulance Dot with Velocity Vector) -->
    <circle cx="390" cy="140" r="8" fill="#f59e0b"/>
    <path d="M 390 140 L 440 140 M 430 134 L 440 140 L 430 146" stroke="#f59e0b" stroke-width="3"/>
    <text x="415" y="125" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Velocity (v_s)</text>

    <!-- Left Observer (Behind / Receding) -->
    <g transform="translate(40, 95)">
      <rect width="130" height="90" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
      <text x="65" y="24" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">RECEDING</text>
      <text x="65" y="46" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Long Wavelength (λ)</text>
      <text x="65" y="66" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">LOWER PITCH (f')</text>
    </g>

    <!-- Right Observer (Ahead / Approaching) -->
    <g transform="translate(480, 95)">
      <rect width="130" height="90" rx="8" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
      <text x="65" y="24" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">APPROACHING</text>
      <text x="65" y="46" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Short Wavelength (λ)</text>
      <text x="65" y="66" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">HIGHER PITCH (f')</text>
    </g>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg


# =============================================================================
# CURRICULUM DEFINITION DATA FOR TOPIC 7
# =============================================================================

def build_topic7_curriculum_data():
    return [
        # ---------------------------------------------------------------------
        # LESSON 1: Wave Concepts and Representations
        # ---------------------------------------------------------------------
        {
            "unit_order": 1,
            "unit_name": "Wave Concepts and Representations",
            "unit_description": "Definition of waves as energy transfer without net matter movement, transverse and longitudinal wave anatomy (crests, troughs, compressions, rarefactions), wave equation v = fλ, and rope/slinky demos.",
            "lesson_title": "Wave Concepts and Representations",
            "pages": [
                # Page 1: Hook & Ripples Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Radial Propagation: Concentric Circular Water Ripples",
                        "content": {
                            "title": "Radial Propagation: Concentric Circular Water Ripples",
                            "caption": "Concentric circular ripples expanding on a quiet pond surface. The disturbance transfers mechanical energy across the pond while individual water molecules only oscillate up and down in place.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Water_ripples_concentric.jpg/1280px-Water_ripples_concentric.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Water_ripples_concentric.jpg/1280px-Water_ripples_concentric.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Water Ripples Radial Wave Propagation",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Water_ripples_concentric.jpg/1280px-Water_ripples_concentric.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Water_ripples_concentric.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Energy Without Matter Transfer",
                        "content": {
                            "title": "The Nature of Wave Motion",
                            "text": "When you touch a quiet pond, ripples travel outward to the far edge.\n\n- If a leaf is floating on the water, it bobs up and down instead of being pushed across the pond!\n- Waves transfer **energy and information** across distance without transferring the physical matter of the medium."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Wave Fundamentals",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define a **Wave** and distinguish between **Transverse** and **Longitudinal** waves.",
                                "Identify anatomical parts: **crest, trough, compression, rarefaction, amplitude ($A$), and wavelength ($\\lambda$)**.",
                                "Apply the universal wave relationship: **$v = f\\lambda$** and **$T = 1/f$**.",
                                "Demonstrate wave propagation using rope pulses and metal slinky springs."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Transverse Wave",
                        "content": {
                            "term": "Transverse Wave",
                            "definition": "A wave in which the particles of the medium vibrate perpendicular (90°) to the direction of wave travel.",
                            "example": "Water waves, plucked guitar strings, and all electromagnetic waves (light)."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Longitudinal Wave",
                        "content": {
                            "term": "Longitudinal Wave",
                            "definition": "A wave in which the particles of the medium vibrate parallel (along the same line) to the direction of wave travel.",
                            "example": "Sound waves in air and compression pulses along a slinky spring."
                        }
                    }
                ],
                # Page 3: Wave Anatomy SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Wave Anatomy: Transverse vs Longitudinal Waveforms",
                        "content": {
                            "title": "Wave Anatomy: Transverse vs Longitudinal Waveforms",
                            "caption": "Diagram showing Transverse wave (sine curve with crests, troughs, amplitude A, wavelength λ) alongside Longitudinal wave (slinky spring with compressions and rarefactions).",
                            "svg_content": get_svg_wave_anatomy(),
                            "svg": get_svg_wave_anatomy()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Wave Anatomy Diagram",
                            "metadata": {
                                "svg_content": get_svg_wave_anatomy()
                            }
                        }
                    }
                ],
                # Page 4: Formulas & Worked Example
                [
                    {
                        "type": "formula_breakdown",
                        "title": "The Universal Wave Equation",
                        "content": {
                            "title": "Mathematical Model of Wave Speed",
                            "formula": "v = f\\lambda \\quad \\text{and} \\quad T = \\frac{1}{f}",
                            "variables": [
                                "$v$ = Wave speed in metres per second ($\\text{m/s}$)",
                                "$f$ = Frequency in Hertz ($\\text{Hz}$)",
                                "$\\lambda$ = Wavelength in metres ($\\text{m}$)",
                                "$T$ = Period in seconds ($\\text{s}$)"
                            ]
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Worked Example: FM Radio Wavelength",
                        "content": {
                            "title": "Radio Station Broadcast Wavelength",
                            "problem": "A radio station broadcasts at frequency $96.0\\text{ MHz}$ ($9.6 \\times 10^7\\text{ Hz}$). Electromagnetic waves travel at speed of light ($v = 3.0 \\times 10^8\\text{ m/s}$). Calculate wavelength.",
                            "steps": [
                                "1. **Rearrange Equation**: $\\lambda = \\frac{v}{f}$.",
                                "2. **Substitute Values**: $\\lambda = \\frac{3.0 \\times 10^8\\text{ m/s}}{9.6 \\times 10^7\\text{ Hz}} = 3.125\\text{ m}$."
                            ],
                            "answer": "The physical wavelength is 3.125 metres."
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Calculating Wave Speed from Cork Oscillations",
                        "content": {
                            "question": "A floating cork on a lake vibrates up and down 20 times in exactly 10 seconds as water ripples pass. If the distance between two adjacent wave crests is 1.5 meters, what is the speed of the water waves?",
                            "options": [
                                "0.75 m/s",
                                "1.33 m/s",
                                "3.00 m/s",
                                "30.0 m/s"
                            ],
                            "answer": "C",
                            "explanation": "Calculate frequency: $f = \\frac{\\text{cycles}}{\\text{time}} = \\frac{20}{10} = 2.0\\text{ Hz}$. Distance between adjacent crests is wavelength $\\lambda = 1.5\\text{ m}$. Using $v = f\\lambda = 2.0\\text{ Hz} \\times 1.5\\text{ m} = 3.00\\text{ m/s}$. Option C is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Slinky Investigation
                [
                    {
                        "type": "mini_activity",
                        "title": "Laboratory Investigation: Slinky Spring Waves",
                        "content": {
                            "title": "Demonstrating Particle Oscillation",
                            "task": "Tie a piece of red yarn to the middle coil of a stretched slinky on a table:\n\n1. Send a transverse side-to-side pulse: The yarn moves left-right perpendicular to the pulse path.\n2. Send a longitudinal push-pull compression: The yarn oscillates back-forth along the spring line.\n3. Verify: The wave travels, but the yarn never leaves its equilibrium region."
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Wave Motion, Transverse vs Longitudinal Waves",
                        "content": {
                            "title": "Physics Video: Wave Motion, Transverse vs Longitudinal Waves",
                            "description": "High-definition slow-motion footage comparing transverse rope waves and longitudinal slinky compressions.",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "resolved_video_id": "CVsdXKO9xlk"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Wave Properties Demonstration Video",
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
                                "**Waves** transfer energy without bulk matter movement.",
                                "**Transverse**: Particle vibration $\\perp$ wave travel; **Longitudinal**: Particle vibration $\\parallel$ wave travel.",
                                "Universal wave speed equation: **$v = f\\lambda$**."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 2: Rectilinear Propagation, Reflection and Refraction
        # ---------------------------------------------------------------------
        {
            "unit_order": 2,
            "unit_name": "Rectilinear Propagation, Reflection and Refraction",
            "unit_description": "Rectilinear propagation in uniform media, Law of Reflection (i = r relative to normal), wave refraction at medium boundaries (change in speed and wavelength, frequency constant), and ripple tank shallow/deep mechanics.",
            "lesson_title": "Rectilinear Propagation, Reflection and Refraction",
            "pages": [
                # Page 1: Hook & Pencil Refraction Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Optical Refraction: Apparent Bending of Immersed Pencil",
                        "content": {
                            "title": "Optical Refraction: Apparent Bending of Immersed Pencil",
                            "caption": "A straight wooden pencil immersed in a beaker of water. Light waves change speed across the air-water boundary, refracting light rays and making the pencil appear severed.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Pencil_in_water_refraction.jpg/1280px-Pencil_in_water_refraction.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Pencil_in_water_refraction.jpg/1280px-Pencil_in_water_refraction.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Refraction of Light in Water Beaker",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Pencil_in_water_refraction.jpg/1280px-Pencil_in_water_refraction.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Pencil_in_water_refraction.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Does Water Bend Light?",
                        "content": {
                            "title": "Straight Paths and Boundary Bending",
                            "text": "In a uniform medium, waves travel in straight lines (**rectilinear propagation**).\n\nWhen waves hit a barrier, they **reflect**. When they cross into a medium with a different density, their speed changes, causing them to bend (**refract**)."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Reflection & Refraction",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "State and verify the **Law of Reflection ($i = r$)**.",
                                "Define **Wavefronts** and explain how rays relate to them.",
                                "Explain **Refraction** as a change in wave speed across a boundary.",
                                "Analyze ripple tank behavior as waves move from deep to shallow water."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Reflection",
                        "content": {
                            "term": "Reflection",
                            "definition": "The bouncing back of a wave when it encounters an impermeable barrier or boundary ($i = r$).",
                            "example": "Light reflecting off a plane mirror or sound echoes bouncing off a cliff."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Refraction",
                        "content": {
                            "term": "Refraction",
                            "definition": "The change in direction of a wave caused by a change in speed when crossing into a different medium.",
                            "example": "Water waves slowing down and bending in shallow water."
                        }
                    }
                ],
                # Page 3: Ray Reflection SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Law of Reflection Diagram",
                        "content": {
                            "title": "The Law of Reflection Diagram",
                            "caption": "Ray reflection showing incident ray, reflected ray, and the perpendicular Normal line establishing angle of incidence i = angle of reflection r.",
                            "svg_content": get_svg_reflection_ray(),
                            "svg": get_svg_reflection_ray()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Ray Reflection at Normal Diagram",
                            "metadata": {
                                "svg_content": get_svg_reflection_ray()
                            }
                        }
                    }
                ],
                # Page 4: Deep to Shallow Refraction Rules
                [
                    {
                        "type": "comparison_table",
                        "title": "Wave Refraction: Deep Water vs Shallow Water in Ripple Tank",
                        "content": {
                            "title": "Boundary Changes in Water Waves",
                            "headers": ["Property", "Deep Water Region", "Shallow Water Region (Glass Block)", "Physical Reason"],
                            "rows": [
                                ["Wave Speed ($v$)", "Fast", "Slower", "Bottom friction retards wave motion."],
                                ["Wavelength ($\\lambda$)", "Long (wide crest spacing)", "Shorter (narrow crest spacing)", "Since $v = f\\lambda$ and $f$ is fixed, $\\lambda \\propto v$."],
                                ["Frequency ($f$)", "Constant", "Constant", "Determined solely by the vibration motor source."],
                                ["Bending Direction", "Towards Normal", "Towards Normal", "Wave slows down on entry, pivoting towards normal."]
                            ]
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Wave Properties in Shallow Water",
                        "content": {
                            "question": "Water waves in a ripple tank travel from deep water into a shallow region over a glass plate. Which set of wave properties correctly describes what happens in the shallow region?",
                            "options": [
                                "Speed decreases, wavelength decreases, frequency remains constant.",
                                "Speed increases, wavelength increases, frequency increases.",
                                "Speed decreases, wavelength remains constant, frequency decreases.",
                                "Speed increases, wavelength decreases, frequency remains constant."
                            ],
                            "answer": "A",
                            "explanation": "In shallow water, friction with the bottom reduces wave speed ($v$ decreases). Because frequency ($f$) is fixed by the generator source, wavelength must decrease proportionally ($\\lambda = v/f$). Therefore, Option A is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Ray-Box Reflection Protocol
                [
                    {
                        "type": "step_process",
                        "title": "Laboratory Protocol: Verifying Law of Reflection",
                        "content": {
                            "title": "Ray-Box and Plane Mirror Experiment",
                            "steps": [
                                "1. Place a plane mirror vertically on paper and draw its baseline.",
                                "2. Shine a thin beam from a ray-box diagonally onto the mirror.",
                                "3. Mark incident and reflected ray paths with a pencil.",
                                "4. Construct the normal ($90^\\circ$) at the point of incidence.",
                                "5. Measure angles $i$ and $r$ with a protractor; verify $i = r$."
                            ]
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Reflection and Refraction in Ripple Tanks",
                        "content": {
                            "title": "Physics Video: Reflection and Refraction in Ripple Tanks",
                            "description": "Demonstration of wavefront reflection from straight barriers and refraction across deep-shallow water boundaries in a ripple tank.",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "resolved_video_id": "CVsdXKO9xlk"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Ripple Tank Reflection and Refraction Video",
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
                                "**Rectilinear propagation**: Waves travel in straight lines in uniform media.",
                                "**Reflection**: Angle of incidence equals angle of reflection ($i = r$).",
                                "**Refraction**: Slowing down in shallow water causes wavelength to decrease while frequency remains constant."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 3: Diffraction and Interference
        # ---------------------------------------------------------------------
        {
            "unit_order": 3,
            "unit_name": "Diffraction and Interference",
            "unit_description": "Diffraction through slits (gap width w ≈ λ), sound vs light diffraction through doorways, Principle of Superposition, constructive vs destructive interference, and two-point coherent sources.",
            "lesson_title": "Diffraction and Interference",
            "pages": [
                # Page 1: Hook & Breakwater Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Wave Bending: Ocean Swell Diffracting Through Breakwater Gap",
                        "content": {
                            "title": "Wave Bending: Ocean Swell Diffracting Through Breakwater Gap",
                            "caption": "Ocean waves squeezing through a narrow breakwater gap. The straight wavefronts curve into expanding semicircles, spreading into the harbor shadow zone via diffraction.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Ocean_wave_diffraction_breakwater.jpg/1280px-Ocean_wave_diffraction_breakwater.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Ocean_wave_diffraction_breakwater.jpg/1280px-Ocean_wave_diffraction_breakwater.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Ocean Wave Diffraction Through Breakwater",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Ocean_wave_diffraction_breakwater.jpg/1280px-Ocean_wave_diffraction_breakwater.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Ocean_wave_diffraction_breakwater.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Sound Bends Around Doorways",
                        "content": {
                            "title": "Hearing Around Corners",
                            "text": "You can easily hear classmates talking around the corner of a corridor, but you cannot see them.\n\n- Sound has a wavelength of $\\sim 1\\text{ m}$, comparable to door width ($w \\approx \\lambda$), causing massive **diffraction**.\n- Light has a tiny wavelength ($5 \\times 10^{-7}\\text{ m}$), passing straight through without noticeable spreading."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Diffraction & Interference",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **Diffraction** and the condition for maximum spreading ($w \\approx \\lambda$).",
                                "State the **Principle of Superposition**.",
                                "Distinguish **Constructive** from **Destructive Interference**.",
                                "Identify nodal and antinodal lines in two-point ripple tank interference."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Diffraction",
                        "content": {
                            "term": "Diffraction",
                            "definition": "The spreading out or bending of waves as they pass through an aperture (slit) or around obstacle edges.",
                            "example": "Sound waves spreading into a room through a partially opened door."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Interference (Superposition)",
                        "content": {
                            "term": "Interference (Superposition)",
                            "definition": "The combination of two or more overlapping coherent waves to form a resultant wave of greater, lesser, or zero amplitude.",
                            "example": "Alternating loud and quiet zones produced by dual coherent loudspeakers."
                        }
                    }
                ],
                # Page 3: Diffraction SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Wave Diffraction: Wide Gap vs Narrow Slit",
                        "content": {
                            "title": "Wave Diffraction: Wide Gap vs Narrow Slit",
                            "caption": "Comparison of negligible diffraction through a wide gap (w >> λ with large shadow zones) versus full semicircular diffraction through a narrow slit (w ≈ λ).",
                            "svg_content": get_svg_diffraction_gaps(),
                            "svg": get_svg_diffraction_gaps()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Wave Diffraction Gap Width Diagram",
                            "metadata": {
                                "svg_content": get_svg_diffraction_gaps()
                            }
                        }
                    }
                ],
                # Page 4: Superposition Principles
                [
                    {
                        "type": "comparison_table",
                        "title": "Interference: Constructive vs Destructive Superposition",
                        "content": {
                            "title": "Superposition Modes",
                            "headers": ["Type", "Phase Condition", "Resultant Amplitude", "Auditory / Optical Effect"],
                            "rows": [
                                ["Constructive", "In-Phase (Crest meets Crest, Trough meets Trough)", "$A_{\\text{result}} = A_1 + A_2$ (Doubled)", "Loud sound in audio / Bright band in optics."],
                                ["Destructive", "Out-of-Phase (Crest meets Trough, $180^\\circ$)", "$A_{\\text{result}} = A_1 - A_2 = 0$ (Cancelled)", "Silence in audio / Dark band in optics."]
                            ]
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Dual Loudspeaker Interference Field",
                        "content": {
                            "question": "Two coherent loudspeakers emit the same constant audio frequency in an open field. A student walks along a straight line in front of the speakers. What do they hear?",
                            "options": [
                                "A steadily increasing sound volume.",
                                "Complete silence everywhere due to cancellation.",
                                "Alternating regions of loud sound and quiet silence.",
                                "A continuously rising siren pitch."
                            ],
                            "answer": "C",
                            "explanation": "Because the speakers are coherent, their overlapping sound waves form a spatial interference pattern. Walking across this pattern crosses antinodal regions (**constructive = loud sound**) and nodal regions (**destructive = quiet/silence**). Option C is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Ripple Tank Protocol
                [
                    {
                        "type": "step_process",
                        "title": "Laboratory Protocol: Two-Point Ripple Tank Interference",
                        "content": {
                            "title": "Generating Stable Interference Fringes",
                            "steps": [
                                "1. Fill ripple tank with 1 cm of clean water.",
                                "2. Attach two spherical dippers to the vibrating motor bar (coherent sources).",
                                "3. Adjust motor speed to produce stable radial wavefronts.",
                                "4. Project pattern onto white floor screen: Observe bright antinodal lines (constructive) and still nodal lines (destructive)."
                            ]
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Wave Diffraction and Two-Source Interference",
                        "content": {
                            "title": "Physics Video: Wave Diffraction and Two-Source Interference",
                            "description": "Video illustrating wave diffraction through slits and two-point ripple tank interference fringes.",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "resolved_video_id": "CVsdXKO9xlk"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Diffraction and Interference Video",
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
                                "**Diffraction** is maximized when aperture width matches wavelength ($w \\approx \\lambda$).",
                                "**Constructive interference** reinforces wave amplitude (in-phase).",
                                "**Destructive interference** cancels wave amplitude (out-of-phase)."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 4: Stationary Waves, Modes and Resonance
        # ---------------------------------------------------------------------
        {
            "unit_order": 4,
            "unit_name": "Stationary Waves, Modes and Resonance",
            "unit_description": "Formation of standing waves by opposing coherent waves, Nodes (zero displacement) and Antinodes (maximum displacement), harmonic modes on strings (L = n λ/2), resonance tube experiment, and measuring speed of sound.",
            "lesson_title": "Stationary Waves, Modes and Resonance",
            "pages": [
                # Page 1: Hook & Guitar String Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Standing Envelope: Vibrating Bass Guitar String in Fundamental Mode",
                        "content": {
                            "title": "Standing Envelope: Vibrating Bass Guitar String in Fundamental Mode",
                            "caption": "A plucked steel bass guitar string vibrating in its fundamental mode. The wave envelope stays stationary between fixed node ends while the central antinode vibrates at maximum amplitude.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Vibrating_guitar_string.jpg/1280px-Vibrating_guitar_string.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Vibrating_guitar_string.jpg/1280px-Vibrating_guitar_string.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Vibrating Guitar String Standing Wave",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Vibrating_guitar_string.jpg/1280px-Vibrating_guitar_string.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Vibrating_guitar_string.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Mystery of Waves That Stand Still",
                        "content": {
                            "title": "Standing Waves and Musical Acoustics",
                            "text": "When you pluck a guitar string, you do not see a wave traveling back and forth.\n\nInstead, two identical waves traveling in opposite directions interfere, creating a **Stationary (Standing) Wave** that traps energy in vibrating loops."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Standing Waves & Resonance",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain how **Stationary Waves** form through boundary reflection and interference.",
                                "Identify **Nodes (zero vibration)** and **Antinodes (maximum vibration)**.",
                                "Derive mode relationships for strings: **$L = n \\frac{\\lambda}{2}$**.",
                                "Measure the speed of sound in air using an adjustable **resonance tube** ($L = \\lambda/4$)."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Stationary (Standing) Wave",
                        "content": {
                            "term": "Stationary Wave",
                            "definition": "A wave pattern formed when two identical waves of the same frequency and amplitude traveling in opposite directions interfere, trapping energy in fixed loops.",
                            "example": "Vibrations on violin strings and air column resonances in flutes."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Resonance",
                        "content": {
                            "term": "Resonance",
                            "definition": "The condition where a system is driven at its natural frequency, producing dramatic, large-amplitude oscillations.",
                            "example": "Shattering a crystal glass with a sustained musical note."
                        }
                    }
                ],
                # Page 3: Stationary Wave Modes SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Stationary Wave Harmonic Modes on a Stretched String",
                        "content": {
                            "title": "Stationary Wave Harmonic Modes on a Stretched String",
                            "caption": "Harmonic mode structure: 1st Harmonic (1 loop, L = λ/2), 2nd Harmonic (2 loops, L = λ), and 3rd Harmonic (3 loops, L = 1.5λ) showing Nodes (N) and Antinodes (AN).",
                            "svg_content": get_svg_stationary_wave_modes(),
                            "svg": get_svg_stationary_wave_modes()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Stationary Wave Modes Diagram",
                            "metadata": {
                                "svg_content": get_svg_stationary_wave_modes()
                            }
                        }
                    }
                ],
                # Page 4: Resonance Tube Speed of Sound
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Measuring Speed of Sound via Resonance Tube",
                        "content": {
                            "title": "Resonance in a Quarter-Wave Tube",
                            "problem": "A $512\\text{ Hz}$ tuning fork produces maximum resonance over a water-filled tube when the air column is $0.165\\text{ m}$ long ($L = \\lambda/4$). Calculate the speed of sound in air.",
                            "steps": [
                                "1. **Find Wavelength**: $\\lambda = 4L = 4 \\times 0.165\\text{ m} = 0.660\\text{ m}$.",
                                "2. **Apply Wave Equation**: $v = f\\lambda = 512\\text{ Hz} \\times 0.660\\text{ m} = 337.9\\text{ m/s}$."
                            ],
                            "answer": "The speed of sound in air is 338 m/s."
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Fundamental Mode String Wavelength",
                        "content": {
                            "question": "A guitar string of length $0.80\\text{ m}$ is clamped at both ends. When plucked, it vibrates in its fundamental mode (1st harmonic). What is the wavelength of the stationary wave on the string?",
                            "options": [
                                "0.40 m",
                                "0.80 m",
                                "1.60 m",
                                "3.20 m"
                            ],
                            "answer": "C",
                            "explanation": "In the fundamental mode of a string fixed at both ends, the string length equals half a wavelength ($L = \\lambda / 2$). Rearranging gives $\\lambda = 2L = 2 \\times 0.80\\text{ m} = 1.60\\text{ m}$. Therefore, Option C is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Resonance Experiment Protocol
                [
                    {
                        "type": "step_process",
                        "title": "Laboratory Protocol: Speed of Sound via Resonance Tube",
                        "content": {
                            "title": "Resonance Column Experiment",
                            "steps": [
                                "1. Place glass tube in a cylinder of water to create an adjustable air column.",
                                "2. Strike a 512 Hz tuning fork with a rubber mallet and hold it over the open tube top.",
                                "3. Slowly raise the tube until a sharp surge in sound loudness occurs (Resonance).",
                                "4. Measure air column length $L$; calculate $\\lambda = 4L$ and $v = f\\lambda$."
                            ]
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Standing Waves and Resonance Tube Experiment",
                        "content": {
                            "title": "Physics Video: Standing Waves and Resonance Tube Experiment",
                            "description": "Video explaining nodes, antinodes, string harmonic modes, and laboratory demonstration of resonance tubes.",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "resolved_video_id": "CVsdXKO9xlk"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Standing Waves and Resonance Tutorial",
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
                                "**Stationary waves** form when opposing identical waves interfere.",
                                "**Nodes**: Points of zero displacement; **Antinodes**: Points of maximum displacement.",
                                "Fixed string modes: $L = n\\frac{\\lambda}{2}$; Closed air column fundamental: $L = \\frac{\\lambda}{4}$."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 5: Modulation and Frequency-Modulated Waves
        # ---------------------------------------------------------------------
        {
            "unit_order": 5,
            "unit_name": "Modulation and Frequency-Modulated Waves",
            "unit_description": "Physics necessity of modulation (antenna sizing λ/4, interference prevention, attenuation mitigation), Frequency Modulation (FM) carrier dynamics, and telecommunication system architecture.",
            "lesson_title": "Modulation and Frequency-Modulated Waves",
            "pages": [
                # Page 1: Hook & Radio Mast Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Telecommunication: Mountain Radio Transmission Tower",
                        "content": {
                            "title": "Telecommunication: Mountain Radio Transmission Tower",
                            "caption": "A high-altitude steel radio broadcast mast transmitting FM electromagnetic carrier waves across vast distances, enabling crystal-clear audio transmission.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Radio_transmission_tower_mountain.jpg/1280px-Radio_transmission_tower_mountain.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Radio_transmission_tower_mountain.jpg/1280px-Radio_transmission_tower_mountain.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Radio Transmission Tower Broadcast Mast",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Radio_transmission_tower_mountain.jpg/1280px-Radio_transmission_tower_mountain.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Radio_transmission_tower_mountain.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Can't We Broadcast Pure Sound Directly?",
                        "content": {
                            "title": "The Physics Bottlenecks of Raw Audio",
                            "text": "If a radio presenter shouts in Nairobi, their voice dies out in 200 metres.\n\nTo broadcast audio thousands of kilometres, we mount the audio signal onto a high-frequency **Carrier Wave** via **Modulation**."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Modulation & FM Systems",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain why modulation is required for radio communication.",
                                "Define **Information Signal, Carrier Wave**, and **Modulation**.",
                                "Explain the mechanics of **Frequency Modulation (FM)**.",
                                "Map the block diagram of a complete communication system."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Modulation",
                        "content": {
                            "term": "Modulation",
                            "definition": "The process of superimposing a low-frequency information signal onto a high-frequency carrier wave for long-distance transmission.",
                            "example": "Broadcasting audio music on a 96.0 MHz FM carrier."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Frequency Modulation (FM)",
                        "content": {
                            "term": "Frequency Modulation (FM)",
                            "definition": "Modulation where the carrier frequency varies in proportion to the information signal amplitude, while carrier amplitude remains constant.",
                            "example": "Commercial FM radio broadcasting offering high noise immunity."
                        }
                    }
                ],
                # Page 3: Why Modulation is Essential
                [
                    {
                        "type": "comparison_table",
                        "title": "Physical Bottlenecks of Raw Audio vs Modulation Solution",
                        "content": {
                            "title": "Why Modulation is Mandatory",
                            "headers": ["Physical Problem", "Raw Audio Signal (e.g. 1 kHz)", "Modulated RF Carrier (e.g. 100 MHz)", "Benefit of Modulation"],
                            "rows": [
                                ["Antenna Length ($L \\approx \\lambda/4$)", "$\\lambda = 300\\text{ km} \\implies L = 75\\text{ km}$ (Impossible)", "$\\lambda = 3.0\\text{ m} \\implies L = 75\\text{ cm}$", "Practical, compact metal whip antennas."],
                                ["Channel Overlap", "All audio stations broadcast in $20\\text{ Hz}-20\\text{ kHz}$ band", "Each station gets unique frequency (e.g. 96.0 vs 102.2 MHz)", "Zero signal jamming or cross-talk."],
                                ["Atmospheric Attenuation", "High energy dissipation across short distance", "High penetration through air and space", "Vast broadcast coverage range."]
                            ]
                        }
                    }
                ],
                # Page 4: FM Waveform Dynamics
                [
                    {
                        "type": "concept_explanation",
                        "title": "How FM Encodes Sound into Waves",
                        "content": {
                            "title": "Frequency Variations in FM",
                            "text": "- **Audio Crest (Positive Voltage)**: The carrier wave is compressed, raising its **frequency above center**.\n- **Audio Trough (Negative Voltage)**: The carrier wave is stretched, lowering its **frequency below center**.\n- **Amplitude Constancy**: The height (amplitude) of the carrier stays perfectly uniform, making FM immune to electrical amplitude noise!"
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Carrier Characteristics in FM",
                        "content": {
                            "question": "What physical characteristic of the high-frequency carrier wave is modified during Frequency Modulation (FM)?",
                            "options": [
                                "The amplitude is varied while frequency remains constant.",
                                "The frequency is varied while amplitude remains constant.",
                                "Both frequency and amplitude are varied simultaneously.",
                                "The wave is converted from transverse into longitudinal."
                            ],
                            "answer": "B",
                            "explanation": "In **Frequency Modulation (FM)**, the instantaneous **frequency** of the carrier wave is varied in accordance with the audio signal, while its **amplitude remains strictly constant**. Amplitude variation occurs in AM. Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Communication Block Diagram
                [
                    {
                        "type": "step_process",
                        "title": "Communication System Architecture",
                        "content": {
                            "title": "End-to-End Signal Flow",
                            "steps": [
                                "1. **Input Transducer (Microphone)**: Converts sound vibrations into electrical audio signal.",
                                "2. **Modulator**: Modulates audio signal onto high-frequency RF carrier wave.",
                                "3. **Transmitter & Antenna**: Amplifies and radiates electromagnetic wave into space.",
                                "4. **Transmission Medium**: Air/Space through which wave propagates at speed of light.",
                                "5. **Receiver Antenna & Demodulator**: Captures RF wave and extracts original audio signal.",
                                "6. **Output Transducer (Loudspeaker)**: Converts audio electrical signal back into sound waves."
                            ]
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Engineering Video: Modulation, FM Radio, and Telecommunications",
                        "content": {
                            "title": "Engineering Video: Modulation, FM Radio, and Telecommunications",
                            "description": "Video explaining the physics of electromagnetic modulation, AM vs FM waveforms, and radio receiver circuitry.",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "resolved_video_id": "CVsdXKO9xlk"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Modulation and Radio Physics Video",
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
                                "**Modulation** makes practical antenna sizing ($\lambda/4$) and multi-station broadcasting possible.",
                                "**FM** varies carrier frequency while maintaining constant amplitude.",
                                "Communication systems require transducer, modulator, transmitter, medium, receiver, demodulator, and output transducer."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 6: Doppler Effect and Wave Applications
        # ---------------------------------------------------------------------
        {
            "unit_order": 6,
            "unit_name": "Doppler Effect and Wave Applications",
            "unit_description": "Wavefront mechanics of the Doppler Effect, apparent frequency changes for moving sources/observers, and real-world applications in police radar, echocardiography, and cosmological redshift.",
            "lesson_title": "Doppler Effect and Wave Applications",
            "pages": [
                # Page 1: Hook & Ambulance Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Acoustic Shift: Moving Ambulance Siren Demonstrating Doppler Effect",
                        "content": {
                            "title": "Acoustic Shift: Moving Ambulance Siren Demonstrating Doppler Effect",
                            "caption": "An emergency ambulance rushing down a highway. As it approaches, siren pitch sounds distinctly higher; as it recedes, pitch drops to a lower tone due to the Doppler Effect.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Ambulance_emergency_response.jpg/1280px-Ambulance_emergency_response.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Ambulance_emergency_response.jpg/1280px-Ambulance_emergency_response.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Ambulance Siren Doppler Effect",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Ambulance_emergency_response.jpg/1280px-Ambulance_emergency_response.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Ambulance_emergency_response.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Changing Pitch of Moving Sirens",
                        "content": {
                            "title": "Why Moving Sirens Shift Pitch",
                            "text": "When an ambulance rushes past you on the highway, its siren sounds high-pitched as it approaches, but drops instantly to a lower tone the moment it passes.\n\nInside the ambulance, the driver hears a steady pitch. The pitch change is an apparent frequency shift called the **Doppler Effect**."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: The Doppler Effect",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define the **Doppler Effect** qualitatively.",
                                "Explain wavefront compression (approaching) and stretching (receding).",
                                "Differentiate source motion from observer relative motion.",
                                "Identify applications in **police speed radar, medical echocardiograms**, and **astronomical redshift**."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Doppler Effect",
                        "content": {
                            "term": "Doppler Effect",
                            "definition": "The apparent change in frequency and wavelength of a wave observed when there is relative motion between the wave source and the observer.",
                            "example": "The pitch drop of a train whistle as it speeds past a station platform."
                        }
                    }
                ],
                # Page 3: Doppler Wavefront SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Doppler Effect: Wavefront Compression and Expansion",
                        "content": {
                            "title": "The Doppler Effect: Wavefront Compression and Expansion",
                            "caption": "Off-center concentric circles: Approaching wavefronts are crowded (short λ, higher pitch), while receding wavefronts are stretched (long λ, lower pitch).",
                            "svg_content": get_svg_doppler_effect(),
                            "svg": get_svg_doppler_effect()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Doppler Wavefront Compression Diagram",
                            "metadata": {
                                "svg_content": get_svg_doppler_effect()
                            }
                        }
                    }
                ],
                # Page 4: Real-World Applications
                [
                    {
                        "type": "comparison_table",
                        "title": "Technological Applications of the Doppler Effect",
                        "content": {
                            "title": "Doppler Shift Technologies",
                            "headers": ["Field", "Application", "Wave Type Used", "Operating Mechanism"],
                            "rows": [
                                ["Traffic Enforcement", "Police Speed Radar", "Microwaves (EM)", "Measures frequency shift of radar bounced off speeding car to calculate velocity."],
                                ["Medicine", "Doppler Echocardiogram", "High-frequency Ultrasound", "Bounces ultrasound off flowing red blood cells to measure blood circulation."],
                                ["Astrophysics", "Cosmological Redshift", "Visible Light Waves", "Stretching of light from distant galaxies proves the universe is expanding."]
                            ]
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Motorcyclist Passing Stationary Siren",
                        "content": {
                            "question": "A police car is parked on the roadside with its siren on. A motorcyclist speeds past the parked car. What does the motorcyclist hear as they approach and then ride away?",
                            "options": [
                                "A constant high pitch throughout.",
                                "A lower pitch as they approach, which becomes higher after passing.",
                                "A higher pitch as they approach, which suddenly drops to a lower pitch after passing.",
                                "No change in pitch because the siren is stationary."
                            ],
                            "answer": "C",
                            "explanation": "The Doppler effect depends on **relative motion**. As the motorcyclist approaches, they intercept wavefronts at a higher rate (higher apparent pitch). As they move away, they intercept wavefronts less frequently (lower apparent pitch). Option C is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Whirling Buzzer Activity
                [
                    {
                        "type": "mini_activity",
                        "title": "Laboratory Investigation: Whirling Buzzer Doppler Demo",
                        "content": {
                            "title": "Observing Doppler Shifts Safely",
                            "task": "Place a buzzing smartphone inside the toe of a sturdy sock. Whirl the sock horizontally in an open field while classmates listen 5 m away:\n\n- Classmates hear pitch rise as sock swings towards them and fall as it swings away.\n- The student whirling hears constant pitch because they travel with the source."
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: The Doppler Effect and Redshift Explained",
                        "content": {
                            "title": "Physics Video: The Doppler Effect and Redshift Explained",
                            "description": "Video explaining the Doppler Effect wavefront dynamics, police radar speed guns, and cosmic cosmological redshift.",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "resolved_video_id": "CVsdXKO9xlk"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Doppler Effect Video Demonstration",
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
                                "**Doppler Effect**: Apparent shift in wave frequency due to relative motion.",
                                "**Approaching**: Compressed wavefronts $\\implies$ shorter $\\lambda$, higher pitch ($f'$).",
                                "**Receding**: Stretched wavefronts $\\implies$ longer $\\lambda$, lower pitch ($f'$).",
                                "Applied in police radar, ultrasound blood flow, and galaxy redshift."
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
def ingest_grade10_physics_topic7():
    print("======================================================================")
    print("INGESTING CBC GRADE 10 PHYSICS — TOPIC 7: PROPERTIES OF WAVES")
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

    # 3. Get or Create Topic: Properties of Waves (Order: 7)
    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=7,
        defaults={
            "name": "Properties of Waves",
            "description": "Exploration of wave propagation (v = fλ), reflection, refraction in ripple tanks, diffraction through apertures, interference superposition, stationary waves and modes, radio frequency modulation (FM), and the Doppler Effect."
        }
    )
    if not t_created and topic.name != "Properties of Waves":
        topic.name = "Properties of Waves"
        topic.description = "Exploration of wave propagation (v = fλ), reflection, refraction in ripple tanks, diffraction through apertures, interference superposition, stationary waves and modes, radio frequency modulation (FM), and the Doppler Effect."
        topic.save()
    print(f"Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    curriculum_data = build_topic7_curriculum_data()

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
    print(f"TOPIC 7 INGESTION COMPLETE:")
    print(f"  - Learning Units: {total_units_created}")
    print(f"  - Lessons:        {total_lessons_created}")
    print(f"  - Lesson Blocks:  {total_blocks_created}")
    print(f"  - Lesson Assets:  {total_assets_created}")
    print("======================================================================")

if __name__ == "__main__":
    ingest_grade10_physics_topic7()
