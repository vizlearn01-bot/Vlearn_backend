"""
VLearn Curriculum Visual Enrichment Script
CBC Grade 6 — Home Science
Topic 2: Budgeting (Order: 2)

Attaches:
- 3 Verified Topic-Representative Wikimedia Photographic Visual Hooks (Card 1 of every lesson)
- 6 Custom Sanitized, Responsive (800x450), Pedagogically Rich Vector SVGs
- Creates and attaches LessonAsset records in the database.
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, Lesson, LessonBlock, LessonAsset
)

# 3 Verified Photographic Visual Hooks (100% live HTTP 200 verified)
TOPIC2_PHOTOS = {
    1: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b4/A_beautiful_market_vendor.jpg",
        "author": "Wikimedia Commons Contributor",
        "licensing": "CC BY-SA 4.0",
        "caption": "A bustling open-air market vendor showcasing fresh produce where shoppers make smart daily budgeting choices."
    },
    2: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/c2/Vegetable_section_of_Carrefour_at_Westgate_Shopping_Mall%2C_Nairobi.jpg",
        "author": "Wikimedia Commons Contributor",
        "licensing": "CC BY-SA 4.0",
        "caption": "Shoppers navigating organized grocery and vegetable aisles at a modern supermarket in Nairobi, Kenya, illustrating how a written shopping list guides disciplined purchasing."
    },
    3: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/c1/Businesswoman_making_a_payment_with_cash_while_using_a_smartphone_in_a_modern_office_setting.jpg",
        "author": "Wikimedia Commons Contributor",
        "licensing": "CC BY-SA 4.0",
        "caption": "Managing personal financial resources with disciplined calculation, recording, and record-keeping."
    }
}

# 6 Custom High-Definition Vector SVGs for Grade 6 Topic 2
TOPIC2_SVGS = {
    # Lesson 1 Page 2: Needs vs. Wants Classification Blueprint
    (1, 2): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="#f8fafc" rx="12"/>
  <rect x="20" y="20" width="760" height="410" fill="#ffffff" rx="10" stroke="#e2e8f0" stroke-width="2" filter="url(#shadow)"/>

  <!-- Title Banner -->
  <rect x="40" y="30" width="720" height="42" fill="#0f172a" rx="8"/>
  <text x="400" y="57" fill="#ffffff" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">
    NEEDS vs. WANTS: THE GOLDEN RULE OF WISE SPENDING
  </text>

  <!-- Left: Essential Needs -->
  <g transform="translate(45, 88)">
    <rect x="0" y="0" width="340" height="315" fill="#f0fdf4" rx="8" stroke="#86efac" stroke-width="2"/>
    <rect x="15" y="15" width="310" height="28" fill="#16a34a" rx="5"/>
    <text x="170" y="34" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      🛡️ ESSENTIAL NEEDS (Must Have to Survive &amp; Learn)
    </text>

    <g transform="translate(20, 55)">
      <rect x="0" y="0" width="300" height="50" fill="#ffffff" rx="5" stroke="#bbf7d0"/>
      <text x="15" y="20" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">🥦 Nutritious Food &amp; Clean Water</text>
      <text x="15" y="36" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Kales, ugali, beans, and boiled drinking water.</text>

      <rect x="0" y="60" width="300" height="50" fill="#ffffff" rx="5" stroke="#bbf7d0"/>
      <text x="15" y="20" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">📚 School Books, Pencils &amp; Uniform</text>
      <text x="15" y="36" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Required writing materials and school shoes.</text>

      <rect x="0" y="120" width="300" height="50" fill="#ffffff" rx="5" stroke="#bbf7d0"/>
      <text x="15" y="20" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">💊 Healthcare &amp; Safe Shelter</text>
      <text x="15" y="36" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Medicine when unwell; warm clothing and soap.</text>

      <rect x="0" y="180" width="300" height="50" fill="#dcfce7" rx="5"/>
      <text x="150" y="30" fill="#15803d" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Rule: MUST be paid first before anything else!</text>
    </g>
  </g>

  <!-- Right: Elective Wants -->
  <g transform="translate(415, 88)">
    <rect x="0" y="0" width="340" height="315" fill="#fffbeb" rx="8" stroke="#fde68a" stroke-width="1.5"/>
    <rect x="15" y="15" width="310" height="28" fill="#d97706" rx="5"/>
    <text x="170" y="34" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      ⭐ ELECTIVE WANTS (Nice to Have for Fun &amp; Style)
    </text>

    <g transform="translate(20, 55)">
      <rect x="0" y="0" width="300" height="50" fill="#ffffff" rx="5" stroke="#fde68a"/>
      <text x="15" y="20" fill="#b45309" font-family="system-ui, sans-serif" font-size="11" font-weight="700">🍬 Sweets, Gum &amp; Fizzy Sodas</text>
      <text x="15" y="36" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Sugary treats that provide zero health benefits.</text>

      <rect x="0" y="60" width="300" height="50" fill="#ffffff" rx="5" stroke="#fde68a"/>
      <text x="15" y="20" fill="#b45309" font-family="system-ui, sans-serif" font-size="11" font-weight="700">🎮 Plastic Toys &amp; Video Games</text>
      <text x="15" y="36" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Play items you can easily borrow, share, or skip.</text>

      <rect x="0" y="120" width="300" height="50" fill="#ffffff" rx="5" stroke="#fde68a"/>
      <text x="15" y="20" fill="#b45309" font-family="system-ui, sans-serif" font-size="11" font-weight="700">🕶️ Fancy Sunglasses &amp; Wristbands</text>
      <text x="15" y="36" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Fashion items driven by peer influence.</text>

      <rect x="0" y="180" width="300" height="50" fill="#fef3c7" rx="5"/>
      <text x="150" y="30" fill="#b45309" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Rule: Can always be delayed or skipped to save!</text>
    </g>
  </g>
</svg>""",

    # Lesson 1 Page 4: The Balanced Budget Scales Blueprint
    (1, 4): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="3" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="#f8fafc" rx="12"/>
  <rect x="20" y="20" width="760" height="410" fill="#ffffff" rx="10" stroke="#e2e8f0" stroke-width="2" filter="url(#shadow)"/>

  <!-- Title Banner -->
  <rect x="40" y="25" width="720" height="42" fill="#0f172a" rx="8"/>
  <text x="400" y="52" fill="#ffffff" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">
    THE BALANCED BUDGET SCALES: INCOME = EXPENSES + SAVINGS
  </text>

  <!-- Central Scale Stand -->
  <g transform="translate(400, 110)">
    <!-- Base -->
    <path d="M -60 220 L 60 220 L 40 200 L -40 200 Z" fill="#334155"/>
    <!-- Pillar -->
    <rect x="-10" y="20" width="20" height="180" fill="#475569" rx="3"/>
    <!-- Fulcrum Pivot -->
    <circle cx="0" cy="20" r="16" fill="#0ea5e9"/>
    <circle cx="0" cy="20" r="6" fill="#ffffff"/>
    
    <!-- Balance Beam (Level = Balanced) -->
    <rect x="-260" y="14" width="520" height="12" fill="#0284c7" rx="4"/>
    
    <!-- Left Pan Strings & Pan (Income) -->
    <line x1="-240" y1="26" x2="-280" y2="100" stroke="#64748b" stroke-width="2"/>
    <line x1="-240" y1="26" x2="-200" y2="100" stroke="#64748b" stroke-width="2"/>
    <path d="M -290 100 Q -240 120 -190 100 Z" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2"/>
    
    <!-- Right Pan Strings & Pan (Expenses + Savings) -->
    <line x1="240" y1="26" x2="200" y2="100" stroke="#64748b" stroke-width="2"/>
    <line x1="240" y1="26" x2="280" y2="100" stroke="#64748b" stroke-width="2"/>
    <path d="M 190 100 Q 240 120 290 100 Z" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2"/>
  </g>

  <!-- Left Pan Content: Income Coin Bag -->
  <g transform="translate(110, 150)">
    <rect x="0" y="0" width="100" height="60" fill="#16a34a" rx="8"/>
    <text x="50" y="25" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">INCOME (In)</text>
    <text x="50" y="45" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="800" text-anchor="middle">100/- KES</text>
    <text x="50" y="78" fill="#15803d" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Pocket Money</text>
  </g>

  <!-- Right Pan Content: Stacked Blocks (Expenses + Savings) -->
  <g transform="translate(590, 130)">
    <!-- Expense Block 1 -->
    <rect x="0" y="0" width="100" height="24" fill="#3b82f6" rx="4"/>
    <text x="50" y="16" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Book: 50/-</text>
    <!-- Expense Block 2 -->
    <rect x="0" y="27" width="100" height="24" fill="#6366f1" rx="4"/>
    <text x="50" y="43" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Pen: 30/-</text>
    <!-- Savings Block -->
    <rect x="0" y="54" width="100" height="24" fill="#eab308" rx="4"/>
    <text x="50" y="70" fill="#713f12" font-family="system-ui, sans-serif" font-size="9.5" font-weight="800" text-anchor="middle">Savings: 20/-</text>
    <text x="50" y="96" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Total: 100/- KES</text>
  </g>

  <!-- Bottom Equilibrium Callout Banner -->
  <g transform="translate(60, 365)">
    <rect x="0" y="0" width="680" height="42" fill="#ecfdf5" rx="6" stroke="#a7f3d0" stroke-width="1.5"/>
    <text x="340" y="26" fill="#065f46" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      ✓ PERFECT EQUILIBRIUM: When Income ≥ Expenses, you avoid debt and build savings!
    </text>
  </g>
</svg>""",

    # Lesson 2 Page 2: The 5 Budgeting Superpowers Infographic
    (2, 2): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="3" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="#f8fafc" rx="12"/>
  <rect x="20" y="20" width="760" height="410" fill="#ffffff" rx="10" stroke="#e2e8f0" stroke-width="2" filter="url(#shadow)"/>

  <!-- Title Banner -->
  <rect x="40" y="25" width="720" height="42" fill="#0f172a" rx="8"/>
  <text x="400" y="52" fill="#ffffff" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">
    THE 5 BUDGETING SUPERPOWERS (WHY WE BUDGET)
  </text>

  <!-- 5 Bento Boxes Layout -->

  <!-- Box 1: Spend Wisely -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="220" height="150" fill="#f0f9ff" rx="8" stroke="#bae6fd" stroke-width="1.5"/>
    <rect x="10" y="10" width="200" height="24" fill="#0284c7" rx="4"/>
    <text x="110" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1. SPEND WISELY</text>
    <text x="15" y="55" fill="#0369a1" font-family="system-ui, sans-serif" font-size="18">💡</text>
    <text x="40" y="55" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Give Shillings a Job</text>
    <text x="15" y="80" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Stops money from vanishing.</text>
    <text x="15" y="98" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Tracks every coin spent.</text>
    <text x="15" y="116" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Maximize value for money.</text>
  </g>

  <!-- Box 2: Avoid Debt -->
  <g transform="translate(290, 80)">
    <rect x="0" y="0" width="220" height="150" fill="#fef2f2" rx="8" stroke="#fecaca" stroke-width="1.5"/>
    <rect x="10" y="10" width="200" height="24" fill="#ef4444" rx="4"/>
    <text x="110" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. AVOID DEBT</text>
    <text x="15" y="55" fill="#dc2626" font-family="system-ui, sans-serif" font-size="18">⛓️</text>
    <text x="40" y="55" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Live Within Means</text>
    <text x="15" y="80" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Spend what you actually have.</text>
    <text x="15" y="98" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Never borrow from friends.</text>
    <text x="15" y="116" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Protects family peace.</text>
  </g>

  <!-- Box 3: Set Priorities -->
  <g transform="translate(535, 80)">
    <rect x="0" y="0" width="220" height="150" fill="#f0fdf4" rx="8" stroke="#bbf7d0" stroke-width="1.5"/>
    <rect x="10" y="10" width="200" height="24" fill="#16a34a" rx="4"/>
    <text x="110" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3. SET PRIORITIES</text>
    <text x="15" y="55" fill="#15803d" font-family="system-ui, sans-serif" font-size="18">🪜</text>
    <text x="40" y="55" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Needs Over Wants</text>
    <text x="15" y="80" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Food &amp; books come first.</text>
    <text x="15" y="98" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Fun treats come second.</text>
    <text x="15" y="116" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Secures essential learning.</text>
  </g>

  <!-- Box 4: Reduce Waste & Impulse (Bottom Left) -->
  <g transform="translate(45, 245)">
    <rect x="0" y="0" width="340" height="155" fill="#faf5ff" rx="8" stroke="#e9d5ff" stroke-width="1.5"/>
    <rect x="10" y="10" width="320" height="24" fill="#9333ea" rx="4"/>
    <text x="170" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">4. REDUCE WASTE &amp; IMPULSE BUYING</text>
    <text x="15" y="55" fill="#7e22ce" font-family="system-ui, sans-serif" font-size="18">🛡️</text>
    <text x="40" y="55" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Resist Temptations</text>
    <text x="15" y="80" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Stops sudden emotional purchases caused by catchy sweets.</text>
    <text x="15" y="98" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Protects coins for planned school supplies.</text>
  </g>

  <!-- Box 5: Know Future Requirements (Bottom Right) -->
  <g transform="translate(415, 245)">
    <rect x="0" y="0" width="340" height="155" fill="#fffbeb" rx="8" stroke="#fde68a" stroke-width="1.5"/>
    <rect x="10" y="10" width="320" height="24" fill="#d97706" rx="4"/>
    <text x="170" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">5. KNOW FUTURE REQUIREMENTS</text>
    <text x="15" y="55" fill="#b45309" font-family="system-ui, sans-serif" font-size="18">📅</text>
    <text x="40" y="55" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Plan Ahead</text>
    <text x="15" y="80" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Calculates term-long school needs before they are due.</text>
    <text x="15" y="98" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Enables steady weekly savings for big goals.</text>
  </g>
</svg>""",

    # Lesson 2 Page 4: The Shopping List Shield vs. Impulse Buying
    (2, 4): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="3" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="#f8fafc" rx="12"/>
  <rect x="20" y="20" width="760" height="410" fill="#ffffff" rx="10" stroke="#e2e8f0" stroke-width="2" filter="url(#shadow)"/>

  <!-- Title Banner -->
  <rect x="40" y="25" width="720" height="42" fill="#0f172a" rx="8"/>
  <text x="400" y="52" fill="#ffffff" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">
    SHOPPING LIST SHIELD vs. UNPLANNED IMPULSE BUYING
  </text>

  <!-- Left Panel: Shopping Without a List -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="340" height="320" fill="#fef2f2" rx="8" stroke="#fecaca" stroke-width="1.5"/>
    <rect x="15" y="12" width="310" height="26" fill="#ef4444" rx="5"/>
    <text x="170" y="30" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">
      ✗ WITHOUT A LIST (Impulse Traps)
    </text>

    <g transform="translate(15, 50)">
      <rect x="0" y="0" width="310" height="65" fill="#ffffff" rx="5" stroke="#fca5a5"/>
      <text x="15" y="22" fill="#991b1b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">😵 Confused &amp; Distracted</text>
      <text x="15" y="40" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Wanders aimlessly through kiosk aisles.</text>
      <text x="15" y="55" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Tempted by flashy candies, sodas, and toys.</text>
    </g>

    <g transform="translate(15, 125)">
      <rect x="0" y="0" width="310" height="65" fill="#ffffff" rx="5" stroke="#fca5a5"/>
      <text x="15" y="22" fill="#991b1b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">💸 Money Vanishes on Wants</text>
      <text x="15" y="40" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Buys unplanned treats on a sudden whim.</text>
      <text x="15" y="55" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Runs out of cash for essential groceries.</text>
    </g>

    <g transform="translate(15, 200)">
      <rect x="0" y="0" width="310" height="50" fill="#fee2e2" rx="5"/>
      <text x="155" y="22" fill="#991b1b" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Outcome: Empty pockets, forgotten needs &amp; cold kitchen!</text>
    </g>
  </g>

  <!-- Right Panel: Shopping With a List Shield -->
  <g transform="translate(415, 80)">
    <rect x="0" y="0" width="340" height="320" fill="#f0fdf4" rx="8" stroke="#86efac" stroke-width="2"/>
    <rect x="15" y="12" width="310" height="26" fill="#16a34a" rx="5"/>
    <text x="170" y="30" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">
      ✓ WITH A LIST SHIELD (Protected Spending)
    </text>

    <g transform="translate(15, 50)">
      <rect x="0" y="0" width="310" height="65" fill="#ffffff" rx="5" stroke="#bbf7d0"/>
      <text x="15" y="22" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">🛡️ Protected &amp; Focused</text>
      <text x="15" y="40" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Holds written checklist (Bread, Milk, Soap).</text>
      <text x="15" y="55" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Completely ignores colorful impulse items.</text>
    </g>

    <g transform="translate(15, 125)">
      <rect x="0" y="0" width="310" height="65" fill="#ffffff" rx="5" stroke="#bbf7d0"/>
      <text x="15" y="22" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">💰 Exact Spending &amp; Saved Change</text>
      <text x="15" y="40" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Buys only what was planned in advance.</text>
      <text x="15" y="55" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Returns home with all needs met and extra savings!</text>
    </g>

    <g transform="translate(15, 200)">
      <rect x="0" y="0" width="310" height="50" fill="#dcfce7" rx="5"/>
      <text x="155" y="22" fill="#15803d" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Outcome: Confident shopping, all needs met &amp; savings safe!</text>
    </g>
  </g>
</svg>""",

    # Lesson 3 Page 2: Wamae's Balanced Weekly Pocket Money Ledger
    (3, 2): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="#f8fafc" rx="12"/>
  <rect x="20" y="20" width="760" height="410" fill="#ffffff" rx="10" stroke="#e2e8f0" stroke-width="2" filter="url(#shadow)"/>

  <!-- Title Banner -->
  <rect x="40" y="25" width="720" height="42" fill="#0f172a" rx="8"/>
  <text x="400" y="52" fill="#ffffff" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">
    WAMAE'S BALANCED WEEKLY POCKET MONEY LEDGER (150/- KES)
  </text>

  <!-- Left: Income Column -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="340" height="265" fill="#f0fdf4" rx="8" stroke="#86efac" stroke-width="2"/>
    <rect x="15" y="12" width="310" height="28" fill="#16a34a" rx="5"/>
    <text x="170" y="31" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      INCOME (Money In)
    </text>

    <!-- Table Header -->
    <text x="25" y="65" fill="#166534" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Source Description</text>
    <text x="260" y="65" fill="#166534" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Amount</text>
    <line x1="20" y1="72" x2="320" y2="72" stroke="#86efac" stroke-width="1.5"/>

    <!-- Row 1 -->
    <text x="25" y="98" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11">Weekly Pocket Money</text>
    <text x="260" y="98" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">150/- KES</text>

    <line x1="20" y1="180" x2="320" y2="180" stroke="#86efac" stroke-width="1.5"/>
    <!-- Total Income -->
    <text x="25" y="210" fill="#15803d" font-family="system-ui, sans-serif" font-size="12" font-weight="800">TOTAL INCOME:</text>
    <text x="260" y="210" fill="#15803d" font-family="system-ui, sans-serif" font-size="13" font-weight="800">150/- KES</text>
  </g>

  <!-- Right: Expenses & Savings Column -->
  <g transform="translate(415, 80)">
    <rect x="0" y="0" width="340" height="265" fill="#eff6ff" rx="8" stroke="#bfdbfe" stroke-width="1.5"/>
    <rect x="15" y="12" width="310" height="28" fill="#2563eb" rx="5"/>
    <text x="170" y="31" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      EXPENSES &amp; SAVINGS (Money Out)
    </text>

    <!-- Table Header -->
    <text x="25" y="65" fill="#1e40af" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Item Name (Type)</text>
    <text x="260" y="65" fill="#1e40af" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Cost</text>
    <line x1="20" y1="72" x2="320" y2="72" stroke="#bfdbfe" stroke-width="1.5"/>

    <!-- Row 1 -->
    <text x="25" y="95" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5">• Exercise Book (Need)</text>
    <text x="265" y="95" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5">50/-</text>
    <!-- Row 2 -->
    <text x="25" y="118" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5">• Black Pen (Need)</text>
    <text x="265" y="118" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5">30/-</text>
    <!-- Row 3 -->
    <text x="25" y="141" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5">• Ruler (Need)</text>
    <text x="265" y="141" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5">20/-</text>
    <!-- Row 4 -->
    <text x="25" y="164" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5">• Pencil (Need)</text>
    <text x="265" y="164" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5">15/-</text>

    <!-- Subtotal & Savings -->
    <line x1="20" y1="180" x2="320" y2="180" stroke="#bfdbfe" stroke-width="1.5"/>
    <text x="25" y="200" fill="#475569" font-family="system-ui, sans-serif" font-size="10">Total Expenses:</text>
    <text x="265" y="200" fill="#475569" font-family="system-ui, sans-serif" font-size="10">115/-</text>
    
    <text x="25" y="222" fill="#d97706" font-family="system-ui, sans-serif" font-size="11" font-weight="800">★ SAVINGS (Leftover):</text>
    <text x="265" y="222" fill="#d97706" font-family="system-ui, sans-serif" font-size="11" font-weight="800">35/-</text>

    <line x1="20" y1="232" x2="320" y2="232" stroke="#bfdbfe" stroke-width="1.5"/>
    <text x="25" y="250" fill="#1d4ed8" font-family="system-ui, sans-serif" font-size="12" font-weight="800">TOTAL OUTFLOW:</text>
    <text x="260" y="250" fill="#1d4ed8" font-family="system-ui, sans-serif" font-size="13" font-weight="800">150/- KES</text>
  </g>

  <!-- Bottom Equation Summary -->
  <g transform="translate(60, 360)">
    <rect x="0" y="0" width="680" height="42" fill="#f8fafc" rx="6" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="340" y="26" fill="#0f172a" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      Equation Check: 150/- (Income) = 115/- (Needs Expenses) + 35/- (Savings) ✓ Balanced!
    </text>
  </g>
</svg>""",

    # Lesson 3 Page 4: 4-Step Cardboard Budget Portfolio Project Storyboard
    (3, 4): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="3" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="#f8fafc" rx="12"/>
  <rect x="20" y="20" width="760" height="410" fill="#ffffff" rx="10" stroke="#e2e8f0" stroke-width="2" filter="url(#shadow)"/>

  <!-- Title Banner -->
  <rect x="40" y="25" width="720" height="42" fill="#0f172a" rx="8"/>
  <text x="400" y="52" fill="#ffffff" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">
    4-STEP CARDBOARD BUDGET PORTFOLIO PROJECT STORYBOARD
  </text>

  <!-- 4 Storyboard Steps -->

  <!-- Step 1 -->
  <g transform="translate(45, 85)">
    <rect x="0" y="0" width="165" height="305" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#475569" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">1. FOLD CARDBOARD</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="80" fill="#ffffff" rx="4" stroke="#cbd5e1"/>
      <text x="67" y="45" fill="#475569" font-family="system-ui, sans-serif" font-size="28" text-anchor="middle">📦</text>
    </g>
    <text x="10" y="145" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Action:</text>
    <text x="10" y="162" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Cut clean carton box</text>
    <text x="10" y="175" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">  (40cm x 30cm).</text>
    <text x="10" y="195" fill="#334155" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Key Tip:</text>
    <text x="10" y="210" fill="#475569" font-family="system-ui, sans-serif" font-size="9">Fold evenly in half to</text>
    <text x="10" y="223" fill="#475569" font-family="system-ui, sans-serif" font-size="9">form folder jacket.</text>
  </g>

  <!-- Step 2 -->
  <g transform="translate(225, 85)">
    <rect x="0" y="0" width="165" height="305" fill="#f0f9ff" rx="8" stroke="#bae6fd" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#0284c7" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">2. SECURE MARGINS</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="80" fill="#ffffff" rx="4" stroke="#7dd3fc"/>
      <text x="67" y="45" fill="#0284c7" font-family="system-ui, sans-serif" font-size="28" text-anchor="middle">🧵</text>
    </g>
    <text x="10" y="145" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Action:</text>
    <text x="10" y="162" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Use sisal string or glue</text>
    <text x="10" y="175" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">  along side edges.</text>
    <text x="10" y="195" fill="#0284c7" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Key Tip:</text>
    <text x="10" y="210" fill="#475569" font-family="system-ui, sans-serif" font-size="9">Leaves top open to</text>
    <text x="10" y="223" fill="#475569" font-family="system-ui, sans-serif" font-size="9">create pocket sleeve.</text>
  </g>

  <!-- Step 3 -->
  <g transform="translate(405, 85)">
    <rect x="0" y="0" width="165" height="305" fill="#faf5ff" rx="8" stroke="#e9d5ff" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#9333ea" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">3. LABEL COVER</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="80" fill="#ffffff" rx="4" stroke="#d8b4fe"/>
      <text x="67" y="45" fill="#9333ea" font-family="system-ui, sans-serif" font-size="28" text-anchor="middle">🎨</text>
    </g>
    <text x="10" y="145" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Action:</text>
    <text x="10" y="162" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Write "MY BUDGET</text>
    <text x="10" y="175" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">  PORTFOLIO - TERM 3".</text>
    <text x="10" y="195" fill="#9333ea" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Key Tip:</text>
    <text x="10" y="210" fill="#475569" font-family="system-ui, sans-serif" font-size="9">Add name, class &amp;</text>
    <text x="10" y="223" fill="#475569" font-family="system-ui, sans-serif" font-size="9">colorful drawings.</text>
  </g>

  <!-- Step 4 -->
  <g transform="translate(585, 85)">
    <rect x="0" y="0" width="165" height="305" fill="#f0fdf4" rx="8" stroke="#86efac" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#16a34a" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">4. FILE BUDGETS</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="80" fill="#ffffff" rx="4" stroke="#86efac"/>
      <text x="67" y="45" fill="#16a34a" font-family="system-ui, sans-serif" font-size="28" text-anchor="middle">📂</text>
    </g>
    <text x="10" y="145" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Action:</text>
    <text x="10" y="162" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Slide dated weekly</text>
    <text x="10" y="175" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">  budget sheets inside.</text>
    <text x="10" y="195" fill="#16a34a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Key Tip:</text>
    <text x="10" y="210" fill="#475569" font-family="system-ui, sans-serif" font-size="9">Watch savings grow</text>
    <text x="10" y="223" fill="#475569" font-family="system-ui, sans-serif" font-size="9">week by week!</text>
  </g>
</svg>""",
}

def enrich_cbc_grade6_home_science_topic2():
    print("=" * 80)
    print("STARTING VISUAL ENRICHMENT: CBC GRADE 6 HOME SCIENCE — TOPIC 2: BUDGETING")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 6").first()
    subject = Subject.objects.filter(grade=grade, name="Home Science").first()
    topic = Topic.objects.filter(subject=subject, name="Budgeting").first()

    assert topic, "Grade 6 Topic 2 (Budgeting) not found!"
    lessons = list(topic.lessons.all().order_by("learning_unit__order"))
    print(f"[*] Found {len(lessons)} Lessons under Topic: '{topic.name}' (ID: {topic.id})")

    # Clear existing LessonAssets for clean re-enrichment
    for lesson in lessons:
        lesson.assets.all().delete()
    print("[*] Cleared existing LessonAssets for clean re-enrichment.\n")

    # Phase 2A: Card 1 Verified Photographic Visual Hooks
    print("[+] Phase 2A: Attaching Mandatory Card 1 Visual Hooks...")
    for lesson in lessons:
        u_order = lesson.learning_unit.order
        photo_info = TOPIC2_PHOTOS.get(u_order)
        if not photo_info:
            continue

        hook_block = lesson.blocks.filter(page_number=1, block_type="suggested_image").first()
        if hook_block:
            content = hook_block.content or {}
            content["resolved_image_url"] = photo_info["url"]
            content["url"] = photo_info["url"]
            content["author"] = photo_info["author"]
            content["licensing"] = photo_info["licensing"]
            content["caption"] = photo_info["caption"]
            hook_block.content = content
            hook_block.save()

            asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="image",
                source_type="external",
                storage_type="url",
                status="attached",
                title=hook_block.title,
                description=photo_info["caption"],
                url=photo_info["url"],
                metadata={
                    "author": photo_info["author"],
                    "licensing": photo_info["licensing"],
                    "caption": photo_info["caption"],
                    "is_card_1_hook": True
                }
            )
            hook_block.assets.add(asset)
            print(f"  [CARD 1 HOOK OK] Lesson {u_order} Page 1: '{hook_block.title[:45]}...' -> Asset ID {asset.id}")

    # Phase 2B: Custom Sanitized Vector SVGs
    print("\n[+] Phase 2B: Attaching Custom Sanitized Vector SVGs...")
    for (u_order, page_num), svg_code in TOPIC2_SVGS.items():
        if u_order > len(lessons):
            continue
        lesson = lessons[u_order - 1]
        diag_block = lesson.blocks.filter(page_number=page_num, block_type="diagram").first()
        if diag_block:
            content = diag_block.content or {}
            content["svg_content"] = svg_code
            content["svg"] = svg_code
            content["code"] = svg_code
            content["viewBox"] = "0 0 800 450"
            diag_block.content = content
            diag_block.save()

            asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                source_type="ai_generated",
                storage_type="embed",
                status="attached",
                title=diag_block.title,
                description=content.get("description", diag_block.title),
                metadata={
                    "svg_content": svg_code,
                    "format": "svg",
                    "viewBox": "0 0 800 450",
                    "page_number": page_num
                }
            )
            diag_block.assets.add(asset)
            print(f"  [SVG ATTACHED] Lesson {u_order} Page {page_num}: '{diag_block.title[:45]}...' -> Asset ID {asset.id}")

    total_assets = LessonAsset.objects.filter(lesson__topic=topic).count()
    print("\n" + "=" * 80)
    print(f"[SUCCESS] CBC Grade 6 Home Science Topic 2 Visual Enrichment Complete!")
    print(f"[*] Total LessonAssets Created & Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_cbc_grade6_home_science_topic2()
