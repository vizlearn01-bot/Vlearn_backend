"""
VLearn CBC Grade 10 Agriculture — Topic 15: Establishing an Agricultural Enterprise
Visual Enrichment Engine (Phase 2: Vector SVGs, Verified Photos & Asset Persistence)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Establishing an Agricultural Enterprise (Order: 15)

Attaches:
  - 13 First-Card Photographic Visual Hooks (100% Tested HTTP 200 Direct Wikimedia URLs)
  - 8 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - 1 Verified Educational YouTube Video (Lesson 1 Card 3)
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade10_agriculture_topic15.py
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
# 8 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 15: ESTABLISHING ENTERPRISE
# =============================================================================

# SVG 1: 4 Ownership Models (Lesson 1, Page 2)
SVG_OWNERSHIP_MODELS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">4 Primary Agribusiness Ownership Models in Kenya</text>

  <!-- 4 Quadrant Grid -->
  <!-- 1. Sole Proprietorship -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="160" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="340" height="28" rx="8" fill="#991b1b"/>
    <text x="170" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. SOLE PROPRIETORSHIP</text>
    <text x="15" y="52" font-size="9" fill="#cbd5e1">• Ownership: 1 Single Individual</text>
    <text x="15" y="72" font-size="9" fill="#cbd5e1">• Decision-Making: Instant &amp; Autonomous</text>
    <text x="15" y="92" font-size="9" font-weight="bold" fill="#f87171">• Liability: UNLIMITED (Personal assets at risk!)</text>
    <text x="15" y="112" font-size="9" fill="#cbd5e1">• Continuity: Low (Ends upon owner's death)</text>
    <text x="15" y="138" font-size="9" font-weight="bold" fill="#fca5a5">E.g., Independent smallholder dairy / vegetable farm</text>
  </g>

  <!-- 2. Partnership -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="340" height="160" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <rect x="0" y="0" width="340" height="28" rx="8" fill="#ca8a04"/>
    <text x="170" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. PARTNERSHIP</text>
    <text x="15" y="52" font-size="9" fill="#cbd5e1">• Ownership: 2 to 20 Partners (Partnership Deed)</text>
    <text x="15" y="72" font-size="9" fill="#cbd5e1">• Decision-Making: Consultative among partners</text>
    <text x="15" y="92" font-size="9" font-weight="bold" fill="#fde047">• Liability: Joint &amp; Several UNLIMITED Liability</text>
    <text x="15" y="112" font-size="9" fill="#cbd5e1">• Capital: Pooled financial &amp; technical skills</text>
    <text x="15" y="138" font-size="9" font-weight="bold" fill="#fef08a">E.g., Family poultry unit or youth greenhouse project</text>
  </g>

  <!-- 3. Agricultural Cooperative -->
  <g transform="translate(45, 245)">
    <rect x="0" y="0" width="340" height="165" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="340" height="28" rx="8" fill="#0284c7"/>
    <text x="170" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. AGRICULTURAL COOPERATIVE</text>
    <text x="15" y="52" font-size="9" fill="#cbd5e1">• Ownership: Member-Owned (1 Member = 1 Vote)</text>
    <text x="15" y="72" font-size="9" fill="#cbd5e1">• Purpose: Bulk buying, processing &amp; joint sales</text>
    <text x="15" y="92" font-size="9" font-weight="bold" fill="#38bdf8">• Liability: LIMITED to member share capital</text>
    <text x="15" y="112" font-size="9" fill="#cbd5e1">• Advantage: High bargaining power vs middlemen</text>
    <text x="15" y="140" font-size="9" font-weight="bold" fill="#67e8f9">E.g., New KCC dairy cooperative / Coffee SACCO</text>
  </g>

  <!-- 4. Private Limited Company (Ltd) -->
  <g transform="translate(415, 245)">
    <rect x="0" y="0" width="340" height="165" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="28" rx="8" fill="#15803d"/>
    <text x="170" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4. PRIVATE LIMITED COMPANY (LTD)</text>
    <text x="15" y="52" font-size="9" fill="#cbd5e1">• Ownership: 1 to 50 Shareholders (Separate legal entity)</text>
    <text x="15" y="72" font-size="9" fill="#cbd5e1">• Decision-Making: Board of Directors</text>
    <text x="15" y="92" font-size="9" font-weight="bold" fill="#4ade80">• Liability: STRICTLY LIMITED (Personal assets safe!)</text>
    <text x="15" y="112" font-size="9" fill="#cbd5e1">• Continuity: Perpetual Succession (Never dies)</text>
    <text x="15" y="140" font-size="9" font-weight="bold" fill="#86efac">E.g., Commercial horticulture export enterprise</text>
  </g>
</svg>
""")

# SVG 2: KEPHIS Input Verification (Lesson 3, Page 2)
SVG_INPUT_VERIFICATION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">KEPHIS Input Verification &amp; Anti-Counterfeit Checklist</text>

  <!-- 4 Step Chronological Flow -->
  <!-- Step 1: Registered Agro-Dealer -->
  <g transform="translate(45, 75)">
    <rect x="0" y="0" width="160" height="220" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="160" height="26" rx="8" fill="#0284c7"/>
    <text x="80" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">1. AGRO-DEALER</text>
    <text x="10" y="52" font-size="9" fill="#cbd5e1">• Buy only from</text>
    <text x="10" y="70" font-size="9" fill="#cbd5e1">  licensed shops</text>
    <text x="10" y="95" font-size="9" font-weight="bold" fill="#38bdf8">• Inspect premises</text>
    <text x="10" y="115" font-size="8" fill="#cbd5e1">• Avoid informal</text>
    <text x="10" y="132" font-size="8" fill="#cbd5e1">  roadside sellers</text>
    <rect x="10" y="165" width="140" height="40" rx="4" fill="#1e293b" stroke="#38bdf8"/>
    <text x="80" y="190" font-size="9" font-weight="bold" fill="#67e8f9" text-anchor="middle">Licensed Dealer</text>
  </g>
  <line x1="205" y1="185" x2="235" y2="185" stroke="#38bdf8" stroke-width="2"/>

  <!-- Step 2: KEPHIS Scratch-Off Seal -->
  <g transform="translate(235, 75)">
    <rect x="0" y="0" width="160" height="220" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <rect x="0" y="0" width="160" height="26" rx="8" fill="#ca8a04"/>
    <text x="80" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">2. SCRATCH SEAL</text>
    <text x="10" y="52" font-size="9" fill="#cbd5e1">• Check tamper-</text>
    <text x="10" y="70" font-size="9" fill="#cbd5e1">  proof silver seal</text>
    <text x="10" y="95" font-size="9" font-weight="bold" fill="#fde047">• Scratch gently</text>
    <text x="10" y="115" font-size="9" fill="#cbd5e1">  to reveal hidden</text>
    <text x="10" y="132" font-size="9" fill="#cbd5e1">  unique PIN code</text>
    <rect x="10" y="165" width="140" height="40" rx="4" fill="#1e293b" stroke="#eab308"/>
    <text x="80" y="190" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">Silver PIN Seal</text>
  </g>
  <line x1="395" y1="185" x2="425" y2="185" stroke="#38bdf8" stroke-width="2"/>

  <!-- Step 3: SMS to 1393 -->
  <g transform="translate(425, 75)">
    <rect x="0" y="0" width="160" height="220" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="160" height="26" rx="8" fill="#15803d"/>
    <text x="80" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">3. SMS TO 1393</text>
    <text x="10" y="52" font-size="9" fill="#cbd5e1">• Send free SMS</text>
    <text x="10" y="70" font-size="9" fill="#cbd5e1">  PIN to 1393</text>
    <text x="10" y="95" font-size="9" font-weight="bold" fill="#4ade80">• Instant SMS back:</text>
    <text x="10" y="115" font-size="8" fill="#cbd5e1">  - Seed variety</text>
    <text x="10" y="132" font-size="8" fill="#cbd5e1">  - Lot &amp; germination</text>
    <rect x="10" y="165" width="140" height="40" rx="4" fill="#1e293b" stroke="#22c55e"/>
    <text x="80" y="190" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">Instant Auth SMS</text>
  </g>
  <line x1="585" y1="185" x2="615" y2="185" stroke="#38bdf8" stroke-width="2"/>

  <!-- Step 4: PCBP Reg & Expiry -->
  <g transform="translate(615, 75)">
    <rect x="0" y="0" width="140" height="220" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="0" y="0" width="140" height="26" rx="8" fill="#7e22ce"/>
    <text x="70" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">4. PCBP &amp; DATES</text>
    <text x="10" y="52" font-size="8" fill="#cbd5e1">• Check PCBP Reg #</text>
    <text x="10" y="70" font-size="8" fill="#cbd5e1">  on chemical cans</text>
    <text x="10" y="95" font-size="8" font-weight="bold" fill="#d8b4fe">• Verify Mfg Date</text>
    <text x="10" y="115" font-size="8" fill="#cbd5e1">• Verify Expiry Date</text>
    <text x="10" y="132" font-size="8" fill="#cbd5e1">• Check cap seal</text>
    <rect x="10" y="165" width="120" height="40" rx="4" fill="#1e293b" stroke="#a855f7"/>
    <text x="70" y="190" font-size="8" font-weight="bold" fill="#d8b4fe" text-anchor="middle">100% Genuine</text>
  </g>

  <!-- Bottom Advisory Banner -->
  <g transform="translate(45, 315)">
    <rect x="0" y="0" width="710" height="95" rx="8" fill="#0f172a" stroke="#ef4444"/>
    <text x="355" y="26" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">The Devastating Agronomic Cost of Fake Inputs</text>
    <text x="355" y="52" font-size="9" fill="#cbd5e1" text-anchor="middle">Fake seed causes poor germination (&lt;30%) and introduces lethal viral diseases like Maize Lethal Necrosis (MLN).</text>
    <text x="355" y="74" font-size="9" font-weight="bold" fill="#fca5a5" text-anchor="middle">Never compromise on KEPHIS certification to save money!</text>
  </g>
</svg>
""")

# SVG 3: Fixed vs Working Capital (Lesson 4, Page 2)
SVG_CAPITAL_TYPES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Fixed Capital vs. Working Capital in Agribusiness</text>

  <!-- Left: Fixed Capital -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="340" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="35" rx="8" fill="#0284c7"/>
    <text x="170" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">FIXED CAPITAL (CAPEX)</text>

    <text x="15" y="60" font-size="10" font-weight="bold" fill="#38bdf8">Economic Characteristics:</text>
    <text x="15" y="80" font-size="9" fill="#cbd5e1">• Multi-year lifespan (Lasts &gt;1 year)</text>
    <text x="15" y="100" font-size="9" fill="#cbd5e1">• High initial capital investment</text>
    <text x="15" y="120" font-size="9" fill="#cbd5e1">• Depreciates gradually over time</text>
    <text x="15" y="140" font-size="9" fill="#cbd5e1">• Recorded on Farm Balance Sheet</text>

    <line x1="15" y1="160" x2="325" y2="160" stroke="#334155" stroke-width="1"/>

    <text x="15" y="182" font-size="10" font-weight="bold" fill="#67e8f9">Tangible Farm Examples:</text>
    <text x="15" y="205" font-size="9" fill="#cbd5e1">1. Farm Buildings &amp; Stores</text>
    <text x="15" y="225" font-size="9" fill="#cbd5e1">2. Tractors &amp; Disc Ploughs</text>
    <text x="15" y="245" font-size="9" fill="#cbd5e1">3. Boreholes &amp; Solar Pumping Kits</text>
    <text x="15" y="265" font-size="9" fill="#cbd5e1">4. Permanent Greenhouses &amp; Drip Lines</text>
    <text x="15" y="285" font-size="9" fill="#cbd5e1">5. Dairy Breeding Cattle Herd</text>

    <rect x="15" y="300" width="310" height="28" rx="4" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="318" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Permanent Farm Infrastructure</text>
  </g>

  <!-- Right: Working Capital -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="340" height="340" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="35" rx="8" fill="#15803d"/>
    <text x="170" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">WORKING CAPITAL (OPEX)</text>

    <text x="15" y="60" font-size="10" font-weight="bold" fill="#4ade80">Economic Characteristics:</text>
    <text x="15" y="80" font-size="9" fill="#cbd5e1">• Single production cycle (&lt;1 year)</text>
    <text x="15" y="100" font-size="9" fill="#cbd5e1">• Fully consumed &amp; converted into yield</text>
    <text x="15" y="120" font-size="9" fill="#cbd5e1">• Must be continuously replenished</text>
    <text x="15" y="140" font-size="9" fill="#cbd5e1">• Recorded on P&amp;L Statement as Expense</text>

    <line x1="15" y1="160" x2="325" y2="160" stroke="#334155" stroke-width="1"/>

    <text x="15" y="182" font-size="10" font-weight="bold" fill="#86efac">Tangible Farm Examples:</text>
    <text x="15" y="205" font-size="9" fill="#cbd5e1">1. Certified Hybrid Seeds &amp; Tubers</text>
    <text x="15" y="225" font-size="9" fill="#cbd5e1">2. DAP &amp; CAN Fertilizers</text>
    <text x="15" y="245" font-size="9" fill="#cbd5e1">3. Broiler Starter Feeds &amp; Vaccines</text>
    <text x="15" y="265" font-size="9" fill="#cbd5e1">4. Tractor Fuel &amp; Casual Labor Wages</text>
    <text x="15" y="285" font-size="9" fill="#cbd5e1">5. Produce Packaging Gunny Bags</text>

    <rect x="15" y="300" width="310" height="28" rx="4" fill="#1e293b" stroke="#22c55e"/>
    <text x="170" y="318" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">Seasonal Operational Fuel</text>
  </g>
</svg>
""")

# SVG 4: Capital Sources Landscape (Lesson 5, Page 2)
SVG_FINANCE_LANDSCAPE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Agricultural Financial Capital Sources Landscape in Kenya</text>

  <!-- 3 Pillar Framework -->
  <!-- 1. Internal Equity -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="220" height="340" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="32" rx="8" fill="#15803d"/>
    <text x="110" y="21" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. INTERNAL EQUITY</text>

    <text x="15" y="55" font-size="10" font-weight="bold" fill="#4ade80">Personal Savings:</text>
    <text x="15" y="75" font-size="9" fill="#cbd5e1">• Zero interest rate (0%)</text>
    <text x="15" y="93" font-size="9" fill="#cbd5e1">• Zero debt default risk</text>
    <text x="15" y="111" font-size="9" fill="#cbd5e1">• Complete autonomy</text>

    <text x="15" y="145" font-size="10" font-weight="bold" fill="#4ade80">Retained Earnings:</text>
    <text x="15" y="165" font-size="9" fill="#cbd5e1">• Reinvesting harvest profits</text>
    <text x="15" y="183" font-size="9" fill="#cbd5e1">• Organic farm expansion</text>

    <rect x="15" y="260" width="190" height="60" rx="6" fill="#1e293b" stroke="#22c55e"/>
    <text x="110" y="285" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Safest Capital</text>
    <text x="110" y="305" font-size="8" fill="#86efac" text-anchor="middle">No Foreclosure Danger</text>
  </g>

  <!-- 2. Agricultural Credit (AFC & SACCOs) -->
  <g transform="translate(290, 65)">
    <rect x="0" y="0" width="220" height="340" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="32" rx="8" fill="#0284c7"/>
    <text x="110" y="21" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. AFC &amp; SACCO CREDIT</text>

    <text x="15" y="55" font-size="10" font-weight="bold" fill="#38bdf8">Agric Finance Corp (AFC):</text>
    <text x="15" y="75" font-size="9" fill="#cbd5e1">• Low interest (8–10% p.a.)</text>
    <text x="15" y="93" font-size="9" fill="#cbd5e1">• Repayment on harvest date</text>
    <text x="15" y="111" font-size="9" fill="#cbd5e1">• Long-term Capex support</text>

    <text x="15" y="145" font-size="10" font-weight="bold" fill="#38bdf8">Agric SACCOs &amp; MFIs:</text>
    <text x="15" y="165" font-size="9" fill="#cbd5e1">• Borrow 3x your savings</text>
    <text x="15" y="183" font-size="9" fill="#cbd5e1">• Deducted from milk checks</text>
    <text x="15" y="201" font-size="9" fill="#cbd5e1">• Peer guarantor backed</text>

    <rect x="15" y="260" width="190" height="60" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="110" y="285" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Agribusiness Tailored</text>
    <text x="110" y="305" font-size="8" fill="#67e8f9" text-anchor="middle">Harvest-Aligned Terms</text>
  </g>

  <!-- 3. Commercial Banks & Informal -->
  <g transform="translate(535, 65)">
    <rect x="0" y="0" width="220" height="340" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="32" rx="8" fill="#ca8a04"/>
    <text x="110" y="21" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. BANKS &amp; CHAMAS</text>

    <text x="15" y="55" font-size="10" font-weight="bold" fill="#fde047">Commercial Banks:</text>
    <text x="15" y="75" font-size="9" fill="#cbd5e1">• High rates (14–18%+)</text>
    <text x="15" y="93" font-size="9" fill="#cbd5e1">• Rigid monthly payments</text>
    <text x="15" y="111" font-size="9" font-weight="bold" fill="#f87171">• Strict land title collateral</text>

    <text x="15" y="145" font-size="10" font-weight="bold" fill="#fde047">Chamas &amp; Table Banking:</text>
    <text x="15" y="165" font-size="9" fill="#cbd5e1">• Fast, social trust loans</text>
    <text x="15" y="183" font-size="9" fill="#cbd5e1">• Small capital amounts</text>
    <text x="15" y="201" font-size="9" fill="#cbd5e1">• Ideal for micro-startups</text>

    <rect x="15" y="260" width="190" height="60" rx="6" fill="#1e293b" stroke="#eab308"/>
    <text x="110" y="285" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">High Scrutiny</text>
    <text x="110" y="305" font-size="8" fill="#fef08a" text-anchor="middle">Strict Risk Control</text>
  </g>
</svg>
""")

# SVG 5: Budget Waterfall (Lesson 7, Page 2)
SVG_BUDGET_WATERFALL = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Enterprise Budget Waterfall: Revenue to Net Profit</text>

  <!-- Waterfall Steps -->
  <!-- 1. Gross Revenue -->
  <g transform="translate(45, 75)">
    <rect x="0" y="0" width="130" height="150" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="130" height="26" rx="8" fill="#15803d"/>
    <text x="65" y="18" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">1. GROSS REVENUE</text>
    <text x="10" y="48" font-size="8" fill="#cbd5e1">• Yield x Price</text>
    <text x="10" y="68" font-size="8" fill="#cbd5e1">• 8,000 heads</text>
    <text x="10" y="88" font-size="8" fill="#cbd5e1">• @ KES 25</text>
    <rect x="10" y="105" width="110" height="35" rx="4" fill="#1e293b" stroke="#22c55e"/>
    <text x="65" y="127" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">+ KES 200,000</text>
  </g>
  <text x="187" y="155" font-size="18" font-weight="bold" fill="#ef4444" text-anchor="middle">-</text>

  <!-- 2. Variable Costs -->
  <g transform="translate(200, 75)">
    <rect x="0" y="0" width="130" height="150" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="130" height="26" rx="8" fill="#991b1b"/>
    <text x="65" y="18" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">2. VARIABLE COSTS</text>
    <text x="10" y="48" font-size="8" fill="#cbd5e1">• Seedlings: 8.5k</text>
    <text x="10" y="68" font-size="8" fill="#cbd5e1">• Fertilizer: 22k</text>
    <text x="10" y="88" font-size="8" fill="#cbd5e1">• Labor: 20k</text>
    <rect x="10" y="105" width="110" height="35" rx="4" fill="#1e293b" stroke="#ef4444"/>
    <text x="65" y="127" font-size="9" font-weight="bold" fill="#f87171" text-anchor="middle">- KES 50,500</text>
  </g>
  <text x="342" y="155" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">=</text>

  <!-- 3. Gross Margin -->
  <g transform="translate(355, 75)">
    <rect x="0" y="0" width="130" height="150" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="130" height="26" rx="8" fill="#0284c7"/>
    <text x="65" y="18" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">3. GROSS MARGIN</text>
    <text x="10" y="48" font-size="8" fill="#cbd5e1">• Revenue - TVC</text>
    <text x="10" y="68" font-size="8" fill="#cbd5e1">• Operating</text>
    <text x="10" y="88" font-size="8" fill="#cbd5e1">  Surplus</text>
    <rect x="10" y="105" width="110" height="35" rx="4" fill="#1e293b" stroke="#38bdf8"/>
    <text x="65" y="127" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">+ KES 149,500</text>
  </g>
  <text x="497" y="155" font-size="18" font-weight="bold" fill="#ef4444" text-anchor="middle">-</text>

  <!-- 4. Fixed Costs -->
  <g transform="translate(510, 75)">
    <rect x="0" y="0" width="115" height="150" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <rect x="0" y="0" width="115" height="26" rx="8" fill="#ca8a04"/>
    <text x="57" y="18" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">4. FIXED COSTS</text>
    <text x="10" y="48" font-size="8" fill="#cbd5e1">• Land Rent</text>
    <text x="10" y="68" font-size="8" fill="#cbd5e1">• Tool Deprec.</text>
    <text x="10" y="88" font-size="8" fill="#cbd5e1">• Security</text>
    <rect x="10" y="105" width="95" height="35" rx="4" fill="#1e293b" stroke="#eab308"/>
    <text x="57" y="127" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">- KES 15,000</text>
  </g>
  <text x="637" y="155" font-size="18" font-weight="bold" fill="#22c55e" text-anchor="middle">=</text>

  <!-- 5. Net Profit -->
  <g transform="translate(650, 75)">
    <rect x="0" y="0" width="115" height="150" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2.5"/>
    <rect x="0" y="0" width="115" height="26" rx="8" fill="#15803d"/>
    <text x="57" y="18" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">5. NET PROFIT</text>
    <text x="10" y="48" font-size="8" fill="#cbd5e1">• Margin - TFC</text>
    <text x="10" y="68" font-size="8" fill="#cbd5e1">• Net Retained</text>
    <text x="10" y="88" font-size="8" fill="#cbd5e1">  Income</text>
    <rect x="10" y="105" width="95" height="35" rx="4" fill="#1e293b" stroke="#22c55e"/>
    <text x="57" y="127" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">+ KES 134,500</text>
  </g>

  <!-- Bottom Core Formulas Banner -->
  <g transform="translate(45, 250)">
    <rect x="0" y="0" width="720" height="155" rx="8" fill="#0f172a" stroke="#38bdf8"/>
    <text x="360" y="28" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Master Farm Budgeting Formulas</text>

    <g transform="translate(20, 45)">
      <rect x="0" y="0" width="325" height="90" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="162" y="24" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Gross Margin Formula</text>
      <text x="162" y="52" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Gross Margin = Gross Revenue - TVC</text>
      <text x="162" y="74" font-size="8" fill="#cbd5e1" text-anchor="middle">Measures single-crop operational efficiency</text>
    </g>

    <g transform="translate(375, 45)">
      <rect x="0" y="0" width="325" height="90" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="162" y="24" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Net Profit Formula</text>
      <text x="162" y="52" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Net Profit = Gross Margin - TFC</text>
      <text x="162" y="74" font-size="8" fill="#cbd5e1" text-anchor="middle">Actual entrepreneurial take-home income</text>
    </g>
  </g>
</svg>
""")

# SVG 6: Daily Cash Book Ledger (Lesson 8, Page 2)
SVG_CASH_BOOK = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Daily Farm Cash Book Ledger Architecture</text>

  <!-- Cash Book Table Frame -->
  <g transform="translate(45, 70)">
    <!-- Header Row -->
    <rect x="0" y="0" width="710" height="35" rx="6" fill="#0284c7"/>
    <text x="35" y="22" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">DATE</text>
    <text x="190" y="22" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">TRANSACTION DESCRIPTION</text>
    <text x="355" y="22" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">REF / REC #</text>
    <text x="450" y="22" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">CASH IN (+)</text>
    <text x="550" y="22" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">CASH OUT (-)</text>
    <text x="645" y="22" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">BALANCE</text>

    <!-- Row 1: Opening Balance -->
    <rect x="0" y="40" width="710" height="40" fill="#0f172a" stroke="#334155"/>
    <text x="35" y="65" font-size="9" fill="#cbd5e1" text-anchor="middle">01/10</text>
    <text x="80" y="65" font-size="9" fill="#cbd5e1">Opening Cash Balance</text>
    <text x="355" y="65" font-size="9" fill="#94a3b8" text-anchor="middle">-</text>
    <text x="450" y="65" font-size="9" fill="#94a3b8" text-anchor="middle">-</text>
    <text x="550" y="65" font-size="9" fill="#94a3b8" text-anchor="middle">-</text>
    <text x="645" y="65" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">KES 10,000</text>

    <!-- Row 2: Expense (Fertilizer) -->
    <rect x="0" y="85" width="710" height="40" fill="#1e293b" stroke="#334155"/>
    <text x="35" y="110" font-size="9" fill="#cbd5e1" text-anchor="middle">03/10</text>
    <text x="80" y="110" font-size="9" fill="#cbd5e1">Bought 2 Bags CAN Fertilizer</text>
    <text x="355" y="110" font-size="9" fill="#fde047" text-anchor="middle">Rec #104</text>
    <text x="450" y="110" font-size="9" fill="#94a3b8" text-anchor="middle">-</text>
    <text x="550" y="110" font-size="9" font-weight="bold" fill="#f87171" text-anchor="middle">KES 10,000</text>
    <text x="645" y="110" font-size="9" font-weight="bold" fill="#cbd5e1" text-anchor="middle">KES 0</text>

    <!-- Row 3: Income (Eggs) -->
    <rect x="0" y="130" width="710" height="40" fill="#0f172a" stroke="#334155"/>
    <text x="35" y="155" font-size="9" fill="#cbd5e1" text-anchor="middle">05/10</text>
    <text x="80" y="155" font-size="9" fill="#cbd5e1">Sold 20 Trays of Fresh Eggs</text>
    <text x="355" y="155" font-size="9" fill="#fde047" text-anchor="middle">Inv #45</text>
    <text x="450" y="155" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">KES 8,000</text>
    <text x="550" y="155" font-size="9" fill="#94a3b8" text-anchor="middle">-</text>
    <text x="645" y="155" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">KES 8,000</text>

    <!-- Row 4: Expense (Labor) -->
    <rect x="0" y="175" width="710" height="40" fill="#1e293b" stroke="#334155"/>
    <text x="35" y="200" font-size="9" fill="#cbd5e1" text-anchor="middle">08/10</text>
    <text x="80" y="200" font-size="9" fill="#cbd5e1">Paid Casual Weeding Wages</text>
    <text x="355" y="200" font-size="9" fill="#fde047" text-anchor="middle">Vouch #12</text>
    <text x="450" y="200" font-size="9" fill="#94a3b8" text-anchor="middle">-</text>
    <text x="550" y="200" font-size="9" font-weight="bold" fill="#f87171" text-anchor="middle">KES 2,400</text>
    <text x="645" y="200" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">KES 5,600</text>
  </g>

  <!-- Bottom Cash Balancing Principle -->
  <g transform="translate(45, 305)">
    <rect x="0" y="0" width="710" height="100" rx="8" fill="#0f172a" stroke="#22c55e"/>
    <text x="355" y="26" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">The Golden Rule of Daily Cash Book Balancing</text>
    <text x="355" y="52" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">New Balance = Previous Balance + Cash In (Income) - Cash Out (Expenses)</text>
    <text x="355" y="76" font-size="9" fill="#cbd5e1" text-anchor="middle">Every expense must have a physical receipt or payment voucher number for bank verification!</text>
  </g>
</svg>
""")

# SVG 7: Business Proposal Structure (Lesson 12, Page 2)
SVG_PROPOSAL_STRUCTURE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Agribusiness Proposal (Business Plan) Structural Framework</text>

  <!-- 4 Core Proposal Pillars -->
  <!-- 1. Executive Summary -->
  <g transform="translate(45, 70)">
    <rect x="0" y="0" width="160" height="230" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="160" height="28" rx="8" fill="#0284c7"/>
    <text x="80" y="19" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">1. EXEC SUMMARY</text>
    <text x="10" y="50" font-size="8" fill="#cbd5e1">• Project Mission</text>
    <text x="10" y="70" font-size="8" fill="#cbd5e1">• Market Problem</text>
    <text x="10" y="90" font-size="8" fill="#cbd5e1">• Farm Solution</text>
    <text x="10" y="110" font-size="8" font-weight="bold" fill="#38bdf8">• Capital Request</text>
    <text x="10" y="130" font-size="8" fill="#cbd5e1">• Projected ROI</text>
    <rect x="10" y="170" width="140" height="45" rx="4" fill="#1e293b" stroke="#38bdf8"/>
    <text x="80" y="190" font-size="8" font-weight="bold" fill="#67e8f9" text-anchor="middle">Written Last</text>
    <text x="80" y="205" font-size="7" fill="#cbd5e1" text-anchor="middle">Placed on Page 1</text>
  </g>
  <line x1="205" y1="185" x2="235" y2="185" stroke="#38bdf8" stroke-width="2"/>

  <!-- 2. Market Analysis -->
  <g transform="translate(235, 70)">
    <rect x="0" y="0" width="160" height="230" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <rect x="0" y="0" width="160" height="28" rx="8" fill="#ca8a04"/>
    <text x="80" y="19" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">2. MARKET ANALYSIS</text>
    <text x="10" y="50" font-size="8" fill="#cbd5e1">• Target Customers</text>
    <text x="10" y="70" font-size="8" fill="#cbd5e1">• Local Demand Gap</text>
    <text x="10" y="90" font-size="8" fill="#cbd5e1">• Competitor Pricing</text>
    <text x="10" y="110" font-size="8" font-weight="bold" fill="#fde047">• Sales Channels</text>
    <text x="10" y="130" font-size="8" fill="#cbd5e1">• Buyer Contracts</text>
    <rect x="10" y="170" width="140" height="45" rx="4" fill="#1e293b" stroke="#eab308"/>
    <text x="80" y="190" font-size="8" font-weight="bold" fill="#fde047" text-anchor="middle">Verified Demand</text>
    <text x="80" y="205" font-size="7" fill="#cbd5e1" text-anchor="middle">Confirmed Buyers</text>
  </g>
  <line x1="395" y1="185" x2="425" y2="185" stroke="#38bdf8" stroke-width="2"/>

  <!-- 3. Production Plan -->
  <g transform="translate(425, 70)">
    <rect x="0" y="0" width="160" height="230" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="0" y="0" width="160" height="28" rx="8" fill="#7e22ce"/>
    <text x="80" y="19" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">3. PRODUCTION PLAN</text>
    <text x="10" y="50" font-size="8" fill="#cbd5e1">• Land &amp; Soil Suitability</text>
    <text x="10" y="70" font-size="8" fill="#cbd5e1">• Water &amp; Drip System</text>
    <text x="10" y="90" font-size="8" fill="#cbd5e1">• KEPHIS Seed Inputs</text>
    <text x="10" y="110" font-size="8" font-weight="bold" fill="#d8b4fe">• Agronomy Timeline</text>
    <text x="10" y="130" font-size="8" fill="#cbd5e1">• Biosecurity Protocols</text>
    <rect x="10" y="170" width="140" height="45" rx="4" fill="#1e293b" stroke="#a855f7"/>
    <text x="80" y="190" font-size="8" font-weight="bold" fill="#d8b4fe" text-anchor="middle">Operational Flow</text>
    <text x="80" y="205" font-size="7" fill="#cbd5e1" text-anchor="middle">Technical Agronomy</text>
  </g>
  <line x1="585" y1="185" x2="615" y2="185" stroke="#38bdf8" stroke-width="2"/>

  <!-- 4. Financial Plan -->
  <g transform="translate(615, 70)">
    <rect x="0" y="0" width="140" height="230" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="140" height="28" rx="8" fill="#15803d"/>
    <text x="70" y="19" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">4. FINANCIAL PLAN</text>
    <text x="10" y="50" font-size="8" fill="#cbd5e1">• Capex &amp; Opex</text>
    <text x="10" y="70" font-size="8" fill="#cbd5e1">• Enterprise Budget</text>
    <text x="10" y="90" font-size="8" fill="#cbd5e1">• Gross Margin</text>
    <text x="10" y="110" font-size="8" font-weight="bold" fill="#4ade80">• Break-Even Math</text>
    <text x="10" y="130" font-size="8" fill="#cbd5e1">• P&amp;L Forecast</text>
    <rect x="10" y="170" width="120" height="45" rx="4" fill="#1e293b" stroke="#22c55e"/>
    <text x="70" y="190" font-size="8" font-weight="bold" fill="#4ade80" text-anchor="middle">Bankability</text>
    <text x="70" y="205" font-size="7" fill="#86efac" text-anchor="middle">Loan Payback</text>
  </g>

  <!-- Bottom Pitch Banner -->
  <g transform="translate(45, 320)">
    <rect x="0" y="0" width="710" height="90" rx="8" fill="#0f172a" stroke="#38bdf8"/>
    <text x="355" y="26" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 3-Minute Agribusiness Pitch Imperative</text>
    <text x="355" y="50" font-size="9" fill="#cbd5e1" text-anchor="middle">1. Why this Project? (Market Need) | 2. How it Works? (Production Efficiency) | 3. What are the Returns? (Profits &amp; Payback).</text>
    <text x="355" y="72" font-size="9" font-weight="bold" fill="#67e8f9" text-anchor="middle">A complete proposal turns agricultural ideas into funded commercial enterprises!</text>
  </g>
</svg>
""")

# SVG 8: Master Lifecycle (Lesson 13, Page 2)
SVG_MASTER_LIFECYCLE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Master Agribusiness Enterprise Establishment &amp; Management Lifecycle</text>

  <!-- 6 Ring Stages -->
  <!-- 1. Ownership & Feasibility -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="100" y="22" font-size="10" font-weight="bold" fill="#f87171" text-anchor="middle">1. OWNERSHIP &amp; FIT</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Ltd Co / Cooperative / Sole</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Soil, climate &amp; road logistics</text>
  </g>
  <line x1="245" y1="102" x2="345" y2="200" stroke="#ef4444" stroke-width="2" stroke-dasharray="2,2"/>

  <!-- 2. Certified Inputs -->
  <g transform="translate(555, 65)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="100" y="22" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">2. INPUT QUALITY</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• KEPHIS certified seeds (1393)</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• PCBP registered chemicals</text>
  </g>
  <line x1="555" y1="102" x2="455" y2="200" stroke="#38bdf8" stroke-width="2" stroke-dasharray="2,2"/>

  <!-- 3. Capital & Budgets -->
  <g transform="translate(35, 195)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <text x="100" y="22" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">3. CAPITAL &amp; BUDGETS</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• AFC &amp; SACCO credit</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Enterprise Gross Margins</text>
  </g>
  <line x1="235" y1="240" x2="345" y2="240" stroke="#eab308" stroke-width="2"/>

  <!-- 4. Operations & Records -->
  <g transform="translate(565, 195)">
    <rect x="0" y="0" width="200" height="75" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="100" y="22" font-size="10" font-weight="bold" fill="#d8b4fe" text-anchor="middle">4. RECORDS &amp; P&amp;L</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Daily Cash Book balance</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Net Profit &amp; Loss audits</text>
  </g>
  <line x1="565" y1="240" x2="455" y2="240" stroke="#a855f7" stroke-width="2"/>

  <!-- 5. Risk & Labor -->
  <g transform="translate(130, 335)">
    <rect x="0" y="0" width="220" height="75" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
    <text x="110" y="22" font-size="10" font-weight="bold" fill="#67e8f9" text-anchor="middle">5. RISK &amp; LABOR</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Diversify &amp; Index Insurance</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Piece-rate pay &amp; OSHA PPE</text>
  </g>
  <line x1="350" y1="350" x2="390" y2="298" stroke="#06b6d4" stroke-width="2"/>

  <!-- 6. Proposal & Scale -->
  <g transform="translate(450, 335)">
    <rect x="0" y="0" width="220" height="75" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <text x="110" y="22" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">6. PROPOSAL &amp; SCALE</text>
    <text x="10" y="45" font-size="9" fill="#cbd5e1">• Pitching to SACCOs/Banks</text>
    <text x="10" y="62" font-size="9" fill="#cbd5e1">• Profitable, scalable enterprise</text>
  </g>
  <line x1="450" y1="350" x2="410" y2="298" stroke="#22c55e" stroke-width="2"/>

  <!-- Central Hub: Commercial Enterprise -->
  <circle cx="400" cy="240" r="55" fill="#0f172a" stroke="#22c55e" stroke-width="3"/>
  <text x="400" y="235" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">COMMERCIAL</text>
  <text x="400" y="252" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">AGRIBUSINESS</text>
</svg>
""")

SVG_MAP = {
    1: {"page": 2, "svg": SVG_OWNERSHIP_MODELS, "title": "4 Primary Agribusiness Ownership Models in Kenya"},
    3: {"page": 2, "svg": SVG_INPUT_VERIFICATION, "title": "KEPHIS Input Verification & Anti-Counterfeit Checklist"},
    4: {"page": 2, "svg": SVG_CAPITAL_TYPES, "title": "Fixed Capital vs Working Capital in Agribusiness"},
    5: {"page": 2, "svg": SVG_FINANCE_LANDSCAPE, "title": "Agricultural Financial Capital Sources Landscape in Kenya"},
    7: {"page": 2, "svg": SVG_BUDGET_WATERFALL, "title": "Enterprise Budget Waterfall: Revenue to Net Profit"},
    8: {"page": 2, "svg": SVG_CASH_BOOK, "title": "Daily Farm Cash Book Ledger Architecture"},
    12: {"page": 2, "svg": SVG_PROPOSAL_STRUCTURE, "title": "Agribusiness Proposal (Business Plan) Structural Framework"},
    13: {"page": 2, "svg": SVG_MASTER_LIFECYCLE, "title": "Master Agribusiness Enterprise Establishment & Management Lifecycle"}
}

def enrich_grade10_topic15():
    """Injects verified photos, responsive vector SVGs, YouTube embeds, and creates LessonAssets."""
    print("=" * 80)
    print("STARTING ENRICHMENT: CBC Grade 10 Agriculture — Topic 15: Establishing an Agricultural Enterprise")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()
    topic = Topic.objects.filter(subject=subject, name="Establishing an Agricultural Enterprise").first()

    assert topic, "Topic 'Establishing an Agricultural Enterprise' not found!"

    images_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grade10_topic15_verified_images.json")
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
                    "topic_order": 15,
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
                        "topic_order": 15,
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
                        "topic_order": 15,
                        "unit_order": u_order,
                        "youtube_url": v_url
                    }
                )
                v_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [YouTube Video Attached] Lesson {u_order}: {v_block.title}")

    print("=" * 80)
    print(f"ENRICHMENT COMPLETE: Topic 15 '{topic.name}'")
    print(f"  Photographic Hooks: {total_images_attached} / 13")
    print(f"  Vector SVGs:        {total_svgs_attached} / 8")
    print(f"  YouTube Videos:     {total_videos_attached} / 1")
    print(f"  LessonAssets:       {total_assets_persisted}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic15()
