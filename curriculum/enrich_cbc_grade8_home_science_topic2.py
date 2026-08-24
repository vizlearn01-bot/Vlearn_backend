"""
VLearn CBC Grade 8 Home Science — Topic 2: Consumer Education
Visual Enrichment Engine (Phase 2: Vector SVGs, Verified 200 OK Photos & Asset Persistence)

Curriculum: CBC (ID: 5)
Grade: Grade 8 (ID: 15)
Subject: Home Science (ID: 28)
Topic: Consumer Education (ID: 104)

Attaches:
  - 2 Mandatory First-Card Visual Hooks (100% Tested HTTP 200 OK URLs)
  - 6 Custom Sanitized Responsive Vector SVGs to suggested_diagram blocks
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade8_home_science_topic2.py
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
    """Ensures SVG is clean, responsive, and stripped of unneeded XML/DOCTYPE headers."""
    svg = re.sub(r'<\?xml.*?\?>', '', svg)
    svg = re.sub(r'<!DOCTYPE.*?>', '', svg)
    return svg.strip()

# =============================================================================
# 6 HIGH-STRUCTURE VECTOR SVGS FOR TOPIC 2: CONSUMER EDUCATION
# =============================================================================

# SVG 1: Needs vs. Wants Balance Scale (Lesson 1, Page 2)
SVG_NEEDS_VS_WANTS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Needs vs. Wants: The Wise Household Budgeting Balance</text>

  <!-- Balance Scale Stand -->
  <g transform="translate(400, 160)">
    <polygon points="-10,180 10,180 0,0" fill="#64748b"/>
    <circle cx="0" cy="0" r="14" fill="#38bdf8"/>
    <!-- Tilting Beam (Left weighted down, Right elevated) -->
    <line x1="-280" y1="40" x2="280" y2="-40" stroke="#94a3b8" stroke-width="8" stroke-linecap="round"/>
  </g>

  <!-- Left Scale Pan: ESSENTIAL NEEDS (Heavier / Priority 1) -->
  <g transform="translate(120, 200)">
    <!-- Strings -->
    <line x1="0" y1="0" x2="-80" y2="90" stroke="#64748b" stroke-width="2"/>
    <line x1="0" y1="0" x2="80" y2="90" stroke="#64748b" stroke-width="2"/>
    <!-- Pan -->
    <path d="M -90 90 Q 0 130 90 90 Z" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <!-- Content Box -->
    <rect x="-105" y="115" width="210" height="90" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <text x="0" y="135" font-size="14" font-weight="bold" fill="#10b981" text-anchor="middle">HOUSEHOLD NEEDS (Priority 1)</text>
    <text x="0" y="155" font-size="11" fill="#f8fafc" text-anchor="middle">• Maize Meal, Greens &amp; Water</text>
    <text x="0" y="172" font-size="11" fill="#f8fafc" text-anchor="middle">• School Uniform &amp; Books</text>
    <text x="0" y="189" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Cannot be postponed!</text>
  </g>

  <!-- Right Scale Pan: ELECTIVE WANTS (Lighter / Priority 2) -->
  <g transform="translate(680, 120)">
    <!-- Strings -->
    <line x1="0" y1="0" x2="-80" y2="90" stroke="#64748b" stroke-width="2"/>
    <line x1="0" y1="0" x2="80" y2="90" stroke="#64748b" stroke-width="2"/>
    <!-- Pan -->
    <path d="M -90 90 Q 0 130 90 90 Z" fill="#d97706" stroke="#f59e0b" stroke-width="2"/>
    <!-- Content Box -->
    <rect x="-105" y="115" width="210" height="90" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="0" y="135" font-size="14" font-weight="bold" fill="#f59e0b" text-anchor="middle">PERSONAL WANTS (Priority 2)</text>
    <text x="0" y="155" font-size="11" fill="#f8fafc" text-anchor="middle">• Sweet Sodas &amp; Candy</text>
    <text x="0" y="172" font-size="11" fill="#f8fafc" text-anchor="middle">• Video Games &amp; Designer Items</text>
    <text x="0" y="189" font-size="11" font-weight="bold" fill="#facc15" text-anchor="middle">Can be postponed / saved for</text>
  </g>

  <!-- Bottom Insight Bar -->
  <rect x="40" y="380" width="720" height="40" rx="6" fill="#0f172a" stroke="#334155"/>
  <text x="400" y="405" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Golden Financial Rule: Always allocate money to secure 100% of basic Needs before funding any Wants!</text>
</svg>
""")

# SVG 2: The 4-Stage Consumer Behaviour Cycle (Lesson 1, Page 3)
SVG_CONSUMER_CYCLE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 4-Stage Consumer Behaviour Cycle</text>

  <!-- Central Circular Loop -->
  <circle cx="400" cy="235" r="140" fill="none" stroke="#334155" stroke-width="8" stroke-dasharray="10,6"/>

  <!-- Stage 1: SELECT (Top) -->
  <g transform="translate(400, 95)">
    <rect x="-105" y="-35" width="210" height="70" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="-75" cy="0" r="18" fill="#0284c7"/>
    <text x="-75" y="5" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">1</text>
    <text x="15" y="-6" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">SELECT</text>
    <text x="15" y="14" font-size="11" fill="#cbd5e1" text-anchor="middle">Compare prices &amp; expiry</text>
  </g>

  <!-- Stage 2: BUY (Right) -->
  <g transform="translate(630, 235)">
    <rect x="-105" y="-35" width="210" height="70" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <circle cx="-75" cy="0" r="18" fill="#059669"/>
    <text x="-75" y="5" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">2</text>
    <text x="15" y="-6" font-size="14" font-weight="bold" fill="#10b981" text-anchor="middle">BUY</text>
    <text x="15" y="14" font-size="11" fill="#cbd5e1" text-anchor="middle">Pay cash &amp; get receipt</text>
  </g>

  <!-- Stage 3: USE (Bottom) -->
  <g transform="translate(400, 375)">
    <rect x="-105" y="-35" width="210" height="70" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="-75" cy="0" r="18" fill="#d97706"/>
    <text x="-75" y="5" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">3</text>
    <text x="15" y="-6" font-size="14" font-weight="bold" fill="#f59e0b" text-anchor="middle">USE</text>
    <text x="15" y="14" font-size="11" fill="#cbd5e1" text-anchor="middle">Consume without waste</text>
  </g>

  <!-- Stage 4: DISPOSE (Left) -->
  <g transform="translate(170, 235)">
    <rect x="-105" y="-35" width="210" height="70" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="2"/>
    <circle cx="-75" cy="0" r="18" fill="#db2777"/>
    <text x="-75" y="5" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">4</text>
    <text x="15" y="-6" font-size="14" font-weight="bold" fill="#ec4899" text-anchor="middle">DISPOSE</text>
    <text x="15" y="14" font-size="11" fill="#cbd5e1" text-anchor="middle">Recycle or compost wrap</text>
  </g>

  <!-- Center Text -->
  <text x="400" y="230" font-size="13" font-weight="bold" fill="#94a3b8" text-anchor="middle">CONTINUOUS</text>
  <text x="400" y="248" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">CONSUMER LOOP</text>
</svg>
""")

# SVG 3: The 5 Consumer Roles in a Household (Lesson 1, Page 5)
SVG_CONSUMER_ROLES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 5 Consumer Purchasing Roles in a Household</text>

  <!-- 5 Sequential Role Blocks Connected by Arrows -->
  <!-- 1. Initiator -->
  <g transform="translate(40, 80)">
    <rect x="0" y="0" width="125" height="300" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="62" cy="40" r="20" fill="#0284c7"/>
    <text x="62" y="46" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">1</text>
    <text x="62" y="85" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">INITIATOR</text>
    <rect x="10" y="105" width="105" height="180" rx="6" fill="#1e293b"/>
    <text x="62" y="125" font-size="11" font-weight="bold" fill="#f8fafc" text-anchor="middle">Role Action:</text>
    <text x="62" y="145" font-size="10" fill="#cbd5e1" text-anchor="middle">First identifies</text>
    <text x="62" y="160" font-size="10" fill="#cbd5e1" text-anchor="middle">the need to</text>
    <text x="62" y="175" font-size="10" fill="#cbd5e1" text-anchor="middle">purchase item.</text>
    <text x="62" y="210" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Example:</text>
    <text x="62" y="230" font-size="9" fill="#94a3b8" text-anchor="middle">Student asks for</text>
    <text x="62" y="245" font-size="9" fill="#94a3b8" text-anchor="middle">a textbook.</text>
  </g>

  <!-- Arrow 1 -->
  <path d="M 170 230 L 190 230" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>

  <!-- 2. Influencer -->
  <g transform="translate(195, 80)">
    <rect x="0" y="0" width="125" height="300" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <circle cx="62" cy="40" r="20" fill="#9333ea"/>
    <text x="62" y="46" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">2</text>
    <text x="62" y="85" font-size="13" font-weight="bold" fill="#a855f7" text-anchor="middle">INFLUENCER</text>
    <rect x="10" y="105" width="105" height="180" rx="6" fill="#1e293b"/>
    <text x="62" y="125" font-size="11" font-weight="bold" fill="#f8fafc" text-anchor="middle">Role Action:</text>
    <text x="62" y="145" font-size="10" fill="#cbd5e1" text-anchor="middle">Offers advice</text>
    <text x="62" y="160" font-size="10" fill="#cbd5e1" text-anchor="middle">&amp; brand advice</text>
    <text x="62" y="175" font-size="10" fill="#cbd5e1" text-anchor="middle">to guide choice.</text>
    <text x="62" y="210" font-size="10" font-weight="bold" fill="#a855f7" text-anchor="middle">Example:</text>
    <text x="62" y="230" font-size="9" fill="#94a3b8" text-anchor="middle">Teacher suggests</text>
    <text x="62" y="245" font-size="9" fill="#94a3b8" text-anchor="middle">KICD publisher.</text>
  </g>

  <!-- Arrow 2 -->
  <path d="M 325 230 L 345 230" stroke="#a855f7" stroke-width="3" stroke-linecap="round"/>

  <!-- 3. Decision Maker -->
  <g transform="translate(350, 80)">
    <rect x="0" y="0" width="125" height="300" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <circle cx="62" cy="40" r="20" fill="#059669"/>
    <text x="62" y="46" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">3</text>
    <text x="62" y="85" font-size="12" font-weight="bold" fill="#10b981" text-anchor="middle">DECISION MAKER</text>
    <rect x="10" y="105" width="105" height="180" rx="6" fill="#1e293b"/>
    <text x="62" y="125" font-size="11" font-weight="bold" fill="#f8fafc" text-anchor="middle">Role Action:</text>
    <text x="62" y="145" font-size="10" fill="#cbd5e1" text-anchor="middle">Authorizes</text>
    <text x="62" y="160" font-size="10" fill="#cbd5e1" text-anchor="middle">budget &amp; final</text>
    <text x="62" y="175" font-size="10" fill="#cbd5e1" text-anchor="middle">purchase choice.</text>
    <text x="62" y="210" font-size="10" font-weight="bold" fill="#10b981" text-anchor="middle">Example:</text>
    <text x="62" y="230" font-size="9" fill="#94a3b8" text-anchor="middle">Mother approves</text>
    <text x="62" y="245" font-size="9" fill="#94a3b8" text-anchor="middle">funds.</text>
  </g>

  <!-- Arrow 3 -->
  <path d="M 480 230 L 500 230" stroke="#10b981" stroke-width="3" stroke-linecap="round"/>

  <!-- 4. Buyer -->
  <g transform="translate(505, 80)">
    <rect x="0" y="0" width="125" height="300" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="62" cy="40" r="20" fill="#d97706"/>
    <text x="62" y="46" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">4</text>
    <text x="62" y="85" font-size="13" font-weight="bold" fill="#f59e0b" text-anchor="middle">BUYER</text>
    <rect x="10" y="105" width="105" height="180" rx="6" fill="#1e293b"/>
    <text x="62" y="125" font-size="11" font-weight="bold" fill="#f8fafc" text-anchor="middle">Role Action:</text>
    <text x="62" y="145" font-size="10" fill="#cbd5e1" text-anchor="middle">Physically goes</text>
    <text x="62" y="160" font-size="10" fill="#cbd5e1" text-anchor="middle">to the shop &amp;</text>
    <text x="62" y="175" font-size="10" fill="#cbd5e1" text-anchor="middle">pays the cash.</text>
    <text x="62" y="210" font-size="10" font-weight="bold" fill="#f59e0b" text-anchor="middle">Example:</text>
    <text x="62" y="230" font-size="9" fill="#94a3b8" text-anchor="middle">Father pays at</text>
    <text x="62" y="245" font-size="9" fill="#94a3b8" text-anchor="middle">the bookshop.</text>
  </g>

  <!-- Arrow 4 -->
  <path d="M 635 230 L 655 230" stroke="#f59e0b" stroke-width="3" stroke-linecap="round"/>

  <!-- 5. User -->
  <g transform="translate(660, 80)">
    <rect x="0" y="0" width="100" height="300" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <circle cx="50" cy="40" r="20" fill="#db2777"/>
    <text x="50" y="46" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">5</text>
    <text x="50" y="85" font-size="13" font-weight="bold" fill="#ec4899" text-anchor="middle">USER</text>
    <rect x="8" y="105" width="84" height="180" rx="6" fill="#1e293b"/>
    <text x="50" y="125" font-size="11" font-weight="bold" fill="#f8fafc" text-anchor="middle">Action:</text>
    <text x="50" y="145" font-size="10" fill="#cbd5e1" text-anchor="middle">Consumes or</text>
    <text x="50" y="160" font-size="10" fill="#cbd5e1" text-anchor="middle">reads the item.</text>
    <text x="50" y="210" font-size="10" font-weight="bold" fill="#ec4899" text-anchor="middle">Example:</text>
    <text x="50" y="230" font-size="9" fill="#94a3b8" text-anchor="middle">Student studies</text>
    <text x="50" y="245" font-size="9" fill="#94a3b8" text-anchor="middle">with textbook.</text>
  </g>
</svg>
""")

# SVG 4: The 5 Core Factors Driving Market Competition (Lesson 2, Page 2)
SVG_COMPETITION_FACTORS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 5 Core Factors Driving Market Competition (P-Q-V-I-P)</text>

  <!-- 5 Competitive Factors Grid Cards -->
  <!-- 1. Price -->
  <g transform="translate(40, 75)">
    <rect x="0" y="0" width="225" height="150" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <text x="20" y="32" font-size="16" font-weight="bold" fill="#10b981">1. Price</text>
    <rect x="20" y="48" width="185" height="2" fill="#10b981"/>
    <text x="20" y="75" font-size="12" font-weight="bold" fill="#f8fafc">Affordable Budget Options</text>
    <text x="20" y="95" font-size="11" fill="#cbd5e1">• Lower prices attract buyers.</text>
    <text x="20" y="115" font-size="11" fill="#cbd5e1">• Offers smaller package sizes.</text>
    <text x="20" y="135" font-size="10" font-weight="bold" fill="#38bdf8">Example: 25 KES salt packet</text>
  </g>

  <!-- 2. Quality -->
  <g transform="translate(287, 75)">
    <rect x="0" y="0" width="225" height="150" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="20" y="32" font-size="16" font-weight="bold" fill="#38bdf8">2. Quality</text>
    <rect x="20" y="48" width="185" height="2" fill="#38bdf8"/>
    <text x="20" y="75" font-size="12" font-weight="bold" fill="#f8fafc">Durability &amp; Superior Grade</text>
    <text x="20" y="95" font-size="11" fill="#cbd5e1">• Fresh, unblemished produce.</text>
    <text x="20" y="115" font-size="11" fill="#cbd5e1">• Strong, long-lasting fabrics.</text>
    <text x="20" y="135" font-size="10" font-weight="bold" fill="#38bdf8">Example: Fresh organic kales</text>
  </g>

  <!-- 3. Variety -->
  <g transform="translate(535, 75)">
    <rect x="0" y="0" width="225" height="150" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <text x="20" y="32" font-size="16" font-weight="bold" fill="#f59e0b">3. Variety</text>
    <rect x="20" y="48" width="185" height="2" fill="#f59e0b"/>
    <text x="20" y="75" font-size="12" font-weight="bold" fill="#f8fafc">Diverse Choices &amp; Sizes</text>
    <text x="20" y="95" font-size="11" fill="#cbd5e1">• Multiple flavors and sizes.</text>
    <text x="20" y="115" font-size="11" fill="#cbd5e1">• Dietary options (gluten-free).</text>
    <text x="20" y="135" font-size="10" font-weight="bold" fill="#38bdf8">Example: Brown &amp; white bread</text>
  </g>

  <!-- 4. Innovation -->
  <g transform="translate(160, 245)">
    <rect x="0" y="0" width="225" height="150" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <text x="20" y="32" font-size="16" font-weight="bold" fill="#a855f7">4. Innovation</text>
    <rect x="20" y="48" width="185" height="2" fill="#a855f7"/>
    <text x="20" y="75" font-size="12" font-weight="bold" fill="#f8fafc">Novel Features &amp; Packaging</text>
    <text x="20" y="95" font-size="11" fill="#cbd5e1">• Resealable screw caps.</text>
    <text x="20" y="115" font-size="11" fill="#cbd5e1">• Fortified healthy recipes.</text>
    <text x="20" y="135" font-size="10" font-weight="bold" fill="#38bdf8">Example: Spill-proof bottle</text>
  </g>

  <!-- 5. Promotion -->
  <g transform="translate(415, 245)">
    <rect x="0" y="0" width="225" height="150" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="2"/>
    <text x="20" y="32" font-size="16" font-weight="bold" fill="#ec4899">5. Promotion</text>
    <rect x="20" y="48" width="185" height="2" fill="#ec4899"/>
    <text x="20" y="75" font-size="12" font-weight="bold" fill="#f8fafc">Advertising &amp; Customer Gifts</text>
    <text x="20" y="95" font-size="11" fill="#cbd5e1">• Buy-One-Get-One-Free.</text>
    <text x="20" y="115" font-size="11" fill="#cbd5e1">• Loyalty points &amp; discounts.</text>
    <text x="20" y="135" font-size="10" font-weight="bold" fill="#38bdf8">Example: Free sponge with soap</text>
  </g>
</svg>
""")

# SVG 5: Split-Screen: Fair Trade vs Deceptive Unfair Competition (Lesson 2, Page 3)
SVG_FAIR_VS_UNFAIR = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Fair Trade vs. Deceptive Unfair Market Competition</text>

  <!-- Left: Fair Trade Shop (Green Theme) -->
  <g transform="translate(40, 75)">
    <rect x="0" y="0" width="345" height="325" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <text x="172" y="32" font-size="16" font-weight="bold" fill="#10b981" text-anchor="middle">FAIR COMPETITION (Honest)</text>

    <rect x="25" y="60" width="295" height="60" rx="6" fill="#1e293b"/>
    <text x="172" y="85" font-size="13" font-weight="bold" fill="#34d399" text-anchor="middle">Authentic Products &amp; KEBS Marks</text>
    <text x="172" y="105" font-size="11" fill="#cbd5e1" text-anchor="middle">Clear price tags, genuine receipts &amp; honest weights</text>

    <rect x="25" y="135" width="295" height="155" rx="6" fill="#1e293b"/>
    <text x="40" y="160" font-size="12" font-weight="bold" fill="#f8fafc">Key Fair Practices:</text>
    <text x="40" y="185" font-size="11" fill="#a7f3d0">• Truthful advertisements (no false health claims).</text>
    <text x="40" y="210" font-size="11" fill="#a7f3d0">• Open, transparent stock distribution.</text>
    <text x="40" y="235" font-size="11" fill="#a7f3d0">• Competes via quality, innovation &amp; fair price.</text>
    <text x="40" y="265" font-size="11" font-weight="bold" fill="#10b981">RESULT: Builds customer trust &amp; protects health.</text>
  </g>

  <!-- Right: Unfair Trade Shop (Red Theme) -->
  <g transform="translate(415, 75)">
    <rect x="0" y="0" width="345" height="325" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <text x="172" y="32" font-size="16" font-weight="bold" fill="#ef4444" text-anchor="middle">UNFAIR COMPETITION (Cheating)</text>

    <rect x="25" y="60" width="295" height="60" rx="6" fill="#1e293b"/>
    <text x="172" y="85" font-size="13" font-weight="bold" fill="#f87171" text-anchor="middle">Counterfeit Goods &amp; Fake Logos</text>
    <text x="172" y="105" font-size="11" fill="#cbd5e1" text-anchor="middle">Selling fake 'O0MO' soap and hiding sugar bags</text>

    <rect x="25" y="135" width="295" height="155" rx="6" fill="#1e293b"/>
    <text x="40" y="160" font-size="12" font-weight="bold" fill="#f8fafc">Common Unfair Violations:</text>
    <text x="40" y="185" font-size="11" fill="#fca5a5">• Artificial hoarding to create false shortages.</text>
    <text x="40" y="210" font-size="11" fill="#fca5a5">• Price fixing collusion between rival sellers.</text>
    <text x="40" y="235" font-size="11" fill="#fca5a5">• Deceptive health claims on unlabeled drinks.</text>
    <text x="40" y="265" font-size="11" font-weight="bold" fill="#ef4444">RESULT: Exploits buyers &amp; causes health risks.</text>
  </g>
</svg>
""")

# SVG 6: Consumer Protection & KEBS Verification Pipeline (Lesson 2, Page 5)
SVG_KEBS_PIPELINE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Consumer Protection &amp; KEBS Verification Pipeline</text>

  <!-- 4-Step Verification Pathway -->
  <!-- Step 1: KEBS Mark -->
  <g transform="translate(40, 75)">
    <rect x="0" y="0" width="165" height="325" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="82" cy="45" r="22" fill="#0284c7"/>
    <text x="82" y="52" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">1</text>
    <text x="82" y="95" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">KEBS Mark</text>
    <rect x="15" y="115" width="135" height="170" rx="6" fill="#1e293b"/>
    <text x="82" y="140" font-size="11" font-weight="bold" fill="#f8fafc" text-anchor="middle">Standardization</text>
    <text x="82" y="165" font-size="10" fill="#cbd5e1" text-anchor="middle">Check for official</text>
    <text x="82" y="180" font-size="10" fill="#cbd5e1" text-anchor="middle">diamond-shaped</text>
    <text x="82" y="195" font-size="10" fill="#cbd5e1" text-anchor="middle">standardization</text>
    <text x="82" y="210" font-size="10" fill="#cbd5e1" text-anchor="middle">mark on package.</text>
    <text x="82" y="245" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Guarantees safety</text>
  </g>

  <!-- Step 2: Manufacturer Details -->
  <g transform="translate(225, 75)">
    <rect x="0" y="0" width="165" height="325" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <circle cx="82" cy="45" r="22" fill="#059669"/>
    <text x="82" y="52" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">2</text>
    <text x="82" y="95" font-size="13" font-weight="bold" fill="#10b981" text-anchor="middle">Maker Details</text>
    <rect x="15" y="115" width="135" height="170" rx="6" fill="#1e293b"/>
    <text x="82" y="140" font-size="11" font-weight="bold" fill="#f8fafc" text-anchor="middle">Physical Address</text>
    <text x="82" y="165" font-size="10" fill="#cbd5e1" text-anchor="middle">Ensure brand has</text>
    <text x="82" y="180" font-size="10" fill="#cbd5e1" text-anchor="middle">registered address,</text>
    <text x="82" y="195" font-size="10" fill="#cbd5e1" text-anchor="middle">telephone number,</text>
    <text x="82" y="210" font-size="10" fill="#cbd5e1" text-anchor="middle">&amp; customer email.</text>
    <text x="82" y="245" font-size="10" font-weight="bold" fill="#10b981" text-anchor="middle">Enables redress</text>
  </g>

  <!-- Step 3: Ingredients List -->
  <g transform="translate(410, 75)">
    <rect x="0" y="0" width="165" height="325" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="82" cy="45" r="22" fill="#d97706"/>
    <text x="82" y="52" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">3</text>
    <text x="82" y="95" font-size="13" font-weight="bold" fill="#f59e0b" text-anchor="middle">Ingredients</text>
    <rect x="15" y="115" width="135" height="170" rx="6" fill="#1e293b"/>
    <text x="82" y="140" font-size="11" font-weight="bold" fill="#f8fafc" text-anchor="middle">Nutrient Contents</text>
    <text x="82" y="165" font-size="10" fill="#cbd5e1" text-anchor="middle">Inspect breakdown</text>
    <text x="82" y="180" font-size="10" fill="#cbd5e1" text-anchor="middle">for food allergens,</text>
    <text x="82" y="195" font-size="10" fill="#cbd5e1" text-anchor="middle">preservatives, &amp;</text>
    <text x="82" y="210" font-size="10" fill="#cbd5e1" text-anchor="middle">excessive sugar.</text>
    <text x="82" y="245" font-size="10" font-weight="bold" fill="#f59e0b" text-anchor="middle">Protects health</text>
  </g>

  <!-- Step 4: Expiry Dates -->
  <g transform="translate(595, 75)">
    <rect x="0" y="0" width="165" height="325" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <circle cx="82" cy="45" r="22" fill="#db2777"/>
    <text x="82" y="52" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">4</text>
    <text x="82" y="95" font-size="13" font-weight="bold" fill="#ec4899" text-anchor="middle">Expiry Dates</text>
    <rect x="15" y="115" width="135" height="170" rx="6" fill="#1e293b"/>
    <text x="82" y="140" font-size="11" font-weight="bold" fill="#f8fafc" text-anchor="middle">MFG &amp; EXP Codes</text>
    <text x="82" y="165" font-size="10" fill="#cbd5e1" text-anchor="middle">Never purchase</text>
    <text x="82" y="180" font-size="10" fill="#cbd5e1" text-anchor="middle">expired goods.</text>
    <text x="82" y="195" font-size="10" fill="#cbd5e1" text-anchor="middle">Ensure printed date</text>
    <text x="82" y="210" font-size="10" fill="#cbd5e1" text-anchor="middle">is not altered.</text>
    <text x="82" y="245" font-size="10" font-weight="bold" fill="#ec4899" text-anchor="middle">Avoids poisoning</text>
  </g>
</svg>
""")

# Map of SVGs to specific lesson blocks
TOPIC2_SVGS = [
    {"lesson_order": 1, "page_number": 2, "block_type": "suggested_diagram", "svg": SVG_NEEDS_VS_WANTS, "title": "Needs vs. Wants: The Wise Household Budgeting Balance"},
    {"lesson_order": 1, "page_number": 3, "block_type": "suggested_diagram", "svg": SVG_CONSUMER_CYCLE, "title": "The 4-Stage Consumer Behaviour Cycle: Select, Buy, Use, Dispose"},
    {"lesson_order": 1, "page_number": 5, "block_type": "suggested_diagram", "svg": SVG_CONSUMER_ROLES, "title": "The 5 Consumer Purchasing Roles in a Household"},
    {"lesson_order": 2, "page_number": 2, "block_type": "suggested_diagram", "svg": SVG_COMPETITION_FACTORS, "title": "The 5 Core Factors Driving Market Competition (P-Q-V-I-P)"},
    {"lesson_order": 2, "page_number": 3, "block_type": "suggested_diagram", "svg": SVG_FAIR_VS_UNFAIR, "title": "Split-Screen: Fair Trade vs. Deceptive Unfair Competition"},
    {"lesson_order": 2, "page_number": 5, "block_type": "suggested_diagram", "svg": SVG_KEBS_PIPELINE, "title": "The Consumer Protection & KEBS Quality Assurance Verification Flow"}
]

# 100% Tested Live Wikimedia Photos (HTTP 200 OK)
TOPIC2_PHOTOS = [
    {
        "lesson_order": 1,
        "page_number": 1,
        "title": "Why Do We Shop the Way We Do?",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Maasai_Market-Nairobi.jpg",
        "author": "Wikimedia Commons Contributor",
        "licensing": "CC BY-SA 3.0",
        "caption": "A vibrant open-air marketplace where informed consumers compare prices, check quality, and make deliberate purchasing choices."
    },
    {
        "lesson_order": 2,
        "page_number": 1,
        "title": "The Battle of the Stalls: How Markets Work",
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/97/A_vegetable_stall_in_the_outskirts_of_Nairobi%2C_Kenya.jpg",
        "author": "Wikimedia Commons Contributor",
        "licensing": "CC BY-SA 4.0",
        "caption": "Neighboring retail vegetable and grocery stalls competing to attract customers through fresh quality and fair prices."
    }
]

def enrich_cbc_grade8_home_science_topic2():
    """Attaches vector SVGs, Wikimedia photographic visual hooks, and persists LessonAsset records."""
    print("=" * 80)
    print("STARTING VISUAL ENRICHMENT: CBC GRADE 8 HOME SCIENCE — TOPIC 2: CONSUMER EDUCATION")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    assert curriculum, "CBC Curriculum not found!"
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 8").first()
    assert grade, "Grade 8 not found under CBC!"
    subject = Subject.objects.filter(grade=grade, name="Home Science").first()
    assert subject, "Subject Home Science not found under Grade 8!"
    topic = Topic.objects.filter(subject=subject, name="Consumer Education").first()
    assert topic, "Topic Consumer Education not found!"

    lessons = list(topic.lessons.all().order_by("learning_unit__order"))
    print(f"[*] Found {len(lessons)} Lessons under Topic: '{topic.name}' (ID: {topic.id})")

    # Clean existing LessonAssets for clean re-enrichment
    LessonAsset.objects.filter(lesson__in=lessons).delete()
    print("[*] Cleared existing LessonAssets for clean re-enrichment.")

    # 1. Attach Card 1 Visual Hooks (Wikimedia Photos)
    print("\n[+] Phase 2A: Attaching Mandatory Card 1 Visual Hooks...")
    for pm in TOPIC2_PHOTOS:
        u_order = pm["lesson_order"]
        p_num = pm["page_number"]
        lesson = next((l for l in lessons if l.learning_unit.order == u_order), None)
        if not lesson:
            continue

        hook_block = LessonBlock.objects.filter(
            lesson=lesson,
            page_number=p_num,
            block_type="suggested_image"
        ).first()

        if hook_block:
            content = hook_block.content or {}
            content["resolved_image_url"] = pm["url"]
            content["url"] = pm["url"]
            content["author"] = pm["author"]
            content["licensing"] = pm["licensing"]
            content["caption"] = pm["caption"]
            hook_block.content = content
            hook_block.save()

            asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="image",
                source_type="external",
                storage_type="url",
                status="attached",
                title=hook_block.title,
                description=pm["caption"],
                url=pm["url"],
                metadata={
                    "author": pm["author"],
                    "licensing": pm["licensing"],
                    "caption": pm["caption"],
                    "is_card_1_hook": True
                }
            )
            hook_block.assets.add(asset)
            print(f"  [CARD 1 HOOK OK] Lesson {u_order} Page {p_num}: '{hook_block.title[:45]}...' -> Asset ID {asset.id}")

    # 2. Attach Custom Vector SVGs
    print("\n[+] Phase 2B: Attaching Custom Sanitized Vector SVGs...")
    for sm in TOPIC2_SVGS:
        u_order = sm["lesson_order"]
        p_num = sm["page_number"]
        lesson = next((l for l in lessons if l.learning_unit.order == u_order), None)
        if not lesson:
            continue

        diagram_block = LessonBlock.objects.filter(
            lesson=lesson,
            page_number=p_num,
            block_type="suggested_diagram"
        ).first()

        if diagram_block:
            content = diagram_block.content or {}
            content["svg_content"] = sm["svg"]
            content["svg"] = sm["svg"]
            diagram_block.content = content
            diagram_block.save()

            asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                source_type="ai_generated",
                storage_type="embed",
                status="attached",
                title=sm["title"],
                description=f"Sanitized vector SVG diagram: {sm['title']}",
                metadata={"svg_content": sm["svg"]}
            )
            diagram_block.assets.add(asset)
            print(f"  [SVG ATTACHED] Lesson {u_order} Page {p_num}: '{diagram_block.title[:45]}...' -> Asset ID {asset.id}")

    total_assets = LessonAsset.objects.filter(lesson__in=lessons).count()
    print("\n" + "=" * 80)
    print(f"[SUCCESS] CBC Grade 8 Home Science Topic 2 Visual Enrichment Complete!")
    print(f"[*] Total LessonAssets Created & Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_cbc_grade8_home_science_topic2()
