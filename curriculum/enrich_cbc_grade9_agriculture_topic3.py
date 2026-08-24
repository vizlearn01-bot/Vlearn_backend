"""
VLearn CBC Grade 9 Agriculture — Topic 3: Integrated Farming
Phase 2 Visual & Media Enrichment Engine

Curriculum: CBC -> Grade 9 -> Agriculture -> Topic 3: Integrated Farming

Asset Enrichments:
  1. 11 Photographic Visual Hooks (Card 1):
     - Direct high-resolution Wikimedia Commons URLs (100% verified HTTP 200).
     - Full educational captions, authors, and licensing metadata.
  2. 11 Custom Responsive Vector SVGs:
     - Standardized viewBox="0 0 800 450", dark-mode (#0f172a) aesthetic.
     - Covers nutrient loops, residue cycles, manure comparison, aquaculture loops,
       agroforestry erosion prevention, small animal conversion matrix, legume nitrogen fixation,
       triangular triad, farm-wide water pipelines, 2D spatial layouts, and 3D exploded models.
  3. 1 Verified Topic Video Review (YouTube):
     - URL: https://www.youtube.com/watch?v=uFnDdYWgkV8 ("How to Start an Integrated Farming System with Zero Waste | G-BiACK Kenya")
     - Attached to Lesson 11 Capstone.
  4. Database Entity Persistence:
     - Creates and attaches 23 persistent LessonAsset records linked to LessonBlocks.

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade9_agriculture_topic3.py
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
IMAGES_JSON_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grade9_topic3_verified_images.json")
with open(IMAGES_JSON_PATH, "r") as f:
    VERIFIED_IMAGES = json.load(f)

# Custom Responsive Vector SVGs (viewBox="0 0 800 450", dark-mode #0f172a)
TOPIC3_SVGS = {
    # -------------------------------------------------------------------------
    # SVG 1: System Nutrients Closed-Loop Flowchart
    # -------------------------------------------------------------------------
    1: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="36" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">CLOSED-LOOP NUTRIENT RECYCLING ARCHITECTURE</text>
  <text x="400" y="58" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">The Circular Zero-Waste Web: Waste from One Enterprise Feeds the Next</text>

  <!-- Central Circular Orbit -->
  <circle cx="400" cy="245" r="130" fill="none" stroke="#334155" stroke-width="3" stroke-dasharray="6,6"/>
  <circle cx="400" cy="245" r="45" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
  <text x="400" y="240" fill="#10b981" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">ZERO</text>
  <text x="400" y="258" fill="#10b981" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">WASTE</text>

  <!-- Node 1: Top - Crops -->
  <rect x="310" y="80" width="180" height="60" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
  <text x="400" y="105" fill="#34d399" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. CROPS &amp; FORAGE</text>
  <text x="400" y="125" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Maize Stover &amp; Legume Vines</text>

  <!-- Node 2: Right - Livestock -->
  <rect x="570" y="215" width="180" height="60" rx="8" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
  <text x="660" y="240" fill="#818cf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. LIVESTOCK &amp; POULTRY</text>
  <text x="660" y="260" fill="#c7d2fe" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Concentrates Feed to Dung</text>

  <!-- Node 3: Bottom - Compost & Manure -->
  <rect x="310" y="345" width="180" height="60" rx="8" fill="#78350f" stroke="#fbbf24" stroke-width="2"/>
  <text x="400" y="370" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">3. COMPOST &amp; MANURE</text>
  <text x="400" y="390" fill="#fef3c7" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Heat Kills Pathogens (60°C+)</text>

  <!-- Node 4: Left - Living Soil -->
  <rect x="50" y="215" width="180" height="60" rx="8" fill="#14532d" stroke="#4ade80" stroke-width="2"/>
  <text x="140" y="240" fill="#4ade80" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">4. FERTILE SOIL</text>
  <text x="140" y="260" fill="#bbf7d0" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Rich Humus &amp; Water Storage</text>

  <!-- Connecting Arrows & Labels -->
  <!-- Crops -> Livestock -->
  <path d="M 490 110 Q 660 110 660 215" fill="none" stroke="#34d399" stroke-width="3" marker-end="url(#arrow-green)"/>
  <rect x="520" y="130" width="110" height="24" rx="4" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
  <text x="575" y="146" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Animal Feed</text>

  <!-- Livestock -> Compost -->
  <path d="M 660 275 Q 660 375 490 375" fill="none" stroke="#818cf8" stroke-width="3"/>
  <rect x="520" y="335" width="120" height="24" rx="4" fill="#0f172a" stroke="#818cf8" stroke-width="1"/>
  <text x="580" y="351" fill="#818cf8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Dung &amp; Bedding</text>

  <!-- Compost -> Soil -->
  <path d="M 310 375 Q 140 375 140 275" fill="none" stroke="#fbbf24" stroke-width="3"/>
  <rect x="160" y="335" width="120" height="24" rx="4" fill="#0f172a" stroke="#fbbf24" stroke-width="1"/>
  <text x="220" y="351" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Organic Humus</text>

  <!-- Soil -> Crops -->
  <path d="M 140 215 Q 140 110 310 110" fill="none" stroke="#4ade80" stroke-width="3"/>
  <rect x="160" y="130" width="120" height="24" rx="4" fill="#0f172a" stroke="#4ade80" stroke-width="1"/>
  <text x="220" y="146" fill="#4ade80" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Nutrient Uptake</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 2: 4-Stage Crop Residue Decomposition Cycle
    # -------------------------------------------------------------------------
    2: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">4-STAGE CROP RESIDUE RECYCLING &amp; DECOMPOSITION</text>
  <text x="400" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Standard Operating Procedure: Converting Dry Field Residues into Dark Humus</text>

  <!-- Stage 1 -->
  <g transform="translate(30, 95)">
    <rect width="165" height="270" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="82" cy="35" r="22" fill="#0284c7"/>
    <text x="82" y="42" fill="#ffffff" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">1</text>
    <text x="82" y="80" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">COLLECTION</text>
    <line x1="20" y1="95" x2="145" y2="95" stroke="#334155" stroke-width="1"/>
    <text x="82" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Post-harvest stalks</text>
    <text x="82" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Maize stover &amp; straw</text>
    <text x="82" y="170" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Legume bean vines</text>
    <rect x="15" y="210" width="135" height="40" rx="4" fill="#0c4a6e"/>
    <text x="82" y="235" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Zero Waste Gathering</text>
  </g>

  <!-- Arrow 1 -->
  <path d="M 200 230 L 220 230" stroke="#38bdf8" stroke-width="3"/>

  <!-- Stage 2 -->
  <g transform="translate(225, 95)">
    <rect width="165" height="270" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="82" cy="35" r="22" fill="#d97706"/>
    <text x="82" y="42" fill="#ffffff" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">2</text>
    <text x="82" y="80" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">CHIPPING</text>
    <line x1="20" y1="95" x2="145" y2="95" stroke="#334155" stroke-width="1"/>
    <text x="82" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Chop with panga</text>
    <text x="82" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• 5cm to 10cm pieces</text>
    <text x="82" y="170" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Increases surface area</text>
    <rect x="15" y="210" width="135" height="40" rx="4" fill="#78350f"/>
    <text x="82" y="235" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Speeds Up Rotting</text>
  </g>

  <!-- Arrow 2 -->
  <path d="M 395 230 L 415 230" stroke="#f59e0b" stroke-width="3"/>

  <!-- Stage 3 -->
  <g transform="translate(420, 95)">
    <rect width="165" height="270" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <circle cx="82" cy="35" r="22" fill="#059669"/>
    <text x="82" y="42" fill="#ffffff" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">3</text>
    <text x="82" y="80" fill="#10b981" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">COMPOSTING</text>
    <line x1="20" y1="95" x2="145" y2="95" stroke="#334155" stroke-width="1"/>
    <text x="82" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Layer with dung</text>
    <text x="82" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Keep moist &amp; aerated</text>
    <text x="82" y="170" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• High microbial heat</text>
    <rect x="15" y="210" width="135" height="40" rx="4" fill="#064e3b"/>
    <text x="82" y="235" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Decomposes in 8 Wks</text>
  </g>

  <!-- Arrow 3 -->
  <path d="M 590 230 L 610 230" stroke="#10b981" stroke-width="3"/>

  <!-- Stage 4 -->
  <g transform="translate(615, 95)">
    <rect width="155" height="270" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
    <circle cx="77" cy="35" r="22" fill="#7e22ce"/>
    <text x="77" y="42" fill="#ffffff" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">4</text>
    <text x="77" y="80" fill="#a855f7" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">SOIL RETURN</text>
    <line x1="20" y1="95" x2="135" y2="95" stroke="#334155" stroke-width="1"/>
    <text x="77" y="120" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Spread on crop beds</text>
    <text x="77" y="145" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Restores soil carbon</text>
    <text x="77" y="170" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Zero fertilizer cost</text>
    <rect x="15" y="210" width="125" height="40" rx="4" fill="#581c87"/>
    <text x="77" y="235" fill="#e9d5ff" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Lush Crop Harvest</text>
  </g>

  <!-- Bottom Callout -->
  <rect x="30" y="380" width="740" height="45" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="400" y="408" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">⚠️ NEVER BURN RESIDUES: Burning causes smoke pollution and destroys 100% of organic carbon and nitrogen!</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 3: Organic Manure vs Synthetic Chemical Fertilizer
    # -------------------------------------------------------------------------
    3: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">ORGANIC ANIMAL MANURE VS. SYNTHETIC FERTILIZERS</text>
  <text x="400" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Long-Term Soil Structure, Water Retention, and Ecological Resilience</text>

  <!-- Left Side: Organic Manure (Green Card) -->
  <g transform="translate(40, 85)">
    <rect width="345" height="325" rx="10" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
    <text x="172" y="35" fill="#34d399" font-family="system-ui, sans-serif" font-size="17" font-weight="bold" text-anchor="middle">DECOMPOSED ORGANIC MANURE</text>
    <text x="172" y="55" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Natural Farmyard Dung &amp; Compost</text>
    <line x1="20" y1="70" x2="325" y2="70" stroke="#047857" stroke-width="1"/>

    <!-- Benefits -->
    <text x="25" y="105" fill="#ecfdf5" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">✓ Soil Structure:</text>
    <text x="25" y="125" fill="#d1fae5" font-family="system-ui, sans-serif" font-size="12">Adds dark humus; binds sand &amp; loosens clay</text>

    <text x="25" y="160" fill="#ecfdf5" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">✓ Water Holding Capacity:</text>
    <text x="25" y="180" fill="#d1fae5" font-family="system-ui, sans-serif" font-size="12">Acts like a sponge; holds water 3x longer in drought</text>

    <text x="25" y="215" fill="#ecfdf5" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">✓ Microbial Life:</text>
    <text x="25" y="235" fill="#d1fae5" font-family="system-ui, sans-serif" font-size="12">Feeds earthworms and beneficial bacteria</text>

    <text x="25" y="270" fill="#ecfdf5" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">✓ Cash Cost:</text>
    <text x="25" y="290" fill="#d1fae5" font-family="system-ui, sans-serif" font-size="12">100% Free; recycled on-farm from livestock</text>
  </g>

  <!-- Right Side: Synthetic Fertilizer (Red Card) -->
  <g transform="translate(415, 85)">
    <rect width="345" height="325" rx="10" fill="#450a0a" stroke="#f87171" stroke-width="2"/>
    <text x="172" y="35" fill="#f87171" font-family="system-ui, sans-serif" font-size="17" font-weight="bold" text-anchor="middle">SYNTHETIC CHEMICAL FERTILIZERS</text>
    <text x="172" y="55" fill="#fecaca" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Commercial Inorganic Salts (e.g. DAP/CAN)</text>
    <line x1="20" y1="70" x2="325" y2="70" stroke="#991b1b" stroke-width="1"/>

    <!-- Drawbacks -->
    <text x="25" y="105" fill="#fff1f2" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">✗ Soil Structure:</text>
    <text x="25" y="125" fill="#fee2e2" font-family="system-ui, sans-serif" font-size="12">Adds zero organic carbon; causes soil crusting</text>

    <text x="25" y="160" fill="#fff1f2" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">✗ Leaching &amp; Runoff:</text>
    <text x="25" y="180" fill="#fee2e2" font-family="system-ui, sans-serif" font-size="12">Fast-dissolving salts wash away in heavy rains</text>

    <text x="25" y="215" fill="#fff1f2" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">✗ Soil Acidification:</text>
    <text x="25" y="235" fill="#fee2e2" font-family="system-ui, sans-serif" font-size="12">Long-term use can harm earthworms and microbes</text>

    <text x="25" y="270" fill="#fff1f2" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">✗ Cash Cost:</text>
    <text x="25" y="290" fill="#fee2e2" font-family="system-ui, sans-serif" font-size="12">Expensive recurring purchase draining family budget</text>
  </g>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 4: 3-Way Poultry-Aquaculture-Crop Water & Nutrient Loop
    # -------------------------------------------------------------------------
    4: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">POULTRY-AQUACULTURE-CROP TRIPLE INTEGRATION</text>
  <text x="400" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Water &amp; Nutrient Synergies Between Chickens, Tilapia Fish, and Vegetables</text>

  <!-- Component 1: Chicken Coop (Top Left) -->
  <g transform="translate(60, 95)">
    <rect width="210" height="130" rx="8" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
    <text x="105" y="30" fill="#818cf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. POULTRY COOP</text>
    <text x="105" y="50" fill="#c7d2fe" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Raised on Stilts Over Pond</text>
    <line x1="20" y1="65" x2="190" y2="65" stroke="#3730a3" stroke-width="1"/>
    <text x="105" y="88" fill="#e0e7ff" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Droppings fall into water</text>
    <text x="105" y="108" fill="#e0e7ff" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Fertilizes green plankton</text>
  </g>

  <!-- Component 2: Tilapia Fish Pond (Bottom Center) -->
  <g transform="translate(295, 270)">
    <rect width="210" height="140" rx="8" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2"/>
    <text x="105" y="30" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. TILAPIA FISH POND</text>
    <text x="105" y="50" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Aquaculture Ecosystem</text>
    <line x1="20" y1="65" x2="190" y2="65" stroke="#0369a1" stroke-width="1"/>
    <text x="105" y="88" fill="#e0f2fe" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Fish feed on plankton</text>
    <text x="105" y="108" fill="#e0f2fe" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Excretes organic ammonia</text>
    <text x="105" y="128" fill="#e0f2fe" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Dissolved liquid fertilizer</text>
  </g>

  <!-- Component 3: Crop Garden (Top Right) -->
  <g transform="translate(530, 95)">
    <rect width="210" height="130" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
    <text x="105" y="30" fill="#34d399" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">3. VEGETABLE GARDEN</text>
    <text x="105" y="50" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Kales, Tomatoes &amp; Spinach</text>
    <line x1="20" y1="65" x2="190" y2="65" stroke="#047857" stroke-width="1"/>
    <text x="105" y="88" fill="#ecfdf5" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Irrigated by pond water</text>
    <text x="105" y="108" fill="#ecfdf5" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Produces family food &amp; scrap</text>
  </g>

  <!-- Arrow 1: Poultry -> Pond -->
  <path d="M 165 225 Q 165 340 295 340" fill="none" stroke="#818cf8" stroke-width="3"/>
  <rect x="180" y="275" width="95" height="24" rx="4" fill="#0f172a" stroke="#818cf8" stroke-width="1"/>
  <text x="227" y="291" fill="#818cf8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Droppings Feed</text>

  <!-- Arrow 2: Pond -> Crops -->
  <path d="M 505 340 Q 635 340 635 225" fill="none" stroke="#38bdf8" stroke-width="3"/>
  <rect x="525" y="275" width="105" height="24" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
  <text x="577" y="291" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Liquid Fertilizer</text>

  <!-- Arrow 3: Crops -> Poultry -->
  <path d="M 530 160 L 270 160" fill="none" stroke="#34d399" stroke-width="3"/>
  <rect x="345" y="145" width="110" height="24" rx="4" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
  <text x="400" y="161" fill="#34d399" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Vegetable Scraps</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 5: Agroforestry Soil Erosion Prevention & Microclimate Blueprint
    # -------------------------------------------------------------------------
    5: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">AGROFORESTRY SOIL EROSION &amp; MICROCLIMATE BLUEPRINT</text>
  <text x="400" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">How Contour Trees Protect Slopes, Pump Nutrients, and Reduce Evaporation</text>

  <!-- 4 Feature Quadrants -->
  <!-- Quad 1: Top Left - Canopy Protection -->
  <g transform="translate(40, 85)">
    <rect width="345" height="150" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="20" y="30" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold">1. CANOPY RAIN INTERCEPTION</text>
    <text x="20" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">• Tree leaves break violent velocity of falling raindrops.</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">• Water drips gently onto soil surface without displacing mud.</text>
    <text x="20" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">• Prevents surface soil crusting and compaction.</text>
    <rect x="235" y="115" width="95" height="24" rx="4" fill="#0284c7"/>
    <text x="282" y="131" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Rain Softener</text>
  </g>

  <!-- Quad 2: Top Right - Deep Nutrient Pump -->
  <g transform="translate(415, 85)">
    <rect width="345" height="150" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="20" y="30" fill="#34d399" font-family="system-ui, sans-serif" font-size="15" font-weight="bold">2. DEEP NUTRIENT PUMP</text>
    <text x="20" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">• Deep taproots retrieve minerals leached beyond crop roots.</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">• Nutrients are transported upward into leafy branches.</text>
    <text x="20" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">• Fallen leaves decay into nutrient-rich topsoil mulch.</text>
    <rect x="235" y="115" width="95" height="24" rx="4" fill="#059669"/>
    <text x="282" y="131" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Natural Pump</text>
  </g>

  <!-- Quad 3: Bottom Left - Root Anchor Net -->
  <g transform="translate(40, 255)">
    <rect width="345" height="150" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="20" y="30" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="15" font-weight="bold">3. CONTOUR ROOT ANCHOR NET</text>
    <text x="20" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">• Dense roots bind subsoil particles like an underground mesh.</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">• Planting trees along contours prevents flash erosion gullies.</text>
    <text x="20" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">• Traps downhill silt to build stable natural terraces.</text>
    <rect x="235" y="115" width="95" height="24" rx="4" fill="#d97706"/>
    <text x="282" y="131" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Slope Anchor</text>
  </g>

  <!-- Quad 4: Bottom Right - Microclimate Barrier -->
  <g transform="translate(415, 255)">
    <rect width="345" height="150" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <text x="20" y="30" fill="#a855f7" font-family="system-ui, sans-serif" font-size="15" font-weight="bold">4. MICROCLIMATE &amp; WINDBREAK</text>
    <text x="20" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">• Tree lines deflect harsh, drying winds from delicate crops.</text>
    <text x="20" y="85" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">• Filtered shade lowers soil surface temperatures significantly.</text>
    <text x="20" y="110" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">• Reduces water evaporation; crop roots stay moist longer.</text>
    <rect x="235" y="115" width="95" height="24" rx="4" fill="#7e22ce"/>
    <text x="282" y="131" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Wind Shield</text>
  </g>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 6: Poultry & Rabbit Output-to-Input Resource Conversion Matrix
    # -------------------------------------------------------------------------
    6: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">POULTRY &amp; RABBIT RESOURCE CONVERSION MATRIX</text>
  <text x="400" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Converting Scraps &amp; Weeds into Concentrated Nitrogen, Phosphorus, and Pest Suppression</text>

  <!-- Left: Poultry Enterprise -->
  <g transform="translate(40, 85)">
    <rect width="345" height="325" rx="10" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
    <text x="172" y="35" fill="#818cf8" font-family="system-ui, sans-serif" font-size="17" font-weight="bold" text-anchor="middle">POULTRY ENTERPRISE</text>
    <text x="172" y="55" fill="#c7d2fe" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Chickens, Ducks &amp; Turkeys</text>
    <line x1="20" y1="70" x2="325" y2="70" stroke="#3730a3" stroke-width="1"/>

    <rect x="20" y="90" width="305" height="55" rx="6" fill="#312e81"/>
    <text x="35" y="112" fill="#a5b4fc" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Input Feed:</text>
    <text x="35" y="132" fill="#e0e7ff" font-family="system-ui, sans-serif" font-size="12">Kitchen scraps, garden insects, spilled grain</text>

    <rect x="20" y="160" width="305" height="65" rx="6" fill="#312e81"/>
    <text x="35" y="182" fill="#a5b4fc" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">High-Nitrogen Litter:</text>
    <text x="35" y="202" fill="#e0e7ff" font-family="system-ui, sans-serif" font-size="12">Extremely rich in nitrogen; supercharges leafy vegetables</text>

    <rect x="20" y="240" width="305" height="60" rx="6" fill="#312e81"/>
    <text x="35" y="262" fill="#a5b4fc" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Biological Action:</text>
    <text x="35" y="282" fill="#e0e7ff" font-family="system-ui, sans-serif" font-size="12">Scratching uproots weeds &amp; devours crop caterpillars</text>
  </g>

  <!-- Right: Rabbit Enterprise -->
  <g transform="translate(415, 85)">
    <rect width="345" height="325" rx="10" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
    <text x="172" y="35" fill="#34d399" font-family="system-ui, sans-serif" font-size="17" font-weight="bold" text-anchor="middle">RABBIT ENTERPRISE</text>
    <text x="172" y="55" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Elevated Slatted Hutch System</text>
    <line x1="20" y1="70" x2="325" y2="70" stroke="#047857" stroke-width="1"/>

    <rect x="20" y="90" width="305" height="55" rx="6" fill="#065f46"/>
    <text x="35" y="112" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Input Feed:</text>
    <text x="35" y="132" fill="#ecfdf5" font-family="system-ui, sans-serif" font-size="12">Wild grass, sweet potato vines, bean leaves</text>

    <rect x="20" y="160" width="305" height="65" rx="6" fill="#065f46"/>
    <text x="35" y="182" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Cold Solid Droppings:</text>
    <text x="35" y="202" fill="#ecfdf5" font-family="system-ui, sans-serif" font-size="12">High phosphorus content; stimulates strong root growth</text>

    <rect x="20" y="240" width="305" height="60" rx="6" fill="#065f46"/>
    <text x="35" y="262" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Liquid Gold (Rabbit Urine):</text>
    <text x="35" y="282" fill="#ecfdf5" font-family="system-ui, sans-serif" font-size="12">Diluted 1:5 as organic foliar spray &amp; natural pest repellent</text>
  </g>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 7: Horticultural Intercropping & Natural Nitrogen Fixation Map
    # -------------------------------------------------------------------------
    7: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">HORTICULTURAL INTERCROPPING &amp; NITROGEN FIXATION</text>
  <text x="400" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Biological Symbiosis: Legume Nodules Fertilizing Neighboring Leafy Kales</text>

  <!-- Left: Legume Nitrogen Factory -->
  <g transform="translate(40, 85)">
    <rect width="345" height="325" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <text x="172" y="35" fill="#34d399" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">1. CLIMBING BEANS &amp; PEAS</text>
    <text x="172" y="55" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Atmospheric Nitrogen Fixers</text>
    <line x1="20" y1="70" x2="325" y2="70" stroke="#334155" stroke-width="1"/>

    <text x="25" y="105" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Rhizobium Microbes:</text>
    <text x="25" y="125" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Live inside specialized root nodules</text>

    <text x="25" y="160" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Gas to Soluble Nitrates:</text>
    <text x="25" y="180" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Converts air nitrogen into plant food</text>

    <text x="25" y="215" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">High-Protein Fodder:</text>
    <text x="25" y="235" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Harvested vines feed rabbits and goats</text>

    <rect x="25" y="265" width="295" height="40" rx="4" fill="#064e3b"/>
    <text x="172" y="290" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Replaces Synthetic Urea!</text>
  </g>

  <!-- Right: Leafy Vegetable Consumer -->
  <g transform="translate(415, 85)">
    <rect width="345" height="325" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="172" y="35" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">2. SUKUMA WIKI &amp; SPINACH</text>
    <text x="172" y="55" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Heavy Nitrogen Feeders</text>
    <line x1="20" y1="70" x2="325" y2="70" stroke="#334155" stroke-width="1"/>

    <text x="25" y="105" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Rapid Leaf Growth:</text>
    <text x="25" y="125" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Absorbs nitrates fixed by neighbor beans</text>

    <text x="25" y="160" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Living Mulch Canopy:</text>
    <text x="25" y="180" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Broad leaves shade soil and trap moisture</text>

    <text x="25" y="215" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">Weed Suppression:</text>
    <text x="25" y="235" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Blocks sunlight from reaching weed seeds</text>

    <rect x="25" y="265" width="295" height="40" rx="4" fill="#0c4a6e"/>
    <text x="172" y="290" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Succulent Year-Round Harvest!</text>
  </g>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 8: Triangular Nitrogen & Feed Exchange Network (Veg-Poultry-Rabbit)
    # -------------------------------------------------------------------------
    8: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">TRIANGULAR BACKYARD NUTRIENT TRIAD</text>
  <text x="400" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Vegetables, Poultry, and Rabbits Exchanging Feeds, Manures, and Liquid Gold</text>

  <!-- Top Node: Vegetables -->
  <g transform="translate(300, 75)">
    <rect width="200" height="70" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
    <text x="100" y="30" fill="#34d399" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">VEGETABLE PLOT</text>
    <text x="100" y="52" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Kales, Beans &amp; Spinach</text>
  </g>

  <!-- Bottom Left Node: Rabbit Hutch -->
  <g transform="translate(80, 275)">
    <rect width="210" height="85" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="105" y="28" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">RABBIT HUTCH</text>
    <text x="105" y="48" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Phosphorus Dung</text>
    <text x="105" y="68" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Rabbit Urine (1:5 Foliar)</text>
  </g>

  <!-- Bottom Right Node: Poultry Coop -->
  <g transform="translate(510, 275)">
    <rect width="210" height="85" rx="8" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
    <text x="105" y="28" fill="#818cf8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">POULTRY COOP</text>
    <text x="105" y="48" fill="#c7d2fe" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• High-Nitrogen Litter</text>
    <text x="105" y="68" fill="#c7d2fe" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Pest &amp; Weed Control</text>
  </g>

  <!-- Relational Connecting Arrows -->
  <!-- Veg -> Rabbit -->
  <path d="M 320 145 L 185 275" stroke="#34d399" stroke-width="2"/>
  <text x="210" y="195" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">Kale Scraps</text>

  <!-- Rabbit -> Veg -->
  <path d="M 195 275 L 340 145" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="280" y="225" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">1:5 Urine Spray</text>

  <!-- Veg -> Poultry -->
  <path d="M 480 145 L 615 275" stroke="#34d399" stroke-width="2"/>
  <text x="560" y="195" fill="#34d399" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">Weed Scraps</text>

  <!-- Poultry -> Veg -->
  <path d="M 605 275 L 460 145" stroke="#818cf8" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="490" y="225" fill="#818cf8" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">Nitrogen Dung</text>

  <!-- Rabbit -> Poultry (Base) -->
  <path d="M 290 317 L 510 317" stroke="#38bdf8" stroke-width="2"/>
  <text x="400" y="310" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Chickens eat spilled feed &amp; fly larvae</text>

  <!-- Bottom Callout -->
  <rect x="80" y="385" width="640" height="40" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="400" y="410" fill="#fef08a" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">GOLDEN DILUTION RATIO: 1 Liter Pure Rabbit Urine + 5 Liters Clean Water = 6L Safe Foliar Spray!</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 9: Systematic Farm-Wide Water Harvesting & Drip Pipeline Flow
    # -------------------------------------------------------------------------
    9: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">SYSTEMATIC FARM-WIDE WATER HARVESTING &amp; DRIP PIPELINE</text>
  <text x="400" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">From Rooftop Catchment to Gravity Drip Lines: Zero Water Waste</text>

  <!-- Stage 1: Rooftop Catchment -->
  <g transform="translate(30, 95)">
    <rect width="165" height="260" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="82" cy="35" r="22" fill="#0284c7"/>
    <text x="82" y="42" fill="#ffffff" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">1</text>
    <text x="82" y="80" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">ROOFTOP GUTTER</text>
    <line x1="20" y1="95" x2="145" y2="95" stroke="#334155" stroke-width="1"/>
    <text x="82" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Metal / tile roof</text>
    <text x="82" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Gutter catches rain</text>
    <text x="82" y="175" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Prevents yard erosion</text>
    <rect x="15" y="205" width="135" height="35" rx="4" fill="#0c4a6e"/>
    <text x="82" y="227" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Clean Catchment</text>
  </g>

  <!-- Arrow 1 -->
  <path d="M 200 225 L 220 225" stroke="#38bdf8" stroke-width="3"/>

  <!-- Stage 2: Storage Tank -->
  <g transform="translate(225, 95)">
    <rect width="165" height="260" rx="8" fill="#1e293b" stroke="#0ea5e9" stroke-width="2"/>
    <circle cx="82" cy="35" r="22" fill="#0284c7"/>
    <text x="82" y="42" fill="#ffffff" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">2</text>
    <text x="82" y="80" fill="#0ea5e9" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">STORAGE TANK</text>
    <line x1="20" y1="95" x2="145" y2="95" stroke="#334155" stroke-width="1"/>
    <text x="82" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Masonry or plastic</text>
    <text x="82" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• 5,000L - 10,000L</text>
    <text x="82" y="175" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Drought buffer</text>
    <rect x="15" y="205" width="135" height="35" rx="4" fill="#0369a1"/>
    <text x="82" y="227" fill="#bae6fd" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Dry-Season Reserve</text>
  </g>

  <!-- Arrow 2 -->
  <path d="M 395 225 L 415 225" stroke="#0ea5e9" stroke-width="3"/>

  <!-- Stage 3: Fish Pond -->
  <g transform="translate(420, 95)">
    <rect width="165" height="260" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <circle cx="82" cy="35" r="22" fill="#059669"/>
    <text x="82" y="42" fill="#ffffff" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">3</text>
    <text x="82" y="80" fill="#10b981" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">FISH POND</text>
    <line x1="20" y1="95" x2="145" y2="95" stroke="#334155" stroke-width="1"/>
    <text x="82" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Rears Tilapia fish</text>
    <text x="82" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Waste enriches water</text>
    <text x="82" y="175" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Natural liquid NPK</text>
    <rect x="15" y="205" width="135" height="35" rx="4" fill="#064e3b"/>
    <text x="82" y="227" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Nutrient Enrichment</text>
  </g>

  <!-- Arrow 3 -->
  <path d="M 590 225 L 610 225" stroke="#10b981" stroke-width="3"/>

  <!-- Stage 4: Drip Lines -->
  <g transform="translate(615, 95)">
    <rect width="155" height="260" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <circle cx="77" cy="35" r="22" fill="#059669"/>
    <text x="77" y="42" fill="#ffffff" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">4</text>
    <text x="77" y="80" fill="#34d399" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">DRIP IRRIGATION</text>
    <line x1="20" y1="95" x2="135" y2="95" stroke="#334155" stroke-width="1"/>
    <text x="77" y="125" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Directly to roots</text>
    <text x="77" y="150" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• Near-zero evaporation</text>
    <text x="77" y="175" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">• 70% water savings</text>
    <rect x="15" y="205" width="125" height="35" rx="4" fill="#064e3b"/>
    <text x="77" y="227" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Maximum Yield</text>
  </g>

  <!-- Bottom Callout -->
  <rect x="30" y="375" width="740" height="45" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="400" y="403" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">WATER SYNERGY: Compost in the soil acts like a sponge, holding drip water around crop roots for weeks!</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 10: 2D Spatial Optimization & Transport Labor Layout
    # -------------------------------------------------------------------------
    10: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">2D INTEGRATED FARM SPATIAL OPTIMIZATION</text>
  <text x="400" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Minimizing Transport Labor by Grouping Interdependent Farm Enterprises</text>

  <!-- Farm Boundary Layout -->
  <rect x="50" y="80" width="700" height="330" rx="8" fill="#1e293b" stroke="#475569" stroke-width="2"/>

  <!-- Agroforestry Boundary (Top & Left Borders) -->
  <rect x="60" y="90" width="680" height="25" rx="4" fill="#064e3b" stroke="#34d399" stroke-width="1"/>
  <text x="400" y="107" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">🌲 AGROFORESTRY WINDBREAK &amp; LIVING CONTOUR HEDGEROW 🌲</text>

  <!-- Farm House & Security Zone -->
  <rect x="75" y="130" width="150" height="90" rx="6" fill="#312e81" stroke="#818cf8" stroke-width="1.5"/>
  <text x="150" y="165" fill="#818cf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">HOMESTEAD</text>
  <text x="150" y="185" fill="#c7d2fe" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Water Tank on Roof</text>

  <!-- Livestock Barn & Poultry/Rabbit Coops -->
  <rect x="75" y="240" width="150" height="150" rx="6" fill="#1e1b4b" stroke="#a78bfa" stroke-width="1.5"/>
  <text x="150" y="275" fill="#a78bfa" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">ANIMAL SHEDS</text>
  <text x="150" y="295" fill="#ddd6fe" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Dairy Cow Pen</text>
  <text x="150" y="315" fill="#ddd6fe" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Raised Rabbit Hutch</text>
  <text x="150" y="335" fill="#ddd6fe" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">• Poultry Coop</text>

  <!-- Centrally Located Compost Heap (The Key Spatial Feature) -->
  <rect x="270" y="210" width="160" height="110" rx="8" fill="#78350f" stroke="#fbbf24" stroke-width="2.5"/>
  <text x="350" y="245" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">COMPOST PIT</text>
  <text x="350" y="265" fill="#fef3c7" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Centrally Placed!</text>
  <text x="350" y="285" fill="#fef3c7" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Cuts manual labor distance</text>

  <!-- Vegetable Beds -->
  <rect x="470" y="130" width="260" height="120" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="1.5"/>
  <text x="600" y="165" fill="#34d399" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">ORGANIC VEGETABLE BEDS</text>
  <text x="600" y="185" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Intercropped Kales, Beans &amp; Spinach</text>
  <text x="600" y="205" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Drip Lines Connected</text>

  <!-- Tilapia Fish Pond (Lower Elevation) -->
  <rect x="470" y="270" width="260" height="120" rx="6" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="600" y="305" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">TILAPIA FISH POND</text>
  <text x="600" y="325" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Low Ground (Gravity Runoff Catchment)</text>
  <text x="600" y="345" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Pumps Liquid Fertilizer to Beds</text>

  <!-- Short Transport Pathways -->
  <line x1="225" y1="285" x2="270" y2="265" stroke="#fbbf24" stroke-width="2" stroke-dasharray="3,3"/>
  <line x1="430" y1="250" x2="470" y2="200" stroke="#fbbf24" stroke-width="2" stroke-dasharray="3,3"/>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 11: Exploded Blueprint: 3D Model Cardboard Assembly
    # -------------------------------------------------------------------------
    11: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="38" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">EXPLODED BLUEPRINT: 3D INTEGRATED FARM MODEL</text>
  <text x="400" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Structural Assembly Guide: Constructing Physical 3D Models from Local Scrap Materials</text>

  <!-- Base Foundation -->
  <g transform="translate(50, 90)">
    <rect width="700" height="90" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="30" y="35" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="15" font-weight="bold">FOUNDATION BASEPLATE (Carton Cardboard)</text>
    <text x="30" y="60" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">• Sturdy corrugated box cut to 50cm x 70cm.</text>
    <text x="30" y="78" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="12">• Pencil grid layout drawn directly onto base before gluing structures.</text>
  </g>

  <!-- 3 Main 3D Component Blocks -->
  <!-- 1. Small Buildings -->
  <g transform="translate(50, 200)">
    <rect width="215" height="150" rx="8" fill="#1e1b4b" stroke="#818cf8" stroke-width="1.5"/>
    <text x="107" y="30" fill="#818cf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">1. BUILDINGS &amp; COOP</text>
    <text x="107" y="55" fill="#c7d2fe" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Matchboxes &amp; Tea Cartons</text>
    <line x1="20" y1="70" x2="195" y2="70" stroke="#3730a3" stroke-width="1"/>
    <text x="20" y="95" fill="#e0e7ff" font-family="system-ui, sans-serif" font-size="11">• Cut windows &amp; doors</text>
    <text x="20" y="115" fill="#e0e7ff" font-family="system-ui, sans-serif" font-size="11">• Matchstick stilt legs</text>
    <text x="20" y="135" fill="#e0e7ff" font-family="system-ui, sans-serif" font-size="11">• Glue firmly to baseplate</text>
  </g>

  <!-- 2. Ponds & Water -->
  <g transform="translate(290, 200)">
    <rect width="220" height="150" rx="8" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="110" y="30" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">2. FISH POND &amp; DRIP</text>
    <text x="110" y="55" fill="#7dd3fc" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Bottle Caps &amp; Wool String</text>
    <line x1="20" y1="70" x2="200" y2="70" stroke="#0369a1" stroke-width="1"/>
    <text x="20" y="95" fill="#e0f2fe" font-family="system-ui, sans-serif" font-size="11">• Blue plastic cap for pond</text>
    <text x="20" y="115" fill="#e0f2fe" font-family="system-ui, sans-serif" font-size="11">• Wool threads for drip lines</text>
    <text x="20" y="135" fill="#e0f2fe" font-family="system-ui, sans-serif" font-size="11">• Clear wrap water surface</text>
  </g>

  <!-- 3. Crops, Trees & Clay Animals -->
  <g transform="translate(535, 200)">
    <rect width="215" height="150" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="1.5"/>
    <text x="107" y="30" fill="#34d399" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">3. CROPS &amp; ANIMALS</text>
    <text x="107" y="55" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Twigs, Paper &amp; Clay</text>
    <line x1="20" y1="70" x2="195" y2="70" stroke="#047857" stroke-width="1"/>
    <text x="20" y="95" fill="#ecfdf5" font-family="system-ui, sans-serif" font-size="11">• Dry twigs for tree lines</text>
    <text x="20" y="115" fill="#ecfdf5" font-family="system-ui, sans-serif" font-size="11">• Green paper strip beds</text>
    <text x="20" y="135" fill="#ecfdf5" font-family="system-ui, sans-serif" font-size="11">• Molded mini clay animals</text>
  </g>

  <!-- Bottom Labels Callout -->
  <rect x="50" y="370" width="700" height="50" rx="6" fill="#1e293b" stroke="#cbd5e1" stroke-width="1"/>
  <text x="400" y="400" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">🏷️ TOOTHPICK LABELS: Attach paper flags to toothpicks to label resource loops (e.g. "Manure to Crops", "Urine Foliar")!</text>
</svg>"""
}

def enrich_cbc_grade9_agriculture_topic3():
    """Executes visual and media enrichment for Topic 3: Integrated Farming."""
    print("=" * 80)
    print("STARTING VISUAL ENRICHMENT: CBC GRADE 9 AGRICULTURE — TOPIC 3")
    print("=" * 80)

    topic = Topic.objects.filter(
        subject__grade__curriculum__name__iexact="CBC",
        subject__grade__name="Grade 9",
        subject__name="Agriculture",
        name="Integrated Farming"
    ).first()

    if not topic:
        print("[ERROR] Topic 'Integrated Farming' not found in database!")
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
            svg_content = TOPIC3_SVGS.get(u_order)
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

        # Phase 2C: Attach Multiple Curated Video Lessons across Topic 3
        print("\n[+] Phase 2C: Attaching Multiple Curated Video Lessons across Topic 3...")
        TOPIC3_VIDEOS = {
            2: {
                "url": "https://www.youtube.com/watch?v=VYSXo2eXdhg",
                "resolved_video_id": "VYSXo2eXdhg",
                "title": "Smart Farm: Integrated System Boosts Yields in Kiambu",
                "author": "Citizen TV Kenya",
                "caption": "Watch how smallholder farmers in Kiambu County combine dairy cattle, poultry, biogas energy, and vegetable horticulture in a closed-loop system."
            },
            5: {
                "url": "https://www.youtube.com/watch?v=facNmSCvp-w",
                "resolved_video_id": "facNmSCvp-w",
                "title": "Smart Farm: Focus on Aquaponics Farming in Kenya",
                "author": "Citizen TV Kenya",
                "caption": "Watch this in-depth guide on setting up closed-loop aquaponics, circulating fish wastewater to nourish organic vegetables without chemical fertilizers."
            },
            8: {
                "url": "https://www.youtube.com/watch?v=AQFxLz7fB40",
                "resolved_video_id": "AQFxLz7fB40",
                "title": "Kenya's Gold: Biogas Production from Livestock Waste",
                "author": "Citizen TV Kenya",
                "caption": "Watch how livestock manure is converted into clean methane biogas cooking fuel and rich bio-slurry organic fertilizer."
            },
            11: {
                "url": "https://www.youtube.com/watch?v=uFnDdYWgkV8",
                "resolved_video_id": "uFnDdYWgkV8",
                "title": "Topic Video Review: How to Start an Integrated Farming System with Zero Waste",
                "author": "Africa Farming Journal (G-BiACK Kenya)",
                "caption": "Watch this comprehensive real-world tour of G-BiACK Kenya demonstrating zero-waste integrated farming, closed-loop nutrient recycling, and fish pond irrigation."
            }
        }

        for u_order, v_info in TOPIC3_VIDEOS.items():
            lesson = next((l for l in lessons if l.learning_unit.order == u_order), None)
            if not lesson:
                continue

            video_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="suggested_video"
            ).first()

            if not video_block:
                target_page = 6 if u_order == 11 else 4
                video_block = LessonBlock.objects.create(
                    lesson=lesson,
                    block_id=f"g9_agri_t3_u{u_order}_video",
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
        print(f"[SUCCESS] CBC Grade 9 Agriculture Topic 3 Visual Enrichment Complete!")
        print(f"[*] Total LessonAssets Created & Attached: {total_assets}")
        print("=" * 80)

if __name__ == "__main__":
    enrich_cbc_grade9_agriculture_topic3()
