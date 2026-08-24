"""
VLearn Curriculum Visual Enrichment Script
CBC Grade 7 — Home Science
Topic 9: Special Treatments in Laundrywork (Order: 9)

Attaches:
- 4 Verified Topic-Representative Wikimedia Photographic Visual Hooks (Card 1 of every lesson)
- 8 Custom Sanitized, Responsive (800x450), Pedagogically Rich Vector SVGs
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

# Photographic visual hooks verified live with HTTP 200 responses
TOPIC9_PHOTOS = {
    1: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a4/Wardrobe_with_clothes_hangers_and_gap_illuminated_from_window_light_01.jpg",
        "author": "Wikimedia Commons Contributor",
        "licensing": "CC BY-SA 4.0",
        "caption": "A household wardrobe with garments organized on hangers, showcasing proper textile care and garment preservation."
    },
    2: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e2/Perspiration_stain_on_white_cotton_T-shirt.jpg",
        "author": "Wikimedia Commons Contributor",
        "licensing": "CC BY-SA 4.0",
        "caption": "A localized stain on white cotton fabric requiring targeted spotting treatment before general washing."
    },
    3: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e2/Potato_Starch.JPG",
        "author": "Wikimedia Commons Contributor",
        "licensing": "CC BY-SA 3.0",
        "caption": "Pure white potato laundry starch extracted cleanly from kitchen root vegetables."
    },
    4: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/60/A_dry_cleaner_shop.jpg",
        "author": "Wikimedia Commons Contributor",
        "licensing": "CC BY-SA 3.0",
        "caption": "Dry-cleaned and sponged structured wool suits and garments hanging on hangers to preserve tailored shapes."
    }
}

# 8 Custom High-Definition Vector SVGs
TOPIC9_SVGS = {
    # Lesson 1 Page 2: 4 Special Treatments Wardrobe Blueprint
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
    WARDROBE CARE: THE 4 SPECIAL LAUNDRY TREATMENTS
  </text>

  <!-- 4 Wardrobe Garment Panels -->

  <!-- 1. Cotton Shirt -> Starching -->
  <g transform="translate(45, 88)">
    <rect x="0" y="0" width="165" height="310" fill="#f0f9ff" rx="8" stroke="#bae6fd" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#0284c7" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">1. STARCHING</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="95" fill="#ffffff" rx="4" stroke="#7dd3fc"/>
      <path d="M 40 25 L 95 25 L 115 50 L 95 90 L 40 90 L 20 50 Z" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
      <text x="67" y="60" fill="#0369a1" font-family="system-ui, sans-serif" font-size="8.5" font-weight="800" text-anchor="middle">COTTON SHIRT</text>
    </g>
    <text x="10" y="155" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Garment:</text>
    <text x="10" y="172" fill="#0369a1" font-family="system-ui, sans-serif" font-size="9.5">• White school shirts</text>
    <text x="10" y="185" fill="#0369a1" font-family="system-ui, sans-serif" font-size="9.5">• Table napkins, aprons</text>
    <text x="10" y="205" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Special Care:</text>
    <text x="10" y="222" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Dip in potato starch</text>
    <text x="10" y="235" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Iron damp for crisp shield</text>
    <rect x="8" y="260" width="149" height="28" fill="#e0f2fe" rx="4"/>
    <text x="82" y="278" fill="#0284c7" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Benefit: Crisp &amp; dirt-resistant</text>
  </g>

  <!-- 2. Wool Blazer -> Sponging -->
  <g transform="translate(225, 88)">
    <rect x="0" y="0" width="165" height="310" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#334155" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">2. SPONGING</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="95" fill="#ffffff" rx="4" stroke="#cbd5e1"/>
      <path d="M 35 25 L 100 25 L 115 90 L 20 90 Z" fill="#334155" stroke="#0f172a" stroke-width="2"/>
      <text x="67" y="60" fill="#ffffff" font-family="system-ui, sans-serif" font-size="8.5" font-weight="800" text-anchor="middle">WOOL BLAZER</text>
    </g>
    <text x="10" y="155" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Garment:</text>
    <text x="10" y="172" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Dark school blazers</text>
    <text x="10" y="185" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5">• Heavy winter coats</text>
    <text x="10" y="205" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Special Care:</text>
    <text x="10" y="222" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Brush dry dust down</text>
    <text x="10" y="235" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Wipe with damp soapy sponge</text>
    <rect x="8" y="260" width="149" height="28" fill="#f1f5f9" rx="4"/>
    <text x="82" y="278" fill="#334155" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Benefit: Zero wool shrinkage</text>
  </g>

  <!-- 3. Stained Trousers -> Spotting -->
  <g transform="translate(405, 88)">
    <rect x="0" y="0" width="165" height="310" fill="#fef2f2" rx="8" stroke="#fecaca" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#dc2626" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">3. SPOTTING</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="95" fill="#ffffff" rx="4" stroke="#fca5a5"/>
      <rect x="35" y="20" width="65" height="70" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>
      <circle cx="67" cy="55" r="14" fill="#dc2626"/>
      <text x="67" y="58" fill="#ffffff" font-family="system-ui, sans-serif" font-size="7.5" font-weight="800" text-anchor="middle">STAIN</text>
    </g>
    <text x="10" y="155" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Garment:</text>
    <text x="10" y="172" fill="#991b1b" font-family="system-ui, sans-serif" font-size="9.5">• Ink on sleeves</text>
    <text x="10" y="185" fill="#991b1b" font-family="system-ui, sans-serif" font-size="9.5">• Grease/tea on uniform</text>
    <text x="10" y="205" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Special Care:</text>
    <text x="10" y="222" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Target blemish first</text>
    <text x="10" y="235" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Rub outside-in with blotter</text>
    <rect x="8" y="260" width="149" height="28" fill="#fee2e2" rx="4"/>
    <text x="82" y="278" fill="#991b1b" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Benefit: Erases before wash</text>
  </g>

  <!-- 4. Silk Scarf -> Dry-Cleaning -->
  <g transform="translate(585, 88)">
    <rect x="0" y="0" width="165" height="310" fill="#faf5ff" rx="8" stroke="#e9d5ff" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#9333ea" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">4. DRY-CLEANING</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="95" fill="#ffffff" rx="4" stroke="#d8b4fe"/>
      <path d="M 35 30 Q 67 15 100 30 Q 110 70 85 90 Q 55 60 35 30 Z" fill="#f3e8ff" stroke="#9333ea" stroke-width="2"/>
      <text x="67" y="60" fill="#7e22ce" font-family="system-ui, sans-serif" font-size="8.5" font-weight="800" text-anchor="middle">SILK SCARF</text>
    </g>
    <text x="10" y="155" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Garment:</text>
    <text x="10" y="172" fill="#7e22ce" font-family="system-ui, sans-serif" font-size="9.5">• Pure silk scarves</text>
    <text x="10" y="185" fill="#7e22ce" font-family="system-ui, sans-serif" font-size="9.5">• Fine woolen neckties</text>
    <text x="10" y="205" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Special Care:</text>
    <text x="10" y="222" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Liquid chemical solvent</text>
    <text x="10" y="235" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Open window &amp; gloves</text>
    <rect x="8" y="260" width="149" height="28" fill="#f3e8ff" rx="4"/>
    <text x="82" y="278" fill="#7e22ce" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Benefit: Waterless fiber safety</text>
  </g>
</svg>""",

    # Lesson 1 Page 4: Fabric Structure Decision Matrix
    (1, 4): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="3" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="#f8fafc" rx="12"/>
  <rect x="20" y="20" width="760" height="410" fill="#ffffff" rx="10" stroke="#e2e8f0" stroke-width="2" filter="url(#shadow)"/>

  <!-- Title Banner -->
  <rect x="40" y="30" width="720" height="42" fill="#0f172a" rx="8"/>
  <text x="400" y="57" fill="#ffffff" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">
    FABRIC STRUCTURE &amp; SPECIAL CARE DECISION MATRIX
  </text>

  <!-- 4 Decision Cards (2x2 Grid) -->

  <!-- Top-Left: Cottons -->
  <g transform="translate(45, 85)">
    <rect x="0" y="0" width="345" height="150" fill="#f0f9ff" rx="8" stroke="#bae6fd" stroke-width="1.5"/>
    <rect x="10" y="10" width="325" height="24" fill="#0284c7" rx="4"/>
    <text x="172" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      COTTON &amp; LINEN GARMENTS
    </text>
    <text x="15" y="60" fill="#0369a1" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Properties: Strong when wet; wrinkles easily.</text>
    <text x="15" y="80" fill="#475569" font-family="system-ui, sans-serif" font-size="10">• Problem: Floppy collars &amp; deep dust penetration.</text>
    <text x="15" y="100" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ Prescribed Treatment: STARCHING</text>
    <text x="15" y="120" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Restores crispness and creates a dirt-repelling shield.</text>
  </g>

  <!-- Top-Right: Tailored Wool -->
  <g transform="translate(410, 85)">
    <rect x="0" y="0" width="345" height="150" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="10" y="10" width="325" height="24" fill="#334155" rx="4"/>
    <text x="172" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      STRUCTURED WOOLEN BLAZERS
    </text>
    <text x="15" y="60" fill="#334155" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Properties: Scale-covered fibers; inner pads.</text>
    <text x="15" y="80" fill="#475569" font-family="system-ui, sans-serif" font-size="10">• Problem: Tub washing causes felting &amp; shrinkage.</text>
    <text x="15" y="100" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ Prescribed Treatment: SPONGING</text>
    <text x="15" y="120" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Cleans surface sweat and dust without soaking pads.</text>
  </g>

  <!-- Bottom-Left: Stained Fabrics -->
  <g transform="translate(45, 250)">
    <rect x="0" y="0" width="345" height="155" fill="#fef2f2" rx="8" stroke="#fecaca" stroke-width="1.5"/>
    <rect x="10" y="10" width="325" height="24" fill="#dc2626" rx="4"/>
    <text x="172" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      LOCALIZED FABRIC BLEMISHES
    </text>
    <text x="15" y="60" fill="#991b1b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Properties: Blood, ink, tea, grease spots.</text>
    <text x="15" y="80" fill="#475569" font-family="system-ui, sans-serif" font-size="10">• Problem: Washing hot bakes protein/dye into weave.</text>
    <text x="15" y="100" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ Prescribed Treatment: SPOTTING</text>
    <text x="15" y="120" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Targeted outside-in treatment before general wash.</text>
  </g>

  <!-- Bottom-Right: Delicates -->
  <g transform="translate(410, 250)">
    <rect x="0" y="0" width="345" height="155" fill="#faf5ff" rx="8" stroke="#e9d5ff" stroke-width="1.5"/>
    <rect x="10" y="10" width="325" height="24" fill="#9333ea" rx="4"/>
    <text x="172" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      DELICATE SILKS &amp; FINE TIES
    </text>
    <text x="15" y="60" fill="#7e22ce" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Properties: Protein filament; water weakens fibers.</text>
    <text x="15" y="80" fill="#475569" font-family="system-ui, sans-serif" font-size="10">• Problem: Water bleeds dyes and distorts shape.</text>
    <text x="15" y="100" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ Prescribed Treatment: DRY-CLEANING</text>
    <text x="15" y="120" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Liquid dry solvents dissolve grease without water.</text>
  </g>
</svg>""",

    # Lesson 2 Page 2: 4 Stain Categories & Reagents
    (2, 2): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
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
    THE 4 COMMON STAIN CATEGORIES &amp; HOUSEHOLD REAGENTS
  </text>

  <!-- 4 Stain Category Cards -->

  <!-- 1. Protein Stains -->
  <g transform="translate(45, 88)">
    <rect x="0" y="0" width="165" height="310" fill="#fef2f2" rx="8" stroke="#fecaca" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#ef4444" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">1. PROTEIN (Blood)</text>
    <g transform="translate(15, 40)">
      <rect x="0" y="0" width="135" height="75" fill="#ffffff" rx="4" stroke="#fca5a5"/>
      <circle cx="67" cy="38" r="20" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
      <text x="67" y="44" fill="#991b1b" font-family="system-ui, sans-serif" font-size="14" text-anchor="middle">🩸</text>
    </g>
    <text x="10" y="135" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Reagents:</text>
    <text x="10" y="152" fill="#dc2626" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Cold Water + Salt</text>
    <text x="10" y="175" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Crucial Rule:</text>
    <text x="10" y="192" fill="#991b1b" font-family="system-ui, sans-serif" font-size="9.5">• NEVER USE HOT WATER!</text>
    <text x="10" y="205" fill="#475569" font-family="system-ui, sans-serif" font-size="9">  Heat coagulates protein</text>
    <text x="10" y="218" fill="#475569" font-family="system-ui, sans-serif" font-size="9">  permanently into weave.</text>
    <rect x="8" y="255" width="149" height="30" fill="#fee2e2" rx="4"/>
    <text x="82" y="274" fill="#991b1b" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Examples: Blood, egg, milk</text>
  </g>

  <!-- 2. Grease & Oil -->
  <g transform="translate(225, 88)">
    <rect x="0" y="0" width="165" height="310" fill="#fefce8" rx="8" stroke="#fef08a" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#eab308" rx="4"/>
    <text x="82" y="24" fill="#713f12" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">2. GREASE &amp; OIL</text>
    <g transform="translate(15, 40)">
      <rect x="0" y="0" width="135" height="75" fill="#ffffff" rx="4" stroke="#fde047"/>
      <circle cx="67" cy="38" r="20" fill="#fef9c3" stroke="#ca8a04" stroke-width="2"/>
      <text x="67" y="44" fill="#854d0e" font-family="system-ui, sans-serif" font-size="14" text-anchor="middle">🧈</text>
    </g>
    <text x="10" y="135" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Reagents:</text>
    <text x="10" y="152" fill="#854d0e" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Chalk / Talcum Powder</text>
    <text x="10" y="167" fill="#854d0e" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Warm Detergent</text>
    <text x="10" y="188" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Mechanism:</text>
    <text x="10" y="205" fill="#475569" font-family="system-ui, sans-serif" font-size="9">  Powder absorbs oil;</text>
    <text x="10" y="218" fill="#475569" font-family="system-ui, sans-serif" font-size="9">  warm soap emulsifies.</text>
    <rect x="8" y="255" width="149" height="30" fill="#fef9c3" rx="4"/>
    <text x="82" y="274" fill="#854d0e" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Examples: Cooking oil, fat</text>
  </g>

  <!-- 3. Chemical & Ink -->
  <g transform="translate(405, 88)">
    <rect x="0" y="0" width="165" height="310" fill="#eff6ff" rx="8" stroke="#bfdbfe" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#2563eb" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">3. CHEMICAL (Ink)</text>
    <g transform="translate(15, 40)">
      <rect x="0" y="0" width="135" height="75" fill="#ffffff" rx="4" stroke="#93c5fd"/>
      <circle cx="67" cy="38" r="20" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
      <text x="67" y="44" fill="#1e40af" font-family="system-ui, sans-serif" font-size="14" text-anchor="middle">🖋️</text>
    </g>
    <text x="10" y="135" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Reagents:</text>
    <text x="10" y="152" fill="#1d4ed8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Fresh Lemon Juice</text>
    <text x="10" y="167" fill="#1d4ed8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Sour Milk (Lactic Acid)</text>
    <text x="10" y="188" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Mechanism:</text>
    <text x="10" y="205" fill="#475569" font-family="system-ui, sans-serif" font-size="9">  Mild natural acid breaks</text>
    <text x="10" y="218" fill="#475569" font-family="system-ui, sans-serif" font-size="9">  down dye chemical bonds.</text>
    <rect x="8" y="255" width="149" height="30" fill="#dbeafe" rx="4"/>
    <text x="82" y="274" fill="#1e40af" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Examples: Ballpoint, fruit</text>
  </g>

  <!-- 4. Tannin (Tea/Coffee) -->
  <g transform="translate(585, 88)">
    <rect x="0" y="0" width="165" height="310" fill="#faf5ff" rx="8" stroke="#e9d5ff" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#7c3aed" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">4. TANNIN (Tea)</text>
    <g transform="translate(15, 40)">
      <rect x="0" y="0" width="135" height="75" fill="#ffffff" rx="4" stroke="#d8b4fe"/>
      <circle cx="67" cy="38" r="20" fill="#f3e8ff" stroke="#7c3aed" stroke-width="2"/>
      <text x="67" y="44" fill="#6b21a8" font-family="system-ui, sans-serif" font-size="14" text-anchor="middle">☕</text>
    </g>
    <text x="10" y="135" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Reagents:</text>
    <text x="10" y="152" fill="#6b21a8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Boiling Water Flush</text>
    <text x="10" y="167" fill="#6b21a8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">• Glycerine</text>
    <text x="10" y="188" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Mechanism:</text>
    <text x="10" y="205" fill="#475569" font-family="system-ui, sans-serif" font-size="9">  Height flush forces tannin</text>
    <text x="10" y="218" fill="#475569" font-family="system-ui, sans-serif" font-size="9">  out of white cotton.</text>
    <rect x="8" y="255" width="149" height="30" fill="#f3e8ff" rx="4"/>
    <text x="82" y="274" fill="#6b21a8" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Examples: Black tea, coffee</text>
  </g>
</svg>""",

    # Lesson 2 Page 4: 4-Step Precision Spotting Sequence
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
    THE 4-STEP PRECISION SPOTTING PROTOCOL
  </text>

  <!-- 4 Steps Across -->

  <!-- Step 1 -->
  <g transform="translate(45, 85)">
    <rect x="0" y="0" width="165" height="305" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#dc2626" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">1. COLD SALT SOAK</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="85" fill="#fee2e2" rx="4"/>
      <text x="67" y="48" fill="#991b1b" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">COLD WATER</text>
    </g>
    <text x="10" y="145" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Action:</text>
    <text x="10" y="162" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Soak stained spot</text>
    <text x="10" y="175" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">  in cold salted water.</text>
    <text x="10" y="195" fill="#dc2626" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Key Purpose:</text>
    <text x="10" y="210" fill="#475569" font-family="system-ui, sans-serif" font-size="9">Dissolves protein</text>
    <text x="10" y="223" fill="#475569" font-family="system-ui, sans-serif" font-size="9">without heat coagulation.</text>
  </g>

  <!-- Step 2 -->
  <g transform="translate(225, 85)">
    <rect x="0" y="0" width="165" height="305" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#0284c7" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">2. PLACE BLOTTER</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="85" fill="#e0f2fe" rx="4"/>
      <rect x="25" y="30" width="85" height="30" fill="#ffffff" stroke="#0284c7" stroke-width="1.5"/>
      <text x="67" y="50" fill="#0369a1" font-family="system-ui, sans-serif" font-size="9" font-weight="800" text-anchor="middle">PAD UNDER</text>
    </g>
    <text x="10" y="145" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Action:</text>
    <text x="10" y="162" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Place clean white</text>
    <text x="10" y="175" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">  cloth underneath.</text>
    <text x="10" y="195" fill="#0284c7" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Key Purpose:</text>
    <text x="10" y="210" fill="#475569" font-family="system-ui, sans-serif" font-size="9">Absorbs lifted dye;</text>
    <text x="10" y="223" fill="#475569" font-family="system-ui, sans-serif" font-size="9">prevents back bleed.</text>
  </g>

  <!-- Step 3 -->
  <g transform="translate(405, 85)">
    <rect x="0" y="0" width="165" height="305" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#eab308" rx="4"/>
    <text x="82" y="24" fill="#713f12" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">3. RUB OUTSIDE-IN</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="85" fill="#fef9c3" rx="4"/>
      <circle cx="67" cy="42" r="22" fill="#fef08a" stroke="#ca8a04" stroke-dasharray="3 3"/>
      <text x="67" y="47" fill="#713f12" font-family="system-ui, sans-serif" font-size="14" text-anchor="middle">🎯</text>
    </g>
    <text x="10" y="145" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Action:</text>
    <text x="10" y="162" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Dab reagent gently</text>
    <text x="10" y="175" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">  from edge to center.</text>
    <text x="10" y="195" fill="#854d0e" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Key Purpose:</text>
    <text x="10" y="210" fill="#475569" font-family="system-ui, sans-serif" font-size="9">Stops stain from</text>
    <text x="10" y="223" fill="#475569" font-family="system-ui, sans-serif" font-size="9">spreading outwards!</text>
  </g>

  <!-- Step 4 -->
  <g transform="translate(585, 85)">
    <rect x="0" y="0" width="165" height="305" fill="#f0fdf4" rx="8" stroke="#86efac" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#16a34a" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">4. FLUSH &amp; BLOT</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="85" fill="#dcfce7" rx="4"/>
      <text x="67" y="48" fill="#15803d" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">CLEAN FLUSH</text>
    </g>
    <text x="10" y="145" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Action:</text>
    <text x="10" y="162" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Flush thoroughly with</text>
    <text x="10" y="175" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">  clean cold water.</text>
    <text x="10" y="195" fill="#15803d" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Key Purpose:</text>
    <text x="10" y="210" fill="#475569" font-family="system-ui, sans-serif" font-size="9">Removes all chemical</text>
    <text x="10" y="223" fill="#475569" font-family="system-ui, sans-serif" font-size="9">residues &amp; dissolved dirt.</text>
  </g>
</svg>""",

    # Lesson 3 Page 2: 6-Step Potato Starch Extraction Flowchart
    (3, 2): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
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
    6-STEP HOMEMADE POTATO STARCH EXTRACTION FLOWCHART
  </text>

  <!-- 6 Process Steps (2 Rows of 3) -->

  <!-- Step 1 -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="225" height="150" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="10" y="10" width="205" height="22" fill="#0284c7" rx="4"/>
    <text x="112" y="25" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1. PEEL &amp; WASH</text>
    <text x="15" y="55" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Peel 2 medium potatoes.</text>
    <text x="15" y="70" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Wash in cold water thoroughly.</text>
    <text x="15" y="90" fill="#0284c7" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Goal: Remove all surface soil.</text>
  </g>

  <!-- Step 2 -->
  <g transform="translate(285, 80)">
    <rect x="0" y="0" width="225" height="150" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="10" y="10" width="205" height="22" fill="#0284c7" rx="4"/>
    <text x="112" y="25" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. GRATE FINELY</text>
    <text x="15" y="55" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Grate finely into clean bowl.</text>
    <text x="15" y="70" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Use small grater holes.</text>
    <text x="15" y="90" fill="#0284c7" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Goal: Rupture cells to free starch.</text>
  </g>

  <!-- Step 3 -->
  <g transform="translate(525, 80)">
    <rect x="0" y="0" width="225" height="150" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="10" y="10" width="205" height="22" fill="#0284c7" rx="4"/>
    <text x="112" y="25" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3. SOAK &amp; STIR</text>
    <text x="15" y="55" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Add 500 ml cold water.</text>
    <text x="15" y="70" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Stir vigorously with spoon.</text>
    <text x="15" y="90" fill="#0284c7" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Goal: Suspend starch in water.</text>
  </g>

  <!-- Step 4 -->
  <g transform="translate(45, 245)">
    <rect x="0" y="0" width="225" height="155" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="10" y="10" width="205" height="22" fill="#16a34a" rx="4"/>
    <text x="112" y="25" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">4. STRAIN THROUGH CLOTH</text>
    <text x="15" y="55" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Pour through fine mesh cloth.</text>
    <text x="15" y="70" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Squeeze out starchy liquid.</text>
    <text x="15" y="90" fill="#16a34a" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Goal: Trap solid potato shreds.</text>
  </g>

  <!-- Step 5 -->
  <g transform="translate(285, 245)">
    <rect x="0" y="0" width="225" height="155" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="10" y="10" width="205" height="22" fill="#16a34a" rx="4"/>
    <text x="112" y="25" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">5. SETTLE SEDIMENT</text>
    <text x="15" y="55" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Let sit 10 to 15 minutes.</text>
    <text x="15" y="70" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Heavy starch settles to bottom.</text>
    <text x="15" y="90" fill="#16a34a" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Goal: Dense white sediment layer.</text>
  </g>

  <!-- Step 6 -->
  <g transform="translate(525, 245)">
    <rect x="0" y="0" width="225" height="155" fill="#f0fdf4" rx="8" stroke="#86efac" stroke-width="1.5"/>
    <rect x="10" y="10" width="205" height="22" fill="#16a34a" rx="4"/>
    <text x="112" y="25" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">6. DECANT WATER</text>
    <text x="15" y="55" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Pour off top water slowly.</text>
    <text x="15" y="70" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Keep thick pure white paste.</text>
    <text x="15" y="90" fill="#15803d" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Result: 100% Pure Laundry Starch!</text>
  </g>
</svg>""",

    # Lesson 3 Page 4: Microscopic Fiber Model
    (3, 4): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
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
    MICROSCOPIC FIBER MODEL: UNSTARCHED vs. STARCHED SHIELD
  </text>

  <!-- Left: Unstarched Cotton Weave -->
  <g transform="translate(45, 85)">
    <rect x="0" y="0" width="340" height="315" fill="#fef2f2" rx="8" stroke="#fecaca" stroke-width="1.5"/>
    <rect x="15" y="15" width="310" height="28" fill="#ef4444" rx="5"/>
    <text x="170" y="34" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      UNSTARCHED COTTON (Fuzzy &amp; Trapping Dirt)
    </text>

    <!-- Microscopic View -->
    <g transform="translate(20, 55)">
      <rect x="0" y="0" width="300" height="115" fill="#ffffff" rx="6" stroke="#fca5a5"/>
      <!-- Fuzzy Fibers with Gaps -->
      <line x1="40" y1="30" x2="260" y2="30" stroke="#f87171" stroke-width="8" stroke-linecap="round"/>
      <line x1="40" y1="60" x2="260" y2="60" stroke="#f87171" stroke-width="8" stroke-linecap="round"/>
      <line x1="40" y1="90" x2="260" y2="90" stroke="#f87171" stroke-width="8" stroke-linecap="round"/>
      <!-- Trapped Dirt deep inside -->
      <circle cx="100" cy="45" r="7" fill="#7f1d1d"/>
      <circle cx="160" cy="75" r="8" fill="#7f1d1d"/>
      <circle cx="210" cy="45" r="6" fill="#7f1d1d"/>
      <text x="150" y="105" fill="#991b1b" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Dirt Trapped Deep in Gaps!</text>
    </g>

    <g transform="translate(20, 185)">
      <text x="0" y="15" fill="#991b1b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✗ Surface: Fuzzy, rough thread hairs.</text>
      <text x="0" y="35" fill="#991b1b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✗ Dust Penetration: Sinks deep into fibers.</text>
      <text x="0" y="55" fill="#991b1b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✗ Appearance: Limp, floppy, easily wrinkled.</text>
      <text x="0" y="75" fill="#991b1b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✗ Next Laundry: Hard to scrub out trapped dirt.</text>
    </g>
  </g>

  <!-- Right: Starched Cotton Weave -->
  <g transform="translate(415, 85)">
    <rect x="0" y="0" width="340" height="315" fill="#f0fdf4" rx="8" stroke="#bbf7d0" stroke-width="2"/>
    <rect x="15" y="15" width="310" height="28" fill="#16a34a" rx="5"/>
    <text x="170" y="34" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      STARCHED COTTON (Smooth Protective Shield)
    </text>

    <!-- Microscopic View -->
    <g transform="translate(20, 55)">
      <rect x="0" y="0" width="300" height="115" fill="#ffffff" rx="6" stroke="#86efac"/>
      <!-- Sealed Smooth Starch Film Over Fibers -->
      <rect x="30" y="20" width="240" height="75" fill="#dcfce7" rx="4" stroke="#22c55e" stroke-width="2"/>
      <line x1="40" y1="35" x2="260" y2="35" stroke="#86efac" stroke-width="6"/>
      <line x1="40" y1="60" x2="260" y2="60" stroke="#86efac" stroke-width="6"/>
      <line x1="40" y1="85" x2="260" y2="85" stroke="#86efac" stroke-width="6"/>
      <!-- Dirt Sits on Top of Starch Layer -->
      <circle cx="90" cy="15" r="5" fill="#b45309"/>
      <circle cx="150" cy="14" r="6" fill="#b45309"/>
      <circle cx="210" cy="15" r="5" fill="#b45309"/>
      <text x="150" y="105" fill="#15803d" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Dirt Sits Safely On Top of Barrier!</text>
    </g>

    <g transform="translate(20, 185)">
      <text x="0" y="15" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ Surface: Smooth, sealed, glazed finish.</text>
      <text x="0" y="35" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ Dust Penetration: Blocked by starch layer.</text>
      <text x="0" y="55" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ Appearance: Crisp, sharp, smart posture.</text>
      <text x="0" y="75" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ Next Laundry: Dirt slides off with starch!</text>
    </g>
  </g>
</svg>""",

    # Lesson 4 Page 2: 4-Step Blazer Sponging Protocol
    (4, 2): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
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
    4-STEP PROTOCOL: SPONGING A STRUCTURED SCHOOL BLAZER
  </text>

  <!-- 4 Steps Across -->

  <!-- Step 1 -->
  <g transform="translate(45, 85)">
    <rect x="0" y="0" width="165" height="305" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#334155" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">1. BRUSH DOWN</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="85" fill="#f1f5f9" rx="4"/>
      <text x="67" y="48" fill="#334155" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">DRY BRUSH</text>
    </g>
    <text x="10" y="145" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Action:</text>
    <text x="10" y="162" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Hang on hanger.</text>
    <text x="10" y="175" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Brush dust downwards.</text>
    <text x="10" y="195" fill="#334155" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Rule:</text>
    <text x="10" y="210" fill="#475569" font-family="system-ui, sans-serif" font-size="9">Stops dust from</text>
    <text x="10" y="223" fill="#475569" font-family="system-ui, sans-serif" font-size="9">turning into mud.</text>
  </g>

  <!-- Step 2 -->
  <g transform="translate(225, 85)">
    <rect x="0" y="0" width="165" height="305" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#0284c7" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">2. DAMP SOAP WIPE</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="85" fill="#e0f2fe" rx="4"/>
      <text x="67" y="48" fill="#0369a1" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">DAMP SPONGE</text>
    </g>
    <text x="10" y="145" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Action:</text>
    <text x="10" y="162" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Warm soapy water.</text>
    <text x="10" y="175" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Squeeze until barely damp.</text>
    <text x="10" y="195" fill="#0284c7" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Focus Areas:</text>
    <text x="10" y="210" fill="#475569" font-family="system-ui, sans-serif" font-size="9">Collar, cuffs &amp;</text>
    <text x="10" y="223" fill="#475569" font-family="system-ui, sans-serif" font-size="9">sweaty underarms.</text>
  </g>

  <!-- Step 3 -->
  <g transform="translate(405, 85)">
    <rect x="0" y="0" width="165" height="305" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#0891b2" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">3. CLEAN RINSE</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="85" fill="#cffafe" rx="4"/>
      <text x="67" y="48" fill="#0891b2" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">CLEAN CLOTH</text>
    </g>
    <text x="10" y="145" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Action:</text>
    <text x="10" y="162" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Dip cloth in clean water.</text>
    <text x="10" y="175" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Wring tightly &amp; wipe.</text>
    <text x="10" y="195" fill="#0891b2" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Goal:</text>
    <text x="10" y="210" fill="#475569" font-family="system-ui, sans-serif" font-size="9">Removes all soap</text>
    <text x="10" y="223" fill="#475569" font-family="system-ui, sans-serif" font-size="9">residues completely.</text>
  </g>

  <!-- Step 4 -->
  <g transform="translate(585, 85)">
    <rect x="0" y="0" width="165" height="305" fill="#f0fdf4" rx="8" stroke="#86efac" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#16a34a" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">4. SHADE HANGER DRY</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="85" fill="#dcfce7" rx="4"/>
      <text x="67" y="48" fill="#15803d" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">VENTILATED SHADE</text>
    </g>
    <text x="10" y="145" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Action:</text>
    <text x="10" y="162" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Hang on shaped hanger.</text>
    <text x="10" y="175" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Dry in breezy shade.</text>
    <text x="10" y="195" fill="#15803d" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Result:</text>
    <text x="10" y="210" fill="#475569" font-family="system-ui, sans-serif" font-size="9">Preserves shoulder</text>
    <text x="10" y="223" fill="#475569" font-family="system-ui, sans-serif" font-size="9">fit and shape 100%!</text>
  </g>
</svg>""",

    # Lesson 4 Page 4: Home Dry-Cleaning Safety & Eco-Disposal
    (4, 4): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
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
    DRY-CLEANING SAFETY &amp; ECO-FRIENDLY CHEMICAL DISPOSAL
  </text>

  <!-- Left: Dry Cleaning Safety Rules -->
  <g transform="translate(45, 85)">
    <rect x="0" y="0" width="340" height="315" fill="#fef2f2" rx="8" stroke="#fecaca" stroke-width="1.5"/>
    <rect x="15" y="15" width="310" height="28" fill="#dc2626" rx="5"/>
    <text x="170" y="34" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      DRY-CLEANING SAFETY PROTOCOLS
    </text>

    <g transform="translate(20, 55)">
      <rect x="0" y="0" width="300" height="48" fill="#ffffff" rx="4" stroke="#fca5a5"/>
      <text x="15" y="20" fill="#991b1b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">🪟 1. Wide-Open Windows</text>
      <text x="15" y="35" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Cross-ventilation carries toxic solvent fumes away.</text>

      <rect x="0" y="58" width="300" height="48" fill="#ffffff" rx="4" stroke="#fca5a5"/>
      <text x="15" y="78" fill="#991b1b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">🧤 2. Rubber Gloves Mandatory</text>
      <text x="15" y="93" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Protects skin from chemical burns and drying.</text>

      <rect x="0" y="116" width="300" height="48" fill="#ffffff" rx="4" stroke="#fca5a5"/>
      <text x="15" y="136" fill="#991b1b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">🚫🔥 3. ZERO FLAMES / NO HEAT</text>
      <text x="15" y="151" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Solvents are highly flammable! Never heat near fire.</text>

      <rect x="0" y="174" width="300" height="48" fill="#ffffff" rx="4" stroke="#fca5a5"/>
      <text x="15" y="194" fill="#991b1b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">👨‍🏫 4. Adult Supervision</text>
      <text x="15" y="209" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Teacher or parent must supervise every step.</text>
    </g>
  </g>

  <!-- Right: Eco-Friendly Waste Disposal -->
  <g transform="translate(415, 85)">
    <rect x="0" y="0" width="340" height="315" fill="#f0fdf4" rx="8" stroke="#86efac" stroke-width="2"/>
    <rect x="15" y="15" width="310" height="28" fill="#16a34a" rx="5"/>
    <text x="170" y="34" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      ECO-FRIENDLY DISPOSAL VS. DUMPING
    </text>

    <g transform="translate(20, 55)">
      <rect x="0" y="0" width="300" height="95" fill="#ffffff" rx="4" stroke="#bbf7d0"/>
      <text x="15" y="22" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ Decant into Sealed Glass Bottle</text>
      <text x="15" y="40" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Label: 'WASTE CHEMICAL SOLVENT'.</text>
      <text x="15" y="55" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Let dirt settle for reuse or collection.</text>
      <text x="15" y="75" fill="#15803d" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Preserves garden soil &amp; earthworms!</text>

      <rect x="0" y="105" width="300" height="95" fill="#fee2e2" rx="4" stroke="#f87171"/>
      <text x="15" y="127" fill="#991b1b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✗ NEVER Dump on Garden Soil!</text>
      <text x="15" y="145" fill="#7f1d1d" font-family="system-ui, sans-serif" font-size="9.5">• Poisons soil nutrients &amp; food crops.</text>
      <text x="15" y="160" fill="#7f1d1d" font-family="system-ui, sans-serif" font-size="9.5">• Leaches into underground well water.</text>
      <text x="15" y="180" fill="#991b1b" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700">Causes severe environmental degradation!</text>
    </g>
  </g>
</svg>""",
}

def enrich_cbc_grade7_home_science_topic9():
    print("=" * 80)
    print("STARTING VISUAL ENRICHMENT: CBC GRADE 7 HOME SCIENCE — TOPIC 9: SPECIAL TREATMENTS IN LAUNDRYWORK")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 7").first()
    subject = Subject.objects.filter(grade=grade, name="Home Science").first()
    topic = Topic.objects.filter(subject=subject, name="Special Treatments in Laundrywork").first()

    assert topic, "Topic 9 (Special Treatments in Laundrywork) not found!"
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
        photo_info = TOPIC9_PHOTOS.get(u_order)
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
    for (u_order, page_num), svg_code in TOPIC9_SVGS.items():
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
    print(f"[SUCCESS] CBC Grade 7 Home Science Topic 9 Visual Enrichment Complete!")
    print(f"[*] Total LessonAssets Created & Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_cbc_grade7_home_science_topic9()
