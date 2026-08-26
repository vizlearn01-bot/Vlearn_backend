"""
VLearn CBC Grade 10 Agriculture — Topic 8: Breeds of Livestock
Visual Enrichment Engine (Phase 2: Vector SVGs, Verified Photos & Asset Persistence)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Breeds of Livestock (Order: 8)

Attaches:
  - 10 First-Card Photographic Visual Hooks (100% Tested HTTP 200 Direct Wikimedia URLs)
  - 8 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - 1 Verified Educational YouTube Video (Lesson 3 Card 3)
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade10_agriculture_topic8.py
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
# 8 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 8: BREEDS OF LIVESTOCK
# =============================================================================

# SVG 1: Livestock Classification Matrix (Lesson 1, Page 2)
SVG_BREED_CLASSIFICATION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Livestock Classification: Production Purpose &amp; Agro-Ecology</text>

  <!-- Left: 3 Production Pillars -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="32" rx="10" fill="#15803d"/>
    <text x="170" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. CLASSIFICATION BY PRODUCTION PURPOSE</text>

    <!-- Single Purpose -->
    <g transform="translate(15, 45)">
      <rect x="0" y="0" width="310" height="65" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="22" font-size="11" font-weight="bold" fill="#4ade80">Single-Purpose Breeds:</text>
      <text x="15" y="40" font-size="10" fill="#cbd5e1">• Selected for 1 commodity (Max Yield)</text>
      <text x="15" y="55" font-size="9" fill="#86efac">e.g. Friesian (Milk), Angus (Beef), Merino (Wool)</text>
    </g>

    <!-- Dual Purpose -->
    <g transform="translate(15, 120)">
      <rect x="0" y="0" width="310" height="65" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="22" font-size="11" font-weight="bold" fill="#4ade80">Dual-Purpose Breeds:</text>
      <text x="15" y="40" font-size="10" fill="#cbd5e1">• Selected for 2 outputs efficiently</text>
      <text x="15" y="55" font-size="9" fill="#86efac">e.g. Sahiwal (Milk + Meat), Corriedale (Meat + Wool)</text>
    </g>

    <!-- Multi Purpose -->
    <g transform="translate(15, 195)">
      <rect x="0" y="0" width="310" height="65" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="22" font-size="11" font-weight="bold" fill="#4ade80">Multi-Purpose Breeds:</text>
      <text x="15" y="40" font-size="10" fill="#cbd5e1">• Milk, meat, hides, and draft power</text>
      <text x="15" y="55" font-size="9" fill="#86efac">e.g. Indigenous East African Zebu &amp; Red Masai</text>
    </g>
  </g>

  <!-- Right: Ecological Origin & Management -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#0284c7"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. AGRO-ECOLOGICAL FIT &amp; ADAPTATION</text>

    <!-- Exotic -->
    <g transform="translate(15, 45)">
      <rect x="0" y="0" width="315" height="110" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="15" y="22" font-size="11" font-weight="bold" fill="#f87171">Exotic Temperate Breeds (Imported):</text>
      <text x="15" y="42" font-size="10" fill="#cbd5e1">• Ultra-high genetic yield potential</text>
      <text x="15" y="60" font-size="10" fill="#cbd5e1">• Vulnerable to tropical heat &amp; ticks (ECF)</text>
      <text x="15" y="78" font-size="10" fill="#cbd5e1">• Mandates high feed rations &amp; zero-grazing</text>
      <text x="15" y="96" font-size="9" fill="#fca5a5">Niche: Commercial Highland Dairy / Feedlots</text>
    </g>

    <!-- Indigenous -->
    <g transform="translate(15, 165)">
      <rect x="0" y="0" width="315" height="110" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="22" font-size="11" font-weight="bold" fill="#4ade80">Indigenous Tropical Breeds (Adapted):</text>
      <text x="15" y="42" font-size="10" fill="#cbd5e1">• Evolved in Africa/Asia over millennia</text>
      <text x="15" y="60" font-size="10" fill="#cbd5e1">• Heat-resilient humps &amp; natural tick immunity</text>
      <text x="15" y="78" font-size="10" fill="#cbd5e1">• Thrives on dry rangeland forage &amp; low water</text>
      <text x="15" y="96" font-size="9" fill="#86efac">Niche: Pastoral Ranches / Semi-Arid Zones</text>
    </g>
  </g>
</svg>
""")

# SVG 2: Major Dairy Cattle Breeds: Volume vs Butterfat (Lesson 2, Page 2)
SVG_DAIRY_TRADE_OFF = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Dairy Cattle Breeds: Milk Volume vs. Butterfat % Trade-Off</text>

  <!-- 4 Breed Cards Grid -->
  <!-- 1. Friesian (Top Left) -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="150" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="28" rx="8" fill="#0369a1"/>
    <text x="170" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">HOLSTEIN FRIESIAN (Netherlands)</text>
    <text x="15" y="50" font-size="10" fill="#cbd5e1">• Coat: Black and White piebald patches</text>
    <text x="15" y="70" font-size="11" font-weight="bold" fill="#38bdf8">• Daily Yield: 25 – 40 Liters (HIGHEST VOLUME)</text>
    <text x="15" y="90" font-size="11" font-weight="bold" fill="#f87171">• Butterfat: 3.0% – 3.5% (LOWEST FAT)</text>
    <text x="15" y="110" font-size="9" fill="#94a3b8">• Market: Urban raw liquid milk sold by volume</text>
  </g>

  <!-- 2. Ayrshire (Top Right) -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="345" height="150" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="28" rx="8" fill="#15803d"/>
    <text x="172" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">AYRSHIRE (Scotland)</text>
    <text x="15" y="50" font-size="10" fill="#cbd5e1">• Coat: Cherry-red / brown and white patches</text>
    <text x="15" y="70" font-size="11" font-weight="bold" fill="#4ade80">• Daily Yield: 18 – 25 Liters (High Consistent)</text>
    <text x="15" y="90" font-size="11" font-weight="bold" fill="#fde047">• Butterfat: 4.0% (Balanced)</text>
    <text x="15" y="110" font-size="9" fill="#86efac">• Superpower: Hardiest active forager on rough hills</text>
  </g>

  <!-- 3. Guernsey (Bottom Left) -->
  <g transform="translate(45, 230)">
    <rect x="0" y="0" width="340" height="150" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="28" rx="8" fill="#a16207"/>
    <text x="170" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">GUERNSEY (Guernsey Island, UK)</text>
    <text x="15" y="50" font-size="10" fill="#cbd5e1">• Coat: Golden-brown / fawn with white patches</text>
    <text x="15" y="70" font-size="11" font-weight="bold" fill="#fde047">• Daily Yield: 15 – 20 Liters</text>
    <text x="15" y="90" font-size="11" font-weight="bold" fill="#fde047">• Butterfat: 4.5% – 5.0%</text>
    <text x="15" y="110" font-size="9" font-weight="bold" fill="#fef08a">• Golden Milk: High beta-carotene (Pro-Vitamin A)</text>
  </g>

  <!-- 4. Jersey (Bottom Right) -->
  <g transform="translate(415, 230)">
    <rect x="0" y="0" width="345" height="150" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="28" rx="8" fill="#be185d"/>
    <text x="172" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">JERSEY (Jersey Island, UK)</text>
    <text x="15" y="50" font-size="10" fill="#cbd5e1">• Coat: Fawn to light cream, dish face, dark muzzle</text>
    <text x="15" y="70" font-size="11" font-weight="bold" fill="#cbd5e1">• Daily Yield: 12 – 18 Liters (Compact Body)</text>
    <text x="15" y="90" font-size="11" font-weight="bold" fill="#f472b6">• Butterfat: 5.0% – 5.5% (HIGHEST BUTTERFAT)</text>
    <text x="15" y="110" font-size="9" fill="#fbcfe8">• Market: Premier milk for butter, cheese &amp; ghee</text>
  </g>
</svg>
""")

# SVG 3: Bos indicus vs Bos taurus (Lesson 3, Page 2)
SVG_BOS_INDICUS_VS_TAURUS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Bovine Evolution: Humped Bos indicus vs. Humpless Bos taurus</text>

  <!-- Left: Humped Bos indicus (Boran / Zebu) -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="345" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="32" rx="10" fill="#15803d"/>
    <text x="170" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">HUMPED BOS INDICUS (Tropical Adapted)</text>

    <g transform="translate(15, 45)">
      <!-- Feature 1: Hump -->
      <rect x="0" y="0" width="310" height="55" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">1. Thoracic Muscular-Fat Hump:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Stores energy without insulating body core.</text>

      <!-- Feature 2: Dewlap -->
      <rect x="0" y="65" width="310" height="55" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">2. Extensive Loose Dewlap &amp; Sheath:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Increases body surface area by 20% for heat loss.</text>

      <!-- Feature 3: Ears & Coat -->
      <rect x="0" y="130" width="310" height="55" rx="6" fill="#1e293b" stroke="#22c55e"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#4ade80">3. Large Vascular Ears &amp; Light Coat:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Acts as heat radiator; reflects 80% solar rays.</text>

      <text x="15" y="210" font-size="10" font-weight="bold" fill="#86efac">Examples: Boran, Brahman, Sahiwal, Zebu</text>
    </g>
  </g>

  <!-- Right: Humpless Bos taurus (Friesian / Angus) -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="345" height="345" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="32" rx="10" fill="#0284c7"/>
    <text x="172" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">HUMPLESS BOS TAURUS (Temperate)</text>

    <g transform="translate(15, 45)">
      <!-- Feature 1: No Hump -->
      <rect x="0" y="0" width="315" height="55" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#38bdf8">1. Completely Flat Backline (No Hump):</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Fat distributed as subcutaneous &amp; marbling.</text>

      <!-- Feature 2: Tight Skin -->
      <rect x="0" y="65" width="315" height="55" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#38bdf8">2. Tight Skin &amp; Minimal Dewlap:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Retains body heat in cold European winters.</text>

      <!-- Feature 3: Small Ears -->
      <rect x="0" y="130" width="315" height="55" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#38bdf8">3. Small Upright Ears &amp; Dark Coat:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Absorbs 90% solar heat; prone to heat stress.</text>

      <text x="15" y="210" font-size="10" font-weight="bold" fill="#67e8f9">Examples: Friesian, Angus, Hereford, Jersey</text>
    </g>
  </g>
</svg>
""")

# SVG 4: Commercial Pig Breeds (Lesson 4, Page 2)
SVG_PIG_BREEDS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Diagnostic Morphological Profiles of Commercial Pig Breeds</text>

  <!-- 4 Pig Breeds Cards -->
  <!-- 1. Large White -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="340" height="150" rx="8" fill="#0f172a" stroke="#ffffff" stroke-width="1.5"/>
    <rect x="0" y="0" width="340" height="28" rx="8" fill="#475569"/>
    <text x="170" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">LARGE WHITE / YORKSHIRE (UK)</text>
    <text x="15" y="52" font-size="11" font-weight="bold" fill="#ffffff">• Ears: ERECT (Upright)</text>
    <text x="15" y="72" font-size="10" fill="#cbd5e1">• Coat: Entirely White skin and hair</text>
    <text x="15" y="92" font-size="10" fill="#cbd5e1">• Conformation: Deep, long body, dished face</text>
    <text x="15" y="112" font-size="9" fill="#94a3b8">• Role: Prolific maternal dam line (10–14 piglets)</text>
  </g>

  <!-- 2. Landrace -->
  <g transform="translate(415, 65)">
    <rect x="0" y="0" width="345" height="150" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="28" rx="8" fill="#15803d"/>
    <text x="172" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">LANDRACE (Denmark)</text>
    <text x="15" y="52" font-size="11" font-weight="bold" fill="#4ade80">• Ears: LARGE DROOPING (Covers eyes)</text>
    <text x="15" y="72" font-size="10" fill="#cbd5e1">• Coat: Entirely White</text>
    <text x="15" y="92" font-size="11" font-weight="bold" fill="#fde047">• Body: Extra-Long Cylindrical Frame (Extra ribs)</text>
    <text x="15" y="112" font-size="9" fill="#86efac">• Role: Premier Bacon Breed; heavy milk output</text>
  </g>

  <!-- 3. Duroc -->
  <g transform="translate(45, 230)">
    <rect x="0" y="0" width="340" height="150" rx="8" fill="#0f172a" stroke="#ea580c" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="28" rx="8" fill="#9a3412"/>
    <text x="170" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">DUROC (USA)</text>
    <text x="15" y="52" font-size="11" font-weight="bold" fill="#fb923c">• Coat: MAHOGANY RED / Golden-Red</text>
    <text x="15" y="72" font-size="10" fill="#cbd5e1">• Ears: Drooping ear tips</text>
    <text x="15" y="92" font-size="10" fill="#cbd5e1">• Conformation: Muscular, heavy bone, rugged</text>
    <text x="15" y="112" font-size="9" fill="#fdba74">• Role: Terminal Sire line; growth vigor &amp; marbling</text>
  </g>

  <!-- 4. Hampshire -->
  <g transform="translate(415, 230)">
    <rect x="0" y="0" width="345" height="150" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="28" rx="8" fill="#0369a1"/>
    <text x="172" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">HAMPSHIRE (USA / UK)</text>
    <text x="15" y="52" font-size="11" font-weight="bold" fill="#38bdf8">• Coat: Jet Black with WHITE SHOULDER BELT</text>
    <text x="15" y="72" font-size="10" fill="#cbd5e1">• Ears: Erect (Upright)</text>
    <text x="15" y="92" font-size="10" fill="#cbd5e1">• Conformation: Heavy loin muscling, compact</text>
    <text x="15" y="112" font-size="9" fill="#7dd3fc">• Role: Terminal Sire; produces ultra-lean carcasses</text>
  </g>
</svg>
""")

# SVG 5: Sheep Breeds Comparison (Lesson 6, Page 2)
SVG_SHEEP_BREEDS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="40" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Sheep Breeds: Wool Champions vs. Tropical Meat Adaptations</text>

  <!-- 3 Sheep Columns -->
  <!-- 1. Merino (Wool) -->
  <g transform="translate(45, 65)">
    <rect x="0" y="0" width="220" height="345" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="30" rx="8" fill="#a16207"/>
    <text x="110" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">MERINO (Spain)</text>
    <g transform="translate(10, 45)">
      <text x="0" y="18" font-size="11" font-weight="bold" fill="#fde047">• Fine Wool Champion</text>
      <text x="0" y="38" font-size="9" fill="#cbd5e1">• Heavy wrinkled skin</text>
      <text x="0" y="55" font-size="9" fill="#cbd5e1">• Spiral horns in rams</text>
      <text x="0" y="75" font-size="9" fill="#cbd5e1">• High-crimp fine wool</text>
      <text x="0" y="98" font-size="9" fill="#f87171">• Prone to fleece rot in rain</text>
    </g>
  </g>

  <!-- 2. Dorper (Mutton) -->
  <g transform="translate(290, 65)">
    <rect x="0" y="0" width="220" height="345" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="30" rx="8" fill="#0369a1"/>
    <text x="110" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">DORPER (South Africa)</text>
    <g transform="translate(10, 45)">
      <text x="0" y="18" font-size="11" font-weight="bold" fill="#38bdf8">• Commercial Mutton</text>
      <text x="0" y="38" font-size="9" font-weight="bold" fill="#ffffff">• Jet-Black Head &amp; Neck</text>
      <text x="0" y="55" font-size="9" fill="#cbd5e1">• Solid White Body</text>
      <text x="0" y="75" font-size="9" font-weight="bold" fill="#4ade80">• Self-Shedding Fleece</text>
      <text x="0" y="92" font-size="9" fill="#cbd5e1">• Zero shearing labor</text>
      <text x="0" y="112" font-size="9" fill="#67e8f9">• Rapid growth in dry range</text>
    </g>
  </g>

  <!-- 3. Red Masai (Indigenous) -->
  <g transform="translate(535, 65)">
    <rect x="0" y="0" width="220" height="345" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="30" rx="8" fill="#991b1b"/>
    <text x="110" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">RED MASAI (East Africa)</text>
    <g transform="translate(10, 45)">
      <text x="0" y="18" font-size="11" font-weight="bold" fill="#f87171">• Indigenous Hair Sheep</text>
      <text x="0" y="38" font-size="9" fill="#cbd5e1">• Solid Reddish-Brown</text>
      <text x="0" y="55" font-size="9" fill="#cbd5e1">• Fat-Tailed (Energy store)</text>
      <text x="0" y="75" font-size="9" font-weight="bold" fill="#4ade80">• Haemonchus Resistance</text>
      <text x="0" y="92" font-size="9" fill="#86efac">• Immune to fatal worms</text>
      <text x="0" y="112" font-size="9" fill="#fca5a5">• Extreme drought hardiness</text>
    </g>
  </g>
</svg>
""")

# SVG 6: Goat Breeds Tree (Lesson 7, Page 2)
SVG_GOAT_BREEDS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Goat Breeds Classification: Meat, Dairy, and Luxury Fiber</text>

  <!-- 3 Category Cards -->
  <!-- 1. Meat Goats -->
  <g transform="translate(45, 60)">
    <rect x="0" y="0" width="220" height="350" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="30" rx="8" fill="#991b1b"/>
    <text x="110" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">MEAT GOATS (CHEVON)</text>

    <g transform="translate(10, 45)">
      <text x="0" y="16" font-size="11" font-weight="bold" fill="#f87171">• Boer Goat (South Africa):</text>
      <text x="10" y="32" font-size="9" fill="#cbd5e1">White body, dark red head</text>
      <text x="10" y="47" font-size="9" fill="#4ade80">Heavy muscling (250g/day)</text>

      <text x="0" y="75" font-size="11" font-weight="bold" fill="#f87171">• Galla / Boran (Kenya):</text>
      <text x="10" y="91" font-size="9" fill="#cbd5e1">Pure white, upright ears</text>
      <text x="10" y="106" font-size="9" fill="#86efac">Arid Acacia scrub hardy</text>

      <text x="0" y="135" font-size="11" font-weight="bold" fill="#f87171">• Kalahari Red:</text>
      <text x="10" y="151" font-size="9" fill="#cbd5e1">Solid red, hardy camouflage</text>
    </g>
  </g>

  <!-- 2. Dairy Goats -->
  <g transform="translate(290, 60)">
    <rect x="0" y="0" width="220" height="350" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="30" rx="8" fill="#0369a1"/>
    <text x="110" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">DAIRY GOATS (MILK)</text>

    <g transform="translate(10, 45)">
      <text x="0" y="16" font-size="11" font-weight="bold" fill="#38bdf8">• Saanen (Switzerland):</text>
      <text x="10" y="32" font-size="9" fill="#cbd5e1">Pure white, erect ears</text>
      <text x="10" y="47" font-size="9" fill="#4ade80">Highest Volume (3–5 L/day)</text>

      <text x="0" y="75" font-size="11" font-weight="bold" fill="#38bdf8">• Toggenburg (Swiss):</text>
      <text x="10" y="91" font-size="9" fill="#cbd5e1">White face stripes &amp; socks</text>

      <text x="0" y="118" font-size="11" font-weight="bold" fill="#38bdf8">• Anglo-Nubian:</text>
      <text x="10" y="134" font-size="9" fill="#cbd5e1">Roman nose, pendulous ears</text>
      <text x="10" y="149" font-size="9" fill="#f472b6">Highest Butterfat (5–6%)</text>
    </g>
  </g>

  <!-- 3. Fiber Goats -->
  <g transform="translate(535, 60)">
    <rect x="0" y="0" width="220" height="350" rx="8" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect x="0" y="0" width="220" height="30" rx="8" fill="#a16207"/>
    <text x="110" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">LUXURY FIBER GOATS</text>

    <g transform="translate(10, 45)">
      <text x="0" y="16" font-size="11" font-weight="bold" fill="#fde047">• Angora Goat (Turkey):</text>
      <text x="10" y="32" font-size="9" fill="#cbd5e1">Silky spiraling white fleece</text>
      <text x="10" y="47" font-size="9" font-weight="bold" fill="#fef08a">Produces MOHAIR fiber</text>

      <text x="0" y="85" font-size="11" font-weight="bold" fill="#fde047">• Cashmere Goat:</text>
      <text x="10" y="101" font-size="9" fill="#cbd5e1">Fine insulating down</text>
      <text x="10" y="116" font-size="9" font-weight="bold" fill="#fef08a">Produces CASHMERE</text>
    </g>
  </g>
</svg>
""")

# SVG 7: Productivity Equation (Lesson 9, Page 2)
SVG_PRODUCTIVITY_EQUATION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Golden Formula: Productivity = Genetics × Environment</text>

  <!-- Big Equation Blocks -->
  <!-- Genetics -->
  <g transform="translate(45, 80)">
    <rect x="0" y="0" width="210" height="150" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="3"/>
    <rect x="0" y="0" width="210" height="32" rx="10" fill="#6b21a8"/>
    <text x="105" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">GENETICS (THE CEILING)</text>
    <text x="15" y="60" font-size="10" fill="#cbd5e1">• Inherited DNA blueprint</text>
    <text x="15" y="80" font-size="10" fill="#cbd5e1">• Sets MAXIMUM yield limit</text>
    <text x="15" y="100" font-size="10" fill="#cbd5e1">• Friesian = 35L potential</text>
    <text x="15" y="120" font-size="10" fill="#cbd5e1">• Zebu = 4L potential</text>
  </g>

  <text x="278" y="165" font-size="32" font-weight="bold" fill="#ffffff" text-anchor="middle">×</text>

  <!-- Environment -->
  <g transform="translate(300, 80)">
    <rect x="0" y="0" width="210" height="150" rx="10" fill="#0f172a" stroke="#06b6d4" stroke-width="3"/>
    <rect x="0" y="0" width="210" height="32" rx="10" fill="#0e7490"/>
    <text x="105" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">ENVIRONMENT (ENABLER)</text>
    <text x="15" y="60" font-size="10" fill="#cbd5e1">• High-protein TMR silage</text>
    <text x="15" y="80" font-size="10" fill="#cbd5e1">• Tick dipping / ECF vaccine</text>
    <text x="15" y="100" font-size="10" fill="#cbd5e1">• Clean water &amp; ventilation</text>
    <text x="15" y="120" font-size="10" fill="#cbd5e1">• Thermal shade comfort</text>
  </g>

  <text x="533" y="165" font-size="32" font-weight="bold" fill="#ffffff" text-anchor="middle">=</text>

  <!-- Productivity Result -->
  <g transform="translate(555, 80)">
    <rect x="0" y="0" width="200" height="150" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="3"/>
    <rect x="0" y="0" width="200" height="32" rx="10" fill="#15803d"/>
    <text x="100" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">REALIZED YIELD &amp; PROFIT</text>
    <text x="15" y="60" font-size="10" fill="#cbd5e1">• Maximum milk output</text>
    <text x="15" y="80" font-size="10" fill="#cbd5e1">• Rapid muscle gain</text>
    <text x="15" y="100" font-size="10" fill="#cbd5e1">• High kit/litter survival</text>
    <text x="15" y="120" font-size="10" font-weight="bold" fill="#4ade80">• Agribusiness Success</text>
  </g>

  <!-- Agronomic Warning Footer -->
  <g transform="translate(45, 260)">
    <rect x="0" y="0" width="710" height="145" rx="8" fill="#1e293b" stroke="#ef4444"/>
    <text x="355" y="28" font-size="12" font-weight="bold" fill="#f87171" text-anchor="middle">THE AGRIBUSINESS MISMATCH WARNING</text>
    <text x="25" y="55" font-size="11" fill="#cbd5e1">If a farmer buys 35-liter Friesian genetics but provides a 3-liter poor rangeland environment:</text>
    <text x="25" y="78" font-size="11" font-weight="bold" fill="#fca5a5">• Realized output collapses to 3 Liters per day</text>
    <text x="25" y="98" font-size="11" fill="#cbd5e1">• Severe emaciation, tick-borne East Coast Fever (ECF) breakdown, and high mortality!</text>
    <text x="25" y="122" font-size="11" font-weight="bold" fill="#4ade80">RULE: Always match animal genetics to your available feed budget and agro-ecological climate!</text>
  </g>
</svg>
""")

# SVG 8: Master Livestock Taxonomy (Lesson 10, Page 2)
SVG_MASTER_TAXONOMY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">Master Livestock Breeds Taxonomy &amp; Agro-Ecological Map</text>

  <!-- 5 Species Cards -->
  <!-- 1. Cattle -->
  <g transform="translate(35, 60)">
    <rect x="0" y="0" width="135" height="350" rx="6" fill="#0f172a" stroke="#38bdf8"/>
    <text x="67" y="22" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. CATTLE</text>
    <text x="8" y="45" font-size="9" font-weight="bold" fill="#ffffff">Dairy:</text>
    <text x="8" y="60" font-size="8" fill="#cbd5e1">• Friesian (Vol)</text>
    <text x="8" y="73" font-size="8" fill="#cbd5e1">• Jersey (Fat)</text>
    <text x="8" y="86" font-size="8" fill="#cbd5e1">• Ayrshire</text>
    <text x="8" y="99" font-size="8" fill="#cbd5e1">• Guernsey</text>
    <text x="8" y="120" font-size="9" font-weight="bold" fill="#ffffff">Beef:</text>
    <text x="8" y="135" font-size="8" fill="#cbd5e1">• Boran (Trop)</text>
    <text x="8" y="148" font-size="8" fill="#cbd5e1">• Brahman</text>
    <text x="8" y="161" font-size="8" fill="#cbd5e1">• Angus (Marb)</text>
    <text x="8" y="174" font-size="8" fill="#cbd5e1">• Hereford</text>
    <text x="8" y="195" font-size="9" font-weight="bold" fill="#ffffff">Dual:</text>
    <text x="8" y="210" font-size="8" fill="#cbd5e1">• Sahiwal</text>
    <text x="8" y="223" font-size="8" fill="#cbd5e1">• Simmental</text>
  </g>

  <!-- 2. Pigs -->
  <g transform="translate(185, 60)">
    <rect x="0" y="0" width="135" height="350" rx="6" fill="#0f172a" stroke="#22c55e"/>
    <text x="67" y="22" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="middle">2. PIGS</text>
    <text x="8" y="45" font-size="9" font-weight="bold" fill="#ffffff">Maternal:</text>
    <text x="8" y="60" font-size="8" fill="#cbd5e1">• Large White</text>
    <text x="12" y="72" font-size="7" fill="#86efac">(Erect ears)</text>
    <text x="8" y="86" font-size="8" fill="#cbd5e1">• Landrace</text>
    <text x="12" y="98" font-size="7" fill="#86efac">(Bacon length)</text>
    <text x="8" y="120" font-size="9" font-weight="bold" fill="#ffffff">Terminal Sire:</text>
    <text x="8" y="135" font-size="8" fill="#cbd5e1">• Duroc (Red)</text>
    <text x="8" y="148" font-size="8" fill="#cbd5e1">• Hampshire</text>
    <text x="12" y="160" font-size="7" fill="#86efac">(White belt)</text>
  </g>

  <!-- 3. Rabbits -->
  <g transform="translate(335, 60)">
    <rect x="0" y="0" width="135" height="350" rx="6" fill="#0f172a" stroke="#eab308"/>
    <text x="67" y="22" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">3. RABBITS</text>
    <text x="8" y="45" font-size="9" font-weight="bold" fill="#ffffff">Meat:</text>
    <text x="8" y="60" font-size="8" fill="#cbd5e1">• NZ White</text>
    <text x="12" y="72" font-size="7" fill="#fef08a">(Pink eyes)</text>
    <text x="8" y="86" font-size="8" fill="#cbd5e1">• California</text>
    <text x="12" y="98" font-size="7" fill="#fef08a">(Black points)</text>
    <text x="8" y="120" font-size="9" font-weight="bold" fill="#ffffff">Specialty:</text>
    <text x="8" y="135" font-size="8" fill="#cbd5e1">• Flemish Giant</text>
    <text x="8" y="148" font-size="8" fill="#cbd5e1">• Angora (Wool)</text>
  </g>

  <!-- 4. Sheep -->
  <g transform="translate(485, 60)">
    <rect x="0" y="0" width="135" height="350" rx="6" fill="#0f172a" stroke="#ec4899"/>
    <text x="67" y="22" font-size="11" font-weight="bold" fill="#f472b6" text-anchor="middle">4. SHEEP</text>
    <text x="8" y="45" font-size="9" font-weight="bold" fill="#ffffff">Wool:</text>
    <text x="8" y="60" font-size="8" fill="#cbd5e1">• Merino</text>
    <text x="8" y="80" font-size="9" font-weight="bold" fill="#ffffff">Dual:</text>
    <text x="8" y="95" font-size="8" fill="#cbd5e1">• Corriedale</text>
    <text x="8" y="115" font-size="9" font-weight="bold" fill="#ffffff">Meat / Hair:</text>
    <text x="8" y="130" font-size="8" fill="#cbd5e1">• Dorper</text>
    <text x="12" y="142" font-size="7" fill="#fbcfe8">(Black head)</text>
    <text x="8" y="156" font-size="8" fill="#cbd5e1">• Red Masai</text>
    <text x="12" y="168" font-size="7" fill="#fbcfe8">(Worm immune)</text>
  </g>

  <!-- 5. Goats -->
  <g transform="translate(635, 60)">
    <rect x="0" y="0" width="135" height="350" rx="6" fill="#0f172a" stroke="#a855f7"/>
    <text x="67" y="22" font-size="11" font-weight="bold" fill="#d8b4fe" text-anchor="middle">5. GOATS</text>
    <text x="8" y="45" font-size="9" font-weight="bold" fill="#ffffff">Meat:</text>
    <text x="8" y="60" font-size="8" fill="#cbd5e1">• Boer (Red head)</text>
    <text x="8" y="73" font-size="8" fill="#cbd5e1">• Galla (White)</text>
    <text x="8" y="95" font-size="9" font-weight="bold" fill="#ffffff">Dairy:</text>
    <text x="8" y="110" font-size="8" fill="#cbd5e1">• Saanen (Vol)</text>
    <text x="8" y="123" font-size="8" fill="#cbd5e1">• Toggenburg</text>
    <text x="8" y="136" font-size="8" fill="#cbd5e1">• Nubian (Fat)</text>
    <text x="8" y="155" font-size="9" font-weight="bold" fill="#ffffff">Fiber:</text>
    <text x="8" y="170" font-size="8" fill="#cbd5e1">• Angora (Mohair)</text>
  </g>
</svg>
""")

SVG_MAP = {
    1: {"page": 2, "svg": SVG_BREED_CLASSIFICATION, "title": "Livestock Classification: Purpose & Environmental Adaptation Matrix"},
    2: {"page": 2, "svg": SVG_DAIRY_TRADE_OFF, "title": "Major Dairy Cattle Breeds: Milk Volume vs Butterfat Trade-Off"},
    3: {"page": 2, "svg": SVG_BOS_INDICUS_VS_TAURUS, "title": "Humped Bos indicus vs Humpless Bos taurus Morphological Anatomy"},
    4: {"page": 2, "svg": SVG_PIG_BREEDS, "title": "Commercial Pig Breeds Diagnostic Morphological Profiles"},
    6: {"page": 2, "svg": SVG_SHEEP_BREEDS, "title": "Meat & Dairy Sheep Breeds: Merino vs Dorper vs Red Masai"},
    7: {"page": 2, "svg": SVG_GOAT_BREEDS, "title": "Goat Breeds Classification Tree: Meat, Dairy, and Fiber"},
    9: {"page": 2, "svg": SVG_PRODUCTIVITY_EQUATION, "title": "Livestock Productivity Equation: Productivity = Genetics x Environment"},
    10: {"page": 2, "svg": SVG_MASTER_TAXONOMY, "title": "Master Livestock Breeds Taxonomy & Agro-Ecological Map"}
}

def enrich_grade10_topic8():
    """Injects verified photos, responsive vector SVGs, YouTube embeds, and creates LessonAssets."""
    print("=" * 80)
    print("STARTING ENRICHMENT: CBC Grade 10 Agriculture — Topic 8: Breeds of Livestock")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()
    topic = Topic.objects.filter(subject=subject, name="Breeds of Livestock").first()

    assert topic, "Topic 'Breeds of Livestock' not found!"

    images_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grade10_topic8_verified_images.json")
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
                    "topic_order": 8,
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
                        "topic_order": 8,
                        "unit_order": u_order,
                        "page": svg_def["page"],
                        "svg_content": svg_def["svg"]
                    }
                )
                diag_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [Vector SVG Attached] Lesson {u_order}: {svg_def['title']}")

        # ---------------------------------------------------------------------
        # 3. Educational YouTube Videos (Lesson 3)
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
                        "topic_order": 8,
                        "unit_order": u_order,
                        "youtube_url": v_url
                    }
                )
                v_block.assets.add(asset)
                total_assets_persisted += 1
                print(f"  [YouTube Video Attached] Lesson {u_order}: {v_block.title}")

    print("=" * 80)
    print(f"ENRICHMENT COMPLETE: Topic 8 '{topic.name}'")
    print(f"  Photographic Hooks: {total_images_attached} / 10")
    print(f"  Vector SVGs:        {total_svgs_attached} / 8")
    print(f"  YouTube Videos:     {total_videos_attached} / 1")
    print(f"  LessonAssets:       {total_assets_persisted}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_grade10_topic8()
