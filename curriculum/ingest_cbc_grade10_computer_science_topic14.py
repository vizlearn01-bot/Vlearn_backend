"""
VLearn CBC Grade 10 Computer Science — Topic 14: Identifiers and Operators
Production Ingestion & Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Computer Science (Subject ID: 38)
Topic: Identifiers and Operators (Topic Order: 14)

Decomposed into 5 Comprehensive Learning Units & 5 Published Lessons:
  1. Elementary Elements of a Program and Naming Identifiers (Lesson 57)
  2. Variables, Constants, and Typing Systems (Lesson 58)
  3. Input and Output Statements and Data Type Casting (Lesson 59)
  4. Operators, Expressions, and Mathematical Precedence (Lesson 60 & 61)
  5. Practice, Assessment, and Applied Scenario Implementations (Lesson 62)
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
# HIGH PRECISION VECTOR SVGS FOR TOPIC 14 (DARK THEME 960x520)
# =====================================================================

SVG_ELEMENTARY_PROGRAM_ELEMENTS = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Six Elementary Elements of Software Architecture</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">The fundamental syntactic and structural building blocks required to translate human algorithms into machine execution</text>

  <!-- Central Header Banner -->
  <g transform="translate(240, 85)">
    <rect width="480" height="38" rx="8" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="240" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">ATOMIC ELEMENTS OF ALL MODERN PROGRAMMING LANGUAGES</text>
  </g>

  <!-- 6 Feature Cards (2 Rows x 3 Columns) -->
  
  <!-- Row 1, Card 1: Program Structure -->
  <g transform="translate(45, 135)">
    <rect width="270" height="160" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#0284c7"/>
    <text x="135" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Program Structure</text>
    <text x="15" y="48" font-size="10" font-weight="bold" fill="#38bdf8">&#8226; Architectural Flow:</text>
    <text x="15" y="66" font-size="9" fill="#cbd5e1">Organizes algorithmic statements into:</text>
    <text x="15" y="82" font-size="9" fill="#cbd5e1">1. Sequence (Linear top-to-bottom step)</text>
    <text x="15" y="98" font-size="9" fill="#cbd5e1">2. Selection (Branching: if / else)</text>
    <text x="15" y="114" font-size="9" fill="#cbd5e1">3. Iteration (Loops: while / for)</text>
    <rect x="15" y="125" width="240" height="24" rx="4" fill="#1e293b"/>
    <text x="135" y="141" font-size="8.5" fill="#7dd3fc" text-anchor="middle">Governs macro logic execution path</text>
  </g>

  <!-- Row 1, Card 2: Syntax Grammar -->
  <g transform="translate(345, 135)">
    <rect width="270" height="160" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#d97706"/>
    <text x="135" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Syntax Grammar</text>
    <text x="15" y="48" font-size="10" font-weight="bold" fill="#fbbf24">&#8226; Formal Lexical Rules:</text>
    <text x="15" y="66" font-size="9" fill="#cbd5e1">The strict punctuation, indentation, and</text>
    <text x="15" y="82" font-size="9" fill="#cbd5e1">structural rules required by compiler parsers.</text>
    <text x="15" y="102" font-size="9.5" font-weight="bold" fill="#f87171">&#9888; Syntax Error Halt:</text>
    <text x="15" y="118" font-size="9" fill="#cbd5e1">Grammar breaches abort before compiling.</text>
    <rect x="15" y="125" width="240" height="24" rx="4" fill="#1e293b"/>
    <text x="135" y="141" font-size="8.5" fill="#fde68a" text-anchor="middle">Colons, semicolons, matching quotes</text>
  </g>

  <!-- Row 1, Card 3: Keywords (Reserved) -->
  <g transform="translate(645, 135)">
    <rect width="270" height="160" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#dc2626"/>
    <text x="135" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Keywords (Reserved)</text>
    <text x="15" y="48" font-size="10" font-weight="bold" fill="#f87171">&#8226; Pre-allocated Vocabulary:</text>
    <text x="15" y="66" font-size="9" fill="#cbd5e1">Special tokens reserved for translator commands.</text>
    <text x="15" y="84" font-size="9" fill="#cbd5e1">Cannot be redefined as custom variable names.</text>
    <text x="15" y="104" font-size="9.5" font-family="monospace" fill="#fca5a5">if, def, while, return, class, const</text>
    <rect x="15" y="125" width="240" height="24" rx="4" fill="#1e293b"/>
    <text x="135" y="141" font-size="8.5" fill="#fca5a5" text-anchor="middle">Pre-programmed compiler instructions</text>
  </g>

  <!-- Row 2, Card 4: Identifiers -->
  <g transform="translate(45, 310)">
    <rect width="270" height="165" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#059669"/>
    <text x="135" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">4. Identifiers</text>
    <text x="15" y="48" font-size="10" font-weight="bold" fill="#34d399">&#8226; Developer-Created Names:</text>
    <text x="15" y="66" font-size="9" fill="#cbd5e1">Symbolic labels assigned to memory cells,</text>
    <text x="15" y="82" font-size="9" fill="#cbd5e1">functions, arrays, and classes.</text>
    <text x="15" y="100" font-size="9" fill="#cbd5e1">Replaces raw hexadecimal hardware addresses.</text>
    <text x="15" y="118" font-size="9.5" font-family="monospace" fill="#6ee7b7">student_age, total_tax, calculate_gpa()</text>
    <rect x="15" y="130" width="240" height="24" rx="4" fill="#1e293b"/>
    <text x="135" y="146" font-size="8.5" fill="#a7f3d0" text-anchor="middle">User-defined symbolic memory pointers</text>
  </g>

  <!-- Row 2, Card 5: Data Types -->
  <g transform="translate(345, 310)">
    <rect width="270" height="165" rx="10" fill="#0f172a" stroke="#818cf8" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#4f46e5"/>
    <text x="135" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">5. Data Types</text>
    <text x="15" y="48" font-size="10" font-weight="bold" fill="#a5b4fc">&#8226; Binary Memory Templates:</text>
    <text x="15" y="66" font-size="9" fill="#cbd5e1">Defines how bit sequences are interpreted.</text>
    <text x="15" y="84" font-size="9" fill="#cbd5e1">&#8226; Integer (int): Whole counts (e.g. 42)</text>
    <text x="15" y="100" font-size="9" fill="#cbd5e1">&#8226; Floating Point (float): Decimals (e.g. 3.14)</text>
    <text x="15" y="116" font-size="9" fill="#cbd5e1">&#8226; String (str): Text characters; Boolean (bool)</text>
    <rect x="15" y="130" width="240" height="24" rx="4" fill="#1e293b"/>
    <text x="135" y="146" font-size="8.5" fill="#c7d2fe" text-anchor="middle">Dictates byte allocation and valid operations</text>
  </g>

  <!-- Row 2, Card 6: Standard Libraries -->
  <g transform="translate(645, 310)">
    <rect width="270" height="165" rx="10" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#db2777"/>
    <text x="135" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">6. Standard Libraries</text>
    <text x="15" y="48" font-size="10" font-weight="bold" fill="#f472b6">&#8226; Pre-Compiled Toolkits:</text>
    <text x="15" y="66" font-size="9" fill="#cbd5e1">High-speed, pre-written modules bundled</text>
    <text x="15" y="82" font-size="9" fill="#cbd5e1">with language runtimes to avoid reinventing tools.</text>
    <text x="15" y="102" font-size="9.5" font-family="monospace" fill="#fbcfe8">import math, &lt;iostream&gt;, java.util.*</text>
    <text x="15" y="120" font-size="9" fill="#cbd5e1">Provides math, I/O streams, and networking.</text>
    <rect x="15" y="130" width="240" height="24" rx="4" fill="#1e293b"/>
    <text x="135" y="146" font-size="8.5" fill="#fbcfe8" text-anchor="middle">Reusable, optimized system subroutines</text>
  </g>
</svg>
""")

SVG_IDENTIFIER_NAMING_RULES_MATRIX = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Identifier Construction Rules &amp; Lexical Compliance Matrix</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Compiler lexical rules governing variable, constant, and subroutine naming standards</text>

  <!-- Left: 6 Core Strict Rules -->
  <g transform="translate(45, 95)">
    <rect width="420" height="385" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="420" height="30" rx="8" fill="#0284c7"/>
    <text x="210" y="20" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">The 6 Inviolable Identifier Rules</text>

    <!-- Rule 1 -->
    <g transform="translate(15, 42)">
      <rect width="390" height="48" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <text x="15" y="20" font-size="10.5" font-weight="bold" fill="#38bdf8">1. Allowed Character Set</text>
      <text x="15" y="36" font-size="9" fill="#cbd5e1">Must contain ONLY letters (<tspan font-family="monospace">a-z, A-Z</tspan>), digits (<tspan font-family="monospace">0-9</tspan>), and underscores (<tspan font-family="monospace">_</tspan>).</text>
    </g>

    <!-- Rule 2 -->
    <g transform="translate(15, 96)">
      <rect width="390" height="48" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
      <text x="15" y="20" font-size="10.5" font-weight="bold" fill="#f87171">2. No Leading Digits (First Character Rule)</text>
      <text x="15" y="36" font-size="9" fill="#cbd5e1">Must start with a letter or underscore. Starting with a digit causes <tspan fill="#fca5a5" font-weight="bold">SyntaxError</tspan>.</text>
    </g>

    <!-- Rule 3 -->
    <g transform="translate(15, 150)">
      <rect width="390" height="48" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
      <text x="15" y="20" font-size="10.5" font-weight="bold" fill="#f87171">3. No Whitespaces (Spaces are Illegal)</text>
      <text x="15" y="36" font-size="9" fill="#cbd5e1">Spaces split names into two separate tokens. Use <tspan font-family="monospace" fill="#38bdf8">snake_case</tspan> or <tspan font-family="monospace" fill="#38bdf8">camelCase</tspan>.</text>
    </g>

    <!-- Rule 4 -->
    <g transform="translate(15, 204)">
      <rect width="390" height="48" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
      <text x="15" y="20" font-size="10.5" font-weight="bold" fill="#f87171">4. No Punctuation / Math Symbols</text>
      <text x="15" y="36" font-size="9" fill="#cbd5e1">Hyphens (<tspan font-family="monospace">-</tspan>), dots (<tspan font-family="monospace">.</tspan>), <tspan font-family="monospace">$</tspan>, <tspan font-family="monospace">@</tspan>, <tspan font-family="monospace">%</tspan> are reserved for operators/member access.</text>
    </g>

    <!-- Rule 5 -->
    <g transform="translate(15, 258)">
      <rect width="390" height="48" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
      <text x="15" y="20" font-size="10.5" font-weight="bold" fill="#f87171">5. No Reserved Keywords</text>
      <text x="15" y="36" font-size="9" fill="#cbd5e1">Cannot name a variable <tspan font-family="monospace" fill="#fca5a5">if, while, for, class, import, return</tspan>.</text>
    </g>

    <!-- Rule 6 -->
    <g transform="translate(15, 312)">
      <rect width="390" height="58" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
      <text x="15" y="20" font-size="10.5" font-weight="bold" fill="#34d399">6. Strict Case Sensitivity</text>
      <text x="15" y="36" font-size="9" fill="#cbd5e1"><tspan font-family="monospace" fill="#6ee7b7">studentAge</tspan>, <tspan font-family="monospace" fill="#6ee7b7">studentage</tspan>, and <tspan font-family="monospace" fill="#6ee7b7">STUDENTAGE</tspan> are 3 distinct memory slots!</text>
      <text x="15" y="50" font-size="8.5" fill="#94a3b8">Compilers map upper and lower ASCII bytes to distinct hash keys.</text>
    </g>
  </g>

  <!-- Right: Valid vs Invalid Comparison Matrix -->
  <g transform="translate(495, 95)">
    <rect width="420" height="385" rx="12" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
    <rect width="420" height="30" rx="8" fill="#334155"/>
    <text x="210" y="20" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Compliance Audit Table</text>

    <!-- Header Row -->
    <g transform="translate(10, 40)">
      <rect width="400" height="24" fill="#1e293b"/>
      <text x="15" y="16" font-size="10" font-weight="bold" fill="#38bdf8">Proposed Name</text>
      <text x="135" y="16" font-size="10" font-weight="bold" fill="#ffffff">Status</text>
      <text x="215" y="16" font-size="10" font-weight="bold" fill="#cbd5e1">Technical Reason</text>
    </g>

    <!-- Row 1 -->
    <g transform="translate(10, 70)">
      <rect width="400" height="32" rx="4" fill="#064e3b" stroke="#34d399" stroke-width="1"/>
      <text x="15" y="20" font-family="monospace" font-size="10" fill="#a7f3d0">student_mark</text>
      <text x="135" y="20" font-size="10" font-weight="bold" fill="#34d399">&#10003; VALID</text>
      <text x="215" y="20" font-size="8.5" fill="#cbd5e1">Letters &amp; underscore; starts with letter</text>
    </g>

    <!-- Row 2 -->
    <g transform="translate(10, 108)">
      <rect width="400" height="32" rx="4" fill="#450a0a" stroke="#ef4444" stroke-width="1"/>
      <text x="15" y="20" font-family="monospace" font-size="10" fill="#fca5a5">student mark</text>
      <text x="135" y="20" font-size="10" font-weight="bold" fill="#f87171">&#10007; INVALID</text>
      <text x="215" y="20" font-size="8.5" fill="#fca5a5">Contains illegal space character</text>
    </g>

    <!-- Row 3 -->
    <g transform="translate(10, 146)">
      <rect width="400" height="32" rx="4" fill="#450a0a" stroke="#ef4444" stroke-width="1"/>
      <text x="15" y="20" font-family="monospace" font-size="10" fill="#fca5a5">1st_place</text>
      <text x="135" y="20" font-size="10" font-weight="bold" fill="#f87171">&#10007; INVALID</text>
      <text x="215" y="20" font-size="8.5" fill="#fca5a5">Begins with a digit (must start with letter/_)</text>
    </g>

    <!-- Row 4 -->
    <g transform="translate(10, 184)">
      <rect width="400" height="32" rx="4" fill="#064e3b" stroke="#34d399" stroke-width="1"/>
      <text x="15" y="20" font-family="monospace" font-size="10" fill="#a7f3d0">first_place</text>
      <text x="135" y="20" font-size="10" font-weight="bold" fill="#34d399">&#10003; VALID</text>
      <text x="215" y="20" font-size="8.5" fill="#cbd5e1">Leading digit replaced with word</text>
    </g>

    <!-- Row 5 -->
    <g transform="translate(10, 222)">
      <rect width="400" height="32" rx="4" fill="#450a0a" stroke="#ef4444" stroke-width="1"/>
      <text x="15" y="20" font-family="monospace" font-size="10" fill="#fca5a5">calculate-tax</text>
      <text x="135" y="20" font-size="10" font-weight="bold" fill="#f87171">&#10007; INVALID</text>
      <text x="215" y="20" font-size="8.5" fill="#fca5a5">Hyphen parsed as subtraction operator</text>
    </g>

    <!-- Row 6 -->
    <g transform="translate(10, 260)">
      <rect width="400" height="32" rx="4" fill="#450a0a" stroke="#ef4444" stroke-width="1"/>
      <text x="15" y="20" font-family="monospace" font-size="10" fill="#fca5a5">while</text>
      <text x="135" y="20" font-size="10" font-weight="bold" fill="#f87171">&#10007; INVALID</text>
      <text x="215" y="20" font-size="8.5" fill="#fca5a5">Reserved control structure keyword</text>
    </g>

    <!-- Row 7 -->
    <g transform="translate(10, 298)">
      <rect width="400" height="32" rx="4" fill="#064e3b" stroke="#34d399" stroke-width="1"/>
      <text x="15" y="20" font-family="monospace" font-size="10" fill="#a7f3d0">while_loop</text>
      <text x="135" y="20" font-size="10" font-weight="bold" fill="#34d399">&#10003; VALID</text>
      <text x="215" y="20" font-size="8.5" fill="#cbd5e1">Joined with underscore; unique token</text>
    </g>

    <!-- Row 8 -->
    <g transform="translate(10, 336)">
      <rect width="400" height="32" rx="4" fill="#064e3b" stroke="#34d399" stroke-width="1"/>
      <text x="15" y="20" font-family="monospace" font-size="10" fill="#a7f3d0">_internal_id</text>
      <text x="135" y="20" font-size="10" font-weight="bold" fill="#34d399">&#10003; VALID</text>
      <text x="215" y="20" font-size="8.5" fill="#cbd5e1">Leading underscore allowed for private fields</text>
    </g>
  </g>
</svg>
""")

SVG_MEMORY_VARIABLES_VS_CONSTANTS = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Memory Cell Allocation: Mutable Variables vs. Immutable Constants</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Physical RAM architecture, register overwriting, and static vs dynamic type binding</text>

  <!-- Left: Variable Cell (user_score) -->
  <g transform="translate(45, 95)">
    <rect width="420" height="385" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="420" height="30" rx="8" fill="#0284c7"/>
    <text x="210" y="20" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1. VARIABLE: Mutable Storage Cell</text>

    <!-- RAM Box Graphic -->
    <g transform="translate(30, 45)">
      <!-- Memory Cell Slot -->
      <rect width="360" height="130" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
      <text x="15" y="25" font-size="11" font-weight="bold" fill="#38bdf8">RAM Cell Address: <tspan font-family="monospace">0x7FFF5FBFF8C0</tspan></text>
      <text x="15" y="44" font-size="10" fill="#94a3b8">Identifier Label: <tspan font-family="monospace" fill="#ffffff" font-weight="bold">user_score</tspan></text>

      <!-- Old value crossed out -->
      <rect x="30" y="60" width="100" height="50" rx="6" fill="#0f172a" stroke="#64748b"/>
      <text x="80" y="92" font-size="18" font-weight="bold" fill="#64748b" text-anchor="middle">50</text>
      <line x1="35" y1="65" x2="125" y2="105" stroke="#ef4444" stroke-width="2.5"/>

      <!-- Arrow overwriting -->
      <line x1="140" y1="85" x2="195" y2="85" stroke="#38bdf8" stroke-width="2.5"/>
      <polygon points="195,80 205,85 195,90" fill="#38bdf8"/>
      <text x="168" y="75" font-size="8.5" fill="#38bdf8" text-anchor="middle">Update</text>

      <!-- New value -->
      <rect x="210" y="60" width="120" height="50" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
      <text x="270" y="92" font-size="20" font-weight="bold" fill="#34d399" text-anchor="middle">75</text>
    </g>

    <!-- Execution Code Walkthrough -->
    <g transform="translate(30, 190)">
      <rect width="360" height="75" rx="6" fill="#1e1b4b" stroke="#818cf8"/>
      <text x="15" y="20" font-family="monospace" font-size="10" fill="#c7d2fe"># Python Variable Reassignment</text>
      <text x="15" y="38" font-family="monospace" font-size="10.5" fill="#38bdf8">user_score = 50   <tspan fill="#94a3b8"># Allocated &amp; initialized to 50</tspan></text>
      <text x="15" y="56" font-family="monospace" font-size="10.5" fill="#34d399">user_score = 75   <tspan fill="#94a3b8"># 50 erased; cell now stores 75</tspan></text>
    </g>

    <!-- Summary Points -->
    <g transform="translate(30, 280)">
      <text x="0" y="15" font-size="10.5" font-weight="bold" fill="#38bdf8">&#9889; Variable Characteristics:</text>
      <text x="0" y="34" font-size="9" fill="#cbd5e1">&#8226; Contents can be written over repeatedly during runtime.</text>
      <text x="0" y="50" font-size="9" fill="#cbd5e1">&#8226; Memory label remains identical; underlying bits change.</text>
      <text x="0" y="66" font-size="9" fill="#cbd5e1">&#8226; In Python, data type adapts dynamically during assignment.</text>
      <text x="0" y="82" font-size="9" fill="#cbd5e1">&#8226; In C++/Java, variable type is statically locked in memory.</text>
    </g>
  </g>

  <!-- Right: Constant Cell (GRAVITY) -->
  <g transform="translate(495, 95)">
    <rect width="420" height="385" rx="12" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="420" height="30" rx="8" fill="#d97706"/>
    <text x="210" y="20" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2. CONSTANT: Locked Immutable Cell</text>

    <!-- RAM Box Graphic with Padlock Cage -->
    <g transform="translate(30, 45)">
      <rect width="360" height="130" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
      <text x="15" y="25" font-size="11" font-weight="bold" fill="#fbbf24">RAM Cell Address: <tspan font-family="monospace">0x7FFF5FBFF8D8</tspan></text>
      <text x="15" y="44" font-size="10" fill="#94a3b8">Identifier Label: <tspan font-family="monospace" fill="#ffffff" font-weight="bold">GRAVITY</tspan> <tspan fill="#f59e0b">(LOCKED)</tspan></text>

      <!-- Constant Locked Value with Steel Grate -->
      <rect x="30" y="60" width="130" height="50" rx="6" fill="#451a03" stroke="#f59e0b" stroke-width="2"/>
      <!-- Grate lines -->
      <line x1="55" y1="60" x2="55" y2="110" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="3"/>
      <line x1="85" y1="60" x2="85" y2="110" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="3"/>
      <line x1="115" y1="60" x2="115" y2="110" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="3"/>
      <text x="95" y="92" font-size="20" font-weight="bold" fill="#fbbf24" text-anchor="middle">9.80</text>

      <!-- Bouncing Arrow Update Attempt -->
      <path d="M 280,65 Q 210,85 190,85" fill="none" stroke="#ef4444" stroke-width="2.5"/>
      <polygon points="190,85 200,80 198,90" fill="#ef4444"/>
      <!-- Bounce recoil -->
      <path d="M 195,85 Q 220,105 280,105" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="3"/>
      <text x="255" y="60" font-size="9" font-weight="bold" fill="#f87171">Assign 10.5</text>
      <text x="285" y="100" font-size="8.5" font-weight="bold" fill="#ef4444">BOUNCE / ERROR!</text>
    </g>

    <!-- Execution Code Walkthrough -->
    <g transform="translate(30, 190)">
      <rect width="360" height="75" rx="6" fill="#1e1b4b" stroke="#ef4444"/>
      <text x="15" y="20" font-family="monospace" font-size="10" fill="#fca5a5">// C++ / Java Constant Enforcement</text>
      <text x="15" y="38" font-family="monospace" font-size="10.5" fill="#38bdf8">const double GRAVITY = 9.8;   <tspan fill="#94a3b8">// Locked</tspan></text>
      <text x="15" y="56" font-family="monospace" font-size="10.5" fill="#f87171">GRAVITY = 10.5;   <tspan fill="#fca5a5">// COMPILE ERROR: Read-only!</tspan></text>
    </g>

    <!-- Summary Points -->
    <g transform="translate(30, 280)">
      <text x="0" y="15" font-size="10.5" font-weight="bold" fill="#fbbf24">&#128274; Constant Characteristics:</text>
      <text x="0" y="34" font-size="9" fill="#cbd5e1">&#8226; Initialized once; locked against future memory writes.</text>
      <text x="0" y="50" font-size="9" fill="#cbd5e1">&#8226; C++ uses <tspan font-family="monospace" fill="#fbbf24">const</tspan>; Java uses <tspan font-family="monospace" fill="#fbbf24">final</tspan> keyword modifiers.</text>
      <text x="0" y="66" font-size="9" fill="#cbd5e1">&#8226; Python uses uppercase convention (<tspan font-family="monospace" fill="#fbbf24">PI = 3.14159</tspan>) for constants.</text>
      <text x="0" y="82" font-size="9" fill="#cbd5e1">&#8226; Prevents accidental modification of physical constants in code.</text>
    </g>
  </g>
</svg>
""")

SVG_INPUT_OUTPUT_CASTING_PIPELINE = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Input, Type-Casting Pipeline, &amp; Console Output Mechanics</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Keyboard string capture, explicit numerical casting, arithmetic processing, and formatted f-string delivery</text>

  <!-- Top Pipeline Flow (4 Horizontal Stages) -->
  <g transform="translate(45, 95)">
    <!-- Stage 1: Console Input (Keyboard) -->
    <g transform="translate(0, 0)">
      <rect width="190" height="150" rx="8" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
      <rect width="190" height="26" rx="6" fill="#0284c7"/>
      <text x="95" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. User Console Input</text>
      <text x="15" y="48" font-size="9.5" font-weight="bold" fill="#38bdf8">&#8226; Keyboard Capture:</text>
      <text x="15" y="66" font-size="8.5" fill="#cbd5e1">Prompts user on console.</text>
      <rect x="15" y="78" width="160" height="30" rx="4" fill="#1e293b"/>
      <text x="25" y="97" font-family="monospace" font-size="9" fill="#7dd3fc">input("Age: ")</text>
      <text x="15" y="125" font-size="8" font-weight="bold" fill="#f59e0b">&#9888; CRITICAL TRAP:</text>
      <text x="15" y="138" font-size="8" fill="#fde68a">Returns raw string "16"</text>
    </g>

    <!-- Arrow 1 -> 2 -->
    <g transform="translate(195, 65)">
      <line x1="0" y1="0" x2="25" y2="0" stroke="#38bdf8" stroke-width="2.5"/>
      <polygon points="25,-4 32,0 25,4" fill="#38bdf8"/>
    </g>

    <!-- Stage 2: Explicit Type-Casting -->
    <g transform="translate(230, 0)">
      <rect width="200" height="150" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
      <rect width="200" height="26" rx="6" fill="#d97706"/>
      <text x="100" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Explicit Type Casting</text>
      <text x="15" y="48" font-size="9.5" font-weight="bold" fill="#fbbf24">&#8226; Binary Re-encoding:</text>
      <text x="15" y="66" font-size="8.5" fill="#cbd5e1">Converts ASCII text to int/float.</text>
      <rect x="15" y="78" width="170" height="30" rx="4" fill="#1e293b"/>
      <text x="25" y="97" font-family="monospace" font-size="9" fill="#fde68a">int("16") &#8594; 16</text>
      <text x="15" y="125" font-size="8" font-weight="bold" fill="#34d399">&#10003; Memory Allocation:</text>
      <text x="15" y="138" font-size="8" fill="#a7f3d0">Stored as 2's complement int</text>
    </g>

    <!-- Arrow 2 -> 3 -->
    <g transform="translate(435, 65)">
      <line x1="0" y1="0" x2="25" y2="0" stroke="#38bdf8" stroke-width="2.5"/>
      <polygon points="25,-4 32,0 25,4" fill="#38bdf8"/>
    </g>

    <!-- Stage 3: Arithmetic / Logic -->
    <g transform="translate(470, 0)">
      <rect width="190" height="150" rx="8" fill="#0f172a" stroke="#818cf8" stroke-width="1.5"/>
      <rect width="190" height="26" rx="6" fill="#4f46e5"/>
      <text x="95" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. CPU Processing</text>
      <text x="15" y="48" font-size="9.5" font-weight="bold" fill="#a5b4fc">&#8226; Mathematical Engine:</text>
      <text x="15" y="66" font-size="8.5" fill="#cbd5e1">Evaluates valid operations.</text>
      <rect x="15" y="78" width="160" height="30" rx="4" fill="#1e293b"/>
      <text x="25" y="97" font-family="monospace" font-size="9" fill="#c7d2fe">next_age = 16 + 1</text>
      <text x="15" y="125" font-size="8" font-weight="bold" fill="#38bdf8">&#10003; Result Generated:</text>
      <text x="15" y="138" font-size="8" fill="#7dd3fc">Numerical value: 17</text>
    </g>

    <!-- Arrow 3 -> 4 -->
    <g transform="translate(665, 65)">
      <line x1="0" y1="0" x2="25" y2="0" stroke="#38bdf8" stroke-width="2.5"/>
      <polygon points="25,-4 32,0 25,4" fill="#38bdf8"/>
    </g>

    <!-- Stage 4: Formatted Output -->
    <g transform="translate(700, 0)">
      <rect width="170" height="150" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
      <rect width="170" height="26" rx="6" fill="#059669"/>
      <text x="85" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4. Formatted Output</text>
      <text x="15" y="48" font-size="9.5" font-weight="bold" fill="#34d399">&#8226; Console Display:</text>
      <text x="15" y="66" font-size="8.5" fill="#cbd5e1">f-string interpolation.</text>
      <rect x="10" y="78" width="150" height="30" rx="4" fill="#1e293b"/>
      <text x="15" y="97" font-family="monospace" font-size="8" fill="#6ee7b7">print(f"Age: {17}")</text>
      <text x="15" y="125" font-size="8" font-weight="bold" fill="#34d399">&#10003; Delivered:</text>
      <text x="15" y="138" font-size="8" fill="#a7f3d0">"Next year you are 17"</text>
    </g>
  </g>

  <!-- Bottom Half: Comparison of Uncast Bug vs Correct Casting -->
  <g transform="translate(45, 265)">
    <!-- Bug Box (Left) -->
    <g transform="translate(0, 0)">
      <rect width="420" height="210" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
      <rect width="420" height="26" rx="8" fill="#dc2626"/>
      <text x="210" y="18" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">&#9888; The Fatal Uncast String Bug (Common Trap)</text>

      <g transform="translate(15, 38)">
        <rect width="390" height="70" rx="6" fill="#1e1b4b" stroke="#ef4444"/>
        <text x="15" y="20" font-family="monospace" font-size="9.5" fill="#fca5a5">user_num = input("Enter number: ")  # user types 5</text>
        <text x="15" y="40" font-family="monospace" font-size="9.5" fill="#f87171">result = user_num + 10</text>
        <text x="15" y="58" font-family="monospace" font-size="9" fill="#f87171">&#10007; TypeError: can only concatenate str to str, not int</text>
      </g>

      <text x="15" y="130" font-size="9.5" font-weight="bold" fill="#f87171">&#8226; Why it fails:</text>
      <text x="15" y="148" font-size="9" fill="#cbd5e1"><tspan font-family="monospace">input()</tspan> returns the text string <tspan font-family="monospace">"5"</tspan>. Python cannot add raw text to an integer.</text>
      <text x="15" y="166" font-size="9" fill="#cbd5e1">If both were strings, <tspan font-family="monospace">"5" + "10"</tspan> results in concatenation <tspan font-family="monospace">"510"</tspan>, NOT 15!</text>
    </g>

    <!-- Fix Box (Right) -->
    <g transform="translate(450, 0)">
      <rect width="420" height="210" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
      <rect width="420" height="26" rx="8" fill="#059669"/>
      <text x="210" y="18" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">&#10003; Professional Casting &amp; Clean Implementation</text>

      <g transform="translate(15, 38)">
        <rect width="390" height="70" rx="6" fill="#1e1b4b" stroke="#10b981"/>
        <text x="15" y="20" font-family="monospace" font-size="9.5" fill="#a7f3d0"># Explicit Integer or Float Casting</text>
        <text x="15" y="40" font-family="monospace" font-size="9.5" fill="#38bdf8">user_num = int(input("Enter number: "))  # cast to 5</text>
        <text x="15" y="58" font-family="monospace" font-size="9.5" fill="#34d399">result = user_num + 10                 # evaluates to 15</text>
      </g>

      <text x="15" y="130" font-size="9.5" font-weight="bold" fill="#34d399">&#8226; Industry Standard Best Practices:</text>
      <text x="15" y="148" font-size="9" fill="#cbd5e1">&#8226; Nest casting directly: <tspan font-family="monospace" fill="#38bdf8">price = float(input("Price: "))</tspan></text>
      <text x="15" y="166" font-size="9" fill="#cbd5e1">&#8226; Use formatted f-strings: <tspan font-family="monospace" fill="#38bdf8">print(f"Total price is KES {price:.2f}")</tspan></text>
      <text x="15" y="184" font-size="9" fill="#cbd5e1">&#8226; In C++, <tspan font-family="monospace" fill="#38bdf8">std::cin &gt;&gt; price</tspan> automatically casts based on declared type.</text>
    </g>
  </g>
</svg>
""")

SVG_OPERATOR_PRECEDENCE_PARSE_TREE = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Operator Precedence Hierarchy &amp; Parse Tree Reduction</text>
  <text x="480" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Step-by-step mathematical evaluation of compound expression: 5 + 3 * 2 &gt; 10 and not 4 &lt; 2</text>

  <!-- Left: 8-Level Operator Precedence Scale -->
  <g transform="translate(45, 90)">
    <rect width="320" height="390" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="320" height="28" rx="8" fill="#0284c7"/>
    <text x="160" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Operator Precedence Scale</text>

    <!-- Ladder items -->
    <g transform="translate(15, 38)">
      <rect width="290" height="34" rx="4" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
      <text x="10" y="22" font-size="10" font-weight="bold" fill="#f87171">1. Parentheses ( )</text>
      <text x="180" y="22" font-size="9" fill="#fca5a5">[Forces first priority]</text>
    </g>

    <g transform="translate(15, 78)">
      <rect width="290" height="34" rx="4" fill="#1e293b" stroke="#f59e0b"/>
      <text x="10" y="22" font-size="10" font-weight="bold" fill="#fbbf24">2. Exponentiation **</text>
      <text x="180" y="22" font-size="9" fill="#fde68a">Power operations</text>
    </g>

    <g transform="translate(15, 118)">
      <rect width="290" height="34" rx="4" fill="#1e293b" stroke="#38bdf8"/>
      <text x="10" y="22" font-size="10" font-weight="bold" fill="#38bdf8">3. Multiplicative (*, /, //, %)</text>
      <text x="180" y="22" font-size="9" fill="#bae6fd">Mult, Div, Modulo</text>
    </g>

    <g transform="translate(15, 158)">
      <rect width="290" height="34" rx="4" fill="#1e293b" stroke="#38bdf8"/>
      <text x="10" y="22" font-size="10" font-weight="bold" fill="#38bdf8">4. Additive (+, -)</text>
      <text x="180" y="22" font-size="9" fill="#bae6fd">Add, Subtract</text>
    </g>

    <g transform="translate(15, 198)">
      <rect width="290" height="34" rx="4" fill="#1e293b" stroke="#10b981"/>
      <text x="10" y="22" font-size="10" font-weight="bold" fill="#34d399">5. Relational (==, !=, &gt;, &lt;, &gt;=, &lt;=)</text>
      <text x="195" y="22" font-size="9" fill="#a7f3d0">Comparisons</text>
    </g>

    <g transform="translate(15, 238)">
      <rect width="290" height="34" rx="4" fill="#1e293b" stroke="#818cf8"/>
      <text x="10" y="22" font-size="10" font-weight="bold" fill="#a5b4fc">6. Logical NOT (not)</text>
      <text x="180" y="22" font-size="9" fill="#c7d2fe">Inverts truth state</text>
    </g>

    <g transform="translate(15, 278)">
      <rect width="290" height="34" rx="4" fill="#1e293b" stroke="#818cf8"/>
      <text x="10" y="22" font-size="10" font-weight="bold" fill="#a5b4fc">7. Logical AND (and)</text>
      <text x="180" y="22" font-size="9" fill="#c7d2fe">Both must be True</text>
    </g>

    <g transform="translate(15, 318)">
      <rect width="290" height="34" rx="4" fill="#1e293b" stroke="#64748b"/>
      <text x="10" y="22" font-size="10" font-weight="bold" fill="#94a3b8">8. Logical OR (or)</text>
      <text x="180" y="22" font-size="9" fill="#cbd5e1">[Evaluated last]</text>
    </g>
  </g>

  <!-- Right: Step-by-Step Parse Tree Collapse -->
  <g transform="translate(390, 90)">
    <rect width="525" height="390" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="525" height="28" rx="8" fill="#059669"/>
    <text x="262" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Step-by-Step Parse Tree Evaluation</text>

    <!-- Expression Top Box -->
    <g transform="translate(20, 38)">
      <rect width="485" height="36" rx="6" fill="#1e1b4b" stroke="#38bdf8"/>
      <text x="242" y="23" font-family="monospace" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">5 + 3 * 2 &gt; 10 and not 4 &lt; 2</text>
    </g>

    <!-- Step 1: Multiplication -->
    <g transform="translate(20, 85)">
      <rect width="485" height="42" rx="6" fill="#1e293b" stroke="#334155"/>
      <circle cx="25" cy="21" r="12" fill="#0284c7"/>
      <text x="25" y="25" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">1</text>
      <text x="48" y="17" font-size="10" font-weight="bold" fill="#38bdf8">Multiplication: <tspan font-family="monospace" fill="#ffffff">3 * 2 = 6</tspan></text>
      <text x="48" y="32" font-family="monospace" font-size="9.5" fill="#cbd5e1">&#8594; 5 + 6 &gt; 10 and not 4 &lt; 2</text>
    </g>

    <!-- Step 2: Addition -->
    <g transform="translate(20, 137)">
      <rect width="485" height="42" rx="6" fill="#1e293b" stroke="#334155"/>
      <circle cx="25" cy="21" r="12" fill="#0284c7"/>
      <text x="25" y="25" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">2</text>
      <text x="48" y="17" font-size="10" font-weight="bold" fill="#38bdf8">Addition: <tspan font-family="monospace" fill="#ffffff">5 + 6 = 11</tspan></text>
      <text x="48" y="32" font-family="monospace" font-size="9.5" fill="#cbd5e1">&#8594; 11 &gt; 10 and not 4 &lt; 2</text>
    </g>

    <!-- Step 3: Relational 1 -->
    <g transform="translate(20, 189)">
      <rect width="485" height="42" rx="6" fill="#1e293b" stroke="#334155"/>
      <circle cx="25" cy="21" r="12" fill="#d97706"/>
      <text x="25" y="25" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">3</text>
      <text x="48" y="17" font-size="10" font-weight="bold" fill="#fbbf24">First Comparison: <tspan font-family="monospace" fill="#ffffff">11 &gt; 10 &#8594; True</tspan></text>
      <text x="48" y="32" font-family="monospace" font-size="9.5" fill="#cbd5e1">&#8594; True and not 4 &lt; 2</text>
    </g>

    <!-- Step 4: Relational 2 -->
    <g transform="translate(20, 241)">
      <rect width="485" height="42" rx="6" fill="#1e293b" stroke="#334155"/>
      <circle cx="25" cy="21" r="12" fill="#d97706"/>
      <text x="25" y="25" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">4</text>
      <text x="48" y="17" font-size="10" font-weight="bold" fill="#fbbf24">Second Comparison: <tspan font-family="monospace" fill="#ffffff">4 &lt; 2 &#8594; False</tspan></text>
      <text x="48" y="32" font-family="monospace" font-size="9.5" fill="#cbd5e1">&#8594; True and not False</text>
    </g>

    <!-- Step 5: Logical NOT -->
    <g transform="translate(20, 293)">
      <rect width="485" height="42" rx="6" fill="#1e293b" stroke="#334155"/>
      <circle cx="25" cy="21" r="12" fill="#4f46e5"/>
      <text x="25" y="25" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">5</text>
      <text x="48" y="17" font-size="10" font-weight="bold" fill="#a5b4fc">Logical NOT: <tspan font-family="monospace" fill="#ffffff">not False &#8594; True</tspan></text>
      <text x="48" y="32" font-family="monospace" font-size="9.5" fill="#cbd5e1">&#8594; True and True</text>
    </g>

    <!-- Step 6: Logical AND Final Result -->
    <g transform="translate(20, 342)">
      <rect width="485" height="38" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
      <circle cx="25" cy="19" r="12" fill="#059669"/>
      <text x="25" y="23" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">6</text>
      <text x="48" y="15" font-size="10" font-weight="bold" fill="#34d399">Logical AND (Final Result): <tspan font-family="monospace" fill="#ffffff">True and True</tspan></text>
      <text x="48" y="29" font-family="monospace" font-size="11" font-weight="bold" fill="#6ee7b7">&#8594; FINAL VALUE: True</text>
    </g>
  </g>
</svg>
""")

SVG_DAIRY_COOPERATIVE_CASE_STUDY = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Applied Case Study: Nyahururu Automated Dairy Milk Aggregator</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Data flow architecture: Mass Sensor &#8594; Constant Density Division &#8594; Floor Division // &amp; Modulo % &#8594; Boolean Bonus</text>

  <!-- Left: System Input & Constants -->
  <g transform="translate(45, 95)">
    <rect width="270" height="385" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#0284c7"/>
    <text x="135" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Inputs &amp; Locked Constants</text>

    <!-- Constant -->
    <g transform="translate(15, 40)">
      <rect width="240" height="65" rx="6" fill="#1e293b" stroke="#f59e0b"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#fbbf24">&#128274; Constant Definition:</text>
      <text x="15" y="38" font-family="monospace" font-size="10" fill="#ffffff">DENSITY_CONVERSION = 1.03</text>
      <text x="15" y="54" font-size="8.5" fill="#94a3b8">(1 Liter milk = 1.03 kg mass)</text>
    </g>

    <!-- Inputs -->
    <g transform="translate(15, 115)">
      <rect width="240" height="95" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#38bdf8">&#128187; Captured Sensor Inputs:</text>
      <text x="15" y="38" font-family="monospace" font-size="9" fill="#ffffff">farmer_name = "Wanjiku"</text>
      <text x="15" y="56" font-family="monospace" font-size="9" fill="#ffffff">milk_mass_kg = 103.0</text>
      <text x="15" y="74" font-size="8" fill="#cbd5e1">Captured via float(input())</text>
      <text x="15" y="88" font-size="8" fill="#a7f3d0">&#10003; Stored as float data type</text>
    </g>

    <g transform="translate(15, 220)">
      <rect width="240" height="145" rx="6" fill="#1e1b4b" stroke="#818cf8"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#c7d2fe">&#128221; Required Variables:</text>
      <text x="15" y="38" font-size="8.5" fill="#cbd5e1">&#8226; <tspan font-family="monospace" fill="#38bdf8">farmer_name</tspan>: str</text>
      <text x="15" y="54" font-size="8.5" fill="#cbd5e1">&#8226; <tspan font-family="monospace" fill="#38bdf8">milk_mass_kg</tspan>: float</text>
      <text x="15" y="70" font-size="8.5" fill="#cbd5e1">&#8226; <tspan font-family="monospace" fill="#38bdf8">milk_volume_liters</tspan>: float</text>
      <text x="15" y="86" font-size="8.5" fill="#cbd5e1">&#8226; <tspan font-family="monospace" fill="#38bdf8">complete_bottles</tspan>: int</text>
      <text x="15" y="102" font-size="8.5" fill="#cbd5e1">&#8226; <tspan font-family="monospace" fill="#38bdf8">leftover_liters</tspan>: float</text>
      <text x="15" y="118" font-size="8.5" fill="#cbd5e1">&#8226; <tspan font-family="monospace" fill="#38bdf8">premium_bonus</tspan>: bool</text>
      <text x="15" y="134" font-size="8.5" fill="#fbbf24">&#8226; <tspan font-family="monospace" fill="#fbbf24">DENSITY_CONVERSION</tspan>: const</text>
    </g>
  </g>

  <!-- Middle: Processing & Arithmetic Pipeline -->
  <g transform="translate(345, 95)">
    <rect width="270" height="385" rx="10" fill="#0f172a" stroke="#818cf8" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#4f46e5"/>
    <text x="135" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Mathematical Processing</text>

    <!-- Formula 1: Volume -->
    <g transform="translate(15, 38)">
      <rect width="240" height="75" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="10" y="18" font-size="9.5" font-weight="bold" fill="#38bdf8">Step 1: Volume Calculation</text>
      <text x="10" y="36" font-family="monospace" font-size="8.5" fill="#ffffff">volume = mass / DENSITY</text>
      <text x="10" y="52" font-family="monospace" font-size="8.5" fill="#7dd3fc">volume = 103.0 / 1.03</text>
      <text x="10" y="68" font-size="9" font-weight="bold" fill="#34d399">&#8594; 100.0 Liters</text>
    </g>

    <!-- Formula 2: Bottles & Modulo -->
    <g transform="translate(15, 122)">
      <rect width="240" height="110" rx="6" fill="#1e293b" stroke="#f59e0b"/>
      <text x="10" y="18" font-size="9.5" font-weight="bold" fill="#fbbf24">Step 2: Bottles &amp; Leftovers</text>
      <text x="10" y="36" font-family="monospace" font-size="8.5" fill="#ffffff">bottles = int(volume // 2)</text>
      <text x="10" y="50" font-family="monospace" font-size="8.5" fill="#fde68a">100.0 // 2 &#8594; 50 Bottles</text>
      <text x="10" y="70" font-family="monospace" font-size="8.5" fill="#ffffff">leftover = volume % 2</text>
      <text x="10" y="86" font-family="monospace" font-size="8.5" fill="#fde68a">100.0 % 2 &#8594; 0.0 Liters</text>
      <text x="10" y="102" font-size="8.5" fill="#a7f3d0">&#10003; Modulo cuts zero remainder</text>
    </g>

    <!-- Formula 3: Boolean Bonus -->
    <g transform="translate(15, 240)">
      <rect width="240" height="125" rx="6" fill="#1e293b" stroke="#10b981"/>
      <text x="10" y="18" font-size="9.5" font-weight="bold" fill="#34d399">Step 3: Premium Bonus Logic</text>
      <text x="10" y="34" font-family="monospace" font-size="8" fill="#ffffff">bonus = (volume &gt; 50.0) and</text>
      <text x="65" y="48" font-family="monospace" font-size="8" fill="#ffffff">(leftover == 0.0)</text>
      <text x="10" y="68" font-family="monospace" font-size="8" fill="#a7f3d0">(100.0 &gt; 50.0) &#8594; True</text>
      <text x="10" y="84" font-family="monospace" font-size="8" fill="#a7f3d0">(0.0 == 0.0) &#8594; True</text>
      <text x="10" y="100" font-family="monospace" font-size="8" fill="#6ee7b7">True and True &#8594; True</text>
      <text x="10" y="118" font-size="9" font-weight="bold" fill="#34d399">&#8594; premium_bonus = True</text>
    </g>
  </g>

  <!-- Right: Formatted Delivery Summary Receipt -->
  <g transform="translate(645, 95)">
    <rect width="270" height="385" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#059669"/>
    <text x="135" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Automated Delivery Receipt</text>

    <!-- Console Output Simulation -->
    <g transform="translate(15, 40)">
      <rect width="240" height="260" rx="8" fill="#000000" stroke="#334155"/>
      <text x="120" y="24" font-family="monospace" font-size="9" font-weight="bold" fill="#fbbf24" text-anchor="middle">NYAHURURU DAIRY CO-OP</text>
      <text x="120" y="38" font-family="monospace" font-size="8" fill="#64748b" text-anchor="middle">-------------------------</text>
      
      <text x="15" y="60" font-family="monospace" font-size="8.5" fill="#cbd5e1">Farmer: <tspan fill="#38bdf8">Wanjiku</tspan></text>
      <text x="15" y="80" font-family="monospace" font-size="8.5" fill="#cbd5e1">Delivered: <tspan fill="#ffffff">103.00 kg</tspan></text>
      <text x="15" y="100" font-family="monospace" font-size="8.5" fill="#cbd5e1">Calculated Vol: <tspan fill="#34d399">100.00 L</tspan></text>
      <text x="15" y="120" font-family="monospace" font-size="8.5" fill="#cbd5e1">2L Bottles: <tspan fill="#fbbf24">50</tspan></text>
      <text x="15" y="140" font-family="monospace" font-size="8.5" fill="#cbd5e1">Leftover: <tspan fill="#a5b4fc">0.00 L</tspan></text>
      
      <text x="120" y="165" font-family="monospace" font-size="8" fill="#64748b" text-anchor="middle">-------------------------</text>
      <text x="15" y="185" font-family="monospace" font-size="9" font-weight="bold" fill="#34d399">PREMIUM BONUS: AWARDED</text>
      <text x="15" y="202" font-family="monospace" font-size="8" fill="#a7f3d0">(Bonus Flag: True)</text>

      <text x="120" y="235" font-family="monospace" font-size="8" fill="#38bdf8" text-anchor="middle">Processed via Python 3 Engine</text>
    </g>

    <g transform="translate(15, 310)">
      <rect width="240" height="55" rx="6" fill="#1e293b"/>
      <text x="10" y="20" font-size="9" font-weight="bold" fill="#34d399">&#10003; Verification Complete:</text>
      <text x="10" y="36" font-size="8" fill="#cbd5e1">All variables cleanly typed and</text>
      <text x="10" y="48" font-size="8" fill="#cbd5e1">verified against rubric criteria.</text>
    </g>
  </g>
</svg>
""")

# =====================================================================
# CURRICULUM DEFINITIONS FOR GRADE 10 TOPIC 14
# =====================================================================

def build_topic14_curriculum():
    return [
        # =====================================================================
        # LEARNING UNIT 1: Elementary Elements of a Program and Naming Identifiers
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Elementary Elements of a Program and Naming Identifiers",
            "unit_description": "The six foundational building blocks of software syntax, compiler lexical rules, reserved keywords, and standard conventions for naming legal identifiers.",
            "lesson_title": "Lesson 57: Elementary Elements of a Program and Naming Identifiers",
            "pages": [
                # Page 1: Introduction, The Mailroom Cubby Analogy & Core Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Elementary Elements and Identifier Syntax",
                        "content": {
                            "goal": "Master the six atomic elements of software syntax, understand how the computer's memory assigns labels to storage cells, and distinguish between identifiers, keywords, literals, and data types."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Introduction & The 'Mailroom Cubby' Analogy",
                        "content": {
                            "text": "Imagine a busy school mailroom containing hundreds of wooden mail cubbies. To keep correspondence organized, every cubby has a unique plastic name label taped to the front (e.g., 'Principal', 'Science Dept', 'Library'). When a letter arrives, the clerk places it into the matching cubby. If the librarian receives a new package, the old letter is removed, and the new package is placed inside. The label remains exactly the same, but the physical item inside changes constantly.\n\nIn computer science, **the computer's RAM is a massive mailroom containing billions of microscopic storage cells**. We cannot navigate memory using raw, volatile hexadecimal physical address numbers (such as `0x7FFF5FBFF8C0`); instead, we tape human-readable 'name labels' onto these storage cells so our program can find and manipulate them easily. These names are called **identifiers**. The storage boxes whose contents can change during execution are called **variables**; if we lock a box so its contents can never be changed once set, it is called a **constant**."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "The Six Elementary Elements of Software Architecture",
                        "content": {
                            "svg_content": SVG_ELEMENTARY_PROGRAM_ELEMENTS,
                            "caption": "The six atomic elements present across all programming languages: Program Structure, Syntax Grammar, Keywords, Identifiers, Data Types, and Standard Libraries."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Core Definitions in Software Syntax",
                        "content": {
                            "text": "Every programming language relies on a formal syntactic foundation:\n\n- **Identifier**: A user-defined name given to a variable, constant, function, class, or other program entity to reference its location in memory.\n- **Keyword (Reserved Word)**: A special word with a predefined meaning in a programming language's translator (compiler/interpreter) that cannot be used as a custom identifier (e.g., `if`, `while`, `def`, `class`, `import`).\n- **Literal**: A fixed, raw value written directly into source code (e.g., the number `5`, the decimal `3.14`, or the text string `\"Hello Nairobi\"`).\n- **Data Type**: A classification of data that tells the computer how to allocate memory, represent bits, and perform valid operations on a value.\n- **Standard Library**: A collection of pre-written, highly optimized modules and functions bundled with a programming language to simplify common tasks (such as Python's `math` or C++'s `<iostream>`)."
                        }
                    }
                ],

                # Page 2: The Six Elementary Elements & Lexical Architecture
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Six Elementary Elements of Software Architecture",
                        "content": {
                            "text": "Regardless of whether a programming language is interpreted or compiled, procedural or object-oriented, it is constructed from six fundamental elements:\n\n1. **Program Structure**: The structural organization of statements governing the sequence of execution. Modern programming structures fall into three classical paradigms: Sequence (linear top-to-bottom execution), Selection (conditional branching using `if/else`), and Iteration (repetitive loops using `while/for`).\n2. **Syntax Grammar**: The formal punctuation, indentation, and grammatical rules that dictate how valid statements must be constructed. Violating these rules triggers a **Syntax Error**, causing the compiler or interpreter to immediately halt execution before running any code.\n3. **Keywords**: Reserved vocabularies pre-allocated by language creators that dictate control structures, scope, and function definitions.\n4. **Identifiers**: Symbolic names created by developers to hold active data values, data structures, and subroutines.\n5. **Data Types**: Memory templates used to represent integers, floating-point real numbers, alphanumeric characters, text strings, and Boolean truth values.\n6. **Standard Libraries**: Built-in, high-speed software toolkits that save developers from rewriting complex mathematical, file, or network algorithms from scratch."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Source Code Syntax Highlighting in a Modern Editor",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Python_3._Source_Code_Coloring_in_Kate.png/800px-Python_3._Source_Code_Coloring_in_Kate.png",
                            "caption": "A code editor parsing Python source code: keywords, string literals, numerical literals, and identifiers are visually tokenized into distinct color categories by lexical analyzers.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "step_by_step_worked_example",
                        "title": "Worked Example: Lexical Token Classification",
                        "content": {
                            "goal": "Deconstruct a standard Python code statement into its elementary software tokens.",
                            "problem": "Classify every token in the statement: `import math; circle_radius = 7.5; if circle_radius > 0: area = math.pi * (circle_radius ** 2)`",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "step_title": "Identify Keywords (Reserved Words)",
                                    "step_description": "`import` (module loading keyword), `if` (conditional selection keyword)."
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Identify Identifiers (User & Library Names)",
                                    "step_description": "`math` (standard library module identifier), `circle_radius` (user-defined variable identifier), `area` (user-defined variable identifier), `pi` (library constant identifier)."
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Identify Literals (Raw Hardcoded Values)",
                                    "step_description": "`7.5` (floating-point numerical literal), `0` (integer numerical literal), `2` (integer exponent literal)."
                                },
                                {
                                    "step_number": 4,
                                    "step_title": "Identify Operators & Punctuation Grammar",
                                    "step_description": "`=` (assignment operator), `>` (relational comparison operator), `*` (multiplication operator), `**` (exponentiation operator), `;` and `:` and `.` and `()` (syntactic punctuation and member access)."
                                }
                            ],
                            "conclusion": "The statement combines program structure (selection), syntax grammar (colons and parentheses), keywords, identifiers, literals, and standard libraries into an executable instruction."
                        }
                    }
                ],

                # Page 3: Identifier Naming Rules and Compliance Matrix
                [
                    {
                        "type": "concept_explanation",
                        "title": "Rules for Drafting Valid Identifiers",
                        "content": {
                            "text": "To prevent ambiguity in compiler lexical analyzers (lexers), programming languages enforce strict rules for creating custom identifiers:\n\n1. **Allowed Character Set**: Identifiers can contain alphanumeric letters (`a-z`, `A-Z`), numerical digits (`0-9`), and underscores (`_`).\n2. **No Leading Digits**: An identifier **must** begin with a letter or an underscore. It can **never** start with a number (e.g., `1st_place` is illegal; `first_place` or `place_1` is legal).\n3. **No Whitespaces**: Spaces are strictly illegal inside identifiers because compilers treat spaces as token separators. Use `snake_case` (e.g., `student_mark`) or `camelCase` (e.g., `studentMark`) to join multiple words.\n4. **No Special Characters or Punctuation**: Symbols such as `-`, `$`, `@`, `%`, `!`, or `.` are prohibited. Hyphens (`-`) are parsed as subtraction operators, causing syntax crashes.\n5. **No Reserved Keywords**: You cannot name a variable `if`, `while`, `for`, `def`, `class`, or `const`.\n6. **Strict Case Sensitivity**: Identifiers are strictly case-sensitive. The identifiers `studentAge`, `studentage`, and `STUDENTAGE` point to three completely different memory addresses."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Identifier Construction Rules & Compliance Matrix",
                        "content": {
                            "svg_content": SVG_IDENTIFIER_NAMING_RULES_MATRIX,
                            "caption": "The six strict compiler rules for drafting valid identifiers and the technical diagnostic reasons why invalid tokens trigger syntax errors."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Identifier Compliance Directory",
                        "content": {
                            "text": "The table below reviews common proposed identifiers, their validity status, and the technical explanation for compiler compliance:\n\n- `student_mark`: **VALID** — Contains only letters and an underscore; begins with a letter.\n- `student mark`: **INVALID** — Contains a whitespace character (spaces are illegal).\n- `1st_place`: **INVALID** — Begins with a digit (must start with a letter or underscore).\n- `first_place`: **VALID** — Replaced the leading digit with letters.\n- `calculate-tax`: **INVALID** — Contains a hyphen (compilers read hyphens as subtraction operators).\n- `calculate_tax`: **VALID** — Replaced the hyphen with an underscore.\n- `if`: **INVALID** — Misuses a programming keyword (reserved control structure code).\n- `if_condition`: **VALID** — Combined with an underscore and descriptive noun, creating a legal unique token."
                        }
                    }
                ],

                # Page 4: Formative Knowledge Checks (4 MCQs)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 1: Identifying Invalid Identifiers",
                        "content": {
                            "question": "Which of the following proposed variable identifiers is INVALID in Python and will cause a SyntaxError?",
                            "options": [
                                "total_price",
                                "totalPrice",
                                "1st_student",
                                "_total_price"
                            ],
                            "correct_answer": "1st_student",
                            "explanation": "`1st_student` is invalid because an identifier cannot begin with a numerical digit. It must begin with a letter (a-z, A-Z) or an underscore (_)."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 2: Reserved Keywords",
                        "content": {
                            "question": "Why can the word 'while' NOT be used as a custom variable identifier in a Python program?",
                            "options": [
                                "It exceeds the maximum allowable character length of names.",
                                "It is a reserved programming keyword with a predefined loop control meaning in the language translator.",
                                "It contains an illegal hyphen character.",
                                "It begins with a lowercase letter, which is prohibited for variable names."
                            ],
                            "correct_answer": "It is a reserved programming keyword with a predefined loop control meaning in the language translator.",
                            "explanation": "Keywords are pre-allocated words reserved for the language's compiler/interpreter to dictate control flow. Redefining them as variable names would cause compiler ambiguity."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 3: Identifier Case Sensitivity",
                        "content": {
                            "question": "If a programmer declares 'studentScore = 85' and later writes 'print(studentscore)', what will happen in a case-sensitive language like Python?",
                            "options": [
                                "The computer will automatically convert both names to lowercase and display 85.",
                                "The interpreter will raise a NameError because 'studentScore' and 'studentscore' are treated as two completely distinct identifier labels.",
                                "The program will reassign studentScore to 0.",
                                "The compiler will halt with a hardware memory parity error."
                            ],
                            "correct_answer": "The interpreter will raise a NameError because 'studentScore' and 'studentscore' are treated as two completely distinct identifier labels.",
                            "explanation": "Programming languages are case-sensitive; uppercase and lowercase letters map to different ASCII/Unicode byte values, creating distinct memory references."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 4: Elementary Program Elements",
                        "content": {
                            "question": "Which elementary element of software is responsible for providing pre-written, reusable modules like 'math' or '<iostream>' so developers do not have to write basic utilities from scratch?",
                            "options": [
                                "Syntax Grammar",
                                "Keywords",
                                "Standard Libraries",
                                "Program Structure"
                            ],
                            "correct_answer": "Standard Libraries",
                            "explanation": "Standard Libraries are pre-compiled collections of functions, classes, and subroutines bundled with a language runtime to perform common mathematical, I/O, and string operations."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LEARNING UNIT 2: Variables, Constants, and Typing Systems
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Variables, Constants, and Typing Systems",
            "unit_description": "Memory allocation mechanics, mutable variables versus immutable constants, dynamic versus static typing systems, and cross-language declaration architectures.",
            "lesson_title": "Lesson 58: Variables, Constants, and Typing Systems",
            "pages": [
                # Page 1: Variables vs. Constants & Memory Register Architecture
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Memory Management, Mutability, and Typing",
                        "content": {
                            "goal": "Distinguish between mutable variables and immutable constants in RAM, and compare the architecture of statically typed and dynamically typed programming languages."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Core Definitions: Variables, Constants, and Memory Lifecycle",
                        "content": {
                            "text": "Every program requires storage locations to hold operational values:\n\n- **Variable**: A named memory location in RAM whose stored value can be modified, updated, or written over during active program execution.\n- **Constant**: A named memory location whose stored value is locked at initialization and cannot be changed or overwritten during execution.\n- **Declaration**: An instruction that alerts the compiler or interpreter to reserve a specific amount of memory for a named identifier and define its data type.\n- **Initialization**: The process of assigning an absolute initial starting value to a newly declared variable or constant."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Memory Location Cell Allocation: Variables vs. Constants",
                        "content": {
                            "svg_content": SVG_MEMORY_VARIABLES_VS_CONSTANTS,
                            "caption": "RAM cell architecture illustrating mutable variables (where new values overwrite old data) versus immutable constants (where compiler locks prevent memory updates)."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Random Access Memory (RAM) Physical Storage Cells",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Swissbit_2GB_PC2-6400_DDR2_SO-DIMM.jpg/800px-Swissbit_2GB_PC2-6400_DDR2_SO-DIMM.jpg",
                            "caption": "A physical RAM module containing billions of microscopic capacitive memory cells mapped symbolically by identifiers during code execution.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    }
                ],

                # Page 2: Static vs. Dynamic Typing Paradigms
                [
                    {
                        "type": "concept_explanation",
                        "title": "Dynamic vs. Statically Typed Languages",
                        "content": {
                            "text": "Computer languages manage memory registers using one of two primary typing architectures:\n\n### **1. Statically Typed Languages (e.g., C++, Java, C#)**\n- **Rule**: The developer **must explicitly declare the exact data type** of a variable before it can hold values.\n- **Type Locking**: Once declared, the data type is locked for the lifetime of that variable; the variable can never store a different data type.\n- **Compile-Time Checking**: Incompatible assignments (such as assigning text to an integer variable) trigger compile-time errors before the program is ever run.\n- *C++ Example*:\n  ```cpp\n  int studentAge = 16;       // studentAge is locked as an integer\n  studentAge = \"sixteen\";    // COMPILE-TIME ERROR! Cannot assign string to int.\n  ```\n\n### **2. Dynamically Typed Languages (e.g., Python, JavaScript, Ruby)**\n- **Rule**: Developers do **not** declare data types explicitly.\n- **Type Inference**: The interpreter automatically inspects the assigned value at runtime and infers the appropriate data type.\n- **Re-tagging**: A variable's data type can change dynamically if a different class of data is written over it.\n- *Python Example*:\n  ```python\n  student_age = 16            # student_age dynamically stores an integer\n  student_age = \"sixteen\"     # student_age dynamically shifts to store a string\n  ```"
                        }
                    },
                    {
                        "type": "step_by_step_worked_example",
                        "title": "Worked Example: Cross-Language Declaration Blueprint",
                        "content": {
                            "goal": "Compare the declaration and initialization syntax for fundamental variables and constants across Python, C++, and Java.",
                            "problem": "Construct variable declarations for an integer score (100), a decimal price (45.50), a city name ('Nairobi'), a security boolean (True), and a mathematical constant PI (3.14159).",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "step_title": "Python Syntax (Dynamic Typing)",
                                    "step_description": "score = 100\nprice = 45.50\nname = \"Nairobi\"\nis_safe = True\nPI = 3.14159  # Uppercase naming convention indicates constant by agreement"
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "C++ Syntax (Static Typing)",
                                    "step_description": "int score = 100;\nfloat price = 45.50f;\nstd::string name = \"Nairobi\";\nbool isSafe = true;\nconst double PI = 3.14159;  // const keyword prevents compiler reassignment"
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Java Syntax (Static Typing)",
                                    "step_description": "int score = 100;\ndouble price = 45.50;\nString name = \"Nairobi\";\nboolean isSafe = true;\nfinal double PI = 3.14159;  // final keyword locks variable immutably"
                                }
                            ],
                            "conclusion": "Static languages require explicit type keywords (`int`, `double`, `String`) and constant modifiers (`const`, `final`), whereas Python infers types dynamically."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Variables and Data Types in Computer Science",
                        "content": {
                            "youtube_id": "kqtD5dpn9C8",
                            "description": "Comprehensive tutorial explaining variable declarations, memory cell allocation, and data type systems across Python and static programming languages."
                        }
                    }
                ],

                # Page 3: Memory Lifecycles, Scope, and Immutability Enforcements
                [
                    {
                        "type": "concept_explanation",
                        "title": "Memory Lifecycles and Scope Principles",
                        "content": {
                            "text": "When a program executes, variables pass through a structured lifecycle:\n\n1. **Allocation & Declaration**: Memory space is reserved in the computer's RAM stack or heap.\n2. **Initialization**: The variable receives its starting binary bit representation.\n3. **Read / Write Cycles**: The CPU reads the value to perform math or writes an updated value into the cell.\n4. **Destruction / Deallocation**: When the variable goes out of scope (such as when a function finishes executing), the memory is released back to the operating system.\n\n### **Local vs. Global Scope**\n- **Local Scope**: Variables declared inside a specific function or block exist only while that function is running. They are completely hidden from the outside program, preventing unintended variable collisions.\n- **Global Scope**: Variables declared at the top level of a script are accessible throughout the entire file."
                        }
                    },
                    {
                        "type": "step_by_step_worked_example",
                        "title": "Trace Problem: Tracing Variable Mutability and Constant Errors",
                        "content": {
                            "goal": "Trace the memory state across successive assignment statements and identify illegal operations.",
                            "problem": "Evaluate the state of memory registers after executing this C++ pseudo-routine:\n1: int count = 10;\n2: const double TAX_RATE = 0.16;\n3: count = count + 5;\n4: TAX_RATE = 0.18;\n5: count = count * 2;",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "step_title": "Trace Line 1 & 2 (Initialization)",
                                    "step_description": "`count` is allocated 4 bytes in RAM storing integer 10. `TAX_RATE` is allocated 8 bytes storing 0.16 and locked as read-only (`const`)."
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Trace Line 3 (Valid Reassignment)",
                                    "step_description": "CPU evaluates `10 + 5 = 15` and writes 15 into `count`. Memory cell `count` is now 15."
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Trace Line 4 (Constant Violation Error)",
                                    "step_description": "The statement attempts to write `0.18` into `TAX_RATE`. The compiler detects that `TAX_RATE` is flagged `const` and throws a compile-time error: 'error: assignment of read-only variable TAX_RATE'."
                                },
                                {
                                    "step_number": 4,
                                    "step_title": "Trace Line 5 (Execution Halted)",
                                    "step_description": "Because compilation aborted on Line 4 due to the constant mutation violation, Line 5 is never reached."
                                }
                            ],
                            "conclusion": "Constants provide compile-time safety by preventing critical configuration values (like tax rates or physical constants) from being overwritten during runtime."
                        }
                    }
                ],

                # Page 4: Formative Knowledge Checks (4 MCQs)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 1: Static Typing Systems",
                        "content": {
                            "question": "Which typing system requires developers to explicitly declare a variable's data type before writing values to it, and prevents changing that type at runtime?",
                            "options": [
                                "Dynamic Typing",
                                "Static Typing",
                                "Algorithmic Typing",
                                "Logical Typing"
                            ],
                            "correct_answer": "Static Typing",
                            "explanation": "Statically typed languages (such as C++, Java, and Rust) require variable types to be declared explicitly at compile time and enforce strict type immutability."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 2: Purpose of a Variable",
                        "content": {
                            "question": "What is the primary architectural purpose of a variable in computer software?",
                            "options": [
                                "To run defragmentation diagnostics on memory hardware.",
                                "To act as a named, symbolic storage location in RAM that holds values that can be read and modified during runtime.",
                                "To compress text files into zip archives.",
                                "To encrypt packet headers transmitted over optical fibers."
                            ],
                            "correct_answer": "To act as a named, symbolic storage location in RAM that holds values that can be read and modified during runtime.",
                            "explanation": "Variables provide human-readable labels for memory cells, allowing software to store, retrieve, and update intermediate data during program execution."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 3: Modifying Constants",
                        "content": {
                            "question": "What happens if a program attempts to assign a new value to an identifier declared with the 'const' keyword in C++ or 'final' in Java?",
                            "options": [
                                "The program silently ignores the constant and updates the memory cell.",
                                "The compiler aborts compilation with a syntax/type error indicating that a read-only constant cannot be reassigned.",
                                "The constant becomes a dynamic variable automatically.",
                                "The operating system restarts the computer in safe mode."
                            ],
                            "correct_answer": "The compiler aborts compilation with a syntax/type error indicating that a read-only constant cannot be reassigned.",
                            "explanation": "The `const` and `final` modifiers lock memory cells against write operations, causing compiler errors if any code attempts to overwrite them."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 4: Dynamic Type Inference in Python",
                        "content": {
                            "question": "In Python, what is the data type of variable 'x' after executing: x = 25 followed by x = 'Kenya'?",
                            "options": [
                                "Integer (int)",
                                "String (str)",
                                "Float (float)",
                                "Compilation Error"
                            ],
                            "correct_answer": "String (str)",
                            "explanation": "Because Python is dynamically typed, the variable 'x' is re-bound at runtime from an integer to a string object upon reassignment."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LEARNING UNIT 3: Input and Output Statements and Data Type Casting
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Input and Output Statements and Data Type Casting",
            "unit_description": "Console I/O streams, user prompts, string capture behavior in modern interpreters, explicit type casting pipelines, and structured formatted output.",
            "lesson_title": "Lesson 59: Input and Output Statements",
            "pages": [
                # Page 1: Core Principles of Console I/O & User Prompts
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Input/Output Streams and Type Casting",
                        "content": {
                            "goal": "Understand console input and output pipelines, master user prompts, avoid the default string input trap through explicit type casting, and construct formatted console outputs."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Core Principles of Input and Output (I/O)",
                        "content": {
                            "text": "Software interacts with users and external systems via Input and Output channels:\n\n- **Input**: The pathway by which external human data, sensor readings, or file records enter the program's active memory variables (Standard Input: `stdin`).\n- **Output**: The pathway by which processed digital values are rendered onto user consoles, display screens, printer queues, or disk storage (Standard Output: `stdout`).\n- **Prompt**: A clear, human-readable text string displayed to the user *before* requesting input, guiding them on what specific data format the system expects (e.g., `\"Enter your age in years: \"`)."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Input, Type-Casting Pipeline, & Console Output Mechanics",
                        "content": {
                            "svg_content": SVG_INPUT_OUTPUT_CASTING_PIPELINE,
                            "caption": "The four-stage I/O pipeline: console string capture, explicit numerical casting, CPU arithmetic execution, and interpolated f-string formatted display."
                        }
                    }
                ],

                # Page 2: Python I/O Mechanics & The String Trap
                [
                    {
                        "type": "concept_explanation",
                        "title": "Python I/O Mechanics & The Critical String Trap",
                        "content": {
                            "text": "Python captures console input using the built-in `input()` function. However, there is a fundamental architectural rule every programmer must master:\n\n> **`input()` ALWAYS returns user data as a text string (`str`), even if the user types digits!**\n\n### **The Concatenation Bug**\nIf a user enters `5` and your code executes `result = input() + 10`, Python raises a `TypeError` because it cannot add an integer to a string. Furthermore, if you add two captured inputs together without casting (e.g., `\"5\" + \"10\"`), Python performs **string concatenation**, resulting in the text `\"510\"` instead of the arithmetic sum `15`.\n\n### **Explicit Type Casting Solutions**\nTo perform mathematical operations, you must explicitly convert the string into a numeric data type using type casting functions:\n- `int()`: Converts a valid integer string (e.g., `\"25\"`) into integer `25`.\n- `float()`: Converts a decimal string (e.g., `\"45.50\"`) into floating-point `45.50`.\n- `str()`: Converts numbers into string representations.\n- `bool()`: Evaluates truth values."
                        }
                    },
                    {
                        "type": "step_by_step_worked_example",
                        "title": "Worked Example: Supermarket Checkout I/O Pipeline",
                        "content": {
                            "goal": "Write a robust Python script to capture an item's unit price, quantity purchased, and customer name, and print a formatted receipt.",
                            "problem": "Prompt for customer name, floating-point item price, and integer quantity. Compute total cost with a 16% VAT and display using formatted string literals.",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "step_title": "Capture String Input (Name)",
                                    "step_description": "customer_name = input(\"Enter customer name: \")  # Stored directly as str"
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Capture and Cast Numeric Inputs",
                                    "step_description": "item_price = float(input(\"Enter unit price (KES): \"))  # Nested float casting\nquantity = int(input(\"Enter quantity purchased: \"))     # Nested int casting"
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Compute Arithmetic Total & Tax",
                                    "step_description": "subtotal = item_price * quantity\nvat_amount = subtotal * 0.16\ntotal_payable = subtotal + vat_amount"
                                },
                                {
                                    "step_number": 4,
                                    "step_title": "Render Formatted Output via f-strings",
                                    "step_description": "print(f\"\\n--- RECEIPT FOR {customer_name.upper()} ---\")\nprint(f\"Subtotal ({quantity} items): KES {subtotal:.2f}\")\nprint(f\"VAT (16%): KES {vat_amount:.2f}\")\nprint(f\"Total Payable: KES {total_payable:.2f}\")"
                                }
                            ],
                            "conclusion": "Nesting `float(input())` and `int(input())` guarantees clean numerical memory registers, allowing arithmetic calculations and formatted `.2f` rounding."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Python Input Function, Type Conversion, and Formatted Strings",
                        "content": {
                            "youtube_id": "L_T-L_8pAek",
                            "description": "Visual guide demonstrating Python input prompts, type-casting with int() and float(), and avoiding common string concatenation bugs."
                        }
                    }
                ],

                # Page 3: C++ Stream I/O Architecture & Cross-Language Comparison
                [
                    {
                        "type": "concept_explanation",
                        "title": "C++ Stream I/O Mechanics (<iostream>)",
                        "content": {
                            "text": "Unlike Python's functional `input()` and `print()`, C++ handles I/O using standard data stream pipelines provided by the `<iostream>` library:\n\n- `std::cin >> variable`: **Console Input Stream** — Extracts data from the keyboard buffer and streams it into the variable. Because C++ is statically typed, `cin` automatically parses and type-checks the input according to the variable's declared type.\n- `std::cout << expression`: **Console Output Stream** — Inserts data into the console display stream.\n- `std::endl`: Flushes the output buffer and inserts a newline character.\n\n```cpp\n#include <iostream>\n#include <string>\n\nint main() {\n    std::string userName;\n    int userAge;\n\n    std::cout << \"Enter your name: \";\n    std::cin >> userName;\n\n    std::cout << \"Enter your age: \";\n    std::cin >> userAge;  // cin automatically parses input into integer bits\n\n    std::cout << \"Hello \" << userName << \", next year you will be \" \n              << (userAge + 1) << \" years old.\" << std::endl;\n    return 0;\n}\n```"
                        }
                    },
                    {
                        "type": "step_by_step_worked_example",
                        "title": "Comparison: Dynamic Casting (Python) vs Stream Extraction (C++)",
                        "content": {
                            "goal": "Contrast how Python and C++ handle type safety during user input operations.",
                            "problem": "Explain what happens in both Python and C++ when a user types the text 'twenty' when prompted for an age.",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "step_title": "Python Runtime Behavior",
                                    "step_description": "`int(input(\"Age: \"))` receives `\"twenty\"`. The `int()` function attempts to parse the characters as decimal digits, fails, and throws a runtime `ValueError: invalid literal for int() with base 10: 'twenty'`."
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "C++ Stream Extraction Behavior",
                                    "step_description": "`std::cin >> userAge;` attempts to extract digits into an `int`. Finding alphabetic characters, `cin` sets its internal `failbit` flag to true, leaves `userAge` at 0 (or unassigned), and ignores subsequent stream extractions until cleared."
                                }
                            ],
                            "conclusion": "Both languages enforce type constraints, but Python signals failure via runtime exceptions while C++ flags stream state errors."
                        }
                    }
                ],

                # Page 4: Formative Knowledge Checks (4 MCQs)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 1: Default Return Type of input()",
                        "content": {
                            "question": "What data type does Python's input() function return by default, regardless of what the user types?",
                            "options": [
                                "Integer (int)",
                                "Floating-point decimal (float)",
                                "Text string (str)",
                                "Logical Boolean (bool)"
                            ],
                            "correct_answer": "Text string (str)",
                            "explanation": "Python's `input()` function always captures console keystrokes as a text string (`str`). If numerical operations are needed, explicit casting with `int()` or `float()` is required."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 2: Uncast String Addition",
                        "content": {
                            "question": "If a user enters '10' for variable a and '20' for variable b using uncast input(), what is the output of print(a + b)?",
                            "options": [
                                "30",
                                "1020",
                                "200",
                                "TypeError: cannot add numbers"
                            ],
                            "correct_answer": "1020",
                            "explanation": "Because `a` and `b` are strings (`\"10\"` and `\"20\"`), the `+` operator performs string concatenation, joining the two text fragments into `\"1020\"`."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 3: Purpose of Type Casting",
                        "content": {
                            "question": "Why is type casting (e.g., float(input())) essential before calculating mathematical equations with user inputs?",
                            "options": [
                                "It encrypts user inputs to prevent network sniffing.",
                                "It converts raw text string bits into binary numerical representations suitable for ALU arithmetic operations.",
                                "It decreases the physical temperature of the CPU cache.",
                                "It permanently renames the variable identifier."
                            ],
                            "correct_answer": "It converts raw text string bits into binary numerical representations suitable for ALU arithmetic operations.",
                            "explanation": "Type casting translates ASCII/Unicode text characters into integer or IEEE-754 floating-point binary formats so the processor can execute mathematical math."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 4: C++ Stream Operators",
                        "content": {
                            "question": "In C++, which operator is used with std::cin to extract user input from the keyboard buffer into a variable?",
                            "options": [
                                "<< (Insertion operator)",
                                ">> (Extraction operator)",
                                "== (Equality operator)",
                                ":: (Scope resolution operator)"
                            ],
                            "correct_answer": ">> (Extraction operator)",
                            "explanation": "`cin >> variable` uses the stream extraction operator (`>>`) to pull data from the standard input stream into the specified memory variable."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LEARNING UNIT 4: Operators, Expressions, and Mathematical Precedence
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Operators, Expressions, and Mathematical Precedence",
            "unit_description": "Comprehensive breakdown of arithmetic, relational, and logical operators, truth table logic, modulus arithmetic, and hierarchical order of operations.",
            "lesson_title": "Lesson 60 & 61: Operators and Expressions",
            "pages": [
                # Page 1: Operator Categorization & Arithmetic Mechanics
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Operators, Truth Tables, and Precedence",
                        "content": {
                            "goal": "Master arithmetic, relational, and logical operators, understand modulo and floor division, and evaluate compound expressions using the formal 8-level precedence hierarchy."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Core Definitions: Operators, Operands, and Expressions",
                        "content": {
                            "text": "Every algorithm transforms data by applying operations:\n\n- **Operator**: A special mathematical or logical symbol that performs specific operations on one, two, or more values.\n- **Operand**: The raw literal value or variable that is acted upon by an operator (e.g., in `10 + 5`, `10` and `5` are operands; `+` is the operator).\n- **Expression**: Any valid combination of operators, operands, and variables that evaluates to a single final value.\n\n### **Arithmetic Operators Breakdown**\n- `+` (Addition): `10 + 5` evaluates to `15`.\n- `-` (Subtraction): `10 - 5` evaluates to `5`.\n- `*` (Multiplication): `10 * 5` evaluates to `50`.\n- `/` (True Division): Divides operands and **always returns a float**. `10 / 4` evaluates to `2.5`.\n- `//` (Floor Division): Divides two numbers and cuts off the decimal fraction, returning only the integer quotient. `10 // 4` evaluates to `2`.\n- `%` (Modulo / Remainder): Divides two numbers and returns **only the integer remainder**. `10 % 4` evaluates to `2` (since 4 goes into 10 twice with a remainder of 2). Essential for parity checks (`num % 2 == 0` for even numbers).\n- `**` (Exponentiation): Raises a base to a power. `2 ** 3` represents $2^3$, evaluating to `8`."
                        }
                    },
                    {
                        "type": "step_by_step_worked_example",
                        "title": "Worked Example: Modulo and Floor Division Applications",
                        "content": {
                            "goal": "Apply floor division `//` and modulo `%` to convert a raw duration in minutes into whole hours and remaining minutes.",
                            "problem": "A video download takes 135 minutes. Calculate total hours and leftover minutes using Python arithmetic operators.",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "step_title": "Calculate Whole Hours using Floor Division",
                                    "step_description": "hours = 135 // 60  # 60 goes into 135 exactly 2 whole times (evaluates to 2)"
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Calculate Remaining Minutes using Modulo",
                                    "step_description": "minutes = 135 % 60  # 135 - (2 * 60) leaves a remainder of 15 (evaluates to 15)"
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Construct Output String",
                                    "step_description": "print(f\"Duration: {hours} hours and {minutes} minutes\")"
                                }
                            ],
                            "conclusion": "Floor division `//` extracts complete measurement intervals, while modulo `%` captures leftover fractional remainders."
                        }
                    }
                ],

                # Page 2: Relational Comparisons and Boolean Logic Gates
                [
                    {
                        "type": "concept_explanation",
                        "title": "Relational and Logical Operators",
                        "content": {
                            "text": "### **Relational (Comparison) Operators**\nUsed to test the relationship between two values. **Relational operators always return a Boolean result (`True` or `False`)**:\n- `==` (Equal to): `5 == 5` is `True` | `5 == 6` is `False`.\n- `!=` (Not equal to): `5 != 10` is `True` | `5 != 5` is `False`.\n- `>` (Greater than): `10 > 5` is `True`.\n- `<` (Less than): `5 < 10` is `True`.\n- `>=` (Greater than or equal to): `10 >= 10` is `True`.\n- `<=` (Less than or equal to): `12 <= 5` is `False`.\n\n### **Logical (Boolean) Operators**\nUsed to combine multiple Boolean conditions together:\n- `and` (Logical AND): Returns `True` **only if both operands are True**.\n  - `True and True` $\\rightarrow$ `True`\n  - `True and False` $\\rightarrow$ `False`\n- `or` (Logical OR): Returns `True` **if at least one operand is True**.\n  - `True or False` $\\rightarrow$ `True`\n  - `False or False` $\\rightarrow$ `False`\n- `not` (Logical NOT): Reverses the Boolean truth value.\n  - `not True` $\\rightarrow$ `False`\n  - `not False` $\\rightarrow$ `True`"
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Logic Gate Truth Tables & Boolean Operations",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Logic-gate-truth-table.png/800px-Logic-gate-truth-table.png",
                            "caption": "Standard Boolean logic truth tables illustrating AND, OR, and NOT operations identical to software logical evaluation rules.",
                            "author": "Wikimedia Commons",
                            "licensing": "Public Domain"
                        }
                    },
                    {
                        "type": "step_by_step_worked_example",
                        "title": "Worked Example: Evaluating Compound Boolean Expressions",
                        "content": {
                            "goal": "Evaluate the Boolean output of a compound conditional statement given specific variable values.",
                            "problem": "If `age = 17` and `has_id = True` and `is_supervised = False`, evaluate:\n`can_enter = (age >= 18 and has_id) or (age >= 16 and is_supervised)`",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "step_title": "Evaluate Left Sub-clause",
                                    "step_description": "`(age >= 18 and has_id)` &#8594; `(17 >= 18 and True)` &#8594; `(False and True)` &#8594; `False`"
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Evaluate Right Sub-clause",
                                    "step_description": "`(age >= 16 and is_supervised)` &#8594; `(17 >= 16 and False)` &#8594; `(True and False)` &#8594; `False`"
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Evaluate Compound OR Operator",
                                    "step_description": "`can_enter = False or False` &#8594; `False`"
                                }
                            ],
                            "conclusion": "The compound expression evaluates to `False` because neither the adult admission nor the supervised youth condition is fully satisfied."
                        }
                    }
                ],

                # Page 3: Operator Precedence & Step-by-Step Parse Tree Walkthrough
                [
                    {
                        "type": "concept_explanation",
                        "title": "Mathematical Precedence (Order of Operations)",
                        "content": {
                            "text": "When evaluating complex expressions containing multiple operators, programming language parsers follow a strict precedence scale to prevent mathematical ambiguity:\n\n1. **Parentheses `( )`**: Forces sub-expressions to evaluate first.\n2. **Exponentiation `**`**: Power calculations.\n3. **Multiplicative Operators `*`, `/`, `//`, `%`**: Multiplications, true divisions, floor divisions, and modulus operations (evaluated left to right).\n4. **Additive Operators `+`, `-`**: Additions and subtractions (evaluated left to right).\n5. **Relational Comparisons `==`, `!=`, `>`, `<`, `>=`, `<=`**: Magnitude and equivalence checks.\n6. **Logical `not`**: Unary logical negation.\n7. **Logical `and`**: Conjunction.\n8. **Logical `or`**: Disjunction (evaluated absolute last)."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Operator Precedence Hierarchy & Parse Tree Reduction",
                        "content": {
                            "svg_content": SVG_OPERATOR_PRECEDENCE_PARSE_TREE,
                            "caption": "Step-by-step parse tree collapsing the compound expression `5 + 3 * 2 > 10 and not 4 < 2` down to its final Boolean terminal state `True`."
                        }
                    },
                    {
                        "type": "step_by_step_worked_example",
                        "title": "Detailed Trace: Step-by-Step Expression Reduction",
                        "content": {
                            "goal": "Trace every intermediate reduction step of the expression: `result = 5 + 3 * 2 > 10 and not 4 < 2`.",
                            "problem": "Evaluate the final Boolean state showing exact operator precedence order.",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "step_title": "Step 1: Multiplication (Level 3 Precedence)",
                                    "step_description": "Evaluate `3 * 2 = 6`. Expression becomes: `5 + 6 > 10 and not 4 < 2`"
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Step 2: Addition (Level 4 Precedence)",
                                    "step_description": "Evaluate `5 + 6 = 11`. Expression becomes: `11 > 10 and not 4 < 2`"
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Step 3: First Relational Comparison (Level 5 Precedence)",
                                    "step_description": "Evaluate `11 > 10` &#8594; `True`. Expression becomes: `True and not 4 < 2`"
                                },
                                {
                                    "step_number": 4,
                                    "step_title": "Step 4: Second Relational Comparison (Level 5 Precedence)",
                                    "step_description": "Evaluate `4 < 2` &#8594; `False`. Expression becomes: `True and not False`"
                                },
                                {
                                    "step_number": 5,
                                    "step_title": "Step 5: Logical NOT (Level 6 Precedence)",
                                    "step_description": "Evaluate `not False` &#8594; `True`. Expression becomes: `True and True`"
                                },
                                {
                                    "step_number": 6,
                                    "step_title": "Step 6: Logical AND (Level 7 Precedence)",
                                    "step_description": "Evaluate `True and True` &#8594; `True`."
                                }
                            ],
                            "conclusion": "The entire expression evaluates rigorously to `True` following the compiler's 8-level precedence hierarchy."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Python Operators and Operator Precedence",
                        "content": {
                            "youtube_id": "v5MR5JnKcZI",
                            "description": "Educational guide walking through arithmetic, comparison, and logical operators with precedence rules and expression parse trees."
                        }
                    }
                ],

                # Page 4: Formative Knowledge Checks (4 MCQs)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 1: Modulo Arithmetic",
                        "content": {
                            "question": "What is the exact output of the mathematical expression '17 % 5' in Python?",
                            "options": [
                                "3.4",
                                "3",
                                "2",
                                "1"
                            ],
                            "correct_answer": "2",
                            "explanation": "The modulo operator (`%`) computes the remainder after division. 5 divides into 17 three full times ($5 \\times 3 = 15$) with a remainder of 2 ($17 - 15 = 2$)."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 2: Exponentiation Precedence",
                        "content": {
                            "question": "What is the final value of the arithmetic expression '2 ** 3 * 2' in Python?",
                            "options": [
                                "16",
                                "64",
                                "12",
                                "8"
                            ],
                            "correct_answer": "16",
                            "explanation": "Exponentiation (`**`) has higher precedence than multiplication (`*`). Thus, `2 ** 3` evaluates first to `8`, and `8 * 2` evaluates to `16`."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 3: Logical Operators with Variables",
                        "content": {
                            "question": "If x = True and y = False, what does the logical expression 'not x or y' evaluate to?",
                            "options": [
                                "True",
                                "False",
                                "None",
                                "TypeError"
                            ],
                            "correct_answer": "False",
                            "explanation": "`not` has higher precedence than `or`. `not True` evaluates to `False`. Then `False or False` evaluates to `False`."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 4: Floor Division vs True Division",
                        "content": {
                            "question": "Which arithmetic operator divides two numbers and returns ONLY the integer whole number part, discarding any fractional decimals?",
                            "options": [
                                "/ (True Division)",
                                "// (Floor Division)",
                                "% (Modulo)",
                                "** (Exponentiation)"
                            ],
                            "correct_answer": "// (Floor Division)",
                            "explanation": "`//` is the floor division operator; it computes quotient division and rounds down to the nearest lower integer (e.g., `10 // 4` produces `2`)."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LEARNING UNIT 5: Practice, Assessment, and Applied Scenario Implementations
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Practice, Assessment, and Applied Scenario Implementations",
            "unit_description": "Synthesis and summative assessment of identifiers, typing, I/O, operators, and real-world algorithmic implementation via the Nyahururu Dairy Cooperative case study.",
            "lesson_title": "Lesson 62: Practice and Assessment Library",
            "pages": [
                # Page 1: Comprehensive Assessment: Concepts, Matching & Syntax Correction
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Algorithmic Synthesis & Production Problem Solving",
                        "content": {
                            "goal": "Synthesize all topic concepts to solve multifaceted algorithmic syntax debugging, compound expression evaluations, and real-world industrial software automation challenges."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Topic Synthesis & Syntax Debugging Protocol",
                        "content": {
                            "text": "Before building complete software systems, developers must be proficient at identifying syntax bugs, correcting illegal identifier tokens, and verifying compound logic equations.\n\n### **Common Developer Syntax Pitfalls**\n1. **Unchecked Concatenation**: Forgetting to type-cast user input values before mathematical operations.\n2. **Identifier Token Errors**: Using hyphens, leading digits, or spaces in variable names.\n3. **Precedence Assumptions**: Omitting parentheses in compound Boolean expressions where `and` and `or` are mixed.\n4. **Constant Reassignment**: Attempting to alter locked constant memory cells during runtime."
                        }
                    },
                    {
                        "type": "step_by_step_worked_example",
                        "title": "Worked Example: Syntax Correction and Expression Evaluation",
                        "content": {
                            "goal": "Correct three invalid variable identifiers and evaluate a multi-operator compound logic expression.",
                            "problem": "Task A: Correct the invalid identifiers: (1) `class_average-score`, (2) `5th_student_name`, (3) `total price$`.\nTask B: Step-by-step evaluate the compound expression: `(10 // 3 == 3) and (not (5 * 2 > 12) or 3 % 2 == 1)`.",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "step_title": "Correct Invalid Identifier 1",
                                    "step_description": "`class_average-score` contains an illegal hyphen. Corrected: `class_average_score` (using underscores)."
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Correct Invalid Identifier 2",
                                    "step_description": "`5th_student_name` begins with a digit. Corrected: `fifth_student_name` or `student_name_5`."
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Correct Invalid Identifier 3",
                                    "step_description": "`total price$` contains an illegal space and currency symbol `$`. Corrected: `total_price`."
                                },
                                {
                                    "step_number": 4,
                                    "step_title": "Evaluate Compound Expression Step-by-Step",
                                    "step_description": "1. `10 // 3` = 3 &#8594; `3 == 3` &#8594; `True`.\n2. `5 * 2` = 10 &#8594; `10 > 12` &#8594; `False` &#8594; `not False` &#8594; `True`.\n3. `3 % 2` = 1 &#8594; `1 == 1` &#8594; `True`.\n4. Right sub-clause: `True or True` &#8594; `True`.\n5. Compound: `True and True` &#8594; `True`."
                                }
                            ],
                            "conclusion": "The corrected identifiers comply with compiler lexical rules, and the compound expression simplifies systematically to `True`."
                        }
                    }
                ],

                # Page 2: Challenging Application Scenario: Nyahururu Dairy Cooperative
                [
                    {
                        "type": "concept_explanation",
                        "title": "Challenging Scenario: The Nyahururu Automated Dairy Milk Aggregator",
                        "content": {
                            "text": "You are commissioned to develop an automated utility program for a dairy cooperative in Nyahururu. The system receives raw milk deliveries from local farmers, processes weights via digital intake scales, calculates packaged 2-liter bottle outputs, identifies leftover quantities, and evaluates eligibility for cooperative premium bonuses.\n\n### **System Specification Requirements**\n1. **Constant Declaration**: Define a locked constant `DENSITY_CONVERSION = 1.03` (representing that 1.0 liter of cow's milk weighs exactly 1.03 kg).\n2. **Input Capture**: Prompt for the farmer's name (`farmer_name`: `str`) and delivered mass in kilograms (`milk_mass_kg`: `float`).\n3. **Volume Conversion**: Compute volume in liters using:\n   $$\\text{milk\\_volume\\_liters} = \\frac{\\text{milk\\_mass\\_kg}}{\\text{DENSITY\\_CONVERSION}}$$\n4. **Bottling Calculations**: Milk is packaged exclusively in complete **2-liter bottles**.\n   - Complete 2L Bottles (`complete_bottles`: `int`): Use floor division `milk_volume_liters // 2`.\n   - Leftover Liters (`leftover_liters`: `float`): Use modulo `milk_volume_liters % 2`.\n5. **Premium Bonus Evaluation**: The cooperative awards a bonus flag (`premium_bonus`: `bool`) of `True` **only if** the farmer delivers more than $50.0\\text{ liters}$ **AND** the volume is exactly divisible into 2-liter bottles with zero leftover milk ($0.0\\text{ L}$). Otherwise, the bonus is `False`.\n6. **Structured Summary**: Print a receipt with customer name, liters calculated, complete bottles, leftover liters, and bonus status."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Applied Case Study: Nyahururu Automated Dairy Milk Aggregator",
                        "content": {
                            "svg_content": SVG_DAIRY_COOPERATIVE_CASE_STUDY,
                            "caption": "Complete architectural pipeline for the Nyahururu Dairy Co-op system: constant definition, input capture, floor/modulo arithmetic, and Boolean bonus evaluation."
                        }
                    },
                    {
                        "type": "step_by_step_worked_example",
                        "title": "Worked Example: Nyahururu Dairy Co-op Python Implementation & Dry Run",
                        "content": {
                            "goal": "Author the complete production Python script and execute a manual dry-run trace for farmer Wanjiku delivering 103.0 kg of milk.",
                            "problem": "Write the Python code and trace all variable states for `farmer_name = 'Wanjiku'` and `milk_mass_kg = 103.0`.",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "step_title": "Production Python Script Implementation",
                                    "step_description": "# Nyahururu Dairy Cooperative Milk Aggregator System\n\n# 1. Constant Definition\nDENSITY_CONVERSION = 1.03  # 1 Liter = 1.03 kg\n\n# 2. Interactive Input Capture with Explicit Casting\nfarmer_name = input(\"Enter farmer's name: \")\nmilk_mass_kg = float(input(\"Enter milk mass delivered (kg): \"))\n\n# 3. Volume and Bottling Calculations\nmilk_volume_liters = milk_mass_kg / DENSITY_CONVERSION\ncomplete_bottles = int(milk_volume_liters // 2)\nleftover_liters = milk_volume_liters % 2\n\n# 4. Premium Bonus Compound Boolean Logic\npremium_bonus = (milk_volume_liters > 50.0) and (leftover_liters == 0.0)\n\n# 5. Formatted Delivery Receipt Display\nprint(\"\\n====================================\")\nprint(\"   NYAHURURU DAIRY COOPERATIVE      \")\nprint(\"      MILK INTAKE SUMMARY           \")\nprint(\"====================================\")\nprint(f\"Farmer Name:       {farmer_name}\")\nprint(f\"Mass Delivered:    {milk_mass_kg:.2f} kg\")\nprint(f\"Calculated Volume: {milk_volume_liters:.2f} Liters\")\nprint(f\"Complete 2L Units: {complete_bottles} Bottles\")\nprint(f\"Leftover Volume:   {leftover_liters:.2f} Liters\")\nprint(\"------------------------------------\")\nprint(f\"Premium Bonus:     {'AWARDED (True)' if premium_bonus else 'NOT ELIGIBLE (False)'}\")\nprint(\"====================================\")"
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Dry-Run Trace Table for Wanjiku (103.0 kg)",
                                    "step_description": "1. `farmer_name` = 'Wanjiku' (str)\n2. `milk_mass_kg` = 103.0 (float)\n3. `DENSITY_CONVERSION` = 1.03 (const float)\n4. `milk_volume_liters` = 103.0 / 1.03 = 100.0 (float)\n5. `complete_bottles` = 100.0 // 2 = 50 (int)\n6. `leftover_liters` = 100.0 % 2 = 0.0 (float)\n7. `premium_bonus` = (100.0 > 50.0) and (0.0 == 0.0) -> True and True -> True (bool)"
                                }
                            ],
                            "conclusion": "Wanjiku delivers 103.0 kg, yielding exactly 100.0 liters of milk, filling 50 complete 2-liter bottles with 0.0 liters leftover, successfully qualifying for the Premium Bonus (True)."
                        }
                    }
                ],

                # Page 3: Summative Knowledge Checks Part 1 (4 MCQs)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative Check 1: Translator Keyword Error",
                        "content": {
                            "question": "If a programmer accidentally miskeys a reserved keyword in Python (e.g. typing 'whle' instead of 'while'), what category of error will the interpreter trigger?",
                            "options": [
                                "Syntax Error (or NameError)",
                                "Hardware Parity Error",
                                "Network Timeout Error",
                                "Defragmentation Error"
                            ],
                            "correct_answer": "Syntax Error (or NameError)",
                            "explanation": "Misspelling a keyword prevents the lexer from recognizing the control structure, causing a SyntaxError (or a NameError if treated as an undeclared identifier)."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative Check 2: Bottling and Modulo Logic",
                        "content": {
                            "question": "In the Nyahururu Dairy program, which arithmetic operator extracts ONLY the leftover milk volume that cannot fill a full 2-liter bottle?",
                            "options": [
                                "/ (True division)",
                                "// (Floor division)",
                                "% (Modulo remainder)",
                                "** (Power exponent)"
                            ],
                            "correct_answer": "% (Modulo remainder)",
                            "explanation": "The modulo operator `milk_volume_liters % 2` calculates the mathematical remainder after dividing by 2, representing the leftover liters."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative Check 3: Compound Bonus Evaluation",
                        "content": {
                            "question": "If a farmer delivers 40.0 liters of milk with 0.0 liters leftover, what does (milk_volume_liters > 50.0 and leftover_liters == 0.0) evaluate to?",
                            "options": [
                                "True",
                                "False",
                                "None",
                                "TypeError"
                            ],
                            "correct_answer": "False",
                            "explanation": "Because `40.0 > 50.0` is `False`, the logical `and` operator produces `False and True`, which evaluates to `False`."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative Check 4: Relational Inequality Operator",
                        "content": {
                            "question": "Which relational operator tests whether two values are NOT equal and returns a Boolean result?",
                            "options": [
                                "=",
                                "==",
                                "!=",
                                "<>"
                            ],
                            "correct_answer": "!=",
                            "explanation": "`!=` is the standard relational operator for 'not equal to' in Python, C++, Java, and modern programming languages."
                        }
                    }
                ],

                # Page 4: Summative Knowledge Checks Part 2 (4 MCQs)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative Check 5: Static Typing Data Type Mutability",
                        "content": {
                            "question": "True or False: In statically typed languages (like C++ or Java), a variable's data type can be changed to a string after being declared as an integer.",
                            "options": [
                                "True — Any variable can store text at any time.",
                                "False — In statically typed languages, variable types are locked at declaration and cannot be changed at runtime.",
                                "True — Provided the string contains only digits.",
                                "False — But only if the variable is declared inside a loop."
                            ],
                            "correct_answer": "False — In statically typed languages, variable types are locked at declaration and cannot be changed at runtime.",
                            "explanation": "Statically typed languages enforce strict compile-time type locking; a variable declared as an `int` can never hold a string."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative Check 6: Precedence Order Comparison",
                        "content": {
                            "question": "True or False: Division (/) and Exponentiation (**) have the exact same level of precedence when evaluating arithmetic expressions.",
                            "options": [
                                "True — All arithmetic operators share identical priority.",
                                "False — Exponentiation (**) has higher precedence than division (/) and is evaluated first.",
                                "True — Provided there are no parentheses in the expression.",
                                "False — Division has higher precedence than exponentiation."
                            ],
                            "correct_answer": "False — Exponentiation (**) has higher precedence than division (/) and is evaluated first.",
                            "explanation": "In operator precedence hierarchy, exponentiation (`**`) is evaluated before multiplicative operations (`*`, `/`, `//`, `%`)."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative Check 7: Local vs Global Variable Scope",
                        "content": {
                            "question": "True or False: Variables declared inside a local function scope are protected and hidden from the global main program, preventing variable naming collisions.",
                            "options": [
                                "True — Local variables exist only within their defining function scope.",
                                "False — All variables in computer programs are automatically global.",
                                "True — But only if they are declared as constants.",
                                "False — Local variables overwrite global variables permanently."
                            ],
                            "correct_answer": "True — Local variables exist only within their defining function scope.",
                            "explanation": "Local variable scoping encapsulates variables within functions, preventing unintended side effects across the rest of the application."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative Check 8: Allowed Special Characters in Identifiers",
                        "content": {
                            "question": "True or False: The underscore (_) is the only non-alphanumeric character permitted when drafting standard custom identifiers in Python, C++, and Java.",
                            "options": [
                                "True — Punctuation symbols like hyphens, dollar signs, and periods are prohibited in standard Python identifier naming.",
                                "False — Hyphens and spaces are also freely permitted.",
                                "False — Percentage symbols (%) are legal in identifiers.",
                                "True — But only if placed at the end of the variable name."
                            ],
                            "correct_answer": "True — Punctuation symbols like hyphens, dollar signs, and periods are prohibited in standard Python identifier naming.",
                            "explanation": "The underscore (`_`) is the unique special character permitted in standard identifier syntax; other symbols are reserved for operators and syntax."
                        }
                    }
                ]
            ]
        }
    ]

# =====================================================================
# INGESTION EXECUTOR
# =====================================================================

def ingest_grade10_topic14(replace: bool = True):
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 10 Computer Science — Topic 14")
    print("Topic: Identifiers and Operators")
    print("=" * 80)

    curriculum = Curriculum.objects.get(id=5)
    grade = Grade.objects.get(curriculum=curriculum, level=10)
    subject, _ = Subject.objects.get_or_create(grade=grade, name="Computer Science")

    with transaction.atomic():
        topic, created = Topic.objects.get_or_create(
            subject=subject,
            order=14,
            defaults={
                "name": "Identifiers and Operators",
                "description": "Comprehensive study of program elementary elements, identifier naming rules, variables, constants, dynamic vs. static typing systems, console input/output mechanics, type-casting pipelines, arithmetic, relational, and logical operators, operator precedence hierarchies, and applied algorithmic problem solving."
            }
        )

        if not created and replace:
            print(f"[*] Topic 14 already exists (ID: {topic.id}). Performing clean replacement of units and lessons...")
            topic.learning_units.all().delete()
            topic.lessons.all().delete()
            topic.name = "Identifiers and Operators"
            topic.description = "Comprehensive study of program elementary elements, identifier naming rules, variables, constants, dynamic vs. static typing systems, console input/output mechanics, type-casting pipelines, arithmetic, relational, and logical operators, operator precedence hierarchies, and applied algorithmic problem solving."
            topic.save()

        curriculum_data = build_topic14_curriculum()

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
                    "topic_order": 14,
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
                        block_id=f"g10_cs_t14_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={"topic_order": 14, "unit_order": u_order, "page": page_idx}
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
    print(f"TOPIC 14 INGESTION COMPLETE:")
    print(f"  Units Created:   {total_units}")
    print(f"  Lessons Created: {total_lessons}")
    print(f"  Pages Created:   {total_pages}")
    print(f"  Blocks Created:  {total_blocks}")
    print(f"  Assets Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_grade10_topic14(replace=True)
