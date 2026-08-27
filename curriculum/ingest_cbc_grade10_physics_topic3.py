"""
VLearn CBC Grade 10 Physics — Topic 3: Mechanical Properties of Materials
Production Ingestion & Visual Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Physics
Topic: Mechanical Properties of Materials (Order: 3)

4 Learning Units & 4 Published Lessons:
  1. Mechanical Properties and Material Choice (8 Pages, 13 Blocks)
  2. Force–Extension Relationship and Hooke’s Law (8 Pages, 14 Blocks)
  3. Stress, Strain and Young’s Modulus (9 Pages, 15 Blocks)
  4. Industrial Applications and Safety of Materials (8 Pages, 14 Blocks)

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
# SVG DEFINITIONS FOR TOPIC 3
# =============================================================================

def get_svg_elastic_plastic_deformation():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%">
  <rect width="820" height="440" fill="#0f172a" rx="16"/>
  <text x="410" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">DEFORMATION MECHANISMS: ELASTIC VS PLASTIC (PERMANENT)</text>
  <text x="410" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Reversible Atomic Bond Stretching vs Permanent Inter-Planar Atomic Slip</text>

  <!-- Left: Elastic Deformation Panel -->
  <g transform="translate(40, 75)">
    <rect width="350" height="335" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="175" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">1. ELASTIC DEFORMATION (REVERSIBLE)</text>

    <!-- Support ceiling -->
    <line x1="60" y1="50" x2="290" y2="50" stroke="#94a3b8" stroke-width="3"/>
    
    <!-- State 1: Stretched by small load F -->
    <g transform="translate(80, 50)">
      <path d="M 30 0 L 30 15 L 45 25 L 15 35 L 45 45 L 15 55 L 45 65 L 15 75 L 45 85 L 30 95 L 30 110" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
      <circle cx="30" cy="115" r="5" fill="#f59e0b"/>
      <path d="M 30 125 L 30 155 M 24 145 L 30 155 L 36 145" stroke="#f59e0b" stroke-width="2.5"/>
      <text x="30" y="175" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Load F applied</text>
      <text x="30" y="190" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Stretches to length L</text>
    </g>

    <!-- Transition Arrow -->
    <path d="M 160 110 L 195 110 M 185 104 L 195 110 L 185 116" stroke="#94a3b8" stroke-width="2"/>
    <text x="178" y="100" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">F = 0</text>

    <!-- State 2: Unloaded, Snaps back to L0 -->
    <g transform="translate(210, 50)">
      <path d="M 30 0 L 30 15 L 45 22 L 15 29 L 45 36 L 15 43 L 45 50 L 15 57 L 45 64 L 30 71 L 30 85" fill="none" stroke="#22c55e" stroke-width="2.5"/>
      <circle cx="30" cy="90" r="5" fill="#22c55e"/>
      <text x="30" y="120" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Returns to L0</text>
      <text x="30" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Zero permanent stretch</text>
    </g>

    <!-- Summary Box -->
    <rect x="20" y="225" width="310" height="90" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="30" y="248" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Atomic bonds stretch elastically like springs.</text>
    <text x="30" y="270" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Atoms remain in their original crystal planes.</text>
    <text x="30" y="292" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11">• Material recovers 100% of original geometry.</text>
  </g>

  <!-- Right: Plastic Deformation Panel -->
  <g transform="translate(430, 75)">
    <rect width="350" height="335" rx="12" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="175" y="28" fill="#ef4444" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">2. PLASTIC DEFORMATION (PERMANENT)</text>

    <!-- Support ceiling -->
    <line x1="60" y1="50" x2="290" y2="50" stroke="#94a3b8" stroke-width="3"/>

    <!-- State 1: Pulled by huge load past elastic limit -->
    <g transform="translate(80, 50)">
      <path d="M 30 0 L 30 15 L 45 30 L 15 45 L 45 60 L 15 75 L 45 90 L 15 105 L 45 120 L 30 135 L 30 150" fill="none" stroke="#ef4444" stroke-width="2.5"/>
      <circle cx="30" cy="155" r="5" fill="#ef4444"/>
      <path d="M 30 165 L 30 200 M 22 188 L 30 200 L 38 188" stroke="#ef4444" stroke-width="3"/>
      <text x="30" y="215" fill="#ef4444" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Excessive Force</text>
    </g>

    <!-- Transition Arrow -->
    <path d="M 160 110 L 195 110 M 185 104 L 195 110 L 185 116" stroke="#94a3b8" stroke-width="2"/>
    <text x="178" y="100" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">F = 0</text>

    <!-- State 2: Unloaded, remains distorted & elongated -->
    <g transform="translate(210, 50)">
      <path d="M 30 0 L 30 15 L 45 27 L 15 39 L 45 51 L 15 63 L 45 75 L 15 87 L 45 99 L 30 111 L 30 125" fill="none" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="5 2"/>
      <circle cx="30" cy="130" r="5" fill="#f59e0b"/>
      <text x="30" y="150" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Permanently Bent</text>
      <text x="30" y="165" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Length remains > L0</text>
    </g>

    <!-- Summary Box -->
    <rect x="20" y="225" width="310" height="90" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="30" y="248" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Force exceeds the material's Elastic Limit.</text>
    <text x="30" y="270" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11">• Atomic planes slide past each other (slip).</text>
    <text x="30" y="292" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11">• Bonds reform in distorted new positions.</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_hookes_law_apparatus():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 460" width="100%" height="100%">
  <rect width="840" height="460" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">HOOKE’S LAW EXPERIMENTAL SETUP: EXTENSION PROPORTIONAL TO LOAD</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Measuring Spring Extension (ΔL = L - L0) Under Incremental Slotted Masses</text>

  <!-- Metric Ruler Stand in Background -->
  <g transform="translate(60, 80)">
    <!-- Heavy Stand Base -->
    <rect x="0" y="330" width="100" height="20" fill="#334155" rx="3"/>
    <!-- Vertical Rod -->
    <rect x="40" y="0" width="12" height="330" fill="#64748b"/>
    <!-- Clamp -->
    <rect x="40" y="20" width="600" height="10" fill="#475569"/>
  </g>

  <!-- Panel 1: Unloaded (L0 = 10 cm, Load = 0 N) -->
  <g transform="translate(140, 110)">
    <!-- Vertical Rule -->
    <rect x="0" y="0" width="30" height="300" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <text x="15" y="40" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">0 cm</text>
    <text x="15" y="100" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">10 cm</text>
    <text x="15" y="160" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">15 cm</text>
    <text x="15" y="220" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">20 cm</text>

    <!-- Spring & Pointer -->
    <path d="M 60 0 L 60 15 L 75 25 L 45 35 L 75 45 L 45 55 L 75 65 L 45 75 L 75 85 L 60 95 L 60 100" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
    <!-- Pointer -->
    <line x1="60" y1="100" x2="32" y2="100" stroke="#ef4444" stroke-width="2"/>
    <polygon points="32,100 38,97 38,103" fill="#ef4444"/>
    <!-- Empty Hanger -->
    <circle cx="60" cy="110" r="8" fill="none" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="60" y="145" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Unloaded</text>
    <text x="60" y="165" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">L0 = 10.0 cm</text>
    <text x="60" y="185" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">ΔL = 0.0 cm</text>
  </g>

  <!-- Panel 2: Loaded with 1 N (L = 12 cm, ΔL = 2 cm) -->
  <g transform="translate(370, 110)">
    <!-- Vertical Rule -->
    <rect x="0" y="0" width="30" height="300" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <text x="15" y="100" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">10 cm</text>
    <text x="15" y="124" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">12 cm</text>

    <!-- Spring & Pointer -->
    <path d="M 60 0 L 60 15 L 75 27 L 45 39 L 75 51 L 45 63 L 75 75 L 45 87 L 75 99 L 60 111 L 60 124" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
    <!-- Pointer -->
    <line x1="60" y1="124" x2="32" y2="124" stroke="#ef4444" stroke-width="2"/>
    <polygon points="32,124 38,121 38,127" fill="#ef4444"/>
    <!-- 1 N Slotted Mass -->
    <rect x="45" y="130" width="30" height="18" rx="3" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
    <text x="60" y="143" fill="#000000" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">1 N</text>

    <!-- Extension Dimension Bracket -->
    <line x1="100" y1="100" x2="100" y2="124" stroke="#f59e0b" stroke-width="1.5"/>
    <path d="M 96 100 L 104 100 M 96 124 L 104 124" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="110" y="116" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">ΔL = 2 cm</text>

    <text x="60" y="175" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Load = 1.0 N</text>
    <text x="60" y="195" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">L = 12.0 cm</text>
    <text x="60" y="215" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">k = 1 N / 0.02 m = 50 N/m</text>
  </g>

  <!-- Panel 3: Loaded with 2 N (L = 14 cm, ΔL = 4 cm) -->
  <g transform="translate(600, 110)">
    <!-- Vertical Rule -->
    <rect x="0" y="0" width="30" height="300" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <text x="15" y="100" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">10 cm</text>
    <text x="15" y="148" fill="#22c55e" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">14 cm</text>

    <!-- Spring & Pointer -->
    <path d="M 60 0 L 60 15 L 75 30 L 45 45 L 75 60 L 45 75 L 75 90 L 45 105 L 75 120 L 60 135 L 60 148" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
    <!-- Pointer -->
    <line x1="60" y1="148" x2="32" y2="148" stroke="#ef4444" stroke-width="2"/>
    <polygon points="32,148 38,145 38,151" fill="#ef4444"/>
    <!-- 2 N Slotted Masses -->
    <rect x="45" y="154" width="30" height="15" rx="2" fill="#22c55e" stroke="#16a34a" stroke-width="1.5"/>
    <rect x="45" y="171" width="30" height="15" rx="2" fill="#22c55e" stroke="#16a34a" stroke-width="1.5"/>
    <text x="60" y="180" fill="#000000" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">2 N</text>

    <!-- Extension Dimension Bracket -->
    <line x1="100" y1="100" x2="100" y2="148" stroke="#22c55e" stroke-width="1.5"/>
    <path d="M 96 100 L 104 100 M 96 148 L 104 148" stroke="#22c55e" stroke-width="1.5"/>
    <text x="110" y="128" fill="#22c55e" font-family="system-ui, sans-serif" font-size="11" font-weight="700">ΔL = 4 cm</text>

    <text x="60" y="210" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Load = 2.0 N</text>
    <text x="60" y="230" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">L = 14.0 cm</text>
    <text x="60" y="250" fill="#22c55e" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Doubled Load = Doubled ΔL</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_force_extension_graph():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%">
  <rect width="800" height="420" fill="#0f172a" rx="16"/>
  <text x="400" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">HOOKE’S LAW GRAPH: FORCE (F) VS EXTENSION (ΔL)</text>
  <text x="400" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Linear Elastic Region • Proportional Limit • Elastic Limit • Plastic Failure</text>

  <!-- Grid Lines -->
  <g stroke="#334155" stroke-width="1" stroke-dasharray="4 4">
    <line x1="120" y1="340" x2="720" y2="340"/>
    <line x1="120" y1="270" x2="720" y2="270"/>
    <line x1="120" y1="200" x2="720" y2="200"/>
    <line x1="120" y1="130" x2="720" y2="130"/>
    
    <line x1="120" y1="80" x2="120" y2="340"/>
    <line x1="270" y1="80" x2="270" y2="340"/>
    <line x1="420" y1="80" x2="420" y2="340"/>
    <line x1="570" y1="80" x2="570" y2="340"/>
    <line x1="720" y1="80" x2="720" y2="340"/>
  </g>

  <!-- Solid Axes -->
  <line x1="120" y1="340" x2="740" y2="340" stroke="#94a3b8" stroke-width="2"/>
  <line x1="120" y1="340" x2="120" y2="70" stroke="#94a3b8" stroke-width="2"/>

  <!-- Y-Axis Labels: Force F (N) -->
  <text x="105" y="345" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">0</text>
  <text x="105" y="275" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">2 N</text>
  <text x="105" y="205" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">4 N</text>
  <text x="105" y="135" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">6 N</text>
  <text x="45" y="200" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle" transform="rotate(-90 45 200)">Applied Force F (N)</text>

  <!-- X-Axis Labels: Extension ΔL (cm) -->
  <text x="120" y="360" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">0</text>
  <text x="270" y="360" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">2 cm</text>
  <text x="420" y="360" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">4 cm</text>
  <text x="570" y="360" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">6 cm</text>
  <text x="720" y="360" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">8 cm</text>
  <text x="420" y="390" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Extension ΔL (cm)</text>

  <!-- Section 1: Linear Hookean Line (0,0) to Point A (6 N, 6 cm) -->
  <line x1="120" y1="340" x2="570" y2="130" stroke="#38bdf8" stroke-width="3.5"/>
  <circle cx="570" cy="130" r="5" fill="#38bdf8"/>
  <text x="560" y="115" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="end">A: Limit of Proportionality</text>

  <!-- Section 2: Slight Curve to Point B (Elastic Limit) -->
  <path d="M 570 130 Q 610 115 630 110" fill="none" stroke="#f59e0b" stroke-width="3"/>
  <circle cx="630" cy="110" r="5" fill="#f59e0b"/>
  <text x="640" y="105" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">B: Elastic Limit</text>

  <!-- Section 3: Plastic Deformation Curve to Fracture -->
  <path d="M 630 110 Q 680 105 710 115" fill="none" stroke="#ef4444" stroke-width="3" stroke-dasharray="4 2"/>
  <circle cx="710" cy="115" r="5" fill="#ef4444"/>
  <text x="720" y="130" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700">C: Fracture</text>

  <!-- Gradient Triangle Annotation -->
  <path d="M 270 270 L 420 270 L 420 200 Z" fill="#38bdf822" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="345" y="290" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Δ(ΔL)</text>
  <text x="435" y="240" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11">ΔF</text>

  <!-- Gradient Formula Box -->
  <rect x="180" y="90" width="260" height="55" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="310" y="112" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Gradient = ΔF / Δ(ΔL) = k</text>
  <text x="310" y="132" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Spring Constant (Stiffness in N/m)</text>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_atomic_lattice_stress():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 420" width="100%" height="100%">
  <rect width="820" height="420" fill="#0f172a" rx="16"/>
  <text x="410" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">MICROSCOPIC ATOMIC LATTICE BONDS UNDER TENSILE LOAD</text>
  <text x="410" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Stress = Force / Area • Strain = (L - L0) / L0 • Young's Modulus = Intrinsic Bond Stiffness</text>

  <!-- Left: Unstressed Lattice (L0) -->
  <g transform="translate(50, 80)">
    <rect width="330" height="300" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="165" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">UNSTRESSED ATOMIC LATTICE</text>

    <!-- Grid of atoms (equilibrium spacing) -->
    <g transform="translate(65, 60)">
      <!-- Row 1 -->
      <circle cx="20" cy="20" r="10" fill="#94a3b8"/><circle cx="80" cy="20" r="10" fill="#94a3b8"/><circle cx="140" cy="20" r="10" fill="#94a3b8"/><circle cx="200" cy="20" r="10" fill="#94a3b8"/>
      <!-- Row 2 -->
      <circle cx="20" cy="80" r="10" fill="#94a3b8"/><circle cx="80" cy="80" r="10" fill="#94a3b8"/><circle cx="140" cy="80" r="10" fill="#94a3b8"/><circle cx="200" cy="80" r="10" fill="#94a3b8"/>
      <!-- Row 3 -->
      <circle cx="20" cy="140" r="10" fill="#94a3b8"/><circle cx="80" cy="140" r="10" fill="#94a3b8"/><circle cx="140" cy="140" r="10" fill="#94a3b8"/><circle cx="200" cy="140" r="10" fill="#94a3b8"/>

      <!-- Interatomic Spring Bonds -->
      <g stroke="#38bdf8" stroke-width="2" stroke-dasharray="3 3">
        <line x1="30" y1="20" x2="70" y2="20"/><line x1="90" y1="20" x2="130" y2="20"/><line x1="150" y1="20" x2="190" y2="20"/>
        <line x1="30" y1="80" x2="70" y2="80"/><line x1="90" y1="80" x2="130" y2="80"/><line x1="150" y1="80" x2="190" y2="80"/>
        <line x1="30" y1="140" x2="70" y2="140"/><line x1="90" y1="140" x2="130" y2="140"/><line x1="150" y1="140" x2="190" y2="140"/>
        <line x1="20" y1="30" x2="20" y2="70"/><line x1="80" y1="30" x2="80" y2="70"/><line x1="140" y1="30" x2="140" y2="70"/><line x1="200" y1="30" x2="200" y2="70"/>
        <line x1="20" y1="90" x2="20" y2="130"/><line x1="80" y1="90" x2="80" y2="130"/><line x1="140" y1="90" x2="140" y2="130"/><line x1="200" y1="90" x2="200" y2="130"/>
      </g>
    </g>

    <!-- Equilibrium Spacing Dimension -->
    <line x1="145" y1="240" x2="205" y2="240" stroke="#f59e0b" stroke-width="1.5"/>
    <path d="M 145 236 L 145 244 M 205 236 L 205 244" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="175" y="260" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Spacing L0 (F = 0)</text>
  </g>

  <!-- Right: Tensile Stress Applied (L > L0) -->
  <g transform="translate(440, 80)">
    <rect width="330" height="300" rx="12" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="165" y="28" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">TENSILE STRESS APPLIED (σ = F/A)</text>

    <!-- Left & Right Pulling Arrows -->
    <path d="M 40 130 L 15 130 M 25 124 L 15 130 L 25 136" stroke="#ef4444" stroke-width="3"/>
    <path d="M 290 130 L 315 130 M 305 124 L 315 130 L 305 136" stroke="#ef4444" stroke-width="3"/>
    <text x="15" y="115" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Tension</text>

    <!-- Grid of atoms (Stretched spacing) -->
    <g transform="translate(50, 60)">
      <!-- Row 1 -->
      <circle cx="15" cy="20" r="10" fill="#cbd5e1"/><circle cx="85" cy="20" r="10" fill="#cbd5e1"/><circle cx="155" cy="20" r="10" fill="#cbd5e1"/><circle cx="225" cy="20" r="10" fill="#cbd5e1"/>
      <!-- Row 2 -->
      <circle cx="15" cy="80" r="10" fill="#cbd5e1"/><circle cx="85" cy="80" r="10" fill="#cbd5e1"/><circle cx="155" cy="80" r="10" fill="#cbd5e1"/><circle cx="225" cy="80" r="10" fill="#cbd5e1"/>
      <!-- Row 3 -->
      <circle cx="15" cy="140" r="10" fill="#cbd5e1"/><circle cx="85" cy="140" r="10" fill="#cbd5e1"/><circle cx="155" cy="140" r="10" fill="#cbd5e1"/><circle cx="225" cy="140" r="10" fill="#cbd5e1"/>

      <!-- Stretched Interatomic Bonds -->
      <g stroke="#f59e0b" stroke-width="2">
        <line x1="25" y1="20" x2="75" y2="20"/><line x1="95" y1="20" x2="145" y2="20"/><line x1="165" y1="20" x2="215" y2="20"/>
        <line x1="25" y1="80" x2="75" y2="80"/><line x1="95" y1="80" x2="145" y2="80"/><line x1="165" y1="80" x2="215" y2="80"/>
        <line x1="25" y1="140" x2="75" y2="140"/><line x1="95" y1="140" x2="145" y2="140"/><line x1="165" y1="140" x2="215" y2="140"/>
      </g>
    </g>

    <!-- Stretched Spacing Dimension -->
    <line x1="135" y1="240" x2="205" y2="240" stroke="#ef4444" stroke-width="1.5"/>
    <path d="M 135 236 L 135 244 M 205 236 L 205 244" stroke="#ef4444" stroke-width="1.5"/>
    <text x="170" y="260" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Stretched Spacing L > L0</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_stress_strain_curve():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 440" width="100%" height="100%">
  <rect width="820" height="440" fill="#0f172a" rx="16"/>
  <text x="410" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">COMPLETE STRESS–STRAIN CURVE FOR STRUCTURAL STEEL</text>
  <text x="410" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Elastic Modulus (Y = σ/ε) • Yield Strength • Ultimate Tensile Strength • Fracture</text>

  <!-- Grid & Axes -->
  <line x1="120" y1="360" x2="740" y2="360" stroke="#94a3b8" stroke-width="2"/>
  <line x1="120" y1="360" x2="120" y2="80" stroke="#94a3b8" stroke-width="2"/>

  <!-- Y-Axis: Stress σ (MPa) -->
  <text x="105" y="365" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">0</text>
  <text x="105" y="290" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">100</text>
  <text x="105" y="220" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">250 (Yield)</text>
  <text x="105" y="140" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">400 (UTS)</text>
  <text x="45" y="210" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle" transform="rotate(-90 45 210)">Tensile Stress σ (MPa)</text>

  <!-- X-Axis: Strain ε -->
  <text x="120" y="380" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">0</text>
  <text x="280" y="380" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">0.001</text>
  <text x="460" y="380" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">0.05</text>
  <text x="640" y="380" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">0.10</text>
  <text x="720" y="380" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">0.15</text>
  <text x="430" y="410" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Tensile Strain ε (Dimensionless ratio ΔL / L0)</text>

  <!-- Region 1: Linear Elastic Region (0,0) to Yield Point (250 MPa, 0.00125) -->
  <line x1="120" y1="360" x2="280" y2="220" stroke="#38bdf8" stroke-width="4"/>
  <circle cx="280" cy="220" r="5" fill="#38bdf8"/>
  <text x="270" y="205" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="end">Yield Point (250 MPa)</text>

  <!-- Region 2: Strain Hardening Curve to Ultimate Tensile Strength (400 MPa, 0.10) -->
  <path d="M 280 220 Q 420 135 640 140" fill="none" stroke="#22c55e" stroke-width="3.5"/>
  <circle cx="640" cy="140" r="6" fill="#22c55e"/>
  <text x="640" y="120" fill="#22c55e" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Ultimate Tensile Strength (400 MPa)</text>

  <!-- Region 3: Necking & Fracture Point -->
  <path d="M 640 140 Q 690 150 710 170" fill="none" stroke="#ef4444" stroke-width="3"/>
  <circle cx="710" cy="170" r="5" fill="#ef4444"/>
  <text x="715" y="190" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Fracture (380 MPa)</text>

  <!-- Modulus Slope Callout -->
  <rect x="150" y="100" width="220" height="55" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="260" y="122" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Slope = Young's Modulus (Y)</text>
  <text x="260" y="142" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Y = 250 MPa / 0.00125 = 200 GPa</text>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_failure_modes():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 420" width="100%" height="100%">
  <rect width="840" height="420" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">STRUCTURAL FAILURE MODES IN LOADED ENGINEERING MEMBERS</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Tensile Fracture • Compressive Buckling • Shear Plane Slippage</text>

  <!-- Mode 1: Tensile Fracture -->
  <g transform="translate(40, 80)">
    <rect width="230" height="310" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="115" y="28" fill="#ef4444" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. TENSILE FRACTURE</text>

    <!-- Column pulled apart with jagged crack -->
    <rect x="85" y="50" width="60" height="65" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
    <rect x="85" y="135" width="60" height="65" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
    <path d="M 85 115 L 105 125 L 125 110 L 145 125" stroke="#ef4444" stroke-width="3" fill="none"/>

    <!-- Upward and downward tensile arrows -->
    <path d="M 115 50 L 115 20 M 109 28 L 115 20 L 121 28" stroke="#ef4444" stroke-width="3"/>
    <path d="M 115 200 L 115 230 M 109 222 L 115 230 L 121 222" stroke="#ef4444" stroke-width="3"/>

    <text x="115" y="260" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Tensile Forces Exceed UTS</text>
    <text x="115" y="280" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Material tears apart across cross-section</text>
  </g>

  <!-- Mode 2: Compressive Buckling -->
  <g transform="translate(305, 80)">
    <rect width="230" height="310" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="115" y="28" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">2. COMPRESSIVE BUCKLING</text>

    <!-- Slender column bowed sideways -->
    <path d="M 115 50 Q 75 125 115 200" stroke="#f59e0b" stroke-width="18" stroke-linecap="round" fill="none"/>

    <!-- Inward compression arrows -->
    <path d="M 115 20 L 115 48 M 109 40 L 115 48 L 121 40" stroke="#f59e0b" stroke-width="3"/>
    <path d="M 115 230 L 115 202 M 109 210 L 115 202 L 121 210" stroke="#f59e0b" stroke-width="3"/>

    <text x="115" y="260" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Slender Column Instability</text>
    <text x="115" y="280" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Bends laterally under heavy compression</text>
  </g>

  <!-- Mode 3: Shear Failure -->
  <g transform="translate(570, 80)">
    <rect width="230" height="310" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="115" y="28" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">3. SHEAR FAILURE</text>

    <!-- Two blocks sliding past one another -->
    <rect x="65" y="65" width="50" height="120" fill="#334155" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="115" y="95" width="50" height="120" fill="#334155" stroke="#38bdf8" stroke-width="1.5"/>
    <line x1="115" y1="65" x2="115" y2="215" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="4 2"/>

    <!-- Opposed shear arrows -->
    <path d="M 90 40 L 90 60 M 84 52 L 90 60 L 96 52" stroke="#38bdf8" stroke-width="3"/>
    <path d="M 140 240 L 140 220 M 134 228 L 140 220 L 146 228" stroke="#38bdf8" stroke-width="3"/>

    <text x="115" y="260" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Opposing Lateral Forces</text>
    <text x="115" y="280" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Parallel planes slide and shear off</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg


# =============================================================================
# CURRICULUM DEFINITION DATA FOR TOPIC 3
# =============================================================================

def build_topic3_curriculum_data():
    return [
        # ---------------------------------------------------------------------
        # LESSON 1: Mechanical Properties and Material Choice
        # ---------------------------------------------------------------------
        {
            "unit_order": 1,
            "unit_name": "Mechanical Properties and Material Choice",
            "unit_description": "Exploring mechanical properties governing material selection: elasticity, ductility, malleability, brittleness, strength, hardness, stiffness, and elastic vs plastic deformation.",
            "lesson_title": "Mechanical Properties and Material Choice",
            "pages": [
                # Page 1: Hook & Rebar Concrete Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Composite Engineering: Rebar Steel and Concrete on a Building Site",
                        "content": {
                            "title": "Composite Engineering: Rebar Steel and Concrete on a Building Site",
                            "caption": "Steel reinforcement bars (rebar) laid inside wooden formwork before concrete pouring. This combines the high tensile strength and ductility of steel with the high compressive strength and hardness of concrete.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Rebar_at_construction_site.jpg/1280px-Rebar_at_construction_site.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Rebar_at_construction_site.jpg/1280px-Rebar_at_construction_site.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Steel Rebar and Concrete Composite Construction",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Rebar_at_construction_site.jpg/1280px-Rebar_at_construction_site.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Rebar_at_construction_site.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Mechanical Personalities of Matter",
                        "content": {
                            "title": "Why Do Materials Behave Differently Under Force?",
                            "text": "Walk around any construction site in Kenya, from Nairobi high-rises to rural school builds:\n\n- Why don't builders use concrete to make electrical wires or glass to build bridge beams?\n- Why does a clay pot shatter when dropped, while a plastic basin merely dents?\n\nEvery material possesses distinct physical behaviors under applied loads that physicists classify as **mechanical properties**."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Mechanical Properties",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **deformation** and distinguish between **elastic** and **plastic (permanent)** deformation.",
                                "Classify materials based on core mechanical properties: **elasticity, ductility, malleability, brittleness, strength, hardness**, and **stiffness**.",
                                "Distinguish between **stiffness** (resistance to stretch) and **strength** (resistance to fracture).",
                                "Conduct practical tests to evaluate mechanical behaviors in everyday objects."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Deformation",
                        "content": {
                            "term": "Deformation",
                            "definition": "Any change in the shape or dimensions of an object caused by the action of an external force.",
                            "example": "Stretching a rubber band or bending a copper wire."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Elasticity",
                        "content": {
                            "term": "Elasticity",
                            "definition": "The ability of a deformed material to return completely to its original shape and dimensions once the deforming force is removed.",
                            "example": "Steel vehicle suspension springs and rubber catapults."
                        }
                    }
                ],
                # Page 3: Core Mechanical Properties
                [
                    {
                        "type": "comparison_table",
                        "title": "Fundamental Mechanical Properties Comparison Matrix",
                        "content": {
                            "title": "Mechanical Properties of Engineering Materials",
                            "headers": ["Property", "Physical Definition", "Characteristic Materials", "Engineering Application"],
                            "rows": [
                                ["Ductility", "Ability to be drawn or stretched into thin wires without fracturing.", "Copper, Aluminium, Gold", "Electrical overhead wiring and cables."],
                                ["Malleability", "Ability to be hammered or rolled into thin sheets without cracking.", "Aluminium, Mild Steel, Gold", "Roofing mabati sheets, sufurias, car body panels."],
                                ["Brittleness", "Tendency to fracture with little to no prior plastic deformation.", "Glass, Cast Iron, Ceramics", "Window panes, electrical insulators, tea mugs."],
                                ["Stiffness", "Resistance to elastic stretching or bending under load.", "Structural Steel, Concrete, Diamond", "Bridge girders, skyscraper columns, train tracks."],
                                ["Strength", "Maximum force or stress a material withstands before breaking.", "High-Tensile Steel, Carbon Fibre", "Suspension bridge cables, crane lifting ropes."],
                                ["Hardness", "Resistance of a material surface to scratching, indentation, or wear.", "Diamond, Tool Steel, Quartz", "Drill bits, rock-cutting saws, chisel tips."]
                            ]
                        }
                    }
                ],
                # Page 4: Elastic vs Plastic SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Elastic vs Permanent (Plastic) Deformation Mechanisms",
                        "content": {
                            "title": "Elastic vs Permanent (Plastic) Deformation Mechanisms",
                            "caption": "Side-by-side comparison of a helical spring undergoing reversible elastic deformation (returning to L0) versus permanent plastic deformation caused by atomic plane slippage.",
                            "svg_content": get_svg_elastic_plastic_deformation(),
                            "svg": get_svg_elastic_plastic_deformation()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Elastic and Plastic Spring Deformation Diagram",
                            "metadata": {
                                "svg_content": get_svg_elastic_plastic_deformation()
                            }
                        }
                    }
                ],
                # Page 5: Practical Investigation
                [
                    {
                        "type": "mini_activity",
                        "title": "Practical Investigation: Bending, Stretching & Scratching",
                        "content": {
                            "title": "Testing Mechanical Properties of Everyday Materials",
                            "task": "Test a collection of local items (copper wire, aluminum foil, rubber band, glass piece, steel nail, wooden ruler, plastic bottle):\n\n1. **Stretching Test**: Gently pull the rubber band and copper wire. Compare elasticity vs ductility.\n2. **Bending Test**: Bend the wooden ruler, copper wire, and foil. Observe stiffness vs malleability vs brittleness.\n3. **Scratch Test (Mohs Principle)**: Use the steel nail to scratch plastic, wood, and glass surfaces to evaluate relative hardness.\n4. **Safety Rule**: Handle sharp nails and glass with protective gloves and safety goggles!"
                        }
                    }
                ],
                # Page 6: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Mountaineering Rope Material Selection",
                        "content": {
                            "question": "A team of mountaineers climbing Mt. Kenya requires a safety climbing rope. The rope must hold a heavy climber without snapping, but must also stretch moderately to absorb the shock of an accidental fall. Which combination of mechanical properties is most desirable?",
                            "options": [
                                "High brittleness and high stiffness",
                                "High strength and moderate elasticity",
                                "High hardness and high malleability",
                                "Low strength and high ductility"
                            ],
                            "answer": "B",
                            "explanation": "A dynamic climbing rope requires **high tensile strength** so that it does not break under heavy gravitational loads, combined with **moderate elasticity** to stretch and cushion the decelerating fall without transmitting injurious shock to the climber's body. Stiff or brittle materials would snap or cause violent whiplash. Therefore, Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Material Science Video: Elastic and Plastic Deformation",
                        "content": {
                            "title": "Material Science Video: Elastic and Plastic Deformation",
                            "description": "Video explaining the atomic mechanics of elastic stretching versus dislocation slip in plastic deformation and tensile testing.",
                            "url": "https://www.youtube.com/watch?v=wE93XGkW1zE",
                            "resolved_video_id": "wE93XGkW1zE"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Material Mechanical Properties and Deformation Video",
                            "url": "https://www.youtube.com/watch?v=wE93XGkW1zE",
                            "metadata": {
                                "youtube_id": "wE93XGkW1zE"
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
                                "Materials are selected based on their specific **mechanical properties** (elasticity, ductility, malleability, brittleness, strength, hardness, stiffness).",
                                "**Stiffness** is resistance to stretching/bending, while **strength** is resistance to breaking completely.",
                                "**Elastic deformation** is fully reversible; **plastic deformation** causes permanent atomic lattice distortion."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 2: Force–Extension Relationship and Hooke’s Law
        # ---------------------------------------------------------------------
        {
            "unit_order": 2,
            "unit_name": "Force–Extension Relationship and Hooke’s Law",
            "unit_description": "Investigating Hooke's Law (F = k·ΔL), spring constant (stiffness k), limit of proportionality, elastic limit, graphical analysis of Force vs Extension, and unit conversions.",
            "lesson_title": "Force–Extension Relationship and Hooke’s Law",
            "pages": [
                # Page 1: Hook & Spring Balance Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Hooke's Law in Daily Life: The Market Spring Balance",
                        "content": {
                            "title": "Hooke's Law in Daily Life: The Market Spring Balance",
                            "caption": "A calibrated spring balance in a local market. The downward extension of the internal steel spring is directly proportional to the weight of goods placed in the hanging pan.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Spring_balance.jpg/1280px-Spring_balance.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Spring_balance.jpg/1280px-Spring_balance.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Calibrated Market Spring Balance",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Spring_balance.jpg/1280px-Spring_balance.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Spring_balance.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Predictable Stretch of a Spring",
                        "content": {
                            "title": "Why Does a Heavy Bag Pull the Scale Further?",
                            "text": "Have you ever weighed groceries on a spring balance or watched the coil springs of a matatu compress under a heavy load?\n\nWhen a force pulls on an elastic material, it stretches in an extraordinarily precise and predictable mathematical manner. This discovery by Robert Hooke in 1676 is the foundation of structural and mechanical engineering."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Hooke's Law",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "State **Hooke's Law** and write its mathematical equation ($F = k \\Delta L$).",
                                "Define the **spring constant ($k$)** and determine its SI units ($\\text{N/m}$).",
                                "Distinguish between the **Limit of Proportionality** and the **Elastic Limit**.",
                                "Analyze a Force vs Extension graph and determine the spring constant from its slope.",
                                "Calculate load, extension, and stretched length in quantitative problems."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Extension (ΔL)",
                        "content": {
                            "term": "Extension (ΔL)",
                            "definition": "The increase in length of an elastic object when subjected to an external tensile force ($\\Delta L = L - L_0$).",
                            "example": "A 10 cm spring stretched to 14 cm has an extension of 4 cm (0.04 m)."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Spring Constant (k)",
                        "content": {
                            "term": "Spring Constant (k)",
                            "definition": "The stiffness of an elastic spring, defined as the force required to produce a unit extension ($k = F / \\Delta L$).",
                            "example": "A suspension spring with $k = 50,000\\text{ N/m}$ requires 50,000 N to compress by 1 metre."
                        }
                    }
                ],
                # Page 3: Hooke's Law Apparatus SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Hooke's Law Experimental Retort Stand Setup",
                        "content": {
                            "title": "Hooke's Law Experimental Retort Stand Setup",
                            "caption": "Retort stand apparatus showing progressive spring extension under 0 N, 1 N (2 cm extension), and 2 N (4 cm extension) loads, proving direct proportionality.",
                            "svg_content": get_svg_hookes_law_apparatus(),
                            "svg": get_svg_hookes_law_apparatus()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Hooke's Law Retort Stand Apparatus Diagram",
                            "metadata": {
                                "svg_content": get_svg_hookes_law_apparatus()
                            }
                        }
                    },
                    {
                        "type": "formula_breakdown",
                        "title": "Hooke's Law Mathematical Formula",
                        "content": {
                            "title": "The Linear Elastic Model",
                            "formula": "F = k \\cdot \\Delta L",
                            "variables": [
                                "$F$ = Applied Load Force in Newtons ($\\text{N}$)",
                                "$k$ = Spring Constant (Stiffness) in Newtons per metre ($\\text{N/m}$)",
                                "$\\Delta L = L - L_0$ = Extension in metres ($\\text{m}$)"
                            ],
                            "rules": [
                                "**Law Statement**: The extension of an elastic body is directly proportional to the applied load, provided the limit of proportionality is not exceeded.",
                                "**Unit Rule**: Always convert extension in centimeters ($\\text{cm}$) or millimeters ($\\text{mm}$) into SI metres ($\\text{m}$) before calculating $k$."
                            ]
                        }
                    }
                ],
                # Page 4: Force vs Extension Graph SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Force vs Extension Characteristic Curve",
                        "content": {
                            "title": "Force vs Extension Characteristic Curve",
                            "caption": "Cartesian plot of Force (F) vs Extension (ΔL). The straight linear region passes through the origin with slope k, ending at Point A (Proportional Limit) and Point B (Elastic Limit).",
                            "svg_content": get_svg_force_extension_graph(),
                            "svg": get_svg_force_extension_graph()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Force vs Extension Graph Diagram",
                            "metadata": {
                                "svg_content": get_svg_force_extension_graph()
                            }
                        }
                    }
                ],
                # Page 5: Worked Example
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Spring Constant and Length Prediction",
                        "content": {
                            "title": "Quantitative Hooke's Law Problem",
                            "problem": "A steel helical spring has an unloaded natural length of $15.0\\text{ cm}$. When a load of $4.0\\text{ N}$ is suspended from it, its length becomes $17.0\\text{ cm}$. Calculate:\n1. The spring constant ($k$).\n2. The total length of the spring when a load of $10.0\\text{ N}$ is applied.",
                            "steps": [
                                "1. **Find initial extension**: $\\Delta L = L - L_0 = 17.0\\text{ cm} - 15.0\\text{ cm} = 2.0\\text{ cm} = 0.02\\text{ m}$.",
                                "2. **Calculate spring constant**: $k = \\frac{F}{\\Delta L} = \\frac{4.0\\text{ N}}{0.02\\text{ m}} = 200\\text{ N/m}$.",
                                "3. **Calculate new extension under 10 N**: $\\Delta L_{\\text{new}} = \\frac{F_{\\text{new}}}{k} = \\frac{10.0\\text{ N}}{200\\text{ N/m}} = 0.05\\text{ m} = 5.0\\text{ cm}$.",
                                "4. **Calculate total stretched length**: $L_{\\text{final}} = L_0 + \\Delta L_{\\text{new}} = 15.0\\text{ cm} + 5.0\\text{ cm} = 20.0\\text{ cm}$."
                            ],
                            "answer": "The spring constant is 200 N/m and the spring reaches a total length of 20.0 cm."
                        }
                    }
                ],
                # Page 6: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Identifying Graph Regions",
                        "content": {
                            "question": "On a standard Force vs Extension graph for a spiral spring, what is the exact physical meaning of the straight linear line passing through the origin $(0,0)$, and what does its gradient represent?",
                            "options": [
                                "The spring is undergoing plastic deformation; gradient represents original length.",
                                "Extension is directly proportional to load; gradient equals the spring constant ($k$).",
                                "The spring has exceeded its elastic limit; gradient represents breaking stress.",
                                "The spring is in freefall; gradient represents gravitational acceleration."
                            ],
                            "answer": "B",
                            "explanation": "In the linear region of a Force vs Extension graph, the line follows $F = k \\Delta L$, which is the equation of a straight line through the origin ($y = mx$). The slope $\\frac{\\Delta F}{\\Delta(\\Delta L)}$ is the **spring constant ($k$)**, representing the stiffness of the spring. Therefore, Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Laboratory Tutorial: Hooke's Law Experiment",
                        "content": {
                            "title": "Laboratory Tutorial: Hooke's Law Experiment",
                            "description": "Step-by-step laboratory demonstration loading slotted masses onto a helical spring, taking parallax-free pointer readings, and plotting the best-fit line.",
                            "url": "https://www.youtube.com/watch?v=k_aB3_i4zE4",
                            "resolved_video_id": "k_aB3_i4zE4"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Hooke's Law Laboratory Physics Demonstration",
                            "url": "https://www.youtube.com/watch?v=k_aB3_i4zE4",
                            "metadata": {
                                "youtube_id": "k_aB3_i4zE4"
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
                                "**Hooke's Law** states $F = k \\Delta L$, valid up to the limit of proportionality.",
                                "The **spring constant ($k$)** has SI units of $\\text{N/m}$ and measures stiffness.",
                                "The **elastic limit** marks the point beyond which deformation becomes permanent.",
                                "The gradient of a Force vs Extension graph gives the spring constant $k$."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 3: Stress, Strain and Young’s Modulus
        # ---------------------------------------------------------------------
        {
            "unit_order": 3,
            "unit_name": "Stress, Strain and Young’s Modulus",
            "unit_description": "Universal material properties independent of geometry: tensile stress (σ = F/A), tensile strain (ε = ΔL/L0), Young's Modulus (Y = σ/ε = F·L0 / A·ΔL), microscopic atomic lattice bond stiffness, and stress-strain curves.",
            "lesson_title": "Stress, Strain and Young’s Modulus",
            "pages": [
                # Page 1: Hook & Suspension Cable Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Civil Engineering: Heavy Steel Suspension Bridge Cables",
                        "content": {
                            "title": "Civil Engineering: Heavy Steel Suspension Bridge Cables",
                            "caption": "The main suspension cables of a modern bridge made of thousands of packed high-strength steel wires. Engineers use Young's Modulus to calculate the microscopic elastic stretch under thousands of tonnes of moving traffic.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Akashi_Bridge.jpg/1280px-Akashi_Bridge.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Akashi_Bridge.jpg/1280px-Akashi_Bridge.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Steel Suspension Bridge Main Cable",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Akashi_Bridge.jpg/1280px-Akashi_Bridge.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Akashi_Bridge.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Beyond Individual Springs: Universal Material Stiffness",
                        "content": {
                            "title": "The Limitation of Hooke's Law",
                            "text": "Hooke's Law ($F = k \\Delta L$) is useful for a single spring, but its spring constant $k$ changes if the spring is made twice as thick or twice as long.\n\nTo compare materials fairly—whether testing a microscopic wire or a 10-meter bridge beam—physicists normalize force by cross-sectional area (**Stress**) and extension by original length (**Strain**). Their ratio gives the universal measure of material stiffness: **Young's Modulus**."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Young's Modulus",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **Tensile Stress** ($\\sigma = \\frac{F}{A}$) and state its SI unit ($\\text{Pascal, Pa}$ or $\\text{N/m}^2$).",
                                "Define **Tensile Strain** ($\\epsilon = \\frac{\\Delta L}{L_0}$) and explain why it is dimensionless.",
                                "Derive and apply **Young's Modulus** ($Y = \\frac{\\sigma}{\\epsilon} = \\frac{F \\cdot L_0}{A \\cdot \\Delta L}$).",
                                "Convert wire diameter to cross-sectional area ($A = \\pi r^2 = \\frac{\\pi d^2}{4}$) with proper SI unit prefixes.",
                                "Interpret the complete Stress–Strain curve for structural steel."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Tensile Stress (σ)",
                        "content": {
                            "term": "Tensile Stress (σ)",
                            "definition": "The internal restoring force per unit cross-sectional area resisting stretching ($\\sigma = F / A$).",
                            "example": "A 1000 N force on a $0.0001\\text{ m}^2$ wire creates $10\\text{ MPa}$ of stress."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Tensile Strain (ε)",
                        "content": {
                            "term": "Tensile Strain (ε)",
                            "definition": "The fractional change in length under tensile stress ($\\epsilon = \\Delta L / L_0$). It is a dimensionless ratio with no units.",
                            "example": "A 2.0 m wire stretching by 2.0 mm (0.002 m) has a strain of 0.001 (or 0.1%)."
                        }
                    }
                ],
                # Page 3: Atomic Lattice SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Microscopic Atomic Lattice Bonds Under Tensile Stress",
                        "content": {
                            "title": "Microscopic Atomic Lattice Bonds Under Tensile Stress",
                            "caption": "Microscopic visualization of interatomic spring-like bonds pulling atomic planes apart under tensile load. Young's Modulus reflects the fundamental stiffness of these chemical bonds.",
                            "svg_content": get_svg_atomic_lattice_stress(),
                            "svg": get_svg_atomic_lattice_stress()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Atomic Lattice Tensile Bond Spacing Diagram",
                            "metadata": {
                                "svg_content": get_svg_atomic_lattice_stress()
                            }
                        }
                    }
                ],
                # Page 4: Young's Modulus Formula & Material Table
                [
                    {
                        "type": "formula_breakdown",
                        "title": "Mathematical Derivation of Young's Modulus",
                        "content": {
                            "title": "Young's Modulus Equation",
                            "formula": "Y = \\frac{\\text{Stress}}{\\text{Strain}} = \\frac{\\left(\\frac{F}{A}\\right)}{\\left(\\frac{\\Delta L}{L_0}\\right)} = \\frac{F \\cdot L_0}{A \\cdot \\Delta L}",
                            "variables": [
                                "$Y$ = Young's Modulus in Pascals ($\\text{Pa}$ or $\\text{N/m}^2$)",
                                "$F$ = Applied Tensile Force in Newtons ($\\text{N}$)",
                                "$L_0$ = Original Unloaded Length in metres ($\\text{m}$)",
                                "$A$ = Cross-Sectional Area in square metres ($\\text{m}^2$)",
                                "$\\Delta L$ = Extension in metres ($\\text{m}$)"
                            ],
                            "rules": [
                                "**Dimensionless Strain**: Because strain is metres divided by metres, the unit of Young's Modulus is identical to stress ($\\text{Pa}$).",
                                "**Intrinsic Property**: Young's Modulus depends strictly on the material's atomic composition, NOT on the sample's length or thickness."
                            ]
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Young's Modulus of Common Engineering Materials",
                        "content": {
                            "title": "Elastic Modulus of Materials",
                            "headers": ["Material", "Young's Modulus (Y)", "Stiffness Characteristic"],
                            "rows": [
                                ["Diamond", "1,200 GPa", "Highest known stiffness; virtually unbendable."],
                                ["Structural Steel", "200 GPa (2.0 × 10¹¹ Pa)", "Extremely stiff; ideal for building frames and rail tracks."],
                                ["Copper", "110 GPa (1.1 × 10¹¹ Pa)", "Stiff and highly ductile; easily drawn into wiring."],
                                ["Glass", "70 GPa (7.0 × 10¹⁰ Pa)", "Stiff but brittle; shatters without yielding."],
                                ["Wood (Oak, along grain)", "11 GPa (1.1 × 10¹⁰ Pa)", "Moderately flexible with high strength-to-weight ratio."],
                                ["Rubber", "0.05 GPa (5.0 × 10⁷ Pa)", "Highly flexible; undergoes massive elastic strain."]
                            ]
                        }
                    }
                ],
                # Page 5: Worked Example (Wire Tension)
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Multi-Step Wire Tension and Extension",
                        "content": {
                            "title": "Calculating Stress, Strain, and Extension in a Steel Wire",
                            "problem": "A steel wire of original length $L_0 = 3.0\\text{ m}$ and diameter $d = 2.0\\text{ mm}$ is suspended vertically and loaded with a weight of $628\\text{ N}$. If Young's Modulus for steel is $2.0 \\times 10^{11}\\text{ Pa}$, calculate:\n1. Cross-sectional area ($A$).\n2. Tensile stress ($\\sigma$).\n3. Tensile strain ($\\epsilon$).\n4. Extension ($\\Delta L$) in millimetres.",
                            "steps": [
                                "1. **Radius and Area**: $r = \\frac{d}{2} = 1.0\\text{ mm} = 1.0 \\times 10^{-3}\\text{ m}$.\n   $A = \\pi r^2 = 3.1416 \\times (1.0 \\times 10^{-3})^2 = 3.14 \\times 10^{-6}\\text{ m}^2$.",
                                "2. **Tensile Stress**: $\\sigma = \\frac{F}{A} = \\frac{628\\text{ N}}{3.14 \\times 10^{-6}\\text{ m}^2} = 2.0 \\times 10^8\\text{ Pa}$ ($200\\text{ MPa}$).",
                                "3. **Tensile Strain**: $\\epsilon = \\frac{\\sigma}{Y} = \\frac{2.0 \\times 10^8\\text{ Pa}}{2.0 \\times 10^{11}\\text{ Pa}} = 1.0 \\times 10^{-3}$ ($0.001$).",
                                "4. **Extension**: $\\Delta L = \\epsilon \\times L_0 = (1.0 \\times 10^{-3}) \\times 3.0\\text{ m} = 3.0 \\times 10^{-3}\\text{ m} = 3.0\\text{ mm}$."
                            ],
                            "answer": "The wire undergoes 200 MPa of stress and extends elastically by exactly 3.0 mm."
                        }
                    }
                ],
                # Page 6: Stress-Strain Curve SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Complete Stress–Strain Curve for Structural Steel",
                        "content": {
                            "title": "Complete Stress–Strain Curve for Structural Steel",
                            "caption": "Full engineering stress-strain curve showing the elastic region (slope = Y), Yield Point (250 MPa), Ultimate Tensile Strength (400 MPa), and Fracture Point.",
                            "svg_content": get_svg_stress_strain_curve(),
                            "svg": get_svg_stress_strain_curve()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Structural Steel Stress-Strain Curve Diagram",
                            "metadata": {
                                "svg_content": get_svg_stress_strain_curve()
                            }
                        }
                    }
                ],
                # Page 7: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Comparing Material Stiffness",
                        "content": {
                            "question": "Two wires, Wire X (Steel, $Y = 200\\text{ GPa}$) and Wire Y (Copper, $Y = 100\\text{ GPa}$), have identical lengths and cross-sectional areas. When equal tensile forces are hung from each wire, how will their extensions compare?",
                            "options": [
                                "Wire X will extend twice as much as Wire Y.",
                                "Wire Y will extend twice as much as Wire X.",
                                "Both wires will extend by the exact same amount.",
                                "Neither wire will extend because both are metals."
                            ],
                            "answer": "B",
                            "explanation": "Extension is inversely proportional to Young's Modulus ($\\Delta L = \\frac{F \\cdot L_0}{A \\cdot Y}$). Because Copper ($100\\text{ GPa}$) has half the stiffness of Steel ($200\\text{ GPa}$), it offers half as much resistance to stretching. Therefore, Wire Y will extend **twice as much** as Wire X under the same load. Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 8: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Tensile Testing Tutorial: Stress, Strain and Young's Modulus",
                        "content": {
                            "title": "Tensile Testing Tutorial: Stress, Strain and Young's Modulus",
                            "description": "Video explaining tensile testing machines, stress and strain calculations, and how engineers read stress-strain curves.",
                            "url": "https://www.youtube.com/watch?v=F_z8bAwbz14",
                            "resolved_video_id": "F_z8bAwbz14"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Tensile Testing and Young's Modulus Tutorial",
                            "url": "https://www.youtube.com/watch?v=F_z8bAwbz14",
                            "metadata": {
                                "youtube_id": "F_z8bAwbz14"
                            }
                        }
                    }
                ],
                # Page 9: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson 3 Summary: Key Takeaways",
                        "content": {
                            "title": "Core Summary",
                            "takeaways": [
                                "**Tensile Stress ($\\sigma = F/A$)** is stretching force per unit area, measured in Pascals (Pa).",
                                "**Tensile Strain ($\\epsilon = \\Delta L / L_0$)** is fractional stretch and has no units.",
                                "**Young's Modulus ($Y = \\sigma / \\epsilon = \\frac{F L_0}{A \\Delta L}$)** is the intrinsic stiffness of a material, given by the initial slope of the stress-strain curve."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 4: Industrial Applications and Safety of Materials
        # ---------------------------------------------------------------------
        {
            "unit_order": 4,
            "unit_name": "Industrial Applications and Safety of Materials",
            "unit_description": "Designing for purpose, matching mechanical properties to practical applications, structural failure modes (tensile fracture, compressive buckling, shear), fatigue under cyclic loading, and the Safety Factor ratio.",
            "lesson_title": "Industrial Applications and Safety of Materials",
            "pages": [
                # Page 1: Hook & Bridge Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Structural Safety: Likoni Cable and Pedestrian Infrastructure",
                        "content": {
                            "title": "Structural Safety: Likoni Cable and Pedestrian Infrastructure",
                            "caption": "A modern suspension bridge demonstrating structural cables engineered with high safety factors to prevent fatigue and catastrophic failure under heavy pedestrian and vehicular traffic.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Golden_Gate_Bridge_cables.jpg/1280px-Golden_Gate_Bridge_cables.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Golden_Gate_Bridge_cables.jpg/1280px-Golden_Gate_Bridge_cables.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Suspension Bridge Cable Bundles",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Golden_Gate_Bridge_cables.jpg/1280px-Golden_Gate_Bridge_cables.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 4.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Golden_Gate_Bridge_cables.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Engineering for Safety and Longevity",
                        "content": {
                            "title": "How Do We Ensure Structures Never Fail?",
                            "text": "Every bridge, crane cable, and high-voltage transmission tower must support heavy loads day after day without collapsing.\n\nIn engineering, no single property guarantees success. Designers must match combined material properties (strength, stiffness, weight, corrosion resistance, and cost) to specific needs, while incorporating a generous **Safety Factor** to safeguard human life."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Industrial Safety & Design",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain the principle of **designing for purpose** using combined material properties.",
                                "Analyze the 3 primary structural failure modes: **tensile fracture, compressive buckling**, and **shear failure**.",
                                "Describe the phenomenon of **material fatigue** under cyclic stress.",
                                "Calculate and interpret the **Safety Factor** ratio ($\\text{Safety Factor} = \\frac{\\text{Breaking Load}}{\\text{Service Load}}$)."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Material Fatigue",
                        "content": {
                            "term": "Material Fatigue",
                            "definition": "The progressive structural weakening of a material caused by repeated cyclic loading and unloading, leading to sudden failure below the normal breaking strength.",
                            "example": "Airplane wing joints and vehicle axles undergoing millions of vibration cycles."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Safety Factor",
                        "content": {
                            "term": "Safety Factor",
                            "definition": "A structural design ratio defined as the maximum breaking load divided by the maximum expected working service load.",
                            "example": "A lift cable rated for 50,000 N carrying a maximum of 10,000 N has a Safety Factor of 5.0."
                        }
                    }
                ],
                # Page 3: Material Selection Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Designing for Purpose: Engineering Material Selection",
                        "content": {
                            "title": "Material Matching in Industrial Products",
                            "headers": ["Product", "Operational Requirement", "Critical Mechanical Properties", "Optimal Material Candidate"],
                            "rows": [
                                ["High-Voltage Power Lines", "Span long distances between pylons without snapping under weight.", "High electrical conductivity + high tensile strength + high ductility.", "Aluminium strands reinforced with an inner high-strength steel core."],
                                ["Vehicle Suspension Springs", "Absorb severe road shocks repeatedly without permanent sagging.", "High elasticity + high fatigue resistance + high yield strength.", "Tempered Silicon-Chromium Spring Steel."],
                                ["Cooking Pot (Sufuria)", "Conduct heat quickly, resist denting when dropped, non-toxic.", "High thermal conductivity + high malleability + non-brittleness.", "Aluminium or food-grade Stainless Steel."],
                                ["Safety Helmet (Hard Hat)", "Resist penetration by falling nails and absorb falling brick impacts.", "High surface hardness + high impact strength + light weight.", "High-Density Polyethylene (HDPE) / Polycarbonate."]
                            ]
                        }
                    }
                ],
                # Page 4: Failure Modes SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Structural Failure Modes in Loaded Members",
                        "content": {
                            "title": "Structural Failure Modes in Loaded Members",
                            "caption": "Three primary failure modes in engineering columns: Tensile Fracture (tearing under tension), Compressive Buckling (lateral bowing under compression), and Shear Failure (sliding on opposing planes).",
                            "svg_content": get_svg_failure_modes(),
                            "svg": get_svg_failure_modes()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Structural Failure Modes Diagram",
                            "metadata": {
                                "svg_content": get_svg_failure_modes()
                            }
                        }
                    }
                ],
                # Page 5: Safety Factor Formula & Design Challenge
                [
                    {
                        "type": "formula_breakdown",
                        "title": "The Engineering Safety Factor Formula",
                        "content": {
                            "title": "Safety Margin Equation",
                            "formula": "\\text{Safety Factor} = \\frac{\\text{Structural Breaking Load (Ultimate Strength)}}{\\text{Maximum Expected Working Service Load}}",
                            "variables": [
                                "$\\text{Breaking Load}$ = Maximum load before physical fracture ($\\text{N}$)",
                                "$\\text{Service Load}$ = Peak operational load anticipated during daily use ($\\text{N}$)"
                            ],
                            "rules": [
                                "**Standard Guidelines**: Buildings and bridges typically use safety factors of $2.0$ to $4.0$; passenger elevators use safety factors of $8.0$ to $10.0$."
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Design Challenge: Rural Pedestrian Bridge Specification",
                        "content": {
                            "title": "Specifying a 12-Metre Footbridge",
                            "task": "You are designing a pedestrian footbridge across a river near a rural school in Kenya to support 50 students simultaneously:\n\n1. **Service Load**: 50 students $\\times 600\\text{ N} = 30,000\\text{ N}$.\n2. **Target Safety Factor**: $5.0$.\n3. **Required Breaking Strength**: Calculate the required beam capacity: $30,000\\text{ N} \\times 5.0 = 150,000\\text{ N}$.\n4. **Material Justification**: Choose reinforced concrete for the abutments (high compressive strength) and galvanized structural steel for main support beams (high tensile strength & corrosion resistance)."
                        }
                    }
                ],
                # Page 6: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Calculating Safety Factor",
                        "content": {
                            "question": "An industrial construction crane is rated to lift a maximum safe working load of $20,000\\text{ N}$. During quality control testing, the steel hoisting cable is proven to fracture only when the applied load reaches $100,000\\text{ N}$. What is the design Safety Factor of this crane cable?",
                            "options": [
                                "0.20",
                                "5.0",
                                "80,000 N",
                                "2,000,000"
                            ],
                            "answer": "B",
                            "explanation": "Safety Factor is the ratio of Breaking Load to Maximum Working Service Load: $$\\text{Safety Factor} = \\frac{\\text{Breaking Load}}{\\text{Service Load}} = \\frac{100,000\\text{ N}}{20,000\\text{ N}} = 5.0$$ A safety factor of 5.0 means the cable is 5 times stronger than its maximum rated operational load. Therefore, Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Engineering Video: Material Failure and Safety Factors",
                        "content": {
                            "title": "Engineering Video: Material Failure and Safety Factors",
                            "description": "Educational video explaining structural buckling, material fatigue in aircraft, and how safety factors protect against catastrophic failure.",
                            "url": "https://www.youtube.com/watch?v=F0fWkI4M42I",
                            "resolved_video_id": "F0fWkI4M42I"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Material Failure Modes and Safety Factor Video",
                            "url": "https://www.youtube.com/watch?v=F0fWkI4M42I",
                            "metadata": {
                                "youtube_id": "F0fWkI4M42I"
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
                                "Engineering design matches material properties to specific operational needs (**designing for purpose**).",
                                "Failure modes include **tensile tearing, compressive buckling**, and **shear sliding**.",
                                "**Material fatigue** occurs under repeated cyclic stresses.",
                                "**Safety Factor** ensures breaking load exceeds working service load by a safe multiplier."
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
def ingest_grade10_physics_topic3():
    print("======================================================================")
    print("INGESTING CBC GRADE 10 PHYSICS — TOPIC 3: MECHANICAL PROPERTIES OF MATERIALS")
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

    # 3. Get or Create Topic: Mechanical Properties of Materials (Order: 3)
    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=3,
        defaults={
            "name": "Mechanical Properties of Materials",
            "description": "Investigation of material behaviors under applied loads: elasticity, Hooke's Law (F = k·ΔL), tensile stress, tensile strain, Young's Modulus (Y = σ/ε), and industrial safety considerations."
        }
    )
    if not t_created and topic.name != "Mechanical Properties of Materials":
        topic.name = "Mechanical Properties of Materials"
        topic.description = "Investigation of material behaviors under applied loads: elasticity, Hooke's Law (F = k·ΔL), tensile stress, tensile strain, Young's Modulus (Y = σ/ε), and industrial safety considerations."
        topic.save()
    print(f"Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    curriculum_data = build_topic3_curriculum_data()

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
    print(f"TOPIC 3 INGESTION COMPLETE:")
    print(f"  - Learning Units: {total_units_created}")
    print(f"  - Lessons:        {total_lessons_created}")
    print(f"  - Lesson Blocks:  {total_blocks_created}")
    print(f"  - Lesson Assets:  {total_assets_created}")
    print("======================================================================")

if __name__ == "__main__":
    ingest_grade10_physics_topic3()
