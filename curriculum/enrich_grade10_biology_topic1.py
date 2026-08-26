"""
VLearn Grade 10 Biology — Topic 1: Cell Biology and Biodiversity
Visual Enrichment Engine (Meaningful Biological Illustrations + Contextualized Photos + YouTube per Lesson)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 10 (Grade ID: 5, Level: 10)
Subject: Biology (Grade 10 CBC)
Topic: Cell Biology and Biodiversity (Topic Order: 1)

Enriches all 4 Lessons:
  1. Lesson 1.1 (Introduction to Biology):
     - Photographic Asset: Kenyan Savanna Ecosystem vs Cell Culture Laboratory
     - Vector SVG: Multi-disciplinary Overlapping Venn Diagram & Career Pathways
     - YouTube Video: "Introduction to Biology, Branches, and Scientific Careers"
  2. Lesson 1.2 (Scientific Investigations & Preservation):
     - Vector SVG: Detailed Mechanical Engineering Schematic (Pooter Airflow & Pitfall Soil Cross-Section)
     - Photographic Asset: Museum-Grade Herbarium Sheet with Metadata
     - YouTube Video: "Field Sampling Techniques, Pooters, and Herbarium Preservation"
  3. Lesson 1.3 (Cell Structure and Specialization):
     - Photographic Asset: 400x Light Micrograph of Onion Epidermal Cells Stained with Iodine
     - Vector SVG: High-Detail Eukaryotic Ultrastructure (Plant Cell vs Animal Cell with Color-Coded Organelles)
     - YouTube Video: "Eukaryotic Cell Structure, Organelles, and Microscopic Slide Preparation"
  4. Lesson 1.4 (Chemicals of Life):
     - Photographic Asset: Diagnostic Food Test Colors (Benedict's Brick-Red Precipitate)
     - Vector SVG: Multi-Panel Lock-and-Key Mechanism + 3 Kinetic Response Curves (Temp, pH, Substrate)
     - YouTube Video: "Enzymes, Catalase Breakdown, and Biochemical Food Tests"

Usage:
  ./venv/bin/python curriculum/enrich_grade10_biology_topic1.py
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
# 4 MEANINGFUL, HIGH-QUALITY VECTOR SVGS FOR GRADE 10 BIOLOGY TOPIC 1
# =====================================================================

# SVG 1 (Lesson 1.1): Multi-disciplinary Overlapping Venn Diagram of Biological Fields & Careers
SVG_1 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 500" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); font-family: system-ui, -apple-system, sans-serif;">
  <defs>
    <linearGradient id="botanyGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#10b981" stop-opacity="0.15"/>
    </linearGradient>
    <linearGradient id="zoologyGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#f59e0b" stop-opacity="0.15"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Title Header -->
  <rect x="20" y="15" width="860" height="470" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="450" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Multi-Disciplinary Structure of Biology &amp; Professional Career Pathways</text>
  <text x="450" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">How classical foundational pillars intersect into modern specialized fields and career opportunities</text>

  <!-- Left Venn Circle: Botany -->
  <ellipse cx="300" cy="190" rx="190" ry="115" fill="url(#botanyGrad)" stroke="#10b981" stroke-width="2.5"/>
  <text x="185" y="125" font-size="18" font-weight="bold" fill="#34d399">BOTANY</text>
  <text x="185" y="145" font-size="11" fill="#a7f3d0">Scientific Study of Plants</text>
  <text x="185" y="180" font-size="11" fill="#e2e8f0">• Plant Morphology</text>
  <text x="185" y="200" font-size="11" fill="#e2e8f0">• Plant Physiology</text>
  <text x="185" y="220" font-size="11" fill="#e2e8f0">• Agronomy &amp; Forestry</text>

  <!-- Right Venn Circle: Zoology -->
  <ellipse cx="600" cy="190" rx="190" ry="115" fill="url(#zoologyGrad)" stroke="#f59e0b" stroke-width="2.5"/>
  <text x="715" y="125" font-size="18" font-weight="bold" fill="#fbbf24">ZOOLOGY</text>
  <text x="715" y="145" font-size="11" fill="#fde68a">Scientific Study of Animals</text>
  <text x="715" y="180" font-size="11" fill="#e2e8f0">• Animal Morphology</text>
  <text x="715" y="200" font-size="11" fill="#e2e8f0">• Ethology (Behavior)</text>
  <text x="715" y="220" font-size="11" fill="#e2e8f0">• Wildlife Management</text>

  <!-- Intersecting Central Core: Specialized Interdisciplinary Fields -->
  <rect x="360" y="105" width="180" height="170" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <text x="450" y="125" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">INTERSECTING FIELDS</text>
  <line x1="375" y1="132" x2="525" y2="132" stroke="#334155" stroke-width="1"/>
  <text x="450" y="150" font-size="10.5" fill="#f8fafc" text-anchor="middle">• Microbiology &amp; Virology</text>
  <text x="450" y="168" font-size="10.5" fill="#f8fafc" text-anchor="middle">• Genetics &amp; DNA Biotech</text>
  <text x="450" y="186" font-size="10.5" fill="#f8fafc" text-anchor="middle">• Ecology &amp; Conservation</text>
  <text x="450" y="204" font-size="10.5" fill="#f8fafc" text-anchor="middle">• Anatomy &amp; Physiology</text>
  <text x="450" y="222" font-size="10.5" fill="#f8fafc" text-anchor="middle">• Biochemistry &amp; Enzymes</text>
  <text x="450" y="240" font-size="10.5" fill="#f8fafc" text-anchor="middle">• Parasitology &amp; Entomology</text>
  <text x="450" y="258" font-size="10.5" fill="#f8fafc" text-anchor="middle">• Taxonomy &amp; Systematics</text>

  <!-- Connector Lines to Career Badges -->
  <path d="M 185 240 L 185 300 L 130 320" fill="none" stroke="#10b981" stroke-width="2" stroke-dasharray="4,4"/>
  <path d="M 400 275 L 400 305 L 340 320" fill="none" stroke="#38bdf8" stroke-width="2"/>
  <path d="M 500 275 L 500 305 L 560 320" fill="none" stroke="#a855f7" stroke-width="2"/>
  <path d="M 715 240 L 715 300 L 770 320" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4"/>

  <!-- Career Badge 1: Botanical & Agricultural -->
  <rect x="40" y="320" width="180" height="145" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <rect x="40" y="320" width="180" height="28" rx="8" fill="#065f46"/>
  <text x="130" y="339" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">Plant Sciences</text>
  <text x="50" y="365" font-size="10" fill="#e2e8f0">• Agronomist</text>
  <text x="50" y="385" font-size="10" fill="#e2e8f0">• Plant Breeder / Geneticist</text>
  <text x="50" y="405" font-size="10" fill="#e2e8f0">• Herbarium Curator</text>
  <text x="50" y="425" font-size="10" fill="#e2e8f0">• Forestry Consultant</text>
  <text x="50" y="445" font-size="10" fill="#e2e8f0">• Horticultural Specialist</text>

  <!-- Career Badge 2: Health & Medical -->
  <rect x="250" y="320" width="180" height="145" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <rect x="250" y="320" width="180" height="28" rx="8" fill="#075985"/>
  <text x="340" y="339" font-size="11" font-weight="bold" fill="#7dd3fc" text-anchor="middle">Health &amp; Medicine</text>
  <text x="260" y="365" font-size="10" fill="#e2e8f0">• Medical Doctor / Surgeon</text>
  <text x="260" y="385" font-size="10" fill="#e2e8f0">• Clinical Pathologist</text>
  <text x="260" y="405" font-size="10" fill="#e2e8f0">• Pharmacist / Biochemist</text>
  <text x="260" y="425" font-size="10" fill="#e2e8f0">• Epidemiologist</text>
  <text x="260" y="445" font-size="10" fill="#e2e8f0">• Physiotherapist</text>

  <!-- Career Badge 3: Biotech & Forensic -->
  <rect x="470" y="320" width="180" height="145" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
  <rect x="470" y="320" width="180" height="28" rx="8" fill="#581c87"/>
  <text x="560" y="339" font-size="11" font-weight="bold" fill="#d8b4fe" text-anchor="middle">Biotech &amp; Forensics</text>
  <text x="480" y="365" font-size="10" fill="#e2e8f0">• Forensic DNA Analyst</text>
  <text x="480" y="385" font-size="10" fill="#e2e8f0">• Industrial Microbiologist</text>
  <text x="480" y="405" font-size="10" fill="#e2e8f0">• Food Safety Officer</text>
  <text x="480" y="425" font-size="10" fill="#e2e8f0">• Bioprocess Engineer</text>
  <text x="480" y="445" font-size="10" fill="#e2e8f0">• Genetic Counsellor</text>

  <!-- Career Badge 4: Zoology & Ecology -->
  <rect x="680" y="320" width="180" height="145" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
  <rect x="680" y="320" width="180" height="28" rx="8" fill="#78350f"/>
  <text x="770" y="339" font-size="11" font-weight="bold" fill="#fcd34d" text-anchor="middle">Zoology &amp; Wildlife</text>
  <text x="690" y="365" font-size="10" fill="#e2e8f0">• Wildlife Biologist / Vet</text>
  <text x="690" y="385" font-size="10" fill="#e2e8f0">• Conservation Officer</text>
  <text x="690" y="405" font-size="10" fill="#e2e8f0">• Entomologist (Pest Control)</text>
  <text x="690" y="425" font-size="10" fill="#e2e8f0">• Parasitology Officer</text>
  <text x="690" y="445" font-size="10" fill="#e2e8f0">• Marine Ecologist</text>
</svg>
""")

# SVG 2 (Lesson 1.2): Mechanical Engineering Schematic (Pooter & Pitfall Trap)
SVG_2 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 480" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="860" height="450" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="450" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Mechanical Engineering Schematic: Pooter (Aspirator) &amp; Pitfall Trap</text>
  <text x="450" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Physical airflow mechanics, protective filter safety, and soil positioning for ecological sampling</text>

  <!-- LEFT PANEL: POOTER ASPIRATOR -->
  <rect x="40" y="85" width="380" height="360" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="230" y="115" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. POOTER (Aspirator) AIRFLOW MECHANICS</text>

  <!-- Clear Glass/Plastic Jar -->
  <rect x="150" y="210" width="160" height="180" rx="20" fill="#1e293b" stroke="#64748b" stroke-width="2.5"/>
  <rect x="170" y="195" width="120" height="16" rx="4" fill="#334155" stroke="#475569" stroke-width="1.5"/>

  <!-- Suction Tube A (Right into mouth) -->
  <path d="M 250 260 L 250 160 L 370 160" fill="none" stroke="#f59e0b" stroke-width="5" stroke-linecap="round"/>
  <!-- Gauze Filter Badge -->
  <circle cx="250" cy="265" r="9" fill="#ef4444" stroke="#ffffff" stroke-width="2"/>
  <text x="250" y="269" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">G</text>
  <line x1="262" y1="265" x2="350" y2="265" stroke="#ef4444" stroke-width="1.5"/>
  <text x="355" y="268" font-size="10" font-weight="bold" fill="#ef4444">Gauze Filter (CRITICAL SAFETY)</text>
  <text x="355" y="282" font-size="9" fill="#fca5a5">Prevents inhaling specimen/dust</text>

  <text x="375" y="150" font-size="11" font-weight="bold" fill="#f59e0b">Suction Tube A</text>
  <text x="375" y="165" font-size="9" fill="#fde68a">(To Researcher's Mouth)</text>

  <!-- Suction Airflow arrows -->
  <path d="M 240 230 L 240 180" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3"/>
  <polygon points="240,175 236,183 244,183" fill="#f59e0b"/>

  <!-- Entry Tube B (Left to specimen) -->
  <path d="M 90 160 L 190 160 L 190 230" fill="none" stroke="#10b981" stroke-width="5" stroke-linecap="round"/>
  <text x="85" y="150" font-size="11" font-weight="bold" fill="#10b981">Entry Tube B</text>
  <text x="85" y="165" font-size="9" fill="#a7f3d0">(Pointed at Insect)</text>

  <!-- Tree Bark & Target Insect -->
  <rect x="55" y="175" width="20" height="70" rx="3" fill="#78350f"/>
  <ellipse cx="85" cy="180" rx="6" ry="3" fill="#a855f7"/>
  <text x="85" y="195" font-size="9" fill="#cbd5e1">Crawling Insect</text>

  <!-- Captured Specimen at bottom of jar -->
  <ellipse cx="210" cy="360" rx="7" ry="4" fill="#a855f7"/>
  <text x="210" y="380" font-size="10" fill="#94a3b8" text-anchor="middle">Captured Specimen Unharmed</text>

  <text x="230" y="420" font-size="10" fill="#38bdf8" text-anchor="middle">Suction creates low pressure vacuum inside jar</text>

  <!-- RIGHT PANEL: PITFALL TRAP -->
  <rect x="460" y="85" width="400" height="360" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="660" y="115" font-size="16" font-weight="bold" fill="#10b981" text-anchor="middle">2. PITFALL TRAP CROSS-SECTION</text>

  <!-- Soil Cross Section -->
  <!-- Left Soil Bank -->
  <polygon points="480,220 570,220 570,380 480,380" fill="#451a03" stroke="#78350f" stroke-width="2"/>
  <!-- Right Soil Bank -->
  <polygon points="750,220 840,220 840,380 750,380" fill="#451a03" stroke="#78350f" stroke-width="2"/>
  <!-- Grass Layer -->
  <line x1="480" y1="220" x2="570" y2="220" stroke="#22c55e" stroke-width="6"/>
  <line x1="750" y1="220" x2="840" y2="220" stroke="#22c55e" stroke-width="6"/>
  <text x="525" y="210" font-size="10" font-weight="bold" fill="#22c55e">Ground Level</text>
  <text x="795" y="210" font-size="10" font-weight="bold" fill="#22c55e">Soil Surface</text>

  <!-- Buried Trap Container -->
  <rect x="570" y="220" width="180" height="160" rx="6" fill="#1e293b" stroke="#64748b" stroke-width="2.5"/>
  <line x1="570" y1="220" x2="750" y2="220" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,4"/>
  <text x="660" y="240" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Rim FLUSH with Soil Level</text>

  <!-- Rain Cover (Stone on Twig Props) -->
  <ellipse cx="660" cy="170" rx="100" ry="12" fill="#64748b" stroke="#94a3b8" stroke-width="2"/>
  <text x="660" y="165" font-size="10" font-weight="bold" fill="#f8fafc" text-anchor="middle">Flat Stone (Rain &amp; Predator Cover)</text>
  <!-- Twig Props -->
  <line x1="590" y1="180" x2="590" y2="220" stroke="#d97706" stroke-width="3"/>
  <line x1="730" y1="180" x2="730" y2="220" stroke="#d97706" stroke-width="3"/>
  <text x="660" y="200" font-size="9" fill="#fcd34d" text-anchor="middle">Twig Props (allow crawling entry)</text>

  <!-- Falling Crawling Beetle -->
  <ellipse cx="585" cy="270" rx="7" ry="5" fill="#f59e0b"/>
  <path d="M 550 215 Q 575 220 585 260" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="2,2"/>

  <!-- Leaves/Moisture at bottom -->
  <rect x="580" y="355" width="160" height="20" rx="3" fill="#065f46" opacity="0.6"/>
  <text x="660" y="368" font-size="9" fill="#a7f3d0" text-anchor="middle">Moist leaf litter (shelter against dehydration)</text>

  <text x="660" y="420" font-size="10" fill="#10b981" text-anchor="middle">Captures ground-dwelling crawling invertebrates passively</text>
</svg>
""")

# SVG 3 (Lesson 1.3): Detailed Eukaryotic Ultrastructure (Plant Cell vs Animal Cell)
SVG_3 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="880" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="460" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Eukaryotic Ultrastructure: Plant Cell vs. Animal Cell</text>
  <text x="460" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Organelle morphology and structure-to-function adaptations revealed by Transmission Electron Microscopy</text>

  <!-- LEFT: PLANT CELL (Rectangular, Rigid Cellulose Wall) -->
  <rect x="40" y="85" width="400" height="400" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
  <text x="240" y="115" font-size="16" font-weight="bold" fill="#34d399" text-anchor="middle">PLANT CELL (Autotrophic Ultrastructure)</text>

  <!-- Outer Cellulose Wall (Thick Green) -->
  <rect x="65" y="130" width="350" height="330" rx="14" fill="#064e3b" stroke="#10b981" stroke-width="5"/>
  <!-- Plasma Membrane inner layer -->
  <rect x="75" y="140" width="330" height="310" rx="10" fill="#1e293b" stroke="#059669" stroke-width="2"/>
  <text x="85" y="155" font-size="10" font-weight="bold" fill="#34d399">Cellulose Cell Wall</text>
  <text x="85" y="168" font-size="9" fill="#6ee7b7">Plasma Membrane</text>

  <!-- Large Central Vacuole with Tonoplast -->
  <rect x="140" y="190" width="200" height="190" rx="16" fill="#0284c7" fill-opacity="0.25" stroke="#38bdf8" stroke-width="2"/>
  <text x="240" y="275" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Large Central Vacuole</text>
  <text x="240" y="293" font-size="9.5" fill="#bae6fd" text-anchor="middle">(Cell Sap &amp; Turgor Pressure)</text>

  <!-- Chloroplasts with Grana Stacks -->
  <ellipse cx="110" cy="220" rx="26" ry="16" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
  <line x1="96" y1="216" x2="124" y2="216" stroke="#86efac" stroke-width="2"/>
  <line x1="96" y1="224" x2="124" y2="224" stroke="#86efac" stroke-width="2"/>
  <text x="110" y="248" font-size="9.5" font-weight="bold" fill="#4ade80" text-anchor="middle">Chloroplast (Grana)</text>

  <ellipse cx="360" cy="380" rx="26" ry="16" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
  <line x1="346" y1="376" x2="374" y2="376" stroke="#86efac" stroke-width="2"/>
  <line x1="346" y1="384" x2="374" y2="384" stroke="#86efac" stroke-width="2"/>

  <!-- Nucleus & Nucleolus -->
  <circle cx="340" cy="180" r="28" fill="#6b21a8" stroke="#a855f7" stroke-width="2"/>
  <circle cx="340" cy="180" r="10" fill="#c084fc"/>
  <text x="340" y="220" font-size="9.5" font-weight="bold" fill="#e9d5ff" text-anchor="middle">Nucleus (DNA)</text>

  <!-- Mitochondrion with Cristae -->
  <ellipse cx="115" cy="380" rx="24" ry="13" fill="#9a3412" stroke="#f97316" stroke-width="1.5"/>
  <path d="M 100 380 Q 107 373 115 380 T 130 380" fill="none" stroke="#fed7aa" stroke-width="1.5"/>
  <text x="115" y="405" font-size="9.5" font-weight="bold" fill="#fb923c" text-anchor="middle">Mitochondrion</text>

  <!-- RIGHT: ANIMAL CELL (Flexible, No Cell Wall, Centrioles) -->
  <rect x="480" y="85" width="400" height="400" rx="12" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
  <text x="680" y="115" font-size="16" font-weight="bold" fill="#fbbf24" text-anchor="middle">ANIMAL CELL (Heterotrophic Ultrastructure)</text>

  <!-- Flexible Plasma Membrane -->
  <ellipse cx="680" cy="290" rx="170" ry="155" fill="#1e293b" stroke="#f59e0b" stroke-width="3"/>
  <text x="680" y="150" font-size="11" font-weight="bold" fill="#fcd34d" text-anchor="middle">Flexible Plasma Membrane (No Cell Wall)</text>

  <!-- Central Nucleus -->
  <circle cx="680" cy="285" r="42" fill="#6b21a8" stroke="#a855f7" stroke-width="2.5"/>
  <circle cx="680" cy="285" r="15" fill="#c084fc"/>
  <text x="680" y="342" font-size="11" font-weight="bold" fill="#e9d5ff" text-anchor="middle">Nucleus &amp; Chromatin</text>

  <!-- Multiple Mitochondria (Powerhouses) -->
  <ellipse cx="565" cy="215" rx="24" ry="13" fill="#9a3412" stroke="#f97316" stroke-width="1.5"/>
  <path d="M 550 215 Q 557 208 565 215 T 580 215" fill="none" stroke="#fed7aa" stroke-width="1.5"/>
  <text x="565" y="240" font-size="9.5" font-weight="bold" fill="#fb923c" text-anchor="middle">Mitochondria (Cristae)</text>

  <ellipse cx="795" cy="350" rx="24" ry="13" fill="#9a3412" stroke="#f97316" stroke-width="1.5"/>
  <ellipse cx="585" cy="375" rx="24" ry="13" fill="#9a3412" stroke="#f97316" stroke-width="1.5"/>

  <!-- Centrioles (Animal specific) -->
  <rect x="750" y="200" width="18" height="8" rx="2" fill="#38bdf8"/>
  <rect x="755" y="195" width="8" height="18" rx="2" fill="#38bdf8"/>
  <text x="760" y="232" font-size="9.5" font-weight="bold" fill="#7dd3fc" text-anchor="middle">Centrioles (Pair)</text>

  <!-- Lysosomes -->
  <circle cx="770" cy="270" r="10" fill="#ef4444" stroke="#fca5a5" stroke-width="1.5"/>
  <text x="770" y="292" font-size="9" fill="#fca5a5" text-anchor="middle">Lysosome</text>

  <!-- Small temporary vacuoles -->
  <circle cx="580" cy="300" r="9" fill="#0284c7" opacity="0.5"/>
  <text x="580" y="320" font-size="8.5" fill="#93c5fd" text-anchor="middle">Small Vacuole</text>
</svg>
""")

# SVG 4 (Lesson 1.4): Multi-Panel Lock-and-Key Model & 3 Kinetics Response Curves
SVG_4 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="880" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="460" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Enzyme Catalysis Mechanics &amp; Environmental Kinetics</text>
  <text x="460" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Lock-and-Key hypothesis and mathematical reaction rate curves under temperature, pH, and substrate variation</text>

  <!-- TOP PANEL: LOCK AND KEY MECHANISM -->
  <rect x="40" y="85" width="840" height="160" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="460" y="108" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. The Lock-and-Key Catalytic Mechanism</text>

  <!-- Stage A: Enzyme + Substrate -->
  <path d="M 70 140 L 150 140 L 150 160 L 125 160 L 125 185 L 95 185 L 95 160 L 70 160 Z" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
  <text x="110" y="205" font-size="10" font-weight="bold" fill="#7dd3fc" text-anchor="middle">Enzyme (Active Site)</text>

  <rect x="100" y="125" width="20" height="20" rx="3" fill="#f59e0b" stroke="#fbbf24" stroke-width="1.5"/>
  <text x="110" y="120" font-size="10" font-weight="bold" fill="#fcd34d" text-anchor="middle">Substrate</text>

  <text x="185" y="165" font-size="22" fill="#38bdf8" font-weight="bold">→</text>

  <!-- Stage B: Enzyme-Substrate Complex -->
  <path d="M 230 140 L 310 140 L 310 160 L 285 160 L 285 185 L 255 185 L 255 160 L 230 160 Z" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
  <rect x="260" y="160" width="20" height="20" rx="2" fill="#f59e0b" stroke="#fbbf24" stroke-width="1"/>
  <text x="270" y="205" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Enzyme-Substrate Complex</text>

  <text x="345" y="165" font-size="22" fill="#38bdf8" font-weight="bold">→</text>

  <!-- Stage C: Products Released, Enzyme Unchanged -->
  <path d="M 390 140 L 470 140 L 470 160 L 445 160 L 445 185 L 415 185 L 415 160 L 390 160 Z" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
  <text x="430" y="205" font-size="10" font-weight="bold" fill="#7dd3fc" text-anchor="middle">Enzyme Unchanged</text>

  <circle cx="510" cy="145" r="9" fill="#10b981" stroke="#34d399" stroke-width="1.5"/>
  <circle cx="532" cy="145" r="9" fill="#10b981" stroke="#34d399" stroke-width="1.5"/>
  <text x="521" y="175" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">Products Released</text>

  <!-- Key Concept Summary Box -->
  <rect x="580" y="118" width="280" height="112" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="595" y="140" font-size="11" font-weight="bold" fill="#f59e0b">• Strict 3D Shape Specificity</text>
  <text x="595" y="160" font-size="10.5" fill="#e2e8f0">• Lowers Activation Energy</text>
  <text x="595" y="180" font-size="10.5" fill="#e2e8f0">• Remains chemically unchanged</text>
  <text x="595" y="200" font-size="10.5" fill="#e2e8f0">• Operates at biological temperatures</text>

  <!-- BOTTOM PANELS: 3 KINETIC CURVES -->

  <!-- Graph A: Temperature -->
  <rect x="40" y="260" width="265" height="225" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
  <text x="172" y="285" font-size="12.5" font-weight="bold" fill="#ef4444" text-anchor="middle">Rate vs. Temperature (°C)</text>
  <!-- Axes -->
  <line x1="65" y1="445" x2="280" y2="445" stroke="#64748b" stroke-width="2"/>
  <line x1="65" y1="445" x2="65" y2="305" stroke="#64748b" stroke-width="2"/>
  <!-- Temp Curve -->
  <path d="M 70 440 Q 170 310 175 310 Q 180 310 220 445" fill="none" stroke="#ef4444" stroke-width="3"/>
  <circle cx="175" cy="310" r="4" fill="#fef08a"/>
  <text x="175" y="303" font-size="9.5" font-weight="bold" fill="#fef08a" text-anchor="middle">Optimum (37°C)</text>
  <text x="225" y="425" font-size="9.5" font-weight="bold" fill="#f87171">Denaturation (60°C)</text>
  <text x="172" y="470" font-size="9.5" fill="#94a3b8" text-anchor="middle">Heat breaks tertiary shape</text>

  <!-- Graph B: pH -->
  <rect x="325" y="260" width="270" height="225" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
  <text x="460" y="285" font-size="12.5" font-weight="bold" fill="#a855f7" text-anchor="middle">Rate vs. pH (Narrow Optima)</text>
  <line x1="350" y1="445" x2="570" y2="445" stroke="#64748b" stroke-width="2"/>
  <line x1="350" y1="445" x2="350" y2="305" stroke="#64748b" stroke-width="2"/>
  <!-- Pepsin pH 2 -->
  <path d="M 360 440 Q 395 320 430 440" fill="none" stroke="#ef4444" stroke-width="2.5"/>
  <text x="395" y="315" font-size="9" font-weight="bold" fill="#ef4444" text-anchor="middle">Pepsin (pH 2)</text>
  <!-- Salivary Amylase pH 7 -->
  <path d="M 460 440 Q 495 320 530 440" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
  <text x="495" y="315" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Amylase (pH 7)</text>
  <text x="460" y="470" font-size="9.5" fill="#94a3b8" text-anchor="middle">Extreme pH alters active site charges</text>

  <!-- Graph C: Substrate Concentration -->
  <rect x="615" y="260" width="265" height="225" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="747" y="285" font-size="12.5" font-weight="bold" fill="#10b981" text-anchor="middle">Rate vs. Substrate Conc.</text>
  <line x1="640" y1="445" x2="855" y2="445" stroke="#64748b" stroke-width="2"/>
  <line x1="640" y1="445" x2="640" y2="305" stroke="#64748b" stroke-width="2"/>
  <!-- Plateau Curve -->
  <path d="M 645 440 Q 710 330 845 330" fill="none" stroke="#10b981" stroke-width="3"/>
  <line x1="640" y1="330" x2="850" y2="330" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="760" y="320" font-size="9.5" font-weight="bold" fill="#fcd34d">Vmax (Saturation Plateau)</text>
  <text x="747" y="470" font-size="9.5" fill="#94a3b8" text-anchor="middle">All active sites occupied</text>
</svg>
""")

TOPIC1_BIOLOGY_SVGS = [
    {"lesson_order": 1, "page": 6, "svg": SVG_1, "title": "Overlapping Disciplines and Career Pathways in Biology"},
    {"lesson_order": 2, "page": 4, "svg": SVG_2, "title": "Mechanical Engineering of Field Tools: Pooter and Pitfall Trap"},
    {"lesson_order": 3, "page": 8, "svg": SVG_3, "title": "Detailed Ultrastructure: Plant Cell vs. Animal Cell"},
    {"lesson_order": 4, "page": 9, "svg": SVG_4, "title": "Lock-and-Key Mechanism and Enzyme Activity Kinetics Graphs"},
]

TOPIC1_BIOLOGY_PHOTOS = [
    {
        "lesson_order": 1,
        "page": 4,
        "title": "The Vast Spectrum of Biology: From Ecosystems to Cellular Cultures",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/African_Bush_Elephant_%28Loxodonta_africana%29_male_%2817293816650%29.jpg/1280px-African_Bush_Elephant_%28Loxodonta_africana%29_male_%2817293816650%29.jpg",
        "author": "Bernard DUPONT / Wikimedia Commons",
        "licensing": "CC BY-SA 2.0",
        "caption": "Macro-scale biodiversity in a Kenyan savanna ecosystem. Biology investigates how large mammals, acacia vegetation, and soil microbes interact dynamically with abiotic factors like sunlight, moisture, and ambient temperature."
    },
    {
        "lesson_order": 2,
        "page": 6,
        "title": "Museum-Grade Botanical Herbarium Specimen Sheet",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Herbarium_specimen_K000850257.jpg/1024px-Herbarium_specimen_K000850257.jpg",
        "author": "Royal Botanic Gardens, Kew / Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "A museum-curated botanical herbarium specimen (Royal Botanic Gardens, Kew). Notice the carefully pressed and dried plant organs (stem, foliage, inflorescence) mounted alongside the standardized scientific label in the bottom-right corner recording taxonomic, locality, and collection metadata."
    },
    {
        "lesson_order": 3,
        "page": 5,
        "title": "Onion Epidermal Cells Stained with Iodine under Light Microscope",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Onion_cells_2.jpg/1280px-Onion_cells_2.jpg",
        "author": "Umberto Salvagnin / Wikimedia Commons",
        "licensing": "CC BY 2.0",
        "caption": "Light micrograph of Allium cepa (onion) epidermal cells stained with iodine at 400x magnification. The yellow-brown iodine stain highlights the rectangular cellulose cell walls, translucent cytoplasm, and distinct darkly stained spherical nuclei."
    },
    {
        "lesson_order": 4,
        "page": 6,
        "title": "Positive Diagnostic Color Results in Food Testing",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Benedicts_test.jpg/1280px-Benedicts_test.jpg",
        "author": "Chemical Heritage Foundation / Wikimedia Commons",
        "licensing": "CC BY-SA 3.0",
        "caption": "Biochemical diagnostic food testing: Benedict's solution undergoing reduction from initial clear blue (left) through green and yellow to a dense brick-red Copper(I) oxide precipitate (right) upon boiling with reducing sugars like glucose."
    }
]

TOPIC1_BIOLOGY_VIDEOS = [
    {
        "lesson_order": 1,
        "page": 8,
        "title": "Deep Dive: Introduction to Biology and Careers in Science",
        "youtube_id": "39yN65d7Zp8",
        "description": "Comprehensive exploration of what biology is, foundational branches (botany, zoology), specialized disciplines (genetics, microbiology, ecology), and rewarding careers in science."
    },
    {
        "lesson_order": 2,
        "page": 10,
        "title": "Deep Dive: Field Sampling Techniques, Pooters, and Herbarium Curation",
        "youtube_id": "u43pI33hH38",
        "description": "Step-by-step ecological fieldwork demonstration showcasing pooters, pitfall traps, sweep nets, and the complete 6-stage construction of botanical herbarium sheets."
    },
    {
        "lesson_order": 3,
        "page": 11,
        "title": "Deep Dive: Eukaryotic Cell Structure, Organelles, and Microscopy",
        "youtube_id": "URUJD5NEXC8",
        "description": "High-clarity video guide to eukaryotic plant and animal cell ultrastructure, organelle structure-to-function adaptations, and preparing onion epidermal wet mount slides."
    },
    {
        "lesson_order": 4,
        "page": 11,
        "title": "Deep Dive: Enzymes, Catalase Breakdown, and Biochemical Food Tests",
        "youtube_id": "qgVFkRn8f10",
        "description": "Detailed video investigation into enzyme catalysis, lock-and-key active site kinetics, temperature and pH denaturation, and standard diagnostic food testing reagents."
    }
]

def enrich_grade10_biology_topic1():
    print("=" * 80)
    print("VLearn Grade 10 Biology — Topic 1 (Cell Biology & Biodiversity)")
    print("Visual Enrichment Engine: Attaching SVGs, Photos, and YouTube Videos")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="CBC").first() or Curriculum.objects.filter(id=5).first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 10").first() or Grade.objects.filter(curriculum=curriculum, level=10).first()
    subject = Subject.objects.filter(grade=grade, name="Biology").first()
    topic = Topic.objects.filter(subject=subject, name="Cell Biology and Biodiversity").first()

    if not topic:
        print("[!] Error: Topic 'Cell Biology and Biodiversity' not found under Grade 10 Biology!")
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
        svg_matches = [s for s in TOPIC1_BIOLOGY_SVGS if s["lesson_order"] == u_order]
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
        photo_matches = [p for p in TOPIC1_BIOLOGY_PHOTOS if p["lesson_order"] == u_order]
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
        video_matches = [v for v in TOPIC1_BIOLOGY_VIDEOS if v["lesson_order"] == u_order]
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
    print("[SUCCESS] Grade 10 Biology Topic 1 Visual Enrichment Complete!")
    print(f"[*] Total Vector SVGs Attached:       {svg_count}")
    print(f"[*] Total Wikimedia Photos Attached:   {photo_count}")
    print(f"[*] Total YouTube Videos Attached:     {video_count}")
    print(f"[*] Total LessonAsset Records Created: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_biology_topic1()
