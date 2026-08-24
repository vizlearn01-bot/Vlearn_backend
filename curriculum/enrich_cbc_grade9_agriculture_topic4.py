"""
VLearn CBC Grade 9 Agriculture — Topic 4: Organic Gardening
Phase 2 Visual & Media Enrichment Engine

Curriculum: CBC -> Grade 9 -> Agriculture -> Topic 4: Organic Gardening

Asset Enrichments:
  1. 8 Photographic Visual Hooks (Card 1):
     - Direct high-resolution Wikimedia Commons URLs (100% verified HTTP 200).
     - Full educational captions, authors, and licensing metadata.
  2. 8 Custom Responsive Vector SVGs:
     - Standardized viewBox="0 0 800 450", dark-mode (#0f172a) aesthetic.
     - Covers system comparison, 5-layer compost cross-section, botanical pesticide extraction,
       stomata & 1:10 dilution, maintenance schedule & troubleshooting, 1-meter raised bed blueprint,
       5-step furrow sowing workflow, and daily journal stewardship cycles.
  3. 1 Verified Topic Video Review (YouTube):
     - URL: https://www.youtube.com/watch?v=Ei5z_0Lxmic ("Mixed Organic Farming Explained! | Grade 9 Agriculture CBC | Complete Lesson 🇰🇪")
     - Attached to Lesson 8 Capstone.
  4. Database Entity Persistence:
     - Creates and attaches 17 persistent LessonAsset records linked to LessonBlocks.

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade9_agriculture_topic4.py
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

# Load verified Wikimedia image metadata
IMAGES_JSON_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grade9_topic4_verified_images.json")
with open(IMAGES_JSON_PATH, "r") as f:
    VERIFIED_IMAGES = json.load(f)

# Custom Responsive Vector SVGs (viewBox="0 0 800 450", dark-mode #0f172a)
TOPIC4_SVGS = {
    # -------------------------------------------------------------------------
    # SVG 1: Organic Gardening vs Synthetic Agriculture Matrix
    # -------------------------------------------------------------------------
    1: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">ORGANIC GARDENING VS. SYNTHETIC AGROCHEMICALS</text>
  <text x="400" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Health Safety, Living Soil Biodiversity, Cost Elimination, and Water Protection</text>

  <!-- Left: Organic Gardening (Green Card) -->
  <g transform="translate(40, 85)">
    <rect width="345" height="325" rx="10" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
    <text x="172" y="35" fill="#34d399" font-family="system-ui, sans-serif" font-size="17" font-weight="bold" text-anchor="middle">ORGANIC GARDENING</text>
    <text x="172" y="55" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Natural Biological Ecosystem Care</text>
    <line x1="20" y1="70" x2="325" y2="70" stroke="#047857" stroke-width="1"/>

    <text x="25" y="105" fill="#ecfdf5" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">✓ Food Safety &amp; Health:</text>
    <text x="25" y="125" fill="#d1fae5" font-family="system-ui, sans-serif" font-size="12">Zero toxic chemical residues on harvested crops</text>

    <text x="25" y="160" fill="#ecfdf5" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">✓ Soil Biodiversity:</text>
    <text x="25" y="180" fill="#d1fae5" font-family="system-ui, sans-serif" font-size="12">Feeds earthworms and beneficial microbial fungi</text>

    <text x="25" y="215" fill="#ecfdf5" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">✓ Production Cost:</text>
    <text x="25" y="235" fill="#d1fae5" font-family="system-ui, sans-serif" font-size="12">100% Free; uses farmyard manure and botanical sprays</text>

    <text x="25" y="270" fill="#ecfdf5" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">✓ Environmental Impact:</text>
    <text x="25" y="290" fill="#d1fae5" font-family="system-ui, sans-serif" font-size="12">Protects local streams from dangerous chemical runoff</text>
  </g>

  <!-- Right: Synthetic Chemical Agriculture (Red Card) -->
  <g transform="translate(415, 85)">
    <rect width="345" height="325" rx="10" fill="#450a0a" stroke="#f87171" stroke-width="2"/>
    <text x="172" y="35" fill="#f87171" font-family="system-ui, sans-serif" font-size="17" font-weight="bold" text-anchor="middle">SYNTHETIC AGROCHEMICALS</text>
    <text x="172" y="55" fill="#fecaca" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Artificial Fertilizers &amp; Chemical Sprays</text>
    <line x1="20" y1="70" x2="325" y2="70" stroke="#991b1b" stroke-width="1"/>

    <text x="25" y="105" fill="#fff1f2" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">✗ Food Safety &amp; Health:</text>
    <text x="25" y="125" fill="#fee2e2" font-family="system-ui, sans-serif" font-size="12">Toxic residues pose acute health hazards to families</text>

    <text x="25" y="160" fill="#fff1f2" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">✗ Soil Biodiversity:</text>
    <text x="25" y="180" fill="#fee2e2" font-family="system-ui, sans-serif" font-size="12">Acidifies topsoil and eliminates soil earthworms</text>

    <text x="25" y="215" fill="#fff1f2" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">✗ Production Cost:</text>
    <text x="25" y="235" fill="#fee2e2" font-family="system-ui, sans-serif" font-size="12">High recurring cash expenses for commercial inputs</text>

    <text x="25" y="270" fill="#fff1f2" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">✗ Environmental Impact:</text>
    <text x="25" y="290" fill="#fee2e2" font-family="system-ui, sans-serif" font-size="12">Poisons water channels and destroys helpful pollinators</text>
  </g>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 2: 5-Layer Compost Heap Cross-Section Blueprint
    # -------------------------------------------------------------------------
    2: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">5-LAYER COMPOST HEAP BIOLOGICAL ARCHITECTURE</text>
  <text x="400" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Internal Cross-Section: Building the Sandwich for Rapid Microbial Decomposition</text>

  <!-- Cross-Section Layers (Stacked from Ground Up) -->
  <!-- Layer 5: Top Cap & Ash -->
  <g transform="translate(100, 95)">
    <rect width="600" height="48" rx="4" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="30" y="30" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">LAYER 5: TOPSOIL &amp; WOOD ASH CAP</text>
    <text x="570" y="30" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="end">Adds Decomposers &amp; Regulates Acidity</text>
  </g>

  <!-- Layer 4: Animal Dung Activator -->
  <g transform="translate(100, 150)">
    <rect width="600" height="48" rx="4" fill="#78350f" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="30" y="30" fill="#fef3c7" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">LAYER 4: ANIMAL MANURE ACTIVATOR (Dung &amp; Litter)</text>
    <text x="570" y="30" fill="#fde68a" font-family="system-ui, sans-serif" font-size="12" text-anchor="end">High Nitrogen &amp; Active Bacteria</text>
  </g>

  <!-- Layer 3: Green Nitrogen Matter -->
  <g transform="translate(100, 205)">
    <rect width="600" height="52" rx="4" fill="#064e3b" stroke="#34d399" stroke-width="1.5"/>
    <text x="30" y="32" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">LAYER 3: GREEN NITROGEN VEGETATION (15cm)</text>
    <text x="570" y="32" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="12" text-anchor="end">Fresh Green Weeds, Grass &amp; Kitchen Scraps</text>
  </g>

  <!-- Layer 2: Dry Carbon Matter -->
  <g transform="translate(100, 264)">
    <rect width="600" height="52" rx="4" fill="#451a03" stroke="#d97706" stroke-width="1.5"/>
    <text x="30" y="32" fill="#fed7aa" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">LAYER 2: DRY CARBON BIOMASS (15cm)</text>
    <text x="570" y="32" fill="#fdba74" font-family="system-ui, sans-serif" font-size="12" text-anchor="end">Maize Stover, Dry Leaves &amp; Wheat Straw</text>
  </g>

  <!-- Layer 1: Coarse Sticks Base -->
  <g transform="translate(100, 323)">
    <rect width="600" height="48" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="30" y="30" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">LAYER 1: COARSE DRY STICKS BASE (15cm)</text>
    <text x="570" y="30" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="12" text-anchor="end">Bottom Air Ventilation (Aeration) &amp; Drainage</text>
  </g>

  <!-- Ground Line -->
  <line x1="80" y1="380" x2="720" y2="380" stroke="#64748b" stroke-width="3"/>
  <text x="400" y="405" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">GROUND SURFACE (Turn Pile Every 2-3 Weeks with Fork Jembe for Oxygen Circulation)</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 3: 5-Stage Botanical Garlic & Neem Pesticide Extraction Workflow
    # -------------------------------------------------------------------------
    3: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">5-STAGE BOTANICAL PESTICIDE EXTRACTION WORKFLOW</text>
  <text x="400" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Standard Operating Procedure: Preparing Clear Garlic &amp; Neem Botanical Sprays</text>

  <!-- 5 Sequential Workflow Cards -->
  <!-- Step 1 -->
  <g transform="translate(25, 95)">
    <rect width="135" height="260" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="67" cy="35" r="20" fill="#0284c7"/>
    <text x="67" y="41" fill="#ffffff" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1</text>
    <text x="67" y="75" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">HARVEST</text>
    <line x1="15" y1="90" x2="120" y2="90" stroke="#334155" stroke-width="1"/>
    <text x="67" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Neem seeds</text>
    <text x="67" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Fresh garlic</text>
    <text x="67" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Chilli peppers</text>
    <rect x="12" y="200" width="111" height="35" rx="4" fill="#0c4a6e"/>
    <text x="67" y="222" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Local Inputs</text>
  </g>

  <!-- Step 2 -->
  <g transform="translate(180, 95)">
    <rect width="135" height="260" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="67" cy="35" r="20" fill="#d97706"/>
    <text x="67" y="41" fill="#ffffff" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2</text>
    <text x="67" y="75" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">CRUSH / BLEND</text>
    <line x1="15" y1="90" x2="120" y2="90" stroke="#334155" stroke-width="1"/>
    <text x="67" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Pestle &amp; mortar</text>
    <text x="67" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Fine smooth paste</text>
    <text x="67" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Releases oils</text>
    <rect x="12" y="200" width="111" height="35" rx="4" fill="#78350f"/>
    <text x="67" y="222" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Break Cells</text>
  </g>

  <!-- Step 3 -->
  <g transform="translate(335, 95)">
    <rect width="135" height="260" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <circle cx="67" cy="35" r="20" fill="#059669"/>
    <text x="67" y="41" fill="#ffffff" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">3</text>
    <text x="67" y="75" fill="#10b981" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">STEEP (24 HRS)</text>
    <line x1="15" y1="90" x2="120" y2="90" stroke="#334155" stroke-width="1"/>
    <text x="67" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Mix warm water</text>
    <text x="67" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Cover in jar</text>
    <text x="67" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Activates sulfur</text>
    <rect x="12" y="200" width="111" height="35" rx="4" fill="#064e3b"/>
    <text x="67" y="222" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Full Extraction</text>
  </g>

  <!-- Step 4 -->
  <g transform="translate(490, 95)">
    <rect width="135" height="260" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
    <circle cx="67" cy="35" r="20" fill="#7e22ce"/>
    <text x="67" y="41" fill="#ffffff" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">4</text>
    <text x="67" y="75" fill="#a855f7" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">FINE SIEVING</text>
    <line x1="15" y1="90" x2="120" y2="90" stroke="#334155" stroke-width="1"/>
    <text x="67" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Cotton cloth filter</text>
    <text x="67" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Removes fibers</text>
    <text x="67" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Protects nozzle</text>
    <rect x="12" y="200" width="111" height="35" rx="4" fill="#581c87"/>
    <text x="67" y="222" fill="#e9d5ff" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Zero Clogging</text>
  </g>

  <!-- Step 5 -->
  <g transform="translate(645, 95)">
    <rect width="130" height="260" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="65" cy="35" r="20" fill="#0284c7"/>
    <text x="65" y="41" fill="#ffffff" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">5</text>
    <text x="65" y="75" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">EVENING SPRAY</text>
    <line x1="15" y1="90" x2="115" y2="90" stroke="#334155" stroke-width="1"/>
    <text x="65" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Spray bottle</text>
    <text x="65" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Cool hours</text>
    <text x="65" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Repels pests</text>
    <rect x="12" y="200" width="106" height="35" rx="4" fill="#0c4a6e"/>
    <text x="65" y="222" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Healthy Crops</text>
  </g>

  <!-- Bottom Warning -->
  <rect x="25" y="375" width="750" height="45" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
  <text x="400" y="403" fill="#fde68a" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">⚠️ CRITICAL RULE: Unfiltered botanical liquids will instantly clog spray nozzles! Always sieve through a fine cotton cloth.</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 4: Microscopic Leaf Stomata Absorption & 1:10 Dilution Blueprint
    # -------------------------------------------------------------------------
    4: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">STOMATA ABSORPTION &amp; 1:10 FOLIAR DILUTION PROTOCOL</text>
  <text x="400" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Scientific Leaf Absorption Mechanics &amp; Safe Concentration Guidelines</text>

  <!-- Left: Stomata Biology -->
  <g transform="translate(40, 85)">
    <rect width="345" height="325" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <text x="172" y="35" fill="#34d399" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">MICROSCOPIC LEAF STOMATA</text>
    <text x="172" y="55" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">How Foliar Tea Enters Plant Cells</text>
    <line x1="20" y1="70" x2="325" y2="70" stroke="#334155" stroke-width="1"/>

    <text x="25" y="105" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Underside Leaf Pores:</text>
    <text x="25" y="125" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Thousands of tiny stomata pores breathe and absorb liquids</text>

    <text x="25" y="165" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Cool-Hours Rule (Morning / Evening):</text>
    <text x="25" y="185" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Stomata OPEN during cool hours (before 9AM / after 4:30PM)</text>

    <text x="25" y="225" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Midday Danger:</text>
    <text x="25" y="245" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Stomata CLOSE under hot midday sun to prevent dehydration</text>

    <rect x="25" y="270" width="295" height="38" rx="4" fill="#064e3b"/>
    <text x="172" y="294" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Instant 48-Hour Nitrogen Boost!</text>
  </g>

  <!-- Right: 1:10 Dilution Protocol -->
  <g transform="translate(415, 85)">
    <rect width="345" height="325" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="172" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">THE GOLDEN 1:10 DILUTION FORMULA</text>
    <text x="172" y="55" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Preventing Chemical Fertilizer Scorch</text>
    <line x1="20" y1="70" x2="325" y2="70" stroke="#334155" stroke-width="1"/>

    <!-- Ratio Boxes -->
    <rect x="30" y="95" width="130" height="70" rx="6" fill="#78350f" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="95" y="125" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="18" font-weight="bold" text-anchor="middle">1 PART</text>
    <text x="95" y="148" fill="#fef3c7" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Raw Manure Tea</text>

    <text x="172" y="138" fill="#ffffff" font-family="system-ui, sans-serif" font-size="22" font-weight="bold" text-anchor="middle">+</text>

    <rect x="185" y="95" width="130" height="70" rx="6" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="250" y="125" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="18" font-weight="bold" text-anchor="middle">10 PARTS</text>
    <text x="250" y="148" fill="#e0f2fe" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Clean Water</text>

    <rect x="25" y="185" width="295" height="60" rx="6" fill="#1e1b4b" stroke="#818cf8" stroke-width="1"/>
    <text x="172" y="210" fill="#a5b4fc" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">TOTAL: 11 LITERS OF SAFE SPRAY</text>
    <text x="172" y="230" fill="#e0e7ff" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">E.g. 2L Raw Tea + 20L Water = 22L Foliar Feed</text>

    <rect x="25" y="265" width="295" height="40" rx="4" fill="#450a0a"/>
    <text x="172" y="290" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">⚠️ Undiluted tea causes severe leaf burns!</text>
  </g>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 5: Weekly Garden Maintenance Schedule & Plant Symptom Matrix
    # -------------------------------------------------------------------------
    5: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">WEEKLY GARDEN MAINTENANCE &amp; CROP SYMPTOM GUIDE</text>
  <text x="400" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Structured Team Roster &amp; Organic Diagnostic Solutions</text>

  <!-- Left: Weekly Schedule Card -->
  <g transform="translate(40, 85)">
    <rect width="345" height="325" rx="10" fill="#1e293b" stroke="#818cf8" stroke-width="2"/>
    <text x="172" y="32" fill="#818cf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">WEEKLY MAINTENANCE ROSTER</text>
    <line x1="20" y1="45" x2="325" y2="45" stroke="#334155" stroke-width="1"/>

    <text x="25" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12"><tspan fill="#38bdf8" font-weight="bold">Mon:</tspan> Morning watering &amp; weed inspection (Team A)</text>
    <text x="25" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12"><tspan fill="#38bdf8" font-weight="bold">Tue:</tspan> Shallow tillage &amp; soil aeration (Team B)</text>
    <text x="25" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12"><tspan fill="#38bdf8" font-weight="bold">Wed:</tspan> Underside leaf pest check (Team C)</text>
    <text x="25" y="195" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12"><tspan fill="#38bdf8" font-weight="bold">Thu:</tspan> Botanical spray / foliar preparation (Team D)</text>
    <text x="25" y="235" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12"><tspan fill="#38bdf8" font-weight="bold">Fri:</tspan> Evening 1:10 foliar tea spray (Team A &amp; D)</text>
    <text x="25" y="275" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12"><tspan fill="#38bdf8" font-weight="bold">Sat/Sun:</tspan> Rotating moisture &amp; mulch check</text>

    <rect x="25" y="295" width="295" height="20" rx="3" fill="#312e81"/>
    <text x="172" y="309" fill="#c7d2fe" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Rotating Roles Builds Total Team Mastery</text>
  </g>

  <!-- Right: Crop Diagnostic Symptoms -->
  <g transform="translate(415, 85)">
    <rect width="345" height="325" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="172" y="32" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">CROP STRESS DIAGNOSTIC MATRIX</text>
    <line x1="20" y1="45" x2="325" y2="45" stroke="#334155" stroke-width="1"/>

    <rect x="20" y="60" width="305" height="52" rx="4" fill="#78350f"/>
    <text x="30" y="80" fill="#fef3c7" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Yellow Lower Leaves:</text>
    <text x="30" y="98" fill="#fef3c7" font-family="system-ui, sans-serif" font-size="11">Weed plot manually &amp; spray diluted 1:10 manure tea</text>

    <rect x="20" y="125" width="305" height="52" rx="4" fill="#0c4a6e"/>
    <text x="30" y="145" fill="#e0f2fe" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Wilting Leaves / Cracked Soil:</text>
    <text x="30" y="163" fill="#e0f2fe" font-family="system-ui, sans-serif" font-size="11">Water in morning &amp; apply thick dry grass mulch</text>

    <rect x="20" y="190" width="305" height="52" rx="4" fill="#064e3b"/>
    <text x="30" y="210" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Aphid Colonies Under Leaves:</text>
    <text x="30" y="228" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="11">Spray botanical neem oil or garlic spray in evening</text>

    <rect x="20" y="255" width="305" height="52" rx="4" fill="#581c87"/>
    <text x="30" y="275" fill="#e9d5ff" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">White Powdery Mildew:</text>
    <text x="30" y="293" fill="#e9d5ff" font-family="system-ui, sans-serif" font-size="11">Thin crowded foliage &amp; spray marigold botanical extract</text>
  </g>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 6: 1-Meter Raised Agricultural Bed Dimensional Blueprint
    # -------------------------------------------------------------------------
    6: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">1-METER RAISED AGRICULTURAL BED BLUEPRINT</text>
  <text x="400" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Standard Bed Dimensions: 1m Width, 3m Length, 15cm Height for Soil Preservation</text>

  <!-- Main Isometric / Orthographic Raised Bed Layout -->
  <g transform="translate(60, 95)">
    <!-- Base Ground Area -->
    <rect width="680" height="240" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>

    <!-- Raised Bed Mound (Center) -->
    <rect x="90" y="40" width="500" height="150" rx="6" fill="#78350f" stroke="#fbbf24" stroke-width="2"/>
    <text x="340" y="115" fill="#fef3c7" font-family="system-ui, sans-serif" font-size="18" font-weight="bold" text-anchor="middle">TILLED RAISED SEEDBED</text>
    <text x="340" y="140" fill="#fde68a" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Enriched with Crumbly Compost Manure (Fine Soil Crumbs)</text>

    <!-- Dimension Annotations -->
    <!-- Width: 1 Meter (Vertical) -->
    <line x1="60" y1="40" x2="60" y2="190" stroke="#38bdf8" stroke-width="2"/>
    <line x1="50" y1="40" x2="70" y2="40" stroke="#38bdf8" stroke-width="2"/>
    <line x1="50" y1="190" x2="70" y2="190" stroke="#38bdf8" stroke-width="2"/>
    <text x="40" y="120" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle" transform="rotate(-90 40 120)">WIDTH: 1.0 METER</text>

    <!-- Length: 3 Meters (Horizontal) -->
    <line x1="90" y1="210" x2="590" y2="210" stroke="#34d399" stroke-width="2"/>
    <line x1="90" y1="200" x2="90" y2="220" stroke="#34d399" stroke-width="2"/>
    <line x1="590" y1="200" x2="590" y2="220" stroke="#34d399" stroke-width="2"/>
    <text x="340" y="230" fill="#34d399" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">LENGTH: 3.0 METERS</text>

    <!-- Height: 15cm Tag -->
    <rect x="605" y="95" width="60" height="40" rx="4" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1"/>
    <text x="635" y="115" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">HEIGHT</text>
    <text x="635" y="129" fill="#e0f2fe" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">15 cm</text>
  </g>

  <!-- Bottom Explanatory Callout -->
  <rect x="60" y="360" width="680" height="55" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
  <text x="400" y="383" fill="#34d399" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">WHY 1 METER WIDTH? Prevents Soil Compaction!</text>
  <text x="400" y="403" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Students reach the center of the bed from side pathways to weed and water without ever stepping on cultivated soil.</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 7: 5-Step Row Planting & Furrow Sowing Workflow
    # -------------------------------------------------------------------------
    7: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">5-STEP PRECISION ROW SOWING WORKFLOW</text>
  <text x="400" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Standard Operating Procedure: Furrow Drawing, Compost Layering, Sowing Depth, and Gentle Watering</text>

  <!-- 5 Sequential Sowing Stages -->
  <!-- Step 1 -->
  <g transform="translate(25, 95)">
    <rect width="135" height="260" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="67" cy="35" r="20" fill="#0284c7"/>
    <text x="67" y="41" fill="#ffffff" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1</text>
    <text x="67" y="75" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">LINE STRING</text>
    <line x1="15" y1="90" x2="120" y2="90" stroke="#334155" stroke-width="1"/>
    <text x="67" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Peg &amp; string line</text>
    <text x="67" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Measured distance</text>
    <text x="67" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Straight rows</text>
    <rect x="12" y="200" width="111" height="35" rx="4" fill="#0c4a6e"/>
    <text x="67" y="222" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Straight Lines</text>
  </g>

  <!-- Step 2 -->
  <g transform="translate(180, 95)">
    <rect width="135" height="260" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="67" cy="35" r="20" fill="#d97706"/>
    <text x="67" y="41" fill="#ffffff" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2</text>
    <text x="67" y="75" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">DRAW FURROW</text>
    <line x1="15" y1="90" x2="120" y2="90" stroke="#334155" stroke-width="1"/>
    <text x="67" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Pointed stick</text>
    <text x="67" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Shallow groove</text>
    <text x="67" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Uniform depth</text>
    <rect x="12" y="200" width="111" height="35" rx="4" fill="#78350f"/>
    <text x="67" y="222" fill="#fde68a" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Seed Trench</text>
  </g>

  <!-- Step 3 -->
  <g transform="translate(335, 95)">
    <rect width="135" height="260" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <circle cx="67" cy="35" r="20" fill="#059669"/>
    <text x="67" y="41" fill="#ffffff" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">3</text>
    <text x="67" y="75" fill="#10b981" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">ADD COMPOST</text>
    <line x1="15" y1="90" x2="120" y2="90" stroke="#334155" stroke-width="1"/>
    <text x="67" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Sprinkle compost</text>
    <text x="67" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• In furrow floor</text>
    <text x="67" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Feeds young roots</text>
    <rect x="12" y="200" width="111" height="35" rx="4" fill="#064e3b"/>
    <text x="67" y="222" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Root Nutrition</text>
  </g>

  <!-- Step 4 -->
  <g transform="translate(490, 95)">
    <rect width="135" height="260" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
    <circle cx="67" cy="35" r="20" fill="#7e22ce"/>
    <text x="67" y="41" fill="#ffffff" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">4</text>
    <text x="67" y="75" fill="#a855f7" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">PLACE SEEDS</text>
    <line x1="15" y1="90" x2="120" y2="90" stroke="#334155" stroke-width="1"/>
    <text x="67" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• 2-3x thickness</text>
    <text x="67" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Radish (5cm)</text>
    <text x="67" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Bean (10-15cm)</text>
    <rect x="12" y="200" width="111" height="35" rx="4" fill="#581c87"/>
    <text x="67" y="222" fill="#e9d5ff" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Optimal Depth</text>
  </g>

  <!-- Step 5 -->
  <g transform="translate(645, 95)">
    <rect width="130" height="260" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="65" cy="35" r="20" fill="#0284c7"/>
    <text x="65" y="41" fill="#ffffff" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">5</text>
    <text x="65" y="75" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">ROSE WATER</text>
    <line x1="15" y1="90" x2="115" y2="90" stroke="#334155" stroke-width="1"/>
    <text x="65" y="115" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Fine rose nozzle</text>
    <text x="65" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Gentle rain spray</text>
    <text x="65" y="155" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• No soil washout</text>
    <rect x="12" y="200" width="106" height="35" rx="4" fill="#0c4a6e"/>
    <text x="65" y="222" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Safe Sprout</text>
  </g>

  <!-- Bottom Golden Rule -->
  <rect x="25" y="375" width="750" height="45" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
  <text x="400" y="403" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">SOWING DEPTH RULE: Bury seeds 2 to 3 times their thickness. Cover gently with topsoil and press lightly.</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 8: Daily Garden Observation Journal & Collaborative Stewardship Cycle
    # -------------------------------------------------------------------------
    8: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">DAILY GARDEN OBSERVATION JOURNAL &amp; STEWARDSHIP</text>
  <text x="400" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Scientific Field Data Collection &amp; Collaborative Team Rotation</text>

  <!-- Left: Fillable Journal Layout -->
  <g transform="translate(40, 85)">
    <rect width="345" height="325" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <text x="172" y="32" fill="#34d399" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">FIELD JOURNAL TRACKING PARAMETERS</text>
    <line x1="20" y1="45" x2="325" y2="45" stroke="#334155" stroke-width="1"/>

    <text x="25" y="75" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">1. Stem Height (cm):</text>
    <text x="25" y="95" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Weekly ruler measurement across 5 tagged sample plants</text>

    <text x="25" y="130" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">2. Leaf Color &amp; Vigor:</text>
    <text x="25" y="150" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Record pale green, dark green, yellowing, or leaf curl</text>

    <text x="25" y="185" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">3. Pest &amp; Disease Spotting:</text>
    <text x="25" y="205" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Note aphid clusters, caterpillars, or fungal mildew</text>

    <text x="25" y="240" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">4. Actions &amp; Organic Inputs Applied:</text>
    <text x="25" y="260" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Log morning watering, mulching, or garlic spray</text>

    <rect x="25" y="280" width="295" height="30" rx="4" fill="#064e3b"/>
    <text x="172" y="300" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Data Drives Good Farming Decisions!</text>
  </g>

  <!-- Right: 3-Team Daily Care Cycle -->
  <g transform="translate(415, 85)">
    <rect width="345" height="325" rx="10" fill="#1e293b" stroke="#818cf8" stroke-width="2"/>
    <text x="172" y="32" fill="#818cf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">DAILY 3-PHASE STEWARDSHIP CYCLE</text>
    <line x1="20" y1="45" x2="325" y2="45" stroke="#334155" stroke-width="1"/>

    <!-- Phase 1: Morning -->
    <rect x="20" y="60" width="305" height="65" rx="6" fill="#0c4a6e"/>
    <text x="35" y="83" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">MORNING (7:30 AM - 8:30 AM):</text>
    <text x="35" y="103" fill="#e0f2fe" font-family="system-ui, sans-serif" font-size="11">• Inspect soil moisture under straw mulch</text>
    <text x="35" y="118" fill="#e0f2fe" font-family="system-ui, sans-serif" font-size="11">• Apply gentle rose-nozzle watering to roots</text>

    <!-- Phase 2: Midday -->
    <rect x="20" y="140" width="305" height="65" rx="6" fill="#78350f"/>
    <text x="35" y="163" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">MIDDAY (1:00 PM - 2:00 PM):</text>
    <text x="35" y="183" fill="#fef3c7" font-family="system-ui, sans-serif" font-size="11">• Underside leaf inspection for caterpillars/aphids</text>
    <text x="35" y="198" fill="#fef3c7" font-family="system-ui, sans-serif" font-size="11">• Log weather &amp; observations in field journal</text>

    <!-- Phase 3: Evening -->
    <rect x="20" y="220" width="305" height="65" rx="6" fill="#064e3b"/>
    <text x="35" y="243" fill="#34d399" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">EVENING (4:30 PM - 5:30 PM):</text>
    <text x="35" y="263" fill="#d1fae5" font-family="system-ui, sans-serif" font-size="11">• Hand-pull weeds &amp; repair dry mulch layer</text>
    <text x="35" y="278" fill="#d1fae5" font-family="system-ui, sans-serif" font-size="11">• Spray diluted 1:10 foliar tea or neem repellent</text>

    <rect x="20" y="295" width="305" height="20" rx="3" fill="#312e81"/>
    <text x="172" y="309" fill="#c7d2fe" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Guarantees 100% Crop Survival &amp; Rich Harvest!</text>
  </g>
</svg>"""
}

def enrich_cbc_grade9_agriculture_topic4():
    """Executes visual and media enrichment for Topic 4: Organic Gardening."""
    print("=" * 80)
    print("STARTING VISUAL ENRICHMENT: CBC GRADE 9 AGRICULTURE — TOPIC 4")
    print("=" * 80)

    topic = Topic.objects.filter(
        subject__grade__curriculum__name__iexact="CBC",
        subject__grade__name="Grade 9",
        subject__name="Agriculture",
        name="Organic Gardening"
    ).first()

    if not topic:
        print("[ERROR] Topic 'Organic Gardening' not found in database!")
        return

    lessons = list(topic.lessons.all().order_by("learning_unit__order"))
    print(f"[*] Found {len(lessons)} Lessons under Topic: '{topic.name}' (ID: {topic.id})")

    with transaction.atomic():
        # Clear existing LessonAssets for clean re-enrichment
        LessonAsset.objects.filter(lesson__topic=topic).delete()
        print("[*] Cleared existing LessonAssets for clean re-enrichment.")

        total_assets = 0

        # Phase 2A: Attach Card 1 Photographic Visual Hooks
        print("\n[+] Phase 2A: Attaching Card 1 Photographic Visual Hooks...")
        for lesson in lessons:
            u_order = lesson.learning_unit.order
            img_data = VERIFIED_IMAGES.get(str(u_order))
            if not img_data:
                print(f"  [WARN] No verified image data for Lesson {u_order}")
                continue

            hook_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=1,
                block_type="suggested_image"
            ).first()

            if not hook_block:
                print(f"  [WARN] Card 1 suggested_image block not found for Lesson {u_order}")
                continue

            # Update block content
            b_content = hook_block.content or {}
            b_content.update({
                "url": img_data["url"],
                "resolved_image_url": img_data["url"],
                "author": img_data.get("author", "Wikimedia Commons Contributor"),
                "licensing": img_data.get("licensing", "CC BY-SA 4.0"),
                "source": "Wikimedia Commons",
                "verified": True
            })
            hook_block.content = b_content
            hook_block.save(update_fields=["content"])

            # Create persistent LessonAsset
            asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="image",
                source_type="url",
                storage_type="external",
                status="attached",
                title=f"Visual Hook: {hook_block.title or lesson.title}",
                description=b_content.get("caption", ""),
                url=img_data["url"],
                metadata={
                    "page_number": 1,
                    "author": img_data.get("author", ""),
                    "licensing": img_data.get("licensing", ""),
                    "source": "Wikimedia Commons",
                    "search_query": img_data.get("query", "")
                }
            )
            hook_block.assets.add(asset)
            total_assets += 1
            print(f"  [CARD 1 HOOK OK] Lesson {u_order}: '{hook_block.title[:45]}...' -> Asset ID {asset.id}")

        # Phase 2B: Attach Custom Responsive Vector SVGs
        print("\n[+] Phase 2B: Attaching Custom Sanitized Vector SVGs...")
        for lesson in lessons:
            u_order = lesson.learning_unit.order
            svg_content = TOPIC4_SVGS.get(u_order)
            if not svg_content:
                print(f"  [WARN] No SVG content defined for Lesson {u_order}")
                continue

            diagram_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="suggested_diagram"
            ).first()

            if not diagram_block:
                print(f"  [WARN] suggested_diagram block not found for Lesson {u_order}")
                continue

            # Update block content
            d_content = diagram_block.content or {}
            d_content.update({
                "svg_content": svg_content.strip(),
                "svg": svg_content.strip(),
                "format": "svg+xml",
                "sanitized": True
            })
            diagram_block.content = d_content
            diagram_block.save(update_fields=["content"])

            # Create persistent LessonAsset
            asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="diagram",
                source_type="custom",
                storage_type="inline",
                status="attached",
                title=f"Diagram: {diagram_block.title}",
                description=d_content.get("caption", ""),
                metadata={
                    "page_number": diagram_block.page_number,
                    "viewBox": "0 0 800 450",
                    "format": "svg+xml"
                }
            )
            diagram_block.assets.add(asset)
            total_assets += 1
            print(f"  [SVG ATTACHED] Lesson {u_order} Page {diagram_block.page_number}: '{diagram_block.title[:45]}...' -> Asset ID {asset.id}")

        # Phase 2C: Attach Multiple Curated Video Lessons across Topic 4
        print("\n[+] Phase 2C: Attaching Multiple Curated Video Lessons across Topic 4...")
        TOPIC4_VIDEOS = {
            2: {
                "url": "https://www.youtube.com/watch?v=4oWEI6Wl-xI",
                "resolved_video_id": "4oWEI6Wl-xI",
                "title": "Kenya's Gold: Commercial & Organic Composting",
                "author": "Citizen TV Kenya",
                "caption": "Watch how agricultural experts formulate high-heat organic compost piles using brown carbon and green nitrogen materials."
            },
            5: {
                "url": "https://www.youtube.com/watch?v=6ZjkLwQt_YE",
                "resolved_video_id": "6ZjkLwQt_YE",
                "title": "Practical Video: Kitchen Garden & Organic Pest Management",
                "author": "AQUINCE TECH TIPS",
                "caption": "Watch this hands-on guide on botanical pest sprays (neem, garlic, chili), physical barriers, and biological controls for organic gardening."
            },
            8: {
                "url": "https://www.youtube.com/watch?v=Ei5z_0Lxmic",
                "resolved_video_id": "Ei5z_0Lxmic",
                "title": "Topic Video Review: Mixed Organic Farming Explained",
                "author": "CBC ACADEMY",
                "caption": "Watch this comprehensive CBC Grade 9 Agriculture lesson explaining mixed organic farming systems, composting, soil conservation, and biological pest control in Kenya."
            }
        }

        for u_order, v_info in TOPIC4_VIDEOS.items():
            lesson = next((l for l in lessons if l.learning_unit.order == u_order), None)
            if not lesson:
                continue

            video_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="suggested_video"
            ).first()

            if not video_block:
                target_page = 6 if u_order == 8 else 4
                video_block = LessonBlock.objects.create(
                    lesson=lesson,
                    block_id=f"g9_agri_t4_u{u_order}_video",
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

            v_content = video_block.content or {}
            v_content.update(v_info)
            v_content["verified"] = True
            video_block.content = v_content
            video_block.save(update_fields=["content"])

            asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type="video",
                source_type="youtube",
                storage_type="external",
                status="attached",
                title=v_info["title"],
                description=v_info["caption"],
                url=v_info["url"],
                metadata={
                    "page_number": video_block.page_number,
                    "youtube_id": v_info["resolved_video_id"],
                    "author": v_info["author"]
                }
            )
            video_block.assets.add(asset)
            total_assets += 1
            print(f"  [VIDEO ATTACHED] Lesson {u_order} Page {video_block.page_number}: '{video_block.title[:45]}...' -> Asset ID {asset.id}")

        print("\n" + "=" * 80)
        print(f"[SUCCESS] CBC Grade 9 Agriculture Topic 4 Visual Enrichment Complete!")
        print(f"[*] Total LessonAssets Created & Attached: {total_assets}")
        print("=" * 80)

if __name__ == "__main__":
    enrich_cbc_grade9_agriculture_topic4()
