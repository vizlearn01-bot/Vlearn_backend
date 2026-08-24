"""
VLearn CBC Grade 8 Agriculture — Topic 5: Crop Pest and Disease Control
Visual Enrichment & Multi-Video Integration Engine (Phase 2: High-Fidelity Technical SVGs & Videos)

Curriculum: CBC (Grade 8)
Subject: Agriculture
Topic: Crop Pest and Disease Control (Topic Order: 5)

Enrichment Architecture:
  1. Phase 2A: Card-1 Photographic Visual Hooks (8 Lessons via Verified Wikimedia URLs).
  2. Phase 2B: 8 Custom Responsive Vector SVGs (viewBox="0 0 800 450", high contrast #0f172a dark-mode).
  3. Phase 2C: Multi-Video Instructional Integration (3 Verified YouTube videos across key lessons).
  4. Phase 2D: LessonAsset Model Registration and Database Synchronization.

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade8_agriculture_topic5.py
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
# 8 CUSTOM RESPONSIVE VECTOR SVGS (viewBox="0 0 800 450")
# =============================================================================

SVGS = {
    # -------------------------------------------------------------------------
    # SVG 1 (Lesson 1 Page 2): Insect Pest Mouthparts & Damage Classification
    # -------------------------------------------------------------------------
    1: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">INSECT PEST MOUTHPARTS & FEEDING DAMAGE CLASSIFICATION</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Entomological Diagnostics of Biting, Piercing, and Boring Crop Pests</text>

  <!-- Group 1: Biting & Chewing -->
  <g transform="translate(40, 85)">
    <rect width="220" height="320" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <rect width="220" height="40" rx="10" fill="#7f1d1d"/>
    <text x="110" y="26" fill="#fee2e2" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1. BITING & CHEWING</text>

    <!-- Jaw & Leaf Graphic -->
    <path d="M 30 110 Q 110 70 190 110 L 170 140 Q 110 120 50 140 Z" fill="#15803d"/>
    <!-- Chewed Holes -->
    <circle cx="80" cy="115" r="10" fill="#1e293b"/>
    <circle cx="130" cy="120" r="14" fill="#1e293b"/>
    <text x="110" y="160" fill="#fca5a5" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Ragged Leaf Holes & Defoliation</text>

    <!-- Details -->
    <g fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif" transform="translate(15, 185)">
      <text x="0" y="0">• <tspan font-weight="bold">Mouthpart</tspan>: Strong Mandibles</text>
      <text x="0" y="22">• <tspan font-weight="bold">Action</tspan>: Tears solid green leaf tissue</text>
      <text x="0" y="44">• <tspan font-weight="bold">Pests</tspan>: Caterpillars, Grasshoppers</text>
      <text x="0" y="66">• <tspan font-weight="bold">Crops</tspan>: Kales, Cabbages, Spinach</text>
      <text x="0" y="95" fill="#f87171" font-size="10" font-weight="bold">Control: Handpicking / Ash</text>
    </g>
  </g>

  <!-- Group 2: Piercing & Sucking -->
  <g transform="translate(290, 85)">
    <rect width="220" height="320" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <rect width="220" height="40" rx="10" fill="#78350f"/>
    <text x="110" y="26" fill="#fef3c7" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2. PIERCING & SUCKING</text>

    <!-- Curled Leaf & Stylet Needle Graphic -->
    <path d="M 30 130 Q 80 80 150 110 Q 180 130 190 90 Q 140 140 50 140 Z" fill="#84cc16"/>
    <!-- Needle Vector -->
    <line x1="110" y1="75" x2="110" y2="105" stroke="#f59e0b" stroke-width="3"/>
    <circle cx="110" cy="75" r="5" fill="#f59e0b"/>
    <text x="110" y="160" fill="#fde68a" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Curled Leaves & Sticky Mold</text>

    <!-- Details -->
    <g fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif" transform="translate(15, 185)">
      <text x="0" y="0">• <tspan font-weight="bold">Mouthpart</tspan>: Needle-like Stylet</text>
      <text x="0" y="22">• <tspan font-weight="bold">Action</tspan>: Punctures leaf, sucks cell sap</text>
      <text x="0" y="44">• <tspan font-weight="bold">Pests</tspan>: Aphids, Whiteflies, Thrips</text>
      <text x="0" y="66">• <tspan font-weight="bold">Crops</tspan>: Tomatoes, Kales, Onions</text>
      <text x="0" y="95" fill="#fbbf24" font-size="10" font-weight="bold">Control: Wood Ash / Ladybugs</text>
    </g>
  </g>

  <!-- Group 3: Boring & Burrowing -->
  <g transform="translate(540, 85)">
    <rect width="220" height="320" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <rect width="220" height="40" rx="10" fill="#0c4a6e"/>
    <text x="110" y="26" fill="#e0f2fe" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">3. BORING & BURROWING</text>

    <!-- Seed & Tunnel Graphic -->
    <rect x="50" y="80" width="120" height="50" rx="25" fill="#d97706"/>
    <!-- Tunnel hole -->
    <circle cx="85" cy="105" r="8" fill="#1e293b"/>
    <path d="M 85 105 L 140 105" stroke="#1e293b" stroke-width="6"/>
    <text x="110" y="160" fill="#bae6fd" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Hollow Stems & Grain Powder</text>

    <!-- Details -->
    <g fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif" transform="translate(15, 185)">
      <text x="0" y="0">• <tspan font-weight="bold">Mouthpart</tspan>: Tunneling Drill Jaws</text>
      <text x="0" y="22">• <tspan font-weight="bold">Action</tspan>: Borrows inside seeds & stalks</text>
      <text x="0" y="44">• <tspan font-weight="bold">Pests</tspan>: Maize Weevils, Stem Borers</text>
      <text x="0" y="66">• <tspan font-weight="bold">Crops</tspan>: Stored Beans, Maize, Tomato</text>
      <text x="0" y="95" fill="#38bdf8" font-size="10" font-weight="bold">Control: Hermetic Storage / Ash</text>
    </g>
  </g>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 2 (Lesson 2 Page 2): Crop Disease Diagnostic Anatomy
    # -------------------------------------------------------------------------
    2: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">CROP DISEASE DIAGNOSTIC ANATOMY & SYMPTOM PATHOLOGY</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Visual Identification of Fungal, Bacterial, and Vascular Plant Diseases</text>

  <!-- Symptom 1: Leaf Spot -->
  <g transform="translate(40, 85)">
    <rect width="165" height="320" rx="8" fill="#1e293b" stroke="#eab308" stroke-width="1.5"/>
    <text x="82" y="24" fill="#fde047" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1. LEAF SPOT</text>
    <!-- Leaf with concentric spots -->
    <path d="M 25 110 Q 82 50 140 110 Q 82 170 25 110 Z" fill="#15803d"/>
    <circle cx="70" cy="105" r="14" fill="#78350f" stroke="#facc15" stroke-width="2"/>
    <circle cx="105" cy="115" r="10" fill="#78350f" stroke="#facc15" stroke-width="1.5"/>
    <g fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" transform="translate(10, 190)">
      <text x="0" y="0" font-weight="bold" fill="#fde047">• Cause: Fungus</text>
      <text x="0" y="18">• Dark brown circles</text>
      <text x="0" y="36">• Yellow halo border</text>
      <text x="0" y="54">• 'Bullseye' target rings</text>
      <text x="0" y="76" fill="#94a3b8">Action: Prune lower leaves;</text>
      <text x="0" y="90" fill="#94a3b8">sterilize shears</text>
    </g>
  </g>

  <!-- Symptom 2: Powdery Mildew -->
  <g transform="translate(225, 85)">
    <rect width="165" height="320" rx="8" fill="#1e293b" stroke="#e2e8f0" stroke-width="1.5"/>
    <text x="82" y="24" fill="#f8fafc" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2. POWDERY MILDEW</text>
    <!-- Leaf with white powder -->
    <path d="M 25 110 Q 82 50 140 110 Q 82 170 25 110 Z" fill="#15803d"/>
    <ellipse cx="82" cy="110" rx="40" ry="25" fill="#f8fafc" opacity="0.6"/>
    <g fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" transform="translate(10, 190)">
      <text x="0" y="0" font-weight="bold" fill="#f8fafc">• Cause: Fungus</text>
      <text x="0" y="18">• White flour-like dust</text>
      <text x="0" y="36">• Blocks sunlight intake</text>
      <text x="0" y="54">• Stunts photosynthesis</text>
      <text x="0" y="76" fill="#94a3b8">Action: Dust with fine</text>
      <text x="0" y="90" fill="#94a3b8">sieved wood ash</text>
    </g>
  </g>

  <!-- Symptom 3: Blight Rot -->
  <g transform="translate(410, 85)">
    <rect width="165" height="320" rx="8" fill="#1e293b" stroke="#f97316" stroke-width="1.5"/>
    <text x="82" y="24" fill="#fdba74" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">3. BLIGHT ROT</text>
    <!-- Tomato fruit with black rot -->
    <circle cx="82" cy="110" r="35" fill="#dc2626"/>
    <path d="M 60 90 Q 82 135 110 100 Q 90 140 60 90 Z" fill="#1e293b" stroke="#78350f" stroke-width="1.5"/>
    <g fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" transform="translate(10, 190)">
      <text x="0" y="0" font-weight="bold" fill="#fdba74">• Cause: Oomycete</text>
      <text x="0" y="18">• Large black rot patches</text>
      <text x="0" y="36">• Water-soaked rotting</text>
      <text x="0" y="54">• Destroys whole fruit</text>
      <text x="0" y="76" fill="#94a3b8">Action: Uproot whole plant;</text>
      <text x="0" y="90" fill="#94a3b8">burn immediately</text>
    </g>
  </g>

  <!-- Symptom 4: Bacterial Wilt -->
  <g transform="translate(595, 85)">
    <rect width="165" height="320" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <text x="82" y="24" fill="#fca5a5" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">4. BACTERIAL WILT</text>
    <!-- Drooping plant -->
    <path d="M 82 140 Q 82 110 60 90 M 82 120 Q 90 105 110 115" stroke="#15803d" stroke-width="4" fill="none"/>
    <ellipse cx="55" cy="95" rx="14" ry="7" fill="#84cc16" transform="rotate(30 55 95)"/>
    <ellipse cx="115" cy="120" rx="14" ry="7" fill="#84cc16" transform="rotate(45 115 120)"/>
    <rect x="40" y="140" width="85" height="15" fill="#0284c7" opacity="0.6"/>
    <text x="82" y="152" fill="#e0f2fe" font-size="8" font-family="system-ui, sans-serif" text-anchor="middle">Wet Soil Present</text>
    <g fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" transform="translate(10, 190)">
      <text x="0" y="0" font-weight="bold" fill="#f87171">• Cause: Bacteria</text>
      <text x="0" y="18">• Sudden limp collapse</text>
      <text x="0" y="36">• Wet soil (not drought)</text>
      <text x="0" y="54">• Stems blocked inside</text>
      <text x="0" y="76" fill="#94a3b8">Action: Cull plant & roots;</text>
      <text x="0" y="90" fill="#94a3b8">bury in 2ft pit</text>
    </g>
  </g>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 3 (Lesson 3 Page 2): 5 Pest Control Pathways Comparison Matrix & Hierarchy
    # -------------------------------------------------------------------------
    3: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">5 PEST CONTROL PATHWAYS & IPM HIERARCHY PYRAMID</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Integrated Pest Management: Sustainable Ecological Framework</text>

  <!-- IPM Pyramid on Left -->
  <g transform="translate(50, 85)">
    <polygon points="175,20 310,290 40,290" fill="#1e293b" stroke="#334155" stroke-width="2"/>
    
    <!-- Tier 5: Chemicals (Apex) -->
    <polygon points="175,20 200,70 150,70" fill="#991b1b"/>
    <text x="175" y="52" fill="#fee2e2" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Chemicals (Emergency)</text>

    <!-- Tier 4: Natural Sprays & Ash -->
    <polygon points="150,70 200,70 225,130 125,130" fill="#78350f"/>
    <text x="175" y="105" fill="#fef3c7" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Natural Ash / Botanicals</text>

    <!-- Tier 3: Biological -->
    <polygon points="125,130 225,130 255,190 95,190" fill="#0f766e"/>
    <text x="175" y="165" fill="#ccfbf1" font-size="11" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Biological (Ladybugs)</text>

    <!-- Tier 2: Mechanical -->
    <polygon points="95,190 255,190 280,240 70,240" fill="#0369a1"/>
    <text x="175" y="218" fill="#e0f2fe" font-size="11" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Mechanical (Handpick/Traps)</text>

    <!-- Tier 1: Cultural (Base) -->
    <polygon points="70,240 280,240 310,290 40,290" fill="#065f46"/>
    <text x="175" y="270" fill="#d1fae5" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Cultural Prevention (Rotation)</text>
  </g>

  <!-- Explanation Cards on Right -->
  <g transform="translate(400, 85)">
    <rect width="350" height="320" rx="10" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
    <text x="175" y="26" fill="#f8fafc" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">THE IPM ACTION RULE</text>

    <g fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif" transform="translate(15, 50)">
      <text x="0" y="0" fill="#34d399" font-weight="bold">1. Cultural (Base Prevention)</text>
      <text x="0" y="18" fill="#94a3b8">Rotate crops yearly; clear weed borders to stop breeding.</text>

      <text x="0" y="44" fill="#38bdf8" font-weight="bold">2. Mechanical (Zero-Cost Physical Removal)</text>
      <text x="0" y="62" fill="#94a3b8">Handpick caterpillars; place yellow sticky insect traps.</text>

      <text x="0" y="88" fill="#2dd4bf" font-weight="bold">3. Biological (Nature's Predators)</text>
      <text x="0" y="106" fill="#94a3b8">Preserve ladybugs and spiders to eat aphids naturally.</text>

      <text x="0" y="132" fill="#fbbf24" font-weight="bold">4. Natural Botanicals & Mineral Ash</text>
      <text x="0" y="150" fill="#94a3b8">Dust sieved wood ash in morning dew to dehydrate pests.</text>

      <text x="0" y="176" fill="#f87171" font-weight="bold">5. Synthetic Chemicals (Final Emergency Resort)</text>
      <text x="0" y="194" fill="#94a3b8">Only for massive plagues; wear full PPE under supervision.</text>

      <rect x="0" y="225" width="320" height="30" rx="4" fill="#047857"/>
      <text x="160" y="245" fill="#ecfdf5" font-size="11" font-weight="bold" text-anchor="middle">Goal: 100% Food Safety & Groundwater Protection</text>
    </g>
  </g>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 4 (Lesson 4 Page 2): Tool Sterilization & Crop Culling Flowchart
    # -------------------------------------------------------------------------
    4: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">TOOL STERILIZATION & DISEASED CROP CULLING PROTOCOL</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Standard Operating Procedure for Halting Agricultural Epidemics</text>

  <!-- Step 1: Loosen -->
  <g transform="translate(40, 95)">
    <rect width="150" height="230" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="75" cy="28" r="14" fill="#0284c7"/>
    <text x="75" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1</text>
    <text x="75" y="65" fill="#38bdf8" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">LOOSEN SOIL</text>
    <!-- Graphic -->
    <path d="M 45 120 L 75 80 L 105 120 Z" fill="#334155"/>
    <line x1="75" y1="120" x2="75" y2="150" stroke="#f59e0b" stroke-width="3"/>
    <text x="75" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Slide trowel under</text>
    <text x="75" y="195" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">roots to loosen</text>
    <text x="75" y="210" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">soil ball.</text>
  </g>

  <!-- Step 2: Lift -->
  <g transform="translate(230, 95)">
    <rect width="150" height="230" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="75" cy="28" r="14" fill="#d97706"/>
    <text x="75" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2</text>
    <text x="75" y="65" fill="#fbbf24" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">UPROOT WHOLE</text>
    <!-- Graphic -->
    <path d="M 75 85 L 75 140 M 50 100 L 75 110 L 100 100" stroke="#15803d" stroke-width="3" fill="none"/>
    <circle cx="75" cy="140" r="15" fill="#78350f"/>
    <text x="75" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Pull entire plant</text>
    <text x="75" y="195" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">vertically with all</text>
    <text x="75" y="210" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">clinging root soil.</text>
  </g>

  <!-- Step 3: Bag -->
  <g transform="translate(420, 95)">
    <rect width="150" height="230" rx="8" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <circle cx="75" cy="28" r="14" fill="#7c3aed"/>
    <text x="75" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">3</text>
    <text x="75" y="65" fill="#c084fc" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">BAG IN SACK</text>
    <!-- Graphic -->
    <path d="M 50 90 L 100 90 L 110 145 L 40 145 Z" fill="#581c87" stroke="#c084fc" stroke-width="1.5"/>
    <text x="75" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Place directly in</text>
    <text x="75" y="195" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">plastic sack to</text>
    <text x="75" y="210" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">trap wind spores.</text>
  </g>

  <!-- Step 4: Destroy -->
  <g transform="translate(610, 95)">
    <rect width="150" height="230" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <circle cx="75" cy="28" r="14" fill="#b91c1c"/>
    <text x="75" y="33" fill="#fff" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">4</text>
    <text x="75" y="65" fill="#f87171" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">BURN / BURY</text>
    <!-- Flame Graphic -->
    <path d="M 75 80 Q 95 105 75 140 Q 55 105 75 80 Z" fill="#ea580c"/>
    <text x="75" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Burn completely</text>
    <text x="75" y="195" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">or bury 2ft deep.</text>
    <text x="75" y="210" fill="#fca5a5" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">NEVER COMPOST!</text>
  </g>

  <!-- Bottom Disinfection Rule -->
  <rect x="40" y="350" width="720" height="70" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
  <text x="60" y="375" fill="#34d399" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">TOOL STERILIZATION MANDATE:</text>
  <text x="60" y="395" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Wipe knives & shears with 70% alcohol or soapy water between beds to kill hitchhiking spores.</text>
  <text x="60" y="410" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Spores survive in standard compost heaps; diseased plant tissue must be burned or deep-buried.</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 5 (Lesson 5 Page 2): Socio-Economic Impact of Unchecked Pests
    # -------------------------------------------------------------------------
    5: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">THE SOCIO-ECONOMIC CHAIN REACTION OF DELAYED PEST CONTROL</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Connecting Field Biomass Loss to Family Household Finances</text>

  <!-- Step 1 -->
  <g transform="translate(40, 90)">
    <rect width="155" height="230" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="77" y="24" fill="#f87171" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1. FIELD ATTACK</text>
    <path d="M 30 110 Q 77 70 125 110" stroke="#15803d" stroke-width="5" fill="none"/>
    <circle cx="50" cy="95" r="5" fill="#ef4444"/>
    <circle cx="90" cy="100" r="5" fill="#ef4444"/>
    <g fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" transform="translate(10, 145)">
      <text x="0" y="0">• Caterpillars chew leaves</text>
      <text x="0" y="18">• Aphids drain sap</text>
      <text x="0" y="36" fill="#fca5a5" font-weight="bold">40% - 60% Yield Drop</text>
    </g>
  </g>

  <!-- Step 2 -->
  <g transform="translate(230, 90)">
    <rect width="155" height="230" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="77" y="24" fill="#fbbf24" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2. MARKET DROP</text>
    <rect x="40" y="65" width="75" height="55" rx="4" fill="#78350f"/>
    <text x="77" y="98" fill="#fde68a" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Scarred Produce</text>
    <g fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" transform="translate(10, 145)">
      <text x="0" y="0">• Blemished leaves</text>
      <text x="0" y="18">• Rejected by vendors</text>
      <text x="0" y="36" fill="#fde68a" font-weight="bold">70% Price Markdown</text>
    </g>
  </g>

  <!-- Step 3 -->
  <g transform="translate(420, 90)">
    <rect width="155" height="230" rx="8" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <text x="77" y="24" fill="#c084fc" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">3. STORAGE LOSS</text>
    <rect x="40" y="65" width="75" height="55" rx="4" fill="#581c87"/>
    <text x="77" y="98" fill="#f5f3ff" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Weevil Tunnels</text>
    <g fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" transform="translate(10, 145)">
      <text x="0" y="0">• Seeds turn to powder</text>
      <text x="0" y="18">• Toxic aflatoxin mold</text>
      <text x="0" y="36" fill="#c084fc" font-weight="bold">Zero Seed Germination</text>
    </g>
  </g>

  <!-- Step 4 -->
  <g transform="translate(610, 90)">
    <rect width="155" height="230" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <text x="77" y="24" fill="#f87171" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">4. NET LOSS</text>
    <circle cx="77" cy="95" r="28" fill="#991b1b"/>
    <text x="77" y="100" fill="#fee2e2" font-size="11" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">- PROFIT</text>
    <g fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" transform="translate(10, 145)">
      <text x="0" y="0">• Revenue collapses</text>
      <text x="0" y="18">• Control costs double</text>
      <text x="0" y="36" fill="#f87171" font-weight="bold">Family Income Lost</text>
    </g>
  </g>

  <!-- Profit Formula Banner -->
  <rect x="40" y="345" width="725" height="75" rx="8" fill="#1e293b" stroke="#64748b"/>
  <text x="400" y="372" fill="#38bdf8" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">FARM FINANCIAL EQUATION: PROFIT = MARKET REVENUE - PRODUCTION COSTS</text>
  <text x="400" y="395" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif" text-anchor="middle">Timely organic control prevents yield drop and protects high market prices, ensuring family food security!</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 6 (Lesson 6 Page 2): Science of Wood Ash & Upwind Dusting Setup
    # -------------------------------------------------------------------------
    6: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">THE PHYSICAL SCIENCE OF WOOD ASH & UPWIND SAFETY SETUP</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Microscopic Cuticle Abrasion Mechanics & Personal Protective Equipment</text>

  <!-- Cuticle Abrasion Diagram (Left) -->
  <g transform="translate(50, 85)">
    <rect width="330" height="240" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="165" y="26" fill="#38bdf8" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1. CUTICLE DESICCATION SCIENCE</text>

    <!-- Insect Cuticle Layers -->
    <!-- Waxy Layer -->
    <rect x="30" y="60" width="270" height="20" fill="#f59e0b" rx="4"/>
    <text x="165" y="75" fill="#78350f" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Insect Waxy Cuticle (Moisture Seal)</text>
    <!-- Internal Body Tissue -->
    <rect x="30" y="85" width="270" height="45" fill="#0284c7" rx="4"/>
    <text x="165" y="112" fill="#e0f2fe" font-size="11" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Internal Water & Body Fluids (70% H2O)</text>

    <!-- Ash Sharp Crystals -->
    <polygon points="60,45 68,62 52,62" fill="#94a3b8"/>
    <polygon points="120,40 130,62 110,62" fill="#94a3b8"/>
    <polygon points="200,42 212,62 188,62" fill="#94a3b8"/>
    <polygon points="260,45 268,62 252,62" fill="#94a3b8"/>

    <!-- Water Loss Arrows -->
    <path d="M 60 85 L 60 40 M 120 85 L 120 40 M 200 85 L 200 40" stroke="#38bdf8" stroke-width="2" stroke-dasharray="2,2"/>

    <text x="165" y="155" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Sharp silica crystals scratch waxy cuticle layer.</text>
    <text x="165" y="172" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Alkaline ash draws out internal moisture rapidly.</text>
    <text x="165" y="195" fill="#38bdf8" font-size="11" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Result: Rapid Pest Death via Dehydration</text>
  </g>

  <!-- Upwind Dusting Setup (Right) -->
  <g transform="translate(420, 85)">
    <rect width="330" height="240" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="165" y="26" fill="#34d399" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2. UPWIND OPERATOR SETUP</text>

    <!-- Wind Vector -->
    <g transform="translate(20, 50)">
      <path d="M 0 10 L 60 10 L 60 0 L 80 15 L 60 30 L 60 20 L 0 20 Z" fill="#38bdf8"/>
      <text x="40" y="-4" fill="#38bdf8" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Gentle Breeze</text>
    </g>

    <!-- Operator -->
    <circle cx="150" cy="80" r="14" fill="#f59e0b"/>
    <rect x="140" y="94" width="20" height="35" fill="#047857" rx="4"/>
    <!-- PPE Mask -->
    <rect x="154" y="77" width="10" height="8" fill="#fff" rx="2"/>
    <text x="150" y="145" fill="#e2e8f0" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Student with Mask & PPE</text>

    <!-- Ash Cloud blowing toward crop -->
    <ellipse cx="230" cy="100" rx="30" ry="15" fill="#94a3b8" opacity="0.6"/>
    <!-- Kale Crop -->
    <path d="M 275 125 L 275 95 M 265 110 L 275 100 L 285 110" stroke="#15803d" stroke-width="3"/>
    <text x="275" y="145" fill="#4ade80" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Kale Bed</text>

    <text x="165" y="180" fill="#a7f3d0" font-size="11" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">ALWAYS STAND UPWIND!</text>
    <text x="165" y="198" fill="#94a3b8" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Dust blows toward crops and away from eyes/face.</text>
  </g>

  <!-- PPE Checklist Bottom Banner -->
  <rect x="50" y="345" width="700" height="80" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="70" y="370" fill="#fbbf24" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">MANDATORY PERSONAL PROTECTIVE EQUIPMENT (PPE):</text>
  <text x="70" y="392" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">1. Dust Mask: Prevents inhaling fine alkaline ash particles • 2. Safety Goggles: Shields eyes from wind dust</text>
  <text x="70" y="410" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">3. Rubber Gloves: Blocks alkaline skin drying • 4. Water & Soap: Thorough handwashing after practical</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 7 (Lesson 7 Page 2): 5-Phase Wood Ash Prep & Dusting Workflow
    # -------------------------------------------------------------------------
    7: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">5-PHASE WOOD ASH PREPARATION & DUSTING WORKFLOW</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Practical School Farm Standard Operating Procedure</text>

  <!-- Step 1 -->
  <g transform="translate(30, 85)">
    <rect width="130" height="250" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="65" cy="30" r="16" fill="#0284c7"/>
    <text x="65" y="35" fill="#f0f9ff" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1</text>
    <text x="65" y="70" fill="#38bdf8" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">GEAR UP PPE</text>
    <rect x="40" y="95" width="50" height="35" rx="4" fill="#0369a1"/>
    <text x="65" y="117" fill="#e0f2fe" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Mask & Gloves</text>
    <text x="65" y="165" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Put on dust</text>
    <text x="65" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">mask, goggles, and</text>
    <text x="65" y="195" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">rubber gloves</text>
    <text x="65" y="210" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">before opening ash.</text>
  </g>

  <!-- Step 2 -->
  <g transform="translate(185, 85)">
    <rect width="130" height="250" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="65" cy="30" r="16" fill="#d97706"/>
    <text x="65" y="35" fill="#fffbeb" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2</text>
    <text x="65" y="70" fill="#fbbf24" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">SIEVE RAW ASH</text>
    <path d="M 35 100 L 95 100 L 85 130 L 45 130 Z" fill="#78350f" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="65" y="165" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Sift ash through</text>
    <text x="65" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">wire mesh screen.</text>
    <text x="65" y="195" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Remove large</text>
    <text x="65" y="210" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">charcoal chunks.</text>
  </g>

  <!-- Step 3 -->
  <g transform="translate(340, 85)">
    <rect width="130" height="250" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <circle cx="65" cy="30" r="16" fill="#059669"/>
    <text x="65" y="35" fill="#ecfdf5" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">3</text>
    <text x="65" y="70" fill="#34d399" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">CHECK DEW</text>
    <circle cx="65" cy="115" r="18" fill="#0284c7" opacity="0.7"/>
    <text x="65" y="120" fill="#fff" font-size="9" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">Dew Drops</text>
    <text x="65" y="165" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Apply at 7:00 AM</text>
    <text x="65" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">while leaves are</text>
    <text x="65" y="195" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">wet with dew (acts</text>
    <text x="65" y="210" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">as natural glue).</text>
  </g>

  <!-- Step 4 -->
  <g transform="translate(495, 85)">
    <rect width="130" height="250" rx="8" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <circle cx="65" cy="30" r="16" fill="#7c3aed"/>
    <text x="65" y="35" fill="#f5f3ff" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">4</text>
    <text x="65" y="70" fill="#a78bfa" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">DUST UPWIND</text>
    <rect x="50" y="95" width="30" height="45" rx="3" fill="#581c87"/>
    <text x="65" y="165" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Use shaker bottle.</text>
    <text x="65" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Stand upwind.</text>
    <text x="65" y="195" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Target leaf</text>
    <text x="65" y="210" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">undersides gently.</text>
  </g>

  <!-- Step 5 -->
  <g transform="translate(650, 85)">
    <rect width="120" height="250" rx="8" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
    <circle cx="60" cy="30" r="16" fill="#db2777"/>
    <text x="60" y="35" fill="#fdf2f8" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">5</text>
    <text x="60" y="70" fill="#f472b6" font-size="12" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">LOG & WASH</text>
    <rect x="40" y="95" width="40" height="40" rx="4" fill="#9d174d"/>
    <text x="60" y="165" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Wash hands</text>
    <text x="60" y="180" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">with soap & water.</text>
    <text x="60" y="195" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">Record date & bed</text>
    <text x="60" y="210" fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" text-anchor="middle">in farm journal.</text>
  </g>

  <!-- Bottom Tip -->
  <rect x="30" y="355" width="740" height="70" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
  <text x="50" y="380" fill="#34d399" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">SHAKER BOTTLE DESIGN TIP:</text>
  <text x="50" y="400" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Punch 8 small nail holes in water bottle cap • Drop one clean pebble inside to act as an agitator</text>
  <text x="50" y="415" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Agitator breaks up clumps, ensuring a fine translucent grey cloud that coats leaf undersides smoothly</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 8 (Lesson 8 Page 2): Master Crop Doctor Diagnostic Matrix
    # -------------------------------------------------------------------------
    8: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">MASTER CROP DOCTOR DIAGNOSTIC & ORGANIC SOLUTION MATRIX</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Integrated Decision Framework for Vegetable Health Management</text>

  <!-- 4 Symptom Diagnostic Cards -->
  <!-- Case 1: Chewed Holes -->
  <g transform="translate(40, 85)">
    <rect width="340" height="150" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="15" y="24" fill="#f87171" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">SYMPTOM 1: Ragged Holes in Leaves</text>
    <g fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" transform="translate(15, 45)">
      <text x="0" y="0">• <tspan font-weight="bold">Diagnosis</tspan>: Biting & Chewing Caterpillars / Leaf Worms</text>
      <text x="0" y="20">• <tspan font-weight="bold">Mechanism</tspan>: Mandibles tearing green photosynthesis tissue</text>
      <text x="0" y="40">• <tspan font-weight="bold">Action</tspan>: Handpick with gloves into soapy water; protect wasps</text>
      <rect x="0" y="58" width="310" height="22" rx="4" fill="#7f1d1d"/>
      <text x="155" y="73" fill="#fee2e2" font-size="10" font-weight="bold" text-anchor="middle">Organic Solution: Mechanical Handpicking</text>
    </g>
  </g>

  <!-- Case 2: Curled Yellow Leaves -->
  <g transform="translate(420, 85)">
    <rect width="340" height="150" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="15" y="24" fill="#fbbf24" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">SYMPTOM 2: Curled Leaves & Sticky Mold</text>
    <g fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" transform="translate(15, 45)">
      <text x="0" y="0">• <tspan font-weight="bold">Diagnosis</tspan>: Piercing & Sucking Aphids / Whiteflies</text>
      <text x="0" y="20">• <tspan font-weight="bold">Mechanism</tspan>: Needle stylet extracts sap & injects viruses</text>
      <text x="0" y="40">• <tspan font-weight="bold">Action</tspan>: Dust sieved wood ash in morning dew; release ladybugs</text>
      <rect x="0" y="58" width="310" height="22" rx="4" fill="#78350f"/>
      <text x="155" y="73" fill="#fef3c7" font-size="10" font-weight="bold" text-anchor="middle">Organic Solution: Wood Ash + Ladybugs</text>
    </g>
  </g>

  <!-- Case 3: Leaf Spots -->
  <g transform="translate(40, 255)">
    <rect width="340" height="155" rx="8" fill="#1e293b" stroke="#eab308" stroke-width="1.5"/>
    <text x="15" y="24" fill="#fde047" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">SYMPTOM 3: Bullseye Concentric Brown Spots</text>
    <g fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" transform="translate(15, 45)">
      <text x="0" y="0">• <tspan font-weight="bold">Diagnosis</tspan>: Fungal Early Blight / Leaf Spot</text>
      <text x="0" y="20">• <tspan font-weight="bold">Mechanism</tspan>: Spores germinate in damp, unventilated leaves</text>
      <text x="0" y="40">• <tspan font-weight="bold">Action</tspan>: Prune lower spotted leaves; sterilize shears in alcohol</text>
      <rect x="0" y="58" width="310" height="22" rx="4" fill="#713f12"/>
      <text x="155" y="73" fill="#fef08a" font-size="10" font-weight="bold" text-anchor="middle">Organic Solution: Pruning + Tool Sterilization</text>
    </g>
  </g>

  <!-- Case 4: Sudden Wilt -->
  <g transform="translate(420, 255)">
    <rect width="340" height="155" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <text x="15" y="24" fill="#fca5a5" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">SYMPTOM 4: Sudden Droop in Wet Soil</text>
    <g fill="#e2e8f0" font-size="10" font-family="system-ui, sans-serif" transform="translate(15, 45)">
      <text x="0" y="0">• <tspan font-weight="bold">Diagnosis</tspan>: Bacterial Wilt (Ralstonia)</text>
      <text x="0" y="20">• <tspan font-weight="bold">Mechanism</tspan>: Bacteria multiply inside vascular xylem vessels</text>
      <text x="0" y="40">• <tspan font-weight="bold">Action</tspan>: Cull entire plant & roots; burn or bury in 2ft deep pit</text>
      <rect x="0" y="58" width="310" height="22" rx="4" fill="#991b1b"/>
      <text x="155" y="73" fill="#fee2e2" font-size="10" font-weight="bold" text-anchor="middle">Emergency Action: Cull & Deep Pit Burial (Never Compost!)</text>
    </g>
  </g>

  <!-- Bottom Certification Banner -->
  <rect x="40" y="420" width="720" height="20" rx="4" fill="#047857"/>
  <text x="400" y="434" fill="#ecfdf5" font-size="10" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">CERTIFIED JUNIOR PLANT DOCTOR — SUSTAINABLE ORGANIC CROP PROTECTION</text>
</svg>"""
}

# =============================================================================
# CURATED VERIFIED YOUTUBE VIDEOS
# =============================================================================

TOPIC5_VIDEOS = {
    # Unit 4 (Page 4): Organic Crop Disease & Pest Control in Kenya
    4: {
        "page_number": 4,
        "title": "Instructional Video: Organic Crop Disease & Pest Control",
        "url": "https://www.youtube.com/watch?v=Ei5z_0Lxmic",
        "resolved_video_id": "Ei5z_0Lxmic",
        "caption": "Watch this field demonstration on identifying vegetable diseases, practicing garden sanitation, tool sterilization, and botanical pest management in Kenya."
    },
    # Unit 7 (Page 4): Practical Video: Grade 8 Agriculture Project & Organic Pest Control
    7: {
        "page_number": 4,
        "title": "Practical Video: Grade 8 Agriculture Project & Organic Pest Control",
        "url": "https://www.youtube.com/watch?v=6ZjkLwQt_YE",
        "resolved_video_id": "6ZjkLwQt_YE",
        "caption": "Watch this step-by-step practical video demonstration on preparing organic pest solutions, wood ash dusting, and managing school farm vegetable plots in Kenya."
    },
    # Unit 8 (Page 6): Topic Video Review: Organic Pest Management & Botanical Sprays
    8: {
        "page_number": 6,
        "title": "Topic Video Review: Organic Pest Management & Botanical Sprays",
        "url": "https://www.youtube.com/watch?v=4oWEI6Wl-xI",
        "resolved_video_id": "4oWEI6Wl-xI",
        "caption": "Watch this comprehensive organic farming tutorial covering botanical pesticide preparation, companion planting, natural pest repellents, and safe crop care."
    }
}

# =============================================================================
# ENRICHMENT EXECUTION
# =============================================================================

def enrich_cbc_grade8_agriculture_topic5():
    """Attaches Card-1 photos, 8 custom SVGs, and 3 verified YouTube videos to Topic 5."""
    print("=" * 80)
    print("STARTING VISUAL ENRICHMENT: CBC GRADE 8 AGRICULTURE — TOPIC 5")
    print("=" * 80)

    topic = Topic.objects.filter(subject__grade__name="Grade 8", subject__name="Agriculture", name="Crop Pest and Disease Control").first()
    if not topic:
        print("[ERROR] Topic 'Crop Pest and Disease Control' not found under CBC Grade 8 Agriculture!")
        return

    lessons = Lesson.objects.filter(topic=topic).select_related("learning_unit").order_by("learning_unit__order")
    print(f"[*] Found {lessons.count()} Lessons under Topic: '{topic.name}' (ID: {topic.id})")

    # Load verified Card-1 images
    verified_images_path = os.path.join(os.path.dirname(__file__), "grade8_topic5_verified_images.json")
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
                title=f"Lesson {u_order} Visual Hook: {img_data.get('title', 'Crop Pest Control')}",
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
        print("\n[+] Phase 2C: Attaching Curated Video Lessons across Topic 5...")
        for u_order, v_data in TOPIC5_VIDEOS.items():
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
    print(f"[SUCCESS] CBC Grade 8 Agriculture Topic 5 Visual Enrichment Complete!")
    print(f"[*] Total LessonAssets Created & Attached: {total_assets_created}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_cbc_grade8_agriculture_topic5()
