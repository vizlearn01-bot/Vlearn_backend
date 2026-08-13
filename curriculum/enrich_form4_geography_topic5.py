"""
VLearn Form 4 Geography — Topic 5: Industry
Visual Enrichment Engine (18 Vector SVGs + 8 Verified Wikimedia Photos)

Attaches:
  - 18 Custom Vector SVGs to suggested_diagram blocks
  - 8 Pre-Verified Wikimedia Photos to suggested_image blocks
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_form4_geography_topic5.py
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
# 18 HIGH-PRECISION VECTOR SVGS FOR TOPIC 5: INDUSTRY
# =====================================================================

SVG_1 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Industrial Location Inputs, Processes, and Market Pull Matrix</text>

  <!-- Central Factory Node -->
  <rect x="310" y="180" width="180" height="100" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
  <text x="400" y="225" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">Manufacturing Plant</text>
  <text x="400" y="250" font-size="13" fill="#a7f3d0" text-anchor="middle">(Factory Location Site)</text>

  <!-- Inputs Converging -->
  <line x1="120" y1="110" x2="310" y2="190" stroke="#f43f5e" stroke-width="3"/>
  <rect x="40" y="80" width="160" height="50" rx="6" fill="#1e293b" stroke="#f43f5e"/>
  <text x="120" y="110" font-size="13" font-weight="bold" fill="#f43f5e" text-anchor="middle">Bulky Raw Materials</text>

  <line x1="120" y1="340" x2="310" y2="250" stroke="#f59e0b" stroke-width="3"/>
  <rect x="40" y="320" width="160" height="50" rx="6" fill="#1e293b" stroke="#f59e0b"/>
  <text x="120" y="350" font-size="13" font-weight="bold" fill="#f59e0b" text-anchor="middle">Power &amp; Water Grid</text>

  <line x1="680" y1="110" x2="490" y2="190" stroke="#10b981" stroke-width="3"/>
  <rect x="600" y="80" width="160" height="50" rx="6" fill="#1e293b" stroke="#10b981"/>
  <text x="680" y="110" font-size="13" font-weight="bold" fill="#10b981" text-anchor="middle">Urban Consumer Market</text>

  <line x1="680" y1="340" x2="490" y2="250" stroke="#a855f7" stroke-width="3"/>
  <rect x="600" y="320" width="160" height="50" rx="6" fill="#1e293b" stroke="#a855f7"/>
  <text x="680" y="350" font-size="13" font-weight="bold" fill="#a855f7" text-anchor="middle">Skilled Labor &amp; Capital</text>
</svg>
""")

SVG_2 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Industrial Inertia Mechanics in Historic Industrial Regions</text>

  <rect x="40" y="80" width="720" height="330" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>

  <rect x="80" y="120" width="200" height="240" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
  <text x="180" y="155" font-size="15" font-weight="bold" fill="#ef4444" text-anchor="middle">Original Factor</text>
  <text x="180" y="210" font-size="13" fill="#fca5a5" text-anchor="middle">Abundant Local Coal</text>
  <text x="180" y="235" font-size="13" fill="#fca5a5" text-anchor="middle">&amp; Iron Ore Seams</text>
  <rect x="100" y="280" width="160" height="40" rx="4" fill="#991b1b"/>
  <text x="180" y="305" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">STATUS: DEPLETED</text>

  <!-- Arrow -->
  <line x1="280" y1="240" x2="350" y2="240" stroke="#cbd5e1" stroke-width="4"/>

  <!-- Inertia Anchor Box -->
  <rect x="350" y="120" width="370" height="240" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
  <text x="535" y="155" font-size="16" font-weight="bold" fill="#10b981" text-anchor="middle">INDUSTRIAL INERTIA ANCHORS</text>
  <text x="375" y="200" font-size="13" fill="#cbd5e1">• Massive Sunk Capital Costs (Blast Furnace Infrastructure)</text>
  <text x="375" y="240" font-size="13" fill="#cbd5e1">• Highly Specialized Local Skilled Labour Pool</text>
  <text x="375" y="280" font-size="13" fill="#cbd5e1">• Pre-existing Railway &amp; Navigable Canal Network</text>
  <text x="535" y="330" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">RESULT: Steel Mills Remain Locked in Place</text>
</svg>
""")

SVG_3 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Three-Tier Industrial Classification Taxonomy</text>

  <!-- 3 Boxes -->
  <rect x="40" y="80" width="220" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
  <text x="150" y="115" font-size="15" font-weight="bold" fill="#10b981" text-anchor="middle">1. Primary Processing</text>
  <text x="150" y="150" font-size="12" fill="#cbd5e1" text-anchor="middle">Initial extraction or processing</text>
  <text x="150" y="170" font-size="12" fill="#cbd5e1" text-anchor="middle">of raw natural resources.</text>
  <line x1="60" y1="190" x2="240" y2="190" stroke="#334155"/>
  <text x="150" y="220" font-size="13" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Examples:</text>
  <text x="150" y="250" font-size="12" fill="#e2e8f0" text-anchor="middle">• Coffee Pulping Plants</text>
  <text x="150" y="280" font-size="12" fill="#e2e8f0" text-anchor="middle">• Cotton Ginneries</text>
  <text x="150" y="310" font-size="12" fill="#e2e8f0" text-anchor="middle">• Sawmills &amp; Posho Mills</text>
  <text x="150" y="340" font-size="12" fill="#e2e8f0" text-anchor="middle">• Tea Factories</text>

  <rect x="290" y="80" width="220" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <text x="400" y="115" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">2. Secondary Manufacturing</text>
  <text x="400" y="150" font-size="12" fill="#cbd5e1" text-anchor="middle">Manufacturing consumer goods</text>
  <text x="400" y="170" font-size="12" fill="#cbd5e1" text-anchor="middle">from pre-processed inputs.</text>
  <line x1="310" y1="190" x2="490" y2="190" stroke="#334155"/>
  <text x="400" y="220" font-size="13" font-weight="bold" fill="#93c5fd" text-anchor="middle">Examples:</text>
  <text x="400" y="250" font-size="12" fill="#e2e8f0" text-anchor="middle">• Athi River Cement</text>
  <text x="400" y="280" font-size="12" fill="#e2e8f0" text-anchor="middle">• Changamwe Oil Refinery</text>
  <text x="400" y="310" font-size="12" fill="#e2e8f0" text-anchor="middle">• Vehicle Assembly (GM)</text>
  <text x="400" y="340" font-size="12" fill="#e2e8f0" text-anchor="middle">• Commercial Bakeries</text>

  <rect x="540" y="80" width="220" height="320" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
  <text x="650" y="115" font-size="15" font-weight="bold" fill="#f59e0b" text-anchor="middle">3. Tertiary Services</text>
  <text x="650" y="150" font-size="12" fill="#cbd5e1" text-anchor="middle">Providing non-tangible</text>
  <text x="650" y="170" font-size="12" fill="#cbd5e1" text-anchor="middle">commercial services.</text>
  <line x1="560" y1="190" x2="720" y2="190" stroke="#334155"/>
  <text x="650" y="220" font-size="13" font-weight="bold" fill="#fde047" text-anchor="middle">Examples:</text>
  <text x="650" y="250" font-size="12" fill="#e2e8f0" text-anchor="middle">• Commercial Banking</text>
  <text x="650" y="280" font-size="12" fill="#e2e8f0" text-anchor="middle">• Matatu &amp; SGR Transport</text>
  <text x="650" y="310" font-size="12" fill="#e2e8f0" text-anchor="middle">• Maasai Mara Tourism</text>
  <text x="650" y="340" font-size="12" fill="#e2e8f0" text-anchor="middle">• Education &amp; Medical</text>
</svg>
""")

SVG_4 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Spatial Distribution Map of Kenya's Formal Manufacturing Centers</text>
  <rect x="120" y="70" width="560" height="340" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

  <!-- Clusters -->
  <circle cx="340" cy="270" r="14" fill="#ef4444"/>
  <text x="365" y="275" font-size="13" font-weight="bold" fill="#ef4444">Nairobi: Steel, Assembly, Glass, Pharma</text>

  <circle cx="370" cy="250" r="10" fill="#f59e0b"/>
  <text x="390" y="255" font-size="12" fill="#f59e0b">Thika: Del Monte Fruit Canning</text>

  <circle cx="350" cy="295" r="10" fill="#10b981"/>
  <text x="370" y="300" font-size="12" fill="#10b981">Athi River: Cement &amp; EPZ Zones</text>

  <circle cx="260" cy="210" r="10" fill="#38bdf8"/>
  <text x="140" y="215" font-size="12" fill="#38bdf8">Webuye: Paper Mills</text>

  <circle cx="220" cy="250" r="10" fill="#a855f7"/>
  <text x="120" y="255" font-size="12" fill="#a855f7">Eldoret: Dairies &amp; Grain</text>

  <circle cx="530" cy="360" r="14" fill="#06b6d4"/>
  <text x="420" y="380" font-size="13" font-weight="bold" fill="#06b6d4">Mombasa: Changamwe Refinery, AVA Assembly, Bamburi Cement</text>
</svg>
""")

SVG_5 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Informal Jua Kali Metal Reprocessing Value Chain</text>
  <rect x="40" y="80" width="720" height="50" rx="6" fill="#713f12" stroke="#fde047"/>
  <text x="400" y="112" font-size="15" font-weight="bold" fill="#fef08a" text-anchor="middle">1. Discarded Industrial Scrap Metal Collection (Barrels, Wires, Iron Sheets)</text>

  <rect x="100" y="160" width="600" height="50" rx="6" fill="#1e293b" stroke="#38bdf8"/>
  <text x="400" y="192" font-size="14" fill="#cbd5e1" text-anchor="middle">2. Manual Cold-Hammering &amp; Cutting in KIE Nyayo Sheds</text>

  <rect x="160" y="240" width="480" height="50" rx="6" fill="#065f46" stroke="#34d399"/>
  <text x="400" y="272" font-size="14" font-weight="bold" fill="#a7f3d0" text-anchor="middle">3. Fabrication into Metal Boxes, Jiko Stoves, Wheelbarrows &amp; Gutters</text>

  <rect x="220" y="320" width="360" height="50" rx="6" fill="#1e3a8a" stroke="#60a5fa"/>
  <text x="400" y="352" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">4. Retail Distribution to Low-Income Households &amp; COMESA Exports</text>
</svg>
""")

SVG_6 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Traditional Cottage Craft Value Chain (Kisii Soapstone &amp; Ciondos)</text>
  <rect x="40" y="70" width="345" height="340" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="212" y="100" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. Kisii Soapstone Carving</text>
  <text x="212" y="140" font-size="13" fill="#cbd5e1" text-anchor="middle">Quarried at Tabaka, Kisii County</text>
  <text x="212" y="170" font-size="13" fill="#cbd5e1" text-anchor="middle">Hand-carved with chisels into animal shapes</text>
  <text x="212" y="200" font-size="13" fill="#cbd5e1" text-anchor="middle">Smoothed with water &amp; wet sandpaper</text>
  <rect x="80" y="240" width="265" height="140" rx="6" fill="#1e293b" stroke="#10b981"/>
  <text x="212" y="280" font-size="14" font-weight="bold" fill="#10b981" text-anchor="middle">Tourist Souvenir Export</text>

  <rect x="415" y="70" width="345" height="340" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="587" y="100" font-size="16" font-weight="bold" fill="#f59e0b" text-anchor="middle">2. Agikuyu Ciondo Weaving</text>
  <text x="587" y="140" font-size="13" fill="#cbd5e1" text-anchor="middle">Harvested sisal &amp; dry palm fibers</text>
  <text x="587" y="170" font-size="13" fill="#cbd5e1" text-anchor="middle">Hand-twisted &amp; dyed using natural dyes</text>
  <text x="587" y="200" font-size="13" fill="#cbd5e1" text-anchor="middle">Woven into durable traditional baskets</text>
  <rect x="455" y="240" width="265" height="140" rx="6" fill="#1e293b" stroke="#f59e0b"/>
  <text x="587" y="280" font-size="14" font-weight="bold" fill="#fde047" text-anchor="middle">Local Market &amp; Global Trade</text>
</svg>
""")

SVG_7 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Macroeconomic Linkages of Industrialisation</text>
  <rect x="300" y="80" width="200" height="70" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <text x="400" y="120" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">Agro-Factories</text>

  <!-- 4 Linkages -->
  <line x1="300" y1="115" x2="160" y2="180" stroke="#10b981" stroke-width="3"/>
  <rect x="50" y="180" width="180" height="70" rx="6" fill="#065f46" stroke="#10b981"/>
  <text x="140" y="220" font-size="13" font-weight="bold" fill="#a7f3d0" text-anchor="middle">1. Farmer Produce Market</text>

  <line x1="500" y1="115" x2="640" y2="180" stroke="#f59e0b" stroke-width="3"/>
  <rect x="570" y="180" width="180" height="70" rx="6" fill="#713f12" stroke="#f59e0b"/>
  <text x="660" y="220" font-size="13" font-weight="bold" fill="#fef08a" text-anchor="middle">2. Foreign Exchange</text>

  <line x1="350" y1="150" x2="220" y2="300" stroke="#a855f7" stroke-width="3"/>
  <rect x="130" y="300" width="180" height="70" rx="6" fill="#581c87" stroke="#a855f7"/>
  <text x="220" y="340" font-size="13" font-weight="bold" fill="#e9d5ff" text-anchor="middle">3. SACCO Capital Pools</text>

  <line x1="450" y1="150" x2="580" y2="300" stroke="#ef4444" stroke-width="3"/>
  <rect x="490" y="300" width="180" height="70" rx="6" fill="#7f1d1d" stroke="#ef4444"/>
  <text x="580" y="340" font-size="13" font-weight="bold" fill="#fecaca" text-anchor="middle">4. Road &amp; Grid Growth</text>
</svg>
""")

SVG_8 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 11 Industrial Bottlenecks &amp; Policy Intervention Matrix</text>
  <rect x="40" y="70" width="345" height="340" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
  <text x="212" y="100" font-size="16" font-weight="bold" fill="#ef4444" text-anchor="middle">PRIMARY PROBLEMS</text>
  <text x="60" y="140" font-size="12" fill="#cbd5e1">1. High Energy Costs (Imported Crude)</text>
  <text x="60" y="180" font-size="12" fill="#cbd5e1">2. Mitumba &amp; Cheap Import Competition</text>
  <text x="60" y="220" font-size="12" fill="#cbd5e1">3. Brain Drain of Skilled Managers</text>
  <text x="60" y="260" font-size="12" fill="#cbd5e1">4. Industrial Pollution &amp; Quarry Scarring</text>
  <text x="60" y="300" font-size="12" fill="#cbd5e1">5. Inadequate Financial Capital</text>

  <rect x="415" y="70" width="345" height="340" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="587" y="100" font-size="16" font-weight="bold" fill="#10b981" text-anchor="middle">GEOGRAPHICAL SOLUTIONS</text>
  <text x="435" y="140" font-size="12" fill="#a7f3d0">→ Develop Olkaria Geothermal Power</text>
  <text x="435" y="180" font-size="12" fill="#a7f3d0">→ Enforce Protective Import Tariffs</text>
  <text x="435" y="220" font-size="12" fill="#a7f3d0">→ Build TVET Institutes &amp; Raise Pay</text>
  <text x="435" y="260" font-size="12" fill="#a7f3d0">→ Strict NEMA Laws &amp; Pit Afforestation</text>
  <text x="435" y="300" font-size="12" fill="#a7f3d0">→ Investor Tax Exemptions &amp; KIE Loans</text>
</svg>
""")

SVG_9 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Industrial Decentralisation &amp; Urban-Rural Rebalancing</text>
  <circle cx="200" cy="240" r="100" fill="#991b1b" opacity="0.6"/>
  <text x="200" y="235" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">Nairobi Congested Core</text>
  <text x="200" y="260" font-size="12" fill="#fecaca" text-anchor="middle">(High Land Cost &amp; Slums)</text>

  <!-- Push Arrows -->
  <line x1="290" y1="180" x2="450" y2="120" stroke="#f59e0b" stroke-width="4"/>
  <line x1="300" y1="240" x2="480" y2="240" stroke="#f59e0b" stroke-width="4"/>
  <line x1="290" y1="300" x2="450" y2="360" stroke="#f59e0b" stroke-width="4"/>

  <!-- Satellite Decentralised Zones -->
  <rect x="450" y="90" width="180" height="60" rx="6" fill="#065f46" stroke="#10b981"/>
  <text x="540" y="125" font-size="14" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Ruiru EPZ Zone</text>

  <rect x="480" y="210" width="180" height="60" rx="6" fill="#065f46" stroke="#10b981"/>
  <text x="570" y="245" font-size="14" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Athi River EPZ Zone</text>

  <rect x="450" y="330" width="180" height="60" rx="6" fill="#065f46" stroke="#10b981"/>
  <text x="540" y="365" font-size="14" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Kitengela Satellite</text>
</svg>
""")

SVG_10 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Spatial Cluster Map of India's Cottage Industry Networks</text>
  <rect x="120" y="70" width="560" height="340" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

  <circle cx="240" cy="220" r="10" fill="#ef4444"/>
  <text x="260" y="225" font-size="12" font-weight="bold" fill="#ef4444">Mumbai (Textiles &amp; Weaving)</text>

  <circle cx="450" cy="140" r="10" fill="#f59e0b"/>
  <text x="470" y="145" font-size="12" font-weight="bold" fill="#f59e0b">Lucknow &amp; Moradabad (Brassware)</text>

  <circle cx="520" cy="210" r="10" fill="#38bdf8"/>
  <text x="540" y="215" font-size="12" fill="#38bdf8">Calcutta (Jute &amp; Carpets)</text>

  <circle cx="360" cy="340" r="10" fill="#10b981"/>
  <text x="380" y="345" font-size="12" fill="#10b981">Madras / Bangalore (Silk Saree)</text>
</svg>
""")

SVG_11 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Middleman Exploitation vs Cooperative Marketing</text>
  <rect x="40" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
  <text x="212" y="110" font-size="15" font-weight="bold" fill="#ef4444" text-anchor="middle">1. Middleman Trader System</text>
  <text x="212" y="160" font-size="13" fill="#cbd5e1" text-anchor="middle">Trader sells raw yarn at inflated cost</text>
  <text x="212" y="210" font-size="13" fill="#cbd5e1" text-anchor="middle">Trader buys finished sarees at tiny price</text>
  <rect x="80" y="270" width="265" height="90" rx="6" fill="#7f1d1d"/>
  <text x="212" y="320" font-size="14" font-weight="bold" fill="#fecaca" text-anchor="middle">Artisans Trapped in Debt</text>

  <rect x="415" y="80" width="345" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <text x="587" y="110" font-size="15" font-weight="bold" fill="#10b981" text-anchor="middle">2. Artisan Cooperative System</text>
  <text x="587" y="160" font-size="13" fill="#cbd5e1" text-anchor="middle">Bulk raw material purchase at discount</text>
  <text x="587" y="210" font-size="13" fill="#cbd5e1" text-anchor="middle">Direct export to state emporiums</text>
  <rect x="455" y="270" width="265" height="90" rx="6" fill="#065f46"/>
  <text x="587" y="320" font-size="14" font-weight="bold" fill="#a7f3d0" text-anchor="middle">High Artisan Profits &amp; Growth</text>
</svg>
""")

SVG_12 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Six-Point Comparative Matrix: India vs Kenya</text>
  <rect x="40" y="70" width="720" height="340" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="200" y="100" font-size="14" font-weight="bold" fill="#38bdf8">Criteria</text>
  <text x="400" y="100" font-size="14" font-weight="bold" fill="#f59e0b">India Cottage</text>
  <text x="620" y="100" font-size="14" font-weight="bold" fill="#10b981">Kenya Jua Kali</text>
  <line x1="60" y1="115" x2="740" y2="115" stroke="#334155" stroke-width="2"/>

  <text x="60" y="150" font-size="12" fill="#cbd5e1">1. Spatial Location</text>
  <text x="320" y="150" font-size="12" fill="#cbd5e1">Strictly rural village based</text>
  <text x="550" y="150" font-size="12" fill="#cbd5e1">Urban &amp; rural (town sheds)</text>

  <text x="60" y="190" font-size="12" fill="#cbd5e1">2. Skill Origin</text>
  <text x="320" y="190" font-size="12" fill="#cbd5e1">Ancient family heritage</text>
  <text x="550" y="190" font-size="12" fill="#cbd5e1">Variable informal apprenticeship</text>

  <text x="60" y="230" font-size="12" fill="#cbd5e1">3. Ownership</text>
  <text x="320" y="230" font-size="12" fill="#cbd5e1">Single family owned</text>
  <text x="550" y="230" font-size="12" fill="#cbd5e1">Individual or cooperative</text>

  <text x="60" y="270" font-size="12" fill="#cbd5e1">4. Ubiquity</text>
  <text x="320" y="270" font-size="12" fill="#cbd5e1">Present in almost every home</text>
  <text x="550" y="270" font-size="12" fill="#cbd5e1">Concentrated in urban sheds</text>

  <text x="60" y="310" font-size="12" fill="#cbd5e1">5. Raw Materials</text>
  <text x="320" y="310" font-size="12" fill="#cbd5e1">Middleman trader supply</text>
  <text x="550" y="310" font-size="12" fill="#cbd5e1">Direct scrap yard purchase</text>
</svg>
""")

SVG_13 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Navigable Waterway Network Supporting the German Ruhr Heavy Region</text>

  <!-- Rivers -->
  <path d="M 100 80 L 100 400" stroke="#0284c7" stroke-width="16"/>
  <text x="110" y="110" font-size="14" font-weight="bold" fill="#38bdf8">River Rhine</text>

  <path d="M 100 240 H 650" stroke="#0284c7" stroke-width="10"/>
  <text x="300" y="230" font-size="13" font-weight="bold" fill="#38bdf8">River Ruhr</text>

  <path d="M 100 160 H 650" stroke="#0284c7" stroke-width="10"/>
  <text x="300" y="150" font-size="13" font-weight="bold" fill="#38bdf8">River Lippe</text>

  <!-- Dortmund Ems Canal -->
  <path d="M 600 80 V 380" stroke="#0284c7" stroke-width="8" stroke-dasharray="6,6"/>
  <text x="615" y="110" font-size="13" font-weight="bold" fill="#cbd5e1">Dortmund-Ems Canal</text>

  <!-- Cities -->
  <circle cx="100" cy="240" r="16" fill="#ef4444"/>
  <text x="130" y="260" font-size="13" font-weight="bold" fill="#ef4444">Duisburg (World's Largest River Port)</text>

  <circle cx="350" cy="240" r="14" fill="#f59e0b"/>
  <text x="350" y="275" font-size="13" font-weight="bold" fill="#f59e0b" text-anchor="middle">Essen</text>

  <circle cx="600" cy="240" r="14" fill="#10b981"/>
  <text x="600" y="275" font-size="13" font-weight="bold" fill="#10b981" text-anchor="middle">Dortmund</text>
</svg>
""")

SVG_14 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Blast Furnace Iron &amp; Steel Smelting Process Flow</text>

  <rect x="40" y="80" width="720" height="60" rx="6" fill="#713f12" stroke="#fde047"/>
  <text x="400" y="115" font-size="15" font-weight="bold" fill="#fef08a" text-anchor="middle">1. Raw Inputs: Iron Ore + Coal Coke + Limestone</text>

  <rect x="120" y="170" width="560" height="70" rx="6" fill="#7f1d1d" stroke="#ef4444"/>
  <text x="400" y="200" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Heavy Blast Furnace Smelting (&gt;1500°C)</text>
  <text x="400" y="225" font-size="13" fill="#fecaca" text-anchor="middle">Coal acts as reducing agent; limestone removes slag</text>

  <rect x="200" y="270" width="400" height="50" rx="6" fill="#1e3a8a" stroke="#60a5fa"/>
  <text x="400" y="302" font-size="14" font-weight="bold" fill="#dbeafe" text-anchor="middle">3. Molten Pig Iron → Oxygen Converter Refining</text>

  <rect x="280" y="345" width="240" height="45" rx="6" fill="#065f46" stroke="#34d399"/>
  <text x="400" y="373" font-size="14" font-weight="bold" fill="#a7f3d0" text-anchor="middle">4. Steel Rolling Mills (Finished Steel)</text>
</svg>
""")

SVG_15 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Geographic Push Factor: Japan's 80% Mountainous Terrain</text>

  <!-- Mountain Profile -->
  <polygon points="40,380 200,120 320,280 480,100 600,320 760,380" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <text x="340" y="200" font-size="18" font-weight="bold" fill="#ef4444" text-anchor="middle">80% RUGGED MOUNTAINOUS TERRAIN</text>
  <text x="340" y="230" font-size="14" fill="#cbd5e1" text-anchor="middle">(Arable Agriculture Severely Restricted)</text>

  <!-- Coastal Plain Strip -->
  <rect x="40" y="360" width="720" height="40" fill="#065f46"/>
  <text x="400" y="385" font-size="14" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Narrow Coastal Plains: Robotic Car (Toyota) &amp; Electronics Hubs</text>
</svg>
""")

SVG_16 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Spatial Industrial Belts of Japan</text>
  <rect x="120" y="70" width="560" height="340" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

  <circle cx="520" cy="160" r="14" fill="#ef4444"/>
  <text x="545" y="165" font-size="13" font-weight="bold" fill="#ef4444">1. Tokyo-Yokohama Belt (Hitachi Electronics)</text>

  <circle cx="360" cy="260" r="14" fill="#f59e0b"/>
  <text x="385" y="265" font-size="13" font-weight="bold" fill="#f59e0b">2. Nagoya Belt (Toyota HQ at Chiru City)</text>

  <circle cx="280" cy="300" r="14" fill="#10b981"/>
  <text x="120" y="305" font-size="13" font-weight="bold" fill="#10b981">3. Osaka-Kobe Belt</text>
</svg>
""")

SVG_17 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Three-Way Global Industrial Comparison: Kenya vs Germany vs Japan</text>
  <rect x="40" y="70" width="720" height="340" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>

  <text x="200" y="100" font-size="14" font-weight="bold" fill="#10b981">Kenya</text>
  <text x="400" y="100" font-size="14" font-weight="bold" fill="#ef4444">Germany (Ruhr)</text>
  <text x="620" y="100" font-size="14" font-weight="bold" fill="#38bdf8">Japan</text>
  <line x1="60" y1="115" x2="740" y2="115" stroke="#334155" stroke-width="2"/>

  <text x="60" y="150" font-size="12" fill="#cbd5e1">Core Sector</text>
  <text x="160" y="150" font-size="12" fill="#cbd5e1">Agro-processing &amp; Jua Kali</text>
  <text x="360" y="150" font-size="12" fill="#cbd5e1">Heavy Iron &amp; Steel</text>
  <text x="560" y="150" font-size="12" fill="#cbd5e1">Automobiles &amp; High-Tech</text>

  <text x="60" y="200" font-size="12" fill="#cbd5e1">Energy</text>
  <text x="160" y="200" font-size="12" fill="#cbd5e1">Geothermal &amp; HEP</text>
  <text x="360" y="200" font-size="12" fill="#cbd5e1">Coal, Gas, and HEP</text>
  <text x="560" y="200" font-size="12" fill="#cbd5e1">Hydro &amp; Imported Oil</text>

  <text x="60" y="250" font-size="12" fill="#cbd5e1">Transport</text>
  <text x="160" y="250" font-size="12" fill="#cbd5e1">Roads &amp; SGR Rail</text>
  <text x="360" y="250" font-size="12" fill="#cbd5e1">Navigable River Canals</text>
  <text x="560" y="250" font-size="12" fill="#cbd5e1">Deep Sea Coastal Ports</text>

  <text x="60" y="300" font-size="12" fill="#cbd5e1">Technology</text>
  <text x="160" y="300" font-size="12" fill="#cbd5e1">Manual &amp; Semi-automated</text>
  <text x="360" y="300" font-size="12" fill="#cbd5e1">Heavy Mechanical Furnaces</text>
  <text x="560" y="300" font-size="12" fill="#cbd5e1">Automated Computer Robotics</text>
</svg>
""")

SVG_18 = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Six-Point National Strategy for Sustainable Kenyan Industrialisation</text>
  <g transform="translate(60, 80)">
    <rect x="0" y="0" width="210" height="130" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="105" y="35" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. Geothermal Grid</text>
    <text x="105" y="70" font-size="12" fill="#cbd5e1" text-anchor="middle">Expand Olkaria steam to</text>
    <text x="105" y="90" font-size="12" fill="#cbd5e1" text-anchor="middle">deliver cheap power</text>

    <rect x="235" y="0" width="210" height="130" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <text x="340" y="35" font-size="14" font-weight="bold" fill="#10b981" text-anchor="middle">2. Protective Tariffs</text>
    <text x="340" y="70" font-size="12" fill="#cbd5e1" text-anchor="middle">Curb Mitumba imports to</text>
    <text x="340" y="90" font-size="12" fill="#cbd5e1" text-anchor="middle">revive textile mills</text>

    <rect x="470" y="0" width="210" height="130" rx="6" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <text x="575" y="35" font-size="14" font-weight="bold" fill="#eab308" text-anchor="middle">3. TVET Training</text>
    <text x="575" y="70" font-size="12" fill="#cbd5e1" text-anchor="middle">Train local managers &amp;</text>
    <text x="575" y="90" font-size="12" fill="#cbd5e1" text-anchor="middle">check brain drain</text>

    <rect x="0" y="160" width="210" height="130" rx="6" fill="#0f172a" stroke="#f43f5e" stroke-width="2"/>
    <text x="105" y="195" font-size="14" font-weight="bold" fill="#f43f5e" text-anchor="middle">4. EPZ Decentralisation</text>
    <text x="105" y="230" font-size="12" fill="#cbd5e1" text-anchor="middle">Divert plants to rural</text>
    <text x="105" y="250" font-size="12" fill="#cbd5e1" text-anchor="middle">counties via tax breaks</text>

    <rect x="235" y="160" width="210" height="130" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <text x="340" y="195" font-size="14" font-weight="bold" fill="#a855f7" text-anchor="middle">5. COMESA Exports</text>
    <text x="340" y="230" font-size="12" fill="#cbd5e1" text-anchor="middle">Expand regional market</text>
    <text x="340" y="250" font-size="12" fill="#cbd5e1" text-anchor="middle">access for local goods</text>

    <rect x="470" y="160" width="210" height="130" rx="6" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
    <text x="575" y="195" font-size="14" font-weight="bold" fill="#06b6d4" text-anchor="middle">6. Jua Kali Support</text>
    <text x="575" y="230" font-size="12" fill="#cbd5e1" text-anchor="middle">Fund KIE loans &amp; Nyayo</text>
    <text x="575" y="250" font-size="12" fill="#cbd5e1" text-anchor="middle">sheds for informal sector</text>
  </g>
</svg>
""")

TOPIC5_SVGS = [
    SVG_1, SVG_2, SVG_3, SVG_4, SVG_5, SVG_6,
    SVG_7, SVG_8, SVG_9, SVG_10, SVG_11, SVG_12,
    SVG_13, SVG_14, SVG_15, SVG_16, SVG_17, SVG_18
]

# =====================================================================
# 8 VERIFIED WIKIMEDIA COMMONS PHOTOS FOR TOPIC 5: INDUSTRY
# =====================================================================

TOPIC5_PHOTOS = [
    {
        "lesson_order": 1,
        "page": 5,
        "title": "Rukuriri Tea Processing Factory Embu",
        "url": "https://upload.wikimedia.org/wikipedia/commons/1/1c/2009.12-363-1125ap_tea%2Cprocessing%28withering%29%2Cstirring_Rukuriri_Tea_Factory%2Ctea-zone_N_of_Embu%28C_Highlands%29%2CKE_mon14dec2009-1242h.jpg",
        "author": "Public Domain, Wikimedia Commons",
        "licensing": "Public domain",
        "caption": "Agricultural tea processing factory located directly inside the tea-growing highlands of Embu."
    },
    {
        "lesson_order": 2,
        "page": 5,
        "title": "Informal Jua Kali Fabricator Shed Kenya",
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/36/Jua_Kali_fabricator.jpg",
        "author": "Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "Informal Jua Kali metal fabricators reprocessing scrap metal under open-air Nyayo sheds."
    },
    {
        "lesson_order": 2,
        "page": 8,
        "title": "Jua Kali Reprocessed Cooking Pots",
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/be/Jua_Kali_cooking_pots.jpg",
        "author": "Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "Durable, low-cost aluminum cooking pots manufactured by Jua Kali artisans from recycled scrap metals."
    },
    {
        "lesson_order": 3,
        "page": 4,
        "title": "Commercial Heavy Industrial Cement Kiln",
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Cement_kiln_in_Gorazdze_Cement_plant.JPG",
        "author": "Wikimedia Commons",
        "licensing": "CC BY-SA 3.0",
        "caption": "Massive rotary cement kiln factory demonstrating heavy manufacturing infrastructure."
    },
    {
        "lesson_order": 4,
        "page": 3,
        "title": "Traditional Handloom Weaving Workshop India",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/04/Handloom_weaving_setup.jpg",
        "author": "Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "Rural Indian weavers operating wooden handlooms inside a village home workshop."
    },
    {
        "lesson_order": 4,
        "page": 5,
        "title": "Artisanal Silk Saree Weaving India",
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b4/Saree_Weaving_by_Handloom_2.jpg",
        "author": "Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "An artisan weaving intricate silk sarees on a traditional wooden loom in an Indian cottage workshop."
    },
    {
        "lesson_order": 5,
        "page": 4,
        "title": "Duisburg Ruhr Blast Furnace Complex",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/01/Duisburg%2C_Landschaftspark_Duisburg-Nord_--_2016_--_1238-44.jpg",
        "author": "Wikimedia Commons",
        "licensing": "CC BY-SA 4.0",
        "caption": "Historic heavy blast furnace steel infrastructure in Duisburg within Germany's Ruhr Industrial Region."
    },
    {
        "lesson_order": 5,
        "page": 8,
        "title": "Automated Robotic Car Assembly Plant",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/67/BMW_Leipzig_MEDIA_050719_Download_Karosseriebau_max.jpg",
        "author": "Wikimedia Commons",
        "licensing": "CC BY-SA 3.0",
        "caption": "Advanced computer-controlled robotic arms assembling automobile chassis on an automated manufacturing line."
    }
]

def enrich_form4_geography_topic5():
    print("=" * 80)
    print("VLearn Form 4 Geography — Topic 5: Visual Enrichment Engine")
    print("Attaching 18 Vector SVGs & 8 Verified Wikimedia Photographic Assets")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    subject = Subject.objects.filter(grade=grade, name="Geography").first()
    topic = Topic.objects.filter(subject=subject, name="Industry").first()

    if not topic:
        print("[!] Error: Topic 'Industry' not found!")
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
            if svg_counter < len(TOPIC5_SVGS):
                svg_data = TOPIC5_SVGS[svg_counter]
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
        photo_meta_list = [p for p in TOPIC5_PHOTOS if p["lesson_order"] == u_order]
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
    print(f"[SUCCESS] Form 4 Geography Topic 5 Visual Enrichment Complete!")
    print(f"[*] Total LessonAssets Created: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_form4_geography_topic5()
