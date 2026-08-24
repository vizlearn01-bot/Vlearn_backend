"""
VLearn CBC Grade 8 Agriculture — Topic 7: Kitchen Hygiene Practices
Visual Enrichment & Multi-Video Integration Engine (Phase 2: High-Fidelity Technical SVGs & Videos)

Curriculum: CBC (Grade 8)
Subject: Agriculture
Topic: Kitchen Hygiene Practices (Topic Order: 7)

Enrichment Architecture:
  1. Phase 2A: Card-1 Photographic Visual Hooks (6 Lessons via Verified Wikimedia URLs).
  2. Phase 2B: 6 Custom Responsive Vector SVGs (viewBox="0 0 800 450", high contrast #0f172a dark-mode).
  3. Phase 2C: Multi-Video Instructional Integration (3 Verified YouTube videos across key lessons).
  4. Phase 2D: LessonAsset Model Registration and Database Synchronization.

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade8_agriculture_topic7.py
"""

import os
import sys
import json
import django
from django.db import transaction

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Topic, Lesson, LessonBlock, LessonAsset
)

# =============================================================================
# 6 CUSTOM RESPONSIVE VECTOR SVGS (viewBox="0 0 800 450")
# =============================================================================

SVGS = {
    # -------------------------------------------------------------------------
    # SVG 1 (Lesson 1 Page 2): Four Pillars of Kitchen Hygiene
    # -------------------------------------------------------------------------
    1: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">FOUR PILLARS OF KITCHEN HYGIENE & SANITATION</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Biological Health Shield, Vector Control, Fire Prevention & Tool Longevity</text>

  <!-- Pillar 1: Health Shield -->
  <g transform="translate(35, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="82" cy="30" r="15" fill="#0284c7"/>
    <text x="82" y="35" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1</text>
    <text x="82" y="68" fill="#38bdf8" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">HEALTH SHIELD</text>
    <circle cx="82" cy="115" r="25" fill="#0369a1"/>
    <text x="82" y="120" fill="#bae6fd" font-size="9" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Kills Pathogens</text>
    <text x="82" y="165" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Destroys Salmonella,</text>
    <text x="82" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">E. coli &amp; molds</text>
    <text x="82" y="195" fill="#38bdf8" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">on food counters.</text>
  </g>

  <!-- Pillar 2: Vector Control -->
  <g transform="translate(225, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <circle cx="82" cy="30" r="15" fill="#059669"/>
    <text x="82" y="35" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2</text>
    <text x="82" y="68" fill="#34d399" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">PEST BLOCK</text>
    <ellipse cx="82" cy="115" rx="28" ry="18" fill="#065f46"/>
    <text x="82" y="119" fill="#a7f3d0" font-size="9" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">No Food Scraps</text>
    <text x="82" y="165" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Deters houseflies,</text>
    <text x="82" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">cockroaches &amp; rats</text>
    <text x="82" y="195" fill="#34d399" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">from breeding.</text>
  </g>

  <!-- Pillar 3: Fire & Slip Safety -->
  <g transform="translate(415, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="82" cy="30" r="15" fill="#d97706"/>
    <text x="82" y="35" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">3</text>
    <text x="82" y="68" fill="#fbbf24" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">ACCIDENT BLOCK</text>
    <polygon points="82,90 110,135 54,135" fill="#78350f" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="82" y="122" fill="#fde68a" font-size="9" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Zero Oil Fires</text>
    <text x="82" y="165" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Wiping grease stops</text>
    <text x="82" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">cooker fire flare-ups;</text>
    <text x="82" y="195" fill="#fbbf24" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">dry tiles stop slips.</text>
  </g>

  <!-- Pillar 4: Tool Protection -->
  <g transform="translate(605, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <circle cx="82" cy="30" r="15" fill="#7c3aed"/>
    <text x="82" y="35" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">4</text>
    <text x="82" y="68" fill="#c084fc" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">TOOL SHIELD</text>
    <rect x="57" y="100" width="50" height="30" rx="4" fill="#581c87"/>
    <text x="82" y="119" fill="#e9d5ff" font-size="9" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Anti-Rust</text>
    <text x="82" y="165" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Washes acidic lemon</text>
    <text x="82" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">&amp; tomato juices off</text>
    <text x="82" y="195" fill="#c084fc" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">knives and pots.</text>
  </g>

  <!-- Summary Banner -->
  <rect x="35" y="345" width="735" height="80" rx="8" fill="#1e293b" stroke="#475569"/>
  <text x="55" y="370" fill="#38bdf8" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">KEY HYGIENE PRINCIPLE:</text>
  <text x="55" y="392" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Bacteria double every 20 minutes in warm kitchen food scraps • Standing water accelerates bacterial biofilm</text>
  <text x="55" y="410" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Daily sanitation is the primary barrier safeguarding household and school food security</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 2 (Lesson 2 Page 2): Loose Dirt vs Fixed Dirt Mechanics
    # -------------------------------------------------------------------------
    2: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">LOOSE DIRT VS. FIXED DIRT: ATTACHMENT & REMOVAL MECHANICS</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Dry Particulates (Gravity Held) vs Chemical Bonded Soils (Oil, Heat, Scale)</text>

  <!-- Left: Loose Dirt -->
  <g transform="translate(40, 85)">
    <rect width="340" height="240" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="170" y="26" fill="#38bdf8" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1. LOOSE DIRT (DRY PARTICULATES)</text>

    <!-- Table Surface & Loose Dust/Flour -->
    <line x1="40" y1="120" x2="300" y2="120" stroke="#94a3b8" stroke-width="4"/>
    <circle cx="80" cy="110" r="4" fill="#f8fafc"/>
    <circle cx="120" cy="112" r="3" fill="#f8fafc"/>
    <circle cx="160" cy="108" r="5" fill="#f8fafc"/>
    <circle cx="210" cy="111" r="4" fill="#f8fafc"/>
    <circle cx="260" cy="113" r="3" fill="#f8fafc"/>

    <!-- Dry Broom Vector -->
    <path d="M 60 70 L 110 115" stroke="#f59e0b" stroke-width="3"/>
    <text x="170" y="75" fill="#38bdf8" font-size="10" font-weight="bold">Dry Sweeping / Dusting</text>

    <text x="170" y="155" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">• Held only by gravity / static force.</text>
    <text x="170" y="172" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">• Examples: Dry flour, bread crumbs, dust, onion skins.</text>
    <text x="170" y="195" fill="#f87171" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">WARNING: NEVER USE WET CLOTH!</text>
    <text x="170" y="212" fill="#94a3b8" font-size="9" font-family="system-ui, sans-serif" text-anchor="middle">Water turns loose flour into sticky dough (fixed mud)!</text>
  </g>

  <!-- Right: Fixed Dirt -->
  <g transform="translate(420, 85)">
    <rect width="340" height="240" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="170" y="26" fill="#fbbf24" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2. FIXED DIRT (BONDED SOILS)</text>

    <!-- Wall Tile & Grease Splatters -->
    <line x1="40" y1="120" x2="300" y2="120" stroke="#94a3b8" stroke-width="4"/>
    <ellipse cx="100" cy="118" rx="25" ry="6" fill="#ea580c"/>
    <ellipse cx="180" cy="118" rx="30" ry="8" fill="#78350f"/>
    <ellipse cx="250" cy="118" rx="20" ry="5" fill="#991b1b"/>

    <!-- Soap + Sponge Vector -->
    <rect x="135" y="65" width="70" height="25" rx="4" fill="#047857" stroke="#34d399" stroke-width="1.5"/>
    <text x="170" y="81" fill="#ecfdf5" font-size="9" font-weight="bold" text-anchor="middle">Soap + Scrub</text>

    <text x="170" y="155" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">• Bonded tightly by oil, grease, sugar, or cooking heat.</text>
    <text x="170" y="172" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">• Examples: Cooker grease, pot soot, tap scale, egg stains.</text>
    <text x="170" y="195" fill="#34d399" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">REMOVAL TRIFECTA REQUIRED:</text>
    <text x="170" y="212" fill="#a7f3d0" font-size="9" font-family="system-ui, sans-serif" text-anchor="middle">Water (Solvent) + Soap (Chemistry) + Scrubbing (Friction)</text>
  </g>

  <!-- Bottom Comparison Banner -->
  <rect x="40" y="345" width="720" height="80" rx="8" fill="#1e293b" stroke="#10b981"/>
  <text x="60" y="370" fill="#34d399" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">CLEANING EFFICIENCY RULE:</text>
  <text x="60" y="392" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• ALWAYS sweep or brush loose dirt dry before washing surfaces with water and soap</text>
  <text x="60" y="410" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Use warm water to dissolve sugary residues and soften cooking fats before scrubbing</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 3 (Lesson 3 Page 2): Detergent Chemistry & Micelle Formation
    # -------------------------------------------------------------------------
    3: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">DETERGENT CHEMISTRY: MICELLE FORMATION & GREASE LIFTING</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Lipophilic Tails Grip Oil, Hydrophilic Heads Bond to Wash Water</text>

  <!-- Step 1: Grease on Surface -->
  <g transform="translate(30, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#0284c7"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1</text>
    <text x="82" y="65" fill="#38bdf8" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">GREASE LAYER</text>
    <line x1="20" y1="125" x2="145" y2="125" stroke="#94a3b8" stroke-width="4"/>
    <rect x="45" y="105" width="75" height="20" rx="4" fill="#78350f"/>
    <text x="82" y="118" fill="#fef3c7" font-size="8" font-weight="bold" text-anchor="middle">Cooking Oil</text>
    <text x="82" y="165" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Grease clings firmly</text>
    <text x="82" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">to pot. Water alone</text>
    <text x="82" y="195" fill="#38bdf8" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">slides off without cleaning.</text>
  </g>

  <!-- Step 2: Soap Attachment -->
  <g transform="translate(220, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#d97706"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2</text>
    <text x="82" y="65" fill="#fbbf24" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">SOAP ATTACHES</text>
    <line x1="20" y1="125" x2="145" y2="125" stroke="#94a3b8" stroke-width="4"/>
    <rect x="45" y="105" width="75" height="20" rx="4" fill="#78350f"/>
    <!-- Soap molecules penetrating -->
    <line x1="60" y1="90" x2="60" y2="105" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="60" cy="88" r="4" fill="#38bdf8"/>
    <line x1="105" y1="90" x2="105" y2="105" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="105" cy="88" r="4" fill="#38bdf8"/>
    <text x="82" y="165" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Lipophilic tails stick</text>
    <text x="82" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">deep into the grease;</text>
    <text x="82" y="195" fill="#fbbf24" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">heads point to water.</text>
  </g>

  <!-- Step 3: Micelle Encapsulation -->
  <g transform="translate(410, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#059669"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">3</text>
    <text x="82" y="65" fill="#34d399" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">MICELLE LIFTS</text>
    <!-- Micelle Sphere -->
    <circle cx="82" cy="110" r="22" fill="#78350f" stroke="#38bdf8" stroke-width="3"/>
    <text x="82" y="114" fill="#fff" font-size="8" font-weight="bold" text-anchor="middle">Micelle</text>
    <text x="82" y="165" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Soap molecules form</text>
    <text x="82" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">a sphere around oil,</text>
    <text x="82" y="195" fill="#34d399" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">lifting it off the surface.</text>
  </g>

  <!-- Step 4: Water Rinsing -->
  <g transform="translate(600, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#7c3aed"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">4</text>
    <text x="82" y="65" fill="#c084fc" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">RINSE AWAY</text>
    <path d="M 60 90 L 105 90 L 100 135 L 65 135 Z" fill="#0284c7" opacity="0.6"/>
    <text x="82" y="117" fill="#fff" font-size="8" font-weight="bold" text-anchor="middle">Rinse H2O</text>
    <text x="82" y="165" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Running water pulls</text>
    <text x="82" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">hydrophilic heads,</text>
    <text x="82" y="195" fill="#c084fc" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">washing grease away!</text>
  </g>

  <!-- Bottom Matrix -->
  <rect x="30" y="345" width="735" height="80" rx="8" fill="#1e293b" stroke="#475569"/>
  <text x="50" y="370" fill="#38bdf8" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">SURFACE &amp; TOOL MATCHING MANDATE:</text>
  <text x="50" y="392" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Glass &amp; Ceramic Tiles: Soft sponge + liquid soap (NEVER steel wool; scratches glaze permanently)</text>
  <text x="50" y="410" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Metal Sufurias: Steel wool + scouring powder (Vim) to scrape black charcoal soot</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 4 (Lesson 4 Page 2): Daily, Weekly, Special Cleaning Cycles
    # -------------------------------------------------------------------------
    4: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">STRUCTURED KITCHEN SANITATION SCHEDULE MATRIX</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Daily Hygiene Shield, Weekly Prevention &amp; Special Deep-Clean Cycles</text>

  <!-- Daily Card -->
  <g transform="translate(40, 85)">
    <rect width="220" height="240" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <rect width="220" height="35" rx="8" fill="#0369a1"/>
    <text x="110" y="23" fill="#e0f2fe" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1. DAILY CHORES (EVERY DAY)</text>
    <text x="20" y="65" fill="#38bdf8" font-size="11" font-weight="bold">• Wash dishes after every meal</text>
    <text x="20" y="85" fill="#e2e8f0" font-size="10">• Wipe cooker &amp; counter spills</text>
    <text x="20" y="105" fill="#e2e8f0" font-size="10">• Sweep floor &amp; mop juice spills</text>
    <text x="20" y="125" fill="#38bdf8" font-size="10" font-weight="bold">• Empty organic food waste bin</text>
    <text x="20" y="145" fill="#e2e8f0" font-size="10">• Wash bin &amp; air dry in sun</text>
    <text x="110" y="195" fill="#bae6fd" font-size="10" font-weight="bold" text-anchor="middle">PREVENTS IMMEDIATE ROT</text>
    <text x="110" y="215" fill="#94a3b8" font-size="9" text-anchor="middle">&amp; pest attraction (flies/mice)</text>
  </g>

  <!-- Weekly Card -->
  <g transform="translate(290, 85)">
    <rect width="220" height="240" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <rect width="220" height="35" rx="8" fill="#047857"/>
    <text x="110" y="23" fill="#ecfdf5" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2. WEEKLY (ONCE A WEEK)</text>
    <text x="20" y="65" fill="#34d399" font-size="11" font-weight="bold">• Scrub sink basin &amp; taps</text>
    <text x="20" y="85" fill="#e2e8f0" font-size="10">• Wipe inside refrigerator</text>
    <text x="20" y="105" fill="#e2e8f0" font-size="10">• Wash dishcloths in hot water</text>
    <text x="20" y="125" fill="#34d399" font-size="10" font-weight="bold">• Sweep ceiling cobwebs</text>
    <text x="20" y="145" fill="#e2e8f0" font-size="10">• Sanitize cutting boards</text>
    <text x="110" y="195" fill="#a7f3d0" font-size="10" font-weight="bold" text-anchor="middle">PREVENTS GRIME BUILDUP</text>
    <text x="110" y="215" fill="#94a3b8" font-size="9" text-anchor="middle">&amp; hard water mineral stains</text>
  </g>

  <!-- Special Deep-Clean Card -->
  <g transform="translate(540, 85)">
    <rect width="220" height="240" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <rect width="220" height="35" rx="8" fill="#d97706"/>
    <text x="110" y="23" fill="#fef3c7" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">3. SPECIAL (PERIODIC DEEP)</text>
    <text x="20" y="65" fill="#fbbf24" font-size="11" font-weight="bold">• Empty &amp; wash pantry shelves</text>
    <text x="20" y="85" fill="#e2e8f0" font-size="10">• Wash window screens &amp; vents</text>
    <text x="20" y="105" fill="#e2e8f0" font-size="10">• Soak &amp; scrape stove burners</text>
    <text x="20" y="125" fill="#fbbf24" font-size="10" font-weight="bold">• Descale kettles with vinegar</text>
    <text x="20" y="145" fill="#e2e8f0" font-size="10">• Disinfect outdoor trash area</text>
    <text x="110" y="195" fill="#fde68a" font-size="10" font-weight="bold" text-anchor="middle">DEEP SANITATION</text>
    <text x="110" y="215" fill="#94a3b8" font-size="9" text-anchor="middle">Done monthly or before holidays</text>
  </g>

  <!-- Bottom Tip -->
  <rect x="40" y="345" width="720" height="80" rx="8" fill="#1e293b" stroke="#475569"/>
  <text x="60" y="370" fill="#38bdf8" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">REFRIGERATOR HYGIENE INSIGHT:</text>
  <text x="60" y="392" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Cold temperatures DO NOT kill bacteria; they only slow reproduction</text>
  <text x="60" y="410" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Spilled milk and meat drippings breed mold and Listeria bacteria in refrigerators; wipe weekly with baking soda</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 5 (Lesson 5 Page 2): Double-Bucket Mopping & Figure-8 System
    # -------------------------------------------------------------------------
    5: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">DOUBLE-BUCKET MOPPING SYSTEM &amp; FIGURE-8 TECHNIQUE</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Separating Wash &amp; Rinse Waters to Eliminate Bacterial Cross-Contamination</text>

  <!-- Bucket 1: Wash -->
  <g transform="translate(50, 85)">
    <rect width="180" height="240" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="90" y="26" fill="#38bdf8" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">BUCKET 1: SOAPY WASH</text>
    <rect x="50" y="65" width="80" height="80" rx="6" fill="#0284c7"/>
    <text x="90" y="110" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">Warm Soap</text>
    <text x="90" y="170" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Dip mop into warm</text>
    <text x="90" y="185" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">soapy water to</text>
    <text x="90" y="200" fill="#38bdf8" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">load detergent.</text>
  </g>

  <!-- Middle: Figure-8 Stroke -->
  <g transform="translate(260, 85)">
    <rect width="280" height="240" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="140" y="26" fill="#34d399" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">FIGURE-8 MOPPING MOTION</text>

    <!-- Figure-8 Path Graphic -->
    <path d="M 90 90 C 140 50, 190 130, 140 140 C 90 150, 140 50, 190 90" stroke="#34d399" stroke-width="4" fill="none" stroke-dasharray="6,4"/>
    <circle cx="90" cy="90" r="7" fill="#f59e0b"/>
    <circle cx="190" cy="90" r="7" fill="#38bdf8"/>

    <text x="140" y="175" fill="#ecfdf5" font-size="11" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">OVERLAPPING FIGURE-8 STROKES</text>
    <text x="140" y="195" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Keeps all dirt particles moving forward</text>
    <text x="140" y="210" fill="#a7f3d0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">without spreading muddy water sideways!</text>
  </g>

  <!-- Bucket 2: Rinse -->
  <g transform="translate(570, 85)">
    <rect width="180" height="240" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="90" y="26" fill="#fbbf24" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">BUCKET 2: CLEAN RINSE</text>
    <rect x="50" y="65" width="80" height="80" rx="6" fill="#d97706"/>
    <text x="90" y="110" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">Clean Water</text>
    <text x="90" y="170" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Rinse dirty mop</text>
    <text x="90" y="185" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">&amp; wring tightly.</text>
    <text x="90" y="200" fill="#fbbf24" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Keeps Bucket 1 clean!</text>
  </g>

  <!-- Squeegee & Safety Banner -->
  <rect x="40" y="345" width="720" height="80" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
  <text x="60" y="370" fill="#f87171" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">SLIP &amp; FALL HAZARD PREVENTION:</text>
  <text x="60" y="392" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Wet tiles are extremely slippery • Always place a bright yellow "WET FLOOR" warning sign</text>
  <text x="60" y="410" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Use a rubber squeegee blade to push excess water directly into floor drains for rapid air drying</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 6 (Lesson 6 Page 2): Chemical Hazards & Full PPE Equipment
    # -------------------------------------------------------------------------
    6: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">KITCHEN CLEANING CHEMICAL HAZARDS, TOXIC GASES &amp; PPE</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Hazard Warning Symbols, Deadly Chlorine Gas Reaction, and Full Protective Gear</text>

  <!-- Hazard Symbols (Left) -->
  <g transform="translate(40, 85)">
    <rect width="220" height="240" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <rect width="220" height="35" rx="8" fill="#7f1d1d"/>
    <text x="110" y="23" fill="#fee2e2" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1. WARNING SYMBOLS</text>

    <!-- Corrosive -->
    <rect x="25" y="50" width="170" height="36" rx="4" fill="#334155"/>
    <text x="40" y="72" fill="#fca5a5" font-size="10" font-weight="bold">CORROSIVE (Acid):</text>
    <text x="135" y="72" fill="#fff" font-size="9">Burns skin/eyes</text>

    <!-- Toxic -->
    <rect x="25" y="95" width="170" height="36" rx="4" fill="#334155"/>
    <text x="40" y="117" fill="#fca5a5" font-size="10" font-weight="bold">TOXIC (Skull):</text>
    <text x="115" y="117" fill="#fff" font-size="9">Poison if swallowed</text>

    <!-- Flammable -->
    <rect x="25" y="140" width="170" height="36" rx="4" fill="#334155"/>
    <text x="40" y="162" fill="#fca5a5" font-size="10" font-weight="bold">FLAMMABLE (Fire):</text>
    <text x="145" y="162" fill="#fff" font-size="9">Keep off stove</text>

    <text x="110" y="200" fill="#f87171" font-size="10" font-weight="bold" text-anchor="middle">Always read labels!</text>
  </g>

  <!-- Chemical Reaction Danger (Middle) -->
  <g transform="translate(290, 85)">
    <rect width="220" height="240" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <rect width="220" height="35" rx="8" fill="#78350f"/>
    <text x="110" y="23" fill="#fef3c7" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2. DEADLY MIXING HAZARD</text>

    <rect x="25" y="55" width="170" height="30" rx="4" fill="#0369a1"/>
    <text x="110" y="74" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">Chlorine Bleach</text>
    <text x="110" y="100" fill="#ef4444" font-size="16" font-weight="bold" text-anchor="middle">+</text>
    <rect x="25" y="110" width="170" height="30" rx="4" fill="#d97706"/>
    <text x="110" y="129" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">Acid / Vinegar / Ammonia</text>

    <line x1="25" y1="150" x2="195" y2="150" stroke="#ef4444" stroke-width="2"/>
    <text x="110" y="175" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">TOXIC CHLORINE GAS (Cl2)</text>
    <text x="110" y="195" fill="#fca5a5" font-size="9" text-anchor="middle">Causes instant chemical lung burns!</text>
    <text x="110" y="212" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">NEVER MIX CHEMICALS!</text>
  </g>

  <!-- Full PPE (Right) -->
  <g transform="translate(540, 85)">
    <rect width="220" height="240" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <rect width="220" height="35" rx="8" fill="#047857"/>
    <text x="110" y="23" fill="#ecfdf5" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">3. MANDATORY PPE GEAR</text>

    <text x="25" y="65" fill="#34d399" font-size="10" font-weight="bold">• Rubber Gloves:</text>
    <text x="25" y="80" fill="#e2e8f0" font-size="9">Protects hands from harsh acid &amp; soap</text>

    <text x="25" y="105" fill="#34d399" font-size="10" font-weight="bold">• Canvas Apron:</text>
    <text x="25" y="120" fill="#e2e8f0" font-size="9">Shields clothes from chemical bleaches</text>

    <text x="25" y="145" fill="#34d399" font-size="10" font-weight="bold">• Dust Mask:</text>
    <text x="25" y="160" fill="#e2e8f0" font-size="9">Blocks inhaling scouring powder &amp; fumes</text>

    <text x="25" y="185" fill="#34d399" font-size="10" font-weight="bold">• Closed Shoes:</text>
    <text x="25" y="200" fill="#e2e8f0" font-size="9">Protects feet from dropped pots &amp; glass</text>
  </g>

  <!-- Bottom Ventilation Banner -->
  <rect x="40" y="345" width="720" height="80" rx="8" fill="#1e293b" stroke="#38bdf8"/>
  <text x="60" y="370" fill="#38bdf8" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">MANDATORY VENTILATION STANDARD:</text>
  <text x="60" y="392" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• ALWAYS open all windows and doors wide before using chemical cleaning agents</text>
  <text x="60" y="410" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Constant fresh airflow dilutes chemical vapors and prevents respiratory irritation</text>
</svg>"""
}

# =============================================================================
# CURATED VERIFIED YOUTUBE VIDEOS
# =============================================================================

TOPIC7_VIDEOS = {
    # Unit 3 (Page 4): Cleaning Methods, Dishwashing & Emulsification
    3: {
        "page_number": 4,
        "title": "Instructional Video: Cleaning Methods, Dishwashing & Emulsification",
        "url": "https://www.youtube.com/watch?v=TXJPk-QfhDU",
        "resolved_video_id": "TXJPk-QfhDU",
        "caption": "Watch this practical demonstration on mechanical vs chemical cleaning, soap lather grease lifting, and caring for kitchen equipment."
    },
    # Unit 5 (Page 4): Practical Kitchen Cleaning, Stove Care & Mopping
    5: {
        "page_number": 4,
        "title": "Practical Video: Grade 8 Kitchen Cleaning, Stove Care & Mopping",
        "url": "https://www.youtube.com/watch?v=6ZjkLwQt_YE",
        "resolved_video_id": "6ZjkLwQt_YE",
        "caption": "Watch this step-by-step practical demonstration on clearing worktops, degreasing cookers, descaling sinks, and professional double-bucket floor mopping in Kenya."
    },
    # Unit 6 (Page 6): Topic Video Review: Kitchen Hygiene Practices & Safety
    6: {
        "page_number": 6,
        "title": "Topic Video Review: Kitchen Hygiene Practices & Safety",
        "url": "https://www.youtube.com/watch?v=Ei5z_0Lxmic",
        "resolved_video_id": "Ei5z_0Lxmic",
        "caption": "Watch this comprehensive educational review covering kitchen hygiene pillars, loose vs fixed dirt, double-bucket mopping, and chemical safety precautions."
    }
}

# =============================================================================
# ENRICHMENT EXECUTION
# =============================================================================

def enrich_cbc_grade8_agriculture_topic7():
    """Attaches Card-1 photos, 6 custom SVGs, and 3 verified YouTube videos to Topic 7."""
    print("=" * 80)
    print("STARTING VISUAL ENRICHMENT: CBC GRADE 8 AGRICULTURE — TOPIC 7")
    print("=" * 80)

    topic = Topic.objects.filter(subject__grade__name="Grade 8", subject__name="Agriculture", name="Kitchen Hygiene Practices").first()
    if not topic:
        print("[ERROR] Topic 'Kitchen Hygiene Practices' not found under CBC Grade 8 Agriculture!")
        return

    lessons = Lesson.objects.filter(topic=topic).select_related("learning_unit").order_by("learning_unit__order")
    print(f"[*] Found {lessons.count()} Lessons under Topic: '{topic.name}' (ID: {topic.id})")

    # Load verified Card-1 images
    verified_images_path = os.path.join(os.path.dirname(__file__), "grade8_topic7_verified_images.json")
    if not os.path.exists(verified_images_path):
        print(f"[ERROR] '{verified_images_path}' not found!")
        return

    with open(verified_images_path, "r") as f:
        verified_images = json.load(f)

    # Clean existing LessonAssets for this topic
    deleted_count, _ = LessonAsset.objects.filter(lesson__topic=topic).delete()
    print(f"[*] Cleared {deleted_count} existing LessonAssets for clean re-enrichment.\n")

    total_assets_created = 0

    with transaction.atomic():
        # Phase 2A: Card 1 Photographic Visual Hooks
        print("[+] Phase 2A: Attaching Card 1 Photographic Visual Hooks...")
        for lesson in lessons:
            u_order = str(lesson.learning_unit.order)
            img_data = verified_images.get(u_order)
            if not img_data:
                print(f"  [WARN] No verified image data for Unit {u_order}")
                continue

            hook_block = LessonBlock.objects.filter(lesson=lesson, page_number=1, block_type="suggested_image").first()
            if not hook_block:
                print(f"  [WARN] No suggested_image block found on Page 1 of Lesson {u_order}")
                continue

            content = hook_block.content or {}
            content.update({
                "resolved_image_url": img_data["url"],
                "url": img_data["url"],
                "author": img_data["author"],
                "licensing": img_data["licensing"],
                "verified": True
            })
            hook_block.content = content
            hook_block.save(update_fields=["content"])

            asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="image",
                source_type="wikimedia",
                storage_type="url",
                status="attached",
                title=f"Lesson {u_order} Visual Hook: {img_data.get('title', 'Kitchen Hygiene')}",
                url=img_data["url"],
                description=content.get("caption", ""),
                metadata={
                    "page_number": 1,
                    "author": img_data["author"],
                    "licensing": img_data["licensing"]
                }
            )
            hook_block.assets.add(asset)
            total_assets_created += 1
            print(f"  [CARD 1 HOOK OK] Lesson {u_order}: '{lesson.title[:45]}...' -> Asset ID {asset.id}")

        # Phase 2B: Custom Sanitized Vector SVGs
        print("\n[+] Phase 2B: Attaching Custom Sanitized Vector SVGs...")
        for lesson in lessons:
            u_order = lesson.learning_unit.order
            svg_content = SVGS.get(u_order)
            if not svg_content:
                print(f"  [WARN] No SVG defined for Unit {u_order}")
                continue

            diagram_block = LessonBlock.objects.filter(lesson=lesson, block_type="suggested_diagram").first()
            if not diagram_block:
                print(f"  [WARN] No suggested_diagram block found for Lesson {u_order}")
                continue

            content = diagram_block.content or {}
            content.update({
                "svg_content": svg_content.strip(),
                "svg": svg_content.strip(),
                "format": "svg+xml",
                "sanitized": True,
                "rendered": True,
                "verified": True
            })
            diagram_block.content = content
            diagram_block.save(update_fields=["content"])

            asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                source_type="custom",
                storage_type="inline",
                status="attached",
                title=f"Lesson {u_order} Technical SVG: {diagram_block.title}",
                url="",
                description=content.get("caption", ""),
                metadata={
                    "page_number": diagram_block.page_number,
                    "viewBox": "0 0 800 450",
                    "format": "svg+xml"
                }
            )
            diagram_block.assets.add(asset)
            total_assets_created += 1
            print(f"  [SVG ATTACHED] Lesson {u_order} Page {diagram_block.page_number}: '{diagram_block.title[:45]}...' -> Asset ID {asset.id}")

        # Phase 2C: Multi-Video Integrations
        print("\n[+] Phase 2C: Attaching Curated Video Lessons across Topic 7...")
        for u_order, v_data in TOPIC7_VIDEOS.items():
            lesson = next((l for l in lessons if l.learning_unit.order == u_order), None)
            if not lesson:
                continue

            v_block = LessonBlock.objects.filter(lesson=lesson, block_type="suggested_video").first()
            if not v_block:
                print(f"  [WARN] No suggested_video block found in Lesson {u_order}")
                continue

            content = v_block.content or {}
            content.update({
                "url": v_data["url"],
                "resolved_video_id": v_data["resolved_video_id"],
                "caption": v_data["caption"],
                "verified": True
            })
            v_block.content = content
            v_block.save(update_fields=["content"])

            asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="video",
                source_type="youtube",
                storage_type="url",
                status="attached",
                title=v_data["title"],
                url=v_data["url"],
                description=v_data["caption"],
                metadata={
                    "page_number": v_data["page_number"],
                    "video_id": v_data["resolved_video_id"]
                }
            )
            v_block.assets.add(asset)
            total_assets_created += 1
            print(f"  [VIDEO ATTACHED] Lesson {u_order} Page {v_data['page_number']}: '{v_data['title'][:45]}...' -> Asset ID {asset.id}")

    print("\n" + "=" * 80)
    print(f"[SUCCESS] CBC Grade 8 Agriculture Topic 7 Visual Enrichment Complete!")
    print(f"[*] Total LessonAssets Created & Attached: {total_assets_created}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_cbc_grade8_agriculture_topic7()
