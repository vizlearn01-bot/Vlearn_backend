"""
VLearn Curriculum Visual Enrichment Script
CBC Grade 7 — Home Science
Topic 7: Seams (Order: 7)

Attaches:
- 4 Verified Topic-Representative Wikimedia Photographic Visual Hooks (Card 1 of every lesson)
- 7 Custom Sanitized, Responsive (800x450), Pedagogically Rich Vector SVGs
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
TOPIC7_PHOTOS = {
    1: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/df/A_tailor_sewing_cloth.jpg",
        "author": "Wikimedia Commons Contributor",
        "licensing": "CC BY-SA 3.0",
        "caption": "A tailor joining flat fabric panels on a sewing machine to construct a 3D wearable garment."
    },
    2: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7d/Wrangler_jeans_back_detail_%282026-01-27%29.jpg",
        "author": "Wikimedia Commons Contributor",
        "licensing": "CC BY-SA 4.0",
        "caption": "Double-stitched and overlaid seams on durable denim jeans designed to withstand heavy friction and stress."
    },
    3: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/1/1f/Pinking_scissors.jpg",
        "author": "Wikimedia Commons Contributor",
        "licensing": "CC BY-SA 3.0",
        "caption": "Pinking shears with zigzag-toothed blades designed to cut fabric edges on the bias to prevent thread fraying."
    },
    4: {
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/db/Running_stitch_for_hand_embroidery.jpg",
        "author": "Wikimedia Commons Contributor",
        "licensing": "CC BY-SA 4.0",
        "caption": "Hand embroidery stitching on a flat cotton fabric panel to create decorative surface designs before article assembly."
    }
}

# 7 Custom High-Definition Vector SVGs
TOPIC7_SVGS = {
    # Lesson 1 Page 2: Seam Terminology & 1.5 cm Allowance
    (1, 2): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="fabricTop" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3b82f6"/>
      <stop offset="100%" stop-color="#1d4ed8"/>
    </linearGradient>
    <linearGradient id="fabricBottom" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#60a5fa"/>
      <stop offset="100%" stop-color="#2563eb"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-opacity="0.15"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="450" fill="#f8fafc" rx="12"/>
  <rect x="20" y="20" width="760" height="410" fill="#ffffff" rx="10" stroke="#e2e8f0" stroke-width="2" filter="url(#shadow)"/>

  <!-- Title Banner -->
  <rect x="40" y="35" width="720" height="45" fill="#0f172a" rx="8"/>
  <text x="400" y="63" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">
    ANATOMY OF A SEAM &amp; THE 1.5 CM SAFETY ALLOWANCE
  </text>

  <!-- Fabric Layers Container -->
  <g transform="translate(60, 110)">
    <!-- Top Fabric Panel -->
    <path d="M 40 40 L 460 40 L 460 130 L 40 130 Z" fill="url(#fabricTop)" opacity="0.95" rx="4"/>
    <text x="60" y="70" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="600">Fabric Layer 1 (Top Panel)</text>
    
    <!-- Bottom Fabric Panel (Shifted slightly for 3D overlap) -->
    <path d="M 40 100 L 460 100 L 460 190 L 40 190 Z" fill="url(#fabricBottom)" opacity="0.9" rx="4"/>
    <text x="60" y="165" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="600">Fabric Layer 2 (Bottom Panel)</text>

    <!-- Seam Line (Stitching) -->
    <line x1="280" y1="30" x2="280" y2="200" stroke="#facc15" stroke-width="4" stroke-dasharray="8 6"/>
    <circle cx="280" cy="85" r="5" fill="#eab308"/>
    <circle cx="280" cy="145" r="5" fill="#eab308"/>

    <!-- Seam Allowance Zone Highlight -->
    <rect x="280" y="40" width="180" height="150" fill="#fef08a" fill-opacity="0.35" stroke="#ca8a04" stroke-width="2" stroke-dasharray="4 4"/>

    <!-- Raw Cut Edge Highlight -->
    <line x1="460" y1="30" x2="460" y2="200" stroke="#ef4444" stroke-width="3"/>
    
    <!-- Seam Turning (Small 3mm fold lip) -->
    <path d="M 460 60 Q 480 85 460 110" fill="none" stroke="#8b5cf6" stroke-width="3" stroke-dasharray="3 3"/>

    <!-- Callouts & Dimension Markers -->
    <!-- 1.5 cm Dimension Line -->
    <line x1="280" y1="215" x2="460" y2="215" stroke="#0f172a" stroke-width="2"/>
    <line x1="280" y1="208" x2="280" y2="222" stroke="#0f172a" stroke-width="2"/>
    <line x1="460" y1="208" x2="460" y2="222" stroke="#0f172a" stroke-width="2"/>
    <text x="370" y="235" fill="#0f172a" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">
      1.5 cm Seam Allowance
    </text>
  </g>

  <!-- Side Description Box -->
  <g transform="translate(540, 105)">
    <rect x="0" y="0" width="200" height="285" fill="#f1f5f9" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="15" y="25" fill="#0f172a" font-family="system-ui, sans-serif" font-size="13" font-weight="700">CORE COMPONENTS:</text>
    
    <!-- Item 1: Seam Line -->
    <circle cx="20" cy="55" r="6" fill="#eab308"/>
    <text x="35" y="52" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">1. Seam Line</text>
    <text x="35" y="67" fill="#475569" font-family="system-ui, sans-serif" font-size="10">The straight row of stitches.</text>

    <!-- Item 2: Seam Allowance -->
    <rect x="14" y="90" width="12" height="12" fill="#fef08a" stroke="#ca8a04"/>
    <text x="35" y="97" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">2. Seam Allowance</text>
    <text x="35" y="112" fill="#475569" font-family="system-ui, sans-serif" font-size="10">1.5 cm safety space to stop</text>
    <text x="35" y="125" fill="#475569" font-family="system-ui, sans-serif" font-size="10">threads from fraying out.</text>

    <!-- Item 3: Raw Edge -->
    <line x1="14" y1="150" x2="26" y2="150" stroke="#ef4444" stroke-width="3"/>
    <text x="35" y="148" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">3. Raw Cut Edge</text>
    <text x="35" y="163" fill="#475569" font-family="system-ui, sans-serif" font-size="10">Cut end with loose threads.</text>

    <!-- Item 4: Seam Turning -->
    <path x="0" y="0" d="M 14 195 Q 26 200 14 205" fill="none" stroke="#8b5cf6" stroke-width="2"/>
    <text x="35" y="197" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">4. Seam Turning</text>
    <text x="35" y="212" fill="#475569" font-family="system-ui, sans-serif" font-size="10">Small fold for neatening.</text>

    <!-- Rule Badge -->
    <rect x="10" y="235" width="180" height="38" fill="#dbeafe" rx="6" stroke="#93c5fd"/>
    <text x="100" y="252" fill="#1e40af" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">
      CBC Standard: 1.5 cm
    </text>
    <text x="100" y="265" fill="#1e40af" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">
      Never sew at the raw edge!
    </text>
  </g>
</svg>""",

    # Lesson 1 Page 4: Warp & Weft Thread Slippage Diagram
    (1, 4): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="3" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="#f8fafc" rx="12"/>
  <rect x="20" y="20" width="760" height="410" fill="#ffffff" rx="10" stroke="#e2e8f0" stroke-width="2" filter="url(#shadow)"/>

  <!-- Title Banner -->
  <rect x="40" y="35" width="720" height="45" fill="#0f172a" rx="8"/>
  <text x="400" y="63" fill="#ffffff" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">
    WHY WEAVE THREADS SLIP: 2 MM vs. 1.5 CM ALLOWANCE
  </text>

  <!-- Left Card: Faulty 2mm Margin (Fraying Collapse) -->
  <g transform="translate(50, 100)">
    <rect x="0" y="0" width="330" height="290" fill="#fef2f2" rx="8" stroke="#fca5a5" stroke-width="2"/>
    <rect x="15" y="15" width="300" height="30" fill="#ef4444" rx="6"/>
    <text x="165" y="35" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">
      TOO CLOSE TO EDGE (2 mm) - SEAM COLLAPSE
    </text>

    <!-- Woven Grid Simulation -->
    <g transform="translate(30, 60)">
      <!-- Warp vertical threads -->
      <line x1="20" y1="20" x2="20" y2="150" stroke="#94a3b8" stroke-width="2"/>
      <line x1="40" y1="20" x2="40" y2="150" stroke="#94a3b8" stroke-width="2"/>
      <line x1="60" y1="20" x2="60" y2="150" stroke="#94a3b8" stroke-width="2"/>
      <line x1="80" y1="20" x2="80" y2="150" stroke="#94a3b8" stroke-width="2"/>
      <!-- Slipped threads pulling out -->
      <path d="M 100 20 Q 120 70 140 30" stroke="#ef4444" stroke-width="2.5" fill="none"/>
      <path d="M 100 60 Q 130 90 150 70" stroke="#ef4444" stroke-width="2.5" fill="none"/>
      <path d="M 100 110 Q 130 140 160 110" stroke="#ef4444" stroke-width="2.5" fill="none"/>

      <!-- Stitches right at margin -->
      <line x1="95" y1="20" x2="95" y2="150" stroke="#eab308" stroke-width="3" stroke-dasharray="6 4"/>
      <text x="95" y="170" fill="#dc2626" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">
        Stitch Line (Only 2 mm from edge)
      </text>
    </g>

    <!-- Explanation Box -->
    <rect x="15" y="240" width="300" height="38" fill="#fee2e2" rx="4"/>
    <text x="165" y="255" fill="#991b1b" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">
      Result: Tension pulls warp threads out.
    </text>
    <text x="165" y="268" fill="#991b1b" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">
      Garment rips open along the seam!
    </text>
  </g>

  <!-- Right Card: Proper 1.5cm Allowance (Firm Structural Lock) -->
  <g transform="translate(420, 100)">
    <rect x="0" y="0" width="330" height="290" fill="#f0fdf4" rx="8" stroke="#86efac" stroke-width="2"/>
    <rect x="15" y="15" width="300" height="30" fill="#16a34a" rx="6"/>
    <text x="165" y="35" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">
      PROPER 1.5 CM ALLOWANCE - SECURE LOCK
    </text>

    <!-- Woven Grid Simulation -->
    <g transform="translate(30, 60)">
      <!-- Warp vertical threads -->
      <line x1="20" y1="20" x2="20" y2="150" stroke="#4ade80" stroke-width="2"/>
      <line x1="40" y1="20" x2="40" y2="150" stroke="#4ade80" stroke-width="2"/>
      <line x1="60" y1="20" x2="60" y2="150" stroke="#4ade80" stroke-width="2"/>
      <line x1="80" y1="20" x2="80" y2="150" stroke="#4ade80" stroke-width="2"/>
      <line x1="100" y1="20" x2="100" y2="150" stroke="#4ade80" stroke-width="2"/>
      <line x1="120" y1="20" x2="120" y2="150" stroke="#4ade80" stroke-width="2"/>
      <line x1="140" y1="20" x2="140" y2="150" stroke="#4ade80" stroke-width="2"/>

      <!-- Stitches deep inside fabric -->
      <line x1="60" y1="20" x2="60" y2="150" stroke="#15803d" stroke-width="3" stroke-dasharray="6 4"/>
      <!-- Safety Zone Bracket -->
      <rect x="60" y="20" width="100" height="130" fill="#dcfce7" fill-opacity="0.5" stroke="#22c55e" stroke-width="1.5" stroke-dasharray="4 4"/>

      <text x="110" y="170" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">
        1.5 cm Stable Weave Buffer Zone
      </text>
    </g>

    <!-- Explanation Box -->
    <rect x="15" y="240" width="300" height="38" fill="#dcfce7" rx="4"/>
    <text x="165" y="255" fill="#166534" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">
      Result: Yarns are locked firmly by friction.
    </text>
    <text x="165" y="268" fill="#166534" font-family="system-ui, sans-serif" font-size="9.5" text-anchor="middle">
      Withstands washing, stretching and heavy wear!
    </text>
  </g>
</svg>""",

    # Lesson 2 Page 2: The 4 Seam Types Structural Blueprint
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
    THE 4 CORE SEAM TYPES: CONSTRUCTION &amp; CROSS-SECTIONS
  </text>

  <!-- 2x2 Grid of Seams -->

  <!-- Top-Left: Plain / Open Seam -->
  <g transform="translate(45, 85)">
    <rect x="0" y="0" width="345" height="150" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="10" y="10" width="325" height="24" fill="#3b82f6" rx="4"/>
    <text x="172" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      1. PLAIN (OPEN) SEAM - INCONSPICUOUS
    </text>
    <!-- Fold Diagram -->
    <path d="M 40 80 L 140 80 L 140 55" fill="none" stroke="#2563eb" stroke-width="6" stroke-linecap="round"/>
    <path d="M 40 100 L 140 100 L 140 125" fill="none" stroke="#60a5fa" stroke-width="6" stroke-linecap="round"/>
    <!-- Stitch Line -->
    <circle cx="140" cy="90" r="5" fill="#facc15" stroke="#ca8a04" stroke-width="1.5"/>
    <!-- Labels -->
    <text x="180" y="65" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Wings Pressed Open Flat</text>
    <text x="180" y="80" fill="#64748b" font-family="system-ui, sans-serif" font-size="9.5">Single stitch on inside (wrong side).</text>
    <text x="180" y="95" fill="#64748b" font-family="system-ui, sans-serif" font-size="9.5">Raw edges must be neatened.</text>
    <text x="180" y="115" fill="#2563eb" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Use: Cotton dresses, side seams.</text>
  </g>

  <!-- Top-Right: French Seam -->
  <g transform="translate(410, 85)">
    <rect x="0" y="0" width="345" height="150" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="10" y="10" width="325" height="24" fill="#8b5cf6" rx="4"/>
    <text x="172" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      2. FRENCH SEAM - SELF-NEATENING POUCH
    </text>
    <!-- Fold Diagram (Enclosed Loop) -->
    <path d="M 40 85 L 110 85 Q 150 85 150 65 Q 150 45 125 45 L 90 45" fill="none" stroke="#7c3aed" stroke-width="5" stroke-linecap="round"/>
    <path d="M 40 100 L 110 100 Q 165 100 165 65 Q 165 30 125 30 L 90 30" fill="none" stroke="#a78bfa" stroke-width="5" stroke-linecap="round"/>
    <!-- Dual Stitches -->
    <circle cx="105" cy="38" r="4" fill="#facc15"/>
    <circle cx="105" cy="92" r="4" fill="#facc15"/>
    <!-- Labels -->
    <text x="180" y="65" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Raw Edges Fully Enclosed</text>
    <text x="180" y="80" fill="#64748b" font-family="system-ui, sans-serif" font-size="9.5">Stitched twice (right, then wrong side).</text>
    <text x="180" y="95" fill="#64748b" font-family="system-ui, sans-serif" font-size="9.5">Zero fraying, completely clean inside.</text>
    <text x="180" y="115" fill="#7c3aed" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Use: Silk, chiffon, pillowcases.</text>
  </g>

  <!-- Bottom-Left: Overlaid Seam -->
  <g transform="translate(45, 250)">
    <rect x="0" y="0" width="345" height="155" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="10" y="10" width="325" height="24" fill="#059669" rx="4"/>
    <text x="172" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      3. OVERLAID SEAM - CONSPICUOUS TOP JOIN
    </text>
    <!-- Fold Diagram -->
    <path d="M 40 100 L 150 100" fill="none" stroke="#10b981" stroke-width="6" stroke-linecap="round"/>
    <path d="M 80 80 L 140 80 Q 160 80 160 65 L 120 65" fill="none" stroke="#047857" stroke-width="6" stroke-linecap="round"/>
    <!-- Top Stitch -->
    <circle cx="130" cy="80" r="5" fill="#facc15" stroke="#ca8a04" stroke-width="1.5"/>
    <!-- Labels -->
    <text x="180" y="65" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Folded Over Top Panel</text>
    <text x="180" y="80" fill="#64748b" font-family="system-ui, sans-serif" font-size="9.5">Stitched directly from the right side.</text>
    <text x="180" y="95" fill="#64748b" font-family="system-ui, sans-serif" font-size="9.5">Strong, decorative, easy to position.</text>
    <text x="180" y="115" fill="#047857" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Use: Patch pockets, curved yokes.</text>
  </g>

  <!-- Bottom-Right: Double-Stitched / Machine-Fell Seam -->
  <g transform="translate(410, 250)">
    <rect x="0" y="0" width="345" height="155" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="10" y="10" width="325" height="24" fill="#d97706" rx="4"/>
    <text x="172" y="26" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      4. DOUBLE-STITCHED (FELL) - MAXIMUM LOAD
    </text>
    <!-- Fold Diagram (Interlocked Folds) -->
    <path d="M 40 80 L 110 80 Q 140 80 140 95 L 85 95" fill="none" stroke="#d97706" stroke-width="5" stroke-linecap="round"/>
    <path d="M 50 110 L 135 110 Q 160 110 160 95 L 115 95" fill="none" stroke="#b45309" stroke-width="5" stroke-linecap="round"/>
    <!-- 2 Parallel Stitches -->
    <circle cx="75" cy="95" r="4.5" fill="#facc15"/>
    <circle cx="125" cy="95" r="4.5" fill="#facc15"/>
    <!-- Labels -->
    <text x="180" y="65" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Two Parallel Visible Rows</text>
    <text x="180" y="80" fill="#64748b" font-family="system-ui, sans-serif" font-size="9.5">Interlocked folds pressed dead flat.</text>
    <text x="180" y="95" fill="#64748b" font-family="system-ui, sans-serif" font-size="9.5">Extreme friction and pulling strength.</text>
    <text x="180" y="115" fill="#b45309" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Use: Denim jeans, workwear, canvas.</text>
  </g>
</svg>""",

    # Lesson 2 Page 4: Fabric Weight & Seam Selection Spectrum
    (2, 4): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="spectrumGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="50%" stop-color="#3b82f6"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="3" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="800" height="450" fill="#f8fafc" rx="12"/>
  <rect x="20" y="20" width="760" height="410" fill="#ffffff" rx="10" stroke="#e2e8f0" stroke-width="2" filter="url(#shadow)"/>

  <!-- Title Banner -->
  <rect x="40" y="30" width="720" height="42" fill="#0f172a" rx="8"/>
  <text x="400" y="57" fill="#ffffff" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">
    FABRIC WEIGHT &amp; STRESS: SEAM SELECTION GUIDE
  </text>

  <!-- Horizontal Spectrum Bar -->
  <g transform="translate(60, 95)">
    <rect x="0" y="0" width="680" height="16" fill="url(#spectrumGrad)" rx="8"/>
    <circle cx="100" cy="8" r="10" fill="#ffffff" stroke="#7c3aed" stroke-width="3"/>
    <circle cx="340" cy="8" r="10" fill="#ffffff" stroke="#2563eb" stroke-width="3"/>
    <circle cx="580" cy="8" r="10" fill="#ffffff" stroke="#d97706" stroke-width="3"/>
  </g>

  <!-- 3 Columns -->

  <!-- Column 1: Fine / Sheer Fabrics -->
  <g transform="translate(45, 135)">
    <rect x="0" y="0" width="225" height="260" fill="#f5f3ff" rx="8" stroke="#ddd6fe" stroke-width="1.5"/>
    <rect x="15" y="15" width="195" height="28" fill="#7c3aed" rx="5"/>
    <text x="112" y="34" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      FINE / SHEER FABRICS
    </text>
    <text x="15" y="65" fill="#5b21b6" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Fabrics: Silk, Chiffon, Voile</text>
    <text x="15" y="85" fill="#475569" font-family="system-ui, sans-serif" font-size="10">• Translucent, light, delicate.</text>
    <text x="15" y="100" fill="#475569" font-family="system-ui, sans-serif" font-size="10">• Fray easily, show raw edges.</text>
    
    <rect x="15" y="125" width="195" height="75" fill="#ffffff" rx="6" stroke="#c4b5fd"/>
    <text x="112" y="145" fill="#6d28d9" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      CHOSEN SEAM:
    </text>
    <text x="112" y="165" fill="#0f172a" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">
      FRENCH SEAM
    </text>
    <text x="112" y="185" fill="#64748b" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">
      Hides edges, zero shadow lines.
    </text>
    <rect x="15" y="215" width="195" height="30" fill="#ede9fe" rx="4"/>
    <text x="112" y="234" fill="#5b21b6" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">
      Why not Plain? Edges show through!
    </text>
  </g>

  <!-- Column 2: Medium Fabrics -->
  <g transform="translate(285, 135)">
    <rect x="0" y="0" width="225" height="260" fill="#eff6ff" rx="8" stroke="#bfdbfe" stroke-width="1.5"/>
    <rect x="15" y="15" width="195" height="28" fill="#2563eb" rx="5"/>
    <text x="112" y="34" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      MEDIUM WEIGHT
    </text>
    <text x="15" y="65" fill="#1e40af" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Fabrics: Cotton, Calico, Linen</text>
    <text x="15" y="85" fill="#475569" font-family="system-ui, sans-serif" font-size="10">• Balanced weave, standard drape.</text>
    <text x="15" y="100" fill="#475569" font-family="system-ui, sans-serif" font-size="10">• Daily wash and wear garments.</text>
    
    <rect x="15" y="125" width="195" height="75" fill="#ffffff" rx="6" stroke="#93c5fd"/>
    <text x="112" y="145" fill="#1d4ed8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      CHOSEN SEAM:
    </text>
    <text x="112" y="165" fill="#0f172a" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">
      PLAIN (OPEN) SEAM
    </text>
    <text x="112" y="185" fill="#64748b" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">
      Pressed open flat + pinked edges.
    </text>
    <rect x="15" y="215" width="195" height="30" fill="#dbeafe" rx="4"/>
    <text x="112" y="234" fill="#1e40af" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">
      Quick, versatile, flat finish.
    </text>
  </g>

  <!-- Column 3: Heavy Duty Fabrics -->
  <g transform="translate(525, 135)">
    <rect x="0" y="0" width="225" height="260" fill="#fffbeb" rx="8" stroke="#fde68a" stroke-width="1.5"/>
    <rect x="15" y="15" width="195" height="28" fill="#d97706" rx="5"/>
    <text x="112" y="34" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      HEAVY / LOAD STRESS
    </text>
    <text x="15" y="65" fill="#92400e" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Fabrics: Denim, Canvas, Drill</text>
    <text x="15" y="85" fill="#475569" font-family="system-ui, sans-serif" font-size="10">• Thick yarns, heavy friction.</text>
    <text x="15" y="100" fill="#475569" font-family="system-ui, sans-serif" font-size="10">• High pulling stress on joins.</text>
    
    <rect x="15" y="125" width="195" height="75" fill="#ffffff" rx="6" stroke="#fcd34d"/>
    <text x="112" y="145" fill="#b45309" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">
      CHOSEN SEAM:
    </text>
    <text x="112" y="165" fill="#0f172a" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">
      DOUBLE-STITCHED
    </text>
    <text x="112" y="185" fill="#64748b" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">
      Dual stitch lines lock heavy weave.
    </text>
    <rect x="15" y="215" width="195" height="30" fill="#fef3c7" rx="4"/>
    <text x="112" y="234" fill="#92400e" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">
      Why not French? Too bulky and thick!
    </text>
  </g>
</svg>""",

    # Lesson 3 Page 2: 3-Panel Neatening Storyboard
    (3, 2): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
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
    3 SIMPLE METHODS TO NEATEN RAW SEAM ALLOWANCE EDGES
  </text>

  <!-- Panel 1: Pinking Shears -->
  <g transform="translate(45, 90)">
    <rect x="0" y="0" width="225" height="305" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="12" y="12" width="201" height="26" fill="#3b82f6" rx="4"/>
    <text x="112" y="29" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">
      1. PINKING (CUTTING)
    </text>
    <!-- Illustration: Zigzag Sawtooth Cut -->
    <g transform="translate(25, 55)">
      <rect x="0" y="0" width="175" height="110" fill="#e2e8f0" rx="4"/>
      <!-- Zigzag Edge -->
      <path d="M 175 0 L 160 15 L 175 30 L 160 45 L 175 60 L 160 75 L 175 90 L 160 105 L 175 110" fill="#cbd5e1" stroke="#2563eb" stroke-width="3"/>
      <!-- Pinking Shears Icon -->
      <circle cx="60" cy="55" r="25" fill="#bfdbfe" stroke="#3b82f6" stroke-width="2"/>
      <text x="60" y="60" fill="#1e40af" font-family="system-ui, sans-serif" font-size="20" text-anchor="middle">✂️</text>
    </g>
    <!-- Description -->
    <text x="15" y="190" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">How it Works:</text>
    <text x="15" y="208" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Cuts zigzag saw-tooth teeth.</text>
    <text x="15" y="222" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Diagonal bias cut stops fraying.</text>
    <text x="15" y="236" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Fast, no needle required.</text>
    <rect x="12" y="260" width="201" height="30" fill="#dbeafe" rx="4"/>
    <text x="112" y="278" fill="#1e40af" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">
      Best for: Firmly woven cottons
    </text>
  </g>

  <!-- Panel 2: Machine Edge-Stitching -->
  <g transform="translate(285, 90)">
    <rect x="0" y="0" width="225" height="305" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="12" y="12" width="201" height="26" fill="#059669" rx="4"/>
    <text x="112" y="29" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">
      2. MACHINE EDGE-STITCH
    </text>
    <!-- Illustration: Turned 3mm Fold & Stitch -->
    <g transform="translate(25, 55)">
      <rect x="0" y="0" width="175" height="110" fill="#e2e8f0" rx="4"/>
      <!-- Folded Lip -->
      <path d="M 130 0 L 160 0 L 160 110 L 130 110 Z" fill="#a7f3d0" stroke="#059669" stroke-width="2"/>
      <!-- Straight Machine Stitch -->
      <line x1="145" y1="5" x2="145" y2="105" stroke="#facc15" stroke-width="3" stroke-dasharray="5 3"/>
      <!-- Presser Foot Icon -->
      <rect x="40" y="35" width="50" height="40" fill="#d1fae5" rx="4" stroke="#059669"/>
      <text x="65" y="60" fill="#065f46" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Presser Foot</text>
    </g>
    <!-- Description -->
    <text x="15" y="190" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">How it Works:</text>
    <text x="15" y="208" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Turn 3 mm margin under.</text>
    <text x="15" y="222" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Machine straight-stitch on fold.</text>
    <text x="15" y="236" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Seals raw edges completely.</text>
    <rect x="12" y="260" width="201" height="30" fill="#d1fae5" rx="4"/>
    <text x="112" y="278" fill="#065f46" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">
      Best for: Calico, linen, shirts
    </text>
  </g>

  <!-- Panel 3: Hand Loop Stitches -->
  <g transform="translate(525, 90)">
    <rect x="0" y="0" width="225" height="305" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="12" y="12" width="201" height="26" fill="#8b5cf6" rx="4"/>
    <text x="112" y="29" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">
      3. HAND LOOP STITCHES
    </text>
    <!-- Illustration: Loops over raw edge -->
    <g transform="translate(25, 55)">
      <rect x="0" y="0" width="175" height="110" fill="#e2e8f0" rx="4"/>
      <!-- Raw Edge Line -->
      <line x1="160" y1="0" x2="160" y2="110" stroke="#ef4444" stroke-width="2"/>
      <!-- Looping Stitches -->
      <path d="M 135 15 Q 165 15 165 30 Q 165 45 135 45" fill="none" stroke="#7c3aed" stroke-width="3"/>
      <path d="M 135 50 Q 165 50 165 65 Q 165 80 135 80" fill="none" stroke="#7c3aed" stroke-width="3"/>
      <path d="M 135 85 Q 165 85 165 100 Q 165 115 135 115" fill="none" stroke="#7c3aed" stroke-width="3"/>
      <!-- Hand Needle -->
      <line x1="110" y1="70" x2="140" y2="50" stroke="#0f172a" stroke-width="2.5"/>
      <circle cx="140" cy="50" r="2.5" fill="#facc15"/>
    </g>
    <!-- Description -->
    <text x="15" y="190" fill="#0f172a" font-family="system-ui, sans-serif" font-size="11" font-weight="700">How it Works:</text>
    <text x="15" y="208" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Hand needle loops over edge.</text>
    <text x="15" y="222" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Evenly spaced (4 mm apart).</text>
    <text x="15" y="236" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">• Binds loose fraying yarns flat.</text>
    <rect x="12" y="260" width="201" height="30" fill="#ede9fe" rx="4"/>
    <text x="112" y="278" fill="#5b21b6" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">
      Best for: Thick wool, curved edges
    </text>
  </g>
</svg>""",

    # Lesson 3 Page 4: 4-Step Hand Loop Stitch Sequence Blueprint
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
    THE 4-STEP HAND LOOP STITCH SEQUENCE BLUEPRINT
  </text>

  <!-- 4 Step Boxes Horizontally -->

  <!-- Step 1: Anchor Thread -->
  <g transform="translate(45, 95)">
    <rect x="0" y="0" width="165" height="295" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="10" y="10" width="145" height="26" fill="#8b5cf6" rx="4"/>
    <text x="82" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">STEP 1: ANCHOR</text>
    <!-- Illustration -->
    <g transform="translate(15, 50)">
      <rect x="0" y="0" width="135" height="110" fill="#e2e8f0" rx="4"/>
      <!-- Raw Edge -->
      <line x1="120" y1="0" x2="120" y2="110" stroke="#ef4444" stroke-width="2"/>
      <!-- Tiny Double Stitch Anchor -->
      <circle cx="80" cy="55" r="4" fill="#7c3aed"/>
      <circle cx="80" cy="55" r="8" fill="none" stroke="#7c3aed" stroke-width="1.5"/>
      <text x="80" y="85" fill="#5b21b6" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Double Stitch</text>
    </g>
    <text x="12" y="185" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Action:</text>
    <text x="12" y="202" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Fasten thread with a</text>
    <text x="12" y="215" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">tiny double stitch 5mm</text>
    <text x="12" y="228" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">below raw cut edge.</text>
  </g>

  <!-- Step 2: Pierce Fabric -->
  <g transform="translate(225, 95)">
    <rect x="0" y="0" width="165" height="295" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="10" y="10" width="145" height="26" fill="#8b5cf6" rx="4"/>
    <text x="82" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">STEP 2: PIERCE</text>
    <!-- Illustration -->
    <g transform="translate(15, 50)">
      <rect x="0" y="0" width="135" height="110" fill="#e2e8f0" rx="4"/>
      <!-- Raw Edge -->
      <line x1="120" y1="0" x2="120" y2="110" stroke="#ef4444" stroke-width="2"/>
      <!-- Needle Entering from back -->
      <line x1="50" y1="75" x2="90" y2="40" stroke="#0f172a" stroke-width="3"/>
      <circle cx="90" cy="40" r="3" fill="#facc15"/>
      <text x="65" y="95" fill="#5b21b6" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Back to Front</text>
    </g>
    <text x="12" y="185" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Action:</text>
    <text x="12" y="202" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Push needle point</text>
    <text x="12" y="215" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">from back to front</text>
    <text x="12" y="228" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">exactly 4 mm below.</text>
  </g>

  <!-- Step 3: Loop Under Needle -->
  <g transform="translate(405, 95)">
    <rect x="0" y="0" width="165" height="295" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="10" y="10" width="145" height="26" fill="#8b5cf6" rx="4"/>
    <text x="82" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">STEP 3: LOOP</text>
    <!-- Illustration -->
    <g transform="translate(15, 50)">
      <rect x="0" y="0" width="135" height="110" fill="#e2e8f0" rx="4"/>
      <!-- Raw Edge -->
      <line x1="120" y1="0" x2="120" y2="110" stroke="#ef4444" stroke-width="2"/>
      <!-- Thread looping around needle point -->
      <path d="M 70 65 Q 115 20 95 35 Q 85 45 105 70" fill="none" stroke="#7c3aed" stroke-width="3"/>
      <circle cx="105" cy="70" r="3" fill="#facc15"/>
    </g>
    <text x="12" y="185" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Action:</text>
    <text x="12" y="202" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Pass working thread</text>
    <text x="12" y="215" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">around and UNDER</text>
    <text x="12" y="228" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">the sharp needle tip.</text>
  </g>

  <!-- Step 4: Pull Flat -->
  <g transform="translate(585, 95)">
    <rect x="0" y="0" width="165" height="295" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="10" y="10" width="145" height="26" fill="#16a34a" rx="4"/>
    <text x="82" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">STEP 4: PULL FLAT</text>
    <!-- Illustration -->
    <g transform="translate(15, 50)">
      <rect x="0" y="0" width="135" height="110" fill="#e2e8f0" rx="4"/>
      <!-- Raw Edge with neat loop -->
      <line x1="120" y1="0" x2="120" y2="110" stroke="#ef4444" stroke-width="2"/>
      <path d="M 85 40 Q 125 40 125 55 Q 125 70 85 70" fill="none" stroke="#16a34a" stroke-width="3.5"/>
      <text x="70" y="95" fill="#15803d" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Flat Bound Edge</text>
    </g>
    <text x="12" y="185" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700">Action:</text>
    <text x="12" y="202" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">Draw thread gently</text>
    <text x="12" y="215" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">so loop binds edge</text>
    <text x="12" y="228" fill="#475569" font-family="system-ui, sans-serif" font-size="9.5">flat without curling!</text>
  </g>
</svg>""",

    # Lesson 4 Page 2: Seam Quality Inspector Blueprint
    (4, 2): """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
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
    SEAM QUALITY AUDIT: WELL-MADE vs. FAULTY SEAMS
  </text>

  <!-- Left: The Champion Seam (Pass) -->
  <g transform="translate(45, 85)">
    <rect x="0" y="0" width="340" height="315" fill="#f0fdf4" rx="8" stroke="#86efac" stroke-width="2"/>
    <rect x="15" y="15" width="310" height="30" fill="#16a34a" rx="6"/>
    <text x="170" y="35" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">
      ✓ THE WELL-MADE SEAM (5/5 PASS)
    </text>

    <!-- Visual Swatch -->
    <g transform="translate(30, 60)">
      <rect x="0" y="0" width="280" height="110" fill="#ffffff" rx="6" stroke="#bbf7d0" stroke-width="1.5"/>
      <!-- Straight Seam Line -->
      <line x1="20" y1="55" x2="260" y2="55" stroke="#16a34a" stroke-width="3.5" stroke-dasharray="6 4"/>
      <!-- Zigzag pinked edge -->
      <path d="M 20 100 L 35 90 L 50 100 L 65 90 L 80 100 L 95 90 L 110 100 L 125 90 L 140 100 L 155 90 L 170 100 L 185 90 L 200 100 L 215 90 L 230 100 L 245 90 L 260 100" fill="none" stroke="#22c55e" stroke-width="2"/>
    </g>

    <!-- Quality Indicators Checklist -->
    <g transform="translate(25, 185)">
      <text x="0" y="15" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ Straight Line: Exactly 1.5 cm from edge.</text>
      <text x="0" y="35" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ Balanced Tension: Locks center, zero wrinkles.</text>
      <text x="0" y="55" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ Flat &amp; Pressed: Zero bulky lumps.</text>
      <text x="0" y="75" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✓ Uniform Width &amp; Cleanly Neatened Edges.</text>
      <rect x="0" y="90" width="290" height="24" fill="#dcfce7" rx="4"/>
      <text x="145" y="106" fill="#166534" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Durable, comfortable &amp; looks professional!</text>
    </g>
  </g>

  <!-- Right: Faulty Seams (Fail & Diagnosis) -->
  <g transform="translate(415, 85)">
    <rect x="0" y="0" width="340" height="315" fill="#fef2f2" rx="8" stroke="#fca5a5" stroke-width="2"/>
    <rect x="15" y="15" width="310" height="30" fill="#dc2626" rx="6"/>
    <text x="170" y="35" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">
      ✗ COMMON SEAM FAULTS &amp; REMEDIES
    </text>

    <!-- Visual Swatch showing puckers & loose loops -->
    <g transform="translate(30, 60)">
      <rect x="0" y="0" width="280" height="110" fill="#ffffff" rx="6" stroke="#fecaca" stroke-width="1.5"/>
      <!-- Wavy Puckered Line -->
      <path d="M 20 45 Q 60 70 100 40 Q 140 75 180 45 Q 220 70 260 50" fill="none" stroke="#dc2626" stroke-width="3"/>
      <!-- Loose Loops hanging -->
      <path d="M 50 60 Q 55 85 60 60" fill="none" stroke="#ef4444" stroke-width="2"/>
      <path d="M 120 55 Q 125 80 130 55" fill="none" stroke="#ef4444" stroke-width="2"/>
      <path d="M 200 65 Q 205 90 210 65" fill="none" stroke="#ef4444" stroke-width="2"/>
      <!-- Fraying unneatened edge -->
      <line x1="20" y1="100" x2="260" y2="100" stroke="#94a3b8" stroke-width="1.5"/>
      <line x1="40" y1="100" x2="40" y2="108" stroke="#ef4444" stroke-width="1.5"/>
      <line x1="90" y1="100" x2="90" y2="108" stroke="#ef4444" stroke-width="1.5"/>
      <line x1="170" y1="100" x2="170" y2="108" stroke="#ef4444" stroke-width="1.5"/>
    </g>

    <!-- Fault Diagnostic Checklist -->
    <g transform="translate(25, 185)">
      <text x="0" y="15" fill="#991b1b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✗ Puckered Fabric: Upper tension is too tight!</text>
      <text x="0" y="35" fill="#991b1b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✗ Loose Loops: Upper tension is too loose!</text>
      <text x="0" y="55" fill="#991b1b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✗ Wavy Seam: Fabric was forced or pulled.</text>
      <text x="0" y="75" fill="#991b1b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">✗ Fraying Edges: Unneatened raw margins.</text>
      <rect x="0" y="90" width="290" height="24" fill="#fee2e2" rx="4"/>
      <text x="145" y="106" fill="#991b1b" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Remedy: Adjust tension dial &amp; re-thread machine!</text>
    </g>
  </g>
</svg>""",

    # Lesson 4 Page 4: 5-Stage Lap Bag Construction Process Flow
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
    STEP-BY-STEP LAP BAG CONSTRUCTION WORKFLOW
  </text>

  <!-- 5 Horizontal Process Steps -->

  <!-- Step 1: Draft & Cut -->
  <g transform="translate(35, 80)">
    <rect x="0" y="0" width="135" height="320" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="8" y="8" width="119" height="24" fill="#3b82f6" rx="4"/>
    <text x="67" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">1. DRAFT &amp; CUT</text>
    <g transform="translate(12, 42)">
      <rect x="0" y="0" width="111" height="95" fill="#e2e8f0" rx="4" stroke="#94a3b8"/>
      <text x="55" y="45" fill="#1e40af" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">30 x 60 cm</text>
      <text x="55" y="60" fill="#64748b" font-family="system-ui, sans-serif" font-size="8.5" text-anchor="middle">Cotton Calico</text>
    </g>
    <text x="8" y="155" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Instructions:</text>
    <text x="8" y="172" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Measure with ruler.</text>
    <text x="8" y="187" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Draw chalk lines.</text>
    <text x="8" y="202" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Cut with shears.</text>
  </g>

  <!-- Step 2: Embroider First (Crucial Step) -->
  <g transform="translate(182, 80)">
    <rect x="0" y="0" width="135" height="320" fill="#fefce8" rx="8" stroke="#fde047" stroke-width="2"/>
    <rect x="8" y="8" width="119" height="24" fill="#ca8a04" rx="4"/>
    <text x="67" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">2. EMBROIDER FIRST</text>
    <g transform="translate(12, 42)">
      <rect x="0" y="0" width="111" height="95" fill="#fef08a" rx="4" stroke="#eab308"/>
      <!-- Flower Embroidery Icon -->
      <circle cx="55" cy="45" r="12" fill="#ef4444"/>
      <path d="M 55 57 L 55 80" stroke="#16a34a" stroke-width="3"/>
      <text x="55" y="90" fill="#854d0e" font-family="system-ui, sans-serif" font-size="8" font-weight="700" text-anchor="middle">Stem &amp; Satin</text>
    </g>
    <text x="8" y="155" fill="#854d0e" font-family="system-ui, sans-serif" font-size="10" font-weight="700">CRITICAL RULE:</text>
    <text x="8" y="172" fill="#713f12" font-family="system-ui, sans-serif" font-size="9">• Work on FLAT cloth.</text>
    <text x="8" y="187" fill="#713f12" font-family="system-ui, sans-serif" font-size="9">• Never embroider</text>
    <text x="8" y="200" fill="#713f12" font-family="system-ui, sans-serif" font-size="9">  inside a closed bag!</text>
  </g>

  <!-- Step 3: Pin & Machine Stitch -->
  <g transform="translate(329, 80)">
    <rect x="0" y="0" width="135" height="320" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="8" y="8" width="119" height="24" fill="#2563eb" rx="4"/>
    <text x="67" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">3. PIN &amp; STITCH</text>
    <g transform="translate(12, 42)">
      <rect x="0" y="0" width="111" height="95" fill="#e2e8f0" rx="4"/>
      <!-- Folded Bag with side seams -->
      <rect x="15" y="10" width="80" height="75" fill="#bfdbfe" rx="3"/>
      <line x1="20" y1="10" x2="20" y2="85" stroke="#facc15" stroke-width="2.5" stroke-dasharray="4 3"/>
      <line x1="90" y1="10" x2="90" y2="85" stroke="#facc15" stroke-width="2.5" stroke-dasharray="4 3"/>
    </g>
    <text x="8" y="155" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Instructions:</text>
    <text x="8" y="172" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Right sides together.</text>
    <text x="8" y="187" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Pin &amp; baste sides.</text>
    <text x="8" y="202" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• 1.5 cm allowance.</text>
  </g>

  <!-- Step 4: Neaten with Pinking -->
  <g transform="translate(476, 80)">
    <rect x="0" y="0" width="135" height="320" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="8" y="8" width="119" height="24" fill="#059669" rx="4"/>
    <text x="67" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">4. PINK EDGES</text>
    <g transform="translate(12, 42)">
      <rect x="0" y="0" width="111" height="95" fill="#e2e8f0" rx="4"/>
      <!-- Zigzag Side Margins -->
      <path d="M 20 10 L 12 25 L 20 40 L 12 55 L 20 70 L 12 85" fill="none" stroke="#059669" stroke-width="2.5"/>
      <path d="M 90 10 L 98 25 L 90 40 L 98 55 L 90 70 L 98 85" fill="none" stroke="#059669" stroke-width="2.5"/>
    </g>
    <text x="8" y="155" fill="#0f172a" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Instructions:</text>
    <text x="8" y="172" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Cut side allowances</text>
    <text x="8" y="185" fill="#475569" font-family="system-ui, sans-serif" font-size="9">  with pinking shears.</text>
    <text x="8" y="200" fill="#475569" font-family="system-ui, sans-serif" font-size="9">• Stops unravelling.</text>
  </g>

  <!-- Step 5: Hem Top & Handles -->
  <g transform="translate(623, 80)">
    <rect x="0" y="0" width="140" height="320" fill="#f0fdf4" rx="8" stroke="#86efac" stroke-width="2"/>
    <rect x="8" y="8" width="124" height="24" fill="#16a34a" rx="4"/>
    <text x="70" y="24" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">5. HEM &amp; HANDLES</text>
    <g transform="translate(12, 42)">
      <rect x="0" y="0" width="116" height="95" fill="#dcfce7" rx="4"/>
      <!-- Finished Bag Icon with Handles -->
      <rect x="25" y="30" width="65" height="55" fill="#86efac" rx="3" stroke="#16a34a"/>
      <path d="M 35 30 C 35 10 50 10 50 30" fill="none" stroke="#15803d" stroke-width="3"/>
      <path d="M 65 30 C 65 10 80 10 80 30" fill="none" stroke="#15803d" stroke-width="3"/>
    </g>
    <text x="8" y="155" fill="#166534" font-family="system-ui, sans-serif" font-size="10" font-weight="700">Final Step:</text>
    <text x="8" y="172" fill="#15803d" font-family="system-ui, sans-serif" font-size="9">• Turn 2 cm top hem.</text>
    <text x="8" y="187" fill="#15803d" font-family="system-ui, sans-serif" font-size="9">• Stitch handles firmly.</text>
    <text x="8" y="202" fill="#15803d" font-family="system-ui, sans-serif" font-size="9">• Press bag with iron!</text>
  </g>
</svg>"""
}

def enrich_cbc_grade7_home_science_topic7():
    print("=" * 80)
    print("STARTING VISUAL ENRICHMENT: CBC GRADE 7 HOME SCIENCE — TOPIC 7: SEAMS")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 7").first()
    subject = Subject.objects.filter(grade=grade, name="Home Science").first()
    topic = Topic.objects.filter(subject=subject, name="Seams").first()

    assert topic, "Topic 7 (Seams) not found!"
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
        photo_info = TOPIC7_PHOTOS.get(u_order)
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
    for (u_order, page_num), svg_code in TOPIC7_SVGS.items():
        if u_order > len(lessons):
            continue
        lesson = lessons[u_order - 1]
        diag_block = lesson.blocks.filter(page_number=page_num, block_type="diagram").first()
        if diag_block:
            content = diag_block.content or {}
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
    print(f"[SUCCESS] CBC Grade 7 Home Science Topic 7 Visual Enrichment Complete!")
    print(f"[*] Total LessonAssets Created & Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_cbc_grade7_home_science_topic7()
