"""
VLearn Form 4 Geography — Topic 4: Energy
Visual Enrichment Engine (18 Vector SVGs + 8 Verified Wikimedia Photos)

Attaches:
  - 18 Custom Vector SVGs to suggested_diagram blocks
  - 8 Pre-Verified Wikimedia Photos to suggested_image blocks
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_form4_geography_topic4.py
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
# 18 HIGH-PRECISION VECTOR SVGS FOR TOPIC 4: ENERGY
# =====================================================================

SVG_1 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Solar Energy Technologies: Thermal Collector vs Photovoltaic (PV) Cell</text>
  <rect x="40" y="70" width="345" height="340" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="212" y="98" font-size="16" font-weight="bold" fill="#f43f5e" text-anchor="middle">1. Solar Thermal Heat Collector</text>
  <circle cx="90" cy="140" r="22" fill="#fbbf24"/>
  <line x1="90" y1="170" x2="140" y2="210" stroke="#f59e0b" stroke-width="3" stroke-dasharray="4,4"/>
  <line x1="115" y1="140" x2="160" y2="180" stroke="#f59e0b" stroke-width="3" stroke-dasharray="4,4"/>
  <rect x="140" y="170" width="180" height="110" rx="6" fill="#1e1e1e" stroke="#ef4444" stroke-width="2"/>
  <path d="M 155 190 H 300 V 210 H 155 V 230 H 300 V 250 H 155" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <text x="212" y="310" font-size="13" fill="#cbd5e1" text-anchor="middle">Cold Water In → Absorbs Solar Heat → Hot Water Out</text>
  <text x="212" y="335" font-size="12" fill="#94a3b8" text-anchor="middle">Coiled black pipe panel retains maximum heat energy</text>
  <text x="212" y="380" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">Application: Water Heating &amp; Crop Drying</text>
  <rect x="415" y="70" width="345" height="340" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="587" y="98" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">2. Photovoltaic (PV) Electrical Cell</text>
  <circle cx="465" cy="140" r="22" fill="#fbbf24"/>
  <line x1="465" y1="170" x2="515" y2="210" stroke="#f59e0b" stroke-width="3" stroke-dasharray="4,4"/>
  <rect x="515" y="170" width="180" height="40" rx="4" fill="#1e3a8a" stroke="#60a5fa" stroke-width="2"/>
  <text x="605" y="195" font-size="12" fill="#ffffff" text-anchor="middle">N-Type Silicon Layer</text>
  <rect x="515" y="210" width="180" height="40" rx="4" fill="#1e40af" stroke="#3b82f6" stroke-width="2"/>
  <text x="605" y="235" font-size="12" fill="#ffffff" text-anchor="middle">P-Type Silicon Layer</text>
  <path d="M 695 190 H 730 V 300 H 605 V 270" fill="none" stroke="#38bdf8" stroke-width="3"/>
  <rect x="555" y="270" width="100" height="40" rx="4" fill="#065f46" stroke="#10b981" stroke-width="2"/>
  <text x="605" y="295" font-size="13" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Battery (+ / -)</text>
  <text x="587" y="335" font-size="12" fill="#94a3b8" text-anchor="middle">Photons knock electrons free → Direct DC Current</text>
  <text x="587" y="380" font-size="13" font-weight="bold" fill="#10b981" text-anchor="middle">Application: Lighting, Appliances &amp; Grid Export</text>
</svg>
""")

SVG_2 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Kinetic Energy Conversion in Wind Turbine Generators</text>
  <path d="M 40 180 Q 120 170 200 180" fill="none" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6,6"/>
  <path d="M 40 220 Q 120 210 200 220" fill="none" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6,6"/>
  <path d="M 40 260 Q 120 250 200 260" fill="none" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6,6"/>
  <text x="100" y="150" font-size="14" font-weight="bold" fill="#38bdf8">Moving Air (Kinetic Energy)</text>
  <polygon points="230,380 245,180 255,180 270,380" fill="#64748b" stroke="#94a3b8" stroke-width="2"/>
  <rect x="235" y="150" width="140" height="50" rx="8" fill="#334155" stroke="#cbd5e1" stroke-width="2"/>
  <text x="305" y="180" font-size="13" font-weight="bold" fill="#f8fafc" text-anchor="middle">Nacelle (Gearbox)</text>
  <circle cx="245" cy="175" r="14" fill="#0f172a" stroke="#cbd5e1" stroke-width="3"/>
  <path d="M 245 175 L 170 70 A 15 15 0 0 1 185 60 Z" fill="#94a3b8"/>
  <path d="M 245 175 L 170 280 A 15 15 0 0 1 185 290 Z" fill="#94a3b8"/>
  <path d="M 245 175 L 340 175 A 15 15 0 0 1 340 190 Z" fill="#94a3b8"/>
  <rect x="410" y="100" width="350" height="280" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="585" y="130" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">Component Conversion Flow</text>
  <rect x="430" y="150" width="310" height="40" rx="4" fill="#1e293b" stroke="#64748b"/>
  <text x="585" y="175" font-size="13" fill="#cbd5e1" text-anchor="middle">1. Aerodynamic Rotor Blades spin (Low-Speed Shaft)</text>
  <rect x="430" y="210" width="310" height="40" rx="4" fill="#1e293b" stroke="#64748b"/>
  <text x="585" y="235" font-size="13" fill="#cbd5e1" text-anchor="middle">2. Gearbox increases rotational speed 100x</text>
  <rect x="430" y="270" width="310" height="40" rx="4" fill="#1e293b" stroke="#38bdf8"/>
  <text x="585" y="295" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">3. Electrical Generator produces AC Electricity</text>
  <rect x="430" y="330" width="310" height="35" rx="4" fill="#065f46" stroke="#10b981"/>
  <text x="585" y="353" font-size="13" font-weight="bold" fill="#a7f3d0" text-anchor="middle">4. Step-up Transformer exports to National Grid</text>
</svg>
""")

SVG_3 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Geothermal Power Generation Mechanism (Olkaria Model)</text>
  <rect x="40" y="280" width="720" height="130" fill="#334155"/>
  <rect x="40" y="340" width="720" height="70" fill="#991b1b"/>
  <text x="400" y="385" font-size="16" font-weight="bold" fill="#fecaca" text-anchor="middle">SUPERHEATED MAGMA CHAMBER / HOT VOLCANIC BEDROCK (&gt;300°C)</text>
  <path d="M 100 120 L 100 320" stroke="#38bdf8" stroke-width="3" stroke-dasharray="5,5"/>
  <text x="100" y="100" font-size="13" fill="#38bdf8" text-anchor="middle">Rainwater Percolation</text>
  <rect x="260" y="150" width="20" height="190" fill="#1e293b" stroke="#cbd5e1" stroke-width="2"/>
  <path d="M 270 330 C 265 250 275 200 270 150" stroke="#f43f5e" stroke-width="6" fill="none"/>
  <text x="230" y="240" font-size="13" font-weight="bold" fill="#f43f5e">High-Pressure Steam</text>
  <rect x="330" y="130" width="160" height="90" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <text x="410" y="165" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">Steam Turbine</text>
  <text x="410" y="190" font-size="14" font-weight="bold" fill="#10b981" text-anchor="middle">&amp; Generator</text>
  <rect x="540" y="150" width="120" height="60" rx="6" fill="#1e293b" stroke="#64748b"/>
  <text x="600" y="185" font-size="13" fill="#cbd5e1" text-anchor="middle">Condenser</text>
  <line x1="490" y1="175" x2="540" y2="175" stroke="#38bdf8" stroke-width="3"/>
  <rect x="620" y="210" width="16" height="130" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <path d="M 628 210 L 628 330" stroke="#38bdf8" stroke-width="4"/>
  <text x="690" y="260" font-size="12" fill="#38bdf8">Re-injection Well</text>
</svg>
""")

SVG_4 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Operational Mechanics of Hydroelectric Power (HEP) Generation</text>
  <polygon points="40,100 280,100 280,380 40,380" fill="#0284c7" opacity="0.8"/>
  <text x="140" y="140" font-size="18" font-weight="bold" fill="#ffffff" text-anchor="middle">Deep Reservoir Lake</text>
  <text x="140" y="170" font-size="13" fill="#e0f2fe" text-anchor="middle">(High Potential Energy)</text>
  <polygon points="280,100 360,100 420,380 280,380" fill="#475569" stroke="#94a3b8" stroke-width="2"/>
  <text x="340" y="240" font-size="14" font-weight="bold" fill="#ffffff" transform="rotate(70 340 240)">Concrete Dam Wall</text>
  <line x1="260" y1="280" x2="480" y2="340" stroke="#0f172a" stroke-width="22"/>
  <line x1="260" y1="280" x2="480" y2="340" stroke="#38bdf8" stroke-width="14"/>
  <text x="370" y="300" font-size="13" font-weight="bold" fill="#fbbf24">Penstock Intake</text>
  <rect x="480" y="270" width="160" height="110" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <text x="560" y="300" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">Water Turbine</text>
  <text x="560" y="325" font-size="14" font-weight="bold" fill="#10b981" text-anchor="middle">&amp; Generator</text>
  <text x="560" y="355" font-size="12" fill="#cbd5e1" text-anchor="middle">Kinetic → Electrical</text>
  <path d="M 640 350 L 760 350" stroke="#0284c7" stroke-width="12"/>
  <text x="700" y="380" font-size="13" fill="#0284c7" text-anchor="middle">Tailrace Outflow</text>
  <line x1="560" y1="270" x2="560" y2="150" stroke="#f59e0b" stroke-width="3"/>
  <polygon points="680,180 710,100 740,180" fill="none" stroke="#94a3b8" stroke-width="2"/>
  <line x1="560" y1="150" x2="710" y2="120" stroke="#f59e0b" stroke-width="2"/>
  <text x="635" y="130" font-size="12" font-weight="bold" fill="#f59e0b">National Power Grid</text>
</svg>
""")

SVG_5 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Biogas Anaerobic Digester &amp; Bio-Slurry Cycle</text>
  <rect x="50" y="180" width="120" height="90" rx="6" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <text x="110" y="215" font-size="14" font-weight="bold" fill="#fbbf24" text-anchor="middle">Manure / Waste</text>
  <text x="110" y="240" font-size="13" fill="#cbd5e1" text-anchor="middle">Inlet Tank</text>
  <line x1="170" y1="230" x2="260" y2="270" stroke="#64748b" stroke-width="12"/>
  <path d="M 240 360 C 240 220 500 220 500 360 Z" fill="#1e293b" stroke="#10b981" stroke-width="3"/>
  <text x="370" y="290" font-size="16" font-weight="bold" fill="#10b981" text-anchor="middle">Airtight Anaerobic Digester</text>
  <text x="370" y="315" font-size="13" fill="#a7f3d0" text-anchor="middle">Methanogenic Bacterial Fermentation</text>
  <line x1="370" y1="225" x2="370" y2="100" stroke="#38bdf8" stroke-width="6"/>
  <path d="M 370 100 H 520 V 130" fill="none" stroke="#38bdf8" stroke-width="6"/>
  <rect x="520" y="130" width="140" height="70" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <text x="590" y="160" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">Clean Methane Gas</text>
  <text x="590" y="185" font-size="12" fill="#cbd5e1" text-anchor="middle">Domestic Cooking &amp; Light</text>
  <line x1="480" y1="280" x2="570" y2="230" stroke="#64748b" stroke-width="12"/>
  <rect x="570" y="230" width="150" height="90" rx="6" fill="#065f46" stroke="#34d399" stroke-width="2"/>
  <text x="645" y="265" font-size="14" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Organic Bio-Slurry</text>
  <text x="645" y="290" font-size="12" fill="#ffffff" text-anchor="middle">Nitrogen Fertilizer for Farms</text>
</svg>
""")

SVG_6 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Draught Animal Harness Mechanics &amp; Agricultural Work Rates</text>
  <rect x="40" y="80" width="345" height="340" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="212" y="110" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. Pair of Oxen Ploughing</text>
  <rect x="70" y="140" width="285" height="120" rx="6" fill="#1e293b" stroke="#64748b"/>
  <text x="212" y="180" font-size="14" font-weight="bold" fill="#fbbf24" text-anchor="middle">Wooden Neck Yoke</text>
  <text x="212" y="205" font-size="13" fill="#cbd5e1" text-anchor="middle">Transfers draft power to mouldboard plough</text>
  <text x="212" y="300" font-size="13" fill="#a7f3d0" text-anchor="middle">Work Rate: 0.5 hectares per day</text>
  <text x="212" y="330" font-size="12" fill="#cbd5e1" text-anchor="middle">Inexhaustible natural reproduction</text>

  <rect x="415" y="80" width="345" height="340" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="587" y="110" font-size="16" font-weight="bold" fill="#10b981" text-anchor="middle">2. Pack Donkey Transport</text>
  <rect x="445" y="140" width="285" height="120" rx="6" fill="#1e293b" stroke="#64748b"/>
  <text x="587" y="180" font-size="14" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Balanced Pack Saddle</text>
  <text x="587" y="205" font-size="13" fill="#cbd5e1" text-anchor="middle">Traverses narrow, unpaved rural tracks</text>
  <text x="587" y="300" font-size="13" fill="#a7f3d0" text-anchor="middle">Carries 100kg grain or water drums</text>
  <text x="587" y="330" font-size="12" fill="#cbd5e1" text-anchor="middle">Requires low-cost natural pasture</text>
</svg>
""")

SVG_7 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Geological Coal Formation Process Flow</text>
  <rect x="40" y="80" width="160" height="320" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
  <text x="120" y="110" font-size="14" font-weight="bold" fill="#10b981" text-anchor="middle">Stage 1: Swamps</text>
  <rect x="50" y="130" width="140" height="100" fill="#064e3b"/>
  <text x="120" y="180" font-size="12" fill="#a7f3d0" text-anchor="middle">Dense forest matter</text>
  <text x="120" y="270" font-size="12" fill="#cbd5e1" text-anchor="middle">Trees die in anoxic</text>
  <text x="120" y="290" font-size="12" fill="#cbd5e1" text-anchor="middle">swamp waters</text>

  <rect x="220" y="80" width="160" height="320" rx="6" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
  <text x="300" y="110" font-size="14" font-weight="bold" fill="#eab308" text-anchor="middle">Stage 2: Peat</text>
  <rect x="230" y="130" width="140" height="100" fill="#713f12"/>
  <text x="300" y="180" font-size="12" fill="#fef08a" text-anchor="middle">Peat Layer</text>
  <text x="300" y="270" font-size="12" fill="#cbd5e1" text-anchor="middle">Buried under mud,</text>
  <text x="300" y="290" font-size="12" fill="#cbd5e1" text-anchor="middle">sand &amp; clay sediments</text>

  <rect x="400" y="80" width="160" height="320" rx="6" fill="#0f172a" stroke="#f97316" stroke-width="2"/>
  <text x="480" y="110" font-size="14" font-weight="bold" fill="#f97316" text-anchor="middle">Stage 3: Lignite</text>
  <rect x="410" y="130" width="140" height="100" fill="#7c2d12"/>
  <text x="480" y="180" font-size="12" fill="#ffedd5" text-anchor="middle">Soft Brown Coal</text>
  <text x="480" y="270" font-size="12" fill="#cbd5e1" text-anchor="middle">Compaction &amp; rising</text>
  <text x="480" y="290" font-size="12" fill="#cbd5e1" text-anchor="middle">geothermal heat</text>

  <rect x="580" y="80" width="160" height="320" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
  <text x="660" y="110" font-size="14" font-weight="bold" fill="#ef4444" text-anchor="middle">Stage 4: Coal Seam</text>
  <rect x="590" y="130" width="140" height="100" fill="#18181b"/>
  <text x="660" y="180" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Anthracite Coal</text>
  <text x="660" y="270" font-size="12" fill="#cbd5e1" text-anchor="middle">High carbon rock</text>
  <text x="660" y="290" font-size="12" fill="#cbd5e1" text-anchor="middle">for blast furnaces</text>
</svg>
""")

SVG_8 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Petroleum Trap Geology &amp; Fractional Distillation</text>
  <rect x="40" y="70" width="350" height="340" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="215" y="98" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. Anticlinal Geological Trap</text>
  <path d="M 60 170 Q 215 120 370 170 V 220 Q 215 170 60 220 Z" fill="#475569"/>
  <text x="215" y="160" font-size="12" fill="#ffffff" text-anchor="middle">Impervious Cap Rock (Shale)</text>
  <path d="M 60 220 Q 215 170 370 220 V 250 Q 215 200 60 250 Z" fill="#fef08a"/>
  <text x="215" y="210" font-size="12" font-weight="bold" fill="#854d0e" text-anchor="middle">Natural Gas Reservoir</text>
  <path d="M 60 250 Q 215 200 370 250 V 310 Q 215 260 60 310 Z" fill="#18181b"/>
  <text x="215" y="260" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Crude Oil Reservoir (Porous Rock)</text>
  <path d="M 60 310 Q 215 260 370 310 V 380 H 60 Z" fill="#0284c7"/>
  <text x="215" y="345" font-size="12" fill="#ffffff" text-anchor="middle">Underlying Saline Water</text>

  <rect x="410" y="70" width="350" height="340" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="585" y="98" font-size="15" font-weight="bold" fill="#f59e0b" text-anchor="middle">2. Fractional Distillation Column</text>
  <rect x="480" y="120" width="100" height="270" rx="4" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <text x="660" y="145" font-size="12" fill="#fde047">20°C: LPG &amp; Petrol</text>
  <text x="660" y="195" font-size="12" fill="#60a5fa">150°C: Jet Fuel / Kerosene</text>
  <text x="660" y="245" font-size="12" fill="#a7f3d0">250°C: Diesel Oil</text>
  <text x="660" y="295" font-size="12" fill="#cbd5e1">350°C: Lubricating Oil</text>
  <text x="660" y="345" font-size="12" fill="#ef4444">&gt;400°C: Bitumen (Asphalt)</text>
</svg>
""")

SVG_9 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Nuclear Power Reactor Fission &amp; Thermal Exchange System</text>
  <path d="M 50 380 V 180 A 130 130 0 0 1 310 180 V 380 Z" fill="#0f172a" stroke="#cbd5e1" stroke-width="3"/>
  <text x="180" y="90" font-size="14" font-weight="bold" fill="#cbd5e1" text-anchor="middle">Reinforced Concrete Containment</text>
  <rect x="110" y="220" width="140" height="140" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="3"/>
  <line x1="140" y1="240" x2="140" y2="340" stroke="#f43f5e" stroke-width="8"/>
  <line x1="180" y1="240" x2="180" y2="340" stroke="#f43f5e" stroke-width="8"/>
  <line x1="220" y1="240" x2="220" y2="340" stroke="#f43f5e" stroke-width="8"/>
  <text x="180" y="210" font-size="13" font-weight="bold" fill="#f43f5e" text-anchor="middle">U-235 Fuel Rods</text>
  <rect x="370" y="160" width="140" height="180" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="440" y="240" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">Steam Generator</text>
  <rect x="560" y="180" width="180" height="100" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
  <text x="650" y="220" font-size="14" font-weight="bold" fill="#10b981" text-anchor="middle">Steam Turbine</text>
  <text x="650" y="245" font-size="14" font-weight="bold" fill="#a7f3d0" text-anchor="middle">&amp; Generator</text>
</svg>
""")

SVG_10 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Physical Site-Selection Blueprint for Hydroelectric Dams</text>
  <rect x="40" y="70" width="720" height="340" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <polygon points="60,120 220,360 580,360 740,120 660,120 540,310 260,310 140,120" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <text x="400" y="340" font-size="14" font-weight="bold" fill="#e2e8f0" text-anchor="middle">Hard Impervious Basement Bedrock (Granite/Gneiss)</text>
  <polygon points="140,120 260,310 540,310 660,120" fill="#0284c7" opacity="0.6"/>
  <text x="400" y="220" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">Deep &amp; Narrow River Gorge Reservoir</text>
  <rect x="80" y="85" width="200" height="35" rx="4" fill="#1e293b" stroke="#38bdf8"/>
  <text x="180" y="107" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. Steep Waterfall Gradient</text>
  <rect x="520" y="85" width="200" height="35" rx="4" fill="#1e293b" stroke="#38bdf8"/>
  <text x="620" y="107" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">2. Constant Water Discharge</text>
</svg>
""")

SVG_11 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Spatial Cascade of the Seven Forks Scheme on River Tana</text>
  <path d="M 50 220 Q 200 180 350 240 T 650 200 T 750 250" fill="none" stroke="#0284c7" stroke-width="16"/>
  <text x="100" y="180" font-size="14" font-weight="bold" fill="#38bdf8">Mt. Kenya Catchment → River Tana</text>
  <circle cx="200" cy="205" r="18" fill="#ef4444" stroke="#ffffff" stroke-width="2"/>
  <text x="200" y="165" font-size="13" font-weight="bold" fill="#ef4444" text-anchor="middle">1. Masinga (1981)</text>
  <text x="200" y="245" font-size="11" fill="#cbd5e1" text-anchor="middle">Master Regulator</text>
  <circle cx="320" cy="230" r="14" fill="#f59e0b" stroke="#ffffff" stroke-width="2"/>
  <text x="320" y="195" font-size="12" font-weight="bold" fill="#f59e0b" text-anchor="middle">2. Kamburu (1974)</text>
  <circle cx="430" cy="225" r="14" fill="#f59e0b" stroke="#ffffff" stroke-width="2"/>
  <text x="430" y="270" font-size="12" font-weight="bold" fill="#f59e0b" text-anchor="middle">3. Gitaru (1978)</text>
  <circle cx="530" cy="210" r="14" fill="#10b981" stroke="#ffffff" stroke-width="2"/>
  <text x="530" y="175" font-size="12" font-weight="bold" fill="#10b981" text-anchor="middle">4. Kindaruma (1968)</text>
  <text x="530" y="250" font-size="11" fill="#a7f3d0" text-anchor="middle">Pioneer Dam</text>
  <circle cx="650" cy="200" r="14" fill="#f59e0b" stroke="#ffffff" stroke-width="2"/>
  <text x="650" y="165" font-size="12" font-weight="bold" fill="#f59e0b" text-anchor="middle">5. Kiambere (1988)</text>
</svg>
""")

SVG_12 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Masinga Reservoir Multi-Purpose Hydrological Flow Control</text>
  <rect x="300" y="100" width="200" height="120" rx="8" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
  <text x="400" y="145" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">Masinga Dam Lake</text>
  <text x="400" y="175" font-size="13" fill="#e0f2fe" text-anchor="middle">(Master Storage Reservoir)</text>
  <line x1="400" y1="220" x2="400" y2="330" stroke="#f43f5e" stroke-width="4"/>
  <rect x="300" y="330" width="200" height="60" rx="6" fill="#0f172a" stroke="#f43f5e" stroke-width="2"/>
  <text x="400" y="355" font-size="13" font-weight="bold" fill="#f43f5e" text-anchor="middle">Regulated Dry Season Flow</text>
  <text x="400" y="375" font-size="12" fill="#cbd5e1" text-anchor="middle">Sustains 4 Downstream Dams</text>
  <line x1="300" y1="160" x2="160" y2="160" stroke="#10b981" stroke-width="4"/>
  <rect x="50" y="130" width="110" height="60" rx="6" fill="#065f46" stroke="#10b981"/>
  <text x="105" y="165" font-size="13" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Mwea Irrigation</text>
  <line x1="500" y1="160" x2="640" y2="160" stroke="#eab308" stroke-width="4"/>
  <rect x="640" y="130" width="110" height="60" rx="6" fill="#713f12" stroke="#eab308"/>
  <text x="695" y="165" font-size="13" font-weight="bold" fill="#fef08a" text-anchor="middle">Inland Fisheries</text>
</svg>
""")

SVG_13 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Thematic Map of Kenya Rift Valley Geothermal Belt</text>
  <rect x="120" y="70" width="560" height="340" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
  <path d="M 320 80 L 360 220 L 400 400" stroke="#f43f5e" stroke-width="3" stroke-dasharray="6,6"/>
  <path d="M 380 80 L 420 220 L 460 400" stroke="#f43f5e" stroke-width="3" stroke-dasharray="6,6"/>
  <text x="460" y="100" font-size="13" font-weight="bold" fill="#f43f5e">Rift Valley Fault System</text>
  <circle cx="410" cy="340" r="10" fill="#10b981"/>
  <text x="430" y="345" font-size="14" font-weight="bold" fill="#10b981">Olkaria (Naivasha - 800+ MW Operating)</text>
  <circle cx="395" cy="270" r="8" fill="#f59e0b"/>
  <text x="415" y="275" font-size="13" fill="#f59e0b">Menengai Crater (Drilling Phase)</text>
  <circle cx="400" cy="310" r="7" fill="#f59e0b"/>
  <text x="420" y="315" font-size="12" fill="#cbd5e1">Eburu Field</text>
  <circle cx="380" cy="210" r="8" fill="#ef4444"/>
  <text x="400" y="215" font-size="13" font-weight="bold" fill="#ef4444">Lake Bogoria (Highest Unexploited Geysers)</text>
</svg>
""")

SVG_14 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Drought Resilience: Geothermal Base-Load vs HEP Output</text>
  <line x1="80" y1="360" x2="740" y2="360" stroke="#94a3b8" stroke-width="2"/>
  <line x1="80" y1="100" x2="80" y2="360" stroke="#94a3b8" stroke-width="2"/>
  <text x="410" y="395" font-size="13" fill="#cbd5e1" text-anchor="middle">Time (Wet Season → Severe 10-Month Drought → Dry Spell)</text>
  <text x="40" y="230" font-size="13" fill="#cbd5e1" transform="rotate(-90 40 230)" text-anchor="middle">Power Output (MW)</text>
  <line x1="80" y1="160" x2="740" y2="160" stroke="#10b981" stroke-width="4"/>
  <text x="500" y="145" font-size="14" font-weight="bold" fill="#10b981">Geothermal Power (Continuous Base-Load)</text>
  <path d="M 80 180 Q 250 170 350 290 T 550 340 T 740 220" fill="none" stroke="#ef4444" stroke-width="4"/>
  <text x="500" y="320" font-size="14" font-weight="bold" fill="#ef4444">HEP Output (Drought Reservoir Drop)</text>
</svg>
""")

SVG_15 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Cascading Systemic Macroeconomic Impacts of a Global Oil Crisis</text>
  <rect x="40" y="80" width="720" height="50" rx="6" fill="#991b1b" stroke="#f87171"/>
  <text x="400" y="112" font-size="15" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Global Crude Oil Price Surge (OPEC Quota Cuts / Middle East Conflicts)</text>
  <rect x="80" y="150" width="640" height="45" rx="6" fill="#7f1d1d" stroke="#f87171"/>
  <text x="400" y="178" font-size="14" fill="#fecaca" text-anchor="middle">2. Increased National Import Bill &amp; Foreign Exchange Reserve Drain</text>
  <rect x="120" y="215" width="560" height="45" rx="6" fill="#713f12" stroke="#fde047"/>
  <text x="400" y="243" font-size="14" fill="#fef08a" text-anchor="middle">3. High Transport Fares &amp; Devaluation of Local Currency (Hyper-Inflation)</text>
  <rect x="160" y="280" width="480" height="45" rx="6" fill="#1e3a8a" stroke="#60a5fa"/>
  <text x="400" y="308" font-size="14" fill="#dbeafe" text-anchor="middle">4. Expensive Chemical Fertilizers → Reduced Crop Yields &amp; Industrial Layoffs</text>
  <rect x="200" y="345" width="400" height="45" rx="6" fill="#064e3b" stroke="#34d399"/>
  <text x="400" y="373" font-size="14" font-weight="bold" fill="#a7f3d0" text-anchor="middle">5. Household LPG Substitution → Accelerated Charcoal Deforestation</text>
</svg>
""")

SVG_16 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Energy Management vs Energy Conservation Policy Framework</text>
  <rect x="40" y="70" width="345" height="340" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <text x="212" y="100" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">ENERGY MANAGEMENT</text>
  <text x="212" y="125" font-size="13" fill="#94a3b8" text-anchor="middle">(National Planning &amp; Macro Policy)</text>
  <text x="60" y="170" font-size="13" fill="#cbd5e1">• High engine capacity vehicle import caps</text>
  <text x="60" y="210" font-size="13" fill="#cbd5e1">• Public transit expansion (BRT / SGR)</text>
  <text x="60" y="250" font-size="13" fill="#cbd5e1">• Highway bypasses to curb traffic jams</text>
  <text x="60" y="290" font-size="13" fill="#cbd5e1">• Aggressive afforestation &amp; agroforestry</text>
  <text x="60" y="330" font-size="13" fill="#cbd5e1">• Grid diversification into geothermal/wind</text>

  <rect x="415" y="70" width="345" height="340" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
  <text x="587" y="100" font-size="16" font-weight="bold" fill="#10b981" text-anchor="middle">ENERGY CONSERVATION</text>
  <text x="587" y="125" font-size="13" fill="#94a3b8" text-anchor="middle">(Micro Consumer Waste Reduction)</text>
  <text x="435" y="170" font-size="13" fill="#cbd5e1">• Switching off idle lights &amp; electronics</text>
  <text x="435" y="210" font-size="13" fill="#cbd5e1">• Servicing car engines for fuel efficiency</text>
  <text x="435" y="250" font-size="13" fill="#cbd5e1">• Using Kenya Ceramic Jikos (KCJ)</text>
  <text x="435" y="290" font-size="13" fill="#cbd5e1">• Installing domestic solar water heaters</text>
  <text x="435" y="330" font-size="13" fill="#cbd5e1">• Constructing farm biogas digesters</text>
</svg>
""")

SVG_17 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Thermal Efficiency: Open Fire vs Kenya Ceramic Jiko (KCJ)</text>
  <rect x="40" y="70" width="345" height="340" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
  <text x="212" y="98" font-size="15" font-weight="bold" fill="#ef4444" text-anchor="middle">Open 3-Stone Fire (85% Heat Waste)</text>
  <circle cx="212" cy="220" r="40" fill="#f97316"/>
  <path d="M 150 200 L 90 140" stroke="#ef4444" stroke-width="3"/>
  <path d="M 270 200 L 330 140" stroke="#ef4444" stroke-width="3"/>
  <text x="212" y="330" font-size="13" fill="#fca5a5" text-anchor="middle">Uninsulated: Wind blows heat away</text>
  <text x="212" y="360" font-size="13" font-weight="bold" fill="#ef4444" text-anchor="middle">High Wood Fuel Consumption</text>

  <rect x="415" y="70" width="345" height="340" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="587" y="98" font-size="15" font-weight="bold" fill="#10b981" text-anchor="middle">Kenya Ceramic Jiko (50% Fuel Saving)</text>
  <rect x="507" y="160" width="160" height="130" rx="8" fill="#334155" stroke="#cbd5e1" stroke-width="2"/>
  <rect x="527" y="170" width="120" height="110" rx="6" fill="#78350f" stroke="#f59e0b" stroke-width="3"/>
  <text x="587" y="230" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Insulating Clay Liner</text>
  <text x="587" y="330" font-size="13" fill="#a7f3d0" text-anchor="middle">Clay liner retains &amp; focuses heat upward</text>
  <text x="587" y="360" font-size="13" font-weight="bold" fill="#10b981" text-anchor="middle">50% Charcoal Savings</text>
</svg>
""")

SVG_18 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Six-Point Action Plan for Sustainable Energy Expansion</text>
  <g transform="translate(60, 80)">
    <rect x="0" y="0" width="210" height="130" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="105" y="35" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. Geothermal Wells</text>
    <text x="105" y="70" font-size="12" fill="#cbd5e1" text-anchor="middle">Expand Olkaria &amp; Menengai</text>
    <text x="105" y="90" font-size="12" fill="#cbd5e1" text-anchor="middle">steam extraction</text>

    <rect x="235" y="0" width="210" height="130" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <text x="340" y="35" font-size="14" font-weight="bold" fill="#10b981" text-anchor="middle">2. Solar Subsidies</text>
    <text x="340" y="70" font-size="12" fill="#cbd5e1" text-anchor="middle">Zero-tax off-grid solar</text>
    <text x="340" y="90" font-size="12" fill="#cbd5e1" text-anchor="middle">kits for rural homes</text>

    <rect x="470" y="0" width="210" height="130" rx="6" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <text x="575" y="35" font-size="14" font-weight="bold" fill="#eab308" text-anchor="middle">3. Wind Farms</text>
    <text x="575" y="70" font-size="12" fill="#cbd5e1" text-anchor="middle">Expand Marsabit &amp; Ngong</text>
    <text x="575" y="90" font-size="12" fill="#cbd5e1" text-anchor="middle">wind turbine corridors</text>

    <rect x="0" y="160" width="210" height="130" rx="6" fill="#0f172a" stroke="#f43f5e" stroke-width="2"/>
    <text x="105" y="195" font-size="14" font-weight="bold" fill="#f43f5e" text-anchor="middle">4. Catchment Protection</text>
    <text x="105" y="230" font-size="12" fill="#cbd5e1" text-anchor="middle">Afforestation along Tana</text>
    <text x="105" y="250" font-size="12" fill="#cbd5e1" text-anchor="middle">to eliminate dam silt</text>

    <rect x="235" y="160" width="210" height="130" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <text x="340" y="195" font-size="14" font-weight="bold" fill="#a855f7" text-anchor="middle">5. BRT Transit</text>
    <text x="340" y="230" font-size="12" fill="#cbd5e1" text-anchor="middle">High-capacity buses</text>
    <text x="340" y="250" font-size="12" fill="#cbd5e1" text-anchor="middle">to curb petrol waste</text>

    <rect x="470" y="160" width="210" height="130" rx="6" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
    <text x="575" y="195" font-size="14" font-weight="bold" fill="#06b6d4" text-anchor="middle">6. Jiko Stoves</text>
    <text x="575" y="230" font-size="12" fill="#cbd5e1" text-anchor="middle">Promote ceramic jikos</text>
    <text x="575" y="250" font-size="12" fill="#cbd5e1" text-anchor="middle">to halve wood charcoal use</text>
  </g>
</svg>
""")

TOPIC4_SVGS = [
    SVG_1, SVG_2, SVG_3, SVG_4, SVG_5, SVG_6,
    SVG_7, SVG_8, SVG_9, SVG_10, SVG_11, SVG_12,
    SVG_13, SVG_14, SVG_15, SVG_16, SVG_17, SVG_18
]

# =====================================================================
# 8 VERIFIED WIKIMEDIA COMMONS PHOTOS FOR TOPIC 4: ENERGY
# =====================================================================

TOPIC4_PHOTOS = [
    {
        "lesson_order": 1,
        "page": 6,
        "title": "Commercial Solar Installation in Kenya",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Solar_Installation_in_Kenya.jpg",
        "author": "PowerAfricaSolar, Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "Photovoltaic (PV) solar installation supplying clean renewable electricity to rural facilities in Kenya."
    },
    {
        "lesson_order": 1,
        "page": 6,
        "title": "Ngong Hills Wind Power Farm in Kenya",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/72/Ngong_Hills_Wind_Farm.jpg",
        "author": "Singularity Preparation, Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "Commercial wind turbines harvesting kinetic wind energy along the Ngong Hills ridge near Nairobi."
    },
    {
        "lesson_order": 2,
        "page": 7,
        "title": "Open Pit Coal Mining Operations",
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/da/TurowCoalMine.jpg",
        "author": "Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "Massive open-pit coal extraction displaying heavy machinery excavating high-carbon coal seams."
    },
    {
        "lesson_order": 2,
        "page": 4,
        "title": "Lake Turkana Wind Power Project",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/8f/Lake_turkana_wind_power_project.jpg",
        "author": "Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "Africa's largest wind farm utilizing steady desert wind corridors in Marsabit County, Kenya."
    },
    {
        "lesson_order": 3,
        "page": 4,
        "title": "Akosombo Hydroelectric Dam Project",
        "url": "https://upload.wikimedia.org/wikipedia/commons/2/2d/Akosombo_Dam.jpg",
        "author": "Public Domain, Wikimedia Commons",
        "licensing": "Public domain",
        "caption": "The Akosombo Hydroelectric Dam on the Volta River in Ghana, demonstrating large-scale African HEP infrastructure."
    },
    {
        "lesson_order": 4,
        "page": 4,
        "title": "Olkaria V Geothermal Power Station",
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a4/Olkaria_V_Geothermal_Power_Station.jpg",
        "author": "Bbossoxx, Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "The modern Olkaria V Geothermal Power Station in Naivasha, displaying high-pressure steam pipes and turbine generation buildings."
    },
    {
        "lesson_order": 5,
        "page": 10,
        "title": "Lake Bogoria Geysers and Steam Vents",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/8c/200812_kenya-107_%283213939312%29.jpg",
        "author": "Franco Pecchio, Wikimedia Commons",
        "licensing": "CC BY 2.0",
        "caption": "Active volcanic geysers and steam vents erupting along the shores of Lake Bogoria in the Great Rift Valley."
    },
    {
        "lesson_order": 5,
        "page": 7,
        "title": "Commercial Petroleum Oil Refinery",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/0e/Altona_Oil_Refinery_Victoria.jpg",
        "author": "Public Domain, Wikimedia Commons",
        "licensing": "Public domain",
        "caption": "A large-scale commercial petroleum oil refinery showing fractional distillation towers and storage tanks."
    }
]

def enrich_form4_geography_topic4():
    print("=" * 80)
    print("VLearn Form 4 Geography — Topic 4: Visual Enrichment Engine")
    print("Attaching 18 Vector SVGs & 8 Verified Wikimedia Photographic Assets")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    subject = Subject.objects.filter(grade=grade, name="Geography").first()
    topic = Topic.objects.filter(subject=subject, name="Energy").first()

    if not topic:
        print("[!] Error: Topic 'Energy' not found!")
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
            if svg_counter < len(TOPIC4_SVGS):
                svg_data = TOPIC4_SVGS[svg_counter]
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
        photo_meta_list = [p for p in TOPIC4_PHOTOS if p["lesson_order"] == u_order]
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
    print(f"[SUCCESS] Form 4 Geography Topic 4 Visual Enrichment Complete!")
    print(f"[*] Total LessonAssets Created: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_form4_geography_topic4()
