"""
VLearn CBC Grade 10 Computer Science — Topic 16: Containers and Data Structures
Production Ingestion & Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Computer Science (Subject ID: 38)
Topic: Containers and Data Structures (Topic Order: 16)

Decomposed into 5 Comprehensive Learning Units & 5 Published Lessons:
  1. Introduction to Containers: Lists, Tuples, and Memory Architecture (Lessons 78–82)
  2. Associative Containers: Dictionaries, Hashing Systems, and Set Operations (Lessons 83–86)
  3. Fundamental Search and Sorting Algorithms (Lessons 87–91)
  4. Practical Classroom Labs and Software Implementations (Lesson 92)
  5. Unit Assessment, Algorithm Tracing, and Agricultural Cooperative Case Study (Lesson 93)
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
# HIGH PRECISION VECTOR SVGS FOR TOPIC 16 (DARK THEME 960x520)
# =====================================================================

SVG_CONTIGUOUS_MEMORY_ARRAY = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Hardware Memory Architecture: Contiguous Array Allocation</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Physical RAM Addressing and Constant-Time O(1) Index Calculation Formula</text>

  <!-- Top: Array Memory Slots Graphic -->
  <g transform="translate(60, 95)">
    <!-- Base Address Pointer -->
    <path d="M 50,15 L 50,55" stroke="#38bdf8" stroke-width="2.5" fill="none"/>
    <polygon points="45,55 50,65 55,55" fill="#38bdf8"/>
    <rect x="0" y="0" width="100" height="24" rx="4" fill="#0284c7"/>
    <text x="50" y="16" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Base Address</text>

    <!-- 5 Memory Slots -->
    <!-- Slot 0 -->
    <g transform="translate(0, 70)">
      <rect width="160" height="90" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
      <rect width="160" height="24" rx="6" fill="#0284c7"/>
      <text x="80" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Index [0]</text>
      <text x="80" y="55" font-size="22" font-weight="bold" fill="#38bdf8" text-anchor="middle">82</text>
      <text x="80" y="78" font-family="monospace" font-size="10.5" fill="#94a3b8" text-anchor="middle">RAM: 0x100</text>
    </g>

    <!-- Slot 1 -->
    <g transform="translate(170, 70)">
      <rect width="160" height="90" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
      <rect width="160" height="24" rx="6" fill="#0284c7"/>
      <text x="80" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Index [1]</text>
      <text x="80" y="55" font-size="22" font-weight="bold" fill="#38bdf8" text-anchor="middle">95</text>
      <text x="80" y="78" font-family="monospace" font-size="10.5" fill="#94a3b8" text-anchor="middle">RAM: 0x104</text>
    </g>

    <!-- Slot 2 -->
    <g transform="translate(340, 70)">
      <rect width="160" height="90" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
      <rect width="160" height="24" rx="6" fill="#0284c7"/>
      <text x="80" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Index [2]</text>
      <text x="80" y="55" font-size="22" font-weight="bold" fill="#38bdf8" text-anchor="middle">67</text>
      <text x="80" y="78" font-family="monospace" font-size="10.5" fill="#94a3b8" text-anchor="middle">RAM: 0x108</text>
    </g>

    <!-- Slot 3 (Highlighted Target) -->
    <g transform="translate(510, 70)">
      <rect width="160" height="90" rx="8" fill="#1e1b4b" stroke="#f59e0b" stroke-width="2.5"/>
      <rect width="160" height="24" rx="6" fill="#d97706"/>
      <text x="80" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Index [3] (Target)</text>
      <text x="80" y="55" font-size="22" font-weight="bold" fill="#fbbf24" text-anchor="middle">88</text>
      <text x="80" y="78" font-family="monospace" font-size="10.5" font-weight="bold" fill="#fde68a" text-anchor="middle">RAM: 0x10C</text>
    </g>

    <!-- Slot 4 -->
    <g transform="translate(680, 70)">
      <rect width="160" height="90" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
      <rect width="160" height="24" rx="6" fill="#0284c7"/>
      <text x="80" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Index [4]</text>
      <text x="80" y="55" font-size="22" font-weight="bold" fill="#38bdf8" text-anchor="middle">91</text>
      <text x="80" y="78" font-family="monospace" font-size="10.5" fill="#94a3b8" text-anchor="middle">RAM: 0x110</text>
    </g>
  </g>

  <!-- Bottom: Formula and Direct Calculation Cards -->
  <g transform="translate(60, 290)">
    <!-- Mathematical Formula Box -->
    <g transform="translate(0, 0)">
      <rect width="390" height="185" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
      <rect width="390" height="28" rx="8" fill="#0284c7"/>
      <text x="195" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Hardware Address Calculation Formula</text>
      
      <rect x="20" y="45" width="350" height="42" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="195" y="71" font-family="monospace" font-size="12.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Address = Base + (Index &#215; Element_Size)</text>
      
      <text x="25" y="112" font-size="10" font-weight="bold" fill="#cbd5e1">&#8226; Base Address: <tspan font-family="monospace" fill="#38bdf8">0x100</tspan> (RAM location of index 0)</text>
      <text x="25" y="132" font-size="10" font-weight="bold" fill="#cbd5e1">&#8226; Element Size: <tspan font-family="monospace" fill="#38bdf8">4 Bytes</tspan> (Standard 32-bit Integer)</text>
      <text x="25" y="152" font-size="10" font-weight="bold" fill="#cbd5e1">&#8226; Time Complexity: <tspan fill="#34d399" font-weight="bold">O(1) Constant Time</tspan> (Instant arithmetic)</text>
      <text x="25" y="172" font-size="9" fill="#94a3b8">The CPU never scans preceding elements; it jumps directly to RAM address.</text>
    </g>

    <!-- Calculation Trace Box -->
    <g transform="translate(420, 0)">
      <rect width="420" height="185" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
      <rect width="420" height="28" rx="8" fill="#d97706"/>
      <text x="210" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Step-by-Step Calculation: Accessing Index [3]</text>

      <g transform="translate(20, 42)">
        <rect width="380" height="32" rx="4" fill="#1e1b4b" stroke="#fbbf24"/>
        <text x="15" y="21" font-family="monospace" font-size="10.5" fill="#fde68a">Step 1: Offset = 3 &#215; 4 bytes = 12 bytes (0x0C)</text>
      </g>

      <g transform="translate(20, 82)">
        <rect width="380" height="32" rx="4" fill="#1e1b4b" stroke="#fbbf24"/>
        <text x="15" y="21" font-family="monospace" font-size="10.5" fill="#fde68a">Step 2: RAM Address = 0x100 + 0x0C = 0x10C</text>
      </g>

      <g transform="translate(20, 122)">
        <rect width="380" height="48" rx="4" fill="#064e3b" stroke="#34d399"/>
        <text x="15" y="20" font-size="10" font-weight="bold" fill="#a7f3d0">&#10003; Value Retrieved: 88</text>
        <text x="15" y="38" font-size="9" fill="#cbd5e1">Memory controller accesses byte 0x10C directly in single cycle.</text>
      </g>
    </g>
  </g>
</svg>
""")

SVG_LIST_VS_TUPLE_MUTABILITY = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Data Structure Mutability: Python Lists vs. Tuples</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Comparing Dynamic Mutable Buffers against Static Immutable Read-Only Records</text>

  <!-- Left: Python List (Mutable) -->
  <g transform="translate(45, 95)">
    <rect width="420" height="385" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="420" height="30" rx="8" fill="#059669"/>
    <text x="210" y="20" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1. PYTHON LIST: Mutable Sequence [ ]</text>

    <!-- Visual Container -->
    <g transform="translate(25, 45)">
      <rect width="370" height="90" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
      <text x="15" y="22" font-size="10.5" font-weight="bold" fill="#34d399">Variable: <tspan font-family="monospace" fill="#ffffff">fruits = ["mango", "banana", "passion"]</tspan></text>
      
      <!-- Modified slot -->
      <g transform="translate(15, 35)">
        <rect width="95" height="40" rx="4" fill="#0f172a" stroke="#64748b"/>
        <text x="47" y="25" font-size="10" fill="#64748b" text-anchor="middle">0: mango</text>
      </g>
      <g transform="translate(120, 35)">
        <rect width="115" height="40" rx="4" fill="#064e3b" stroke="#34d399" stroke-width="1.5"/>
        <text x="57" y="17" font-size="9" fill="#94a3b8" text-anchor="middle"><tspan text-decoration="line-through">banana</tspan></text>
        <text x="57" y="32" font-size="10" font-weight="bold" fill="#a7f3d0" text-anchor="middle">1: avocado</text>
      </g>
      <g transform="translate(245, 35)">
        <rect width="105" height="40" rx="4" fill="#0f172a" stroke="#64748b"/>
        <text x="52" y="25" font-size="10" fill="#64748b" text-anchor="middle">2: passion</text>
      </g>
    </g>

    <!-- Code Box -->
    <g transform="translate(25, 150)">
      <rect width="370" height="95" rx="6" fill="#1e1b4b" stroke="#818cf8"/>
      <text x="15" y="20" font-family="monospace" font-size="9.5" fill="#c7d2fe"># Python List In-Place Modification</text>
      <text x="15" y="38" font-family="monospace" font-size="10" fill="#38bdf8">fruits[1] = "avocado"   <tspan fill="#94a3b8"># Updates slot 1</tspan></text>
      <text x="15" y="56" font-family="monospace" font-size="10" fill="#34d399">fruits.append("pineapple")  <tspan fill="#94a3b8"># Appends to end</tspan></text>
      <text x="15" y="76" font-family="monospace" font-size="9.5" fill="#6ee7b7"># Result: ['mango', 'avocado', 'passion', 'pineapple']</text>
    </g>

    <!-- Characteristics -->
    <g transform="translate(25, 260)">
      <text x="0" y="15" font-size="10.5" font-weight="bold" fill="#34d399">&#10003; Key Operational Characteristics:</text>
      <text x="0" y="34" font-size="9" fill="#cbd5e1">&#8226; Elements can be added, updated, inserted, or removed in-place.</text>
      <text x="0" y="50" font-size="9" fill="#cbd5e1">&#8226; Declared using square brackets <tspan font-family="monospace" fill="#38bdf8">[ ]</tspan>.</text>
      <text x="0" y="66" font-size="9" fill="#cbd5e1">&#8226; Slightly higher RAM overhead to allow dynamic growth.</text>
      <text x="0" y="82" font-size="9" fill="#cbd5e1">&#8226; Ideal for shopping carts, exam marks, dynamic queues.</text>
    </g>
  </g>

  <!-- Right: Python Tuple (Immutable) -->
  <g transform="translate(495, 95)">
    <rect width="420" height="385" rx="12" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="420" height="30" rx="8" fill="#d97706"/>
    <text x="210" y="20" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2. PYTHON TUPLE: Immutable Record ( )</text>

    <!-- Visual Container with Lock -->
    <g transform="translate(25, 45)">
      <rect width="370" height="90" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="15" y="22" font-size="10.5" font-weight="bold" fill="#fbbf24">Variable: <tspan font-family="monospace" fill="#ffffff">coordinates = (-1.2921, 36.8219)</tspan></text>
      
      <!-- Locked slots -->
      <g transform="translate(30, 35)">
        <rect width="140" height="40" rx="4" fill="#451a03" stroke="#f59e0b"/>
        <text x="70" y="25" font-size="10.5" font-weight="bold" fill="#fde68a" text-anchor="middle">0: -1.2921 &#128274;</text>
      </g>
      <g transform="translate(195, 35)">
        <rect width="140" height="40" rx="4" fill="#451a03" stroke="#f59e0b"/>
        <text x="70" y="25" font-size="10.5" font-weight="bold" fill="#fde68a" text-anchor="middle">1: 36.8219 &#128274;</text>
      </g>
    </g>

    <!-- Code Box with TypeError -->
    <g transform="translate(25, 150)">
      <rect width="370" height="95" rx="6" fill="#1e1b4b" stroke="#ef4444"/>
      <text x="15" y="20" font-family="monospace" font-size="9.5" fill="#fca5a5"># Illegal Mutation Attempt</text>
      <text x="15" y="38" font-family="monospace" font-size="10" fill="#38bdf8">coordinates[0] = -1.3000</text>
      <text x="15" y="58" font-family="monospace" font-size="9" font-weight="bold" fill="#ef4444">&#9888; TypeError: 'tuple' object does not support</text>
      <text x="15" y="74" font-family="monospace" font-size="9" font-weight="bold" fill="#ef4444">  item assignment</text>
    </g>

    <!-- Characteristics -->
    <g transform="translate(25, 260)">
      <text x="0" y="15" font-size="10.5" font-weight="bold" fill="#fbbf24">&#128274; Key Operational Characteristics:</text>
      <text x="0" y="34" font-size="9" fill="#cbd5e1">&#8226; Elements are write-protected once allocated in RAM.</text>
      <text x="0" y="50" font-size="9" fill="#cbd5e1">&#8226; Declared using round parentheses <tspan font-family="monospace" fill="#fbbf24">( )</tspan>.</text>
      <text x="0" y="66" font-size="9" fill="#cbd5e1">&#8226; Highly optimized memory footprint; faster read speeds.</text>
      <text x="0" y="82" font-size="9" fill="#cbd5e1">&#8226; Ideal for GPS coordinates, RGB colors, database primary keys.</text>
    </g>
  </g>
</svg>
""")

SVG_LIST_VS_DICTIONARY_LOOKUP_HASHING = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Search Efficiency: Sequential List Search vs. Hash Map (Dictionary)</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Comparing O(N) Linear Traversals against O(1) Key-Value Hashing Lookups</text>

  <!-- Left: Linear Search in List -->
  <g transform="translate(45, 95)">
    <rect width="420" height="385" rx="12" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="420" height="30" rx="8" fill="#dc2626"/>
    <text x="210" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Sequential Search in List — O(N) Time</text>

    <!-- Stepping Array -->
    <g transform="translate(25, 45)">
      <!-- Step 0 -->
      <rect x="0" y="0" width="370" height="32" rx="4" fill="#1e293b" stroke="#ef4444"/>
      <text x="15" y="20" font-family="monospace" font-size="10" fill="#94a3b8">Index 0: "Kofi" != "Jane" (Mismatch, step next)</text>
      <!-- Step 1 -->
      <rect x="0" y="38" width="370" height="32" rx="4" fill="#1e293b" stroke="#ef4444"/>
      <text x="15" y="20" font-family="monospace" font-size="10" fill="#94a3b8">Index 1: "Mwangi" != "Jane" (Mismatch, step next)</text>
      <!-- Step 2 -->
      <rect x="0" y="76" width="370" height="32" rx="4" fill="#1e293b" stroke="#ef4444"/>
      <text x="15" y="20" font-family="monospace" font-size="10" fill="#94a3b8">Index 2: "Abdi" != "Jane" (Mismatch, step next)</text>
      <!-- Step 3 -->
      <rect x="0" y="114" width="370" height="32" rx="4" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
      <text x="15" y="20" font-family="monospace" font-size="10" font-weight="bold" fill="#a7f3d0">Index 3: "Jane" == "Jane" &#10003; (Found at step 4!)</text>
    </g>

    <!-- Stepping Arrows -->
    <g transform="translate(5, 55)">
      <line x1="10" y1="5" x2="10" y2="125" stroke="#ef4444" stroke-width="2" stroke-dasharray="3"/>
      <polygon points="5,125 10,135 15,125" fill="#ef4444"/>
    </g>

    <!-- Technical Analysis -->
    <g transform="translate(25, 210)">
      <rect width="370" height="70" rx="6" fill="#1e1b4b" stroke="#ef4444"/>
      <text x="15" y="22" font-size="10" font-weight="bold" fill="#f87171">&#9888; Performance Scaling Penalty:</text>
      <text x="15" y="42" font-size="9" fill="#cbd5e1">For 10,000 items, worst case requires 10,000 checks.</text>
      <text x="15" y="58" font-size="9" fill="#cbd5e1">Time grows proportionally with dataset size: <tspan font-weight="bold" fill="#fca5a5">O(N)</tspan>.</text>
    </g>

    <g transform="translate(25, 295)">
      <text x="0" y="15" font-size="10" font-weight="bold" fill="#f87171">&#8226; Unordered elements require sequential sweep.</text>
      <text x="0" y="32" font-size="9" fill="#cbd5e1">&#8226; High CPU overhead on large database lookups.</text>
      <text x="0" y="49" font-size="9" fill="#cbd5e1">&#8226; Inefficient for key-to-record relational retrieval.</text>
    </g>
  </g>

  <!-- Right: Hash Map Lookup in Dictionary -->
  <g transform="translate(495, 95)">
    <rect width="420" height="385" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="420" height="30" rx="8" fill="#0284c7"/>
    <text x="210" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Instant Hash Map Lookup — O(1) Time</text>

    <!-- Key -> Hash Function -> Memory Bucket -->
    <g transform="translate(20, 45)">
      <!-- Key Box -->
      <rect x="0" y="20" width="90" height="45" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="45" y="40" font-size="9" fill="#94a3b8" text-anchor="middle">Search Key</text>
      <text x="45" y="55" font-family="monospace" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">"Jane"</text>

      <!-- Arrow to Hash Function -->
      <line x1="95" y1="42" x2="125" y2="42" stroke="#38bdf8" stroke-width="2"/>
      <polygon points="125,38 133,42 125,46" fill="#38bdf8"/>

      <!-- Hash Function Engine -->
      <rect x="135" y="10" width="105" height="65" rx="8" fill="#1e1b4b" stroke="#818cf8" stroke-width="1.5"/>
      <text x="187" y="32" font-size="9.5" font-weight="bold" fill="#c7d2fe" text-anchor="middle">Hash Function</text>
      <text x="187" y="48" font-family="monospace" font-size="8.5" fill="#a5b4fc" text-anchor="middle">hash("Jane")</text>
      <text x="187" y="64" font-size="8.5" fill="#34d399" text-anchor="middle">&#8594; Bucket #7</text>

      <!-- Arrow to Bucket -->
      <line x1="245" y1="42" x2="275" y2="42" stroke="#34d399" stroke-width="2"/>
      <polygon points="275,38 283,42 275,46" fill="#34d399"/>

      <!-- Target Value Bucket -->
      <rect x="285" y="10" width="95" height="65" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="1.5"/>
      <text x="332" y="28" font-size="9" fill="#a7f3d0" text-anchor="middle">Direct Value</text>
      <text x="332" y="44" font-size="9.5" font-weight="bold" fill="#ffffff" text-anchor="middle">GPA: 3.8</text>
      <text x="332" y="60" font-family="monospace" font-size="8" fill="#a7f3d0" text-anchor="middle">Admin: 4512</text>
    </g>

    <!-- Python Dictionary Code -->
    <g transform="translate(20, 140)">
      <rect width="380" height="70" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="15" y="20" font-family="monospace" font-size="9.5" fill="#7dd3fc">student = {"Jane": {"gpa": 3.8, "id": 4512}}</text>
      <text x="15" y="38" font-family="monospace" font-size="9.5" fill="#34d399">print(student["Jane"])  # Instant O(1) access</text>
      <text x="15" y="56" font-size="9" fill="#94a3b8"># No looping; hash computes bucket RAM address directly</text>
    </g>

    <!-- Summary Points -->
    <g transform="translate(20, 225)">
      <rect width="380" height="60" rx="6" fill="#064e3b" stroke="#34d399"/>
      <text x="15" y="22" font-size="10" font-weight="bold" fill="#34d399">&#10003; Constant-Time Performance Advantage:</text>
      <text x="15" y="42" font-size="9" fill="#cbd5e1">Whether the dictionary holds 10 or 10,000,000 entries,</text>
      <text x="15" y="54" font-size="9" fill="#a7f3d0">retrieval executes in 1 single hash calculation step: <tspan font-weight="bold">O(1)</tspan>.</text>
    </g>

    <g transform="translate(20, 300)">
      <text x="0" y="15" font-size="10" font-weight="bold" fill="#38bdf8">&#8226; Keys must be immutable and unique (strings, ints, tuples).</text>
      <text x="0" y="32" font-size="9" fill="#cbd5e1">&#8226; Values can be any data type (lists, dicts, objects).</text>
      <text x="0" y="49" font-size="9" fill="#cbd5e1">&#8226; Built-in mathematical hashing replaces linear iterations.</text>
    </g>
  </g>
</svg>
""")

SVG_SET_THEORY_VENN_OPERATIONS = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Python Set Mechanics &amp; Mathematical Venn Operations</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Automatic Deduplication, Union, Intersection, and Difference Operations</text>

  <!-- Left: Venn Diagram Graphic -->
  <g transform="translate(45, 95)">
    <rect width="450" height="385" rx="12" fill="#0f172a" stroke="#818cf8" stroke-width="1.5"/>
    <rect width="450" height="30" rx="8" fill="#4f46e5"/>
    <text x="225" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Club Membership Venn Diagram</text>

    <!-- Venn Circles -->
    <g transform="translate(30, 45)">
      <!-- Circle A (Science Club) -->
      <circle cx="130" cy="110" r="95" fill="#0284c7" fill-opacity="0.35" stroke="#38bdf8" stroke-width="2.5"/>
      <!-- Circle B (Math Club) -->
      <circle cx="260" cy="110" r="95" fill="#d97706" fill-opacity="0.35" stroke="#fbbf24" stroke-width="2.5"/>

      <!-- Labels & Members -->
      <!-- Left (Science only) -->
      <text x="75" y="55" font-size="11" font-weight="bold" fill="#38bdf8">Science Club</text>
      <text x="75" y="105" font-family="monospace" font-size="11" fill="#ffffff">"Amina"</text>
      <text x="75" y="130" font-family="monospace" font-size="11" fill="#ffffff">"Kofi"</text>

      <!-- Center (Intersection - Mwangi) -->
      <rect x="155" y="90" width="80" height="40" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="1.5"/>
      <text x="195" y="108" font-size="9" font-weight="bold" fill="#a7f3d0" text-anchor="middle">INTERSECTION</text>
      <text x="195" y="123" font-family="monospace" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">"Mwangi"</text>

      <!-- Right (Math only) -->
      <text x="315" y="55" font-size="11" font-weight="bold" fill="#fbbf24">Math Club</text>
      <text x="315" y="105" font-family="monospace" font-size="11" fill="#ffffff">"Abdi"</text>
      <text x="315" y="130" font-family="monospace" font-size="11" fill="#ffffff">"Chipo"</text>
    </g>

    <!-- Deduplication Banner -->
    <g transform="translate(25, 275)">
      <rect width="400" height="90" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="15" y="20" font-size="10.5" font-weight="bold" fill="#38bdf8">&#128260; Automatic Deduplication Mechanism:</text>
      <text x="15" y="38" font-family="monospace" font-size="9.5" fill="#fca5a5">input_list = ["Kofi", "Amina", "Kofi", "Abdi", "Amina"]</text>
      <text x="15" y="56" font-family="monospace" font-size="9.5" fill="#34d399">unique_set = set(input_list)</text>
      <text x="15" y="74" font-family="monospace" font-size="9.5" fill="#6ee7b7"># Output: {'Kofi', 'Amina', 'Abdi'} (Duplicates pruned)</text>
    </g>
  </g>

  <!-- Right: 3 Core Set Operations & Python Syntax -->
  <g transform="translate(525, 95)">
    <rect width="390" height="385" rx="12" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
    <rect width="390" height="30" rx="8" fill="#334155"/>
    <text x="195" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Mathematical Set Operations in Python</text>

    <!-- 1. Intersection -->
    <g transform="translate(15, 42)">
      <rect width="360" height="95" rx="6" fill="#1e1b4b" stroke="#34d399" stroke-width="1.5"/>
      <text x="15" y="20" font-size="10.5" font-weight="bold" fill="#34d399">1. Intersection ( &amp; / .intersection() )</text>
      <text x="15" y="36" font-size="9" fill="#cbd5e1">Finds elements common to BOTH sets.</text>
      <rect x="15" y="44" width="330" height="42" rx="4" fill="#0f172a"/>
      <text x="25" y="60" font-family="monospace" font-size="9.5" fill="#38bdf8">both = science_club.intersection(math_club)</text>
      <text x="25" y="76" font-family="monospace" font-size="9.5" fill="#a7f3d0"># Result: {'Mwangi'}</text>
    </g>

    <!-- 2. Union -->
    <g transform="translate(15, 150)">
      <rect width="360" height="100" rx="6" fill="#1e1b4b" stroke="#0ea5e9" stroke-width="1.5"/>
      <text x="15" y="20" font-size="10.5" font-weight="bold" fill="#38bdf8">2. Union ( | / .union() )</text>
      <text x="15" y="36" font-size="9" fill="#cbd5e1">Combines elements from EITHER set without duplicates.</text>
      <rect x="15" y="44" width="330" height="46" rx="4" fill="#0f172a"/>
      <text x="25" y="60" font-family="monospace" font-size="9.5" fill="#38bdf8">all_members = science_club.union(math_club)</text>
      <text x="25" y="78" font-family="monospace" font-size="8.5" fill="#7dd3fc"># Result: {'Amina', 'Kofi', 'Mwangi', 'Abdi', 'Chipo'}</text>
    </g>

    <!-- 3. Difference -->
    <g transform="translate(15, 262)">
      <rect width="360" height="105" rx="6" fill="#1e1b4b" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="15" y="20" font-size="10.5" font-weight="bold" fill="#fbbf24">3. Difference ( - / .difference() )</text>
      <text x="15" y="36" font-size="9" fill="#cbd5e1">Finds elements in First set but NOT in Second set.</text>
      <rect x="15" y="44" width="330" height="50" rx="4" fill="#0f172a"/>
      <text x="25" y="60" font-family="monospace" font-size="9.5" fill="#38bdf8">science_only = science_club - math_club</text>
      <text x="25" y="78" font-family="monospace" font-size="9.5" fill="#fde68a"># Result: {'Amina', 'Kofi'}</text>
    </g>
  </g>
</svg>
""")

SVG_BUBBLE_SORT_PASSES_TRACE = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Bubble Sort Execution: Multi-Pass Adjacent Swap Trace</text>
  <text x="480" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Step-by-step state visualization sorting list [14, 5, 8, 2] in ascending order</text>

  <!-- Left: Pass 1 (3 Swaps) -->
  <g transform="translate(45, 90)">
    <rect width="270" height="390" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#0284c7"/>
    <text x="135" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Pass 1 (i = 0): Bubbling Largest (14)</text>

    <!-- Initial state -->
    <g transform="translate(15, 38)">
      <text x="0" y="14" font-size="9" fill="#94a3b8">Initial State:</text>
      <rect x="0" y="20" width="55" height="30" rx="4" fill="#1e293b" stroke="#38bdf8"/>
      <text x="27" y="40" font-family="monospace" font-size="12" fill="#ffffff" text-anchor="middle">14</text>
      <rect x="60" y="20" width="55" height="30" rx="4" fill="#1e293b" stroke="#38bdf8"/>
      <text x="87" y="40" font-family="monospace" font-size="12" fill="#ffffff" text-anchor="middle">5</text>
      <rect x="120" y="20" width="55" height="30" rx="4" fill="#1e293b" stroke="#38bdf8"/>
      <text x="147" y="40" font-family="monospace" font-size="12" fill="#ffffff" text-anchor="middle">8</text>
      <rect x="180" y="20" width="55" height="30" rx="4" fill="#1e293b" stroke="#38bdf8"/>
      <text x="207" y="40" font-family="monospace" font-size="12" fill="#ffffff" text-anchor="middle">2</text>
    </g>

    <!-- Step 1: Swap 14 and 5 -->
    <g transform="translate(15, 100)">
      <text x="0" y="14" font-size="9" font-weight="bold" fill="#f87171">Step 1: Compare 14 &gt; 5 &#8594; SWAP</text>
      <rect x="0" y="20" width="55" height="30" rx="4" fill="#064e3b" stroke="#34d399"/>
      <text x="27" y="40" font-family="monospace" font-size="12" fill="#34d399" text-anchor="middle">5</text>
      <rect x="60" y="20" width="55" height="30" rx="4" fill="#451a03" stroke="#f59e0b"/>
      <text x="87" y="40" font-family="monospace" font-size="12" fill="#fbbf24" text-anchor="middle">14</text>
      <rect x="120" y="20" width="55" height="30" rx="4" fill="#1e293b"/>
      <text x="147" y="40" font-family="monospace" font-size="12" fill="#94a3b8" text-anchor="middle">8</text>
      <rect x="180" y="20" width="55" height="30" rx="4" fill="#1e293b"/>
      <text x="207" y="40" font-family="monospace" font-size="12" fill="#94a3b8" text-anchor="middle">2</text>
    </g>

    <!-- Step 2: Swap 14 and 8 -->
    <g transform="translate(15, 170)">
      <text x="0" y="14" font-size="9" font-weight="bold" fill="#f87171">Step 2: Compare 14 &gt; 8 &#8594; SWAP</text>
      <rect x="0" y="20" width="55" height="30" rx="4" fill="#1e293b"/>
      <text x="27" y="40" font-family="monospace" font-size="12" fill="#cbd5e1" text-anchor="middle">5</text>
      <rect x="60" y="20" width="55" height="30" rx="4" fill="#064e3b" stroke="#34d399"/>
      <text x="87" y="40" font-family="monospace" font-size="12" fill="#34d399" text-anchor="middle">8</text>
      <rect x="120" y="20" width="55" height="30" rx="4" fill="#451a03" stroke="#f59e0b"/>
      <text x="147" y="40" font-family="monospace" font-size="12" fill="#fbbf24" text-anchor="middle">14</text>
      <rect x="180" y="20" width="55" height="30" rx="4" fill="#1e293b"/>
      <text x="207" y="40" font-family="monospace" font-size="12" fill="#94a3b8" text-anchor="middle">2</text>
    </g>

    <!-- Step 3: Swap 14 and 2 -> 14 Locked -->
    <g transform="translate(15, 240)">
      <text x="0" y="14" font-size="9" font-weight="bold" fill="#f87171">Step 3: Compare 14 &gt; 2 &#8594; SWAP</text>
      <rect x="0" y="20" width="55" height="30" rx="4" fill="#1e293b"/>
      <text x="27" y="40" font-family="monospace" font-size="12" fill="#cbd5e1" text-anchor="middle">5</text>
      <rect x="60" y="20" width="55" height="30" rx="4" fill="#1e293b"/>
      <text x="87" y="40" font-family="monospace" font-size="12" fill="#cbd5e1" text-anchor="middle">8</text>
      <rect x="120" y="20" width="55" height="30" rx="4" fill="#064e3b" stroke="#34d399"/>
      <text x="147" y="40" font-family="monospace" font-size="12" fill="#34d399" text-anchor="middle">2</text>
      <rect x="180" y="20" width="55" height="30" rx="4" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
      <text x="207" y="40" font-family="monospace" font-size="12" font-weight="bold" fill="#a7f3d0" text-anchor="middle">14 &#128274;</text>
    </g>

    <rect x="15" y="325" width="240" height="48" rx="6" fill="#1e293b"/>
    <text x="135" y="345" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Pass 1 Outcome:</text>
    <text x="135" y="362" font-size="8.5" fill="#cbd5e1" text-anchor="middle">14 reaches final index [3] (Locked)</text>
  </g>

  <!-- Center: Pass 2 (1 Swap) -->
  <g transform="translate(345, 90)">
    <rect width="270" height="390" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#d97706"/>
    <text x="135" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Pass 2 (i = 1): Bubbling 8</text>

    <!-- State at start of Pass 2 -->
    <g transform="translate(15, 38)">
      <text x="0" y="14" font-size="9" fill="#94a3b8">Start of Pass 2:</text>
      <rect x="0" y="20" width="55" height="30" rx="4" fill="#1e293b"/>
      <text x="27" y="40" font-family="monospace" font-size="12" fill="#cbd5e1" text-anchor="middle">5</text>
      <rect x="60" y="20" width="55" height="30" rx="4" fill="#1e293b"/>
      <text x="87" y="40" font-family="monospace" font-size="12" fill="#cbd5e1" text-anchor="middle">8</text>
      <rect x="120" y="20" width="55" height="30" rx="4" fill="#1e293b"/>
      <text x="147" y="40" font-family="monospace" font-size="12" fill="#cbd5e1" text-anchor="middle">2</text>
      <rect x="180" y="20" width="55" height="30" rx="4" fill="#064e3b" stroke="#34d399"/>
      <text x="207" y="40" font-family="monospace" font-size="12" fill="#a7f3d0" text-anchor="middle">14 &#128274;</text>
    </g>

    <!-- Step 4: Compare 5 and 8 -> No Swap -->
    <g transform="translate(15, 100)">
      <text x="0" y="14" font-size="9" font-weight="bold" fill="#38bdf8">Step 4: Compare 5 &lt;= 8 &#8594; NO SWAP</text>
      <rect x="0" y="20" width="55" height="30" rx="4" fill="#1e293b" stroke="#38bdf8"/>
      <text x="27" y="40" font-family="monospace" font-size="12" fill="#38bdf8" text-anchor="middle">5</text>
      <rect x="60" y="20" width="55" height="30" rx="4" fill="#1e293b" stroke="#38bdf8"/>
      <text x="87" y="40" font-family="monospace" font-size="12" fill="#38bdf8" text-anchor="middle">8</text>
      <rect x="120" y="20" width="55" height="30" rx="4" fill="#1e293b"/>
      <text x="147" y="40" font-family="monospace" font-size="12" fill="#94a3b8" text-anchor="middle">2</text>
      <rect x="180" y="20" width="55" height="30" rx="4" fill="#064e3b"/>
      <text x="207" y="40" font-family="monospace" font-size="12" fill="#a7f3d0" text-anchor="middle">14 &#128274;</text>
    </g>

    <!-- Step 5: Compare 8 and 2 -> Swap -->
    <g transform="translate(15, 170)">
      <text x="0" y="14" font-size="9" font-weight="bold" fill="#f87171">Step 5: Compare 8 &gt; 2 &#8594; SWAP</text>
      <rect x="0" y="20" width="55" height="30" rx="4" fill="#1e293b"/>
      <text x="27" y="40" font-family="monospace" font-size="12" fill="#cbd5e1" text-anchor="middle">5</text>
      <rect x="60" y="20" width="55" height="30" rx="4" fill="#064e3b" stroke="#34d399"/>
      <text x="87" y="40" font-family="monospace" font-size="12" fill="#34d399" text-anchor="middle">2</text>
      <rect x="120" y="20" width="55" height="30" rx="4" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
      <text x="147" y="40" font-family="monospace" font-size="12" font-weight="bold" fill="#a7f3d0" text-anchor="middle">8 &#128274;</text>
      <rect x="180" y="20" width="55" height="30" rx="4" fill="#064e3b"/>
      <text x="207" y="40" font-family="monospace" font-size="12" fill="#a7f3d0" text-anchor="middle">14 &#128274;</text>
    </g>

    <rect x="15" y="325" width="240" height="48" rx="6" fill="#1e293b"/>
    <text x="135" y="345" font-size="9.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">Pass 2 Outcome:</text>
    <text x="135" y="362" font-size="8.5" fill="#cbd5e1" text-anchor="middle">8 locked in place at index [2]</text>
  </g>

  <!-- Right: Pass 3 (1 Swap -> Sorted) -->
  <g transform="translate(645, 90)">
    <rect width="270" height="390" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#059669"/>
    <text x="135" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Pass 3 (i = 2): Final Pass</text>

    <!-- Start of Pass 3 -->
    <g transform="translate(15, 38)">
      <text x="0" y="14" font-size="9" fill="#94a3b8">Start of Pass 3:</text>
      <rect x="0" y="20" width="55" height="30" rx="4" fill="#1e293b"/>
      <text x="27" y="40" font-family="monospace" font-size="12" fill="#cbd5e1" text-anchor="middle">5</text>
      <rect x="60" y="20" width="55" height="30" rx="4" fill="#1e293b"/>
      <text x="87" y="40" font-family="monospace" font-size="12" fill="#cbd5e1" text-anchor="middle">2</text>
      <rect x="120" y="20" width="55" height="30" rx="4" fill="#064e3b"/>
      <text x="147" y="40" font-family="monospace" font-size="12" fill="#a7f3d0" text-anchor="middle">8 &#128274;</text>
      <rect x="180" y="20" width="55" height="30" rx="4" fill="#064e3b"/>
      <text x="207" y="40" font-family="monospace" font-size="12" fill="#a7f3d0" text-anchor="middle">14 &#128274;</text>
    </g>

    <!-- Step 6: Compare 5 and 2 -> Swap -->
    <g transform="translate(15, 100)">
      <text x="0" y="14" font-size="9" font-weight="bold" fill="#f87171">Step 6: Compare 5 &gt; 2 &#8594; SWAP</text>
      <rect x="0" y="20" width="55" height="30" rx="4" fill="#064e3b" stroke="#34d399"/>
      <text x="27" y="40" font-family="monospace" font-size="12" fill="#34d399" text-anchor="middle">2</text>
      <rect x="60" y="20" width="55" height="30" rx="4" fill="#064e3b" stroke="#34d399"/>
      <text x="87" y="40" font-family="monospace" font-size="12" fill="#34d399" text-anchor="middle">5</text>
      <rect x="120" y="20" width="55" height="30" rx="4" fill="#064e3b"/>
      <text x="147" y="40" font-family="monospace" font-size="12" fill="#a7f3d0" text-anchor="middle">8 &#128274;</text>
      <rect x="180" y="20" width="55" height="30" rx="4" fill="#064e3b"/>
      <text x="207" y="40" font-family="monospace" font-size="12" fill="#a7f3d0" text-anchor="middle">14 &#128274;</text>
    </g>

    <!-- Final Sorted State -->
    <g transform="translate(15, 170)">
      <rect width="240" height="85" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
      <text x="120" y="24" font-size="11" font-weight="bold" fill="#a7f3d0" text-anchor="middle">&#10003; FULLY SORTED ARRAY</text>
      <text x="120" y="52" font-family="monospace" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">[2, 5, 8, 14]</text>
      <text x="120" y="72" font-size="9" fill="#a7f3d0" text-anchor="middle">N - 1 = 3 Passes Completed</text>
    </g>

    <rect x="15" y="325" width="240" height="48" rx="6" fill="#1e293b"/>
    <text x="135" y="345" font-size="9.5" font-weight="bold" fill="#34d399" text-anchor="middle">Algorithm Termination:</text>
    <text x="135" y="362" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Array ascending order guaranteed</text>
  </g>
</svg>
""")

SVG_COOPERATIVE_DATA_SYSTEM_ARCHITECTURE = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Applied Case Study: Rift Valley Farmer Cooperative Data System</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Multi-Tier Data Architecture: Key-Value Farmer Profiles, Sequential Yield Search, and Bubble Sort Performance Analytics</text>

  <!-- Left: Member Profile Dictionary (O(1) Map) -->
  <g transform="translate(45, 95)">
    <rect width="270" height="385" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#0284c7"/>
    <text x="135" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Member Registry (Dictionary)</text>

    <g transform="translate(15, 40)">
      <rect width="240" height="65" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#38bdf8">Dictionary Key-Value Map:</text>
      <text x="15" y="38" font-family="monospace" font-size="9" fill="#ffffff">Key: 101 &#8594; "Cheruiyot"</text>
      <text x="15" y="54" font-family="monospace" font-size="9" fill="#ffffff">Key: 102 &#8594; "Chepngetich"</text>
    </g>

    <g transform="translate(15, 115)">
      <rect width="240" height="120" rx="6" fill="#1e1b4b" stroke="#818cf8"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#c7d2fe">&#128187; Monthly Yield List:</text>
      <text x="15" y="40" font-family="monospace" font-size="9" fill="#38bdf8">weights = [120.5, 95.0,</text>
      <text x="15" y="56" font-family="monospace" font-size="9" fill="#38bdf8">           110.0, 85.5]</text>
      <text x="15" y="80" font-size="8.5" fill="#cbd5e1">&#8226; Type: Mutable float list</text>
      <text x="15" y="96" font-size="8.5" fill="#cbd5e1">&#8226; Size: N = 4 monthly entries</text>
      <text x="15" y="112" font-size="8.5" fill="#34d399">&#10003; Average: 102.75 kg</text>
    </g>

    <g transform="translate(15, 245)">
      <rect width="240" height="120" rx="6" fill="#0f172a" stroke="#64748b"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#cbd5e1">&#128274; Architectural Design:</text>
      <text x="15" y="38" font-size="8.5" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#38bdf8">Dictionary</tspan>: Instant lookup by Member ID.</text>
      <text x="15" y="66" font-size="8.5" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#34d399">List</tspan>: Ordered numerical data for sorting &amp; math averages.</text>
      <text x="15" y="94" font-size="8.5" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#fbbf24">Tuple</tspan>: Locks GPS coordinates of farm intake point.</text>
    </g>
  </g>

  <!-- Center: Sequential Search Engine -->
  <g transform="translate(345, 95)">
    <rect width="270" height="385" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#d97706"/>
    <text x="135" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Sequential Search Engine</text>

    <g transform="translate(15, 40)">
      <rect width="240" height="85" rx="6" fill="#1e1b4b" stroke="#f59e0b"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#fbbf24">&#128269; Target Verification:</text>
      <text x="15" y="38" font-family="monospace" font-size="9" fill="#ffffff">search_key = 110.0</text>
      <text x="15" y="56" font-size="8.5" fill="#cbd5e1">Checks index 0: 120.5 (No)</text>
      <text x="15" y="72" font-size="8.5" fill="#cbd5e1">Checks index 1: 95.0 (No)</text>
    </g>

    <g transform="translate(15, 135)">
      <rect width="240" height="75" rx="6" fill="#064e3b" stroke="#34d399"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#a7f3d0">&#10003; Match Found:</text>
      <text x="15" y="38" font-family="monospace" font-size="9" fill="#ffffff">weights[2] == 110.0</text>
      <text x="15" y="56" font-size="8.5" fill="#a7f3d0">Returns index position: 2</text>
      <text x="15" y="70" font-size="8.5" fill="#cbd5e1">(3 comparisons executed)</text>
    </g>

    <g transform="translate(15, 220)">
      <rect width="240" height="145" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#38bdf8">&#128221; Search Algorithm Specs:</text>
      <text x="15" y="38" font-size="8.5" fill="#cbd5e1">&#8226; Scans elements from index 0 to N-1.</text>
      <text x="15" y="58" font-size="8.5" fill="#cbd5e1">&#8226; Terminate early upon match.</text>
      <text x="15" y="78" font-size="8.5" fill="#cbd5e1">&#8226; Returns -1 if item is not found.</text>
      <text x="15" y="98" font-size="8.5" fill="#fca5a5">&#8226; Time: O(N) linear scan.</text>
      <text x="15" y="118" font-size="8.5" fill="#a7f3d0">&#8226; Does NOT require presorted data.</text>
    </g>
  </g>

  <!-- Right: Bubble Sort Performance Engine -->
  <g transform="translate(645, 95)">
    <rect width="270" height="385" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#059669"/>
    <text x="135" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Bubble Sort Analytics Engine</text>

    <g transform="translate(15, 40)">
      <rect width="240" height="85" rx="6" fill="#1e1b4b" stroke="#10b981"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#34d399">&#128202; Ascending Productivity:</text>
      <text x="15" y="38" font-size="8.5" fill="#cbd5e1">Input: [120.5, 95.0, 110.0, 85.5]</text>
      <text x="15" y="56" font-family="monospace" font-size="9" fill="#6ee7b7">Output: [85.5, 95.0,</text>
      <text x="15" y="72" font-family="monospace" font-size="9" fill="#6ee7b7">         110.0, 120.5]</text>
    </g>

    <g transform="translate(15, 135)">
      <rect width="240" height="95" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#38bdf8">&#128203; Sorting Execution Specs:</text>
      <text x="15" y="38" font-size="8.5" fill="#cbd5e1">&#8226; Total Passes: N - 1 = 3</text>
      <text x="15" y="54" font-size="8.5" fill="#cbd5e1">&#8226; Pass 1 Swaps: 3 (120.5 to end)</text>
      <text x="15" y="70" font-size="8.5" fill="#cbd5e1">&#8226; Pass 2 Swaps: 2 (110.0 to index 2)</text>
      <text x="15" y="86" font-size="8.5" fill="#cbd5e1">&#8226; Pass 3 Swaps: 1 (95.0 / 85.5)</text>
    </g>

    <g transform="translate(15, 240)">
      <rect width="240" height="125" rx="6" fill="#064e3b" stroke="#34d399"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#a7f3d0">&#128079; Decision Output:</text>
      <text x="15" y="38" font-size="8.5" fill="#cbd5e1">Lowest Month: <tspan font-weight="bold" fill="#ffffff">85.5 kg</tspan></text>
      <text x="15" y="54" font-size="8.5" fill="#cbd5e1">Highest Month: <tspan font-weight="bold" fill="#ffffff">120.5 kg</tspan></text>
      <text x="15" y="70" font-size="8.5" fill="#cbd5e1">Growth Trend: Ascending Rank</text>
      <text x="15" y="88" font-size="8" fill="#a7f3d0">&#10003; Automated co-op reporting ready</text>
    </g>
  </g>
</svg>
""")

# =====================================================================
# CURRICULUM DATA DECONSTRUCTION FOR TOPIC 16
# =====================================================================

def build_topic16_curriculum():
    return [
        # =====================================================================
        # LEARNING UNIT 1: Introduction to Containers: Lists, Tuples, and Memory Architecture
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Introduction to Containers: Lists, Tuples, and Memory Architecture",
            "unit_description": "Conceptual introduction to data structure containers, the pigeonhole mailroom analogy, core definitions of arrays, indices, mutability vs immutability, hardware memory contiguous allocation, and Python list and tuple operations.",
            "lesson_title": "Lessons 78 to 82: Introduction to Containers — Lists, Tuples, and Memory Architecture",
            "pages": [
                # Page 1: Introduction & The Pigeonhole Organizer Analogy
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Understand Container Data Structures and Memory Indexing",
                        "content": {
                            "goal": "Explain how container data structures organize multi-element collections in memory, evaluate the architectural trade-offs between mutable lists and immutable tuples, and calculate contiguous hardware memory addresses using base-offset arithmetic."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 'Pigeonhole Organizer' Analogy & Core Definitions",
                        "content": {
                            "text": "Imagine a mailroom at a large school. If you only had one teacher, you could put their mail on a single desk. But when you have 15 teachers, placing 15 separate desks in the mailroom is chaotic, inefficient, and occupies excessive space.\n\nInstead, you build a wooden cabinet with a grid of 15 numbered compartments—**pigeonholes**:\n- The cabinet represents a single structural unit: **The List (or Array)**.\n- Each compartment has a fixed, sequential address: **The Index** (starting from 0).\n- The letters resting inside each compartment are: **The Elements**.\n\nInstead of managing 15 separate variable names (`teacher1_mail`, `teacher2_mail`, ...), you manage one unified cabinet variable and use index numbers to find or change the contents of any specific compartment.\n\n### **Core Data Structure Definitions**\n1. **Data Structure**: A specialized format designed to organize, store, manage, and manipulate collections of related data elements in computer memory so they can be accessed and modified efficiently.\n2. **List (Array)**: An ordered, index-based, and mutable collection of data elements.\n3. **Index**: A numerical integer value representing the exact sequential position of an element within a sequence container (typically 0-indexed in modern languages).\n4. **Mutable**: The property of a data structure that allows its elements to be modified, updated, inserted, or deleted after creation without creating a new object in memory.\n5. **Immutable**: The property of a data structure that prevents any modifications to its elements, size, or order once it has been written to memory."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Array Memory and Indexing Representation",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Array_indexing.svg/1024px-Array_indexing.svg.png",
                            "caption": "Diagram demonstrating zero-indexed array elements mapped to continuous physical memory indices.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    }
                ],

                # Page 2: Hardware Contiguous Memory Allocation
                [
                    {
                        "type": "concept_explanation",
                        "title": "Under the Hood: Contiguous Memory Allocation and Addressing",
                        "content": {
                            "text": "In computer hardware architecture, a standard array is allocated as a **contiguous block of memory** in physical RAM.\n\nWhen a program creates an array of 5 integers, the operating system's memory manager reserves 5 adjacent physical slots in RAM.\n\nBecause the memory blocks are strictly side-by-side, the CPU does not need to traverse through previous elements to find a specific item. Instead, the CPU calculates the exact physical RAM address of any element instantly using the **Hardware Address Calculation Formula**:\n\n$$\\text{Address} = \\text{Base Address} + (\\text{Index} \\times \\text{Size of Element})$$\n\n### **Formula Variable Breakdown**\n- **Base Address**: The starting hexadecimal memory address of index `0` in RAM (e.g., `0x100`).\n- **Index**: The zero-based numerical target position (e.g., `3`).\n- **Size of Element**: The number of bytes required by the data type (e.g., standard 32-bit integers occupy `4 bytes`).\n\n### **Constant-Time O(1) Access Advantage**\nBecause the address calculation requires only a single multiplication and addition operation at the hardware register level, accessing an element by index executes in **constant time $O(1)$**, regardless of whether the array contains 5 elements or 5,000,000 elements!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Hardware Memory Architecture: Contiguous Array Allocation",
                        "content": {
                            "svg_content": SVG_CONTIGUOUS_MEMORY_ARRAY,
                            "caption": "Visual representation of contiguous RAM allocation showing base address pointer, 4-byte offsets, and the instantaneous calculation of index [3] at address 0x10C."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Arrays and Contiguous Memory Allocation in Computer Science",
                        "content": {
                            "youtube_id": "wjDY5GYp71A",
                            "description": "Educational lecture exploring contiguous memory layout, pointer arithmetic, array indexing, and memory allocation mechanics."
                        }
                    }
                ],

                # Page 3: Python Operations: Lists vs Tuples & Mutability Worked Example
                [
                    {
                        "type": "concept_explanation",
                        "title": "Python Lists (Mutable) vs. Tuples (Immutable)",
                        "content": {
                            "text": "Python provides two primary sequence containers for ordered collections of elements:\n\n### **1. Python Lists (Mutable)**\nLists are used when you need an ordered collection that will expand, shrink, or change during program execution (e.g., adding items to a shopping cart or tracking real-time student test marks).\n\n```python\n# Creation\nfruits = [\"mango\", \"banana\", \"passion\"]\n\n# Accessing elements (0-indexed)\nprint(fruits[0])  # Output: mango\n\n# In-place modification\nfruits[1] = \"avocado\"\nprint(fruits)  # Output: ['mango', 'avocado', 'passion']\n\n# Appending elements to the end\nfruits.append(\"pineapple\")\nprint(fruits)  # Output: ['mango', 'avocado', 'passion', 'pineapple']\n\n# Measuring container length\nprint(len(fruits))  # Output: 4\n```\n\n### **2. Python Tuples (Immutable)**\nTuples are used to store collections of data that **must not change** during program execution (e.g., geographical GPS coordinates of a school, RGB color values, or database primary keys). Because tuples are write-protected, the Python interpreter optimizes their memory storage, making them faster to read and immune to accidental tampering.\n\n```python\n# Creation (using round parentheses)\ncoordinates = (-1.2921, 36.8219)  # Latitude, Longitude of Nairobi\n\n# Reading elements\nprint(coordinates[0])  # Output: -1.2921\n\n# Attempting mutation raises TypeError\ntry:\n    coordinates[0] = -1.3000\nexcept TypeError as e:\n    print(f\"Error caught: {e}\")  # 'tuple' object does not support item assignment\n```"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Data Structure Mutability: Python Lists vs. Tuples",
                        "content": {
                            "svg_content": SVG_LIST_VS_TUPLE_MUTABILITY,
                            "caption": "Side-by-side architectural comparison of mutable Python list memory buffers vs immutable locked tuple records."
                        }
                    },
                    {
                        "type": "step_by_step_worked_example",
                        "title": "Worked Example: Memory Address Calculation and Tuple Write Protection",
                        "content": {
                            "goal": "Calculate the physical RAM address of an array element and demonstrate why tuples prevent runtime corruption.",
                            "problem": "Part A: An array of 64-bit floating-point numbers (8 bytes each) has a base memory address of 0x2000. Calculate the exact physical RAM address of the element at index position 4.\nPart B: Explain the runtime behavior if a developer executes `location = (0.514, 35.269); location[1] = 35.300`.",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "step_title": "Identify Address Formula Parameters",
                                    "step_description": "Base Address = 0x2000\nTarget Index = 4\nElement Size = 8 bytes\nFormula: Address = Base + (Index * Element_Size)"
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Compute Byte Offset and Physical RAM Address",
                                    "step_description": "Byte Offset = 4 * 8 bytes = 32 bytes (decimal).\nConvert 32 decimal to hexadecimal: 32 = 0x20.\nRAM Address = 0x2000 + 0x20 = 0x2020."
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Analyze Tuple Modification Runtime Error",
                                    "step_description": "In Python, `location` is declared as a tuple using parentheses `()`. When `location[1] = 35.300` is executed, the interpreter raises a `TypeError: 'tuple' object does not support item assignment` because tuples are immutable and stored in read-only memory buffers."
                                }
                            ],
                            "conclusion": "The element at index 4 resides at RAM address 0x2020. The tuple assignment is rejected at runtime, preventing accidental data modification."
                        }
                    }
                ],

                # Page 4: Formative Knowledge Checks (4 MCQs)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 1: Constant-Time Array Indexing",
                        "content": {
                            "question": "Why is accessing an element in an array by its index an extremely fast, constant-time O(1) operation?",
                            "options": [
                                "Array elements are stored contiguously in physical RAM, allowing the CPU to compute the exact memory address mathematically using a base-offset formula.",
                                "The compiler converts the array into a hash map before running the code.",
                                "Arrays do not require physical RAM allocations and execute directly inside CPU cache registers.",
                                "The operating system sorts the entire array prior to every read request."
                            ],
                            "correct_answer": "Array elements are stored contiguously in physical RAM, allowing the CPU to compute the exact memory address mathematically using a base-offset formula.",
                            "explanation": "Because array memory slots are contiguous and uniform in byte size, the CPU computes `Address = Base + (Index * Element_Size)` in a single hardware arithmetic cycle without scanning previous elements."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 2: Identification of Immutable Containers",
                        "content": {
                            "question": "Which of the following Python data structures is immutable, preventing any in-place element modifications after creation?",
                            "options": [
                                "List",
                                "Tuple",
                                "Dictionary",
                                "Set"
                            ],
                            "correct_answer": "Tuple",
                            "explanation": "Tuples are immutable sequence containers in Python. Once created, their elements cannot be changed, appended, or deleted, raising a `TypeError` on assignment attempts."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 3: Physical Address Calculation",
                        "content": {
                            "question": "An array of 4-byte integers begins at base address 0x1000. What is the physical memory address of the element stored at index 5?",
                            "options": [
                                "0x1005",
                                "0x1014",
                                "0x1020",
                                "0x1050"
                            ],
                            "correct_answer": "0x1014",
                            "explanation": "Offset = 5 * 4 bytes = 20 bytes (decimal). Converting 20 to hexadecimal gives `0x14` ($16 \\times 1 + 4$). Adding to base `0x1000 + 0x14` yields `0x1014`."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 4: List Modification Operations",
                        "content": {
                            "question": "Given scores = [70, 85, 90], what will be the content of scores after executing scores[1] = 88 followed by scores.append(95)?",
                            "options": [
                                "[70, 88, 90, 95]",
                                "[88, 85, 90, 95]",
                                "[70, 85, 88, 95]",
                                "[95, 70, 88, 90]"
                            ],
                            "correct_answer": "[70, 88, 90, 95]",
                            "explanation": "In Python lists (0-indexed), `scores[1] = 88` replaces the second element (85) with 88. Then `scores.append(95)` adds 95 to the end of the list, resulting in `[70, 88, 90, 95]`."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LEARNING UNIT 2: Associative Containers: Dictionaries, Hashing Systems, and Set Operations
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Associative Containers: Dictionaries, Hashing Systems, and Set Operations",
            "unit_description": "Exploring key-value pairs, the English dictionary analogy, hash table mechanics, constant-time O(1) associative lookups, and Python set operations (deduplication, union, intersection, and difference).",
            "lesson_title": "Lessons 83 to 86: Dictionaries, Hashing Systems, and Set Operations",
            "pages": [
                # Page 1: Introduction & The English Dictionary Analogy
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Master Key-Value Hashing and Mathematical Set Operations",
                        "content": {
                            "goal": "Explain how hash tables achieve constant-time key-value lookups in dictionaries, manipulate associative data structures in Python, and apply set theory operations (union, intersection, difference) for data filtering."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 'English Dictionary' Analogy & Key-Value Mechanics",
                        "content": {
                            "text": "Imagine opening a physical English dictionary. If you want to find the definition of the word **'Kilobyte'**, you do not start at page 1 and read every single word sequentially. That would take hours!\n\nInstead, you look up the word ('Kilobyte') directly as a **Key** to retrieve its corresponding definition ('1024 Bytes') as the **Value**.\n\nIn modern software development, a **Dictionary (Map / Associative Array)** is an unordered container that stores data as **Key-Value pairs**.\n\n### **How Hashing Powers Instant Lookups**\nUnder the hood, dictionaries use a mathematical algorithm called a **Hash Function**:\n1. When you request `student[\"name\"]`, the string key `\"name\"` is passed into the hash function.\n2. The hash function converts the characters into a unique numerical integer hash code.\n3. This hash code maps directly to an internal memory index bucket in RAM.\n4. The value is retrieved instantly in **$O(1)$ constant time**, regardless of whether the dictionary contains 10 records or 10,000,000 records!"
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Hash Table Key-Value Mapping Structure",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Hash_table_3_1_1_0_1_0_0_SP.svg/1024px-Hash_table_3_1_1_0_1_0_0_SP.svg.png",
                            "caption": "Hash table schematic showing keys processed by a hash function to point directly to data bucket slots.",
                            "author": "Wikimedia Commons",
                            "licensing": "Public Domain"
                        }
                    }
                ],

                # Page 2: Python Dictionary Operations & Visual Hashing Pipeline
                [
                    {
                        "type": "concept_explanation",
                        "title": "Python Dictionary Mechanics and Data Manipulation",
                        "content": {
                            "text": "In Python, dictionaries are defined using curly braces `{}` with colon-separated key-value pairs.\n\n### **Python Dictionary Operations**\n```python\n# 1. Creation of a student database record\nstudent = {\n    \"admission_no\": 4512,\n    \"name\": \"Jane Amina\",\n    \"class\": \"10 Blue\",\n    \"gpa\": 3.8\n}\n\n# 2. Accessing values using keys\nprint(student[\"name\"])  # Output: Jane Amina\n\n# 3. Modifying an existing value\nstudent[\"gpa\"] = 3.9\n\n# 4. Adding a new key-value pair\nstudent[\"school_fees_paid\"] = True\n\n# 5. Deleting a key-value pair\ndel student[\"class\"]\n\n# 6. Checking key existence\nif \"admission_no\" in student:\n    print(f\"ID Verified: {student['admission_no']}\")\n```\n\n### **Rules for Dictionary Keys**\n- Keys **must be unique** (duplicate keys will overwrite previous values).\n- Keys **must be immutable** (strings, integers, floats, or tuples are allowed; mutable lists cannot be keys)."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Search Efficiency: Sequential List Search vs. Hash Map (Dictionary)",
                        "content": {
                            "svg_content": SVG_LIST_VS_DICTIONARY_LOOKUP_HASHING,
                            "caption": "Comparative diagram contrasting linear $O(N)$ list search against instant $O(1)$ key-value hashing."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Python Dictionaries and Hash Maps Explained",
                        "content": {
                            "youtube_id": "daefaLgNkw0",
                            "description": "Comprehensive tutorial covering dictionary creation, key-value lookups, hash functions, and algorithmic complexity."
                        }
                    }
                ],

                # Page 3: Python Set Mechanics and Venn Operations
                [
                    {
                        "type": "concept_explanation",
                        "title": "Python Set Mechanics & Mathematical Set Operations",
                        "content": {
                            "text": "A **Set** is an unordered collection of **unique elements** with no duplicate values permitted.\n\nSets are widely used for automatic data deduplication and performing mathematical set algebra (Union, Intersection, Difference).\n\n### **Python Set Operations**\n```python\n# 1. Automatic Deduplication\nroll_call = {\"Kofi\", \"Amina\", \"Kofi\", \"Abdi\", \"Amina\"}\nprint(roll_call)  # Output: {'Kofi', 'Amina', 'Abdi'} (duplicates pruned)\n\n# 2. Adding Elements\nroll_call.add(\"Chipo\")\n\n# 3. Mathematical Venn Set Operations\nscience_club = {\"Amina\", \"Kofi\", \"Mwangi\"}\nmath_club = {\"Mwangi\", \"Abdi\", \"Chipo\"}\n\n# Intersection (Members in BOTH clubs: &)\nboth_clubs = science_club.intersection(math_club)\nprint(both_clubs)  # Output: {'Mwangi'}\n\n# Union (Members in EITHER club: |)\nall_members = science_club.union(math_club)\nprint(all_members)  # Output: {'Amina', 'Kofi', 'Mwangi', 'Abdi', 'Chipo'}\n\n# Difference (Members in Science BUT NOT in Math: -)\nscience_only = science_club - math_club\nprint(science_only)  # Output: {'Amina', 'Kofi'}\n```"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Python Set Mechanics & Mathematical Venn Operations",
                        "content": {
                            "svg_content": SVG_SET_THEORY_VENN_OPERATIONS,
                            "caption": "Venn diagram showing set intersection, union, difference, and automated duplicate elimination in Python."
                        }
                    },
                    {
                        "type": "step_by_step_worked_example",
                        "title": "Worked Example: Deduplication and Relational Set Filtering",
                        "content": {
                            "goal": "Filter duplicate entries from an attendance log and determine exclusive club participants.",
                            "problem": "A school ICT club and Robotics club have the following rosters:\n`ict_club = [\"Wanjiku\", \"Kamau\", \"Amina\", \"Wanjiku\", \"Otieno\"]`\n`robotics_club = [\"Kamau\", \"Otieno\", \"Chebet\"]`\nTask 1: Convert `ict_club` to a set to remove duplicates.\nTask 2: Find students registered ONLY in the ICT club.",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "step_title": "Deduplicate ICT Club Roster",
                                    "step_description": "Convert list to set: `ict_set = set(ict_club)`. The duplicate `\"Wanjiku\"` is automatically removed: `{'Wanjiku', 'Kamau', 'Amina', 'Otieno'}` (Length: 4)."
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Convert Robotics Club and Calculate Set Difference",
                                    "step_description": "`robotics_set = set(robotics_club)` -> `{'Kamau', 'Otieno', 'Chebet'}`.\nCalculate Difference: `ict_only = ict_set.difference(robotics_set)`.\nRemoves `\"Kamau\"` and `\"Otieno\"` (present in robotics)."
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Evaluate Final Result",
                                    "step_description": "`ict_only` produces `{'Wanjiku', 'Amina'}`."
                                }
                            ],
                            "conclusion": "The deduplicated ICT club contains 4 unique members. The students participating exclusively in the ICT club are Wanjiku and Amina."
                        }
                    }
                ],

                # Page 4: Formative Knowledge Checks (4 MCQs)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 1: Set Deduplication Execution",
                        "content": {
                            "question": "Examine the following Python code execution:\n\ndata = {\"apple\", \"banana\", \"apple\", \"mango\"}\nprint(len(data))\n\nWhat output will be printed to the console?",
                            "options": [
                                "4",
                                "3",
                                "2",
                                "Syntax Error"
                            ],
                            "correct_answer": "3",
                            "explanation": "In Python, curly braces `{}` containing comma-separated elements without colons declare a `set`. Sets automatically eliminate duplicate entries. The duplicate `\"apple\"` is removed, leaving 3 unique items (`\"apple\"`, `\"banana\"`, `\"mango\"`), so `len(data)` evaluates to 3."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 2: Dictionary Key Immutability",
                        "content": {
                            "question": "Why can a Python list NOT be used as a key in a dictionary?",
                            "options": [
                                "Lists are mutable and therefore unhashable, meaning their hash code could change if modified.",
                                "Lists occupy too much RAM to fit inside a dictionary.",
                                "Python dictionaries only accept floating-point numbers as keys.",
                                "Lists are automatically converted to strings when passed as keys."
                            ],
                            "correct_answer": "Lists are mutable and therefore unhashable, meaning their hash code could change if modified.",
                            "explanation": "Dictionary keys must be immutable so their hash values remain constant throughout execution. Because lists can be modified in-place, Python raises a `TypeError: unhashable type: 'list'` if used as a key."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 3: Mathematical Set Intersection",
                        "content": {
                            "question": "If set A = {10, 20, 30} and set B = {20, 30, 40}, what is the result of A.intersection(B)?",
                            "options": [
                                "{20, 30}",
                                "{10, 20, 30, 40}",
                                "{10}",
                                "{40}"
                            ],
                            "correct_answer": "{20, 30}",
                            "explanation": "The intersection of two sets contains only elements that exist in BOTH sets. Elements 20 and 30 are shared by both A and B."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 4: Dictionary Key Lookup Complexity",
                        "content": {
                            "question": "What is the average time complexity for retrieving a value associated with a known key in a standard Python dictionary?",
                            "options": [
                                "O(1) Constant Time",
                                "O(N) Linear Time",
                                "O(N^2) Quadratic Time",
                                "O(log N) Logarithmic Time"
                            ],
                            "correct_answer": "O(1) Constant Time",
                            "explanation": "Dictionaries use hash tables to translate keys directly into bucket memory addresses, allowing instantaneous O(1) average lookup times."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LEARNING UNIT 3: Fundamental Search and Sorting Algorithms
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Fundamental Search and Sorting Algorithms",
            "unit_description": "Algorithmic logic and step-by-step tracing of Sequential Search and Bubble Sort algorithms, pseudocode specifications, Python implementations, and trace table dry runs.",
            "lesson_title": "Lessons 87 to 91: Sequential Search and Bubble Sort Algorithms",
            "pages": [
                # Page 1: Sequential Search Algorithm
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Understand Sequential Search and Bubble Sort Logic",
                        "content": {
                            "goal": "Construct, implement, and trace the Sequential (Linear) Search and Bubble Sort algorithms, analyze their loop mechanics, and perform dry-run trace table verifications."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Sequential Search Algorithm",
                        "content": {
                            "text": "Sequential search (also known as **Linear Search**) is the most straightforward search algorithm.\n\nIt starts at the very first element (index 0) of a list and checks each element one-by-one in order until a match is found or the end of the list is reached.\n\n### **Algorithmic Pseudocode Specification**\n```text\nSTART\n    SET found = False\n    SET index = 0\n    SET search_key = 88\n    SET list = [45, 12, 88, 30, 91]\n    \n    WHILE index < len(list) AND found == False DO\n        IF list[index] == search_key THEN\n            SET found = True\n            SET position = index\n        ELSE\n            SET index = index + 1\n        ENDIF\n    ENDWHILE\n    \n    IF found == True THEN\n        OUTPUT \"Item found at index position: \", position\n    ELSE\n        OUTPUT \"Item not found in list.\"\n    ENDIF\nEND\n```\n\n### **Python Implementation**\n```python\ndef sequential_search(target_list, key):\n    index = 0\n    while index < len(target_list):\n        if target_list[index] == key:\n            return index  # Match found! Return index position immediately\n        index += 1\n    return -1  # Target does not exist in list\n```\n\n### **Performance Characteristics**\n- **Best-Case**: Match is at index `0` $\\to 1$ comparison ($O(1)$).\n- **Worst-Case**: Target is at the last index or missing entirely $\\to N$ comparisons ($O(N)$)."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Sequential Search Algorithm Stepping Workflow",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Linear_search_algorithm.svg/1024px-Linear_search_algorithm.svg.png",
                            "caption": "Linear search pointer stepping through list indices sequentially until a target match is encountered.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    }
                ],

                # Page 2: Bubble Sort Algorithm Mechanics & Logic
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Bubble Sort Algorithm",
                        "content": {
                            "text": "**Bubble Sort** is a comparison-based sorting algorithm that repeatedly steps through a list, compares adjacent elements, and swaps them if they are in the wrong order.\n\nThe algorithm gets its name because larger elements gradually \"bubble\" to the end of the list with each complete pass.\n\n### **Bubble Sort Execution Rules**\n- For a list of size $N$, the algorithm requires up to **$N - 1$ passes** to guarantee complete sorting.\n- On each pass, the inner loop compares adjacent elements at `index` and `index + 1`.\n- If `list[index] > list[index + 1]`, the elements are swapped.\n- After pass $i$, the largest remaining unsorted element is locked in its permanent final position.\n\n### **Pseudocode Specification**\n```text\nSTART\n    SET list = [14, 5, 8, 2]\n    SET n = len(list)\n    FOR pass = 0 TO n - 2 STEP 1 DO\n        FOR index = 0 TO n - pass - 2 STEP 1 DO\n            IF list[index] > list[index + 1] THEN\n                # Swap adjacent elements\n                SET temp = list[index]\n                SET list[index] = list[index + 1]\n                SET list[index + 1] = temp\n            ENDIF\n        ENDFOR\n    ENDFOR\nEND\n```\n\n### **Python Implementation**\n```python\ndef bubble_sort(arr):\n    n = len(arr)\n    for i in range(n):\n        # Inner loop: Last i elements are already in place\n        for j in range(0, n - i - 1):\n            if arr[j] > arr[j + 1]:\n                # Swap elements using Python tuple packing shortcut\n                arr[j], arr[j + 1] = arr[j + 1], arr[j]\n    return arr\n```"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Bubble Sort Execution: Multi-Pass Adjacent Swap Trace",
                        "content": {
                            "svg_content": SVG_BUBBLE_SORT_PASSES_TRACE,
                            "caption": "Complete multi-pass execution diagram tracing adjacent comparisons and swaps for list [14, 5, 8, 2]."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Bubble Sort Algorithm Visualized and Explained",
                        "content": {
                            "youtube_id": "xli_FI7CuzA",
                            "description": "Visual animation and code walkthrough explaining nested loop passes, swapping logic, and time complexity in bubble sort."
                        }
                    }
                ],

                # Page 3: Detailed Tracing of Bubble Sort & Worked Example
                [
                    {
                        "type": "concept_explanation",
                        "title": "Detailed Dry-Run State Tracing of Bubble Sort",
                        "content": {
                            "text": "Let us trace the complete execution of Bubble Sort sorting the array `[14, 5, 8, 2]` ($N = 4$) using a trace table.\n\n### **Pass 1 Tracing ($i = 0$):**\n| Step | Inner Index `j` | Element `arr[j]` | Adjacent `arr[j+1]` | Swap Required? | Current List State |\n| :---: | :---: | :---: | :---: | :---: | :---: |\n| 1 | `0` | `14` | `5` | `True` ($14 > 5$) | `[5, 14, 8, 2]` |\n| 2 | `1` | `14` | `8` | `True` ($14 > 8$) | `[5, 8, 14, 2]` |\n| 3 | `2` | `14` | `2` | `True` ($14 > 2$) | `[5, 8, 2, 14]` |\n*(Outcome: The largest element, 14, has bubbled to its final position at index 3 and is locked).* \n\n### **Pass 2 Tracing ($i = 1$):**\n| Step | Inner Index `j` | Element `arr[j]` | Adjacent `arr[j+1]` | Swap Required? | Current List State |\n| :---: | :---: | :---: | :---: | :---: | :---: |\n| 4 | `0` | `5` | `8` | `False` ($5 \\le 8$) | `[5, 8, 2, 14]` |\n| 5 | `1` | `8` | `2` | `True` ($8 > 2$) | `[5, 2, 8, 14]` |\n*(Outcome: The second-largest element, 8, is now locked in place at index 2).* \n\n### **Pass 3 Tracing ($i = 2$):**\n| Step | Inner Index `j` | Element `arr[j]` | Adjacent `arr[j+1]` | Swap Required? | Current List State |\n| :---: | :---: | :---: | :---: | :---: | :---: |\n| 6 | `0` | `5` | `2` | `True` ($5 > 2$) | `[2, 5, 8, 14]` |\n*(Outcome: 5 is placed at index 1 and 2 at index 0. The list is fully sorted: `[2, 5, 8, 14]`!)*"
                        }
                    },
                    {
                        "type": "step_by_step_worked_example",
                        "title": "Worked Example: Dry-Run Tracing a 4-Element List",
                        "content": {
                            "goal": "Perform a manual dry run of Bubble Sort on array [9, 3, 7, 1] and determine the total number of swaps.",
                            "problem": "Trace each pass for `arr = [9, 3, 7, 1]` ($N = 4$). List the array state after each pass and count total swaps.",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "step_title": "Execute Pass 1",
                                    "step_description": "- Compare (9, 3) -> Swap -> [3, 9, 7, 1] (Swap 1)\n- Compare (9, 7) -> Swap -> [3, 7, 9, 1] (Swap 2)\n- Compare (9, 1) -> Swap -> [3, 7, 1, 9] (Swap 3)\nPass 1 Result: `[3, 7, 1, 9]` (9 locked at index 3)."
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Execute Pass 2",
                                    "step_description": "- Compare (3, 7) -> No Swap -> [3, 7, 1, 9]\n- Compare (7, 1) -> Swap -> [3, 1, 7, 9] (Swap 4)\nPass 2 Result: `[3, 1, 7, 9]` (7 locked at index 2)."
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Execute Pass 3",
                                    "step_description": "- Compare (3, 1) -> Swap -> [1, 3, 7, 9] (Swap 5)\nPass 3 Result: `[1, 3, 7, 9]` (All sorted)."
                                }
                            ],
                            "conclusion": "The list is sorted in 3 passes with a total of 5 swap operations, yielding final sorted array `[1, 3, 7, 9]`."
                        }
                    }
                ],

                # Page 4: Formative Knowledge Checks (4 MCQs)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 1: Bubble Sort Passes Calculation",
                        "content": {
                            "question": "What is the maximum number of comparison passes required to sort a list of N elements using the standard Bubble Sort algorithm?",
                            "options": [
                                "N - 1",
                                "N^2",
                                "2 * N",
                                "1024"
                            ],
                            "correct_answer": "N - 1",
                            "explanation": "For an array of $N$ elements, after $N - 1$ passes, $N - 1$ elements are guaranteed to be in their correct positions. The remaining single element is inherently in the correct position, so at most $N - 1$ passes are required."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 2: Sequential Search on Missing Target",
                        "content": {
                            "question": "What does a sequential search algorithm do if the target element does not exist in the list?",
                            "options": [
                                "It scans the entire list from index 0 to N-1 and then reports a not-found state (e.g. returning -1).",
                                "It crashes immediately with an IndexError.",
                                "It inserts the missing item automatically at index 0.",
                                "It enters an infinite loop until the computer is restarted."
                            ],
                            "correct_answer": "It scans the entire list from index 0 to N-1 and then reports a not-found state (e.g. returning -1).",
                            "explanation": "In sequential search, the algorithm must verify every element from start to finish before concluding that the target does not exist, subsequently returning a sentinel failure value like -1."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 3: Variable Swapping with Temp",
                        "content": {
                            "question": "In pseudocode, why is a temporary variable ('temp') used when swapping list[j] and list[j+1]?",
                            "options": [
                                "To temporarily hold the value of list[j] so it is not overwritten and lost when list[j+1] is copied into list[j].",
                                "To calculate the average of the two numbers.",
                                "To convert integers into strings before swapping.",
                                "To notify the CPU memory manager to allocate a new array."
                            ],
                            "correct_answer": "To temporarily hold the value of list[j] so it is not overwritten and lost when list[j+1] is copied into list[j].",
                            "explanation": "Assigning `list[j] = list[j+1]` directly overwrites the original value stored in `list[j]`. A `temp` variable preserves `list[j]` so it can be assigned to `list[j+1]`."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 4: Bubble Sort State After Pass 1",
                        "content": {
                            "question": "If Bubble Sort is applied to [8, 3, 6, 2], what is the list state immediately after the first complete pass (i = 0)?",
                            "options": [
                                "[3, 6, 2, 8]",
                                "[2, 3, 6, 8]",
                                "[8, 6, 3, 2]",
                                "[3, 8, 2, 6]"
                            ],
                            "correct_answer": "[3, 6, 2, 8]",
                            "explanation": "Pass 1 compares (8,3)->[3,8,6,2], (8,6)->[3,6,8,2], (8,2)->[3,6,2,8]. The largest value (8) bubbles to the end of the list."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LEARNING UNIT 4: Practical Classroom Labs and Software Implementations
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Practical Classroom Labs and Software Implementations",
            "unit_description": "Hands-on programming laboratory activities: building a dynamic student examination grade tracker using lists and a store inventory lookup system using dictionaries in Python.",
            "lesson_title": "Lesson 92: Practical Classroom Programming Labs",
            "pages": [
                # Page 1: Lab Activity 1: The School Examination Tracker
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Implement Real-World List and Dictionary Software Systems",
                        "content": {
                            "goal": "Develop production Python scripts utilizing dynamic lists, sentinel-controlled intake loops, numerical analytics, and dictionary associative searches."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Lab Activity 1: The School Examination Tracker",
                        "content": {
                            "text": "### **Objective**\nBuild an interactive Python program to record, manage, and analyze student examination scores.\n\n### **Program Requirements**\n1. **Sentinel Intake Loop**: Continuously prompt a teacher to enter student exam marks, appending each valid score to a `marks` list until `-1` is entered to terminate data entry.\n2. **Class Average Calculation**: Sum all scores in the list and divide by `len(marks)`.\n3. **Extremum Extraction**: Determine and output the highest (`max(marks)`) and lowest (`min(marks)`) marks.\n4. **Input Validation**: Ensure empty lists are handled gracefully without zero-division runtime crashes.\n\n### **Python Production Implementation**\n```python\n# Lab 1: School Examination Score Tracker\nmarks = []\nprint(\"=== KCSE Grade Tracker (Enter -1 to Finish) ===\")\n\nwhile True:\n    try:\n        score = float(input(\"Enter student mark (0-100 or -1): \"))\n        if score == -1:\n            break\n        if 0 <= score <= 100:\n            marks.append(score)\n        else:\n            print(\"Invalid score! Must be between 0 and 100.\")\n    except ValueError:\n        print(\"Please enter a valid numeric number.\")\n\nif len(marks) > 0:\n    class_avg = sum(marks) / len(marks)\n    highest = max(marks)\n    lowest = min(marks)\n    \n    print(\"\\n--- Score Summary Report ---\")\n    print(f\"Total Students: {len(marks)}\")\n    print(f\"Class Average:  {class_avg:.2f}%\")\n    print(f\"Highest Score:  {highest:.1f}%\")\n    print(f\"Lowest Score:   {lowest:.1f}%\")\nelse:\n    print(\"No exam scores were entered.\")\n```"
                        }
                    },
                    {
                        "type": "step_by_step_worked_example",
                        "title": "Worked Example: Exam Tracker Dry Run with Real Marks",
                        "content": {
                            "goal": "Execute a manual dry run of the Exam Tracker with user inputs: 82, 91, 64, 75, 50, -1.",
                            "problem": "Trace list contents, calculate sum, class average, highest, and lowest values for inputs `[82, 91, 64, 75, 50, -1]`.",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "step_title": "Trace Loop Appending",
                                    "step_description": "Input 82 -> `marks = [82]`\nInput 91 -> `marks = [82, 91]`\nInput 64 -> `marks = [82, 91, 64]`\nInput 75 -> `marks = [82, 91, 64, 75]`\nInput 50 -> `marks = [82, 91, 64, 75, 50]`\nInput -1 -> Sentinel triggered; break while loop."
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Compute Sum and Class Average",
                                    "step_description": "Sum = 82 + 91 + 64 + 75 + 50 = 362.\nTotal Students = 5.\nAverage = 362 / 5 = 72.40%."
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Extract Max and Min Values",
                                    "step_description": "Highest Mark: `max([82, 91, 64, 75, 50]) = 91.0%`.\nLowest Mark: `min([82, 91, 64, 75, 50]) = 50.0%`."
                                }
                            ],
                            "conclusion": "The program processes 5 students with an average score of 72.40%, highest mark of 91.0%, and lowest mark of 50.0%."
                        }
                    }
                ],

                # Page 2: Lab Activity 2: Fast Store Inventory Lookup System
                [
                    {
                        "type": "concept_explanation",
                        "title": "Lab Activity 2: Building a Fast Inventory Lookup System",
                        "content": {
                            "text": "### **Objective**\nCreate a dictionary-based storage and instant search system for a local school canteen/store.\n\n### **Program Requirements**\n1. **Dictionary Catalogue**: Initialize a dictionary where keys are item names (`str`) and values are prices in Kenyan Shillings (`float`).\n2. **Dynamic Search Query**: Prompt the user to input an item name to look up.\n3. **Membership Check**: Use the `in` operator to verify if the item exists in the catalogue.\n4. **Formatted Output**: If found, print the price formatted with 2 decimal places. If missing, output `\"Item out of stock / Not found.\"`.\n\n### **Python Production Implementation**\n```python\n# Lab 2: School Store Inventory Lookup System\ninventory = {\n    \"exercise book\": 80.00,\n    \"blue pen\": 25.00,\n    \"ruler\": 45.00,\n    \"mathematical set\": 350.00,\n    \"eraser\": 15.00,\n    \"pencil\": 20.00\n}\n\nprint(\"=== School Canteen Inventory Terminal ===\")\nquery = input(\"Enter item name to search: \").strip().lower()\n\nif query in inventory:\n    price = inventory[query]\n    print(f\"\\n[IN STOCK] {query.title()}: KES {price:.2f}\")\nelse:\n    print(f\"\\n[OUT OF STOCK] '{query}' is currently unavailable in the store.\")\n```\n\n### **Engineering Rationale**\nUsing a dictionary allows store staff to look up prices instantaneously ($O(1)$) rather than scrolling through hundreds of paper records."
                        }
                    },
                    {
                        "type": "step_by_step_worked_example",
                        "title": "Worked Example: Inventory Search and Price Lookup",
                        "content": {
                            "goal": "Trace the dictionary lookup for queries 'mathematical set' and 'calculator'.",
                            "problem": "Given inventory = {'exercise book': 80.0, 'mathematical set': 350.0, 'pencil': 20.0}, evaluate search execution for (1) 'mathematical set' and (2) 'calculator'.",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "step_title": "Search Query 1: 'mathematical set'",
                                    "step_description": "Check `'mathematical set' in inventory` -> Evaluates to `True`.\nExtract value: `inventory['mathematical set']` -> 350.00.\nOutput: `[IN STOCK] Mathematical Set: KES 350.00`."
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Search Query 2: 'calculator'",
                                    "step_description": "Check `'calculator' in inventory` -> Evaluates to `False`.\nExecute else branch: Output `[OUT OF STOCK] 'calculator' is currently unavailable in the store.`"
                                }
                            ],
                            "conclusion": "Existing items are retrieved with exact prices in constant time, while absent keys are caught safely without throwing KeyError exceptions."
                        }
                    }
                ],

                # Page 3: Formative Knowledge Checks (4 MCQs)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 1: Sentinel Value Loop Control",
                        "content": {
                            "question": "What is the primary role of the sentinel value '-1' in the examination tracker loop?",
                            "options": [
                                "It serves as a special stopping signal to terminate data entry without being added as a student score.",
                                "It calculates the average score automatically.",
                                "It deletes previous scores if the teacher makes a mistake.",
                                "It is stored as the minimum score in the list."
                            ],
                            "correct_answer": "It serves as a special stopping signal to terminate data entry without being added as a student score.",
                            "explanation": "A sentinel value is a distinct data value used to indicate the end of input in a loop without participating in calculations."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 2: Safe Dictionary Key Checking",
                        "content": {
                            "question": "What happens in Python if you execute inventory['calculator'] when 'calculator' is NOT present in the dictionary?",
                            "options": [
                                "Python raises a KeyError exception and halts program execution if unhandled.",
                                "Python returns None without throwing any error.",
                                "Python automatically creates the key with a price of 0.0.",
                                "Python converts the dictionary into a list."
                            ],
                            "correct_answer": "Python raises a KeyError exception and halts program execution if unhandled.",
                            "explanation": "Directly indexing a dictionary with a non-existent key raises a `KeyError`. Using `if key in dictionary:` or `dictionary.get(key)` prevents runtime crashes."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 3: Handling Empty Container Calculations",
                        "content": {
                            "question": "Why is it critical to check 'if len(marks) > 0:' before executing sum(marks) / len(marks)?",
                            "options": [
                                "To prevent a ZeroDivisionError runtime crash if the user enters -1 immediately without entering any marks.",
                                "To sort the marks in descending order.",
                                "Because Python lists cannot calculate sums of positive numbers.",
                                "To convert integer scores into floating-point decimals."
                            ],
                            "correct_answer": "To prevent a ZeroDivisionError runtime crash if the user enters -1 immediately without entering any marks.",
                            "explanation": "If `marks` is empty, `len(marks)` is 0. Dividing by 0 causes a fatal `ZeroDivisionError`."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 4: List Append Operation Complexity",
                        "content": {
                            "question": "What is the amortized time complexity of appending an element to the end of a dynamic list (e.g. marks.append(score))?",
                            "options": [
                                "O(1) Constant Time",
                                "O(N) Linear Time",
                                "O(N^2) Quadratic Time",
                                "O(log N) Logarithmic Time"
                            ],
                            "correct_answer": "O(1) Constant Time",
                            "explanation": "Appending an element to the end of a dynamic array operates in amortized $O(1)$ constant time."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LEARNING UNIT 5: Unit Assessment, Algorithm Tracing, and Agricultural Cooperative Case Study
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Unit Assessment, Algorithm Tracing, and Agricultural Cooperative Case Study",
            "unit_description": "Comprehensive summative assessment of containers and data structures, full dry-run trace table synthesis, and production implementation of the Rift Valley Farmer Cooperative database system.",
            "lesson_title": "Lesson 93: Comprehensive Practice Assessment and Agricultural Case Study",
            "pages": [
                # Page 1: Topic Practice & Assessment Library
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Synthesize Data Structures & Algorithmic Problem Solving",
                        "content": {
                            "goal": "Demonstrate mastery over lists, tuples, dictionaries, sets, sequential search, and bubble sort by solving multi-tier practical engineering challenges and executing comprehensive dry-run traces."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Data Structures & Operational Properties Synthesis Matrix",
                        "content": {
                            "text": "Before developing integrated agricultural systems, review the fundamental properties and computational complexities of all four core containers and search/sort algorithms.\n\n### **Operational Properties Comparison Table**\n| Data Structure / Algorithm | Order / Indexing | Mutability | Duplicates? | Primary Use Case & Complexity |\n| :--- | :--- | :--- | :--- | :--- |\n| **List (Array)** | Ordered (0-indexed) | Mutable | Allowed | Dynamic collections, sorting, $O(1)$ index access |\n| **Tuple** | Ordered (0-indexed) | Immutable | Allowed | Fixed coordinates, RGB records, read-only protection |\n| **Dictionary** | Unordered (Key-indexed) | Mutable | Unique Keys | Fast relational key-value lookups, $O(1)$ hash retrieval |\n| **Set** | Unordered (Non-indexed) | Mutable | No Duplicates | Deduplication, union/intersection Venn operations |\n| **Sequential Search** | Linear sweep ($0 \\dots N-1$) | N/A | N/A | Unsorted search, $O(N)$ worst-case time |\n| **Bubble Sort** | Adjacent swap passes | N/A | N/A | Educational sorting, $O(N^2)$ worst-case comparisons |"
                        }
                    },
                    {
                        "type": "step_by_step_worked_example",
                        "title": "Worked Example: Selecting Optimal Data Structures for Real-World Systems",
                        "content": {
                            "goal": "Select and justify the most appropriate data container for three distinct system components.",
                            "problem": "Component 1: School ID to student profile lookup.\nComponent 2: Daily temperature readings recorded every hour for sorting and calculating daily average.\nComponent 3: Kenya County GPS boundary coordinates that must never be altered during program runtime.",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "step_title": "Select Container for Component 1 (ID Lookup)",
                                    "step_description": "Selection: **Dictionary (Key-Value Map)**. Justification: Member/School ID serves as a unique key mapping to student details, enabling $O(1)$ instant lookups without linear searching."
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Select Container for Component 2 (Hourly Temperatures)",
                                    "step_description": "Selection: **List (Array)**. Justification: Temperatures are ordered sequential numbers requiring dynamic insertion, mathematical summation for averages, and element reordering for sorting."
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Select Container for Component 3 (County Coordinates)",
                                    "step_description": "Selection: **Tuple**. Justification: GPS coordinates (Latitude, Longitude) are fixed pairs that must be immutable to prevent accidental runtime tampering."
                                }
                            ],
                            "conclusion": "Using dictionaries for associative lookups, lists for mutable numerical streams, and tuples for locked records optimizes both system performance and data security."
                        }
                    }
                ],

                # Page 2: Challenging Application Scenario: Rift Valley Farmer Cooperative Database
                [
                    {
                        "type": "concept_explanation",
                        "title": "Challenging Scenario: The Rift Valley Farmer Cooperative Database",
                        "content": {
                            "text": "### **Scenario Background**\nAn agricultural cooperative in the Rift Valley requires a unified Python software system to manage member farmer records and milk delivery productivity.\n\n### **System Requirements**\nEach farmer has:\n- A unique **Member ID** (integer key)\n- A **Farmer Name** (string value)\n- A list of monthly **Milk Delivery Weights** (in kilograms, decimal float values)\n\n### **Required Operations**\n1. **Fast Profile Lookup**: Given a Member ID, retrieve the Farmer's Name instantly ($O(1)$ dictionary lookup).\n2. **Average Yield Calculation**: Calculate the average monthly milk weight delivered by a specific farmer.\n3. **Sequential Yield Search**: Verify if a specific delivery weight exists in the farmer's monthly records.\n4. **Performance Sorting (Bubble Sort)**: Sort a farmer's monthly delivery weights in ascending order to analyze productivity growth."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Applied Case Study: Rift Valley Farmer Cooperative Data System",
                        "content": {
                            "svg_content": SVG_COOPERATIVE_DATA_SYSTEM_ARCHITECTURE,
                            "caption": "Three-tier architecture showing dictionary farmer lookups, sequential yield search, and bubble sort analytics."
                        }
                    }
                ],

                # Page 3: Worked Implementation & Dry-Run Trace Table
                [
                    {
                        "type": "concept_explanation",
                        "title": "Rift Valley Cooperative Production Implementation",
                        "content": {
                            "text": "```python\n# Rift Valley Farmer Cooperative Management System\n\n# 1. Member Registry Dictionary (Member ID -> Profile)\nfarmers = {\n    101: {\"name\": \"Cheruiyot\", \"weights\": [120.5, 95.0, 110.0, 85.5]},\n    102: {\"name\": \"Chepngetich\", \"weights\": [140.0, 155.5, 130.0, 160.0]},\n    103: {\"name\": \"Kiprono\", \"weights\": [90.0, 88.5, 92.0, 95.0]}\n}\n\n# 2. Sequential Search Function\ndef search_delivery_weight(weights_list, target_weight):\n    for index in range(len(weights_list)):\n        if weights_list[index] == target_weight:\n            return index  # Found at index position\n    return -1  # Not found\n\n# 3. Bubble Sort Function\ndef bubble_sort_weights(weights_list):\n    arr = list(weights_list)  # Create a working copy\n    n = len(arr)\n    for i in range(n - 1):\n        for j in range(0, n - i - 1):\n            if arr[j] > arr[j + 1]:\n                arr[j], arr[j + 1] = arr[j + 1], arr[j]\n    return arr\n\n# Execution for Member 101 (Cheruiyot)\nmember_id = 101\nfarmer = farmers[member_id]\nraw_weights = farmer[\"weights\"]\n\navg_yield = sum(raw_weights) / len(raw_weights)\nsorted_weights = bubble_sort_weights(raw_weights)\nsearch_target = 110.0\nfound_pos = search_delivery_weight(raw_weights, search_target)\n\nprint(f\"Farmer: {farmer['name']} (ID: {member_id})\")\nprint(f\"Average Monthly Yield: {avg_yield:.2f} kg\")\nprint(f\"Search for {search_target} kg: Found at raw index {found_pos}\")\nprint(f\"Sorted Yields (Ascending): {sorted_weights}\")\n```"
                        }
                    },
                    {
                        "type": "step_by_step_worked_example",
                        "title": "Worked Example: Bubble Sort Complete Trace Table for [120.5, 95.0, 110.0, 85.5]",
                        "content": {
                            "goal": "Provide a complete trace table of the Bubble Sort function sorting Cheruiyot's delivery weights [120.5, 95.0, 110.0, 85.5].",
                            "problem": "Trace array state, comparison values, and swap outcomes for `[120.5, 95.0, 110.0, 85.5]` ($N = 4$).",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "step_title": "Trace Pass 1 (i = 0)",
                                    "step_description": "Step 1 (j=0): Compare 120.5 > 95.0 -> Swap -> `[95.0, 120.5, 110.0, 85.5]`\nStep 2 (j=1): Compare 120.5 > 110.0 -> Swap -> `[95.0, 110.0, 120.5, 85.5]`\nStep 3 (j=2): Compare 120.5 > 85.5 -> Swap -> `[95.0, 110.0, 85.5, 120.5]`\nOutcome: 120.5 locked at index 3."
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Trace Pass 2 (i = 1)",
                                    "step_description": "Step 4 (j=0): Compare 95.0 <= 110.0 -> No Swap -> `[95.0, 110.0, 85.5, 120.5]`\nStep 5 (j=1): Compare 110.0 > 85.5 -> Swap -> `[95.0, 85.5, 110.0, 120.5]`\nOutcome: 110.0 locked at index 2."
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Trace Pass 3 (i = 2)",
                                    "step_description": "Step 6 (j=0): Compare 95.0 > 85.5 -> Swap -> `[85.5, 95.0, 110.0, 120.5]`\nOutcome: All elements locked in ascending order."
                                }
                            ],
                            "conclusion": "The delivery weights are sorted into `[85.5, 95.0, 110.0, 120.5]` across 3 passes and 5 total swaps."
                        }
                    }
                ],

                # Page 4: Summative Knowledge Checks (4 MCQs)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative Check 1: Trade-Off Between Lists and Dictionaries",
                        "content": {
                            "question": "What is the primary architectural trade-off between using a sequential list and a key-value dictionary for storing searchable records?",
                            "options": [
                                "Lists preserve chronological order and require less memory but have slow O(N) search times, whereas dictionaries provide fast O(1) searches using extra memory for hash tables.",
                                "Lists can only store integers, while dictionaries can only store strings.",
                                "Dictionaries are immutable, while lists are mutable.",
                                "Lists execute faster than dictionaries for million-record lookups."
                            ],
                            "correct_answer": "Lists preserve chronological order and require less memory but have slow O(N) search times, whereas dictionaries provide fast O(1) searches using extra memory for hash tables.",
                            "explanation": "Dictionaries trade off increased memory consumption for hash tables to achieve constant-time $O(1)$ search lookups, whereas lists use compact contiguous memory but require linear $O(N)$ scans."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative Check 2: Immutability Design Decision",
                        "content": {
                            "question": "In the Rift Valley Cooperative system, why is a tuple the most appropriate data container for storing a farm's fixed GPS intake coordinates (e.g. (-0.2833, 36.0667))?",
                            "options": [
                                "Tuples are immutable, preventing accidental or malicious modification of critical geographical location coordinates during runtime.",
                                "Tuples allow duplicate coordinates to be merged automatically.",
                                "Tuples sort themselves automatically from North to South.",
                                "Tuples cannot be read by other functions in the script."
                            ],
                            "correct_answer": "Tuples are immutable, preventing accidental or malicious modification of critical geographical location coordinates during runtime.",
                            "explanation": "Fixed constants and geographical coordinates should be stored in tuples because their immutability protects them from unintended runtime reassignment."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative Check 3: True or False on Set Ordering",
                        "content": {
                            "question": "True or False: A Python set is an ordered sequence container that allows duplicate keys to map to the same value index.",
                            "options": [
                                "False — Sets are unordered collections of unique elements and do not permit duplicate values or index-based access.",
                                "True — Sets maintain strict insertion order and allow duplicates.",
                                "True — But only if the set contains numeric values.",
                                "False — Sets permit duplicates as long as they are strings."
                            ],
                            "correct_answer": "False — Sets are unordered collections of unique elements and do not permit duplicate values or index-based access.",
                            "explanation": "Sets in Python are unordered and do not support indexing or duplicate elements. Deduplication is inherent to set architecture."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative Check 4: Sequential Search Execution State",
                        "content": {
                            "question": "If a sequential search is executed on raw_weights = [120.5, 95.0, 110.0, 85.5] for target 110.0, how many element comparisons are executed before returning the result?",
                            "options": [
                                "3 comparisons (checking index 0, index 1, and index 2)",
                                "1 comparison",
                                "4 comparisons",
                                "16 comparisons"
                            ],
                            "correct_answer": "3 comparisons (checking index 0, index 1, and index 2)",
                            "explanation": "Sequential search evaluates index 0 (120.5 != 110.0), index 1 (95.0 != 110.0), and index 2 (110.0 == 110.0), finding a match on the 3rd comparison."
                        }
                    }
                ]
            ]
        }
    ]

# =====================================================================
# INGESTION EXECUTOR
# =====================================================================

def ingest_grade10_topic16(replace: bool = True):
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 10 Computer Science — Topic 16")
    print("Topic: Containers and Data Structures")
    print("=" * 80)

    curriculum = Curriculum.objects.get(id=5)
    grade = Grade.objects.get(curriculum=curriculum, level=10)
    subject, _ = Subject.objects.get_or_create(grade=grade, name="Computer Science")

    with transaction.atomic():
        topic, created = Topic.objects.get_or_create(
            subject=subject,
            order=16,
            defaults={
                "name": "Containers and Data Structures",
                "description": "Comprehensive study of multi-element data structures, hardware contiguous memory allocation, lists, tuples, mutability vs immutability, dictionaries, hashing algorithms, set theory operations, sequential linear search, and bubble sorting with trace verification."
            }
        )

        if not created and replace:
            print(f"[*] Topic 16 already exists (ID: {topic.id}). Performing clean replacement of units and lessons...")
            topic.learning_units.all().delete()
            topic.lessons.all().delete()
            topic.name = "Containers and Data Structures"
            topic.description = "Comprehensive study of multi-element data structures, hardware contiguous memory allocation, lists, tuples, mutability vs immutability, dictionaries, hashing algorithms, set theory operations, sequential linear search, and bubble sorting with trace verification."
            topic.save()

        curriculum_data = build_topic16_curriculum()

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
                    "topic_order": 16,
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
                        block_id=f"g10_cs_t16_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={"topic_order": 16, "unit_order": u_order, "page": page_idx}
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
    print(f"TOPIC 16 INGESTION COMPLETE:")
    print(f"  Units Created:   {total_units}")
    print(f"  Lessons Created: {total_lessons}")
    print(f"  Pages Created:   {total_pages}")
    print(f"  Blocks Created:  {total_blocks}")
    print(f"  Assets Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_grade10_topic16(replace=True)
