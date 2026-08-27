"""
VLearn CBC Grade 10 Computer Science — Topic 12: Computer Programming Concepts
Production Ingestion & Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (Level: 10)
Subject: Computer Science (ID: 38)
Topic: Computer Programming Concepts (Topic Order: 12)

Decomposed into 3 Comprehensive Learning Units & 3 Published Lessons:
  1. Programming Terminology and Program Representation (Lesson 42: Programming Terminology and Program Representation)
  2. Evolution and Paradigms of Programming Languages (Lesson 43: Evolution and Paradigms of Programming Languages)
  3. Translation and Execution of Programs (Lesson 44: Translation and Execution of Programs)
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
# HIGH-FIDELITY VECTOR SVGS FOR TOPIC 12 (DARK THEME 960x520)
# =====================================================================

SVG_PROGRAM_EXECUTION_PIPELINE = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Complete Program Lifecycle: Mind to Silicon Execution</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">How human algorithmic logic transforms across translation layers into physical CPU register operations</text>

  <!-- 5 Stage Pipeline Flow -->
  <!-- Stage 1: Programmer Mind -->
  <g transform="translate(45, 95)">
    <rect width="155" height="230" rx="10" fill="#0f172a" stroke="#818cf8" stroke-width="2"/>
    <rect width="155" height="32" rx="8" fill="#4338ca"/>
    <text x="77.5" y="21" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Human Mind</text>
    
    <circle cx="77.5" cy="75" r="28" fill="#1e1b4b" stroke="#818cf8" stroke-width="1.5"/>
    <text x="77.5" y="80" font-size="24" text-anchor="middle">💡</text>
    
    <text x="77.5" y="125" font-size="10" font-weight="bold" fill="#a5b4fc" text-anchor="middle">Algorithmic Problem</text>
    <text x="77.5" y="145" font-size="9" fill="#cbd5e1" text-anchor="middle">Decomposition</text>
    <text x="77.5" y="160" font-size="9" fill="#cbd5e1" text-anchor="middle">Pattern Recognition</text>
    <text x="77.5" y="175" font-size="9" fill="#cbd5e1" text-anchor="middle">Pseudocode &amp; Logic</text>
    
    <rect x="15" y="195" width="125" height="22" rx="4" fill="#312e81"/>
    <text x="77.5" y="210" font-size="8.5" fill="#c7d2fe" text-anchor="middle">"Add two integers"</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <path d="M 205 210 L 225 210" stroke="#38bdf8" stroke-width="3" fill="none"/>

  <!-- Stage 2: Source Code -->
  <g transform="translate(230, 95)">
    <rect width="155" height="230" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect width="155" height="32" rx="8" fill="#0284c7"/>
    <text x="77.5" y="21" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Source Code</text>
    
    <rect x="15" y="45" width="125" height="60" rx="6" fill="#1e293b" stroke="#0ea5e9" stroke-width="1"/>
    <text x="25" y="65" font-size="9" font-family="monospace" fill="#38bdf8">x = 8</text>
    <text x="25" y="80" font-size="9" font-family="monospace" fill="#38bdf8">y = 4</text>
    <text x="25" y="95" font-size="9" font-family="monospace" fill="#22c55e">total = x + y</text>

    <text x="77.5" y="125" font-size="10" font-weight="bold" fill="#7dd3fc" text-anchor="middle">High-Level Syntax</text>
    <text x="77.5" y="145" font-size="9" fill="#cbd5e1" text-anchor="middle">Human-Readable Text</text>
    <text x="77.5" y="160" font-size="9" fill="#cbd5e1" text-anchor="middle">Keywords &amp; Rules</text>
    <text x="77.5" y="175" font-size="9" fill="#cbd5e1" text-anchor="middle">Python / Java / C++</text>

    <rect x="15" y="195" width="125" height="22" rx="4" fill="#075985"/>
    <text x="77.5" y="210" font-size="8.5" fill="#bae6fd" text-anchor="middle">Grammar (Syntax)</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <path d="M 390 210 L 410 210" stroke="#38bdf8" stroke-width="3" fill="none"/>

  <!-- Stage 3: Translator -->
  <g transform="translate(415, 95)">
    <rect width="155" height="230" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect width="155" height="32" rx="8" fill="#d97706"/>
    <text x="77.5" y="21" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Translator</text>

    <circle cx="77.5" cy="75" r="28" fill="#451a03" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="77.5" y="80" font-size="22" text-anchor="middle">⚙️</text>

    <text x="77.5" y="125" font-size="10" font-weight="bold" fill="#fcd34d" text-anchor="middle">Lexical &amp; Syntax</text>
    <text x="77.5" y="145" font-size="9" fill="#cbd5e1" text-anchor="middle">Parsing &amp; AST</text>
    <text x="77.5" y="160" font-size="9" fill="#cbd5e1" text-anchor="middle">Compiler (Ahead-of-Time)</text>
    <text x="77.5" y="175" font-size="9" fill="#cbd5e1" text-anchor="middle">Interpreter (Line-by-Line)</text>

    <rect x="15" y="195" width="125" height="22" rx="4" fill="#78350f"/>
    <text x="77.5" y="210" font-size="8.5" fill="#fef3c7" text-anchor="middle">Error Detection</text>
  </g>

  <!-- Arrow 3 -> 4 -->
  <path d="M 575 210 L 595 210" stroke="#38bdf8" stroke-width="3" fill="none"/>

  <!-- Stage 4: Machine Code -->
  <g transform="translate(600, 95)">
    <rect width="155" height="230" rx="10" fill="#0f172a" stroke="#ec4899" stroke-width="2"/>
    <rect width="155" height="32" rx="8" fill="#db2777"/>
    <text x="77.5" y="21" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">4. Machine Code</text>

    <rect x="15" y="45" width="125" height="60" rx="6" fill="#1e293b" stroke="#f472b6" stroke-width="1"/>
    <text x="77.5" y="65" font-size="8.5" font-family="monospace" fill="#f472b6" text-anchor="middle">10110000 00001000</text>
    <text x="77.5" y="80" font-size="8.5" font-family="monospace" fill="#f472b6" text-anchor="middle">10110001 00000100</text>
    <text x="77.5" y="95" font-size="8.5" font-family="monospace" fill="#f472b6" text-anchor="middle">00000000 11001000</text>

    <text x="77.5" y="125" font-size="10" font-weight="bold" fill="#fbcfe8" text-anchor="middle">Pure Binary Stream</text>
    <text x="77.5" y="145" font-size="9" fill="#cbd5e1" text-anchor="middle">Opcode + Operand</text>
    <text x="77.5" y="160" font-size="9" fill="#cbd5e1" text-anchor="middle">Architecture Specific</text>
    <text x="77.5" y="175" font-size="9" fill="#cbd5e1" text-anchor="middle">(x86_64, ARM, RISC-V)</text>

    <rect x="15" y="195" width="125" height="22" rx="4" fill="#831843"/>
    <text x="77.5" y="210" font-size="8.5" fill="#fce7f3" text-anchor="middle">0s and 1s Pattern</text>
  </g>

  <!-- Arrow 4 -> 5 -->
  <path d="M 760 210 L 780 210" stroke="#38bdf8" stroke-width="3" fill="none"/>

  <!-- Stage 5: CPU Execution -->
  <g transform="translate(785, 95)">
    <rect width="130" height="230" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <rect width="130" height="32" rx="8" fill="#059669"/>
    <text x="65" y="21" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">5. CPU Hardware</text>

    <rect x="15" y="45" width="100" height="60" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="1"/>
    <text x="65" y="68" font-size="9" font-family="monospace" fill="#a7f3d0" text-anchor="middle">R1 = 8</text>
    <text x="65" y="85" font-size="9" font-family="monospace" fill="#a7f3d0" text-anchor="middle">R2 = 4</text>
    <text x="65" y="98" font-size="8" font-family="monospace" fill="#34d399" text-anchor="middle">ALU: 8 + 4 = 12</text>

    <text x="65" y="125" font-size="10" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Silicon Execution</text>
    <text x="65" y="145" font-size="9" fill="#cbd5e1" text-anchor="middle">Transistor Gates</text>
    <text x="65" y="160" font-size="9" fill="#cbd5e1" text-anchor="middle">Voltage Switching</text>
    <text x="65" y="175" font-size="9" fill="#cbd5e1" text-anchor="middle">Registers &amp; Buses</text>

    <rect x="10" y="195" width="110" height="22" rx="4" fill="#065f46"/>
    <text x="65" y="210" font-size="8.5" fill="#d1fae5" text-anchor="middle">Physical Result</text>
  </g>

  <!-- Bottom Comparison Card: Syntax vs Semantics -->
  <g transform="translate(45, 345)">
    <rect width="870" height="135" rx="10" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <rect width="870" height="28" rx="8" fill="#334155"/>
    <text x="435" y="19" font-size="12" font-weight="bold" fill="#f8fafc" text-anchor="middle">Crucial Engineering Distinction: Syntax vs. Semantics</text>

    <!-- Syntax Column -->
    <g transform="translate(25, 38)">
      <text x="0" y="16" font-size="12" font-weight="bold" fill="#ef4444">1. Syntax (Grammatical Form)</text>
      <text x="0" y="34" font-size="10.5" fill="#cbd5e1">&#8226; Strict spelling, punctuation, and keyword structures of the language.</text>
      <text x="0" y="52" font-size="10.5" fill="#cbd5e1">&#8226; Caught immediately by translator: <tspan font-family="monospace" fill="#f87171">prnt("Hello")</tspan> &rarr; <tspan fill="#fca5a5" font-weight="bold">SyntaxError</tspan>.</text>
      <text x="0" y="70" font-size="10" fill="#94a3b8">analogy: "Drank cat milk cold the" (Broken grammar prevents understanding).</text>
    </g>

    <!-- Divider -->
    <line x1="440" y1="35" x2="440" y2="125" stroke="#334155" stroke-width="1.5" stroke-dasharray="4"/>

    <!-- Semantics Column -->
    <g transform="translate(460, 38)">
      <text x="0" y="16" font-size="12" font-weight="bold" fill="#eab308">2. Semantics (Logical Meaning &amp; Behavior)</text>
      <text x="0" y="34" font-size="10.5" fill="#cbd5e1">&#8226; The actual runtime behavior and mathematical logic of statements.</text>
      <text x="0" y="52" font-size="10.5" fill="#cbd5e1">&#8226; Runs without translator crashing, but gives wrong result: <tspan font-family="monospace" fill="#fde047">area = l + w</tspan>.</text>
      <text x="0" y="70" font-size="10" fill="#94a3b8">analogy: "The milk drank the cat" (Valid grammar, but illogical meaning).</text>
    </g>
  </g>
</svg>
""")

SVG_LANGUAGE_GENERATIONS_TIMELINE = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Generational Evolution of Programming Languages (1GL &ndash; 5GL)</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">The Journey of Increasing Abstraction: From Raw Silicon Switching to Natural Constraint-Based Logic</text>

  <!-- Left Abstraction Arrow -->
  <g transform="translate(45, 95)">
    <defs>
      <linearGradient id="absGrad" x1="0%" y1="100%" x2="0%" y2="0%">
        <stop offset="0%" stop-color="#ef4444"/>
        <stop offset="25%" stop-color="#f59e0b"/>
        <stop offset="50%" stop-color="#38bdf8"/>
        <stop offset="75%" stop-color="#818cf8"/>
        <stop offset="100%" stop-color="#34d399"/>
      </linearGradient>
    </defs>
    <rect x="0" y="0" width="16" height="380" rx="8" fill="url(#absGrad)"/>
    <text x="-190" y="-24" font-size="11" font-weight="bold" fill="#38bdf8" transform="rotate(-90)" text-anchor="middle">INCREASING ABSTRACTION (Closer to Human Thought)</text>
  </g>

  <!-- 5 Generation Cards -->
  <!-- 5GL Card -->
  <g transform="translate(85, 90)">
    <rect width="820" height="66" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect width="8" height="66" rx="4" fill="#10b981"/>
    <text x="25" y="22" font-size="13" font-weight="bold" fill="#34d399">5GL &mdash; Fifth Generation: Constraint-Based &amp; AI Languages (Present &amp; Future)</text>
    <text x="25" y="42" font-size="10.5" fill="#cbd5e1"><tspan font-weight="bold" fill="#94a3b8">Characteristics:</tspan> Problem solving using constraints, facts, and inference rules rather than algorithms.</text>
    <text x="25" y="58" font-size="10" fill="#94a3b8"><tspan font-weight="bold" fill="#6ee7b7">Examples:</tspan> Prolog, LISP, Mercury, Constraint Logic Solvers | <tspan font-weight="bold" fill="#e2e8f0">Hardware Dependency:</tspan> Zero (Fully Abstract)</text>
  </g>

  <!-- 4GL Card -->
  <g transform="translate(85, 166)">
    <rect width="820" height="66" rx="8" fill="#0f172a" stroke="#818cf8" stroke-width="1.5"/>
    <rect width="8" height="66" rx="4" fill="#6366f1"/>
    <text x="25" y="22" font-size="13" font-weight="bold" fill="#a5b4fc">4GL &mdash; Fourth Generation: Very High-Level / Declarative (1970s &ndash; Present)</text>
    <text x="25" y="42" font-size="10.5" fill="#cbd5e1"><tspan font-weight="bold" fill="#94a3b8">Characteristics:</tspan> Non-procedural. Developer declares <tspan font-weight="bold" fill="#e0e7ff">WHAT</tspan> result is needed, not <tspan font-weight="bold" fill="#e0e7ff">HOW</tspan> to compute it.</text>
    <text x="25" y="58" font-size="10" fill="#94a3b8"><tspan font-weight="bold" fill="#c7d2fe">Examples:</tspan> SQL (<tspan font-family="monospace">SELECT name FROM students WHERE grade=10;</tspan>), R, MATLAB, ABAP</text>
  </g>

  <!-- 3GL Card -->
  <g transform="translate(85, 242)">
    <rect width="820" height="66" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="8" height="66" rx="4" fill="#0284c7"/>
    <text x="25" y="22" font-size="13" font-weight="bold" fill="#38bdf8">3GL &mdash; Third Generation: High-Level Procedural &amp; Structured (1950s &ndash; 1970s)</text>
    <text x="25" y="42" font-size="10.5" fill="#cbd5e1"><tspan font-weight="bold" fill="#94a3b8">Characteristics:</tspan> Machine-independent, English-like syntax, mathematical notation, structured loops &amp; functions.</text>
    <text x="25" y="58" font-size="10" fill="#94a3b8"><tspan font-weight="bold" fill="#7dd3fc">Examples:</tspan> C, C++, Java, Python, BASIC, Pascal | <tspan font-weight="bold" fill="#e2e8f0">Translators:</tspan> Compilers &amp; Interpreters</text>
  </g>

  <!-- 2GL Card -->
  <g transform="translate(85, 318)">
    <rect width="820" height="66" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="8" height="66" rx="4" fill="#d97706"/>
    <text x="25" y="22" font-size="13" font-weight="bold" fill="#fbbf24">2GL &mdash; Second Generation: Assembly Language (1950s)</text>
    <text x="25" y="42" font-size="10.5" fill="#cbd5e1"><tspan font-weight="bold" fill="#94a3b8">Characteristics:</tspan> Low-level mnemonics (<tspan font-family="monospace">MOV, ADD, SUB, JMP</tspan>). Highly machine-dependent; 1-to-1 instruction mapping.</text>
    <text x="25" y="58" font-size="10" fill="#94a3b8"><tspan font-weight="bold" fill="#fde68a">Translator:</tspan> Assembler | <tspan font-weight="bold" fill="#e2e8f0">Hardware Dependency:</tspan> Strict (Tied to specific CPU architecture)</text>
  </g>

  <!-- 1GL Card -->
  <g transform="translate(85, 394)">
    <rect width="820" height="66" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="8" height="66" rx="4" fill="#dc2626"/>
    <text x="25" y="22" font-size="13" font-weight="bold" fill="#f87171">1GL &mdash; First Generation: Machine Language (Late 1940s)</text>
    <text x="25" y="42" font-size="10.5" fill="#cbd5e1"><tspan font-weight="bold" fill="#94a3b8">Characteristics:</tspan> Raw binary strings (<tspan font-family="monospace">01100010 10101111</tspan>). Native execution on hardware switches with 0 translation overhead.</text>
    <text x="25" y="58" font-size="10" fill="#94a3b8"><tspan font-weight="bold" fill="#fca5a5">Readability:</tspan> Extremely hard for humans | <tspan font-weight="bold" fill="#e2e8f0">Portability:</tspan> None (Tied to physical transistor wiring)</text>
  </g>

  <!-- Bottom Legend -->
  <g transform="translate(85, 470)">
    <text x="0" y="14" font-size="10.5" fill="#94a3b8"><tspan font-weight="bold" fill="#e2e8f0">Manufacturing Analogy:</tspan> 1GL = Hand-chopping raw tree &bull; 2GL = Standard hand tools &bull; 3GL = Factory machines &bull; 4GL = Flat-pack furniture &bull; 5GL = AI automated design</text>
  </g>
</svg>
""")

SVG_PARADIGMS_COMPARISON = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Major Programming Paradigms (Philosophies of Computation)</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">How different architectural approaches organize logic, state, data structures, and execution flow</text>

  <!-- 4 Quadrants -->
  <!-- Quadrant 1: Structured Programming -->
  <g transform="translate(45, 90)">
    <rect width="415" height="185" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="415" height="30" rx="8" fill="#0369a1"/>
    <text x="207.5" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Structured Programming</text>

    <text x="18" y="52" font-size="11" font-weight="bold" fill="#38bdf8">Core Concept: The 3 Canonical Constructs</text>
    <text x="18" y="70" font-size="10" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#7dd3fc">Sequence:</tspan> Strict statement-by-statement execution order.</text>
    <text x="18" y="86" font-size="10" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#7dd3fc">Selection:</tspan> Branching logic based on conditions (<tspan font-family="monospace">if / else</tspan>).</text>
    <text x="18" y="102" font-size="10" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#7dd3fc">Iteration:</tspan> Repetition of blocks (<tspan font-family="monospace">for / while</tspan>).</text>

    <rect x="18" y="118" width="379" height="48" rx="6" fill="#1e293b"/>
    <text x="28" y="136" font-size="9.5" fill="#f87171">&#10006; Strictly eliminates spaghetti code and uncontrolled <tspan font-family="monospace">goto</tspan> jumps.</text>
    <text x="28" y="154" font-size="9.5" fill="#94a3b8"><tspan font-weight="bold" fill="#cbd5e1">Languages:</tspan> Pascal, C, Structured BASIC, Ada</text>
  </g>

  <!-- Quadrant 2: Procedural Programming -->
  <g transform="translate(500, 90)">
    <rect width="415" height="185" rx="10" fill="#0f172a" stroke="#818cf8" stroke-width="1.5"/>
    <rect width="415" height="30" rx="8" fill="#4338ca"/>
    <text x="207.5" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Procedural Programming</text>

    <text x="18" y="52" font-size="11" font-weight="bold" fill="#a5b4fc">Core Concept: Modular Functions &amp; Procedures</text>
    <text x="18" y="70" font-size="10" fill="#cbd5e1">&#8226; Programs broken into reusable subroutines / procedures.</text>
    <text x="18" y="86" font-size="10" fill="#cbd5e1">&#8226; Execution driven by calling functions with parameters and return values.</text>
    <text x="18" y="102" font-size="10" fill="#cbd5e1">&#8226; Clear separation of data (variables) and behavior (functions).</text>

    <rect x="18" y="118" width="379" height="48" rx="6" fill="#1e293b"/>
    <text x="28" y="136" font-size="9.5" fill="#34d399">&#10004; High code reusability, modular testing, and top-down design.</text>
    <text x="28" y="154" font-size="9.5" fill="#94a3b8"><tspan font-weight="bold" fill="#cbd5e1">Languages:</tspan> C, Fortran, Pascal, COBOL</text>
  </g>

  <!-- Quadrant 3: Object-Oriented Programming (OOP) -->
  <g transform="translate(45, 295)">
    <rect width="415" height="190" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="415" height="30" rx="8" fill="#059669"/>
    <text x="207.5" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Object-Oriented Programming (OOP)</text>

    <text x="18" y="52" font-size="11" font-weight="bold" fill="#34d399">Core Concept: Classes, Objects &amp; Encapsulation</text>
    <text x="18" y="70" font-size="10" fill="#cbd5e1">&#8226; Models real-world entities: Bundles data (attributes) + methods.</text>
    <text x="18" y="86" font-size="10" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#6ee7b7">Encapsulation:</tspan> Internal state hidden from external corruption.</text>
    <text x="18" y="102" font-size="10" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#6ee7b7">Inheritance &amp; Polymorphism:</tspan> Specialized sub-classes reuse logic.</text>

    <rect x="18" y="118" width="379" height="52" rx="6" fill="#1e293b"/>
    <text x="28" y="136" font-size="9.5" fill="#6ee7b7">&#10004; Ideal for enterprise, large software systems, and GUI frameworks.</text>
    <text x="28" y="154" font-size="9.5" fill="#94a3b8"><tspan font-weight="bold" fill="#cbd5e1">Languages:</tspan> Java, C++, Python, C#, Kotlin, Swift</text>
  </g>

  <!-- Quadrant 4: Event-Driven Programming -->
  <g transform="translate(500, 295)">
    <rect width="415" height="190" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="415" height="30" rx="8" fill="#d97706"/>
    <text x="207.5" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">4. Event-Driven Programming</text>

    <text x="18" y="52" font-size="11" font-weight="bold" fill="#fbbf24">Core Concept: Asynchronous Listeners &amp; Handlers</text>
    <text x="18" y="70" font-size="10" fill="#cbd5e1">&#8226; Program execution flow is dictated by external events.</text>
    <text x="18" y="86" font-size="10" fill="#cbd5e1">&#8226; Events: Mouse clicks, key presses, sensor signals, network messages.</text>
    <text x="18" y="102" font-size="10" fill="#cbd5e1">&#8226; Main loop listens continuously; triggers registered Callback Handlers.</text>

    <rect x="18" y="118" width="379" height="52" rx="6" fill="#1e293b"/>
    <text x="28" y="136" font-size="9.5" fill="#fde68a">&#10004; Perfect for web apps, mobile touchscreens, robotics, and Scratch.</text>
    <text x="28" y="154" font-size="9.5" fill="#94a3b8"><tspan font-weight="bold" fill="#cbd5e1">Languages:</tspan> JavaScript, Python (Tkinter/Pygame), Scratch, C# GUI</text>
  </g>
</svg>
""")

SVG_COMPILER_VS_INTERPRETER = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Language Translators: Compilers vs. Interpreters vs. Assemblers</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Contrasting Ahead-of-Time Binary Compilation against Real-Time Line-by-Line Execution</text>

  <!-- Panel 1: Compiler Pipeline -->
  <g transform="translate(45, 90)">
    <rect width="415" height="235" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="415" height="32" rx="8" fill="#0284c7"/>
    <text x="207.5" y="21" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">A. Compiler Workflow (Ahead-of-Time)</text>

    <!-- Steps -->
    <g transform="translate(15, 45)">
      <!-- Box 1: Source File -->
      <rect x="0" y="0" width="85" height="45" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <text x="42.5" y="20" font-size="9" font-weight="bold" fill="#e0f2fe" text-anchor="middle">Source File</text>
      <text x="42.5" y="34" font-size="8" fill="#7dd3fc" text-anchor="middle">main.c / .cpp</text>

      <path d="M 88 22 L 108 22" stroke="#38bdf8" stroke-width="2" fill="none"/>

      <!-- Box 2: Compiler -->
      <rect x="110" y="0" width="85" height="45" rx="6" fill="#0369a1" stroke="#38bdf8" stroke-width="1"/>
      <text x="152.5" y="20" font-size="9.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Compiler</text>
      <text x="152.5" y="34" font-size="8" fill="#bae6fd" text-anchor="middle">Full Scan &amp; AST</text>

      <path d="M 198 22 L 218 22" stroke="#38bdf8" stroke-width="2" fill="none"/>

      <!-- Box 3: Binary Executable -->
      <rect x="220" y="0" width="85" height="45" rx="6" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
      <text x="262.5" y="20" font-size="9" font-weight="bold" fill="#86efac" text-anchor="middle">Binary File</text>
      <text x="262.5" y="34" font-size="8" fill="#4ade80" text-anchor="middle">app.exe / ELF</text>

      <path d="M 308 22 L 328 22" stroke="#22c55e" stroke-width="2" fill="none"/>

      <!-- Box 4: CPU Run -->
      <rect x="330" y="0" width="55" height="45" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="1"/>
      <text x="357.5" y="22" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">CPU</text>
      <text x="357.5" y="36" font-size="7.5" fill="#a7f3d0" text-anchor="middle">Fast Run</text>
    </g>

    <g transform="translate(15, 105)">
      <text x="0" y="15" font-size="10" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#38bdf8">Compile-Time Check:</tspan> Scans entire file at once. If error exists, NO file produced.</text>
      <text x="0" y="33" font-size="10" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#38bdf8">Run-Time Execution:</tspan> Blazing fast native speed (Zero translation delay).</text>
      <text x="0" y="51" font-size="10" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#38bdf8">Distribution:</tspan> End user does NOT need source code or compiler.</text>
      <text x="0" y="69" font-size="9.5" fill="#94a3b8"><tspan font-weight="bold" fill="#cbd5e1">Examples:</tspan> C, C++, Rust, Go, Fortran</text>
      <text x="0" y="87" font-size="9.5" fill="#e0f2fe"><tspan font-weight="bold" fill="#0284c7">Analogy:</tspan> Book translator prints complete Spanish edition beforehand.</text>
    </g>
  </g>

  <!-- Panel 2: Interpreter Pipeline -->
  <g transform="translate(500, 90)">
    <rect width="415" height="235" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="415" height="32" rx="8" fill="#d97706"/>
    <text x="207.5" y="21" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">B. Interpreter Workflow (Line-by-Line)</text>

    <!-- Steps -->
    <g transform="translate(15, 45)">
      <!-- Box 1: Source File -->
      <rect x="0" y="0" width="85" height="45" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1"/>
      <text x="42.5" y="20" font-size="9" font-weight="bold" fill="#fef3c7" text-anchor="middle">Source File</text>
      <text x="42.5" y="34" font-size="8" fill="#fde68a" text-anchor="middle">script.py / .js</text>

      <path d="M 88 22 L 108 22" stroke="#fbbf24" stroke-width="2" fill="none"/>

      <!-- Box 2: Interpreter Engine -->
      <rect x="110" y="0" width="130" height="45" rx="6" fill="#78350f" stroke="#f59e0b" stroke-width="1"/>
      <text x="175" y="18" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Interpreter Engine</text>
      <text x="175" y="34" font-size="7.5" fill="#fef08a" text-anchor="middle">Reads line &rarr; Translates</text>

      <path d="M 243 22 L 263 22" stroke="#f59e0b" stroke-width="2" fill="none"/>

      <!-- Box 3: Immediate Execution -->
      <rect x="265" y="0" width="120" height="45" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
      <text x="325" y="18" font-size="9" font-weight="bold" fill="#fde68a" text-anchor="middle">Immediate Action</text>
      <text x="325" y="34" font-size="7.5" fill="#cbd5e1" text-anchor="middle">CPU runs line now</text>
    </g>

    <g transform="translate(15, 105)">
      <text x="0" y="15" font-size="10" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#fbbf24">Run-Time Translation:</tspan> Translates and executes line-by-line in real-time.</text>
      <text x="0" y="33" font-size="10" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#fbbf24">Error Behavior:</tspan> Runs lines 1..N-1, crashes ONLY when hitting error line.</text>
      <text x="0" y="51" font-size="10" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#fbbf24">No Executable File:</tspan> Must have interpreter installed to run.</text>
      <text x="0" y="69" font-size="9.5" fill="#94a3b8"><tspan font-weight="bold" fill="#cbd5e1">Examples:</tspan> Python, JavaScript, Ruby, PHP</text>
      <text x="0" y="87" font-size="9.5" fill="#fef3c7"><tspan font-weight="bold" fill="#d97706">Analogy:</tspan> Live diplomatic interpreter translating speech sentence-by-sentence.</text>
    </g>
  </g>

  <!-- Bottom Comparison Summary Table -->
  <g transform="translate(45, 340)">
    <rect width="870" height="145" rx="10" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <rect width="870" height="26" rx="8" fill="#334155"/>
    <text x="435" y="18" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Translator Comparison Matrix</text>

    <!-- Table Header -->
    <g transform="translate(20, 48)">
      <text x="0" y="0" font-size="10" font-weight="bold" fill="#38bdf8">Feature</text>
      <text x="170" y="0" font-size="10" font-weight="bold" fill="#38bdf8">Compiler</text>
      <text x="410" y="0" font-size="10" font-weight="bold" fill="#fbbf24">Interpreter</text>
      <text x="650" y="0" font-size="10" font-weight="bold" fill="#34d399">Assembler</text>
      <line x1="0" y1="8" x2="830" y2="8" stroke="#334155" stroke-width="1"/>
    </g>

    <!-- Row 1 -->
    <g transform="translate(20, 72)">
      <text x="0" y="0" font-size="9.5" fill="#cbd5e1">Input Format</text>
      <text x="170" y="0" font-size="9.5" fill="#cbd5e1">High-Level Source Code</text>
      <text x="410" y="0" font-size="9.5" fill="#cbd5e1">High-Level Source Code</text>
      <text x="650" y="0" font-size="9.5" fill="#cbd5e1">Assembly Mnemonics (2GL)</text>
    </g>

    <!-- Row 2 -->
    <g transform="translate(20, 92)">
      <text x="0" y="0" font-size="9.5" fill="#86efac">Standalone Binary (.exe/ELF)</text>
      <text x="410" y="0" font-size="9.5" fill="#fca5a5">No binary file produced</text>
      <text x="650" y="0" font-size="9.5" fill="#86efac">Native Machine Code Object</text>
    </g>

    <!-- Row 3 -->
    <g transform="translate(20, 112)">
      <text x="0" y="0" font-size="9.5" fill="#cbd5e1">Execution Speed</text>
      <text x="170" y="0" font-size="9.5" fill="#86efac">Very Fast (Native CPU speed)</text>
      <text x="410" y="0" font-size="9.5" fill="#fca5a5">Slower (Run-time overhead)</text>
      <text x="650" y="0" font-size="9.5" fill="#86efac">Very Fast (Native CPU speed)</text>
    </g>

    <!-- Row 4 -->
    <g transform="translate(20, 132)">
      <text x="0" y="0" font-size="9.5" fill="#cbd5e1">Debugging Phase</text>
      <text x="170" y="0" font-size="9.5" fill="#cbd5e1">Compile-Time (Pre-run)</text>
      <text x="410" y="0" font-size="9.5" fill="#cbd5e1">Run-Time (Line-by-line)</text>
      <text x="650" y="0" font-size="9.5" fill="#cbd5e1">Assembly-Time (Syntax)</text>
    </g>
  </g>
</svg>
""")

SVG_CPU_REGISTER_TRACE = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Under the Hood: CPU Register State Simulation &amp; Program Trace</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Tracing Low-Level Assembly Instructions: LOAD R1, 8 | LOAD R2, 4 | ADD R1, R2 | STORE R1 | HALT</text>

  <!-- Left: Assembly Program Listing -->
  <g transform="translate(45, 90)">
    <rect width="250" height="390" rx="10" fill="#0f172a" stroke="#818cf8" stroke-width="1.5"/>
    <rect width="250" height="32" rx="8" fill="#4338ca"/>
    <text x="125" y="21" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Assembly Instruction Sequence</text>

    <!-- Instruction Lines -->
    <g transform="translate(15, 48)">
      <!-- Line 1 -->
      <rect x="0" y="0" width="220" height="48" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <text x="10" y="20" font-size="11" font-family="monospace" font-weight="bold" fill="#38bdf8">1. LOAD R1, 8</text>
      <text x="10" y="38" font-size="9" fill="#94a3b8">; Load value 8 into register R1</text>

      <!-- Line 2 -->
      <rect x="0" y="58" width="220" height="48" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <text x="10" y="78" font-size="11" font-family="monospace" font-weight="bold" fill="#38bdf8">2. LOAD R2, 4</text>
      <text x="10" y="96" font-size="9" fill="#94a3b8">; Load value 4 into register R2</text>

      <!-- Line 3 -->
      <rect x="0" y="116" width="220" height="48" rx="6" fill="#1e293b" stroke="#22c55e" stroke-width="1"/>
      <text x="10" y="136" font-size="11" font-family="monospace" font-weight="bold" fill="#4ade80">3. ADD  R1, R2</text>
      <text x="10" y="154" font-size="9" fill="#94a3b8">; R1 = R1 + R2 (8 + 4 = 12)</text>

      <!-- Line 4 -->
      <rect x="0" y="174" width="220" height="48" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
      <text x="10" y="194" font-size="11" font-family="monospace" font-weight="bold" fill="#fbbf24">4. STORE R1</text>
      <text x="10" y="212" font-size="9" fill="#94a3b8">; Send R1 value to output bus</text>

      <!-- Line 5 -->
      <rect x="0" y="232" width="220" height="48" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
      <text x="10" y="252" font-size="11" font-family="monospace" font-weight="bold" fill="#f87171">5. HALT</text>
      <text x="10" y="270" font-size="9" fill="#94a3b8">; Terminate clock &amp; execution</text>
    </g>
  </g>

  <!-- Right: CPU Architecture & Step Trace -->
  <g transform="translate(315, 90)">
    <!-- CPU Visual Registers -->
    <g transform="translate(0, 0)">
      <rect width="600" height="150" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
      <text x="300" y="22" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">CPU Internal Hardware State (At Step 3)</text>

      <!-- Register R1 Box -->
      <g transform="translate(30, 38)">
        <rect width="160" height="95" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="80" y="24" font-size="11" font-weight="bold" fill="#7dd3fc" text-anchor="middle">Register 1 (R1)</text>
        <rect x="25" y="35" width="110" height="45" rx="6" fill="#0369a1"/>
        <text x="80" y="65" font-size="22" font-family="monospace" font-weight="bold" fill="#ffffff" text-anchor="middle">12</text>
      </g>

      <!-- ALU Arithmetic Logic Unit -->
      <g transform="translate(220, 38)">
        <polygon points="20,10 140,10 120,85 40,85" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
        <text x="80" y="42" font-size="11" font-weight="bold" fill="#a5b4fc" text-anchor="middle">ALU Unit</text>
        <text x="80" y="65" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">8 + 4 = 12</text>
      </g>

      <!-- Register R2 Box -->
      <g transform="translate(410, 38)">
        <rect width="160" height="95" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
        <text x="80" y="24" font-size="11" font-weight="bold" fill="#fde68a" text-anchor="middle">Register 2 (R2)</text>
        <rect x="25" y="35" width="110" height="45" rx="6" fill="#78350f"/>
        <text x="80" y="65" font-size="22" font-family="monospace" font-weight="bold" fill="#ffffff" text-anchor="middle">4</text>
      </g>
    </g>

    <!-- Trace Table -->
    <g transform="translate(0, 165)">
      <rect width="600" height="225" rx="10" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
      <rect width="600" height="28" rx="8" fill="#334155"/>
      <text x="300" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Step-by-Step Register Execution Trace Table</text>

      <!-- Header -->
      <g transform="translate(15, 48)">
        <text x="0" y="0" font-size="10" font-weight="bold" fill="#38bdf8">Step</text>
        <text x="45" y="0" font-size="10" font-weight="bold" fill="#38bdf8">Instruction</text>
        <text x="210" y="0" font-size="10" font-weight="bold" fill="#38bdf8">R1 Value</text>
        <text x="310" y="0" font-size="10" font-weight="bold" fill="#38bdf8">R2 Value</text>
        <text x="430" y="0" font-size="10" font-weight="bold" fill="#38bdf8">Screen / Output</text>
        <line x1="0" y1="8" x2="570" y2="8" stroke="#334155" stroke-width="1"/>
      </g>

      <!-- Row 0: Start -->
      <g transform="translate(15, 72)">
        <text x="0" y="0" font-size="9.5" fill="#94a3b8">0</text>
        <text x="45" y="0" font-size="9.5" fill="#94a3b8">(Initial State)</text>
        <text x="210" y="0" font-size="9.5" font-family="monospace" fill="#94a3b8">0</text>
        <text x="310" y="0" font-size="9.5" font-family="monospace" fill="#94a3b8">0</text>
        <text x="430" y="0" font-size="9.5" fill="#94a3b8">&mdash;</text>
      </g>

      <!-- Row 1 -->
      <g transform="translate(15, 96)">
        <text x="0" y="0" font-size="9.5" fill="#e2e8f0">1</text>
        <text x="45" y="0" font-size="9.5" font-family="monospace" fill="#38bdf8">LOAD R1, 8</text>
        <text x="210" y="0" font-size="9.5" font-family="monospace" font-weight="bold" fill="#38bdf8">8</text>
        <text x="310" y="0" font-size="9.5" font-family="monospace" fill="#94a3b8">0</text>
        <text x="430" y="0" font-size="9.5" fill="#94a3b8">&mdash;</text>
      </g>

      <!-- Row 2 -->
      <g transform="translate(15, 120)">
        <text x="0" y="0" font-size="9.5" fill="#e2e8f0">2</text>
        <text x="45" y="0" font-size="9.5" font-family="monospace" fill="#38bdf8">LOAD R2, 4</text>
        <text x="210" y="0" font-size="9.5" font-family="monospace" fill="#cbd5e1">8</text>
        <text x="310" y="0" font-size="9.5" font-family="monospace" font-weight="bold" fill="#fbbf24">4</text>
        <text x="430" y="0" font-size="9.5" fill="#94a3b8">&mdash;</text>
      </g>

      <!-- Row 3 -->
      <g transform="translate(15, 144)">
        <text x="0" y="0" font-size="9.5" fill="#e2e8f0">3</text>
        <text x="45" y="0" font-size="9.5" font-family="monospace" fill="#4ade80">ADD R1, R2</text>
        <text x="210" y="0" font-size="9.5" font-family="monospace" font-weight="bold" fill="#4ade80">12 (8+4)</text>
        <text x="310" y="0" font-size="9.5" font-family="monospace" fill="#cbd5e1">4</text>
        <text x="430" y="0" font-size="9.5" fill="#94a3b8">&mdash;</text>
      </g>

      <!-- Row 4 -->
      <g transform="translate(15, 168)">
        <text x="0" y="0" font-size="9.5" fill="#e2e8f0">4</text>
        <text x="45" y="0" font-size="9.5" font-family="monospace" fill="#fbbf24">STORE R1</text>
        <text x="210" y="0" font-size="9.5" font-family="monospace" fill="#cbd5e1">12</text>
        <text x="310" y="0" font-size="9.5" font-family="monospace" fill="#cbd5e1">4</text>
        <text x="430" y="0" font-size="10" font-family="monospace" font-weight="bold" fill="#86efac">12</text>
      </g>

      <!-- Row 5 -->
      <g transform="translate(15, 192)">
        <text x="0" y="0" font-size="9.5" fill="#e2e8f0">5</text>
        <text x="45" y="0" font-size="9.5" font-family="monospace" fill="#f87171">HALT</text>
        <text x="210" y="0" font-size="9.5" font-family="monospace" fill="#cbd5e1">12</text>
        <text x="310" y="0" font-size="9.5" font-family="monospace" fill="#cbd5e1">4</text>
        <text x="430" y="0" font-size="9" fill="#fca5a5">[Execution Halted]</text>
      </g>
    </g>
  </g>
</svg>
""")

# =====================================================================
# CURRICULUM DATA DECONSTRUCTION
# =====================================================================

def build_topic12_curriculum():
    return [
        # -------------------------------------------------------------
        # LEARNING UNIT 1 / LESSON 42
        # -------------------------------------------------------------
        {
            "unit_order": 1,
            "unit_name": "Programming Terminology and Program Representation",
            "unit_description": "Fundamental concepts of computer software: definitions, source code vs. machine code, syntax vs. semantics, debugging, and how computers represent programs.",
            "lesson_title": "Programming Terminology and Program Representation",
            "pages": [
                # Page 1: Hook & Core Concepts
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Programming Terminology and Program Representation",
                        "content": {
                            "goal": "Define fundamental programming terminology (programs, source code, machine code, syntax, semantics, debugging, IDEs) and explain how algorithmic instructions are represented and executed in computer hardware."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Cake Recipe Analogy & The Nature of Software",
                        "content": {
                            "markdown": """### **The 'Cake Recipe' Analogy & Software Fundamentals**

Imagine you want to teach a friend how to bake your favorite chocolate cake. If you simply hand them a mixing bowl and say "make a cake," they will be lost. To ensure success, you must write a **recipe**: a clear, unambiguous, step-by-step sequence of instructions written in a language they understand (such as English or Kiswahili).

A successful recipe requires precision:
1. **Instruction**: *"Preheat the oven to 180°C."*
2. **Data & Action**: *"Mix 200g of sugar and 3 fresh eggs."*
3. **Logic / Semantic Error**: If you accidentally write *"Bake for 3 hours"* instead of *"30 minutes,"* the friend follows your instruction perfectly, but the cake burns to ash.
4. **Syntax Error**: If you write *"Flour sugar mix oven"* instead of *"Mix flour and sugar,"* your friend cannot parse the sentence structure and halts immediately.

In computer science, a **computer program** functions exactly like that recipe. The computer is an extraordinarily fast, but entirely unthinking electronic device. It will execute instructions *literally* as written, without question or intuition. To communicate these instructions, software engineers use **programming languages**."""
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Grace Hopper: Programming Pioneer",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/a/ad/Commodore_Grace_M._Hopper%2C_USN_%28covered%29.jpg",
                            "caption": "Rear Admiral Grace Hopper, pioneer of computer programming and inventor of the first high-level language compiler (A-0) and co-designer of COBOL.",
                            "author": "United States Navy",
                            "licensing": "Public Domain"
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Programming Lexicon",
                        "content": {
                            "points": [
                                "**Program**: A complete sequence of precise, step-by-step instructions telling a computer how to execute a specific task.",
                                "**Programming**: The end-to-end engineering process of designing, writing, testing, and maintaining source code.",
                                "**Programming Language**: A formal system of syntax rules and keywords used to instruct hardware.",
                                "**Source Code**: Human-readable program text written in a high-level language (e.g., Python, C++, Java).",
                                "**Machine Code**: Native binary instructions (`0`s and `1`s) executed directly by CPU logic circuits.",
                                "**Syntax**: The strict grammatical rules governing statement formation.",
                                "**Semantics**: The underlying logic, behavior, and meaning of syntactically valid code.",
                                "**Bug & Debugging**: A bug is any flaw causing unintended behavior; debugging is the systematic discovery and resolution of bugs.",
                                "**IDE (Integrated Development Environment)**: A unified software suite combining code editor, translator, and interactive debugger."
                            ]
                        }
                    }
                ],

                # Page 2: Representation & Translation Pipeline
                [
                    {
                        "type": "concept_explanation",
                        "title": "Under the Hood: How Hardware Represents Programs",
                        "content": {
                            "markdown": """### **Under the Hood: From Text to Transistor Voltages**

A physical CPU chip cannot inherently comprehend English words like `PRINT`, `IF`, or `WHILE`. Modern processors are silicon chips containing billions of microscopic electronic switches called **transistors**.

Transistors operate in two discrete electrical states:
- **High Voltage (~1.2V to 3.3V)**: Evaluated digitally as binary `1` (True / Closed switch).
- **Low Voltage (~0V / Ground)**: Evaluated digitally as binary `0` (False / Open switch).

Because hardware is purely electrical, all software must be translated into **machine code**—a continuous stream of binary patterns. 

When you write a simple assignment in Python:
```python
x = 5 + 3
```
A language translator decomposes this single high-level command into several low-level machine instructions:
1. Load the constant `5` into CPU Register `R1`.
2. Load the constant `3` into CPU Register `R2`.
3. Signal the **Arithmetic Logic Unit (ALU)** to compute `R1 + R2`.
4. Store the resulting sum (`8`) into the memory address allocated for variable `x`."""
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "The Program Translation and Execution Pipeline",
                        "content": {
                            "svg_content": SVG_PROGRAM_EXECUTION_PIPELINE,
                            "caption": "Figure 12.1: The end-to-end software execution lifecycle, illustrating the progression from human thought to high-level source code, translator parsing, binary machine code, and silicon register execution."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "How Computers Execute Code Under the Hood",
                        "content": {
                            "youtube_id": "Mv2XQgfpT30",
                            "url": "https://www.youtube.com/watch?v=Mv2XQgfpT30",
                            "description": "An illustrated deep-dive into how instructions are fetched, decoded, and executed by hardware circuits."
                        }
                    }
                ],

                # Page 3: Activity & Diagnostics
                [
                    {
                        "type": "activity",
                        "title": "Hands-On Audit: Syntax vs. Semantics",
                        "content": {
                            "markdown": """### **Class Activity: The Syntax vs. Semantics Audit**

**Objective**: Develop analytical precision in differentiating between grammatical correctness (Syntax) and logical meaning (Semantics).

#### **Scenario Analysis: Natural Language & Code**
Evaluate the four natural language sentences below and classify each as **Valid**, **Syntax Error**, or **Semantic Error**:

1. *"The cat drank the cold milk."* &rarr; **Valid** (Grammar and meaning are both sound).
2. *"The milk drank the cold cat."* &rarr; **Semantic Error** (Grammatically correct English structure, but physically impossible / nonsensical meaning).
3. *"Drank cat milk cold the."* &rarr; **Syntax Error** (Invalid word order; violates English grammatical rules).
4. *"The blue triangle smells like an alarm clock."* &rarr; **Semantic Error** (Valid sentence construction, but meaningless logic).

#### **Programming Translation Equivalent**
- **Syntax Error in Python**:
  ```python
  prnt("Welcome to Grade 10 CS")  # NameError / Syntax Error - Interpreter halts before execution
  ```
- **Semantic / Logic Error in Python**:
  ```python
  length = 20
  width = 10
  area = length + width  # Runs smoothly, but computes 30 instead of 200!
  ```"""
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Real-World Case Study: Automated Irrigation Bug",
                        "content": {
                            "problem": "A farmer in Nakuru installs an automated IoT irrigation system. The valve must open ONLY if the soil moisture sensor reads below 20%. However, during a torrential thunderstorm where soil moisture is at 95%, the valve opens and floods the entire crop field. Analyze the bug type and provide a systematic troubleshooting path.",
                            "steps": [
                                "1. Bug Classification: This is a Semantic / Logic Error. The code syntax was valid because the program ran on the microcontroller without crashing, but the logical operator was inverted.",
                                "2. Root Cause Analysis: The programmer likely wrote `if (soil_moisture > 20): open_valve()` instead of `if (soil_moisture < 20): open_valve()` or misplaced a sensor calibration threshold.",
                                "3. Systematic Debugging Path:\n   a. Read the live telemetry from the soil moisture sensor via serial terminal.\n   b. Inspect the conditional branching statement inside the controller source code.\n   c. Correct the comparison operator to `< 20`.\n   d. Conduct unit testing with simulated moisture values (e.g., 10%, 20%, 90%) before reconnecting the physical water pump actuator."
                            ]
                        }
                    }
                ],

                # Page 4: Knowledge Checks
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Terminology and Program Representation",
                        "content": {
                            "question": "Which of the following best defines 'Source Code' in computer programming?",
                            "options": [
                                "The raw electrical high and low voltages traversing the CPU system bus",
                                "Human-readable program instructions written in a high-level programming language",
                                "The binary machine instructions stored directly in read-only memory (ROM)",
                                "The metallic chassis protecting computer circuit boards"
                            ],
                            "correct_answer": 1,
                            "explanation": "Source code refers to the high-level, human-readable text written by programmers using formal languages such as Python, Java, or C++. It must be translated into binary machine code before hardware can execute it."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Error Identification",
                        "content": {
                            "question": "A student creates a program to calculate the average exam score of a class. The program runs without crashing, but outputs a final average of -45. What category of error has occurred?",
                            "options": [
                                "Syntax Error",
                                "Semantic / Logic Error",
                                "CPU Hardware Interruption",
                                "Network Collision"
                            ],
                            "correct_answer": 1,
                            "explanation": "Because the program compiled and executed without violating language grammar rules, the syntax is valid. However, the calculation produced an incorrect, nonsensical result, indicating a Semantic (Logical) Error in the algorithm."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Hardware Program Execution",
                        "content": {
                            "question": "Why is a CPU unable to directly execute high-level Python or C++ source code files without an intermediary translator?",
                            "options": [
                                "High-level languages require too much physical disk storage for the CPU",
                                "Microscopic transistor circuits only respond to binary electrical switching states (0s and 1s)",
                                "CPUs can only understand spoken human language",
                                "High-level code is encrypted with proprietary digital signatures"
                            ],
                            "correct_answer": 1,
                            "explanation": "CPUs are physical silicon devices composed of billions of transistors that operate exclusively on binary electrical signals (high voltage for 1, low voltage for 0). Translators are essential to bridge high-level text to binary machine instructions."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Development Environments",
                        "content": {
                            "question": "Which software tool combines a source code editor, an automated compiler/interpreter, and an interactive debugger into a single graphical application?",
                            "options": [
                                "Operating System Kernel",
                                "Integrated Development Environment (IDE)",
                                "Network Interface Card (NIC)",
                                "Arithmetic Logic Unit (ALU)"
                            ],
                            "correct_answer": 1,
                            "explanation": "An Integrated Development Environment (IDE) is a unified application (such as VS Code, PyCharm, or Eclipse) designed to streamline software engineering by combining editing, translation, and debugging tools."
                        }
                    }
                ]
            ]
        },

        # -------------------------------------------------------------
        # LEARNING UNIT 2 / LESSON 43
        # -------------------------------------------------------------
        {
            "unit_order": 2,
            "unit_name": "Evolution and Paradigms of Programming Languages",
            "unit_description": "Chronological generations of programming languages (1GL to 5GL), increasing abstraction, and major paradigms: Structured, Procedural, Object-Oriented, and Event-Driven.",
            "lesson_title": "Evolution and Paradigms of Programming Languages",
            "pages": [
                # Page 1: Generations & Abstraction
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Evolution and Paradigms of Programming Languages",
                        "content": {
                            "goal": "Trace the historical evolution of programming language generations from 1GL to 5GL, and differentiate core programming paradigms including procedural, object-oriented, structured, and event-driven models."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Generational Evolution and Abstraction",
                        "content": {
                            "markdown": """### **The Evolution of Programming Languages: Increasing Abstraction**

The history of software engineering is defined by **abstraction**: the deliberate hiding of low-level hardware complexity to allow developers to focus on high-level problem solving.

#### **The Manufacturing Abstraction Analogy**
- **1GL (Manual Raw Crafting)**: Chopping a tree by hand with an axe to carve a table. Extremely laborious, error-prone, and slow. (Equivalent to writing raw **Machine Language** binary).
- **2GL (Standardized Hand Tools)**: Using standardized chisels, saws, and planes. Much faster, but still physically demanding and manual. (Equivalent to **Assembly Language** mnemonics).
- **3GL (Factory Machinery)**: Guiding power tools and industrial saws. You steer the process while machines perform the heavy lifting. (Equivalent to **High-Level Languages** like C, Java, and Python).
- **4GL (Flat-Pack Assembly)**: Ordering pre-fabricated furniture and snapping pieces together by following a diagram. You declare *what* you want built. (Equivalent to **Declarative Languages** like SQL).
- **5GL (Intelligent Automation)**: Stating functional constraints to an AI system that generates the furniture model automatically. (Equivalent to **Constraint-Based AI Languages** like Prolog)."""
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Punch Cards: Early 1GL/2GL Medium",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/5/58/Card汇编.80col.agr.jpg",
                            "caption": "An 80-column punched card, used to encode machine instructions and assembly routines in early mainframe computing.",
                            "author": "SecretDisc",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Timeline of Programming Language Generations",
                        "content": {
                            "svg_content": SVG_LANGUAGE_GENERATIONS_TIMELINE,
                            "caption": "Figure 12.2: Chronological progression of programming language generations from 1GL raw machine code to 5GL constraint-based artificial intelligence paradigms."
                        }
                    }
                ],

                # Page 2: Deep-Dive into 1GL - 5GL
                [
                    {
                        "type": "key_takeaway",
                        "title": "The Five Generations of Programming Languages",
                        "content": {
                            "points": [
                                "**1GL — Machine Language (1940s)**: Direct binary (`0`s and `1`s). Machine-dependent, zero translation delay, but extremely difficult to write and maintain.",
                                "**2GL — Assembly Language (1950s)**: Short mnemonic abbreviations (`MOV`, `ADD`, `SUB`, `JMP`). Requires an **Assembler** to convert to binary. Tied to specific CPU architectures.",
                                "**3GL — High-Level Languages (1950s–1970s)**: English-like words, mathematical formulas, portable across CPU architectures (C, Java, Python, Pascal).",
                                "**4GL — Very High-Level / Declarative (1970s–Present)**: Focuses on **WHAT** data to produce rather than **HOW** to compute it. Standard in relational databases (e.g., `SELECT * FROM users WHERE active = 1`).",
                                "**5GL — Constraint-Based & Logic (Present)**: Uses formal facts, rules, and mathematical logic trees for expert systems and AI (e.g., Prolog, LISP)."
                            ]
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "The History and Generations of Programming Languages",
                        "content": {
                            "youtube_id": "pA6g4r7C3r4",
                            "url": "https://www.youtube.com/watch?v=pA6g4r7C3r4",
                            "description": "A visual breakdown of how programming languages evolved from machine punch cards to modern high-level frameworks."
                        }
                    }
                ],

                # Page 3: Programming Paradigms
                [
                    {
                        "type": "concept_explanation",
                        "title": "Programming Paradigms: Ways of Thinking",
                        "content": {
                            "markdown": """### **Programming Paradigms: Architectural Philosophies**

A **programming paradigm** is an overarching approach or methodology used to structure code and organize computation.

#### **1. Structured Programming**
- Enforces strict control flow using three foundational structures: **Sequence**, **Selection** (`if-else`), and **Iteration** (`loops`).
- Eliminates unconditional jump commands (`goto`), preventing tangled, unmaintainable "spaghetti code".
- *Key Languages*: Pascal, C, Structured BASIC.

#### **2. Procedural Programming**
- Organizes large programs into modular, reusable blocks termed **procedures**, **subroutines**, or **functions**.
- Emphasizes step-by-step algorithms with clear separation between state variables and functional operations.
- *Key Languages*: C, Fortran, Pascal.

#### **3. Object-Oriented Programming (OOP)**
- Models systems around real-world entities called **Objects**, instantiated from structural blueprints called **Classes**.
- Encapsulates state data (attributes) together with the behaviors (methods) that manipulate that data.
- Core principles: Encapsulation, Inheritance, and Polymorphism.
- *Key Languages*: Java, C++, Python, C#.

#### **4. Event-Driven Programming**
- Execution order is not predetermined; rather, it responds dynamically to incoming **events** (user taps, mouse clicks, keystrokes, sensor triggers, or network packets).
- Operates via an infinite Event Loop that dispatches signals to registered Callback functions.
- *Key Languages*: JavaScript, Scratch, Python (GUI Tkinter/Pygame), C# Windows Forms."""
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Major Programming Paradigms Compared",
                        "content": {
                            "svg_content": SVG_PARADIGMS_COMPARISON,
                            "caption": "Figure 12.3: Structural comparison of Structured, Procedural, Object-Oriented, and Event-Driven programming paradigms."
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Real-World Architecture Challenge: Mobile Banking Application",
                        "content": {
                            "problem": "A financial tech startup in Nairobi is architecting a mobile banking platform with three core modules: (1) A financial interest calculation engine, (2) A touchscreen GUI that reacts when a user taps 'Transfer Funds', and (3) A database query module to fetch account balances. Recommend appropriate programming paradigms and language generations for each module.",
                            "steps": [
                                "1. Financial Calculation Engine: Use Procedural or Object-Oriented Programming in a 3GL language (e.g., C++ or Java). This provides high mathematical precision, modular unit testing, and robust algorithm performance.",
                                "2. Touchscreen GUI: Use Event-Driven Programming in a high-level 3GL framework (e.g., Kotlin, Swift, or Flutter/Dart). The UI remains in an idle listening state and triggers asynchronous transfer handlers when the screen tap event fires.",
                                "3. Database Module: Use 4GL Declarative Language (SQL) via structured queries (e.g., `SELECT balance FROM accounts WHERE user_id = :id`). The developer specifies WHAT data to retrieve without manually writing low-level disk indexing algorithms."
                            ]
                        }
                    }
                ],

                # Page 4: Knowledge Checks
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Language Generations",
                        "content": {
                            "question": "Which programming language generation is executed natively by hardware circuits without requiring an interpreter, compiler, or assembler?",
                            "options": [
                                "Second Generation (Assembly Language)",
                                "Third Generation (High-Level Language)",
                                "First Generation (Machine Language)",
                                "Fourth Generation (Declarative Language)"
                            ],
                            "correct_answer": 2,
                            "explanation": "First Generation (1GL) Machine Language consists of raw binary 0s and 1s that directly drive CPU electronic circuits, requiring zero software translation."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Declarative Programming",
                        "content": {
                            "question": "A database administrator writes the statement: 'SELECT student_name, score FROM exam_results WHERE grade = 10;'. This query belongs to which language category?",
                            "options": [
                                "1GL Machine Binary",
                                "2GL Assembly Mnemonic",
                                "4GL Very High-Level / Declarative Language",
                                "5GL Expert Constraint Solver"
                            ],
                            "correct_answer": 2,
                            "explanation": "SQL is a Fourth Generation (4GL) Declarative language where the user specifies WHAT data is needed, and the relational database engine automatically determines the most efficient search algorithm."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Event-Driven Systems",
                        "content": {
                            "question": "Which programming paradigm is structured around an event loop that listens for user actions such as mouse clicks, keyboard presses, or sensor triggers?",
                            "options": [
                                "Event-Driven Programming",
                                "Linear Procedural Programming",
                                "Monolithic Machine Programming",
                                "Batch Processing Paradigm"
                            ],
                            "correct_answer": 0,
                            "explanation": "Event-Driven programming models interactive software where execution flow is determined asynchronously by external triggers like user interface actions or hardware interrupts."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Principles of Structured Programming",
                        "content": {
                            "question": "What primary engineering problem did Structured Programming solve when introduced in the late 1960s?",
                            "options": [
                                "It allowed computers to operate without electrical power",
                                "It eliminated unconstrained 'goto' jumps and spaghetti code using sequence, selection, and iteration",
                                "It converted all high-level code directly into natural human speech",
                                "It removed the requirement for RAM in modern computers"
                            ],
                            "correct_answer": 1,
                            "explanation": "Structured Programming replaced chaotic, error-prone 'goto' jump statements with clear sequences, selections (if-else), and iterations (loops), vastly improving software readability and reliability."
                        }
                    }
                ]
            ]
        },

        # -------------------------------------------------------------
        # LEARNING UNIT 3 / LESSON 44
        # -------------------------------------------------------------
        {
            "unit_order": 3,
            "unit_name": "Translation and Execution of Programs",
            "unit_description": "Translators: Compilers vs. Interpreters vs. Assemblers. CPU register simulation, instruction cycles, and step-by-step assembly trace tables.",
            "lesson_title": "Translation and Execution of Programs",
            "pages": [
                # Page 1: Translators: Compilers vs Interpreters
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Translation and Execution of Programs",
                        "content": {
                            "goal": "Distinguish between compilers, interpreters, and assemblers, evaluate their trade-offs in execution speed and error handling, and trace step-by-step assembly instructions in CPU registers."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Translators: Compilers vs. Interpreters",
                        "content": {
                            "markdown": """### **The Diplomat Translators Analogy**

Imagine a foreign diplomat visiting Kenya who speaks only Spanish and needs to understand a 300-page Swahili agricultural manual. There are two primary translation approaches:

- **Method A (The Compiler / Book Translator)**: A professional translator translates all 300 pages of the Swahili book into Spanish, publishes a brand-new Spanish edition, and hands it to the diplomat. The diplomat can now read through the Spanish book at maximum speed, share copies with colleagues, and re-read it anytime without needing the translator again.
- **Method B (The Interpreter / Live Translator)**: A live interpreter sits beside the diplomat. They read sentence 1 in Swahili, translate it into Spanish aloud, wait for the diplomat's response, and proceed to sentence 2. If the diplomat wants to read the book again tomorrow, the live interpreter must repeat the entire translation process sentence by sentence.

#### **Technical Mechanics of Translators**
1. **Compiler**: Translates the entire high-level source file before runtime into a standalone machine binary executable (e.g., `.exe` or Linux ELF). Fast execution, but translation fails if even one syntax error is present. (Examples: C, C++, Rust, Go).
2. **Interpreter**: Reads, parses, and executes source code line-by-line in real-time. Execution is slower due to runtime translation overhead, but debugging is interactive and rapid. (Examples: Python, JavaScript, Ruby).
3. **Assembler**: A specialized low-level translator that maps assembly mnemonics (2GL) directly 1-to-1 into native binary machine code (1GL)."""
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Assembly Code on an Oscilloscope Display",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/7/75/Assembly_language_program_on_screen.jpg",
                            "caption": "Low-level assembly language mnemonics displayed on a developer monitor, illustrating direct register manipulation.",
                            "author": "Gautam Saxena",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Compiler vs. Interpreter Execution Workflows",
                        "content": {
                            "svg_content": SVG_COMPILER_VS_INTERPRETER,
                            "caption": "Figure 12.4: Architectural pipeline comparison of Ahead-of-Time (AOT) Compilers versus Real-Time Interpreters and Assemblers."
                        }
                    }
                ],

                # Page 2: Low-Level Machine Operations & Trace Lab
                [
                    {
                        "type": "concept_explanation",
                        "title": "Low-Level Machine Simulation & Register Mechanics",
                        "content": {
                            "markdown": """### **Simulating CPU Registers and the Instruction Cycle**

Inside the central processor, arithmetic operations do not happen in abstract space; they occur inside microscopic ultra-fast storage cells called **Registers**, manipulated by the **ALU (Arithmetic Logic Unit)**.

#### **Simplified Virtual CPU Architecture**
- **Register 1 (`R1`)**: Internal high-speed accumulator slot.
- **Register 2 (`R2`)**: Secondary internal operand slot.
- **Instruction Set**:
  - `LOAD [Reg], [Value]`: Moves an immediate numeric constant into the specified register.
  - `ADD [RegA], [RegB]`: Instructs the ALU to add the contents of `RegB` to `RegA`, updating `RegA`.
  - `STORE [Reg]`: Outputs the current numerical value stored in the register to the screen/bus.
  - `HALT`: Suspends processor clock cycles and terminates program execution."""
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "CPU Register State Simulation and Trace",
                        "content": {
                            "svg_content": SVG_CPU_REGISTER_TRACE,
                            "caption": "Figure 12.5: Low-level simulation tracing register contents and ALU operations across a five-instruction assembly routine."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Translator Properties Matrix",
                        "content": {
                            "points": [
                                "**Input Source**: Compilers and Interpreters accept 3GL/4GL source code; Assemblers accept 2GL assembly mnemonics.",
                                "**Output File**: Compilers generate standalone binary executables (`.exe`/ELF); Assemblers generate binary object files; Interpreters generate no permanent output file.",
                                "**Execution Speed**: Compiled and assembled programs run at peak hardware speed; Interpreted programs have slower runtime execution due to continuous translation.",
                                "**Error Timing**: Compilers catch all syntax errors at compile-time before execution; Interpreters catch errors at runtime when the specific faulty line is reached."
                            ]
                        }
                    }
                ],

                # Page 3: Step-by-Step Assembly Trace Lab
                [
                    {
                        "type": "worked_example",
                        "title": "Assembly Trace Problem: Step-by-Step Register State Table",
                        "content": {
                            "problem": "Trace the step-by-step execution of the following assembly routine and compute the final output printed to the screen:\n\n1. LOAD  R1, 8\n2. LOAD  R2, 4\n3. ADD   R1, R2\n4. STORE R1\n5. HALT",
                            "steps": [
                                "Initial State: R1 = 0, R2 = 0, Output = None.",
                                "Step 1 (LOAD R1, 8): The integer 8 is moved into R1. (R1 = 8, R2 = 0, Output = None).",
                                "Step 2 (LOAD R2, 4): The integer 4 is moved into R2. (R1 = 8, R2 = 4, Output = None).",
                                "Step 3 (ADD R1, R2): The ALU adds R1 (8) and R2 (4). The result (12) is saved back into R1. (R1 = 12, R2 = 4, Output = None).",
                                "Step 4 (STORE R1): The value inside R1 (12) is dispatched to the output bus. (R1 = 12, R2 = 4, Output = '12').",
                                "Step 5 (HALT): The CPU clock halts execution. Final printed output: 12."
                            ]
                        }
                    },
                    {
                        "type": "activity",
                        "title": "Engineering Scenario: Autonomous Drone Controller",
                        "content": {
                            "markdown": """### **Application Challenge: The Mount Kenya Weather Drone**

**Scenario**: An autonomous high-altitude drone monitors wind speeds on Mount Kenya. The onboard flight stabilization controller must adjust motor speeds 200 times per second (every 5 milliseconds) to avoid turbulence crashes. The onboard microcontroller has limited RAM (512 KB) and cannot tolerate unexpected garbage collection delays or interpreter lag.

**Task**: The software team is debating whether to write the flight control firmware in **Python** (Interpreted) or **C++** (Compiled). 

#### **Engineering Evaluation**
- **Option A (Python)**: Rapid prototyping and easy readability, but suffers from interpreter overhead, higher RAM usage, and non-deterministic execution times. In a 5ms critical stabilization loop, an interpreter delay could cause physical failure.
- **Option B (C++)**: Compiled directly into native ARM machine code ahead-of-time. Operates with predictable microsecond timing, minimal RAM overhead, and maximum CPU efficiency.
- **Recommendation**: Write the core flight control loop in **C++** for mission-critical determinism, while using Python for offline data analysis and telemetry logging on ground servers."""
                        }
                    }
                ],

                # Page 4: Knowledge Checks
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Interpreters vs Compilers",
                        "content": {
                            "question": "What type of language translator parses and executes high-level source code line-by-line without creating a standalone binary executable file?",
                            "options": [
                                "Compiler",
                                "Assembler",
                                "Interpreter",
                                "Linker"
                            ],
                            "correct_answer": 2,
                            "explanation": "An Interpreter directly executes instructions written in a programming language line-by-line in real-time, without producing an intermediate standalone binary file."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Error Halting Behavior",
                        "content": {
                            "question": "If a Python script has a syntax error on line 50, what occurs when the user runs the script with the Python interpreter?",
                            "options": [
                                "The program refuses to run lines 1 through 49 at all",
                                "Lines 1 through 49 execute successfully, and the program crashes only when it reaches line 50",
                                "The CPU automatically fixes the syntax error and completes execution",
                                "The computer initiates a hardware reboot"
                            ],
                            "correct_answer": 1,
                            "explanation": "Because an interpreter processes code sequentially in real-time, statements prior to the syntax error execute normally until the interpreter physically encounters the invalid statement on line 50."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Register Trace Calculation",
                        "content": {
                            "question": "Consider the assembly sequence:\nLOAD R1, 10\nLOAD R2, 15\nADD R1, R2\nSTORE R1\n\nWhat value is sent to the output by STORE R1?",
                            "options": [
                                "10",
                                "15",
                                "25",
                                "1015"
                            ],
                            "correct_answer": 2,
                            "explanation": "LOAD R1, 10 places 10 into R1. LOAD R2, 15 places 15 into R2. ADD R1, R2 adds 10 + 15 = 25 and stores it in R1. STORE R1 outputs the value 25."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Role of Assemblers",
                        "content": {
                            "question": "What is the primary role of an Assembler in computer systems?",
                            "options": [
                                "To translate assembly language mnemonics into native binary machine code",
                                "To physically connect computer chips to motherboard sockets",
                                "To clean virus infections from secondary storage disks",
                                "To convert Python scripts into English speech"
                            ],
                            "correct_answer": 0,
                            "explanation": "An Assembler is a low-level translator designed specifically to convert second-generation (2GL) assembly mnemonics into first-generation (1GL) binary machine instructions."
                        }
                    }
                ]
            ]
        }
    ]

# =====================================================================
# INGESTION EXECUTOR
# =====================================================================

def ingest_grade10_topic12(replace: bool = True):
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 10 Computer Science — Topic 12")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(id=5).first()
    if not curriculum:
        print("[!] Error: CBC Curriculum (ID: 5) not found.")
        return

    grade = Grade.objects.filter(curriculum=curriculum, level=10).first()
    if not grade:
        print("[!] Error: Grade 10 not found.")
        return

    subject = Subject.objects.filter(grade=grade, name__icontains="Computer Science").first()
    if not subject:
        print("[!] Error: Computer Science subject not found.")
        return

    print(f"[*] Target Curriculum: {curriculum.name} (ID: {curriculum.id})")
    print(f"[*] Target Grade: {grade.name} (Level: {grade.level})")
    print(f"[*] Target Subject: {subject.name} (ID: {subject.id})")

    with transaction.atomic():
        topic, created = Topic.objects.get_or_create(
            subject=subject,
            order=12,
            defaults={
                "name": "Computer Programming Concepts",
                "description": "Foundational principles of computer programming: core definitions, program representation in silicon, evolution of language generations (1GL to 5GL), programming paradigms (Structured, Procedural, OOP, Event-Driven), translators (Compilers, Interpreters, Assemblers), and CPU register simulation."
            }
        )

        if not created and replace:
            print(f"[*] Topic 12 already exists (ID: {topic.id}). Performing clean replacement of units and lessons...")
            topic.learning_units.all().delete()
            topic.lessons.all().delete()
            topic.name = "Computer Programming Concepts"
            topic.description = "Foundational principles of computer programming: core definitions, program representation in silicon, evolution of language generations (1GL to 5GL), programming paradigms (Structured, Procedural, OOP, Event-Driven), translators (Compilers, Interpreters, Assemblers), and CPU register simulation."
            topic.save()

        curriculum_data = build_topic12_curriculum()

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
                    "topic_order": 12,
                    "unit_order": u_order
                }
            )
            total_lessons += 1

            block_counter = 1
            for page_idx, page_blocks in enumerate(pages, start=1):
                total_pages += 1
                for comp_idx, block_def in enumerate(page_blocks, start=1):
                    b_type = block_def["type"]
                    if b_type in ["step_by_step_worked_example", "step_process"]:
                        b_type = "worked_example"
                    elif b_type in ["concept", "activity"]:
                        b_type = "concept_explanation"
                    elif b_type in ["key_takeaways", "summary"]:
                        b_type = "key_takeaway"

                    b_title = clean_text(block_def.get("title", ""))
                    b_content = clean_dict(block_def.get("content", {}))

                    if b_type == "knowledge_check" and isinstance(b_content, dict):
                        options = b_content.get("options", [])
                        ans = b_content.get("correct_answer") or b_content.get("answer")
                        idx = b_content.get("correct_option_index")
                        if idx is None and isinstance(ans, int) and 0 <= ans < len(options):
                            idx = ans
                            ans = options[idx]
                        elif idx is None and isinstance(ans, str) and ans in options:
                            idx = options.index(ans)
                        elif ans is None and isinstance(idx, int) and 0 <= idx < len(options):
                            ans = options[idx]
                        b_content["correct_answer"] = ans
                        b_content["correct_option_index"] = idx

                    block = LessonBlock.objects.create(
                        lesson=lesson,
                        block_id=f"g10_cs_t12_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={"topic_order": 12, "unit_order": u_order, "page": page_idx}
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
    print("TOPIC 12 INGESTION COMPLETE:")
    print(f"  Units Created:   {total_units}")
    print(f"  Lessons Created: {total_lessons}")
    print(f"  Pages Created:   {total_pages}")
    print(f"  Blocks Created:  {total_blocks}")
    print(f"  Assets Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_grade10_topic12(replace=True)
