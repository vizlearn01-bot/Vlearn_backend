"""
VLearn CBC Grade 10 Computer Science — Topic 13: Program Development
Production Ingestion & Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Computer Science (ID: 38)
Topic: Program Development (Topic Order: 13)

Decomposed into 4 Comprehensive Learning Units & 4 Published Lessons:
  1. The Program Development Cycle (PDC) and System Requirements (Lesson 45)
  2. Algorithm Representation: Standard Pseudocode & Flowchart Symbols (Lessons 46, 47 & 48)
  3. Logic Verification: Tracing, Dry Runs & Systematic Test Strategies (Lessons 49, 50 & 51)
  4. Algorithm Integrity, Design Review, Documentation & Applied Practicals (Lessons 52A, 52B, 53, 54, 55 & 56)
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
    # Remove citations like [129], [135, 157], [image_1], [S12], etc.
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
# HIGH PRECISION VECTOR SVGS FOR TOPIC 13 (DARK THEME, VIEWBOX 960x520)
# =====================================================================

SVG_PDC_LIFECYCLE = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Six Stages of the Program Development Cycle (PDC)</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Systematic, iterative software engineering methodology from problem formulation to lifetime maintenance</text>

  <!-- Stage 1: Problem Definition -->
  <g transform="translate(50, 95)">
    <rect width="255" height="115" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="2"/>
    <rect width="255" height="26" rx="8" fill="#0284c7"/>
    <text x="127" y="18" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Problem Definition &amp; Reqs</text>
    <text x="15" y="48" font-size="10" font-weight="bold" fill="#38bdf8">&#8226; Stakeholder Interviews</text>
    <text x="15" y="66" font-size="9" fill="#cbd5e1">&#8226; Inputs, Outputs &amp; Constraints</text>
    <text x="15" y="84" font-size="9" fill="#cbd5e1">&#8226; Deliverable: SRS Specification</text>
    <rect x="15" y="93" width="225" height="15" rx="3" fill="#1e293b"/>
    <text x="127" y="104" font-size="8" fill="#7dd3fc" text-anchor="middle">Example: Identify l, w &gt; 0 for Area</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <g transform="translate(305, 152)">
    <line x1="0" y1="0" x2="45" y2="0" stroke="#38bdf8" stroke-width="2.5"/>
    <polygon points="45,-4 53,0 45,4" fill="#38bdf8"/>
  </g>

  <!-- Stage 2: Program Design -->
  <g transform="translate(355, 95)">
    <rect width="255" height="115" rx="10" fill="#0f172a" stroke="#8b5cf6" stroke-width="2"/>
    <rect width="255" height="26" rx="8" fill="#7c3aed"/>
    <text x="127" y="18" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Program Design (Algorithm)</text>
    <text x="15" y="48" font-size="10" font-weight="bold" fill="#c4b5fd">&#8226; Language-Independent Logic</text>
    <text x="15" y="66" font-size="9" fill="#cbd5e1">&#8226; Pseudocode &amp; Flowcharts</text>
    <text x="15" y="84" font-size="9" fill="#cbd5e1">&#8226; Trace Table Verification (Dry Run)</text>
    <rect x="15" y="93" width="225" height="15" rx="3" fill="#1e293b"/>
    <text x="127" y="104" font-size="8" fill="#ddd6fe" text-anchor="middle">SET area = length * width</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <g transform="translate(610, 152)">
    <line x1="0" y1="0" x2="45" y2="0" stroke="#8b5cf6" stroke-width="2.5"/>
    <polygon points="45,-4 53,0 45,4" fill="#8b5cf6"/>
  </g>

  <!-- Stage 3: Coding -->
  <g transform="translate(660, 95)">
    <rect width="250" height="115" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <rect width="250" height="26" rx="8" fill="#059669"/>
    <text x="125" y="18" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Coding (Implementation)</text>
    <text x="15" y="48" font-size="10" font-weight="bold" fill="#34d399">&#8226; Translate Logic into Code</text>
    <text x="15" y="66" font-size="9" fill="#cbd5e1">&#8226; Select Language (Python, C++)</text>
    <text x="15" y="84" font-size="9" fill="#cbd5e1">&#8226; IDE Syntax &amp; Structure Standards</text>
    <rect x="15" y="93" width="220" height="15" rx="3" fill="#1e293b"/>
    <text x="125" y="104" font-size="8" fill="#a7f3d0" text-anchor="middle">area = float(l) * float(w)</text>
  </g>

  <!-- Vertical Arrow Down (Stage 3 -> Stage 4) -->
  <g transform="translate(785, 210)">
    <line x1="0" y1="0" x2="0" y2="40" stroke="#10b981" stroke-width="2.5"/>
    <polygon points="-4,40 4,40 0,48" fill="#10b981"/>
  </g>

  <!-- Stage 4: Testing & Debugging -->
  <g transform="translate(660, 260)">
    <rect width="250" height="120" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect width="250" height="26" rx="8" fill="#d97706"/>
    <text x="125" y="18" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">4. Testing &amp; Debugging</text>
    <text x="15" y="48" font-size="10" font-weight="bold" fill="#fbbf24">&#8226; Test Data Suites (Normal/Bound/Err)</text>
    <text x="15" y="66" font-size="9" fill="#cbd5e1">&#8226; Isolate &amp; Fix Bugs (Syntax/Logic)</text>
    <text x="15" y="84" font-size="9" fill="#cbd5e1">&#8226; Regression &amp; Boundary Testing</text>
    <rect x="15" y="96" width="220" height="15" rx="3" fill="#1e293b"/>
    <text x="125" y="107" font-size="8" fill="#fde68a" text-anchor="middle">Test: l=5, w=10 -&gt; Expected: 50</text>
  </g>

  <!-- Arrow 4 -> 5 -->
  <g transform="translate(660, 320)">
    <line x1="0" y1="0" x2="-45" y2="0" stroke="#f59e0b" stroke-width="2.5"/>
    <polygon points="-45,-4 -53,0 -45,4" fill="#f59e0b"/>
  </g>

  <!-- Stage 5: System Documentation -->
  <g transform="translate(355, 260)">
    <rect width="255" height="120" rx="10" fill="#0f172a" stroke="#ec4899" stroke-width="2"/>
    <rect width="255" height="26" rx="8" fill="#db2777"/>
    <text x="127" y="18" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">5. System Documentation</text>
    <text x="15" y="48" font-size="10" font-weight="bold" fill="#f472b6">&#8226; Internal: Comments &amp; Identifiers</text>
    <text x="15" y="66" font-size="9" fill="#cbd5e1">&#8226; External: User &amp; Technical Manuals</text>
    <text x="15" y="84" font-size="9" fill="#cbd5e1">&#8226; Maintenance &amp; Architecture Specs</text>
    <rect x="15" y="96" width="225" height="15" rx="3" fill="#1e293b"/>
    <text x="127" y="107" font-size="8" fill="#fbcfe8" text-anchor="middle"># Computes area in square meters</text>
  </g>

  <!-- Arrow 5 -> 6 -->
  <g transform="translate(355, 320)">
    <line x1="0" y1="0" x2="-45" y2="0" stroke="#ec4899" stroke-width="2.5"/>
    <polygon points="-45,-4 -53,0 -45,4" fill="#ec4899"/>
  </g>

  <!-- Stage 6: System Maintenance -->
  <g transform="translate(50, 260)">
    <rect width="255" height="120" rx="10" fill="#0f172a" stroke="#6366f1" stroke-width="2"/>
    <rect width="255" height="26" rx="8" fill="#4f46e5"/>
    <text x="127" y="18" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">6. System Maintenance</text>
    <text x="15" y="48" font-size="10" font-weight="bold" fill="#818cf8">&#8226; Corrective: Fix Discovered Bugs</text>
    <text x="15" y="66" font-size="9" fill="#cbd5e1">&#8226; Adaptive: New OS &amp; Environment</text>
    <text x="15" y="84" font-size="9" fill="#cbd5e1">&#8226; Perfective: Add Features / Speed</text>
    <rect x="15" y="96" width="225" height="15" rx="3" fill="#1e293b"/>
    <text x="127" y="107" font-size="8" fill="#c7d2fe" text-anchor="middle">Feature: Support Imperial/Metric Units</text>
  </g>

  <!-- FEEDBACK LOOP PATH: From Testing/Debugging & Maintenance back to Requirements/Design -->
  <path d="M 785,380 C 785,460 177,460 177,215" fill="none" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="6,4"/>
  <polygon points="173,220 181,220 177,210" fill="#ef4444"/>

  <!-- Feedback Loop Banner -->
  <rect x="330" y="430" width="300" height="35" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
  <text x="480" y="452" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">&#8635; Iterative Feedback Loop: Logic Refinement &amp; Re-Testing</text>
</svg>
""")

SVG_FLOWCHART_SYMBOLS_MATRIX = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Standard Flowchart Geometric Symbols &amp; Computational Roles</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">ISO / ANSI standardized graphical primitives for language-independent algorithm design</text>

  <!-- Symbol 1: Terminal -->
  <g transform="translate(45, 90)">
    <rect width="270" height="120" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="15" y="15" width="100" height="40" rx="20" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="39" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">START / END</text>
    <text x="130" y="30" font-size="12" font-weight="bold" fill="#38bdf8">1. Terminal</text>
    <text x="130" y="48" font-size="9.5" fill="#94a3b8">Shape: Rounded Oval</text>
    <text x="15" y="78" font-size="9" fill="#cbd5e1"><tspan font-weight="bold" fill="#7dd3fc">Role:</tspan> Marks start or stop boundary.</text>
    <text x="15" y="95" font-size="8.5" fill="#94a3b8">Pseudocode: <tspan font-family="monospace" fill="#38bdf8">START</tspan>, <tspan font-family="monospace" fill="#38bdf8">STOP</tspan>, <tspan font-family="monospace" fill="#38bdf8">END</tspan></text>
    <text x="15" y="110" font-size="8" fill="#64748b">Rule: Exactly 1 Start; 1 exit line from Start.</text>
  </g>

  <!-- Symbol 2: Input / Output -->
  <g transform="translate(345, 90)">
    <rect width="270" height="120" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <polygon points="35,15 115,15 95,55 15,55" fill="#059669" stroke="#10b981" stroke-width="2"/>
    <text x="65" y="39" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">READ / PRINT</text>
    <text x="130" y="30" font-size="12" font-weight="bold" fill="#34d399">2. Input / Output</text>
    <text x="130" y="48" font-size="9.5" fill="#94a3b8">Shape: Parallelogram</text>
    <text x="15" y="78" font-size="9" fill="#cbd5e1"><tspan font-weight="bold" fill="#6ee7b7">Role:</tspan> Captures user input or outputs data.</text>
    <text x="15" y="95" font-size="8.5" fill="#94a3b8">Pseudocode: <tspan font-family="monospace" fill="#34d399">INPUT</tspan>, <tspan font-family="monospace" fill="#34d399">READ</tspan>, <tspan font-family="monospace" fill="#34d399">OUTPUT</tspan>, <tspan font-family="monospace" fill="#34d399">DISPLAY</tspan></text>
    <text x="15" y="110" font-size="8" fill="#64748b">Example: INPUT length, DISPLAY area</text>
  </g>

  <!-- Symbol 3: Process -->
  <g transform="translate(645, 90)">
    <rect width="270" height="120" rx="8" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect x="15" y="15" width="100" height="40" fill="#7c3aed" stroke="#8b5cf6" stroke-width="2"/>
    <text x="65" y="39" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">CALCULATION</text>
    <text x="130" y="30" font-size="12" font-weight="bold" fill="#c4b5fd">3. Process</text>
    <text x="130" y="48" font-size="9.5" fill="#94a3b8">Shape: Rectangle</text>
    <text x="15" y="78" font-size="9" fill="#cbd5e1"><tspan font-weight="bold" fill="#ddd6fe">Role:</tspan> Arithmetic or variable assignment.</text>
    <text x="15" y="95" font-size="8.5" fill="#94a3b8">Pseudocode: <tspan font-family="monospace" fill="#c4b5fd">SET</tspan>, <tspan font-family="monospace" fill="#c4b5fd">LET</tspan>, mathematical operations</text>
    <text x="15" y="110" font-size="8" fill="#64748b">Example: SET sum = sum + counter</text>
  </g>

  <!-- Symbol 4: Decision (Diamond with 2 Branches) -->
  <g transform="translate(45, 225)">
    <rect width="420" height="145" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <!-- Diamond -->
    <polygon points="65,15 115,45 65,75 15,45" fill="#d97706" stroke="#f59e0b" stroke-width="2"/>
    <text x="65" y="49" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Condition?</text>
    
    <!-- True/False Exit lines -->
    <line x1="115" y1="45" x2="140" y2="45" stroke="#10b981" stroke-width="2"/>
    <text x="127" y="38" font-size="8" font-weight="bold" fill="#34d399">Yes</text>
    <line x1="65" y1="75" x2="65" y2="95" stroke="#ef4444" stroke-width="2"/>
    <text x="73" y="90" font-size="8" font-weight="bold" fill="#f87171">No</text>

    <text x="160" y="30" font-size="12" font-weight="bold" fill="#fbbf24">4. Decision Diamond</text>
    <text x="160" y="48" font-size="9.5" fill="#94a3b8">Shape: Rhombus / Diamond</text>
    <text x="160" y="70" font-size="9" fill="#cbd5e1"><tspan font-weight="bold" fill="#fde68a">Role:</tspan> Evaluates a Boolean condition (True/False).</text>
    <text x="160" y="88" font-size="8.5" fill="#94a3b8">Pseudocode: <tspan font-family="monospace" fill="#fbbf24">IF ... THEN ... ELSE</tspan>, <tspan font-family="monospace" fill="#fbbf24">WHILE ... DO</tspan></text>
    <text x="15" y="120" font-size="8.5" fill="#fbbf24"><tspan font-weight="bold">&#9888; CRITICAL RULE:</tspan> Must have exactly 1 entry and exactly 2 labeled exits (Yes/No or True/False).</text>
  </g>

  <!-- Symbol 5: Flow Lines & Connectors -->
  <g transform="translate(495, 225)">
    <rect width="420" height="145" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    
    <!-- Connectors Visual -->
    <circle cx="45" cy="45" r="18" fill="#db2777" stroke="#ec4899" stroke-width="2"/>
    <text x="45" y="50" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">A</text>
    
    <polygon points="105,25 125,25 135,45 125,65 105,65" fill="#9d174d" stroke="#f472b6" stroke-width="2"/>
    <text x="117" y="48" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">Pg.2</text>

    <text x="155" y="30" font-size="12" font-weight="bold" fill="#f472b6">5. Connectors &amp; Flow Lines</text>
    <text x="155" y="48" font-size="9.5" fill="#94a3b8">Shapes: Circle (On-Page), Pentagon (Off-Page), Arrows</text>
    <text x="155" y="70" font-size="9" fill="#cbd5e1"><tspan font-weight="bold" fill="#fbcfe8">On-Page Circle:</tspan> Connects sections on same sheet.</text>
    <text x="155" y="88" font-size="9" fill="#cbd5e1"><tspan font-weight="bold" fill="#fbcfe8">Off-Page Shield:</tspan> Links flow across multi-page diagrams.</text>
    <text x="15" y="120" font-size="8.5" fill="#cbd5e1"><tspan font-weight="bold" fill="#f472b6">Flow Direction:</tspan> Strict Top-to-Bottom and Left-to-Right layout convention.</text>
  </g>

  <!-- Summary Footer Table -->
  <g transform="translate(45, 385)">
    <rect width="870" height="100" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="20" y="24" font-size="11" font-weight="bold" fill="#38bdf8">Flowchart Design Principles Quick-Check</text>
    <line x1="20" y1="32" x2="850" y2="32" stroke="#334155" stroke-width="1"/>
    <text x="25" y="52" font-size="9" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#38bdf8">Unambiguous Pathways:</tspan> Flow lines must not intersect without clarity; use connectors to avoid clutter.</text>
    <text x="25" y="70" font-size="9" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#10b981">Single Entrance/Exit:</tspan> Processing and I/O boxes have 1 in, 1 out. Terminal Start has 1 out; Stop has 1 in.</text>
    <text x="25" y="88" font-size="9" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#f59e0b">Infinite Loop Prevention:</tspan> Every decision branch inside a loop must possess a verified path to termination.</text>
  </g>
</svg>
""")

SVG_TRACE_TABLE_EXECUTION = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Dry Run Execution &amp; Trace Table State Transitions (N = 3)</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Manual CPU simulation tracking variable registers, condition evaluations, and console output step-by-step</text>

  <!-- Left: Pseudocode Algorithm Window -->
  <g transform="translate(45, 90)">
    <rect width="330" height="395" rx="10" fill="#000000" stroke="#334155" stroke-width="1.5"/>
    <rect width="330" height="28" rx="8" fill="#1e293b"/>
    <circle cx="20" cy="14" r="5" fill="#ef4444"/>
    <circle cx="35" cy="14" r="5" fill="#f59e0b"/>
    <circle cx="50" cy="14" r="5" fill="#10b981"/>
    <text x="165" y="19" font-size="11" font-weight="bold" fill="#94a3b8" text-anchor="middle">Cumulative Sum Algorithm</text>

    <!-- Monospace Code Lines -->
    <g transform="translate(15, 45)" font-family="monospace" font-size="10">
      <text x="0" y="15" fill="#64748b">1: <tspan fill="#38bdf8">START</tspan></text>
      <text x="0" y="35" fill="#64748b">2:   <tspan fill="#34d399">INPUT</tspan> N</text>
      <text x="0" y="55" fill="#64748b">3:   <tspan fill="#c4b5fd">SET</tspan> sum = 0</text>
      <text x="0" y="75" fill="#64748b">4:   <tspan fill="#c4b5fd">SET</tspan> counter = 1</text>
      <text x="0" y="95" fill="#64748b">5:   <tspan fill="#fbbf24">WHILE</tspan> counter &lt;= N <tspan fill="#fbbf24">DO</tspan></text>
      
      <!-- Highlighted Line 6 -->
      <rect x="-10" y="102" width="310" height="22" rx="4" fill="#0369a1" fill-opacity="0.3" stroke="#38bdf8" stroke-width="1"/>
      <text x="0" y="117" font-weight="bold" fill="#38bdf8">&#9654; 6:     SET sum = sum + counter</text>
      
      <text x="0" y="137" fill="#64748b">7:     <tspan fill="#c4b5fd">SET</tspan> counter = counter + 1</text>
      <text x="0" y="157" fill="#64748b">8:   <tspan fill="#fbbf24">ENDWHILE</tspan></text>
      <text x="0" y="177" fill="#64748b">9:   <tspan fill="#34d399">OUTPUT</tspan> sum</text>
      <text x="0" y="197" fill="#64748b">10: <tspan fill="#38bdf8">END</tspan></text>
    </g>

    <!-- Register Memory Inspector Callout -->
    <g transform="translate(15, 275)">
      <rect width="300" height="105" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#38bdf8">CPU Variable Registers (Active State):</text>
      <rect x="15" y="30" width="80" height="40" rx="4" fill="#0f172a" stroke="#0ea5e9"/>
      <text x="55" y="46" font-size="9" fill="#94a3b8" text-anchor="middle">Register [N]</text>
      <text x="55" y="63" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">3</text>

      <rect x="110" y="30" width="80" height="40" rx="4" fill="#0f172a" stroke="#10b981"/>
      <text x="150" y="46" font-size="9" fill="#94a3b8" text-anchor="middle">Register [sum]</text>
      <text x="150" y="63" font-size="13" font-weight="bold" fill="#34d399" text-anchor="middle">6</text>

      <rect x="205" y="30" width="80" height="40" rx="4" fill="#0f172a" stroke="#f59e0b"/>
      <text x="245" y="46" font-size="9" fill="#94a3b8" text-anchor="middle">Reg [counter]</text>
      <text x="245" y="63" font-size="13" font-weight="bold" fill="#fbbf24" text-anchor="middle">4</text>
      <text x="150" y="92" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Loop Terminated: (4 &lt;= 3 is FALSE) &#8594; Output: 6</text>
    </g>
  </g>

  <!-- Right: Multi-Step Trace Table Matrix -->
  <g transform="translate(395, 90)">
    <rect width="520" height="395" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    
    <!-- Table Header -->
    <rect width="520" height="28" rx="8" fill="#1e293b"/>
    <text x="30" y="19" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Step</text>
    <text x="110" y="19" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Line Executed</text>
    <text x="195" y="19" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">N</text>
    <text x="245" y="19" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">sum</text>
    <text x="295" y="19" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">counter</text>
    <text x="380" y="19" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">counter &lt;= N ?</text>
    <text x="470" y="19" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Output</text>

    <!-- Table Rows -->
    <g font-size="9" fill="#cbd5e1">
      <!-- Row 1 -->
      <line x1="0" y1="50" x2="520" y2="50" stroke="#1e293b"/>
      <text x="30" y="42" text-anchor="middle">1</text>
      <text x="110" y="42" text-anchor="middle">Line 2 (INPUT N)</text>
      <text x="195" y="42" font-weight="bold" fill="#38bdf8" text-anchor="middle">3</text>
      <text x="245" y="42" fill="#64748b" text-anchor="middle">-</text>
      <text x="295" y="42" fill="#64748b" text-anchor="middle">-</text>
      <text x="380" y="42" fill="#64748b" text-anchor="middle">-</text>
      <text x="470" y="42" fill="#64748b" text-anchor="middle">-</text>

      <!-- Row 2 -->
      <line x1="0" y1="74" x2="520" y2="74" stroke="#1e293b"/>
      <text x="30" y="66" text-anchor="middle">2, 3</text>
      <text x="110" y="66" text-anchor="middle">Line 3, 4 (Init)</text>
      <text x="195" y="66" text-anchor="middle">3</text>
      <text x="245" y="66" font-weight="bold" fill="#34d399" text-anchor="middle">0</text>
      <text x="295" y="66" font-weight="bold" fill="#fbbf24" text-anchor="middle">1</text>
      <text x="380" y="66" fill="#64748b" text-anchor="middle">-</text>
      <text x="470" y="66" fill="#64748b" text-anchor="middle">-</text>

      <!-- Row 3: Pass 1 -->
      <line x1="0" y1="110" x2="520" y2="110" stroke="#1e293b"/>
      <text x="30" y="95" text-anchor="middle">4..6</text>
      <text x="110" y="90" text-anchor="middle">Pass 1: Lines 5,6,7</text>
      <text x="110" y="103" font-size="8" fill="#94a3b8" text-anchor="middle">sum=0+1, cnt=1+1</text>
      <text x="195" y="95" text-anchor="middle">3</text>
      <text x="245" y="95" font-weight="bold" fill="#34d399" text-anchor="middle">1</text>
      <text x="295" y="95" font-weight="bold" fill="#fbbf24" text-anchor="middle">2</text>
      <text x="380" y="95" fill="#34d399" text-anchor="middle">True (1 &lt;= 3)</text>
      <text x="470" y="95" fill="#64748b" text-anchor="middle">-</text>

      <!-- Row 4: Pass 2 -->
      <line x1="0" y1="150" x2="520" y2="150" stroke="#1e293b"/>
      <text x="30" y="135" text-anchor="middle">7..9</text>
      <text x="110" y="130" text-anchor="middle">Pass 2: Lines 5,6,7</text>
      <text x="110" y="143" font-size="8" fill="#94a3b8" text-anchor="middle">sum=1+2, cnt=2+1</text>
      <text x="195" y="135" text-anchor="middle">3</text>
      <text x="245" y="135" font-weight="bold" fill="#34d399" text-anchor="middle">3</text>
      <text x="295" y="135" font-weight="bold" fill="#fbbf24" text-anchor="middle">3</text>
      <text x="380" y="135" fill="#34d399" text-anchor="middle">True (2 &lt;= 3)</text>
      <text x="470" y="135" fill="#64748b" text-anchor="middle">-</text>

      <!-- Row 5: Pass 3 (Highlighted Glowing Row) -->
      <rect x="0" y="152" width="520" height="42" fill="#065f46" fill-opacity="0.3"/>
      <line x1="0" y1="195" x2="520" y2="195" stroke="#10b981"/>
      <text x="30" y="177" font-weight="bold" fill="#34d399" text-anchor="middle">10..12</text>
      <text x="110" y="172" font-weight="bold" fill="#34d399" text-anchor="middle">Pass 3: Lines 5,6,7</text>
      <text x="110" y="186" font-size="8" fill="#6ee7b7" text-anchor="middle">sum=3+3, cnt=3+1</text>
      <text x="195" y="177" text-anchor="middle">3</text>
      <text x="245" y="177" font-weight="bold" fill="#34d399" text-anchor="middle">6</text>
      <text x="295" y="177" font-weight="bold" fill="#fbbf24" text-anchor="middle">4</text>
      <text x="380" y="177" fill="#34d399" text-anchor="middle">True (3 &lt;= 3)</text>
      <text x="470" y="177" fill="#64748b" text-anchor="middle">-</text>

      <!-- Row 6: Exit Loop -->
      <line x1="0" y1="230" x2="520" y2="230" stroke="#1e293b"/>
      <text x="30" y="215" text-anchor="middle">13</text>
      <text x="110" y="215" text-anchor="middle">Line 5 (WHILE check)</text>
      <text x="195" y="215" text-anchor="middle">3</text>
      <text x="245" y="215" text-anchor="middle">6</text>
      <text x="295" y="215" text-anchor="middle">4</text>
      <text x="380" y="215" font-weight="bold" fill="#f87171" text-anchor="middle">False (4 &lt;= 3)</text>
      <text x="470" y="215" fill="#64748b" text-anchor="middle">-</text>

      <!-- Row 7: Output & Terminate -->
      <line x1="0" y1="270" x2="520" y2="270" stroke="#1e293b"/>
      <text x="30" y="255" text-anchor="middle">14, 15</text>
      <text x="110" y="255" font-weight="bold" fill="#38bdf8" text-anchor="middle">Line 9, 10 (OUTPUT/END)</text>
      <text x="195" y="255" text-anchor="middle">3</text>
      <text x="245" y="255" text-anchor="middle">6</text>
      <text x="295" y="255" text-anchor="middle">4</text>
      <text x="380" y="255" fill="#64748b" text-anchor="middle">-</text>
      <text x="470" y="255" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">6</text>
    </g>

    <!-- Verification Check Callout Box -->
    <g transform="translate(15, 290)">
      <rect width="490" height="90" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
      <text x="20" y="22" font-size="11" font-weight="bold" fill="#34d399">&#10003; Verification Result: Algorithm Logic Verified Correct</text>
      <text x="20" y="42" font-size="9" fill="#cbd5e1">&#8226; Formula Expected: 1 + 2 + 3 = 6</text>
      <text x="20" y="58" font-size="9" fill="#cbd5e1">&#8226; Trace Output: Exactly 6 produced after 3 complete iterations</text>
      <text x="20" y="74" font-size="9" fill="#cbd5e1">&#8226; Loop Counter successfully reached 4, cleanly breaking the condition (4 &lt;= 3) without an infinite loop</text>
    </g>
  </g>
</svg>
""")

SVG_TEST_DATA_SPECTRUM = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Test Data Spectrum: Normal, Boundary &amp; Invalid Categories</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Systematic input partition testing for a School Grading System (Valid Range: 0 to 100 | Pass Threshold: &gt;= 50)</text>

  <!-- Number Line Visual -->
  <g transform="translate(50, 100)">
    <!-- Invalid Zone Left -->
    <rect x="0" y="20" width="160" height="50" rx="6" fill="#7f1d1d" fill-opacity="0.4" stroke="#ef4444" stroke-width="1.5"/>
    <text x="80" y="43" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">INVALID DATA</text>
    <text x="80" y="58" font-size="9" fill="#fca5a5" text-anchor="middle">Score &lt; 0 (e.g., -15, -1)</text>

    <!-- Boundary Marker 0 -->
    <circle cx="160" cy="45" r="9" fill="#f59e0b" stroke="#ffffff" stroke-width="2"/>
    <text x="160" y="85" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">0 (Edge)</text>

    <!-- Normal Fail Zone (1 - 48) -->
    <rect x="160" y="20" width="220" height="50" fill="#1e293b" stroke="#0ea5e9" stroke-width="1.5"/>
    <text x="270" y="43" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">NORMAL DATA (Fail)</text>
    <text x="270" y="58" font-size="9" fill="#94a3b8" text-anchor="middle">1 to 48 (e.g., 25, 32)</text>

    <!-- Boundary Pair: 49 & 50 -->
    <circle cx="380" cy="45" r="9" fill="#f59e0b" stroke="#ffffff" stroke-width="2"/>
    <text x="380" y="85" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">49 (Fail)</text>
    <line x1="380" y1="20" x2="380" y2="70" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3"/>

    <circle cx="430" cy="45" r="9" fill="#f59e0b" stroke="#ffffff" stroke-width="2"/>
    <text x="430" y="85" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">50 (Pass)</text>

    <!-- Normal Pass Zone (51 - 99) -->
    <rect x="430" y="20" width="270" height="50" fill="#064e3b" fill-opacity="0.4" stroke="#10b981" stroke-width="1.5"/>
    <text x="565" y="43" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">NORMAL DATA (Pass)</text>
    <text x="565" y="58" font-size="9" fill="#a7f3d0" text-anchor="middle">51 to 99 (e.g., 75, 88)</text>

    <!-- Boundary Marker 100 -->
    <circle cx="700" cy="45" r="9" fill="#f59e0b" stroke="#ffffff" stroke-width="2"/>
    <text x="700" y="85" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">100 (Edge)</text>

    <!-- Invalid Zone Right -->
    <rect x="700" y="20" width="160" height="50" rx="6" fill="#7f1d1d" fill-opacity="0.4" stroke="#ef4444" stroke-width="1.5"/>
    <text x="780" y="43" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">INVALID DATA</text>
    <text x="780" y="58" font-size="9" fill="#fca5a5" text-anchor="middle">Score &gt; 100 / Text "A"</text>
  </g>

  <!-- Detail Cards (3 Columns) -->
  <g transform="translate(45, 210)">
    <!-- 1. Normal Data Card -->
    <g transform="translate(0, 0)">
      <rect width="275" height="270" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
      <rect width="275" height="28" rx="8" fill="#059669"/>
      <text x="137" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Normal (Valid) Data</text>
      
      <text x="15" y="50" font-size="10" font-weight="bold" fill="#34d399">&#8226; Definition:</text>
      <text x="15" y="68" font-size="9" fill="#cbd5e1">Standard expected values lying well within operational bounds.</text>
      
      <text x="15" y="98" font-size="10" font-weight="bold" fill="#34d399">&#8226; Grading Examples:</text>
      <text x="15" y="116" font-size="9" fill="#cbd5e1">- Score = <tspan font-family="monospace" fill="#38bdf8">75</tspan> &#8594; Output: <tspan font-weight="bold" fill="#34d399">"Pass"</tspan></text>
      <text x="15" y="134" font-size="9" fill="#cbd5e1">- Score = <tspan font-family="monospace" fill="#38bdf8">32</tspan> &#8594; Output: <tspan font-weight="bold" fill="#f87171">"Fail"</tspan></text>
      
      <text x="15" y="164" font-size="10" font-weight="bold" fill="#34d399">&#8226; Test Purpose:</text>
      <text x="15" y="182" font-size="8.5" fill="#94a3b8">Validates primary functional business logic under ordinary everyday conditions.</text>

      <rect x="15" y="205" width="245" height="50" rx="6" fill="#1e293b"/>
      <text x="25" y="224" font-size="8.5" font-weight="bold" fill="#34d399">&#10003; Target Behavior:</text>
      <text x="25" y="240" font-size="8" fill="#cbd5e1">Calculates and produces correct Pass/Fail status without warnings.</text>
    </g>

    <!-- 2. Boundary Data Card -->
    <g transform="translate(295, 0)">
      <rect width="280" height="270" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
      <rect width="280" height="28" rx="8" fill="#d97706"/>
      <text x="140" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Boundary (Edge) Data</text>
      
      <text x="15" y="50" font-size="10" font-weight="bold" fill="#fbbf24">&#8226; Definition:</text>
      <text x="15" y="68" font-size="9" fill="#cbd5e1">Values sitting exactly on upper/lower limits of allowable partitions.</text>
      
      <text x="15" y="98" font-size="10" font-weight="bold" fill="#fbbf24">&#8226; Critical Edge Values:</text>
      <text x="15" y="116" font-size="9" fill="#cbd5e1">- Score = <tspan font-family="monospace" fill="#fbbf24">50</tspan> &#8594; <tspan font-weight="bold" fill="#34d399">"Pass"</tspan> (Min Pass)</text>
      <text x="15" y="134" font-size="9" fill="#cbd5e1">- Score = <tspan font-family="monospace" fill="#fbbf24">49</tspan> &#8594; <tspan font-weight="bold" fill="#f87171">"Fail"</tspan> (Max Fail)</text>
      <text x="15" y="152" font-size="9" fill="#cbd5e1">- Score = <tspan font-family="monospace" fill="#fbbf24">0</tspan> &amp; <tspan font-family="monospace" fill="#fbbf24">100</tspan> &#8594; Absolute Edges</text>
      
      <text x="15" y="180" font-size="10" font-weight="bold" fill="#fbbf24">&#8226; Primary Bug Caught:</text>
      <text x="15" y="198" font-size="8.5" fill="#94a3b8">Off-by-one errors (e.g., using `&gt; 50` instead of `&gt;= 50`).</text>

      <rect x="15" y="215" width="250" height="40" rx="6" fill="#1e293b"/>
      <text x="25" y="232" font-size="8.5" font-weight="bold" fill="#fbbf24">&#9888; Key Verification:</text>
      <text x="25" y="246" font-size="8" fill="#cbd5e1">Ensures exact threshold score 50 passes.</text>
    </g>

    <!-- 3. Invalid Data Card -->
    <g transform="translate(595, 0)">
      <rect width="275" height="270" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
      <rect width="275" height="28" rx="8" fill="#dc2626"/>
      <text x="137" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Invalid (Erroneous) Data</text>
      
      <text x="15" y="50" font-size="10" font-weight="bold" fill="#f87171">&#8226; Definition:</text>
      <text x="15" y="68" font-size="9" fill="#cbd5e1">Out-of-range, negative, or wrong data types completely outside specs.</text>
      
      <text x="15" y="98" font-size="10" font-weight="bold" fill="#f87171">&#8226; Erroneous Inputs:</text>
      <text x="15" y="116" font-size="9" fill="#cbd5e1">- Score = <tspan font-family="monospace" fill="#f87171">-1</tspan> &#8594; "Error: Out of bounds"</text>
      <text x="15" y="134" font-size="9" fill="#cbd5e1">- Score = <tspan font-family="monospace" fill="#f87171">105</tspan> &#8594; "Error: Out of bounds"</text>
      <text x="15" y="152" font-size="9" fill="#cbd5e1">- Score = <tspan font-family="monospace" fill="#f87171">"eighty"</tspan> &#8594; "Invalid Type"</text>
      
      <text x="15" y="180" font-size="10" font-weight="bold" fill="#f87171">&#8226; Test Purpose:</text>
      <text x="15" y="198" font-size="8.5" fill="#94a3b8">Validates defensive input sanitization and error handling routines.</text>

      <rect x="15" y="215" width="245" height="40" rx="6" fill="#1e293b"/>
      <text x="25" y="232" font-size="8.5" font-weight="bold" fill="#f87171">&#9760; Robustness Requirement:</text>
      <text x="25" y="246" font-size="8" fill="#cbd5e1">System must reject bad data without crashing.</text>
    </g>
  </g>
</svg>
""")

SVG_TRAFFIC_LIGHT_ALGORITHM = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Nairobi Smart Pedestrian Traffic Coordinator: State Machine Flow</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Algorithmic timing sequence managing vehicular flow and pedestrian crossing safety</text>

  <!-- State 1: Default State -->
  <g transform="translate(50, 100)">
    <rect width="180" height="150" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <rect width="180" height="26" rx="8" fill="#059669"/>
    <text x="90" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">State 1: Default Flow</text>
    
    <!-- Vehicle Light Graphic -->
    <rect x="15" y="38" width="40" height="95" rx="6" fill="#1e293b" stroke="#334155"/>
    <circle cx="35" cy="53" r="8" fill="#334155"/>
    <circle cx="35" cy="73" r="8" fill="#334155"/>
    <circle cx="35" cy="93" r="8" fill="#10b981"/> <!-- Green ON -->
    <text x="23" y="125" font-size="7" fill="#34d399">VEHICLE</text>

    <!-- Pedestrian Light Graphic -->
    <rect x="65" y="38" width="40" height="95" rx="6" fill="#1e293b" stroke="#334155"/>
    <circle cx="85" cy="58" r="9" fill="#ef4444"/> <!-- Red ON -->
    <circle cx="85" cy="88" r="9" fill="#334155"/>
    <text x="75" y="125" font-size="7" fill="#f87171">PED</text>

    <text x="115" y="55" font-size="8.5" font-weight="bold" fill="#34d399">Veh: GREEN</text>
    <text x="115" y="72" font-size="8.5" font-weight="bold" fill="#f87171">Ped: RED</text>
    <text x="115" y="95" font-size="8" fill="#94a3b8">Continuous</text>
    <text x="115" y="108" font-size="8" fill="#94a3b8">polling...</text>
  </g>

  <!-- Button Decision Diamond -->
  <g transform="translate(265, 125)">
    <polygon points="50,0 100,50 50,100 0,50" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="50" y="45" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Button</text>
    <text x="50" y="60" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Pressed?</text>
    
    <!-- No Loop back to State 1 -->
    <path d="M 50,0 C 50,-40 -125,-40 -125,95" fill="none" stroke="#64748b" stroke-width="2"/>
    <polygon points="-128,95 -122,95 -125,102" fill="#64748b"/>
    <text x="55" y="-15" font-size="8" font-weight="bold" fill="#94a3b8">No (Stay)</text>

    <!-- Yes Arrow to State 2 -->
    <line x1="100" y1="50" x2="135" y2="50" stroke="#10b981" stroke-width="2.5"/>
    <polygon points="135,46 143,50 135,54" fill="#10b981"/>
    <text x="118" y="42" font-size="8.5" font-weight="bold" fill="#34d399">Yes</text>
  </g>

  <!-- State 2: Vehicular Warning -->
  <g transform="translate(420, 100)">
    <rect width="160" height="150" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect width="160" height="26" rx="8" fill="#d97706"/>
    <text x="80" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">State 2: Transition</text>
    
    <text x="15" y="50" font-size="9" font-weight="bold" fill="#fbbf24">&#8226; Delay 10 Seconds</text>
    <text x="15" y="68" font-size="8.5" fill="#cbd5e1">(Clear intersection)</text>
    <text x="15" y="90" font-size="9" font-weight="bold" fill="#fbbf24">&#8226; Veh: YELLOW (3s)</text>
    <text x="15" y="108" font-size="9" font-weight="bold" fill="#f87171">&#8226; Ped: RED</text>
    <text x="15" y="130" font-size="8" fill="#94a3b8">Vehicles decelerate</text>
  </g>

  <!-- Arrow State 2 -> State 3 -->
  <g transform="translate(580, 175)">
    <line x1="0" y1="0" x2="35" y2="0" stroke="#f59e0b" stroke-width="2.5"/>
    <polygon points="35,-4 43,0 35,4" fill="#f59e0b"/>
  </g>

  <!-- State 3: Pedestrian Walk -->
  <g transform="translate(625, 100)">
    <rect width="150" height="150" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <rect width="150" height="26" rx="8" fill="#059669"/>
    <text x="75" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">State 3: Safe Walk</text>
    
    <text x="15" y="50" font-size="9" font-weight="bold" fill="#f87171">&#8226; Veh: RED</text>
    <text x="15" y="70" font-size="9" font-weight="bold" fill="#34d399">&#8226; Ped: GREEN</text>
    <text x="15" y="92" font-size="9" fill="#cbd5e1">&#8226; Timer: <tspan font-weight="bold" fill="#38bdf8">20 Seconds</tspan></text>
    <text x="15" y="115" font-size="8" fill="#94a3b8">Safe pedestrian crossing active</text>
  </g>

  <!-- Arrow State 3 -> State 4 -->
  <g transform="translate(775, 175)">
    <line x1="0" y1="0" x2="30" y2="0" stroke="#10b981" stroke-width="2.5"/>
    <polygon points="30,-4 38,0 30,4" fill="#10b981"/>
  </g>

  <!-- State 4: Pedestrian Warning Flashing -->
  <g transform="translate(790, 100)">
    <rect width="125" height="150" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect width="125" height="26" rx="8" fill="#dc2626"/>
    <text x="62" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">State 4: Flash</text>
    <text x="10" y="50" font-size="8.5" font-weight="bold" fill="#f87171">&#8226; Ped: FLASH RED</text>
    <text x="10" y="70" font-size="8.5" fill="#cbd5e1">&#8226; 5 Seconds</text>
    <text x="10" y="90" font-size="8" fill="#94a3b8">Warning: Finish crossing</text>
    <text x="10" y="115" font-size="8.5" font-weight="bold" fill="#f87171">&#8226; Veh: RED</text>
  </g>

  <!-- Reset Loop Arrow back to State 1 -->
  <path d="M 852,250 C 852,320 140,320 140,255" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="5,4"/>
  <polygon points="136,255 144,255 140,248" fill="#38bdf8"/>

  <!-- Code Logic Callout Table -->
  <g transform="translate(50, 340)">
    <rect width="860" height="145" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="20" y="24" font-size="11" font-weight="bold" fill="#38bdf8">Algorithmic Pseudocode Implementation Architecture</text>
    <line x1="20" y1="32" x2="840" y2="32" stroke="#334155" stroke-width="1"/>

    <g font-family="monospace" font-size="9" fill="#cbd5e1">
      <text x="25" y="50"><tspan fill="#38bdf8">WHILE</tspan> system_power == True <tspan fill="#38bdf8">DO</tspan></text>
      <text x="45" y="66"><tspan fill="#c4b5fd">SET</tspan> vehicle_light = "GREEN", pedestrian_light = "RED"</text>
      <text x="45" y="82"><tspan fill="#fbbf24">IF</tspan> READ_BUTTON() == True <tspan fill="#fbbf24">THEN</tspan></text>
      <text x="65" y="98">WAIT(10); <tspan fill="#c4b5fd">SET</tspan> vehicle_light = "YELLOW"; WAIT(3); <tspan fill="#c4b5fd">SET</tspan> vehicle_light = "RED"</text>
      <text x="65" y="114"><tspan fill="#c4b5fd">SET</tspan> pedestrian_light = "GREEN"; WAIT(20); FLASH_RED_PEDESTRIAN(5)</text>
      <text x="45" y="130"><tspan fill="#fbbf24">ENDIF</tspan></text>
      <text x="25" y="142"><tspan fill="#38bdf8">ENDWHILE</tspan></text>
    </g>
  </g>
</svg>
""")

SVG_LAKE_VICTORIA_WATER_MONITOR = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Lake Victoria Smart Water Quality Station: Algorithmic Logic &amp; Decision Tree</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Autonomous embedded microcontroller decision pipeline executing continuous environmental pH analysis</text>

  <!-- Left: Sensor & Station Input -->
  <g transform="translate(45, 95)">
    <rect width="230" height="385" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="230" height="28" rx="8" fill="#0284c7"/>
    <text x="115" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Sensor &amp; Power Inputs</text>

    <!-- Solar Box -->
    <rect x="15" y="40" width="200" height="65" rx="6" fill="#1e293b" stroke="#f59e0b"/>
    <text x="25" y="58" font-size="10" font-weight="bold" fill="#fbbf24">&#9728; Solar Power Subsystem</text>
    <text x="25" y="75" font-size="8.5" fill="#cbd5e1">&#8226; Continuous 24/7 Battery</text>
    <text x="25" y="90" font-size="8.5" fill="#cbd5e1">&#8226; Infinite Monitoring Loop</text>

    <!-- Submerged pH Sensor Box -->
    <rect x="15" y="120" width="200" height="110" rx="6" fill="#1e293b" stroke="#0ea5e9"/>
    <text x="25" y="138" font-size="10" font-weight="bold" fill="#38bdf8">&#9875; Submerged pH Probe</text>
    <text x="25" y="156" font-size="8.5" fill="#cbd5e1">&#8226; Sampling: 1 Sample / Minute</text>
    <text x="25" y="172" font-size="8.5" fill="#cbd5e1">&#8226; Physics Range: 0.0 to 14.0</text>
    <text x="25" y="188" font-size="8.5" fill="#cbd5e1">&#8226; 7.0 = Pure Neutral Water</text>
    <rect x="25" y="200" width="180" height="20" rx="4" fill="#0f172a"/>
    <text x="115" y="214" font-family="monospace" font-size="9" fill="#38bdf8" text-anchor="middle">INPUT current_pH</text>

    <!-- System Requirements Specs -->
    <rect x="15" y="245" width="200" height="120" rx="6" fill="#1e293b"/>
    <text x="25" y="265" font-size="9.5" font-weight="bold" fill="#34d399">Requirement Bounds:</text>
    <text x="25" y="285" font-size="8.5" fill="#cbd5e1">&#8226; Safe Zone: [6.5, 8.5]</text>
    <text x="25" y="303" font-size="8.5" fill="#f87171">&#8226; Acid Alert: &lt; 6.5</text>
    <text x="25" y="321" font-size="8.5" fill="#a78bfa">&#8226; Alkaline Alert: &gt; 8.5</text>
    <text x="25" y="339" font-size="8.5" fill="#ef4444">&#8226; Fault: &lt; 0.0 OR &gt; 14.0</text>
  </g>

  <!-- Arrow Input -> Decision Tree -->
  <g transform="translate(275, 230)">
    <line x1="0" y1="0" x2="35" y2="0" stroke="#38bdf8" stroke-width="2.5"/>
    <polygon points="35,-4 43,0 35,4" fill="#38bdf8"/>
  </g>

  <!-- Middle: Multi-Tier Decision Tree -->
  <g transform="translate(320, 95)">
    <rect width="320" height="385" rx="10" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect width="320" height="28" rx="8" fill="#7c3aed"/>
    <text x="160" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Algorithmic Multi-Way Logic</text>

    <!-- Tier 1: Hardware Fault Check (Highest Priority) -->
    <rect x="15" y="40" width="290" height="70" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="25" y="58" font-size="10" font-weight="bold" fill="#f87171">Tier 1: Physical Sensor Fault</text>
    <text x="25" y="74" font-family="monospace" font-size="8.5" fill="#fca5a5">IF current_pH &lt; 0.0 OR &gt; 14.0</text>
    <text x="25" y="92" font-size="8" fill="#cbd5e1">&#8594; Hardware out-of-voltage / severed cable</text>

    <!-- Tier 2: Safe Range Check -->
    <rect x="15" y="125" width="290" height="70" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="25" y="143" font-size="10" font-weight="bold" fill="#34d399">Tier 2: Safe Water Quality</text>
    <text x="25" y="159" font-family="monospace" font-size="8.5" fill="#a7f3d0">ELSEIF pH &gt;= 6.5 AND pH &lt;= 8.5</text>
    <text x="25" y="177" font-size="8" fill="#cbd5e1">&#8594; Healthy aquatic life &amp; municipal water</text>

    <!-- Tier 3: Acidic Hazard Check -->
    <rect x="15" y="210" width="290" height="70" rx="6" fill="#1e293b" stroke="#f59e0b"/>
    <text x="25" y="228" font-size="10" font-weight="bold" fill="#fbbf24">Tier 3: Acid Contamination</text>
    <text x="25" y="244" font-family="monospace" font-size="8.5" fill="#fde68a">ELSEIF current_pH &lt; 6.5</text>
    <text x="25" y="262" font-size="8" fill="#cbd5e1">&#8594; Chemical runoff / acid precipitation</text>

    <!-- Tier 4: Alkaline Hazard Check -->
    <rect x="15" y="295" width="290" height="70" rx="6" fill="#1e293b" stroke="#a855f7"/>
    <text x="25" y="313" font-size="10" font-weight="bold" fill="#c084fc">Tier 4: Alkaline Contamination</text>
    <text x="25" y="329" font-family="monospace" font-size="8.5" fill="#e9d5ff">ELSE (pH &gt; 8.5)</text>
    <text x="25" y="347" font-size="8" fill="#cbd5e1">&#8594; Industrial discharge / detergent spill</text>
  </g>

  <!-- Arrow Decision -> Actuators -->
  <g transform="translate(640, 230)">
    <line x1="0" y1="0" x2="35" y2="0" stroke="#8b5cf6" stroke-width="2.5"/>
    <polygon points="35,-4 43,0 35,4" fill="#8b5cf6"/>
  </g>

  <!-- Right: Outputs & Actuators -->
  <g transform="translate(685, 95)">
    <rect width="230" height="385" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="230" height="28" rx="8" fill="#059669"/>
    <text x="115" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Actions &amp; Telemetry</text>

    <!-- Actuator 1: Display Output -->
    <rect x="15" y="40" width="200" height="85" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="25" y="58" font-size="10" font-weight="bold" fill="#38bdf8">&#128435; Station LCD Screen</text>
    <text x="25" y="76" font-size="8.5" fill="#cbd5e1">&#8226; "Water Quality: Safe"</text>
    <text x="25" y="92" font-size="8.5" fill="#f87171">&#8226; "Alert: High Acid Content!"</text>
    <text x="25" y="108" font-size="8.5" fill="#a78bfa">&#8226; "Alert: High Alkaline Content!"</text>

    <!-- Actuator 2: Physical Valve & Siren -->
    <rect x="15" y="140" width="200" height="110" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="25" y="158" font-size="10" font-weight="bold" fill="#f87171">&#9888; Physical Protection Actuators</text>
    <text x="25" y="176" font-size="8.5" fill="#cbd5e1">&#8226; Trigger Emergency Siren</text>
    <text x="25" y="192" font-size="8.5" fill="#cbd5e1">&#8226; Close Water Intake Valve</text>
    <text x="25" y="208" font-size="8.5" fill="#cbd5e1">&#8226; Transmit GSM Cellular SMS to Lake Basin Authority</text>
    <rect x="25" y="222" width="180" height="18" rx="3" fill="#0f172a"/>
    <text x="115" y="234" font-size="8" fill="#f87171" text-anchor="middle">ACTUATE_SHUTDOWN()</text>

    <!-- Test Suite Confirmation -->
    <rect x="15" y="265" width="200" height="100" rx="6" fill="#1e293b"/>
    <text x="25" y="285" font-size="9.5" font-weight="bold" fill="#34d399">5-Case Test Suite Verified:</text>
    <text x="25" y="303" font-size="8" fill="#cbd5e1">TC-01: pH 7.2 &#8594; Safe (Normal)</text>
    <text x="25" y="318" font-size="8" fill="#cbd5e1">TC-02: pH 6.5 &#8594; Safe (Boundary)</text>
    <text x="25" y="333" font-size="8" fill="#cbd5e1">TC-03: pH 4.2 &#8594; Acid Alert</text>
    <text x="25" y="348" font-size="8" fill="#cbd5e1">TC-04: pH 9.8 &#8594; Alkaline Alert</text>
    <text x="25" y="363" font-size="8" fill="#f87171">TC-05: pH -2.0 &#8594; Fault Warning</text>
  </g>
</svg>
""")

# =====================================================================
# CURRICULUM DATA DEFINITION FOR TOPIC 13
# =====================================================================

def build_topic13_curriculum():
    return [
        # -----------------------------------------------------------------
        # UNIT 1: THE PROGRAM DEVELOPMENT CYCLE & REQUIREMENTS ANALYSIS
        # -----------------------------------------------------------------
        {
            "unit_order": 1,
            "unit_name": "The Program Development Cycle (PDC) and Requirements Analysis",
            "unit_description": "Comprehensive introduction to the engineering methodology of software construction: the architectural blueprint analogy, core definitions (stakeholders, requirements, constraints, success criteria), the six iterative stages of the Program Development Cycle (PDC), and the feedback loop for continuous refinement.",
            "lesson_title": "The Program Development Cycle (PDC) and Requirements",
            "pages": [
                # Page 1: Introduction & Architectural Analogy
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Foundations of the Program Development Cycle",
                        "content": {
                            "goal": "Understand why programming is an engineering discipline requiring systematic planning, and define the core concepts of stakeholders, system requirements, constraints, and success criteria."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Introduction & The 'Architectural Blueprint' Analogy",
                        "content": {
                            "markdown": """### **The 'Architectural Blueprint' Analogy**
Imagine a city planning committee that commissions a modern multi-story public library. If the construction foreman immediately orders trucks of concrete and starts laying bricks on day one without architectural blueprints, what will happen?
- Doors will open into solid brick walls.
- High-voltage electrical wiring will collide with water drainage pipes.
- The foundation will buckle under uncalculated structural weight, causing the entire building to collapse.

To build a safe, durable, and functional structure, the architect must first:
1. **Interview community members and city officials** to establish capacity and service needs.
2. **Survey the physical terrain** to assess bedrock depth and drainage slopes.
3. **Draft detailed structural schematics and 3D architectural blueprints**.
4. **Submit designs to safety inspectors and structural engineers** for rigorous peer review.
5. **Only then pour concrete and lay bricks** according to exact engineering tolerances.

```
[ Problem Analysis ] ➔ [ Blueprint Design ] ➔ [ Construction ] ➔ [ Inspection ] ➔ [ Commissioning ]
```

### **Programming as an Engineering Discipline**
In computer science, **writing code immediately in an IDE without planning is like laying bricks without a blueprint**. 

Computer programming is not simply typing syntax into a compiler; it is an engineering discipline that demands systematic problem decomposition, language-independent algorithm design, manual logic verification, and rigorous testing before a single line of production code is compiled.

The **Program Development Cycle (PDC)** is our architectural sequence. It provides a structured, multi-stage roadmap to transform real-world user problems into reliable, efficient, and maintainable software solutions.

---

### **Core Definitions**
Before designing software systems, systems analysts and software engineers rely on a standardized vocabulary:

- **Program Development Cycle (PDC)**: A structured, multi-stage methodology followed by software developers to analyze, design, implement, verify, document, and maintain computer programs throughout their operational lifespan.
- **Stakeholder**: Any individual or organization who is affected by, interested in, or has a direct say in the outcome of a software project (such as clients, end-users, system administrators, or business managers).
- **System Requirement**: A specific condition, capability, or functional behavior that a software application must possess to fulfill a stakeholder's practical need.
- **Constraint**: A limitation or boundary restriction imposed on the software project, such as system memory limits, CPU processing speed, display resolutions, battery consumption, network bandwidth, regulatory compliance, or financial budgets.
- **Success Criteria**: The explicit, measurable benchmarks and standards used to objectively determine whether the delivered program successfully solves the original problem."""
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Architectural Blueprints in Software",
                        "content": {
                            "text": "Writing code without an algorithm is like building without a blueprint. The Program Development Cycle (PDC) ensures software is systematically analyzed, designed, coded, verified, documented, and maintained."
                        }
                    }
                ],

                # Page 2: The Six Stages of the PDC
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: The Six Stages of the Program Development Cycle",
                        "content": {
                            "goal": "Analyze each of the six iterative stages of the Program Development Cycle (Problem Definition, Design, Coding, Testing, Documentation, Maintenance) and their specific inputs, outputs, and feedback loops."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Six Stages of the Program Development Cycle (PDC)",
                        "content": {
                            "markdown": """### **The Six Stages of the Program Development Cycle**
The Program Development Cycle consists of six distinct, sequential yet iterative phases. When an error is uncovered during later stages, developers feed lessons learned back into earlier stages to refine the design.

```
                      +-----------------------------------+
                      | 1. PROBLEM DEFINITION & REQS     | <----+
                      +-----------------------------------+      |
                                        |                        |
                                        v                        |
                      +-----------------------------------+      |
                      | 2. PROGRAM DESIGN (ALGORITHMS)   |       |
                      +-----------------------------------+      |
                                        |                        |
                                        v                        |
                      +-----------------------------------+      |
                      | 3. CODING (IMPLEMENTATION)        |       | Feedback
                      +-----------------------------------+      | Loop for
                                        |                        | Continuous
                                        v                        | Refinement
                      +-----------------------------------+      |
                      | 4. TESTING & DEBUGGING            | ------+
                      +-----------------------------------+
                                        |
                                        v
                      +-----------------------------------+
                      | 5. SYSTEM DOCUMENTATION           |
                      +-----------------------------------+
                                        |
                                        v
                      +-----------------------------------+
                      | 6. SYSTEM MAINTENANCE             |
                      +-----------------------------------+
```

---

#### **Stage 1: Problem Definition and Requirements Analysis**
- **Objective**: Clearly understand the exact nature of the problem, identify all available inputs, determine the required outputs, and establish environmental constraints.
- **Process**: Developers interview stakeholders, observe business workflows, and compile a formal **Software Requirements Specification (SRS)** document.
- **Rectangle Area Case Study**: 
  - *Problem*: Calculate the surface area of rectangular floor spaces.
  - *Inputs*: Length ($l$) and Width ($w$) as positive floating-point numbers.
  - *Output*: Calculated surface area ($area$).
  - *Constraint*: Length and width must strictly be numbers greater than zero.

---

#### **Stage 2: Program Design (Algorithm Design)**
- **Objective**: Formulate the step-by-step logical sequence required to solve the problem, completely independent of the syntax of any specific programming language.
- **Process**: Software architects model logic using **pseudocode** (structured human-readable text) and **flowcharts** (standard geometric diagrams), verifying the logic manually with paper-based **trace tables** (dry runs).
- **Rectangle Area Case Study**:
  ```text
  START
      INPUT length
      INPUT width
      SET area = length * width
      OUTPUT area
  END
  ```

---

#### **Stage 3: Coding (Implementation)**
- **Objective**: Translate the verified algorithm design into executable source code using a chosen high-level programming language inside an Integrated Development Environment (IDE).
- **Process**: Programmers write clean, syntactically correct code, adhering to language-specific grammar, data types, and naming conventions.
- **Rectangle Area Case Study** (Python):
  ```python
  length = float(input("Enter rectangle length: "))
  width = float(input("Enter rectangle width: "))
  area = length * width
  print(f"Calculated Area = {area:.2f} sq units")
  ```

---

#### **Stage 4: Testing and Debugging**
- **Objective**: Run the program with diverse test datasets to ensure it executes without crashing, produces mathematically correct results, handles illegal user input gracefully, and satisfies all SRS requirements.
- **Process**: Developers execute test suites containing **Normal Data**, **Boundary Data**, and **Invalid Data**, isolating and repairing **syntax errors**, **logic errors**, and **runtime crashes**.
- **Rectangle Area Case Study**:
  - *Normal Data*: $l=5, w=10 \rightarrow \text{Output: } 50$ (Pass).
  - *Boundary Data*: $l=0.01, w=0.01 \rightarrow \text{Output: } 0.0001$ (Pass).
  - *Invalid Data*: $l=-5, w=10 \rightarrow \text{System displays: "Error: Dimensions must be positive"}$ (Pass).

---

#### **Stage 5: System Documentation**
- **Objective**: Produce readable guides and reference manuals explaining how the system is structured internally for software maintainers and how to operate it externally for end-users.
- **Process**: 
  - **Internal Documentation**: Meaningful variable identifiers (`length`, `area`), explanatory comments (`# Calculate area in square meters`), and indentation.
  - **External Documentation**: Comprehensive User Manuals (installation, configuration, troubleshooting) and Technical Architecture Guides (system diagrams, data dictionaries).

---

#### **Stage 6: System Maintenance**
- **Objective**: Ensure the software continues to operate reliably over its multi-year operational lifetime by fixing discovered defects, adapting to new operating systems or hardware, and adding requested features.
- **Process**:
  - **Corrective Maintenance**: Fixing latent bugs reported by end-users.
  - **Adaptive Maintenance**: Updating code to support new OS versions, security protocols, or database engines.
  - **Perfective Maintenance**: Adding new capabilities, such as supporting metric/imperial unit conversions or computing rectangle perimeter."""
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: The Six PDC Stages",
                        "content": {
                            "text": "The six PDC stages are: (1) Problem Definition, (2) Program Design, (3) Coding, (4) Testing & Debugging, (5) Documentation, and (6) Maintenance. The feedback loop ensures continuous refinement."
                        }
                    }
                ],

                # Page 3: Visual & Media Anchor
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Visualizing the Lifecycle of Program Development",
                        "content": {
                            "goal": "Visualize the iterative flow of software engineering from initial problem definition to long-term maintenance and external user support."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "The Six Stages of the Program Development Cycle",
                        "content": {
                            "svg_content": SVG_PDC_LIFECYCLE,
                            "caption": "Figure 13.1: The 6-Stage Program Development Cycle (PDC) highlighting stage objectives, deliverables, and the iterative feedback loop between testing/maintenance and initial requirements."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Software Development Life Cycle Architecture",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/SDLC_-_Software_Development_Life_Cycle.jpg/800px-SDLC_-_Software_Development_Life_Cycle.jpg",
                            "caption": "Figure 13.2: Real-world engineering model of the Systems Development Life Cycle (SDLC) used across international software engineering teams.",
                            "author": "Wikimedia Commons / Educational Media",
                            "licensing": "Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)"
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "The Program Development Life Cycle Explained",
                        "content": {
                            "url": "https://www.youtube.com/watch?v=7A_ePz4gq1Y",
                            "youtube_id": "7A_ePz4gq1Y",
                            "description": "Comprehensive educational overview of the Program Development Life Cycle, explaining requirements analysis, pseudocode design, implementation, and quality assurance testing."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Systematic Engineering Over Guesswork",
                        "content": {
                            "text": "Skipping design stages to immediately write code leads to structural defects, higher debugging costs, and failure to satisfy stakeholder expectations."
                        }
                    }
                ],

                # Page 4: Formative Knowledge Check (4 MCQs)
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: PDC Concepts Mastery Assessment",
                        "content": {
                            "goal": "Evaluate your understanding of the Program Development Cycle stages, requirements analysis, constraints, and debugging feedback mechanisms."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "PDC Knowledge Check 1: Stage Sequence",
                        "content": {
                            "question": "Which of the following lists the six stages of the Program Development Cycle (PDC) in their correct logical order?",
                            "options": [
                                "Coding ➔ Testing ➔ Maintenance ➔ Documentation ➔ Design ➔ Problem Definition",
                                "Problem Definition ➔ Program Design ➔ Coding ➔ Testing & Debugging ➔ Documentation ➔ Maintenance",
                                "Program Design ➔ Coding ➔ Testing ➔ Problem Definition ➔ Maintenance ➔ Documentation",
                                "Documentation ➔ Maintenance ➔ Problem Definition ➔ Coding ➔ Testing ➔ Design"
                            ],
                            "correct_answer": "Problem Definition ➔ Program Design ➔ Coding ➔ Testing & Debugging ➔ Documentation ➔ Maintenance",
                            "explanation": "The PDC begins with defining the problem and gathering requirements, followed by designing the algorithm, writing source code, testing/debugging, creating documentation, and ongoing maintenance."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "PDC Knowledge Check 2: System Constraints",
                        "content": {
                            "question": "An app developer is told that a new smartphone application must not consume more than 50 MB of RAM and must run on a battery for at least 8 hours. What term best describes these limitations?",
                            "options": [
                                "Success Criteria",
                                "System Constraints",
                                "Stakeholder Profiles",
                                "Trace Tables"
                            ],
                            "correct_answer": "System Constraints",
                            "explanation": "Constraints are technical, physical, or budgetary boundaries and limitations imposed on the system, such as memory caps, processing limits, or battery life thresholds."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "PDC Knowledge Check 3: Deliverable of Stage 1",
                        "content": {
                            "question": "What is the primary document produced at the conclusion of Stage 1 (Problem Definition and Requirements Analysis)?",
                            "options": [
                                "Machine Code Binary (.exe)",
                                "Software Requirements Specification (SRS)",
                                "External User Installation Guide",
                                "Trace Table Execution Matrix"
                            ],
                            "correct_answer": "Software Requirements Specification (SRS)",
                            "explanation": "The Software Requirements Specification (SRS) is the formal contract created during Stage 1 that defines all stakeholder requirements, inputs, expected outputs, constraints, and success criteria."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "PDC Knowledge Check 4: The Feedback Loop",
                        "content": {
                            "question": "Why is the Program Development Cycle represented as a cyclical process rather than a strictly one-way linear pipeline?",
                            "options": [
                                "Because compilers automatically rewrite algorithms into high-level source code.",
                                "Because bugs, missed edge cases, or changed stakeholder needs discovered during testing and maintenance feed back into earlier stages for refinement.",
                                "Because internal documentation eliminates the need for software testing.",
                                "Because flowcharts can only be drawn in circular shapes."
                            ],
                            "correct_answer": "Because bugs, missed edge cases, or changed stakeholder needs discovered during testing and maintenance feed back into earlier stages for refinement.",
                            "explanation": "Software engineering is iterative: when testing exposes logical errors or when users request enhancements during maintenance, developers must return to problem definition or design to revise the system."
                        }
                    }
                ]
            ]
        },

        # -----------------------------------------------------------------
        # UNIT 2: ALGORITHM REPRESENTATION: PSEUDOCODE & FLOWCHARTS
        # -----------------------------------------------------------------
        {
            "unit_order": 2,
            "unit_name": "Algorithm Design, Standard Pseudocode, and Flowchart Modeling",
            "unit_description": "In-depth exploration of language-independent algorithm design: four fundamental criteria of a quality algorithm (finiteness, definiteness, input/output bounds, effectiveness), standardized uppercase pseudocode keywords, control structures, and geometric flowchart symbol standards.",
            "lesson_title": "Algorithm Design, Standard Pseudocode and Flowchart Modeling",
            "pages": [
                # Page 1: Criteria of a Quality Algorithm & Pseudocode Keywords
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Algorithmic Quality & Standard Pseudocode Conventions",
                        "content": {
                            "goal": "Master the four quality criteria of an algorithm and understand how standardized pseudocode enables language-independent problem-solving."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Criteria of a Quality Algorithm & Pseudocode Conventions",
                        "content": {
                            "markdown": """### **Core Definitions**
- **Algorithm**: A finite, precise, unambiguous, and step-by-step sequence of instructions designed to solve a specific computational problem or perform a calculation.
- **Pseudocode**: A high-level, structured, and informal representation of an algorithm's logical execution that uses programming keywords and indentations formatted for human comprehension rather than direct machine compilation.

---

### **The Four Universal Rules of a Quality Algorithm**
To be considered mathematically valid and practically useful in computer science, every algorithm must satisfy four core criteria:

1. **Finiteness**: The algorithm must guaranteed terminate after a finite number of computational steps. It must never trap the CPU in an infinite loop without an exit condition.
2. **Definiteness (Precision)**: Every single instruction must be clear, unambiguous, and uniquely defined. A computer cannot guess subjective human intent.
3. **Input and Output Bounds**: The algorithm must accept zero or more well-defined inputs and must produce at least one meaningful output.
4. **Effectiveness**: Each step must be basic enough that it can be carried out by a human using paper and pencil in a finite amount of time (desk tracing).

---

### **Standard Capitalized Pseudocode Keywords**
To ensure universal readability across international development teams, computer scientists adhere to standardized uppercase keywords for programmatic control actions:

| Keyword | Category | Purpose | Example Usage |
| :--- | :--- | :--- | :--- |
| **`START` / `BEGIN`** | Boundary | Marks the start of the algorithm | `START` |
| **`INPUT` / `READ`** | Input | Captures data from user or sensor | `INPUT student_mark` |
| **`OUTPUT` / `DISPLAY`** | Output | Displays data onto screen or printer | `DISPLAY "Pass"` |
| **`SET` / `LET`** | Assignment | Assigns value or calculation to variable | `SET total = total + mark` |
| **`IF ... THEN ... ELSE`** | Selection | Conditional branching logic | `IF score >= 50 THEN` |
| **`ENDIF`** | Selection Limit | Marks boundary of selection structure | `ENDIF` |
| **`WHILE ... DO`** | Iteration | Pre-condition loop; repeats while True | `WHILE count <= 10 DO` |
| **`ENDWHILE`** | Loop Limit | Marks boundary of while loop | `ENDWHILE` |
| **`FOR ... TO ... STEP`** | Iteration | Count-controlled definite loop | `FOR i = 1 TO 10 STEP 1` |
| **`ENDFOR`** | Loop Limit | Marks boundary of for loop | `ENDFOR` |
| **`END` / `STOP`** | Boundary | Marks the termination of the algorithm | `END` |"""
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Algorithm Rigor and Pseudocode",
                        "content": {
                            "text": "Quality algorithms must be finite, definite, bounded, and effective. Standard uppercase keywords (START, INPUT, OUTPUT, SET, IF, WHILE, END) structure logic cleanly without language syntax constraints."
                        }
                    }
                ],

                # Page 2: Pseudocode Implementation Examples & Conversion Matrix
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Designing Structured Pseudocode Algorithms",
                        "content": {
                            "goal": "Construct structured pseudocode algorithms for selection and iteration problems, and map natural language statements to pseudocode instructions."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Pseudocode Implementation Examples & Conversion Matrix",
                        "content": {
                            "markdown": r"""### **Natural Language to Pseudocode Conversion Matrix**
Transforming informal problem statements into structured pseudocode requires mapping everyday language directly to capitalized control keywords:

| Everyday Natural Language Statement | Standard Pseudocode Equivalent | Control Category |
| :--- | :--- | :--- |
| "Prompt the user for their age and store it" | `INPUT age` | Input Operation |
| "Compute the average by dividing sum by count" | `SET average = sum / count` | Process / Assignment |
| "Check if the score is at least 50; if so pass, otherwise fail" | `IF score >= 50 THEN`<br>&nbsp;&nbsp;&nbsp;&nbsp;`OUTPUT "Pass"`<br>`ELSE`<br>&nbsp;&nbsp;&nbsp;&nbsp;`OUTPUT "Fail"`<br>`ENDIF` | Selection Structure |
| "Repeat adding numbers until the counter exceeds 100" | `WHILE counter <= 100 DO`<br>&nbsp;&nbsp;&nbsp;&nbsp;`SET sum = sum + counter`<br>&nbsp;&nbsp;&nbsp;&nbsp;`SET counter = counter + 1`<br>`ENDWHILE` | Iteration Structure |
| "Print the final calculated tax to the screen" | `DISPLAY calculated_tax` | Output Operation |

---

### **Standard Algorithm Examples**

#### **Example A: Selection Logic — Finding the Larger of Two Numbers**
```text
START
    INPUT number1
    INPUT number2
    IF number1 > number2 THEN
        OUTPUT number1
    ELSE
        OUTPUT number2
    ENDIF
END
```

#### **Example B: Iterative Logic — Cumulative Sum from 1 to N**
```text
START
    INPUT N
    SET sum = 0
    SET counter = 1
    WHILE counter <= N DO
        SET sum = sum + counter
        SET counter = counter + 1
    ENDWHILE
    OUTPUT sum
END
```

*Explanation of Cumulative Sum*:
1. The user provides a positive boundary integer $N$ (e.g., $N=3$).
2. An accumulator variable `sum` is initialized to $0$.
3. A loop index variable `counter` is initialized to $1$.
4. The `WHILE` condition evaluates `counter <= N`. As long as this is True, the loop body adds `counter` to `sum` and increments `counter` by $1$.
5. When `counter` exceeds $N$, the loop terminates, and the final value of `sum` ($1 + 2 + \dots + N$) is printed to the screen."""
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Selection vs. Iteration",
                        "content": {
                            "text": "Selection structures (IF-THEN-ELSE) direct control flow along alternative conditional paths. Iteration structures (WHILE-DO, FOR-TO) execute repetitive operations until an exit condition is reached."
                        }
                    }
                ],

                # Page 3: Flowchart Architecture & Standard Symbol Library
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Flowchart Symbology and Design Rules",
                        "content": {
                            "goal": "Identify and properly utilize all standard geometric flowchart symbols, adhering to rigorous control flow conventions."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Flowchart Architecture & Standard Symbol Library",
                        "content": {
                            "markdown": """### **Core Definition**
- **Flowchart**: A standardized geometric diagram that uses distinct shapes connected by directional arrows (flow lines) to represent the step-by-step logical sequence of an algorithm.

---

### **The ISO/ANSI Flowchart Symbol Library**
Every standard shape in a flowchart represents an exclusive category of computation:

| Symbol Name | Geometric Shape | Computational Purpose | Pseudocode Equivalent |
| :--- | :--- | :--- | :--- |
| **Terminal** | Rounded Oval / Capsule | Marks the start or end of an algorithm. | `START` / `STOP` / `END` |
| **Input / Output** | Parallelogram | Captures data from user or prints data to console. | `INPUT`, `READ`, `OUTPUT`, `DISPLAY` |
| **Process** | Rectangle | Performs calculations, assignments, or data mutations. | `SET sum = 0`, `SET area = l * w` |
| **Decision** | Diamond (Rhombus) | Evaluates a Boolean condition to branch flow into two paths. | `IF condition THEN`, `WHILE condition` |
| **Flow Lines** | Directional Arrows | Indicates the exact order of instruction execution. | Top-to-bottom / Left-to-right flow |
| **On-Page Connector** | Small Circle | Connects separate flow lines on the same physical page. | Connector labels: `(A)`, `(B)` |
| **Off-Page Connector** | Pentagon / Shield | Links flow lines across different physical sheets/pages. | Connector labels: `[Page 2]`, `[Sheet B]` |

---

### **The Four Core Flowchart Design Rules**
1. **Direction of Flow**: Diagrams must flow consistently from **top to bottom** or from **left to right**.
2. **Single Entrance/Exit for Process & I/O**: Rectangles and parallelograms must have exactly **one entry arrow** and **one exit arrow**.
3. **The 2-Branch Decision Rule**: A Decision Diamond must have exactly **one entry arrow** and exactly **two exit arrows**, each explicitly labeled with **Yes/No** or **True/False**.
4. **Terminal Boundaries**: Every flowchart must possess exactly **one Start terminal** and at least **one End/Stop terminal**."""
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Geometric Precision in Flowcharts",
                        "content": {
                            "text": "Every flowchart shape has a strict computational meaning: Ovals for Terminals, Parallelograms for I/O, Rectangles for Calculations, and Diamonds with exactly two labeled exits for Decisions."
                        }
                    }
                ],

                # Page 4: Visual & Media Anchor
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Visualizing Flowchart Symbology & Logic Models",
                        "content": {
                            "goal": "Visualize standard flowchart symbology, decision branches, and their direct one-to-one mapping with structured pseudocode."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Standard Flowchart Geometric Symbols & Mapping Matrix",
                        "content": {
                            "svg_content": SVG_FLOWCHART_SYMBOLS_MATRIX,
                            "caption": "Figure 13.3: ISO/ANSI standard flowchart symbol library illustrating Terminals, I/O Parallelograms, Process Rectangles, Decision Diamonds with dual exit branches, and Connectors."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Flowchart Logic Decision Model",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Flowchart_en.svg/800px-Flowchart_en.svg.png",
                            "caption": "Figure 13.4: Example of a logical flowchart diagram illustrating decision branching and loop pathways.",
                            "author": "Wikimedia Commons / Standard Diagrams",
                            "licensing": "Creative Commons Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)"
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Algorithm Design, Pseudocode & Flowcharts",
                        "content": {
                            "url": "https://www.youtube.com/watch?v=X4p5oXpL0e4",
                            "youtube_id": "X4p5oXpL0e4",
                            "description": "Comprehensive tutorial on writing standard pseudocode and constructing accurate flowcharts for computer science algorithm design."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Visual vs. Textual Algorithms",
                        "content": {
                            "text": "Flowcharts and pseudocode are two complementary representations of the same underlying algorithm: flowcharts provide visual structural clarity, while pseudocode provides precise textual structure."
                        }
                    }
                ],

                # Page 5: Formative Knowledge Check (4 MCQs)
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Algorithm & Flowchart Mastery Assessment",
                        "content": {
                            "goal": "Evaluate your ability to identify algorithm quality criteria, standard pseudocode keywords, and flowchart geometric rules."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Algorithm Check 1: Quality Criteria Violation",
                        "content": {
                            "question": "An algorithm repeatedly prints numbers without ever hitting a stop condition or incrementing its counter, running endlessly. Which fundamental quality criterion of an algorithm has been violated?",
                            "options": [
                                "Definiteness (Precision)",
                                "Finiteness",
                                "Input Bounds",
                                "Effectiveness"
                            ],
                            "correct_answer": "Finiteness",
                            "explanation": "Finiteness dictates that every algorithm must terminate after a finite number of computational steps. An infinite loop directly violates the finiteness principle."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Algorithm Check 2: Pseudocode Assignment Keyword",
                        "content": {
                            "question": "Which standardized pseudocode keyword is used to store the result of a mathematical calculation into a named memory variable?",
                            "options": [
                                "READ",
                                "OUTPUT",
                                "SET",
                                "IF"
                            ],
                            "correct_answer": "SET",
                            "explanation": "The 'SET' (or 'LET') keyword is the standard pseudocode convention for variable assignment and calculation storage (e.g., 'SET total = price * 1.16')."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Algorithm Check 3: Flowchart Shape Identification",
                        "content": {
                            "question": "A student needs to draw a flowchart symbol to represent asking the user to enter their age. Which geometric shape must they draw?",
                            "options": [
                                "Rectangle",
                                "Oval",
                                "Parallelogram",
                                "Diamond"
                            ],
                            "correct_answer": "Parallelogram",
                            "explanation": "In ISO/ANSI flowchart standards, a parallelogram represents Input and Output operations (such as reading user input or printing results)."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Algorithm Check 4: Decision Diamond Exit Constraints",
                        "content": {
                            "question": "What is the mandatory structural constraint regarding the exit flow lines of a flowchart Decision Diamond?",
                            "options": [
                                "It must have exactly one exit line going directly to an End terminal.",
                                "It must have exactly two exit lines, each explicitly labeled with outcomes such as Yes/No or True/False.",
                                "It can have three unlabeled exit lines connecting to parallel processes.",
                                "It must not have any exit lines if used inside a loop."
                            ],
                            "correct_answer": "It must have exactly two exit lines, each explicitly labeled with outcomes such as Yes/No or True/False.",
                            "explanation": "Every Decision Diamond evaluates a Boolean condition and must have exactly two exit arrows, clearly labeled with the binary branches (Yes/No or True/False)."
                        }
                    }
                ]
            ]
        },

        # -----------------------------------------------------------------
        # UNIT 3: LOGIC VERIFICATION: TRACING & TEST STRATEGIES
        # -----------------------------------------------------------------
        {
            "unit_order": 3,
            "unit_name": "Logic Verification, Dry Running, and Systematic Test Strategies",
            "unit_description": "Techniques for manually verifying algorithmic correctness and system reliability prior to implementation: dry-run mechanics, trace table construction, test data categorization (normal, boundary, invalid), and building structured test suites.",
            "lesson_title": "Tracing, Dry Runs, and Systematic Test Strategies",
            "pages": [
                # Page 1: Manual Logic Verification & Trace Tables
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Dry Running Mechanics & Trace Tables",
                        "content": {
                            "goal": "Understand how dry-running simulates CPU instruction execution on paper and learn how to construct multi-column trace tables."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Manual Logic Verification & Trace Tables",
                        "content": {
                            "markdown": r"""### **Core Definitions**
- **Dry Run**: A manual, paper-based verification technique where an engineer steps through an algorithm line-by-line, pretending to be the CPU, to track how variable values change in memory.
- **Trace Table**: A structured multi-column matrix used during a dry run to record the exact sequential state of every system variable, conditional evaluation, and output display after each instruction executes.

---

### **Why Dry-Run Algorithms Before Coding?**
1. **Catch Silent Logic Errors Early**: Catching a logic bug on paper takes seconds; debugging a logic error buried in compiled software can take days.
2. **Verify Loop Boundaries**: Trace tables expose "off-by-one" loop errors (e.g., executing 9 or 11 times instead of 10).
3. **Confirm Variable Accumulation**: Tracing verifies whether accumulators (like `sum = sum + counter`) increment correctly and whether initializations (like `sum = 0`) occurred.
4. **Language Independence**: Logic is verified without confounding syntax errors, compiler warnings, or IDE configuration glitches.

---

### **Architecture of a Trace Table**
A complete trace table consists of six distinct column types:
1. **Step Number**: Sequential counter tracking each executed action ($0, 1, 2, \dots$).
2. **Line / Instruction Executed**: The exact line of pseudocode or flowchart block currently being processed.
3. **Variable Columns**: One dedicated column for every variable allocated in system memory (e.g., `N`, `sum`, `counter`).
4. **Condition Evaluation Column**: Explicit evaluation of Boolean statements (e.g., `counter <= N \rightarrow \text{True/False}`).
5. **Output Console Column**: Characters or numbers printed to the user display."""
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Desk Checking With Trace Tables",
                        "content": {
                            "text": "A dry run simulates CPU execution on paper. Trace tables track variable registers, conditions, and console outputs line-by-line to isolate logic errors before typing code."
                        }
                    }
                ],

                # Page 2: Step-by-Step Cumulative Sum Trace Table Walkthrough
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Step-by-Step Algorithmic Trace Walkthrough",
                        "content": {
                            "goal": "Perform a step-by-step trace of a loop-based algorithm, documenting register transitions and loop termination conditions."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Cumulative Sum Trace Table Walkthrough (N = 3)",
                        "content": {
                            "markdown": r"""### **The Algorithm Under Test**
```text
1: START
2:     INPUT N
3:     SET sum = 0
4:     SET counter = 1
5:     WHILE counter <= N DO
6:         SET sum = sum + counter
7:         SET counter = counter + 1
8:     ENDWHILE
9:     OUTPUT sum
10: END
```

---

### **Complete 15-Step Trace Table Matrix for Input $N = 3$**
Target: Compute $1 + 2 + 3 = 6$.

| Step | Line Executed | Variable: `N` | Variable: `sum` | Variable: `counter` | Condition: `counter <= N` | Output Console |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **0** | *Initial Unallocated State* | *None* | *None* | *None* | *None* | *None* |
| **1** | Line 2 (`INPUT N`) | **3** | *None* | *None* | *None* | *None* |
| **2** | Line 3 (`SET sum = 0`) | 3 | **0** | *None* | *None* | *None* |
| **3** | Line 4 (`SET counter = 1`) | 3 | 0 | **1** | *None* | *None* |
| **4** | Line 5 (`WHILE check`) | 3 | 0 | 1 | **True** ($1 \le 3$) | *None* |
| **5** | Line 6 (`sum = sum + counter`) | 3 | **1** ($0 + 1$) | 1 | *None* | *None* |
| **6** | Line 7 (`counter = counter + 1`) | 3 | 1 | **2** ($1 + 1$) | *None* | *None* |
| **7** | Line 5 (`WHILE check`) | 3 | 1 | 2 | **True** ($2 \le 3$) | *None* |
| **8** | Line 6 (`sum = sum + counter`) | 3 | **3** ($1 + 2$) | 2 | *None* | *None* |
| **9** | Line 7 (`counter = counter + 1`) | 3 | 3 | **3** ($2 + 1$) | *None* | *None* |
| **10** | Line 5 (`WHILE check`) | 3 | 3 | 3 | **True** ($3 \le 3$) | *None* |
| **11** | Line 6 (`sum = sum + counter`) | 3 | **6** ($3 + 3$) | 3 | *None* | *None* |
| **12** | Line 7 (`counter = counter + 1`) | 3 | 6 | **4** ($3 + 1$) | *None* | *None* |
| **13** | Line 5 (`WHILE check`) | 3 | 6 | 4 | **False** ($4 \le 3$) | *None* |
| **14** | Line 9 (`OUTPUT sum`) | 3 | 6 | 4 | *None* | **6** |
| **15** | Line 10 (`END`) | 3 | 6 | 4 | *None* | *Execution Terminated* |

---

### **Analysis of Execution Verification**
1. **Variable Updates**: At Step 11, `sum` correctly accumulated to $6$.
2. **Loop Exit Condition**: At Step 12, `counter` incremented to $4$. Step 13 evaluated $4 \le 3$, which yielded **False**, successfully branching control to Line 9.
3. **Conclusion**: The logic is formally proven sound and verified for implementation."""
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Verifying Loop Termination",
                        "content": {
                            "text": "By documenting variable states across each loop pass, trace tables prove whether accumulator registers update accurately and verify that loop boundary conditions terminate on schedule."
                        }
                    }
                ],

                # Page 3: Test Data Spectrum & Test Suites
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Test Data Categorization & Test Suites",
                        "content": {
                            "goal": "Classify test inputs into Normal, Boundary, and Invalid categories, and construct comprehensive test suites for software validation."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Test Data Categorization & Systematic Test Suites",
                        "content": {
                            "markdown": r"""### **Core Definitions**
- **Test Case**: A formal specification consisting of a set of test inputs, execution preconditions, and expected system outputs designed to verify a specific software requirement.
- **Test Coverage**: A quantitative measure of the proportion of program paths, decision branches, and boundary conditions exercised by a test suite.

---

### **The Three Test Data Classifications**
To achieve robust test coverage, developers must partition test inputs across three distinct spectrums:

```
                      +------------------------------------------+
                      |           TEST DATA SPECTRUM             |
                      +------------------------------------------+
                           /                  |                 \
                          /                   |                  \
                         v                    v                   v
                 [ NORMAL DATA ]      [ BOUNDARY DATA ]   [ INVALID DATA ]
                  Valid inputs         Limits of range     Illegal inputs
                  e.g., Exam: 75       e.g., Exam: 0, 50   e.g., Exam: -15, "A"
```

1. **Normal (Valid) Data**: Typical, expected inputs that lie well inside the acceptable operational boundaries of the requirements.
   - *Example*: In a $0\text{--}100$ student grading system, $75$ (Pass) or $32$ (Fail).
2. **Boundary (Edge) Data**: Inputs situated exactly at the minimum, maximum, and internal transition thresholds of the allowable range.
   - *Example*: $0$ (minimum boundary), $100$ (maximum boundary), $50$ (lower Pass boundary), and $49$ (upper Fail boundary).
   - *Purpose*: Catches off-by-one relational errors (e.g., writing `> 50` instead of `>= 50`).
3. **Invalid (Erroneous) Data**: Inputs that violate the allowable range, contain incorrect data types, or represent illegal operations.
   - *Example*: Negative scores ($-1$, $-15$), over-maximum numbers ($101$, $500$), or alphabetic text (`"eighty"`).
   - *Purpose*: Verifies defensive input validation and ensures the program reports clean error messages without crashing.

---

### **Designing a Comprehensive Test Suite (Calculated Grade Example)**
System Requirement: Allowable scores: $0 \le \text{score} \le 100$. If $\text{score} \ge 50 \rightarrow \text{"Pass"}$; else $\text{"Fail"}$.

| Test ID | Category | Input Value | Expected System Output | Purpose of the Test Case |
| :---: | :--- | :---: | :--- | :--- |
| **TC-01** | Normal Data | `75` | Displays `"Pass"` | Verify typical passing execution. |
| **TC-02** | Normal Data | `32` | Displays `"Fail"` | Verify typical failing execution. |
| **TC-03** | Boundary Data | `50` | Displays `"Pass"` | Test exact lower threshold of Pass grade. |
| **TC-04** | Boundary Data | `49` | Displays `"Fail"` | Test exact upper threshold of Fail grade. |
| **TC-05** | Boundary Data | `0` | Displays `"Fail"` | Test absolute minimum allowable score. |
| **TC-06** | Boundary Data | `100` | Displays `"Pass"` | Test absolute maximum allowable score. |
| **TC-07** | Invalid Data | `-1` | Displays `"Error: Out of bounds"` | Verify rejection of negative values. |
| **TC-08** | Invalid Data | `101` | Displays `"Error: Out of bounds"` | Verify rejection of oversized values. |
| **TC-09** | Invalid Data | `"eighty"` | Displays `"Error: Invalid Type"` | Verify string input rejection. |"""
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Comprehensive Test Coverage",
                        "content": {
                            "text": "Robust software testing requires a balanced suite of Normal data (typical operations), Boundary data (edge transitions), and Invalid data (error-handling verification)."
                        }
                    }
                ],

                # Page 4: Visual & Media Anchor
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Visualizing Trace Matrices and Test Spectrums",
                        "content": {
                            "goal": "Visualize trace table state transitions, variable register changes, and test data boundary distributions."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Trace Table State Transitions and Execution Matrix",
                        "content": {
                            "svg_content": SVG_TRACE_TABLE_EXECUTION,
                            "caption": "Figure 13.5: Side-by-side visualization of pseudocode execution and trace table state transitions showing CPU variable register mutations during the N=3 cumulative sum dry run."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "The Test Data Spectrum: Normal, Boundary, and Invalid Partitions",
                        "content": {
                            "svg_content": SVG_TEST_DATA_SPECTRUM,
                            "caption": "Figure 13.6: Number line partition model of the 0–100 grading system illustrating Normal, Boundary (0, 49, 50, 100), and Invalid (<0, >100, non-numeric) test partitions."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "The First Computer Bug (1947)",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/First_Computer_Bug%2C_1947.jpg/800px-First_Computer_Bug%2C_1947.jpg",
                            "caption": "Figure 13.7: Grace Hopper's historic 1947 logbook entry with the moth found trapped inside a Mark II computer relay, popularizing the term 'debugging'.",
                            "author": "Wikimedia Commons / Naval Surface Warfare Center",
                            "licensing": "Public Domain"
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "How to Construct and Execute Trace Tables",
                        "content": {
                            "url": "https://www.youtube.com/watch?v=3Xk3GjY5e1k",
                            "youtube_id": "3Xk3GjY5e1k",
                            "description": "Step-by-step tutorial on conducting desk dry runs and populating multi-column trace tables for computer science examination problems."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: The Value of Structured Verification",
                        "content": {
                            "text": "Combining dry-run trace tables during design with structured test suites during implementation guarantees both logical correctness and software resilience."
                        }
                    }
                ],

                # Page 5: Formative Knowledge Check (4 MCQs)
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Tracing & Testing Mastery Assessment",
                        "content": {
                            "goal": "Evaluate your mastery of trace table construction, variable state tracking, and test data classification."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Tracing Check 1: Purpose of Trace Tables",
                        "content": {
                            "question": "What is the primary reason software developers construct trace tables during the algorithm design phase?",
                            "options": [
                                "To automatically compile high-level source code into machine language binaries.",
                                "To manually track variable values and condition outcomes line-by-line, catching logic errors before writing code.",
                                "To benchmark the physical clock speed of multi-core microprocessors.",
                                "To encrypt source code files for cloud backup storage."
                            ],
                            "correct_answer": "To manually track variable values and condition outcomes line-by-line, catching logic errors before writing code.",
                            "explanation": "Trace tables are used during manual dry runs to simulate CPU execution on paper, tracking memory registers and verifying logical correctness before coding begins."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Testing Check 2: Classifying Test Inputs",
                        "content": {
                            "question": "A grading software accepts scores from 0 to 100 with a pass threshold of 50. A tester enters score values of '50' and '49'. Which category of test data do these inputs represent?",
                            "options": [
                                "Normal Data",
                                "Boundary Data",
                                "Invalid Data",
                                "Synthetic Data"
                            ],
                            "correct_answer": "Boundary Data",
                            "explanation": "Values of 50 (minimum passing score) and 49 (maximum failing score) sit exactly on the decision boundary between Pass and Fail, making them Boundary (Edge) Data."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Testing Check 3: Invalid Test Case Identification",
                        "content": {
                            "question": "Which of the following test inputs represents 'Invalid Data' for a software module calculating employee monthly working hours (valid range: 1 to 240 hours)?",
                            "options": [
                                "160 hours",
                                "1 hour",
                                "240 hours",
                                "-12 hours"
                            ],
                            "correct_answer": "-12 hours",
                            "explanation": "-12 hours is completely outside the allowable range of positive working hours, making it Invalid (Erroneous) Data designed to test system error handling."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Tracing Check 4: Loop Counter Termination",
                        "content": {
                            "question": "In the Cumulative Sum algorithm for N=3, what is the final value of the variable 'counter' when the loop condition (counter <= 3) evaluates to False and halts execution?",
                            "options": [
                                "2",
                                "3",
                                "4",
                                "6"
                            ],
                            "correct_answer": "4",
                            "explanation": "During the third pass, counter increments from 3 to 4. In the subsequent loop check, '4 <= 3' evaluates to False, terminating the loop with counter equal to 4."
                        }
                    }
                ]
            ]
        },

        # -----------------------------------------------------------------
        # UNIT 4: INTEGRITY, DESIGN REVIEW, DOCUMENTATION & PRACTICALS
        # -----------------------------------------------------------------
        {
            "unit_order": 4,
            "unit_name": "Algorithm Integrity, Design Review, Documentation, and Applied Practicals",
            "unit_description": "Advanced engineering practices: Requirements Traceability Matrices, peer design review checklists, internal vs. external documentation standards, and applied real-world municipal and environmental programming practicals.",
            "lesson_title": "Algorithm Integrity, Design Review, Documentation and Applied Practicals",
            "pages": [
                # Page 1: Requirements Traceability & Peer Design Reviews
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Requirements Traceability & Peer Design Review",
                        "content": {
                            "goal": "Apply Requirements Traceability Matrices (RTM) to prevent functional gaps and conduct rigorous pre-coding peer design reviews."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Requirements Traceability & Peer Design Reviews",
                        "content": {
                            "markdown": """### **Requirements Traceability**
A classic hazard in software development is designing a mathematically brilliant algorithm that completely forgets to solve the client's original problem.

**Requirements Traceability** is the engineering practice of linking every single stated requirement in the SRS directly to specific algorithm modules, flowchart shapes, and test cases.

#### **The Requirements Traceability Matrix (RTM)**
| Req ID | Stakeholder Requirement | Algorithm / Flowchart Component | Test Case ID | Verification Status |
| :---: | :--- | :--- | :---: | :---: |
| **REQ-01** | System must calculate rectangle area | `SET area = length * width` | TC-01, TC-02 | Verified |
| **REQ-02** | System must reject negative dimensions | `IF length <= 0 OR width <= 0 THEN` | TC-07, TC-08 | Verified |
| **REQ-03** | System must output result formatted | `OUTPUT "Area: " + area` | TC-01 | Verified |

---

### **Pre-Coding Peer Design Review Checklist**
Before writing source code in an IDE, senior analysts and peer engineers review the algorithm package (pseudocode, flowcharts, trace tables, test suites). The review verifies:

1. **Logical Equivalence**: Does the flowchart represent the exact same step-by-step logic as the pseudocode?
2. **Guaranteed Loop Termination**: Is every loop mathematically guaranteed to reach its exit boundary without creating an infinite loop?
3. **Dead / Unreachable Code Detection**: Are there conditional branches that can never physically execute (e.g., `IF score > 100 AND score < 50`)?
4. **Relational & Off-by-One Diagnostics**: Are comparison operators properly chosen (`>=` vs `>`, `<=` vs `<`) to correctly handle boundary edge values?"""
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Traceability and Review",
                        "content": {
                            "text": "Requirements Traceability ensures no customer requirements are forgotten. Peer design reviews catch dead code, logic gaps, and termination bugs before costly implementation begins."
                        }
                    }
                ],

                # Page 2: Code Quality & Documentation Standards
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Documentation Standards and Code Readability",
                        "content": {
                            "goal": "Implement professional code documentation standards, distinguishing between internal source documentation and external user reference manuals."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Code Quality & Documentation Standards",
                        "content": {
                            "markdown": """### **The Two Pillars of Software Documentation**
Software is written once, but read, updated, and debugged hundreds of times. Documentation ensures code longevity.

```
                    +------------------------------------------+
                    |          SOFTWARE DOCUMENTATION          |
                    +------------------------------------------+
                           /                            \
                          /                              \
                         v                                v
               [ INTERNAL DOCUMENTATION ]      [ EXTERNAL DOCUMENTATION ]
                Inside source files             Outside source files
                e.g., Comments, Identifiers     e.g., User Manuals, Tech Specs
```

---

### **1. Internal Documentation (For Developers & Maintainers)**
Internal documentation is embedded directly inside the program's source code files:

- **Meaningful Identifiers**: Use descriptive variable and function names rather than cryptic letters.
  - *Bad*: `a = b * c`
  - *Good*: `rectangle_area = room_length * room_width`
- **Explanatory Comments**: Non-executable explanatory notes written in plain language that explain *why* complex formulas or non-obvious logic were written.
  ```python
  # Apply 16% standard VAT tax to taxable subtotal
  tax_amount = subtotal * 0.16
  ```
- **Consistent Layout & Indentation**: Use uniform whitespace indentation to visually reveal nested blocks, loops, and conditional structures to the human eye.

---

### **2. External Documentation (For Users & System Administrators)**
External documentation comprises separate printed or digital publications compiled for non-technical users and IT administrators:

- **User Guide / Operator Manual**: Step-by-step guides explaining how to install, launch, operate, configure, and troubleshoot the program.
- **Technical Design Specification**: Comprehensive engineering manuals detailing system architecture, database schemas, API endpoints, hardware prerequisites, and data dictionaries."""
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Internal vs. External Documentation",
                        "content": {
                            "text": "Internal documentation (meaningful identifiers, comments, indentation) lives inside source code for developers. External documentation (user guides, technical specs) guides end-users and administrators."
                        }
                    }
                ],

                # Page 3: Real-World Interactive Engineering Practicals
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Real-World Municipal and Retail Problem Solving",
                        "content": {
                            "goal": "Apply algorithmic design and debugging techniques to solve municipal control and retail business logic problems."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Real-World Engineering Practicals: Nairobi Traffic & Flawed Discount",
                        "content": {
                            "markdown": """### **Practical 1: The Nairobi Smart Traffic Light Coordinator**
**Problem**: Nairobi City Council requires an automated pedestrian crossing controller for a busy road crossing.

#### **System Requirements**:
1. **Default State**: Vehicle Light is **GREEN**; Pedestrian Light is **RED**.
2. **Pedestrian Request**: When button is pressed (`button_pressed == True`), wait 10 seconds, change Vehicle Light to **YELLOW** for 3 seconds, then to **RED**.
3. **Crossing Window**: Once vehicle light is RED, Pedestrian Light turns **GREEN** for 20 seconds.
4. **Warning Clearance**: Pedestrian Light flashes **RED** for 5 seconds before returning to the Default State.

#### **Standard Pseudocode Controller**:
```text
START
    SET vehicle_light = "GREEN"
    SET pedestrian_light = "RED"
    WHILE system_power == True DO
        IF READ_BUTTON() == True THEN
            WAIT(10)
            SET vehicle_light = "YELLOW"
            WAIT(3)
            SET vehicle_light = "RED"
            SET pedestrian_light = "GREEN"
            WAIT(20)
            FLASH_RED_PEDESTRIAN(5)
            SET pedestrian_light = "RED"
            SET vehicle_light = "GREEN"
        ENDIF
    ENDWHILE
END
```

---

### **Practical 2: Debugging a Flawed Discount Algorithm**
**Scenario**: A supermarket offers a 10% discount on purchases exceeding 1000 KSh. A junior programmer drafts this algorithm:

```text
1: START
2:     INPUT sale_total
3:     SET discount = 0
4:     IF sale_total > 1000 THEN
5:         SET discount = sale_total * 0.10
6:         SET final_total = sale_total - discount
7:     ENDIF
8:     OUTPUT final_total
9: END
```

#### **The Walkthrough Trace for `sale_total = 800`**:
- Step 1: `sale_total = 800`
- Step 2: `discount = 0`
- Step 3: Condition `800 > 1000` evaluates to **False**.
- Step 4: Execution skips lines 5 and 6 directly to line 8.
- Step 5: Line 8 attempts `OUTPUT final_total`. **CRITICAL ERROR**: `final_total` was never initialized or defined when `sale_total <= 1000`!

#### **Error Classification**:
- This is a classic **Logic Error** that results in an uninitialized variable runtime crash.

#### **Corrected Pseudocode**:
```text
START
    INPUT sale_total
    SET discount = 0
    IF sale_total > 1000 THEN
        SET discount = sale_total * 0.10
    ENDIF
    SET final_total = sale_total - discount
    OUTPUT final_total
END
```"""
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Initializing All Execution Paths",
                        "content": {
                            "text": "In conditional logic, variables used downstream (like final_total) must be initialized or computed along all possible branching pathways."
                        }
                    }
                ],

                # Page 4: Applied Environmental Case Study
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Autonomous IoT Water Quality Monitoring System",
                        "content": {
                            "goal": "Design an autonomous sensor monitoring algorithm and test suite for the Lake Victoria Smart Water Quality Station."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Case Study: Lake Victoria Smart Water Quality Station",
                        "content": {
                            "markdown": r"""### **The Lake Victoria Smart Water Quality Monitoring Station**
An environmental conservation agency installs an autonomous, solar-powered water sensing station on Lake Victoria. A submerged sensor reads the water's pH level once every minute (valid physical pH range: $0.0\text{--}14.0$).

---

### **1. System Requirements Analysis**
- **Inputs**: Continuous floating-point pH reading (`current_pH`) from submerged probe.
- **Outputs**: LCD status messages, emergency audio siren, GSM alert SMS.
- **Constraints**: Solar-powered 24/7 continuous operation; sensor malfunction must trigger an emergency valve shutdown.
- **Success Criteria**: 100% accurate classification of water safety with zero unhandled sensor exceptions.

---

### **2. Standard Pseudocode Implementation**
```text
START
    WHILE station_active == True DO
        INPUT current_pH
        
        IF current_pH < 0.0 OR current_pH > 14.0 THEN
            DISPLAY "Warning: Sensor Malfunction!"
            ACTUATE_ALARM_VALVE("SHUTDOWN")
            SEND_SMS("Alert: Lake Victoria Sensor Hardware Fault")
        ELSEIF current_pH >= 6.5 AND current_pH <= 8.5 THEN
            DISPLAY "Water Quality: Safe"
            SET valve_state = "OPEN"
        ELSEIF current_pH < 6.5 THEN
            DISPLAY "Alert: High Acid Content!"
            ACTUATE_ALARM_VALVE("ALERT")
        ELSE
            DISPLAY "Alert: High Alkaline Content!"
            ACTUATE_ALARM_VALVE("ALERT")
        ENDIF
        
        WAIT(60)
    ENDWHILE
END
```

---

### **3. Five-Case Verification Test Suite**
| Test ID | Category | Input pH | Expected System Output | Verification Purpose |
| :---: | :--- | :---: | :--- | :--- |
| **TC-01** | Normal Data | `7.2` | `"Water Quality: Safe"` | Verify neutral water operations. |
| **TC-02** | Boundary Data | `6.5` | `"Water Quality: Safe"` | Verify exact lower boundary of safe range. |
| **TC-03** | Normal (Acid) | `4.8` | `"Alert: High Acid Content!"` | Verify acid runoff alert trigger. |
| **TC-04** | Boundary (Alk) | `8.6` | `"Alert: High Alkaline Content!"` | Verify upper alkaline transition trigger. |
| **TC-05** | Invalid / Fault | `-2.5` | `"Warning: Sensor Malfunction!"` | Verify hardware fault interception and valve shutdown. |"""
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Autonomous Sensor Decision Logic",
                        "content": {
                            "text": "Autonomous systems require infinite polling loops with prioritized multi-tier decision trees, ensuring hardware faults are handled with immediate failsafe actuator actions."
                        }
                    }
                ],

                # Page 5: Visual & Media Anchor
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Visualizing Municipal and Environmental Control Systems",
                        "content": {
                            "goal": "Visualize real-world municipal state transitions and environmental water quality decision pipelines."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Nairobi Smart Traffic Controller State Machine Flow",
                        "content": {
                            "svg_content": SVG_TRAFFIC_LIGHT_ALGORITHM,
                            "caption": "Figure 13.8: State machine flowchart showing the vehicle-to-pedestrian transition timing sequence (10s delay, 3s yellow, 20s green walk, 5s red flash)."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Lake Victoria Water Quality Sensor Decision Tree Architecture",
                        "content": {
                            "svg_content": SVG_LAKE_VICTORIA_WATER_MONITOR,
                            "caption": "Figure 13.9: Embedded microcontroller decision pipeline showing solar input, pH range classifications, and actuator/telemetry triggers."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Traffic Light & Pedestrian Control System",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Pedestrian_crossing_light.svg/800px-Pedestrian_crossing_light.svg.png",
                            "caption": "Figure 13.10: Automated pedestrian signal system used in modern urban traffic management.",
                            "author": "Wikimedia Commons / Traffic Systems",
                            "licensing": "Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)"
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Software Engineering Best Practices & Documentation",
                        "content": {
                            "url": "https://www.youtube.com/watch?v=kM9ASKAni_s",
                            "youtube_id": "kM9ASKAni_s",
                            "description": "Educational guide to code readability, internal vs external documentation, variable naming conventions, and testing strategies."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Real-World Systems Engineering",
                        "content": {
                            "text": "Algorithmic thinking scales from simple arithmetic calculations to complex municipal traffic controllers and autonomous environmental IoT monitoring stations."
                        }
                    }
                ],

                # Page 6: Summative & Comprehensive Knowledge Check (4 MCQs)
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Comprehensive Program Development Assessment",
                        "content": {
                            "goal": "Demonstrate mastery across requirements traceability, documentation types, logic debugging, and multi-tier algorithm design."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Integrity Check 1: Traceability Matrix",
                        "content": {
                            "question": "What is the primary role of a Requirements Traceability Matrix (RTM) during program development?",
                            "options": [
                                "To compile source code into machine language instructions automatically.",
                                "To map every stated customer requirement directly to specific algorithm modules and test cases, guaranteeing no functional omissions.",
                                "To defragment system hard drives and optimize RAM allocation.",
                                "To monitor CPU clock speeds during benchmark runs."
                            ],
                            "correct_answer": "To map every stated customer requirement directly to specific algorithm modules and test cases, guaranteeing no functional omissions.",
                            "explanation": "The Requirements Traceability Matrix (RTM) ensures complete coverage by linking every user requirement from Stage 1 directly to its corresponding design component and test case."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Documentation Check 2: Internal vs External",
                        "content": {
                            "question": "Which of the following represents an example of 'Internal Documentation'?",
                            "options": [
                                "A 50-page printed User Manual included in software packaging.",
                                "A website containing pricing and subscription plans.",
                                "Meaningful variable identifiers, consistent layout indentation, and explanatory comments inside source code files.",
                                "A server rack wiring diagram in a datacenter."
                            ],
                            "correct_answer": "Meaningful variable identifiers, consistent layout indentation, and explanatory comments inside source code files.",
                            "explanation": "Internal documentation exists directly inside the source code files for maintainers (comments, meaningful variable names, whitespace indentation)."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Debugging Check 3: Flawed Discount Logic Error",
                        "content": {
                            "question": "In the flawed discount algorithm where 'final_total' was only computed inside 'IF sale_total > 1000 THEN', what type of error occurred when sale_total was 800?",
                            "options": [
                                "Syntax Error (misspelled keyword).",
                                "Logic / Runtime Error because 'final_total' was accessed without being initialized for sales of 1000 or less.",
                                "Hardware Error (damaged CPU register).",
                                "Network Transmission Error."
                            ],
                            "correct_answer": "Logic / Runtime Error because 'final_total' was accessed without being initialized for sales of 1000 or less.",
                            "explanation": "When sale_total was 800, the IF condition evaluated to False and skipped computing final_total. Attempting to output an uninitialized variable is a logic/runtime error."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Application Check 4: Lake Victoria Water Monitor",
                        "content": {
                            "question": "The Lake Victoria Water Quality station reads a pH value of -1.5 from its sensor. What action does its algorithm take?",
                            "options": [
                                "Displays 'Water Quality: Safe' because -1.5 is less than 6.5.",
                                "Displays 'Alert: High Acid Content!' and keeps water valves open.",
                                "Intercepts -1.5 as out-of-bounds, displays 'Warning: Sensor Malfunction!', and triggers the emergency shutdown valve.",
                                "Ignores the reading and halts the CPU permanently."
                            ],
                            "correct_answer": "Intercepts -1.5 as out-of-bounds, displays 'Warning: Sensor Malfunction!', and triggers the emergency shutdown valve.",
                            "explanation": "Physical pH ranges from 0.0 to 14.0. A reading of -1.5 indicates a broken sensor or severed wire, which the algorithm immediately flags as a hardware malfunction, shutting down the intake valve."
                        }
                    }
                ]
            ]
        }
    ]

# =====================================================================
# INGESTION EXECUTOR
# =====================================================================

def ingest_grade10_topic13(replace: bool = True):
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 10 Computer Science — Topic 13")
    print("Topic: Program Development")
    print("=" * 80)

    curriculum = Curriculum.objects.get(id=5)
    grade = Grade.objects.get(curriculum=curriculum, level=10)
    subject, _ = Subject.objects.get_or_create(grade=grade, name="Computer Science")

    with transaction.atomic():
        topic, created = Topic.objects.get_or_create(
            subject=subject,
            order=13,
            defaults={
                "name": "Program Development",
                "description": "Comprehensive study of the Program Development Cycle (PDC): problem definition, language-independent algorithm design, standard pseudocode conventions, geometric flowchart modeling, dry running and trace tables, test data spectrums (normal, boundary, invalid), requirements traceability, and documentation standards."
            }
        )

        if not created and replace:
            print(f"[*] Topic 13 already exists (ID: {topic.id}). Performing clean replacement of units and lessons...")
            topic.learning_units.all().delete()
            topic.lessons.all().delete()
            topic.name = "Program Development"
            topic.description = "Comprehensive study of the Program Development Cycle (PDC): problem definition, language-independent algorithm design, standard pseudocode conventions, geometric flowchart modeling, dry running and trace tables, test data spectrums (normal, boundary, invalid), requirements traceability, and documentation standards."
            topic.save()

        curriculum_data = build_topic13_curriculum()

        total_units = 0
        total_lessons = 0
        total_pages = 0
        total_blocks = 0
        total_assets = 0

        for u_data in curriculum_data:
            u_order = u_data["unit_order"]
            u_name = clean_text(u_data["unit_name"])
            u_desc = clean_text(u_data["unit_description"])
            l_title = clean_text(u_data["lesson_title"])
            pages = u_data["pages"]

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
                    "topic_order": 13,
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
                        block_id=f"g10_cs_t13_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={"topic_order": 13, "unit_order": u_order, "page": page_idx}
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
    print(f"TOPIC 13 INGESTION COMPLETE:")
    print(f"  Topic ID:        {topic.id}")
    print(f"  Topic Name:      {topic.name}")
    print(f"  Units Created:   {total_units}")
    print(f"  Lessons Created: {total_lessons}")
    print(f"  Pages Created:   {total_pages}")
    print(f"  Blocks Created:  {total_blocks}")
    print(f"  Assets Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_grade10_topic13(replace=True)
