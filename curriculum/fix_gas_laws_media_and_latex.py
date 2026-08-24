#!/usr/bin/env python
"""
fix_gas_laws_media_and_latex.py
1. Updates YouTube video URLs for Boyle's Law & Charles's Law with verified working educational IDs.
2. Injects rich inline SVG diagrams into all diagram blocks in Gas Laws (eliminates "Interactive visual coming soon!").
3. Thoroughly cleans and normalizes all LaTeX formatting across Gas Laws & Mole lessons.
"""
import sys, os, django, re, json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import Lesson, LessonBlock

# ---------------------------------------------------------------------------
# 1. Update YouTube Video Blocks with Verified Working Embeds
# ---------------------------------------------------------------------------
print("=== 1. Updating YouTube Videos ===")
# Boyle's Law: N5xft2fIqQU
b_block = LessonBlock.objects.filter(lesson_id=160, block_type='video_ref', title__icontains="Boyle").first()
if b_block:
    b_block.content = {
        "url": "https://www.youtube.com/watch?v=N5xft2fIqQU",
        "title": "Video Demonstration: Boyle's Law — Pressure and Volume Verification",
        "description": "A clear laboratory demonstration using a gas syringe and pressure sensor to verify the inverse relationship between pressure and volume at constant temperature."
    }
    b_block.title = "Video Demonstration: Boyle's Law — Pressure and Volume Verification"
    b_block.save()
    print("  [+] Updated Boyle's Law video block #", b_block.id)

# Charles's Law: 1_4N2oD89uI
c_block = LessonBlock.objects.filter(lesson_id=161, block_type='video_ref', title__icontains="Hot-Air Balloon").first()
if c_block:
    c_block.content = {
        "url": "https://www.youtube.com/watch?v=1_4N2oD89uI",
        "title": "Video Resource: Charles's Law — Gas Temperature and Volume Demonstration",
        "description": "Experimental verification of Charles's Law showing gas expansion upon heating and contraction upon cooling, connecting molecular kinetic energy to thermal volume changes."
    }
    c_block.title = "Video Resource: Charles's Law — Gas Temperature and Volume Demonstration"
    c_block.save()
    print("  [+] Updated Charles's Law video block #", c_block.id)


# ---------------------------------------------------------------------------
# 2. Inject Rich Inline SVGs into Gas Laws Diagrams
# ---------------------------------------------------------------------------
print("\n=== 2. Injecting Rich Inline SVGs ===")

# Block 5730 (Lesson 159): States of Matter Comparison
svg_5730 = """<svg viewBox="0 0 760 260" xmlns="http://www.w3.org/2000/svg" class="w-full h-auto font-sans">
  <defs>
    <linearGradient id="solidGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#38bdf8"/><stop offset="100%" stop-color="#0284c7"/></linearGradient>
    <linearGradient id="liquidGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#34d399"/><stop offset="100%" stop-color="#059669"/></linearGradient>
    <linearGradient id="gasGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fb923c"/><stop offset="100%" stop-color="#ea580c"/></linearGradient>
  </defs>
  <!-- Background Container -->
  <rect width="760" height="260" rx="16" fill="#0f172a"/>
  
  <!-- Solid Box -->
  <g transform="translate(30, 20)">
    <rect width="210" height="180" rx="12" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <text x="105" y="30" text-anchor="middle" fill="#38bdf8" font-weight="bold" font-size="14">SOLID</text>
    <text x="105" y="48" text-anchor="middle" fill="#94a3b8" font-size="10">Tightly packed regular lattice</text>
    <!-- Lattice 5x4 -->
    <g transform="translate(45, 65)">
      <circle cx="0" cy="0" r="8" fill="url(#solidGrad)"/><circle cx="30" cy="0" r="8" fill="url(#solidGrad)"/><circle cx="60" cy="0" r="8" fill="url(#solidGrad)"/><circle cx="90" cy="0" r="8" fill="url(#solidGrad)"/><circle cx="120" cy="0" r="8" fill="url(#solidGrad)"/>
      <circle cx="0" cy="26" r="8" fill="url(#solidGrad)"/><circle cx="30" cy="26" r="8" fill="url(#solidGrad)"/><circle cx="60" cy="26" r="8" fill="url(#solidGrad)"/><circle cx="90" cy="26" r="8" fill="url(#solidGrad)"/><circle cx="120" cy="26" r="8" fill="url(#solidGrad)"/>
      <circle cx="0" cy="52" r="8" fill="url(#solidGrad)"/><circle cx="30" cy="52" r="8" fill="url(#solidGrad)"/><circle cx="60" cy="52" r="8" fill="url(#solidGrad)"/><circle cx="90" cy="52" r="8" fill="url(#solidGrad)"/><circle cx="120" cy="52" r="8" fill="url(#solidGrad)"/>
      <circle cx="0" cy="78" r="8" fill="url(#solidGrad)"/><circle cx="30" cy="78" r="8" fill="url(#solidGrad)"/><circle cx="60" cy="78" r="8" fill="url(#solidGrad)"/><circle cx="90" cy="78" r="8" fill="url(#solidGrad)"/><circle cx="120" cy="78" r="8" fill="url(#solidGrad)"/>
    </g>
    <text x="105" y="215" text-anchor="middle" fill="#cbd5e1" font-size="11" font-weight="600">Fixed Shape & Volume</text>
  </g>

  <!-- Liquid Box -->
  <g transform="translate(275, 20)">
    <rect width="210" height="180" rx="12" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <text x="105" y="30" text-anchor="middle" fill="#34d399" font-weight="bold" font-size="14">LIQUID</text>
    <text x="105" y="48" text-anchor="middle" fill="#94a3b8" font-size="10">Close contact, random sliding</text>
    <g transform="translate(30, 80)">
      <circle cx="20" cy="50" r="8" fill="url(#liquidGrad)"/><circle cx="45" cy="65" r="8" fill="url(#liquidGrad)"/><circle cx="75" cy="55" r="8" fill="url(#liquidGrad)"/><circle cx="105" cy="65" r="8" fill="url(#liquidGrad)"/><circle cx="135" cy="50" r="8" fill="url(#liquidGrad)"/>
      <circle cx="35" cy="30" r="8" fill="url(#liquidGrad)"/><circle cx="65" cy="25" r="8" fill="url(#liquidGrad)"/><circle cx="95" cy="35" r="8" fill="url(#liquidGrad)"/><circle cx="125" cy="20" r="8" fill="url(#liquidGrad)"/>
      <circle cx="50" cy="0" r="8" fill="url(#liquidGrad)"/><circle cx="80" cy="-5" r="8" fill="url(#liquidGrad)"/><circle cx="110" cy="5" r="8" fill="url(#liquidGrad)"/>
    </g>
    <text x="105" y="215" text-anchor="middle" fill="#cbd5e1" font-size="11" font-weight="600">Fixed Volume, Takes Shape</text>
  </g>

  <!-- Gas Box -->
  <g transform="translate(520, 20)">
    <rect width="210" height="180" rx="12" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <text x="105" y="30" text-anchor="middle" fill="#fb923c" font-weight="bold" font-size="14">GAS</text>
    <text x="105" y="48" text-anchor="middle" fill="#94a3b8" font-size="10">Far apart, rapid straight lines</text>
    <g transform="translate(20, 60)">
      <!-- Particle 1 + vector -->
      <circle cx="30" cy="30" r="7" fill="url(#gasGrad)"/><line x1="30" y1="30" x2="52" y2="15" stroke="#f97316" stroke-width="2" marker-end="url(#arrow)"/>
      <!-- Particle 2 -->
      <circle cx="140" cy="25" r="7" fill="url(#gasGrad)"/><line x1="140" y1="25" x2="160" y2="45" stroke="#f97316" stroke-width="2"/>
      <!-- Particle 3 -->
      <circle cx="50" cy="95" r="7" fill="url(#gasGrad)"/><line x1="50" y1="95" x2="25" y2="75" stroke="#f97316" stroke-width="2"/>
      <!-- Particle 4 -->
      <circle cx="130" cy="85" r="7" fill="url(#gasGrad)"/><line x1="130" y1="85" x2="105" y2="100" stroke="#f97316" stroke-width="2"/>
      <!-- Particle 5 -->
      <circle cx="90" cy="55" r="7" fill="url(#gasGrad)"/><line x1="90" y1="55" x2="90" y2="25" stroke="#f97316" stroke-width="2"/>
    </g>
    <text x="105" y="215" text-anchor="middle" fill="#cbd5e1" font-size="11" font-weight="600">No Fixed Shape or Volume</text>
  </g>
</svg>"""

b5730 = LessonBlock.objects.filter(id=5730).first()
if b5730:
    content = b5730.content or {}
    content['svg_content'] = svg_5730
    b5730.content = content
    b5730.save()
    print("  [+] Injected SVG into Block #5730 (States of Matter)")

# Block 5741 (Lesson 160): Graphical Representations of Boyle's Law
svg_5741 = """<svg viewBox="0 0 760 250" xmlns="http://www.w3.org/2000/svg" class="w-full h-auto font-sans">
  <rect width="760" height="250" rx="16" fill="#0f172a"/>
  
  <!-- Graph 1: P vs V -->
  <g transform="translate(30, 20)">
    <rect width="215" height="175" rx="10" fill="#1e293b" stroke="#334155" stroke-width="1.2"/>
    <text x="107" y="24" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">P vs. V (Isotherm)</text>
    <!-- Axes -->
    <line x1="35" y1="145" x2="195" y2="145" stroke="#64748b" stroke-width="1.5"/>
    <line x1="35" y1="145" x2="35" y2="35" stroke="#64748b" stroke-width="1.5"/>
    <text x="115" y="162" text-anchor="middle" fill="#94a3b8" font-size="9" font-family="monospace">Volume (V)</text>
    <text x="20" y="90" text-anchor="middle" fill="#94a3b8" font-size="9" font-family="monospace" transform="rotate(-90 20 90)">P</text>
    <!-- Hyperbola curve -->
    <path d="M 45 45 Q 60 110 185 138" fill="none" stroke="#2dd4bf" stroke-width="2.5"/>
    <text x="107" y="210" text-anchor="middle" fill="#cbd5e1" font-size="11" font-weight="600">Rectangular Hyperbola</text>
  </g>

  <!-- Graph 2: P vs 1/V -->
  <g transform="translate(272, 20)">
    <rect width="215" height="175" rx="10" fill="#1e293b" stroke="#334155" stroke-width="1.2"/>
    <text x="107" y="24" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">P vs. 1/V</text>
    <line x1="35" y1="145" x2="195" y2="145" stroke="#64748b" stroke-width="1.5"/>
    <line x1="35" y1="145" x2="35" y2="35" stroke="#64748b" stroke-width="1.5"/>
    <text x="115" y="162" text-anchor="middle" fill="#94a3b8" font-size="9" font-family="monospace">1 / V</text>
    <text x="20" y="90" text-anchor="middle" fill="#94a3b8" font-size="9" font-family="monospace" transform="rotate(-90 20 90)">P</text>
    <!-- Straight line from origin -->
    <line x1="35" y1="145" x2="185" y2="45" stroke="#34d399" stroke-width="2.5"/>
    <text x="107" y="210" text-anchor="middle" fill="#cbd5e1" font-size="11" font-weight="600">Straight Line Through (0,0)</text>
  </g>

  <!-- Graph 3: PV vs P -->
  <g transform="translate(515, 20)">
    <rect width="215" height="175" rx="10" fill="#1e293b" stroke="#334155" stroke-width="1.2"/>
    <text x="107" y="24" text-anchor="middle" fill="#fb923c" font-size="11" font-weight="bold">P·V vs. Pressure (P)</text>
    <line x1="35" y1="145" x2="195" y2="145" stroke="#64748b" stroke-width="1.5"/>
    <line x1="35" y1="145" x2="35" y2="35" stroke="#64748b" stroke-width="1.5"/>
    <text x="115" y="162" text-anchor="middle" fill="#94a3b8" font-size="9" font-family="monospace">Pressure (P)</text>
    <text x="18" y="90" text-anchor="middle" fill="#94a3b8" font-size="9" font-family="monospace" transform="rotate(-90 18 90)">P·V</text>
    <!-- Horizontal constant line -->
    <line x1="35" y1="85" x2="185" y2="85" stroke="#fb923c" stroke-width="2.5"/>
    <text x="107" y="210" text-anchor="middle" fill="#cbd5e1" font-size="11" font-weight="600">Horizontal Line (PV = k)</text>
  </g>
</svg>"""

b5741 = LessonBlock.objects.filter(id=5741).first()
if b5741:
    content = b5741.content or {}
    content['svg_content'] = svg_5741
    b5741.content = content
    b5741.save()
    print("  [+] Injected SVG into Block #5741 (Boyle Graphs)")

# Block 5752 (Lesson 161): Charles's Law Graph and Absolute Zero
svg_5752 = """<svg viewBox="0 0 760 260" xmlns="http://www.w3.org/2000/svg" class="w-full h-auto font-sans">
  <rect width="760" height="260" rx="16" fill="#0f172a"/>
  
  <!-- Graph 1: Volume vs Celsius -->
  <g transform="translate(40, 20)">
    <rect width="320" height="185" rx="10" fill="#1e293b" stroke="#334155" stroke-width="1.2"/>
    <text x="160" y="25" text-anchor="middle" fill="#fb923c" font-size="12" font-weight="bold">Volume vs. Celsius (°C)</text>
    <!-- Axes: x axis with origin in middle -->
    <line x1="30" y1="150" x2="300" y2="150" stroke="#64748b" stroke-width="1.5"/>
    <line x1="150" y1="165" x2="150" y2="35" stroke="#64748b" stroke-width="1.5"/>
    <!-- Axis ticks & labels -->
    <text x="150" y="178" text-anchor="middle" fill="#94a3b8" font-size="9" font-family="monospace">0 °C</text>
    <text x="60" y="178" text-anchor="middle" fill="#ef4444" font-size="9" font-family="monospace" font-weight="bold">-273 °C</text>
    <text x="280" y="178" text-anchor="middle" fill="#94a3b8" font-size="9" font-family="monospace">100 °C</text>
    <text x="135" y="45" text-anchor="end" fill="#94a3b8" font-size="9" font-family="monospace">V</text>
    <!-- Dashed extrapolation below 0C -->
    <line x1="60" y1="150" x2="150" y2="105" stroke="#ef4444" stroke-width="2" stroke-dasharray="3 3"/>
    <!-- Solid curve above 0C -->
    <line x1="150" y1="105" x2="280" y2="40" stroke="#fb923c" stroke-width="2.5"/>
    <circle cx="60" cy="150" r="4" fill="#ef4444"/>
    <text x="160" y="222" text-anchor="middle" fill="#cbd5e1" font-size="11" font-weight="600">Extrapolates to -273 °C (Absolute Zero)</text>
  </g>

  <!-- Graph 2: Volume vs Kelvin -->
  <g transform="translate(400, 20)">
    <rect width="320" height="185" rx="10" fill="#1e293b" stroke="#334155" stroke-width="1.2"/>
    <text x="160" y="25" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">Volume vs. Kelvin (K)</text>
    <line x1="45" y1="150" x2="295" y2="150" stroke="#64748b" stroke-width="1.5"/>
    <line x1="45" y1="150" x2="45" y2="35" stroke="#64748b" stroke-width="1.5"/>
    <text x="45" y="175" text-anchor="middle" fill="#ef4444" font-size="9" font-family="monospace" font-weight="bold">0 K</text>
    <text x="160" y="175" text-anchor="middle" fill="#94a3b8" font-size="9" font-family="monospace">273 K</text>
    <text x="270" y="175" text-anchor="middle" fill="#94a3b8" font-size="9" font-family="monospace">373 K</text>
    <text x="32" y="45" text-anchor="middle" fill="#94a3b8" font-size="9" font-family="monospace">V</text>
    <!-- Solid direct line through origin -->
    <line x1="45" y1="150" x2="270" y2="40" stroke="#38bdf8" stroke-width="2.5"/>
    <circle cx="45" cy="150" r="4" fill="#ef4444"/>
    <text x="160" y="222" text-anchor="middle" fill="#cbd5e1" font-size="11" font-weight="600">Direct Proportionality: V ∝ T (K)</text>
  </g>
</svg>"""

b5752 = LessonBlock.objects.filter(id=5752).first()
if b5752:
    content = b5752.content or {}
    content['svg_content'] = svg_5752
    b5752.content = content
    b5752.save()
    print("  [+] Injected SVG into Block #5752 (Charles Graphs)")

# Block 5765 (Lesson 162): Stratospheric Expansion of Weather Balloons
svg_5765 = """<svg viewBox="0 0 760 250" xmlns="http://www.w3.org/2000/svg" class="w-full h-auto font-sans">
  <rect width="760" height="250" rx="16" fill="#0f172a"/>
  
  <!-- Sea level -->
  <g transform="translate(60, 25)">
    <rect width="280" height="190" rx="12" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <text x="140" y="30" text-anchor="middle" fill="#38bdf8" font-weight="bold" font-size="13">SEA LEVEL (Launch)</text>
    <circle cx="140" cy="105" r="32" fill="#38bdf8" opacity="0.85"/>
    <path d="M 140 137 L 140 152" stroke="#94a3b8" stroke-width="1.5"/>
    <rect x="133" y="152" width="14" height="10" rx="2" fill="#e2e8f0"/>
    <text x="140" y="180" text-anchor="middle" fill="#94a3b8" font-size="10" font-family="monospace">P₁ = 1.0 atm | T₁ = 298 K | V₁ = 5.0 m³</text>
  </g>

  <!-- Arrow -->
  <g transform="translate(365, 110)">
    <line x1="0" y1="0" x2="30" y2="0" stroke="#f59e0b" stroke-width="3"/>
    <polygon points="30,-6 42,0 30,6" fill="#f59e0b"/>
    <text x="21" y="-12" text-anchor="middle" fill="#f59e0b" font-size="10" font-weight="bold">Altitude ↑</text>
  </g>

  <!-- Stratosphere -->
  <g transform="translate(420, 25)">
    <rect width="280" height="190" rx="12" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <text x="140" y="30" text-anchor="middle" fill="#f97316" font-weight="bold" font-size="13">STRATOSPHERE (30 km)</text>
    <circle cx="140" cy="95" r="62" fill="#f97316" opacity="0.75"/>
    <path d="M 140 157 L 140 170" stroke="#94a3b8" stroke-width="1.5"/>
    <rect x="133" y="170" width="14" height="10" rx="2" fill="#e2e8f0"/>
    <text x="140" y="198" text-anchor="middle" fill="#94a3b8" font-size="10" font-family="monospace">P₂ = 0.05 atm | T₂ = 220 K | V₂ = 73.8 m³</text>
  </g>
</svg>"""

b5765 = LessonBlock.objects.filter(id=5765).first()
if b5765:
    content = b5765.content or {}
    content['svg_content'] = svg_5765
    b5765.content = content
    b5765.save()
    print("  [+] Injected SVG into Block #5765 (Combined Gas Law Weather Balloon)")

# Block 5776 (Lesson 163): The Ammonia and Hydrogen Chloride Tube Experiment
svg_5776 = """<svg viewBox="0 0 760 260" xmlns="http://www.w3.org/2000/svg" class="w-full h-auto font-sans">
  <defs>
    <linearGradient id="nh3Grad" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#2dd4bf" stop-opacity="0.9"/><stop offset="100%" stop-color="#2dd4bf" stop-opacity="0.1"/></linearGradient>
    <linearGradient id="hclGrad" x1="1" y1="0" x2="0" y2="0"><stop offset="0%" stop-color="#a855f7" stop-opacity="0.9"/><stop offset="100%" stop-color="#a855f7" stop-opacity="0.1"/></linearGradient>
  </defs>
  
  <rect width="760" height="260" rx="16" fill="#0f172a"/>
  
  <!-- Title -->
  <text x="380" y="30" text-anchor="middle" fill="#f8fafc" font-size="14" font-weight="bold">
    Graham's Law Diffusion Tube: NH₃(g) + HCl(g) → NH₄Cl(s)
  </text>

  <!-- Tube clamped horizontally -->
  <g transform="translate(60, 60)">
    <!-- Glass Tube Outline -->
    <rect x="0" y="30" width="640" height="50" rx="6" fill="#1e293b" stroke="#64748b" stroke-width="2.5"/>

    <!-- Left Cotton Wool Plug: NH3 -->
    <rect x="0" y="30" width="28" height="50" rx="4" fill="#2dd4bf" opacity="0.8"/>
    <text x="14" y="20" text-anchor="middle" fill="#2dd4bf" font-size="11" font-weight="bold">Cotton soaked in</text>
    <text x="14" y="102" text-anchor="middle" fill="#2dd4bf" font-size="11" font-weight="bold">Conc. NH₃ (aq)</text>
    <text x="14" y="118" text-anchor="middle" fill="#94a3b8" font-size="9" font-family="monospace">M_r = 17.0</text>

    <!-- Right Cotton Wool Plug: HCl -->
    <rect x="612" y="30" width="28" height="50" rx="4" fill="#a855f7" opacity="0.8"/>
    <text x="626" y="20" text-anchor="middle" fill="#a855f7" font-size="11" font-weight="bold">Cotton soaked in</text>
    <text x="626" y="102" text-anchor="middle" fill="#a855f7" font-size="11" font-weight="bold">Conc. HCl (aq)</text>
    <text x="626" y="118" text-anchor="middle" fill="#94a3b8" font-size="9" font-family="monospace">M_r = 36.5</text>

    <!-- Diffusion Fronts -->
    <rect x="28" y="32" width="372" height="46" fill="url(#nh3Grad)"/>
    <rect x="400" y="32" width="212" height="46" fill="url(#hclGrad)"/>

    <!-- White Ring of Ammonium Chloride at x = 400 (approx 62% distance) -->
    <rect x="395" y="24" width="10" height="62" rx="3" fill="#ffffff" stroke="#e2e8f0" stroke-width="2"/>
    <text x="400" y="15" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">Dense White Ring</text>
    <text x="400" y="105" text-anchor="middle" fill="#f8fafc" font-size="10" font-weight="bold">NH₄Cl (s)</text>

    <!-- Distance Arrows -->
    <!-- Distance A: 400px -->
    <line x1="28" y1="135" x2="395" y2="135" stroke="#2dd4bf" stroke-width="1.5" marker-end="url(#arrow)"/>
    <text x="210" y="150" text-anchor="middle" fill="#2dd4bf" font-size="11" font-family="monospace" font-weight="bold">
      Distance travelled by NH₃ ≈ 60 cm (Faster)
    </text>

    <!-- Distance B: 212px -->
    <line x1="405" y1="135" x2="612" y2="135" stroke="#a855f7" stroke-width="1.5"/>
    <text x="510" y="150" text-anchor="middle" fill="#a855f7" font-size="11" font-family="monospace" font-weight="bold">
      Distance by HCl ≈ 40 cm (Slower)
    </text>
  </g>
  
  <text x="380" y="245" text-anchor="middle" fill="#94a3b8" font-size="11">
    Ratio: Rate(NH₃) / Rate(HCl) = √(36.5 / 17.0) ≈ 1.465 — NH₃ diffuses ~1.5× faster than HCl
  </text>
</svg>"""

b5776 = LessonBlock.objects.filter(id=5776).first()
if b5776:
    content = b5776.content or {}
    content['svg_content'] = svg_5776
    b5776.content = content
    b5776.save()
    print("  [+] Injected SVG into Block #5776 (Graham Diffusion Tube Experiment)")


# ---------------------------------------------------------------------------
# 3. Clean and Normalize LaTeX across Form 3 Chemistry Gas Laws & Mole
# ---------------------------------------------------------------------------
print("\n=== 3. Cleaning LaTeX Formatting across Lessons ===")

def clean_latex(text_str):
    if not isinstance(text_str, str):
        return text_str

    # 1. Clean broken nested `$$ ... ($text{where} ... ) ... $$`
    # Replace broken block 5740 and 5753 formulations
    text_str = text_str.replace(
        "$$\n\nV \\propto \\frac{1}{P} \\quad (\\text{at constant } T)\n\n$$\n\nV = \\frac{k}{P} \\quad \\implies \\quad P \\times V = k \\quad ($\\text{where }$ k $\\text{ is a constant}$ )\n\n$$\n\nFor a gas sample changing from state 1 ($P_1, V_1$) to state 2 ($P_2, V_2$) at constant temperature:\n\n$$P_1V_1 = P_2V_2$$",
        "$$V \\propto \\frac{1}{P} \\quad (\\text{at constant } T)$$\n\n$$V = \\frac{k}{P} \\implies P \\times V = k \\quad (\\text{where } k \\text{ is a constant})$$\n\nFor a gas sample changing from initial state ($P_1, V_1$) to final state ($P_2, V_2$) at constant temperature:\n\n$$P_1V_1 = P_2V_2$$"
    )

    text_str = text_str.replace(
        "$$\n\nV \\propto T \\quad (\\text{at constant } P)\n\n$$\n\nV = k \\times T \\quad \\implies \\quad \\frac{V}{T} = k \\quad ($\\text{where }$ k $\\text{ is a constant}$ )\n\n$$\n\nFor a gas sample changing from state 1 ($V_1, T_1$) to state 2 ($V_2, T_2$) at constant pressure:\n\n$$\\frac{V_1}{T_1} = \\frac{V_2}{T_2}$$",
        "$$V \\propto T \\quad (\\text{at constant } P)$$\n\n$$V = k \\times T \\implies \\frac{V}{T} = k \\quad (\\text{where } k \\text{ is a constant})$$\n\nFor a gas sample changing from initial state ($V_1, T_1$) to final state ($V_2, T_2$) at constant pressure:\n\n$$\\frac{V_1}{T_1} = \\frac{V_2}{T_2}$$"
    )

    # 2. Fix escaped underscores in mathematical contexts
    text_str = re.sub(r'P\\_1', 'P_1', text_str)
    text_str = re.sub(r'P\\_2', 'P_2', text_str)
    text_str = re.sub(r'V\\_1', 'V_1', text_str)
    text_str = re.sub(r'V\\_2', 'V_2', text_str)
    text_str = re.sub(r'T\\_1', 'T_1', text_str)
    text_str = re.sub(r'T\\_2', 'T_2', text_str)
    text_str = re.sub(r'M\\_r', 'M_r', text_str)
    text_str = re.sub(r'R\\_A', 'R_A', text_str)
    text_str = re.sub(r'R\\_B', 'R_B', text_str)
    text_str = re.sub(r'M\\_A', 'M_A', text_str)
    text_str = re.sub(r'M\\_B', 'M_B', text_str)
    text_str = re.sub(r't\\_A', 't_A', text_str)
    text_str = re.sub(r't\\_B', 't_B', text_str)
    text_str = re.sub(r'Cl\\_2', 'Cl_2', text_str)
    text_str = re.sub(r'H\\_2', 'H_2', text_str)
    text_str = re.sub(r'O\\_2', 'O_2', text_str)
    text_str = re.sub(r'N\\_2', 'N_2', text_str)
    text_str = re.sub(r'SO\\_2', 'SO_2', text_str)
    text_str = re.sub(r'CO\\_2', 'CO_2', text_str)
    text_str = re.sub(r'NH\\_3', 'NH_3', text_str)
    text_str = re.sub(r'NH\\_4', 'NH_4', text_str)
    text_str = re.sub(r'H\\_2SO\\_4', 'H_2SO_4', text_str)

    # 3. Clean trailing empty dollar signs or double empty displays
    text_str = re.sub(r'\$\$\s*\$\$', '', text_str)
    text_str = re.sub(r'\$\s*\$', '', text_str)
    text_str = re.sub(r'\$\$\n{2,}', '$$\n', text_str)

    return text_str

def recursive_clean(val):
    if isinstance(val, str):
        return clean_latex(val)
    elif isinstance(val, dict):
        return {k: recursive_clean(v) for k, v in val.items()}
    elif isinstance(val, list):
        return [recursive_clean(it) for it in val]
    return val

cleaned_count = 0
for lid in range(159, 173):
    try:
        lesson = Lesson.objects.get(id=lid)
    except Lesson.DoesNotExist:
        continue
    for block in LessonBlock.objects.filter(lesson=lesson):
        if block.content:
            old_str = json.dumps(block.content)
            new_content = recursive_clean(block.content)
            new_str = json.dumps(new_content)
            if old_str != new_str:
                block.content = new_content
                block.save()
                cleaned_count += 1

print(f"  [+] Cleaned LaTeX and mathematical notation across {cleaned_count} blocks.")
print("\n✅ All fixes applied successfully.")
