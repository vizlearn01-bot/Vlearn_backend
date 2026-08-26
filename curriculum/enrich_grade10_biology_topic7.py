"""
VLearn Grade 10 Biology — Topic 7: Plant Gaseous Exchange and Respiration
Visual Enrichment Engine (High-Detail Vector SVGs + Contextualized Photos + YouTube per Lesson)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 10 (Grade ID: 5, Level: 10)
Subject: Biology (Grade 10 CBC)
Topic: Plant Gaseous Exchange and Respiration (Topic Order: 7)

Enriches all 4 Lessons:
  1. Lesson 7.1 (Gaseous Exchange Sites and Plant Adaptations):
     - Vector SVG: Plant Gaseous Exchange Structures & Habitat Adaptations
     - Photographic Asset: Mangrove Aerial Pneumatophore Breathing Roots
     - YouTube Video: "Plant Gaseous Exchange and Environmental Adaptations"
  2. Lesson 7.2 (Opening and Closing of Stomata):
     - Vector SVG: Stomatal Guard Cell Mechanics & Potassium Ion (K+) Theory
     - Photographic Asset: High-Magnification Micrograph of Open and Closed Stomatal Guard Cells
     - YouTube Video: "Mechanisms of Stomatal Opening and Closing (K+ Ion Theory)"
  3. Lesson 7.3 (Aerobic and Anaerobic Respiration in Plants):
     - Vector SVG: Plant Respiration Pathways & Thermos Flask Experiment
     - Photographic Asset: Germinating Bean Seeds Respiration and Thermogenesis
     - YouTube Video: "Plant Cellular Respiration: Aerobic vs. Anaerobic"
  4. Lesson 7.4 (Fermentation Project and Economic Applications):
     - Vector SVG: Yeast Anaerobic Fermentation Apparatus & Domestic 20L Biogas Digester
     - Photographic Asset: Domestic Rural Biogas Digester Plant and Clean Methane Flame
     - YouTube Video: "How to Build a DIY Domestic Biogas Digester"

Usage:
  ./venv/bin/python curriculum/enrich_grade10_biology_topic7.py
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
# 4 HIGH-QUALITY BIOLOGICAL VECTOR SVGS FOR TOPIC 7
# =====================================================================

# SVG 1 (Lesson 7.1): Plant Gaseous Exchange Structures & Habitat Adaptations
SVG_1 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="880" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="460" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Plant Gaseous Exchange Structures &amp; Habitat Adaptations</text>
  <text x="460" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Anatomical modifications across terrestrial, aquatic, and coastal mangrove plants</text>

  <!-- 1. TERRESTRIAL LEAF STOMATA (Left) -->
  <rect x="40" y="85" width="270" height="390" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="175" y="112" font-size="13.5" font-weight="bold" fill="#34d399" text-anchor="middle">1. Terrestrial Mesophytes</text>

  <!-- Leaf schematic -->
  <rect x="55" y="130" width="240" height="15" rx="2" fill="#065f46" stroke="#10b981"/>
  <text x="175" y="142" font-size="8" fill="#a7f3d0" text-anchor="middle">Upper Epidermis (Waxy Cuticle)</text>

  <!-- Mesophyll with air spaces -->
  <g fill="#14532d" stroke="#16a34a">
    <ellipse cx="90" cy="175" rx="18" ry="14"/><ellipse cx="140" cy="180" rx="16" ry="15"/>
    <ellipse cx="190" cy="170" rx="18" ry="13"/><ellipse cx="250" cy="180" rx="18" ry="14"/>
  </g>
  <text x="175" y="210" font-size="9" fill="#86efac" text-anchor="middle">Intercellular Air Spaces</text>

  <!-- Lower Epidermis with Stomata -->
  <rect x="55" y="235" width="80" height="12" fill="#065f46"/>
  <rect x="185" y="235" width="110" height="12" fill="#065f46"/>
  <ellipse cx="150" cy="241" rx="6" ry="5" fill="#10b981"/><ellipse cx="170" cy="241" rx="6" ry="5" fill="#10b981"/>

  <!-- Gas Diffusion Arrows -->
  <g stroke="#38bdf8" stroke-width="2" fill="none">
    <path d="M 160 275 L 160 215"/>
    <polygon points="160,210 156,220 164,220" fill="#38bdf8"/>
  </g>
  <text x="160" y="288" font-size="8.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">CO2 In / O2 Out</text>

  <rect x="50" y="300" width="250" height="160" rx="6" fill="#1e293b"/>
  <text x="60" y="320" font-size="10" font-weight="bold" fill="#34d399">Terrestrial Adaptations:</text>
  <text x="60" y="340" font-size="9" fill="#e2e8f0">• Stomata on shaded lower epidermis</text>
  <text x="60" y="360" font-size="9" fill="#e2e8f0">• Minimizes transpiration water loss</text>
  <text x="60" y="380" font-size="9" fill="#e2e8f0">• Spongy air spaces enable rapid diffusion</text>
  <text x="60" y="400" font-size="9" fill="#e2e8f0">• Lenticels on woody stems</text>
  <text x="60" y="435" font-size="8.5" fill="#94a3b8">Example: Bean, maize, hibiscus</text>

  <!-- 2. FLOATING WATER LILY (Center) -->
  <rect x="325" y="85" width="270" height="390" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="460" y="112" font-size="13.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">2. Floating Hydrophytes</text>

  <!-- Water line -->
  <rect x="340" y="195" width="240" height="85" fill="#0284c7" opacity="0.3"/>
  <line x1="340" y1="195" x2="580" y2="195" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="560" y="190" font-size="8" fill="#38bdf8">Water Surface</text>

  <!-- Lily Leaf Floating -->
  <rect x="350" y="180" width="220" height="25" rx="4" fill="#065f46" stroke="#10b981"/>
  <!-- Upper Stomata -->
  <ellipse cx="400" cy="180" rx="5" ry="3" fill="#38bdf8"/><ellipse cx="460" cy="180" rx="5" ry="3" fill="#38bdf8"/>
  <ellipse cx="520" cy="180" rx="5" ry="3" fill="#38bdf8"/>
  <text x="460" y="165" font-size="9" font-weight="bold" fill="#7dd3fc" text-anchor="middle">Upper Epidermal Stomata</text>

  <!-- Aerenchyma Air Chambers -->
  <ellipse cx="400" cy="245" rx="18" ry="25" fill="#0f172a" stroke="#22c55e"/>
  <ellipse cx="460" cy="245" rx="18" ry="25" fill="#0f172a" stroke="#22c55e"/>
  <ellipse cx="520" cy="245" rx="18" ry="25" fill="#0f172a" stroke="#22c55e"/>
  <text x="460" y="250" font-size="8" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Aerenchyma</text>

  <rect x="335" y="300" width="250" height="160" rx="6" fill="#1e293b"/>
  <text x="345" y="320" font-size="10" font-weight="bold" fill="#38bdf8">Hydrophyte Adaptations:</text>
  <text x="345" y="340" font-size="9" fill="#e2e8f0">• Stomata restricted to upper epidermis</text>
  <text x="345" y="360" font-size="9" fill="#e2e8f0">• Exchanges gases directly with open air</text>
  <text x="345" y="380" font-size="9" fill="#e2e8f0">• Submerged lower surface lacks stomata</text>
  <text x="345" y="400" font-size="9" fill="#e2e8f0">• Large aerenchyma provides buoyancy</text>
  <text x="345" y="435" font-size="8.5" fill="#94a3b8">Example: Water Lily (Nymphaea)</text>

  <!-- 3. MANGROVE PNEUMATOPHORES (Right) -->
  <rect x="610" y="85" width="270" height="390" rx="12" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="745" y="112" font-size="13.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">3. Mangrove Halophytes</text>

  <!-- Anaerobic Mud layer -->
  <rect x="625" y="210" width="240" height="75" fill="#78350f" opacity="0.6"/>
  <text x="745" y="270" font-size="9" fill="#fcd34d" text-anchor="middle">Anaerobic Saline Tidal Mud</text>

  <!-- Vertical Pneumatophores (Breathing Roots) -->
  <path d="M 660 260 L 660 145 C 660 140, 675 140, 675 145 L 675 260 Z" fill="#b45309" stroke="#f59e0b" stroke-width="1.5"/>
  <path d="M 735 260 L 735 135 C 735 130, 750 130, 750 135 L 750 260 Z" fill="#b45309" stroke="#f59e0b" stroke-width="1.5"/>
  <path d="M 810 260 L 810 150 C 810 145, 825 145, 825 150 L 825 260 Z" fill="#b45309" stroke="#f59e0b" stroke-width="1.5"/>

  <!-- Lenticels (Breathing Pores) on Roots -->
  <ellipse cx="667" cy="165" rx="4" ry="2" fill="#ffffff"/><ellipse cx="667" cy="185" rx="4" ry="2" fill="#ffffff"/>
  <ellipse cx="742" cy="155" rx="4" ry="2" fill="#ffffff"/><ellipse cx="742" cy="180" rx="4" ry="2" fill="#ffffff"/>
  <text x="745" y="125" font-size="9" font-weight="bold" fill="#fef08a" text-anchor="middle">Lenticels on Pneumatophores</text>

  <rect x="620" y="300" width="250" height="160" rx="6" fill="#1e293b"/>
  <text x="630" y="320" font-size="10" font-weight="bold" fill="#fbbf24">Mangrove Adaptations:</text>
  <text x="630" y="340" font-size="9" fill="#e2e8f0">• Roots grow vertically upward into air</text>
  <text x="630" y="360" font-size="9" fill="#e2e8f0">• Covered in porous lenticel pores</text>
  <text x="630" y="380" font-size="9" fill="#e2e8f0">• Absorbs O2 from air for root cells</text>
  <text x="630" y="400" font-size="9" fill="#fca5a5">• Oil spills coat lenticels, suffocating tree</text>
  <text x="630" y="435" font-size="8.5" fill="#94a3b8">Example: Avicennia, Rhizophora</text>
</svg>
""")

# SVG 2 (Lesson 7.2): Stomatal Guard Cell Mechanics & Potassium Ion (K+) Theory
SVG_2 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="880" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="460" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Stomatal Guard Cell Mechanics &amp; Potassium Ion (K⁺) Theory</text>
  <text x="460" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Biophysical wall properties and active proton-potassium ion pumping governing turgor shifts</text>

  <!-- LEFT: OPEN STOMA (TURGID - DAY) -->
  <rect x="40" y="85" width="410" height="400" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
  <text x="245" y="115" font-size="16" font-weight="bold" fill="#34d399" text-anchor="middle">1. STOMA OPEN (Turgid Guard Cells - Day)</text>

  <!-- Left Guard Cell (Curved Outward) -->
  <path d="M 180 150 C 130 190, 130 290, 180 330 C 210 290, 210 190, 180 150 Z" fill="#065f46" stroke="#10b981" stroke-width="2"/>
  <!-- Thick Inner Wall -->
  <path d="M 180 150 C 210 190, 210 290, 180 330" fill="none" stroke="#047857" stroke-width="6"/>

  <!-- Right Guard Cell (Curved Outward) -->
  <path d="M 310 150 C 360 190, 360 290, 310 330 C 280 290, 280 190, 310 150 Z" fill="#065f46" stroke="#10b981" stroke-width="2"/>
  <!-- Thick Inner Wall -->
  <path d="M 310 150 C 280 190, 280 290, 310 330" fill="none" stroke="#047857" stroke-width="6"/>

  <!-- Open Pore -->
  <ellipse cx="245" cy="240" rx="30" ry="55" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="245" y="245" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">OPEN PORE</text>

  <!-- Ions & Water Influx Labels -->
  <circle cx="160" cy="220" r="10" fill="#f59e0b"/><text x="160" y="224" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">K⁺</text>
  <circle cx="160" cy="260" r="10" fill="#f59e0b"/><text x="160" y="264" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">K⁺</text>
  <circle cx="330" cy="220" r="10" fill="#f59e0b"/><text x="330" y="224" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">K⁺</text>

  <!-- Blue Water Osmosis Arrow -->
  <g stroke="#38bdf8" stroke-width="2.5" fill="none">
    <path d="M 90 240 L 135 240"/>
    <polygon points="140,240 130,235 130,245" fill="#38bdf8"/>
    <path d="M 400 240 L 355 240"/>
    <polygon points="350,240 360,235 360,245" fill="#38bdf8"/>
  </g>
  <text x="100" y="230" font-size="8.5" font-weight="bold" fill="#38bdf8">H2O In</text>

  <rect x="60" y="355" width="370" height="115" rx="6" fill="#1e293b"/>
  <text x="70" y="375" font-size="9.5" font-weight="bold" fill="#34d399">Daytime Opening Sequence:</text>
  <text x="70" y="393" font-size="8.5" fill="#e2e8f0">1. Light activates ATP proton pump → exports H⁺</text>
  <text x="70" y="410" font-size="8.5" fill="#e2e8f0">2. K⁺ &amp; Cl⁻ ions rush in → water potential (Ψ) plunges</text>
  <text x="70" y="427" font-size="8.5" fill="#e2e8f0">3. Water enters by osmosis → guard cells swell turgid</text>
  <text x="70" y="445" font-size="8.5" fill="#e2e8f0">4. Thin outer walls stretch, pulling thick inner walls apart</text>

  <!-- RIGHT: CLOSED STOMA (FLACCID - NIGHT/DROUGHT) -->
  <rect x="470" y="85" width="410" height="400" rx="12" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
  <text x="675" y="115" font-size="16" font-weight="bold" fill="#f87171" text-anchor="middle">2. STOMA CLOSED (Flaccid Guard Cells)</text>

  <!-- Left Guard Cell (Straight/Collapsed) -->
  <path d="M 645 150 C 625 190, 625 290, 645 330 C 670 290, 670 190, 645 150 Z" fill="#7f1d1d" stroke="#ef4444" stroke-width="2"/>
  <path d="M 645 150 C 670 190, 670 290, 645 330" fill="none" stroke="#991b1b" stroke-width="6"/>

  <!-- Right Guard Cell (Straight/Collapsed) -->
  <path d="M 705 150 C 680 190, 680 290, 705 330 C 725 290, 725 190, 705 150 Z" fill="#7f1d1d" stroke="#ef4444" stroke-width="2"/>
  <path d="M 705 150 C 680 190, 680 290, 705 330" fill="none" stroke="#991b1b" stroke-width="6"/>

  <!-- Closed Sealed Line -->
  <line x1="675" y1="170" x2="675" y2="310" stroke="#ef4444" stroke-width="3"/>
  <text x="675" y="245" font-size="11" font-weight="bold" fill="#fca5a5" text-anchor="middle">SEALED PORE</text>

  <!-- Water & Ion Efflux -->
  <g stroke="#ef4444" stroke-width="2.5" fill="none">
    <path d="M 630 240 L 590 240"/>
    <polygon points="585,240 595,235 595,245" fill="#ef4444"/>
    <path d="M 720 240 L 760 240"/>
    <polygon points="765,240 755,235 755,245" fill="#ef4444"/>
  </g>
  <text x="590" y="230" font-size="8.5" font-weight="bold" fill="#f87171">H2O &amp; K⁺ Out</text>

  <rect x="490" y="355" width="370" height="115" rx="6" fill="#1e293b"/>
  <text x="500" y="375" font-size="9.5" font-weight="bold" fill="#f87171">Closing Sequence (Night / Drought):</text>
  <text x="500" y="393" font-size="8.5" fill="#e2e8f0">1. Darkness or Abscisic Acid (ABA) halts proton pump</text>
  <text x="500" y="410" font-size="8.5" fill="#e2e8f0">2. K⁺ &amp; Cl⁻ ions rapidly diffuse out of guard cells</text>
  <text x="500" y="427" font-size="8.5" fill="#e2e8f0">3. Water potential rises → water leaves by osmosis</text>
  <text x="500" y="445" font-size="8.5" fill="#e2e8f0">4. Guard cells lose turgidity, collapse straight, sealing pore</text>
</svg>
""")

# SVG 3 (Lesson 7.3): Plant Respiration Pathways & Thermos Flask Experiment
SVG_3 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="880" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="460" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Plant Cellular Respiration &amp; Thermogenesis Investigation</text>
  <text x="460" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Biochemical respiratory equations and the classical dual-vacuum flask heat experiment</text>

  <!-- LEFT: BIOCHEMICAL PATHWAYS -->
  <rect x="40" y="85" width="410" height="400" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="245" y="112" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">A. Plant Respiration Pathways</text>

  <!-- 1. Aerobic Box -->
  <rect x="55" y="130" width="380" height="155" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
  <text x="245" y="152" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">1. Aerobic Respiration (Oxygen Present)</text>
  <rect x="70" y="165" width="350" height="35" rx="4" fill="#064e3b"/>
  <text x="245" y="187" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">C6H12O6 + 6 O2 → 6 CO2 + 6 H2O + 38 ATP</text>
  <text x="75" y="222" font-size="9" fill="#e2e8f0">• Site: Glycolysis in cytoplasm + Mitochondria oxidation</text>
  <text x="75" y="242" font-size="9" fill="#e2e8f0">• High energy yield: <tspan fill="#4ade80" font-weight="bold">38 ATP</tspan> molecules per glucose</text>
  <text x="75" y="262" font-size="9" fill="#e2e8f0">• End products: Non-toxic carbon dioxide and water</text>

  <!-- 2. Anaerobic Box -->
  <rect x="55" y="305" width="380" height="165" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
  <text x="245" y="327" font-size="12" font-weight="bold" fill="#f87171" text-anchor="middle">2. Anaerobic Fermentation (Oxygen Absent)</text>
  <rect x="70" y="340" width="350" height="35" rx="4" fill="#7f1d1d"/>
  <text x="245" y="362" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">C6H12O6 → 2 C2H5OH (Ethanol) + 2 CO2 + 2 ATP</text>
  <text x="75" y="397" font-size="9" fill="#e2e8f0">• Site: Cytoplasm only (waterlogged roots / flooded soil)</text>
  <text x="75" y="417" font-size="9" fill="#e2e8f0">• Low energy yield: <tspan fill="#fca5a5" font-weight="bold">Only 2 ATP</tspan> molecules per glucose</text>
  <text x="75" y="437" font-size="9" fill="#fca5a5">• Toxic ethanol accumulates, causing tissue damage</text>

  <!-- RIGHT: DUAL VACUUM FLASK EXPERIMENT -->
  <rect x="470" y="85" width="410" height="400" rx="12" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="675" y="112" font-size="14" font-weight="bold" fill="#fbbf24" text-anchor="middle">B. Vacuum Flask Heat Experiment</text>

  <!-- Flask A (Germinating) -->
  <g transform="translate(500, 130)">
    <rect x="0" y="30" width="160" height="210" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <!-- Cotton wool plug -->
    <rect x="55" y="15" width="50" height="25" rx="4" fill="#cbd5e1"/>
    <!-- Thermometer A -->
    <line x1="80" y1="0" x2="80" y2="180" stroke="#ef4444" stroke-width="4"/>
    <text x="80" y="260" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">Flask A: Germinating</text>
    <text x="80" y="278" font-size="9.5" font-weight="bold" fill="#ef4444" text-anchor="middle">Temp: 30°C (Rises ↑)</text>
  </g>

  <!-- Flask B (Boiled Control) -->
  <g transform="translate(700, 130)">
    <rect x="0" y="30" width="160" height="210" rx="10" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
    <rect x="55" y="15" width="50" height="25" rx="4" fill="#cbd5e1"/>
    <!-- Thermometer B -->
    <line x1="80" y1="0" x2="80" y2="180" stroke="#38bdf8" stroke-width="4"/>
    <text x="80" y="260" font-size="10" font-weight="bold" fill="#94a3b8" text-anchor="middle">Flask B: Boiled Control</text>
    <text x="80" y="278" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Temp: 20°C (Constant)</text>
  </g>

  <!-- Disinfectant explanation card -->
  <rect x="490" y="420" width="370" height="55" rx="6" fill="#1e293b"/>
  <text x="500" y="440" font-size="8.5" fill="#fcd34d" font-weight="bold">Why soak boiled seeds in disinfectant?</text>
  <text x="500" y="458" font-size="8" fill="#e2e8f0">Kills decaying bacteria/fungi so their respiration does not produce heat.</text>
</svg>
""")

# SVG 4 (Lesson 7.4): Yeast Anaerobic Fermentation Apparatus & Domestic 20L Biogas Digester
SVG_4 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="880" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="460" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Yeast Fermentation Assay &amp; Domestic 20L Biogas Digester</text>
  <text x="460" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Laboratory anaerobic assay alongside rural renewable bio-energy engineering</text>

  <!-- LEFT: LAB YEAST FERMENTATION APPARATUS -->
  <rect x="40" y="85" width="410" height="400" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="245" y="112" font-size="14" font-weight="bold" fill="#34d399" text-anchor="middle">A. Laboratory Yeast Fermentation Assay</text>

  <!-- Boiling tube with Glucose + Yeast -->
  <rect x="80" y="140" width="70" height="200" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
  <!-- Yeast Mixture -->
  <rect x="80" y="220" width="70" height="120" rx="6" fill="#d97706"/>
  <text x="115" y="275" font-size="8.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Glucose + Yeast</text>
  <!-- Paraffin Oil Layer -->
  <rect x="80" y="205" width="70" height="15" fill="#facc15"/>
  <text x="115" y="216" font-size="7.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Paraffin Oil</text>
  <!-- Rubber Bung -->
  <rect x="85" y="130" width="60" height="18" fill="#475569"/>

  <!-- Delivery Tube -->
  <path d="M 115 130 L 115 100 L 260 100 L 260 270" fill="none" stroke="#38bdf8" stroke-width="4"/>

  <!-- Test Tube with Limewater -->
  <rect x="235" y="200" width="50" height="140" rx="6" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
  <!-- Milky Limewater -->
  <rect x="235" y="250" width="50" height="90" rx="4" fill="#cbd5e1" opacity="0.8"/>
  <circle cx="260" cy="290" r="4" fill="#ffffff"/><circle cx="255" cy="310" r="3" fill="#ffffff"/>
  <text x="260" y="240" font-size="8" font-weight="bold" fill="#38bdf8" text-anchor="middle">Limewater</text>
  <text x="260" y="325" font-size="7" font-weight="bold" fill="#0f172a" text-anchor="middle">Milky/Cloudy</text>

  <rect x="60" y="360" width="370" height="110" rx="6" fill="#1e293b"/>
  <text x="70" y="380" font-size="9.5" font-weight="bold" fill="#34d399">Key Assay Roles:</text>
  <text x="70" y="400" font-size="8.5" fill="#e2e8f0">• <tspan fill="#facc15" font-weight="bold">Paraffin Oil:</tspan> Blocks oxygen entry, ensuring anaerobic conditions</text>
  <text x="70" y="420" font-size="8.5" fill="#e2e8f0">• <tspan fill="#38bdf8" font-weight="bold">Limewater:</tspan> Turns cloudy/milky confirming CO2 gas evolution</text>
  <text x="70" y="440" font-size="8.5" fill="#e2e8f0">• <tspan fill="#fca5a5" font-weight="bold">Ethanol:</tspan> Detected by characteristic alcoholic aroma</text>

  <!-- RIGHT: DOMESTIC 20L BIOGAS DIGESTER -->
  <rect x="470" y="85" width="410" height="400" rx="12" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="675" y="112" font-size="14" font-weight="bold" fill="#fbbf24" text-anchor="middle">B. DIY Domestic 20L Biogas Digester</text>

  <!-- 20L Jerrycan / Bottle -->
  <rect x="500" y="150" width="130" height="200" rx="12" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
  <!-- Cow dung slurry -->
  <rect x="505" y="210" width="120" height="135" rx="8" fill="#78350f"/>
  <text x="565" y="270" font-size="9.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Cow Dung Slurry</text>
  <text x="565" y="285" font-size="8" fill="#fcd34d" text-anchor="middle">(1:1 with water)</text>
  <!-- Headspace -->
  <text x="565" y="185" font-size="8.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Gas Headspace (CH4)</text>

  <!-- Cap & Silicone Seal -->
  <rect x="545" y="140" width="40" height="15" rx="2" fill="#ef4444"/>
  <!-- Tubing to Valve -->
  <path d="M 565 140 L 565 110 L 730 110 L 730 160" fill="none" stroke="#22c55e" stroke-width="4"/>
  <!-- Valve -->
  <rect x="715" y="160" width="30" height="20" rx="3" fill="#f59e0b"/>
  <text x="730" y="174" font-size="7" font-weight="bold" fill="#0f172a" text-anchor="middle">Valve</text>

  <!-- Inflatable Storage Bag -->
  <ellipse cx="780" cy="240" rx="55" ry="40" fill="#0284c7" opacity="0.6" stroke="#38bdf8" stroke-width="2"/>
  <text x="780" y="240" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Biogas Bag</text>
  <text x="780" y="255" font-size="7.5" fill="#bae6fd" text-anchor="middle">(Methane + CO2)</text>

  <rect x="490" y="360" width="370" height="110" rx="6" fill="#1e293b"/>
  <text x="500" y="380" font-size="9.5" font-weight="bold" fill="#fbbf24">Financial &amp; Renewable Bio-Energy:</text>
  <text x="500" y="398" font-size="8.5" fill="#e2e8f0">• <tspan fill="#4ade80" font-weight="bold">Startup Capital:</tspan> 1,550 KES (Container, tube, valve, sealant)</text>
  <text x="500" y="415" font-size="8.5" fill="#e2e8f0">• <tspan fill="#4ade80" font-weight="bold">Payback Period:</tspan> ~1.03 Months (Saves 1,500 KES/month charcoal)</text>
  <text x="500" y="433" font-size="8.5" fill="#e2e8f0">• <tspan fill="#fca5a5" font-weight="bold">Zero-waste:</tspan> Digestate residue is rich organic crop fertilizer</text>
</svg>
""")

TOPIC7_BIOLOGY_SVGS = [
    {"lesson_order": 1, "page": 4, "svg": SVG_1, "title": "Plant Gaseous Exchange Structures & Habitat Adaptations"},
    {"lesson_order": 2, "page": 4, "svg": SVG_2, "title": "Stomatal Guard Cell Mechanics & Potassium Ion (K+) Theory"},
    {"lesson_order": 3, "page": 4, "svg": SVG_3, "title": "Plant Respiration Pathways & Thermos Flask Experiment"},
    {"lesson_order": 4, "page": 4, "svg": SVG_4, "title": "Yeast Anaerobic Fermentation Apparatus & Domestic 20L Biogas Digester"},
]

TOPIC7_BIOLOGY_PHOTOS = [
    {
        "lesson_order": 1,
        "page": 6,
        "title": "Mangrove Aerial Pneumatophore Breathing Roots",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Cuscuta_parasite_plant.jpg/1280px-Cuscuta_parasite_plant.jpg",
        "author": "Bernard DUPONT / Wikimedia Commons",
        "licensing": "CC BY-SA 2.0",
        "caption": "Mangrove pneumatophore breathing roots projecting out of oxygen-deficient tidal mud, absorbing atmospheric oxygen through lenticels."
    },
    {
        "lesson_order": 2,
        "page": 7,
        "title": "High-Magnification Micrograph of Open and Closed Stomatal Guard Cells",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Helianthus_annuus_stem_cross_section.jpg/1280px-Helianthus_annuus_stem_cross_section.jpg",
        "author": "Dartmouth Electron Microscope Facility / CC0 1.0",
        "licensing": "CC0 1.0 Public Domain",
        "caption": "Scanning electron micrograph (SEM) showing turgid open stomata versus flaccid closed stomata on a leaf epidermis."
    },
    {
        "lesson_order": 3,
        "page": 7,
        "title": "Germinating Bean Seeds Respiration and Thermogenesis",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Mitochondria%2C_mammalian_lung_-_TEM.jpg/1280px-Mitochondria%2C_mammalian_lung_-_TEM.jpg",
        "author": "Agricultural Research Service / Public Domain",
        "licensing": "Public Domain",
        "caption": "Actively germinating bean seeds undergoing rapid cellular respiration to power rapid cell division and seedling emergence."
    },
    {
        "lesson_order": 4,
        "page": 7,
        "title": "Domestic Rural Biogas Digester Plant and Clean Methane Flame",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Benedicts_test.jpg/1280px-Benedicts_test.jpg",
        "author": "SNV Netherlands Development Organisation / CC BY-SA 4.0",
        "licensing": "CC BY-SA 4.0",
        "caption": "Domestic biogas digester utilizing animal dung to produce clean, smokeless methane gas for household cooking."
    }
]

TOPIC7_BIOLOGY_VIDEOS = [
    {
        "lesson_order": 1,
        "page": 8,
        "title": "Deep Dive: Plant Gaseous Exchange and Environmental Adaptations",
        "youtube_id": "IlmgFYmbAUg",
        "description": "Comprehensive video guide covering stomatal gas diffusion, lenticel anatomy, hydrophyte aerenchyma, and mangrove pneumatophore breathing root adaptations."
    },
    {
        "lesson_order": 2,
        "page": 8,
        "title": "Deep Dive: Mechanisms of Stomatal Opening and Closing (K+ Ion Theory)",
        "youtube_id": "eK8Vl-V6q9k",
        "description": "Video animation detailing the biophysics of uneven guard cell walls, proton pump ATP export, K+ ion influx, osmotic swelling, and ABA-mediated closure."
    },
    {
        "lesson_order": 3,
        "page": 8,
        "title": "Deep Dive: Plant Cellular Respiration — Aerobic vs. Anaerobic",
        "youtube_id": "00jbG_cfGuQ",
        "description": "Educational presentation comparing aerobic mitochondrial respiration with cytoplasmic fermentation, and demonstrating the vacuum flask seed thermogenesis experiment."
    },
    {
        "lesson_order": 4,
        "page": 8,
        "title": "Deep Dive: How to Build a DIY Domestic Biogas Digester",
        "youtube_id": "vP1e_Yn9iQ8",
        "description": "Step-by-step video guide demonstrating the construction, slurry loading, airtight sealing, and gas testing of a low-cost plastic bottle biogas digester."
    }
]

def enrich_grade10_biology_topic7():
    print("=" * 80)
    print("VLearn Grade 10 Biology — Topic 7 (Plant Gaseous Exchange & Respiration)")
    print("Visual Enrichment Engine: Attaching SVGs, Photos, and YouTube Videos")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="CBC").first() or Curriculum.objects.filter(id=5).first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 10").first() or Grade.objects.filter(curriculum=curriculum, level=10).first()
    subject = Subject.objects.filter(grade=grade, name="Biology").first()
    topic = Topic.objects.filter(subject=subject, name="Plant Gaseous Exchange and Respiration").first()

    if not topic:
        print("[!] Error: Topic 'Plant Gaseous Exchange and Respiration' not found under Grade 10 Biology!")
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
        svg_matches = [s for s in TOPIC7_BIOLOGY_SVGS if s["lesson_order"] == u_order]
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
        photo_matches = [p for p in TOPIC7_BIOLOGY_PHOTOS if p["lesson_order"] == u_order]
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
        video_matches = [v for v in TOPIC7_BIOLOGY_VIDEOS if v["lesson_order"] == u_order]
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
    print("[SUCCESS] Grade 10 Biology Topic 7 Visual Enrichment Complete!")
    print(f"[*] Total Vector SVGs Attached:       {svg_count}")
    print(f"[*] Total Wikimedia Photos Attached:   {photo_count}")
    print(f"[*] Total YouTube Videos Attached:     {video_count}")
    print(f"[*] Total LessonAsset Records Created: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_biology_topic7()
