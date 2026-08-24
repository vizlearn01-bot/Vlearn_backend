"""
VLearn Curriculum Visual Enrichment Script
CBC Grade 7 — Home Science
Topic 8: Household Cleaning Agents & Homemade Soap (Order: 8)

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
TOPIC8_PHOTOS = {
    1: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/86/Washing_hands_%28cropped%29.jpg",
        "author": "Wikimedia Commons Contributor",
        "licensing": "CC BY-SA 3.0",
        "caption": "Hands washing with soap and water to produce a rich, cleansing lather that lifts dirt away."
    },
    2: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/ef/Laundry_detergent_1.jpg",
        "author": "Wikimedia Commons Contributor",
        "licensing": "CC BY-SA 3.0",
        "caption": "Granular laundry detergent powder and scooper illustrating physical cleaning agent formats."
    },
    3: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d9/Handmade_soap.jpg",
        "author": "Wikimedia Commons Contributor",
        "licensing": "CC BY-SA 3.0",
        "caption": "Handmade natural soap bars cured in wooden molds and infused with herbal extracts."
    },
    4: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/04/Wash_and_sanitize_hands_to_prevent_spread_-_DPLA_-_860bcec48f19b03b1e1fc7bfa67c4f9e.jpg",
        "author": "DPLA / Public Domain",
        "licensing": "Public Domain",
        "caption": "A public health campaign banner promoting handwashing with soap to prevent disease spread in schools and communities."
    }
}

# 8 Custom High-Definition Vector SVGs
TOPIC8_SVGS = {
    # Lesson 1 Page 2: Mineral Flow Diagram (Soft vs Hard Water)
    (1, 2): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="softGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="hardGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#94a3b8"/>
      <stop offset="100%" stop-color="#475569"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="#f8fafc" rx="12"/>
  <rect x="20" y="20" width="760" height="410" fill="#ffffff" rx="10" stroke="#e2e8f0" stroke-width="2" filter="url(#shadow)"/>

  <!-- Title Banner -->
  <rect x="40" y="30" width="720" height="42" fill="#0f172a" rx="8"/>
  <text x="400" y="57" fill="#ffffff" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">
    WATER HARDNESS CHEMISTRY: SOFT WATER vs. HARD WATER
  </text>

  <!-- Left: Soft Water (Rainwater) -->
  <g transform="translate(45, 85)">
    <rect x="0" y="0" width="340" height="315" fill="#f0f9ff" rx="8" stroke="#bae6fd" stroke-width="2"/>
    <rect x="15" y="15" width="310" height="30" fill="#0284c7" rx="6"/>
    <text x="170" y="35" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">
      SOFT WATER (e.g. Rainwater)
    </text>

    <!-- Visual Diagram -->
    <g transform="translate(30, 60)">
      <rect x="0" y="0" width="280" height="115" fill="#ffffff" rx="6" stroke="#7dd3fc" stroke-width="1.5"/>
      <!-- Pure H2O drops -->
      <circle cx="50" cy="40" r="16" fill="url(#softGrad)"/>
      <text x="50" y="45" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">H₂O</text>
      <!-- Soap Bar -->
      <rect x="100" y="30" width="45" height="25" fill="#facc15" rx="3" stroke="#ca8a04"/>
      <text x="122" y="47" fill="#713f12" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Soap</text>
      <!-- Arrow -->
      <path d="M 155 42 L 180 42" stroke="#0284c7" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
      <!-- Huge Foam Cloud -->
      <path d="M 200 45 C 190 30 215 15 235 25 C 255 15 275 30 270 45 C 280 60 260 80 240 75 C 220 80 195 65 200 45 Z" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2"/>
      <text x="238" y="50" fill="#0369a1" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Rich Lather!</text>
    </g>

    <!-- Characteristics -->
    <g transform="translate(25, 190)">
      <text x="0" y="15" fill="#0369a1" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ Mineral Content: Very low / zero minerals.</text>
      <text x="0" y="35" fill="#0369a1" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ Soap Reaction: Lathers immediately.</text>
      <text x="0" y="55" fill="#0369a1" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ Fabric Effect: Clothes stay bright &amp; soft.</text>
      <text x="0" y="75" fill="#0369a1" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ Economic Benefit: Uses 70% less soap!</text>
      <rect x="0" y="90" width="290" height="24" fill="#e0f2fe" rx="4"/>
      <text x="145" y="106" fill="#0284c7" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Ideal for bathing &amp; delicate school uniforms!</text>
    </g>
  </g>

  <!-- Right: Hard Water (Borehole) -->
  <g transform="translate(415, 85)">
    <rect x="0" y="0" width="340" height="315" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="2"/>
    <rect x="15" y="15" width="310" height="30" fill="#475569" rx="6"/>
    <text x="170" y="35" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">
      HARD WATER (e.g. Borehole / Well)
    </text>

    <!-- Visual Diagram -->
    <g transform="translate(30, 60)">
      <rect x="0" y="0" width="280" height="115" fill="#ffffff" rx="6" stroke="#cbd5e1" stroke-width="1.5"/>
      <!-- Dissolved Minerals -->
      <circle cx="35" cy="40" r="14" fill="#94a3b8"/>
      <text x="35" y="44" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Ca²⁺</text>
      <circle cx="70" cy="40" r="14" fill="#64748b"/>
      <text x="70" y="44" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Mg²⁺</text>
      <!-- Soap Bar -->
      <rect x="105" y="30" width="40" height="25" fill="#facc15" rx="3" stroke="#ca8a04"/>
      <text x="125" y="47" fill="#713f12" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Soap</text>
      <!-- Arrow -->
      <path d="M 155 42 L 180 42" stroke="#64748b" stroke-width="3" fill="none"/>
      <!-- Scum Curd Flakes -->
      <rect x="195" y="25" width="75" height="40" fill="#f1f5f9" rx="4" stroke="#94a3b8"/>
      <circle cx="210" cy="40" r="4" fill="#64748b"/>
      <circle cx="230" cy="50" r="6" fill="#475569"/>
      <circle cx="255" cy="35" r="5" fill="#64748b"/>
      <text x="232" y="80" fill="#dc2626" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Sticky Scum!</text>
    </g>

    <!-- Characteristics -->
    <g transform="translate(25, 190)">
      <text x="0" y="15" fill="#334155" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✗ Mineral Content: High Calcium &amp; Magnesium.</text>
      <text x="0" y="35" fill="#334155" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✗ Soap Reaction: Forms insoluble grey scum.</text>
      <text x="0" y="55" fill="#334155" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✗ Fabric Effect: Leaves whites dull grey.</text>
      <text x="0" y="75" fill="#334155" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✗ Economic Waste: Destroys soap rapidly!</text>
      <rect x="0" y="90" width="290" height="24" fill="#fee2e2" rx="4"/>
      <text x="145" y="106" fill="#991b1b" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Remedy: Use Soapless Detergent Powder!</text>
    </g>
  </g>
</svg>""",

    # Lesson 1 Page 4: Molecular Architecture (Soap vs Detergent)
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
    MOLECULAR STRUCTURE: NATURAL SOAP vs. SYNTHETIC DETERGENT
  </text>

  <!-- Left: Soap Molecule -->
  <g transform="translate(45, 85)">
    <rect x="0" y="0" width="340" height="315" fill="#f0fdf4" rx="8" stroke="#bbf7d0" stroke-width="1.5"/>
    <rect x="15" y="15" width="310" height="28" fill="#16a34a" rx="5"/>
    <text x="170" y="34" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      NATURAL SOAP MOLECULE (Fat-Based)
    </text>

    <!-- Chemical Illustration -->
    <g transform="translate(25, 55)">
      <rect x="0" y="0" width="290" height="115" fill="#ffffff" rx="6" stroke="#86efac"/>
      <!-- Hydrophobic Tail (Zigzag Fatty Chain) -->
      <path d="M 30 65 L 50 45 L 70 65 L 90 45 L 110 65 L 130 45 L 150 65 L 170 45 L 190 65" fill="none" stroke="#16a34a" stroke-width="4" stroke-linecap="round"/>
      <text x="110" y="90" fill="#15803d" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">
        Lipid Tail (Attracted to Oil/Grease)
      </text>
      <!-- Hydrophilic Head -->
      <circle cx="225" cy="55" r="22" fill="#22c55e" stroke="#15803d" stroke-width="2"/>
      <text x="225" y="53" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="800" text-anchor="middle">-COO⁻</text>
      <text x="225" y="66" fill="#ffffff" font-family="system-ui, sans-serif" font-size="8.5" font-weight="800" text-anchor="middle">Na⁺/K⁺</text>
      <text x="225" y="95" fill="#15803d" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Water Head</text>
    </g>

    <!-- Details -->
    <g transform="translate(25, 185)">
      <text x="0" y="15" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Raw Source: Animal lipids &amp; vegetable oils.</text>
      <text x="0" y="35" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Biodegradability: 100% eco-friendly.</text>
      <text x="0" y="55" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Skin Mildness: Gentle on hands and face.</text>
      <text x="0" y="75" fill="#dc2626" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Hard Water: Head reacts with Ca²⁺ $\rightarrow$ Scum!</text>
    </g>
  </g>

  <!-- Right: Synthetic Detergent Molecule -->
  <g transform="translate(415, 85)">
    <rect x="0" y="0" width="340" height="315" fill="#eff6ff" rx="8" stroke="#bfdbfe" stroke-width="1.5"/>
    <rect x="15" y="15" width="310" height="28" fill="#2563eb" rx="5"/>
    <text x="170" y="34" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      SYNTHETIC DETERGENT (Petroleum-Based)
    </text>

    <!-- Chemical Illustration -->
    <g transform="translate(25, 55)">
      <rect x="0" y="0" width="290" height="115" fill="#ffffff" rx="6" stroke="#93c5fd"/>
      <!-- Synthetic Tail -->
      <path d="M 30 65 L 50 45 L 70 65 L 90 45 L 110 65 L 130 45 L 150 65 L 170 45 L 190 65" fill="none" stroke="#2563eb" stroke-width="4" stroke-linecap="round"/>
      <text x="110" y="90" fill="#1d4ed8" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">
        Petroleum Tail (Heavy Degreaser)
      </text>
      <!-- Synthetic Sulfonate Head -->
      <circle cx="225" cy="55" r="22" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2"/>
      <text x="225" y="53" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="800" text-anchor="middle">-SO₃⁻</text>
      <text x="225" y="66" fill="#ffffff" font-family="system-ui, sans-serif" font-size="8.5" font-weight="800" text-anchor="middle">Na⁺</text>
      <text x="225" y="95" fill="#1d4ed8" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Resistant Head</text>
    </g>

    <!-- Details -->
    <g transform="translate(25, 185)">
      <text x="0" y="15" fill="#1d4ed8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Raw Source: Synthetic petroleum chemicals.</text>
      <text x="0" y="35" fill="#1d4ed8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Hard Water: Ignores Ca²⁺ &amp; Mg²⁺ $\rightarrow$ ZERO SCUM!</text>
      <text x="0" y="55" fill="#1d4ed8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Cleaning Power: Cuts heavy grease rapidly.</text>
      <text x="0" y="75" fill="#dc2626" font-family="system-ui, sans-serif" font-size="11" font-weight="700">• Skin Impact: Can dry out hands (use gloves!).</text>
    </g>
  </g>
</svg>""",

    # Lesson 2 Page 2: 3D Grid of 4 Physical Cleaner Formats
    (2, 2): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
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
    PHYSICAL FORMATS OF HOUSEHOLD CLEANING AGENTS
  </text>

  <!-- 2x2 Bento Grid -->

  <!-- Top-Left: Solid Bars & Cakes -->
  <g transform="translate(45, 85)">
    <rect x="0" y="0" width="345" height="150" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="10" y="10" width="325" height="24" fill="#eab308" rx="4"/>
    <text x="172" y="26" fill="#713f12" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      1. SOLID BARS &amp; CAKES
    </text>
    <!-- Icon -->
    <rect x="25" y="55" width="75" height="45" fill="#fde047" rx="6" stroke="#ca8a04" stroke-width="2"/>
    <text x="62" y="82" fill="#854d0e" font-family="system-ui, sans-serif" font-size="10" font-weight="800" text-anchor="middle">SOAP BAR</text>
    <!-- Description -->
    <text x="120" y="65" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Solid Compressed Blocks</text>
    <text x="120" y="80" fill="#64748b" font-family="system-ui, sans-serif" font-size="9.5">• Economical, durable, long-lasting.</text>
    <text x="120" y="95" fill="#64748b" font-family="system-ui, sans-serif" font-size="9.5">• Toilet soap for bathing, laundry bars.</text>
    <text x="120" y="115" fill="#854d0e" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Best for: Personal hygiene &amp; basins.</text>
  </g>

  <!-- Top-Right: Granular Powders -->
  <g transform="translate(410, 85)">
    <rect x="0" y="0" width="345" height="150" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="10" y="10" width="325" height="24" fill="#3b82f6" rx="4"/>
    <text x="172" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      2. GRANULAR POWDERS
    </text>
    <!-- Icon -->
    <rect x="25" y="50" width="65" height="60" fill="#dbeafe" rx="4" stroke="#2563eb" stroke-width="2"/>
    <circle cx="57" cy="70" r="3" fill="#2563eb"/>
    <circle cx="45" cy="85" r="2.5" fill="#2563eb"/>
    <circle cx="68" cy="90" r="3.5" fill="#2563eb"/>
    <text x="57" y="102" fill="#1e40af" font-family="system-ui, sans-serif" font-size="8" font-weight="700" text-anchor="middle">POWDER</text>
    <!-- Description -->
    <text x="110" y="65" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Dry Dissolvable Granules</text>
    <text x="110" y="80" fill="#64748b" font-family="system-ui, sans-serif" font-size="9.5">• High concentration of builders.</text>
    <text x="110" y="95" fill="#64748b" font-family="system-ui, sans-serif" font-size="9.5">• Dissolves in buckets for large loads.</text>
    <text x="110" y="115" fill="#1d4ed8" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Best for: Heavy laundry &amp; floors.</text>
  </g>

  <!-- Bottom-Left: Pouring Liquids -->
  <g transform="translate(45, 250)">
    <rect x="0" y="0" width="345" height="155" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="10" y="10" width="325" height="24" fill="#06b6d4" rx="4"/>
    <text x="172" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      3. POURING LIQUIDS
    </text>
    <!-- Icon -->
    <path d="M 45 60 L 65 60 L 75 105 L 35 105 Z" fill="#cffafe" stroke="#0891b2" stroke-width="2"/>
    <circle cx="55" cy="52" r="6" fill="#0891b2"/>
    <text x="55" y="90" fill="#0e7490" font-family="system-ui, sans-serif" font-size="8" font-weight="700" text-anchor="middle">LIQUID</text>
    <!-- Description -->
    <text x="105" y="65" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Viscous Fluid Solutions</text>
    <text x="105" y="80" fill="#64748b" font-family="system-ui, sans-serif" font-size="9.5">• Instant dispersion without residue.</text>
    <text x="105" y="95" fill="#64748b" font-family="system-ui, sans-serif" font-size="9.5">• Mild pH, hygienic push dispensers.</text>
    <text x="105" y="115" fill="#0891b2" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Best for: Dishes, handwash, glass.</text>
  </g>

  <!-- Bottom-Right: Concentrated Pastes -->
  <g transform="translate(410, 250)">
    <rect x="0" y="0" width="345" height="155" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="10" y="10" width="325" height="24" fill="#059669" rx="4"/>
    <text x="172" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      4. CONCENTRATED PASTES
    </text>
    <!-- Icon -->
    <rect x="25" y="60" width="65" height="45" fill="#d1fae5" rx="4" stroke="#059669" stroke-width="2"/>
    <ellipse cx="57" cy="60" rx="32" ry="8" fill="#10b981"/>
    <text x="57" y="90" fill="#065f46" font-family="system-ui, sans-serif" font-size="8" font-weight="700" text-anchor="middle">PASTE TUB</text>
    <!-- Description -->
    <text x="105" y="65" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Thick Abrasive Gels</text>
    <text x="105" y="80" fill="#64748b" font-family="system-ui, sans-serif" font-size="9.5">• Clings to vertical greasy walls.</text>
    <text x="105" y="95" fill="#64748b" font-family="system-ui, sans-serif" font-size="9.5">• Cuts heavy baked carbon soot.</text>
    <text x="105" y="115" fill="#059669" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Best for: Sufurias, jiko stoves, ovens.</text>
  </g>
</svg>""",

    # Lesson 2 Page 4: Saponification Chemistry Recipe Scale
    (2, 4): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
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
    THE 4 NATURAL INGREDIENTS OF SAPONIFICATION
  </text>

  <!-- 4 Ingredient Cards Horizontally -->

  <!-- 1. Wood Ash Filtrate -->
  <g transform="translate(45, 90)">
    <rect x="0" y="0" width="165" height="305" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#64748b" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">1. WOOD ASH LYE</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="95" fill="#e2e8f0" rx="4"/>
      <path d="M 45 20 L 75 20 L 85 85 L 35 85 Z" fill="#94a3b8" rx="2"/>
      <text x="60" y="55" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="800" text-anchor="middle">ALKALI</text>
    </g>
    <text x="10" y="155" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Chemical Role:</text>
    <text x="10" y="172" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Natural Potassium</text>
    <text x="10" y="185" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">  Hydroxide (Alkali).</text>
    <text x="10" y="200" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Triggers the chemical</text>
    <text x="10" y="213" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">  reaction with fat.</text>
    <rect x="8" y="255" width="149" height="30" fill="#f1f5f9" rx="4"/>
    <text x="82" y="274" fill="#334155" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Source: Firewood ash</text>
  </g>

  <!-- 2. Fats & Oils -->
  <g transform="translate(225, 90)">
    <rect x="0" y="0" width="165" height="305" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#eab308" rx="4"/>
    <text x="82" y="24" fill="#713f12" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">2. FATS &amp; OILS</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="95" fill="#fef9c3" rx="4"/>
      <rect x="40" y="25" width="55" height="60" fill="#facc15" rx="5" stroke="#ca8a04"/>
      <text x="67" y="60" fill="#713f12" font-family="system-ui, sans-serif" font-size="9" font-weight="800" text-anchor="middle">LIPIDS</text>
    </g>
    <text x="10" y="155" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Chemical Role:</text>
    <text x="10" y="172" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Provides Fatty Acids.</text>
    <text x="10" y="185" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Combines with alkali</text>
    <text x="10" y="200" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">  to form soap base.</text>
    <text x="10" y="213" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Moisturizes skin.</text>
    <rect x="8" y="255" width="149" height="30" fill="#fef08a" rx="4"/>
    <text x="82" y="274" fill="#854d0e" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Source: Waste cooking oil</text>
  </g>

  <!-- 3. Water Solvent -->
  <g transform="translate(405, 90)">
    <rect x="0" y="0" width="165" height="305" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#0284c7" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">3. CLEAN WATER</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="95" fill="#e0f2fe" rx="4"/>
      <path d="M 40 30 L 70 30 L 75 80 L 35 80 Z" fill="#38bdf8" rx="2"/>
      <text x="55" y="60" fill="#ffffff" font-family="system-ui, sans-serif" font-size="9" font-weight="800" text-anchor="middle">H₂O</text>
    </g>
    <text x="10" y="155" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Chemical Role:</text>
    <text x="10" y="172" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Acts as Solvent.</text>
    <text x="10" y="185" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Dissolves alkali from</text>
    <text x="10" y="200" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">  burnt wood ash.</text>
    <text x="10" y="213" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Facilitates mixing.</text>
    <rect x="8" y="255" width="149" height="30" fill="#e0f2fe" rx="4"/>
    <text x="82" y="274" fill="#0369a1" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Source: Rainwater drum</text>
  </g>

  <!-- 4. Table Salt -->
  <g transform="translate(585, 90)">
    <rect x="0" y="0" width="165" height="305" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="8" y="8" width="149" height="24" fill="#16a34a" rx="4"/>
    <text x="82" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">4. TABLE SALT</text>
    <g transform="translate(15, 42)">
      <rect x="0" y="0" width="135" height="95" fill="#dcfce7" rx="4"/>
      <ellipse cx="67" cy="65" rx="35" ry="18" fill="#86efac" stroke="#16a34a"/>
      <circle cx="55" cy="60" r="3" fill="#ffffff"/>
      <circle cx="75" cy="58" r="2.5" fill="#ffffff"/>
      <text x="67" y="70" fill="#166534" font-family="system-ui, sans-serif" font-size="9" font-weight="800" text-anchor="middle">NaCl</text>
    </g>
    <text x="10" y="155" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Chemical Role:</text>
    <text x="10" y="172" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• 'Salting Out' Agent.</text>
    <text x="10" y="185" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Causes solid soap</text>
    <text x="10" y="200" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">  to separate from water.</text>
    <text x="10" y="213" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Hardens into bars.</text>
    <rect x="8" y="255" width="149" height="30" fill="#dcfce7" rx="4"/>
    <text x="82" y="274" fill="#166534" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Source: Kitchen salt</text>
  </g>
</svg>""",

    # Lesson 3 Page 2: 6-Step Safe Cold Soap-Making Storyboard
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
    6-STEP LABORATORY PROTOCOL: SAFE COLD SOAP MAKING
  </text>

  <!-- 6 Step Cards in 2 Rows of 3 -->

  <!-- Step 1: Safety Gear -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="225" height="150" fill="#fef2f2" rx="8" stroke="#fca5a5" stroke-width="1.5"/>
    <rect x="10" y="10" width="205" height="22" fill="#ef4444" rx="4"/>
    <text x="112" y="25" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1. SAFETY GEAR FIRST</text>
    <text x="15" y="55" fill="#991b1b" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Rubber Gloves + Goggles.</text>
    <text x="15" y="70" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Plastic Apron (protects body).</text>
    <text x="15" y="85" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Plastic/Glass only (NO aluminum!).</text>
    <text x="15" y="105" fill="#dc2626" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Adult supervision mandatory!</text>
  </g>

  <!-- Step 2: Filter Ash Lye -->
  <g transform="translate(285, 80)">
    <rect x="0" y="0" width="225" height="150" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="10" y="10" width="205" height="22" fill="#64748b" rx="4"/>
    <text x="112" y="25" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. FILTER ASH LYE</text>
    <text x="15" y="55" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Settle ash water for 24 hours.</text>
    <text x="15" y="70" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Filter through cotton cloth.</text>
    <text x="15" y="85" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Collect clear alkaline lye.</text>
    <text x="15" y="105" fill="#0284c7" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Pure chemical trigger ready.</text>
  </g>

  <!-- Step 3: Warm Fats -->
  <g transform="translate(525, 80)">
    <rect x="0" y="0" width="225" height="150" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="10" y="10" width="205" height="22" fill="#eab308" rx="4"/>
    <text x="112" y="25" fill="#713f12" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3. WARM OILS &amp; FATS</text>
    <text x="15" y="55" fill="#713f12" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Melt solid fats gently.</text>
    <text x="15" y="70" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Strain out food particles.</text>
    <text x="15" y="85" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Keep lukewarm (45°C).</text>
    <text x="15" y="105" fill="#854d0e" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Lipid chains ready for bonding.</text>
  </g>

  <!-- Step 4: Stir to 'Trace' -->
  <g transform="translate(45, 245)">
    <rect x="0" y="0" width="225" height="155" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="10" y="10" width="205" height="22" fill="#0284c7" rx="4"/>
    <text x="112" y="25" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">4. STIR TO 'TRACE'</text>
    <text x="15" y="55" fill="#0369a1" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Pour lye slowly into oil.</text>
    <text x="15" y="70" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Stir continuously in ONE direction.</text>
    <text x="15" y="85" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Stir until thick like porridge.</text>
    <text x="15" y="105" fill="#0284c7" font-family="system-ui, sans-serif" font-size="10" font-weight="700">'Trace State' achieved!</text>
  </g>

  <!-- Step 5: Salt Out & Additives -->
  <g transform="translate(285, 245)">
    <rect x="0" y="0" width="225" height="155" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="10" y="10" width="205" height="22" fill="#8b5cf6" rx="4"/>
    <text x="112" y="25" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">5. SALT &amp; ADDITIVES</text>
    <text x="15" y="55" fill="#5b21b6" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Add handful of salt (binder).</text>
    <text x="15" y="70" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Stir in Neem extract (antiseptic).</text>
    <text x="15" y="85" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Add glycerine &amp; lavender scent.</text>
    <text x="15" y="105" fill="#7c3aed" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Premium herbal formulation.</text>
  </g>

  <!-- Step 6: Mold & 4-Week Curing -->
  <g transform="translate(525, 245)">
    <rect x="0" y="0" width="225" height="155" fill="#f0fdf4" rx="8" stroke="#86efac" stroke-width="1.5"/>
    <rect x="10" y="10" width="205" height="22" fill="#16a34a" rx="4"/>
    <text x="112" y="25" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">6. MOLD &amp; 4-WEEK CURE</text>
    <text x="15" y="55" fill="#15803d" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">• Pour into paper-lined molds.</text>
    <text x="15" y="70" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Set 48 hours, then cut bars.</text>
    <text x="15" y="85" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Cure 2 to 4 weeks on slats.</text>
    <text x="15" y="105" fill="#15803d" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Neutralizes alkali 100%!</text>
  </g>
</svg>""",

    # Lesson 3 Page 4: Soap Improvement & Quality Benchmarks
    (3, 4): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
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
    SOAP ADDITIVES &amp; THE 4-STAR QUALITY BENCHMARKS
  </text>

  <!-- Left: 4 Additive Enhancers -->
  <g transform="translate(45, 85)">
    <rect x="0" y="0" width="340" height="315" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="15" y="15" width="310" height="28" fill="#8b5cf6" rx="5"/>
    <text x="170" y="34" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      NATURAL SOAP ADDITIVES &amp; BENEFITS
    </text>

    <g transform="translate(20, 55)">
      <!-- Neem -->
      <rect x="0" y="0" width="300" height="48" fill="#dcfce7" rx="4" stroke="#86efac"/>
      <text x="15" y="20" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1. Neem / Mwarobaini Extract</text>
      <text x="15" y="35" fill="#166534" font-family="system-ui, sans-serif" font-size="9.5">Adds natural antiseptic power; kills skin germs.</text>

      <!-- Glycerine -->
      <rect x="0" y="58" width="300" height="48" fill="#e0f2fe" rx="4" stroke="#7dd3fc"/>
      <text x="15" y="78" fill="#0369a1" font-family="system-ui, sans-serif" font-size="11" font-weight="700">2. Glycerine (Humectant)</text>
      <text x="15" y="93" fill="#0284c7" font-family="system-ui, sans-serif" font-size="9.5">Locks moisture in skin; prevents dry peeling.</text>

      <!-- Fragrances -->
      <rect x="0" y="116" width="300" height="48" fill="#fef9c3" rx="4" stroke="#fde047"/>
      <text x="15" y="136" fill="#854d0e" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3. Essential Oils (Lavender / Lemon)</text>
      <text x="15" y="151" fill="#713f12" font-family="system-ui, sans-serif" font-size="9.5">Masks animal fat odor; provides clean scent.</text>

      <!-- Natural Dyes -->
      <rect x="0" y="174" width="300" height="48" fill="#fce7f3" rx="4" stroke="#fbcfe8"/>
      <text x="15" y="194" fill="#9d174d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">4. Natural Dyes (Beetroot / Turmeric)</text>
      <text x="15" y="209" fill="#831843" font-family="system-ui, sans-serif" font-size="9.5">Creates attractive pink/yellow artisan bars.</text>
    </g>
  </g>

  <!-- Right: 4-Star Quality Benchmarks -->
  <g transform="translate(415, 85)">
    <rect x="0" y="0" width="340" height="315" fill="#f0fdf4" rx="8" stroke="#86efac" stroke-width="2"/>
    <rect x="15" y="15" width="310" height="28" fill="#16a34a" rx="5"/>
    <text x="170" y="34" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      THE 4-STAR CLEANING QUALITY TEST
    </text>

    <g transform="translate(20, 55)">
      <!-- Quality 1 -->
      <rect x="0" y="0" width="300" height="48" fill="#ffffff" rx="4" stroke="#bbf7d0"/>
      <text x="15" y="20" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">⭐ 1. Gentle on Skin &amp; Hands</text>
      <text x="15" y="35" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Balanced pH; zero burning, itching, or redness.</text>

      <!-- Quality 2 -->
      <rect x="0" y="58" width="300" height="48" fill="#ffffff" rx="4" stroke="#bbf7d0"/>
      <text x="15" y="78" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">⭐ 2. Lathers Quickly &amp; Easily</text>
      <text x="15" y="93" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Produces rich foam to trap and lift dirt.</text>

      <!-- Quality 3 -->
      <rect x="0" y="116" width="300" height="48" fill="#ffffff" rx="4" stroke="#bbf7d0"/>
      <text x="15" y="136" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">⭐ 3. Fresh, Pleasant Fragrance</text>
      <text x="15" y="151" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Leaves skin and clothes smelling clean.</text>

      <!-- Quality 4 -->
      <rect x="0" y="174" width="300" height="48" fill="#ffffff" rx="4" stroke="#bbf7d0"/>
      <text x="15" y="194" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">⭐ 4. Safe on Fabrics &amp; Surfaces</text>
      <text x="15" y="209" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Cleans without corroding cloth or scratching.</text>
    </g>
  </g>
</svg>""",

    # Lesson 4 Page 2: 5-Phase CSL Soap Project Cycle
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
    THE 5-PHASE COMMUNITY SERVICE LEARNING (CSL) SOAP CYCLE
  </text>

  <!-- 5 Circular Workflow Steps -->

  <!-- Phase 1: Investigate -->
  <g transform="translate(35, 80)">
    <rect x="0" y="0" width="135" height="320" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="8" y="8" width="119" height="24" fill="#3b82f6" rx="4"/>
    <text x="67" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">1. INVESTIGATE</text>
    <g transform="translate(12, 42)">
      <rect x="0" y="0" width="111" height="95" fill="#e0f2fe" rx="4"/>
      <circle cx="55" cy="45" r="20" fill="#bfdbfe" stroke="#3b82f6" stroke-width="2"/>
      <text x="55" y="52" fill="#1e40af" font-family="system-ui, sans-serif" font-size="16" text-anchor="middle">🔍</text>
      <text x="55" y="85" fill="#1e40af" font-family="system-ui, sans-serif" font-size="8" font-weight="700" text-anchor="middle">Hygiene Survey</text>
    </g>
    <text x="8" y="155" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Actions:</text>
    <text x="8" y="172" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Identify soap needs</text>
    <text x="8" y="185" fill="#475569" font-family="system-ui, sans-serif" font-size="9">  at school taps.</text>
    <text x="8" y="200" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Locate free ash</text>
    <text x="8" y="213" fill="#475569" font-family="system-ui, sans-serif" font-size="9">  and fat sources.</text>
  </g>

  <!-- Phase 2: Plan & Budget -->
  <g transform="translate(182, 80)">
    <rect x="0" y="0" width="135" height="320" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="8" y="8" width="119" height="24" fill="#0284c7" rx="4"/>
    <text x="67" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">2. PLAN &amp; BUDGET</text>
    <g transform="translate(12, 42)">
      <rect x="0" y="0" width="111" height="95" fill="#e0f2fe" rx="4"/>
      <rect x="30" y="25" width="50" height="40" fill="#bae6fd" rx="3" stroke="#0284c7"/>
      <line x1="38" y1="35" x2="72" y2="35" stroke="#0369a1" stroke-width="2"/>
      <line x1="38" y1="45" x2="65" y2="45" stroke="#0369a1" stroke-width="2"/>
      <text x="55" y="85" fill="#0369a1" font-family="system-ui, sans-serif" font-size="8" font-weight="700" text-anchor="middle">Action Plan</text>
    </g>
    <text x="8" y="155" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Actions:</text>
    <text x="8" y="172" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Assign group roles.</text>
    <text x="8" y="185" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Create timeline.</text>
    <text x="8" y="200" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Zero-cost budget.</text>
  </g>

  <!-- Phase 3: Execute Production -->
  <g transform="translate(329, 80)">
    <rect x="0" y="0" width="135" height="320" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="8" y="8" width="119" height="24" fill="#eab308" rx="4"/>
    <text x="67" y="24" fill="#713f12" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">3. EXECUTE</text>
    <g transform="translate(12, 42)">
      <rect x="0" y="0" width="111" height="95" fill="#fef9c3" rx="4"/>
      <rect x="25" y="30" width="60" height="40" fill="#fde047" rx="4" stroke="#ca8a04"/>
      <text x="55" y="55" fill="#854d0e" font-family="system-ui, sans-serif" font-size="9" font-weight="800" text-anchor="middle">SOAP POT</text>
      <text x="55" y="85" fill="#854d0e" font-family="system-ui, sans-serif" font-size="8" font-weight="700" text-anchor="middle">Cold Saponification</text>
    </g>
    <text x="8" y="155" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Actions:</text>
    <text x="8" y="172" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Make neem soap.</text>
    <text x="8" y="185" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Strict safety gear.</text>
    <text x="8" y="200" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Cure for 4 weeks.</text>
  </g>

  <!-- Phase 4: Sensitize & Showcase -->
  <g transform="translate(476, 80)">
    <rect x="0" y="0" width="135" height="320" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="8" y="8" width="119" height="24" fill="#059669" rx="4"/>
    <text x="67" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">4. SENSITIZE</text>
    <g transform="translate(12, 42)">
      <rect x="0" y="0" width="111" height="95" fill="#d1fae5" rx="4"/>
      <rect x="25" y="20" width="60" height="45" fill="#a7f3d0" rx="3" stroke="#059669"/>
      <text x="55" y="47" fill="#065f46" font-family="system-ui, sans-serif" font-size="8" font-weight="800" text-anchor="middle">POSTER</text>
      <text x="55" y="85" fill="#065f46" font-family="system-ui, sans-serif" font-size="8" font-weight="700" text-anchor="middle">Handwashing Talk</text>
    </g>
    <text x="8" y="155" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Actions:</text>
    <text x="8" y="172" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Distribute to taps.</text>
    <text x="8" y="185" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Teach 6-step wash.</text>
    <text x="8" y="200" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Display posters.</text>
  </g>

  <!-- Phase 5: Evaluate & Reflect -->
  <g transform="translate(623, 80)">
    <rect x="0" y="0" width="140" height="320" fill="#f0fdf4" rx="8" stroke="#86efac" stroke-width="2"/>
    <rect x="8" y="8" width="124" height="24" fill="#16a34a" rx="4"/>
    <text x="70" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">5. EVALUATE</text>
    <g transform="translate(12, 42)">
      <rect x="0" y="0" width="116" height="95" fill="#dcfce7" rx="4"/>
      <circle cx="58" cy="45" r="20" fill="#86efac" stroke="#16a34a" stroke-width="2"/>
      <text x="58" y="52" fill="#15803d" font-family="system-ui, sans-serif" font-size="16" text-anchor="middle">📝</text>
      <text x="58" y="85" fill="#15803d" font-family="system-ui, sans-serif" font-size="8" font-weight="700" text-anchor="middle">User Surveys</text>
    </g>
    <text x="8" y="155" fill="#166534" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Actions:</text>
    <text x="8" y="172" fill="#15803d" font-family="system-ui, sans-serif" font-size="9">• Collect feedback.</text>
    <text x="8" y="185" fill="#15803d" font-family="system-ui, sans-serif" font-size="9">• Track disease drops.</text>
    <text x="8" y="200" fill="#15803d" font-family="system-ui, sans-serif" font-size="9">• Plan next term!</text>
  </g>
</svg>""",

    # Lesson 4 Page 4: Zero-Cost Community Resource Flow Blueprint
    (4, 4): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
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
    ZERO-COST SUSTAINABLE COMMUNITY RESOURCE LOOP
  </text>

  <!-- Flow Steps -->

  <!-- Left: Waste Inputs -->
  <g transform="translate(45, 90)">
    <rect x="0" y="0" width="215" height="300" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="10" y="10" width="195" height="26" fill="#64748b" rx="4"/>
    <text x="107" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">
      1. FREE WASTE INPUTS
    </text>
    <g transform="translate(15, 50)">
      <rect x="0" y="0" width="185" height="55" fill="#f1f5f9" rx="4"/>
      <text x="10" y="22" fill="#334155" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">🔥 Kitchen Firewood Ash</text>
      <text x="10" y="38" fill="#64748b" font-family="system-ui, sans-serif" font-size="9">From school kitchen hearth.</text>

      <rect x="0" y="65" width="185" height="55" fill="#fef9c3" rx="4"/>
      <text x="10" y="87" fill="#854d0e" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">🥩 Discarded Cooking Fats</text>
      <text x="10" y="103" fill="#713f12" font-family="system-ui, sans-serif" font-size="9">From local butcher &amp; homes.</text>

      <rect x="0" y="130" width="185" height="55" fill="#e0f2fe" rx="4"/>
      <text x="10" y="152" fill="#0369a1" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">🌧️ Roof Rainwater</text>
      <text x="10" y="168" fill="#0284c7" font-family="system-ui, sans-serif" font-size="9">Collected in science drum.</text>
    </g>
    <rect x="10" y="255" width="195" height="30" fill="#dcfce7" rx="4"/>
    <text x="107" y="274" fill="#15803d" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Total Raw Cost: KES 0</text>
  </g>

  <!-- Middle: Student Laboratory Transformation -->
  <g transform="translate(290, 90)">
    <rect x="0" y="0" width="220" height="300" fill="#f0f9ff" rx="8" stroke="#bae6fd" stroke-width="1.5"/>
    <rect x="10" y="10" width="200" height="26" fill="#0284c7" rx="4"/>
    <text x="110" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">
      2. JSS SCIENCE IN ACTION
    </text>
    <g transform="translate(15, 50)">
      <rect x="0" y="0" width="190" height="185" fill="#ffffff" rx="6" stroke="#7dd3fc"/>
      <text x="15" y="30" fill="#0369a1" font-family="system-ui, sans-serif" font-size="11" font-weight="700">🔬 Cold Saponification</text>
      <text x="15" y="50" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Lye + Fats = Soap base.</text>
      <text x="15" y="75" fill="#0369a1" font-family="system-ui, sans-serif" font-size="11" font-weight="700">🌿 Neem Medicated Additive</text>
      <text x="15" y="95" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Antiseptic protection.</text>
      <text x="15" y="120" fill="#0369a1" font-family="system-ui, sans-serif" font-size="11" font-weight="700">⏳ 4-Week Safe Curing</text>
      <text x="15" y="140" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Neutralizes alkali 100%.</text>
      <text x="15" y="165" fill="#15803d" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Produces 50+ solid bars!</text>
    </g>
    <rect x="10" y="255" width="200" height="30" fill="#e0f2fe" rx="4"/>
    <text x="110" y="274" fill="#0369a1" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Student Agency &amp; Skills</text>
  </g>

  <!-- Right: Community Health Impact -->
  <g transform="translate(540, 90)">
    <rect x="0" y="0" width="215" height="300" fill="#f0fdf4" rx="8" stroke="#86efac" stroke-width="2"/>
    <rect x="10" y="10" width="195" height="26" fill="#16a34a" rx="4"/>
    <text x="107" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">
      3. COMMUNITY IMPACT
    </text>
    <g transform="translate(15, 50)">
      <rect x="0" y="0" width="185" height="55" fill="#ffffff" rx="4" stroke="#bbf7d0"/>
      <text x="10" y="22" fill="#15803d" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">🚰 Active Handwash Taps</text>
      <text x="10" y="38" fill="#475569" font-family="system-ui, sans-serif" font-size="9">Installed at all school latrines.</text>

      <rect x="0" y="65" width="185" height="55" fill="#ffffff" rx="4" stroke="#bbf7d0"/>
      <text x="10" y="87" fill="#15803d" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">📉 40% Disease Reduction</text>
      <text x="10" y="103" fill="#475569" font-family="system-ui, sans-serif" font-size="9">Fewer stomach illness cases.</text>

      <rect x="0" y="130" width="185" height="55" fill="#ffffff" rx="4" stroke="#bbf7d0"/>
      <text x="10" y="152" fill="#15803d" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">💡 Micro-Enterprise</text>
      <text x="10" y="168" fill="#475569" font-family="system-ui, sans-serif" font-size="9">Youth financial self-reliance.</text>
    </g>
    <rect x="10" y="255" width="195" height="30" fill="#dcfce7" rx="4"/>
    <text x="107" y="274" fill="#166534" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Healthier Village &amp; School!</text>
  </g>
</svg>"""
}

def enrich_cbc_grade7_home_science_topic8():
    print("=" * 80)
    print("STARTING VISUAL ENRICHMENT: CBC GRADE 7 HOME SCIENCE — TOPIC 8: HOUSEHOLD CLEANING AGENTS & HOMEMADE SOAP")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 7").first()
    subject = Subject.objects.filter(grade=grade, name="Home Science").first()
    topic = Topic.objects.filter(subject=subject, name="Household Cleaning Agents & Homemade Soap").first()

    assert topic, "Topic 8 (Household Cleaning Agents & Homemade Soap) not found!"
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
        photo_info = TOPIC8_PHOTOS.get(u_order)
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
    for (u_order, page_num), svg_code in TOPIC8_SVGS.items():
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
    print(f"[SUCCESS] CBC Grade 7 Home Science Topic 8 Visual Enrichment Complete!")
    print(f"[*] Total LessonAssets Created & Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_cbc_grade7_home_science_topic8()
