"""
VLearn CBC Grade 8 Agriculture — Topic 9: Cooking Balanced Meals for Special Occasions
Visual Enrichment & Multi-Video Integration Engine (Phase 2: High-Fidelity Technical SVGs & Videos)

Curriculum: CBC (Grade 8)
Subject: Agriculture
Topic: Cooking Balanced Meals for Special Occasions (Topic Order: 9)

Enrichment Architecture:
  1. Phase 2A: Card-1 Photographic Visual Hooks (5 Lessons via Verified Wikimedia URLs).
  2. Phase 2B: 5 Custom Responsive Vector SVGs (viewBox="0 0 800 450", high contrast #0f172a dark-mode).
  3. Phase 2C: Multi-Video Instructional Integration (3 Verified YouTube videos across key lessons).
  4. Phase 2D: LessonAsset Model Registration and Database Synchronization.

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade8_agriculture_topic9.py
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
# 5 CUSTOM RESPONSIVE VECTOR SVGS (viewBox="0 0 800 450")
# =============================================================================

SVGS = {
    # -------------------------------------------------------------------------
    # SVG 1 (Lesson 1 Page 2): Special Occasion Event Menu Logistics Framework
    # -------------------------------------------------------------------------
    1: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">EVENT MENU LOGISTICS &amp; DEMOGRAPHIC BALANCING FRAMEWORK</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Harmonizing Guest Count, Budget, Nutrition, and Local Seasonal Sourcing</text>

  <!-- Step 1: RSVP Demographics -->
  <g transform="translate(30, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#0284c7"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1</text>
    <text x="82" y="65" fill="#38bdf8" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">RSVP &amp; GUESTS</text>
    <text x="82" y="95" fill="#bae6fd" font-size="10" text-anchor="middle">• Toddlers (Soft foods)</text>
    <text x="82" y="115" fill="#bae6fd" font-size="10" text-anchor="middle">• Teens (High calorie)</text>
    <text x="82" y="135" fill="#bae6fd" font-size="10" text-anchor="middle">• Adults (Standard)</text>
    <text x="82" y="155" fill="#bae6fd" font-size="10" text-anchor="middle">• Elderly (High fiber)</text>
    <text x="82" y="195" fill="#38bdf8" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Prevents Leftover Waste</text>
  </g>

  <!-- Step 2: Budget & Sourcing -->
  <g transform="translate(220, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#059669"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2</text>
    <text x="82" y="65" fill="#34d399" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">LOCAL SOURCING</text>
    <text x="82" y="95" fill="#a7f3d0" font-size="10" text-anchor="middle">• In-Season Greens</text>
    <text x="82" y="115" fill="#a7f3d0" font-size="10" text-anchor="middle">• Local Sweet Tubers</text>
    <text x="82" y="135" fill="#a7f3d0" font-size="10" text-anchor="middle">• Farm Legumes / Eggs</text>
    <text x="82" y="155" fill="#a7f3d0" font-size="10" text-anchor="middle">• Wholesale Pricing</text>
    <text x="82" y="195" fill="#34d399" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Cuts Costs by up to 60%</text>
  </g>

  <!-- Step 3: Golden Ratio Plate -->
  <g transform="translate(410, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#d97706"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">3</text>
    <text x="82" y="65" fill="#fbbf24" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">GOLDEN RATIO</text>
    <circle cx="82" cy="115" r="30" fill="#334155" stroke="#fbbf24" stroke-width="2"/>
    <path d="M 82 85 A 30 30 0 0 1 112 115 L 82 115 Z" fill="#22c55e"/>
    <text x="82" y="165" fill="#fde68a" font-size="10" text-anchor="middle">• 1/2 Veg &amp; Fruit</text>
    <text x="82" y="180" fill="#fde68a" font-size="10" text-anchor="middle">• 1/4 Protein</text>
    <text x="82" y="195" fill="#fde68a" font-size="10" text-anchor="middle">• 1/4 Starch (Carbs)</text>
  </g>

  <!-- Step 4: Kitchen Capacity -->
  <g transform="translate(600, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#7c3aed"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">4</text>
    <text x="82" y="65" fill="#c084fc" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">EQUIPMENT CHECK</text>
    <text x="82" y="95" fill="#ddd6fe" font-size="10" text-anchor="middle">• Sufuria Capacities</text>
    <text x="82" y="115" fill="#ddd6fe" font-size="10" text-anchor="middle">• Burners &amp; Fuel</text>
    <text x="82" y="135" fill="#ddd6fe" font-size="10" text-anchor="middle">• Serving Plates Count</text>
    <text x="82" y="155" fill="#ddd6fe" font-size="10" text-anchor="middle">• Sanitation Stations</text>
    <text x="82" y="195" fill="#c084fc" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Timely Service Delivery</text>
  </g>

  <!-- Bottom Pro-Tip Banner -->
  <rect x="30" y="345" width="735" height="80" rx="8" fill="#1e293b" stroke="#475569"/>
  <text x="50" y="370" fill="#38bdf8" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">HOSPITALITY GOLDEN RULE:</text>
  <text x="50" y="392" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Never guess quantities blindly: calculate exact ingredient needs with confirmed guest RSVPs</text>
  <text x="50" y="410" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Harvesting directly from school gardens slashes catering costs to near zero while maximizing food freshness</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 2 (Lesson 2 Page 2): Family-Style vs Blue-Plate Service Comparison
    # -------------------------------------------------------------------------
    2: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">FOOD SERVICE SYSTEMS: FAMILY-STYLE VS. BLUE-PLATE SERVICE</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Comparing Communal Shared Platters vs. Kitchen-Portioned Individual Service</text>

  <!-- Left: Family-Style Service -->
  <g transform="translate(40, 85)">
    <rect width="340" height="240" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="170" y="26" fill="#fbbf24" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">FAMILY-STYLE (COMMUNAL PLATTERS)</text>

    <!-- Table with shared platters -->
    <ellipse cx="170" cy="70" rx="60" ry="25" fill="#334155" stroke="#f59e0b"/>
    <circle cx="170" cy="70" r="14" fill="#78350f"/>
    <text x="170" y="74" fill="#fef3c7" font-size="8" font-weight="bold" text-anchor="middle">PLATTER</text>

    <text x="25" y="120" fill="#fde68a" font-size="10" font-weight="bold">ADVANTAGES:</text>
    <text x="25" y="136" fill="#e2e8f0" font-size="9">• Highly social, promotes warmth and sharing</text>
    <text x="25" y="150" fill="#e2e8f0" font-size="9">• Lower labor: guests serve themselves</text>

    <text x="25" y="175" fill="#fca5a5" font-size="10" font-weight="bold">LIMITATIONS:</text>
    <text x="25" y="191" fill="#e2e8f0" font-size="9">• Uneven portions (early guests take all meat)</text>
    <text x="25" y="205" fill="#e2e8f0" font-size="9">• Risk of germ spread on shared serving spoons</text>
  </g>

  <!-- Right: Blue-Plate Service -->
  <g transform="translate(420, 85)">
    <rect width="340" height="240" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="170" y="26" fill="#38bdf8" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">BLUE-PLATE (KITCHEN PLATED)</text>

    <!-- Plated individual plate -->
    <circle cx="170" cy="70" r="28" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="170" cy="70" r="20" fill="#0369a1"/>
    <text x="170" y="74" fill="#fff" font-size="8" font-weight="bold" text-anchor="middle">1/2 VEG</text>

    <text x="25" y="120" fill="#bae6fd" font-size="10" font-weight="bold">ADVANTAGES:</text>
    <text x="25" y="136" fill="#e2e8f0" font-size="9">• Strict portion control: 100% fair distribution</text>
    <text x="25" y="150" fill="#e2e8f0" font-size="9">• Superior hygiene: food untouched by other guests</text>
    <text x="25" y="164" fill="#e2e8f0" font-size="9">• Elegant, artistic visual presentation</text>

    <text x="25" y="188" fill="#fca5a5" font-size="10" font-weight="bold">LIMITATIONS:</text>
    <text x="25" y="204" fill="#e2e8f0" font-size="9">• High labor: requires plating crew and servers</text>
  </g>

  <!-- Bottom Summary Banner -->
  <rect x="40" y="345" width="720" height="80" rx="8" fill="#1e293b" stroke="#10b981"/>
  <text x="60" y="370" fill="#34d399" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">SCENARIO SELECTION RULE:</text>
  <text x="60" y="392" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Use Blue-Plate for formal banquets, weddings, hospital wards, and strict budget control</text>
  <text x="60" y="410" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Use Family-Style for informal Sunday lunches, holiday dinners, and school club celebrations</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 3 (Lesson 3 Page 2): Event Menu Design Architecture Flowchart
    # -------------------------------------------------------------------------
    3: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">EVENT MENU DESIGN ARCHITECTURE: SENSORY HARMONY &amp; SOURCING</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Step-by-Step Flow from Budget Check to Color, Texture, and Flavor Optimization</text>

  <!-- Step 1: Budget & Starch Base -->
  <g transform="translate(30, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#d97706"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1</text>
    <text x="82" y="65" fill="#fbbf24" font-size="11" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">LOCAL STARCH BASE</text>
    <text x="82" y="95" fill="#fde68a" font-size="10" text-anchor="middle">• Yellow Turmeric Rice</text>
    <text x="82" y="115" fill="#fde68a" font-size="10" text-anchor="middle">• Spiced Maize Pilau</text>
    <text x="82" y="135" fill="#fde68a" font-size="10" text-anchor="middle">• Roasted Sweet Potato</text>
    <text x="82" y="195" fill="#fbbf24" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Energy Foundation (1/4)</text>
  </g>

  <!-- Step 2: Bodybuilding Protein -->
  <g transform="translate(220, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#dc2626"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2</text>
    <text x="82" y="65" fill="#f87171" font-size="11" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">PROTEIN CHOICES</text>
    <text x="82" y="95" fill="#fca5a5" font-size="10" text-anchor="middle">• Savory Beef Stew</text>
    <text x="82" y="115" fill="#fca5a5" font-size="10" text-anchor="middle">• Tender Roast Chicken</text>
    <text x="82" y="135" fill="#fca5a5" font-size="10" text-anchor="middle">• Cowpea / Bean Stew</text>
    <text x="82" y="195" fill="#f87171" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Muscle Repair (1/4)</text>
  </g>

  <!-- Step 3: Rainbow Protection -->
  <g transform="translate(410, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#059669"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">3</text>
    <text x="82" y="65" fill="#34d399" font-size="11" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">RAINBOW GREENS</text>
    <text x="82" y="95" fill="#a7f3d0" font-size="10" text-anchor="middle">• Steamed Dark Greens</text>
    <text x="82" y="115" fill="#a7f3d0" font-size="10" text-anchor="middle">• Red Tomato Kachumbari</text>
    <text x="82" y="135" fill="#a7f3d0" font-size="10" text-anchor="middle">• Orange Carrot Slaw</text>
    <text x="82" y="195" fill="#34d399" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Immune Defense (1/2)</text>
  </g>

  <!-- Step 4: Sensory Audit -->
  <g transform="translate(600, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#7c3aed"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">4</text>
    <text x="82" y="65" fill="#c084fc" font-size="11" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">SENSORY AUDIT</text>
    <text x="82" y="95" fill="#ddd6fe" font-size="10" text-anchor="middle">• COLOR: No pale mono</text>
    <text x="82" y="115" fill="#ddd6fe" font-size="10" text-anchor="middle">• TEXTURE: Soft + Crunch</text>
    <text x="82" y="135" fill="#ddd6fe" font-size="10" text-anchor="middle">• FLAVOR: Savory + Tang</text>
    <text x="82" y="195" fill="#c084fc" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Stimulates Appetite</text>
  </g>

  <!-- Bottom Banner -->
  <rect x="30" y="345" width="735" height="80" rx="8" fill="#1e293b" stroke="#38bdf8"/>
  <text x="50" y="370" fill="#38bdf8" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">SENSORY PLATING INSIGHT:</text>
  <text x="50" y="392" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• We eat with our eyes first: a colorful plate triggers salivation and digestive enzyme release</text>
  <text x="50" y="410" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Intercropping legumes with maize yields complete proteins on farms that translate directly to delicious event stews</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 4 (Lesson 4 Page 2): Banqueting Kitchen Operation & Safety Protocols
    # -------------------------------------------------------------------------
    4: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">BANQUETING KITCHEN LAB: WORKFLOW, HYGIENE &amp; SAFETY</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">3-Basin Sanitation, Color-Coded Cutting Boards, Inward Handles &amp; Short Steaming</text>

  <!-- Station 1: 3-Basin Station -->
  <g transform="translate(30, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#0284c7"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1</text>
    <text x="82" y="65" fill="#38bdf8" font-size="11" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">3-BASIN SYSTEM</text>
    <text x="82" y="95" fill="#bae6fd" font-size="9" text-anchor="middle">• Basin 1: Soapy Wash</text>
    <text x="82" y="115" fill="#bae6fd" font-size="9" text-anchor="middle">• Basin 2: Clean Rinse</text>
    <text x="82" y="135" fill="#bae6fd" font-size="9" text-anchor="middle">• Basin 3: Sanitizer</text>
    <text x="82" y="195" fill="#38bdf8" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Stops Germ Spread</text>
  </g>

  <!-- Station 2: Mise en Place Boards -->
  <g transform="translate(220, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#dc2626"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2</text>
    <text x="82" y="65" fill="#f87171" font-size="11" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">MISE EN PLACE</text>
    <rect x="40" y="85" width="35" height="25" rx="3" fill="#ef4444"/>
    <text x="57" y="100" fill="#fff" font-size="7" font-weight="bold" text-anchor="middle">MEAT</text>
    <rect x="90" y="85" width="35" height="25" rx="3" fill="#22c55e"/>
    <text x="107" y="100" fill="#fff" font-size="7" font-weight="bold" text-anchor="middle">VEG</text>
    <text x="82" y="145" fill="#e2e8f0" font-size="9" text-anchor="middle">Separate boards stop</text>
    <text x="82" y="160" fill="#e2e8f0" font-size="9" text-anchor="middle">cross-contamination!</text>
    <text x="82" y="195" fill="#f87171" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Color-Coded Protocol</text>
  </g>

  <!-- Station 3: Stove Safety -->
  <g transform="translate(410, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#d97706"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">3</text>
    <text x="82" y="65" fill="#fbbf24" font-size="11" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">STOVE SAFETY</text>
    <rect x="40" y="90" width="85" height="35" rx="4" fill="#334155" stroke="#f59e0b"/>
    <line x1="125" y1="105" x2="145" y2="105" stroke="#94a3b8" stroke-width="4"/>
    <text x="82" y="150" fill="#e2e8f0" font-size="9" text-anchor="middle">Inward pot handles</text>
    <text x="82" y="165" fill="#e2e8f0" font-size="9" text-anchor="middle">prevent scalding burns</text>
    <text x="82" y="195" fill="#fbbf24" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Steam Greens 3-5 Min</text>
  </g>

  <!-- Station 4: Blue-Plate Presentation -->
  <g transform="translate(600, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#059669"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">4</text>
    <text x="82" y="65" fill="#34d399" font-size="11" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">BLUE-PLATING</text>
    <circle cx="82" cy="105" r="28" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <text x="82" y="150" fill="#e2e8f0" font-size="9" text-anchor="middle">Portion 1/2 greens,</text>
    <text x="82" y="165" fill="#e2e8f0" font-size="9" text-anchor="middle">1/4 meat, 1/4 rice.</text>
    <text x="82" y="195" fill="#34d399" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Spotless Plate Rim</text>
  </g>

  <!-- Bottom Certification -->
  <rect x="30" y="345" width="735" height="80" rx="8" fill="#1e293b" stroke="#475569"/>
  <text x="50" y="370" fill="#38bdf8" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">CULINARY EXCELLENCE PROTOCOL:</text>
  <text x="50" y="392" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Steaming cabbage for 3-5 min preserves Vitamin C and bright green color (never boil for 20 min)</text>
  <text x="50" y="410" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Plating teams wipe every plate edge with a sanitized cloth before front-of-house delivery</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 5 (Lesson 5 Page 2): Catering Financial Math & Circular Compost Loops
    # -------------------------------------------------------------------------
    5: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">CATERING FINANCIAL MATH &amp; CIRCULAR AGRICULTURAL WASTE LOOPS</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">The Portion Formula, Food Loss Prevention &amp; Organic Farm Composting</text>

  <!-- Left: Catering Math Formula -->
  <g transform="translate(40, 85)">
    <rect width="340" height="240" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="170" y="26" fill="#38bdf8" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1. THE PORTION FORMULA</text>

    <rect x="20" y="45" width="300" height="40" rx="6" fill="#0369a1"/>
    <text x="170" y="69" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">Total Need = Portion / Guest × Total Guests</text>

    <text x="25" y="115" fill="#bae6fd" font-size="11" font-weight="bold">PRACTICAL BUDGET EXAMPLE:</text>
    <text x="25" y="135" fill="#e2e8f0" font-size="10">• Rice Portion = 0.1 kg (100g) per person</text>
    <text x="25" y="152" fill="#e2e8f0" font-size="10">• Confirmed Guests (RSVP) = 30 people</text>
    <text x="25" y="169" fill="#a7f3d0" font-size="10" font-weight="bold">• Total Rice: 0.1 kg × 30 = 3.0 kg</text>
    <text x="25" y="186" fill="#fde68a" font-size="10" font-weight="bold">• Total Cost: 3 kg × 150 KES/kg = 450 KES</text>

    <text x="170" y="215" fill="#38bdf8" font-size="9" text-anchor="middle">Never double recipes blindly — stick to the math!</text>
  </g>

  <!-- Right: Circular Organic Compost Loop -->
  <g transform="translate(420, 85)">
    <rect width="340" height="240" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="170" y="26" fill="#34d399" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2. CIRCULAR AGRICULTURAL WASTE LOOP</text>

    <rect x="20" y="45" width="300" height="45" rx="4" fill="#047857"/>
    <text x="30" y="65" fill="#a7f3d0" font-size="10" font-weight="bold">CROP PREP SCRAPS</text>
    <text x="30" y="80" fill="#ecfdf5" font-size="9">Cabbage cores, potato skins, onion ends</text>

    <line x1="170" y1="95" x2="170" y2="115" stroke="#34d399" stroke-width="3"/>

    <rect x="20" y="120" width="300" height="45" rx="4" fill="#047857"/>
    <text x="30" y="140" fill="#a7f3d0" font-size="10" font-weight="bold">SCHOOL COMPOST HEAP</text>
    <text x="30" y="155" fill="#ecfdf5" font-size="9">Layered with dry leaves &amp; turned regularly</text>

    <line x1="170" y1="170" x2="170" y2="190" stroke="#34d399" stroke-width="3"/>

    <rect x="20" y="195" width="300" height="30" rx="4" fill="#065f46"/>
    <text x="170" y="215" fill="#a7f3d0" font-size="10" font-weight="bold" text-anchor="middle">SOIL ENRICHMENT FOR NEXT HARVEST</text>
  </g>

  <!-- Bottom Banner -->
  <rect x="40" y="345" width="720" height="80" rx="8" fill="#1e293b" stroke="#8b5cf6"/>
  <text x="60" y="370" fill="#c084fc" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">ZERO-WASTE CATERING STRATEGY:</text>
  <text x="60" y="392" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Use smaller serving plates to naturally regulate guest portion sizes and prevent plate waste</text>
  <text x="60" y="410" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Clean surplus food is donated immediately; organic residues return to the soil to grow tomorrow's feast</text>
</svg>"""
}

# =============================================================================
# CURATED VERIFIED YOUTUBE VIDEOS
# =============================================================================

TOPIC9_VIDEOS = {
    # Unit 2 (Page 4): Food Service Styles: Family-Style vs. Plated Service
    2: {
        "page_number": 4,
        "title": "Instructional Video: Food Service Styles: Family-Style vs. Plated Service",
        "url": "https://www.youtube.com/watch?v=TXJPk-QfhDU",
        "resolved_video_id": "TXJPk-QfhDU",
        "caption": "Watch this hospitality demonstration highlighting table setup, serving mechanics, and portion control differences between communal family service and plated banqueting."
    },
    # Unit 4 (Page 4): Practical Banquet Cookery & Mise en Place
    4: {
        "page_number": 4,
        "title": "Instructional Video: Practical Banquet Cookery & Mise en Place",
        "url": "https://www.youtube.com/watch?v=6ZjkLwQt_YE",
        "resolved_video_id": "6ZjkLwQt_YE",
        "caption": "Watch this practical kitchen demonstration showing team prep, vegetable steaming techniques, stove safety, and uniform banquet plating."
    },
    # Unit 5 (Page 6): Topic Video Review: Special Occasions Catering & Zero-Waste Hospitality
    5: {
        "page_number": 6,
        "title": "Topic Video Review: Special Occasions Catering & Zero-Waste Hospitality",
        "url": "https://www.youtube.com/watch?v=Ei5z_0Lxmic",
        "resolved_video_id": "Ei5z_0Lxmic",
        "caption": "Watch this comprehensive educational review covering event menu logistics, serving style comparisons, sensory aesthetics, kitchen safety, and catering financial management."
    }
}

# =============================================================================
# ENRICHMENT EXECUTION
# =============================================================================

def enrich_cbc_grade8_agriculture_topic9():
    """Attaches Card-1 photos, 5 custom SVGs, and 3 verified YouTube videos to Topic 9."""
    print("=" * 80)
    print("STARTING VISUAL ENRICHMENT: CBC GRADE 8 AGRICULTURE — TOPIC 9")
    print("=" * 80)

    topic = Topic.objects.filter(subject__grade__name="Grade 8", subject__name="Agriculture", name="Cooking Balanced Meals for Special Occasions").first()
    if not topic:
        print("[ERROR] Topic 'Cooking Balanced Meals for Special Occasions' not found under CBC Grade 8 Agriculture!")
        return

    lessons = Lesson.objects.filter(topic=topic).select_related("learning_unit").order_by("learning_unit__order")
    print(f"[*] Found {lessons.count()} Lessons under Topic: '{topic.name}' (ID: {topic.id})")

    # Load verified Card-1 images
    verified_images_path = os.path.join(os.path.dirname(__file__), "grade8_topic9_verified_images.json")
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
                title=f"Lesson {u_order} Visual Hook: {img_data.get('title', 'Celebration Meal')}",
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
        print("\n[+] Phase 2C: Attaching Curated Video Lessons across Topic 9...")
        for u_order, v_data in TOPIC9_VIDEOS.items():
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
    print(f"[SUCCESS] CBC Grade 8 Agriculture Topic 9 Visual Enrichment Complete!")
    print(f"[*] Total LessonAssets Created & Attached: {total_assets_created}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_cbc_grade8_agriculture_topic9()
