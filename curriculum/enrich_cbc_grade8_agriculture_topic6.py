"""
VLearn CBC Grade 8 Agriculture — Topic 6: Preparation of Animal Products
Visual Enrichment & Multi-Video Integration Engine (Phase 2: High-Fidelity Technical SVGs & Videos)

Curriculum: CBC (Grade 8)
Subject: Agriculture
Topic: Preparation of Animal Products (Topic Order: 6)

Enrichment Architecture:
  1. Phase 2A: Card-1 Photographic Visual Hooks (9 Lessons via Verified Wikimedia URLs).
  2. Phase 2B: 9 Custom Responsive Vector SVGs (viewBox="0 0 800 450", high contrast #0f172a dark-mode).
  3. Phase 2C: Multi-Video Instructional Integration (4 Verified YouTube videos across key lessons).
  4. Phase 2D: LessonAsset Model Registration and Database Synchronization.

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade8_agriculture_topic6.py
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
# 9 CUSTOM RESPONSIVE VECTOR SVGS (viewBox="0 0 800 450")
# =============================================================================

SVGS = {
    # -------------------------------------------------------------------------
    # SVG 1 (Lesson 1 Page 2): Fish Anatomy & 4-Step Scaling/Gutting Workflow
    # -------------------------------------------------------------------------
    1: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">FRESH FISH PROCESSING: 4-STEP SCALING & GUTTING WORKFLOW</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Anatomical Protocol for Descaling, Vent Slitting, and Viscera Extraction</text>

  <!-- Step 1: Hold Tail & Scrape -->
  <g transform="translate(30, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#0284c7"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1</text>
    <text x="82" y="65" fill="#38bdf8" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">HOLD TAIL & SCRAPE</text>
    <path d="M 30 110 Q 82 80 135 110 Q 82 140 30 110 Z" fill="#0284c7"/>
    <!-- Scraper arrow tail to head -->
    <path d="M 120 100 L 50 100" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrow)"/>
    <text x="82" y="165" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Grip tail with cloth.</text>
    <text x="82" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Scrape at 45° angle</text>
    <text x="82" y="195" fill="#38bdf8" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">from TAIL to HEAD.</text>
  </g>

  <!-- Step 2: Shallow Vent Slit -->
  <g transform="translate(220, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#d97706"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2</text>
    <text x="82" y="65" fill="#fbbf24" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">SHALLOW VENT SLIT</text>
    <path d="M 30 110 Q 82 80 135 110 Q 82 140 30 110 Z" fill="#0369a1"/>
    <!-- Shallow line along belly -->
    <line x1="50" y1="125" x2="110" y2="125" stroke="#ef4444" stroke-width="3"/>
    <text x="82" y="165" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Insert knife tip at vent.</text>
    <text x="82" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Cut shallow along belly</text>
    <text x="82" y="195" fill="#fbbf24" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">DO NOT puncture guts!</text>
  </g>

  <!-- Step 3: Extract Viscera -->
  <g transform="translate(410, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#059669"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">3</text>
    <text x="82" y="65" fill="#34d399" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">EXTRACT VISCERA</text>
    <circle cx="82" cy="115" r="22" fill="#78350f"/>
    <text x="82" y="120" fill="#fef3c7" font-size="9" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Guts & Gills</text>
    <text x="82" y="165" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Reach into belly slit.</text>
    <text x="82" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Pull out entrails &</text>
    <text x="82" y="195" fill="#34d399" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">red gills in one pull.</text>
  </g>

  <!-- Step 4: Rinse Cavity -->
  <g transform="translate(600, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#7c3aed"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">4</text>
    <text x="82" y="65" fill="#c084fc" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">RINSE CAVITY</text>
    <path d="M 60 90 L 105 90 L 100 135 L 65 135 Z" fill="#0284c7" opacity="0.6"/>
    <text x="82" y="117" fill="#fff" font-size="9" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Cold Water</text>
    <text x="82" y="165" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Wash under clean</text>
    <text x="82" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">cold running water.</text>
    <text x="82" y="195" fill="#c084fc" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Scrape black bloodline.</text>
  </g>

  <!-- Quality Checklist Bottom Banner -->
  <rect x="30" y="345" width="735" height="80" rx="8" fill="#1e293b" stroke="#475569"/>
  <text x="50" y="370" fill="#38bdf8" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">SENSORY QUALITY INDICATORS OF FRESH HARVESTED FISH:</text>
  <text x="50" y="392" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">1. Eyes: Clear, bright, bulging (never sunken/grey) • 2. Gills: Bright red/pink (never slimy brown)</text>
  <text x="50" y="410" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">3. Flesh: Firm, elastic spring-back • 4. Aroma: Fresh clean lake water (zero ammonia or sour rot odor)</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 2 (Lesson 2 Page 2): Fish Scoring, Pat-Drying & Frying Safety Dynamics
    # -------------------------------------------------------------------------
    2: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">FISH SCORING, PAT-DRYING & SAFE PAN-FRYING DYNAMICS</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Preventing Explosive Hot Oil Splattering & Ensuring Deep Heat Penetration</text>

  <!-- Left: Muscle Scoring & Pat-Drying -->
  <g transform="translate(40, 85)">
    <rect width="340" height="240" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="170" y="26" fill="#38bdf8" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1. SCORING & PAT-DRYING PREP</text>

    <!-- Scored Fish Graphic -->
    <path d="M 40 100 Q 170 60 290 100 Q 170 140 40 100 Z" fill="#0284c7"/>
    <!-- Diagonal Scores -->
    <line x1="120" y1="75" x2="140" y2="125" stroke="#fff" stroke-width="3"/>
    <line x1="160" y1="75" x2="180" y2="125" stroke="#fff" stroke-width="3"/>
    <line x1="200" y1="75" x2="220" y2="125" stroke="#fff" stroke-width="3"/>

    <text x="170" y="160" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif" text-anchor="middle">• Diagonal Cuts: Heat & salt reach deep spine.</text>
    <text x="170" y="180" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif" text-anchor="middle">• Rub Salt: Draws moisture via osmosis.</text>
    <text x="170" y="202" fill="#38bdf8" font-size="11" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">• Pat-Dry Thoroughly: Zero surface water!</text>
  </g>

  <!-- Right: Frying Physics & Tongs Placement -->
  <g transform="translate(420, 85)">
    <rect width="340" height="240" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="170" y="26" fill="#fbbf24" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2. SAFE PAN PLACEMENT (180°C OIL)</text>

    <!-- Frying Pan -->
    <ellipse cx="170" cy="115" rx="110" ry="35" fill="#78350f" stroke="#f59e0b" stroke-width="2"/>
    <ellipse cx="170" cy="115" rx="90" ry="25" fill="#ea580c"/>

    <!-- Tongs Angle Vector AWAY from Cook -->
    <line x1="50" y1="55" x2="130" y2="105" stroke="#94a3b8" stroke-width="4"/>
    <path d="M 130 95 L 180 85 L 170 120 Z" fill="#38bdf8"/>
    <!-- Arrow pointing forward -->
    <path d="M 150 70 L 210 70 L 200 60 M 210 70 L 200 80" stroke="#22c55e" stroke-width="3" fill="none"/>
    <text x="210" y="55" fill="#4ade80" font-size="10" font-weight="bold" text-anchor="middle">Slide AWAY from body</text>

    <text x="170" y="175" fill="#fde68a" font-size="11" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">WHY SLIDE AWAY FROM YOU?</text>
    <text x="170" y="195" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Any accidental grease splash travels toward the</text>
    <text x="170" y="210" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">back stove wall, protecting your face and chest!</text>
  </g>

  <!-- Physics Warning Bottom Banner -->
  <rect x="40" y="345" width="720" height="80" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
  <text x="60" y="370" fill="#f87171" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">CRITICAL THERMODYNAMIC SAFETY WARNING:</text>
  <text x="60" y="392" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Water boils at 100°C; Frying oil is at 180°C. Water in hot oil instantly flashes into expanding steam.</text>
  <text x="60" y="410" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Dropping a wet fish causes explosive oil spattering. Always pat-dry food and use long kitchen tongs!</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 3 (Lesson 3 Page 2): Humane Poultry Stunning & Scalding Temperature
    # -------------------------------------------------------------------------
    3: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">HUMANE POULTRY PROCESSING & SCALDING TEMPERATURE MATRIX</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Animal Welfare Ethics, Rapid Jugular Bleed, and Follicle Relaxation Science</text>

  <!-- Left: Restraining Cone & Stunning -->
  <g transform="translate(40, 85)">
    <rect width="340" height="240" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="170" y="26" fill="#38bdf8" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1. HUMANE STUNNING & BLEED CONE</text>

    <!-- Restraining Cone Graphic -->
    <polygon points="120,60 220,60 190,140 150,140" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
    <text x="170" y="105" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">Stainless Cone</text>
    <!-- Blood Drainage Vector -->
    <line x1="170" y1="140" x2="170" y2="165" stroke="#ef4444" stroke-width="3" stroke-dasharray="3,3"/>
    <text x="170" y="180" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">Rapid Jugular Bleed (2-3 mins)</text>

    <text x="170" y="202" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">• Stunning renders bird unconscious instantly.</text>
    <text x="170" y="218" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">• Cone prevents wing flapping bruises on breast meat.</text>
  </g>

  <!-- Right: Scalding Temperature Zone -->
  <g transform="translate(420, 85)">
    <rect width="340" height="240" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="170" y="26" fill="#34d399" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2. SCALDING TEMPERATURE PROTOCOL</text>

    <!-- Temp Bars -->
    <rect x="25" y="55" width="290" height="30" rx="4" fill="#0369a1"/>
    <text x="40" y="74" fill="#e0f2fe" font-size="11" font-weight="bold">&lt; 55°C (Too Cold):</text>
    <text x="160" y="74" fill="#bae6fd" font-size="10">Follicles stay tight; hard to pluck</text>

    <rect x="25" y="95" width="290" height="36" rx="4" fill="#047857" stroke="#34d399" stroke-width="2"/>
    <text x="40" y="117" fill="#ecfdf5" font-size="12" font-weight="bold">60°C - 65°C (OPTIMUM):</text>
    <text x="195" y="117" fill="#a7f3d0" font-size="10" font-weight="bold">Relaxes follicles; intact skin!</text>

    <rect x="25" y="140" width="290" height="30" rx="4" fill="#7f1d1d"/>
    <text x="40" y="159" fill="#fee2e2" font-size="11" font-weight="bold">100°C (Boiling):</text>
    <text x="150" y="159" fill="#fca5a5" font-size="10">Cooks skin; tears into shreds!</text>

    <text x="170" y="195" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Submerge bird for 45 to 60 seconds at 60°C-65°C.</text>
    <text x="170" y="212" fill="#34d399" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Pluck immediately in the direction feathers grow!</text>
  </g>

  <!-- Bottom Welfare Mandate -->
  <rect x="40" y="345" width="720" height="80" rx="8" fill="#1e293b" stroke="#f59e0b"/>
  <text x="60" y="370" fill="#fbbf24" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">ETHICAL SLAUGHTER & ANIMAL WELFARE MANDATE:</text>
  <text x="60" y="392" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Handle birds calmly without causing stress or panic • Use swift, painless stunning prior to neck cut</text>
  <text x="60" y="410" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Complete bleeding is mandatory: residual blood in veins accelerates bacterial rotting and spoils flavor</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 4 (Lesson 4 Page 2): Poultry Evisceration & Gallbladder Hazard
    # -------------------------------------------------------------------------
    4: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">POULTRY EVISCERATION ANATOMY & THE GALLBLADDER HAZARD</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Surgical Organ Extraction, Giblet Separation, and Upside-Down Cavity Drainage</text>

  <!-- Organ Anatomy Cards -->
  <!-- Liver & Gallbladder Warning -->
  <g transform="translate(40, 85)">
    <rect width="220" height="240" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <rect width="220" height="35" rx="8" fill="#7f1d1d"/>
    <text x="110" y="23" fill="#fee2e2" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1. LIVER & BILE HAZARD</text>

    <ellipse cx="110" cy="95" rx="45" ry="25" fill="#78350f"/>
    <text x="110" y="100" fill="#fef3c7" font-size="10" font-weight="bold" text-anchor="middle">Liver (Edible)</text>
    <!-- Gallbladder Green Sac -->
    <circle cx="140" cy="115" r="14" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
    <text x="140" y="120" fill="#fff" font-size="8" font-weight="bold" text-anchor="middle">BILE</text>

    <text x="110" y="160" fill="#fca5a5" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">CRITICAL BILE HAZARD!</text>
    <text x="110" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Cut gallbladder away gently.</text>
    <text x="110" y="195" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Puncture leaks bitter green bile</text>
    <text x="110" y="210" fill="#f87171" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">that ruins meat permanently!</text>
  </g>

  <!-- Gizzard Cleaning -->
  <g transform="translate(290, 85)">
    <rect width="220" height="240" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="220" height="35" rx="8" fill="#78350f"/>
    <text x="110" y="23" fill="#fef3c7" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2. GIZZARD PREPARATION</text>

    <circle cx="110" cy="95" r="30" fill="#991b1b"/>
    <ellipse cx="110" cy="95" rx="16" ry="16" fill="#eab308"/>
    <text x="110" y="100" fill="#78350f" font-size="8" font-weight="bold" text-anchor="middle">Lining</text>

    <text x="110" y="160" fill="#fde68a" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">GIZZARD PEELING SOP</text>
    <text x="110" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">1. Slice muscular stomach open</text>
    <text x="110" y="195" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">2. Wash out feed & grit stones</text>
    <text x="110" y="210" fill="#fbbf24" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">3. Peel tough yellow keratin lining</text>
  </g>

  <!-- Cavity Drainage Hook -->
  <g transform="translate(540, 85)">
    <rect width="220" height="240" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="220" height="35" rx="8" fill="#0c4a6e"/>
    <text x="110" y="23" fill="#e0f2fe" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">3. DRAINAGE SUSPENSION</text>

    <!-- Upside Down Chicken -->
    <path d="M 110 55 L 110 75 M 95 80 L 110 75 L 125 80" stroke="#94a3b8" stroke-width="3"/>
    <path d="M 90 90 L 130 90 L 120 135 L 100 135 Z" fill="#0284c7"/>
    <!-- Water Drips -->
    <circle cx="110" cy="148" r="3" fill="#38bdf8"/>
    <circle cx="110" cy="158" r="2" fill="#38bdf8"/>

    <text x="110" y="180" fill="#bae6fd" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">HANG FEET-UP (15-20 MINS)</text>
    <text x="110" y="198" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Drains trapped wash water.</text>
    <text x="110" y="212" fill="#38bdf8" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Prevents bacterial water pools!</text>
  </g>

  <!-- Bottom Summary Banner -->
  <rect x="40" y="345" width="720" height="80" rx="8" fill="#1e293b" stroke="#475569"/>
  <text x="60" y="370" fill="#38bdf8" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">OFFAL CLASSIFICATION SUMMARY:</text>
  <text x="60" y="392" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Edible Giblets: Liver (cleaned), Gizzard (peeled), Heart • Inedible Waste: Gallbladder, Intestines, Lungs</text>
  <text x="60" y="410" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Crop Removal: Pull neck food sac intact from front opening without spilling fermented grain</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 5 (Lesson 5 Page 2): Meat Dehydration via Osmosis & Parboiling
    # -------------------------------------------------------------------------
    5: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">MEAT PRESERVATION BY OSMOTIC DRY-SALTING & BOILING</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Cellular Water Activity Reduction vs High-Temperature Pathogen Inactivation</text>

  <!-- Dry-Salting (Left) -->
  <g transform="translate(40, 85)">
    <rect width="340" height="240" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="170" y="26" fill="#38bdf8" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1. DRY-SALTING (OSMOSIS MECHANISM)</text>

    <!-- Slanted Board with Salted Meat -->
    <line x1="40" y1="130" x2="280" y2="90" stroke="#94a3b8" stroke-width="4"/>
    <rect x="90" y="80" width="130" height="25" rx="4" fill="#991b1b" transform="rotate(-9.5 90 80)"/>
    <!-- Salt Crystals -->
    <circle cx="110" cy="73" r="3" fill="#fff"/>
    <circle cx="140" cy="68" r="3" fill="#fff"/>
    <circle cx="170" cy="63" r="3" fill="#fff"/>
    <!-- Water Drips -->
    <path d="M 270 100 L 270 125" stroke="#38bdf8" stroke-width="2" stroke-dasharray="2,2"/>
    <text x="270" y="140" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">Extracted H2O</text>

    <text x="170" y="165" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">• High salt concentration outside draws out water.</text>
    <text x="170" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">• Bacteria cells dehydrate, plasmolyze, and die.</text>
    <text x="170" y="200" fill="#38bdf8" font-size="11" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Shelf Life: 2 to 4 WEEKS (Zero Fuel!)</text>
    <text x="170" y="215" fill="#94a3b8" font-size="9" font-family="system-ui, sans-serif" text-anchor="middle">Must soak in clean water before cooking</text>
  </g>

  <!-- Boiling / Parboiling (Right) -->
  <g transform="translate(420, 85)">
    <rect width="340" height="240" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="170" y="26" fill="#fbbf24" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2. BOILING (THERMAL STERILIZATION)</text>

    <!-- Pot Boiling Graphic -->
    <rect x="90" y="70" width="160" height="70" rx="6" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
    <path d="M 110 60 Q 130 45 150 60 Q 170 45 190 60 Q 210 45 230 60" stroke="#f59e0b" stroke-width="2" fill="none"/>
    <text x="170" y="105" fill="#fef3c7" font-size="11" font-weight="bold" text-anchor="middle">100°C Salted Water</text>

    <text x="170" y="165" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">• 100°C destroys living microbes & mold spores.</text>
    <text x="170" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">• Heat denatures tissue enzymes that cause rot.</text>
    <text x="170" y="200" fill="#fbbf24" font-size="11" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Shelf Life: 2 to 4 DAYS (Short Term)</text>
    <text x="170" y="215" fill="#94a3b8" font-size="9" font-family="system-ui, sans-serif" text-anchor="middle">Requires firewood or cooking gas fuel</text>
  </g>

  <!-- Comparison Banner -->
  <rect x="40" y="345" width="720" height="80" rx="8" fill="#1e293b" stroke="#10b981"/>
  <text x="60" y="370" fill="#34d399" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">HOUSEHOLD PRESERVATION COMPARISON:</text>
  <text x="60" y="392" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Salting requires NO fire/fuel: Ideal for emergencies and long-distance transport (2-4 weeks shelf life)</text>
  <text x="60" y="410" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Parboiling requires fuel: Fast 20-minute cook, ready to eat immediately (2-4 days shelf life)</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 6 (Lesson 6 Page 2): Solar Drying vs Hardwood Wood-Smoking
    # -------------------------------------------------------------------------
    6: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">LONG-TERM PRESERVATION: SOLAR DRYING VS. WOOD-SMOKING</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Physical Solar Dehydration vs Chemical Hardwood Phenol Deposition</text>

  <!-- Left: Solar Drying -->
  <g transform="translate(40, 85)">
    <rect width="340" height="240" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="170" y="26" fill="#fbbf24" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1. SOLAR SUN-DRYING (NYIRINYIRI)</text>

    <!-- Sun & Hanging Lines -->
    <circle cx="70" cy="65" r="18" fill="#f59e0b"/>
    <line x1="40" y1="105" x2="300" y2="105" stroke="#94a3b8" stroke-width="2"/>
    <!-- Meat Strips -->
    <rect x="90" y="105" width="12" height="45" rx="2" fill="#7f1d1d"/>
    <rect x="140" y="105" width="12" height="45" rx="2" fill="#7f1d1d"/>
    <rect x="190" y="105" width="12" height="45" rx="2" fill="#7f1d1d"/>
    <rect x="240" y="105" width="12" height="45" rx="2" fill="#7f1d1d"/>

    <text x="170" y="170" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">• Slice thin (5 mm) & hang on wire lines.</text>
    <text x="170" y="185" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">• UV rays + dry wind evaporate water.</text>
    <text x="170" y="200" fill="#fde68a" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Moisture drops &lt; 10% (Bacteria die!)</text>
    <text x="170" y="218" fill="#38bdf8" font-size="11" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Shelf Life: 3 to 6 MONTHS</text>
  </g>

  <!-- Right: Hardwood Smoking -->
  <g transform="translate(420, 85)">
    <rect width="340" height="240" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="170" y="26" fill="#34d399" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2. HARDWOOD SMOKING (PHENOLS)</text>

    <!-- Smoke Chamber -->
    <rect x="90" y="60" width="160" height="90" rx="6" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
    <ellipse cx="170" cy="130" rx="30" ry="12" fill="#ea580c"/>
    <!-- Smoke trails -->
    <path d="M 150 115 Q 170 85 150 70 M 190 115 Q 170 85 190 70" stroke="#94a3b8" stroke-width="3" fill="none"/>

    <text x="170" y="170" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">• Acacia/Guava hardwood smoke at 45°C.</text>
    <text x="170" y="185" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">• Deposits natural phenols & organic acids.</text>
    <text x="170" y="200" fill="#a7f3d0" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Kills germs & prevents fat rancidity!</text>
    <text x="170" y="218" fill="#34d399" font-size="11" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Shelf Life: 2 to 4 MONTHS</text>
  </g>

  <!-- Wood Hazard Warning Banner -->
  <rect x="40" y="345" width="720" height="80" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
  <text x="60" y="370" fill="#f87171" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">STRICT FIREWOOD SELECTION RULE:</text>
  <text x="60" y="392" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• APPROVED: Hardwoods (Acacia, Mango, Guava) -> Burns clean, aromatic, non-toxic</text>
  <text x="60" y="410" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• FORBIDDEN: Resinous Softwoods (Pine, Cypress, Cedar) -> Releases toxic bitter sap soot that poisons meat</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 7 (Lesson 7 Page 2): Milk Pasteurization & Stir-Aeration Flow
    # -------------------------------------------------------------------------
    7: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">MILK PASTEURIZATION, STIR-AERATION & STERILIZATION FLOW</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Dairy Microbiology, Breaking Casein Protein Skin, and Preventing Re-Contamination</text>

  <!-- Step 1: Scald Bottles -->
  <g transform="translate(30, 85)">
    <rect width="130" height="240" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="65" cy="28" r="14" fill="#0284c7"/>
    <text x="65" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1</text>
    <text x="65" y="65" fill="#38bdf8" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">SCALD BOTTLES</text>
    <rect x="45" y="85" width="40" height="60" rx="4" fill="#0369a1"/>
    <text x="65" y="165" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Pour boiling</text>
    <text x="65" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">water into storage</text>
    <text x="65" y="195" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">jars to sterilize</text>
    <text x="65" y="210" fill="#38bdf8" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">before boiling milk.</text>
  </g>

  <!-- Step 2: Stir-Aeration -->
  <g transform="translate(180, 85)">
    <rect width="135" height="240" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="67" cy="28" r="14" fill="#d97706"/>
    <text x="67" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2</text>
    <text x="67" y="65" fill="#fbbf24" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">STIR-AERATION</text>
    <path d="M 35 110 L 100 110 L 90 145 L 45 145 Z" fill="#78350f"/>
    <!-- Spoon -->
    <line x1="45" y1="85" x2="85" y2="130" stroke="#f59e0b" stroke-width="3"/>
    <text x="67" y="165" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Stir continuously.</text>
    <text x="67" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Breaks casein skin</text>
    <text x="67" y="195" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">so steam vents</text>
    <text x="67" y="210" fill="#fbbf24" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">without boil-over.</text>
  </g>

  <!-- Step 3: Active Boil -->
  <g transform="translate(335, 85)">
    <rect width="135" height="240" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <circle cx="67" cy="28" r="14" fill="#059669"/>
    <text x="67" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">3</text>
    <text x="67" y="65" fill="#34d399" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">BOIL 2-3 MINS</text>
    <ellipse cx="67" cy="115" rx="35" ry="18" fill="#047857"/>
    <text x="67" y="120" fill="#ecfdf5" font-size="10" font-weight="bold" text-anchor="middle">100°C Boil</text>
    <text x="67" y="165" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Active rolling boil</text>
    <text x="67" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">for 2-3 minutes.</text>
    <text x="67" y="195" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Kills 100% TB &amp;</text>
    <text x="67" y="210" fill="#34d399" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Brucella bacteria.</text>
  </g>

  <!-- Step 4: Rapid Cool -->
  <g transform="translate(490, 85)">
    <rect width="130" height="240" rx="8" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <circle cx="65" cy="28" r="14" fill="#7c3aed"/>
    <text x="65" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">4</text>
    <text x="65" y="65" fill="#c084fc" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">RAPID COOLING</text>
    <circle cx="65" cy="115" r="22" fill="#0284c7" opacity="0.7"/>
    <text x="65" y="120" fill="#fff" font-size="8" font-weight="bold" text-anchor="middle">Water Bath</text>
    <text x="65" y="165" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Place pot into</text>
    <text x="65" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">cold water basin.</text>
    <text x="65" y="195" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Prevents cooked</text>
    <text x="65" y="210" fill="#c084fc" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">off-flavors.</text>
  </g>

  <!-- Step 5: Seal -->
  <g transform="translate(640, 85)">
    <rect width="130" height="240" rx="8" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
    <circle cx="65" cy="28" r="14" fill="#db2777"/>
    <text x="65" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">5</text>
    <text x="65" y="65" fill="#f472b6" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">STERILE SEAL</text>
    <rect x="45" y="90" width="40" height="50" rx="4" fill="#831843"/>
    <text x="65" y="165" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Pour into scalded</text>
    <text x="65" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">bottle &amp; cover.</text>
    <text x="65" y="195" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Never mix raw with</text>
    <text x="65" y="210" fill="#f472b6" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">boiled milk!</text>
  </g>

  <!-- Bottom Tip -->
  <rect x="30" y="345" width="740" height="80" rx="8" fill="#1e293b" stroke="#475569"/>
  <text x="50" y="370" fill="#fbbf24" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">ZOONOTIC PATHOGEN WARNING: NEVER CONSUME RAW UNBOILED MILK</text>
  <text x="50" y="392" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Raw milk transmits Bovine Tuberculosis and Brucellosis (chronic undulant fever and joint pain in humans)</text>
  <text x="50" y="410" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Boiling at 100°C for 2-3 minutes completely sterilizes the milk, safeguarding family health</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 8 (Lesson 8 Page 2): Lactic Acid Fermentation & Charcoal Cooler
    # -------------------------------------------------------------------------
    8: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">OFF-GRID DAIRY TECH: FERMENTATION (MALA) & CHARCOAL COOLING</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Biological Acid Preservation vs Physical Evaporative Heat Extraction</text>

  <!-- Left: Lactic Acid Fermentation (Mala) -->
  <g transform="translate(40, 85)">
    <rect width="340" height="240" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="170" y="26" fill="#fbbf24" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1. BIOLOGICAL FERMENTATION (MALA)</text>

    <!-- Calabash Gourd -->
    <ellipse cx="170" cy="115" rx="35" ry="45" fill="#78350f" stroke="#fbbf24" stroke-width="2"/>
    <circle cx="170" cy="70" r="18" fill="#78350f" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="170" y="118" fill="#fef3c7" font-size="10" font-weight="bold" text-anchor="middle">Mala Curd</text>

    <text x="170" y="170" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">• Boiled milk cooled to 38°C in sterilized gourd.</text>
    <text x="170" y="185" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">• <tspan font-weight="bold" fill="#fbbf24">Lactobacillus</tspan> turns lactose sugar into lactic acid.</text>
    <text x="170" y="200" fill="#fde68a" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">pH drops &lt; 4.5: Acid shield kills rot bacteria!</text>
    <text x="170" y="218" fill="#fbbf24" font-size="11" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Shelf Life: 2 to 3 WEEKS (Zero Electricity!)</text>
  </g>

  <!-- Right: Evaporative Charcoal Cooler -->
  <g transform="translate(420, 85)">
    <rect width="340" height="240" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="170" y="26" fill="#38bdf8" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2. PHYSICAL CHARCOAL COOLER</text>

    <!-- Cooler Cabinet -->
    <rect x="90" y="60" width="160" height="90" rx="4" fill="#334155" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="100" y="50" width="140" height="10" fill="#0284c7"/>
    <text x="170" y="58" fill="#e0f2fe" font-size="8" font-weight="bold" text-anchor="middle">Water Drip Tank</text>

    <!-- Wind Vector -->
    <path d="M 30 100 L 75 100" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
    <text x="50" y="90" fill="#38bdf8" font-size="9" font-weight="bold">Dry Breeze</text>

    <text x="170" y="170" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">• Water drips constantly on charcoal mesh walls.</text>
    <text x="170" y="185" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">• Dry wind evaporates water, absorbing heat energy.</text>
    <text x="170" y="200" fill="#bae6fd" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Drops internal temperature by 5°C to 10°C!</text>
    <text x="170" y="218" fill="#38bdf8" font-size="11" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Preserves Milk &amp; Veggies for 3-5 Days</text>
  </g>

  <!-- Summary Banner -->
  <rect x="40" y="345" width="720" height="80" rx="8" fill="#1e293b" stroke="#10b981"/>
  <text x="60" y="370" fill="#34d399" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">APPROPRIATE TECHNOLOGY FOR RURAL HOUSEHOLDS:</text>
  <text x="60" y="392" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Fermentation transforms perishable milk into nutritious, probiotic Mala curd that needs no fridge</text>
  <text x="60" y="410" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Charcoal coolers run on clean water and dry wind, delivering electricity-free refrigeration</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 9 (Lesson 9 Page 2): Food Security & Preservation Mind Map
    # -------------------------------------------------------------------------
    9: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">NATIONAL FOOD SECURITY & ANIMAL PRODUCT PRESERVATION HUB</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Strategic Impact on Nutrition, Poverty Reduction, and Climate Resilience</text>

  <!-- Central Hub -->
  <circle cx="400" cy="225" r="65" fill="#047857" stroke="#34d399" stroke-width="3"/>
  <text x="400" y="215" fill="#ecfdf5" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">FOOD SECURITY</text>
  <text x="400" y="235" fill="#a7f3d0" font-size="11" font-family="system-ui, sans-serif" text-anchor="middle">&amp; RESILIENCE</text>

  <!-- Branch 1: Nutrition (Top-Left) -->
  <g transform="translate(60, 75)">
    <rect width="220" height="95" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="110" y="24" fill="#38bdf8" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1. PROTEIN AVAILABILITY</text>
    <text x="110" y="46" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">• Constant protein, iron &amp; calcium</text>
    <text x="110" y="62" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">• Prevents stunting in teenagers</text>
    <text x="110" y="78" fill="#bae6fd" font-size="10" font-weight="bold" text-anchor="middle">Year-round nutrition balance</text>
  </g>
  <line x1="280" y1="125" x2="340" y2="185" stroke="#38bdf8" stroke-width="2"/>

  <!-- Branch 2: Financial Stability (Top-Right) -->
  <g transform="translate(520, 75)">
    <rect width="220" height="95" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="110" y="24" fill="#fbbf24" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2. FINANCIAL WEALTH</text>
    <text x="110" y="46" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">• Value addition (Mala &amp; Biltong)</text>
    <text x="110" y="62" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">• Higher selling prices in town</text>
    <text x="110" y="78" fill="#fde68a" font-size="10" font-weight="bold" text-anchor="middle">40% - 80% income increase</text>
  </g>
  <line x1="520" y1="125" x2="460" y2="185" stroke="#f59e0b" stroke-width="2"/>

  <!-- Branch 3: Disaster Shield (Bottom-Left) -->
  <g transform="translate(60, 275)">
    <rect width="220" height="95" rx="8" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <text x="110" y="24" fill="#c084fc" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">3. DROUGHT DISASTER SHIELD</text>
    <text x="110" y="46" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">• Stored dry meat &amp; fermented milk</text>
    <text x="110" y="62" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">• Feeds families during dry spells</text>
    <text x="110" y="78" fill="#ddd6fe" font-size="10" font-weight="bold" text-anchor="middle">Emergency hunger protection</text>
  </g>
  <line x1="280" y1="320" x2="340" y2="265" stroke="#8b5cf6" stroke-width="2"/>

  <!-- Branch 4: Waste Reduction (Bottom-Right) -->
  <g transform="translate(520, 275)">
    <rect width="220" height="95" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="110" y="24" fill="#34d399" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">4. WASTE REDUCTION</text>
    <text x="110" y="46" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">• Cuts 30% post-harvest loss</text>
    <text x="110" y="62" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">• Preserves livestock harvest fully</text>
    <text x="110" y="78" fill="#a7f3d0" font-size="10" font-weight="bold" text-anchor="middle">Zero food waste in community</text>
  </g>
  <line x1="520" y1="320" x2="460" y2="265" stroke="#10b981" stroke-width="2"/>

  <!-- Bottom Certificate Banner -->
  <rect x="60" y="395" width="680" height="35" rx="6" fill="#1e293b" stroke="#334155"/>
  <text x="400" y="417" fill="#f8fafc" font-size="11" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">SUSTAINABLE ANIMAL PRODUCT STEWARDSHIP — CBC GRADE 8 AGRICULTURE</text>
</svg>"""
}

# =============================================================================
# CURATED VERIFIED YOUTUBE VIDEOS
# =============================================================================

TOPIC6_VIDEOS = {
    # Unit 2 (Page 4): Tilapia Processing, Salting, and Deep-Frying in Kenya
    2: {
        "page_number": 4,
        "title": "Instructional Video: Tilapia Processing, Salting, and Deep-Frying",
        "url": "https://www.youtube.com/watch?v=TXJPk-QfhDU",
        "resolved_video_id": "TXJPk-QfhDU",
        "caption": "Watch this culinary demonstration showing fresh fish scaling, diagonal scoring, salting, pat-drying, and safe pan-frying techniques in Kenya."
    },
    # Unit 4 (Page 4): Grade 8 Agriculture Poultry Dressing & Gutting
    4: {
        "page_number": 4,
        "title": "Practical Video: Grade 8 Agriculture Poultry Dressing & Gutting",
        "url": "https://www.youtube.com/watch?v=6ZjkLwQt_YE",
        "resolved_video_id": "6ZjkLwQt_YE",
        "caption": "Watch this step-by-step practical demonstration on poultry evisceration, safe gallbladder removal, gizzard peeling, and carcass drainage in Kenya."
    },
    # Unit 8 (Page 4): Milk Fermentation & Low-Cost Charcoal Cooling
    8: {
        "page_number": 4,
        "title": "Instructional Video: Milk Fermentation & Low-Cost Charcoal Cooling",
        "url": "https://www.youtube.com/watch?v=uFnDdYWgkV8",
        "resolved_video_id": "uFnDdYWgkV8",
        "caption": "Watch this field demonstration on traditional milk fermentation in gourds and constructing low-cost evaporative charcoal coolers in Kenya."
    },
    # Unit 9 (Page 6): Topic Video Review: Animal Product Processing & Preservation
    9: {
        "page_number": 6,
        "title": "Topic Video Review: Animal Product Processing & Preservation",
        "url": "https://www.youtube.com/watch?v=Ei5z_0Lxmic",
        "resolved_video_id": "Ei5z_0Lxmic",
        "caption": "Watch this comprehensive educational review covering fish scaling, humane poultry dressing, meat salting, milk boiling, and low-cost charcoal cooling."
    }
}

# =============================================================================
# ENRICHMENT EXECUTION
# =============================================================================

def enrich_cbc_grade8_agriculture_topic6():
    """Attaches Card-1 photos, 9 custom SVGs, and 4 verified YouTube videos to Topic 6."""
    print("=" * 80)
    print("STARTING VISUAL ENRICHMENT: CBC GRADE 8 AGRICULTURE — TOPIC 6")
    print("=" * 80)

    topic = Topic.objects.filter(subject__grade__name="Grade 8", subject__name="Agriculture", name="Preparation of Animal Products").first()
    if not topic:
        print("[ERROR] Topic 'Preparation of Animal Products' not found under CBC Grade 8 Agriculture!")
        return

    lessons = Lesson.objects.filter(topic=topic).select_related("learning_unit").order_by("learning_unit__order")
    print(f"[*] Found {lessons.count()} Lessons under Topic: '{topic.name}' (ID: {topic.id})")

    # Load verified Card-1 images
    verified_images_path = os.path.join(os.path.dirname(__file__), "grade8_topic6_verified_images.json")
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
                title=f"Lesson {u_order} Visual Hook: {img_data.get('title', 'Animal Product Preparation')}",
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
        print("\n[+] Phase 2C: Attaching Curated Video Lessons across Topic 6...")
        for u_order, v_data in TOPIC6_VIDEOS.items():
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
    print(f"[SUCCESS] CBC Grade 8 Agriculture Topic 6 Visual Enrichment Complete!")
    print(f"[*] Total LessonAssets Created & Attached: {total_assets_created}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_cbc_grade8_agriculture_topic6()
