"""
VLearn CBC Grade 10 Chemistry — Topic 1: Introduction to Chemistry
Visual Enrichment Engine (Vector SVGs, Verified Wikimedia Hooks & YouTube Integration)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Chemistry (ID: 5)
Topic: Introduction to Chemistry (Topic Order: 1)
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
# CUSTOM RESPONSIVE VECTOR SVGS FOR TOPIC 1: INTRODUCTION TO CHEMISTRY
# =============================================================================

# SVG 1: The Three Levels of Chemistry (Combustion of Charcoal) (Lesson 1, Page 2)
SVG_THREE_LEVELS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="10" y="10" width="780" height="430" rx="14" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Three Levels of Chemistry: Combustion of Charcoal</text>
  <text x="400" y="64" font-size="12" fill="#94a3b8" text-anchor="middle">Macroscopic Observation  ↔  Submicroscopic Particles  ↔  Symbolic Representation</text>

  <!-- Level 1: Macroscopic -->
  <g transform="translate(25, 85)">
    <rect x="0" y="0" width="235" height="330" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect x="0" y="0" width="235" height="36" rx="10" fill="#b45309"/>
    <text x="117" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">1. MACROSCOPIC LEVEL</text>
    <text x="117" y="55" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">What We See &amp; Feel</text>
    
    <!-- Drawing: Charcoal in Jiko -->
    <ellipse cx="117" cy="140" rx="75" ry="30" fill="#334155" stroke="#475569" stroke-width="2"/>
    <!-- Glowing Charcoal chunks -->
    <path d="M70,135 Q85,115 105,130 Q120,110 145,125 Q165,115 160,140 Q130,155 70,135 Z" fill="#ef4444"/>
    <circle cx="95" cy="130" r="10" fill="#f97316"/>
    <circle cx="130" cy="128" r="12" fill="#fbbf24"/>
    <circle cx="115" cy="140" r="8" fill="#ef4444"/>
    <!-- Heat shimmer / flame -->
    <path d="M95,115 Q100,85 105,105 Q115,75 125,100 Q135,80 135,110" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3"/>
    
    <!-- Explanatory Bullets -->
    <text x="15" y="205" font-size="11" font-weight="bold" fill="#f8fafc">• Solid black charcoal burns</text>
    <text x="15" y="225" font-size="11" fill="#cbd5e1">• Glowing red/orange heat</text>
    <text x="15" y="245" font-size="11" fill="#cbd5e1">• Emits hot, invisible gas</text>
    <text x="15" y="265" font-size="11" fill="#cbd5e1">• Leaves grey ash residue</text>
    <rect x="15" y="285" width="205" height="30" rx="6" fill="#1e293b"/>
    <text x="117" y="305" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">Direct Sensory Evidence</text>
  </g>

  <!-- Level 2: Submicroscopic -->
  <g transform="translate(282, 85)">
    <rect x="0" y="0" width="235" height="330" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="235" height="36" rx="10" fill="#0284c7"/>
    <text x="117" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">2. SUBMICROSCOPIC LEVEL</text>
    <text x="117" y="55" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">What Particles Are Doing</text>

    <!-- Particle drawing -->
    <!-- Carbon atom -->
    <g transform="translate(30, 95)">
      <circle cx="25" cy="25" r="18" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
      <text x="25" y="30" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">C</text>
      <text x="25" y="58" font-size="9" fill="#94a3b8" text-anchor="middle">Carbon atom</text>
    </g>
    <text x="85" y="125" font-size="16" font-weight="bold" fill="#38bdf8">+</text>
    <!-- Oxygen molecule -->
    <g transform="translate(105, 95)">
      <circle cx="20" cy="25" r="14" fill="#ef4444" stroke="#f87171" stroke-width="1.5"/>
      <text x="20" y="29" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">O</text>
      <circle cx="42" cy="25" r="14" fill="#ef4444" stroke="#f87171" stroke-width="1.5"/>
      <text x="42" y="29" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">O</text>
      <text x="31" y="58" font-size="9" fill="#f87171" text-anchor="middle">O₂ molecule</text>
    </g>

    <!-- Reaction Arrow -->
    <path d="M117,165 L117,185" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>
    <text x="117" y="180" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">↓</text>

    <!-- CO2 molecule formed -->
    <g transform="translate(45, 185)">
      <circle cx="20" cy="25" r="13" fill="#ef4444" stroke="#f87171" stroke-width="1.5"/>
      <text x="20" y="29" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">O</text>
      <circle cx="45" cy="25" r="16" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
      <text x="45" y="30" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">C</text>
      <circle cx="70" cy="25" r="13" fill="#ef4444" stroke="#f87171" stroke-width="1.5"/>
      <text x="70" y="29" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">O</text>
      <text x="45" y="54" font-size="9" fill="#38bdf8" text-anchor="middle">CO₂ molecule (Linear)</text>
    </g>

    <!-- Bullets -->
    <text x="15" y="255" font-size="10" fill="#cbd5e1">• C atoms collide with O₂ molecules</text>
    <text x="15" y="272" font-size="10" fill="#cbd5e1">• Covalent bonds break &amp; form</text>
    <rect x="15" y="285" width="205" height="30" rx="6" fill="#1e293b"/>
    <text x="117" y="305" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Atomic Rearrangement</text>
  </g>

  <!-- Level 3: Symbolic -->
  <g transform="translate(540, 85)">
    <rect x="0" y="0" width="235" height="330" rx="10" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
    <rect x="0" y="0" width="235" height="36" rx="10" fill="#059669"/>
    <text x="117" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">3. SYMBOLIC LEVEL</text>
    <text x="117" y="55" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">Chemical Notation</text>

    <!-- Chemical equation display -->
    <rect x="12" y="80" width="211" height="75" rx="8" fill="#1e293b" stroke="#334155"/>
    <text x="117" y="115" font-size="14" font-weight="bold" fill="#34d399" text-anchor="middle">C(s) + O₂(g) → CO₂(g)</text>
    <text x="117" y="140" font-size="10" fill="#94a3b8" text-anchor="middle">ΔH = -393.5 kJ/mol (Exothermic)</text>

    <!-- Breakdown of symbols -->
    <text x="15" y="180" font-size="11" font-weight="bold" fill="#34d399">Equation Anatomy:</text>
    <text x="15" y="200" font-size="10" fill="#cbd5e1">• <tspan fill="#38bdf8" font-weight="bold">C, O</tspan> : Chemical symbols</text>
    <text x="15" y="220" font-size="10" fill="#cbd5e1">• <tspan fill="#f59e0b" font-weight="bold">(s), (g)</tspan> : State symbols (solid, gas)</text>
    <text x="15" y="240" font-size="10" fill="#cbd5e1">• <tspan fill="#34d399" font-weight="bold">→</tspan> : Yields / irreversible change</text>
    <text x="15" y="260" font-size="10" fill="#cbd5e1">• Stoichiometry: 1 mol : 1 mol : 1 mol</text>

    <rect x="15" y="285" width="205" height="30" rx="6" fill="#1e293b"/>
    <text x="117" y="305" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">Universal Chemistry Code</text>
  </g>
</svg>
""")

# SVG 2: Municipal Water Treatment Process (Lesson 3, Page 3)
SVG_WATER_TREATMENT = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="10" y="10" width="780" height="430" rx="14" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">Municipal Water Treatment: 6-Stage Chemical &amp; Physical Purification</text>
  
  <!-- Flow line -->
  <path d="M60,110 L740,110" stroke="#38bdf8" stroke-width="4" stroke-dasharray="6,6"/>

  <!-- Stage 1: Screening -->
  <g transform="translate(30, 75)">
    <rect x="0" y="0" width="105" height="150" rx="8" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
    <rect x="0" y="0" width="105" height="28" rx="8" fill="#475569"/>
    <text x="52" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">1. SCREENING</text>
    <line x1="20" y1="45" x2="20" y2="105" stroke="#94a3b8" stroke-width="2"/>
    <line x1="35" y1="45" x2="35" y2="105" stroke="#94a3b8" stroke-width="2"/>
    <line x1="50" y1="45" x2="50" y2="105" stroke="#94a3b8" stroke-width="2"/>
    <line x1="65" y1="45" x2="65" y2="105" stroke="#94a3b8" stroke-width="2"/>
    <line x1="80" y1="45" x2="80" y2="105" stroke="#94a3b8" stroke-width="2"/>
    <text x="52" y="125" font-size="9" fill="#cbd5e1" text-anchor="middle">Removes large</text>
    <text x="52" y="138" font-size="9" fill="#cbd5e1" text-anchor="middle">floating debris</text>
  </g>

  <!-- Stage 2: Coagulation -->
  <g transform="translate(155, 75)">
    <rect x="0" y="0" width="105" height="150" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="105" height="28" rx="8" fill="#0284c7"/>
    <text x="52" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">2. COAGULATION</text>
    <!-- Chemical dosing -->
    <rect x="25" y="40" width="55" height="22" rx="4" fill="#1e293b" stroke="#38bdf8"/>
    <text x="52" y="55" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">+ Alum</text>
    <circle cx="35" cy="85" r="5" fill="#f59e0b"/>
    <circle cx="50" cy="95" r="6" fill="#f59e0b"/>
    <circle cx="70" cy="88" r="7" fill="#f59e0b"/>
    <text x="52" y="125" font-size="9" fill="#cbd5e1" text-anchor="middle">Neutralizes clay</text>
    <text x="52" y="138" font-size="9" fill="#cbd5e1" text-anchor="middle">Forms flocs</text>
  </g>

  <!-- Stage 3: Sedimentation -->
  <g transform="translate(280, 75)">
    <rect x="0" y="0" width="105" height="150" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect x="0" y="0" width="105" height="28" rx="8" fill="#d97706"/>
    <text x="52" y="18" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">3. SEDIMENTATION</text>
    <!-- Settled sludge -->
    <rect x="5" y="95" width="95" height="18" fill="#78350f" rx="2"/>
    <text x="52" y="108" font-size="8" fill="#fde68a" text-anchor="middle">Settled Sludge</text>
    <text x="52" y="128" font-size="9" fill="#cbd5e1" text-anchor="middle">Gravity settling</text>
    <text x="52" y="140" font-size="9" fill="#cbd5e1" text-anchor="middle">of heavy flocs</text>
  </g>

  <!-- Stage 4: Filtration -->
  <g transform="translate(405, 75)">
    <rect x="0" y="0" width="105" height="150" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
    <rect x="0" y="0" width="105" height="28" rx="8" fill="#059669"/>
    <text x="52" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">4. FILTRATION</text>
    <!-- Sand and gravel layers -->
    <rect x="10" y="45" width="85" height="18" fill="#fde047" opacity="0.6"/>
    <text x="52" y="58" font-size="8" fill="#000000" text-anchor="middle">Fine Sand</text>
    <rect x="10" y="65" width="85" height="18" fill="#64748b" opacity="0.8"/>
    <text x="52" y="78" font-size="8" fill="#ffffff" text-anchor="middle">Gravel</text>
    <text x="52" y="125" font-size="9" fill="#cbd5e1" text-anchor="middle">Traps microscopic</text>
    <text x="52" y="138" font-size="9" fill="#cbd5e1" text-anchor="middle">solid particles</text>
  </g>

  <!-- Stage 5: Chlorination -->
  <g transform="translate(530, 75)">
    <rect x="0" y="0" width="105" height="150" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="2"/>
    <rect x="0" y="0" width="105" height="28" rx="8" fill="#db2777"/>
    <text x="52" y="18" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">5. CHLORINATION</text>
    <rect x="25" y="40" width="55" height="22" rx="4" fill="#1e293b" stroke="#ec4899"/>
    <text x="52" y="55" font-size="9" font-weight="bold" fill="#ec4899" text-anchor="middle">+ Cl₂(g)</text>
    <circle cx="52" cy="85" r="10" fill="#f43f5e" opacity="0.4"/>
    <text x="52" y="89" font-size="10" fill="#ffffff" text-anchor="middle">✕</text>
    <text x="52" y="125" font-size="9" fill="#cbd5e1" text-anchor="middle">Kills pathogenic</text>
    <text x="52" y="138" font-size="9" fill="#cbd5e1" text-anchor="middle">bacteria/viruses</text>
  </g>

  <!-- Stage 6: Storage & Distribution -->
  <g transform="translate(655, 75)">
    <rect x="0" y="0" width="105" height="150" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <rect x="0" y="0" width="105" height="28" rx="8" fill="#7e22ce"/>
    <text x="52" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">6. SAFE TAP</text>
    <!-- Tap icon -->
    <path d="M40,50 L65,50 L65,70 L55,70 L55,60 L40,60 Z" fill="#38bdf8"/>
    <circle cx="52" cy="85" r="4" fill="#38bdf8"/>
    <circle cx="52" cy="98" r="3" fill="#38bdf8"/>
    <text x="52" y="125" font-size="9" fill="#cbd5e1" text-anchor="middle">Clean &amp; safe</text>
    <text x="52" y="138" font-size="9" fill="#cbd5e1" text-anchor="middle">potable water</text>
  </g>

  <!-- Summary Deck below -->
  <g transform="translate(30, 245)">
    <rect x="0" y="0" width="730" height="175" rx="10" fill="#0f172a" stroke="#334155"/>
    <text x="20" y="30" font-size="13" font-weight="bold" fill="#38bdf8">Key Chemical Principles in Water Treatment:</text>
    <text x="20" y="60" font-size="11" fill="#cbd5e1">• <tspan fill="#38bdf8" font-weight="bold">Coagulation Chemistry</tspan>: Alum (Al₂(SO₄)₃) dissociates in water releasing Al³⁺ cations that neutralize the negative zeta-potential on colloidal clay.</text>
    <text x="20" y="90" font-size="11" fill="#cbd5e1">• <tspan fill="#ec4899" font-weight="bold">Disinfection Reaction</tspan>: Cl₂(g) + H₂O(l) ⇌ HOCl(aq) + HCl(aq). Hypochlorous acid (HOCl) oxidizes bacterial cell walls and metabolic enzymes.</text>
    <text x="20" y="120" font-size="11" fill="#cbd5e1">• <tspan fill="#34d399" font-weight="bold">pH Stabilization</tspan>: Lime (Ca(OH)₂) or soda ash (Na₂CO₃) raises water pH to 7.0–8.5 to prevent pipe corrosion across the county distribution grid.</text>
    <text x="20" y="150" font-size="11" fill="#f59e0b">• <tspan fill="#f59e0b" font-weight="bold">Continuous Monitoring</tspan>: Residual chlorine levels are tested before distribution to guarantee sterile conditions all the way to household taps.</text>
  </g>
</svg>
""")

# SVG 3: Safe Medicine Decision Pathway (Lesson 4, Page 3)
SVG_SAFE_MEDICINE_PATHWAY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" style="background-color: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="10" y="10" width="780" height="430" rx="14" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="400" y="38" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 7-Step Safe Medicine Decision &amp; Usage Pathway</text>

  <!-- Step 1 -->
  <g transform="translate(30, 65)">
    <rect x="0" y="0" width="190" height="150" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="25" cy="25" r="14" fill="#0284c7"/>
    <text x="25" y="30" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1</text>
    <text x="50" y="28" font-size="12" font-weight="bold" fill="#38bdf8">Medical Exam</text>
    <text x="12" y="60" font-size="10" fill="#cbd5e1">• Visit a qualified doctor</text>
    <text x="12" y="80" font-size="10" fill="#cbd5e1">• Accurate clinical diagnosis</text>
    <text x="12" y="100" font-size="10" fill="#cbd5e1">• Never self-diagnose</text>
    <text x="12" y="125" font-size="9" fill="#f87171">Avoid guessing illnesses</text>
  </g>

  <!-- Arrow 1->2 -->
  <text x="232" y="145" font-size="20" font-weight="bold" fill="#38bdf8">→</text>

  <!-- Step 2 -->
  <g transform="translate(255, 65)">
    <rect x="0" y="0" width="190" height="150" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <circle cx="25" cy="25" r="14" fill="#7e22ce"/>
    <text x="25" y="30" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2</text>
    <text x="50" y="28" font-size="12" font-weight="bold" fill="#c084fc">Prescription</text>
    <text x="12" y="60" font-size="10" fill="#cbd5e1">• Receive written directive</text>
    <text x="12" y="80" font-size="10" fill="#cbd5e1">• Exact dosage &amp; intervals</text>
    <text x="12" y="100" font-size="10" fill="#cbd5e1">• Duration of treatment</text>
    <text x="12" y="125" font-size="9" fill="#f87171">Never share prescriptions</text>
  </g>

  <!-- Arrow 2->3 -->
  <text x="457" y="145" font-size="20" font-weight="bold" fill="#38bdf8">→</text>

  <!-- Step 3 -->
  <g transform="translate(480, 65)">
    <rect x="0" y="0" width="190" height="150" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <circle cx="25" cy="25" r="14" fill="#15803d"/>
    <text x="25" y="30" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3</text>
    <text x="50" y="28" font-size="12" font-weight="bold" fill="#4ade80">Licensed PPB</text>
    <text x="12" y="60" font-size="10" fill="#cbd5e1">• Buy at licensed pharmacy</text>
    <text x="12" y="80" font-size="10" fill="#cbd5e1">• Verify PPB registered</text>
    <text x="12" y="100" font-size="10" fill="#cbd5e1">• Qualified pharmacist</text>
    <text x="12" y="125" font-size="9" fill="#f87171">Reject street hawkers</text>
  </g>

  <!-- Row 2 -->
  <!-- Step 4 -->
  <g transform="translate(30, 240)">
    <rect x="0" y="0" width="165" height="170" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="22" cy="22" r="12" fill="#b45309"/>
    <text x="22" y="26" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4</text>
    <text x="42" y="26" font-size="11" font-weight="bold" fill="#fbbf24">Inspect Label</text>
    <text x="10" y="55" font-size="9.5" fill="#cbd5e1">• Check KEBS/PPB mark</text>
    <text x="10" y="75" font-size="9.5" fill="#cbd5e1">• Verify expiry date</text>
    <text x="10" y="95" font-size="9.5" fill="#cbd5e1">• Check intact seal</text>
    <text x="10" y="115" font-size="9.5" fill="#cbd5e1">• Read side effects</text>
  </g>

  <!-- Step 5 -->
  <g transform="translate(210, 240)">
    <rect x="0" y="0" width="165" height="170" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="2"/>
    <circle cx="22" cy="22" r="12" fill="#db2777"/>
    <text x="22" y="26" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">5</text>
    <text x="42" y="26" font-size="11" font-weight="bold" fill="#f472b6">Exact Dose</text>
    <text x="10" y="55" font-size="9.5" fill="#cbd5e1">• Take exact prescribed ml/mg</text>
    <text x="10" y="75" font-size="9.5" fill="#cbd5e1">• Respect intervals (e.g. 8h)</text>
    <text x="10" y="95" font-size="9.5" fill="#cbd5e1">• Never double missed dose</text>
    <text x="10" y="115" font-size="9.5" fill="#f87171">• Overdose causes toxicity</text>
  </g>

  <!-- Step 6 -->
  <g transform="translate(390, 240)">
    <rect x="0" y="0" width="165" height="170" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
    <circle cx="22" cy="22" r="12" fill="#0891b2"/>
    <text x="22" y="26" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">6</text>
    <text x="42" y="26" font-size="11" font-weight="bold" fill="#22d3ee">Finish Course</text>
    <text x="10" y="55" font-size="9.5" fill="#cbd5e1">• Complete full duration</text>
    <text x="10" y="75" font-size="9.5" fill="#cbd5e1">• Do NOT stop when better</text>
    <text x="10" y="95" font-size="9.5" fill="#cbd5e1">• Prevents superbug mutation</text>
    <text x="10" y="115" font-size="9.5" fill="#34d399">• Stops antimicrobial resistance</text>
  </g>

  <!-- Step 7 -->
  <g transform="translate(570, 240)">
    <rect x="0" y="0" width="195" height="170" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <circle cx="22" cy="22" r="12" fill="#059669"/>
    <text x="22" y="26" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">7</text>
    <text x="42" y="26" font-size="11" font-weight="bold" fill="#34d399">Safe Storage</text>
    <text x="10" y="55" font-size="9.5" fill="#cbd5e1">• Keep cool, dry &amp; dark</text>
    <text x="10" y="75" font-size="9.5" fill="#cbd5e1">• Out of reach of children</text>
    <text x="10" y="95" font-size="9.5" fill="#cbd5e1">• Keep in original container</text>
    <text x="10" y="115" font-size="9.5" fill="#cbd5e1">• Safely dispose expired pills</text>
  </g>
</svg>
""")

# =============================================================================
# VERIFIED WIKIMEDIA IMAGE HOOKS & ATTACHMENTS FOR TOPIC 1
# =============================================================================

TOPIC1_ASSETS = [
    # Lesson 1 (Lesson 1278): Meaning, Scope, and Language of Chemistry
    {
        "unit_order": 1,
        "page_number": 1,
        "block_type": "suggested_image",
        "asset_type": "image",
        "title": "Welcome to Chemistry: The Central Science",
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/cd/Graduated_chemical_glassware_%28Alessandri_1895.2%29.png",
        "caption": "Precision laboratory glassware used in chemical investigations to observe matter and its transformations.",
        "metadata": {
            "author": "Alessandri / valeg96",
            "licensing": "Public domain",
            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Graduated_chemical_glassware_(Alessandri_1895.2).png"
        }
    },
    {
        "unit_order": 1,
        "page_number": 2,
        "block_type": "suggested_diagram",
        "asset_type": "diagram",
        "title": "The Three Levels of Chemistry: Combustion of Charcoal",
        "svg_content": SVG_THREE_LEVELS,
        "metadata": {
            "svg_content": SVG_THREE_LEVELS,
            "theme": "dark"
        }
    },
    {
        "unit_order": 1,
        "page_number": 4,
        "block_type": "suggested_video",
        "asset_type": "youtube",
        "title": "Laboratory Demonstration: Comparing Physical and Chemical Changes",
        "url": "https://www.youtube.com/watch?v=4ZGULLWEy1c",
        "description": "Watch a laboratory demonstration comparing the reversible physical change of boiling water with the brilliant, irreversible chemical reaction of burning magnesium ribbon in air.",
        "metadata": {
            "youtube_id": "4ZGULLWEy1c"
        }
    },

    # Lesson 2 (Lesson 1279): Branches and Careers in Chemistry
    {
        "unit_order": 2,
        "page_number": 1,
        "block_type": "suggested_image",
        "asset_type": "image",
        "title": "Chemistry: The Central Science",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/6f/A_group_of_scientists_working_in_a_laboratory_Esculab.jpg",
        "caption": "Chemists working in a modern analytical laboratory, conducting precision titrations and diagnostic assays.",
        "metadata": {
            "author": "Esculab Lab",
            "licensing": "CC0",
            "commons_page_url": "https://commons.wikimedia.org/wiki/File:A_group_of_scientists_working_in_a_laboratory_Esculab.jpg"
        }
    },

    # Lesson 3 (Lesson 1280): Chemistry in Daily Life, Industry, and the Environment
    {
        "unit_order": 3,
        "page_number": 1,
        "block_type": "suggested_image",
        "asset_type": "image",
        "title": "Chemistry All Around Us",
        "url": "https://upload.wikimedia.org/wikipedia/commons/1/1c/Jardine_Water_Purification_Plant_2022.jpg",
        "caption": "Municipal water purification facility utilizing chemical coagulation, sand filtration, and chlorination.",
        "metadata": {
            "author": "Sea Cow",
            "licensing": "CC BY-SA 4.0",
            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Jardine_Water_Purification_Plant_2022.jpg"
        }
    },
    {
        "unit_order": 3,
        "page_number": 3,
        "block_type": "suggested_diagram",
        "asset_type": "diagram",
        "title": "Step-by-Step Municipal Water Purification Process",
        "svg_content": SVG_WATER_TREATMENT,
        "metadata": {
            "svg_content": SVG_WATER_TREATMENT,
            "theme": "dark"
        }
    },

    # Lesson 4 (Lesson 1281): Drugs, Substance Use, Consumer Rights, and Safe Learning
    {
        "unit_order": 4,
        "page_number": 1,
        "block_type": "suggested_image",
        "asset_type": "image",
        "title": "Responsible Medicine Use",
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Contraceptive_pills_1000pxw.jpg",
        "caption": "Prescription pharmaceuticals dispensed with exact dosage and regimen schedules to guarantee safe therapeutic outcomes.",
        "metadata": {
            "author": "Anka",
            "licensing": "CC BY 2.5 pl",
            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Contraceptive_pills_1000pxw.jpg"
        }
    },
    {
        "unit_order": 4,
        "page_number": 3,
        "block_type": "suggested_diagram",
        "asset_type": "diagram",
        "title": "The 7-Step Safe Medicine Decision Pathway",
        "svg_content": SVG_SAFE_MEDICINE_PATHWAY,
        "metadata": {
            "svg_content": SVG_SAFE_MEDICINE_PATHWAY,
            "theme": "dark"
        }
    },

    # Lesson 5 (Lesson 1282): Chemistry Communication and Inquiry Project
    {
        "unit_order": 5,
        "page_number": 1,
        "block_type": "suggested_image",
        "asset_type": "image",
        "title": "Communicating Science to Society",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/08/Bunsen_burner_flame_types.jpg",
        "caption": "Laboratory Bunsen burner flame types demonstrating empirical observation and evidence-based reporting in Chemistry.",
        "metadata": {
            "author": "Arthur Jan Fijałkowski",
            "licensing": "CC BY-SA 3.0",
            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Bunsen_burner_flame_types.jpg"
        }
    }
]

def enrich_topic1():
    print("=" * 80)
    print("ENRICHING GRADE 10 CHEMISTRY — TOPIC 1: INTRODUCTION TO CHEMISTRY")
    print("=" * 80)

    topic = Topic.objects.get(subject__id=5, order=1)
    print(f"Target Topic: [{topic.id}] {topic.name}")

    for asset_def in TOPIC1_ASSETS:
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

        # Resolve or create LessonAsset
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

        # Link asset to block
        block.assets.add(asset)

        # Update block content payload with resolved media properties
        content = block.content or {}
        if asset_type == "image":
            content["resolved_image_url"] = asset_def["url"]
            content["caption"] = asset_def.get("caption")
        elif asset_type == "diagram":
            content["svg_content"] = asset_def.get("svg_content")
            content["caption"] = asset_def.get("title")
        elif asset_type == "youtube":
            content["url"] = asset_def.get("url")
            content["description"] = asset_def.get("description")

        block.content = content
        block.save()

    print("\nSUCCESS: Topic 1 Visual & Media Enrichment Completed!")

if __name__ == "__main__":
    enrich_topic1()
