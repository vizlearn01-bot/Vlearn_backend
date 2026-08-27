"""
VLearn CBC Grade 10 Computer Science — Topic 1: Evolution of Computers
Production Ingestion & Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Computer Science
Topic: Evolution of Computers (Topic Order: 1)

Decomposed into 2 Learning Units & 2 Published Lessons:
  1. Evolution and Development of Computers (Lesson 1: Early Computing Devices and Origins of Computation)
  2. Generations of Electronic Computers (Lesson 2: Generations and Development of Electronic Computers)
"""

import os
import sys
import re
import django
from django.db import transaction

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

def clean_text(text: str) -> str:
    """Removes bracket citations and normalizes unicode bullets into standard markdown list items."""
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    text = re.sub(r'^([^\n\-\*\d\>#][^\n]*)\n(- |\* )', r'\1\n\n\2', text, flags=re.MULTILINE)
    return text.strip()

def clean_dict(data):
    """Recursively cleans all strings in dictionary/list data structures."""
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, dict):
        return {k: clean_dict(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_dict(item) for item in data]
    return data

def sanitize_svg(svg: str) -> str:
    svg = re.sub(r'<\?xml.*?\?>', '', svg)
    svg = re.sub(r'<!DOCTYPE.*?>', '', svg)
    return svg.strip()

# =====================================================================
# HIGH PRECISION VECTOR SVGS FOR TOPIC 1
# =====================================================================

SVG_EARLY_DEVICES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="48" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Evolution of Early Computing Devices: From Manual to Programmable</text>
  <text x="480" y="72" font-size="12" fill="#94a3b8" text-anchor="middle">Major historical milestones leading to the modern digital computer architecture</text>

  <!-- Row 1: Manual & Analog Tools -->
  <!-- Abacus -->
  <rect x="40" y="95" width="200" height="175" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
  <rect x="50" y="105" width="180" height="24" rx="5" fill="#0284c7"/>
  <text x="140" y="122" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Abacus (~2400 BC)</text>
  <text x="50" y="145" font-size="10" font-weight="bold" fill="#38bdf8">• Mechanism:</text>
  <text x="50" y="160" font-size="9.5" fill="#e2e8f0">Physical sliding beads on parallel rods (Place values: 1s, 10s, 100s).</text>
  <text x="50" y="195" font-size="10" font-weight="bold" fill="#f59e0b">• Core Contribution:</text>
  <text x="50" y="210" font-size="9.5" fill="#e2e8f0">First physical representation of abstract positional arithmetic.</text>

  <!-- Napier's Bones -->
  <rect x="260" y="95" width="200" height="175" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
  <rect x="270" y="105" width="180" height="24" rx="5" fill="#059669"/>
  <text x="360" y="122" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Napier's Bones (1617)</text>
  <text x="270" y="145" font-size="10" font-weight="bold" fill="#34d399">• Mechanism:</text>
  <text x="270" y="160" font-size="9.5" fill="#e2e8f0">Numbered rods with carved lattice multiplication tables.</text>
  <text x="270" y="195" font-size="10" font-weight="bold" fill="#f59e0b">• Core Contribution:</text>
  <text x="270" y="210" font-size="9.5" fill="#e2e8f0">Pioneered pre-calculated lookup tables to reduce mult. to addition.</text>

  <!-- Slide Rule -->
  <rect x="480" y="95" width="200" height="175" rx="10" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.5"/>
  <rect x="490" y="105" width="180" height="24" rx="5" fill="#7c3aed"/>
  <text x="580" y="122" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Slide Rule (1620)</text>
  <text x="490" y="145" font-size="10" font-weight="bold" fill="#a78bfa">• Mechanism:</text>
  <text x="490" y="160" font-size="9.5" fill="#e2e8f0">Continuous logarithmic scales sliding against each other.</text>
  <text x="490" y="195" font-size="10" font-weight="bold" fill="#f59e0b">• Core Contribution:</text>
  <text x="490" y="210" font-size="9.5" fill="#e2e8f0">Analog computing: continuous physical lengths represent values.</text>

  <!-- Pascaline -->
  <rect x="700" y="95" width="220" height="175" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
  <rect x="710" y="105" width="200" height="24" rx="5" fill="#d97706"/>
  <text x="810" y="122" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Pascaline (1642)</text>
  <text x="710" y="145" font-size="10" font-weight="bold" fill="#fbbf24">• Mechanism:</text>
  <text x="710" y="160" font-size="9.5" fill="#e2e8f0">Interlocking toothed brass gears and dials.</text>
  <text x="710" y="195" font-size="10" font-weight="bold" fill="#38bdf8">• Core Contribution:</text>
  <text x="710" y="210" font-size="9.5" fill="#e2e8f0">Mechanical Carry Mechanism: rotation from 9 to 0 advances next dial.</text>

  <!-- Row 2: Programmability & Modern Architecture -->
  <!-- Jacquard Loom -->
  <rect x="150" y="295" width="300" height="180" rx="10" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
  <rect x="160" y="305" width="280" height="24" rx="5" fill="#db2777"/>
  <text x="300" y="322" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Jacquard Loom (1804) — Programmed Control</text>
  <text x="165" y="348" font-size="10" font-weight="bold" fill="#f472b6">• Punched Card Innovation:</text>
  <text x="165" y="365" font-size="9.5" fill="#e2e8f0">Stiff cards with punched holes directed warp threads to weave intricate patterns.</text>
  <text x="165" y="405" font-size="10" font-weight="bold" fill="#34d399">• Modern Significance:</text>
  <text x="165" y="422" font-size="9.5" fill="#e2e8f0">First storage of binary instructions (hole = 1, no hole = 0) on external media.</text>

  <!-- Babbage Analytical Engine -->
  <rect x="490" y="295" width="430" height="180" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <rect x="500" y="305" width="410" height="24" rx="5" fill="#0284c7"/>
  <text x="705" y="322" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Babbage's Analytical Engine (1837) &amp; Ada Lovelace</text>
  <text x="505" y="348" font-size="10" font-weight="bold" fill="#38bdf8">• 4-Part Computer Architecture:</text>
  <text x="505" y="365" font-size="9.5" fill="#e2e8f0">1. The Store (Memory)  2. The Mill (CPU/ALU)  3. Input (Cards)  4. Output (Printers)</text>
  <text x="505" y="405" font-size="10" font-weight="bold" fill="#fbbf24">• Ada Lovelace (First Programmer):</text>
  <text x="505" y="422" font-size="9.5" fill="#e2e8f0">Authored algorithm to calculate Bernoulli numbers; realized machines could process symbols.</text>
</svg>
""")

SVG_BABBAGE_ENGINE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Charles Babbage's 4-Part Analytical Engine Architecture (1837)</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">The Victorian mechanical blueprint that established the fundamental structure of all modern digital computers</text>

  <!-- Box 1: Input (Punched Cards) -->
  <g transform="translate(50, 110)">
    <rect width="180" height="220" rx="10" fill="#0f172a" stroke="#ec4899" stroke-width="2"/>
    <rect width="180" height="30" rx="8" fill="#db2777"/>
    <text x="90" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. INPUT UNIT</text>
    <text x="15" y="55" font-size="10.5" font-weight="bold" fill="#f472b6">• Operation Cards:</text>
    <text x="15" y="72" font-size="9.5" fill="#cbd5e1">Encoded instructions (+, -, *, /)</text>
    <text x="15" y="105" font-size="10.5" font-weight="bold" fill="#f472b6">• Variable Cards:</text>
    <text x="15" y="122" font-size="9.5" fill="#cbd5e1">Pointed to memory column addresses</text>
    <text x="15" y="155" font-size="10.5" font-weight="bold" fill="#f472b6">• Number Cards:</text>
    <text x="15" y="172" font-size="9.5" fill="#cbd5e1">Supplied constant numeric values</text>
    <rect x="15" y="190" width="150" height="20" rx="4" fill="#1e293b"/>
    <text x="90" y="204" font-size="9" fill="#e2e8f0" text-anchor="middle">Modern: Keyboard / Storage</text>
  </g>

  <!-- Box 2: The Store (Memory) -->
  <g transform="translate(280, 110)">
    <rect width="200" height="220" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="2"/>
    <rect width="200" height="30" rx="8" fill="#0284c7"/>
    <text x="100" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. THE STORE (Memory)</text>
    <text x="15" y="55" font-size="10.5" font-weight="bold" fill="#38bdf8">• Physical Storage:</text>
    <text x="15" y="72" font-size="9.5" fill="#cbd5e1">1,000 vertical brass column axes, each holding 50 toothed gear wheels</text>
    <text x="15" y="115" font-size="10.5" font-weight="bold" fill="#38bdf8">• Total Capacity:</text>
    <text x="15" y="132" font-size="9.5" fill="#cbd5e1">1,000 numbers of 50 decimal digits each (~20.7 KB equivalent)</text>
    <rect x="15" y="190" width="170" height="20" rx="4" fill="#1e293b"/>
    <text x="100" y="204" font-size="9" fill="#e2e8f0" text-anchor="middle">Modern: RAM / Cache Memory</text>
  </g>

  <!-- Box 3: The Mill (CPU / ALU) -->
  <g transform="translate(530, 110)">
    <rect width="200" height="220" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <rect width="200" height="30" rx="8" fill="#059669"/>
    <text x="100" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. THE MILL (CPU/ALU)</text>
    <text x="15" y="55" font-size="10.5" font-weight="bold" fill="#34d399">• Processing Engine:</text>
    <text x="15" y="72" font-size="9.5" fill="#cbd5e1">Massive barrel of rotating gears and mechanical ratchets</text>
    <text x="15" y="115" font-size="10.5" font-weight="bold" fill="#34d399">• Capabilities:</text>
    <text x="15" y="132" font-size="9.5" fill="#cbd5e1">Arithmetic (+, -, *, /) with conditional branching (decision-making)</text>
    <rect x="15" y="190" width="170" height="20" rx="4" fill="#1e293b"/>
    <text x="100" y="204" font-size="9" fill="#e2e8f0" text-anchor="middle">Modern: Processor ALU / CU</text>
  </g>

  <!-- Box 4: Output Unit -->
  <g transform="translate(775, 110)">
    <rect width="140" height="220" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect width="140" height="30" rx="8" fill="#d97706"/>
    <text x="70" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">4. OUTPUT</text>
    <text x="12" y="55" font-size="10" font-weight="bold" fill="#fbbf24">• Mechanical Printer:</text>
    <text x="12" y="72" font-size="9" fill="#cbd5e1">Inked typeface automatically stamped on paper</text>
    <text x="12" y="115" font-size="10" font-weight="bold" fill="#fbbf24">• Card Puncher:</text>
    <text x="12" y="132" font-size="9" fill="#cbd5e1">Punched output cards for later reuse</text>
    <rect x="10" y="190" width="120" height="20" rx="4" fill="#1e293b"/>
    <text x="70" y="204" font-size="8.5" fill="#e2e8f0" text-anchor="middle">Modern: Monitor/Printer</text>
  </g>

  <!-- Bus Interconnects (Bottom Panel) -->
  <g transform="translate(50, 360)">
    <rect width="865" height="120" rx="10" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.5"/>
    <text x="432.5" y="25" font-size="12" font-weight="bold" fill="#c084fc" text-anchor="middle">Ada Lovelace's Vision: The World's First Computer Algorithm (1842)</text>
    <text x="30" y="52" font-size="10.5" fill="#e2e8f0">• <tspan fill="#38bdf8" font-weight="bold">Universal Symbolic Processing:</tspan> Ada recognized the Analytical Engine could process musical notes, letters, or images if they were represented mathematically.</text>
    <text x="30" y="75" font-size="10.5" fill="#e2e8f0">• <tspan fill="#34d399" font-weight="bold">First Algorithmic Program:</tspan> Documented a rigorous step-by-step instruction set to compute Bernoulli numbers using loops and memory variables.</text>
    <text x="30" y="98" font-size="10.5" fill="#e2e8f0">• <tspan fill="#fbbf24" font-weight="bold">Distinction from Hardware:</tspan> She established the clear conceptual boundary between the <tspan fill="#f59e0b">Physical Engine (Hardware)</tspan> and <tspan fill="#38bdf8">Stored Instructions (Software)</tspan>.</text>
  </g>
</svg>
""")

SVG_FIVE_GENERATIONS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Five Generations of Electronic Computers</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Technological breakthroughs, primary components, programming languages, and hardware characteristics</text>

  <!-- 1st Gen -->
  <g transform="translate(40, 85)">
    <rect width="165" height="390" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="165" height="28" rx="8" fill="#dc2626"/>
    <text x="82.5" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1st Gen (1940s-50s)</text>
    <text x="10" y="48" font-size="10" font-weight="bold" fill="#f87171">Core Technology:</text>
    <text x="10" y="65" font-size="9.5" fill="#e2e8f0">Vacuum Tubes (Glass thermionic valves)</text>
    <text x="10" y="105" font-size="10" font-weight="bold" fill="#f87171">Characteristics:</text>
    <text x="10" y="122" font-size="9" fill="#cbd5e1">• Room-sized (27 tons)<br/>• 150 kW power draw<br/>• Massive heat output<br/>• Low reliability (burnouts)</text>
    <text x="10" y="210" font-size="10" font-weight="bold" fill="#f87171">Language:</text>
    <text x="10" y="227" font-size="9" fill="#cbd5e1">Machine Code (1s &amp; 0s), Rewiring patch cables</text>
    <text x="10" y="280" font-size="10" font-weight="bold" fill="#f87171">Examples:</text>
    <text x="10" y="297" font-size="9.5" fill="#e2e8f0">ENIAC, UNIVAC I, EDVAC</text>
  </g>

  <!-- 2nd Gen -->
  <g transform="translate(220, 85)">
    <rect width="165" height="390" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="165" height="28" rx="8" fill="#d97706"/>
    <text x="82.5" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2nd Gen (1950s-60s)</text>
    <text x="10" y="48" font-size="10" font-weight="bold" fill="#fbbf24">Core Technology:</text>
    <text x="10" y="65" font-size="9.5" fill="#e2e8f0">Discrete Transistors (Solid-state switches)</text>
    <text x="10" y="105" font-size="10" font-weight="bold" fill="#fbbf24">Characteristics:</text>
    <text x="10" y="122" font-size="9" fill="#cbd5e1">• 100x smaller footprint<br/>• Low power draw<br/>• Greatly reduced heat<br/>• High physical reliability</text>
    <text x="10" y="210" font-size="10" font-weight="bold" fill="#fbbf24">Language:</text>
    <text x="10" y="227" font-size="9" fill="#cbd5e1">Assembly Language (Mnemonics), Early FORTRAN</text>
    <text x="10" y="280" font-size="10" font-weight="bold" fill="#fbbf24">Examples:</text>
    <text x="10" y="297" font-size="9.5" fill="#e2e8f0">IBM 1401, PDP-1, IBM 7090</text>
  </g>

  <!-- 3rd Gen -->
  <g transform="translate(400, 85)">
    <rect width="165" height="390" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="165" height="28" rx="8" fill="#059669"/>
    <text x="82.5" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">3rd Gen (1960s-70s)</text>
    <text x="10" y="48" font-size="10" font-weight="bold" fill="#34d399">Core Technology:</text>
    <text x="10" y="65" font-size="9.5" fill="#e2e8f0">Integrated Circuits (SSI/MSI silicon chips)</text>
    <text x="10" y="105" font-size="10" font-weight="bold" fill="#34d399">Characteristics:</text>
    <text x="10" y="122" font-size="9" fill="#cbd5e1">• 100s of transistors/chip<br/>• Keyboards &amp; monitors<br/>• Minicomputers born<br/>• Multi-programming OS</text>
    <text x="10" y="210" font-size="10" font-weight="bold" fill="#34d399">Language:</text>
    <text x="10" y="227" font-size="9" fill="#cbd5e1">High-Level (BASIC, COBOL, Pascal, C)</text>
    <text x="10" y="280" font-size="10" font-weight="bold" fill="#34d399">Examples:</text>
    <text x="10" y="297" font-size="9.5" fill="#e2e8f0">IBM System/360, DEC PDP-8</text>
  </g>

  <!-- 4th Gen -->
  <g transform="translate(580, 85)">
    <rect width="165" height="390" rx="8" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="165" height="28" rx="8" fill="#0284c7"/>
    <text x="82.5" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">4th Gen (1970s-Now)</text>
    <text x="10" y="48" font-size="10" font-weight="bold" fill="#38bdf8">Core Technology:</text>
    <text x="10" y="65" font-size="9.5" fill="#e2e8f0">Microprocessors (VLSI / ULSI CPU chips)</text>
    <text x="10" y="105" font-size="10" font-weight="bold" fill="#38bdf8">Characteristics:</text>
    <text x="10" y="122" font-size="9" fill="#cbd5e1">• Millions of transistors<br/>• Personal Computers (PC)<br/>• Laptops &amp; Smartphones<br/>• Internet &amp; GUI era</text>
    <text x="10" y="210" font-size="10" font-weight="bold" fill="#38bdf8">Language:</text>
    <text x="10" y="227" font-size="9" fill="#cbd5e1">Python, Java, C++, JavaScript, Modern IDEs</text>
    <text x="10" y="280" font-size="10" font-weight="bold" fill="#38bdf8">Examples:</text>
    <text x="10" y="297" font-size="9.5" fill="#e2e8f0">Apple Mac, Intel Core, AMD, ARM chips</text>
  </g>

  <!-- 5th Gen -->
  <g transform="translate(760, 85)">
    <rect width="160" height="390" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="160" height="28" rx="8" fill="#9333ea"/>
    <text x="80" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">5th Gen (Present+)</text>
    <text x="10" y="48" font-size="10" font-weight="bold" fill="#c084fc">Core Technology:</text>
    <text x="10" y="65" font-size="9.5" fill="#e2e8f0">Artificial Intelligence &amp; Quantum Circuits</text>
    <text x="10" y="105" font-size="10" font-weight="bold" fill="#c084fc">Characteristics:</text>
    <text x="10" y="122" font-size="9" fill="#cbd5e1">• Massively parallel cores<br/>• Quantum qubits (0 &amp; 1)<br/>• Neural processing units<br/>• Voice &amp; Vision AI</text>
    <text x="10" y="210" font-size="10" font-weight="bold" fill="#c084fc">Language:</text>
    <text x="10" y="227" font-size="9" fill="#cbd5e1">Natural Language, Neural Prompting, Qiskit</text>
    <text x="10" y="280" font-size="10" font-weight="bold" fill="#c084fc">Examples:</text>
    <text x="10" y="297" font-size="9.5" fill="#e2e8f0">AI Supercomputers, Google Sycamore, NPU</text>
  </g>
</svg>
""")

SVG_TRANSISTOR_SCALING = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Electronic Switching Evolution &amp; Moore's Law Trajectory</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">From macroscopic thermionic vacuum tubes to 3-nanometer silicon transistor gates</text>

  <!-- 4 Step Miniaturization Evolution -->
  <!-- 1. Vacuum Tube -->
  <g transform="translate(45, 95)">
    <rect width="200" height="230" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="200" height="26" rx="6" fill="#dc2626"/>
    <text x="100" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Vacuum Tube (~1945)</text>
    <circle cx="100" cy="85" r="30" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <line x1="100" y1="65" x2="100" y2="105" stroke="#fbbf24" stroke-width="2"/>
    <text x="100" y="90" font-size="8" fill="#fbbf24" text-anchor="middle">Glowing Filament</text>
    <text x="15" y="140" font-size="10" font-weight="bold" fill="#f87171">Physical Scale: ~10 cm</text>
    <text x="15" y="160" font-size="9" fill="#cbd5e1">• High voltage (~200V)</text>
    <text x="15" y="178" font-size="9" fill="#cbd5e1">• High heat &amp; power draw</text>
    <text x="15" y="196" font-size="9" fill="#cbd5e1">• Frequent filament burnouts</text>
  </g>

  <!-- 2. Discrete Transistor -->
  <g transform="translate(265, 95)">
    <rect width="200" height="230" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="200" height="26" rx="6" fill="#d97706"/>
    <text x="100" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Transistor (~1955)</text>
    <rect x="75" y="65" width="50" height="40" rx="4" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <line x1="85" y1="105" x2="85" y2="120" stroke="#94a3b8" stroke-width="2"/>
    <line x1="100" y1="105" x2="100" y2="120" stroke="#94a3b8" stroke-width="2"/>
    <line x1="115" y1="105" x2="115" y2="120" stroke="#94a3b8" stroke-width="2"/>
    <text x="15" y="140" font-size="10" font-weight="bold" fill="#fbbf24">Physical Scale: ~1 cm</text>
    <text x="15" y="160" font-size="9" fill="#cbd5e1">• Solid-state germanium/silicon</text>
    <text x="15" y="178" font-size="9" fill="#cbd5e1">• 1/100th power consumption</text>
    <text x="15" y="196" font-size="9" fill="#cbd5e1">• Zero filament failure</text>
  </g>

  <!-- 3. Integrated Circuit -->
  <g transform="translate(485, 95)">
    <rect width="200" height="230" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="200" height="26" rx="6" fill="#059669"/>
    <text x="100" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Integrated Circuit (1965)</text>
    <rect x="65" y="65" width="70" height="40" rx="3" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <circle cx="85" cy="85" r="5" fill="#34d399"/>
    <circle cx="115" cy="85" r="5" fill="#34d399"/>
    <text x="15" y="140" font-size="10" font-weight="bold" fill="#34d399">Physical Scale: ~5 mm</text>
    <text x="15" y="160" font-size="9" fill="#cbd5e1">• Hundreds of components</text>
    <text x="15" y="178" font-size="9" fill="#cbd5e1">• Printed on single silicon wafer</text>
    <text x="15" y="196" font-size="9" fill="#cbd5e1">• Born in Texas Instruments/Fairchild</text>
  </g>

  <!-- 4. Modern SoC Microprocessor -->
  <g transform="translate(705, 95)">
    <rect width="210" height="230" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="210" height="26" rx="6" fill="#0284c7"/>
    <text x="105" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4. Modern SoC / NPU (2020s)</text>
    <rect x="70" y="60" width="70" height="50" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="105" y="88" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">10B+ Gates</text>
    <text x="15" y="140" font-size="10" font-weight="bold" fill="#38bdf8">Physical Scale: 3 Nanometers</text>
    <text x="15" y="160" font-size="9" fill="#cbd5e1">• Billions of 3D FinFET gates</text>
    <text x="15" y="178" font-size="9" fill="#cbd5e1">• Sub-1-volt power efficiency</text>
    <text x="15" y="196" font-size="9" fill="#cbd5e1">• AI acceleration &amp; GPU cores</text>
  </g>

  <!-- Bottom: Moore's Law Trend Box -->
  <g transform="translate(45, 345)">
    <rect width="870" height="135" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="435" y="26" font-size="13" font-weight="bold" fill="#c084fc" text-anchor="middle">Gordon Moore's Law: The Exponential Economic Engine of Computing</text>
    <text x="30" y="55" font-size="10.5" fill="#e2e8f0">• <tspan fill="#38bdf8" font-weight="bold">Core Formulation (1965):</tspan> The number of transistors packed onto a microchip doubles roughly every 18 to 24 months, cutting component cost in half.</text>
    <text x="30" y="80" font-size="10.5" fill="#e2e8f0">• <tspan fill="#34d399" font-weight="bold">Practical Impact:</tspan> Enabled room-sized multi-ton supercomputers to shrink into handheld smartphones with millions of times more memory and speed.</text>
    <text x="30" y="105" font-size="10.5" fill="#e2e8f0">• <tspan fill="#fbbf24" font-weight="bold">Modern Frontier:</tspan> As silicon approaches single-atom limits (quantum tunneling), the industry transitions into 3D chip stacking, NPU neural accelerators, and quantum computing.</text>
  </g>
</svg>
""")

# =====================================================================
# LESSON DATA SPECIFICATION: TOPIC 1
# =====================================================================

def build_topic1_curriculum():
    return [
        # -------------------------------------------------------------
        # LESSON 1: Early Computing Devices and Origins of Computation
        # -------------------------------------------------------------
        {
            "unit_order": 1,
            "unit_name": "Evolution and Development of Computers",
            "unit_description": "Historical development of computation: manual calculating aids (abacus, Napier's bones, slide rule), mechanical calculators (Pascaline), programmable instruction storage (Jacquard loom), and Babbage's Analytical Engine.",
            "lesson_title": "Early Computing Devices and the Origins of Computation",
            "pages": [
                # Card 1: Hook & Learning Goals
                [
                    {
                        "type": "suggested_image",
                        "title": "The Classical Abacus: The Earliest Data Representation Tool",
                        "content": {
                            "title": "The Classical Abacus: The Earliest Data Representation Tool",
                            "caption": "A traditional Chinese Suanpan abacus. Parallel rods hold sliding wooden beads representing place-value units, proving physical objects could automate abstract arithmetic.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Abacus_60.jpg/800px-Abacus_60.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: The Foundations of Computation",
                        "content": {
                            "title": "What We Will Master in This Lesson",
                            "goals": [
                                "Define **early computing devices**, **mechanical calculators**, and **programmable instructions**.",
                                "Analyze the key physical mechanisms of the **Abacus**, **Napier's Bones**, **Slide Rule**, and **Pascaline**.",
                                "Explain how the **Jacquard Loom** pioneered binary instruction storage using punched cards.",
                                "Deconstruct Charles Babbage's **Analytical Engine** into its four core architectural components: **Store**, **Mill**, **Input**, and **Output**.",
                                "Trace calculation algorithms using pre-calculated mathematical tables."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Real-World Hook: Keeping Track of Data in an Ancient Market",
                        "content": {
                            "title": "The Human Need to Calculate",
                            "text": "Imagine you are a merchant in an ancient trading port. You manage 50 sheep, 80 sacks of grain, and 12 amphoras of olive oil. Every day, customers buy fractions of your stock, exchange goods for copper coins, and trade livestock.\n\n- How do you record and recalculate your inventory without human mental fatigue causing costly errors?\n- Early humans began with fingers, pebbles, and notch tallies on bone. But as global trade, sea navigation, and astronomy expanded, humans required **automated, physical mechanisms** to calculate reliably."
                        }
                    }
                ],
                # Card 2: Ancient and Medieval Calculating Aids
                [
                    {
                        "type": "concept_explanation",
                        "title": "Manual and Analog Calculating Aids",
                        "content": {
                            "title": "From Physical Beads to Logarithmic Scales",
                            "text": "Before electronic circuits existed, computational pioneers developed manual tools and analog instruments:\n\n### 1. The Abacus (~2400 BC)\n- **Physical Design**: A wooden frame with parallel rods holding movable beads. A horizontal beam divides the frame into upper and lower decks.\n- **Place-Value System**: Each rod represents a specific power of ten (units, tens, hundreds, thousands).\n- **Evolutionary Impact**: Proved that physical objects could represent numbers and that sliding them according to fixed rules could execute arithmetic operations.\n\n### 2. Napier's Bones (1617)\n- **Invented By**: John Napier (Scotland).\n- **Physical Design**: A set of numbered rods made of bone, wood, or ivory carved with pre-calculated multiplication tables.\n- **Evolutionary Impact**: Introduced the concept of **pre-calculated lookup tables**. By aligning rods, complex multiplication was converted into simple diagonal additions.\n\n### 3. The Slide Rule (1620)\n- **Invented By**: William Oughtred.\n- **Physical Design**: Two logarithmic rulers that slide past each other.\n- **Evolutionary Impact**: Introduced **analog computation**, where continuous physical distances represent numbers to perform rapid multiplication, division, and trigonometric calculations."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Early Computing Evolution Timeline & Contributions",
                        "content": {
                            "svg_content": SVG_EARLY_DEVICES,
                            "caption": "Timeline of early computing aids showing the transition from manual counting (Abacus) to pre-calculated lookup rods (Napier's Bones), analog sliding scales (Slide Rule), and gear-driven mechanics (Pascaline)."
                        }
                    }
                ],
                # Card 3: The Mechanical Era & Automated Carry
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Pascaline: Automating the Mathematical Carry",
                        "content": {
                            "title": "The First Mechanical Calculator (1642)",
                            "text": "Invented by 19-year-old French mathematician **Blaise Pascal** to assist his father (a tax collector), the **Pascaline** was the world's first working mechanical adding machine.\n\n### Mechanical Working Principle\n- The Pascaline contained a series of interlocking toothed brass gears and dials numbered 0 through 9.\n- The user rotated a dial using a stylus to enter a number.\n- **The Critical Breakthrough — The Carry Mechanism**: When the 'units' wheel completed a full rotation from $9$ back to $0$, an internal ratchet mechanism automatically advanced the adjacent 'tens' wheel by one notch. This mechanically solved the problem of carrying numbers in addition!"
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "How the Pascaline Executes an Automatic Carry",
                        "content": {
                            "title": "Mechanical Carry-Over Sequence",
                            "steps": [
                                "**Dial Input**: The user turns the 'Units' wheel to add a value (e.g. $7 + 5$).",
                                "**Rotation Threshold**: The units wheel advances past position $9$ towards $0$.",
                                "**Ratchet Engagement**: A weighted internal gravity lever (the *sautoir*) catches the pin of the adjacent 'Tens' gear.",
                                "**Carry Propagation**: As the units dial drops to $2$, the tens gear is mechanically pushed forward by exactly one notch, registering $12$ on the output display dials."
                            ]
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Blaise Pascal's Mechanical Calculator (Pascaline)",
                        "content": {
                            "title": "Blaise Pascal's Mechanical Calculator (Pascaline)",
                            "caption": "A surviving brass Pascaline calculator (1652). The external dials enter values while internal gear ratchets calculate sums and propagate carry-overs automatically.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Arts_et_Metiers_Pascaline_dsc03869.jpg/800px-Arts_et_Metiers_Pascaline_dsc03869.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    }
                ],
                # Card 4: Birth of Programmable Instructions
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Jacquard Loom: Storing Instructions on Physical Media",
                        "content": {
                            "title": "Weaving the Seeds of Computer Code (1804)",
                            "text": "In the early 19th century, French weaver **Joseph Marie Jacquard** revolutionized textile manufacturing with an invention that changed the future of computer science.\n\n### The Punched-Card Breakthrough\n- Jacquard attached a sequence of stiff cardboard cards punched with rows of holes to a mechanical weaving loom.\n- As the loom operated, mechanical sensing needles pressed against the card:\n  - **Hole Present**: The needle passed through the card, raising specific warp threads to weave colored silk into the pattern.\n  - **Solid Card (No Hole)**: The needle was blocked, keeping the thread lowered.\n- **The Computer Science Impact**: This was the theoretical birth of **programmable software**! It proved that physical patterns on external media could store binary commands ($1 = \\text{hole}, 0 = \\text{no hole}$) to control a machine's behavior automatically without altering its physical hardware."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Essential Terminology: Programmed Computing",
                        "content": {
                            "title": "Core Definitions in Early Computing",
                            "terms": [
                                {"term": "Early Computing Device", "definition": "Any manual or mechanical tool built to assist humans in performing numerical calculations before electronic computers."},
                                {"term": "Mechanical Calculator", "definition": "A calculating machine using physical gears, levers, and ratchets to perform arithmetic operations automatically."},
                                {"term": "Programmable Instruction", "definition": "A stored command or encoded pattern that a machine reads and executes autonomously to generate desired output."}
                            ]
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Jacquard Loom Punched Cards for Stored Pattern Control",
                        "content": {
                            "title": "Jacquard Loom Punched Cards for Stored Pattern Control",
                            "caption": "A chain of stiff punched paper cards used in Jacquard looms. The presence or absence of punched holes served as the earliest physical implementation of binary code instructions.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Jacquard.loom.cards.jpg/800px-Jacquard.loom.cards.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    }
                ],
                # Card 5: Charles Babbage and Ada Lovelace
                [
                    {
                        "type": "concept_explanation",
                        "title": "Charles Babbage: Father of the Digital Computer",
                        "content": {
                            "title": "The Difference Engine and Analytical Engine",
                            "text": "In the 1830s, English mathematician **Charles Babbage** designed two revolutionary mechanical machines:\n\n1. **The Difference Engine**: A massive, steam-powered mechanical calculator designed to automatically compute and print error-free polynomial mathematical tables for navigation and astronomy.\n2. **The Analytical Engine (1837)**: The theoretical blueprint of the modern digital computer. Babbage separated the machine into four distinct functional units:\n   - **The Store (Memory)**: Held 1,000 numbers of 50 digits each (intermediate values and variables).\n   - **The Mill (CPU / ALU)**: The central processing unit that performed additions, subtractions, multiplications, and divisions.\n   - **Input Mechanism**: Punched cards adapted directly from the Jacquard Loom.\n   - **Output Mechanism**: A mechanical printer and card punch.\n\n### Ada Lovelace: The First Computer Programmer\n**Augusta Ada Lovelace** recognized that Babbage's Analytical Engine was not limited to numbers. If symbols, letters, or musical notes could be represented mathematically, the engine could manipulate them. She wrote a complete step-by-step algorithm to calculate **Bernoulli numbers**, earning her historical recognition as the **world's first computer programmer**."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Babbage's Analytical Engine 4-Part Blueprint & Lovelace Algorithm",
                        "content": {
                            "svg_content": SVG_BABBAGE_ENGINE,
                            "caption": "Schematic blueprint of Charles Babbage's Analytical Engine showing The Store (Memory), The Mill (CPU), Input Cards, Printer Output, and Ada Lovelace's algorithmic foundation."
                        }
                    },
                    {
                        "type": "common_misconception",
                        "title": "Misconception: Babbage Built Modern Electronic Computers",
                        "content": {
                            "misconception": "Charles Babbage built operational electronic computers during the Victorian era.",
                            "correction": "Babbage's engines were purely mechanical (using gears, shafts, and steam power) rather than electronic. The precision metal machining of the 19th century was insufficient to complete the Analytical Engine during his lifetime, but his architectural design was 100% correct.",
                            "why_it_matters": "Distinguishes between architectural theoretical design (the 4-part model) and the physical electronic implementation that arrived in the 20th century."
                        }
                    }
                ],
                # Card 6: Guided Practice — Napier's Bones Trace
                [
                    {
                        "type": "worked_example",
                        "title": "Guided Practice: Tracing Lattice Multiplication on Napier's Bones",
                        "content": {
                            "title": "Multiplication Without Mental Math",
                            "problem": "Multiply $7 \\times 4$ using John Napier's pre-calculated lookup rod for the number 7.",
                            "steps": [
                                "**Examine the Rod for 7**: The single rod for 7 displays diagonal multiples: $7\\times1 = [0/7]$, $7\\times2 = [1/4]$, $7\\times3 = [2/1]$, $7\\times4 = [2/8]$, $7\\times5 = [3/5]$.",
                                "**Locate Row 4**: Slide the index pointer down to row 4 of the bone.",
                                "**Read the Split Block**: The diagonal box at row 4 reads $[2 / 8]$.",
                                "**Decompose Place Values**: The upper-left triangle holds the Tens digit ($2$), and the lower-right triangle holds the Ones digit ($8$).",
                                "**Final Value Calculation**: $\\text{Tens} \\times 10 + \\text{Ones} = (2 \\times 10) + 8 = 28$.",
                                "**Pedagogical Takeaway**: No multiplication occurred in the human brain; the user merely performed a coordinate lookup on a physical data storage rod!"
                            ]
                        }
                    },
                    {
                        "type": "prediction",
                        "title": "Prediction Check: Multi-Digit Addition",
                        "content": {
                            "text": "If you align the rod for $7$ and the rod for $3$ to calculate $73 \\times 4$, the row displays $[2/8]$ and $[1/2]$. When adding along the diagonal channels ($2$, $8+1$, $2$), what will the final product be?"
                        }
                    }
                ],
                # Card 7: Educational Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "The Analytical Engine & The Birth of Computer Science",
                        "content": {
                            "title": "How Babbage & Ada Lovelace Designed the First Computer",
                            "youtube_id": "5aP6_b1lAps",
                            "url": "https://www.youtube.com/watch?v=5aP6_b1lAps",
                            "description": "An engaging visual demonstration of Charles Babbage's mechanical gear engines, Jacquard punched card control, and Ada Lovelace's foundational algorithmic programming."
                        }
                    }
                ],
                # Card 8: Formative Knowledge Checks & Application
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 1: Ancient Calculating Devices",
                        "content": {
                            "question": "Which ancient calculating tool represents numerical values and place values using physical beads sliding on parallel rods?",
                            "options": [
                                "The Slide Rule",
                                "The Pascaline",
                                "The Abacus",
                                "The Difference Engine"
                            ],
                            "correct": "C",
                            "explanation": "The Abacus (dating back to ~2400 BC) uses beads on parallel rods representing units, tens, hundreds, and thousands to execute positional arithmetic."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 2: Punched Cards in Computing",
                        "content": {
                            "question": "What major technological concept did early computers borrow directly from the 1804 Jacquard Loom?",
                            "options": [
                                "Using continuous liquid crystal displays",
                                "Storing programmable binary control instructions on punched cards",
                                "Using steam-powered vacuum tubes",
                                "Continuous logarithmic sliding scales"
                            ],
                            "correct": "B",
                            "explanation": "The Jacquard Loom used punched cards (where holes vs solid areas determined thread positions), pioneering the storage of external programmable instructions for machines."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 3: Babbage's 4-Part Architecture",
                        "content": {
                            "question": "In Charles Babbage's Analytical Engine, which component corresponds directly to modern Random Access Memory (RAM)?",
                            "options": [
                                "The Mill",
                                "The Store",
                                "The Punched Card Reader",
                                "The Steam Piston"
                            ],
                            "correct": "B",
                            "explanation": "The 'Store' held 1,000 numbers of 50 digits each, serving as the memory workspace, while the 'Mill' acted as the central processing unit (CPU/ALU)."
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Application Challenge: The Mechanical Lockbox Algorithm",
                        "content": {
                            "title": "Engineering a 3-Digit Mechanical Security Box",
                            "text": "You are tasked with designing a mechanical lockbox that opens only when a 3-digit combination is entered.\n\n1. **Carry Mechanism Application**: Explain how the Pascaline's automatic carry mechanism can be adapted to count failed unlock attempts.\n2. **Algorithm Formulation**: Write a 4-step natural language algorithm describing how a mechanical pin detects an incorrect dial alignment, advances the 'Failure Counter' dial by one notch, and locks the box permanently after 3 failed attempts."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Lesson 1 Key Takeaways",
                        "content": {
                            "text": "1. Computing evolved from manual place-value beads (Abacus) to pre-calculated lookup tables (Napier's Bones) and analog sliding scales (Slide Rule).\n2. The Pascaline introduced automated arithmetic with its gear-driven carry-over ratchet.\n3. The Jacquard Loom proved that external physical media (punched cards) could store program code.\n4. Charles Babbage and Ada Lovelace established the blueprint of modern computing: Memory (Store), CPU (Mill), Input, Output, and Algorithmic Software."
                        }
                    }
                ]
            ]
        },

        # -------------------------------------------------------------
        # LESSON 2: Generations of Electronic Computers
        # -------------------------------------------------------------
        {
            "unit_order": 2,
            "unit_name": "Generations of Electronic Computers",
            "unit_description": "The five generations of electronic computers: vacuum tubes, transistors, integrated circuits (SSI/MSI), microprocessors (VLSI/ULSI), and AI/quantum computing. Physical, economic, and programming abstraction trends.",
            "lesson_title": "Generations and Development of Electronic Computers",
            "pages": [
                # Card 1: Hook & Goals
                [
                    {
                        "type": "suggested_image",
                        "title": "The 1946 ENIAC: The 27-Ton First-Generation Computer",
                        "content": {
                            "title": "The 1946 ENIAC: The 27-Ton First-Generation Computer",
                            "caption": "Operators programming the ENIAC by re-routing patch cables. Occupying an entire room and using 18,000 glass vacuum tubes, it consumed 150 kW of electrical power.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Eniac.jpg/800px-Eniac.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "Public Domain"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Computer Generations",
                        "content": {
                            "title": "What We Will Master in This Lesson",
                            "goals": [
                                "Define what constitutes a **computer generation**.",
                                "Analyze the dominant active electronic hardware of each of the **five computer generations** (Vacuum Tubes $\\rightarrow$ Transistors $\\rightarrow$ ICs $\\rightarrow$ Microprocessors $\\rightarrow$ AI/Quantum).",
                                "Explain the historical evolution of programming interfaces (Machine Code $\\rightarrow$ Assembly $\\rightarrow$ High-Level $\\rightarrow$ GUIs $\\rightarrow$ Natural Language AI).",
                                "Evaluate physical and economic trends: **miniaturization**, **reliability**, **cost**, and **Moore's Law**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Real-World Hook: The Pocket Supercomputer",
                        "content": {
                            "title": "From Room-Sized Furnaces to Pocket Chips",
                            "text": "Every modern smartphone weighs less than 200 grams, runs for a full day on a small battery, and executes billions of instructions per second.\n\nYet in 1946, the world's premier electronic computer—the **ENIAC**—weighed 27,000 kg, occupied a 135-square-meter room, drew 150,000 watts of power, and generated so much heat that operators had to replace burned-out vacuum tubes every two hours!\n\nWhat enabled this staggering transformation in under 80 years? The answer lies in the **five technological generations** of electronic components."
                        }
                    }
                ],
                # Card 2: The Core Electronic Breakthroughs
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Evolutionary Leaps in Electronic Switching",
                        "content": {
                            "title": "How We Learned to Control Electrical Currents",
                            "text": "Computers process information by rapidly turning electrical circuits ON ($1$) and OFF ($0$). The history of computers is the story of making that switch smaller, faster, cooler, and cheaper:\n\n1. **Vacuum Tubes (1st Gen)**: Glass bulbs containing a glowing filament in a vacuum that switched electrical current. Fragile, hot, and power-hungry.\n2. **Transistors (2nd Gen)**: Tiny solid-state semiconductor crystals that switch currents without moving parts or burning filaments.\n3. **Integrated Circuits (3rd Gen)**: Printing dozens to thousands of transistors onto a single thin wafer of silicon.\n4. **Microprocessors (4th Gen)**: Fabricating an entire Central Processing Unit (CPU) with millions/billions of transistors onto a single silicon chip.\n5. **AI & Quantum Circuits (5th Gen)**: Parallel neural processors and quantum qubits operating in superposition."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Five Computer Generations Architectural Evolution",
                        "content": {
                            "svg_content": SVG_FIVE_GENERATIONS,
                            "caption": "Visual matrix of the 5 computer generations showing the progression from room-sized vacuum tubes to microscopic silicon chips and quantum neural processors."
                        }
                    }
                ],
                # Card 3: The 5 Computer Generations Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Comparative Analysis of the Five Computer Generations",
                        "content": {
                            "headers": ["Generation", "Time Period", "Core Component", "Programming Interface", "Key Hardware Traits", "Famous Systems"],
                            "rows": [
                                ["**First**", "1940s – 1950s", "Vacuum Tubes", "Machine Language (1s & 0s), Plugboards", "Room-sized, massive heat, high power draw, low reliability", "ENIAC, UNIVAC I, EDVAC"],
                                ["**Second**", "1950s – 1960s", "Discrete Transistors", "Assembly Language (Mnemonics), Early FORTRAN", "100x smaller, lower power, faster, reliable solid-state", "IBM 1401, PDP-1, IBM 7090"],
                                ["**Third**", "1960s – 1970s", "Integrated Circuits (SSI/MSI)", "High-Level Languages (COBOL, BASIC, C)", "Keyboards, monitors, minicomputers, multi-user OS", "IBM System/360, DEC PDP-8"],
                                ["**Fourth**", "1970s – Present", "Microprocessors (VLSI/ULSI)", "Modern High-Level, GUIs, Python, Java, Web", "Personal computers (PCs), laptops, smartphones, low cost", "Apple Mac, IBM PC, Modern CPUs"],
                                ["**Fifth**", "Present & Beyond", "AI Processors & Quantum Qubits", "Natural Language, Neural Prompting, Voice", "Parallel execution, voice recognition, machine learning", "AI Supercomputers, Google Sycamore"]
                            ]
                        }
                    }
                ],
                # Card 4: Physical & Economic Trends (Miniaturization & Moore's Law)
                [
                    {
                        "type": "concept_explanation",
                        "title": "Physical and Economic Laws of Evolution",
                        "content": {
                            "title": "Miniaturization, Reliability, and Moore's Law",
                            "text": "Across the five generations, four steady trends transformed computing:\n\n### 1. Miniaturization & Heat Reduction\nReplacing vacuum tubes with solid-state silicon allowed components to shrink by factors of millions. Because silicon switches operate at tiny voltages, heat output and power consumption plummeted.\n\n### 2. Solid-State Reliability\nVacuum tubes burned out continuously because their internal filaments evaporated under intense heat (like old lightbulbs). Transistors have no moving parts or burning filaments, lasting for decades without physical breakdown.\n\n### 3. Moore's Law\nIn 1965, Intel co-founder **Gordon Moore** observed that the number of transistors packed onto a microchip doubles approximately every 18 to 24 months, while the manufacturing cost per transistor is cut in half. This exponential growth enabled high-performance computing to become affordable for everyday people."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Transistor Miniaturization & Moore's Law Trajectory",
                        "content": {
                            "svg_content": SVG_TRANSISTOR_SCALING,
                            "caption": "Step-by-step miniaturization timeline from 10cm thermionic vacuum tubes to 3nm silicon transistors, illustrating the exponential trajectory of Moore's Law."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Evolution from Vintage Vacuum Tube to Silicon Microprocessor",
                        "content": {
                            "title": "Evolution from Vintage Vacuum Tube to Silicon Microprocessor",
                            "caption": "A vintage glass vacuum tube contrasted against a modern microprocessor die containing billions of microscopic transistors.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Intel_4004.jpg/800px-Intel_4004.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    }
                ],
                # Card 5: Interface and Software Abstraction Progression
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Ladder of Software Abstraction",
                        "content": {
                            "title": "How Humans Communicate with Machines",
                            "text": "As hardware became more complex, software developed layers of **abstraction** so programmers didn't have to manage raw electronic switches manually:\n\n- **1st Generation (Machine Code)**: Programmers wrote binary instructions (`10110000 01100001`) or physically plugged patch cords into telephone-style switchboards.\n- **2nd Generation (Assembly Language)**: Replaced binary with readable shorthand mnemonics (e.g., `MOV AX, 5` or `ADD BX, 10`).\n- **3rd Generation (High-Level Languages)**: Introduced English-like syntax (e.g., `IF X > 10 THEN PRINT Y`) translated by compilers, allowing programs to run on different computer brands.\n- **4th Generation (Graphical User Interfaces - GUIs)**: Users interacted with icons, mice, windows, and touchscreen buttons.\n- **5th Generation (Natural Language & Neural AI)**: Users interact using conversational speech, voice assistants, and natural language prompts."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Analytical Analogy: Controlling Traffic",
                        "content": {
                            "text": "**How Switching Evolved:**\n- **1st Gen**: Giant, fragile gas lamps manually lit by street workers.\n- **2nd Gen**: Compact, reliable electric switches operated from a booth.\n- **3rd Gen**: Automated electrical junction boxes controlling an entire city street.\n- **4th Gen**: Microcontroller chips synchronizing all traffic across the entire metropolis.\n- **5th Gen**: AI traffic management analyzing live satellite cameras to dynamically adjust flow in real time."
                        }
                    }
                ],
                # Card 6: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "The Transistor and the Computer Revolution",
                        "content": {
                            "title": "How the Transistor Changed the World",
                            "youtube_id": "7ukDKVHnac4",
                            "url": "https://www.youtube.com/watch?v=7ukDKVHnac4",
                            "description": "An engaging visual breakdown of how semiconductor transistors replaced fragile vacuum tubes, enabling the microchip revolution and modern computing devices."
                        }
                    }
                ],
                # Card 7: Applied Scenario Analysis
                [
                    {
                        "type": "worked_example",
                        "title": "Applied Scenario: Equipping an Off-Grid Rural Medical Clinic",
                        "content": {
                            "title": "Evaluating Hardware Constraints for Real-World Deployment",
                            "problem": "A rural health clinic in northern Kenya operates off a single 200W solar panel with no air conditioning. They need a computer to log patient health records and run digital malaria diagnostic software.",
                            "steps": [
                                "**Analyze 1st / 2nd Generation Tech**: 1st-generation vacuum tube computers consumed 150,000 W (instantly overwhelming solar) and produced massive heat. 2nd-gen mainframe computers required dedicated cooled computer rooms and clean grid power.",
                                "**Evaluate 4th Generation SoC Technology**: A modern 4th-generation System-on-Chip (SoC) laptop or tablet consumes less than 15 W of electricity, runs completely silent with passive heatsinks, and can be charged directly from a 12V solar battery system.",
                                "**Environmental Assessment**: Solid-state flash storage and sealed semiconductor chips resist dust, vibration, and temperature fluctuations.",
                                "**Decision Rationale**: A low-power 4th-generation microprocessor device is the only viable engineering solution for off-grid rural deployment."
                            ]
                        }
                    }
                ],
                # Card 8: Formative Knowledge Checks & Key Takeaways
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 1: 1st Generation Active Component",
                        "content": {
                            "question": "Which electronic component was the defining hardware characteristic of First-Generation computers?",
                            "options": [
                                "Transistors",
                                "Integrated Circuits (ICs)",
                                "Vacuum Tubes",
                                "Microprocessors"
                            ],
                            "correct": "C",
                            "explanation": "First-generation computers (like ENIAC and UNIVAC I) utilized glass vacuum tubes as electronic switches, which produced high heat and had frequent burnouts."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 2: Transistors vs Vacuum Tubes",
                        "content": {
                            "question": "Why were discrete transistors fundamentally superior to vacuum tubes in Second-Generation computers?",
                            "options": [
                                "They required higher voltages to generate brighter light",
                                "They were solid-state devices with no burning filaments, consuming less power and generating far less heat",
                                "They were made of large brass gears that never broke",
                                "They could only be programmed in machine code"
                            ],
                            "correct": "B",
                            "explanation": "Transistors are solid-state semiconductors. They eliminated the fragile, glowing filaments of vacuum tubes, drastically improving reliability while reducing power and size."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 3: Microprocessor Definition",
                        "content": {
                            "question": "What technological breakthrough ushered in the Fourth Generation of computers in the 1970s?",
                            "options": [
                                "Fabricating an entire Central Processing Unit (CPU) onto a single silicon chip (Microprocessor)",
                                "The invention of the manual wooden abacus",
                                "The use of punched paper cards on mechanical looms",
                                "Building the first quantum artificial intelligence supercomputer"
                            ],
                            "correct": "A",
                            "explanation": "The Fourth Generation was defined by the microprocessor (such as the Intel 4004), which integrated all arithmetic, logic, and control circuitry onto one silicon chip."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Lesson 2 Key Takeaways",
                        "content": {
                            "text": "1. **1st Gen**: Vacuum Tubes (Machine code, room-sized, high heat).\n2. **2nd Gen**: Transistors (Assembly mnemonics, smaller, reliable solid-state).\n3. **3rd Gen**: Integrated Circuits (High-level languages, monitors, keyboards).\n4. **4th Gen**: Microprocessors (Personal computers, laptops, smartphones, internet).\n5. **5th Gen**: AI & Quantum Computing (Neural processing, voice/vision, natural language).\n6. **Moore's Law**: Transistor density doubles roughly every two years, driving down cost and expanding computing power across the globe."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_grade10_topic1(replace=True):
    print("=" * 80)
    print("INGESTING TOPIC 1: Evolution of Computers (Grade 10 Computer Science)")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="CBC").first() or Curriculum.objects.filter(id=5).first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 10").first() or Grade.objects.filter(curriculum=curriculum, level=10).first()

    subject, _ = Subject.objects.get_or_create(
        grade=grade,
        name="Computer Science",
        defaults={"description": "Senior Secondary Computer Science Curriculum (Grade 10 CBC)"}
    )
    print(f"[*] Resolved Subject: {subject.name} (ID: {subject.id}) in Grade: {grade.name}")

    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=1,
        defaults={"name": "Evolution of Computers", "description": "Origins of computation, mechanical aids, and five generations of electronic computers."}
    )
    if not t_created:
        topic.name = "Evolution of Computers"
        topic.description = "Origins of computation, mechanical aids, and five generations of electronic computers."
        topic.save()
    print(f"[*] Resolved Topic 1: {topic.name} (ID: {topic.id})")

    if replace:
        print("[*] Replacing existing Topic 1 units, lessons, blocks, and assets...")
        existing_lessons = Lesson.objects.filter(topic=topic)
        LessonAsset.objects.filter(lesson__in=existing_lessons).delete()
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    curriculum_data = build_topic1_curriculum()
    total_units = 0
    total_lessons = 0
    total_pages = 0
    total_blocks = 0
    total_assets = 0

    with transaction.atomic():
        for item in curriculum_data:
            u_order = item["unit_order"]
            u_name = item["unit_name"]
            u_desc = item["unit_description"]
            l_title = item["lesson_title"]
            pages = item["pages"]

            unit = LearningUnit.objects.create(
                topic=topic,
                order=u_order,
                name=u_name,
                description=u_desc
            )
            total_units += 1

            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit,
                title=l_title,
                status="published",
                version=1,
                immutable_metadata={
                    "author": "VLearn Senior Computer Science Curriculum Agent",
                    "grade": "Grade 10",
                    "subject": "Computer Science",
                    "topic_order": 1,
                    "unit_order": u_order
                }
            )
            total_lessons += 1

            block_counter = 1
            for page_idx, page_blocks in enumerate(pages, start=1):
                total_pages += 1
                for comp_idx, block_def in enumerate(page_blocks, start=1):
                    b_type = block_def["type"]
                    b_title = clean_text(block_def.get("title", ""))
                    b_content = clean_dict(block_def.get("content", {}))

                    block = LessonBlock.objects.create(
                        lesson=lesson,
                        block_id=f"g10_cs_t1_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={"topic_order": 1, "unit_order": u_order, "page": page_idx}
                    )
                    block_counter += 1
                    total_blocks += 1

                    # Attach LessonAsset if applicable
                    if b_type == "suggested_diagram" and "svg_content" in b_content:
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type="diagram",
                            source_type="ai_generated",
                            storage_type="embed",
                            status="attached",
                            title=b_title,
                            description=b_content.get("caption", b_title),
                            metadata={"svg_content": b_content["svg_content"]}
                        )
                        block.assets.add(asset)
                        total_assets += 1

                    elif b_type == "suggested_image" and "url" in b_content:
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type="image",
                            source_type="external",
                            storage_type="url",
                            status="attached",
                            title=b_title,
                            description=b_content.get("caption", b_title),
                            url=b_content["url"],
                            metadata={
                                "author": b_content.get("author", "Wikimedia Commons"),
                                "licensing": b_content.get("licensing", "CC BY-SA"),
                                "caption": b_content.get("caption", "")
                            }
                        )
                        block.assets.add(asset)
                        total_assets += 1

                    elif b_type == "suggested_video" and "youtube_id" in b_content:
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type="youtube",
                            source_type="external",
                            storage_type="url",
                            status="attached",
                            title=b_title,
                            description=b_content.get("description", b_title),
                            url=b_content.get("url", f"https://www.youtube.com/watch?v={b_content['youtube_id']}"),
                            metadata={"youtube_id": b_content["youtube_id"]}
                        )
                        block.assets.add(asset)
                        total_assets += 1

            print(f"  [+] Ingested Unit {u_order}: '{u_name}' -> Lesson '{l_title}' ({len(pages)} Pages, {block_counter - 1} Blocks)")

    print("=" * 80)
    print(f"TOPIC 1 INGESTION COMPLETE:")
    print(f"  Units Created:   {total_units}")
    print(f"  Lessons Created: {total_lessons}")
    print(f"  Pages Created:   {total_pages}")
    print(f"  Blocks Created:  {total_blocks}")
    print(f"  Assets Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_grade10_topic1(replace=True)
