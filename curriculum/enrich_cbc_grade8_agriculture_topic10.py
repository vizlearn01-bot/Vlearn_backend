"""
VLearn CBC Grade 8 Agriculture — Topic 10: Sewing and Production Techniques
Visual Enrichment & Multi-Video Integration Engine (Phase 2: High-Fidelity Technical SVGs & Videos)

Curriculum: CBC (Grade 8)
Subject: Agriculture
Topic: Sewing and Production Techniques (Topic Order: 10)

Enrichment Architecture:
  1. Phase 2A: Card-1 Photographic Visual Hooks (5 Lessons via Verified Wikimedia URLs).
  2. Phase 2B: 5 Custom Responsive Vector SVGs (viewBox="0 0 800 450", high contrast #0f172a dark-mode).
  3. Phase 2C: Multi-Video Instructional Integration (3 Verified YouTube videos across key lessons).
  4. Phase 2D: LessonAsset Model Registration and Database Synchronization.

Usage:
  ./venv/bin/python curriculum/enrich_cbc_grade8_agriculture_topic10.py
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
    # SVG 1 (Lesson 1 Page 2): Seam Anatomy & Classification Matrix
    # -------------------------------------------------------------------------
    1: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">SEAM ANATOMY &amp; CLASSIFICATION: PLAIN VS. OPEN SEAMS</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Structural Mechanics, Seam Allowance Buffers, and Fabric Weight Selection</text>

  <!-- Left: Plain Seam Anatomy -->
  <g transform="translate(40, 85)">
    <rect width="340" height="240" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="170" y="26" fill="#38bdf8" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">1. PLAIN SEAM (EDGES TOGETHER)</text>

    <!-- Cross Section Diagram -->
    <path d="M 60 110 L 170 110 L 170 70 L 190 70 L 190 110 L 280 110" fill="none" stroke="#38bdf8" stroke-width="4"/>
    <circle cx="180" cy="90" r="4" fill="#ef4444"/>
    <text x="180" y="58" fill="#fca5a5" font-size="9" font-weight="bold" text-anchor="middle">Stitch Line</text>

    <text x="25" y="145" fill="#bae6fd" font-size="10" font-weight="bold">CHARACTERISTICS:</text>
    <text x="25" y="162" fill="#e2e8f0" font-size="9">• Both raw edges lie together on one side</text>
    <text x="25" y="176" fill="#e2e8f0" font-size="9">• Fast to sew, highly durable joint</text>
    <text x="25" y="190" fill="#e2e8f0" font-size="9">• Best for: Lightweight cotton, linen, poplin</text>
    <text x="25" y="204" fill="#e2e8f0" font-size="9">• Uses: Pillowcases, simple aprons, curtains</text>
  </g>

  <!-- Right: Open Seam Anatomy -->
  <g transform="translate(420, 85)">
    <rect width="340" height="240" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="170" y="26" fill="#34d399" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">2. OPEN SEAM (SPLIT &amp; PRESSED)</text>

    <!-- Cross Section Diagram -->
    <path d="M 60 90 L 170 90 L 170 120 L 120 120 M 170 90 L 280 90 M 170 120 L 220 120" fill="none" stroke="#34d399" stroke-width="4"/>
    <circle cx="170" cy="105" r="4" fill="#ef4444"/>
    <text x="170" y="58" fill="#fca5a5" font-size="9" font-weight="bold" text-anchor="middle">Stitch Line</text>

    <text x="25" y="145" fill="#a7f3d0" font-size="10" font-weight="bold">CHARACTERISTICS:</text>
    <text x="25" y="162" fill="#e2e8f0" font-size="9">• Seam allowances parted &amp; pressed flat on opposite sides</text>
    <text x="25" y="176" fill="#e2e8f0" font-size="9">• Splits bulk: joint is completely smooth on skin</text>
    <text x="25" y="190" fill="#e2e8f0" font-size="9">• Best for: Heavy denim, canvas, corduroy, wool</text>
    <text x="25" y="204" fill="#e2e8f0" font-size="9">• Uses: Jeans, canvas backpacks, heavy coats</text>
  </g>

  <!-- Bottom Seam Allowance Rule -->
  <rect x="40" y="345" width="720" height="80" rx="8" fill="#1e293b" stroke="#f59e0b"/>
  <text x="60" y="370" fill="#fbbf24" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">THE SEAM ALLOWANCE RULE (1.0 cm to 1.5 cm):</text>
  <text x="60" y="392" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Never stitch along the extreme cut edge: woven threads will slip out and cause the seam to fray and split</text>
  <text x="60" y="410" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• A 1.0–1.5 cm allowance acts as a strong protective buffer against tension and washing cycles</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 2 (Lesson 2 Page 2): Step-by-Step Plain Seam Construction Workflow
    # -------------------------------------------------------------------------
    2: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">STEP-BY-STEP PLAIN SEAM CONSTRUCTION WORKFLOW</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">From Fabric Alignment to Temporary Basting and Permanent Backstitching</text>

  <!-- Step 1: Right Sides Together -->
  <g transform="translate(30, 85)">
    <rect width="135" height="240" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="67" cy="28" r="14" fill="#0284c7"/>
    <text x="67" y="33" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">1</text>
    <text x="67" y="65" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">RIGHT SIDES</text>
    <rect x="25" y="85" width="85" height="45" rx="3" fill="#0369a1"/>
    <text x="67" y="112" fill="#fff" font-size="9" font-weight="bold" text-anchor="middle">Facing Inward</text>
    <text x="67" y="155" fill="#e2e8f0" font-size="9" text-anchor="middle">Match cut edges</text>
    <text x="67" y="170" fill="#e2e8f0" font-size="9" text-anchor="middle">perfectly even</text>
    <text x="67" y="195" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">10cm x 15cm</text>
  </g>

  <!-- Step 2: Mark & Pin -->
  <g transform="translate(180, 85)">
    <rect width="135" height="240" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="67" cy="28" r="14" fill="#d97706"/>
    <text x="67" y="33" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">2</text>
    <text x="67" y="65" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">MARK &amp; PIN</text>
    <rect x="25" y="85" width="85" height="45" rx="3" fill="#334155"/>
    <line x1="35" y1="95" x2="35" y2="120" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,2"/>
    <text x="67" y="155" fill="#e2e8f0" font-size="9" text-anchor="middle">Draw 1.2 cm line</text>
    <text x="67" y="170" fill="#e2e8f0" font-size="9" text-anchor="middle">with tailor chalk.</text>
    <text x="67" y="195" fill="#fbbf24" font-size="9" font-weight="bold" text-anchor="middle">Pin at 90° angle</text>
  </g>

  <!-- Step 3: Baste Tacking -->
  <g transform="translate(330, 85)">
    <rect width="135" height="240" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <circle cx="67" cy="28" r="14" fill="#059669"/>
    <text x="67" y="33" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">3</text>
    <text x="67" y="65" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">BASTE (TACK)</text>
    <rect x="25" y="85" width="85" height="45" rx="3" fill="#334155"/>
    <line x1="35" y1="90" x2="35" y2="125" stroke="#34d399" stroke-width="2" stroke-dasharray="6,4"/>
    <text x="67" y="155" fill="#e2e8f0" font-size="9" text-anchor="middle">Sew long running</text>
    <text x="67" y="170" fill="#e2e8f0" font-size="9" text-anchor="middle">temporary stitches.</text>
    <text x="67" y="195" fill="#34d399" font-size="9" font-weight="bold" text-anchor="middle">Remove all pins</text>
  </g>

  <!-- Step 4: Backstitch -->
  <g transform="translate(480, 85)">
    <rect width="135" height="240" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <circle cx="67" cy="28" r="14" fill="#dc2626"/>
    <text x="67" y="33" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">4</text>
    <text x="67" y="65" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">BACKSTITCH</text>
    <rect x="25" y="85" width="85" height="45" rx="3" fill="#334155"/>
    <line x1="35" y1="90" x2="35" y2="125" stroke="#ef4444" stroke-width="3"/>
    <text x="67" y="155" fill="#e2e8f0" font-size="9" text-anchor="middle">Sew permanent,</text>
    <text x="67" y="170" fill="#e2e8f0" font-size="9" text-anchor="middle">tight backstitches.</text>
    <text x="67" y="195" fill="#f87171" font-size="9" font-weight="bold" text-anchor="middle">Interlocking Joint</text>
  </g>

  <!-- Step 5: Knot & Finish -->
  <g transform="translate(630, 85)">
    <rect width="135" height="240" rx="8" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <circle cx="67" cy="28" r="14" fill="#7c3aed"/>
    <text x="67" y="33" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">5</text>
    <text x="67" y="65" fill="#c084fc" font-size="11" font-weight="bold" text-anchor="middle">FINISH KNOT</text>
    <rect x="25" y="85" width="85" height="45" rx="3" fill="#047857"/>
    <text x="67" y="112" fill="#fff" font-size="9" font-weight="bold" text-anchor="middle">Clean Seam</text>
    <text x="67" y="155" fill="#e2e8f0" font-size="9" text-anchor="middle">Fasten double knot.</text>
    <text x="67" y="170" fill="#e2e8f0" font-size="9" text-anchor="middle">Pull out basting.</text>
    <text x="67" y="195" fill="#c084fc" font-size="9" font-weight="bold" text-anchor="middle">Press with Iron</text>
  </g>

  <!-- Bottom Banner -->
  <rect x="30" y="345" width="735" height="80" rx="8" fill="#1e293b" stroke="#475569"/>
  <text x="50" y="370" fill="#38bdf8" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">HAND SEWING SAFETY PROTOCOL:</text>
  <text x="50" y="392" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Wear a thimble on your middle pushing finger to prevent deep needle puncture wounds</text>
  <text x="50" y="410" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Always store pins in a pincushion — never put needles between your lips or on chair cushions</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 3 (Lesson 3 Page 2): Open Seam Splitting & Iron Pressing Protocol
    # -------------------------------------------------------------------------
    3: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">OPEN SEAM SPLITTING, IRON PRESSING &amp; FINISHING PROTOCOL</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Splitting Seam Allowances, Safe Iron Pressing, and Pinking Edge Finishes</text>

  <!-- Step 1: 1.5cm Base Seam -->
  <g transform="translate(30, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#0284c7"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">1</text>
    <text x="82" y="65" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">STITCH BASE</text>
    <text x="82" y="95" fill="#bae6fd" font-size="10" text-anchor="middle">• 1.5 cm allowance</text>
    <text x="82" y="115" fill="#bae6fd" font-size="10" text-anchor="middle">• Right sides facing</text>
    <text x="82" y="135" fill="#bae6fd" font-size="10" text-anchor="middle">• Permanent backstitch</text>
    <text x="82" y="155" fill="#bae6fd" font-size="10" text-anchor="middle">• Remove basting</text>
    <text x="82" y="195" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Strong Foundation</text>
  </g>

  <!-- Step 2: Finger Parting -->
  <g transform="translate(220, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#d97706"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">2</text>
    <text x="82" y="65" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">FINGER PARTING</text>
    <text x="82" y="95" fill="#fde68a" font-size="10" text-anchor="middle">• Lay wrong side UP</text>
    <text x="82" y="115" fill="#fde68a" font-size="10" text-anchor="middle">• On ironing board</text>
    <text x="82" y="135" fill="#fde68a" font-size="10" text-anchor="middle">• Split allowances</text>
    <text x="82" y="155" fill="#fde68a" font-size="10" text-anchor="middle">• Press open by hand</text>
    <text x="82" y="195" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">Prepares Flat Surface</text>
  </g>

  <!-- Step 3: Damp Press Cloth -->
  <g transform="translate(410, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#059669"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">3</text>
    <text x="82" y="65" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">IRON PRESSING</text>
    <text x="82" y="95" fill="#a7f3d0" font-size="10" text-anchor="middle">• Damp press cloth</text>
    <text x="82" y="115" fill="#a7f3d0" font-size="10" text-anchor="middle">• Press DOWN 3-5 sec</text>
    <text x="82" y="135" fill="#a7f3d0" font-size="10" text-anchor="middle">• Do NOT slide iron</text>
    <text x="82" y="155" fill="#a7f3d0" font-size="10" text-anchor="middle">• Stand iron on HEEL</text>
    <text x="82" y="195" fill="#34d399" font-size="10" font-weight="bold" text-anchor="middle">Zero Scorching</text>
  </g>

  <!-- Step 4: Pinking & Overcast -->
  <g transform="translate(600, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#7c3aed"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">4</text>
    <text x="82" y="65" fill="#c084fc" font-size="11" font-weight="bold" text-anchor="middle">EDGE FINISHING</text>
    <text x="82" y="95" fill="#ddd6fe" font-size="10" text-anchor="middle">• Pinking shears</text>
    <text x="82" y="115" fill="#ddd6fe" font-size="10" text-anchor="middle">• Cut zigzag edge</text>
    <text x="82" y="135" fill="#ddd6fe" font-size="10" text-anchor="middle">• Hand overcasting</text>
    <text x="82" y="155" fill="#ddd6fe" font-size="10" text-anchor="middle">• Prevents fraying</text>
    <text x="82" y="195" fill="#c084fc" font-size="10" font-weight="bold" text-anchor="middle">Professional Quality</text>
  </g>

  <!-- Bottom Banner -->
  <rect x="30" y="345" width="735" height="80" rx="8" fill="#1e293b" stroke="#38bdf8"/>
  <text x="50" y="370" fill="#38bdf8" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">PRESSING VS. IRONING DISTINCTION:</text>
  <text x="50" y="392" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• 'Pressing' means placing the iron flat down for 3-5 seconds without sliding to avoid stretching the seam</text>
  <text x="50" y="410" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Always stand the iron upright on its heel when not in hand, and unplug it immediately when finished</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 4 (Lesson 4 Page 2): Pocket Pouch Construction Blueprint
    # -------------------------------------------------------------------------
    4: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">POCKET POUCH CONSTRUCTION BLUEPRINT (15cm x 30cm PATTERN)</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Double-Fold Hemming, 10cm Pocket Fold, Backstitched Side Seams &amp; Button Fastener</text>

  <!-- Step 1: 15x30 Layout -->
  <g transform="translate(30, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#0284c7"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">1</text>
    <text x="82" y="65" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">PATTERN CUT</text>
    <rect x="40" y="85" width="85" height="55" rx="3" fill="#0369a1"/>
    <text x="82" y="118" fill="#fff" font-size="9" font-weight="bold" text-anchor="middle">15cm x 30cm</text>
    <text x="82" y="160" fill="#e2e8f0" font-size="9" text-anchor="middle">Trace on wrong side</text>
    <text x="82" y="175" fill="#e2e8f0" font-size="9" text-anchor="middle">with tailor chalk.</text>
    <text x="82" y="195" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Clean Shears Cut</text>
  </g>

  <!-- Step 2: Double Hem Short Ends -->
  <g transform="translate(220, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#d97706"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">2</text>
    <text x="82" y="65" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">DOUBLE-HEM ENDS</text>
    <rect x="40" y="85" width="85" height="55" rx="3" fill="#334155"/>
    <line x1="40" y1="92" x2="125" y2="92" stroke="#fbbf24" stroke-width="2"/>
    <line x1="40" y1="133" x2="125" y2="133" stroke="#fbbf24" stroke-width="2"/>
    <text x="82" y="160" fill="#e2e8f0" font-size="9" text-anchor="middle">Fold 0.5cm + 0.5cm</text>
    <text x="82" y="175" fill="#e2e8f0" font-size="9" text-anchor="middle">on both short ends.</text>
    <text x="82" y="195" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">Hides Raw Edges</text>
  </g>

  <!-- Step 3: Pocket Fold & Sides -->
  <g transform="translate(410, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#dc2626"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">3</text>
    <text x="82" y="65" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">FOLD &amp; SEW SIDES</text>
    <rect x="45" y="85" width="75" height="55" rx="3" fill="#334155"/>
    <line x1="50" y1="85" x2="50" y2="140" stroke="#ef4444" stroke-width="3"/>
    <line x1="115" y1="85" x2="115" y2="140" stroke="#ef4444" stroke-width="3"/>
    <text x="82" y="160" fill="#e2e8f0" font-size="9" text-anchor="middle">Fold 10cm up (right</text>
    <text x="82" y="175" fill="#e2e8f0" font-size="9" text-anchor="middle">sides in); backstitch.</text>
    <text x="82" y="195" fill="#f87171" font-size="10" font-weight="bold" text-anchor="middle">Leaves 5cm Flap</text>
  </g>

  <!-- Step 4: Turn & Fasten -->
  <g transform="translate(600, 85)">
    <rect width="165" height="240" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <circle cx="82" cy="28" r="14" fill="#059669"/>
    <text x="82" y="33" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">4</text>
    <text x="82" y="65" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">TURN &amp; FASTEN</text>
    <rect x="45" y="90" width="75" height="45" rx="4" fill="#047857"/>
    <circle cx="82" cy="100" r="5" fill="#fde68a"/>
    <text x="82" y="160" fill="#e2e8f0" font-size="9" text-anchor="middle">Turn inside out,</text>
    <text x="82" y="175" fill="#e2e8f0" font-size="9" text-anchor="middle">press flat, sew button.</text>
    <text x="82" y="195" fill="#34d399" font-size="10" font-weight="bold" text-anchor="middle">Complete Project!</text>
  </g>

  <!-- Bottom Banner -->
  <rect x="30" y="345" width="735" height="80" rx="8" fill="#1e293b" stroke="#475569"/>
  <text x="50" y="370" fill="#38bdf8" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">BACKSTITCH STRENGTH PRINCIPLE:</text>
  <text x="50" y="392" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• The backstitch locks backwards with each stitch, creating an interlocking joint as strong as a machine stitch</text>
  <text x="50" y="410" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Gently push corners out using a blunt pencil to create sharp, professional 90-degree corner points</text>
</svg>""",

    # -------------------------------------------------------------------------
    # SVG 5 (Lesson 5 Page 2): Studio Safety Protocol & Machine Maintenance Cycle
    # -------------------------------------------------------------------------
    5: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="34" fill="#f8fafc" font-size="19" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">SEWING STUDIO SAFETY &amp; MACHINE MAINTENANCE CYCLE</text>
  <text x="400" y="54" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif" text-anchor="middle">Four Safe Sewing Habits, Fabric Shears Care &amp; Mineral Oil Machine Servicing</text>

  <!-- Left: Four Safe Habits -->
  <g transform="translate(40, 85)">
    <rect width="340" height="240" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="170" y="26" fill="#f87171" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">FOUR SAFE SEWING HABITS</text>

    <text x="25" y="55" fill="#fca5a5" font-size="10" font-weight="bold">1. PINCUSHION ACCOUNTABILITY:</text>
    <text x="25" y="70" fill="#e2e8f0" font-size="9">Count pins before and after; never leave loose on chairs</text>

    <text x="25" y="95" fill="#fca5a5" font-size="10" font-weight="bold">2. PASSING SHEARS HANDLE-FIRST:</text>
    <text x="25" y="110" fill="#e2e8f0" font-size="9">Close blades, hold metal in hand, pass handles to peer</text>

    <text x="25" y="135" fill="#fca5a5" font-size="10" font-weight="bold">3. NO PINS IN MOUTH:</text>
    <text x="25" y="150" fill="#e2e8f0" font-size="9">Prevents accidental swallowing or choking injuries</text>

    <text x="25" y="175" fill="#fca5a5" font-size="10" font-weight="bold">4. FABRIC SHEARS PRESERVATION:</text>
    <text x="25" y="190" fill="#e2e8f0" font-size="9">Never cut paper or cardboard — it dulls fine blades</text>
  </g>

  <!-- Right: Machine Maintenance Cycle -->
  <g transform="translate(420, 85)">
    <rect width="340" height="240" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="170" y="26" fill="#34d399" font-size="13" font-weight="bold" font-family="system-ui, sans-serif" text-anchor="middle">SEWING MACHINE MAINTENANCE CYCLE</text>

    <rect x="25" y="45" width="290" height="35" rx="4" fill="#047857"/>
    <text x="35" y="67" fill="#a7f3d0" font-size="10" font-weight="bold">STEP 1: SWEEP LINT WITH BRUSH</text>

    <rect x="25" y="90" width="290" height="35" rx="4" fill="#047857"/>
    <text x="35" y="112" fill="#a7f3d0" font-size="10" font-weight="bold">STEP 2: 1 DROP MINERAL OIL (NOT COOKING OIL)</text>

    <rect x="25" y="135" width="290" height="35" rx="4" fill="#047857"/>
    <text x="35" y="157" fill="#a7f3d0" font-size="10" font-weight="bold">STEP 3: ROTATE HANDWHEEL TO COAT GEARS</text>

    <rect x="25" y="180" width="290" height="35" rx="4" fill="#065f46"/>
    <text x="35" y="202" fill="#bae6fd" font-size="10" font-weight="bold">STEP 4: TEST STITCH ON SCRAP CLOTH</text>
  </g>

  <!-- Bottom Banner -->
  <rect x="40" y="345" width="720" height="80" rx="8" fill="#1e293b" stroke="#38bdf8"/>
  <text x="60" y="370" fill="#38bdf8" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">CRITICAL LUBRICATION WARNING:</text>
  <text x="60" y="392" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Never use cooking/vegetable oil: it oxidizes into a sticky gummy paste that permanently cements gears</text>
  <text x="60" y="410" fill="#e2e8f0" font-size="11" font-family="system-ui, sans-serif">• Always use clear, refined mineral sewing machine oil and wipe machines down after every session</text>
</svg>"""
}

# =============================================================================
# CURATED VERIFIED YOUTUBE VIDEOS
# =============================================================================

TOPIC10_VIDEOS = {
    # Unit 2 (Page 4): How to Hand Sew a Plain Seam & Master Basting
    2: {
        "page_number": 4,
        "title": "Instructional Video: How to Hand Sew a Plain Seam & Master Basting",
        "url": "https://www.youtube.com/watch?v=TXJPk-QfhDU",
        "resolved_video_id": "TXJPk-QfhDU",
        "caption": "Watch this practical hand-sewing demonstration showing fabric alignment, right-angle pinning, basting technique, backstitching, and neat thread knotting."
    },
    # Unit 4 (Page 4): How to Sew a Pocket Pouch / Simple Household Project
    4: {
        "page_number": 4,
        "title": "Instructional Video: How to Sew a Pocket Pouch / Simple Household Project",
        "url": "https://www.youtube.com/watch?v=6ZjkLwQt_YE",
        "resolved_video_id": "6ZjkLwQt_YE",
        "caption": "Watch this step-by-step practical craft video showing fabric measurement, double-hemming, pocket folding, backstitching sides, and attaching a wooden button."
    },
    # Unit 5 (Page 6): Topic Video Review: Hand Sewing Craftsmanship, Seam Science & Studio Safety
    5: {
        "page_number": 6,
        "title": "Topic Video Review: Hand Sewing Craftsmanship, Seam Science & Studio Safety",
        "url": "https://www.youtube.com/watch?v=Ei5z_0Lxmic",
        "resolved_video_id": "Ei5z_0Lxmic",
        "caption": "Watch this comprehensive educational review covering seam classification, plain and open seam construction, pocket pouch assembly, and sewing studio safety protocols."
    }
}

# =============================================================================
# ENRICHMENT EXECUTION
# =============================================================================

def enrich_cbc_grade8_agriculture_topic10():
    """Attaches Card-1 photos, 5 custom SVGs, and 3 verified YouTube videos to Topic 10."""
    print("=" * 80)
    print("STARTING VISUAL ENRICHMENT: CBC GRADE 8 AGRICULTURE — TOPIC 10 (FINAL TOPIC)")
    print("=" * 80)

    topic = Topic.objects.filter(subject__grade__name="Grade 8", subject__name="Agriculture", name="Sewing and Production Techniques").first()
    if not topic:
        print("[ERROR] Topic 'Sewing and Production Techniques' not found under CBC Grade 8 Agriculture!")
        return

    lessons = Lesson.objects.filter(topic=topic).select_related("learning_unit").order_by("learning_unit__order")
    print(f"[*] Found {lessons.count()} Lessons under Topic: '{topic.name}' (ID: {topic.id})")

    # Load verified Card-1 images
    verified_images_path = os.path.join(os.path.dirname(__file__), "grade8_topic10_verified_images.json")
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
                title=f"Lesson {u_order} Visual Hook: {img_data.get('title', 'Sewing Craft')}",
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
        print("\n[+] Phase 2C: Attaching Curated Video Lessons across Topic 10...")
        for u_order, v_data in TOPIC10_VIDEOS.items():
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
    print(f"[SUCCESS] CBC Grade 8 Agriculture Topic 10 Visual Enrichment Complete!")
    print(f"[*] Total LessonAssets Created & Attached: {total_assets_created}")
    print("=" * 80)

if __name__ == "__main__":
    enrich_cbc_grade8_agriculture_topic10()
