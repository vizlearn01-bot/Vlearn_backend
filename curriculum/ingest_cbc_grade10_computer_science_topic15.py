"""
VLearn CBC Grade 10 Computer Science — Topic 15: Control Structures
Production Ingestion & Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Computer Science (Subject ID: 38)
Topic: Control Structures (Topic Order: 15)

Decomposed into 4 Comprehensive Learning Units & 4 Published Lessons:
  1. Introduction to Control Structures & Sequence Flow (Lesson 63)
  2. Selection and Branching Structures (Lessons 64 to 67)
  3. Iteration and Loop Structures (Lessons 68 to 72)
  4. Algorithm Tracing, System Integration, and Assessment (Lessons 73 to 77)
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
# HIGH PRECISION VECTOR SVGS FOR TOPIC 15 (DARK THEME 960x520)
# =====================================================================

SVG_SEQUENCE_FLOW = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Sequence Control Structure &amp; CPU Program Counter Pipeline</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Strict top-to-bottom procedural execution and the Fetch-Decode-Execute linear instruction step</text>

  <!-- Left: Vertical Flowchart -->
  <g transform="translate(45, 90)">
    <rect width="380" height="395" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="380" height="28" rx="8" fill="#0284c7"/>
    <text x="190" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Linear Sequential Execution Flowchart</text>

    <!-- START Terminal -->
    <g transform="translate(115, 38)">
      <rect width="150" height="32" rx="16" fill="#059669" stroke="#34d399" stroke-width="1.5"/>
      <text x="75" y="21" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">START</text>
    </g>

    <!-- Arrow 1 -->
    <line x1="190" y1="70" x2="190" y2="88" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="186,88 190,96 194,88" fill="#38bdf8"/>

    <!-- INPUT Parallelogram -->
    <g transform="translate(70, 96)">
      <polygon points="20,0 240,0 220,36 0,36" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="120" y="22" font-family="monospace" font-size="9.5" fill="#7dd3fc" text-anchor="middle">INPUT current_kwh, prev_kwh</text>
    </g>

    <!-- Arrow 2 -->
    <line x1="190" y1="132" x2="190" y2="150" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="186,150 190,158 194,150" fill="#38bdf8"/>

    <!-- PROCESS 1 Rectangle -->
    <g transform="translate(65, 158)">
      <rect width="250" height="36" rx="4" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="125" y="22" font-family="monospace" font-size="9" fill="#fde68a" text-anchor="middle">units = current_kwh - prev_kwh</text>
    </g>

    <!-- Arrow 3 -->
    <line x1="190" y1="194" x2="190" y2="212" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="186,212 190,220 194,212" fill="#38bdf8"/>

    <!-- PROCESS 2 Rectangle -->
    <g transform="translate(65, 220)">
      <rect width="250" height="36" rx="4" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="125" y="22" font-family="monospace" font-size="9" fill="#fde68a" text-anchor="middle">total = 150 + (units * 12.50)</text>
    </g>

    <!-- Arrow 4 -->
    <line x1="190" y1="256" x2="190" y2="274" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="186,274 190,282 194,274" fill="#38bdf8"/>

    <!-- OUTPUT Parallelogram -->
    <g transform="translate(70, 282)">
      <polygon points="20,0 240,0 220,36 0,36" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="120" y="22" font-family="monospace" font-size="9.5" fill="#7dd3fc" text-anchor="middle">OUTPUT "KES ", total</text>
    </g>

    <!-- Arrow 5 -->
    <line x1="190" y1="318" x2="190" y2="336" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="186,336 190,344 194,336" fill="#38bdf8"/>

    <!-- END Terminal -->
    <g transform="translate(115, 344)">
      <rect width="150" height="32" rx="16" fill="#dc2626" stroke="#f87171" stroke-width="1.5"/>
      <text x="75" y="21" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">END</text>
    </g>
  </g>

  <!-- Right: CPU Program Counter Mechanics -->
  <g transform="translate(450, 90)">
    <rect width="465" height="395" rx="12" fill="#0f172a" stroke="#818cf8" stroke-width="1.5"/>
    <rect width="465" height="28" rx="8" fill="#4f46e5"/>
    <text x="232" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Under the Hood: CPU Program Counter (PC) Progression</text>

    <!-- PC Box -->
    <g transform="translate(20, 40)">
      <rect width="425" height="60" rx="8" fill="#1e1b4b" stroke="#818cf8" stroke-width="1.5"/>
      <text x="15" y="22" font-size="11" font-weight="bold" fill="#a5b4fc">&#9881; CPU Program Counter Register (PC):</text>
      <text x="15" y="42" font-family="monospace" font-size="11" fill="#38bdf8">PC = 0x00401004 <tspan fill="#94a3b8">&#8594; Increments automatically (+4 bytes/word)</tspan></text>
    </g>

    <!-- Fetch-Decode-Execute Memory Stack -->
    <g transform="translate(20, 115)">
      <text x="0" y="15" font-size="11" font-weight="bold" fill="#38bdf8">Linear Memory Address Traversal (No Branch Jumps):</text>

      <g transform="translate(0, 25)">
        <rect width="425" height="34" rx="4" fill="#1e293b" stroke="#34d399"/>
        <text x="15" y="21" font-family="monospace" font-size="10" fill="#34d399">0x00401000</text>
        <text x="120" y="21" font-family="monospace" font-size="10" fill="#ffffff">READ read_current_kwh</text>
        <text x="340" y="21" font-size="9" fill="#a7f3d0">Step 1 (Executed)</text>
      </g>

      <g transform="translate(0, 65)">
        <rect width="425" height="34" rx="4" fill="#1e293b" stroke="#38bdf8"/>
        <text x="15" y="21" font-family="monospace" font-size="10" fill="#38bdf8">0x00401004</text>
        <text x="120" y="21" font-family="monospace" font-size="10" fill="#ffffff">SUB units, curr, prev</text>
        <text x="340" y="21" font-size="9" fill="#7dd3fc">Step 2 (Active)</text>
      </g>

      <g transform="translate(0, 105)">
        <rect width="425" height="34" rx="4" fill="#1e293b" stroke="#64748b"/>
        <text x="15" y="21" font-family="monospace" font-size="10" fill="#94a3b8">0x00401008</text>
        <text x="120" y="21" font-family="monospace" font-size="10" fill="#94a3b8">MUL temp, units, 12.5</text>
        <text x="340" y="21" font-size="9" fill="#64748b">Step 3 (Next)</text>
      </g>

      <g transform="translate(0, 145)">
        <rect width="425" height="34" rx="4" fill="#1e293b" stroke="#64748b"/>
        <text x="15" y="21" font-family="monospace" font-size="10" fill="#94a3b8">0x0040100C</text>
        <text x="120" y="21" font-family="monospace" font-size="10" fill="#94a3b8">ADD total, 150, temp</text>
        <text x="340" y="21" font-size="9" fill="#64748b">Step 4 (Queued)</text>
      </g>
    </g>

    <!-- Key Concept Footer -->
    <g transform="translate(20, 315)">
      <rect width="425" height="55" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#fbbf24">&#128640; Train Track Principle:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">Instructions execute strictly one after another without bypassing or repeating.</text>
    </g>
  </g>
</svg>
""")

SVG_SELECTION_BRANCHING_MATRIX = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Selection &amp; Branching Control Structures</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Single-Way (if), Two-Way (if-else), and Multi-Way (if-elif-else) Boolean Evaluation Logic</text>

  <!-- Left: Two-Way Branching Flowchart -->
  <g transform="translate(45, 90)">
    <rect width="420" height="395" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="420" height="28" rx="8" fill="#0284c7"/>
    <text x="210" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Two-Way Selection Flow (If-Else)</text>

    <!-- START Node -->
    <circle cx="210" cy="50" r="14" fill="#059669"/>
    <text x="210" y="54" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">IN</text>
    <line x1="210" y1="64" x2="210" y2="84" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="206,84 210,92 214,84" fill="#38bdf8"/>

    <!-- Decision Diamond -->
    <g transform="translate(210, 125)">
      <polygon points="0,-32 90,0 0,32 -90,0" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
      <text x="0" y="4" font-family="monospace" font-size="10.5" font-weight="bold" fill="#c7d2fe" text-anchor="middle">score &gt;= 50 ?</text>
    </g>

    <!-- True Branch (Right) -->
    <line x1="300" y1="125" x2="350" y2="125" stroke="#34d399" stroke-width="2"/>
    <line x1="350" y1="125" x2="350" y2="175" stroke="#34d399" stroke-width="2"/>
    <polygon points="346,175 350,183 354,175" fill="#34d399"/>
    <text x="325" y="118" font-size="10" font-weight="bold" fill="#34d399">True</text>

    <g transform="translate(290, 183)">
      <rect width="120" height="42" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="1.5"/>
      <text x="60" y="25" font-family="monospace" font-size="9.5" font-weight="bold" fill="#a7f3d0" text-anchor="middle">OUTPUT "PASS"</text>
    </g>

    <!-- False Branch (Left) -->
    <line x1="120" y1="125" x2="70" y2="125" stroke="#f87171" stroke-width="2"/>
    <line x1="70" y1="125" x2="70" y2="175" stroke="#f87171" stroke-width="2"/>
    <polygon points="66,175 70,183 74,175" fill="#f87171"/>
    <text x="95" y="118" font-size="10" font-weight="bold" fill="#f87171">False</text>

    <g transform="translate(10, 183)">
      <rect width="120" height="42" rx="6" fill="#450a0a" stroke="#ef4444" stroke-width="1.5"/>
      <text x="60" y="25" font-family="monospace" font-size="9.5" font-weight="bold" fill="#fca5a5" text-anchor="middle">OUTPUT "FAIL"</text>
    </g>

    <!-- Reconvergence to Connector -->
    <line x1="70" y1="225" x2="70" y2="280" stroke="#f87171" stroke-width="2"/>
    <line x1="70" y1="280" x2="200" y2="280" stroke="#f87171" stroke-width="2"/>

    <line x1="350" y1="225" x2="350" y2="280" stroke="#34d399" stroke-width="2"/>
    <line x1="350" y1="280" x2="220" y2="280" stroke="#34d399" stroke-width="2"/>

    <!-- Reconnect Circle -->
    <circle cx="210" cy="280" r="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>

    <line x1="210" y1="290" x2="210" y2="325" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="206,325 210,333 214,325" fill="#38bdf8"/>

    <!-- END Node -->
    <g transform="translate(145, 335)">
      <rect width="130" height="32" rx="16" fill="#dc2626" stroke="#f87171" stroke-width="1.5"/>
      <text x="65" y="21" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">END</text>
    </g>
  </g>

  <!-- Right: 3 Selection Classes Comparison -->
  <g transform="translate(495, 90)">
    <rect width="420" height="395" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="420" height="28" rx="8" fill="#059669"/>
    <text x="210" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Selection Hierarchy &amp; Code Syntax</text>

    <!-- Card 1: Single-Way -->
    <g transform="translate(15, 38)">
      <rect width="390" height="68" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="15" y="18" font-size="10.5" font-weight="bold" fill="#38bdf8">1. Single-Way Selection (if)</text>
      <text x="15" y="34" font-size="8.5" fill="#cbd5e1">Bypasses block completely if condition is False.</text>
      <text x="15" y="52" font-family="monospace" font-size="9" fill="#7dd3fc">if temp &gt; 35: activate_fan()</text>
    </g>

    <!-- Card 2: Two-Way -->
    <g transform="translate(15, 114)">
      <rect width="390" height="82" rx="6" fill="#1e293b" stroke="#f59e0b"/>
      <text x="15" y="18" font-size="10.5" font-weight="bold" fill="#fbbf24">2. Two-Way Selection (if - else)</text>
      <text x="15" y="34" font-size="8.5" fill="#cbd5e1">Exactly one of two mutually exclusive paths executes.</text>
      <text x="15" y="52" font-family="monospace" font-size="9" fill="#fde68a">if score &gt;= 50: print("PASS")</text>
      <text x="15" y="68" font-family="monospace" font-size="9" fill="#fde68a">else: print("FAIL")</text>
    </g>

    <!-- Card 3: Multi-Way -->
    <g transform="translate(15, 204)">
      <rect width="390" height="110" rx="6" fill="#1e293b" stroke="#818cf8"/>
      <text x="15" y="18" font-size="10.5" font-weight="bold" fill="#a5b4fc">3. Multi-Way Selection (if - elif - else)</text>
      <text x="15" y="34" font-size="8.5" fill="#cbd5e1">Evaluates sequential ladder; halts at first True match.</text>
      <text x="15" y="52" font-family="monospace" font-size="9" fill="#c7d2fe">if score &gt;= 80: grade = "A"</text>
      <text x="15" y="68" font-family="monospace" font-size="9" fill="#c7d2fe">elif score &gt;= 60: grade = "B"</text>
      <text x="15" y="84" font-family="monospace" font-size="9" fill="#c7d2fe">else: grade = "C"</text>
      <text x="15" y="100" font-size="8" fill="#f87171">&#9888; Arrange from most restrictive to least restrictive!</text>
    </g>

    <!-- Bottom Warning -->
    <g transform="translate(15, 322)">
      <rect width="390" height="58" rx="6" fill="#1e1b4b" stroke="#ef4444"/>
      <text x="15" y="18" font-size="9.5" font-weight="bold" fill="#f87171">&#9888; Logic Trap Alert: Order of Evaluation</text>
      <text x="15" y="34" font-size="8.5" fill="#cbd5e1">Checking <tspan font-family="monospace" fill="#fca5a5">score &gt;= 50</tspan> before <tspan font-family="monospace" fill="#fca5a5">score &gt;= 80</tspan> intercepts A-grade students,</text>
      <text x="15" y="48" font-size="8.5" fill="#cbd5e1">falsely assigning them a passing grade instead of Distinction!</text>
    </g>
  </g>
</svg>
""")

SVG_ITERATION_LOOP_FLOWCHART = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Iteration &amp; Loop Control Mechanics</text>
  <text x="480" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Definite Count-Controlled (FOR) vs. Indefinite Condition-Controlled (WHILE) Loop Architecture</text>

  <!-- Left: Condition-Controlled WHILE Loop Flowchart -->
  <g transform="translate(45, 85)">
    <rect width="420" height="405" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="420" height="28" rx="8" fill="#0284c7"/>
    <text x="210" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">While Loop Flow &amp; State Feedback Loop</text>

    <!-- Initializer Process -->
    <g transform="translate(120, 38)">
      <rect width="180" height="32" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="90" y="20" font-family="monospace" font-size="10" fill="#7dd3fc" text-anchor="middle">temp = 40 (Init LCV)</text>
    </g>

    <line x1="210" y1="70" x2="210" y2="92" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="206,92 210,100 214,92" fill="#38bdf8"/>

    <!-- Re-entry Node -->
    <circle cx="210" cy="105" r="5" fill="#38bdf8"/>

    <!-- Decision Diamond -->
    <g transform="translate(210, 145)">
      <polygon points="0,-32 90,0 0,32 -90,0" fill="#1e1b4b" stroke="#f59e0b" stroke-width="2"/>
      <text x="0" y="4" font-family="monospace" font-size="10" font-weight="bold" fill="#fde68a" text-anchor="middle">temp &gt; 37 ?</text>
    </g>

    <!-- True Branch (Loop Body) -->
    <line x1="210" y1="177" x2="210" y2="205" stroke="#34d399" stroke-width="2"/>
    <polygon points="206,205 210,213 214,205" fill="#34d399"/>
    <text x="220" y="195" font-size="10" font-weight="bold" fill="#34d399">True</text>

    <g transform="translate(95, 213)">
      <rect width="230" height="34" rx="4" fill="#1e293b" stroke="#34d399"/>
      <text x="115" y="21" font-family="monospace" font-size="9" fill="#a7f3d0" text-anchor="middle">OUTPUT "Cooling...", temp</text>
    </g>

    <line x1="210" y1="247" x2="210" y2="265" stroke="#34d399" stroke-width="2"/>
    <polygon points="206,265 210,273 214,265" fill="#34d399"/>

    <!-- State Modification Process (Critical to prevent infinite loop) -->
    <g transform="translate(80, 273)">
      <rect width="260" height="38" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
      <text x="130" y="23" font-family="monospace" font-size="9.5" font-weight="bold" fill="#6ee7b7" text-anchor="middle">temp = temp - 1  (State Update)</text>
    </g>

    <!-- Feedback Loop Upward -->
    <line x1="80" y1="292" x2="35" y2="292" stroke="#38bdf8" stroke-width="2"/>
    <line x1="35" y1="292" x2="35" y2="105" stroke="#38bdf8" stroke-width="2"/>
    <line x1="35" y1="105" x2="205" y2="105" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="197,101 205,105 197,109" fill="#38bdf8"/>
    <text x="45" y="195" font-size="9" fill="#7dd3fc">Repeat Loop</text>

    <!-- False Branch (Exit) -->
    <line x1="300" y1="145" x2="365" y2="145" stroke="#f87171" stroke-width="2"/>
    <line x1="365" y1="145" x2="365" y2="335" stroke="#f87171" stroke-width="2"/>
    <line x1="365" y1="335" x2="280" y2="335" stroke="#f87171" stroke-width="2"/>
    <polygon points="288,331 280,335 288,339" fill="#f87171"/>
    <text x="315" y="138" font-size="10" font-weight="bold" fill="#f87171">False</text>

    <!-- END Terminal -->
    <g transform="translate(145, 345)">
      <rect width="130" height="32" rx="16" fill="#dc2626" stroke="#f87171" stroke-width="1.5"/>
      <text x="65" y="21" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">END (Normal)</text>
    </g>
  </g>

  <!-- Right: Definite vs. Indefinite & Common Traps -->
  <g transform="translate(495, 85)">
    <rect width="420" height="405" rx="12" fill="#0f172a" stroke="#818cf8" stroke-width="1.5"/>
    <rect width="420" height="28" rx="8" fill="#4f46e5"/>
    <text x="210" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Loop Classes &amp; Logical Pitfalls</text>

    <!-- Definite Loop Card -->
    <g transform="translate(15, 38)">
      <rect width="390" height="85" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="15" y="18" font-size="10.5" font-weight="bold" fill="#38bdf8">&#128290; 1. Definite (Count-Controlled) FOR Loop</text>
      <text x="15" y="34" font-size="8.5" fill="#cbd5e1">&#8226; Exact iteration count is known in advance.</text>
      <text x="15" y="50" font-family="monospace" font-size="9" fill="#7dd3fc">for counter in range(1, 6, 1):</text>
      <text x="30" y="66" font-family="monospace" font-size="8.5" fill="#cbd5e1">print(f"Lap {counter}")  # Runs 5 times (1 to 5)</text>
    </g>

    <!-- Indefinite Loop Card -->
    <g transform="translate(15, 130)">
      <rect width="390" height="85" rx="6" fill="#1e293b" stroke="#f59e0b"/>
      <text x="15" y="18" font-size="10.5" font-weight="bold" fill="#fbbf24">&#128337; 2. Indefinite (Condition-Controlled) WHILE Loop</text>
      <text x="15" y="34" font-size="8.5" fill="#cbd5e1">&#8226; Repeats until an unpredictable external condition changes.</text>
      <text x="15" y="50" font-family="monospace" font-size="9" fill="#fde68a">while sensor_reading &lt; threshold:</text>
      <text x="30" y="66" font-family="monospace" font-size="8.5" fill="#cbd5e1">sensor_reading = check_sensor()</text>
    </g>

    <!-- Trap 1: Infinite Loop -->
    <g transform="translate(15, 222)">
      <rect width="390" height="75" rx="6" fill="#450a0a" stroke="#ef4444" stroke-width="1.5"/>
      <text x="15" y="18" font-size="10" font-weight="bold" fill="#f87171">&#9888; Trap A: Infinite Loop (Omission of State Update)</text>
      <text x="15" y="34" font-family="monospace" font-size="8.5" fill="#fca5a5">credits = 10</text>
      <text x="15" y="48" font-family="monospace" font-size="8.5" fill="#fca5a5">while credits &gt; 0: print("Sending...") # Never decrements!</text>
      <text x="15" y="64" font-size="8" fill="#cbd5e1">&#8594; Causes CPU thread freeze and eventual memory exhaustion.</text>
    </g>

    <!-- Trap 2: Off-By-One -->
    <g transform="translate(15, 305)">
      <rect width="390" height="85" rx="6" fill="#1e1b4b" stroke="#818cf8"/>
      <text x="15" y="18" font-size="10" font-weight="bold" fill="#c7d2fe">&#9888; Trap B: Off-by-One Error (Fencepost Bug)</text>
      <text x="15" y="34" font-family="monospace" font-size="8.5" fill="#a5b4fc">for i in range(1, 5): print(i)  # Prints 1, 2, 3, 4 (Not 5!)</text>
      <text x="15" y="50" font-size="8" fill="#cbd5e1">Stop parameter in range(start, stop) is exclusive.</text>
      <text x="15" y="66" font-size="8.5" font-weight="bold" fill="#34d399">&#10003; Remedy: Use range(1, 6) to include 5.</text>
    </g>
  </g>
</svg>
""")

SVG_TRACE_TABLE_STATE_DIAGNOSTICS = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Algorithm Tracing (Dry-Running) &amp; State Table Execution Grid</text>
  <text x="480" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Tracing iteration counter, user input filtering (val &gt;= 0), accumulator updates, and console output for [12, -5, 7, 3]</text>

  <!-- Left: Algorithm Pseudocode Box -->
  <g transform="translate(45, 85)">
    <rect width="300" height="405" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="300" height="28" rx="8" fill="#0284c7"/>
    <text x="150" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Algorithm Code Under Dry Run</text>

    <g transform="translate(15, 38)">
      <rect width="270" height="345" rx="6" fill="#1e1b4b" stroke="#334155"/>
      <text x="15" y="24" font-family="monospace" font-size="10" fill="#38bdf8">START</text>
      <text x="25" y="44" font-family="monospace" font-size="10" fill="#fbbf24">SET sum = 0</text>
      <text x="25" y="68" font-family="monospace" font-size="10" fill="#a5b4fc">FOR counter = 1 TO 4 DO</text>
      <text x="40" y="92" font-family="monospace" font-size="10" fill="#ffffff">INPUT val</text>
      <text x="40" y="116" font-family="monospace" font-size="10" fill="#f472b6">IF val &gt;= 0 THEN</text>
      <text x="55" y="140" font-family="monospace" font-size="10" fill="#34d399">SET sum = sum + val</text>
      <text x="40" y="164" font-family="monospace" font-size="10" fill="#f472b6">ENDIF</text>
      <text x="25" y="188" font-family="monospace" font-size="10" fill="#a5b4fc">ENDFOR</text>
      <text x="25" y="212" font-family="monospace" font-size="10" fill="#38bdf8">OUTPUT sum</text>
      <text x="15" y="236" font-family="monospace" font-size="10" fill="#38bdf8">END</text>

      <!-- Input Stream Banner -->
      <rect x="15" y="260" width="240" height="70" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="25" y="280" font-size="9" font-weight="bold" fill="#38bdf8">&#128229; Test Input Stream:</text>
      <text x="25" y="300" font-family="monospace" font-size="10" fill="#ffffff">[12, -5, 7, 3]</text>
      <text x="25" y="318" font-size="8" fill="#a7f3d0">&#10003; Expects negative values filtered!</text>
    </g>
  </g>

  <!-- Right: Complete Trace Table Grid -->
  <g transform="translate(365, 85)">
    <rect width="550" height="405" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="550" height="28" rx="8" fill="#059669"/>
    <text x="275" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Step-by-Step Diagnostic Trace Table</text>

    <!-- Table Header -->
    <g transform="translate(15, 38)">
      <rect width="520" height="26" fill="#1e293b"/>
      <text x="15" y="17" font-size="9" font-weight="bold" fill="#38bdf8">Step</text>
      <text x="55" y="17" font-size="9" font-weight="bold" fill="#ffffff">Instruction</text>
      <text x="195" y="17" font-size="9" font-weight="bold" fill="#fbbf24">counter</text>
      <text x="260" y="17" font-size="9" font-weight="bold" fill="#38bdf8">val</text>
      <text x="315" y="17" font-size="9" font-weight="bold" fill="#a5b4fc">val &gt;= 0?</text>
      <text x="395" y="17" font-size="9" font-weight="bold" fill="#34d399">sum</text>
      <text x="460" y="17" font-size="9" font-weight="bold" fill="#f472b6">Output</text>
    </g>

    <!-- Row 0: Init -->
    <g transform="translate(15, 68)">
      <rect width="520" height="24" fill="#0f172a"/>
      <text x="15" y="16" font-size="8.5" fill="#94a3b8">—</text>
      <text x="55" y="16" font-size="8.5" fill="#94a3b8">Initialization</text>
      <text x="195" y="16" font-size="8.5" fill="#94a3b8">—</text>
      <text x="260" y="16" font-size="8.5" fill="#94a3b8">—</text>
      <text x="315" y="16" font-size="8.5" fill="#94a3b8">—</text>
      <text x="395" y="16" font-size="9" font-weight="bold" fill="#34d399">0</text>
      <text x="460" y="16" font-size="8.5" fill="#94a3b8">—</text>
    </g>

    <!-- Row 1: Iteration 1 (val = 12) -->
    <g transform="translate(15, 96)">
      <rect width="520" height="24" fill="#1e293b"/>
      <text x="15" y="16" font-size="8.5" fill="#ffffff">1-3</text>
      <text x="55" y="16" font-size="8.5" fill="#cbd5e1">Input 12 &amp; Add</text>
      <text x="195" y="16" font-family="monospace" font-size="8.5" fill="#fbbf24">1</text>
      <text x="260" y="16" font-family="monospace" font-size="8.5" fill="#38bdf8">12</text>
      <text x="315" y="16" font-size="8.5" fill="#34d399">True</text>
      <text x="395" y="16" font-family="monospace" font-size="9" font-weight="bold" fill="#34d399">12</text>
      <text x="460" y="16" font-size="8.5" fill="#94a3b8">—</text>
    </g>

    <!-- Row 2: Iteration 2 (val = -5 Bypassed) -->
    <g transform="translate(15, 124)">
      <rect width="520" height="24" fill="#0f172a" stroke="#ef4444" stroke-width="0.5"/>
      <text x="15" y="16" font-size="8.5" fill="#ffffff">4-6</text>
      <text x="55" y="16" font-size="8.5" fill="#f87171">Input -5 (Bypassed)</text>
      <text x="195" y="16" font-family="monospace" font-size="8.5" fill="#fbbf24">2</text>
      <text x="260" y="16" font-family="monospace" font-size="8.5" fill="#f87171">-5</text>
      <text x="315" y="16" font-size="8.5" font-weight="bold" fill="#f87171">False</text>
      <text x="395" y="16" font-family="monospace" font-size="9" fill="#94a3b8">12</text>
      <text x="460" y="16" font-size="8.5" fill="#94a3b8">—</text>
    </g>

    <!-- Row 3: Iteration 3 (val = 7) -->
    <g transform="translate(15, 152)">
      <rect width="520" height="24" fill="#1e293b"/>
      <text x="15" y="16" font-size="8.5" fill="#ffffff">7-9</text>
      <text x="55" y="16" font-size="8.5" fill="#cbd5e1">Input 7 &amp; Add</text>
      <text x="195" y="16" font-family="monospace" font-size="8.5" fill="#fbbf24">3</text>
      <text x="260" y="16" font-family="monospace" font-size="8.5" fill="#38bdf8">7</text>
      <text x="315" y="16" font-size="8.5" fill="#34d399">True</text>
      <text x="395" y="16" font-family="monospace" font-size="9" font-weight="bold" fill="#34d399">19</text>
      <text x="460" y="16" font-size="8.5" fill="#94a3b8">—</text>
    </g>

    <!-- Row 4: Iteration 4 (val = 3) -->
    <g transform="translate(15, 180)">
      <rect width="520" height="24" fill="#0f172a"/>
      <text x="15" y="16" font-size="8.5" fill="#ffffff">10-12</text>
      <text x="55" y="16" font-size="8.5" fill="#cbd5e1">Input 3 &amp; Add</text>
      <text x="195" y="16" font-family="monospace" font-size="8.5" fill="#fbbf24">4</text>
      <text x="260" y="16" font-family="monospace" font-size="8.5" fill="#38bdf8">3</text>
      <text x="315" y="16" font-size="8.5" fill="#34d399">True</text>
      <text x="395" y="16" font-family="monospace" font-size="9" font-weight="bold" fill="#34d399">22</text>
      <text x="460" y="16" font-size="8.5" fill="#94a3b8">—</text>
    </g>

    <!-- Row 5: Loop Exit & Output -->
    <g transform="translate(15, 208)">
      <rect width="520" height="28" fill="#064e3b" stroke="#34d399" stroke-width="1.5"/>
      <text x="15" y="18" font-size="9" font-weight="bold" fill="#ffffff">13-14</text>
      <text x="55" y="18" font-size="9" font-weight="bold" fill="#a7f3d0">OUTPUT sum</text>
      <text x="195" y="18" font-size="8.5" fill="#94a3b8">—</text>
      <text x="260" y="18" font-size="8.5" fill="#94a3b8">—</text>
      <text x="315" y="18" font-size="8.5" fill="#94a3b8">—</text>
      <text x="395" y="18" font-family="monospace" font-size="10" font-weight="bold" fill="#6ee7b7">22</text>
      <text x="460" y="18" font-family="monospace" font-size="11" font-weight="bold" fill="#38bdf8">22</text>
    </g>

    <!-- Summary Box -->
    <g transform="translate(15, 248)">
      <rect width="520" height="115" rx="6" fill="#1e1b4b" stroke="#38bdf8"/>
      <text x="15" y="20" font-size="10.5" font-weight="bold" fill="#38bdf8">&#128065; Trace Table Key Diagnostic Insights:</text>
      <text x="15" y="38" font-size="9" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#f87171">Negative Filter Verification</tspan>: When val was -5, condition val &gt;= 0 was False,</text>
      <text x="25" y="54" font-size="9" fill="#cbd5e1">safely bypassing line 6 without altering accumulator sum (remained 12).</text>
      <text x="15" y="72" font-size="9" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#fbbf24">Deterministic State Tracking</tspan>: Permits manual dry-running before writing code.</text>
      <text x="15" y="90" font-size="9" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#34d399">Final Console Delivery</tspan>: Output delivers single accumulated integer 22.</text>
    </g>
  </g>
</svg>
""")

SVG_WEATHER_ALERT_SYSTEM_ARCHITECTURE = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Applied Scenario: Mount Kenya Smart Weather Alert Automation</text>
  <text x="480" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Multistage nested selection pipeline integrating Temperature, Wind Speed, and Rainfall sensors</text>

  <!-- Left: Sensor Input Stream -->
  <g transform="translate(45, 85)">
    <rect width="250" height="405" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="250" height="28" rx="8" fill="#0284c7"/>
    <text x="125" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Solar Station Sensors</text>

    <!-- Temp Sensor -->
    <g transform="translate(15, 38)">
      <rect width="220" height="75" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="10" y="18" font-size="9.5" font-weight="bold" fill="#38bdf8">&#127777; Air Temperature (°C)</text>
      <text x="10" y="36" font-family="monospace" font-size="8.5" fill="#ffffff">temp = float(input())</text>
      <text x="10" y="52" font-size="8" fill="#cbd5e1">Threshold: &lt; 0.0 °C</text>
      <text x="10" y="66" font-size="8" fill="#7dd3fc">&#8594; Freeze Alert Trigger</text>
    </g>

    <!-- Wind Sensor -->
    <g transform="translate(15, 122)">
      <rect width="220" height="75" rx="6" fill="#1e293b" stroke="#f59e0b"/>
      <text x="10" y="18" font-size="9.5" font-weight="bold" fill="#fbbf24">&#128168; Wind Speed (km/h)</text>
      <text x="10" y="36" font-family="monospace" font-size="8.5" fill="#ffffff">wind = float(input())</text>
      <text x="10" y="52" font-size="8" fill="#cbd5e1">Threshold: &gt; 60.0 km/h</text>
      <text x="10" y="66" font-size="8" fill="#fde68a">&#8594; Barrier Route Trigger</text>
    </g>

    <!-- Rain Sensor -->
    <g transform="translate(15, 206)">
      <rect width="220" height="75" rx="6" fill="#1e293b" stroke="#818cf8"/>
      <text x="10" y="18" font-size="9.5" font-weight="bold" fill="#a5b4fc">&#127783; Rainfall Rate (mm/h)</text>
      <text x="10" y="36" font-family="monospace" font-size="8.5" fill="#ffffff">rain = float(input())</text>
      <text x="10" y="52" font-size="8" fill="#cbd5e1">Threshold: &gt; 10.0 mm/h</text>
      <text x="10" y="66" font-size="8" fill="#c7d2fe">&#8594; Severe Storm Check</text>
    </g>

    <g transform="translate(15, 292)">
      <rect width="220" height="95" rx="6" fill="#1e1b4b" stroke="#64748b"/>
      <text x="10" y="18" font-size="9" font-weight="bold" fill="#cbd5e1">&#128225; Scan Cycle:</text>
      <text x="10" y="34" font-size="8" fill="#94a3b8">&#8226; Autonomous 60s scan interval</text>
      <text x="10" y="48" font-size="8" fill="#94a3b8">&#8226; Relays digital actuator telemetry</text>
      <text x="10" y="62" font-size="8" fill="#94a3b8">&#8226; Kenya Met Dept compliant</text>
    </g>
  </g>

  <!-- Middle: Multi-Stage Nested Decision Tree -->
  <g transform="translate(315, 85)">
    <rect width="330" height="405" rx="10" fill="#0f172a" stroke="#818cf8" stroke-width="1.5"/>
    <rect width="330" height="28" rx="8" fill="#4f46e5"/>
    <text x="165" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Decision &amp; Nesting Logic Tree</text>

    <!-- Check 1: Freeze -->
    <g transform="translate(15, 38)">
      <rect width="300" height="60" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="15" y="18" font-family="monospace" font-size="9.5" font-weight="bold" fill="#38bdf8">if temp &lt; 0.0:</text>
      <text x="15" y="34" font-size="8.5" fill="#ffffff">&#8594; Action: Freeze Alert</text>
      <text x="15" y="48" font-size="8" fill="#a7f3d0">&#10003; Activates pipe heaters directly</text>
    </g>

    <!-- Check 2: Wind (Nested) -->
    <g transform="translate(15, 108)">
      <rect width="300" height="150" rx="6" fill="#1e1b4b" stroke="#f59e0b"/>
      <text x="15" y="18" font-family="monospace" font-size="9.5" font-weight="bold" fill="#fbbf24">elif wind &gt; 60.0:</text>
      <text x="25" y="36" font-size="8.5" fill="#fde68a">&#9492;&#9472; [Nested Check inside Wind Branch]</text>
      <text x="35" y="56" font-family="monospace" font-size="9" fill="#38bdf8">if rain &gt; 10.0:</text>
      <text x="45" y="74" font-size="8" fill="#fca5a5">&#8594; CRITICAL ALERT: Severe Storm</text>
      <text x="45" y="88" font-size="8" fill="#cbd5e1">(Barriers deployed + Gates opened)</text>
      <text x="35" y="108" font-family="monospace" font-size="9" fill="#38bdf8">else:</text>
      <text x="45" y="124" font-size="8" fill="#fde68a">&#8594; WARNING: High Wind Storm</text>
      <text x="45" y="138" font-size="8" fill="#cbd5e1">(Deploy wind barriers only)</text>
    </g>

    <!-- Check 3: Normal -->
    <g transform="translate(15, 270)">
      <rect width="300" height="55" rx="6" fill="#1e293b" stroke="#10b981"/>
      <text x="15" y="18" font-family="monospace" font-size="9.5" font-weight="bold" fill="#34d399">else:</text>
      <text x="15" y="34" font-size="8.5" fill="#a7f3d0">&#8594; "System operating normally."</text>
      <text x="15" y="46" font-size="8" fill="#cbd5e1">All parameters within baseline range</text>
    </g>

    <!-- Code Rule Badge -->
    <g transform="translate(15, 335)">
      <rect width="300" height="55" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="15" y="18" font-size="8.5" font-weight="bold" fill="#fbbf24">&#128273; Deterministic Mutual Exclusion:</text>
      <text x="15" y="34" font-size="8" fill="#cbd5e1">Only one primary branch triggers per scan pass,</text>
      <text x="15" y="46" font-size="8" fill="#cbd5e1">avoiding conflicting actuator commands.</text>
    </g>
  </g>

  <!-- Right: Physical Actuator Dispatch Output -->
  <g transform="translate(665, 85)">
    <rect width="250" height="405" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="250" height="28" rx="8" fill="#059669"/>
    <text x="125" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Actuator Output Hub</text>

    <!-- Action 1 -->
    <g transform="translate(15, 38)">
      <rect width="220" height="75" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="10" y="18" font-size="9.5" font-weight="bold" fill="#38bdf8">&#9832; Pipe Heaters</text>
      <text x="10" y="34" font-size="8.5" fill="#cbd5e1">Status: Engaged when &lt; 0°C</text>
      <text x="10" y="50" font-size="8" fill="#94a3b8">Prevents frost burst in</text>
      <text x="10" y="64" font-size="8" fill="#94a3b8">sub-zero high altitude lines</text>
    </g>

    <!-- Action 2 -->
    <g transform="translate(15, 122)">
      <rect width="220" height="75" rx="6" fill="#1e293b" stroke="#f59e0b"/>
      <text x="10" y="18" font-size="9.5" font-weight="bold" fill="#fbbf24">&#128737; Wind Barriers</text>
      <text x="10" y="34" font-size="8.5" fill="#cbd5e1">Status: Lowered when &gt; 60 km/h</text>
      <text x="10" y="50" font-size="8" fill="#94a3b8">Protects solar array &amp;</text>
      <text x="10" y="64" font-size="8" fill="#94a3b8">tower masts from sheer load</text>
    </g>

    <!-- Action 3 -->
    <g transform="translate(15, 206)">
      <rect width="220" height="75" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="10" y="18" font-size="9.5" font-weight="bold" fill="#f87171">&#128682; Drainage Sluice Gates</text>
      <text x="10" y="34" font-size="8.5" fill="#cbd5e1">Status: Motorized Gate Open</text>
      <text x="10" y="50" font-size="8" fill="#94a3b8">Triggered when heavy rain</text>
      <text x="10" y="64" font-size="8" fill="#94a3b8">coincides with high wind</text>
    </g>

    <g transform="translate(15, 292)">
      <rect width="220" height="95" rx="6" fill="#064e3b" stroke="#34d399"/>
      <text x="10" y="18" font-size="9.5" font-weight="bold" fill="#34d399">&#10003; Verification Status:</text>
      <text x="10" y="34" font-size="8" fill="#a7f3d0">3-tier test matrix verified:</text>
      <text x="10" y="48" font-size="8" fill="#cbd5e1">&#8226; Normal: (15°C, 20kph, 2mm)</text>
      <text x="10" y="62" font-size="8" fill="#cbd5e1">&#8226; Boundary: (0°C, 60kph, 10mm)</text>
      <text x="10" y="76" font-size="8" fill="#cbd5e1">&#8226; Erroneous: Non-numeric input</text>
    </g>
  </g>
</svg>
""")

# =====================================================================
# DECOMPOSED TOPIC 15 CURRICULUM DATA STRUCTURE
# =====================================================================

TOPIC_15_DATA = {
    "topic_order": 15,
    "topic_name": "Control Structures",
    "topic_description": "Comprehensive study of algorithm execution flow: Sequence structures, CPU program counter mechanics, Selection and branching (single-way, two-way, multi-way, nested), Iteration and loops (definite count-controlled vs. indefinite condition-controlled), logic error pitfalls, trace table dry-running, and real-world system automation.",
    "learning_units": [
        # =====================================================================
        # LEARNING UNIT 1: Introduction to Control Structures & Sequence Flow
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Introduction to Control Structures & Sequence Flow",
            "unit_description": "Foundational definitions of control structures, the Train Track analogy, top-to-bottom sequence flow, flowchart standards, and CPU Program Counter (PC) mechanics.",
            "lesson_title": "Lesson 63: Introduction to Control Structures & Sequence Flow",
            "pages": [
                # Page 1: Train Track Analogy & Core Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Algorithmic Flow and Sequence Mechanics",
                        "content": {
                            "goal": "Explain the role of control structures in computer programming, define linear sequence flow, and trace instruction progression through the CPU Program Counter."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 'Train Track' Analogy & Core Control Structure Definitions",
                        "content": {
                            "text": "Imagine a single-track railway line running through a flat valley. A train starting at Station A must travel through Station B, Station C, and finally arrive at Station D. There are no junctions, switch tracks, or loops on this line. The train cannot bypass any station, nor can it repeat a station it has already passed. It must follow the tracks in the exact order they were laid down, one after another.\n\nThis represents the simplest and most fundamental way a computer executes program code: **Sequence**.\n\n### Core Definitions:\n- **Control Structure**: A logical block within an algorithm that determines the order in which individual statements, instructions, or function calls are executed by a computer system.\n- **Sequence**: The default control structure where instructions are executed sequentially, one after another, in the exact order they appear in the source code from top to bottom.\n- **Flowchart**: A graphical diagram using standardized geometric shapes and connecting arrows to visually map the logical execution paths of an algorithm."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Sequence Control Structure & CPU Program Counter Pipeline",
                        "content": {
                            "svg_content": SVG_SEQUENCE_FLOW,
                            "caption": "Vertical linear flowchart mapping input, calculation, and output stages alongside the CPU Program Counter register incrementation cycle."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Single-Track Linear Railway Illustrating Sequence Flow",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Single_track_railroad_in_winter.jpg/800px-Single_track_railroad_in_winter.jpg",
                            "caption": "A single-track railway line without switches or loops, representing the strict sequential top-to-bottom progression of instructions.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    }
                ],

                # Page 2: Under the Hood - CPU Program Counter & Pseudocode Implementation
                [
                    {
                        "type": "concept_explanation",
                        "title": "Under the Hood: The Sequence Control Mechanism & Program Counter",
                        "content": {
                            "text": "In computer hardware, sequence flow is governed directly by the CPU's **Program Counter (PC)** register during the Fetch-Decode-Execute cycle:\n\n1. **Instruction Fetch**: The CPU loads the memory address of the first instruction into the Program Counter.\n2. **Automatic Incrementation**: During instruction retrieval, the CPU hardware automatically increments the PC to point to the very next contiguous memory address (e.g., adding +4 bytes in a 32-bit word architecture).\n3. **Continuous Downward Flow**: As long as no branch (jump) or call instruction is executed, the CPU executes instruction memory sequentially line-by-line.\n\n### Sequential Algorithm Example: School Science Lab Electricity Billing\n\n```text\nSTART\n    INPUT read_current_kwh\n    INPUT read_previous_kwh\n    SET units_consumed = read_current_kwh - read_previous_kwh\n    SET base_charge = 150.00\n    SET unit_rate = 12.50\n    SET total_bill = base_charge + (units_consumed * unit_rate)\n    OUTPUT \"Total Utility Bill is: KES \", total_bill\nEND\n```"
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Step-by-Step Python Implementation of Sequential Logic",
                        "content": {
                            "problem_statement": "Convert the utility billing pseudocode into an executable Python program, capturing floating-point meter readings, executing sequential calculations, and presenting formatted currency output.",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "step_title": "Capture Sequential Inputs",
                                    "step_description": "Prompt the user for both current and previous meter readings, casting input strings to `float` for numerical precision."
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Execute Mathematical Processing in Order",
                                    "step_description": "Compute `units_consumed`, assign fixed tariff parameters (`base_charge = 150.00`, `unit_rate = 12.50`), and evaluate `total_bill = base_charge + (units_consumed * unit_rate)`."
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Deliver Console Output",
                                    "step_description": "Format the final bill using an f-string to display currency with two decimal places (`KES {total_bill:.2f}`)."
                                }
                            ],
                            "conclusion": "The Python program executes instructions strictly downward: Input -> Calculation -> Output. If line 2 were moved above line 1, the program would fail due to an undefined variable error."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Computer Science Basics: Sequence Control Structure & Algorithms",
                        "content": {
                            "youtube_id": "eSYeHlwDCNA",
                            "title": "Introduction to Algorithms and Flow of Execution",
                            "description": "Educational video explaining how algorithms execute linearly in sequence and how flowcharts visually represent procedural steps."
                        }
                    }
                ],

                # Page 3: Formative Knowledge Checks (4 MCQs)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 1: Sequence Execution Order",
                        "content": {
                            "question": "In a purely sequential control structure, how does the computer execute program instructions?",
                            "options": [
                                "It executes lines randomly based on available CPU cache.",
                                "It executes instructions strictly top-to-bottom, one after another, in the exact order they appear in source code.",
                                "It skips all calculation steps and executes only input and output statements.",
                                "It repeats the entire code block three times before halting."
                            ],
                            "correct_answer": "It executes instructions strictly top-to-bottom, one after another, in the exact order they appear in source code.",
                            "explanation": "Sequence is the default execution flow where the CPU steps through instructions linearly from the first statement downward until the program terminates."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 2: CPU Program Counter Role",
                        "content": {
                            "question": "What is the primary role of the CPU Program Counter (PC) during sequential code execution?",
                            "options": [
                                "To store the user's keyboard inputs in temporary cache.",
                                "To perform floating-point arithmetic calculations.",
                                "To hold the memory address of the next instruction to be fetched and increment automatically during execution.",
                                "To display graphical error messages when syntax rules are broken."
                            ],
                            "correct_answer": "To hold the memory address of the next instruction to be fetched and increment automatically during execution.",
                            "explanation": "The Program Counter (PC) tracks execution by holding the address of the next instruction and auto-incrementing to maintain sequential traversal through contiguous memory."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 3: Flowchart Symbol Identification",
                        "content": {
                            "question": "Which standardized geometric shape in a flowchart represents an Input or Output operation?",
                            "options": [
                                "Rectangle",
                                "Parallelogram",
                                "Diamond",
                                "Oval"
                            ],
                            "correct_answer": "Parallelogram",
                            "explanation": "In ISO/ANSI flowcharting standards, parallelograms represent I/O operations (such as INPUT or OUTPUT), rectangles represent processing steps, and diamonds represent decisions."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 4: Sequential Dependency Error",
                        "content": {
                            "question": "If a programmer attempts to calculate 'total = price * quantity' before the line 'price = 100' is executed, what error occurs in sequential execution?",
                            "options": [
                                "The computer will automatically look ahead, find price = 100, and execute without issue.",
                                "A NameError / Unassigned Variable error will occur because the variable 'price' has not yet been initialized in sequence.",
                                "The program will switch to an infinite loop.",
                                "The CPU will halt and reboot the operating system."
                            ],
                            "correct_answer": "A NameError / Unassigned Variable error will occur because the variable 'price' has not yet been initialized in sequence.",
                            "explanation": "Because execution is strictly top-to-bottom, referencing a variable before its declaration/initialization line causes a runtime lookup failure."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LEARNING UNIT 2: Selection and Branching Structures
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Selection and Branching Structures",
            "unit_description": "The Track Switch analogy, Boolean logic, Single-way (if), Two-way (if-else), Multi-way (if-elif-else), Nested selection, and Order of Evaluation logic pitfalls.",
            "lesson_title": "Lessons 64 to 67: Selection and Branching Structures",
            "pages": [
                # Page 1: The Track Switch Analogy & Boolean Foundation
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Boolean Decisions and Branching Control",
                        "content": {
                            "goal": "Master the design and implementation of single-way, two-way, multi-way, and nested selection structures using relational expressions."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 'Track Switch' Analogy & Boolean Relational Foundation",
                        "content": {
                            "text": "Imagine a train traveling down a track that suddenly splits into two separate paths at a railway switch:\n- If the track indicator shows that the bridge ahead is **closed**, the train is switched to the **Left Track**.\n- If the bridge ahead is **open**, the train is switched to the **Right Track**.\n\nThe train cannot travel on both tracks at the same time. The switch forces a physical decision based on a single condition (the state of the bridge).\n\nIn programming, **Selection (Branching)** evaluates a Boolean condition (`True` or `False`) to choose between alternative execution paths.\n\n### Relational Operators in Boolean Logic:\n\n- `==` (Equal to): Evaluates whether two operands have identical values (e.g. `10 == 5` -> `False`).\n- `!=` (Not equal to): Evaluates whether two operands differ (e.g. `10 != 5` -> `True`).\n- `>` (Greater than): Checks if left operand exceeds right operand (e.g. `10 > 5` -> `True`).\n- `<` (Less than): Checks if left operand is smaller (e.g. `10 < 5` -> `False`).\n- `>=` (Greater than or equal to): Checks if left is greater or equal (e.g. `10 >= 10` -> `True`).\n- `<=` (Less than or equal to): Checks if left is smaller or equal (e.g. `5 <= 3` -> `False`)."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Selection & Branching Control Structures Matrix",
                        "content": {
                            "svg_content": SVG_SELECTION_BRANCHING_MATRIX,
                            "caption": "Two-way selection decision diamond flowchart and code syntax templates comparing single-way, two-way, and multi-way branching."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Railway Track Switch Demonstrating Branching Logic",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Railroad_switch.jpg/800px-Railroad_switch.jpg",
                            "caption": "A mechanical railroad switch mechanism, providing a concrete real-world analogy for conditional branching paths.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    }
                ],

                # Page 2: Three Classes of Selection & Code Architecture
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Three Classes of Selection Architecture",
                        "content": {
                            "text": "Selection structures are categorized into three fundamental classes:\n\n### Class A: Single-Way Selection (`IF`)\nExecutes a block of code only if the condition evaluates to `True`. If `False`, the entire block is bypassed.\n```python\ntemperature = float(input(\"Enter temperature (°C): \"))\nif temperature > 35:\n    print(\"High Temperature Alert! Activating cooling fan.\")\n```\n\n### Class B: Two-Way Selection (`IF-ELSE`)\nOffers exactly two mutually exclusive execution paths. If `True`, the first block executes; if `False`, the second block inside `else` executes.\n```python\nscore = int(input(\"Enter student score: \"))\nif score >= 50:\n    print(\"Status: PASS\")\nelse:\n    print(\"Status: FAIL\")\n```\n\n### Class C: Multi-Way Selection (`IF-ELIF-ELSE`)\nEvaluates multiple sequential conditions in ladder fashion. The first matching condition executes its block, and all remaining checks are bypassed.\n```python\nscore = int(input(\"Enter numeric score: \"))\nif score >= 80:\n    grade = \"A\"\nelif score >= 60:\n    grade = \"B\"\nelif score >= 50:\n    grade = \"C\"\nelse:\n    grade = \"D\"\nprint(f\"Final Grade: {grade}\")\n```"
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Analyzing Nested Selection and the 'Order of Evaluation' Trap",
                        "content": {
                            "problem_statement": "Examine a flawed multi-way grading algorithm where conditions are arranged out of order, and demonstrate how to refactor it to resolve the logic bug.",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "step_title": "Examine the Flawed Code",
                                    "step_description": "Consider `score = 85` evaluated against: `if score >= 50: print('Pass')` followed by `elif score >= 80: print('Distinction')`."
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Trace the Logic Failure",
                                    "step_description": "Because `85 >= 50` evaluates to `True`, the first branch triggers immediately and prints 'Pass', prematurely terminating the structure and bypassing the 'Distinction' check."
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Apply the Golden Rule of Multi-Way Branching",
                                    "step_description": "Re-order conditions from most restrictive to least restrictive: check `score >= 80` first, then `score >= 50`, ensuring accurate grade assignment."
                                }
                            ],
                            "conclusion": "In multi-way selection, order of evaluation determines execution. Always place narrower/stricter conditions before broader conditions."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Selection Control Structures: If, Else, and Elif in Python",
                        "content": {
                            "youtube_id": "f4KOjWS_KZs",
                            "title": "Conditional Statements in Python - If, Elif, Else Explained",
                            "description": "Comprehensive tutorial explaining how conditional branch statements work, how Boolean expressions evaluate, and how to avoid logic traps."
                        }
                    }
                ],

                # Page 3: Formative Knowledge Checks (4 MCQs)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 1: Multi-Way Evaluation Bug",
                        "content": {
                            "question": "Examine the following code block:\n\n```python\nscore = 75\nif score > 60:\n    print('B')\nelif score > 70:\n    print('A')\nelse:\n    print('C')\n```\n\nWhat output will be printed to the console?",
                            "options": [
                                "A",
                                "B",
                                "C",
                                "Syntax Error"
                            ],
                            "correct_answer": "B",
                            "explanation": "Because `75 > 60` is True, the first `if` branch executes immediately, printing 'B' and bypassing all subsequent `elif` checks regardless of their conditions."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 2: Mutually Exclusive Branches",
                        "content": {
                            "question": "In a standard two-way selection structure (if-else), what condition allows both the 'if' block and the 'else' block to execute during the same run?",
                            "options": [
                                "When the condition evaluates to True on a fast CPU.",
                                "When the variable is a floating-point number.",
                                "They can NEVER both execute; the branches are strictly mutually exclusive.",
                                "When both operands are negative numbers."
                            ],
                            "correct_answer": "They can NEVER both execute; the branches are strictly mutually exclusive.",
                            "explanation": "In an `if-else` construct, the paths are mutually exclusive: exactly one path executes depending on whether the Boolean condition evaluates to True or False."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 3: Nested Selection Purpose",
                        "content": {
                            "question": "What is the primary architectural purpose of a 'Nested Selection' structure (an IF inside another IF)?",
                            "options": [
                                "To speed up compiler binary translation time.",
                                "To perform multi-stage dependent validation where a second check is only relevant if the first condition passed.",
                                "To convert integer variables into floating-point numbers.",
                                "To force the program into an indefinite loop."
                            ],
                            "correct_answer": "To perform multi-stage dependent validation where a second check is only relevant if the first condition passed.",
                            "explanation": "Nested selection allows dependent checks (e.g., verifying user exists first, then checking if that specific user has administrator privileges)."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 4: Decision Shape in Flowcharts",
                        "content": {
                            "question": "Which standardized geometric shape in a flowchart represents a conditional decision point with True and False exit paths?",
                            "options": [
                                "Diamond",
                                "Rectangle",
                                "Parallelogram",
                                "Oval"
                            ],
                            "correct_answer": "Diamond",
                            "explanation": "A diamond represents a conditional evaluation or decision point with multiple exit arrows labeled with outcomes (e.g., True/False, Yes/No)."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LEARNING UNIT 3: Iteration and Loop Structures
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Iteration and Loop Structures",
            "unit_description": "The Track Loop analogy, Definite count-controlled loops (FOR), Indefinite condition-controlled loops (WHILE), state modification rules, Infinite loops, and Off-by-one errors.",
            "lesson_title": "Lessons 68 to 72: Iteration and Loop Structures",
            "pages": [
                # Page 1: Track Loop Analogy & Definite vs Indefinite Categories
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Iteration Constructs and Loop Safety",
                        "content": {
                            "goal": "Differentiate between count-controlled (FOR) and condition-controlled (WHILE) loops, analyze loop termination mechanics, and debug infinite loop vulnerabilities."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 'Track Loop' Analogy & Core Iteration Categories",
                        "content": {
                            "text": "Imagine a roller coaster train on a circular loop of track. The train does not simply travel straight through; it circles the same loop multiple times. An automated sensor counts each time the train passes the starting gate. After exactly three laps, the track switch shifts, and the train exits the loop to the station.\n\nIn software engineering, **Iteration (Looping)** allows a block of instructions to repeat multiple times until a specific condition changes.\n\n### The Two Primary Loop Classes:\n\n1. **Definite (Count-Controlled) Loops — The `FOR` Loop**:\n   - Used when the exact number of iterations is known in advance before entering the loop.\n   - Governed by a **Loop Control Variable (LCV)** or counter that starts at a designated initial value, increments/decrements by a fixed step size per cycle, and terminates upon reaching the upper/lower boundary.\n\n2. **Indefinite (Condition-Controlled) Loops — The `WHILE` Loop**:\n   - Used when the number of iterations cannot be predicted in advance because repetition depends on an external runtime event (e.g., user input, sensor threshold, or file end).\n   - Evaluates a Boolean expression *before* each pass. The loop repeats as long as the condition remains `True` and terminates the moment it becomes `False`."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Iteration & Loop Control Mechanics",
                        "content": {
                            "svg_content": SVG_ITERATION_LOOP_FLOWCHART,
                            "caption": "Condition-controlled while loop flowchart showing decision diamond, loop body, state update feedback, and diagnostic comparison with count-controlled for loops."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Roller Coaster Track Loop Illustrating Iteration",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Roller_coaster_loop.jpg/800px-Roller_coaster_loop.jpg",
                            "caption": "A circular roller coaster loop illustrating repetition until an exit condition (lap count or emergency stop) is satisfied.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    }
                ],

                # Page 2: Loop Syntax, State Modification Rule, and Common Traps
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Rule of State Change & Common Iteration Pitfalls",
                        "content": {
                            "text": "### The Inviolable Rule of State Change:\nTo prevent an **infinite loop**, code inside a `WHILE` loop body **must** modify at least one variable involved in the loop continuation condition. If no state change occurs, the condition remains `True` forever.\n\n### Trap A: The Infinite Loop\nAn infinite loop occurs when the loop exit condition is never satisfied, consuming CPU cycles and potentially crashing the application or exhausting system memory.\n```python\n# FLAWED CODE (Infinite Loop Bug)\ncredits = 10\nwhile credits > 0:\n    print(\"Sending message...\")\n    # Bug: Forgot to decrement credits! credits remains 10 forever.\n```\n\n### Trap B: The Off-by-One Error (Fencepost Error)\nAn off-by-one error occurs when a loop executes one time too many or one time too few due to a misunderstanding of boundary operators (`<` vs `<=`) or range function exclusivity.\n```python\n# Intended: Print numbers 1 through 5\nfor i in range(1, 5):  # range(start, stop) excludes stop value!\n    print(i)           # Bug: Prints only 1, 2, 3, 4\n# Fix: Use range(1, 6)\n```"
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Building a Controlled Temperature Cooldown Loop",
                        "content": {
                            "problem_statement": "Construct a condition-controlled Python `while` loop that simulates an industrial furnace cooling down from 40°C to 37°C in 1°C decrements, guaranteeing safe termination.",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "step_title": "Initialize the Loop Control Variable",
                                    "step_description": "Set `temperature = 40` prior to entering the loop structure."
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Define Continuation Condition",
                                    "step_description": "Set condition `while temperature > 37:` to allow passes at 40, 39, and 38."
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Execute Body and Mandatory State Update",
                                    "step_description": "Print `Cooling down... Current: {temperature}°C` and decrement `temperature = temperature - 1`."
                                },
                                {
                                    "step_number": 4,
                                    "step_title": "Handle Loop Exit",
                                    "step_description": "Once temperature reaches 37, `37 > 37` evaluates to `False`, terminating the loop and printing `Normal temperature restored!`."
                                }
                            ],
                            "conclusion": "The state modification step (`temperature = temperature - 1`) ensures that the loop executes exactly 3 times and terminates cleanly."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Loops in Computer Science: For Loops vs While Loops",
                        "content": {
                            "youtube_id": "6iF8Xb7Z3wQ",
                            "title": "Python While and For Loops Explained with Real Examples",
                            "description": "Clear visual explanation of count-controlled versus condition-controlled loops, infinite loop dangers, and boundary conditions."
                        }
                    }
                ],

                # Page 3: Formative Knowledge Checks (4 MCQs)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 1: Definition of Infinite Loop",
                        "content": {
                            "question": "Which of the following is the most accurate definition of an 'infinite loop'?",
                            "options": [
                                "A loop that executes exactly 1024 times before stopping.",
                                "A loop whose logical boundary condition evaluates to True on every pass, causing the block to run indefinitely without terminating.",
                                "A loop that fails to compile due to missing punctuation.",
                                "A loop inside another loop that runs on a secondary CPU core."
                            ],
                            "correct_answer": "A loop whose logical boundary condition evaluates to True on every pass, causing the block to run indefinitely without terminating.",
                            "explanation": "An infinite loop occurs when the loop's exit condition is never satisfied, causing repeated execution that does not terminate on its own."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 2: Loop Iteration Count Tracing",
                        "content": {
                            "question": "Examine the following pseudocode:\n\n```text\nSET i = 1\nWHILE i < 4 DO\n    OUTPUT i\n    SET i = i + 1\nENDWHILE\n```\n\nHow many times will the loop body execute?",
                            "options": [
                                "1 time",
                                "3 times",
                                "4 times",
                                "Infinitely"
                            ],
                            "correct_answer": "3 times",
                            "explanation": "The loop executes for `i = 1`, `i = 2`, and `i = 3` (3 iterations). When `i` becomes 4, `4 < 4` is False, and the loop terminates."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 3: Avoiding Infinite Loops",
                        "content": {
                            "question": "What must a programmer include inside the body of a WHILE loop to guarantee it does not become an infinite loop?",
                            "options": [
                                "An instruction that modifies the value of at least one variable tested in the loop continuation condition.",
                                "A call to a graphical user interface window.",
                                "A comment line explaining the variable names.",
                                "A floating-point conversion of all loop counters."
                            ],
                            "correct_answer": "An instruction that modifies the value of at least one variable tested in the loop continuation condition.",
                            "explanation": "The Rule of State Change requires that loop variables are updated inside the body so the continuation condition eventually evaluates to False."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 4: Understanding Off-by-One Errors",
                        "content": {
                            "question": "What causes an 'off-by-one' error in iteration structures?",
                            "options": [
                                "A divide-by-zero math exception.",
                                "Mismatched boundary conditions (such as confusing `<` with `<=`) that cause a loop to run one time too many or one time too few.",
                                "Using uppercase letters in variable names.",
                                "Placing print statements outside the program body."
                            ],
                            "correct_answer": "Mismatched boundary conditions (such as confusing `<` with `<=`) that cause a loop to run one time too many or one time too few.",
                            "explanation": "Off-by-one errors happen when loop bounds are incorrectly specified, leading to an extra or missing iteration."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LEARNING UNIT 4: Algorithm Tracing, System Integration, and Assessment
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Algorithm Tracing, System Integration, and Assessment",
            "unit_description": "Dry-running algorithms using trace tables, state variable management, practical classroom coding labs, Mount Kenya smart weather alert case study, and summative unit assessment.",
            "lesson_title": "Lessons 73 to 77: Tracing, Integration, and Assessment",
            "pages": [
                # Page 1: State Management and Trace Tables
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Dry-Running Algorithms and Complex Integration",
                        "content": {
                            "goal": "Master algorithm tracing using diagnostic trace tables, implement multi-condition sensor workflows in Python, and validate algorithmic correctness across test matrices."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "State Management and Trace Table (Dry-Running) Mechanics",
                        "content": {
                            "text": "A **Trace Table** is an essential diagnostic grid used by computer scientists to manually test and track the step-by-step state of an algorithm's variables during execution. This manual simulation process is known as **dry-running**.\n\n### The Algorithm Under Test:\nBelow is an algorithm that iterates 4 times, accepting user inputs to calculate a cumulative sum while filtering out negative numbers:\n\n```text\nSTART\n    SET sum = 0\n    FOR counter = 1 TO 4 STEP 1 DO\n        INPUT val\n        IF val >= 0 THEN\n            SET sum = sum + val\n        ENDIF\n    ENDFOR\n    OUTPUT sum\nEND\n```\n\n### Test Input Stream: `[12, -5, 7, 3]`\n- **Pass 1** (`val = 12`): `12 >= 0` is `True` -> `sum = 0 + 12 = 12`\n- **Pass 2** (`val = -5`): `-5 >= 0` is `False` -> Addition bypassed, `sum` remains `12`\n- **Pass 3** (`val = 7`): `7 >= 0` is `True` -> `sum = 12 + 7 = 19`\n- **Pass 4** (`val = 3`): `3 >= 0` is `True` -> `sum = 19 + 3 = 22`\n- **Output**: Program prints `22`."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Algorithm Tracing & State Table Execution Grid",
                        "content": {
                            "svg_content": SVG_TRACE_TABLE_STATE_DIAGNOSTICS,
                            "caption": "Step-by-step diagnostic trace table grid showing variable state changes, branch bypassing, and final accumulator output."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Software Engineering Debugging and Algorithmic Analysis",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Code_Review_Process.jpg/800px-Code_Review_Process.jpg",
                            "caption": "Software engineers analyzing algorithm execution flow and conducting dry runs to diagnose edge-case logic bugs.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    }
                ],

                # Page 2: Applied Scenario - Mount Kenya Smart Weather Alert System
                [
                    {
                        "type": "concept_explanation",
                        "title": "Practical Classroom Labs & Applied Case Studies",
                        "content": {
                            "text": "### Lab 1: Automated Irrigation Valve Switcher\nBuild a multi-way branching algorithm in Python to manage greenhouse water flow based on soil moisture:\n- Moisture < 30%: Open valve fully (`valve = 100`)\n- Moisture 30% to 60% (inclusive): Open valve halfway (`valve = 50`)\n- Moisture > 60%: Close valve completely (`valve = 0`)\n\n### Lab 2: Login Retry Limiter\nImplement a condition-controlled `while` loop that allows a user up to 3 password attempts before locking the account."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Applied Scenario: Mount Kenya Smart Weather Alert Automation",
                        "content": {
                            "svg_content": SVG_WEATHER_ALERT_SYSTEM_ARCHITECTURE,
                            "caption": "Multi-stage nested decision architecture connecting weather sensors (temperature, wind, rain) to automated actuators on Mount Kenya."
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Mount Kenya Smart Weather Alert System Implementation",
                        "content": {
                            "problem_statement": "Implement the complete Python control program for the Mount Kenya automated station following the specification rules:\n1. Rule A: If temperature < 0°C -> Alert freeze warning & activate pipe heaters.\n2. Rule B: If wind speed > 60 km/h, check rainfall rate. If rainfall > 10 mm/h -> Severe storm alert (barriers + drainage gates). Otherwise -> High wind warning (barriers only).\n3. Rule C: Otherwise -> System operating normally.",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "step_title": "Capture Sensor Inputs",
                                    "step_description": "Read `temp = float(input())`, `wind = float(input())`, `rain = float(input())`."
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Evaluate Freeze Threshold",
                                    "step_description": "Execute `if temp < 0:` and print freeze warning."
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Evaluate Wind and Nested Rainfall Thresholds",
                                    "step_description": "Execute `elif wind > 60:` containing nested `if rain > 10:` for severe storm alert and `else:` for high wind warning."
                                },
                                {
                                    "step_number": 4,
                                    "step_title": "Default Baseline Condition",
                                    "step_description": "Execute `else:` block printing `System operating normally.`"
                                }
                            ],
                            "conclusion": "The multi-way nested selection guarantees mutual exclusion: only the relevant sensor alert triggers during any individual scan cycle."
                        }
                    }
                ],

                # Page 3: Summative Unit Assessment Library (MCQs & Diagnostics)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative Check 1: Diagnostic Trace Table Purpose",
                        "content": {
                            "question": "What is the primary function of a trace table in computer science?",
                            "options": [
                                "To compile Python source code into machine binary code at maximum speed.",
                                "To manually track and record the values of variables step-by-step through an algorithm to verify logic correctness.",
                                "To connect a database server to a web interface.",
                                "To draw graphic vector user interfaces."
                            ],
                            "correct_answer": "To manually track and record the values of variables step-by-step through an algorithm to verify logic correctness.",
                            "explanation": "A trace table is a diagnostic tool used during dry-running to track variable states and conditional evaluations step-by-step without executing on a computer."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative Check 2: Loop vs Selection Distinction",
                        "content": {
                            "question": "How does an Iteration (loop) structure differ fundamentally from a Selection (branching) structure?",
                            "options": [
                                "Selection can repeat code multiple times, whereas Iteration only evaluates once.",
                                "Iteration repeats a block of instructions multiple times based on a condition, whereas Selection executes a block at most once.",
                                "Iteration cannot evaluate Boolean expressions.",
                                "Selection requires a loop control variable counter."
                            ],
                            "correct_answer": "Iteration repeats a block of instructions multiple times based on a condition, whereas Selection executes a block at most once.",
                            "explanation": "Selection chooses between alternative paths and executes the chosen block once; Iteration repeats a code block multiple times until its termination condition is met."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative Check 3: Identifying True/False Statement",
                        "content": {
                            "question": "Which of the following statements regarding control structures is TRUE?",
                            "options": [
                                "In sequential control flow, instructions can jump randomly to arbitrary line numbers without branch instructions.",
                                "A FOR loop is classified as an indefinite loop because its boundaries are unknown at runtime.",
                                "In multi-way selection (if-elif-else), once a condition evaluates to True and its block executes, all subsequent elif/else checks in that structure are skipped.",
                                "Off-by-one errors only occur in hardware memory circuits."
                            ],
                            "correct_answer": "In multi-way selection (if-elif-else), once a condition evaluates to True and its block executes, all subsequent elif/else checks in that structure are skipped.",
                            "explanation": "Multi-way selection structures evaluate sequentially from top to bottom; as soon as one branch evaluates to True, its block runs and the remaining branches are bypassed."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative Check 4: Mount Kenya Weather Logic Route",
                        "content": {
                            "question": "Under the Mount Kenya alert logic, if temp = 5.0°C, wind = 75.0 km/h, and rain = 15.0 mm/h, which alert is generated?",
                            "options": [
                                "ALERT: Freeze warning. Activating pipe heaters.",
                                "CRITICAL ALERT: Severe storm detected. Deploying structural wind barriers and opening drainage gates.",
                                "WARNING: High wind storm. Deploying structural wind barriers.",
                                "System operating normally."
                            ],
                            "correct_answer": "CRITICAL ALERT: Severe storm detected. Deploying structural wind barriers and opening drainage gates.",
                            "explanation": "Because `temp < 0` (5.0 < 0) is False, it proceeds to `elif wind > 60` (75.0 > 60 = True). Inside this branch, `rain > 10` (15.0 > 10 = True) triggers the Critical Severe Storm Alert."
                        }
                    }
                ]
            ]
        }
    ]
}

# =====================================================================
# INGESTION RUNNER
# =====================================================================

def ingest_grade10_topic15(replace: bool = True):
    """Executes atomic database transaction to ingest Topic 15 curriculum content."""
    print("=" * 80)
    print("STARTING VLEARN CBC GRADE 10 COMPUTER SCIENCE — TOPIC 15 INGESTION")
    print("=" * 80)

    with transaction.atomic():
        # Validate Subject & Grade
        subject = Subject.objects.get(id=38) # Grade 10 Computer Science
        print(f"[+] Target Subject: {subject.name} (Grade: {subject.grade.name}, Curriculum: {subject.grade.curriculum.name})")

        # Handle Topic 15 creation / retrieval
        topic, created = Topic.objects.get_or_create(
            subject=subject,
            order=TOPIC_15_DATA["topic_order"],
            defaults={
                "name": TOPIC_15_DATA["topic_name"],
                "description": TOPIC_15_DATA["topic_description"]
            }
        )

        if not created and replace:
            print(f"[*] Topic 15 already exists (ID: {topic.id}). Performing clean replacement of sub-entities...")
            topic.name = TOPIC_15_DATA["topic_name"]
            topic.description = TOPIC_15_DATA["topic_description"]
            topic.save()
            # Delete old learning units (cascade deletes lessons, blocks, assets)
            topic.learning_units.all().delete()
            print("    [x] Old learning units purged.")
        elif created:
            print(f"[+] Created Topic 15: '{topic.name}' (ID: {topic.id})")

        total_units = 0
        total_lessons = 0
        total_pages = 0
        total_blocks = 0
        total_assets = 0

        # Iterate over Learning Units
        for unit_data in TOPIC_15_DATA["learning_units"]:
            u_order = unit_data["unit_order"]
            u_name = clean_text(unit_data["unit_name"])
            u_desc = clean_text(unit_data["unit_description"])
            l_title = clean_text(unit_data["lesson_title"])
            pages = unit_data["pages"]

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
                    "author": "VLearn Senior Computer Science Curriculum Ingestion Specialist",
                    "curriculum_id": 5,
                    "grade": "Grade 10",
                    "subject": "Computer Science",
                    "topic_order": 15,
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
                        block_id=f"g10_cs_t15_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={"topic_order": 15, "unit_order": u_order, "page": page_idx}
                    )
                    block_counter += 1
                    total_blocks += 1

                    # Attach LessonAssets
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
    print("TOPIC 15 INGESTION COMPLETE:")
    print(f"  Units Created:   {total_units}")
    print(f"  Lessons Created: {total_lessons}")
    print(f"  Pages Created:   {total_pages}")
    print(f"  Blocks Created:  {total_blocks}")
    print(f"  Assets Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_grade10_topic15(replace=True)
