"""
VLearn CBC Grade 10 Chemistry — Topic 3: The Periodic Table
Visual Enrichment Engine (Vector SVGs, Verified Wikimedia Hooks & YouTube Integration)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Chemistry (ID: 5)
Topic: The Periodic Table (Topic Order: 3)
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
# 6 CUSTOM RESPONSIVE VECTOR SVGS FOR TOPIC 3: THE PERIODIC TABLE
# =============================================================================

# SVG 1: Groups vs Periods (Lesson 1, Page 3)
SVG_GROUPS_PERIODS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="10" y="10" width="780" height="430" rx="14" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">Periodic Table Coordinates: Groups vs. Periods</text>

  <!-- Left Side: Simplified First 20 Elements Grid -->
  <g transform="translate(35, 65)">
    <rect x="0" y="0" width="440" height="355" rx="10" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <text x="220" y="24" font-size="12" font-weight="bold" fill="#cbd5e1" text-anchor="middle">THE FIRST 20 ELEMENTS GRID</text>

    <!-- Period 1 -->
    <rect x="20" y="45" width="45" height="45" rx="5" fill="#facc15" stroke="#eab308" stroke-width="2"/>
    <text x="42" y="66" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">H</text>
    <text x="42" y="80" font-size="8" fill="#0f172a" text-anchor="middle">1s¹</text>

    <rect x="375" y="45" width="45" height="45" rx="5" fill="#334155"/>
    <text x="397" y="66" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">He</text>
    <text x="397" y="80" font-size="8" fill="#94a3b8" text-anchor="middle">1s²</text>

    <!-- Period 2 -->
    <rect x="20" y="98" width="45" height="45" rx="5" fill="#facc15" stroke="#eab308" stroke-width="2"/>
    <text x="42" y="119" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Li</text>
    <text x="42" y="133" font-size="8" fill="#0f172a" text-anchor="middle">2s¹</text>

    <rect x="70" y="98" width="45" height="45" rx="5" fill="#334155"/>
    <text x="92" y="119" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Be</text>

    <rect x="175" y="98" width="35" height="45" rx="4" fill="#334155"/><text x="192" y="125" font-size="10" fill="#94a3b8" text-anchor="middle">B</text>
    <rect x="215" y="98" width="35" height="45" rx="4" fill="#334155"/><text x="232" y="125" font-size="10" fill="#94a3b8" text-anchor="middle">C</text>
    <rect x="255" y="98" width="35" height="45" rx="4" fill="#334155"/><text x="272" y="125" font-size="10" fill="#94a3b8" text-anchor="middle">N</text>
    <rect x="295" y="98" width="35" height="45" rx="4" fill="#334155"/><text x="312" y="125" font-size="10" fill="#94a3b8" text-anchor="middle">O</text>
    <rect x="335" y="98" width="35" height="45" rx="4" fill="#334155"/><text x="352" y="125" font-size="10" fill="#94a3b8" text-anchor="middle">F</text>
    <rect x="375" y="98" width="45" height="45" rx="5" fill="#334155"/><text x="397" y="125" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Ne</text>

    <!-- Period 3 (Highlighted Row) -->
    <rect x="15" y="150" width="410" height="52" rx="6" fill="#0284c7" opacity="0.3" stroke="#38bdf8" stroke-width="2"/>
    <rect x="20" y="153" width="45" height="45" rx="5" fill="#facc15" stroke="#eab308" stroke-width="2"/>
    <text x="42" y="174" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Na</text>
    <text x="42" y="188" font-size="8" fill="#0f172a" text-anchor="middle">3s¹</text>

    <rect x="70" y="153" width="45" height="45" rx="5" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
    <text x="92" y="174" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Mg</text>
    <rect x="175" y="153" width="35" height="45" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/><text x="192" y="180" font-size="10" fill="#ffffff" text-anchor="middle">Al</text>
    <rect x="215" y="153" width="35" height="45" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/><text x="232" y="180" font-size="10" fill="#ffffff" text-anchor="middle">Si</text>
    <rect x="255" y="153" width="35" height="45" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/><text x="272" y="180" font-size="10" fill="#ffffff" text-anchor="middle">P</text>
    <rect x="295" y="153" width="35" height="45" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/><text x="312" y="180" font-size="10" fill="#ffffff" text-anchor="middle">S</text>
    <rect x="335" y="153" width="35" height="45" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/><text x="352" y="180" font-size="10" fill="#ffffff" text-anchor="middle">Cl</text>
    <rect x="375" y="153" width="45" height="45" rx="5" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/><text x="397" y="180" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Ar</text>

    <!-- Period 4 -->
    <rect x="20" y="210" width="45" height="45" rx="5" fill="#facc15" stroke="#eab308" stroke-width="2"/>
    <text x="42" y="231" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">K</text>
    <text x="42" y="245" font-size="8" fill="#0f172a" text-anchor="middle">4s¹</text>

    <rect x="70" y="210" width="45" height="45" rx="5" fill="#334155"/>
    <text x="92" y="231" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Ca</text>

    <!-- Highlighted Group 1 Column Box -->
    <rect x="16" y="40" width="53" height="220" rx="6" fill="none" stroke="#eab308" stroke-width="2.5" stroke-dasharray="4,4"/>
    <text x="42" y="280" font-size="10" font-weight="bold" fill="#facc15" text-anchor="middle">GROUP 1</text>
    <text x="42" y="295" font-size="8" fill="#cbd5e1" text-anchor="middle">(1 valence e⁻)</text>

    <!-- Highlighted Period 3 Row Label -->
    <text x="220" y="325" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">← PERIOD 3 (3 Occupied Shells: Level 1, 2, 3) →</text>
  </g>

  <!-- Right Side: Rules & Definitions -->
  <g transform="translate(495, 65)">
    <rect x="0" y="0" width="275" height="355" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="275" height="32" rx="10" fill="#0284c7"/>
    <text x="137" y="22" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">THE RULES OF THE GRID</text>

    <!-- Group Rule -->
    <rect x="12" y="45" width="251" height="135" rx="8" fill="#1e293b"/>
    <text x="22" y="70" font-size="12" font-weight="bold" fill="#facc15">1. GROUPS (Vertical Columns)</text>
    <text x="22" y="92" font-size="10" fill="#cbd5e1">• 18 vertical columns</text>
    <text x="22" y="112" font-size="10" fill="#cbd5e1">• <tspan fill="#facc15" font-weight="bold">Group # = Valence Electrons</tspan></text>
    <text x="22" y="132" font-size="10" fill="#cbd5e1">• Same chemical family</text>
    <text x="22" y="152" font-size="10" fill="#cbd5e1">• Identical chemical reactivity</text>
    <text x="22" y="170" font-size="9" fill="#94a3b8">Ex: Li, Na, K all end in ns¹</text>

    <!-- Period Rule -->
    <rect x="12" y="195" width="251" height="145" rx="8" fill="#1e293b"/>
    <text x="22" y="220" font-size="12" font-weight="bold" fill="#38bdf8">2. PERIODS (Horizontal Rows)</text>
    <text x="22" y="242" font-size="10" fill="#cbd5e1">• 7 horizontal rows</text>
    <text x="22" y="262" font-size="10" fill="#cbd5e1">• <tspan fill="#38bdf8" font-weight="bold">Period # = Occupied Shells</tspan></text>
    <text x="22" y="282" font-size="10" fill="#cbd5e1">• Electrons add to same main level</text>
    <text x="22" y="302" font-size="10" fill="#cbd5e1">• Atomic number increases by 1</text>
    <text x="22" y="322" font-size="9" fill="#94a3b8">Ex: Na to Ar all occupy n=1, 2, 3</text>
  </g>
</svg>
""")

# SVG 2: Chemical Families & Stability Pathways (Lesson 2, Page 3)
SVG_FAMILIES_STABILITY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="10" y="10" width="780" height="430" rx="14" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">Chemical Families &amp; Electron Stability Pathways</text>

  <!-- Family 1: Alkali Metals -->
  <g transform="translate(25, 65)">
    <rect x="0" y="0" width="175" height="355" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="175" height="28" rx="8" fill="#b91c1c"/>
    <text x="87" y="19" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">GROUP 1: ALKALI</text>

    <!-- Shell Diagram -->
    <circle cx="87" cy="95" r="42" fill="none" stroke="#475569" stroke-width="1.5"/>
    <circle cx="87" cy="95" r="14" fill="#ef4444"/>
    <text x="87" y="99" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Na</text>
    <circle cx="87" cy="53" r="4.5" fill="#facc15"/>
    <text x="87" y="44" font-size="8" fill="#facc15" text-anchor="middle">1 valence e⁻</text>

    <rect x="10" y="150" width="155" height="195" rx="6" fill="#1e293b"/>
    <text x="18" y="172" font-size="10" font-weight="bold" fill="#ef4444">Outer: ns¹</text>
    <text x="18" y="192" font-size="9.5" fill="#cbd5e1">• Members: Li, Na, K</text>
    <text x="18" y="212" font-size="9.5" fill="#cbd5e1">• Soft, cut with knife</text>
    <text x="18" y="232" font-size="9.5" fill="#cbd5e1">• React violently in H₂O</text>
    <text x="18" y="260" font-size="10" font-weight="bold" fill="#facc15">Pathway:</text>
    <text x="18" y="280" font-size="9" fill="#cbd5e1">Lose 1 e⁻ → Na⁺</text>
    <text x="18" y="298" font-size="9" fill="#34d399">Stable [Ne] Octet!</text>
    <text x="18" y="325" font-size="8.5" fill="#94a3b8">Stored in paraffin oil</text>
  </g>

  <!-- Family 2: Alkaline Earth -->
  <g transform="translate(215, 65)">
    <rect x="0" y="0" width="175" height="355" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="0" y="0" width="175" height="28" rx="8" fill="#b45309"/>
    <text x="87" y="19" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">GROUP 2: EARTH</text>

    <!-- Shell Diagram -->
    <circle cx="87" cy="95" r="42" fill="none" stroke="#475569" stroke-width="1.5"/>
    <circle cx="87" cy="95" r="14" fill="#f59e0b"/>
    <text x="87" y="99" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Mg</text>
    <circle cx="60" cy="62" r="4.5" fill="#facc15"/>
    <circle cx="114" cy="62" r="4.5" fill="#facc15"/>
    <text x="87" y="44" font-size="8" fill="#facc15" text-anchor="middle">2 valence e⁻</text>

    <rect x="10" y="150" width="155" height="195" rx="6" fill="#1e293b"/>
    <text x="18" y="172" font-size="10" font-weight="bold" fill="#f59e0b">Outer: ns²</text>
    <text x="18" y="192" font-size="9.5" fill="#cbd5e1">• Members: Be, Mg, Ca</text>
    <text x="18" y="212" font-size="9.5" fill="#cbd5e1">• Harder, denser metals</text>
    <text x="18" y="232" font-size="9.5" fill="#cbd5e1">• Burn with bright flame</text>
    <text x="18" y="260" font-size="10" font-weight="bold" fill="#facc15">Pathway:</text>
    <text x="18" y="280" font-size="9" fill="#cbd5e1">Lose 2 e⁻ → Mg²⁺</text>
    <text x="18" y="298" font-size="9" fill="#34d399">Stable [Ne] Octet!</text>
    <text x="18" y="325" font-size="8.5" fill="#94a3b8">Used in flares &amp; alloys</text>
  </g>

  <!-- Family 3: Halogens -->
  <g transform="translate(405, 65)">
    <rect x="0" y="0" width="175" height="355" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="0" y="0" width="175" height="28" rx="8" fill="#7e22ce"/>
    <text x="87" y="19" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">GROUP 17: HALOGENS</text>

    <!-- Shell Diagram -->
    <circle cx="87" cy="95" r="42" fill="none" stroke="#475569" stroke-width="1.5"/>
    <circle cx="87" cy="95" r="14" fill="#a855f7"/>
    <text x="87" y="99" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Cl</text>
    <circle cx="87" cy="53" r="4.5" fill="#facc15"/>
    <circle cx="120" cy="70" r="4.5" fill="#facc15"/>
    <circle cx="120" cy="120" r="4.5" fill="#facc15"/>
    <circle cx="87" cy="137" r="4.5" fill="#facc15"/>
    <circle cx="54" cy="120" r="4.5" fill="#facc15"/>
    <circle cx="54" cy="70" r="4.5" fill="#facc15"/>
    <circle cx="102" cy="56" r="4.5" fill="#facc15"/>
    <text x="87" y="44" font-size="8" fill="#facc15" text-anchor="middle">7 valence e⁻</text>

    <rect x="10" y="150" width="155" height="195" rx="6" fill="#1e293b"/>
    <text x="18" y="172" font-size="10" font-weight="bold" fill="#a855f7">Outer: ns² np⁵</text>
    <text x="18" y="192" font-size="9.5" fill="#cbd5e1">• Members: F, Cl, Br, I</text>
    <text x="18" y="212" font-size="9.5" fill="#cbd5e1">• Toxic, colored nonmetals</text>
    <text x="18" y="232" font-size="9.5" fill="#cbd5e1">• "Salt-formers"</text>
    <text x="18" y="260" font-size="10" font-weight="bold" fill="#facc15">Pathway:</text>
    <text x="18" y="280" font-size="9" fill="#cbd5e1">Gain 1 e⁻ → Cl⁻</text>
    <text x="18" y="298" font-size="9" fill="#34d399">Stable [Ar] Octet!</text>
    <text x="18" y="325" font-size="8.5" fill="#94a3b8">Diatomic: Cl₂, Br₂, I₂</text>
  </g>

  <!-- Family 4: Noble Gases -->
  <g transform="translate(595, 65)">
    <rect x="0" y="0" width="175" height="355" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect x="0" y="0" width="175" height="28" rx="8" fill="#059669"/>
    <text x="87" y="19" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">GROUP 18: NOBLE</text>

    <!-- Shell Diagram -->
    <circle cx="87" cy="95" r="42" fill="none" stroke="#34d399" stroke-width="2"/>
    <circle cx="87" cy="95" r="14" fill="#34d399"/>
    <text x="87" y="99" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">Ne</text>
    <!-- Full 8 electrons -->
    <circle cx="87" cy="53" r="4" fill="#34d399"/><circle cx="117" cy="65" r="4" fill="#34d399"/>
    <circle cx="129" cy="95" r="4" fill="#34d399"/><circle cx="117" cy="125" r="4" fill="#34d399"/>
    <circle cx="87" cy="137" r="4" fill="#34d399"/><circle cx="57" cy="125" r="4" fill="#34d399"/>
    <circle cx="45" cy="95" r="4" fill="#34d399"/><circle cx="57" cy="65" r="4" fill="#34d399"/>
    <text x="87" y="44" font-size="8" fill="#34d399" text-anchor="middle">Full Octet (8 e⁻)</text>

    <rect x="10" y="150" width="155" height="195" rx="6" fill="#1e293b"/>
    <text x="18" y="172" font-size="10" font-weight="bold" fill="#34d399">Outer: ns² np⁶</text>
    <text x="18" y="192" font-size="9.5" fill="#cbd5e1">• Members: He, Ne, Ar</text>
    <text x="18" y="212" font-size="9.5" fill="#cbd5e1">• Colorless, odorless</text>
    <text x="18" y="232" font-size="9.5" fill="#cbd5e1">• Monatomic gases</text>
    <text x="18" y="260" font-size="10" font-weight="bold" fill="#34d399">Pathway:</text>
    <text x="18" y="280" font-size="9" fill="#34d399">Already Stable!</text>
    <text x="18" y="298" font-size="9" fill="#cbd5e1">0 electron transfer</text>
    <text x="18" y="325" font-size="8.5" fill="#94a3b8">Used in neon signs &amp; lasers</text>
  </g>
</svg>
""")

# SVG 3: Electron Transfer Cation and Anion Formation (Lesson 3, Page 2)
SVG_ELECTRON_TRANSFER = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="10" y="10" width="780" height="430" rx="14" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">Electron Transfer: Sodium Cation &amp; Chloride Anion Formation</text>

  <!-- Left: Sodium Atom loses 1 e- -->
  <g transform="translate(30, 65)">
    <rect x="0" y="0" width="340" height="355" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="0" y="0" width="340" height="30" rx="10" fill="#b91c1c"/>
    <text x="170" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">SODIUM: ELECTRON LOSS (CATION)</text>

    <!-- Sodium Atom -->
    <circle cx="170" cy="110" r="55" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3,3"/>
    <circle cx="170" cy="110" r="38" fill="none" stroke="#64748b" stroke-width="1.5"/>
    <circle cx="170" cy="110" r="22" fill="none" stroke="#64748b" stroke-width="1.5"/>
    <circle cx="170" cy="110" r="14" fill="#ef4444"/>
    <text x="170" y="114" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">11p</text>

    <!-- Leaving electron -->
    <circle cx="230" cy="85" r="5" fill="#facc15" stroke="#f59e0b" stroke-width="1.5"/>
    <path d="M 225,110 Q 240,90 280,75" fill="none" stroke="#facc15" stroke-width="2" stroke-dasharray="3,3"/>
    <text x="280" y="70" font-size="9" font-weight="bold" fill="#facc15">e⁻ departs</text>

    <!-- Reaction Box -->
    <rect x="15" y="195" width="310" height="145" rx="6" fill="#1e293b"/>
    <text x="25" y="220" font-size="11" font-weight="bold" fill="#ef4444">Sodium Atom (Na) → Cation (Na⁺):</text>
    <text x="25" y="242" font-size="10" fill="#cbd5e1">• Atom: 11p⁺, 11e⁻ (1s² 2s² 2p⁶ 3s¹)</text>
    <text x="25" y="264" font-size="10" fill="#cbd5e1">• Loses 1 valence electron from 3s</text>
    <text x="25" y="286" font-size="10" fill="#34d399">• Cation: 11p⁺, 10e⁻ (1s² 2s² 2p⁶ [Ne])</text>
    <text x="25" y="315" font-size="12" font-weight="bold" fill="#fbbf24">Na → Na⁺ + e⁻  (Charge: +1)</text>
  </g>

  <!-- Right: Chlorine Atom gains 1 e- -->
  <g transform="translate(425, 65)">
    <rect x="0" y="0" width="340" height="355" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="340" height="30" rx="10" fill="#0284c7"/>
    <text x="170" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">CHLORINE: ELECTRON GAIN (ANION)</text>

    <!-- Chlorine Atom -->
    <circle cx="170" cy="110" r="55" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="170" cy="110" r="38" fill="none" stroke="#64748b" stroke-width="1.5"/>
    <circle cx="170" cy="110" r="22" fill="none" stroke="#64748b" stroke-width="1.5"/>
    <circle cx="170" cy="110" r="14" fill="#38bdf8"/>
    <text x="170" y="114" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">17p</text>

    <!-- Incoming electron into vacancy -->
    <circle cx="115" cy="110" r="5" fill="#facc15" stroke="#34d399" stroke-width="2"/>
    <text x="80" y="114" font-size="8" font-weight="bold" fill="#34d399">+1 e⁻ in</text>

    <!-- Reaction Box -->
    <rect x="15" y="195" width="310" height="145" rx="6" fill="#1e293b"/>
    <text x="25" y="220" font-size="11" font-weight="bold" fill="#38bdf8">Chlorine Atom (Cl) → Anion (Cl⁻):</text>
    <text x="25" y="242" font-size="10" fill="#cbd5e1">• Atom: 17p⁺, 17e⁻ (1s² 2s² 2p⁶ 3s² 3p⁵)</text>
    <text x="25" y="264" font-size="10" fill="#cbd5e1">• Gains 1 electron into 3p orbital</text>
    <text x="25" y="286" font-size="10" fill="#34d399">• Anion: 17p⁺, 18e⁻ (1s² 2s² 2p⁶ 3s² 3p⁶ [Ar])</text>
    <text x="25" y="315" font-size="12" font-weight="bold" fill="#fbbf24">Cl + e⁻ → Cl⁻  (Charge: -1)</text>
  </g>
</svg>
""")

# SVG 4: Valency Swap & Bracket Rule (Lesson 4, Page 3)
SVG_VALENCY_SWAP = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="10" y="10" width="780" height="430" rx="14" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Valency Swap (Crossover) Method &amp; Radical Bracket Rule</text>

  <!-- Left Example: Aluminium Oxide -->
  <g transform="translate(35, 65)">
    <rect x="0" y="0" width="340" height="355" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="340" height="30" rx="10" fill="#0284c7"/>
    <text x="170" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">EXAMPLE 1: ALUMINIUM OXIDE</text>

    <!-- Top Symbols & Valencies -->
    <rect x="40" y="45" width="100" height="70" rx="8" fill="#1e293b" stroke="#334155"/>
    <text x="90" y="70" font-size="16" font-weight="bold" fill="#f59e0b">Valency: 3</text>
    <text x="90" y="100" font-size="28" font-weight="bold" fill="#ffffff">Al</text>

    <rect x="200" y="45" width="100" height="70" rx="8" fill="#1e293b" stroke="#334155"/>
    <text x="250" y="70" font-size="16" font-weight="bold" fill="#f59e0b">Valency: 2</text>
    <text x="250" y="100" font-size="28" font-weight="bold" fill="#ffffff">O</text>

    <!-- Crossover Arrows -->
    <path d="M 120,65 Q 170,110 240,140" fill="none" stroke="#ef4444" stroke-width="3"/>
    <path d="M 220,65 Q 170,110 100,140" fill="none" stroke="#38bdf8" stroke-width="3"/>

    <!-- Bottom Swapped Subscripts -->
    <rect x="40" y="145" width="260" height="75" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="100" y="192" font-size="36" font-weight="bold" fill="#ffffff">Al</text>
    <text x="140" y="205" font-size="28" font-weight="bold" fill="#38bdf8">2</text>
    <text x="190" y="192" font-size="36" font-weight="bold" fill="#ffffff">O</text>
    <text x="225" y="205" font-size="28" font-weight="bold" fill="#ef4444">3</text>

    <!-- Explanation Box -->
    <rect x="15" y="235" width="310" height="105" rx="6" fill="#1e293b"/>
    <text x="25" y="258" font-size="10.5" fill="#cbd5e1">• Swap valency 3 (from Al) to O subscript</text>
    <text x="25" y="278" font-size="10.5" fill="#cbd5e1">• Swap valency 2 (from O) to Al subscript</text>
    <text x="25" y="298" font-size="10.5" fill="#cbd5e1">• 2:3 ratio cannot be simplified</text>
    <text x="25" y="322" font-size="12" font-weight="bold" fill="#34d399">Final Formula: Al₂O₃</text>
  </g>

  <!-- Right Example: Magnesium Hydroxide (Bracket Rule) -->
  <g transform="translate(425, 65)">
    <rect x="0" y="0" width="340" height="355" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="0" y="0" width="340" height="30" rx="10" fill="#7e22ce"/>
    <text x="170" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">EXAMPLE 2: RADICAL BRACKET RULE</text>

    <!-- Top Symbols & Valencies -->
    <rect x="35" y="45" width="105" height="70" rx="8" fill="#1e293b" stroke="#334155"/>
    <text x="87" y="70" font-size="16" font-weight="bold" fill="#f59e0b">Valency: 2</text>
    <text x="87" y="100" font-size="28" font-weight="bold" fill="#ffffff">Mg</text>

    <rect x="195" y="45" width="115" height="70" rx="8" fill="#1e293b" stroke="#334155"/>
    <text x="252" y="70" font-size="16" font-weight="bold" fill="#f59e0b">Valency: 1</text>
    <text x="252" y="100" font-size="28" font-weight="bold" fill="#ffffff">(OH)</text>

    <!-- Crossover Arrows -->
    <path d="M 115,65 Q 170,110 240,140" fill="none" stroke="#a855f7" stroke-width="3"/>
    <path d="M 220,65 Q 170,110 100,140" fill="none" stroke="#34d399" stroke-width="3"/>

    <!-- Bottom Swapped Subscripts with Brackets -->
    <rect x="35" y="145" width="275" height="75" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="85" y="192" font-size="34" font-weight="bold" fill="#ffffff">Mg</text>
    <text x="165" y="192" font-size="34" font-weight="bold" fill="#facc15">(OH)</text>
    <text x="245" y="205" font-size="28" font-weight="bold" fill="#a855f7">2</text>

    <!-- Explanation Box -->
    <rect x="15" y="235" width="310" height="105" rx="6" fill="#1e293b"/>
    <text x="25" y="258" font-size="10.5" fill="#f87171" font-weight="bold">Mandatory Bracket Rule:</text>
    <text x="25" y="278" font-size="10" fill="#cbd5e1">• Radical (OH) receives subscript 2</text>
    <text x="25" y="298" font-size="10" fill="#cbd5e1">• Must enclose in brackets: <tspan fill="#facc15" font-weight="bold">Mg(OH)₂</tspan></text>
    <text x="25" y="322" font-size="11" font-weight="bold" fill="#ef4444">NOT MgOH₂ (MgOH₂ is chemically invalid!)</text>
  </g>
</svg>
""")

# SVG 5: Submicroscopic Atom Accounting in 2Mg + O2 -> 2MgO (Lesson 5, Page 3)
SVG_BALANCING_ACCOUNTING = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="10" y="10" width="780" height="430" rx="14" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">Submicroscopic Atom Accounting: 2Mg(s) + O₂(g) → 2MgO(s)</text>

  <!-- Left: Reactants (2 Mg atoms + 1 O2 molecule) -->
  <g transform="translate(35, 65)">
    <rect x="0" y="0" width="320" height="355" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="0" y="0" width="320" height="30" rx="10" fill="#0284c7"/>
    <text x="160" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">REACTANTS: 2Mg(s) + O₂(g)</text>

    <!-- 2 Mg separate atoms -->
    <circle cx="70" cy="110" r="28" fill="#64748b" stroke="#94a3b8" stroke-width="2"/>
    <text x="70" y="115" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Mg</text>

    <circle cx="140" cy="110" r="28" fill="#64748b" stroke="#94a3b8" stroke-width="2"/>
    <text x="140" y="115" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Mg</text>

    <text x="195" y="115" font-size="24" font-weight="bold" fill="#ffffff" text-anchor="middle">+</text>

    <!-- 1 O2 bonded diatomic molecule -->
    <circle cx="240" cy="110" r="22" fill="#ef4444" stroke="#f87171" stroke-width="1.5"/>
    <text x="240" y="114" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">O</text>
    <circle cx="275" cy="110" r="22" fill="#ef4444" stroke="#f87171" stroke-width="1.5"/>
    <text x="275" y="114" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">O</text>

    <!-- Atom Tally -->
    <rect x="15" y="180" width="290" height="160" rx="6" fill="#1e293b"/>
    <text x="25" y="205" font-size="12" font-weight="bold" fill="#38bdf8">Reactant Atom Tally:</text>
    <text x="25" y="235" font-size="11" fill="#cbd5e1">• Magnesium atoms: <tspan fill="#ffffff" font-weight="bold">2</tspan> (from 2Mg)</text>
    <text x="25" y="260" font-size="11" fill="#cbd5e1">• Oxygen atoms: <tspan fill="#f87171" font-weight="bold">2</tspan> (from 1 O₂)</text>
    <text x="25" y="300" font-size="10" fill="#94a3b8">Total Reactant Mass = Mass of Products</text>
    <text x="25" y="320" font-size="9" fill="#34d399">Law of Conservation of Mass</text>
  </g>

  <!-- Middle Arrow -->
  <g transform="translate(370, 160)">
    <line x1="0" y1="0" x2="45" y2="0" stroke="#38bdf8" stroke-width="4"/>
    <polygon points="45,-8 60,0 45,8" fill="#38bdf8"/>
    <text x="30" y="-15" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Yields</text>
  </g>

  <!-- Right: Products (2 MgO units) -->
  <g transform="translate(445, 65)">
    <rect x="0" y="0" width="320" height="355" rx="10" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect x="0" y="0" width="320" height="30" rx="10" fill="#059669"/>
    <text x="160" y="20" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">PRODUCTS: 2MgO(s)</text>

    <!-- Unit 1: MgO -->
    <circle cx="80" cy="110" r="28" fill="#64748b" stroke="#94a3b8" stroke-width="2"/>
    <text x="80" y="115" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Mg²⁺</text>
    <circle cx="125" cy="110" r="22" fill="#ef4444" stroke="#f87171" stroke-width="1.5"/>
    <text x="125" y="114" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">O²⁻</text>

    <!-- Unit 2: MgO -->
    <circle cx="200" cy="110" r="28" fill="#64748b" stroke="#94a3b8" stroke-width="2"/>
    <text x="200" y="115" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Mg²⁺</text>
    <circle cx="245" cy="110" r="22" fill="#ef4444" stroke="#f87171" stroke-width="1.5"/>
    <text x="245" y="114" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">O²⁻</text>

    <!-- Atom Tally -->
    <rect x="15" y="180" width="290" height="160" rx="6" fill="#1e293b"/>
    <text x="25" y="205" font-size="12" font-weight="bold" fill="#34d399">Product Atom Tally:</text>
    <text x="25" y="235" font-size="11" fill="#cbd5e1">• Magnesium atoms: <tspan fill="#ffffff" font-weight="bold">2</tspan> (from 2MgO)</text>
    <text x="25" y="260" font-size="11" fill="#cbd5e1">• Oxygen atoms: <tspan fill="#f87171" font-weight="bold">2</tspan> (from 2MgO)</text>
    <text x="25" y="300" font-size="11" font-weight="bold" fill="#34d399">✓ 100% Balanced Equation!</text>
    <text x="25" y="322" font-size="9" fill="#cbd5e1">2 Mg on left = 2 Mg on right; 2 O on left = 2 O on right</text>
  </g>
</svg>
""")

# SVG 6: 4-Step Chemistry Reasoning Pathway (Lesson 6, Page 2)
SVG_REASONING_CHAIN = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="10" y="10" width="780" height="430" rx="14" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 4-Step Chemistry Reasoning Pathway: Element to Balanced Equation</text>

  <!-- Step 1 Box -->
  <g transform="translate(25, 70)">
    <rect x="0" y="0" width="170" height="340" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="170" height="28" rx="8" fill="#0284c7"/>
    <text x="85" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STEP 1: CONFIGURATION</text>

    <rect x="10" y="40" width="150" height="285" rx="6" fill="#1e293b"/>
    <text x="20" y="65" font-size="11" font-weight="bold" fill="#38bdf8">Find Valence e⁻:</text>
    <text x="20" y="90" font-size="10" fill="#cbd5e1">• Aluminium (Z=13):</text>
    <text x="20" y="108" font-size="10.5" font-weight="bold" fill="#ffffff">1s² 2s² 2p⁶ 3s² 3p¹</text>
    <text x="20" y="128" font-size="10" fill="#facc15">→ 3 valence electrons</text>

    <text x="20" y="165" font-size="10" fill="#cbd5e1">• Oxygen (Z=8):</text>
    <text x="20" y="183" font-size="10.5" font-weight="bold" fill="#ffffff">1s² 2s² 2p⁴</text>
    <text x="20" y="203" font-size="10" fill="#facc15">→ 6 valence electrons</text>

    <text x="20" y="250" font-size="9" fill="#94a3b8">Periodic coordinates determine outer orbital filling</text>
  </g>

  <!-- Step 2 Box -->
  <g transform="translate(215, 70)">
    <rect x="0" y="0" width="170" height="340" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect x="0" y="0" width="170" height="28" rx="8" fill="#b45309"/>
    <text x="85" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STEP 2: STABLE IONS</text>

    <rect x="10" y="40" width="150" height="285" rx="6" fill="#1e293b"/>
    <text x="20" y="65" font-size="11" font-weight="bold" fill="#f59e0b">Octet Pathway:</text>
    <text x="20" y="90" font-size="10" fill="#cbd5e1">• Aluminium loses 3 e⁻:</text>
    <text x="20" y="115" font-size="16" font-weight="bold" fill="#ffffff">Al³⁺</text>
    <text x="20" y="135" font-size="10" fill="#cbd5e1">(Valency = <tspan fill="#facc15" font-weight="bold">3</tspan>)</text>

    <text x="20" y="170" font-size="10" fill="#cbd5e1">• Oxygen gains 2 e⁻:</text>
    <text x="20" y="195" font-size="16" font-weight="bold" fill="#ffffff">O²⁻</text>
    <text x="20" y="215" font-size="10" fill="#cbd5e1">(Valency = <tspan fill="#facc15" font-weight="bold">2</tspan>)</text>

    <text x="20" y="250" font-size="9" fill="#94a3b8">Attaining nearest noble gas neon octet</text>
  </g>

  <!-- Step 3 Box -->
  <g transform="translate(405, 70)">
    <rect x="0" y="0" width="170" height="340" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <rect x="0" y="0" width="170" height="28" rx="8" fill="#7e22ce"/>
    <text x="85" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STEP 3: FORMULA</text>

    <rect x="10" y="40" width="150" height="285" rx="6" fill="#1e293b"/>
    <text x="20" y="65" font-size="11" font-weight="bold" fill="#a855f7">Valency Crossover:</text>
    <text x="20" y="95" font-size="14" font-weight="bold" fill="#facc15">Al³  O²</text>
    <text x="20" y="125" font-size="11" fill="#cbd5e1">Swap numbers:</text>
    <text x="20" y="160" font-size="20" font-weight="bold" fill="#ffffff">Al₂O₃</text>
    <text x="20" y="190" font-size="11" fill="#34d399">Aluminium Oxide</text>
    <text x="20" y="215" font-size="10" fill="#cbd5e1">Net Charge = 0</text>

    <text x="20" y="250" font-size="9" fill="#94a3b8">2(+3) + 3(-2) = 0 Electroneutrality</text>
  </g>

  <!-- Step 4 Box -->
  <g transform="translate(595, 70)">
    <rect x="0" y="0" width="180" height="340" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
    <rect x="0" y="0" width="180" height="28" rx="8" fill="#059669"/>
    <text x="90" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">STEP 4: EQUATION</text>

    <rect x="10" y="40" width="160" height="285" rx="6" fill="#1e293b"/>
    <text x="18" y="65" font-size="11" font-weight="bold" fill="#34d399">Stoichiometry:</text>
    <text x="18" y="90" font-size="9.5" fill="#cbd5e1">• Reactants: Al(s), O₂(g)</text>
    <text x="18" y="110" font-size="9.5" fill="#cbd5e1">• Product: Al₂O₃(s)</text>

    <text x="18" y="145" font-size="10" fill="#facc15">Balanced Equation:</text>
    <text x="18" y="175" font-size="11" font-weight="bold" fill="#ffffff">4Al(s) + 3O₂(g)</text>
    <text x="18" y="195" font-size="11" font-weight="bold" fill="#ffffff">↓</text>
    <text x="18" y="215" font-size="12" font-weight="bold" fill="#34d399">2Al₂O₃(s)</text>

    <text x="18" y="255" font-size="9" fill="#94a3b8">4 Al and 6 O on both sides</text>
  </g>
</svg>
""")

# =============================================================================
# VERIFIED WIKIMEDIA ASSETS FOR TOPIC 3
# =============================================================================

TOPIC3_ASSETS = [
    # Lesson 1 (1288)
    {
        "unit_order": 1,
        "page_number": 1,
        "block_type": "suggested_image",
        "asset_type": "image",
        "title": "The Chemist's Map: The Periodic Table",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Periodic_table_large.svg",
        "caption": "Standard modern IUPAC Periodic Table of Elements organizing chemical elements by atomic number and electron configuration.",
        "metadata": {
            "author": "2012rc",
            "licensing": "CC BY-SA 3.0",
            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Periodic_table_large.svg"
        }
    },
    {
        "unit_order": 1,
        "page_number": 3,
        "block_type": "suggested_diagram",
        "asset_type": "diagram",
        "title": "Periodic Table Coordinates: Groups vs. Periods",
        "svg_content": SVG_GROUPS_PERIODS,
        "metadata": {
            "svg_content": SVG_GROUPS_PERIODS,
            "theme": "dark"
        }
    },

    # Lesson 2 (1289)
    {
        "unit_order": 2,
        "page_number": 1,
        "block_type": "suggested_image",
        "asset_type": "image",
        "title": "Chemical Families in the Laboratory",
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Glowing_noble_gases.jpg",
        "caption": "Miniature glass ampoules of glowing noble gases (Helium, Neon, Argon, Krypton, Xenon) under high-voltage excitation.",
        "metadata": {
            "author": "Alchemist-hp",
            "licensing": "CC BY-SA 3.0",
            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Glowing_noble_gases.jpg"
        }
    },
    {
        "unit_order": 2,
        "page_number": 3,
        "block_type": "suggested_diagram",
        "asset_type": "diagram",
        "title": "Chemical Families & Electron Stability Pathways",
        "svg_content": SVG_FAMILIES_STABILITY,
        "metadata": {
            "svg_content": SVG_FAMILIES_STABILITY,
            "theme": "dark"
        }
    },

    # Lesson 3 (1290)
    {
        "unit_order": 3,
        "page_number": 1,
        "block_type": "suggested_image",
        "asset_type": "image",
        "title": "The Transformation from Atoms to Ions",
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/cd/Graduated_chemical_glassware_%28Alessandri_1895.2%29.png",
        "caption": "Precision scientific glassware used in measuring electrolyte ion solutions and titrations.",
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
        "title": "Electron Transfer: Sodium Cation & Chloride Anion Formation",
        "svg_content": SVG_ELECTRON_TRANSFER,
        "metadata": {
            "svg_content": SVG_ELECTRON_TRANSFER,
            "theme": "dark"
        }
    },

    # Lesson 4 (1291)
    {
        "unit_order": 4,
        "page_number": 1,
        "block_type": "suggested_image",
        "asset_type": "image",
        "title": "Chemical Recipes: Formulating Compounds",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/70/Copper_sulfate.jpg",
        "caption": "Vibrant blue crystalline copper(II) sulfate pentahydrate crystals illustrating exact stoichiometric chemical formulae.",
        "metadata": {
            "author": "Stephanb",
            "licensing": "CC BY-SA 3.0",
            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Copper_sulfate.jpg"
        }
    },
    {
        "unit_order": 4,
        "page_number": 3,
        "block_type": "suggested_diagram",
        "asset_type": "diagram",
        "title": "The Valency Swap Method and Bracket Rule",
        "svg_content": SVG_VALENCY_SWAP,
        "metadata": {
            "svg_content": SVG_VALENCY_SWAP,
            "theme": "dark"
        }
    },

    # Lesson 5 (1292)
    {
        "unit_order": 5,
        "page_number": 1,
        "block_type": "suggested_image",
        "asset_type": "image",
        "title": "The Conservation of Mass in Chemical Reactions",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Modern_analytical_balance.jpg",
        "caption": "High-precision digital analytical balance verifying the Law of Conservation of Mass in chemical synthesis.",
        "metadata": {
            "author": "Soerfm",
            "licensing": "CC BY-SA 3.0",
            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Modern_analytical_balance.jpg"
        }
    },
    {
        "unit_order": 5,
        "page_number": 3,
        "block_type": "suggested_diagram",
        "asset_type": "diagram",
        "title": "Submicroscopic Atom Accounting: 2Mg + O₂ → 2MgO",
        "svg_content": SVG_BALANCING_ACCOUNTING,
        "metadata": {
            "svg_content": SVG_BALANCING_ACCOUNTING,
            "theme": "dark"
        }
    },

    # Lesson 6 (1293)
    {
        "unit_order": 6,
        "page_number": 1,
        "block_type": "suggested_image",
        "asset_type": "image",
        "title": "The Master Chemistry Reasoning Pathway",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/6f/A_group_of_scientists_working_in_a_laboratory_Esculab.jpg",
        "caption": "Chemical synthesis researchers designing reactions from fundamental periodic and electronic principles.",
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
        "title": "The 4-Step Chemistry Reasoning Pathway: Element to Balanced Equation",
        "svg_content": SVG_REASONING_CHAIN,
        "metadata": {
            "svg_content": SVG_REASONING_CHAIN,
            "theme": "dark"
        }
    }
]

def enrich_topic3():
    print("=" * 80)
    print("ENRICHING GRADE 10 CHEMISTRY — TOPIC 3: THE PERIODIC TABLE")
    print("=" * 80)

    topic = Topic.objects.get(subject__id=5, order=3)
    print(f"Target Topic: [{topic.id}] {topic.name}")

    for asset_def in TOPIC3_ASSETS:
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

    print("\nSUCCESS: Topic 3 Visual & Media Enrichment Completed!")

if __name__ == "__main__":
    enrich_topic3()
