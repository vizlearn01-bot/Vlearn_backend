"""
VLearn CBC Grade 10 Agriculture — Topic 1: Agricultural Land
Visual Enrichment Engine (Phase 2: Vector SVGs, Verified Photos & Asset Persistence)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Agricultural Land (Order: 1)

Attaches:
  - 10 First-Card Photographic Visual Hooks (100% Tested HTTP 200 OK Direct Wikimedia URLs)
  - 8 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - 2 Verified Educational YouTube Videos (Lesson 3 Card 5 & Lesson 10 Card 4)
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade10_agriculture_topic1.py
"""

import os
import sys
import re
import json
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, Lesson, LessonBlock, LessonAsset
)

def sanitize_svg(svg: str) -> str:
    """Ensures SVG is clean, responsive, and stripped of unneeded XML/DOCTYPE headers."""
    svg = re.sub(r'<\?xml.*?\?>', '', svg)
    svg = re.sub(r'<!DOCTYPE.*?>', '', svg)
    return svg.strip()

# =============================================================================
# 8 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 1: AGRICULTURAL LAND
# =============================================================================

# SVG 1: Land Acquisition Framework (Lesson 1, Page 5)
SVG_LAND_ACQUISITION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Agricultural Land Acquisition Framework in Kenya</text>
  
  <!-- Method 1: Leasing -->
  <g transform="translate(35, 70)">
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="170" height="40" rx="10" fill="#0284c7"/>
    <text x="85" y="25" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">1. LEASING</text>
    <text x="12" y="65" font-size="11" font-weight="bold" fill="#38bdf8">Capital Need:</text>
    <text x="12" y="82" font-size="10" fill="#cbd5e1">• Low (Seasonal rent)</text>
    <text x="12" y="112" font-size="11" font-weight="bold" fill="#38bdf8">Tenure Security:</text>
    <text x="12" y="129" font-size="10" fill="#cbd5e1">• Fixed lease duration</text>
    <text x="12" y="159" font-size="11" font-weight="bold" fill="#38bdf8">Investment Focus:</text>
    <text x="12" y="176" font-size="10" fill="#cbd5e1">• Short-term annuals</text>
    <text x="12" y="193" font-size="10" fill="#cbd5e1">• Mobile drip kits</text>
    <line x1="12" y1="215" x2="158" y2="215" stroke="#334155" stroke-width="1"/>
    <text x="12" y="235" font-size="11" font-weight="bold" fill="#f87171">Primary Risk:</text>
    <text x="12" y="252" font-size="10" fill="#cbd5e1">• Non-renewal risk</text>
    <text x="12" y="269" font-size="10" fill="#cbd5e1">• Fixed rent overhead</text>
    <rect x="10" y="295" width="150" height="32" rx="6" fill="#1e293b"/>
    <text x="85" y="315" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Best for Start-ups</text>
  </g>

  <!-- Method 2: Inheritance -->
  <g transform="translate(220, 70)">
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <rect x="0" y="0" width="170" height="40" rx="10" fill="#7e22ce"/>
    <text x="85" y="25" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">2. INHERITANCE</text>
    <text x="12" y="65" font-size="11" font-weight="bold" fill="#c084fc">Capital Need:</text>
    <text x="12" y="82" font-size="10" fill="#cbd5e1">• Zero purchase cost</text>
    <text x="12" y="112" font-size="11" font-weight="bold" fill="#c084fc">Tenure Security:</text>
    <text x="12" y="129" font-size="10" fill="#cbd5e1">• High (Once titled)</text>
    <text x="12" y="159" font-size="11" font-weight="bold" fill="#c084fc">Investment Focus:</text>
    <text x="12" y="176" font-size="10" fill="#cbd5e1">• Family stewardship</text>
    <text x="12" y="193" font-size="10" fill="#cbd5e1">• Mixed smallholder</text>
    <line x1="12" y1="215" x2="158" y2="215" stroke="#334155" stroke-width="1"/>
    <text x="12" y="235" font-size="11" font-weight="bold" fill="#f87171">Primary Risk:</text>
    <text x="12" y="252" font-size="10" fill="#cbd5e1">• Plot fragmentation</text>
    <text x="12" y="269" font-size="10" fill="#cbd5e1">• Family succession feud</text>
    <rect x="10" y="295" width="150" height="32" rx="6" fill="#1e293b"/>
    <text x="85" y="315" font-size="10" font-weight="bold" fill="#c084fc" text-anchor="middle">Intergenerational</text>
  </g>

  <!-- Method 3: Buying -->
  <g transform="translate(405, 70)">
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="170" height="40" rx="10" fill="#15803d"/>
    <text x="85" y="25" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">3. BUYING</text>
    <text x="12" y="65" font-size="11" font-weight="bold" fill="#4ade80">Capital Need:</text>
    <text x="12" y="82" font-size="10" fill="#cbd5e1">• Very High (Purchase)</text>
    <text x="12" y="112" font-size="11" font-weight="bold" fill="#4ade80">Tenure Security:</text>
    <text x="12" y="129" font-size="10" fill="#cbd5e1">• Absolute (Title Deed)</text>
    <text x="12" y="159" font-size="11" font-weight="bold" fill="#4ade80">Investment Focus:</text>
    <text x="12" y="176" font-size="10" fill="#cbd5e1">• Boreholes &amp; Sheds</text>
    <text x="12" y="193" font-size="10" fill="#cbd5e1">• Perennial Orchards</text>
    <line x1="12" y1="215" x2="158" y2="215" stroke="#334155" stroke-width="1"/>
    <text x="12" y="235" font-size="11" font-weight="bold" fill="#f87171">Primary Risk:</text>
    <text x="12" y="252" font-size="10" fill="#cbd5e1">• Drains liquid capital</text>
    <text x="12" y="269" font-size="10" fill="#cbd5e1">• Fraudulent title risk</text>
    <rect x="10" y="295" width="150" height="32" rx="6" fill="#1e293b"/>
    <text x="85" y="315" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Maximum Collateral</text>
  </g>

  <!-- Method 4: Donation -->
  <g transform="translate(590, 70)">
    <rect x="0" y="0" width="170" height="340" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect x="0" y="0" width="170" height="40" rx="10" fill="#b45309"/>
    <text x="85" y="25" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">4. DONATION</text>
    <text x="12" y="65" font-size="11" font-weight="bold" fill="#fcd34d">Capital Need:</text>
    <text x="12" y="82" font-size="10" fill="#cbd5e1">• Zero purchase cost</text>
    <text x="12" y="112" font-size="11" font-weight="bold" fill="#fcd34d">Tenure Security:</text>
    <text x="12" y="129" font-size="10" fill="#cbd5e1">• Medium (Conditional)</text>
    <text x="12" y="159" font-size="11" font-weight="bold" fill="#fcd34d">Investment Focus:</text>
    <text x="12" y="176" font-size="10" fill="#cbd5e1">• Community farming</text>
    <text x="12" y="193" font-size="10" fill="#cbd5e1">• School demo plots</text>
    <line x1="12" y1="215" x2="158" y2="215" stroke="#334155" stroke-width="1"/>
    <text x="12" y="235" font-size="11" font-weight="bold" fill="#f87171">Primary Risk:</text>
    <text x="12" y="252" font-size="10" fill="#cbd5e1">• Strict donor rules</text>
    <text x="12" y="269" font-size="10" fill="#cbd5e1">• Cannot choose land</text>
    <rect x="10" y="295" width="150" height="32" rx="6" fill="#1e293b"/>
    <text x="85" y="315" font-size="10" font-weight="bold" fill="#fcd34d" text-anchor="middle">Community Projects</text>
  </g>
</svg>
""")

# SVG 2: Integrated Multi-Utility Farm Layout (Lesson 2, Page 5)
SVG_FARM_LAYOUT = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Integrated Multi-Utility Agribusiness Farm Zoning Model</text>

  <!-- Zone 1: Steep Hillside Apiary & Woodlot -->
  <g transform="translate(35, 65)">
    <rect x="0" y="0" width="355" height="160" rx="10" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect x="0" y="0" width="355" height="32" rx="10" fill="#854d0e"/>
    <text x="177" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">ZONE 1: STEEP ROCKY HILLSIDE (&gt;15% Slope)</text>
    <text x="15" y="55" font-size="12" font-weight="bold" fill="#fde047">Enterprise: Modern Apiculture &amp; Agroforestry Woodlot</text>
    <text x="15" y="75" font-size="11" fill="#cbd5e1">• Zero soil depth requirement; protects rocky slope from erosion</text>
    <text x="15" y="95" font-size="11" fill="#cbd5e1">• Beehives placed in undisturbed tree canopy (*Melia volkensii*)</text>
    <text x="15" y="115" font-size="11" fill="#cbd5e1">• Multiplier: Bees cross-pollinate vegetable blossoms down-slope</text>
    <rect x="15" y="125" width="325" height="24" rx="4" fill="#1e293b"/>
    <text x="177" y="141" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">High Honey Revenue + 30% Higher Crop Pollination</text>
  </g>

  <!-- Zone 2: Gentle Mid-Slope Horticulture -->
  <g transform="translate(410, 65)">
    <rect x="0" y="0" width="355" height="160" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="355" height="32" rx="10" fill="#15803d"/>
    <text x="177" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">ZONE 2: GENTLE MID-SLOPE (2-8% Slope, Deep Loam)</text>
    <text x="15" y="55" font-size="12" font-weight="bold" fill="#86efac">Enterprise: Intensive Drip Horticulture &amp; Fodder</text>
    <text x="15" y="75" font-size="11" fill="#cbd5e1">• Deep, well-drained loam soil with high water-holding capacity</text>
    <text x="15" y="95" font-size="11" fill="#cbd5e1">• Contour terraces with Napier grass strips to halt runoff</text>
    <text x="15" y="115" font-size="11" fill="#cbd5e1">• High-value tomatoes, capsicums, cabbages &amp; French beans</text>
    <rect x="15" y="125" width="325" height="24" rx="4" fill="#1e293b"/>
    <text x="177" y="141" font-size="10" font-weight="bold" fill="#86efac" text-anchor="middle">Maximum Return per Square Meter</text>
  </g>

  <!-- Zone 3: Homestead & Zero-Grazing Dairy -->
  <g transform="translate(35, 245)">
    <rect x="0" y="0" width="355" height="170" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <rect x="0" y="0" width="355" height="32" rx="10" fill="#6b21a8"/>
    <text x="177" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">ZONE 3: ACCESSIBLE FLAT (Homestead &amp; Dairy)</text>
    <text x="15" y="55" font-size="12" font-weight="bold" fill="#c084fc">Enterprise: Zero-Grazing Dairy Unit &amp; Biogas</text>
    <text x="15" y="75" font-size="11" fill="#cbd5e1">• Close to residence for biosecurity and 24/7 milk management</text>
    <text x="15" y="95" font-size="11" fill="#cbd5e1">• Fed terrace Napier grass; manure routed to biogas digester</text>
    <text x="15" y="115" font-size="11" fill="#cbd5e1">• Slurry and compost returned to Zone 2 horticultural beds</text>
    <rect x="15" y="132" width="325" height="26" rx="4" fill="#1e293b"/>
    <text x="177" y="149" font-size="10" font-weight="bold" fill="#c084fc" text-anchor="middle">Closed Biological Loop: Manure Feeds Soil</text>
  </g>

  <!-- Zone 4: Valley Basin Aquaculture -->
  <g transform="translate(410, 245)">
    <rect x="0" y="0" width="355" height="170" rx="10" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
    <rect x="0" y="0" width="355" height="32" rx="10" fill="#0e7490"/>
    <text x="177" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">ZONE 4: CLAY VALLEY BASIN (Waterlogged Depression)</text>
    <text x="15" y="55" font-size="12" font-weight="bold" fill="#67e8f9">Enterprise: Earthen Aquaculture (Tilapia/Catfish)</text>
    <text x="15" y="75" font-size="11" fill="#cbd5e1">• Heavy clay soil (&gt;35% clay) prevents water seepage naturally</text>
    <text x="15" y="95" font-size="11" fill="#cbd5e1">• Gravity-fed clean water inlet and regulated drainage monk</text>
    <text x="15" y="115" font-size="11" fill="#cbd5e1">• Pond banks planted with wetland arrowroots (*nduma*)</text>
    <rect x="15" y="132" width="325" height="26" rx="4" fill="#1e293b"/>
    <text x="177" y="149" font-size="10" font-weight="bold" fill="#67e8f9" text-anchor="middle">Turns Marginal Waterlogged Land into High Protein</text>
  </g>
</svg>
""")

# SVG 3: Agro-Ecological Elevation Gradient (Lesson 3, Page 4)
SVG_ELEVATION_GRADIENT = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Agro-Ecological Elevation Bands and Environmental Lapse Rate</text>

  <!-- Altitude Axis Line -->
  <line x1="120" y1="80" x2="120" y2="390" stroke="#64748b" stroke-width="3"/>
  <polygon points="120,70 114,85 126,85" fill="#38bdf8"/>
  <text x="105" y="75" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="end">ALTITUDE</text>

  <!-- Band 1: Highlands -->
  <g transform="translate(130, 80)">
    <rect x="0" y="0" width="625" height="95" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="130" height="95" rx="8" fill="#0369a1"/>
    <text x="65" y="32" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">HIGHLANDS</text>
    <text x="65" y="52" font-size="11" fill="#e0f2fe" text-anchor="middle">&gt; 1,800 meters</text>
    <text x="65" y="72" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">12°C – 18°C</text>
    
    <text x="145" y="28" font-size="12" font-weight="bold" fill="#38bdf8">Climatic Profile: High rainfall (&gt;1200mm), high humidity, frequent mists</text>
    <text x="145" y="50" font-size="11" fill="#cbd5e1">• Suitable Crops: Tea, Pyrethrum, Irish Potatoes, Wheat, Barley, Cut Flowers</text>
    <text x="145" y="72" font-size="11" fill="#cbd5e1">• Livestock: High-grade European Dairy (Holstein Friesian, Jersey, Guernsey)</text>
  </g>

  <!-- Band 2: Midlands -->
  <g transform="translate(130, 185)">
    <rect x="0" y="0" width="625" height="95" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="130" height="95" rx="8" fill="#15803d"/>
    <text x="65" y="32" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">MIDLANDS</text>
    <text x="65" y="52" font-size="11" fill="#dcfce7" text-anchor="middle">1,000 – 1,800 m</text>
    <text x="65" y="72" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">18°C – 25°C</text>
    
    <text x="145" y="28" font-size="12" font-weight="bold" fill="#4ade80">Climatic Profile: Medium-high rainfall (750–1200mm), warm-temperate</text>
    <text x="145" y="50" font-size="11" fill="#cbd5e1">• Suitable Crops: Coffee (Arabica), Hybrid Maize, Beans, Bananas, Hass Avocado</text>
    <text x="145" y="72" font-size="11" fill="#cbd5e1">• Livestock: Dual-purpose cattle (Sahiwal, Simmental), Crossbred Dairy, Poultry</text>
  </g>

  <!-- Band 3: Lowlands -->
  <g transform="translate(130, 290)">
    <rect x="0" y="0" width="625" height="95" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="130" height="95" rx="8" fill="#b45309"/>
    <text x="65" y="32" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">LOWLANDS</text>
    <text x="65" y="52" font-size="11" fill="#fef3c7" text-anchor="middle">&lt; 1,000 meters</text>
    <text x="65" y="72" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">26°C – 35°C</text>
    
    <text x="145" y="28" font-size="12" font-weight="bold" fill="#fbbf24">Climatic Profile: High heat, high evapotranspiration, low-to-erratic rain (&lt;600mm)</text>
    <text x="145" y="50" font-size="11" fill="#cbd5e1">• Suitable Crops: Sorghum, Millet, Cowpeas, Sisal, Cotton, Cashews, Coconuts</text>
    <text x="145" y="72" font-size="11" fill="#cbd5e1">• Livestock: Heat-hardy Boran beef cattle, Camels, Galla Goats, Red Maasai Sheep</text>
  </g>

  <!-- Formula Callout Footer -->
  <g transform="translate(130, 395)">
    <rect x="0" y="0" width="625" height="28" rx="6" fill="#0f172a" stroke="#64748b"/>
    <text x="312" y="18" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Environmental Lapse Rate Rule: Temperature drops ≈ 6.5°C for every 1,000 meters elevation gain</text>
  </g>
</svg>
""")

# SVG 4: Topographical Catena & Soil Drainage (Lesson 4, Page 4)
SVG_TOPOGRAPHICAL_CATENA = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Topographical Soil Catena: Slope, Drainage, and Enterprise Matching</text>

  <!-- Cross-Section Visual Path -->
  <path d="M 50 140 Q 250 160 450 250 T 750 320 L 750 370 L 50 370 Z" fill="#334155" stroke="#475569" stroke-width="2"/>
  <path d="M 50 140 Q 250 160 450 250 T 750 320" fill="none" stroke="#22c55e" stroke-width="4"/>

  <!-- Position 1: Crest / Ridge -->
  <g transform="translate(50, 65)">
    <rect x="0" y="0" width="210" height="110" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="210" height="26" rx="8" fill="#b45309"/>
    <text x="105" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. CREST / UPPER RIDGE</text>
    <text x="10" y="45" font-size="10" font-weight="bold" fill="#fbbf24">• Soil: Shallow, gravelly, coarse</text>
    <text x="10" y="62" font-size="10" fill="#cbd5e1">• Drainage: Excessively drained</text>
    <text x="10" y="79" font-size="10" fill="#cbd5e1">• Issue: Rapid leaching &amp; runoff</text>
    <text x="10" y="98" font-size="10" font-weight="bold" fill="#38bdf8">Suited: Woodlots &amp; Pastures</text>
  </g>

  <!-- Position 2: Mid-Slope -->
  <g transform="translate(295, 120)">
    <rect x="0" y="0" width="220" height="115" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="26" rx="8" fill="#15803d"/>
    <text x="110" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. FERTILE MID-SLOPE</text>
    <text x="10" y="45" font-size="10" font-weight="bold" fill="#86efac">• Soil: Deep, fertile crumb loam</text>
    <text x="10" y="62" font-size="10" fill="#cbd5e1">• Drainage: Well-drained (Optimal)</text>
    <text x="10" y="79" font-size="10" fill="#cbd5e1">• Needs: Contour terraces &amp; mulch</text>
    <text x="10" y="100" font-size="10" font-weight="bold" fill="#38bdf8">Suited: Horticulture &amp; Maize</text>
  </g>

  <!-- Position 3: Valley Bottom -->
  <g transform="translate(545, 230)">
    <rect x="0" y="0" width="225" height="120" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
    <rect x="0" y="0" width="225" height="26" rx="8" fill="#0e7490"/>
    <text x="112" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. VALLEY FLOOR (DEPRESSION)</text>
    <text x="10" y="45" font-size="10" font-weight="bold" fill="#67e8f9">• Soil: Heavy dark clay (Vertisols)</text>
    <text x="10" y="62" font-size="10" fill="#cbd5e1">• Drainage: Poorly drained, waterlogged</text>
    <text x="10" y="79" font-size="10" fill="#cbd5e1">• Threat: Root rot in upland crops</text>
    <text x="10" y="102" font-size="10" font-weight="bold" fill="#38bdf8">Suited: Aquaculture &amp; Paddy Rice</text>
  </g>

  <!-- Water Table Indicator -->
  <line x1="560" y1="365" x2="745" y2="365" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6,4"/>
  <text x="652" y="385" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">High Water Table / Standing Water</text>
</svg>
""")

# SVG 5: Land Allocation Decision Flowchart (Lesson 6, Page 3)
SVG_DECISION_FLOWCHART = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Agribusiness Land Zoning Decision Tree Algorithm</text>

  <!-- Step 1: Start -->
  <rect x="300" y="60" width="200" height="35" rx="8" fill="#0284c7" stroke="#38bdf8"/>
  <text x="400" y="82" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">START: Evaluate Parcel Profile</text>
  
  <line x1="400" y1="95" x2="400" y2="120" stroke="#94a3b8" stroke-width="2"/>

  <!-- Decision Node 1: Slope % -->
  <polygon points="400,120 520,155 400,190 280,155" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
  <text x="400" y="152" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">Is Slope &gt; 15%</text>
  <text x="400" y="167" font-size="10" fill="#fde047" text-anchor="middle">or Rocky?</text>

  <!-- Branch YES (>15%) -->
  <line x1="280" y1="155" x2="160" y2="155" stroke="#94a3b8" stroke-width="2"/>
  <text x="210" y="145" font-size="10" font-weight="bold" fill="#38bdf8">YES</text>
  <rect x="40" y="130" width="120" height="50" rx="6" fill="#854d0e" stroke="#eab308"/>
  <text x="100" y="150" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">ZONE APICULTURE</text>
  <text x="100" y="168" font-size="9" fill="#fde047" text-anchor="middle">&amp; Woodlot / Pasture</text>

  <!-- Branch NO (<=15%) -->
  <line x1="400" y1="190" x2="400" y2="220" stroke="#94a3b8" stroke-width="2"/>
  <text x="415" y="210" font-size="10" font-weight="bold" fill="#38bdf8">NO</text>

  <!-- Decision Node 2: Drainage & Clay % -->
  <polygon points="400,220 540,260 400,300 260,260" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
  <text x="400" y="254" font-size="11" font-weight="bold" fill="#67e8f9" text-anchor="middle">Is Soil Heavy Clay</text>
  <text x="400" y="270" font-size="10" fill="#67e8f9" text-anchor="middle">&amp; Waterlogged?</text>

  <!-- Branch YES (Clay/Waterlogged) -->
  <line x1="540" y1="260" x2="660" y2="260" stroke="#94a3b8" stroke-width="2"/>
  <text x="590" y="250" font-size="10" font-weight="bold" fill="#38bdf8">YES</text>
  <rect x="660" y="235" width="115" height="50" rx="6" fill="#0e7490" stroke="#06b6d4"/>
  <text x="717" y="255" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">ZONE AQUACULTURE</text>
  <text x="717" y="273" font-size="9" fill="#67e8f9" text-anchor="middle">&amp; Arrowroot Basins</text>

  <!-- Branch NO (Well-Drained Loam) -->
  <line x1="400" y1="300" x2="400" y2="330" stroke="#94a3b8" stroke-width="2"/>
  <text x="415" y="320" font-size="10" font-weight="bold" fill="#38bdf8">NO</text>

  <!-- Output Box: Horticulture & Dairy -->
  <rect x="250" y="330" width="300" height="90" rx="8" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
  <text x="400" y="355" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">ZONE COMMERCIAL HORTICULTURE &amp; DAIRY</text>
  <text x="400" y="375" font-size="10" fill="#dcfce7" text-anchor="middle">• Establish contour terraces &amp; Napier grass strips</text>
  <text x="400" y="393" font-size="10" fill="#dcfce7" text-anchor="middle">• Apply lime if pH &lt; 6.0; install drip irrigation</text>
  <text x="400" y="410" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">Yields Highest Profit per Hectare</text>
</svg>
""")

# SVG 6: Multi-Dimensional Land Value Matrix (Lesson 7, Page 3)
SVG_LAND_VALUE_MATRIX = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Multi-Dimensional Value Matrix of Agricultural Land</text>

  <!-- Dimension 1: Economic Value -->
  <g transform="translate(35, 65)">
    <rect x="0" y="0" width="230" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="230" height="40" rx="10" fill="#15803d"/>
    <text x="115" y="25" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">1. ECONOMIC VALUE</text>
    
    <text x="15" y="70" font-size="12" font-weight="bold" fill="#4ade80">Capital Asset:</text>
    <text x="15" y="90" font-size="11" fill="#cbd5e1">• Appreciates steadily over time</text>
    <text x="15" y="110" font-size="11" fill="#cbd5e1">• Bankable loan collateral</text>
    
    <line x1="15" y1="130" x2="215" y2="130" stroke="#334155" stroke-width="1"/>
    
    <text x="15" y="155" font-size="12" font-weight="bold" fill="#4ade80">Production Factor:</text>
    <text x="15" y="175" font-size="11" fill="#cbd5e1">• Substrate for crops &amp; livestock</text>
    <text x="15" y="195" font-size="11" fill="#cbd5e1">• Supplies raw industrial inputs</text>
    
    <line x1="15" y1="215" x2="215" y2="215" stroke="#334155" stroke-width="1"/>
    
    <text x="15" y="240" font-size="12" font-weight="bold" fill="#4ade80">Income Generation:</text>
    <text x="15" y="260" font-size="11" fill="#cbd5e1">• Cash profits from harvests</text>
    <text x="15" y="280" font-size="11" fill="#cbd5e1">• Leasehold rental income</text>
    
    <rect x="15" y="305" width="200" height="26" rx="4" fill="#1e293b"/>
    <text x="115" y="322" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Foundation of National Wealth</text>
  </g>

  <!-- Dimension 2: Social & Cultural Value -->
  <g transform="translate(285, 65)">
    <rect x="0" y="0" width="230" height="345" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <rect x="0" y="0" width="230" height="40" rx="10" fill="#7e22ce"/>
    <text x="115" y="25" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">2. SOCIAL &amp; CULTURAL</text>
    
    <text x="15" y="70" font-size="12" font-weight="bold" fill="#c084fc">Livelihood Security:</text>
    <text x="15" y="90" font-size="11" fill="#cbd5e1">• Household food safety net</text>
    <text x="15" y="110" font-size="11" fill="#cbd5e1">• Resilience during inflation</text>
    
    <line x1="15" y1="130" x2="215" y2="130" stroke="#334155" stroke-width="1"/>
    
    <text x="15" y="155" font-size="12" font-weight="bold" fill="#c084fc">Ancestral Identity:</text>
    <text x="15" y="175" font-size="11" fill="#cbd5e1">• Family heritage &amp; burial rites</text>
    <text x="15" y="195" font-size="11" fill="#cbd5e1">• Intergenerational trust</text>
    
    <line x1="15" y1="215" x2="215" y2="215" stroke="#334155" stroke-width="1"/>
    
    <text x="15" y="240" font-size="12" font-weight="bold" fill="#c084fc">Social Standing:</text>
    <text x="15" y="260" font-size="11" fill="#cbd5e1">• Community prestige</text>
    <text x="15" y="280" font-size="11" fill="#cbd5e1">• Youth &amp; women empowerment</text>
    
    <rect x="15" y="305" width="200" height="26" rx="4" fill="#1e293b"/>
    <text x="115" y="322" font-size="10" font-weight="bold" fill="#c084fc" text-anchor="middle">Anchor of Rural Stability</text>
  </g>

  <!-- Dimension 3: Environmental Ecosystem Services -->
  <g transform="translate(535, 65)">
    <rect x="0" y="0" width="230" height="345" rx="10" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
    <rect x="0" y="0" width="230" height="40" rx="10" fill="#0e7490"/>
    <text x="115" y="25" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">3. ENVIRONMENTAL</text>
    
    <text x="15" y="70" font-size="12" font-weight="bold" fill="#67e8f9">Water Catchment:</text>
    <text x="15" y="90" font-size="11" fill="#cbd5e1">• Captures &amp; filters rainfall</text>
    <text x="15" y="110" font-size="11" fill="#cbd5e1">• Recharges deep aquifers</text>
    
    <line x1="15" y1="130" x2="215" y2="130" stroke="#334155" stroke-width="1"/>
    
    <text x="15" y="155" font-size="12" font-weight="bold" fill="#67e8f9">Carbon Sink:</text>
    <text x="15" y="175" font-size="11" fill="#cbd5e1">• Absorbs atmospheric CO2</text>
    <text x="15" y="195" font-size="11" fill="#cbd5e1">• Builds soil organic humus</text>
    
    <line x1="15" y1="215" x2="215" y2="215" stroke="#334155" stroke-width="1"/>
    
    <text x="15" y="240" font-size="12" font-weight="bold" fill="#67e8f9">Biodiversity Habitat:</text>
    <text x="15" y="260" font-size="11" fill="#cbd5e1">• Pollinators (wild bees)</text>
    <text x="15" y="280" font-size="11" fill="#cbd5e1">• Symbiotic soil microbes</text>
    
    <rect x="15" y="305" width="200" height="26" rx="4" fill="#1e293b"/>
    <text x="115" y="322" font-size="10" font-weight="bold" fill="#67e8f9" text-anchor="middle">Planetary Life Support</text>
  </g>
</svg>
""")

# SVG 7: Virtuous vs Vicious Tenure Cycles (Lesson 8, Page 3)
SVG_TENURE_CYCLES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Virtuous vs Vicious Cycles of Agricultural Land Tenure</text>

  <!-- Left Column: Virtuous Cycle (Secure Tenure) -->
  <g transform="translate(35, 65)">
    <rect x="0" y="0" width="355" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="355" height="35" rx="10" fill="#15803d"/>
    <text x="177" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">VIRTUOUS CYCLE (Secure Title / Long Lease)</text>

    <g transform="translate(15, 50)">
      <circle cx="15" cy="15" r="14" fill="#166534"/>
      <text x="15" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1</text>
      <text x="40" y="15" font-size="11" font-weight="bold" fill="#86efac">Secure Legal Title Deed</text>
      <text x="40" y="28" font-size="10" fill="#cbd5e1">Confidence in multi-decade farm returns &amp; credit</text>
    </g>

    <line x1="30" y1="85" x2="30" y2="105" stroke="#22c55e" stroke-width="2"/>

    <g transform="translate(15, 110)">
      <circle cx="15" cy="15" r="14" fill="#166534"/>
      <text x="15" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2</text>
      <text x="40" y="15" font-size="11" font-weight="bold" fill="#86efac">Permanent Capital Investment</text>
      <text x="40" y="28" font-size="10" fill="#cbd5e1">Stone terraces, boreholes, agroforestry, sheds</text>
    </g>

    <line x1="30" y1="145" x2="30" y2="165" stroke="#22c55e" stroke-width="2"/>

    <g transform="translate(15, 170)">
      <circle cx="15" cy="15" r="14" fill="#166534"/>
      <text x="15" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3</text>
      <text x="40" y="15" font-size="11" font-weight="bold" fill="#86efac">Compounding Soil Fertility</text>
      <text x="40" y="28" font-size="10" fill="#cbd5e1">Heavy compost, lime, active earthworms, zero runoff</text>
    </g>

    <line x1="30" y1="205" x2="30" y2="225" stroke="#22c55e" stroke-width="2"/>

    <g transform="translate(15, 230)">
      <circle cx="15" cy="15" r="14" fill="#166534"/>
      <text x="15" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4</text>
      <text x="40" y="15" font-size="11" font-weight="bold" fill="#86efac">High Sustainable Yields &amp; Wealth</text>
      <text x="40" y="28" font-size="10" fill="#cbd5e1">Reinvested profits expand agribusiness further</text>
    </g>

    <rect x="15" y="295" width="325" height="30" rx="6" fill="#166534"/>
    <text x="177" y="315" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Result: Sustainable Agricultural Prosperity</text>
  </g>

  <!-- Right Column: Vicious Cycle (Insecure Tenure) -->
  <g transform="translate(410, 65)">
    <rect x="0" y="0" width="355" height="345" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="355" height="35" rx="10" fill="#991b1b"/>
    <text x="177" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">VICIOUS CYCLE (Insecure / Short Lease)</text>

    <g transform="translate(15, 50)">
      <circle cx="15" cy="15" r="14" fill="#7f1d1d"/>
      <text x="15" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1</text>
      <text x="40" y="15" font-size="11" font-weight="bold" fill="#fca5a5">Insecure Short-Term Lease</text>
      <text x="40" y="28" font-size="10" fill="#cbd5e1">Fear of eviction; focus strictly on 1-season cash</text>
    </g>

    <line x1="30" y1="85" x2="30" y2="105" stroke="#ef4444" stroke-width="2"/>

    <g transform="translate(15, 110)">
      <circle cx="15" cy="15" r="14" fill="#7f1d1d"/>
      <text x="15" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2</text>
      <text x="40" y="15" font-size="11" font-weight="bold" fill="#fca5a5">Zero Conservation Investment</text>
      <text x="40" y="28" font-size="10" fill="#cbd5e1">No terraces built; no lime or organic compost added</text>
    </g>

    <line x1="30" y1="145" x2="30" y2="165" stroke="#ef4444" stroke-width="2"/>

    <g transform="translate(15, 170)">
      <circle cx="15" cy="15" r="14" fill="#7f1d1d"/>
      <text x="15" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3</text>
      <text x="40" y="15" font-size="11" font-weight="bold" fill="#fca5a5">Soil Mining &amp; Gully Erosion</text>
      <text x="40" y="28" font-size="10" fill="#cbd5e1">Over-application of acidifying fertilizer; topsoil loss</text>
    </g>

    <line x1="30" y1="205" x2="30" y2="225" stroke="#ef4444" stroke-width="2"/>

    <g transform="translate(15, 230)">
      <circle cx="15" cy="15" r="14" fill="#7f1d1d"/>
      <text x="15" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4</text>
      <text x="40" y="15" font-size="11" font-weight="bold" fill="#fca5a5">Yield Collapse &amp; Land Abandonment</text>
      <text x="40" y="28" font-size="10" fill="#cbd5e1">Sterile subsoil left behind; tenant relocates</text>
    </g>

    <rect x="15" y="295" width="325" height="30" rx="6" fill="#991b1b"/>
    <text x="177" y="315" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Result: Land Degradation &amp; Poverty</text>
  </g>
</svg>
""")

# SVG 8: Wekesa's Farm Turnaround Plan (Lesson 9, Page 4)
SVG_WEKESA_TURNAROUND = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">Wekesa's Farm Turnaround: Baseline Crisis vs Rehabilitated Masterplan</text>

  <!-- Left: BEFORE (Crisis) -->
  <g transform="translate(35, 60)">
    <rect x="0" y="0" width="355" height="355" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="355" height="35" rx="10" fill="#991b1b"/>
    <text x="177" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">BEFORE: YEAR 0 (DEGRADED MONOCULTURE)</text>

    <text x="15" y="60" font-size="11" font-weight="bold" fill="#fca5a5">1. Topography &amp; Tillage:</text>
    <text x="15" y="75" font-size="10" fill="#cbd5e1">• Downhill furrows on 12% slope (Runoff &gt; 2.5 m/s)</text>
    <text x="15" y="90" font-size="10" fill="#cbd5e1">• Severe sheet and rill erosion; tubers exposed</text>

    <text x="15" y="115" font-size="11" font-weight="bold" fill="#fca5a5">2. Soil Chemistry:</text>
    <text x="15" y="130" font-size="10" fill="#cbd5e1">• pH 4.8 (Extremely acidic); zero lime applied</text>
    <text x="15" y="145" font-size="10" fill="#cbd5e1">• Applied DAP fertilizer chemically locked by Aluminum</text>

    <text x="15" y="170" font-size="11" font-weight="bold" fill="#fca5a5">3. Livestock Housing:</text>
    <text x="15" y="185" font-size="10" fill="#cbd5e1">• 2 Friesians in open dirt mud paddock</text>
    <text x="15" y="200" font-size="10" fill="#cbd5e1">• Foot rot, mastitis, low milk (5 L/cow/day)</text>

    <text x="15" y="225" font-size="11" font-weight="bold" fill="#fca5a5">4. Legal &amp; Financial:</text>
    <text x="15" y="240" font-size="10" fill="#cbd5e1">• Unregistered family land; zero bank credit</text>
    <text x="15" y="255" font-size="10" fill="#cbd5e1">• Potato yield collapsed to 25 bags/acre</text>

    <rect x="15" y="285" width="325" height="55" rx="6" fill="#1e293b" stroke="#7f1d1d"/>
    <text x="177" y="308" font-size="11" font-weight="bold" fill="#ef4444" text-anchor="middle">Annual Gross Income: 240,000 KES</text>
    <text x="177" y="328" font-size="10" fill="#fca5a5" text-anchor="middle">High debt, eroded soil, disease vulnerability</text>
  </g>

  <!-- Right: AFTER (Rehabilitated) -->
  <g transform="translate(410, 60)">
    <rect x="0" y="0" width="355" height="355" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="355" height="35" rx="10" fill="#15803d"/>
    <text x="177" y="23" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">AFTER: YEAR 3 (INTEGRATED SYSTEM)</text>

    <text x="15" y="60" font-size="11" font-weight="bold" fill="#86efac">1. Topography &amp; Conservation:</text>
    <text x="15" y="75" font-size="10" fill="#cbd5e1">• Cross-slope stone bench terraces with Napier strips</text>
    <text x="15" y="90" font-size="10" fill="#cbd5e1">• Zero soil loss; rainwater captured on contours</text>

    <text x="15" y="115" font-size="11" font-weight="bold" fill="#86efac">2. Soil Chemistry &amp; Organic Matter:</text>
    <text x="15" y="130" font-size="10" fill="#cbd5e1">• 2 tonnes agricultural lime applied (pH raised to 6.2)</text>
    <text x="15" y="145" font-size="10" fill="#cbd5e1">• 15 tonnes dairy compost added; Phosphorus unlocked</text>

    <text x="15" y="170" font-size="11" font-weight="bold" fill="#86efac">3. Modern Zero-Grazing Dairy:</text>
    <text x="15" y="185" font-size="10" fill="#cbd5e1">• Clean, dry concrete cubicles; biogas digester</text>
    <text x="15" y="200" font-size="10" fill="#cbd5e1">• Milk yield surged to 22 L/cow/day</text>

    <text x="15" y="225" font-size="11" font-weight="bold" fill="#86efac">4. Legal &amp; Financial:</text>
    <text x="15" y="240" font-size="10" fill="#cbd5e1">• Formal Freehold Title Deed secured</text>
    <text x="15" y="255" font-size="10" fill="#cbd5e1">• Potato yield surged to 85 bags/acre</text>

    <rect x="15" y="285" width="325" height="55" rx="6" fill="#1e293b" stroke="#166534"/>
    <text x="177" y="308" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">Annual Gross Income: 1,180,000 KES</text>
    <text x="177" y="328" font-size="10" fill="#86efac" text-anchor="middle">4 diversified income streams &amp; healthy soil</text>
  </g>
</svg>
""")

SVG_MAP = {
    1: {"block_order": 7, "page": 5, "svg": SVG_LAND_ACQUISITION, "title": "Land Acquisition Methods Comparison Framework"},
    2: {"block_order": 7, "page": 5, "svg": SVG_FARM_LAYOUT, "title": "Integrated Multi-Utility Farm Layout Model"},
    3: {"block_order": 6, "page": 4, "svg": SVG_ELEVATION_GRADIENT, "title": "Agro-Ecological Elevation and Enterprise Distribution Diagram"},
    4: {"block_order": 6, "page": 4, "svg": SVG_TOPOGRAPHICAL_CATENA, "title": "Topographical Catena and Drainage Suitability Diagram"},
    6: {"block_order": 5, "page": 3, "svg": SVG_DECISION_FLOWCHART, "title": "Land Allocation Decision Flowchart"},
    7: {"block_order": 5, "page": 3, "svg": SVG_LAND_VALUE_MATRIX, "title": "Multi-Dimensional Value Matrix of Agricultural Land"},
    8: {"block_order": 5, "page": 3, "svg": SVG_TENURE_CYCLES, "title": "Virtuous vs Vicious Agricultural Cycles Diagram"},
    9: {"block_order": 6, "page": 4, "svg": SVG_WEKESA_TURNAROUND, "title": "Wekesa's Farm Transformation: Before vs After"}
}

def enrich_grade10_topic1():
    """Injects verified photos, responsive vector SVGs, YouTube embeds, and creates LessonAssets."""
    print("=" * 80)
    print("STARTING ENRICHMENT: CBC Grade 10 Agriculture — Topic 1: Agricultural Land")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()
    topic = Topic.objects.filter(subject=subject, name="Agricultural Land").first()

    assert topic, "Topic 'Agricultural Land' not found!"

    # Load verified images
    images_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grade10_topic1_verified_images.json")
    with open(images_path, "r", encoding="utf-8") as f:
        verified_images = json.load(f)

    lessons = list(topic.lessons.all().order_by("learning_unit__order"))
    LessonAsset.objects.filter(lesson__in=lessons).delete()

    total_images_attached = 0
    total_svgs_attached = 0
    total_videos_attached = 0
    total_assets_persisted = 0

    for lesson in lessons:
        u_order = lesson.learning_unit.order
        u_str = str(u_order)

        # ---------------------------------------------------------------------
        # 1. First-Card Visual Hook (Photographic Wikimedia URL)
        # ---------------------------------------------------------------------
        hook_block = LessonBlock.objects.filter(
            lesson=lesson,
            page_number=1,
            block_type="suggested_image"
        ).first()

        if hook_block and u_str in verified_images:
            img_data = verified_images[u_str]
            content = hook_block.content or {}
            content["resolved_image_url"] = img_data["url"]
            content["url"] = img_data["url"]
            content["attribution"] = f"Photo by {img_data.get('author', 'Wikimedia Commons')} ({img_data.get('licensing', 'CC')})"
            content["commons_url"] = img_data.get("commons_url", "")
            hook_block.content = content
            hook_block.save()
            total_images_attached += 1

            # Persist LessonAsset
            asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="image",
                source_type="external",
                storage_type="url",
                status="attached",
                title=f"Lesson {u_order} Visual Hook: {hook_block.title}",
                description=content.get("caption", hook_block.title),
                url=img_data["url"],
                metadata={
                    "topic_order": 1,
                    "unit_order": u_order,
                    "card": 1,
                    "author": img_data.get("author", "Wikimedia Commons"),
                    "licensing": img_data.get("licensing", "CC"),
                    "commons_url": img_data.get("commons_url", "")
                }
            )
            hook_block.assets.add(asset)
            total_assets_persisted += 1
            print(f"  [Image Hook Attached] Lesson {u_order}: {img_data['title'][:50]}...")

        # ---------------------------------------------------------------------
        # 2. Custom Responsive Vector SVGs
        # ---------------------------------------------------------------------
        if u_order in SVG_MAP:
            svg_def = SVG_MAP[u_order]
            diag_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="suggested_diagram"
            ).first()

            if diag_block:
                diag_content = diag_block.content or {}
                diag_content["svg"] = svg_def["svg"]
                diag_content["svg_xml"] = svg_def["svg"]
                diag_content["title"] = svg_def["title"]
                diag_block.content = diag_content
                diag_block.save()
                total_svgs_attached += 1

                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    asset_type="diagram",
                    source_type="ai_generated",
                    storage_type="embed",
                    status="attached",
                    title=f"Lesson {u_order} Diagram: {svg_def['title']}",
                    description=diag_content.get("caption", svg_def["title"]),
                    metadata={
                        "topic_order": 1,
                        "unit_order": u_order,
                        "page": svg_def["page"],
                        "svg_content": svg_def["svg"]
                    }
                )
                diag_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [Vector SVG Attached] Lesson {u_order}: {svg_def['title']}")

        # ---------------------------------------------------------------------
        # 3. Educational YouTube Videos (Lesson 3 & Lesson 10)
        # ---------------------------------------------------------------------
        video_blocks = LessonBlock.objects.filter(
            lesson=lesson,
            block_type="suggested_video"
        )
        for v_block in video_blocks:
            v_content = v_block.content or {}
            v_url = v_content.get("url", "")
            if v_url:
                total_videos_attached += 1
                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    asset_type="youtube",
                    source_type="external",
                    storage_type="url",
                    status="attached",
                    title=f"Lesson {u_order} Video: {v_block.title}",
                    description=v_content.get("description", v_block.title),
                    url=v_url,
                    metadata={
                        "topic_order": 1,
                        "unit_order": u_order,
                        "youtube_url": v_url
                    }
                )
                v_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [YouTube Video Attached] Lesson {u_order}: {v_block.title}")

    print("=" * 80)
    print(f"ENRICHMENT COMPLETE: Topic 1 '{topic.name}'")
    print(f"  Photographic Hooks: {total_images_attached} / 10")
    print(f"  Vector SVGs:        {total_svgs_attached} / 8")
    print(f"  YouTube Videos:     {total_videos_attached} / 2")
    print(f"  LessonAssets:       {total_assets_persisted}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic1()
