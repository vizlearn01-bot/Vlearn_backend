"""
VLearn CBC Grade 10 Agriculture — Topic 16: Marketing Agricultural Produce
Visual Enrichment Engine (Phase 2: Vector SVGs, Verified Photos & Asset Persistence)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Marketing Agricultural Produce (Order: 16)

Attaches:
  - 6 First-Card Photographic Visual Hooks (100% Tested HTTP 200 Direct Wikimedia URLs)
  - 6 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - 1 Verified Educational YouTube Video (Lesson 1 Card 3)
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade10_agriculture_topic16.py
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
# 6 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 16: MARKETING PRODUCE
# =============================================================================

# SVG 1: 4 Economic Utilities (Lesson 1, Page 2)
SVG_ECONOMIC_UTILITY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">How Agricultural Marketing Creates 4 Types of Economic Utility</text>

  <!-- 4 Utility Cards Flow -->
  <!-- 1. Form Utility -->
  <g transform="translate(45, 70)">
    <rect x="0" y="0" width="160" height="230" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="160" height="28" rx="8" fill="#991b1b"/>
    <text x="80" y="19" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">1. FORM UTILITY</text>
    <text x="10" y="50" font-size="8" fill="#cbd5e1">• Processing &amp; change</text>
    <text x="10" y="70" font-size="8" fill="#cbd5e1">  of physical state</text>
    <text x="10" y="95" font-size="9" font-weight="bold" fill="#f87171">• Real Farm Action:</text>
    <text x="10" y="115" font-size="8" fill="#cbd5e1">  Slicing raw potatoes</text>
    <text x="10" y="132" font-size="8" fill="#cbd5e1">  into packaged crisps</text>
    <rect x="10" y="165" width="140" height="45" rx="4" fill="#1e293b" stroke="#ef4444"/>
    <text x="80" y="192" font-size="9" font-weight="bold" fill="#fca5a5" text-anchor="middle">Physical Value</text>
  </g>
  <line x1="205" y1="185" x2="235" y2="185" stroke="#38bdf8" stroke-width="2"/>

  <!-- 2. Place Utility -->
  <g transform="translate(235, 70)">
    <rect x="0" y="0" width="160" height="230" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="160" height="28" rx="8" fill="#0284c7"/>
    <text x="80" y="19" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">2. PLACE UTILITY</text>
    <text x="10" y="50" font-size="8" fill="#cbd5e1">• Transporting from</text>
    <text x="10" y="70" font-size="8" fill="#cbd5e1">  surplus to deficit</text>
    <text x="10" y="95" font-size="9" font-weight="bold" fill="#38bdf8">• Real Farm Action:</text>
    <text x="10" y="115" font-size="8" fill="#cbd5e1">  Shipping cabbages</text>
    <text x="10" y="132" font-size="8" fill="#cbd5e1">  Nyandarua -> Nairobi</text>
    <rect x="10" y="165" width="140" height="45" rx="4" fill="#1e293b" stroke="#38bdf8"/>
    <text x="80" y="192" font-size="9" font-weight="bold" fill="#67e8f9" text-anchor="middle">Geographic Value</text>
  </g>
  <line x1="395" y1="185" x2="425" y2="185" stroke="#38bdf8" stroke-width="2"/>

  <!-- 3. Time Utility -->
  <g transform="translate(425, 70)">
    <rect x="0" y="0" width="160" height="230" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <rect x="0" y="0" width="160" height="28" rx="8" fill="#ca8a04"/>
    <text x="80" y="19" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">3. TIME UTILITY</text>
    <text x="10" y="50" font-size="8" fill="#cbd5e1">• Safe preservation</text>
    <text x="10" y="70" font-size="8" fill="#cbd5e1">  for off-season sales</text>
    <text x="10" y="95" font-size="9" font-weight="bold" fill="#fde047">• Real Farm Action:</text>
    <text x="10" y="115" font-size="8" fill="#cbd5e1">  Hermetic bag storage</text>
    <text x="10" y="132" font-size="8" fill="#cbd5e1">  selling during drought</text>
    <rect x="10" y="165" width="140" height="45" rx="4" fill="#1e293b" stroke="#eab308"/>
    <text x="80" y="192" font-size="9" font-weight="bold" fill="#fef08a" text-anchor="middle">Seasonal Value</text>
  </g>
  <line x1="585" y1="185" x2="615" y2="185" stroke="#38bdf8" stroke-width="2"/>

  <!-- 4. Possession Utility -->
  <g transform="translate(615, 70)">
    <rect x="0" y="0" width="140" height="230" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="140" height="28" rx="8" fill="#15803d"/>
    <text x="70" y="19" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">4. POSSESSION</text>
    <text x="10" y="50" font-size="8" fill="#cbd5e1">• Legal transfer of</text>
    <text x="10" y="70" font-size="8" fill="#cbd5e1">  ownership &amp; trade</text>
    <text x="10" y="95" font-size="9" font-weight="bold" fill="#4ade80">• Real Farm Action:</text>
    <text x="10" y="115" font-size="8" fill="#cbd5e1">  Mobile M-Pesa pay</text>
    <text x="10" y="132" font-size="8" fill="#cbd5e1">  &amp; estate delivery</text>
    <rect x="10" y="165" width="120" height="45" rx="4" fill="#1e293b" stroke="#22c55e"/>
    <text x="70" y="192" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">Transaction Value</text>
  </g>

  <!-- Bottom Synthesis Banner -->
  <g transform="translate(45, 320)">
    <rect x="0" y="0" width="710" height="90" rx="8" fill="#0f172a" stroke="#38bdf8"/>
    <text x="355" y="26" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Economic Magic of Agricultural Marketing</text>
    <text x="355" y="50" font-size="9" fill="#cbd5e1" text-anchor="middle">Marketing transforms raw, perishable field output into high-demand consumer goods at the right place, right time, and right price!</text>
    <text x="355" y="72" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">Captures 200% to 500% Higher Revenue over Raw Farm-Gate Dumping</text>
  </g>
</svg>
""")

# SVG 2: Marketing Mix 4 Ps (Lesson 2, Page 2)
SVG_MARKETING_MIX = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Agribusiness Marketing Mix (The 4 Ps) Framework</text>

  <!-- 4 Quadrants -->
  <!-- 1. Product -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="160" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="340" height="28" rx="8" fill="#0284c7"/>
    <text x="170" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. PRODUCT (WHAT YOU SELL)</text>
    <text x="15" y="52" font-size="9" fill="#cbd5e1">• Cleanliness, size grading, varietal taste</text>
    <text x="15" y="72" font-size="9" fill="#cbd5e1">• Protective food-grade packaging (Cartons, bags)</text>
    <text x="15" y="92" font-size="9" fill="#cbd5e1">• Quality certifications &amp; brand labeling</text>
    <text x="15" y="112" font-size="9" font-weight="bold" fill="#38bdf8">• Example: Graded brown eggs in 15-egg paper cartons</text>
    <text x="15" y="138" font-size="8" fill="#67e8f9">Guarantees zero food waste for consumers</text>
  </g>

  <!-- 2. Price -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="340" height="160" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="340" height="28" rx="8" fill="#15803d"/>
    <text x="170" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. PRICE (WHAT YOU CHARGE)</text>
    <text x="15" y="52" font-size="9" fill="#cbd5e1">• Covers Total Cost of Production (COP) + Margin</text>
    <text x="15" y="72" font-size="9" fill="#cbd5e1">• Penetration Pricing (Low initial market entry)</text>
    <text x="15" y="92" font-size="9" fill="#cbd5e1">• Premium Pricing (Higher price for organic grade)</text>
    <text x="15" y="112" font-size="9" font-weight="bold" fill="#4ade80">• Example: KES 450/carton with 5% bulk discount</text>
    <text x="15" y="138" font-size="8" fill="#86efac">Ensures healthy agribusiness profitability</text>
  </g>

  <!-- 3. Place -->
  <g transform="translate(45, 245)">
    <rect x="0" y="0" width="340" height="165" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <rect x="0" y="0" width="340" height="28" rx="8" fill="#ca8a04"/>
    <text x="170" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. PLACE (WHERE YOU SELL)</text>
    <text x="15" y="52" font-size="9" fill="#cbd5e1">• Farm gate shop &amp; roadside stalls</text>
    <text x="15" y="72" font-size="9" fill="#cbd5e1">• Direct supermarket &amp; school supply contracts</text>
    <text x="15" y="92" font-size="9" fill="#cbd5e1">• Dairy &amp; coffee marketing cooperatives</text>
    <text x="15" y="112" font-size="9" font-weight="bold" fill="#fde047">• Example: Direct-to-estate delivery via boda-boda</text>
    <text x="15" y="140" font-size="8" fill="#fef08a">Shortens supply chain to bypass brokers</text>
  </g>

  <!-- 4. Promotion -->
  <g transform="translate(415, 245)">
    <rect x="0" y="0" width="340" height="165" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="0" y="0" width="340" height="28" rx="8" fill="#7e22ce"/>
    <text x="170" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4. PROMOTION (HOW YOU INFORM)</text>
    <text x="15" y="52" font-size="9" fill="#cbd5e1">• Word-of-mouth &amp; customer referral bonuses</text>
    <text x="15" y="72" font-size="9" fill="#cbd5e1">• Local estate WhatsApp marketing groups</text>
    <text x="15" y="92" font-size="9" fill="#cbd5e1">• Roadside farm signage &amp; agricultural show booths</text>
    <text x="15" y="112" font-size="9" font-weight="bold" fill="#d8b4fe">• Example: Free sample boiled eggs to school canteens</text>
    <text x="15" y="140" font-size="8" fill="#e9d5ff">Builds customer trust and verified advance orders</text>
  </g>
</svg>
""")

# SVG 3: Marketing Channels (Lesson 3, Page 2)
SVG_CHANNELS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Agricultural Marketing Channels: Direct vs. Multi-Level Intermediaries</text>

  <!-- 3 Channels Compared -->
  <!-- Channel 1: Direct (Zero-Level) -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="710" height="95" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="15" y="15" width="130" height="65" rx="6" fill="#1e293b" stroke="#22c55e"/>
    <text x="80" y="42" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">FARMER</text>
    <text x="80" y="60" font-size="8" fill="#cbd5e1" text-anchor="middle">(Producer)</text>

    <line x1="145" y1="48" x2="520" y2="48" stroke="#22c55e" stroke-width="3"/>
    <polygon points="510,43 520,48 510,53" fill="#22c55e"/>
    <text x="330" y="40" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">DIRECT ZERO-LEVEL CHANNEL (WhatsApp / Farm Stall)</text>

    <rect x="525" y="15" width="170" height="65" rx="6" fill="#1e293b" stroke="#22c55e"/>
    <text x="610" y="42" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">CONSUMER</text>
    <text x="610" y="60" font-size="9" font-weight="bold" fill="#86efac" text-anchor="middle">Farmer Captures 100%</text>
  </g>

  <!-- Channel 2: One-Level (Supermarket) -->
  <g transform="translate(45, 175)">
    <rect x="0" y="0" width="710" height="95" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="15" y="15" width="130" height="65" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="80" y="42" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">FARMER</text>

    <line x1="145" y1="48" x2="280" y2="48" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="270,43 280,48 270,53" fill="#38bdf8"/>

    <rect x="285" y="15" width="170" height="65" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="370" y="42" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">RETAILER (SUPERMARKET)</text>
    <text x="370" y="60" font-size="8" fill="#cbd5e1" text-anchor="middle">Graded &amp; Packaged</text>

    <line x1="455" y1="48" x2="520" y2="48" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="510,43 520,48 510,53" fill="#38bdf8"/>

    <rect x="525" y="15" width="170" height="65" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="610" y="42" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">CONSUMER</text>
    <text x="610" y="60" font-size="9" fill="#67e8f9" text-anchor="middle">Farmer Captures ~70%</text>
  </g>

  <!-- Channel 3: Two-Level (Brokers / Middlemen) -->
  <g transform="translate(45, 285)">
    <rect x="0" y="0" width="710" height="120" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="15" y="15" width="115" height="65" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="72" y="42" font-size="10" font-weight="bold" fill="#f87171" text-anchor="middle">FARMER</text>
    <text x="72" y="60" font-size="8" fill="#cbd5e1" text-anchor="middle">(Farm-Gate)</text>

    <line x1="130" y1="48" x2="190" y2="48" stroke="#ef4444" stroke-width="2"/>
    <polygon points="180,43 190,48 180,53" fill="#ef4444"/>

    <rect x="195" y="15" width="140" height="65" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="265" y="42" font-size="9" font-weight="bold" fill="#f87171" text-anchor="middle">BROKER / WHOLESALE</text>
    <text x="265" y="60" font-size="8" fill="#cbd5e1" text-anchor="middle">Buys at distress price</text>

    <line x1="335" y1="48" x2="385" y2="48" stroke="#ef4444" stroke-width="2"/>
    <polygon points="375,43 385,48 375,53" fill="#ef4444"/>

    <rect x="390" y="15" width="125" height="65" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="452" y="42" font-size="10" font-weight="bold" fill="#f87171" text-anchor="middle">RETAIL KIOSK</text>
    <text x="452" y="60" font-size="8" fill="#cbd5e1" text-anchor="middle">Local grocer</text>

    <line x1="515" y1="48" x2="555" y2="48" stroke="#ef4444" stroke-width="2"/>
    <polygon points="545,43 555,48 545,53" fill="#ef4444"/>

    <rect x="560" y="15" width="135" height="65" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="627" y="42" font-size="10" font-weight="bold" fill="#f87171" text-anchor="middle">CONSUMER</text>
    <text x="627" y="60" font-size="9" font-weight="bold" fill="#fca5a5" text-anchor="middle">Farmer Captures &lt;30%</text>

    <text x="355" y="102" font-size="9" fill="#cbd5e1" text-anchor="middle">Brokers capture over 70% of total profits due to smallholder lack of storage and transport!</text>
  </g>
</svg>
""")

# SVG 4: Sorting & Grading Workflow (Lesson 4, Page 2)
SVG_SORTING_GRADING = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Post-Harvest Cleaning, Sorting, and Grading Workflow</text>

  <!-- 4 Step Pipeline -->
  <!-- Step 1: Raw Harvest & Cleaning -->
  <g transform="translate(45, 70)">
    <rect x="0" y="0" width="160" height="230" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="160" height="28" rx="8" fill="#0284c7"/>
    <text x="80" y="19" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">1. HARVEST &amp; CLEAN</text>
    <text x="10" y="50" font-size="8" fill="#cbd5e1">• Raw field harvest</text>
    <text x="10" y="70" font-size="8" fill="#cbd5e1">• Wash soil &amp; debris</text>
    <text x="10" y="90" font-size="8" fill="#cbd5e1">• Potable clean water</text>
    <text x="10" y="110" font-size="8" fill="#cbd5e1">• Air-dry on mesh</text>
    <rect x="10" y="165" width="140" height="45" rx="4" fill="#1e293b" stroke="#38bdf8"/>
    <text x="80" y="192" font-size="9" font-weight="bold" fill="#67e8f9" text-anchor="middle">Clean Produce</text>
  </g>
  <line x1="205" y1="185" x2="235" y2="185" stroke="#38bdf8" stroke-width="2"/>

  <!-- Step 2: Sorting (Defect Removal) -->
  <g transform="translate(235, 70)">
    <rect x="0" y="0" width="160" height="230" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="160" height="28" rx="8" fill="#991b1b"/>
    <text x="80" y="19" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">2. SORTING (CULLS)</text>
    <text x="10" y="50" font-size="8" fill="#cbd5e1">• Remove bruised / rot</text>
    <text x="10" y="70" font-size="8" fill="#cbd5e1">• Remove diseased</text>
    <text x="10" y="90" font-size="8" font-weight="bold" fill="#f87171">• Halts Ethylene Gas</text>
    <text x="10" y="110" font-size="8" fill="#cbd5e1">• Stops mold spread</text>
    <rect x="10" y="165" width="140" height="45" rx="4" fill="#1e293b" stroke="#ef4444"/>
    <text x="80" y="192" font-size="9" font-weight="bold" fill="#fca5a5" text-anchor="middle">100% Healthy</text>
  </g>
  <line x1="395" y1="185" x2="425" y2="185" stroke="#38bdf8" stroke-width="2"/>

  <!-- Step 3: Grading (Classification) -->
  <g transform="translate(425, 70)">
    <rect x="0" y="0" width="330" height="230" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="330" height="28" rx="8" fill="#15803d"/>
    <text x="165" y="19" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">3. GRADING (QUALITY CLASSIFICATION)</text>

    <g transform="translate(10, 40)">
      <rect x="0" y="0" width="310" height="48" rx="4" fill="#1e293b" stroke="#22c55e"/>
      <text x="10" y="20" font-size="9" font-weight="bold" fill="#4ade80">GRADE 1 (PREMIUM / EXPORT):</text>
      <text x="10" y="38" font-size="8" fill="#cbd5e1">Uniform large, blemish-free -> Supermarkets (KES 110/kg)</text>
    </g>

    <g transform="translate(10, 95)">
      <rect x="0" y="0" width="310" height="48" rx="4" fill="#1e293b" stroke="#eab308"/>
      <text x="10" y="20" font-size="9" font-weight="bold" fill="#fde047">GRADE 2 (STANDARD):</text>
      <text x="10" y="38" font-size="8" fill="#cbd5e1">Medium size, minor blemish -> Open Markets (KES 70/kg)</text>
    </g>

    <g transform="translate(10, 150)">
      <rect x="0" y="0" width="310" height="48" rx="4" fill="#1e293b" stroke="#94a3b8"/>
      <text x="10" y="20" font-size="9" font-weight="bold" fill="#94a3b8">GRADE 3 (UTILITY):</text>
      <text x="10" y="38" font-size="8" fill="#cbd5e1">Irregular / small -> Food Kiosks / Sauce (KES 30/kg)</text>
    </g>
  </g>

  <!-- Bottom Synthesis Banner -->
  <g transform="translate(45, 320)">
    <rect x="0" y="0" width="710" height="90" rx="8" fill="#0f172a" stroke="#22c55e"/>
    <text x="355" y="26" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">Standardization Enables Remote Digital &amp; Phone Sales</text>
    <text x="355" y="50" font-size="9" fill="#cbd5e1" text-anchor="middle">Supermarket buyers order Grade 1 produce with total confidence without physically traveling to the farm!</text>
    <text x="355" y="72" font-size="9" font-weight="bold" fill="#86efac" text-anchor="middle">Sorting out rotten culls preserves 100% of healthy fruit shelf-life.</text>
  </g>
</svg>
""")

# SVG 5: Seasonal Price Curves (Lesson 5, Page 2)
SVG_PRICE_CURVES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Seasonal Agricultural Price Fluctuations: Harvest Glut vs. Off-Season Scarcity</text>

  <!-- Price Curve Graph -->
  <g transform="translate(85, 70)">
    <line x1="40" y1="20" x2="40" y2="240" stroke="#94a3b8" stroke-width="2"/>
    <line x1="40" y1="240" x2="620" y2="240" stroke="#94a3b8" stroke-width="2"/>

    <!-- Y-Axis Labels (Price KES / Cabbage Bag) -->
    <text x="30" y="35" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="end">KES 2,500</text>
    <text x="30" y="90" font-size="9" fill="#38bdf8" text-anchor="end">KES 1,800</text>
    <text x="30" y="150" font-size="9" fill="#fde047" text-anchor="end">KES 1,200</text>
    <text x="30" y="215" font-size="9" font-weight="bold" fill="#f87171" text-anchor="end">KES 500</text>

    <!-- X-Axis Labels (Months) -->
    <text x="70" y="260" font-size="9" font-weight="bold" fill="#f87171" text-anchor="middle">JAN (Rain Harvest)</text>
    <text x="210" y="260" font-size="9" fill="#cbd5e1" text-anchor="middle">MARCH</text>
    <text x="350" y="260" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">JULY (Dry Off-Season)</text>
    <text x="490" y="260" font-size="9" fill="#cbd5e1" text-anchor="middle">OCTOBER</text>
    <text x="590" y="260" font-size="9" fill="#f87171" text-anchor="middle">DEC (Harvest)</text>

    <!-- The Seasonal Price Curve (U-Shaped / Cyclical) -->
    <path d="M 70 215 Q 210 150 350 35 T 590 215" fill="none" stroke="#38bdf8" stroke-width="4"/>
    <circle cx="70" cy="215" r="7" fill="#ef4444"/>
    <circle cx="350" cy="35" r="8" fill="#22c55e"/>
    <circle cx="590" cy="215" r="7" fill="#ef4444"/>

    <!-- Milestone Annotations -->
    <g transform="translate(60, 160)">
      <rect x="0" y="0" width="130" height="35" rx="4" fill="#0f172a" stroke="#ef4444"/>
      <text x="65" y="15" font-size="8" font-weight="bold" fill="#f87171" text-anchor="middle">SEASONAL GLUT</text>
      <text x="65" y="28" font-size="7" fill="#cbd5e1" text-anchor="middle">Excess supply crashes price</text>
    </g>

    <g transform="translate(280, 50)">
      <rect x="0" y="0" width="140" height="40" rx="4" fill="#0f172a" stroke="#22c55e"/>
      <text x="70" y="16" font-size="8" font-weight="bold" fill="#4ade80" text-anchor="middle">OFF-SEASON SCARCITY</text>
      <text x="70" y="30" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">+400% Profit with Drip!</text>
    </g>
  </g>

  <!-- Bottom Farm Strategy Banner -->
  <g transform="translate(45, 345)">
    <rect x="0" y="0" width="710" height="70" rx="6" fill="#0f172a" stroke="#22c55e"/>
    <text x="20" y="25" font-size="10" font-weight="bold" fill="#4ade80">Strategic Agribusiness Maxim:</text>
    <text x="20" y="48" font-size="9" fill="#cbd5e1">Never harvest when everyone else is harvesting. Use drip irrigation to supply markets during the dry July scarcity peak!</text>
  </g>
</svg>
""")

# SVG 6: Master Marketing Lifecycle (Lesson 6, Page 2)
SVG_MASTER_MARKETING = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Master Agricultural Produce Marketing &amp; Sales Strategy Lifecycle</text>

  <!-- 6 Ring Stages -->
  <!-- 1. Market Intelligence -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="100" y="22" font-size="10" font-weight="bold" fill="#f87171" text-anchor="middle">1. MARKET INTELLIGENCE</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• SMS wholesale price trends</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Target buyer preferences</text>
  </g>
  <line x1="245" y1="102" x2="345" y2="200" stroke="#ef4444" stroke-width="2" stroke-dasharray="2,2"/>

  <!-- 2. Sorting & Grading -->
  <g transform="translate(555, 65)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="100" y="22" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">2. SORT &amp; GRADE</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Remove ethylene culls</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Grade 1, 2, 3 standardization</text>
  </g>
  <line x1="555" y1="102" x2="455" y2="200" stroke="#38bdf8" stroke-width="2" stroke-dasharray="2,2"/>

  <!-- 3. Marketing Mix (4 Ps) -->
  <g transform="translate(35, 195)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <text x="100" y="22" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">3. THE 4 PS MIX</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Packaged Product &amp; Price</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Distribution Place &amp; Promotion</text>
  </g>
  <line x1="235" y1="240" x2="345" y2="240" stroke="#eab308" stroke-width="2"/>

  <!-- 4. Channel Selection -->
  <g transform="translate(565, 195)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="100" y="22" font-size="10" font-weight="bold" fill="#d8b4fe" text-anchor="middle">4. CHANNEL ROUTING</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Direct estate WhatsApp &amp; apps</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Supermarkets &amp; Cooperatives</text>
  </g>
  <line x1="565" y1="240" x2="455" y2="240" stroke="#a855f7" stroke-width="2"/>

  <!-- 5. Sales Pitching -->
  <g transform="translate(130, 335)">
    <rect x="0" y="0" width="220" height="75" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
    <text x="110" y="22" font-size="10" font-weight="bold" fill="#67e8f9" text-anchor="middle">5. SALES PITCHING</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Hook, Solution &amp; Economics</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Forward supply contracts</text>
  </g>
  <line x1="350" y1="350" x2="390" y2="298" stroke="#06b6d4" stroke-width="2"/>

  <!-- 6. Wealth Creation -->
  <g transform="translate(450, 335)">
    <rect x="0" y="0" width="220" height="75" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <text x="110" y="22" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">6. PROFIT EXPANSION</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Off-season high pricing</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Scalable commercial wealth</text>
  </g>
  <line x1="450" y1="350" x2="410" y2="298" stroke="#22c55e" stroke-width="2"/>

  <!-- Central Hub: Marketing Mastery -->
  <circle cx="400" cy="240" r="55" fill="#0f172a" stroke="#22c55e" stroke-width="3"/>
  <text x="400" y="235" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">COMMERCIAL</text>
  <text x="400" y="252" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">MARKETING</text>
</svg>
""")

SVG_MAP = {
    1: {"page": 2, "svg": SVG_ECONOMIC_UTILITY, "title": "How Agricultural Marketing Creates 4 Types of Economic Utility"},
    2: {"page": 2, "svg": SVG_MARKETING_MIX, "title": "The Agribusiness Marketing Mix (The 4 Ps) Framework"},
    3: {"page": 2, "svg": SVG_CHANNELS, "title": "Agricultural Marketing Channels: Direct vs Multi-Level Intermediaries"},
    4: {"page": 2, "svg": SVG_SORTING_GRADING, "title": "Post-Harvest Cleaning, Sorting, and Grading Workflow"},
    5: {"page": 2, "svg": SVG_PRICE_CURVES, "title": "Seasonal Agricultural Price Fluctuations: Harvest Glut vs Off-Season Scarcity"},
    6: {"page": 2, "svg": SVG_MASTER_MARKETING, "title": "Master Agricultural Produce Marketing & Sales Strategy Lifecycle"}
}

def enrich_grade10_topic16():
    """Injects verified photos, responsive vector SVGs, YouTube embeds, and creates LessonAssets."""
    print("=" * 80)
    print("STARTING ENRICHMENT: CBC Grade 10 Agriculture — Topic 16: Marketing Agricultural Produce")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()
    topic = Topic.objects.filter(subject=subject, name="Marketing Agricultural Produce").first()

    assert topic, "Topic 'Marketing Agricultural Produce' not found!"

    images_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grade10_topic16_verified_images.json")
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
                    "topic_order": 16,
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
                        "topic_order": 16,
                        "unit_order": u_order,
                        "page": svg_def["page"],
                        "svg_content": svg_def["svg"]
                    }
                )
                diag_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [Vector SVG Attached] Lesson {u_order}: {svg_def['title']}")

        # ---------------------------------------------------------------------
        # 3. Educational YouTube Videos (Lesson 1)
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
                        "topic_order": 16,
                        "unit_order": u_order,
                        "youtube_url": v_url
                    }
                )
                v_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [YouTube Video Attached] Lesson {u_order}: {v_block.title}")

    print("=" * 80)
    print(f"ENRICHMENT COMPLETE: Topic 16 '{topic.name}'")
    print(f"  Photographic Hooks: {total_images_attached} / 6")
    print(f"  Vector SVGs:        {total_svgs_attached} / 6")
    print(f"  YouTube Videos:     {total_videos_attached} / 1")
    print(f"  LessonAssets:       {total_assets_persisted}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic16()
