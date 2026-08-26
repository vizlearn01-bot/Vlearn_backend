"""
VLearn Grade 10 Biology — Topic 3: Cell Structure and Specialization
Visual Enrichment Engine (High-Detail Vector SVGs + Contextualized Photos + YouTube per Lesson)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 10 (Grade ID: 5, Level: 10)
Subject: Biology (Grade 10 CBC)
Topic: Cell Structure and Specialization (Topic Order: 3)

Enriches all 5 Lessons:
  1. Lesson 3.1 (Microscopy: Light and Electron Microscopes):
     - Vector SVG: Visualizing Optical Physics (Magnification vs Resolving Power)
     - Photographic Asset: Modern Research Transmission Electron Microscope (TEM) Laboratory Unit
     - YouTube Video: "Microscopy: Light vs. Electron Microscopes"
  2. Lesson 3.2 (Temporary Slides and Microscopic Observation):
     - Vector SVG: Microscope Field of View (FOV) Calibration & Cell Size Calculation
     - Photographic Asset: Light Micrograph of Stained Onion Epidermal Cells at 400x
     - YouTube Video: "Step-by-Step Slide Preparation and Field of View Calculation"
  3. Lesson 3.3 (Plant and Animal Cell Structure and Functions):
     - Vector SVG: Detailed Eukaryotic Ultrastructure (Plant Cell vs Animal Cell)
     - Photographic Asset: Transmission Electron Micrograph (TEM) of Mitochondria and Organelles
     - YouTube Video: "Eukaryotic Cell Structure, Organelles, and Ultrastructure"
  4. Lesson 3.4 (Specialized Cells and Adaptation to Function):
     - Vector SVG: Specialized Plant and Animal Cell Adaptations Matrix (6 Cells)
     - Photographic Asset: Scanning Electron Micrograph (SEM) of Human Red Blood Cells
     - YouTube Video: "Specialized Cells and Adaptations to Function"
  5. Lesson 3.5 (Levels of Organization in Living Organisms):
     - Vector SVG: Nested Hierarchy of Biological Organization (Concentric Tiers & Dual Pathways)
     - Photographic Asset: Biological Organization (From Cells to Multicellular Organisms)
     - YouTube Video: "Levels of Biological Organization — From Organelles to Organisms"

Usage:
  ./venv/bin/python curriculum/enrich_grade10_biology_topic3.py
"""

import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, Lesson, LessonBlock, LessonAsset
)

def sanitize_svg(svg: str) -> str:
    """Ensures SVG is clean, responsive, and stripped of unneeded XML headers."""
    svg = re.sub(r'<\?xml.*?\?>', '', svg)
    svg = re.sub(r'<!DOCTYPE.*?>', '', svg)
    return svg.strip()

# =====================================================================
# 5 HIGH-QUALITY BIOLOGICAL VECTOR SVGS FOR TOPIC 3
# =====================================================================

# SVG 1 (Lesson 3.1): Magnification vs Resolving Power
SVG_1 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 500" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="880" height="470" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="460" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Visualizing Optical Physics: Magnification vs. Resolving Power</text>
  <text x="460" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Mathematical enlargement without wavelength resolution produces empty, blurry magnification</text>

  <!-- LEFT PANEL: HIGH MAGNIFICATION, LOW RESOLUTION (EMPTY MAGNIFICATION) -->
  <rect x="40" y="85" width="400" height="280" rx="12" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
  <text x="240" y="115" font-size="15" font-weight="bold" fill="#f87171" text-anchor="middle">1. High Magnification, Low Resolution</text>
  <text x="240" y="133" font-size="11" fill="#fca5a5" text-anchor="middle">(Empty Magnification — Visible Light Limit: 200 nm)</text>

  <!-- Blurry overlapping oval -->
  <defs>
    <radialGradient id="blurGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ef4444" stop-opacity="0.8"/>
      <stop offset="60%" stop-color="#ef4444" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#0f172a" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <ellipse cx="240" cy="220" rx="90" ry="55" fill="url(#blurGrad)"/>
  <ellipse cx="210" cy="220" rx="40" ry="40" fill="#f87171" opacity="0.3"/>
  <ellipse cx="270" cy="220" rx="40" ry="40" fill="#f87171" opacity="0.3"/>
  <text x="240" y="225" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Two Points Blurred as One</text>

  <text x="240" y="315" font-size="10.5" fill="#fca5a5" text-anchor="middle">• Magnified 1000×, but points closer than 200 nm</text>
  <text x="240" y="335" font-size="10" fill="#cbd5e1" text-anchor="middle">• Long light waves cannot pass between points</text>

  <!-- RIGHT PANEL: HIGH MAGNIFICATION, HIGH RESOLUTION (ELECTRON MICROSCOPE) -->
  <rect x="480" y="85" width="400" height="280" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="680" y="115" font-size="15" font-weight="bold" fill="#34d399" text-anchor="middle">2. High Magnification, High Resolution</text>
  <text x="680" y="133" font-size="11" fill="#86efac" text-anchor="middle">(High Resolving Power — Electron Beam: 0.2 nm)</text>

  <!-- Two distinct crisp points -->
  <circle cx="630" cy="220" r="30" fill="#065f46" stroke="#22c55e" stroke-width="3"/>
  <circle cx="630" cy="220" r="8" fill="#86efac"/>
  <circle cx="730" cy="220" r="30" fill="#065f46" stroke="#22c55e" stroke-width="3"/>
  <circle cx="730" cy="220" r="8" fill="#86efac"/>

  <line x1="660" y1="220" x2="700" y2="220" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3"/>
  <text x="680" y="210" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Resolved Gap</text>
  <text x="680" y="275" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">Two Distinct Sharp Structures</text>

  <text x="680" y="315" font-size="10.5" fill="#86efac" text-anchor="middle">• Magnified 1000× and clearly separated</text>
  <text x="680" y="335" font-size="10" fill="#cbd5e1" text-anchor="middle">• Tiny electron wavelength (0.005 nm) resolves 0.2 nm gaps</text>

  <!-- BOTTOM COMPARISON BANNER -->
  <rect x="40" y="385" width="840" height="80" rx="8" fill="#0f172a" stroke="#334155"/>
  <text x="460" y="410" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Fundamental Principle of Cytology</text>
  <text x="460" y="432" font-size="11" fill="#e2e8f0" text-anchor="middle">Magnification makes objects look larger; Resolution determines the level of fine structural detail visible.</text>
  <text x="460" y="450" font-size="10" fill="#94a3b8" text-anchor="middle">Light Microscope Limit: 200 nm | Transmission Electron Microscope Limit: 0.2 nm (1,000x greater clarity)</text>
</svg>
""")

# SVG 2 (Lesson 3.2): Field of View (FOV) Calibration & Cell Size Calculation
SVG_2 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 500" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="880" height="470" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="460" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Microscope Field of View (FOV) Calibration &amp; Cell Size Metrology</text>
  <text x="460" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Step-by-step mathematical conversion from millimeter stage ruler to micrometer single-cell dimensions</text>

  <!-- PANEL 1: CALIBRATING FIELD OF VIEW (LEFT) -->
  <rect x="40" y="85" width="410" height="380" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="245" y="115" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">Step 1: Calibrate FOV with Transparent Ruler</text>

  <!-- Circular FOV -->
  <circle cx="245" cy="220" r="95" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>

  <!-- Ruler scale across center -->
  <rect x="150" y="210" width="190" height="40" fill="#334155" opacity="0.8" stroke="#64748b"/>
  <!-- Millimeter tick marks -->
  <line x1="160" y1="210" x2="160" y2="225" stroke="#ffffff" stroke-width="2"/>
  <line x1="215" y1="210" x2="215" y2="225" stroke="#ffffff" stroke-width="2"/>
  <line x1="270" y1="210" x2="270" y2="225" stroke="#ffffff" stroke-width="2"/>
  <line x1="325" y1="210" x2="325" y2="225" stroke="#ffffff" stroke-width="2"/>
  <!-- Labels -->
  <text x="160" y="240" font-size="9" fill="#ffffff" text-anchor="middle">0</text>
  <text x="215" y="240" font-size="9" fill="#ffffff" text-anchor="middle">1 mm</text>
  <text x="270" y="240" font-size="9" fill="#ffffff" text-anchor="middle">2 mm</text>
  <text x="325" y="240" font-size="9" fill="#ffffff" text-anchor="middle">3 mm</text>

  <!-- Measurement bracket -->
  <line x1="160" y1="180" x2="325" y2="180" stroke="#f59e0b" stroke-width="2"/>
  <line x1="160" y1="175" x2="160" y2="185" stroke="#f59e0b" stroke-width="2"/>
  <line x1="325" y1="175" x2="325" y2="185" stroke="#f59e0b" stroke-width="2"/>
  <text x="242" y="172" font-size="11" font-weight="bold" fill="#fef08a" text-anchor="middle">Diameter = 3 mm</text>

  <!-- Conversion callout -->
  <rect x="60" y="340" width="370" height="100" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="245" y="365" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Conversion to Micrometers (µm):</text>
  <text x="245" y="390" font-size="13" font-weight="bold" fill="#fcd34d" text-anchor="middle">1 mm = 1,000 µm</text>
  <text x="245" y="415" font-size="12" fill="#e2e8f0" text-anchor="middle">3 mm × 1,000 = <tspan fill="#34d399" font-weight="bold">3,000 µm (FOV Diameter)</tspan></text>

  <!-- PANEL 2: ESTIMATING CELL SIZE (RIGHT) -->
  <rect x="470" y="85" width="410" height="380" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="675" y="115" font-size="14" font-weight="bold" fill="#34d399" text-anchor="middle">Step 2: Count Cells Across Diameter &amp; Calculate</text>

  <!-- Circular FOV -->
  <circle cx="675" cy="220" r="95" fill="#1e293b" stroke="#10b981" stroke-width="3"/>

  <!-- 15 Onion cells lined up across diameter -->
  <g fill="#065f46" stroke="#34d399" stroke-width="1.5">
    <rect x="580" y="210" width="12.5" height="20" rx="1"/>
    <rect x="592.5" y="210" width="12.5" height="20" rx="1"/>
    <rect x="605" y="210" width="12.5" height="20" rx="1"/>
    <rect x="617.5" y="210" width="12.5" height="20" rx="1"/>
    <rect x="630" y="210" width="12.5" height="20" rx="1"/>
    <rect x="642.5" y="210" width="12.5" height="20" rx="1"/>
    <rect x="655" y="210" width="12.5" height="20" rx="1"/>
    <rect x="667.5" y="210" width="12.5" height="20" rx="1"/>
    <rect x="680" y="210" width="12.5" height="20" rx="1"/>
    <rect x="692.5" y="210" width="12.5" height="20" rx="1"/>
    <rect x="705" y="210" width="12.5" height="20" rx="1"/>
    <rect x="717.5" y="210" width="12.5" height="20" rx="1"/>
    <rect x="730" y="210" width="12.5" height="20" rx="1"/>
    <rect x="742.5" y="210" width="12.5" height="20" rx="1"/>
    <rect x="755" y="210" width="12.5" height="20" rx="1"/>
  </g>
  <text x="675" y="260" font-size="10.5" font-weight="bold" fill="#86efac" text-anchor="middle">15 Onion Cells Aligned Across Diameter</text>

  <!-- Calculation Box -->
  <rect x="490" y="340" width="370" height="100" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="675" y="365" font-size="11.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Actual Cell Size Formula:</text>
  <text x="675" y="390" font-size="11" fill="#cbd5e1" text-anchor="middle">Actual Size = FOV Diameter / Cell Count</text>
  <text x="675" y="418" font-size="13" font-weight="bold" fill="#4ade80" text-anchor="middle">Size = 3,000 µm / 15 cells = 200 µm</text>
</svg>
""")

# SVG 3 (Lesson 3.3): Detailed Eukaryotic Ultrastructure (Plant Cell vs Animal Cell)
SVG_3 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="880" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="460" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Detailed Eukaryotic Ultrastructure: Plant Cell vs. Animal Cell</text>
  <text x="460" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Sub-cellular organelles revealed by high-resolution transmission electron microscopy</text>

  <!-- LEFT: PLANT CELL -->
  <rect x="40" y="85" width="410" height="400" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
  <text x="245" y="115" font-size="15" font-weight="bold" fill="#34d399" text-anchor="middle">Plant Cell (Rigid Cellulose Wall)</text>

  <!-- Thick Cellulose Wall -->
  <rect x="65" y="130" width="360" height="330" rx="8" fill="#064e3b" stroke="#22c55e" stroke-width="5"/>
  <!-- Cell Membrane -->
  <rect x="73" y="138" width="344" height="314" rx="6" fill="#065f46" stroke="#10b981" stroke-width="1.5"/>

  <!-- Large Central Vacuole with Tonoplast -->
  <ellipse cx="230" cy="270" rx="90" ry="80" fill="#0284c7" opacity="0.4" stroke="#38bdf8" stroke-width="2"/>
  <text x="230" y="275" font-size="11" font-weight="bold" fill="#bae6fd" text-anchor="middle">Large Central Vacuole</text>
  <text x="230" y="290" font-size="9" fill="#7dd3fc" text-anchor="middle">(Cell Sap &amp; Turgor)</text>

  <!-- Nucleus (Pushed to periphery) -->
  <circle cx="350" cy="200" r="35" fill="#7c3aed" opacity="0.8" stroke="#a855f7" stroke-width="2"/>
  <circle cx="350" cy="200" r="12" fill="#c084fc"/>
  <text x="350" y="195" font-size="9.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Nucleus</text>
  <text x="350" y="207" font-size="7.5" fill="#f3e8ff" text-anchor="middle">Nucleolus</text>

  <!-- Chloroplasts (Green ovals with grana) -->
  <g fill="#15803d" stroke="#4ade80" stroke-width="1.5">
    <ellipse cx="115" cy="180" rx="26" ry="16"/>
    <ellipse cx="120" cy="380" rx="26" ry="16"/>
    <ellipse cx="340" cy="380" rx="26" ry="16"/>
  </g>
  <text x="115" y="184" font-size="8.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Chloroplast</text>
  <text x="120" y="384" font-size="8.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Chloroplast</text>

  <!-- Mitochondria -->
  <g fill="#991b1b" stroke="#ef4444" stroke-width="1.5">
    <ellipse cx="115" cy="280" rx="20" ry="12"/>
    <ellipse cx="350" cy="300" rx="20" ry="12"/>
  </g>
  <text x="115" y="284" font-size="7.5" font-weight="bold" fill="#fca5a5" text-anchor="middle">Mitochondrion</text>

  <!-- Labels -->
  <text x="75" y="125" font-size="9" font-weight="bold" fill="#4ade80">Cellulose Cell Wall</text>
  <text x="350" y="155" font-size="9" fill="#c084fc">Peripheral Nucleus</text>

  <!-- RIGHT: ANIMAL CELL -->
  <rect x="470" y="85" width="410" height="400" rx="12" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
  <text x="675" y="115" font-size="15" font-weight="bold" fill="#fbbf24" text-anchor="middle">Animal Cell (Flexible Membrane)</text>

  <!-- Irregular Flexible Cell Membrane -->
  <path d="M 510 200 C 500 140, 600 130, 680 135 C 780 140, 850 180, 840 260 C 835 340, 810 440, 710 445 C 600 450, 520 420, 505 340 C 495 280, 515 230, 510 200 Z" fill="#1e293b" stroke="#f59e0b" stroke-width="3"/>

  <!-- Centrally Placed Nucleus -->
  <circle cx="675" cy="260" r="45" fill="#7c3aed" opacity="0.8" stroke="#a855f7" stroke-width="2"/>
  <circle cx="675" cy="260" r="16" fill="#c084fc"/>
  <text x="675" y="255" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Central Nucleus</text>
  <text x="675" y="270" font-size="8.5" fill="#f3e8ff" text-anchor="middle">(DNA Chromatin)</text>

  <!-- Multiple Mitochondria (Dense) -->
  <g fill="#991b1b" stroke="#ef4444" stroke-width="1.5">
    <ellipse cx="560" cy="200" rx="24" ry="14"/>
    <ellipse cx="780" cy="210" rx="24" ry="14"/>
    <ellipse cx="580" cy="350" rx="24" ry="14"/>
    <ellipse cx="770" cy="340" rx="24" ry="14"/>
  </g>
  <text x="560" y="204" font-size="8" font-weight="bold" fill="#fca5a5" text-anchor="middle">Mitochondria</text>
  <text x="780" y="214" font-size="8" font-weight="bold" fill="#fca5a5" text-anchor="middle">Mitochondria</text>

  <!-- Centrioles at 90 degrees -->
  <rect x="660" y="170" width="8" height="22" rx="1" fill="#f59e0b"/>
  <rect x="670" y="178" width="22" height="8" rx="1" fill="#f59e0b"/>
  <text x="675" y="165" font-size="9" font-weight="bold" fill="#fbbf24" text-anchor="middle">Centrioles (Spindle)</text>

  <!-- Lysosomes -->
  <circle cx="560" cy="275" r="12" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="560" y="279" font-size="7.5" fill="#ffffff" text-anchor="middle">Lysosome</text>

  <!-- Golgi Apparatus -->
  <path d="M 740 270 Q 755 280 740 290 M 745 265 Q 760 280 745 295" stroke="#38bdf8" stroke-width="3" fill="none"/>
  <text x="790" y="285" font-size="8.5" fill="#7dd3fc">Golgi Bodies</text>
</svg>
""")

# SVG 4 (Lesson 3.4): Specialized Plant and Animal Cell Adaptations Matrix (6 Cells)
SVG_4 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="880" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="460" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Specialized Plant &amp; Animal Cell Adaptations Matrix</text>
  <text x="460" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Structure-to-function evolutionary modifications for physiological division of labor</text>

  <!-- 1. ROOT HAIR CELL (Top Left) -->
  <rect x="40" y="85" width="270" height="190" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="175" y="108" font-size="12.5" font-weight="bold" fill="#34d399" text-anchor="middle">1. Root Hair Cell (Plant)</text>
  <!-- Cell body with long lateral extension -->
  <path d="M 60 170 L 100 170 L 230 185 L 230 195 L 100 210 L 60 210 Z" fill="#065f46" stroke="#22c55e" stroke-width="1.5"/>
  <text x="175" y="235" font-size="9" font-weight="bold" fill="#86efac" text-anchor="middle">• Long extension expands surface area</text>
  <text x="175" y="250" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• No chloroplasts; high solute vacuole</text>
  <text x="175" y="265" font-size="8.5" fill="#38bdf8" text-anchor="middle">Function: Water &amp; Mineral Uptake</text>

  <!-- 2. PALISADE MESOPHYLL (Top Center) -->
  <rect x="325" y="85" width="270" height="190" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
  <text x="460" y="108" font-size="12.5" font-weight="bold" fill="#4ade80" text-anchor="middle">2. Palisade Cell (Plant)</text>
  <!-- Columnar cell packed with chloroplasts -->
  <rect x="430" y="130" width="60" height="85" rx="4" fill="#15803d" stroke="#22c55e" stroke-width="1.5"/>
  <!-- Chloroplast dots -->
  <circle cx="445" cy="145" r="4" fill="#86efac"/><circle cx="475" cy="145" r="4" fill="#86efac"/>
  <circle cx="445" cy="170" r="4" fill="#86efac"/><circle cx="475" cy="170" r="4" fill="#86efac"/>
  <circle cx="460" cy="195" r="4" fill="#86efac"/>
  <text x="460" y="235" font-size="9" font-weight="bold" fill="#86efac" text-anchor="middle">• Columnar vertical orientation</text>
  <text x="460" y="250" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Packed with dense chloroplasts</text>
  <text x="460" y="265" font-size="8.5" fill="#38bdf8" text-anchor="middle">Function: Maximum Photosynthesis</text>

  <!-- 3. GUARD CELL PAIR (Top Right) -->
  <rect x="610" y="85" width="270" height="190" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="745" y="108" font-size="12.5" font-weight="bold" fill="#34d399" text-anchor="middle">3. Guard Cells (Plant)</text>
  <!-- Pair of guard cells -->
  <path d="M 725 140 C 705 160, 705 190, 725 210 C 715 190, 715 160, 725 140 Z" fill="#065f46" stroke="#22c55e" stroke-width="1.5"/>
  <path d="M 765 140 C 785 160, 785 190, 765 210 C 775 190, 775 160, 765 140 Z" fill="#065f46" stroke="#22c55e" stroke-width="1.5"/>
  <text x="745" y="235" font-size="9" font-weight="bold" fill="#86efac" text-anchor="middle">• Thick inner wall, thin outer wall</text>
  <text x="745" y="250" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Turgor changes open/close pore</text>
  <text x="745" y="265" font-size="8.5" fill="#38bdf8" text-anchor="middle">Function: Gas Exchange Regulation</text>

  <!-- 4. RED BLOOD CELL (Bottom Left) -->
  <rect x="40" y="295" width="270" height="190" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
  <text x="175" y="318" font-size="12.5" font-weight="bold" fill="#f87171" text-anchor="middle">4. Red Blood Cell (Animal)</text>
  <!-- Biconcave disc -->
  <ellipse cx="175" cy="365" rx="55" ry="25" fill="#991b1b" stroke="#ef4444" stroke-width="2"/>
  <ellipse cx="175" cy="365" rx="25" ry="10" fill="#7f1d1d" stroke="#ef4444" stroke-width="1"/>
  <text x="175" y="425" font-size="9" font-weight="bold" fill="#fca5a5" text-anchor="middle">• Biconcave shape (Max Surface Area/Vol)</text>
  <text x="175" y="440" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Lacks nucleus to pack hemoglobin</text>
  <text x="175" y="455" font-size="8.5" fill="#38bdf8" text-anchor="middle">Function: Oxygen Transport</text>

  <!-- 5. SPERM CELL (Bottom Center) -->
  <rect x="325" y="295" width="270" height="190" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="460" y="318" font-size="12.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">5. Sperm Cell (Animal)</text>
  <!-- Head, midpiece, flagellum -->
  <ellipse cx="375" cy="370" rx="16" ry="10" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
  <rect x="391" y="366" width="18" height="8" rx="2" fill="#ef4444"/>
  <path d="M 409 370 Q 450 350 490 375 T 570 365" fill="none" stroke="#38bdf8" stroke-width="2"/>
  <text x="460" y="425" font-size="9" font-weight="bold" fill="#7dd3fc" text-anchor="middle">• Acrosome enzymes + Mitochondria midpiece</text>
  <text x="460" y="440" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Whiplash flagellum tail for motility</text>
  <text x="460" y="455" font-size="8.5" fill="#34d399" text-anchor="middle">Function: Reproduction / Fertilization</text>

  <!-- 6. MOTOR NEURON (Bottom Right) -->
  <rect x="610" y="295" width="270" height="190" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
  <text x="745" y="318" font-size="12.5" font-weight="bold" fill="#c084fc" text-anchor="middle">6. Motor Neuron (Animal)</text>
  <!-- Cell body, dendrites, axon with myelin sheath -->
  <circle cx="645" cy="370" r="14" fill="#6b21a8" stroke="#a855f7" stroke-width="1.5"/>
  <line x1="659" y1="370" x2="840" y2="370" stroke="#c084fc" stroke-width="2"/>
  <!-- Myelin sheaths -->
  <rect x="680" y="363" width="20" height="14" rx="3" fill="#f59e0b"/>
  <rect x="710" y="363" width="20" height="14" rx="3" fill="#f59e0b"/>
  <rect x="740" y="363" width="20" height="14" rx="3" fill="#f59e0b"/>
  <rect x="770" y="363" width="20" height="14" rx="3" fill="#f59e0b"/>
  <text x="745" y="425" font-size="9" font-weight="bold" fill="#e9d5ff" text-anchor="middle">• Long axon transmits signals 1m</text>
  <text x="745" y="440" font-size="8.5" fill="#cbd5e1" text-anchor="middle">• Insulating fatty myelin speeds impulses</text>
  <text x="745" y="455" font-size="8.5" fill="#38bdf8" text-anchor="middle">Function: Rapid Nerve Transmission</text>
</svg>
""")

# SVG 5 (Lesson 3.5): Nested Hierarchy of Biological Organization
SVG_5 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="880" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="460" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Nested Hierarchy of Biological Organization</text>
  <text x="460" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Ascending structural tiers from sub-cellular organelles to complete living multicellular organisms</text>

  <!-- CONCENTRIC CIRCULAR HIERARCHY (LEFT) -->
  <g transform="translate(240, 280)">
    <!-- Level 6: Organism (Outermost) -->
    <circle cx="0" cy="0" r="180" fill="#0f172a" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="0" y="-155" font-size="11.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">6. ORGANISM (Human / Maize Plant)</text>

    <!-- Level 5: Organ System -->
    <circle cx="0" cy="15" r="145" fill="#1e293b" stroke="#818cf8" stroke-width="2"/>
    <text x="0" y="-105" font-size="11" font-weight="bold" fill="#a5b4fc" text-anchor="middle">5. ORGAN SYSTEM (Circulatory / Shoot)</text>

    <!-- Level 4: Organ -->
    <circle cx="0" cy="30" r="110" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <text x="0" y="-55" font-size="10.5" font-weight="bold" fill="#c084fc" text-anchor="middle">4. ORGAN (Heart / Leaf)</text>

    <!-- Level 3: Tissue -->
    <circle cx="0" cy="45" r="80" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
    <text x="0" y="-10" font-size="10" font-weight="bold" fill="#fda4af" text-anchor="middle">3. TISSUE (Muscle / Mesophyll)</text>

    <!-- Level 2: Cell -->
    <circle cx="0" cy="60" r="55" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <text x="0" y="35" font-size="9.5" font-weight="bold" fill="#fcd34d" text-anchor="middle">2. CELL (Myocyte)</text>

    <!-- Level 1: Organelle (Innermost) -->
    <circle cx="0" cy="72" r="30" fill="#065f46" stroke="#22c55e" stroke-width="2"/>
    <text x="0" y="76" font-size="8.5" font-weight="bold" fill="#86efac" text-anchor="middle">1. ORGANELLE</text>
  </g>

  <!-- PARALLEL PATHWAYS TABLE (RIGHT) -->
  <rect x="460" y="85" width="420" height="390" rx="12" fill="#0f172a" stroke="#334155"/>
  <text x="670" y="115" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">Dual Parallel Biological Pathways</text>

  <!-- Step 1: Organelle -->
  <rect x="480" y="130" width="380" height="42" rx="6" fill="#1e293b" stroke="#22c55e" stroke-width="1"/>
  <text x="495" y="148" font-size="11" font-weight="bold" fill="#4ade80">1. Organelle Level:</text>
  <text x="495" y="163" font-size="9.5" fill="#e2e8f0">Plant: Chloroplast / Animal: Mitochondrion</text>

  <!-- Step 2: Cell -->
  <rect x="480" y="180" width="380" height="42" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
  <text x="495" y="198" font-size="11" font-weight="bold" fill="#fcd34d">2. Cell Level:</text>
  <text x="495" y="213" font-size="9.5" fill="#e2e8f0">Plant: Palisade Cell / Animal: Cardiac Muscle Cell</text>

  <!-- Step 3: Tissue -->
  <rect x="480" y="230" width="380" height="42" rx="6" fill="#1e293b" stroke="#f43f5e" stroke-width="1"/>
  <text x="495" y="248" font-size="11" font-weight="bold" fill="#fda4af">3. Tissue Level:</text>
  <text x="495" y="263" font-size="9.5" fill="#e2e8f0">Plant: Mesophyll Tissue / Animal: Cardiac Muscle</text>

  <!-- Step 4: Organ -->
  <rect x="480" y="280" width="380" height="42" rx="6" fill="#1e293b" stroke="#a855f7" stroke-width="1"/>
  <text x="495" y="298" font-size="11" font-weight="bold" fill="#c084fc">4. Organ Level:</text>
  <text x="495" y="313" font-size="9.5" fill="#e2e8f0">Plant: Foliage Leaf / Animal: Human Heart</text>

  <!-- Step 5: Organ System -->
  <rect x="480" y="330" width="380" height="42" rx="6" fill="#1e293b" stroke="#818cf8" stroke-width="1"/>
  <text x="495" y="348" font-size="11" font-weight="bold" fill="#a5b4fc">5. Organ System Level:</text>
  <text x="495" y="363" font-size="9.5" fill="#e2e8f0">Plant: Shoot System / Animal: Circulatory System</text>

  <!-- Step 6: Organism -->
  <rect x="480" y="380" width="380" height="42" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
  <text x="495" y="398" font-size="11" font-weight="bold" fill="#38bdf8">6. Organism Level:</text>
  <text x="495" y="413" font-size="9.5" fill="#e2e8f0">Plant: Whole Maize Plant / Animal: Complete Human</text>

  <text x="670" y="455" font-size="10.5" font-weight="bold" fill="#34d399" text-anchor="middle">Division of Labor Maximizes Metabolic Efficiency &amp; Organism Survival</text>
</svg>
""")

TOPIC3_BIOLOGY_SVGS = [
    {"lesson_order": 1, "page": 4, "svg": SVG_1, "title": "Visualizing Optical Physics: Magnification vs. Resolving Power"},
    {"lesson_order": 2, "page": 5, "svg": SVG_2, "title": "Microscope Field of View (FOV) Calibration & Cell Size Calculation"},
    {"lesson_order": 3, "page": 3, "svg": SVG_3, "title": "Detailed Ultrastructure: Plant Cell vs. Animal Cell"},
    {"lesson_order": 4, "page": 3, "svg": SVG_4, "title": "Specialized Plant and Animal Cell Adaptations Matrix"},
    {"lesson_order": 5, "page": 3, "svg": SVG_5, "title": "Nested Hierarchy of Biological Organization"},
]

TOPIC3_BIOLOGY_PHOTOS = [
    {
        "lesson_order": 1,
        "page": 6,
        "title": "Modern Research Transmission Electron Microscope (TEM) Laboratory Unit",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Transmission_electron_microscope.jpg/1024px-Transmission_electron_microscope.jpg",
        "author": "GrahamColm / Wikimedia Commons",
        "licensing": "CC BY-SA 3.0",
        "caption": "A research-grade Transmission Electron Microscope utilizing high-velocity electron beams in a vacuum column to resolve sub-cellular organelles down to 0.2 nanometers."
    },
    {
        "lesson_order": 2,
        "page": 7,
        "title": "Light Micrograph of Stained Onion Epidermal Cells at 400x",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Onion_cells_2.jpg/1280px-Onion_cells_2.jpg",
        "author": "Umberto Salvagnin / Wikimedia Commons",
        "licensing": "CC BY 2.0",
        "caption": "Light micrograph of onion epidermal cells at 400x magnification revealing rigid rectangular cellulose walls, cytoplasm, and dark stained nuclei."
    },
    {
        "lesson_order": 3,
        "page": 6,
        "title": "Transmission Electron Micrograph (TEM) of Mitochondria and Organelles",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Mitochondria%2C_mammalian_lung_-_TEM.jpg/1280px-Mitochondria%2C_mammalian_lung_-_TEM.jpg",
        "author": "Louisa Howard / Wikimedia Commons",
        "licensing": "CC0 1.0 Public Domain",
        "caption": "Transmission electron micrograph (TEM) revealing the internal cristae folds of a mitochondrion and surrounding rough endoplasmic reticulum."
    },
    {
        "lesson_order": 4,
        "page": 6,
        "title": "Scanning Electron Micrograph (SEM) of Human Red Blood Cells",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Scanning_Electron_Micrograph_of_Normal_and_Sickle_Red_Blood_Cells.jpg/1280px-Scanning_Electron_Micrograph_of_Normal_and_Sickle_Red_Blood_Cells.jpg",
        "author": "National Cancer Institute / Wikimedia Commons",
        "licensing": "CC0 1.0 Public Domain",
        "caption": "Scanning electron micrograph (SEM) of mammalian red blood cells revealing the biconcave disc geometry that maximizes surface-area-to-volume ratio for oxygen transport."
    },
    {
        "lesson_order": 5,
        "page": 5,
        "title": "Biological Organization: From Cells to Multicellular Organisms",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/African_Bush_Elephant_%28Loxodonta_africana%29_male_%2817293816650%29.jpg/1280px-African_Bush_Elephant_%28Loxodonta_africana%29_male_%2817293816650%29.jpg",
        "author": "Bernard DUPONT / Wikimedia Commons",
        "licensing": "CC BY-SA 2.0",
        "caption": "Multicellular organisms represent the integrated coordination of trillions of cells organized into tissues, organs, and organ systems."
    }
]

TOPIC3_BIOLOGY_VIDEOS = [
    {
        "lesson_order": 1,
        "page": 8,
        "title": "Deep Dive: Microscopy — Light vs. Electron Microscopes",
        "youtube_id": "tVcEEw6qbBQ",
        "description": "Educational video exploring optical light microscopy, transmission and scanning electron microscopes, magnification formulas, and resolving power limits."
    },
    {
        "lesson_order": 2,
        "page": 8,
        "title": "Deep Dive: Step-by-Step Slide Preparation and Field of View Calculation",
        "youtube_id": "zY66l6cQJm4",
        "description": "Laboratory demonstration showing onion epidermal peeling, iodine staining, bubble-free coverslip mounting, and field of view calibration formulas."
    },
    {
        "lesson_order": 3,
        "page": 8,
        "title": "Deep Dive: Eukaryotic Cell Structure, Organelles, and Ultrastructure",
        "youtube_id": "URUJD5NEXC8",
        "description": "Detailed video exploration of eukaryotic organelle ultrastructure, mitochondria cristae, chloroplast thylakoids, and comparative plant vs animal cytology."
    },
    {
        "lesson_order": 4,
        "page": 7,
        "title": "Deep Dive: Specialized Cells and Adaptations to Function",
        "youtube_id": "wFYz0b3Uu18",
        "description": "Video presentation exploring cellular differentiation, plant cell adaptations (root hairs, palisade, guard cells), and animal cell specializations (erythrocytes, neurons, sperm)."
    },
    {
        "lesson_order": 5,
        "page": 7,
        "title": "Deep Dive: Levels of Biological Organization — From Organelles to Organisms",
        "youtube_id": "-b3k_Pdr7dM",
        "description": "Video guide exploring the hierarchy of life: organelle, cell, tissue, organ, organ system, and multicellular organism integration."
    }
]

def enrich_grade10_biology_topic3():
    print("=" * 80)
    print("VLearn Grade 10 Biology — Topic 3 (Cell Structure & Specialization)")
    print("Visual Enrichment Engine: Attaching SVGs, Photos, and YouTube Videos")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="CBC").first() or Curriculum.objects.filter(id=5).first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 10").first() or Grade.objects.filter(curriculum=curriculum, level=10).first()
    subject = Subject.objects.filter(grade=grade, name="Biology").first()
    topic = Topic.objects.filter(subject=subject, name="Cell Structure and Specialization").first()

    if not topic:
        print("[!] Error: Topic 'Cell Structure and Specialization' not found under Grade 10 Biology!")
        return

    lessons = list(topic.lessons.all().order_by("learning_unit__order"))
    LessonAsset.objects.filter(lesson__in=lessons).delete()
    print("[*] Cleared existing LessonAssets for clean idempotent visual enrichment.")

    svg_count = 0
    photo_count = 0
    video_count = 0

    for lesson in lessons:
        u_order = lesson.learning_unit.order
        print(f"\n[*] Enriching Lesson {u_order}: {lesson.title}")

        # 1. Attach Vector SVGs to suggested_diagram blocks
        svg_matches = [s for s in TOPIC3_BIOLOGY_SVGS if s["lesson_order"] == u_order]
        diagram_blocks = list(LessonBlock.objects.filter(lesson=lesson, block_type="suggested_diagram").order_by("order"))

        for idx, db in enumerate(diagram_blocks):
            if idx < len(svg_matches):
                sm = svg_matches[idx]
                svg_data = sm["svg"]
                content = db.content or {}
                content["svg_content"] = svg_data
                content["svg"] = svg_data
                content["svg_markup"] = svg_data
                db.content = content
                db.title = sm["title"]
                db.save()

                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    asset_type="diagram",
                    source_type="ai_generated",
                    storage_type="embed",
                    status="attached",
                    title=sm["title"],
                    description=f"High-quality vector diagram: {sm['title']}",
                    metadata={"svg_content": svg_data}
                )
                db.assets.add(asset)
                print(f"  [SVG ATTACHED] '{db.title[:45]}' -> Block ID: {db.id} (Page {db.page_number})")
                svg_count += 1

        # 2. Attach Verified Wikimedia Photos to suggested_image blocks
        photo_matches = [p for p in TOPIC3_BIOLOGY_PHOTOS if p["lesson_order"] == u_order]
        image_blocks = list(LessonBlock.objects.filter(lesson=lesson, block_type="suggested_image").order_by("order"))

        for idx, ib in enumerate(image_blocks):
            if idx < len(photo_matches):
                pm = photo_matches[idx]
                content = ib.content or {}
                content["resolved_image_url"] = pm["url"]
                content["url"] = pm["url"]
                content["author"] = pm["author"]
                content["licensing"] = pm["licensing"]
                content["caption"] = pm["caption"]
                ib.content = content
                ib.title = pm["title"]
                ib.save()

                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    asset_type="image",
                    source_type="external",
                    storage_type="url",
                    status="attached",
                    title=pm["title"],
                    description=pm["caption"],
                    url=pm["url"],
                    metadata={
                        "author": pm["author"],
                        "licensing": pm["licensing"],
                        "caption": pm["caption"]
                    }
                )
                ib.assets.add(asset)
                print(f"  [WIKIMEDIA ATTACHED] '{ib.title[:45]}' -> Block ID: {ib.id} (Page {ib.page_number})")
                photo_count += 1

        # 3. Attach Educational YouTube Videos (Every Lesson)
        video_matches = [v for v in TOPIC3_BIOLOGY_VIDEOS if v["lesson_order"] == u_order]
        for vm in video_matches:
            target_page = vm["page"]
            v_block = LessonBlock.objects.filter(lesson=lesson, page_number=target_page, block_type="suggested_video").first()
            if not v_block:
                last_block = LessonBlock.objects.filter(lesson=lesson, page_number=target_page).order_by("-order").first()
                new_order = (last_block.order + 5) if last_block else 50
                v_block = LessonBlock.objects.create(
                    lesson=lesson,
                    page_number=target_page,
                    page_title=last_block.page_title if last_block else vm["title"],
                    title=vm["title"],
                    block_type="suggested_video",
                    component_type="suggested_video",
                    component_order=new_order,
                    order=new_order,
                    content={
                        "resolved_video_id": vm["youtube_id"],
                        "url": f"https://www.youtube.com/watch?v={vm['youtube_id']}",
                        "description": vm["description"]
                    },
                    metadata={}
                )
            else:
                v_block.title = vm["title"]
                v_block.content = {
                    "resolved_video_id": vm["youtube_id"],
                    "url": f"https://www.youtube.com/watch?v={vm['youtube_id']}",
                    "description": vm["description"]
                }
                v_block.save()

            asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="youtube",
                source_type="external",
                storage_type="url",
                status="attached",
                title=vm["title"],
                description=vm["description"],
                url=f"https://www.youtube.com/watch?v={vm['youtube_id']}",
                metadata={"youtube_id": vm["youtube_id"]}
            )
            v_block.assets.add(asset)
            print(f"  [YOUTUBE ATTACHED] '{v_block.title[:45]}' -> Block ID: {v_block.id} (Page {target_page})")
            video_count += 1

    total_assets = LessonAsset.objects.filter(lesson__in=lessons).count()
    print("=" * 80)
    print("[SUCCESS] Grade 10 Biology Topic 3 Visual Enrichment Complete!")
    print(f"[*] Total Vector SVGs Attached:       {svg_count}")
    print(f"[*] Total Wikimedia Photos Attached:   {photo_count}")
    print(f"[*] Total YouTube Videos Attached:     {video_count}")
    print(f"[*] Total LessonAsset Records Created: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_biology_topic3()
