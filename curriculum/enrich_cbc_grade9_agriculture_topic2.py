"""
VLearn CBC Grade 9 Agriculture — Topic 2: Conserving Leftover Food
Production Visual & Media Enrichment Engine (Phase 2)

Attaches:
  - 9 First-Card Photographic Visual Hooks (Verified HTTP 200 URLs from Wikimedia Commons)
  - 9 Custom, Sanitized, Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light responsive)
  - 1 Verified Instructional YouTube Video (ID: 0EErECU8PXU - Springfield-Greene County Health Dept)
  - Creates and links persistent LessonAsset records for all visual assets.

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade9_agriculture_topic2.py
"""

import os
import sys
import json
import django
from django.db import transaction

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, Lesson, LessonBlock, LessonAsset

# =====================================================================
# 9 CUSTOM SANITIZED RESPONSIVE VECTOR SVGS FOR TOPIC 2
# =====================================================================

TOPIC2_SVGS = [
    {
        "lesson_order": 1,
        "page_number": 3,
        "title": "Resource Efficiency Comparison: Fresh Cooking vs. Conserving Leftovers",
        "svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="freshGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#f87171"/>
    </linearGradient>
    <linearGradient id="leftoverGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#34d399"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bgGrad1)" rx="16"/>
  <text x="400" y="42" font-family="system-ui, -apple-system, sans-serif" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Resource Consumption: Cooking Fresh vs. Conserving Leftovers</text>
  <text x="400" y="66" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Household Expenditure Comparison across Core Kitchen Resources</text>

  <rect x="230" y="85" width="16" height="12" rx="3" fill="url(#freshGrad)"/>
  <text x="254" y="96" font-family="system-ui, sans-serif" font-size="12" fill="#e2e8f0">Cooking Fresh (High Waste &amp; Cost)</text>
  <rect x="460" y="85" width="16" height="12" rx="3" fill="url(#leftoverGrad)"/>
  <text x="484" y="96" font-family="system-ui, sans-serif" font-size="12" fill="#e2e8f0">Conserving Leftovers (High Savings!)</text>

  <g transform="translate(60, 120)">
    <text x="0" y="24" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#f1f5f9">1. Money Spent</text>
    <text x="0" y="44" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Buying New Ingredients</text>
    <rect x="180" y="10" width="460" height="20" rx="4" fill="url(#freshGrad)"/>
    <text x="648" y="25" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#fca5a5">100% Cost</text>
    <rect x="180" y="36" width="40" height="20" rx="4" fill="url(#leftoverGrad)"/>
    <text x="228" y="51" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#6ee7b7">0% (Already Paid!)</text>
  </g>

  <g transform="translate(60, 195)">
    <text x="0" y="24" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#f1f5f9">2. Kitchen Time</text>
    <text x="0" y="44" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Peeling, Boiling, Simmering</text>
    <rect x="180" y="10" width="420" height="20" rx="4" fill="url(#freshGrad)"/>
    <text x="608" y="25" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#fca5a5">45 - 60 mins</text>
    <rect x="180" y="36" width="70" height="20" rx="4" fill="url(#leftoverGrad)"/>
    <text x="258" y="51" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#6ee7b7">5 - 10 mins</text>
  </g>

  <g transform="translate(60, 270)">
    <text x="0" y="24" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#f1f5f9">3. Cooking Fuel</text>
    <text x="0" y="44" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Gas, Charcoal, Firewood</text>
    <rect x="180" y="10" width="380" height="20" rx="4" fill="url(#freshGrad)"/>
    <text x="568" y="25" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#fca5a5">Heavy Fuel Burn</text>
    <rect x="180" y="36" width="60" height="20" rx="4" fill="url(#leftoverGrad)"/>
    <text x="248" y="51" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#6ee7b7">Minimal Reheat</text>
  </g>

  <g transform="translate(60, 345)">
    <text x="0" y="24" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#f1f5f9">4. Physical Labor</text>
    <text x="0" y="44" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Pots to Wash &amp; Prep</text>
    <rect x="180" y="10" width="400" height="20" rx="4" fill="url(#freshGrad)"/>
    <text x="588" y="25" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#fca5a5">Heavy Prep / 4 Pots</text>
    <rect x="180" y="36" width="80" height="20" rx="4" fill="url(#leftoverGrad)"/>
    <text x="268" y="51" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#6ee7b7">Quick Stir / 1 Pot</text>
  </g>

  <rect x="60" y="420" width="680" height="20" rx="6" fill="#1e293b"/>
  <text x="400" y="434" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Conserving Leftovers Saves Family Money, Protects Food Security, and Keeps Communities Clean!</text>
</svg>"""
    },
    {
        "lesson_order": 2,
        "page_number": 3,
        "title": "Household Leftover Conservation Methods Matrix",
        "svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bgGrad2)" rx="16"/>
  <text x="400" y="42" font-family="system-ui, -apple-system, sans-serif" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Household Leftover Conservation Architecture</text>
  <text x="400" y="66" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Matching Leftover Types to Scientific Preservation Mechanisms</text>

  <g transform="translate(45, 90)">
    <rect width="335" height="150" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="335" height="34" rx="10" fill="#0284c7"/>
    <text x="16" y="23" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#ffffff">1. REFRIGERATION (0°C to 4°C)</text>
    <text x="16" y="58" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">Mechanism: Slows down bacterial activity</text>
    <text x="16" y="80" font-family="system-ui, sans-serif" font-size="12" fill="#e2e8f0">• Target: Cooked rice, ugali, githeri, stews</text>
    <text x="16" y="102" font-family="system-ui, sans-serif" font-size="12" fill="#e2e8f0">• Duration: 2 to 3 days of safe storage</text>
    <text x="16" y="126" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Key rule: Store in clean, covered airtight containers.</text>
  </g>

  <g transform="translate(420, 90)">
    <rect width="335" height="150" rx="10" fill="#1e293b" stroke="#6366f1" stroke-width="1.5"/>
    <rect x="0" y="0" width="335" height="34" rx="10" fill="#4f46e5"/>
    <text x="16" y="23" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#ffffff">2. FREEZING (Below 0°C)</text>
    <text x="16" y="58" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#818cf8">Mechanism: Halts all bacterial multiplication</text>
    <text x="16" y="80" font-family="system-ui, sans-serif" font-size="12" fill="#e2e8f0">• Target: Cooked beef, chicken, thick stews</text>
    <text x="16" y="102" font-family="system-ui, sans-serif" font-size="12" fill="#e2e8f0">• Duration: Several weeks to months</text>
    <text x="16" y="126" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Key rule: Leave 1cm headspace for liquid expansion.</text>
  </g>

  <g transform="translate(45, 260)">
    <rect width="335" height="150" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="335" height="34" rx="10" fill="#d97706"/>
    <text x="16" y="23" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#ffffff">3. PICKLING (Acid &amp; Salt Brine)</text>
    <text x="16" y="58" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#fbbf24">Mechanism: High acidity destroys microbes</text>
    <text x="16" y="80" font-family="system-ui, sans-serif" font-size="12" fill="#e2e8f0">• Target: Raw onions, carrots, cucumbers, peppers</text>
    <text x="16" y="102" font-family="system-ui, sans-serif" font-size="12" fill="#e2e8f0">• Duration: Months of crunchy condiment life</text>
    <text x="16" y="126" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Key rule: Submerge clean slices in glass jars with vinegar.</text>
  </g>

  <g transform="translate(420, 260)">
    <rect width="335" height="150" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect x="0" y="0" width="335" height="34" rx="10" fill="#059669"/>
    <text x="16" y="23" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#ffffff">4. COMPOSTING (Nutrient Recycling)</text>
    <text x="16" y="58" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#34d399">Mechanism: Aerobic organic decomposition</text>
    <text x="16" y="80" font-family="system-ui, sans-serif" font-size="12" fill="#e2e8f0">• Target: Potato peels, eggshells, spoiled fruit</text>
    <text x="16" y="102" font-family="system-ui, sans-serif" font-size="12" fill="#e2e8f0">• Result: Rich organic manure for garden crops</text>
    <text x="16" y="126" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Caution: Exclude oily cooked stews and meats.</text>
  </g>

  <text x="400" y="432" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#e2e8f0" text-anchor="middle">Every food scrap has a purpose: eat safely, preserve in acid, or enrich the soil!</text>
</svg>"""
    },
    {
        "lesson_order": 3,
        "page_number": 2,
        "title": "5-Stage Journey of a Safe Leftover: From Warm Plate to Cold Storage",
        "svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bgGrad3)" rx="16"/>
  <text x="400" y="42" font-family="system-ui, -apple-system, sans-serif" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 5-Stage Journey of a Safe Leftover</text>
  <text x="400" y="66" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Standard Operating Procedure for Safe Domestic Cold Storage</text>

  <g transform="translate(30, 110)">
    <rect width="130" height="240" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="65" cy="40" r="22" fill="#0284c7"/>
    <text x="65" y="46" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">1</text>
    <text x="65" y="86" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">WASH &amp; PREP</text>
    <text x="12" y="116" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Soap + clean water</text>
    <text x="12" y="136" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Wash hands 20s</text>
    <text x="12" y="156" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Sanitize counter</text>
    <text x="12" y="186" font-family="system-ui, sans-serif" font-size="10" fill="#94a3b8">Prevents cross-contamination</text>
  </g>

  <g transform="translate(185, 110)">
    <rect width="130" height="240" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="65" cy="40" r="22" fill="#d97706"/>
    <text x="65" y="46" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">2</text>
    <text x="65" y="86" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#fbbf24" text-anchor="middle">COOL DOWN</text>
    <text x="12" y="116" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Room temperature</text>
    <text x="12" y="136" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Max 2 hours</text>
    <text x="12" y="156" font-family="system-ui, sans-serif" font-size="11" fill="#fca5a5">• NEVER put steaming hot food in fridge!</text>
    <text x="12" y="200" font-family="system-ui, sans-serif" font-size="10" fill="#94a3b8">Protects fridge temp</text>
  </g>

  <g transform="translate(340, 110)">
    <rect width="130" height="240" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <circle cx="65" cy="40" r="22" fill="#059669"/>
    <text x="65" y="46" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">3</text>
    <text x="65" y="86" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">AIRTIGHT PACK</text>
    <text x="12" y="116" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Clean dry boxes</text>
    <text x="12" y="136" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Tight sealing lid</text>
    <text x="12" y="156" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• 1cm headspace</text>
    <text x="12" y="186" font-family="system-ui, sans-serif" font-size="10" fill="#94a3b8">Locks out bacteria</text>
  </g>

  <g transform="translate(495, 110)">
    <rect width="130" height="240" rx="8" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <circle cx="65" cy="40" r="22" fill="#7c3aed"/>
    <text x="65" y="46" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">4</text>
    <text x="65" y="86" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#a78bfa" text-anchor="middle">DATE &amp; LABEL</text>
    <text x="12" y="116" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Food item name</text>
    <text x="12" y="136" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Date cooked</text>
    <text x="12" y="156" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Eat-by target</text>
    <text x="12" y="186" font-family="system-ui, sans-serif" font-size="10" fill="#94a3b8">Avoids mystery jars</text>
  </g>

  <g transform="translate(645, 110)">
    <rect width="130" height="240" rx="8" fill="#1e293b" stroke="#06b6d4" stroke-width="1.5"/>
    <circle cx="65" cy="40" r="22" fill="#0891b2"/>
    <text x="65" y="46" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">5</text>
    <text x="65" y="86" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#22d3ee" text-anchor="middle">COLD STORAGE</text>
    <text x="12" y="116" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Fridge (0°-4°C)</text>
    <text x="12" y="136" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Freezer (&lt;0°C)</text>
    <text x="12" y="156" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Prompt storage</text>
    <text x="12" y="186" font-family="system-ui, sans-serif" font-size="10" fill="#94a3b8">Safe for consumption!</text>
  </g>

  <rect x="50" y="385" width="700" height="40" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="400" y="410" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Follow these 5 steps every time to eliminate food waste and keep your family completely healthy!</text>
</svg>"""
    },
    {
        "lesson_order": 4,
        "page_number": 2,
        "title": "The Temperature Danger Zone & 5 Golden Reheating Rules",
        "svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="tempScale" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="25%" stop-color="#0284c7"/>
      <stop offset="35%" stop-color="#f59e0b"/>
      <stop offset="70%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#b91c1c"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bgGrad4)" rx="16"/>
  <text x="400" y="40" font-family="system-ui, -apple-system, sans-serif" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Temperature Danger Zone (5°C to 60°C)</text>
  <text x="400" y="64" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Why High Reheating Heat is Essential to Destroy Food Pathogens</text>

  <g transform="translate(60, 90)">
    <rect x="20" y="0" width="36" height="300" rx="18" fill="#334155"/>
    <rect x="24" y="4" width="28" height="292" rx="14" fill="url(#tempScale)"/>
    <line x1="10" y1="20" x2="66" y2="20" stroke="#ffffff" stroke-width="2"/>
    <text x="75" y="24" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#fca5a5">100°C - Boiling Point (Steam Kills All Pathogens)</text>
    <line x1="10" y1="75" x2="66" y2="75" stroke="#ffffff" stroke-width="2"/>
    <text x="75" y="80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#34d399">74°C+ - Piping Hot Reheating Safety Zone</text>
    <line x1="10" y1="120" x2="66" y2="120" stroke="#ef4444" stroke-width="2"/>
    <text x="75" y="125" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#f87171">60°C - Top of Danger Zone</text>
    <rect x="75" y="132" width="280" height="90" rx="6" fill="#7f1d1d" opacity="0.6"/>
    <text x="90" y="155" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#fca5a5">DANGER ZONE (5°C to 60°C)</text>
    <text x="90" y="175" font-family="system-ui, sans-serif" font-size="11" fill="#fecaca">• Bacteria double every 20 minutes</text>
    <text x="90" y="195" font-family="system-ui, sans-serif" font-size="11" fill="#fecaca">• Produces heat-resistant food toxins</text>
    <text x="90" y="213" font-family="system-ui, sans-serif" font-size="11" fill="#fecaca">• Never leave food here &gt;2 hours!</text>
    <line x1="10" y1="230" x2="66" y2="230" stroke="#38bdf8" stroke-width="2"/>
    <text x="75" y="235" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">4°C - Fridge Cold Storage (0°C to 4°C)</text>
    <line x1="10" y1="280" x2="66" y2="280" stroke="#ffffff" stroke-width="2"/>
    <text x="75" y="285" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#e2e8f0">0°C - Freezing Point (Bacterial Growth Stops)</text>
  </g>

  <g transform="translate(450, 90)">
    <rect width="300" height="300" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="300" height="32" rx="10" fill="#0284c7"/>
    <text x="150" y="22" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">5 GOLDEN REHEATING RULES</text>
    
    <text x="16" y="60" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">1. Reheat Uniformly</text>
    <text x="16" y="78" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">Stir constantly to destroy all cold spots.</text>

    <text x="16" y="108" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">2. Always Cover the Pot</text>
    <text x="16" y="126" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">Traps steam, retains moisture &amp; heats fast.</text>

    <text x="16" y="156" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">3. Eat Immediately</text>
    <text x="16" y="174" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">Do not leave warm food sitting at room temp.</text>

    <text x="16" y="204" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">4. Remove Large Bones</text>
    <text x="16" y="222" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">Bones block heat; removing enables full warming.</text>

    <text x="16" y="252" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">5. Inspect Fish &amp; Meats</text>
    <text x="16" y="270" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">If it smells sour, discard; never reheat spoiled fish!</text>
  </g>

  <text x="400" y="425" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">Keep Hot Food Hot (&gt;60°C) and Cold Food Cold (&lt;4°C) — Avoid the Danger Zone!</text>
</svg>"""
    },
    {
        "lesson_order": 5,
        "page_number": 2,
        "title": "Standard Operating Procedure: Safe Kitchen Reheating Flowchart",
        "svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bgGrad5)" rx="16"/>
  <text x="400" y="40" font-family="system-ui, -apple-system, sans-serif" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Standard Operating Procedure: Safe Kitchen Reheating</text>
  <text x="400" y="64" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Step-by-Step Practical Reheating Protocol</text>

  <g transform="translate(60, 90)">
    <rect width="190" height="120" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="95" y="30" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. SANITIZE &amp; WASH</text>
    <text x="16" y="55" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Wash hands with soap</text>
    <text x="16" y="75" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Sanitize countertops</text>
    <text x="16" y="95" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Turn pot handles inward</text>
  </g>

  <g transform="translate(305, 90)">
    <rect width="190" height="120" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="95" y="30" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#fbbf24" text-anchor="middle">2. INSPECT LEFTOVERS</text>
    <text x="16" y="55" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Smell for sourness</text>
    <text x="16" y="75" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Check for mold growth</text>
    <text x="16" y="95" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Scoop ONLY portion needed</text>
  </g>

  <g transform="translate(550, 90)">
    <rect width="190" height="120" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="95" y="30" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#34d399" text-anchor="middle">3. RESTORE MOISTURE</text>
    <text x="16" y="55" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Add 2-3 tbsp clean water</text>
    <text x="16" y="75" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Or fresh daily gravy</text>
    <text x="16" y="95" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Prevents dry burning</text>
  </g>

  <g transform="translate(60, 245)">
    <rect width="190" height="120" rx="8" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
    <text x="95" y="30" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#f472b6" text-anchor="middle">4. STIR CONTINUOUSLY</text>
    <text x="16" y="55" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Heat on stove or jiko</text>
    <text x="16" y="75" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Stir constantly</text>
    <text x="16" y="95" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Eliminates cold pockets</text>
  </g>

  <g transform="translate(305, 245)">
    <rect width="190" height="120" rx="8" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <text x="95" y="30" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#a78bfa" text-anchor="middle">5. STEAM UNDER LID</text>
    <text x="16" y="55" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Cover pot tightly</text>
    <text x="16" y="75" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Simmer 5 to 10 mins</text>
    <text x="16" y="95" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Steam rises actively (&gt;74°C)</text>
  </g>

  <g transform="translate(550, 245)">
    <rect width="190" height="120" rx="8" fill="#1e293b" stroke="#06b6d4" stroke-width="1.5"/>
    <text x="95" y="30" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#22d3ee" text-anchor="middle">6. SERVE IMMEDIATELY</text>
    <text x="16" y="55" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Use dry pot mittens</text>
    <text x="16" y="75" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Serve piping hot on plate</text>
    <text x="16" y="95" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• NEVER reheat twice!</text>
  </g>

  <text x="400" y="415" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Single-Reheat Rule: Scoop only what you will eat; leave the rest cold in the fridge!</text>
</svg>"""
    },
    {
        "lesson_order": 6,
        "page_number": 2,
        "title": "Anatomy of a Professional Recipe & Réchauffé Cookery Framework",
        "svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bgGrad6)" rx="16"/>
  <text x="400" y="40" font-family="system-ui, -apple-system, sans-serif" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Anatomy of a Recipe &amp; The Réchauffé Framework</text>
  <text x="400" y="64" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Transforming Leftovers from Cold Storage into High-Value Culinary Meals</text>

  <g transform="translate(50, 85)">
    <rect width="330" height="315" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="330" height="34" rx="10" fill="#0284c7"/>
    <text x="165" y="23" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">5 CORE COMPONENTS OF A RECIPE</text>
    
    <text x="16" y="60" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">1. Dish Title</text>
    <text x="16" y="78" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">Exact culinary name of the meal (e.g. Ugali Bites)</text>

    <text x="16" y="110" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">2. Ingredients List &amp; Quantities</text>
    <text x="16" y="128" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">Exact measured items (e.g. 2 cups cooked rice, 1 onion)</text>

    <text x="16" y="160" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">3. Equipment &amp; Tools</text>
    <text x="16" y="178" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">Frying pan, knife, wooden spoon, cutting board</text>

    <text x="16" y="210" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">4. Step-by-Step Instructions</text>
    <text x="16" y="228" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">Sequential cooking actions (dice, sauté, stir-fry, plate)</text>

    <text x="16" y="260" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">5. Cooking Time &amp; Yield</text>
    <text x="16" y="278" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">Preparation duration (10 mins) and servings (4 people)</text>
  </g>

  <g transform="translate(420, 85)">
    <rect width="330" height="315" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="330" height="34" rx="10" fill="#059669"/>
    <text x="165" y="23" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">RÉCHAUFFÉ TRIAD OF BENEFITS</text>
    
    <text x="16" y="65" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#34d399">💰 Financial Savings</text>
    <text x="16" y="85" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">Uses ingredients already purchased.</text>
    <text x="16" y="103" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Cuts grocery expenses by over 25% weekly.</text>

    <text x="16" y="145" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#34d399">🥗 Nutritional Upgrade</text>
    <text x="16" y="165" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">Add fresh local greens, carrots, and eggs.</text>
    <text x="16" y="183" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Boosts vitamins, minerals, fiber, and protein.</text>

    <text x="16" y="225" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#34d399">🎨 Culinary Creativity</text>
    <text x="16" y="245" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">Experiment with spices, herbs, and textures.</text>
    <text x="16" y="263" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Transforms boring starch into restaurant-quality food.</text>
  </g>

  <text x="400" y="426" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Réchauffé Cookery: The French Art of Transforming Leftovers into Culinary Masterpieces!</text>
</svg>"""
    },
    {
        "lesson_order": 7,
        "page_number": 2,
        "title": "The 3 Classic Réchauffé Culinary Pathways",
        "svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bgGrad7)" rx="16"/>
  <text x="400" y="40" font-family="system-ui, -apple-system, sans-serif" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 3 Classic Kenyan Réchauffé Pathways</text>
  <text x="400" y="64" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">From Stale Leftovers to Hot, Nutritious, and Appetizing Meals</text>

  <g transform="translate(40, 85)">
    <rect width="225" height="315" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="225" height="32" rx="10" fill="#d97706"/>
    <text x="112" y="22" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">LEFTOVER UGALI</text>
    
    <text x="12" y="55" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#fbbf24">Original State:</text>
    <text x="12" y="73" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Hard, cold, and dry</text>

    <text x="12" y="105" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#fbbf24">Physical Prep:</text>
    <text x="12" y="123" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Dice into 2cm cubes</text>
    <text x="12" y="141" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Toss in curry powder + salt</text>

    <text x="12" y="173" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#fbbf24">Cooking Technique:</text>
    <text x="12" y="191" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Shallow fry in oil (5 mins)</text>

    <rect x="12" y="220" width="201" height="75" rx="6" fill="#78350f"/>
    <text x="112" y="244" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#fde68a" text-anchor="middle">CRISPY UGALI BITES</text>
    <text x="112" y="266" font-family="system-ui, sans-serif" font-size="10" fill="#ffffff" text-anchor="middle">Golden &amp; crunchy outside,</text>
    <text x="112" y="282" font-family="system-ui, sans-serif" font-size="10" fill="#ffffff" text-anchor="middle">steaming soft inside!</text>
  </g>

  <g transform="translate(288, 85)">
    <rect width="225" height="315" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="225" height="32" rx="10" fill="#059669"/>
    <text x="112" y="22" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">LEFTOVER RICE</text>
    
    <text x="12" y="55" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#34d399">Original State:</text>
    <text x="12" y="73" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Cold, clumped, and bland</text>

    <text x="12" y="105" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#34d399">Physical Prep:</text>
    <text x="12" y="123" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Break clumps gently</text>
    <text x="12" y="141" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Dice carrots, peas &amp; garlic</text>

    <text x="12" y="173" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#34d399">Cooking Technique:</text>
    <text x="12" y="191" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Sauté aromatics &amp; stir-fry</text>

    <rect x="12" y="220" width="201" height="75" rx="6" fill="#064e3b"/>
    <text x="112" y="244" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#a7f3d0" text-anchor="middle">VEGETABLE FRIED RICE</text>
    <text x="112" y="266" font-family="system-ui, sans-serif" font-size="10" fill="#ffffff" text-anchor="middle">Vibrant, colorful, fluffy,</text>
    <text x="112" y="282" font-family="system-ui, sans-serif" font-size="10" fill="#ffffff" text-anchor="middle">and packed with vitamins!</text>
  </g>

  <g transform="translate(535, 85)">
    <rect width="225" height="315" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="225" height="32" rx="10" fill="#dc2626"/>
    <text x="112" y="22" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">LEFTOVER GITHERI</text>
    
    <text x="12" y="55" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#f87171">Original State:</text>
    <text x="12" y="73" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Plain, dry maize &amp; beans</text>

    <text x="12" y="105" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#f87171">Physical Prep:</text>
    <text x="12" y="123" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Prepare fresh tomato puree</text>
    <text x="12" y="141" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Prepare savory meat/veg stock</text>

    <text x="12" y="173" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#f87171">Cooking Technique:</text>
    <text x="12" y="191" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Sauté &amp; simmer in gravy</text>

    <rect x="12" y="220" width="201" height="75" rx="6" fill="#7f1d1d"/>
    <text x="112" y="244" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#fecaca" text-anchor="middle">GITHERI IN TOMATO SAUCE</text>
    <text x="112" y="266" font-family="system-ui, sans-serif" font-size="10" fill="#ffffff" text-anchor="middle">Rich savory coating,</text>
    <text x="112" y="282" font-family="system-ui, sans-serif" font-size="10" fill="#ffffff" text-anchor="middle">tender beans and maize!</text>
  </g>

  <text x="400" y="425" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Never eat boring leftovers again — Adapt, Season, and Repurpose!</text>
</svg>"""
    },
    {
        "lesson_order": 8,
        "page_number": 2,
        "title": "5-Stage Mise en Place & Stir-Frying Operation Workflow",
        "svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad8" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bgGrad8)" rx="16"/>
  <text x="400" y="40" font-family="system-ui, -apple-system, sans-serif" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">5-Stage Practical Stir-Frying Workflow</text>
  <text x="400" y="64" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Standard Kitchen Procedure for Vegetable Fried Rice</text>

  <g transform="translate(30, 105)">
    <rect width="130" height="250" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="65" cy="40" r="22" fill="#0284c7"/>
    <text x="65" y="46" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">1</text>
    <text x="65" y="86" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">MISE EN PLACE</text>
    <text x="12" y="116" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Wash hands + board</text>
    <text x="12" y="136" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Dice onions &amp; garlic</text>
    <text x="12" y="156" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Dice carrots into cubes</text>
    <text x="12" y="176" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Break cold rice clumps</text>
    <text x="12" y="210" font-family="system-ui, sans-serif" font-size="10" fill="#94a3b8">Everything ready first!</text>
  </g>

  <g transform="translate(185, 105)">
    <rect width="130" height="250" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="65" cy="40" r="22" fill="#d97706"/>
    <text x="65" y="46" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">2</text>
    <text x="65" y="86" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#fbbf24" text-anchor="middle">SAUTÉ FLAVOR</text>
    <text x="12" y="116" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• 2 tbsp cooking oil</text>
    <text x="12" y="136" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Add onions &amp; garlic</text>
    <text x="12" y="156" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Sauté for 2 mins</text>
    <text x="12" y="176" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Fragrant &amp; soft</text>
    <text x="12" y="210" font-family="system-ui, sans-serif" font-size="10" fill="#94a3b8">Aromatic foundation</text>
  </g>

  <g transform="translate(340, 105)">
    <rect width="130" height="250" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <circle cx="65" cy="40" r="22" fill="#059669"/>
    <text x="65" y="46" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">3</text>
    <text x="65" y="86" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">HARD VEGGIES</text>
    <text x="12" y="116" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Add diced carrots</text>
    <text x="12" y="136" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Add green peas</text>
    <text x="12" y="156" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Stir-fry for 3 mins</text>
    <text x="12" y="176" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Tender yet crunchy</text>
    <text x="12" y="210" font-family="system-ui, sans-serif" font-size="10" fill="#94a3b8">Vibrant color &amp; crunch</text>
  </g>

  <g transform="translate(495, 105)">
    <rect width="130" height="250" rx="8" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <circle cx="65" cy="40" r="22" fill="#7c3aed"/>
    <text x="65" y="46" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" fill="#a78bfa" text-anchor="middle">4</text>
    <text x="65" y="86" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#a78bfa" text-anchor="middle">STIR-FRY RICE</text>
    <text x="12" y="116" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Add leftover rice</text>
    <text x="12" y="136" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Add egg / chicken</text>
    <text x="12" y="156" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Stir-fry 5 mins</text>
    <text x="12" y="176" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Piping hot throughout</text>
    <text x="12" y="210" font-family="system-ui, sans-serif" font-size="10" fill="#94a3b8">No cold lumps!</text>
  </g>

  <g transform="translate(645, 105)">
    <rect width="130" height="250" rx="8" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
    <circle cx="65" cy="40" r="22" fill="#db2777"/>
    <text x="65" y="46" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">5</text>
    <text x="65" y="86" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#f472b6" text-anchor="middle">SEASON &amp; PLATE</text>
    <text x="12" y="116" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Pinch of salt &amp; spice</text>
    <text x="12" y="136" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Garnish coriander</text>
    <text x="12" y="156" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Serve steaming hot</text>
    <text x="12" y="176" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Wash pans immediately</text>
    <text x="12" y="210" font-family="system-ui, sans-serif" font-size="10" fill="#94a3b8">Professional finish!</text>
  </g>

  <text x="400" y="415" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Teamwork, Safety, and Continuous Stirring make Fried Rice Perfect!</text>
</svg>"""
    },
    {
        "lesson_order": 9,
        "page_number": 2,
        "title": "Kitchen Food Safety Barrier & The 2-Hour Rule Breakdown",
        "svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad9" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#bgGrad9)" rx="16"/>
  <text x="400" y="40" font-family="system-ui, -apple-system, sans-serif" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Kitchen Food Safety Barrier &amp; 2-Hour Rule</text>
  <text x="400" y="64" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#94a3b8" text-anchor="middle">Protecting Family Health from Food Poisoning and Cross-Contamination</text>

  <g transform="translate(50, 85)">
    <rect width="330" height="315" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="330" height="34" rx="10" fill="#dc2626"/>
    <text x="165" y="23" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">CROSS-CONTAMINATION BARRIER</text>
    
    <rect x="16" y="50" width="298" height="60" rx="6" fill="#7f1d1d"/>
    <text x="26" y="72" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#fca5a5">RAW FOOD ZONE (DANGER!)</text>
    <text x="26" y="92" font-family="system-ui, sans-serif" font-size="11" fill="#fecaca">Raw meats, poultry, fish, unwashed soil</text>

    <line x1="16" y1="130" x2="314" y2="130" stroke="#f87171" stroke-width="2" stroke-dasharray="6,4"/>
    <text x="165" y="148" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#fca5a5" text-anchor="middle">STRICT PHYSICAL SEPARATION</text>
    <text x="165" y="165" font-family="system-ui, sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">Separate boards, knives, and clean hands</text>

    <rect x="16" y="180" width="298" height="60" rx="6" fill="#064e3b"/>
    <text x="26" y="202" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#a7f3d0">COOKED LEFTOVERS ZONE (SAFE)</text>
    <text x="26" y="222" font-family="system-ui, sans-serif" font-size="11" fill="#d1fae5">Cooked rice, stews, clean covered containers</text>

    <text x="16" y="265" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Never place cooked food on raw meat boards</text>
    <text x="16" y="285" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">• Never taste with a spoon and put it back in pot</text>
  </g>

  <g transform="translate(420, 85)">
    <rect width="330" height="315" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="330" height="34" rx="10" fill="#0284c7"/>
    <text x="165" y="23" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">THE 2-HOUR COLD STORAGE RULE</text>
    
    <circle cx="165" cy="100" r="40" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
    <text x="165" y="98" font-family="system-ui, sans-serif" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">2 HRS</text>
    <text x="165" y="116" font-family="system-ui, sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">MAX LIMIT</text>

    <text x="16" y="165" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">1. Cool to Room Temp</text>
    <text x="16" y="183" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">Allow steam to dissipate on counter (under 1 hr).</text>

    <text x="16" y="210" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">2. Refrigerate Within 2 Hours</text>
    <text x="16" y="228" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">Halts bacterial multiplying before toxins form.</text>

    <text x="16" y="255" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">3. Single Reheat Policy</text>
    <text x="16" y="273" font-family="system-ui, sans-serif" font-size="11" fill="#e2e8f0">Reheat only the portion you will eat immediately.</text>
  </g>

  <text x="400" y="426" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">Cleanliness + Prompt Cooling + Airtight Storage = Zero Foodborne Illness!</text>
</svg>"""
    }
]

def enrich_cbc_grade9_agriculture_topic2():
    """Enriches Topic 2 lessons with verified photographic hooks, vector SVGs, YouTube video, and LessonAssets."""
    print("=" * 80)
    print("STARTING VISUAL ENRICHMENT: CBC GRADE 9 AGRICULTURE — TOPIC 2")
    print("=" * 80)

    topic_name = "Conserving Leftover Food (Meaning, Importance, and Household Methods)"
    topic = Topic.objects.filter(name=topic_name).first()
    if not topic:
        print(f"[ERROR] Topic '{topic_name}' not found! Run ingestion first.")
        return

    lessons = list(Lesson.objects.filter(topic=topic).order_by("learning_unit__order"))
    print(f"[*] Found {len(lessons)} Lessons under Topic: '{topic.name}' (ID: {topic.id})")

    # Load verified Wikimedia images
    images_file = os.path.join(os.path.dirname(__file__), "grade9_topic2_verified_images.json")
    if not os.path.exists(images_file):
        print(f"[ERROR] Verified images file not found: {images_file}")
        return

    with open(images_file, "r") as f:
        verified_images = json.load(f)

    # Clean existing assets for Topic 2
    LessonAsset.objects.filter(lesson__in=lessons).delete()
    print("[*] Cleared existing LessonAssets for clean re-enrichment.\n")

    with transaction.atomic():
        # Phase 2A: Attach Card 1 Photographic Visual Hooks
        print("[+] Phase 2A: Attaching Card 1 Photographic Visual Hooks...")
        for lesson in lessons:
            u_order = str(lesson.learning_unit.order)
            img_data = verified_images.get(u_order)
            if not img_data:
                continue

            hook_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=1,
                block_type="suggested_image"
            ).first()

            if hook_block:
                content = hook_block.content or {}
                content["resolved_image_url"] = img_data["url"]
                content["url"] = img_data["url"]
                content["author"] = img_data.get("author", "Wikimedia Commons Contributor")
                content["licensing"] = img_data.get("licensing", "CC BY-SA 4.0")
                content["source"] = "Wikimedia Commons"
                content["search_query"] = img_data.get("query", "")
                hook_block.content = content
                hook_block.save()

                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    asset_type="image",
                    source_type="external",
                    storage_type="url",
                    status="attached",
                    title=hook_block.title,
                    description=content.get("caption", hook_block.title),
                    url=img_data["url"],
                    metadata={
                        "author": img_data.get("author", "Wikimedia Commons Contributor"),
                        "licensing": img_data.get("licensing", "CC BY-SA 4.0"),
                        "caption": content.get("caption", ""),
                        "is_card_1_hook": True
                    }
                )
                hook_block.assets.add(asset)
                print(f"  [CARD 1 HOOK OK] Lesson {u_order}: '{hook_block.title[:45]}...' -> Asset ID {asset.id}")

        # Phase 2B: Attach Custom Sanitized Vector SVGs
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

        # Phase 2C: Attach Multiple Curated Video Lessons across Topic 2
        print("\n[+] Phase 2C: Attaching Multiple Curated Video Lessons across Topic 2...")
        TOPIC2_VIDEOS = {
            2: {
                "url": "https://www.youtube.com/watch?v=ft7mSqdde3g",
                "resolved_video_id": "ft7mSqdde3g",
                "title": "Field Video: Natural Solar Food Dryers in Kenya",
                "author": "Grekkon Limited",
                "caption": "Watch how modern solar drying technology preserves surplus food, vegetables, and grains efficiently across Kenyan smallholder farms."
            },
            5: {
                "url": "https://www.youtube.com/watch?v=ckN5aMWXVg8",
                "resolved_video_id": "ckN5aMWXVg8",
                "title": "Instructional Video: How to Build a Solar Food Dryer at Home",
                "author": "Sawa World",
                "caption": "Step-by-step practical demonstration on constructing a low-cost, hygienic solar food dehydrator using local timber, mesh, and UV polythene."
            },
            9: {
                "url": "https://www.youtube.com/watch?v=0EErECU8PXU",
                "resolved_video_id": "0EErECU8PXU",
                "title": "Topic Video Review: Food Safety - Cooling, Storing and Using Leftovers",
                "author": "Springfield-Greene County Health Department",
                "caption": "Comprehensive public health tutorial demonstrating safe cooling, airtight container packaging, and uniform reheating."
            }
        }

        for u_order, v_info in TOPIC2_VIDEOS.items():
            lesson = next((l for l in lessons if l.learning_unit.order == u_order), None)
            if not lesson:
                continue

            video_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="suggested_video"
            ).first()

            if not video_block:
                target_page = 6 if u_order == 9 else 4
                video_block = LessonBlock.objects.create(
                    lesson=lesson,
                    block_id=f"g9_agri_t2_u{u_order}_video",
                    block_type="suggested_video",
                    component_type="suggested_video",
                    title=v_info["title"],
                    content={
                        "title": v_info["title"],
                        "url": v_info["url"],
                        "resolved_video_id": v_info["resolved_video_id"],
                        "caption": v_info["caption"],
                        "author": v_info["author"],
                        "verified": True
                    },
                    page_number=target_page,
                    page_title="Video Demonstration Resource",
                    component_order=9,
                    order=99
                )

            content = video_block.content or {}
            content.update(v_info)
            content["verified"] = True
            video_block.content = content
            video_block.save()

            asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="video",
                source_type="external",
                storage_type="url",
                status="attached",
                title=v_info["title"],
                description=v_info["caption"],
                url=v_info["url"],
                metadata={
                    "resolved_video_id": v_info["resolved_video_id"],
                    "author": v_info["author"],
                    "licensing": "YouTube Standard License"
                }
            )
            video_block.assets.add(asset)
            print(f"  [VIDEO ATTACHED] Lesson {u_order} Page {video_block.page_number}: '{v_info['title'][:45]}...' -> Asset ID {asset.id}")

    total_assets = LessonAsset.objects.filter(lesson__in=lessons).count()
    print("\n" + "=" * 80)
    print(f"[SUCCESS] CBC Grade 9 Agriculture Topic 2 Visual Enrichment Complete!")
    print(f"[*] Total LessonAssets Created & Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_cbc_grade9_agriculture_topic2()
