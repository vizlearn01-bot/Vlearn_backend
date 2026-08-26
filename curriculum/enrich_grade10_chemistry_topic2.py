"""
VLearn CBC Grade 10 Chemistry — Topic 2: The Atom
Visual Enrichment Engine (Vector SVGs, Verified Wikimedia Hooks & YouTube Integration)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Chemistry (ID: 5)
Topic: The Atom (Topic Order: 2)
"""

import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Topic, Lesson, LessonBlock, LessonAsset
)

def sanitize_svg(svg: str) -> str:
    """Ensures SVG is clean, responsive, and stripped of unneeded XML/DOCTYPE headers."""
    svg = re.sub(r'<\?xml.*?\?>', '', svg)
    svg = re.sub(r'<!DOCTYPE.*?>', '', svg)
    return svg.strip()

# =============================================================================
# 5 CUSTOM RESPONSIVE VECTOR SVGS FOR TOPIC 2: THE ATOM
# =============================================================================

# SVG 1: Rutherford Gold Foil Experiment & Scattering (Lesson 1, Page 3)
SVG_RUTHERFORD_EXPERIMENT = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="10" y="10" width="780" height="430" rx="14" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">Rutherford's Gold Foil Experiment (1911) &amp; Alpha Particle Scattering</text>

  <!-- Left Box: Experimental Apparatus -->
  <g transform="translate(25, 60)">
    <rect x="0" y="0" width="365" height="360" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="365" height="32" rx="10" fill="#0284c7"/>
    <text x="182" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">A. LABORATORY APPARATUS SETUP</text>

    <!-- Radioactive source (Lead Box) -->
    <rect x="20" y="140" width="45" height="45" rx="6" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
    <circle cx="42" cy="162" r="8" fill="#f59e0b"/>
    <text x="42" y="202" font-size="9" fill="#cbd5e1" text-anchor="middle">Alpha Source (Ra)</text>

    <!-- Alpha Beam -->
    <line x1="65" y1="162" x2="170" y2="162" stroke="#f59e0b" stroke-width="3"/>

    <!-- Gold Foil -->
    <rect x="170" y="90" width="8" height="150" fill="#fbbf24" stroke="#d97706" stroke-width="1"/>
    <text x="174" y="80" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">Gold Foil</text>

    <!-- Circular Fluorescent Screen -->
    <path d="M 140,70 A 110,110 0 1,1 140,255" fill="none" stroke="#34d399" stroke-width="4" stroke-linecap="round"/>
    <text x="295" y="235" font-size="9" font-weight="bold" fill="#34d399" text-anchor="middle">ZnS Screen (Detector)</text>

    <!-- Deflected rays -->
    <!-- Straight through (99.9%) -->
    <line x1="178" y1="162" x2="280" y2="162" stroke="#f59e0b" stroke-width="3"/>
    <circle cx="280" cy="162" r="4" fill="#34d399"/>
    <text x="285" y="152" font-size="9" fill="#38bdf8">Undeflected (99.9%)</text>

    <!-- Deflected angle -->
    <line x1="178" y1="162" x2="250" y2="95" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3,3"/>
    <circle cx="250" cy="95" r="4" fill="#34d399"/>
    <text x="255" y="88" font-size="9" fill="#f59e0b">Deflected</text>

    <!-- Back-scattered -->
    <line x1="178" y1="162" x2="90" y2="105" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,3"/>
    <circle cx="90" cy="105" r="4" fill="#ef4444"/>
    <text x="75" y="95" font-size="9" font-weight="bold" fill="#ef4444">Bounced back!</text>

    <!-- Legend box -->
    <rect x="15" y="270" width="335" height="75" rx="6" fill="#1e293b"/>
    <text x="25" y="290" font-size="9.5" fill="#cbd5e1">• <tspan fill="#38bdf8" font-weight="bold">Most particles</tspan>: Pass through empty space</text>
    <text x="25" y="310" font-size="9.5" fill="#cbd5e1">• <tspan fill="#f59e0b" font-weight="bold">Close near misses</tspan>: Repelled by positive charge</text>
    <text x="25" y="330" font-size="9.5" fill="#cbd5e1">• <tspan fill="#ef4444" font-weight="bold">Direct collisions (1 in 8,000)</tspan>: Hit dense nucleus</text>
  </g>

  <!-- Right Box: Submicroscopic Atomic Interaction -->
  <g transform="translate(410, 60)">
    <rect x="0" y="0" width="365" height="360" rx="10" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect x="0" y="0" width="365" height="32" rx="10" fill="#059669"/>
    <text x="182" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">B. SUBMICROSCOPIC NUCLEAR COLLISION</text>

    <!-- Gold atom lattice -->
    <!-- Atom 1 Top -->
    <circle cx="182" cy="115" r="65" fill="#1e293b" stroke="#64748b" stroke-width="1" stroke-dasharray="3,3"/>
    <circle cx="182" cy="115" r="9" fill="#ef4444" stroke="#f87171" stroke-width="1"/>
    <text x="182" y="119" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">+</text>

    <!-- Atom 2 Center Target -->
    <circle cx="182" cy="225" r="65" fill="#1e293b" stroke="#64748b" stroke-width="1" stroke-dasharray="3,3"/>
    <circle cx="182" cy="225" r="11" fill="#ef4444" stroke="#f87171" stroke-width="1.5"/>
    <text x="182" y="229" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">+</text>
    <text x="182" y="250" font-size="9" font-weight="bold" fill="#f87171" text-anchor="middle">Dense Nucleus</text>

    <!-- Alpha particle trajectories -->
    <!-- Ray 1: Far away (Straight) -->
    <path d="M 20,75 L 340,75" fill="none" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="330" cy="75" r="3" fill="#f59e0b"/>

    <!-- Ray 2: Near miss (Deflected) -->
    <path d="M 20,185 Q 165,190 280,130" fill="none" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="280" cy="130" r="3" fill="#38bdf8"/>

    <!-- Ray 3: Direct head-on hit (Rebound) -->
    <path d="M 20,225 L 168,225 M 168,225 L 45,295" fill="none" stroke="#ef4444" stroke-width="2.5"/>
    <circle cx="45" cy="295" r="3" fill="#ef4444"/>
    <text x="65" y="325" font-size="10" font-weight="bold" fill="#ef4444">Electrostatic Rebound</text>

    <!-- Summary Box -->
    <rect x="15" y="305" width="335" height="42" rx="6" fill="#1e293b"/>
    <text x="182" y="322" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">Deduction: Atom is 99.999% Empty Space</text>
    <text x="182" y="338" font-size="9" fill="#94a3b8" text-anchor="middle">Tiny central nucleus carries +79 charge in Gold</text>
  </g>
</svg>
""")

# SVG 2: Nuclide Notation & Carbon-12 Structure (Lesson 2, Page 4)
SVG_NUCLIDE_CARBON12 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="10" y="10" width="780" height="430" rx="14" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">Nuclide Notation &amp; Subatomic Architecture of Carbon-12</text>

  <!-- Left: Nuclide Notation Anatomy -->
  <g transform="translate(30, 65)">
    <rect x="0" y="0" width="330" height="355" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="330" height="32" rx="10" fill="#0284c7"/>
    <text x="165" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">NUCLIDE NOTATION FORMULA</text>

    <!-- Large Symbol Display -->
    <rect x="40" y="55" width="250" height="135" rx="10" fill="#1e293b" stroke="#334155"/>
    
    <!-- Mass Number A -->
    <text x="85" y="110" font-size="36" font-weight="bold" fill="#f59e0b">12</text>
    <text x="75" y="130" font-size="10" fill="#fbbf24">Mass Number (A)</text>
    <text x="75" y="145" font-size="9" fill="#94a3b8">Protons + Neutrons</text>

    <!-- Chemical Symbol X -->
    <text x="175" y="140" font-size="64" font-weight="bold" fill="#ffffff">C</text>

    <!-- Atomic Number Z -->
    <text x="95" y="175" font-size="32" font-weight="bold" fill="#38bdf8">6</text>
    <text x="75" y="195" font-size="10" fill="#38bdf8">Atomic Number (Z)</text>
    <text x="75" y="210" font-size="9" fill="#94a3b8">Protons = Electrons</text>

    <!-- Subatomic Particle Equations -->
    <rect x="15" y="225" width="300" height="115" rx="8" fill="#1e293b"/>
    <text x="25" y="248" font-size="11" font-weight="bold" fill="#34d399">Subatomic Calculations for ¹²₆C:</text>
    <text x="25" y="270" font-size="10.5" fill="#cbd5e1">• <tspan fill="#38bdf8" font-weight="bold">Protons (p⁺)</tspan> = Z = 6</text>
    <text x="25" y="292" font-size="10.5" fill="#cbd5e1">• <tspan fill="#38bdf8" font-weight="bold">Electrons (e⁻)</tspan> = Z = 6 (neutral atom)</text>
    <text x="25" y="314" font-size="10.5" fill="#cbd5e1">• <tspan fill="#f59e0b" font-weight="bold">Neutrons (n⁰)</tspan> = A - Z = 12 - 6 = 6</text>
  </g>

  <!-- Right: 2D/3D Carbon-12 Atom Schematic -->
  <g transform="translate(390, 65)">
    <rect x="0" y="0" width="380" height="355" rx="10" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect x="0" y="0" width="380" height="32" rx="10" fill="#059669"/>
    <text x="190" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">CARBON-12 PARTICLE STRUCTURE</text>

    <!-- Atom Drawing -->
    <!-- Shell 2 (Outer) -->
    <circle cx="190" cy="180" r="105" fill="none" stroke="#475569" stroke-width="1.5" stroke-dasharray="4,4"/>
    <text x="190" y="70" font-size="9" fill="#94a3b8" text-anchor="middle">Outer Energy Level (n=2, 4 valence e⁻)</text>

    <!-- Shell 1 (Inner) -->
    <circle cx="190" cy="180" r="60" fill="none" stroke="#475569" stroke-width="1.5" stroke-dasharray="4,4"/>
    <text x="190" y="115" font-size="9" fill="#94a3b8" text-anchor="middle">Inner Level (n=1, 2 e⁻)</text>

    <!-- Nucleus Center -->
    <circle cx="190" cy="180" r="28" fill="#1e293b" stroke="#f87171" stroke-width="2"/>
    <!-- Protons & Neutrons inside -->
    <circle cx="182" cy="174" r="6" fill="#ef4444"/>
    <circle cx="196" cy="172" r="6" fill="#3b82f6"/>
    <circle cx="180" cy="186" r="6" fill="#3b82f6"/>
    <circle cx="194" cy="188" r="6" fill="#ef4444"/>
    <text x="190" y="183" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">6p 6n</text>

    <!-- Electrons in Shell 1 (2 electrons) -->
    <circle cx="190" cy="120" r="6" fill="#facc15"/>
    <text x="190" y="123" font-size="8" font-weight="bold" fill="#000000" text-anchor="middle">-</text>
    <circle cx="190" cy="240" r="6" fill="#facc15"/>
    <text x="190" y="243" font-size="8" font-weight="bold" fill="#000000" text-anchor="middle">-</text>

    <!-- Electrons in Shell 2 (4 electrons) -->
    <circle cx="85" cy="180" r="6" fill="#facc15"/>
    <text x="85" y="183" font-size="8" font-weight="bold" fill="#000000" text-anchor="middle">-</text>
    <circle cx="295" cy="180" r="6" fill="#facc15"/>
    <text x="295" y="183" font-size="8" font-weight="bold" fill="#000000" text-anchor="middle">-</text>
    <circle cx="190" cy="75" r="6" fill="#facc15"/>
    <text x="190" y="78" font-size="8" font-weight="bold" fill="#000000" text-anchor="middle">-</text>
    <circle cx="190" cy="285" r="6" fill="#facc15"/>
    <text x="190" y="288" font-size="8" font-weight="bold" fill="#000000" text-anchor="middle">-</text>

    <!-- Legend below -->
    <rect x="20" y="305" width="340" height="38" rx="6" fill="#1e293b"/>
    <circle cx="45" cy="324" r="5" fill="#ef4444"/>
    <text x="55" y="328" font-size="9" fill="#cbd5e1">Proton (+1)</text>
    <circle cx="140" cy="324" r="5" fill="#3b82f6"/>
    <text x="150" y="328" font-size="9" fill="#cbd5e1">Neutron (0)</text>
    <circle cx="235" cy="324" r="5" fill="#facc15"/>
    <text x="245" y="328" font-size="9" fill="#cbd5e1">Electron (-1)</text>
  </g>
</svg>
""")

# SVG 3: Carbon Isotopes Comparison (Lesson 3, Page 2)
SVG_CARBON_ISOTOPES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="10" y="10" width="780" height="430" rx="14" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">Isotopes of Carbon: Same Protons, Different Neutrons</text>

  <!-- Isotope 1: Carbon-12 -->
  <g transform="translate(25, 65)">
    <rect x="0" y="0" width="235" height="355" rx="10" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
    <rect x="0" y="0" width="235" height="32" rx="10" fill="#059669"/>
    <text x="117" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">CARBON-12 (¹²₆C)</text>

    <!-- Nucleus -->
    <circle cx="117" cy="115" r="45" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="117" y="110" font-size="14" font-weight="bold" fill="#ef4444" text-anchor="middle">6 Protons</text>
    <text x="117" y="130" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">6 Neutrons</text>

    <!-- Data -->
    <rect x="12" y="175" width="211" height="165" rx="8" fill="#1e293b"/>
    <text x="25" y="200" font-size="11" font-weight="bold" fill="#34d399">Properties:</text>
    <text x="25" y="222" font-size="10.5" fill="#cbd5e1">• Mass Number: <tspan fill="#ffffff" font-weight="bold">12</tspan></text>
    <text x="25" y="244" font-size="10.5" fill="#cbd5e1">• Abundance: <tspan fill="#34d399" font-weight="bold">98.9%</tspan></text>
    <text x="25" y="266" font-size="10.5" fill="#cbd5e1">• Stability: <tspan fill="#34d399">Stable</tspan></text>
    <text x="25" y="288" font-size="10.5" fill="#cbd5e1">• Valence e⁻: <tspan fill="#ffffff">4</tspan></text>
    <text x="25" y="315" font-size="9" fill="#94a3b8">Standard for RAM calibration</text>
  </g>

  <!-- Isotope 2: Carbon-13 -->
  <g transform="translate(282, 65)">
    <rect x="0" y="0" width="235" height="355" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="235" height="32" rx="10" fill="#0284c7"/>
    <text x="117" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">CARBON-13 (¹³₆C)</text>

    <!-- Nucleus -->
    <circle cx="117" cy="115" r="45" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="117" y="110" font-size="14" font-weight="bold" fill="#ef4444" text-anchor="middle">6 Protons</text>
    <text x="117" y="130" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">7 Neutrons</text>

    <!-- Data -->
    <rect x="12" y="175" width="211" height="165" rx="8" fill="#1e293b"/>
    <text x="25" y="200" font-size="11" font-weight="bold" fill="#38bdf8">Properties:</text>
    <text x="25" y="222" font-size="10.5" fill="#cbd5e1">• Mass Number: <tspan fill="#ffffff" font-weight="bold">13</tspan></text>
    <text x="25" y="244" font-size="10.5" fill="#cbd5e1">• Abundance: <tspan fill="#38bdf8" font-weight="bold">1.1%</tspan></text>
    <text x="25" y="266" font-size="10.5" fill="#cbd5e1">• Stability: <tspan fill="#34d399">Stable</tspan></text>
    <text x="25" y="288" font-size="10.5" fill="#cbd5e1">• Valence e⁻: <tspan fill="#ffffff">4</tspan></text>
    <text x="25" y="315" font-size="9" fill="#94a3b8">Used in NMR spectroscopy</text>
  </g>

  <!-- Isotope 3: Carbon-14 -->
  <g transform="translate(540, 65)">
    <rect x="0" y="0" width="235" height="355" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect x="0" y="0" width="235" height="32" rx="10" fill="#b45309"/>
    <text x="117" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">CARBON-14 (¹⁴₆C)</text>

    <!-- Nucleus -->
    <circle cx="117" cy="115" r="45" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="117" y="110" font-size="14" font-weight="bold" fill="#ef4444" text-anchor="middle">6 Protons</text>
    <text x="117" y="130" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">8 Neutrons</text>

    <!-- Data -->
    <rect x="12" y="175" width="211" height="165" rx="8" fill="#1e293b"/>
    <text x="25" y="200" font-size="11" font-weight="bold" fill="#f59e0b">Properties:</text>
    <text x="25" y="222" font-size="10.5" fill="#cbd5e1">• Mass Number: <tspan fill="#ffffff" font-weight="bold">14</tspan></text>
    <text x="25" y="244" font-size="10.5" fill="#cbd5e1">• Abundance: <tspan fill="#f59e0b" font-weight="bold">&lt; 0.0001% (Trace)</tspan></text>
    <text x="25" y="266" font-size="10.5" fill="#cbd5e1">• Stability: <tspan fill="#ef4444">Radioactive (β decay)</tspan></text>
    <text x="25" y="288" font-size="10.5" fill="#cbd5e1">• Valence e⁻: <tspan fill="#ffffff">4</tspan></text>
    <text x="25" y="315" font-size="9" fill="#94a3b8">Used in radiocarbon dating fossils</text>
  </g>
</svg>
""")

# SVG 4: 3D Geometries of s and p Orbitals (Lesson 4, Page 2)
SVG_ORBITAL_SHAPES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="10" y="10" width="780" height="430" rx="14" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">3D Shapes and Spatial Orientations of s and p Atomic Orbitals</text>

  <!-- Left: s Orbital (Spherical) -->
  <g transform="translate(30, 65)">
    <rect x="0" y="0" width="220" height="355" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="32" rx="10" fill="#0284c7"/>
    <text x="110" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">s ORBITAL (SPHERICAL)</text>

    <!-- Axes -->
    <line x1="110" y1="60" x2="110" y2="220" stroke="#475569" stroke-width="1.5"/>
    <text x="110" y="55" font-size="10" fill="#94a3b8" text-anchor="middle">z</text>
    <line x1="30" y1="140" x2="190" y2="140" stroke="#475569" stroke-width="1.5"/>
    <text x="198" y="144" font-size="10" fill="#94a3b8">x</text>
    <line x1="60" y1="190" x2="160" y2="90" stroke="#475569" stroke-width="1.5"/>
    <text x="165" y="85" font-size="10" fill="#94a3b8">y</text>

    <!-- Spherical circle -->
    <circle cx="110" cy="140" r="48" fill="#38bdf8" opacity="0.35" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="110" cy="140" r="4" fill="#ffffff"/>

    <!-- Properties -->
    <rect x="10" y="235" width="200" height="105" rx="6" fill="#1e293b"/>
    <text x="20" y="258" font-size="10.5" font-weight="bold" fill="#38bdf8">• Shape: Spherical</text>
    <text x="20" y="278" font-size="10" fill="#cbd5e1">• 1 orbital per energy level</text>
    <text x="20" y="298" font-size="10" fill="#cbd5e1">• Max capacity: <tspan fill="#34d399" font-weight="bold">2 electrons</tspan></text>
    <text x="20" y="318" font-size="10" fill="#cbd5e1">• Non-directional symmetry</text>
  </g>

  <!-- Right: p Orbitals (px, py, pz) -->
  <g transform="translate(265, 65)">
    <rect x="0" y="0" width="505" height="355" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <rect x="0" y="0" width="505" height="32" rx="10" fill="#7e22ce"/>
    <text x="252" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">p SUBLEVEL ORBITALS (DUMBBELL-SHAPED, MAX 6 e⁻)</text>

    <!-- px -->
    <g transform="translate(20, 50)">
      <line x1="70" y1="20" x2="70" y2="160" stroke="#475569" stroke-width="1"/>
      <line x1="10" y1="90" x2="130" y2="90" stroke="#475569" stroke-width="1"/>
      <!-- Horizontal Dumbbell -->
      <path d="M 70,90 C 70,70 20,70 20,90 C 20,110 70,110 70,90 Z" fill="#c084fc" opacity="0.4" stroke="#c084fc" stroke-width="1.5"/>
      <path d="M 70,90 C 70,70 120,70 120,90 C 120,110 70,110 70,90 Z" fill="#c084fc" opacity="0.4" stroke="#c084fc" stroke-width="1.5"/>
      <circle cx="70" cy="90" r="3" fill="#ffffff"/>
      <text x="70" y="180" font-size="11" font-weight="bold" fill="#c084fc" text-anchor="middle">px orbital</text>
    </g>

    <!-- py -->
    <g transform="translate(180, 50)">
      <line x1="70" y1="20" x2="70" y2="160" stroke="#475569" stroke-width="1"/>
      <line x1="10" y1="90" x2="130" y2="90" stroke="#475569" stroke-width="1"/>
      <line x1="25" y1="135" x2="115" y2="45" stroke="#475569" stroke-width="1"/>
      <!-- Diagonal Dumbbell -->
      <path d="M 70,90 C 55,75 25,105 40,120 C 55,135 85,105 70,90 Z" fill="#c084fc" opacity="0.4" stroke="#c084fc" stroke-width="1.5"/>
      <path d="M 70,90 C 85,105 115,75 100,60 C 85,45 55,75 70,90 Z" fill="#c084fc" opacity="0.4" stroke="#c084fc" stroke-width="1.5"/>
      <circle cx="70" cy="90" r="3" fill="#ffffff"/>
      <text x="70" y="180" font-size="11" font-weight="bold" fill="#c084fc" text-anchor="middle">py orbital</text>
    </g>

    <!-- pz -->
    <g transform="translate(340, 50)">
      <line x1="70" y1="20" x2="70" y2="160" stroke="#475569" stroke-width="1"/>
      <line x1="10" y1="90" x2="130" y2="90" stroke="#475569" stroke-width="1"/>
      <!-- Vertical Dumbbell -->
      <path d="M 70,90 C 50,90 50,40 70,40 C 90,40 90,90 70,90 Z" fill="#c084fc" opacity="0.4" stroke="#c084fc" stroke-width="1.5"/>
      <path d="M 70,90 C 50,90 50,140 70,140 C 90,140 90,90 70,90 Z" fill="#c084fc" opacity="0.4" stroke="#c084fc" stroke-width="1.5"/>
      <circle cx="70" cy="90" r="3" fill="#ffffff"/>
      <text x="70" y="180" font-size="11" font-weight="bold" fill="#c084fc" text-anchor="middle">pz orbital</text>
    </g>

    <!-- Summary Box -->
    <rect x="20" y="240" width="465" height="100" rx="8" fill="#1e293b"/>
    <text x="35" y="265" font-size="11" font-weight="bold" fill="#c084fc">Key Quantum Rules for p Orbitals:</text>
    <text x="35" y="288" font-size="10" fill="#cbd5e1">• Three degenerate orbitals: px, py, pz (oriented at 90° angles)</text>
    <text x="35" y="308" font-size="10" fill="#cbd5e1">• Each holds 2 electrons with opposite spins (↑↓), total capacity = <tspan fill="#34d399" font-weight="bold">6 electrons</tspan></text>
    <text x="35" y="328" font-size="10" fill="#cbd5e1">• Electrons fill singly first according to <tspan fill="#f59e0b">Hund's Rule</tspan> before pairing</text>
  </g>
</svg>
""")

# SVG 5: Integrated Sodium (Na) Triplet Representation Profile (Lesson 5, Page 2)
SVG_SODIUM_PROFILE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="10" y="10" width="780" height="430" rx="14" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">Comprehensive Chemical Profile: Sodium (Na) Triplet Representation</text>

  <!-- Level 1: Macroscopic -->
  <g transform="translate(25, 65)">
    <rect x="0" y="0" width="235" height="355" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect x="0" y="0" width="235" height="32" rx="10" fill="#b45309"/>
    <text x="117" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. MACROSCOPIC</text>

    <!-- Metal Drawing -->
    <rect x="35" y="55" width="165" height="90" rx="8" fill="#94a3b8" stroke="#cbd5e1" stroke-width="2"/>
    <line x1="35" y1="100" x2="200" y2="100" stroke="#f8fafc" stroke-width="3"/>
    <text x="117" y="90" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Soft Silvery Metal</text>
    <text x="117" y="130" font-size="9" fill="#1e293b" text-anchor="middle">Easily cut with butter knife</text>

    <!-- Bullets -->
    <rect x="12" y="160" width="211" height="180" rx="6" fill="#1e293b"/>
    <text x="22" y="185" font-size="10.5" font-weight="bold" fill="#fbbf24">• Physical State: Solid (s)</text>
    <text x="22" y="208" font-size="10" fill="#cbd5e1">• Low melting point (97.8 °C)</text>
    <text x="22" y="228" font-size="10" fill="#cbd5e1">• Low density (floats on water)</text>
    <text x="22" y="248" font-size="10" fill="#cbd5e1">• High electrical conductivity</text>
    <text x="22" y="268" font-size="10" fill="#f87171">• Reacts violently with water</text>
    <text x="22" y="295" font-size="9" fill="#94a3b8">Stored under paraffin oil</text>
  </g>

  <!-- Level 2: Submicroscopic -->
  <g transform="translate(282, 65)">
    <rect x="0" y="0" width="235" height="355" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="235" height="32" rx="10" fill="#0284c7"/>
    <text x="117" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. SUBMICROSCOPIC</text>

    <!-- Atom Shells Drawing -->
    <circle cx="117" cy="115" r="55" fill="none" stroke="#475569" stroke-width="1.5" stroke-dasharray="3,3"/>
    <circle cx="117" cy="115" r="38" fill="none" stroke="#475569" stroke-width="1.5" stroke-dasharray="3,3"/>
    <circle cx="117" cy="115" r="22" fill="none" stroke="#475569" stroke-width="1.5" stroke-dasharray="3,3"/>
    <!-- Nucleus -->
    <circle cx="117" cy="115" r="14" fill="#ef4444"/>
    <text x="117" y="118" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">11p 12n</text>

    <!-- Valence electron on outer ring -->
    <circle cx="117" cy="60" r="5" fill="#facc15" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="145" y="65" font-size="9" font-weight="bold" fill="#facc15">1 Valence e⁻</text>

    <!-- Data -->
    <rect x="12" y="180" width="211" height="160" rx="6" fill="#1e293b"/>
    <text x="22" y="205" font-size="10.5" font-weight="bold" fill="#38bdf8">• Protons (p⁺) = 11</text>
    <text x="22" y="225" font-size="10.5" fill="#cbd5e1">• Neutrons (n⁰) = 12</text>
    <text x="22" y="245" font-size="10.5" fill="#cbd5e1">• Electrons (e⁻) = 11</text>
    <text x="22" y="265" font-size="10.5" fill="#34d399">• Outer Shell: 3s¹</text>
    <text x="22" y="290" font-size="9" fill="#cbd5e1">1 loosely held electron easily lost to form Na⁺ cation</text>
  </g>

  <!-- Level 3: Symbolic -->
  <g transform="translate(540, 65)">
    <rect x="0" y="0" width="235" height="355" rx="10" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
    <rect x="0" y="0" width="235" height="32" rx="10" fill="#059669"/>
    <text x="117" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. SYMBOLIC</text>

    <!-- Nuclide Display -->
    <rect x="25" y="45" width="185" height="65" rx="8" fill="#1e293b" stroke="#334155"/>
    <text x="65" y="75" font-size="20" font-weight="bold" fill="#f59e0b">23</text>
    <text x="65" y="98" font-size="20" font-weight="bold" fill="#38bdf8">11</text>
    <text x="125" y="92" font-size="44" font-weight="bold" fill="#ffffff">Na</text>

    <!-- Configurations -->
    <rect x="12" y="120" width="211" height="220" rx="6" fill="#1e293b"/>
    <text x="22" y="145" font-size="11" font-weight="bold" fill="#34d399">s and p Notation:</text>
    <text x="22" y="170" font-size="12" font-weight="bold" fill="#ffffff">1s² 2s² 2p⁶ 3s¹</text>

    <text x="22" y="205" font-size="11" font-weight="bold" fill="#38bdf8">Ionization Reaction:</text>
    <text x="22" y="228" font-size="11" font-weight="bold" fill="#38bdf8">Na → Na⁺ + e⁻</text>
    <text x="22" y="248" font-size="10" fill="#94a3b8">Na⁺ config: 1s² 2s² 2p⁶ [Ne]</text>

    <text x="22" y="280" font-size="11" font-weight="bold" fill="#f59e0b">Water Reaction Equation:</text>
    <text x="22" y="302" font-size="9" fill="#cbd5e1">2Na(s) + 2H₂O(l) →</text>
    <text x="22" y="320" font-size="9" fill="#cbd5e1">2NaOH(aq) + H₂(g)</text>
  </g>
</svg>
""")

# =============================================================================
# VERIFIED WIKIMEDIA IMAGE HOOKS & ATTACHMENTS FOR TOPIC 2
# =============================================================================

TOPIC2_ASSETS = [
    # Lesson 1 (Lesson 1283): Atomic Theory and Models
    {
        "unit_order": 1,
        "page_number": 1,
        "block_type": "suggested_image",
        "asset_type": "image",
        "title": "Unlocking the Subatomic World",
        "url": "https://upload.wikimedia.org/wikipedia/commons/f/f8/Sir_Ernest_Rutherford_LCCN2014716719_-_restoration1.jpg",
        "caption": "Sir Ernest Rutherford, pioneer of modern nuclear physics whose alpha scattering experiment revealed the atomic nucleus.",
        "metadata": {
            "author": "Bain News Service / Library of Congress",
            "licensing": "Public domain",
            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Sir_Ernest_Rutherford_LCCN2014716719_-_restoration1.jpg"
        }
    },
    {
        "unit_order": 1,
        "page_number": 3,
        "block_type": "suggested_diagram",
        "asset_type": "diagram",
        "title": "Rutherford Gold Foil Experiment & Alpha Particle Scattering",
        "svg_content": SVG_RUTHERFORD_EXPERIMENT,
        "metadata": {
            "svg_content": SVG_RUTHERFORD_EXPERIMENT,
            "theme": "dark"
        }
    },
    {
        "unit_order": 1,
        "page_number": 4,
        "block_type": "suggested_video",
        "asset_type": "youtube",
        "title": "3D Animation: Rutherford's Gold Foil Experiment and Nuclear Model",
        "url": "https://www.youtube.com/watch?v=5pZj0u_XMbc",
        "description": "Watch a high-definition 3D visualization showing alpha particles penetrating gold atomic lattices, experiencing electrostatic repulsion near the dense positive nucleus.",
        "metadata": {
            "youtube_id": "5pZj0u_XMbc"
        }
    },

    # Lesson 2 (Lesson 1284): Subatomic Particles, Atomic Number, and Mass Number
    {
        "unit_order": 2,
        "page_number": 1,
        "block_type": "suggested_image",
        "asset_type": "image",
        "title": "The Architecture of the Atom",
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/cd/Graduated_chemical_glassware_%28Alessandri_1895.2%29.png",
        "caption": "Precision scientific instrumentation used to probe the subatomic composition and nuclear mass of matter.",
        "metadata": {
            "author": "Alessandri / valeg96",
            "licensing": "Public domain",
            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Graduated_chemical_glassware_(Alessandri_1895.2).png"
        }
    },
    {
        "unit_order": 2,
        "page_number": 4,
        "block_type": "suggested_diagram",
        "asset_type": "diagram",
        "title": "Nuclide Notation and Carbon-12 Structure",
        "svg_content": SVG_NUCLIDE_CARBON12,
        "metadata": {
            "svg_content": SVG_NUCLIDE_CARBON12,
            "theme": "dark"
        }
    },

    # Lesson 3 (Lesson 1285): Isotopes and Relative Atomic Mass
    {
        "unit_order": 3,
        "page_number": 1,
        "block_type": "suggested_image",
        "asset_type": "image",
        "title": "The Mystery of Fractional Atomic Masses",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/78/Chlorine_liquid_in_an_ampoule.jpg",
        "caption": "Liquid elemental chlorine sealed in a high-pressure ampoule, demonstrating non-integer relative atomic mass (35.5 amu) due to natural isotopic distribution.",
        "metadata": {
            "author": "Alchemist-hp",
            "licensing": "Free Art License (FAL)",
            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Chlorine_liquid_in_an_ampoule.jpg"
        }
    },
    {
        "unit_order": 3,
        "page_number": 2,
        "block_type": "suggested_diagram",
        "asset_type": "diagram",
        "title": "Nuclear Structures of Carbon-12, Carbon-13, and Carbon-14",
        "svg_content": SVG_CARBON_ISOTOPES,
        "metadata": {
            "svg_content": SVG_CARBON_ISOTOPES,
            "theme": "dark"
        }
    },

    # Lesson 4 (Lesson 1286): Energy Levels, Orbitals, and s/p Notation
    {
        "unit_order": 4,
        "page_number": 1,
        "block_type": "suggested_image",
        "asset_type": "image",
        "title": "The Quantum Nature of Electron Orbitals",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/6f/A_group_of_scientists_working_in_a_laboratory_Esculab.jpg",
        "caption": "Research spectroscopy laboratory probing quantized electronic transitions and atomic orbital distributions.",
        "metadata": {
            "author": "Esculab Lab",
            "licensing": "CC0",
            "commons_page_url": "https://commons.wikimedia.org/wiki/File:A_group_of_scientists_working_in_a_laboratory_Esculab.jpg"
        }
    },
    {
        "unit_order": 4,
        "page_number": 2,
        "block_type": "suggested_diagram",
        "asset_type": "diagram",
        "title": "3D Geometries of Spherical s and Dumbbell px, py, pz Orbitals",
        "svg_content": SVG_ORBITAL_SHAPES,
        "metadata": {
            "svg_content": SVG_ORBITAL_SHAPES,
            "theme": "dark"
        }
    },

    # Lesson 5 (Lesson 1287): Integrated Atomic Representation and Review
    {
        "unit_order": 5,
        "page_number": 1,
        "block_type": "suggested_image",
        "asset_type": "image",
        "title": "Connecting the Microscopic to the Macroscopic",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/60/Sodium_%28Element_-_11%29_3.jpg",
        "caption": "Elemental sodium metal chunk immersed in protective mineral oil, displaying metallic lustre and reactivity arising from its single valence electron.",
        "metadata": {
            "author": "James St. John",
            "licensing": "CC BY 2.0",
            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Sodium_(Element_-_11)_3.jpg"
        }
    },
    {
        "unit_order": 5,
        "page_number": 2,
        "block_type": "suggested_diagram",
        "asset_type": "diagram",
        "title": "Comprehensive Chemical Profile: Sodium (Na) Triplet Representation",
        "svg_content": SVG_SODIUM_PROFILE,
        "metadata": {
            "svg_content": SVG_SODIUM_PROFILE,
            "theme": "dark"
        }
    }
]

def enrich_topic2():
    print("=" * 80)
    print("ENRICHING GRADE 10 CHEMISTRY — TOPIC 2: THE ATOM")
    print("=" * 80)

    topic = Topic.objects.get(subject__id=5, order=2)
    print(f"Target Topic: [{topic.id}] {topic.name}")

    for asset_def in TOPIC2_ASSETS:
        unit_order = asset_def["unit_order"]
        page_num = asset_def["page_number"]
        block_type = asset_def["block_type"]
        asset_type = asset_def["asset_type"]
        title = asset_def["title"]
        metadata = asset_def.get("metadata", {})

        lesson = Lesson.objects.get(topic=topic, learning_unit__order=unit_order)
        block = LessonBlock.objects.filter(lesson=lesson, page_number=page_num, block_type=block_type).first()

        if not block:
            print(f"  [WARN] Block not found for Lesson [{lesson.id}] Page {page_num} ({block_type})")
            continue

        # Resolve or create LessonAsset
        existing_asset = LessonAsset.objects.filter(lesson=lesson, title=title).first()
        if not existing_asset:
            asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type=asset_type,
                source_type="external" if asset_type != "diagram" else "ai_generated",
                storage_type="url" if asset_type != "diagram" else "embed",
                status="attached",
                title=title,
                url=asset_def.get("url"),
                description=asset_def.get("caption") or asset_def.get("description"),
                metadata=metadata
            )
            print(f"  [Created Asset] [{asset.asset_type}] '{title}' in Lesson [{lesson.id}]")
        else:
            asset = existing_asset
            asset.asset_type = asset_type
            asset.status = "attached"
            asset.url = asset_def.get("url")
            asset.description = asset_def.get("caption") or asset_def.get("description")
            asset.metadata = metadata
            asset.save()
            print(f"  [Updated Asset] [{asset.asset_type}] '{title}' in Lesson [{lesson.id}]")

        # Link asset to block
        block.assets.add(asset)

        # Update block content payload with resolved media properties
        content = block.content or {}
        if asset_type == "image":
            content["resolved_image_url"] = asset_def["url"]
            content["caption"] = asset_def.get("caption")
        elif asset_type == "diagram":
            content["svg_content"] = asset_def.get("svg_content")
            content["caption"] = asset_def.get("title")
        elif asset_type == "youtube":
            content["url"] = asset_def.get("url")
            content["description"] = asset_def.get("description")

        block.content = content
        block.save()

    print("\nSUCCESS: Topic 2 Visual & Media Enrichment Completed!")

if __name__ == "__main__":
    enrich_topic2()
