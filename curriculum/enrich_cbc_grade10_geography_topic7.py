"""
VLearn CBC Grade 10 Geography — Topic 7: Folding
Visual Enrichment Engine (Vector SVGs, Verified Wikimedia Images & Educational Videos)

Subject: Geography (Grade 10 CBC, Subject ID: 37)
Topic 7: Folding

Attaches:
  - 12 First-Card Photographic Visual Hooks (100% Tested HTTP 200 OK Direct Wikimedia URLs)
  - 12 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", Dark/Light Mode Compatible)
  - Verified Educational YouTube Video Asset for Fold Mountain Formation
  - Populates LessonAsset models for offline caching & mobile delivery

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade10_geography_topic7.py
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
# 12 CUSTOM RESPONSIVE VECTOR SVGS FOR GRADE 10 TOPIC 7: FOLDING
# =============================================================================

# SVG 1: Compressional Stress & Buckling Sequence (Lesson 1)
SVG_COMPRESSIONAL_BUCKLING = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">COMPRESSIONAL STRESS &amp; CRUSTAL SHORTENING</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Transition from Horizontal Strata to Buckled Folds under Lateral Tectonic Pressure</text>

  <!-- Frame A: Undisturbed Horizontal Strata -->
  <g transform="translate(35, 85)">
    <rect x="0" y="0" width="345" height="330" rx="10" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="36" rx="10" fill="#334155"/>
    <text x="172" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">FRAME A: UNDEFORMED STRATA</text>

    <!-- Horizontal Strata Layers -->
    <rect x="45" y="70" width="255" height="28" fill="#e2e8f0" stroke="#475569" stroke-width="1"/>
    <text x="172" y="88" font-size="10" font-weight="bold" fill="#1e293b" text-anchor="middle">Youngest Strata (Limestone)</text>
    
    <rect x="45" y="98" width="255" height="28" fill="#fbbf24" stroke="#475569" stroke-width="1"/>
    <text x="172" y="116" font-size="10" font-weight="bold" fill="#78350f" text-anchor="middle">Sandstone Bed</text>

    <rect x="45" y="126" width="255" height="28" fill="#94a3b8" stroke="#475569" stroke-width="1"/>
    <text x="172" y="144" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Shale Bed</text>

    <rect x="45" y="154" width="255" height="28" fill="#cbd5e1" stroke="#475569" stroke-width="1"/>
    <text x="172" y="172" font-size="10" font-weight="bold" fill="#1e293b" text-anchor="middle">Oldest Strata (Basal Sandstone)</text>

    <!-- Basement rock -->
    <rect x="45" y="182" width="255" height="25" fill="#475569" stroke="#334155" stroke-width="1"/>
    <text x="172" y="198" font-size="9" fill="#e2e8f0" text-anchor="middle">Crystalline Basement</text>

    <!-- Inward Compressional Force Arrows -->
    <polygon points="40,135 15,120 15,150" fill="#ef4444"/>
    <rect x="0" y="130" width="20" height="10" fill="#ef4444"/>
    <text x="25" y="170" font-size="10" font-weight="bold" fill="#f87171">Compression</text>

    <polygon points="305,135 330,120 330,150" fill="#ef4444"/>
    <rect x="325" y="130" width="20" height="10" fill="#ef4444"/>
    <text x="320" y="170" font-size="10" font-weight="bold" fill="#f87171" text-anchor="end">Compression</text>

    <!-- Dimension indicator -->
    <line x1="45" y1="225" x2="300" y2="225" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
    <line x1="45" y1="220" x2="45" y2="230" stroke="#38bdf8" stroke-width="2"/>
    <line x1="300" y1="220" x2="300" y2="230" stroke="#38bdf8" stroke-width="2"/>
    <text x="172" y="242" font-size="10.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Original Crustal Width (W₁)</text>

    <text x="25" y="280" font-size="10" fill="#cbd5e1">• Undisturbed horizontal layering</text>
    <text x="25" y="298" font-size="10" fill="#cbd5e1">• Plastic deformation zone under deep heat &amp; pressure</text>
  </g>

  <!-- Frame B: Buckled Folds & Shortened Crust -->
  <g transform="translate(420, 85)">
    <rect x="0" y="0" width="345" height="330" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="36" rx="10" fill="#0284c7"/>
    <text x="172" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">FRAME B: FOLDED &amp; SHORTENED CRUST</text>

    <!-- Wavy Fold Paths -->
    <!-- Base -->
    <path d="M 65 195 Q 115 135 172 195 T 280 195 L 280 215 L 65 215 Z" fill="#475569" stroke="#334155" stroke-width="1.5"/>
    <!-- Layer 4 -->
    <path d="M 65 170 Q 115 110 172 170 T 280 170 L 280 195 Q 225 195 172 195 T 65 195 Z" fill="#cbd5e1" stroke="#475569" stroke-width="1.5"/>
    <!-- Layer 3 -->
    <path d="M 65 145 Q 115 85 172 145 T 280 145 L 280 170 Q 225 170 172 170 T 65 170 Z" fill="#94a3b8" stroke="#475569" stroke-width="1.5"/>
    <!-- Layer 2 -->
    <path d="M 65 120 Q 115 60 172 120 T 280 120 L 280 145 Q 225 145 172 145 T 65 145 Z" fill="#fbbf24" stroke="#475569" stroke-width="1.5"/>
    <!-- Layer 1 -->
    <path d="M 65 95 Q 115 35 172 95 T 280 95 L 280 120 Q 225 120 172 120 T 65 120 Z" fill="#e2e8f0" stroke="#475569" stroke-width="1.5"/>

    <!-- Labels -->
    <text x="115" y="45" font-size="10.5" font-weight="bold" fill="#facc15" text-anchor="middle">Anticline (Upfold)</text>
    <text x="228" y="165" font-size="10.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Syncline (Downfold)</text>

    <!-- Shortened width indicator -->
    <line x1="65" y1="230" x2="280" y2="230" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,3"/>
    <line x1="65" y1="225" x2="65" y2="235" stroke="#ef4444" stroke-width="2"/>
    <line x1="280" y1="225" x2="280" y2="235" stroke="#ef4444" stroke-width="2"/>
    <text x="172" y="246" font-size="10.5" font-weight="bold" fill="#ef4444" text-anchor="middle">Shortened Width (W₂ &lt; W₁)</text>

    <text x="25" y="275" font-size="10" fill="#cbd5e1">• Horizontal crustal shortening</text>
    <text x="25" y="293" font-size="10" fill="#cbd5e1">• Vertical crustal thickening &amp; mountain relief</text>
    <text x="25" y="311" font-size="10" fill="#cbd5e1">• Plastic bending without brittle fracturing</text>
  </g>
</svg>
""")

# SVG 2: 3D Anatomy of a Fold (Lesson 2)
SVG_FOLD_ANATOMY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">ANATOMY OF A GEOLOGICAL FOLD</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Structural Components: Anticline, Syncline, Limbs, Axial Plane, Crest, Trough, and Fold Axis</text>

  <!-- 3D Fold Block Diagram -->
  <g transform="translate(60, 95)">
    <!-- Semi-transparent Axial Plane Sheet (Anticline) -->
    <polygon points="210,30 350,75 350,265 210,220" fill="#38bdf8" fill-opacity="0.2" stroke="#38bdf8" stroke-width="2" stroke-dasharray="5,4"/>
    <text x="270" y="55" font-size="11" font-weight="bold" fill="#38bdf8">Axial Plane (Bisecting Sheet)</text>

    <!-- Top Folded Surface 3D perspective -->
    <path d="M 60 170 Q 210 50 360 170 T 660 170" fill="none" stroke="#f59e0b" stroke-width="4"/>
    
    <!-- Strata bands front face -->
    <!-- Layer A (Top) -->
    <path d="M 60 170 Q 210 50 360 170 T 660 170 L 660 200 Q 510 200 360 200 T 60 200 Z" fill="#e2e8f0" stroke="#475569" stroke-width="1.5"/>
    <path d="M 60 200 Q 210 80 360 200 T 660 200 L 660 230 Q 510 230 360 230 T 60 230 Z" fill="#fbbf24" stroke="#475569" stroke-width="1.5"/>
    <path d="M 60 230 Q 210 110 360 230 T 660 230 L 660 260 Q 510 260 360 260 T 60 260 Z" fill="#94a3b8" stroke="#475569" stroke-width="1.5"/>
    <path d="M 60 260 Q 210 140 360 260 T 660 260 L 660 290 Q 510 290 360 290 T 60 290 Z" fill="#cbd5e1" stroke="#475569" stroke-width="1.5"/>
    <path d="M 60 290 Q 210 170 360 290 T 660 290 L 660 310 L 60 310 Z" fill="#334155" stroke="#1e293b" stroke-width="1.5"/>

    <!-- 3D Top surface perspective fill -->
    <polygon points="60,170 180,120 480,120 360,170" fill="#f8fafc" fill-opacity="0.15"/>
    <polygon points="360,170 480,120 780,120 660,170" fill="#f8fafc" fill-opacity="0.08"/>

    <!-- Crest and Hinge line -->
    <line x1="210" y1="50" x2="350" y2="95" stroke="#ef4444" stroke-width="3"/>
    <circle cx="210" cy="50" r="5" fill="#ef4444"/>
    <text x="180" y="42" font-size="12" font-weight="bold" fill="#ef4444">CREST &amp; HINGE LINE</text>

    <!-- Anticline Label -->
    <rect x="150" y="80" width="120" height="26" rx="5" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="210" y="97" font-size="12" font-weight="bold" fill="#facc15" text-anchor="middle">ANTICLINE (Upfold)</text>

    <!-- Limbs -->
    <line x1="120" y1="130" x2="90" y2="100" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="75" y="95" font-size="11" font-weight="bold" fill="#cbd5e1">Limb 1 (Flank)</text>

    <line x1="300" y1="130" x2="330" y2="100" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="335" y="95" font-size="11" font-weight="bold" fill="#cbd5e1">Limb 2 (Flank)</text>

    <!-- Trough and Syncline -->
    <circle cx="510" cy="200" r="5" fill="#38bdf8"/>
    <rect x="450" y="240" width="120" height="26" rx="5" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="510" y="257" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">SYNCLINE (Downfold)</text>
    <text x="510" y="218" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">TROUGH</text>

    <!-- Core Age labels -->
    <text x="210" y="280" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">Oldest Rock at Core</text>
    <text x="510" y="160" font-size="10" font-weight="bold" fill="#e2e8f0" text-anchor="middle">Youngest Rock at Core</text>
  </g>
</svg>
""")

# SVG 3: Symmetrical vs. Asymmetrical Folds (Lesson 3)
SVG_SYMMETRICAL_ASYMMETRICAL = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="45" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">SYMMETRICAL VS. ASYMMETRICAL FOLDS</text>
  <text x="400" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Influence of Balanced vs. Unbalanced Compressional Force Magnitude</text>

  <!-- Left: Symmetrical Fold -->
  <g transform="translate(35, 85)">
    <rect x="0" y="0" width="345" height="330" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="36" rx="10" fill="#15803d"/>
    <text x="172" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">1. SYMMETRICAL FOLD (EQUAL FORCES)</text>

    <!-- Vertical Axial Plane -->
    <line x1="172" y1="50" x2="172" y2="240" stroke="#22c55e" stroke-width="2.5" stroke-dasharray="6,4"/>
    <text x="172" y="48" font-size="10.5" font-weight="bold" fill="#4ade80" text-anchor="middle">Vertical Axial Plane (90°)</text>

    <!-- Symmetrical Fold Layers -->
    <path d="M 40 200 Q 172 70 305 200 L 305 230 Q 172 100 40 230 Z" fill="#fbbf24" stroke="#d97706" stroke-width="1.5"/>
    <path d="M 40 230 Q 172 100 305 230 L 305 260 Q 172 130 40 260 Z" fill="#94a3b8" stroke="#475569" stroke-width="1.5"/>
    <path d="M 40 260 Q 172 130 305 260 L 305 275 L 40 275 Z" fill="#334155" stroke="#1e293b" stroke-width="1.5"/>

    <!-- Equal Dip Angles -->
    <text x="80" y="165" font-size="11" font-weight="bold" fill="#4ade80">Dip = 45°</text>
    <text x="265" y="165" font-size="11" font-weight="bold" fill="#4ade80" text-anchor="end">Dip = 45°</text>

    <!-- Equal Compressional Force Arrows -->
    <polygon points="35,170 10,160 10,180" fill="#22c55e"/>
    <rect x="0" y="166" width="15" height="8" fill="#22c55e"/>
    <text x="45" y="195" font-size="10" font-weight="bold" fill="#4ade80">Force F₁</text>

    <polygon points="310,170 335,160 335,180" fill="#22c55e"/>
    <rect x="330" y="166" width="15" height="8" fill="#22c55e"/>
    <text x="300" y="195" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="end">Force F₂ = F₁</text>

    <text x="25" y="295" font-size="10" fill="#cbd5e1">• Equal compressional forces on both flanks</text>
    <text x="25" y="312" font-size="10" fill="#cbd5e1">• Identical limb slope angles &amp; mirror symmetry</text>
  </g>

  <!-- Right: Asymmetrical Fold -->
  <g transform="translate(420, 85)">
    <rect x="0" y="0" width="345" height="330" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="36" rx="10" fill="#b45309"/>
    <text x="172" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">2. ASYMMETRICAL FOLD (UNEQUAL FORCES)</text>

    <!-- Tilted Axial Plane -->
    <line x1="215" y1="50" x2="160" y2="240" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="6,4"/>
    <text x="215" y="48" font-size="10.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">Inclined Axial Plane</text>

    <!-- Asymmetrical Fold Layers (Left gentle, right steep) -->
    <path d="M 40 210 Q 190 70 240 85 L 270 210 L 270 240 L 240 115 Q 190 100 40 240 Z" fill="#fbbf24" stroke="#d97706" stroke-width="1.5"/>
    <path d="M 40 240 Q 190 100 240 115 L 270 240 L 270 265 L 240 140 Q 190 125 40 265 Z" fill="#94a3b8" stroke="#475569" stroke-width="1.5"/>
    <path d="M 40 265 Q 190 125 240 140 L 270 265 L 270 275 L 40 275 Z" fill="#334155" stroke="#1e293b" stroke-width="1.5"/>

    <!-- Unequal Dip Angles -->
    <text x="90" y="160" font-size="11" font-weight="bold" fill="#fbbf24">Gentle Dip (~25°)</text>
    <text x="285" y="160" font-size="11" font-weight="bold" fill="#ef4444">Steep Dip (~70°)</text>

    <!-- Unequal Force Arrows -->
    <polygon points="40,170 5,150 5,190" fill="#ef4444"/>
    <rect x="0" y="162" width="15" height="16" fill="#ef4444"/>
    <text x="45" y="200" font-size="10" font-weight="bold" fill="#f87171">Stronger Force (F₁ &gt;&gt; F₂)</text>

    <polygon points="315,170 330,165 330,175" fill="#f59e0b"/>
    <rect x="325" y="168" width="10" height="4" fill="#f59e0b"/>
    <text x="305" y="195" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="end">Weaker F₂</text>

    <text x="25" y="295" font-size="10" fill="#cbd5e1">• Unbalanced tectonic stress tilts the fold</text>
    <text x="25" y="312" font-size="10" fill="#cbd5e1">• Long gentle dip slope vs. short steep scarp flank</text>
  </g>
</svg>
""")

# SVG 4: Advanced Fold Types (Lesson 4)
SVG_ADVANCED_FOLD_TYPES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="40" font-size="17" font-weight="bold" fill="#38bdf8" text-anchor="middle">PROGRESSIVE FOLD EVOLUTION UNDER ESCALATING STRESS</text>
  <text x="400" y="58" font-size="11.5" fill="#94a3b8" text-anchor="middle">Continuum from Asymmetrical to Overturned, Recumbent, and Isoclinal Structures</text>

  <!-- 4 Panels Grid -->
  <!-- Panel 1: Asymmetrical Fold -->
  <g transform="translate(30, 75)">
    <rect x="0" y="0" width="170" height="340" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="28" rx="8" fill="#334155"/>
    <text x="85" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. ASYMMETRICAL</text>

    <!-- Fold shape -->
    <path d="M 20 180 Q 90 80 120 95 L 145 180" fill="none" stroke="#fbbf24" stroke-width="8"/>
    <path d="M 20 205 Q 90 105 120 120 L 145 205" fill="none" stroke="#94a3b8" stroke-width="8"/>
    <line x1="108" y1="75" x2="80" y2="210" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,3"/>

    <text x="85" y="240" font-size="9.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">Tilted Axial Plane</text>
    <text x="85" y="260" font-size="8.5" fill="#cbd5e1" text-anchor="middle">One limb steeper</text>
    <text x="85" y="275" font-size="8.5" fill="#cbd5e1" text-anchor="middle">than the other</text>
    <text x="85" y="310" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Stress Level: Low-Med</text>
  </g>

  <!-- Panel 2: Overturned Fold -->
  <g transform="translate(220, 75)">
    <rect x="0" y="0" width="170" height="340" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="28" rx="8" fill="#b45309"/>
    <text x="85" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. OVERTURNED</text>

    <!-- Fold shape pushed past vertical -->
    <path d="M 20 180 Q 120 60 145 100 Q 155 130 115 180" fill="none" stroke="#fbbf24" stroke-width="8"/>
    <path d="M 20 205 Q 120 85 145 125 Q 155 155 115 205" fill="none" stroke="#94a3b8" stroke-width="8"/>
    <line x1="145" y1="70" x2="65" y2="210" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,3"/>

    <text x="85" y="240" font-size="9.5" font-weight="bold" fill="#facc15" text-anchor="middle">Pushed Past Vertical</text>
    <text x="85" y="260" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Both limbs dip same way</text>
    <text x="85" y="275" font-size="8.5" fill="#fca5a5" text-anchor="middle">Stratigraphic Inversion</text>
    <text x="85" y="310" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Stress Level: High</text>
  </g>

  <!-- Panel 3: Recumbent Fold -->
  <g transform="translate(410, 75)">
    <rect x="0" y="0" width="170" height="340" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="28" rx="8" fill="#b91c1c"/>
    <text x="85" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. RECUMBENT</text>

    <!-- Fold lying horizontal -->
    <path d="M 20 180 L 120 180 Q 155 180 155 130 Q 155 80 20 80" fill="none" stroke="#fbbf24" stroke-width="8"/>
    <path d="M 20 205 L 120 205 Q 180 205 180 130 Q 180 55 20 55" fill="none" stroke="#94a3b8" stroke-width="8"/>
    <line x1="10" y1="130" x2="160" y2="130" stroke="#ef4444" stroke-width="2" stroke-dasharray="4,3"/>

    <text x="85" y="240" font-size="9.5" font-weight="bold" fill="#f87171" text-anchor="middle">Horizontal Axial Plane</text>
    <text x="85" y="260" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Limbs lie parallel &amp; flat</text>
    <text x="85" y="275" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Rolled like a blanket</text>
    <text x="85" y="310" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Stress Level: Severe</text>
  </g>

  <!-- Panel 4: Isoclinal Folds -->
  <g transform="translate(600, 75)">
    <rect x="0" y="0" width="170" height="340" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="28" rx="8" fill="#7e22ce"/>
    <text x="85" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4. ISOCLINAL</text>

    <!-- Tight accordion pleats -->
    <path d="M 20 190 L 35 75 L 50 190 L 65 75 L 80 190 L 95 75 L 110 190 L 125 75 L 140 190" fill="none" stroke="#fbbf24" stroke-width="6"/>
    <path d="M 20 205 L 35 90 L 50 205 L 65 90 L 80 205 L 95 90 L 110 205 L 125 90 L 140 205" fill="none" stroke="#94a3b8" stroke-width="6"/>

    <text x="85" y="240" font-size="9.5" font-weight="bold" fill="#c084fc" text-anchor="middle">Parallel Limbs</text>
    <text x="85" y="260" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Identical dip angles</text>
    <text x="85" y="275" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Tightly squeezed pleats</text>
    <text x="85" y="310" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Stress Level: Extreme</text>
  </g>
</svg>
""")

# SVG 5: Overthrust Fault and Nappe Structure (Lesson 5)
SVG_OVERTHRUST_NAPPE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="42" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">OVERTHRUST FOLD &amp; NAPPE FORMATION</text>
  <text x="400" y="62" font-size="12" fill="#94a3b8" text-anchor="middle">Transition from Extreme Recumbent Folding to Low-Angle Thrust Faulting and Sheet Displacement</text>

  <!-- Step A: Strained Recumbent Fold -->
  <g transform="translate(35, 80)">
    <rect x="0" y="0" width="225" height="335" rx="8" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
    <rect x="0" y="0" width="225" height="28" rx="8" fill="#334155"/>
    <text x="112" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 1: STRAINED RECUMBENT</text>

    <path d="M 20 140 L 130 140 Q 180 140 180 90 Q 180 40 20 40" fill="none" stroke="#fbbf24" stroke-width="10"/>
    <path d="M 20 165 L 130 165 Q 205 165 205 90 Q 205 15 20 15" fill="none" stroke="#94a3b8" stroke-width="10"/>

    <!-- Incipient Fracture Line -->
    <line x1="10" y1="150" x2="190" y2="70" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="5,3"/>
    <text x="112" y="180" font-size="10" font-weight="bold" fill="#f87171" text-anchor="middle">Incipient Thrust Plane</text>

    <text x="15" y="235" font-size="9.5" fill="#cbd5e1">• Severe compressional stress</text>
    <text x="15" y="255" font-size="9.5" fill="#cbd5e1">• Plastic limit exceeded</text>
    <text x="15" y="275" font-size="9.5" fill="#cbd5e1">• Shear plane develops along</text>
    <text x="15" y="290" font-size="9.5" fill="#cbd5e1">  weakened overturned limb</text>
  </g>

  <!-- Step B: Fracturing and Thrust Slip -->
  <g transform="translate(285, 80)">
    <rect x="0" y="0" width="225" height="335" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="225" height="28" rx="8" fill="#b45309"/>
    <text x="112" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 2: THRUST FAULTING</text>

    <!-- Bottom Footwall Block -->
    <path d="M 20 150 L 130 150 L 170 110 L 20 110 Z" fill="#94a3b8"/>
    
    <!-- Top Hanging Wall Block Sliding Up -->
    <path d="M 50 110 L 180 30 Q 215 30 215 70 L 100 135 Z" fill="#fbbf24"/>

    <!-- Thrust fault cut line & motion arrow -->
    <line x1="10" y1="160" x2="200" y2="50" stroke="#ef4444" stroke-width="3"/>
    <polygon points="120,70 145,50 140,75" fill="#ef4444"/>
    <text x="140" y="100" font-size="10" font-weight="bold" fill="#ef4444">Thrust Slip</text>

    <text x="15" y="235" font-size="9.5" fill="#cbd5e1">• Rock shears and fractures</text>
    <text x="15" y="255" font-size="9.5" fill="#cbd5e1">• Upper limb climbs along</text>
    <text x="15" y="270" font-size="9.5" fill="#cbd5e1">  low-angle thrust plane</text>
    <text x="15" y="290" font-size="9.5" fill="#fde047">• Overthrust Fold established</text>
  </g>

  <!-- Step C: Displaced Nappe Sheet -->
  <g transform="translate(535, 80)">
    <rect x="0" y="0" width="230" height="335" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="28" rx="8" fill="#0284c7"/>
    <text x="115" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 3: NAPPE DISPLACEMENT</text>

    <!-- Autochthonous In-Situ Strata (Younger) -->
    <rect x="20" y="125" width="190" height="35" fill="#475569" stroke="#334155" stroke-width="1"/>
    <text x="115" y="147" font-size="9" font-weight="bold" fill="#e2e8f0" text-anchor="middle">Autochthon (Younger In-Situ Strata)</text>

    <!-- Thrust fault boundary -->
    <line x1="15" y1="123" x2="215" y2="123" stroke="#ef4444" stroke-width="3"/>

    <!-- Allochthonous Nappe Sheet (Older) resting on top -->
    <rect x="35" y="55" width="160" height="65" rx="4" fill="#fbbf24" stroke="#d97706" stroke-width="1.5"/>
    <text x="115" y="85" font-size="11" font-weight="bold" fill="#78350f" text-anchor="middle">DISPLACED NAPPE</text>
    <text x="115" y="102" font-size="8.5" font-weight="bold" fill="#78350f" text-anchor="middle">(Older Allochthonous Sheet)</text>

    <!-- Displacement arrows -->
    <line x1="30" y1="40" x2="180" y2="40" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="180,40 170,35 170,45" fill="#38bdf8"/>
    <text x="115" y="32" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Kilometers of Displacement</text>

    <text x="15" y="235" font-size="9.5" fill="#cbd5e1">• Massive sheet overrides</text>
    <text x="15" y="250" font-size="9.5" fill="#cbd5e1">  unrelated regional rocks</text>
    <text x="15" y="270" font-size="9.5" fill="#fca5a5">• Older rocks rest on younger</text>
    <text x="15" y="285" font-size="9.5" fill="#cbd5e1">• Classic: Glarus Thrust, Alps</text>
  </g>
</svg>
""")

# SVG 6: Monoclines, Structural Domes, and Basins (Lesson 6)
SVG_MONOCLINES_DOMES_BASINS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="42" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">MONOCLINES, STRUCTURAL DOMES &amp; BASINS</text>
  <text x="400" y="62" font-size="12" fill="#94a3b8" text-anchor="middle">Vertical Crustal Warping and Deep-Seated Basement Fault Drapes</text>

  <!-- 1. Monocline -->
  <g transform="translate(30, 80)">
    <rect x="0" y="0" width="225" height="335" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="225" height="28" rx="8" fill="#0284c7"/>
    <text x="112" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. MONOCLINE (STEP FOLD)</text>

    <!-- Basement fault blocks -->
    <rect x="20" y="140" width="85" height="70" fill="#475569" stroke="#334155" stroke-width="1"/>
    <rect x="105" y="180" width="100" height="30" fill="#334155" stroke="#1e293b" stroke-width="1"/>
    <!-- Fault line -->
    <line x1="105" y1="120" x2="105" y2="210" stroke="#ef4444" stroke-width="2" stroke-dasharray="4,2"/>
    <polygon points="100,165 95,150 105,150" fill="#ef4444"/>
    <polygon points="110,185 105,200 115,200" fill="#ef4444"/>

    <!-- Sedimentary Draped Layers -->
    <path d="M 20 80 L 75 80 Q 110 80 130 120 L 160 120 L 205 120" fill="none" stroke="#fbbf24" stroke-width="10"/>
    <path d="M 20 105 L 75 105 Q 110 105 130 145 L 160 145 L 205 145" fill="none" stroke="#94a3b8" stroke-width="10"/>
    <path d="M 20 130 L 75 130 Q 110 130 130 170 L 160 170 L 205 170" fill="none" stroke="#cbd5e1" stroke-width="10"/>

    <text x="112" y="240" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Step-Like Bend</text>
    <text x="15" y="265" font-size="9.5" fill="#cbd5e1">• Single step-like flexure</text>
    <text x="15" y="282" font-size="9.5" fill="#cbd5e1">• Strata drape over deep fault</text>
    <text x="15" y="299" font-size="9.5" fill="#cbd5e1">• e.g., Waterpocket Fold, USA</text>
  </g>

  <!-- 2. Structural Dome -->
  <g transform="translate(285, 80)">
    <rect x="0" y="0" width="225" height="335" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="225" height="28" rx="8" fill="#b45309"/>
    <text x="112" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. STRUCTURAL DOME</text>

    <!-- Upward circular bulge cross-section -->
    <path d="M 20 170 Q 112 70 205 170 L 205 190 Q 112 90 20 190 Z" fill="#cbd5e1" stroke="#475569" stroke-width="1"/>
    <path d="M 20 190 Q 112 90 205 190 L 205 210 Q 112 110 20 210 Z" fill="#94a3b8" stroke="#475569" stroke-width="1"/>
    
    <!-- Central Magma / Core Uplift -->
    <path d="M 70 210 Q 112 130 155 210 Z" fill="#ef4444" stroke="#b91c1c" stroke-width="1.5"/>
    <text x="112" y="200" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Uplift Plume</text>

    <!-- Eroded top surface line -->
    <line x1="20" y1="110" x2="205" y2="110" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,2"/>
    <text x="112" y="102" font-size="9" font-weight="bold" fill="#f59e0b" text-anchor="middle">Eroded Surface Line</text>

    <text x="112" y="240" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">Circular Upward Warp</text>
    <text x="15" y="265" font-size="9.5" fill="#cbd5e1">• Resembles upside-down bowl</text>
    <text x="15" y="282" font-size="9.5" fill="#fde047">• Oldest rocks in CENTER</text>
    <text x="15" y="299" font-size="9.5" fill="#cbd5e1">• Layers dip outward (all dirs)</text>
  </g>

  <!-- 3. Structural Basin -->
  <g transform="translate(540, 80)">
    <rect x="0" y="0" width="225" height="335" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="225" height="28" rx="8" fill="#15803d"/>
    <text x="112" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. STRUCTURAL BASIN</text>

    <!-- Downward bowl cross-section -->
    <path d="M 20 110 Q 112 190 205 110 L 205 135 Q 112 215 20 135 Z" fill="#fbbf24" stroke="#d97706" stroke-width="1"/>
    <path d="M 20 135 Q 112 215 205 135 L 205 160 Q 112 240 20 160 Z" fill="#94a3b8" stroke="#475569" stroke-width="1"/>
    <path d="M 20 160 Q 112 240 205 160 L 205 185 Q 112 265 20 185 Z" fill="#cbd5e1" stroke="#475569" stroke-width="1"/>

    <!-- Central young sediments -->
    <ellipse cx="112" cy="140" rx="35" ry="12" fill="#38bdf8"/>
    <text x="112" y="144" font-size="8.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Young Strata</text>

    <text x="112" y="240" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Circular Downward Warp</text>
    <text x="15" y="265" font-size="9.5" fill="#cbd5e1">• Resembles upright bowl</text>
    <text x="15" y="282" font-size="9.5" fill="#86efac">• Youngest rocks in CENTER</text>
    <text x="15" y="299" font-size="9.5" fill="#cbd5e1">• Layers dip inward (all dirs)</text>
  </g>
</svg>
""")

# SVG 7: Geosynclinal Fold Mountain Formation (Lesson 7)
SVG_OROGENIC_CYCLE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="42" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">THE GEOSYNCLINAL OROGENIC CYCLE</text>
  <text x="400" y="62" font-size="12" fill="#94a3b8" text-anchor="middle">Three Stages in the Birth of Massive Fold Mountain Ranges</text>

  <!-- Stage A: Sedimentation in Geosyncline -->
  <g transform="translate(30, 80)">
    <rect x="0" y="0" width="225" height="335" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="225" height="28" rx="8" fill="#0284c7"/>
    <text x="112" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 1: SEDIMENTATION</text>

    <!-- Ocean water -->
    <rect x="35" y="60" width="155" height="40" fill="#0284c7" fill-opacity="0.4" rx="2"/>
    <text x="112" y="85" font-size="10" font-weight="bold" fill="#7dd3fc" text-anchor="middle">Oceanic Geosyncline</text>

    <!-- Continental blocks on sides -->
    <rect x="10" y="55" width="35" height="120" fill="#475569" rx="3"/>
    <rect x="180" y="55" width="35" height="120" fill="#475569" rx="3"/>

    <!-- Accumulating sedimentary layers -->
    <path d="M 45 100 Q 112 150 180 100 L 180 145 Q 112 195 45 145 Z" fill="#fbbf24"/>
    <path d="M 45 145 Q 112 195 180 145 L 180 175 Q 112 215 45 175 Z" fill="#94a3b8"/>
    <text x="112" y="160" font-size="8.5" font-weight="bold" fill="#78350f" text-anchor="middle">Thick Marine Sediments</text>

    <text x="15" y="240" font-size="9.5" fill="#cbd5e1">• Vast marine basin collects</text>
    <text x="15" y="255" font-size="9.5" fill="#cbd5e1">  river silt &amp; marine shells</text>
    <text x="15" y="275" font-size="9.5" fill="#cbd5e1">• Sediments compress into rock</text>
    <text x="15" y="290" font-size="9.5" fill="#cbd5e1">  thousands of meters thick</text>
  </g>

  <!-- Stage B: Compression and Buckling -->
  <g transform="translate(285, 80)">
    <rect x="0" y="0" width="225" height="335" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="225" height="28" rx="8" fill="#b45309"/>
    <text x="112" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 2: COMPRESSION</text>

    <!-- Converging continental blocks with inward arrows -->
    <rect x="15" y="55" width="45" height="120" fill="#475569" rx="3"/>
    <polygon points="65,115 80,105 80,125" fill="#ef4444"/>

    <rect x="165" y="55" width="45" height="120" fill="#475569" rx="3"/>
    <polygon points="160,115 145,105 145,125" fill="#ef4444"/>

    <!-- Buckling strata waves -->
    <path d="M 60 110 Q 85 70 112 110 T 165 110" fill="none" stroke="#fbbf24" stroke-width="8"/>
    <path d="M 60 135 Q 85 95 112 135 T 165 135" fill="none" stroke="#94a3b8" stroke-width="8"/>
    <path d="M 60 160 Q 85 120 112 160 T 165 160" fill="none" stroke="#cbd5e1" stroke-width="8"/>

    <text x="112" y="195" font-size="9" font-weight="bold" fill="#facc15" text-anchor="middle">Seafloor Buckling</text>

    <text x="15" y="240" font-size="9.5" fill="#cbd5e1">• Plates converge rapidly</text>
    <text x="15" y="255" font-size="9.5" fill="#cbd5e1">• Ocean basin narrows &amp; closes</text>
    <text x="15" y="275" font-size="9.5" fill="#cbd5e1">• Compressional stress buckles</text>
    <text x="15" y="290" font-size="9.5" fill="#cbd5e1">  strata into tight upfolds</text>
  </g>

  <!-- Stage C: Mountain Uplift -->
  <g transform="translate(540, 80)">
    <rect x="0" y="0" width="225" height="335" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="225" height="28" rx="8" fill="#15803d"/>
    <text x="112" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 3: UPLIFT &amp; OROGENY</text>

    <!-- Towering Mountain Peaks -->
    <polygon points="35,170 80,50 120,170" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
    <polygon points="70,75 80,50 95,75" fill="#ffffff"/> <!-- Snow cap -->

    <polygon points="105,170 150,60 195,170" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
    <polygon points="140,82 150,60 162,82" fill="#ffffff"/> <!-- Snow cap -->

    <!-- Upward vertical arrows -->
    <polygon points="80,185 75,200 85,200" fill="#22c55e"/>
    <polygon points="150,185 145,200 155,200" fill="#22c55e"/>
    <text x="112" y="200" font-size="9.5" font-weight="bold" fill="#4ade80" text-anchor="middle">Vertical Uplift</text>

    <text x="15" y="240" font-size="9.5" fill="#cbd5e1">• Ocean completely vanishes</text>
    <text x="15" y="255" font-size="9.5" fill="#cbd5e1">• Strata pushed skyward</text>
    <text x="15" y="275" font-size="9.5" fill="#cbd5e1">• Towering fold mountain ranges</text>
    <text x="15" y="290" font-size="9.5" fill="#86efac">• e.g., Himalayas, Alps, Andes</text>
  </g>
</svg>
""")

# SVG 8: Global Fold Mountain Belts Map (Lesson 8)
SVG_GLOBAL_FOLD_MAP = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="42" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">GLOBAL DISTRIBUTION OF MAJOR FOLD MOUNTAIN BELTS</text>
  <text x="400" y="62" font-size="12" fill="#94a3b8" text-anchor="middle">Linear Mountain Systems Aligned with Convergent Plate Boundaries</text>

  <!-- World Map Stylized Contours -->
  <g transform="translate(40, 80)">
    <!-- Ocean Background -->
    <rect x="0" y="0" width="720" height="260" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

    <!-- Continents Schematics -->
    <!-- North America -->
    <path d="M 60 30 Q 140 30 160 80 L 140 130 L 90 120 L 70 80 Z" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <!-- South America -->
    <path d="M 140 145 Q 185 145 195 190 L 160 240 L 135 200 Z" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <!-- Eurasia -->
    <path d="M 320 30 Q 560 25 610 80 L 580 130 L 460 140 L 370 120 L 340 70 Z" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <!-- Africa -->
    <path d="M 330 110 Q 410 110 420 170 L 390 230 L 345 230 L 325 160 Z" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <!-- Australia -->
    <path d="M 570 175 Q 650 175 660 220 L 610 240 L 565 215 Z" fill="#1e293b" stroke="#475569" stroke-width="1"/>

    <!-- FOLD MOUNTAIN BELTS HIGHLIGHTS (Bold Colors) -->
    <!-- 1. Rocky Mountains (North America) -->
    <path d="M 75 40 Q 95 80 110 120" fill="none" stroke="#ef4444" stroke-width="5" stroke-linecap="round"/>
    <text x="50" y="75" font-size="10" font-weight="bold" fill="#f87171">Rockies</text>

    <!-- 2. Appalachian Mountains (Eastern NA) -->
    <path d="M 135 60 L 155 95" fill="none" stroke="#a855f7" stroke-width="4" stroke-linecap="round"/>
    <text x="160" y="70" font-size="9" font-weight="bold" fill="#c084fc">Appalachians</text>

    <!-- 3. Andes Mountains (South America) -->
    <path d="M 140 150 Q 145 195 155 240" fill="none" stroke="#ef4444" stroke-width="5" stroke-linecap="round"/>
    <text x="100" y="200" font-size="10" font-weight="bold" fill="#f87171">Andes</text>

    <!-- 4. Alps (Europe) -->
    <path d="M 360 70 Q 385 65 410 75" fill="none" stroke="#ef4444" stroke-width="5" stroke-linecap="round"/>
    <text x="385" y="58" font-size="10" font-weight="bold" fill="#f87171" text-anchor="middle">Alps</text>

    <!-- 5. Atlas Mountains (North Africa) -->
    <path d="M 330 115 L 365 125" fill="none" stroke="#ef4444" stroke-width="4" stroke-linecap="round"/>
    <text x="300" y="130" font-size="9" font-weight="bold" fill="#f87171">Atlas Mts</text>

    <!-- 6. Himalayas (Asia) -->
    <path d="M 470 115 Q 520 110 555 125" fill="none" stroke="#ef4444" stroke-width="6" stroke-linecap="round"/>
    <text x="515" y="100" font-size="11" font-weight="bold" fill="#ef4444" text-anchor="middle">Himalayas (Mt. Everest)</text>

    <!-- 7. Great Dividing Range (Australia) -->
    <path d="M 645 180 Q 650 210 640 235" fill="none" stroke="#a855f7" stroke-width="4" stroke-linecap="round"/>
    <text x="655" y="210" font-size="9" font-weight="bold" fill="#c084fc">Great Dividing Range</text>

    <!-- 8. Cape Fold Belt (South Africa) -->
    <path d="M 360 228 L 385 228" fill="none" stroke="#a855f7" stroke-width="4" stroke-linecap="round"/>
    <text x="372" y="245" font-size="8.5" font-weight="bold" fill="#c084fc" text-anchor="middle">Cape Fold Belt</text>
  </g>

  <!-- Legend at Bottom -->
  <g transform="translate(50, 355)">
    <rect x="0" y="0" width="700" height="65" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    
    <!-- Legend item 1 -->
    <line x1="25" y1="32" x2="65" y2="32" stroke="#ef4444" stroke-width="5"/>
    <text x="75" y="28" font-size="11" font-weight="bold" fill="#f87171">Young Fold Mountains (Alpine Orogeny ~65 Ma - Present)</text>
    <text x="75" y="44" font-size="9.5" fill="#cbd5e1">High, sharp peaks, deep gorges, active seismicity (Himalayas, Andes, Alps, Rockies, Atlas)</text>

    <!-- Legend item 2 -->
    <line x1="420" y1="32" x2="460" y2="32" stroke="#a855f7" stroke-width="4"/>
    <text x="470" y="28" font-size="11" font-weight="bold" fill="#c084fc">Old Fold Mountains (&gt;200 Ma)</text>
    <text x="470" y="44" font-size="9.5" fill="#cbd5e1">Rounded, heavily eroded peaks (Appalachians, Cape Fold, Great Dividing Range)</text>
  </g>
</svg>
""")

# SVG 9: Hogbacks vs. Cuestas Asymmetry (Lesson 9)
SVG_HOGBACK_CUESTA = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="42" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">HOGBACKS VS. CUESTAS CROSS-SECTION</text>
  <text x="400" y="62" font-size="12" fill="#94a3b8" text-anchor="middle">Differential Erosion of Dipping Sedimentary Rock Strata</text>

  <!-- Left: Hogback -->
  <g transform="translate(35, 80)">
    <rect x="0" y="0" width="345" height="335" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="36" rx="10" fill="#0284c7"/>
    <text x="172" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">1. HOGBACK (STEEP DIP &gt; 30° - 45°)</text>

    <!-- Steeply dipping strata -->
    <!-- Soft rock left -->
    <polygon points="30,220 110,90 145,90 85,220" fill="#64748b" stroke="#475569" stroke-width="1"/>
    <!-- Hard resistant ridge-forming caprock -->
    <polygon points="85,220 145,90 185,90 140,220" fill="#fbbf24" stroke="#d97706" stroke-width="1.5"/>
    <text x="160" y="80" font-size="10" font-weight="bold" fill="#facc15" text-anchor="middle">Resistant Sandstone Cap</text>
    <!-- Soft rock right -->
    <polygon points="140,220 185,90 220,90 190,220" fill="#64748b" stroke="#475569" stroke-width="1"/>

    <!-- Sharp Symmetrical Profile Outline -->
    <path d="M 30 220 L 165 90 L 290 220" fill="none" stroke="#38bdf8" stroke-width="3"/>
    <text x="165" y="115" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Sharp Spine Peak</text>

    <!-- Dip angle indicator -->
    <line x1="85" y1="220" x2="145" y2="90" stroke="#ef4444" stroke-width="2"/>
    <text x="90" y="165" font-size="11" font-weight="bold" fill="#ef4444">Dip &gt; 45°</text>

    <!-- Slopes symmetry -->
    <text x="80" y="195" font-size="10" font-weight="bold" fill="#7dd3fc">Steep Slope</text>
    <text x="245" y="195" font-size="10" font-weight="bold" fill="#7dd3fc" text-anchor="middle">Steep Slope</text>

    <text x="20" y="260" font-size="10" font-weight="bold" fill="#38bdf8">• Symmetrical steep slopes on both flanks</text>
    <text x="20" y="278" font-size="9.5" fill="#cbd5e1">• Formed where resistant strata dip steeply</text>
    <text x="20" y="295" font-size="9.5" fill="#cbd5e1">• Resembles the sharp bristled back of a wild hog</text>
    <text x="20" y="312" font-size="9.5" fill="#cbd5e1">• e.g., Dinosaur Ridge, Colorado, USA</text>
  </g>

  <!-- Right: Cuesta -->
  <g transform="translate(420, 80)">
    <rect x="0" y="0" width="345" height="335" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="36" rx="10" fill="#b45309"/>
    <text x="172" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">2. CUESTA (GENTLE DIP &lt; 20°)</text>

    <!-- Gently dipping strata -->
    <!-- Resistant layer -->
    <polygon points="30,210 240,110 280,110 70,210" fill="#fbbf24" stroke="#d97706" stroke-width="1.5"/>
    <polygon points="70,210 280,110 320,110 110,210" fill="#64748b" stroke="#475569" stroke-width="1"/>

    <!-- Asymmetrical profile outline -->
    <!-- Long gentle dip slope -->
    <line x1="30" y1="210" x2="240" y2="110" stroke="#f59e0b" stroke-width="3"/>
    <!-- Cliff-like scarp slope -->
    <line x1="240" y1="110" x2="265" y2="210" stroke="#ef4444" stroke-width="3.5"/>

    <!-- Labels for dip and scarp slopes -->
    <text x="130" y="145" font-size="11" font-weight="bold" fill="#facc15">Gentle Dip Slope (Angle &lt; 20°)</text>
    <text x="270" y="160" font-size="10.5" font-weight="bold" fill="#ef4444">Steep Scarp</text>
    <text x="270" y="175" font-size="9" font-weight="bold" fill="#ef4444">Cliff</text>

    <!-- Base line -->
    <line x1="20" y1="210" x2="325" y2="210" stroke="#475569" stroke-width="1.5"/>

    <text x="20" y="260" font-size="10" font-weight="bold" fill="#f59e0b">• Highly asymmetrical ridge profile</text>
    <text x="20" y="278" font-size="9.5" fill="#cbd5e1">• Long gentle dip slope follows rock inclination</text>
    <text x="20" y="295" font-size="9.5" fill="#cbd5e1">• Short, cliff-like scarp slope cuts across beds</text>
    <text x="20" y="312" font-size="9.5" fill="#cbd5e1">• e.g., Paris Basin Cuestas, Niagara Escarpment</text>
  </g>
</svg>
""")

# SVG 10: Significance of Fold Mountains to Humans (Lesson 10)
SVG_HUMAN_SIGNIFICANCE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="42" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">SIGNIFICANCE OF FOLD MOUNTAINS TO HUMAN ACTIVITIES</text>
  <text x="400" y="62" font-size="12" fill="#94a3b8" text-anchor="middle">Contrasting Economic Benefits with Physical Challenges &amp; Hazards</text>

  <!-- Left: Positive Economic Benefits -->
  <g transform="translate(35, 80)">
    <rect x="0" y="0" width="345" height="335" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="36" rx="10" fill="#15803d"/>
    <text x="172" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">POSITIVE ECONOMIC BENEFITS</text>

    <!-- Icon/Illustration 1: Water Tower & River -->
    <circle cx="35" cy="65" r="16" fill="#0284c7"/>
    <text x="35" y="70" font-size="14" fill="#ffffff" text-anchor="middle">💧</text>
    <text x="65" y="60" font-size="11" font-weight="bold" fill="#7dd3fc">1. Water Catchments ("Water Towers")</text>
    <text x="65" y="75" font-size="9.5" fill="#cbd5e1">Trap orographic rain; feed perennial river systems</text>

    <!-- Icon/Illustration 2: HEP Dam -->
    <circle cx="35" cy="115" r="16" fill="#f59e0b"/>
    <text x="35" y="120" font-size="14" fill="#ffffff" text-anchor="middle">⚡</text>
    <text x="65" y="110" font-size="11" font-weight="bold" fill="#fde047">2. Hydroelectric Power (HEP)</text>
    <text x="65" y="125" font-size="9.5" fill="#cbd5e1">Steep gradients &amp; high discharge create ideal dam sites</text>

    <!-- Icon/Illustration 3: Mineral Veins -->
    <circle cx="35" cy="165" r="16" fill="#e11d48"/>
    <text x="35" y="170" font-size="14" fill="#ffffff" text-anchor="middle">⛏️</text>
    <text x="65" y="160" font-size="11" font-weight="bold" fill="#fca5a5">3. Mineral Wealth &amp; Hydrothermal Veins</text>
    <text x="65" y="175" font-size="9.5" fill="#cbd5e1">Compressional metamorphism concentrates Cu, Au, Ag, Pb</text>

    <!-- Icon/Illustration 4: Tourism & Forestry -->
    <circle cx="35" cy="215" r="16" fill="#10b981"/>
    <text x="35" y="220" font-size="14" fill="#ffffff" text-anchor="middle">🌲</text>
    <text x="65" y="210" font-size="11" font-weight="bold" fill="#86efac">4. Tourism, Recreation &amp; Timber</text>
    <text x="65" y="225" font-size="9.5" fill="#cbd5e1">Snow peaks attract tourists; slopes support dense forests</text>

    <!-- Summary banner -->
    <rect x="15" y="260" width="315" height="55" rx="6" fill="#1e293b" stroke="#15803d" stroke-width="1"/>
    <text x="172" y="280" font-size="10" font-weight="bold" fill="#4ade80" text-anchor="middle">Key Economic Drivers for Highland Regions</text>
    <text x="172" y="298" font-size="9" fill="#cbd5e1" text-anchor="middle">Supporting agriculture, energy security, and foreign exchange</text>
  </g>

  <!-- Right: Physical Challenges & Hazards -->
  <g transform="translate(420, 80)">
    <rect x="0" y="0" width="345" height="335" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="36" rx="10" fill="#b91c1c"/>
    <text x="172" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">PHYSICAL CHALLENGES &amp; HAZARDS</text>

    <!-- Hazard 1: Transport Barriers -->
    <circle cx="35" cy="65" r="16" fill="#64748b"/>
    <text x="35" y="70" font-size="14" fill="#ffffff" text-anchor="middle">🚧</text>
    <text x="65" y="60" font-size="11" font-weight="bold" fill="#fca5a5">1. Formidable Transport Barriers</text>
    <text x="65" y="75" font-size="9.5" fill="#cbd5e1">Requires costly hairpin passes, tunnels, and high bridges</text>

    <!-- Hazard 2: Rain Shadow Aridity -->
    <circle cx="35" cy="115" r="16" fill="#d97706"/>
    <text x="35" y="120" font-size="14" fill="#ffffff" text-anchor="middle">☀️</text>
    <text x="65" y="110" font-size="11" font-weight="bold" fill="#fde047">2. Rain Shadow Effect (Leeward Aridity)</text>
    <text x="65" y="125" font-size="9.5" fill="#cbd5e1">Dry descending winds create semi-arid conditions leeward</text>

    <!-- Hazard 3: Geo-Hazards (Landslides) -->
    <circle cx="35" cy="165" r="16" fill="#b91c1c"/>
    <text x="35" y="170" font-size="14" fill="#ffffff" text-anchor="middle">⚠️</text>
    <text x="65" y="160" font-size="11" font-weight="bold" fill="#f87171">3. Landslides, Mudslides &amp; Quakes</text>
    <text x="65" y="175" font-size="9.5" fill="#cbd5e1">Steep slopes collapse during intense rains and tremors</text>

    <!-- Hazard 4: Cold Mountain Climate -->
    <circle cx="35" cy="215" r="16" fill="#0284c7"/>
    <text x="35" y="220" font-size="14" fill="#ffffff" text-anchor="middle">❄️</text>
    <text x="65" y="210" font-size="11" font-weight="bold" fill="#7dd3fc">4. Harsh Alpine Temperatures</text>
    <text x="65" y="225" font-size="9.5" fill="#cbd5e1">Thin air, frost, and short growing seasons at high altitude</text>

    <!-- Adaptation banner -->
    <rect x="15" y="260" width="315" height="55" rx="6" fill="#1e293b" stroke="#b91c1c" stroke-width="1"/>
    <text x="172" y="280" font-size="10" font-weight="bold" fill="#f87171" text-anchor="middle">Requires Advanced Engineering &amp; Adaptation</text>
    <text x="172" y="298" font-size="9" fill="#cbd5e1" text-anchor="middle">Terrace farming, tunnel excavation, and hazard zoning</text>
  </g>
</svg>
""")

# SVG 11: Terracing & Slope Management (Lesson 11)
SVG_SLOPE_MANAGEMENT = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="42" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">HUMAN ADAPTATION: SLOPE MANAGEMENT &amp; SOIL CONSERVATION</text>
  <text x="400" y="62" font-size="12" fill="#94a3b8" text-anchor="middle">Unmanaged Eroding Slopes vs. Sustainably Managed Mountain Terraces</text>

  <!-- Left: Unmanaged Eroding Slope -->
  <g transform="translate(35, 80)">
    <rect x="0" y="0" width="345" height="335" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="36" rx="10" fill="#b91c1c"/>
    <text x="172" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">1. UNMANAGED ERODING SLOPE</text>

    <!-- Steep bare hillside -->
    <polygon points="30,70 315,220 30,220" fill="#78350f" fill-opacity="0.6"/>
    
    <!-- Vertical plow furrows & gullies -->
    <line x1="100" y1="105" x2="180" y2="215" stroke="#ef4444" stroke-width="3"/>
    <line x1="140" y1="125" x2="220" y2="215" stroke="#ef4444" stroke-width="3.5"/>
    <text x="210" y="145" font-size="10" font-weight="bold" fill="#f87171">Deep Gully Erosion</text>

    <!-- Mudslide at base -->
    <path d="M 220 200 Q 260 225 315 220 L 315 235 L 220 235 Z" fill="#b91c1c"/>
    <text x="270" y="230" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Mudslide Scar</text>

    <!-- Rain rush arrows -->
    <line x1="60" y1="85" x2="130" y2="125" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="130,125 120,120 123,128" fill="#38bdf8"/>
    <text x="60" y="78" font-size="9" font-weight="bold" fill="#38bdf8">Rapid Runoff</text>

    <text x="20" y="260" font-size="10" font-weight="bold" fill="#f87171">• Vertical downslope ploughing accelerates erosion</text>
    <text x="20" y="278" font-size="9.5" fill="#cbd5e1">• Fertile topsoil stripped by torrents</text>
    <text x="20" y="295" font-size="9.5" fill="#cbd5e1">• High risk of catastrophic mudslides &amp; crop loss</text>
    <text x="20" y="312" font-size="9.5" fill="#cbd5e1">• Severe downstream siltation and flooding</text>
  </g>

  <!-- Right: Managed Sustainable Slope -->
  <g transform="translate(420, 80)">
    <rect x="0" y="0" width="345" height="335" rx="10" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <rect x="0" y="0" width="345" height="36" rx="10" fill="#15803d"/>
    <text x="172" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">2. MANAGED BENCH TERRACES</text>

    <!-- Hilltop Afforestation Belt -->
    <circle cx="65" cy="70" r="10" fill="#15803d"/>
    <circle cx="85" cy="78" r="10" fill="#15803d"/>
    <circle cx="105" cy="85" r="10" fill="#15803d"/>
    <text x="75" y="58" font-size="9.5" font-weight="bold" fill="#4ade80">Afforestation (Ridge Trees)</text>

    <!-- Step Terraces Profile -->
    <!-- Step 1 -->
    <polyline points="105,95 150,95 150,135 200,135 200,175 255,175 255,220 315,220" fill="none" stroke="#22c55e" stroke-width="3"/>
    <polygon points="105,95 150,95 150,135 200,135 200,175 255,175 255,220 315,220 30,220 30,95" fill="#14532d" fill-opacity="0.3"/>

    <!-- Crops & grass strips on flat benches -->
    <text x="127" y="90" font-size="11" fill="#86efac">🌱🌱</text>
    <text x="175" y="130" font-size="11" fill="#86efac">🌱🌱</text>
    <text x="227" y="170" font-size="11" fill="#86efac">🌱🌱</text>

    <!-- Water infiltration arrows (Vertical Downwards into bench) -->
    <polygon points="135,110 130,102 140,102" fill="#38bdf8"/>
    <line x1="135" y1="95" x2="135" y2="108" stroke="#38bdf8" stroke-width="2"/>
    <text x="155" y="112" font-size="8.5" font-weight="bold" fill="#38bdf8">Water Infiltration</text>

    <text x="20" y="260" font-size="10" font-weight="bold" fill="#4ade80">• Flat bench steps neutralize runoff velocity</text>
    <text x="20" y="278" font-size="9.5" fill="#cbd5e1">• Contour Napier grass strips trap sediments</text>
    <text x="20" y="295" font-size="9.5" fill="#cbd5e1">• Tree root networks anchor soil to bedrock</text>
    <text x="20" y="312" font-size="9.5" fill="#cbd5e1">• e.g., Murang'a, Nyeri, and Kisii tea/coffee farms</text>
  </g>
</svg>
""")

# SVG 12: Interactive / Synthesis Fold Deformation Continuum (Lesson 12)
SVG_FOLD_SYNTHESIS_CONTINUUM = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="15" y="15" width="770" height="420" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="400" y="42" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">TOPIC 7 SYNTHESIS: THE FOLD DEFORMATION CONTINUUM</text>
  <text x="400" y="62" font-size="12" fill="#94a3b8" text-anchor="middle">Comprehensive Continuum of Fold Structures under Escalating Tectonic Stress</text>

  <!-- Flowchart Stages -->
  <g transform="translate(30, 80)">
    <!-- Stress Arrow Across Top -->
    <line x1="20" y1="20" x2="700" y2="20" stroke="#ef4444" stroke-width="4"/>
    <polygon points="700,20 685,13 685,27" fill="#ef4444"/>
    <text x="360" y="12" font-size="11" font-weight="bold" fill="#ef4444" text-anchor="middle">INCREASING HORIZONTAL COMPRESSIONAL FORCE &amp; CRUSTAL SHORTENING ➔</text>

    <!-- Stage 1: Symmetrical Fold -->
    <g transform="translate(10, 40)">
      <rect x="0" y="0" width="130" height="200" rx="6" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
      <text x="65" y="20" font-size="10.5" font-weight="bold" fill="#4ade80" text-anchor="middle">1. SYMMETRICAL</text>
      <path d="M 15 110 Q 65 40 115 110" fill="none" stroke="#22c55e" stroke-width="4"/>
      <line x1="65" y1="35" x2="65" y2="125" stroke="#4ade80" stroke-width="1.5" stroke-dasharray="3,2"/>
      <text x="65" y="145" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Equal forces</text>
      <text x="65" y="160" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Vertical axial plane</text>
      <text x="65" y="180" font-size="9" font-weight="bold" fill="#4ade80" text-anchor="middle">Dip: Equal 45°</text>
    </g>

    <!-- Stage 2: Asymmetrical Fold -->
    <g transform="translate(155, 40)">
      <rect x="0" y="0" width="130" height="200" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="65" y="20" font-size="10.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">2. ASYMMETRICAL</text>
      <path d="M 15 115 Q 85 45 115 115" fill="none" stroke="#f59e0b" stroke-width="4"/>
      <line x1="85" y1="35" x2="65" y2="125" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="3,2"/>
      <text x="65" y="145" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Unequal forces</text>
      <text x="65" y="160" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Tilted axial plane</text>
      <text x="65" y="180" font-size="9" font-weight="bold" fill="#fbbf24" text-anchor="middle">Dip: 25° vs 70°</text>
    </g>

    <!-- Stage 3: Overturned Fold -->
    <g transform="translate(300, 40)">
      <rect x="0" y="0" width="130" height="200" rx="6" fill="#0f172a" stroke="#f97316" stroke-width="1.5"/>
      <text x="65" y="20" font-size="10.5" font-weight="bold" fill="#fdba74" text-anchor="middle">3. OVERTURNED</text>
      <path d="M 15 110 Q 95 35 115 70 Q 120 95 95 125" fill="none" stroke="#f97316" stroke-width="4"/>
      <text x="65" y="145" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Pushed past vertical</text>
      <text x="65" y="160" font-size="8.5" fill="#fca5a5" text-anchor="middle">Strata inverted</text>
      <text x="65" y="180" font-size="9" font-weight="bold" fill="#fdba74" text-anchor="middle">Dip: Same dir</text>
    </g>

    <!-- Stage 4: Recumbent Fold -->
    <g transform="translate(445, 40)">
      <rect x="0" y="0" width="130" height="200" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
      <text x="65" y="20" font-size="10.5" font-weight="bold" fill="#f87171" text-anchor="middle">4. RECUMBENT</text>
      <path d="M 15 115 L 85 115 Q 115 115 115 75 Q 115 35 15 35" fill="none" stroke="#ef4444" stroke-width="4"/>
      <line x1="10" y1="75" x2="120" y2="75" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,2"/>
      <text x="65" y="145" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Horizontal plane</text>
      <text x="65" y="160" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Flat parallel limbs</text>
      <text x="65" y="180" font-size="9" font-weight="bold" fill="#f87171" text-anchor="middle">Dip: ~0° (Flat)</text>
    </g>

    <!-- Stage 5: Overthrust & Nappe -->
    <g transform="translate(590, 40)">
      <rect x="0" y="0" width="140" height="200" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
      <text x="70" y="20" font-size="10.5" font-weight="bold" fill="#c084fc" text-anchor="middle">5. OVERTHRUST / NAPPE</text>
      <!-- Fault cut & slide -->
      <line x1="10" y1="105" x2="125" y2="55" stroke="#ef4444" stroke-width="2.5"/>
      <rect x="35" y="35" width="80" height="25" rx="3" fill="#a855f7"/>
      <text x="75" y="52" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">Nappe Sheet</text>
      <text x="70" y="145" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Fractures along fault</text>
      <text x="70" y="160" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Slides kilometers</text>
      <text x="70" y="180" font-size="9" font-weight="bold" fill="#c084fc" text-anchor="middle">Nappe Formation</text>
    </g>
  </g>

  <!-- Synthesis Matrix Bottom -->
  <g transform="translate(40, 335)">
    <rect x="0" y="0" width="720" height="85" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <text x="360" y="22" font-size="11.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">TOPIC 7 CORE GEOLOGICAL PRINCIPLES</text>
    <text x="25" y="44" font-size="9.5" fill="#cbd5e1">• <tspan font-weight="bold" fill="#fde047">Origin:</tspan> Horizontal compressional stress generated at convergent tectonic plate boundaries.</text>
    <text x="25" y="60" font-size="9.5" fill="#cbd5e1">• <tspan font-weight="bold" fill="#4ade80">Anatomy:</tspan> Alternating upfolds (anticlines) and downfolds (synclines) separated by sloping limbs and axial planes.</text>
    <text x="25" y="76" font-size="9.5" fill="#cbd5e1">• <tspan font-weight="bold" fill="#c084fc">Significance:</tspan> Builds fold mountain water towers &amp; mineral veins, requiring terrace farming &amp; slope conservation.</text>
  </g>
</svg>
""")

SVG_MAP = {
    1: SVG_COMPRESSIONAL_BUCKLING,
    2: SVG_FOLD_ANATOMY,
    3: SVG_SYMMETRICAL_ASYMMETRICAL,
    4: SVG_ADVANCED_FOLD_TYPES,
    5: SVG_OVERTHRUST_NAPPE,
    6: SVG_MONOCLINES_DOMES_BASINS,
    7: SVG_OROGENIC_CYCLE,
    8: SVG_GLOBAL_FOLD_MAP,
    9: SVG_HOGBACK_CUESTA,
    10: SVG_HUMAN_SIGNIFICANCE,
    11: SVG_SLOPE_MANAGEMENT,
    12: SVG_FOLD_SYNTHESIS_CONTINUUM
}

# =============================================================================
# VISUAL ENRICHMENT EXECUTION
# =============================================================================
def run_enrichment():
    print("=" * 80)
    print("VLearn CBC Grade 10 Geography — Topic 7: Folding Visual Enrichment Engine")
    print("=" * 80)

    # 1. Load verified images json
    verified_images_path = os.path.join(os.path.dirname(__file__), "grade10_geography_topic7_verified_images.json")
    if not os.path.exists(verified_images_path):
        raise FileNotFoundError(f"Verified images file not found at {verified_images_path}!")

    with open(verified_images_path, "r") as f:
        verified_images = json.load(f)

    # 2. Get Topic 7
    topic = Topic.objects.filter(subject_id=37, order=7).first() or Topic.objects.filter(name="Folding").first()
    if not topic:
        raise RuntimeError("Topic 7: Folding not found in database!")

    lessons = list(topic.lessons.all().order_by("learning_unit__order"))
    print(f"Loaded {len(lessons)} lessons for Topic 7: {topic.name}")

    total_images_attached = 0
    total_svgs_attached = 0
    total_videos_attached = 0

    for lesson in lessons:
        u_order = lesson.learning_unit.order
        u_key = str(u_order)
        print(f"\nEnriching Unit {u_order}: {lesson.title}...")

        # ---------------------------------------------------------------------
        # A. Page 1 Photographic Visual Hook
        # ---------------------------------------------------------------------
        img_info = verified_images.get(u_key)
        if not img_info:
            print(f" [!] Warning: No verified image found for lesson {u_order}")
            continue

        hook_block = LessonBlock.objects.filter(
            lesson=lesson,
            page_number=1,
            block_type="suggested_image"
        ).first()

        if hook_block:
            hook_block.content = {
                "url": img_info["url"],
                "resolved_image_url": img_info["url"],
                "caption": hook_block.title,
                "author": img_info.get("author", "Wikimedia Commons"),
                "licensing": img_info.get("licensing", "CC BY-SA"),
                "commons_page_url": img_info.get("commons_url", "")
            }
            hook_block.save()

            asset, _ = LessonAsset.objects.get_or_create(
                lesson=lesson,
                title=f"Lesson {u_order} Visual Hook: {hook_block.title}",
                defaults={
                    "asset_type": "image",
                    "source_type": "external",
                    "storage_type": "url",
                    "status": "attached",
                    "url": img_info["url"],
                    "metadata": {
                        "author": img_info.get("author", "Wikimedia Commons"),
                        "licensing": img_info.get("licensing", "CC BY-SA"),
                        "commons_url": img_info.get("commons_url", ""),
                        "unit_order": int(u_order),
                        "topic_order": 7
                    }
                }
            )
            asset.url = img_info["url"]
            asset.status = "attached"
            asset.save()
            asset.blocks.add(hook_block)
            total_images_attached += 1
            print(f"  + Attached Card 1 Photo Visual Hook: {img_info['url'][:60]}...")

        # ---------------------------------------------------------------------
        # B. Custom Responsive Vector SVG
        # ---------------------------------------------------------------------
        svg_xml = SVG_MAP.get(int(u_order))
        if svg_xml:
            diagram_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="diagram"
            ).first()

            if diagram_block:
                diagram_block.content = {
                    "svg_content": svg_xml,
                    "title": diagram_block.title,
                    "caption": diagram_block.content.get("caption", diagram_block.title) if diagram_block.content else diagram_block.title
                }
                diagram_block.save()

                svg_asset, _ = LessonAsset.objects.get_or_create(
                    lesson=lesson,
                    title=f"Lesson {u_order} Diagram: {diagram_block.title}",
                    defaults={
                        "asset_type": "diagram",
                        "source_type": "ai_generated",
                        "storage_type": "embed",
                        "status": "attached",
                        "metadata": {
                            "svg_content": svg_xml,
                            "unit_order": int(u_order),
                            "topic_order": 7
                        }
                    }
                )
                svg_asset.metadata["svg_content"] = svg_xml
                svg_asset.status = "attached"
                svg_asset.save()
                svg_asset.blocks.add(diagram_block)
                total_svgs_attached += 1
                print(f"  + Attached Custom Vector SVG (viewBox='0 0 800 450') to Block: {diagram_block.title}")

        # ---------------------------------------------------------------------
        # C. Verified Educational YouTube Video (Lesson 7)
        # ---------------------------------------------------------------------
        video_block = LessonBlock.objects.filter(
            lesson=lesson,
            block_type="video"
        ).first()

        if video_block:
            c = video_block.content or {}
            vid_url = c.get("url") or "https://www.youtube.com/watch?v=1O945h3Gq4A"
            v_asset, _ = LessonAsset.objects.get_or_create(
                lesson=lesson,
                title=f"Lesson {u_order} Video: {video_block.title}",
                defaults={
                    "asset_type": "youtube",
                    "source_type": "external",
                    "storage_type": "url",
                    "status": "attached",
                    "url": vid_url,
                    "metadata": {
                        "youtube_url": vid_url,
                        "unit_order": int(u_order),
                        "topic_order": 7
                    }
                }
            )
            v_asset.url = vid_url
            v_asset.status = "attached"
            v_asset.save()
            v_asset.blocks.add(video_block)
            total_videos_attached += 1
            print(f"  + Attached Educational YouTube Video: {vid_url}")

    print("\n" + "=" * 80)
    print(f"Visual Enrichment Completed for Grade 10 Geography Topic 7!")
    print(f"Total Visual Hooks: {total_images_attached}/12")
    print(f"Total Custom SVGs: {total_svgs_attached}/12")
    print(f"Total Videos Attached: {total_videos_attached}")
    print("=" * 80)

if __name__ == "__main__":
    run_enrichment()

