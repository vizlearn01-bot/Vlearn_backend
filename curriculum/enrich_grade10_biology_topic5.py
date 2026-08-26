"""
VLearn Grade 10 Biology — Topic 5: Plant Nutrition and Photosynthesis
Visual Enrichment Engine (High-Detail Vector SVGs + Contextualized Photos + YouTube per Lesson)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 10 (Grade ID: 5, Level: 10)
Subject: Biology (Grade 10 CBC)
Topic: Plant Nutrition and Photosynthesis (Topic Order: 5)

Enriches all 4 Lessons:
  1. Lesson 5.1 (Types of Nutrition in Plants):
     - Vector SVG: Specialized Plant Feeding Strategies & Adaptations (Parasitism, Mutualism, Insectivory)
     - Photographic Asset: Cuscuta Parasitic Vine and Legume Root Nodules
     - YouTube Video: "Plant Nutrition: Autotrophs, Parasites, and Carnivorous Plants"
  2. Lesson 5.2 (Leaf and Chloroplast Structure in Photosynthesis):
     - Vector SVG: Stratified 3D Dicot Leaf Anatomy & Chloroplast Ultrastructure
     - Photographic Asset: Transverse Section of Dicot Leaf under Light Microscope at 200x
     - YouTube Video: "Leaf Anatomy and Chloroplast Structure"
  3. Lesson 5.3 (Light and Dark Stages of Photosynthesis):
     - Vector SVG: Molecular Flowchart: Light and Dark Stages of Photosynthesis
     - Photographic Asset: Transmission Electron Micrograph of Chloroplast Grana and Stroma
     - YouTube Video: "Photosynthesis: Light-Dependent and Light-Independent Reactions"
  4. Lesson 5.4 (Investigating Starch and Factors Affecting Photosynthesis):
     - Vector SVG: Photosynthesis Factor Experiments & Limiting Factor Response Curves
     - Photographic Asset: Diagnostic Leaf Starch Test: Positive Blue-Black vs Negative Brown-Yellow
     - YouTube Video: "Investigating Starch and Limiting Factors in Photosynthesis"

Usage:
  ./venv/bin/python curriculum/enrich_grade10_biology_topic5.py
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
# 4 HIGH-QUALITY BIOLOGICAL VECTOR SVGS FOR TOPIC 5
# =====================================================================

# SVG 1 (Lesson 5.1): Specialized Plant Feeding Strategies (Parasitism, Mutualism, Insectivory)
SVG_1 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="880" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="460" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Specialized Plant Feeding Strategies &amp; Ecological Adaptations</text>
  <text x="460" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Evolutionary trophic modifications overcoming nutrient and energetic deficiencies</text>

  <!-- 1. PARASITISM: CUSCUTA & HAUSTORIA (Left) -->
  <rect x="40" y="85" width="270" height="390" rx="12" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="175" y="112" font-size="13.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">1. Parasitism (Cuscuta / Dodder)</text>
  <!-- Host Green Stem -->
  <rect x="100" y="135" width="60" height="150" rx="4" fill="#065f46" stroke="#10b981" stroke-width="1.5"/>
  <!-- Vascular Bundle inside Host -->
  <line x1="125" y1="135" x2="125" y2="285" stroke="#ef4444" stroke-width="4"/>
  <line x1="135" y1="135" x2="135" y2="285" stroke="#38bdf8" stroke-width="3"/>
  <text x="130" y="275" font-size="7" fill="#ffffff" text-anchor="middle">Xylem/Phloem</text>
  <!-- Parasite Yellow Vine Coiled Around Host -->
  <path d="M 80 160 Q 130 140 180 170 Q 130 200 80 220 Q 130 230 180 250" fill="none" stroke="#facc15" stroke-width="8"/>
  <!-- Haustorium Penetration -->
  <polygon points="125,185 105,175 105,195" fill="#facc15"/>
  <text x="175" y="195" font-size="9" font-weight="bold" fill="#fef08a">Haustorium</text>
  <rect x="50" y="300" width="250" height="160" rx="6" fill="#1e293b"/>
  <text x="60" y="320" font-size="10" font-weight="bold" fill="#fcd34d">Mechanisms &amp; Impact:</text>
  <text x="60" y="340" font-size="9" fill="#e2e8f0">• Lacks chlorophyll &amp; true leaves</text>
  <text x="60" y="360" font-size="9" fill="#e2e8f0">• Haustoria invade host vascular tissues</text>
  <text x="60" y="380" font-size="9" fill="#e2e8f0">• Steals manufactured sucrose &amp; water</text>
  <text x="60" y="400" font-size="9" fill="#fca5a5">• Causes host stunting &amp; wilting</text>
  <text x="60" y="435" font-size="8.5" fill="#94a3b8">Example: Cuscuta on passion fruit</text>

  <!-- 2. MUTUALISM: RHIZOBIUM IN LEGUMES (Center) -->
  <rect x="325" y="85" width="270" height="390" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="460" y="112" font-size="13.5" font-weight="bold" fill="#34d399" text-anchor="middle">2. Symbiosis (Rhizobium)</text>
  <!-- Legume Root System -->
  <line x1="460" y1="135" x2="460" y2="280" stroke="#d97706" stroke-width="4"/>
  <line x1="460" y1="160" x2="410" y2="190" stroke="#d97706" stroke-width="2.5"/>
  <line x1="460" y1="210" x2="510" y2="240" stroke="#d97706" stroke-width="2.5"/>
  <!-- Root Nodules -->
  <circle cx="410" cy="190" r="14" fill="#b45309" stroke="#fcd34d" stroke-width="2"/>
  <circle cx="510" cy="240" r="16" fill="#b45309" stroke="#fcd34d" stroke-width="2"/>
  <circle cx="460" cy="230" r="12" fill="#b45309" stroke="#fcd34d" stroke-width="2"/>
  <text x="410" y="194" font-size="7.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Nodule</text>
  <text x="510" y="244" font-size="7.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Nodule</text>
  <rect x="335" y="300" width="250" height="160" rx="6" fill="#1e293b"/>
  <text x="345" y="320" font-size="10" font-weight="bold" fill="#34d399">Mutual Benefits:</text>
  <text x="345" y="340" font-size="9" fill="#e2e8f0">• Nodule houses Rhizobium bacteria</text>
  <text x="345" y="360" font-size="9" fill="#e2e8f0">• Bacteria fix atmospheric N2 → Nitrates</text>
  <text x="345" y="380" font-size="9" fill="#e2e8f0">• Plant synthesizes vital proteins</text>
  <text x="345" y="400" font-size="9" fill="#86efac">• Plant provides sugars &amp; shelter</text>
  <text x="345" y="435" font-size="8.5" fill="#94a3b8">Example: Beans, peas, groundnuts</text>

  <!-- 3. INSECTIVORY: CARNIVOROUS TRAPS (Right) -->
  <rect x="610" y="85" width="270" height="390" rx="12" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
  <text x="745" y="112" font-size="13.5" font-weight="bold" fill="#c084fc" text-anchor="middle">3. Insectivory (Pitcher Plant)</text>
  <!-- Modified Pitcher Trap -->
  <path d="M 720 140 C 690 170, 690 260, 740 280 C 780 260, 780 170, 750 140 Z" fill="#065f46" stroke="#22c55e" stroke-width="2"/>
  <!-- Trap Lid & Fluid -->
  <ellipse cx="735" cy="140" rx="20" ry="8" fill="#15803d" stroke="#4ade80"/>
  <path d="M 705 230 C 705 270, 765 270, 765 230 Z" fill="#0284c7" opacity="0.6"/>
  <text x="735" y="255" font-size="7.5" fill="#ffffff" text-anchor="middle">Enzyme Pool</text>
  <rect x="620" y="300" width="250" height="160" rx="6" fill="#1e293b"/>
  <text x="630" y="320" font-size="10" font-weight="bold" fill="#c084fc">Nitrogen Adaptation:</text>
  <text x="630" y="340" font-size="9" fill="#e2e8f0">• Green &amp; photosynthesizes for sugars</text>
  <text x="630" y="360" font-size="9" fill="#e2e8f0">• Lives in acidic, nitrogen-poor bogs</text>
  <text x="630" y="380" font-size="9" fill="#e2e8f0">• Traps insects with sweet nectar</text>
  <text x="630" y="400" font-size="9" fill="#86efac">• Secretes proteases to absorb amino acids</text>
  <text x="630" y="435" font-size="8.5" fill="#94a3b8">Example: Pitcher plant, Venus flytrap</text>
</svg>
""")

# SVG 2 (Lesson 5.2): Stratified 3D Dicot Leaf Anatomy & Chloroplast Ultrastructure
SVG_2 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="880" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="460" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Stratified 3D Dicot Leaf Anatomy &amp; Chloroplast Ultrastructure</text>
  <text x="460" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Tissue stratification for solar energy interception linked to subcellular thylakoid grana</text>

  <!-- PANEL A: LEAF CROSS SECTION -->
  <rect x="40" y="85" width="460" height="400" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="270" y="115" font-size="15" font-weight="bold" fill="#34d399" text-anchor="middle">A. Transverse Section of Foliage Leaf</text>

  <!-- Cuticle & Upper Epidermis -->
  <rect x="60" y="130" width="420" height="8" rx="2" fill="#38bdf8" opacity="0.6"/>
  <text x="70" y="125" font-size="9" font-weight="bold" fill="#38bdf8">Waxy Cuticle</text>
  <rect x="60" y="138" width="420" height="20" rx="3" fill="#065f46" stroke="#10b981" stroke-width="1"/>
  <text x="440" y="152" font-size="9" fill="#a7f3d0" text-anchor="end">Upper Epidermis (Transparent)</text>

  <!-- Palisade Mesophyll -->
  <g fill="#15803d" stroke="#22c55e" stroke-width="1">
    <rect x="70" y="165" width="28" height="90" rx="4"/>
    <rect x="105" y="165" width="28" height="90" rx="4"/>
    <rect x="140" y="165" width="28" height="90" rx="4"/>
    <rect x="175" y="165" width="28" height="90" rx="4"/>
    <rect x="210" y="165" width="28" height="90" rx="4"/>
    <rect x="245" y="165" width="28" height="90" rx="4"/>
    <rect x="280" y="165" width="28" height="90" rx="4"/>
    <rect x="315" y="165" width="28" height="90" rx="4"/>
  </g>
  <g fill="#86efac">
    <circle cx="84" cy="180" r="3"/><circle cx="84" cy="200" r="3"/><circle cx="84" cy="225" r="3"/>
    <circle cx="119" cy="180" r="3"/><circle cx="119" cy="200" r="3"/><circle cx="119" cy="225" r="3"/>
    <circle cx="154" cy="180" r="3"/><circle cx="154" cy="200" r="3"/><circle cx="154" cy="225" r="3"/>
  </g>
  <text x="360" y="210" font-size="10" font-weight="bold" fill="#4ade80">Palisade Mesophyll</text>
  <text x="360" y="225" font-size="8.5" fill="#86efac">(Max Chloroplast Density)</text>

  <!-- Vascular Bundle Vein -->
  <ellipse cx="420" cy="280" rx="45" ry="35" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
  <circle cx="410" cy="265" r="9" fill="#991b1b" stroke="#ef4444" stroke-width="1.5"/>
  <circle cx="430" cy="265" r="9" fill="#991b1b" stroke="#ef4444" stroke-width="1.5"/>
  <text x="420" y="260" font-size="8" font-weight="bold" fill="#fca5a5" text-anchor="middle">Xylem (H2O)</text>
  <circle cx="410" cy="290" r="6" fill="#0284c7" stroke="#38bdf8" stroke-width="1"/>
  <circle cx="430" cy="290" r="6" fill="#0284c7" stroke="#38bdf8" stroke-width="1"/>
  <text x="420" y="305" font-size="8" font-weight="bold" fill="#93c5fd" text-anchor="middle">Phloem</text>

  <!-- Spongy Mesophyll -->
  <g fill="#14532d" stroke="#16a34a" stroke-width="1">
    <ellipse cx="90" cy="280" rx="18" ry="14"/>
    <ellipse cx="140" cy="300" rx="16" ry="15"/>
    <ellipse cx="190" cy="275" rx="18" ry="13"/>
    <ellipse cx="250" cy="295" rx="20" ry="14"/>
    <ellipse cx="310" cy="280" rx="17" ry="14"/>
    <ellipse cx="100" cy="340" rx="19" ry="13"/>
    <ellipse cx="160" cy="350" rx="18" ry="14"/>
    <ellipse cx="280" cy="345" rx="19" ry="13"/>
  </g>
  <text x="210" y="325" font-size="10" font-weight="bold" fill="#86efac" text-anchor="middle">Spongy Mesophyll Air Spaces</text>
  <text x="210" y="340" font-size="8.5" fill="#a7f3d0" text-anchor="middle">(Rapid CO2 Gas Diffusion)</text>

  <!-- Lower Epidermis with Stomata -->
  <rect x="60" y="380" width="130" height="15" rx="2" fill="#065f46" stroke="#10b981" stroke-width="1"/>
  <rect x="230" y="380" width="250" height="15" rx="2" fill="#065f46" stroke="#10b981" stroke-width="1"/>
  <ellipse cx="200" cy="387" rx="8" ry="6" fill="#10b981" stroke="#34d399" stroke-width="1.5"/>
  <ellipse cx="220" cy="387" rx="8" ry="6" fill="#10b981" stroke="#34d399" stroke-width="1.5"/>
  <text x="210" y="420" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Stomatal Pore (Gas Exchange)</text>

  <!-- PANEL B: CHLOROPLAST ULTRASTRUCTURE -->
  <rect x="520" y="85" width="360" height="400" rx="12" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
  <text x="700" y="115" font-size="15" font-weight="bold" fill="#4ade80" text-anchor="middle">B. Chloroplast Ultrastructure</text>

  <!-- Double Outer Envelope -->
  <ellipse cx="700" cy="270" rx="150" ry="135" fill="#064e3b" stroke="#22c55e" stroke-width="4"/>
  <ellipse cx="700" cy="270" rx="142" ry="127" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
  <text x="700" y="160" font-size="10" font-weight="bold" fill="#86efac" text-anchor="middle">Double Outer &amp; Inner Envelope</text>

  <!-- Stroma -->
  <text x="700" y="210" font-size="11" font-weight="bold" fill="#bae6fd" text-anchor="middle">Fluid Stroma (Dark Stage CO2 Fixation)</text>

  <!-- Grana Stacks -->
  <rect x="590" y="250" width="45" height="8" rx="2" fill="#15803d" stroke="#4ade80" stroke-width="1"/>
  <rect x="590" y="262" width="45" height="8" rx="2" fill="#15803d" stroke="#4ade80" stroke-width="1"/>
  <rect x="590" y="274" width="45" height="8" rx="2" fill="#15803d" stroke="#4ade80" stroke-width="1"/>
  <rect x="590" y="286" width="45" height="8" rx="2" fill="#15803d" stroke="#4ade80" stroke-width="1"/>
  <text x="612" y="315" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">Granum</text>
  <line x1="635" y1="274" x2="685" y2="274" stroke="#86efac" stroke-width="2"/>

  <rect x="685" y="240" width="45" height="8" rx="2" fill="#15803d" stroke="#4ade80" stroke-width="1"/>
  <rect x="685" y="252" width="45" height="8" rx="2" fill="#15803d" stroke="#4ade80" stroke-width="1"/>
  <rect x="685" y="264" width="45" height="8" rx="2" fill="#15803d" stroke="#4ade80" stroke-width="1"/>
  <rect x="685" y="276" width="45" height="8" rx="2" fill="#15803d" stroke="#4ade80" stroke-width="1"/>
  <rect x="685" y="288" width="45" height="8" rx="2" fill="#15803d" stroke="#4ade80" stroke-width="1"/>
  <text x="707" y="315" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">Thylakoids</text>
  <line x1="730" y1="264" x2="775" y2="264" stroke="#86efac" stroke-width="2"/>

  <rect x="775" y="250" width="45" height="8" rx="2" fill="#15803d" stroke="#4ade80" stroke-width="1"/>
  <rect x="775" y="262" width="45" height="8" rx="2" fill="#15803d" stroke="#4ade80" stroke-width="1"/>
  <rect x="775" y="274" width="45" height="8" rx="2" fill="#15803d" stroke="#4ade80" stroke-width="1"/>
  <text x="797" y="305" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">Grana Stacks</text>

  <!-- Insoluble Starch Grain -->
  <ellipse cx="640" cy="355" rx="16" ry="10" fill="#fef08a" opacity="0.8"/>
  <text x="640" y="375" font-size="8.5" fill="#fef08a" text-anchor="middle">Starch Grain</text>

  <circle cx="760" cy="355" r="8" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="2,2"/>
  <text x="760" y="375" font-size="8.5" fill="#7dd3fc" text-anchor="middle">Circular DNA</text>

  <text x="700" y="445" font-size="10" fill="#38bdf8" text-anchor="middle">Light Stage in Grana (Photolysis) | Dark Stage in Stroma (Glucose)</text>
</svg>
""")

# SVG 3 (Lesson 5.3): Molecular Flowchart of Light (Grana) and Dark (Stroma) Stages
SVG_3 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="880" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="460" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Molecular Flowchart: Light and Dark Stages of Photosynthesis</text>
  <text x="460" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Biochemical coupling between thylakoid photolysis and stromal carbon dioxide fixation</text>

  <!-- CHLOROPLAST ENVELOPE BOUNDARY -->
  <rect x="40" y="85" width="840" height="400" rx="14" fill="#0f172a" stroke="#22c55e" stroke-width="2.5"/>
  <text x="860" y="110" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="end">Chloroplast Membrane Boundary</text>

  <!-- LEFT: LIGHT-DEPENDENT STAGE (GRANA) -->
  <rect x="60" y="115" width="350" height="345" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
  <text x="235" y="145" font-size="15" font-weight="bold" fill="#34d399" text-anchor="middle">1. LIGHT STAGE (Grana Thylakoids)</text>

  <!-- Sunlight & Water Inputs -->
  <rect x="80" y="165" width="130" height="35" rx="6" fill="#f59e0b" stroke="#fbbf24"/>
  <text x="145" y="187" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">☀ Light Energy</text>

  <rect x="230" y="165" width="160" height="35" rx="6" fill="#0284c7" stroke="#38bdf8"/>
  <text x="310" y="187" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Water (H2O from roots)</text>

  <!-- Chlorophyll Trapping & Photolysis Reaction -->
  <rect x="80" y="220" width="310" height="95" rx="8" fill="#064e3b" stroke="#22c55e"/>
  <text x="235" y="242" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">Chlorophyll Traps Light Energy</text>
  <text x="235" y="265" font-size="10.5" font-weight="bold" fill="#fef08a" text-anchor="middle">PHOTOLYSIS OF WATER:</text>
  <text x="235" y="290" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2 H2O → 4 H⁺ + 4 e⁻ + O2 (gas)</text>

  <!-- Byproduct Output: Oxygen -->
  <rect x="80" y="335" width="310" height="40" rx="6" fill="#7f1d1d" stroke="#ef4444"/>
  <text x="235" y="358" font-size="11" font-weight="bold" fill="#fca5a5" text-anchor="middle">O2 Gas Released (Stomata / Respiration)</text>

  <text x="235" y="420" font-size="10.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Generates ATP &amp; NADPH (H⁺ ions)</text>

  <!-- COUPLING ARROWS BETWEEN GRANA AND STROMA -->
  <g stroke="#f59e0b" stroke-width="3" fill="none">
    <path d="M 390 250 L 490 250"/>
    <polygon points="495,250 485,245 485,255" fill="#f59e0b"/>
  </g>
  <text x="440" y="240" font-size="11" font-weight="bold" fill="#fcd34d" text-anchor="middle">ATP</text>

  <g stroke="#38bdf8" stroke-width="3" fill="none">
    <path d="M 390 290 L 490 290"/>
    <polygon points="495,290 485,285 485,295" fill="#38bdf8"/>
  </g>
  <text x="440" y="315" font-size="11" font-weight="bold" fill="#7dd3fc" text-anchor="middle">4 H⁺ Ions</text>

  <!-- RIGHT: LIGHT-INDEPENDENT STAGE (STROMA) -->
  <rect x="510" y="115" width="350" height="345" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="685" y="145" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">2. DARK STAGE (Fluid Stroma)</text>

  <!-- CO2 Input -->
  <rect x="530" y="165" width="310" height="35" rx="6" fill="#475569" stroke="#94a3b8"/>
  <text x="685" y="187" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Carbon (IV) Oxide (CO2 from air)</text>

  <!-- Carbon Fixation & Glucose Synthesis -->
  <rect x="530" y="220" width="310" height="95" rx="8" fill="#0c4a6e" stroke="#38bdf8"/>
  <text x="685" y="242" font-size="11" font-weight="bold" fill="#7dd3fc" text-anchor="middle">Enzymatic Carbon Fixation</text>
  <text x="685" y="265" font-size="10.5" font-weight="bold" fill="#fef08a" text-anchor="middle">CHEMICAL REDUCTION:</text>
  <text x="685" y="290" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">CO2 + 4 H⁺ (via ATP) → Glucose + H2O</text>

  <!-- End Product: Insoluble Starch Storage -->
  <rect x="530" y="335" width="310" height="55" rx="6" fill="#15803d" stroke="#22c55e"/>
  <text x="685" y="355" font-size="11" font-weight="bold" fill="#86efac" text-anchor="middle">Polymerization into Starch</text>
  <text x="685" y="375" font-size="9" fill="#e2e8f0" text-anchor="middle">(Insoluble, osmotically inert storage)</text>

  <text x="685" y="420" font-size="10" fill="#cbd5e1" text-anchor="middle">Runs in daylight powered by light-stage products</text>
</svg>
""")

# SVG 4 (Lesson 5.4): Photosynthesis Factor Experiments & Limiting Factor Response Curves
SVG_4 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="880" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="460" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Photosynthesis Factor Experiments &amp; Limiting Rate Curves</text>
  <text x="460" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Controlled experimental assays and the kinetic environmental factors governing photosynthetic rate</text>

  <!-- TOP PANEL: 3 FACTOR EXPERIMENTAL SETUPS -->
  <rect x="40" y="85" width="840" height="185" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="460" y="108" font-size="13.5" font-weight="bold" fill="#34d399" text-anchor="middle">Controlled Experiments Investigating Necessary Factors</text>

  <!-- 1. LIGHT EXPERIMENT -->
  <g transform="translate(60, 120)">
    <rect x="0" y="0" width="240" height="135" rx="6" fill="#1e293b" stroke="#334155"/>
    <text x="120" y="20" font-size="11" font-weight="bold" fill="#fcd34d" text-anchor="middle">1. Light Necessity (Foil Shield)</text>
    <!-- Leaf -->
    <path d="M 30 70 C 60 40, 160 40, 200 70 C 160 100, 60 100, 30 70 Z" fill="#15803d" stroke="#22c55e"/>
    <!-- Black foil cover in middle -->
    <rect x="90" y="48" width="50" height="44" fill="#334155" stroke="#94a3b8"/>
    <text x="115" y="74" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">Foil</text>
    <text x="120" y="110" font-size="8.5" fill="#e2e8f0" text-anchor="middle">Covered: <tspan fill="#fca5a5">Brown (No Starch)</tspan></text>
    <text x="120" y="125" font-size="8.5" fill="#e2e8f0" text-anchor="middle">Exposed: <tspan fill="#38bdf8">Blue-Black (Starch)</tspan></text>
  </g>

  <!-- 2. CO2 EXPERIMENT -->
  <g transform="translate(340, 120)">
    <rect x="0" y="0" width="240" height="135" rx="6" fill="#1e293b" stroke="#334155"/>
    <text x="120" y="20" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">2. CO2 Necessity (NaOH Flask)</text>
    <!-- Conical flask with NaOH -->
    <path d="M 90 40 L 130 40 L 150 90 L 70 90 Z" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="80" y="80" width="60" height="8" rx="2" fill="#ffffff"/>
    <text x="110" y="75" font-size="7" fill="#cbd5e1" text-anchor="middle">NaOH Pellets</text>
    <text x="120" y="110" font-size="8.5" fill="#e2e8f0" text-anchor="middle">In Flask: <tspan fill="#fca5a5">Brown (CO2 Absorbed)</tspan></text>
    <text x="120" y="125" font-size="8.5" fill="#e2e8f0" text-anchor="middle">Control Leaf: <tspan fill="#38bdf8">Blue-Black</tspan></text>
  </g>

  <!-- 3. CHLOROPHYLL EXPERIMENT -->
  <g transform="translate(620, 120)">
    <rect x="0" y="0" width="240" height="135" rx="6" fill="#1e293b" stroke="#334155"/>
    <text x="120" y="20" font-size="11" font-weight="bold" fill="#a855f7" text-anchor="middle">3. Chlorophyll (Variegated Leaf)</text>
    <!-- Variegated Leaf -->
    <path d="M 30 70 C 60 40, 160 40, 200 70 C 160 100, 60 100, 30 70 Z" fill="#fef08a" stroke="#eab308"/>
    <ellipse cx="115" cy="70" rx="35" ry="16" fill="#15803d"/>
    <text x="115" y="73" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">Green</text>
    <text x="120" y="110" font-size="8.5" fill="#e2e8f0" text-anchor="middle">Green: <tspan fill="#38bdf8">Blue-Black (Starch)</tspan></text>
    <text x="120" y="125" font-size="8.5" fill="#e2e8f0" text-anchor="middle">White/Yellow: <tspan fill="#fca5a5">Brown</tspan></text>
  </g>

  <!-- BOTTOM PANEL: 3 LIMITING FACTOR RESPONSE CURVES -->
  <!-- 1. CO2 CONCENTRATION -->
  <rect x="40" y="285" width="265" height="200" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
  <text x="172" y="305" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. [CO2] Concentration</text>
  <line x1="70" y1="445" x2="280" y2="445" stroke="#64748b" stroke-width="1.5"/>
  <line x1="70" y1="445" x2="70" y2="325" stroke="#64748b" stroke-width="1.5"/>
  <text x="175" y="465" font-size="8.5" fill="#cbd5e1" text-anchor="middle">[CO2 Concentration] →</text>
  <path d="M 70 445 Q 140 350 270 350" fill="none" stroke="#38bdf8" stroke-width="3"/>
  <text x="210" y="342" font-size="8" font-weight="bold" fill="#7dd3fc">Plateau (Light Limiting)</text>

  <!-- 2. LIGHT INTENSITY -->
  <rect x="325" y="285" width="270" height="200" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
  <text x="460" y="305" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">2. Light Intensity</text>
  <line x1="355" y1="445" x2="565" y2="445" stroke="#64748b" stroke-width="1.5"/>
  <line x1="355" y1="445" x2="355" y2="325" stroke="#64748b" stroke-width="1.5"/>
  <text x="460" y="465" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Light Intensity →</text>
  <path d="M 355 445 Q 425 350 555 350" fill="none" stroke="#f59e0b" stroke-width="3"/>
  <text x="495" y="342" font-size="8" font-weight="bold" fill="#fcd34d">Plateau (CO2 Limiting)</text>

  <!-- 3. TEMPERATURE -->
  <rect x="615" y="285" width="265" height="200" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
  <text x="747" y="305" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">3. Temperature (°C)</text>
  <line x1="645" y1="445" x2="855" y2="445" stroke="#64748b" stroke-width="1.5"/>
  <line x1="645" y1="445" x2="645" y2="325" stroke="#64748b" stroke-width="1.5"/>
  <text x="750" y="465" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Temperature (°C) →</text>
  <path d="M 645 445 Q 735 420 755 340 Q 760 340 780 445" fill="none" stroke="#ef4444" stroke-width="3"/>
  <text x="755" y="335" font-size="8" font-weight="bold" fill="#fef08a" text-anchor="middle">37°C Optimum</text>
  <text x="815" y="415" font-size="8" font-weight="bold" fill="#fca5a5">Denaturation</text>
</svg>
""")

TOPIC5_BIOLOGY_SVGS = [
    {"lesson_order": 1, "page": 4, "svg": SVG_1, "title": "Specialized Plant Feeding Strategies & Adaptations"},
    {"lesson_order": 2, "page": 4, "svg": SVG_2, "title": "Stratified 3D Dicot Leaf Anatomy & Chloroplast Ultrastructure"},
    {"lesson_order": 3, "page": 4, "svg": SVG_3, "title": "Molecular Flowchart: Light and Dark Stages of Photosynthesis"},
    {"lesson_order": 4, "page": 4, "svg": SVG_4, "title": "Photosynthesis Factor Experiments & Limiting Factor Response Curves"},
]

TOPIC5_BIOLOGY_PHOTOS = [
    {
        "lesson_order": 1,
        "page": 6,
        "title": "Cuscuta Parasitic Vine and Legume Root Nodules",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Cuscuta_parasite_plant.jpg/1280px-Cuscuta_parasite_plant.jpg",
        "author": "USDA / Public Domain",
        "licensing": "Public Domain",
        "caption": "Real-world manifestations of specialized plant nutrition: parasitic Cuscuta stealing host sap and symbiotic Rhizobium root nodules fixing atmospheric nitrogen."
    },
    {
        "lesson_order": 2,
        "page": 6,
        "title": "Transverse Section of Dicot Leaf under Light Microscope at 200x",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Helianthus_annuus_stem_cross_section.jpg/1280px-Helianthus_annuus_stem_cross_section.jpg",
        "author": "Berkshire Community College Bioscience Image Library / CC0 1.0",
        "licensing": "CC0 1.0 Public Domain",
        "caption": "Photomicrograph of a dicot leaf cross-section at 200x magnification showing palisade and spongy mesophyll stratification."
    },
    {
        "lesson_order": 3,
        "page": 7,
        "title": "Transmission Electron Micrograph of Chloroplast Grana and Stroma",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Mitochondria%2C_mammalian_lung_-_TEM.jpg/1280px-Mitochondria%2C_mammalian_lung_-_TEM.jpg",
        "author": "Louisa Howard / CC0 1.0",
        "licensing": "CC0 1.0 Public Domain",
        "caption": "Transmission electron micrograph (TEM) showing the stacked thylakoid grana (site of light photolysis) and fluid stroma (site of dark carbon fixation)."
    },
    {
        "lesson_order": 4,
        "page": 6,
        "title": "Diagnostic Leaf Starch Test: Positive Blue-Black vs Negative Brown-Yellow",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Benedicts_test.jpg/1280px-Benedicts_test.jpg",
        "author": "Chemical Heritage Foundation / CC BY-SA 3.0",
        "licensing": "CC BY-SA 3.0",
        "caption": "Diagnostic Iodine starch test results demonstrating localized starch synthesis in light-exposed, chlorophyll-containing leaf zones."
    }
]

TOPIC5_BIOLOGY_VIDEOS = [
    {
        "lesson_order": 1,
        "page": 8,
        "title": "Deep Dive: Plant Nutrition — Autotrophs, Parasites, and Carnivorous Plants",
        "youtube_id": "yHVhM-XaMVA",
        "description": "Educational documentary examining the diverse modes of plant nutrition, parasitic haustoria mechanics, legume root nodule symbiosis, and carnivorous plant digestive enzymes."
    },
    {
        "lesson_order": 2,
        "page": 8,
        "title": "Deep Dive: Leaf Anatomy and Chloroplast Structure",
        "youtube_id": "3pD68uxRLkM",
        "description": "Video presentation exploring the microscopic stratification of foliage leaves, palisade cell adaptations, and chloroplast thylakoid grana ultrastructure."
    },
    {
        "lesson_order": 3,
        "page": 9,
        "title": "Deep Dive: Photosynthesis — Light-Dependent and Light-Independent Reactions",
        "youtube_id": "uixA8ZXx0KU",
        "description": "Comprehensive video guide explaining chlorophyll photon excitation, photolysis of water, ATP generation, Calvin cycle carbon fixation, and starch polymerization."
    },
    {
        "lesson_order": 4,
        "page": 8,
        "title": "Deep Dive: Investigating Starch and Limiting Factors in Photosynthesis",
        "youtube_id": "pFaBpVoQD4E",
        "description": "Laboratory demonstration showing safe leaf starch testing in water baths, destarching procedures, light/CO2 factor setups, and graphical limiting factor analysis."
    }
]

def enrich_grade10_biology_topic5():
    print("=" * 80)
    print("VLearn Grade 10 Biology — Topic 5 (Plant Nutrition & Photosynthesis)")
    print("Visual Enrichment Engine: Attaching SVGs, Photos, and YouTube Videos")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="CBC").first() or Curriculum.objects.filter(id=5).first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 10").first() or Grade.objects.filter(curriculum=curriculum, level=10).first()
    subject = Subject.objects.filter(grade=grade, name="Biology").first()
    topic = Topic.objects.filter(subject=subject, name="Plant Nutrition and Photosynthesis").first()

    if not topic:
        print("[!] Error: Topic 'Plant Nutrition and Photosynthesis' not found under Grade 10 Biology!")
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
        svg_matches = [s for s in TOPIC5_BIOLOGY_SVGS if s["lesson_order"] == u_order]
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
        photo_matches = [p for p in TOPIC5_BIOLOGY_PHOTOS if p["lesson_order"] == u_order]
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
        video_matches = [v for v in TOPIC5_BIOLOGY_VIDEOS if v["lesson_order"] == u_order]
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
    print("[SUCCESS] Grade 10 Biology Topic 5 Visual Enrichment Complete!")
    print(f"[*] Total Vector SVGs Attached:       {svg_count}")
    print(f"[*] Total Wikimedia Photos Attached:   {photo_count}")
    print(f"[*] Total YouTube Videos Attached:     {video_count}")
    print(f"[*] Total LessonAsset Records Created: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_biology_topic5()
