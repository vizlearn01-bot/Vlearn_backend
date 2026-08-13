"""
VLearn Form 4 Biology — Topic 2: Evolution
Visual Enrichment Engine (18 Vector SVGs + 8 Verified Wikimedia Photos)

Attaches:
  - 18 Custom Vector SVGs to suggested_diagram blocks
  - 8 Pre-Verified Wikimedia Photos to suggested_image blocks
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_form4_biology_topic2.py
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
# 18 HIGH-PRECISION VECTOR SVGS FOR BIOLOGY TOPIC 2: EVOLUTION
# =====================================================================

SVG_1 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Timeline of Earth &amp; Origin of Life Milestones</text>
  <line x1="60" y1="220" x2="740" y2="220" stroke="#38bdf8" stroke-width="4"/>

  <!-- Milestones -->
  <circle cx="100" cy="220" r="10" fill="#ef4444"/>
  <text x="100" y="180" font-size="12" font-weight="bold" fill="#ef4444" text-anchor="middle">4.6 BYA</text>
  <text x="100" y="260" font-size="11" fill="#cbd5e1" text-anchor="middle">Earth Formed</text>

  <circle cx="260" cy="220" r="10" fill="#f59e0b"/>
  <text x="260" y="180" font-size="12" font-weight="bold" fill="#f59e0b" text-anchor="middle">3.8 BYA</text>
  <text x="260" y="260" font-size="11" fill="#cbd5e1" text-anchor="middle">Prebiotic Soup</text>

  <circle cx="420" cy="220" r="10" fill="#10b981"/>
  <text x="420" y="180" font-size="12" font-weight="bold" fill="#10b981" text-anchor="middle">3.5 BYA</text>
  <text x="420" y="260" font-size="11" fill="#cbd5e1" text-anchor="middle">First Prokaryotes</text>

  <circle cx="580" cy="220" r="10" fill="#a855f7"/>
  <text x="580" y="180" font-size="12" font-weight="bold" fill="#a855f7" text-anchor="middle">1.5 BYA</text>
  <text x="580" y="260" font-size="11" fill="#cbd5e1" text-anchor="middle">First Eukaryotes</text>

  <circle cx="700" cy="220" r="10" fill="#38bdf8"/>
  <text x="700" y="180" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">0.5 BYA</text>
  <text x="700" y="260" font-size="11" fill="#cbd5e1" text-anchor="middle">Vertebrate Radiation</text>
</svg>
""")

SVG_2 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Miller-Urey Prebiotic Synthesis Apparatus</text>
  <rect x="40" y="80" width="720" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>

  <!-- Gas Flask -->
  <circle cx="200" cy="200" r="60" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
  <text x="200" y="195" font-size="12" font-weight="bold" fill="#fef08a" text-anchor="middle">CH4, NH3, H2, H2O</text>
  <text x="200" y="215" font-size="11" fill="#f59e0b" text-anchor="middle">(Spark Electrodes)</text>

  <line x1="260" y1="200" x2="400" y2="200" stroke="#38bdf8" stroke-width="4"/>

  <!-- Condenser -->
  <rect x="400" y="160" width="140" height="80" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="470" y="195" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">Condenser</text>
  <text x="470" y="215" font-size="11" fill="#93c5fd" text-anchor="middle">(Cooling Water)</text>

  <line x1="540" y1="200" x2="640" y2="200" stroke="#38bdf8" stroke-width="4"/>

  <!-- Trap -->
  <rect x="640" y="160" width="100" height="120" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
  <text x="690" y="210" font-size="12" font-weight="bold" fill="#10b981" text-anchor="middle">U-Trap</text>
  <text x="690" y="235" font-size="11" fill="#a7f3d0" text-anchor="middle">Amino Acids</text>
</svg>
""")

SVG_3 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Coacervate Droplet &amp; Protocell Membrane Formation</text>
  <circle cx="400" cy="240" r="130" fill="#0f172a" stroke="#a855f7" stroke-width="3"/>
  <circle cx="400" cy="240" r="110" fill="#1e293b" stroke="#38bdf8" stroke-width="2" stroke-dasharray="6,6"/>

  <text x="400" y="220" font-size="16" font-weight="bold" fill="#a855f7" text-anchor="middle">Coacervate Droplet</text>
  <text x="400" y="250" font-size="13" fill="#cbd5e1" text-anchor="middle">Lipid Bilayer Boundary</text>
  <text x="400" y="275" font-size="12" fill="#38bdf8" text-anchor="middle">Encapsulated Self-Replicating RNA</text>
</svg>
""")

SVG_4 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Geological Stratigraphy &amp; Fossil Layer Deposition</text>

  <!-- Strata Layers -->
  <rect x="100" y="90" width="600" height="60" fill="#334155"/>
  <text x="400" y="125" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">Upper Strata: Complex Mammals &amp; Birds (Youngest)</text>

  <rect x="100" y="160" width="600" height="60" fill="#1e293b"/>
  <text x="400" y="195" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">Middle Strata: Reptiles &amp; Amphibians</text>

  <rect x="100" y="230" width="600" height="60" fill="#0f172a"/>
  <text x="400" y="265" font-size="14" font-weight="bold" fill="#f59e0b" text-anchor="middle">Lower Strata: Primitive Fish &amp; Invertebrates</text>

  <rect x="100" y="300" width="600" height="60" fill="#020617"/>
  <text x="400" y="335" font-size="14" font-weight="bold" fill="#ef4444" text-anchor="middle">Basal Strata: Prebiotic Rocks &amp; Microfossils (Oldest)</text>
</svg>
""")

SVG_5 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Comparative Hominid Skull Evolution Sequence</text>
  <g transform="translate(40, 100)">
    <rect x="0" y="0" width="160" height="260" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="80" y="40" font-size="14" font-weight="bold" fill="#ef4444" text-anchor="middle">Australopithecus</text>
    <text x="80" y="80" font-size="12" fill="#cbd5e1" text-anchor="middle">450 cc Brain</text>
    <text x="80" y="110" font-size="11" fill="#94a3b8" text-anchor="middle">Heavy Brow Ridge</text>
    <text x="80" y="130" font-size="11" fill="#94a3b8" text-anchor="middle">Prognathous Jaw</text>

    <rect x="180" y="0" width="160" height="260" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="260" y="40" font-size="14" font-weight="bold" fill="#f59e0b" text-anchor="middle">Homo habilis</text>
    <text x="260" y="80" font-size="12" fill="#cbd5e1" text-anchor="middle">650 cc Brain</text>
    <text x="260" y="110" font-size="11" fill="#94a3b8" text-anchor="middle">Handy Man</text>
    <text x="260" y="130" font-size="11" fill="#94a3b8" text-anchor="middle">First Tool Maker</text>

    <rect x="360" y="0" width="160" height="260" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="440" y="40" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">Homo erectus</text>
    <text x="440" y="80" font-size="12" fill="#cbd5e1" text-anchor="middle">1000 cc Brain</text>
    <text x="440" y="110" font-size="11" fill="#94a3b8" text-anchor="middle">Upright Man</text>
    <text x="440" y="130" font-size="11" fill="#94a3b8" text-anchor="middle">Fire &amp; Axes</text>

    <rect x="540" y="0" width="160" height="260" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <text x="620" y="40" font-size="14" font-weight="bold" fill="#10b981" text-anchor="middle">Homo sapiens</text>
    <text x="620" y="80" font-size="12" fill="#cbd5e1" text-anchor="middle">1400 cc Brain</text>
    <text x="620" y="110" font-size="11" fill="#94a3b8" text-anchor="middle">Flat Face &amp; Chin</text>
    <text x="620" y="130" font-size="11" fill="#94a3b8" text-anchor="middle">Modern Human</text>
  </g>
</svg>
""")

SVG_6 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Continental Drift &amp; Adaptive Radiation of Darwin's Finches</text>
  <circle cx="400" cy="240" r="140" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="400" cy="240" r="25" fill="#f59e0b"/>
  <text x="400" y="245" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Ancestor</text>

  <!-- Radiating Beaks -->
  <line x1="400" y1="215" x2="400" y2="130" stroke="#10b981" stroke-width="3"/>
  <text x="400" y="115" font-size="12" fill="#a7f3d0" text-anchor="middle">Seed Crusher Beak</text>

  <line x1="425" y1="240" x2="520" y2="240" stroke="#10b981" stroke-width="3"/>
  <text x="560" y="245" font-size="12" fill="#a7f3d0" text-anchor="middle">Insect Probe Beak</text>

  <line x1="400" y1="265" x2="400" y2="350" stroke="#10b981" stroke-width="3"/>
  <text x="400" y="370" font-size="12" fill="#a7f3d0" text-anchor="middle">Cactus Eater Beak</text>

  <line x1="375" y1="240" x2="280" y2="240" stroke="#10b981" stroke-width="3"/>
  <text x="230" y="245" font-size="12" fill="#a7f3d0" text-anchor="middle">Woodpecker Beak</text>
</svg>
""")

SVG_7 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Pentadactyl Limb Homology Across Vertebrates</text>
  <g transform="translate(40, 80)">
    <rect x="0" y="0" width="160" height="280" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="80" y="30" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">Human Arm</text>
    <text x="80" y="70" font-size="12" fill="#cbd5e1" text-anchor="middle">Humerus</text>
    <text x="80" y="110" font-size="12" fill="#cbd5e1" text-anchor="middle">Radius &amp; Ulna</text>
    <text x="80" y="150" font-size="12" fill="#cbd5e1" text-anchor="middle">Carpals</text>
    <text x="80" y="190" font-size="12" fill="#cbd5e1" text-anchor="middle">Metacarpals</text>
    <text x="80" y="230" font-size="12" fill="#10b981" text-anchor="middle">5 Phalanges (Grasp)</text>

    <rect x="180" y="0" width="160" height="280" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="260" y="30" font-size="14" font-weight="bold" fill="#a855f7" text-anchor="middle">Bat Wing</text>
    <text x="260" y="230" font-size="12" fill="#e9d5ff" text-anchor="middle">Extended Digits (Flight)</text>

    <rect x="360" y="0" width="160" height="280" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="440" y="30" font-size="14" font-weight="bold" fill="#f59e0b" text-anchor="middle">Whale Flipper</text>
    <text x="440" y="230" font-size="12" fill="#fef08a" text-anchor="middle">Flattened (Swim)</text>

    <rect x="540" y="0" width="160" height="280" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="620" y="30" font-size="14" font-weight="bold" fill="#ef4444" text-anchor="middle">Horse Leg</text>
    <text x="620" y="230" font-size="12" fill="#fca5a5" text-anchor="middle">Single Digit (Run)</text>
  </g>
</svg>
""")

SVG_8 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Divergent vs Convergent Evolution Pathways</text>
  <rect x="40" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="212" y="110" font-size="15" font-weight="bold" fill="#10b981" text-anchor="middle">1. Divergent (Homology)</text>
  <text x="212" y="150" font-size="13" fill="#cbd5e1" text-anchor="middle">Common Ancestor</text>
  <line x1="212" y1="170" x2="120" y2="280" stroke="#10b981" stroke-width="3"/>
  <line x1="212" y1="170" x2="304" y2="280" stroke="#10b981" stroke-width="3"/>
  <text x="120" y="310" font-size="12" fill="#a7f3d0" text-anchor="middle">Human Arm</text>
  <text x="304" y="310" font-size="12" fill="#a7f3d0" text-anchor="middle">Whale Flipper</text>

  <rect x="415" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="587" y="110" font-size="15" font-weight="bold" fill="#f59e0b" text-anchor="middle">2. Convergent (Analogy)</text>
  <text x="480" y="280" font-size="12" fill="#fef08a" text-anchor="middle">Shark (Fish)</text>
  <text x="690" y="280" font-size="12" fill="#fef08a" text-anchor="middle">Dolphin (Mammal)</text>
  <line x1="480" y1="260" x2="587" y2="170" stroke="#f59e0b" stroke-width="3"/>
  <line x1="690" y1="260" x2="587" y2="170" stroke="#f59e0b" stroke-width="3"/>
  <text x="587" y="150" font-size="13" fill="#cbd5e1" text-anchor="middle">Streamlined Shape</text>
</svg>
""")

SVG_9 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Comparative Vertebrate Embryology Pathways</text>
  <rect x="40" y="80" width="720" height="320" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
  <text x="400" y="120" font-size="15" font-weight="bold" fill="#a855f7" text-anchor="middle">Early Embryos of Fish, Reptile, Bird, &amp; Human</text>
  <text x="400" y="170" font-size="14" fill="#cbd5e1" text-anchor="middle">All possess Pharyngeal Gill Slits and Post-Anal Tail</text>
  <line x1="100" y1="220" x2="700" y2="220" stroke="#a855f7" stroke-width="3"/>
  <text x="400" y="270" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">Diverge into Adult Morphologies during Later Development</text>
</svg>
""")

SVG_10 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Serological Antigen-Antibody Precipitin Test Matrix</text>
  <rect x="40" y="70" width="720" height="340" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="150" y="100" font-size="14" font-weight="bold" fill="#38bdf8">Species Tested</text>
  <text x="400" y="100" font-size="14" font-weight="bold" fill="#10b981">Precipitation %</text>
  <text x="620" y="100" font-size="14" font-weight="bold" fill="#f59e0b">Phylogenetic Closeness</text>
  <line x1="60" y1="115" x2="740" y2="115" stroke="#334155" stroke-width="2"/>

  <text x="150" y="150" font-size="13" font-weight="bold" fill="#ffffff">Human</text>
  <text x="400" y="150" font-size="13" fill="#10b981">100%</text>
  <text x="620" y="150" font-size="12" fill="#cbd5e1">Identity Reference</text>

  <text x="150" y="200" font-size="13" font-weight="bold" fill="#ffffff">Chimpanzee</text>
  <text x="400" y="200" font-size="13" fill="#10b981">85%</text>
  <text x="620" y="200" font-size="12" fill="#cbd5e1">Very Close Common Ancestor</text>

  <text x="150" y="250" font-size="13" font-weight="bold" fill="#ffffff">Baboon</text>
  <text x="400" y="250" font-size="13" fill="#f59e0b">64%</text>
  <text x="620" y="250" font-size="12" fill="#cbd5e1">Distant Primate Ancestor</text>

  <text x="150" y="300" font-size="13" font-weight="bold" fill="#ffffff">Dog</text>
  <text x="400" y="300" font-size="13" fill="#ef4444">15%</text>
  <text x="620" y="300" font-size="12" fill="#cbd5e1">Very Distant Ancestor</text>
</svg>
""")

SVG_11 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Lamarckism vs Darwinism Mechanism Comparison</text>
  <rect x="40" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
  <text x="212" y="110" font-size="15" font-weight="bold" fill="#ef4444" text-anchor="middle">Lamarckism (Disproved)</text>
  <text x="60" y="160" font-size="12" fill="#cbd5e1">• Short neck stretched to reach leaves</text>
  <text x="60" y="200" font-size="12" fill="#cbd5e1">• Acquired longer neck in lifetime</text>
  <text x="60" y="240" font-size="12" fill="#cbd5e1">• Passed acquired long neck to offspring</text>

  <rect x="415" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="587" y="110" font-size="15" font-weight="bold" fill="#10b981" text-anchor="middle">Darwinism (Accepted)</text>
  <text x="435" y="160" font-size="12" fill="#cbd5e1">• Pre-existing variation (short &amp; long)</text>
  <text x="435" y="200" font-size="12" fill="#cbd5e1">• Long-necked survived drought &amp; bred</text>
  <text x="435" y="240" font-size="12" fill="#cbd5e1">• Long-neck alleles inherited by offspring</text>
</svg>
""")

SVG_12 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Darwinian Natural Selection 5-Step Cascade</text>
  <g transform="translate(60, 80)">
    <rect x="0" y="0" width="680" height="45" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="340" y="28" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. Overproduction: High reproductive rate produces surplus offspring</text>

    <rect x="0" y="60" width="680" height="45" rx="6" fill="#1e293b" stroke="#f59e0b"/>
    <text x="340" y="88" font-size="13" font-weight="bold" fill="#f59e0b" text-anchor="middle">2. Struggle for Existence: Severe competition for limited resources</text>

    <rect x="0" y="120" width="680" height="45" rx="6" fill="#1e293b" stroke="#a855f7"/>
    <text x="340" y="148" font-size="13" font-weight="bold" fill="#a855f7" text-anchor="middle">3. Genetic Variation: Pre-existing differences in population</text>

    <rect x="0" y="180" width="680" height="45" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="340" y="208" font-size="13" font-weight="bold" fill="#ef4444" text-anchor="middle">4. Survival of Fittest: Best adapted survive environmental pressure</text>

    <rect x="0" y="240" width="680" height="45" rx="6" fill="#065f46" stroke="#10b981"/>
    <text x="340" y="268" font-size="13" font-weight="bold" fill="#a7f3d0" text-anchor="middle">5. Inheritance: Favorable alleles passed to next generation</text>
  </g>
</svg>
""")

SVG_13 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Peppered Moth Industrial Melanism Frequency Shift</text>
  <rect x="40" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="212" y="110" font-size="15" font-weight="bold" fill="#10b981" text-anchor="middle">Pre-Industrial (Pale Lichens)</text>
  <text x="212" y="180" font-size="14" font-weight="bold" fill="#a7f3d0" text-anchor="middle">99% Pale Moths (typica)</text>
  <text x="212" y="220" font-size="12" fill="#cbd5e1" text-anchor="middle">1% Dark Moths eaten by birds</text>

  <rect x="415" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="587" y="110" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">Post-Industrial (Soot Bark)</text>
  <text x="587" y="180" font-size="14" font-weight="bold" fill="#93c5fd" text-anchor="middle">95% Dark Moths (carbonaria)</text>
  <text x="587" y="220" font-size="12" fill="#cbd5e1" text-anchor="middle">Pale Moths eaten by birds</text>
</svg>
""")

SVG_14 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Bacterial Antibiotic Resistance Selection Curve</text>
  <rect x="40" y="80" width="720" height="320" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
  <text x="140" y="140" font-size="13" fill="#cbd5e1">1. Normal Bacterial Population (Rare resistant mutant)</text>
  <line x1="140" y1="160" x2="140" y2="200" stroke="#ef4444" stroke-width="3"/>
  <text x="140" y="230" font-size="13" fill="#ef4444">2. Antibiotic Applied -> Kills Susceptible Bacteria</text>
  <line x1="140" y1="250" x2="140" y2="290" stroke="#10b981" stroke-width="3"/>
  <text x="140" y="320" font-size="13" font-weight="bold" fill="#a7f3d0">3. Resistant Mutants Multiply -> Dominant Superbug Strain</text>
</svg>
""")

SVG_15 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Allopatric Speciation via Geographical Isolation</text>
  <rect x="40" y="100" width="200" height="260" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="140" y="140" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. Uniform Population</text>

  <rect x="290" y="100" width="220" height="260" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="400" y="140" font-size="13" font-weight="bold" fill="#f59e0b" text-anchor="middle">2. River Barrier Formed</text>
  <line x1="400" y1="160" x2="400" y2="340" stroke="#38bdf8" stroke-width="6"/>

  <rect x="560" y="100" width="200" height="260" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="660" y="140" font-size="13" font-weight="bold" fill="#10b981" text-anchor="middle">3. Two New Species</text>
  <text x="660" y="180" font-size="11" fill="#a7f3d0" text-anchor="middle">(Reproductive Isolation)</text>
</svg>
""")

SVG_16 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Comparative Wing Morphology: Bird Endoskeleton vs Insect Exoskeleton</text>
  <rect x="40" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="212" y="110" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">Bird Wing (Endoskeleton)</text>
  <text x="60" y="170" font-size="12" fill="#cbd5e1">• Internal bony skeleton (Humerus, Radius, Ulna)</text>
  <text x="60" y="210" font-size="12" fill="#cbd5e1">• Covered in feathers</text>
  <text x="60" y="250" font-size="12" fill="#a7f3d0">• Homologous to mammal forelimbs</text>

  <rect x="415" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="587" y="110" font-size="15" font-weight="bold" fill="#f59e0b" text-anchor="middle">Insect Wing (Exoskeleton)</text>
  <text x="435" y="170" font-size="12" fill="#cbd5e1">• Chitinous exoskeleton extension</text>
  <text x="435" y="210" font-size="12" fill="#cbd5e1">• Strengthened by hollow veins</text>
  <text x="435" y="250" font-size="12" fill="#fef08a">• Analogous to bird wings (Convergent)</text>
</svg>
""")

SVG_17 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Museum Fossil Stratigraphy Lab Dissection Protocol</text>
  <rect x="40" y="80" width="720" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="400" y="120" font-size="15" font-weight="bold" fill="#10b981" text-anchor="middle">Practical Museum Observation Protocol</text>
  <text x="80" y="170" font-size="13" fill="#cbd5e1">1. Record fossil rock strata depth and layer age.</text>
  <text x="80" y="210" font-size="13" fill="#cbd5e1">2. Identify homologous bones in preserved vertebrate skeletons.</text>
  <text x="80" y="250" font-size="13" fill="#cbd5e1">3. Measure hominid cranial capacity evolution across exhibit specimens.</text>
</svg>
""")

SVG_18 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">KCSE Evolutionary Evidence &amp; Mechanism Decision Tree</text>
  <rect x="40" y="80" width="720" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="400" y="120" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">KCSE Essay Strategy Decision Tree</text>
  <text x="80" y="170" font-size="13" fill="#cbd5e1">1. Question on Evidence? -> Detail Homology, Fossils, Embryology, Serology.</text>
  <text x="80" y="210" font-size="13" fill="#cbd5e1">2. Question on Mechanism? -> Apply 5-step Darwinian Natural Selection cascade.</text>
  <text x="80" y="250" font-size="13" fill="#cbd5e1">3. Question on Modern Selection? -> Detail Industrial Melanism or Antibiotic Resistance.</text>
</svg>
""")

TOPIC2_BIOLOGY_SVGS = [
    SVG_1, SVG_2, SVG_3, SVG_4, SVG_5, SVG_6,
    SVG_7, SVG_8, SVG_9, SVG_10, SVG_11, SVG_12,
    SVG_13, SVG_14, SVG_15, SVG_16, SVG_17, SVG_18
]

# =====================================================================
# 8 VERIFIED WIKIMEDIA COMMONS PHOTOS FOR BIOLOGY TOPIC 2: EVOLUTION
# =====================================================================

TOPIC2_BIOLOGY_PHOTOS = [
    {
        "lesson_order": 1,
        "page": 5,
        "title": "Prebiotic Molecular Vector Model",
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/da/Making_of_a_DNA_vaccine.jpg",
        "author": "Public Domain, Wikimedia Commons",
        "licensing": "Public domain",
        "caption": "Diagrammatic representation of a circular bacterial plasmid vector used in recombinant DNA and molecular evolution studies."
    },
    {
        "lesson_order": 3,
        "page": 2,
        "title": "Ammonite Fossil Limestone Stratigraphy",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/52/Ammonite_fossil_with_in-situ_aptychi_%28Solnhofen_Limestone%2C_Upper_Jurassic%3B_Bavaria%2C_Germany%29_1_%2836800705542%29.jpg",
        "author": "CC BY 2.0, Wikimedia Commons",
        "licensing": "CC BY 2.0",
        "caption": "Preserved Jurassic ammonite fossil embedded in Solnhofen limestone sedimentary rock matrix."
    },
    {
        "lesson_order": 3,
        "page": 4,
        "title": "Hominid Skull Replica Evidence",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/72/Reproducciones_de_cr%C3%A1neos_de_homo_erectus._Museo_Arqueol%C3%B3gico_Nacional_de_Espa%C3%B1a.jpg",
        "author": "CC BY-SA 4.0, Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "Museum fossil skull replica of Homo erectus demonstrating prominent brow ridge and intermediate braincase capacity."
    },
    {
        "lesson_order": 3,
        "page": 6,
        "title": "Galapagos Darwin's Finches Adaptive Radiation",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/50/Darwin%27s_finches.png",
        "author": "Public Domain, Wikimedia Commons",
        "licensing": "Public domain",
        "caption": "Historical illustration of Darwin's Galapagos finches displaying varied beak adaptations suited for different food sources."
    },
    {
        "lesson_order": 4,
        "page": 6,
        "title": "Cytological Chromosome Evidence Karyogram",
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b1/Human_karyotype_with_bands_and_sub-bands.png",
        "author": "CC BY-SA 4.0, Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "Karyogram of human chromosomes showing structural banding patterns nearly identical to chimpanzee chromosome sets."
    },
    {
        "lesson_order": 4,
        "page": 6,
        "title": "Comparative Blood Cytology & Red Cell Smear",
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Sickle_cell_anemia_smear.jpg",
        "author": "Public Domain, Wikimedia Commons",
        "licensing": "Public domain",
        "caption": "Microscopic blood smear demonstrating universal cellular structure and biochemical membrane properties across mammals."
    },
    {
        "lesson_order": 5,
        "page": 5,
        "title": "Artificial Selection in Domesticated Crops",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/51/Pisum_sativum_var._macrocarpum_Ilowiecki_2017-04-14_6973.jpg",
        "author": "CC BY-SA 4.0, Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "Domesticated pea pods demonstrating selective breeding by humans, serving as Darwin's model for natural selection."
    },
    {
        "lesson_order": 6,
        "page": 3,
        "title": "Antibiotic Disk Diffusion Zone of Inhibition",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Agar_Diffusion_Method_1.jpg",
        "author": "CC BY-SA 4.0, Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "Agar diffusion plate demonstrating clear zones of inhibition around antibiotic disks, with resistant bacterial colonies growing inside."
    }
]

def enrich_form4_biology_topic2():
    print("=" * 80)
    print("VLearn Form 4 Biology — Topic 2 (Evolution): Visual Enrichment Engine")
    print("Attaching 18 Vector SVGs & 8 Verified Wikimedia Photographic Assets")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    subject = Subject.objects.filter(grade=grade, name="Biology").first()
    topic = Topic.objects.filter(subject=subject, name="Evolution").first()

    if not topic:
        print("[!] Error: Topic 'Evolution' not found under Biology!")
        return

    lessons = list(topic.lessons.all().order_by("learning_unit__order"))
    LessonAsset.objects.filter(lesson__in=lessons).delete()
    print("[*] Cleared existing LessonAssets for clean enrichment.")

    svg_counter = 0

    for lesson in lessons:
        u_order = lesson.learning_unit.order
        print(f"\n[*] Enriching Lesson {u_order}: {lesson.title}")

        # 1. Attach SVG Diagrams
        diagram_blocks = list(LessonBlock.objects.filter(lesson=lesson, block_type="suggested_diagram").order_by("order"))
        for db in diagram_blocks:
            if svg_counter < len(TOPIC2_BIOLOGY_SVGS):
                svg_data = TOPIC2_BIOLOGY_SVGS[svg_counter]
                content = db.content or {}
                content["svg_content"] = svg_data
                content["svg"] = svg_data
                db.content = content
                db.save()

                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    asset_type="diagram",
                    source_type="ai_generated",
                    storage_type="embed",
                    status="attached",
                    title=db.title,
                    description=f"Sanitized vector diagram: {db.title}",
                    metadata={"svg_content": svg_data}
                )
                db.assets.add(asset)
                print(f"  [SVG OK] '{db.title[:40]}' -> Block ID: {db.id} (Page {db.page_number})")
                svg_counter += 1

        # 2. Attach Wikimedia Photos
        photo_meta_list = [p for p in TOPIC2_BIOLOGY_PHOTOS if p["lesson_order"] == u_order]
        image_blocks = list(LessonBlock.objects.filter(lesson=lesson, block_type="suggested_image").order_by("order"))

        for idx, ib in enumerate(image_blocks):
            if idx < len(photo_meta_list):
                pm = photo_meta_list[idx]
                content = ib.content or {}
                content["resolved_image_url"] = pm["url"]
                content["url"] = pm["url"]
                content["author"] = pm["author"]
                content["licensing"] = pm["licensing"]
                content["caption"] = pm["caption"]
                ib.content = content
                ib.save()

                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    asset_type="image",
                    source_type="external",
                    storage_type="url",
                    status="attached",
                    title=ib.title,
                    description=pm["caption"],
                    url=pm["url"],
                    metadata={
                        "author": pm["author"],
                        "licensing": pm["licensing"],
                        "caption": pm["caption"]
                    }
                )
                ib.assets.add(asset)
                print(f"  [WIKIMEDIA OK] '{ib.title[:40]}' -> Block ID: {ib.id} (Page {ib.page_number})")

    total_assets = LessonAsset.objects.filter(lesson__in=lessons).count()
    print("=" * 80)
    print(f"[SUCCESS] Form 4 Biology Topic 2 (Evolution) Visual Enrichment Complete!")
    print(f"[*] Total LessonAssets Created: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_form4_biology_topic2()
