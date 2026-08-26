"""
VLearn CBC Grade 10 Chemistry — Topic 4: Chemical Bonding
Visual Enrichment Engine (Vector SVGs, Verified Wikimedia Hooks & YouTube Integration)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Chemistry (ID: 5)
Topic: Chemical Bonding (Topic Order: 4)
"""

import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Topic, Lesson, LessonBlock, LessonAsset
)

def sanitize_svg(svg: str) -> str:
    """Ensures SVG is clean, responsive, and stripped of unneeded XML/DOCTYPE headers."""
    svg = re.sub(r'<\?xml.*?\?>', '', svg)
    svg = re.sub(r'<!DOCTYPE.*?>', '', svg)
    return svg.strip()

# =============================================================================
# 6 CUSTOM RESPONSIVE VECTOR SVGS FOR TOPIC 4: CHEMICAL BONDING
# =============================================================================

# SVG 1: Lewis Dot-and-Cross Structures for Elements (Lesson 1, Page 3)
SVG_LEWIS_STRUCTURES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="10" y="10" width="780" height="430" rx="14" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">Lewis Dot-and-Cross Structures for Valence Shells</text>

  <!-- Row 1: Period 1 (H and He) -->
  <g transform="translate(30, 60)">
    <!-- H -->
    <rect x="0" y="0" width="70" height="70" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1"/>
    <text x="35" y="42" font-size="18" font-weight="bold" fill="#ffffff" text-anchor="middle">H</text>
    <circle cx="53" cy="37" r="3.5" fill="#facc15"/>
    <text x="35" y="62" font-size="8" fill="#94a3b8" text-anchor="middle">1 dot (1s¹)</text>

    <!-- He -->
    <rect x="670" y="0" width="70" height="70" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <text x="705" y="42" font-size="18" font-weight="bold" fill="#ffffff" text-anchor="middle">He</text>
    <circle cx="723" cy="32" r="3" fill="#34d399"/>
    <circle cx="723" cy="42" r="3" fill="#34d399"/>
    <text x="705" y="62" font-size="8" fill="#34d399" text-anchor="middle">Duplet (1s²)</text>
  </g>

  <!-- Row 2: Period 2 Elements (Li to Ne) -->
  <g transform="translate(30, 145)">
    <!-- Li (Group 1) -->
    <rect x="0" y="0" width="85" height="110" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="42" y="52" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">Li</text>
    <text x="58" y="46" font-size="14" font-weight="bold" fill="#ef4444">×</text>
    <text x="42" y="80" font-size="9" font-weight="bold" fill="#ef4444" text-anchor="middle">Group 1</text>
    <text x="42" y="95" font-size="8" fill="#cbd5e1" text-anchor="middle">1 valence e⁻</text>

    <!-- Be (Group 2) -->
    <rect x="95" y="0" width="85" height="110" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="137" y="52" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">Be</text>
    <text x="155" y="46" font-size="14" font-weight="bold" fill="#f59e0b">×</text>
    <text x="119" y="46" font-size="14" font-weight="bold" fill="#f59e0b">×</text>
    <text x="137" y="80" font-size="9" font-weight="bold" fill="#f59e0b" text-anchor="middle">Group 2</text>
    <text x="137" y="95" font-size="8" fill="#cbd5e1" text-anchor="middle">2 valence e⁻</text>

    <!-- B (Group 13) -->
    <rect x="190" y="0" width="85" height="110" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <text x="232" y="52" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">B</text>
    <text x="250" y="46" font-size="14" font-weight="bold" fill="#38bdf8">×</text>
    <text x="214" y="46" font-size="14" font-weight="bold" fill="#38bdf8">×</text>
    <text x="232" y="28" font-size="14" font-weight="bold" fill="#38bdf8">×</text>
    <text x="232" y="80" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Group 13</text>
    <text x="232" y="95" font-size="8" fill="#cbd5e1" text-anchor="middle">3 valence e⁻</text>

    <!-- C (Group 14) -->
    <rect x="285" y="0" width="85" height="110" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <text x="327" y="52" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">C</text>
    <text x="345" y="46" font-size="14" font-weight="bold" fill="#38bdf8">×</text>
    <text x="309" y="46" font-size="14" font-weight="bold" fill="#38bdf8">×</text>
    <text x="327" y="28" font-size="14" font-weight="bold" fill="#38bdf8">×</text>
    <text x="327" y="68" font-size="14" font-weight="bold" fill="#38bdf8">×</text>
    <text x="327" y="80" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Group 14</text>
    <text x="327" y="95" font-size="8" fill="#cbd5e1" text-anchor="middle">4 valence e⁻</text>

    <!-- N (Group 15) -->
    <rect x="380" y="0" width="85" height="110" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1"/>
    <text x="422" y="52" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">N</text>
    <circle cx="417" cy="28" r="3" fill="#a855f7"/><circle cx="427" cy="28" r="3" fill="#a855f7"/>
    <circle cx="442" cy="48" r="3" fill="#a855f7"/>
    <circle cx="402" cy="48" r="3" fill="#a855f7"/>
    <circle cx="422" cy="65" r="3" fill="#a855f7"/>
    <text x="422" y="80" font-size="9" font-weight="bold" fill="#a855f7" text-anchor="middle">Group 15</text>
    <text x="422" y="95" font-size="8" fill="#cbd5e1" text-anchor="middle">5 valence e⁻</text>

    <!-- O (Group 16) -->
    <rect x="475" y="0" width="85" height="110" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1"/>
    <text x="517" y="52" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">O</text>
    <circle cx="512" cy="28" r="3" fill="#a855f7"/><circle cx="522" cy="28" r="3" fill="#a855f7"/>
    <circle cx="512" cy="65" r="3" fill="#a855f7"/><circle cx="522" cy="65" r="3" fill="#a855f7"/>
    <circle cx="497" cy="48" r="3" fill="#a855f7"/>
    <circle cx="537" cy="48" r="3" fill="#a855f7"/>
    <text x="517" y="80" font-size="9" font-weight="bold" fill="#a855f7" text-anchor="middle">Group 16</text>
    <text x="517" y="95" font-size="8" fill="#cbd5e1" text-anchor="middle">6 valence e⁻</text>

    <!-- F (Group 17) -->
    <rect x="570" y="0" width="85" height="110" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="612" y="52" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">F</text>
    <circle cx="607" cy="28" r="3" fill="#a855f7"/><circle cx="617" cy="28" r="3" fill="#a855f7"/>
    <circle cx="607" cy="65" r="3" fill="#a855f7"/><circle cx="617" cy="65" r="3" fill="#a855f7"/>
    <circle cx="592" cy="43" r="3" fill="#a855f7"/><circle cx="592" cy="53" r="3" fill="#a855f7"/>
    <circle cx="632" cy="48" r="3" fill="#a855f7"/>
    <text x="612" y="80" font-size="9" font-weight="bold" fill="#a855f7" text-anchor="middle">Group 17</text>
    <text x="612" y="95" font-size="8" fill="#cbd5e1" text-anchor="middle">7 valence e⁻</text>

    <!-- Ne (Group 18) -->
    <rect x="665" y="0" width="75" height="110" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
    <text x="702" y="52" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">Ne</text>
    <circle cx="697" cy="28" r="3" fill="#34d399"/><circle cx="707" cy="28" r="3" fill="#34d399"/>
    <circle cx="697" cy="65" r="3" fill="#34d399"/><circle cx="707" cy="65" r="3" fill="#34d399"/>
    <circle cx="682" cy="43" r="3" fill="#34d399"/><circle cx="682" cy="53" r="3" fill="#34d399"/>
    <circle cx="722" cy="43" r="3" fill="#34d399"/><circle cx="722" cy="53" r="3" fill="#34d399"/>
    <text x="702" y="80" font-size="9" font-weight="bold" fill="#34d399" text-anchor="middle">Group 18</text>
    <text x="702" y="95" font-size="8" fill="#34d399" text-anchor="middle">Full Octet (8)</text>
  </g>

  <!-- Summary Banner -->
  <g transform="translate(30, 275)">
    <rect x="0" y="0" width="740" height="135" rx="8" fill="#1e293b" stroke="#334155"/>
    <text x="25" y="30" font-size="12" font-weight="bold" fill="#38bdf8">Rules of Lewis Dot-and-Cross Representation:</text>
    <text x="25" y="55" font-size="10.5" fill="#cbd5e1">• Symbol represents the nucleus and inner-core non-bonding electrons.</text>
    <text x="25" y="78" font-size="10.5" fill="#cbd5e1">• Dots (•) and crosses (×) represent outermost valence electrons only.</text>
    <text x="25" y="101" font-size="10.5" fill="#cbd5e1">• Electrons are placed singly on 4 sides before pairing up to reflect orbital occupancy.</text>
    <text x="25" y="122" font-size="10" fill="#34d399">Total valence dots = Group number (for main groups 1, 2, 13–18)</text>
  </g>
</svg>
""")

# SVG 2: Giant Ionic Lattice Architecture of NaCl (Lesson 2, Page 3)
SVG_NACL_LATTICE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="10" y="10" width="780" height="430" rx="14" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">3D Giant Ionic Lattice Architecture of Sodium Chloride (NaCl)</text>

  <!-- Left: 3D Isometric Cubic Lattice Grid -->
  <g transform="translate(60, 80)">
    <!-- Back plane bonds -->
    <line x1="80" y1="40" x2="260" y2="40" stroke="#475569" stroke-width="2"/>
    <line x1="80" y1="130" x2="260" y2="130" stroke="#475569" stroke-width="2"/>
    <line x1="80" y1="220" x2="260" y2="220" stroke="#475569" stroke-width="2"/>
    <line x1="80" y1="40" x2="80" y2="220" stroke="#475569" stroke-width="2"/>
    <line x1="170" y1="40" x2="170" y2="220" stroke="#475569" stroke-width="2"/>
    <line x1="260" y1="40" x2="260" y2="220" stroke="#475569" stroke-width="2"/>

    <!-- Depth bonds connecting back to front -->
    <line x1="80" y1="40" x2="30" y2="100" stroke="#475569" stroke-width="2"/>
    <line x1="170" y1="40" x2="120" y2="100" stroke="#475569" stroke-width="2"/>
    <line x1="260" y1="40" x2="210" y2="100" stroke="#475569" stroke-width="2"/>
    <line x1="80" y1="130" x2="30" y2="190" stroke="#475569" stroke-width="2"/>
    <line x1="170" y1="130" x2="120" y2="190" stroke="#475569" stroke-width="2"/>
    <line x1="260" y1="130" x2="210" y2="190" stroke="#475569" stroke-width="2"/>
    <line x1="80" y1="220" x2="30" y2="280" stroke="#475569" stroke-width="2"/>
    <line x1="170" y1="220" x2="120" y2="280" stroke="#475569" stroke-width="2"/>
    <line x1="260" y1="220" x2="210" y2="280" stroke="#475569" stroke-width="2"/>

    <!-- Front plane bonds -->
    <line x1="30" y1="100" x2="210" y2="100" stroke="#94a3b8" stroke-width="2"/>
    <line x1="30" y1="190" x2="210" y2="190" stroke="#94a3b8" stroke-width="2"/>
    <line x1="30" y1="280" x2="210" y2="280" stroke="#94a3b8" stroke-width="2"/>
    <line x1="30" y1="100" x2="30" y2="280" stroke="#94a3b8" stroke-width="2"/>
    <line x1="120" y1="100" x2="120" y2="280" stroke="#94a3b8" stroke-width="2"/>
    <line x1="210" y1="100" x2="210" y2="280" stroke="#94a3b8" stroke-width="2"/>

    <!-- Ions (Back layer) -->
    <circle cx="80" cy="40" r="12" fill="#22c55e"/><circle cx="170" cy="40" r="8" fill="#a855f7"/><circle cx="260" cy="40" r="12" fill="#22c55e"/>
    <circle cx="80" cy="130" r="8" fill="#a855f7"/><circle cx="170" cy="130" r="12" fill="#22c55e"/><circle cx="260" cy="130" r="8" fill="#a855f7"/>
    <circle cx="80" cy="220" r="12" fill="#22c55e"/><circle cx="170" cy="220" r="8" fill="#a855f7"/><circle cx="260" cy="220" r="12" fill="#22c55e"/>

    <!-- Ions (Front layer) -->
    <circle cx="30" cy="100" r="8" fill="#a855f7"/><circle cx="120" cy="100" r="14" fill="#22c55e"/><circle cx="210" cy="100" r="8" fill="#a855f7"/>
    <circle cx="30" cy="190" r="14" fill="#22c55e"/><circle cx="120" cy="190" r="9" fill="#a855f7"/><circle cx="210" cy="190" r="14" fill="#22c55e"/>
    <circle cx="30" cy="280" r="8" fill="#a855f7"/><circle cx="120" cy="280" r="14" fill="#22c55e"/><circle cx="210" cy="280" r="8" fill="#a855f7"/>
  </g>

  <!-- Right: Explanatory Panels -->
  <g transform="translate(380, 65)">
    <rect x="0" y="0" width="385" height="355" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="385" height="32" rx="10" fill="#0284c7"/>
    <text x="192" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">GIANT IONIC LATTICE KEY PRINCIPLES</text>

    <!-- Legend -->
    <rect x="20" y="45" width="345" height="55" rx="6" fill="#1e293b"/>
    <circle cx="45" cy="72" r="8" fill="#a855f7"/>
    <text x="60" y="76" font-size="10.5" font-weight="bold" fill="#ffffff">Na⁺ Cation (Small, +1)</text>
    <circle cx="205" cy="72" r="12" fill="#22c55e"/>
    <text x="225" y="76" font-size="10.5" font-weight="bold" fill="#ffffff">Cl⁻ Anion (Large, -1)</text>

    <!-- Details -->
    <rect x="20" y="110" width="345" height="230" rx="8" fill="#1e293b"/>
    <text x="30" y="135" font-size="11" font-weight="bold" fill="#38bdf8">1. 6:6 Coordination Geometry</text>
    <text x="30" y="155" font-size="10" fill="#cbd5e1">• Each Na⁺ is surrounded by 6 Cl⁻ ions.</text>
    <text x="30" y="172" font-size="10" fill="#cbd5e1">• Each Cl⁻ is surrounded by 6 Na⁺ ions.</text>

    <text x="30" y="200" font-size="11" font-weight="bold" fill="#facc15">2. Extreme Electrostatic Force</text>
    <text x="30" y="220" font-size="10" fill="#cbd5e1">• Non-directional attraction across all 3 dimensions.</text>
    <text x="30" y="237" font-size="10" fill="#cbd5e1">• Results in high melting point (801 °C).</text>

    <text x="30" y="265" font-size="11" font-weight="bold" fill="#34d399">3. Conductivity Breakdown</text>
    <text x="30" y="285" font-size="10" fill="#cbd5e1">• Solid: Non-conductor (ions locked in lattice).</text>
    <text x="30" y="302" font-size="10" fill="#cbd5e1">• Molten/Aqueous: Excellent (mobile Na⁺ and Cl⁻).</text>
    <text x="30" y="325" font-size="9" fill="#94a3b8">Net Formula is empirical ratio: NaCl (1:1)</text>
  </g>
</svg>
""")

# SVG 3: Dot-and-Cross Overlap Diagrams for H2, O2, N2 (Lesson 3, Page 2)
SVG_COVALENT_OVERLAP = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="10" y="10" width="780" height="430" rx="14" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">Dot-and-Cross Overlap Diagrams: Single, Double, and Triple Covalent Bonds</text>

  <!-- 1. Single Bond: H2 -->
  <g transform="translate(25, 65)">
    <rect x="0" y="0" width="235" height="355" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="235" height="30" rx="10" fill="#0284c7"/>
    <text x="117" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">SINGLE BOND: HYDROGEN (H₂)</text>

    <!-- Overlapping Circles -->
    <circle cx="85" cy="115" r="45" fill="none" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="150" cy="115" r="45" fill="none" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="120" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">H</text>
    <text x="170" y="120" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">H</text>
    <!-- Shared Pair (1 dot, 1 cross) -->
    <circle cx="117" cy="105" r="4" fill="#facc15"/>
    <text x="113" y="132" font-size="14" font-weight="bold" fill="#38bdf8">×</text>

    <rect x="10" y="180" width="215" height="160" rx="6" fill="#1e293b"/>
    <text x="20" y="205" font-size="11" font-weight="bold" fill="#38bdf8">H — H (1 Shared Pair)</text>
    <text x="20" y="230" font-size="10" fill="#cbd5e1">• 2 shared valence electrons</text>
    <text x="20" y="250" font-size="10" fill="#cbd5e1">• Both attain duplet stability (1s²)</text>
    <text x="20" y="270" font-size="10" fill="#cbd5e1">• Single line notation: <tspan fill="#ffffff" font-weight="bold">H—H</tspan></text>
    <text x="20" y="300" font-size="9" fill="#94a3b8">Bond length: 74 pm | Energy: 436 kJ/mol</text>
  </g>

  <!-- 2. Double Bond: O2 -->
  <g transform="translate(282, 65)">
    <rect x="0" y="0" width="235" height="355" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="0" y="0" width="235" height="30" rx="10" fill="#7e22ce"/>
    <text x="117" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">DOUBLE BOND: OXYGEN (O₂)</text>

    <!-- Overlapping Circles -->
    <circle cx="85" cy="115" r="45" fill="none" stroke="#a855f7" stroke-width="2"/>
    <circle cx="150" cy="115" r="45" fill="none" stroke="#a855f7" stroke-width="2"/>
    <text x="60" y="120" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">O</text>
    <text x="175" y="120" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">O</text>
    <!-- Shared 2 Pairs (2 dots, 2 crosses) -->
    <circle cx="113" cy="102" r="3.5" fill="#facc15"/><text x="117" y="106" font-size="12" font-weight="bold" fill="#a855f7">×</text>
    <circle cx="113" cy="125" r="3.5" fill="#facc15"/><text x="117" y="129" font-size="12" font-weight="bold" fill="#a855f7">×</text>
    <!-- Non-bonding lone pairs -->
    <circle cx="50" cy="95" r="3" fill="#facc15"/><circle cx="50" cy="135" r="3" fill="#facc15"/>
    <text x="180" y="97" font-size="10" font-weight="bold" fill="#a855f7">×</text><text x="180" y="137" font-size="10" font-weight="bold" fill="#a855f7">×</text>

    <rect x="10" y="180" width="215" height="160" rx="6" fill="#1e293b"/>
    <text x="20" y="205" font-size="11" font-weight="bold" fill="#a855f7">O = O (2 Shared Pairs)</text>
    <text x="20" y="230" font-size="10" fill="#cbd5e1">• 4 shared valence electrons</text>
    <text x="20" y="250" font-size="10" fill="#cbd5e1">• Both attain octet stability (2s² 2p⁶)</text>
    <text x="20" y="270" font-size="10" fill="#cbd5e1">• Double line notation: <tspan fill="#ffffff" font-weight="bold">O=O</tspan></text>
    <text x="20" y="300" font-size="9" fill="#94a3b8">Bond length: 121 pm | Energy: 498 kJ/mol</text>
  </g>

  <!-- 3. Triple Bond: N2 -->
  <g transform="translate(540, 65)">
    <rect x="0" y="0" width="235" height="355" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="235" height="30" rx="10" fill="#b91c1c"/>
    <text x="117" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">TRIPLE BOND: NITROGEN (N₂)</text>

    <!-- Overlapping Circles -->
    <circle cx="85" cy="115" r="45" fill="none" stroke="#ef4444" stroke-width="2"/>
    <circle cx="150" cy="115" r="45" fill="none" stroke="#ef4444" stroke-width="2"/>
    <text x="60" y="120" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">N</text>
    <text x="175" y="120" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">N</text>
    <!-- Shared 3 Pairs (3 dots, 3 crosses) -->
    <circle cx="113" cy="98" r="3" fill="#facc15"/><text x="117" y="102" font-size="11" font-weight="bold" fill="#ef4444">×</text>
    <circle cx="113" cy="115" r="3" fill="#facc15"/><text x="117" y="119" font-size="11" font-weight="bold" fill="#ef4444">×</text>
    <circle cx="113" cy="132" r="3" fill="#facc15"/><text x="117" y="136" font-size="11" font-weight="bold" fill="#ef4444">×</text>
    <!-- Non-bonding lone pairs -->
    <circle cx="50" cy="115" r="3" fill="#facc15"/>
    <text x="180" y="118" font-size="12" font-weight="bold" fill="#ef4444">×</text>

    <rect x="10" y="180" width="215" height="160" rx="6" fill="#1e293b"/>
    <text x="20" y="205" font-size="11" font-weight="bold" fill="#ef4444">N ≡ N (3 Shared Pairs)</text>
    <text x="20" y="230" font-size="10" fill="#cbd5e1">• 6 shared valence electrons</text>
    <text x="20" y="250" font-size="10" fill="#cbd5e1">• Immensely strong &amp; short bond</text>
    <text x="20" y="270" font-size="10" fill="#cbd5e1">• Triple line notation: <tspan fill="#ffffff" font-weight="bold">N≡N</tspan></text>
    <text x="20" y="300" font-size="9" fill="#34d399">Bond Energy: 945 kJ/mol (Ultra-stable!)</text>
  </g>
</svg>
""")

# SVG 4: Intramolecular vs Intermolecular Forces in Water (Lesson 4, Page 2)
SVG_WATER_HYDROGEN_BONDING = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="10" y="10" width="780" height="430" rx="14" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">Intramolecular Covalent Bonds vs. Intermolecular Hydrogen Bonds in Water</text>

  <!-- Left Side: 3 Water Molecules Cluster -->
  <g transform="translate(40, 70)">
    <rect x="0" y="0" width="370" height="350" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>

    <!-- Molecule 1 (Top Center) -->
    <circle cx="185" cy="80" r="24" fill="#ef4444" stroke="#f87171" stroke-width="1.5"/>
    <text x="185" y="85" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">O δ⁻</text>
    <line x1="168" y1="95" x2="140" y2="120" stroke="#ffffff" stroke-width="3"/>
    <circle cx="140" cy="120" r="14" fill="#38bdf8"/>
    <text x="140" y="124" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">H δ⁺</text>
    <line x1="202" y1="95" x2="230" y2="120" stroke="#ffffff" stroke-width="3"/>
    <circle cx="230" cy="120" r="14" fill="#38bdf8"/>
    <text x="230" y="124" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">H δ⁺</text>

    <!-- Molecule 2 (Bottom Left) -->
    <circle cx="90" cy="240" r="24" fill="#ef4444" stroke="#f87171" stroke-width="1.5"/>
    <text x="90" y="245" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">O δ⁻</text>
    <line x1="90" y1="216" x2="90" y2="185" stroke="#ffffff" stroke-width="3"/>
    <circle cx="90" cy="185" r="14" fill="#38bdf8"/><text x="90" y="189" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">H δ⁺</text>
    <line x1="110" y1="255" x2="140" y2="270" stroke="#ffffff" stroke-width="3"/>
    <circle cx="140" cy="270" r="14" fill="#38bdf8"/><text x="140" y="274" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">H δ⁺</text>

    <!-- Molecule 3 (Bottom Right) -->
    <circle cx="280" cy="240" r="24" fill="#ef4444" stroke="#f87171" stroke-width="1.5"/>
    <text x="280" y="245" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">O δ⁻</text>
    <line x1="260" y1="225" x2="230" y2="210" stroke="#ffffff" stroke-width="3"/>
    <circle cx="230" cy="210" r="14" fill="#38bdf8"/><text x="230" y="214" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">H δ⁺</text>
    <line x1="280" y1="264" x2="280" y2="295" stroke="#ffffff" stroke-width="3"/>
    <circle cx="280" cy="295" r="14" fill="#38bdf8"/><text x="280" y="299" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">H δ⁺</text>

    <!-- Dotted Hydrogen Bonds between molecules -->
    <line x1="140" y1="134" x2="90" y2="216" stroke="#facc15" stroke-width="3" stroke-dasharray="4,4"/>
    <line x1="230" y1="134" x2="280" y2="216" stroke="#facc15" stroke-width="3" stroke-dasharray="4,4"/>
    <line x1="154" y1="270" x2="260" y2="245" stroke="#facc15" stroke-width="3" stroke-dasharray="4,4"/>

    <!-- Pointer Labels -->
    <text x="185" y="170" font-size="10" font-weight="bold" fill="#facc15" text-anchor="middle">Hydrogen Bond (Intermolecular)</text>
  </g>

  <!-- Right Side: Comparison & Energy Analysis -->
  <g transform="translate(435, 70)">
    <rect x="0" y="0" width="335" height="350" rx="10" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect x="0" y="0" width="335" height="32" rx="10" fill="#059669"/>
    <text x="167" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">SCIENTIFIC COMPARISON &amp; BOILING</text>

    <!-- Intramolecular Box -->
    <rect x="15" y="45" width="305" height="110" rx="8" fill="#1e293b"/>
    <text x="25" y="70" font-size="11" font-weight="bold" fill="#ffffff">1. INTRAMOLECULAR COVALENT BOND</text>
    <text x="25" y="92" font-size="10" fill="#cbd5e1">• Solid line inside H₂O (between H and O)</text>
    <text x="25" y="112" font-size="10" fill="#cbd5e1">• <tspan fill="#34d399" font-weight="bold">Extremely strong</tspan> (~460 kJ/mol)</text>
    <text x="25" y="132" font-size="10" fill="#cbd5e1">• Never broken during boiling or physical phase change</text>

    <!-- Intermolecular Box -->
    <rect x="15" y="165" width="305" height="135" rx="8" fill="#1e293b"/>
    <text x="25" y="190" font-size="11" font-weight="bold" fill="#facc15">2. INTERMOLECULAR HYDROGEN BOND</text>
    <text x="25" y="212" font-size="10" fill="#cbd5e1">• Dotted line between O δ⁻ and H δ⁺ of neighbors</text>
    <text x="25" y="232" font-size="10" fill="#cbd5e1">• <tspan fill="#facc15" font-weight="bold">Moderate strength</tspan> (~20 kJ/mol)</text>
    <text x="25" y="252" font-size="10" fill="#cbd5e1">• Acts like "sticky velcro" pulling molecules close</text>
    <text x="25" y="275" font-size="10" fill="#38bdf8">• <tspan font-weight="bold">Broken when water boils at 100 °C</tspan></text>

    <text x="167" y="325" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">Steam is still H₂O molecules!</text>
  </g>
</svg>
""")

# SVG 5: Diamond vs Graphite Allotropes (Lesson 5, Page 3)
SVG_DIAMOND_VS_GRAPHITE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="10" y="10" width="780" height="430" rx="14" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">Structural Comparison: Diamond (3D Tetrahedral) vs. Graphite (Layered Hexagons)</text>

  <!-- Left: Diamond 3D Tetrahedral Network -->
  <g transform="translate(30, 65)">
    <rect x="0" y="0" width="345" height="355" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="30" rx="10" fill="#0284c7"/>
    <text x="172" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">DIAMOND: 3D TETRAHEDRAL NETWORK</text>

    <!-- Diamond Structure drawing -->
    <g transform="translate(172, 110)">
      <line x1="0" y1="0" x2="0" y2="-45" stroke="#38bdf8" stroke-width="3"/>
      <line x1="0" y1="0" x2="-45" y2="35" stroke="#38bdf8" stroke-width="3"/>
      <line x1="0" y1="0" x2="45" y2="35" stroke="#38bdf8" stroke-width="3"/>
      <line x1="0" y1="0" x2="0" y2="48" stroke="#38bdf8" stroke-width="3"/>

      <!-- Secondary tetrahedral bonds -->
      <line x1="0" y1="-45" x2="-35" y2="-75" stroke="#38bdf8" stroke-width="2"/>
      <line x1="0" y1="-45" x2="35" y2="-75" stroke="#38bdf8" stroke-width="2"/>
      <line x1="-45" y1="35" x2="-85" y2="45" stroke="#38bdf8" stroke-width="2"/>
      <line x1="45" y1="35" x2="85" y2="45" stroke="#38bdf8" stroke-width="2"/>

      <!-- Carbon Spheres -->
      <circle cx="0" cy="0" r="10" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5"/>
      <circle cx="0" cy="-45" r="8" fill="#38bdf8"/>
      <circle cx="-45" cy="35" r="8" fill="#38bdf8"/>
      <circle cx="45" cy="35" r="8" fill="#38bdf8"/>
      <circle cx="0" cy="48" r="8" fill="#38bdf8"/>
      <circle cx="-35" cy="-75" r="6" fill="#64748b"/>
      <circle cx="35" cy="-75" r="6" fill="#64748b"/>
    </g>

    <!-- Diamond Property Box -->
    <rect x="15" y="195" width="315" height="145" rx="6" fill="#1e293b"/>
    <text x="25" y="220" font-size="11" font-weight="bold" fill="#38bdf8">• 4 Covalent Bonds per Carbon</text>
    <text x="25" y="240" font-size="10" fill="#cbd5e1">• Rigid, interlocking 3D tetrahedral lattice</text>
    <text x="25" y="260" font-size="10" fill="#cbd5e1">• <tspan fill="#ffffff" font-weight="bold">Hardest natural substance</tspan> (MP &gt;3500 °C)</text>
    <text x="25" y="280" font-size="10" fill="#cbd5e1">• <tspan fill="#ef4444" font-weight="bold">Insulator</tspan>: All 4 valence e⁻ locked in bonds</text>
    <text x="25" y="315" font-size="9" fill="#94a3b8">Uses: Glass cutters, rock drill bits, jewelry</text>
  </g>

  <!-- Right: Graphite Hexagonal Sliding Sheets -->
  <g transform="translate(425, 65)">
    <rect x="0" y="0" width="345" height="355" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="30" rx="10" fill="#7e22ce"/>
    <text x="172" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">GRAPHITE: HEXAGONAL SLIDING LAYERS</text>

    <!-- Layer 1 (Top) -->
    <g transform="translate(90, 55)">
      <polygon points="40,0 80,0 100,25 80,50 40,50 20,25" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
      <polygon points="100,25 140,25 160,50 140,75 100,75 80,50" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
      <!-- Delocalized electron traveling -->
      <circle cx="80" cy="50" r="4" fill="#facc15"/>
      <circle cx="100" cy="25" r="4" fill="#facc15"/>
    </g>

    <!-- Dotted Van der Waals lines between layers -->
    <line x1="130" y1="105" x2="130" y2="130" stroke="#facc15" stroke-width="2" stroke-dasharray="3,3"/>
    <line x1="190" y1="105" x2="190" y2="130" stroke="#facc15" stroke-width="2" stroke-dasharray="3,3"/>
    <text x="215" y="122" font-size="8" fill="#facc15">Van der Waals</text>

    <!-- Layer 2 (Bottom) -->
    <g transform="translate(90, 130)">
      <polygon points="40,0 80,0 100,25 80,50 40,50 20,25" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
      <polygon points="100,25 140,25 160,50 140,75 100,75 80,50" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
    </g>

    <!-- Graphite Property Box -->
    <rect x="15" y="195" width="315" height="145" rx="6" fill="#1e293b"/>
    <text x="25" y="220" font-size="11" font-weight="bold" fill="#a855f7">• 3 Covalent Bonds per Carbon</text>
    <text x="25" y="240" font-size="10" fill="#cbd5e1">• Flat hexagonal sheets slide easily</text>
    <text x="25" y="260" font-size="10" fill="#cbd5e1">• <tspan fill="#34d399" font-weight="bold">Soft &amp; slippery</tspan> (weak Van der Waals)</text>
    <text x="25" y="280" font-size="10" fill="#cbd5e1">• <tspan fill="#facc15" font-weight="bold">Excellent Conductor</tspan>: 1 free e⁻/C is delocalized</text>
    <text x="25" y="315" font-size="9" fill="#94a3b8">Uses: Pencil leads, machinery lubricants, battery rods</text>
  </g>
</svg>
""")

# SVG 6: The 4 Major Material Architectures (Lesson 6, Page 2)
SVG_MATERIAL_ARCHITECTURES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="10" y="10" width="780" height="430" rx="14" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">Master Synthesis: The 4 Major Material Architectures</text>

  <!-- 1. Giant Ionic -->
  <g transform="translate(25, 65)">
    <rect x="0" y="0" width="175" height="355" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="175" height="28" rx="8" fill="#b91c1c"/>
    <text x="87" y="19" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">1. GIANT IONIC</text>

    <!-- Lattice drawing -->
    <circle cx="60" cy="70" r="10" fill="#a855f7"/><circle cx="115" cy="70" r="14" fill="#22c55e"/>
    <circle cx="60" cy="115" r="14" fill="#22c55e"/><circle cx="115" cy="115" r="10" fill="#a855f7"/>
    <line x1="60" y1="70" x2="115" y2="70" stroke="#64748b" stroke-width="2"/>
    <line x1="60" y1="115" x2="115" y2="115" stroke="#64748b" stroke-width="2"/>
    <line x1="60" y1="70" x2="60" y2="115" stroke="#64748b" stroke-width="2"/>
    <line x1="115" y1="70" x2="115" y2="115" stroke="#64748b" stroke-width="2"/>

    <rect x="10" y="145" width="155" height="200" rx="6" fill="#1e293b"/>
    <text x="18" y="170" font-size="10" font-weight="bold" fill="#ef4444">Example: NaCl</text>
    <text x="18" y="192" font-size="9" fill="#cbd5e1">• High melting point</text>
    <text x="18" y="210" font-size="9" fill="#cbd5e1">• Hard &amp; brittle</text>
    <text x="18" y="228" font-size="9" fill="#cbd5e1">• Soluble in water</text>
    <text x="18" y="250" font-size="9" font-weight="bold" fill="#facc15">Conductivity:</text>
    <text x="18" y="268" font-size="8.5" fill="#cbd5e1">• Solid: 0</text>
    <text x="18" y="284" font-size="8.5" fill="#34d399">• Molten/Aq: High</text>
    <text x="18" y="325" font-size="8.5" fill="#94a3b8">Electrostatic lattice</text>
  </g>

  <!-- 2. Simple Molecular -->
  <g transform="translate(215, 65)">
    <rect x="0" y="0" width="175" height="355" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="175" height="28" rx="8" fill="#0284c7"/>
    <text x="87" y="19" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">2. SIMPLE MOLECULAR</text>

    <!-- Molecules cluster -->
    <g transform="translate(50, 65)">
      <circle cx="20" cy="15" r="10" fill="#ef4444"/><circle cx="5" cy="28" r="6" fill="#38bdf8"/><circle cx="35" cy="28" r="6" fill="#38bdf8"/>
      <circle cx="65" cy="50" r="10" fill="#ef4444"/><circle cx="50" cy="63" r="6" fill="#38bdf8"/><circle cx="80" cy="63" r="6" fill="#38bdf8"/>
      <line x1="35" y1="28" x2="65" y2="50" stroke="#facc15" stroke-width="1.5" stroke-dasharray="2,2"/>
    </g>

    <rect x="10" y="145" width="155" height="200" rx="6" fill="#1e293b"/>
    <text x="18" y="170" font-size="10" font-weight="bold" fill="#38bdf8">Example: H₂O, CO₂</text>
    <text x="18" y="192" font-size="9" fill="#cbd5e1">• Low melting/boiling pt</text>
    <text x="18" y="210" font-size="9" fill="#cbd5e1">• Gases / liquids at RT</text>
    <text x="18" y="228" font-size="9" fill="#cbd5e1">• Weak intermolecular</text>
    <text x="18" y="250" font-size="9" font-weight="bold" fill="#facc15">Conductivity:</text>
    <text x="18" y="268" font-size="8.5" fill="#ef4444">• Insulator (no ions/e⁻)</text>
    <text x="18" y="325" font-size="8.5" fill="#94a3b8">Covalent molecules</text>
  </g>

  <!-- 3. Giant Covalent -->
  <g transform="translate(405, 65)">
    <rect x="0" y="0" width="175" height="355" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="0" y="0" width="175" height="28" rx="8" fill="#7e22ce"/>
    <text x="87" y="19" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">3. GIANT COVALENT</text>

    <!-- Network drawing -->
    <circle cx="87" cy="85" r="7" fill="#ffffff"/>
    <circle cx="55" cy="115" r="7" fill="#ffffff"/><circle cx="119" cy="115" r="7" fill="#ffffff"/><circle cx="87" cy="60" r="7" fill="#ffffff"/>
    <line x1="87" y1="85" x2="55" y2="115" stroke="#a855f7" stroke-width="2"/>
    <line x1="87" y1="85" x2="119" y2="115" stroke="#a855f7" stroke-width="2"/>
    <line x1="87" y1="85" x2="87" y2="60" stroke="#a855f7" stroke-width="2"/>

    <rect x="10" y="145" width="155" height="200" rx="6" fill="#1e293b"/>
    <text x="18" y="170" font-size="10" font-weight="bold" fill="#a855f7">Ex: Diamond, SiO₂</text>
    <text x="18" y="192" font-size="9" fill="#cbd5e1">• Extremely high MP</text>
    <text x="18" y="210" font-size="9" fill="#cbd5e1">• Insoluble in water</text>
    <text x="18" y="228" font-size="9" fill="#cbd5e1">• Infinite 3D network</text>
    <text x="18" y="250" font-size="9" font-weight="bold" fill="#facc15">Conductivity:</text>
    <text x="18" y="268" font-size="8.5" fill="#ef4444">• Diamond: Insulator</text>
    <text x="18" y="284" font-size="8.5" fill="#34d399">• Graphite: Conductor</text>
    <text x="18" y="325" font-size="8.5" fill="#94a3b8">Continuous bonds</text>
  </g>

  <!-- 4. Giant Metallic -->
  <g transform="translate(595, 65)">
    <rect x="0" y="0" width="175" height="355" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect x="0" y="0" width="175" height="28" rx="8" fill="#059669"/>
    <text x="87" y="19" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">4. GIANT METALLIC</text>

    <!-- Metal cations in sea -->
    <rect x="35" y="55" width="105" height="70" rx="6" fill="#0284c7" opacity="0.3"/>
    <circle cx="55" cy="75" r="8" fill="#38bdf8"/><text x="55" y="78" font-size="7" font-weight="bold" fill="#0f172a" text-anchor="middle">+</text>
    <circle cx="87" cy="75" r="8" fill="#38bdf8"/><text x="87" y="78" font-size="7" font-weight="bold" fill="#0f172a" text-anchor="middle">+</text>
    <circle cx="119" cy="75" r="8" fill="#38bdf8"/><text x="119" y="78" font-size="7" font-weight="bold" fill="#0f172a" text-anchor="middle">+</text>
    <circle cx="70" cy="105" r="8" fill="#38bdf8"/><text x="70" y="108" font-size="7" font-weight="bold" fill="#0f172a" text-anchor="middle">+</text>
    <circle cx="102" cy="105" r="8" fill="#38bdf8"/><text x="102" y="108" font-size="7" font-weight="bold" fill="#0f172a" text-anchor="middle">+</text>

    <rect x="10" y="145" width="155" height="200" rx="6" fill="#1e293b"/>
    <text x="18" y="170" font-size="10" font-weight="bold" fill="#34d399">Example: Cu, Al, Fe</text>
    <text x="18" y="192" font-size="9" fill="#cbd5e1">• Malleable &amp; ductile</text>
    <text x="18" y="210" font-size="9" fill="#cbd5e1">• High thermal transfer</text>
    <text x="18" y="228" font-size="9" fill="#cbd5e1">• Shiny metallic lustre</text>
    <text x="18" y="250" font-size="9" font-weight="bold" fill="#facc15">Conductivity:</text>
    <text x="18" y="268" font-size="8.5" fill="#34d399">• Solid: High</text>
    <text x="18" y="284" font-size="8.5" fill="#34d399">• Liquid: High</text>
    <text x="18" y="325" font-size="8.5" fill="#94a3b8">Delocalized electron sea</text>
  </g>
</svg>
""")

# =============================================================================
# VERIFIED WIKIMEDIA ASSETS FOR TOPIC 4
# =============================================================================

TOPIC4_ASSETS = [
    # Lesson 1 (1294)
    {
        "unit_order": 1,
        "page_number": 1,
        "block_type": "suggested_image",
        "asset_type": "image",
        "title": "The Chemical Cement of the Universe",
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Silicon-unit-cell-3D-balls.png",
        "caption": "Three-dimensional crystal unit cell model showing valence orbital bonding holding silicon atoms in a lattice.",
        "metadata": {
            "author": "Ben Mills",
            "licensing": "Public domain",
            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Silicon-unit-cell-3D-balls.png"
        }
    },
    {
        "unit_order": 1,
        "page_number": 3,
        "block_type": "suggested_diagram",
        "asset_type": "diagram",
        "title": "Lewis Dot-and-Cross Structures for the First 20 Elements",
        "svg_content": SVG_LEWIS_STRUCTURES,
        "metadata": {
            "svg_content": SVG_LEWIS_STRUCTURES,
            "theme": "dark"
        }
    },

    # Lesson 2 (1295)
    {
        "unit_order": 2,
        "page_number": 1,
        "block_type": "suggested_image",
        "asset_type": "image",
        "title": "The Crystalline Architecture of Salt",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/0e/Halite_crystal.jpg",
        "caption": "Natural cubic halite (rock salt) single crystal illustrating clean 90° cleavage planes arising from the repeating 3D giant ionic lattice.",
        "metadata": {
            "author": "Didier Descouens",
            "licensing": "CC BY-SA 4.0",
            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Halite_crystal.jpg"
        }
    },
    {
        "unit_order": 2,
        "page_number": 3,
        "block_type": "suggested_diagram",
        "asset_type": "diagram",
        "title": "3D Giant Ionic Lattice Architecture of Sodium Chloride (NaCl)",
        "svg_content": SVG_NACL_LATTICE,
        "metadata": {
            "svg_content": SVG_NACL_LATTICE,
            "theme": "dark"
        }
    },

    # Lesson 3 (1296)
    {
        "unit_order": 3,
        "page_number": 1,
        "block_type": "suggested_image",
        "asset_type": "image",
        "title": "Electron Sharing: The Covalent Link",
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/cd/Graduated_chemical_glassware_%28Alessandri_1895.2%29.png",
        "caption": "Precision scientific laboratory apparatus used in measuring covalent reaction rates and molecular transformations.",
        "metadata": {
            "author": "Alessandri / valeg96",
            "licensing": "Public domain",
            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Graduated_chemical_glassware_(Alessandri_1895.2).png"
        }
    },
    {
        "unit_order": 3,
        "page_number": 2,
        "block_type": "suggested_diagram",
        "asset_type": "diagram",
        "title": "Dot-and-Cross Overlap Diagrams: Single, Double, and Triple Covalent Bonds",
        "svg_content": SVG_COVALENT_OVERLAP,
        "metadata": {
            "svg_content": SVG_COVALENT_OVERLAP,
            "theme": "dark"
        }
    },

    # Lesson 4 (1297)
    {
        "unit_order": 4,
        "page_number": 1,
        "block_type": "suggested_image",
        "asset_type": "image",
        "title": "Intermolecular Forces & Metallic Structures",
        "url": "https://upload.wikimedia.org/wikipedia/commons/f/f0/Water_droplet_blue_bg05.jpg",
        "caption": "Cohesive spherical water droplet formed on a hydrophobic surface due to powerful intermolecular hydrogen bonding.",
        "metadata": {
            "author": "Daniel Schwen",
            "licensing": "CC BY-SA 4.0",
            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Water_droplet_blue_bg05.jpg"
        }
    },
    {
        "unit_order": 4,
        "page_number": 2,
        "block_type": "suggested_diagram",
        "asset_type": "diagram",
        "title": "Intramolecular Covalent Bonds vs. Intermolecular Hydrogen Bonds in Water",
        "svg_content": SVG_WATER_HYDROGEN_BONDING,
        "metadata": {
            "svg_content": SVG_WATER_HYDROGEN_BONDING,
            "theme": "dark"
        }
    },

    # Lesson 5 (1298)
    {
        "unit_order": 5,
        "page_number": 1,
        "block_type": "suggested_image",
        "asset_type": "image",
        "title": "Allotropes of Carbon: Diamond & Graphite",
        "url": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Rough_diamond.jpg",
        "caption": "Natural uncut octahedral diamond crystal displaying extreme hardness and brilliant adamantine lustre from pure carbon bonding.",
        "metadata": {
            "author": "Parent Géry",
            "licensing": "Public domain",
            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Rough_diamond.jpg"
        }
    },
    {
        "unit_order": 5,
        "page_number": 3,
        "block_type": "suggested_diagram",
        "asset_type": "diagram",
        "title": "Structural Comparison: Diamond (3D Tetrahedral) vs. Graphite (Layered Hexagons)",
        "svg_content": SVG_DIAMOND_VS_GRAPHITE,
        "metadata": {
            "svg_content": SVG_DIAMOND_VS_GRAPHITE,
            "theme": "dark"
        }
    },

    # Lesson 6 (1299)
    {
        "unit_order": 6,
        "page_number": 1,
        "block_type": "suggested_image",
        "asset_type": "image",
        "title": "Connecting Structure to Engineering Applications",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/6f/A_group_of_scientists_working_in_a_laboratory_Esculab.jpg",
        "caption": "Materials science engineering team synthesizing and evaluating modern nanocomposite polymers and alloys.",
        "metadata": {
            "author": "Esculab Lab",
            "licensing": "CC0",
            "commons_page_url": "https://commons.wikimedia.org/wiki/File:A_group_of_scientists_working_in_a_laboratory_Esculab.jpg"
        }
    },
    {
        "unit_order": 6,
        "page_number": 2,
        "block_type": "suggested_diagram",
        "asset_type": "diagram",
        "title": "Master Synthesis: The 4 Major Material Architectures",
        "svg_content": SVG_MATERIAL_ARCHITECTURES,
        "metadata": {
            "svg_content": SVG_MATERIAL_ARCHITECTURES,
            "theme": "dark"
        }
    }
]

def enrich_topic4():
    print("=" * 80)
    print("ENRICHING GRADE 10 CHEMISTRY — TOPIC 4: CHEMICAL BONDING")
    print("=" * 80)

    topic = Topic.objects.get(subject__id=5, order=4)
    print(f"Target Topic: [{topic.id}] {topic.name}")

    for asset_def in TOPIC4_ASSETS:
        unit_order = asset_def["unit_order"]
        page_num = asset_def["page_number"]
        block_type = asset_def["block_type"]
        asset_type = asset_def["asset_type"]
        title = asset_def["title"]
        metadata = asset_def.get("metadata", {})

        lesson = Lesson.objects.get(topic=topic, learning_unit__order=unit_order)
        block = LessonBlock.objects.filter(lesson=lesson, page_number=page_num, block_type=block_type).first()

        if not block:
            print(f"  [WARN] Block not found for Lesson [{lesson.id}] Page {page_num} ({block_type})")
            continue

        existing_asset = LessonAsset.objects.filter(lesson=lesson, title=title).first()
        if not existing_asset:
            asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type=asset_type,
                source_type="external" if asset_type != "diagram" else "ai_generated",
                storage_type="url" if asset_type != "diagram" else "embed",
                status="attached",
                title=title,
                url=asset_def.get("url"),
                description=asset_def.get("caption") or asset_def.get("description"),
                metadata=metadata
            )
            print(f"  [Created Asset] [{asset.asset_type}] '{title}' in Lesson [{lesson.id}]")
        else:
            asset = existing_asset
            asset.asset_type = asset_type
            asset.status = "attached"
            asset.url = asset_def.get("url")
            asset.description = asset_def.get("caption") or asset_def.get("description")
            asset.metadata = metadata
            asset.save()
            print(f"  [Updated Asset] [{asset.asset_type}] '{title}' in Lesson [{lesson.id}]")

        block.assets.add(asset)

        content = block.content or {}
        if asset_type == "image":
            content["resolved_image_url"] = asset_def["url"]
            content["caption"] = asset_def.get("caption")
        elif asset_type == "diagram":
            content["svg_content"] = asset_def.get("svg_content")
            content["caption"] = asset_def.get("title")

        block.content = content
        block.save()

    print("\nSUCCESS: Topic 4 Visual & Media Enrichment Completed!")

if __name__ == "__main__":
    enrich_topic4()
