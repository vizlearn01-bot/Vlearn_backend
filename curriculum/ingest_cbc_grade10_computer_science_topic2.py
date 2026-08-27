"""
VLearn CBC Grade 10 Computer Science — Topic 2: Computer Architecture
Production Ingestion & Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Computer Science
Topic: Computer Architecture (Topic Order: 2)

Decomposed into 2 Learning Units & 2 Published Lessons:
  1. Functional Organisation and the Von Neumann Model (Lesson 3: Functional Units and the Von Neumann Model)
  2. System Performance and Data Representation (Lesson 4: System Performance, Architectural Relationships, and Data Representation)
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
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    text = re.sub(r'^([^\n\-\*\d\>#][^\n]*)\n(- |\* )', r'\1\n\n\2', text, flags=re.MULTILINE)
    return text.strip()

def clean_dict(data):
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
# HIGH PRECISION VECTOR SVGS FOR TOPIC 2
# =====================================================================

SVG_VON_NEUMANN = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="510" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Von Neumann Computer Architecture &amp; System Buses</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">The unified stored-program model with CPU, shared memory, and the three dedicated communication highways</text>

  <!-- CPU Housing Box -->
  <rect x="280" y="95" width="400" height="230" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <rect x="290" y="105" width="380" height="26" rx="6" fill="#0284c7"/>
  <text x="480" y="123" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">CENTRAL PROCESSING UNIT (CPU)</text>

  <!-- Control Unit (CU) -->
  <rect x="300" y="145" width="360" height="70" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="480" y="170" font-size="13" font-weight="bold" fill="#fbbf24" text-anchor="middle">Control Unit (CU) — The Director</text>
  <text x="480" y="192" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Fetches instructions, decodes opcodes, generates clock timing &amp; control signals</text>

  <!-- ALU -->
  <rect x="300" y="235" width="360" height="75" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
  <text x="480" y="260" font-size="13" font-weight="bold" fill="#34d399" text-anchor="middle">Arithmetic Logic Unit (ALU) — The Calculator</text>
  <text x="480" y="282" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Arithmetic (+, -, *, /) and Boolean logic operations (AND, OR, NOT, &gt;, &lt;, =)</text>

  <!-- Input Unit -->
  <g transform="translate(40, 150)">
    <rect width="180" height="120" rx="10" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect width="180" height="26" rx="6" fill="#7c3aed"/>
    <text x="90" y="18" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Input Unit</text>
    <text x="15" y="48" font-size="10" font-weight="bold" fill="#a78bfa">Peripherals:</text>
    <text x="15" y="65" font-size="9.5" fill="#e2e8f0">Keyboard, Mouse, Scanner, Microphone, Sensors</text>
    <text x="15" y="95" font-size="9" fill="#94a3b8">Converts physical input to binary</text>
  </g>

  <!-- Output Unit -->
  <g transform="translate(740, 150)">
    <rect width="180" height="120" rx="10" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <rect width="180" height="26" rx="6" fill="#db2777"/>
    <text x="90" y="18" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Output Unit</text>
    <text x="15" y="48" font-size="10" font-weight="bold" fill="#f472b6">Peripherals:</text>
    <text x="15" y="65" font-size="9.5" fill="#e2e8f0">Monitor, Printer, Speakers, Actuators, Motors</text>
    <text x="15" y="95" font-size="9" fill="#94a3b8">Translates binary to human form</text>
  </g>

  <!-- Memory Unit (RAM) -->
  <g transform="translate(280, 420)">
    <rect width="400" height="85" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="400" height="24" rx="6" fill="#0284c7"/>
    <text x="200" y="17" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Primary Memory Unit (RAM) — Shared Workspace</text>
    <text x="200" y="45" font-size="10.5" fill="#e2e8f0" text-anchor="middle">Holds BOTH Program Instructions and Data Values in Shared Address Spaces</text>
    <text x="200" y="65" font-size="9.5" fill="#f87171" text-anchor="middle">Volatile: Cleared immediately when power is lost</text>
  </g>

  <!-- System Buses (Middle Layer) -->
  <!-- Control Bus -->
  <line x1="130" y1="350" x2="830" y2="350" stroke="#f59e0b" stroke-width="4" stroke-dasharray="6,4"/>
  <text x="80" y="345" font-size="10.5" font-weight="bold" fill="#fbbf24">Control Bus (Commands &amp; Timing)</text>

  <!-- Address Bus -->
  <line x1="130" y1="375" x2="830" y2="375" stroke="#ef4444" stroke-width="4"/>
  <text x="80" y="372" font-size="10.5" font-weight="bold" fill="#f87171">Address Bus (Uni-directional from CPU)</text>

  <!-- Data Bus -->
  <line x1="130" y1="400" x2="830" y2="400" stroke="#10b981" stroke-width="5"/>
  <text x="80" y="398" font-size="10.5" font-weight="bold" fill="#34d399">Data Bus (Bi-directional Data Flow)</text>
</svg>
""")

SVG_FDE_CYCLE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The CPU Instruction Cycle: Fetch, Decode, and Execute (F-D-E)</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">How internal special-purpose registers (PC, MAR, MDR, CIR, ACC) coordinate with memory</text>

  <!-- 3 Stages Columns -->
  <!-- 1. FETCH -->
  <g transform="translate(45, 95)">
    <rect width="265" height="380" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="265" height="28" rx="8" fill="#0284c7"/>
    <text x="132.5" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 1: FETCH</text>
    
    <rect x="15" y="45" width="235" height="60" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
    <text x="25" y="65" font-size="10" font-weight="bold" fill="#38bdf8">1. PC $\\rightarrow$ MAR</text>
    <text x="25" y="82" font-size="9" fill="#cbd5e1">Address in Program Counter (PC) copied to Memory Address Register (MAR).</text>

    <rect x="15" y="115" width="235" height="60" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
    <text x="25" y="135" font-size="10" font-weight="bold" fill="#38bdf8">2. Memory Read</text>
    <text x="25" y="152" font-size="9" fill="#cbd5e1">CU sends Read signal over Control Bus; RAM places data into MDR.</text>

    <rect x="15" y="185" width="235" height="60" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
    <text x="25" y="205" font-size="10" font-weight="bold" fill="#38bdf8">3. MDR $\\rightarrow$ CIR &amp; PC++</text>
    <text x="25" y="222" font-size="9" fill="#cbd5e1">Instruction moved to CIR. Program Counter increments ($PC = PC + 1$).</text>
    
    <rect x="15" y="260" width="235" height="100" rx="6" fill="#0284c7" opacity="0.2"/>
    <text x="132.5" y="285" font-size="10.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Registers Engaged:</text>
    <text x="25" y="310" font-size="9.5" fill="#e2e8f0">• Program Counter (PC)</text>
    <text x="25" y="328" font-size="9.5" fill="#e2e8f0">• Memory Address Register (MAR)</text>
    <text x="25" y="346" font-size="9.5" fill="#e2e8f0">• Memory Data Register (MDR)</text>
  </g>

  <!-- 2. DECODE -->
  <g transform="translate(345, 95)">
    <rect width="265" height="380" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="265" height="28" rx="8" fill="#d97706"/>
    <text x="132.5" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 2: DECODE</text>
    
    <rect x="15" y="45" width="235" height="90" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
    <text x="25" y="68" font-size="10.5" font-weight="bold" fill="#fbbf24">1. Inspect CIR Opcode</text>
    <text x="25" y="88" font-size="9" fill="#cbd5e1">Control Unit instruction decoder interprets the binary operation code (e.g. `ADD`, `LOAD`, `STORE`, `JUMP`).</text>

    <rect x="15" y="145" width="235" height="100" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
    <text x="25" y="168" font-size="10.5" font-weight="bold" fill="#fbbf24">2. Identify Operands</text>
    <text x="25" y="188" font-size="9" fill="#cbd5e1">The CU determines what data memory address or register is needed to supply values for the calculation.</text>

    <rect x="15" y="260" width="235" height="100" rx="6" fill="#d97706" opacity="0.2"/>
    <text x="132.5" y="285" font-size="10.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">Key Components Engaged:</text>
    <text x="25" y="310" font-size="9.5" fill="#e2e8f0">• Current Instruction Reg (CIR)</text>
    <text x="25" y="328" font-size="9.5" fill="#e2e8f0">• Instruction Decoder Circuit</text>
    <text x="25" y="346" font-size="9.5" fill="#e2e8f0">• Control Unit (CU) Timing Matrix</text>
  </g>

  <!-- 3. EXECUTE -->
  <g transform="translate(645, 95)">
    <rect width="270" height="380" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#059669"/>
    <text x="135" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 3: EXECUTE</text>
    
    <rect x="15" y="45" width="240" height="90" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="25" y="68" font-size="10.5" font-weight="bold" fill="#34d399">1. ALU Computation</text>
    <text x="25" y="88" font-size="9" fill="#cbd5e1">ALU performs the mathematical arithmetic or logical comparison requested by the decoded opcode.</text>

    <rect x="15" y="145" width="240" height="100" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="25" y="168" font-size="10.5" font-weight="bold" fill="#34d399">2. Save to Accumulator / RAM</text>
    <text x="25" y="188" font-size="9" fill="#cbd5e1">The calculated result is written to the Accumulator (ACC) or sent across the Data Bus to be saved into RAM.</text>

    <rect x="15" y="260" width="240" height="100" rx="6" fill="#059669" opacity="0.2"/>
    <text x="135" y="285" font-size="10.5" font-weight="bold" fill="#34d399" text-anchor="middle">Key Components Engaged:</text>
    <text x="25" y="310" font-size="9.5" fill="#e2e8f0">• Arithmetic Logic Unit (ALU)</text>
    <text x="25" y="328" font-size="9.5" fill="#e2e8f0">• Accumulator (ACC) Register</text>
    <text x="25" y="346" font-size="9.5" fill="#e2e8f0">• Status Flag Registers</text>
  </g>
</svg>
""")

SVG_MEMORY_HIERARCHY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Computer Memory Hierarchy: Speed vs. Capacity</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Balancing access latency, physical cost per byte, and total storage volume to prevent CPU bottlenecks</text>

  <!-- Pyramid Tiers -->
  <!-- Tier 1: Registers -->
  <polygon points="480,95 380,165 580,165" fill="#ef4444" opacity="0.9"/>
  <text x="480" y="135" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">CPU Registers</text>
  <text x="480" y="152" font-size="9.5" fill="#ffffff" text-anchor="middle">&lt; 1 ns | Bytes to KB</text>

  <!-- Tier 2: Cache L1/L2/L3 -->
  <polygon points="380,170 580,170 650,245 310,245" fill="#f59e0b" opacity="0.9"/>
  <text x="480" y="200" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">CPU Cache (L1, L2, L3 SRAM)</text>
  <text x="480" y="220" font-size="9.5" fill="#ffffff" text-anchor="middle">1 - 10 ns | Megabytes (MB)</text>

  <!-- Tier 3: Main Memory (RAM) -->
  <polygon points="310,250 650,250 730,335 230,335" fill="#10b981" opacity="0.9"/>
  <text x="480" y="285" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">Main Memory (System DRAM)</text>
  <text x="480" y="305" font-size="10" fill="#ffffff" text-anchor="middle">50 - 100 ns | Gigabytes (8GB - 64GB)</text>

  <!-- Tier 4: Secondary Storage (SSD/HDD) -->
  <polygon points="230,340 730,340 820,435 140,435" fill="#0ea5e9" opacity="0.9"/>
  <text x="480" y="380" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">Secondary Storage (NVMe SSD / HDD)</text>
  <text x="480" y="400" font-size="10" fill="#ffffff" text-anchor="middle">SSD: 10 - 100 µs | HDD: 5 - 15 ms | Terabytes (TB)</text>

  <!-- Left Side: Speed & Cost Arrow -->
  <line x1="110" y1="435" x2="110" y2="105" stroke="#f43f5e" stroke-width="4"/>
  <text x="100" y="270" font-size="12" font-weight="bold" fill="#fb7185" transform="rotate(-90 100,270)" text-anchor="middle">▲ SPEED &amp; COST PER BYTE INCREASE</text>

  <!-- Right Side: Capacity Arrow -->
  <line x1="850" y1="105" x2="850" y2="435" stroke="#38bdf8" stroke-width="4"/>
  <text x="865" y="270" font-size="12" font-weight="bold" fill="#38bdf8" transform="rotate(90 865,270)" text-anchor="middle">▲ STORAGE CAPACITY INCREASES</text>
</svg>
""")

SVG_BASE_CONVERSION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Positional Number Systems &amp; 4-Bit Nibble Grouping</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">How Binary (Base-2), Octal (Base-8), Decimal (Base-10), and Hexadecimal (Base-16) map together</text>

  <!-- 4 Base Cards -->
  <!-- Binary Base-2 -->
  <g transform="translate(40, 95)">
    <rect width="200" height="200" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="200" height="26" rx="6" fill="#059669"/>
    <text x="100" y="18" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Binary (Base-2)</text>
    <text x="15" y="45" font-size="10" font-weight="bold" fill="#34d399">Symbols: 0, 1</text>
    <text x="15" y="65" font-size="9.5" fill="#cbd5e1">Place Values: 2^n</text>
    <text x="15" y="85" font-size="9" fill="#94a3b8">128, 64, 32, 16, 8, 4, 2, 1</text>
    <text x="15" y="125" font-size="10" font-weight="bold" fill="#34d399">Why Used?</text>
    <text x="15" y="145" font-size="9" fill="#e2e8f0">Physical ON/OFF states of electronic silicon transistors.</text>
  </g>

  <!-- Octal Base-8 -->
  <g transform="translate(265, 95)">
    <rect width="200" height="200" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="200" height="26" rx="6" fill="#d97706"/>
    <text x="100" y="18" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Octal (Base-8)</text>
    <text x="15" y="45" font-size="10" font-weight="bold" fill="#fbbf24">Symbols: 0 to 7</text>
    <text x="15" y="65" font-size="9.5" fill="#cbd5e1">Place Values: 8^n</text>
    <text x="15" y="85" font-size="9" fill="#94a3b8">512, 64, 8, 1</text>
    <text x="15" y="125" font-size="10" font-weight="bold" fill="#fbbf24">Bit Grouping:</text>
    <text x="15" y="145" font-size="9" fill="#e2e8f0">Groups exactly 3 binary bits into a single character (e.g. 111_2 = 7_8).</text>
  </g>

  <!-- Decimal Base-10 -->
  <g transform="translate(490, 95)">
    <rect width="200" height="200" rx="8" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="200" height="26" rx="6" fill="#0284c7"/>
    <text x="100" y="18" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Decimal (Base-10)</text>
    <text x="15" y="45" font-size="10" font-weight="bold" fill="#38bdf8">Symbols: 0 to 9</text>
    <text x="15" y="65" font-size="9.5" fill="#cbd5e1">Place Values: 10^n</text>
    <text x="15" y="85" font-size="9" fill="#94a3b8">1000, 100, 10, 1</text>
    <text x="15" y="125" font-size="10" font-weight="bold" fill="#38bdf8">Human Standard:</text>
    <text x="15" y="145" font-size="9" fill="#e2e8f0">Standard natural counting system based on ten human fingers.</text>
  </g>

  <!-- Hexadecimal Base-16 -->
  <g transform="translate(715, 95)">
    <rect width="205" height="200" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="205" height="26" rx="6" fill="#9333ea"/>
    <text x="102.5" y="18" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Hexadecimal (Base-16)</text>
    <text x="15" y="45" font-size="10" font-weight="bold" fill="#c084fc">Symbols: 0-9, A-F</text>
    <text x="15" y="65" font-size="9.5" fill="#cbd5e1">A=10, B=11, C=12, D=13, E=14, F=15</text>
    <text x="15" y="85" font-size="9" fill="#94a3b8">4096, 256, 16, 1</text>
    <text x="15" y="125" font-size="10" font-weight="bold" fill="#c084fc">4-Bit Nibble Grouping:</text>
    <text x="15" y="145" font-size="9" fill="#e2e8f0">Compresses 4 binary bits into 1 hex digit (e.g. 1111_2 = F_16).</text>
  </g>

  <!-- Bottom Panel: 8-Bit Byte Nibble Decomposition -->
  <g transform="translate(40, 315)">
    <rect width="880" height="170" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="440" y="28" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">Example: Decomposing an 8-Bit Byte (11110010_2) into Hexadecimal</text>
    
    <!-- Left Nibble -->
    <rect x="180" y="50" width="240" height="95" rx="6" fill="#1e293b" stroke="#a855f7" stroke-width="1"/>
    <text x="300" y="72" font-size="11" font-weight="bold" fill="#c084fc" text-anchor="middle">Upper Nibble: [1 1 1 1]</text>
    <text x="300" y="95" font-size="10" fill="#e2e8f0" text-anchor="middle">8 + 4 + 2 + 1 = 15</text>
    <text x="300" y="125" font-size="16" font-weight="bold" fill="#c084fc" text-anchor="middle">F (Base-16)</text>
    
    <!-- Right Nibble -->
    <rect x="460" y="50" width="240" height="95" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="580" y="72" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">Lower Nibble: [0 0 1 0]</text>
    <text x="580" y="95" font-size="10" fill="#e2e8f0" text-anchor="middle">0 + 0 + 2 + 0 = 2</text>
    <text x="580" y="125" font-size="16" font-weight="bold" fill="#34d399" text-anchor="middle">2 (Base-16)</text>
    
    <text x="760" y="105" font-size="14" font-weight="bold" fill="#38bdf8">= F2 (Hex)</text>
  </g>
</svg>
""")

# =====================================================================
# LESSON DATA SPECIFICATION: TOPIC 2
# =====================================================================

def build_topic2_curriculum():
    return [
        # -------------------------------------------------------------
        # LESSON 3: Functional Units and the Von Neumann Model
        # -------------------------------------------------------------
        {
            "unit_order": 1,
            "unit_name": "Functional Organisation and the Von Neumann Model",
            "unit_description": "The information processing cycle, the stored-program concept, the CPU (ALU and Control Unit), main memory, and system bus pathways (Data, Address, Control).",
            "lesson_title": "Functional Units and the Von Neumann Model",
            "pages": [
                # Card 1: Hook & Goals
                [
                    {
                        "type": "suggested_image",
                        "title": "Modern Multi-Core Desktop Processor & Socket Layout",
                        "content": {
                            "title": "Modern Multi-Core Desktop Processor & Socket Layout",
                            "caption": "A modern Intel Core processor featuring integrated ALU execution cores, caches, and memory controllers, ready to seat into a motherboard socket.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Intel_Core_i7-2600K_top.jpg/800px-Intel_Core_i7-2600K_top.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Computer Architecture",
                        "content": {
                            "title": "What We Will Master in This Lesson",
                            "goals": [
                                "Define **computer architecture**, the **Information Processing Cycle**, and the **Stored-Program Concept**.",
                                "Analyze the distinct functions of the **Arithmetic Logic Unit (ALU)** and **Control Unit (CU)** inside the CPU.",
                                "Deconstruct the **System Bus** into its three dedicated pathways: **Data Bus**, **Address Bus**, and **Control Bus**.",
                                "Trace the internal data flow of an arithmetic calculation ($5 + 3$) through registers, buses, and memory."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Real-World Hook: The Restaurant Kitchen Analogy",
                        "content": {
                            "title": "The Information Processing Cycle in Daily Life",
                            "text": "Think of what happens when you visit a restaurant:\n1. **Input**: You read the menu and state your order to the cashier.\n2. **Storage**: The cashier enters the order into the queue monitor (storing the request).\n3. **Processing**: The chef reads the ticket, gathers ingredients, cooks, and plates the food.\n4. **Output**: The server calls your number and delivers your hot meal.\n\nEvery computer system operates on this exact same **Information Processing Cycle**: **Input $\\rightarrow$ Storage $\\rightarrow$ Processing $\\rightarrow$ Output**!"
                        }
                    }
                ],
                # Card 2: The Stored-Program Concept & CPU Anatomy
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Stored-Program Revolution (John von Neumann, 1945)",
                        "content": {
                            "title": "Why Modern Computers Can Switch Tasks Instantly",
                            "text": "Before 1945, early computers like the ENIAC had fixed hardware circuits. To change what a computer did, engineers spent days physically re-wiring thousands of patch cables.\n\nMathematician **John von Neumann** introduced a radical breakthrough: **The Stored-Program Concept**.\n- Instead of re-wiring hardware, store the program instructions (the recipe) in the exact same electronic memory unit as the data (the ingredients).\n- To change tasks, simply load a new set of instructions into memory!\n\n### The Anatomy of the CPU\n- **Arithmetic Logic Unit (ALU)**: The computational worker. Executes mathematical operations ($+, -, \\times, \\div$) and Boolean comparisons ($=, <, >, \\text{AND}, \\text{OR}, \\text{NOT}$).\n- **Control Unit (CU)**: The supervisor. Fetches instructions from memory, decodes what operation is required, synchronizes the internal clock, and directs electrical signals across the system buses."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Von Neumann Architecture & System Bus Blueprint",
                        "content": {
                            "svg_content": SVG_VON_NEUMANN,
                            "caption": "The von Neumann architecture showing the CPU (ALU and CU), Memory Unit (RAM), Input/Output units, and the three dedicated communication buses."
                        }
                    }
                ],
                # Card 3: The System Buses (Data, Address, Control)
                [
                    {
                        "type": "comparison_table",
                        "title": "The Three System Buses: Functions and Directionality",
                        "content": {
                            "headers": ["Bus Name", "Directionality", "Signals Carried", "Key Purpose & Real-World Analogy"],
                            "rows": [
                                ["**Data Bus**", "Bi-directional (Two-way)", "Binary data values, characters, pixels, operands", "Transports actual payload data between CPU, RAM, and peripherals. Like a two-way delivery highway."],
                                ["**Address Bus**", "Uni-directional (CPU $\\rightarrow$ Memory/Peripherals)", "Binary memory addresses (coordinates)", "Specifies which exact memory cell or peripheral the CPU wants to read from or write to. Like a GPS coordinate pointer."],
                                ["**Control Bus**", "Uni-directional (CU $\\rightarrow$ System)", "Clock pulses, Read/Write commands, Interrupts", "Transmits synchronization timing signals and command instructions (e.g., 'MEMORY READ', 'WRITE TO PRINTER'). Like traffic police whistles."]
                            ]
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "CPU Register Level Fetch-Decode-Execute Cycle",
                        "content": {
                            "svg_content": SVG_FDE_CYCLE,
                            "caption": "Instruction Cycle showing the role of internal special registers (Program Counter, MAR, MDR, CIR, and Accumulator) during Fetch, Decode, and Execute stages."
                        }
                    }
                ],
                # Card 4: Step-by-Step Data Flow Trace ($5 + 3$)
                [
                    {
                        "type": "step_process",
                        "title": "Data Flow Trace: Executing 5 + 3 Inside the Von Neumann Architecture",
                        "content": {
                            "title": "Step-by-Step Instruction Execution Trace",
                            "steps": [
                                "**1. Input & Storage**: The user presses '5', '+', and '3'. The input driver converts keystrokes into binary and transfers them over the Data Bus to be stored at memory addresses in RAM.",
                                "**2. Fetch Instruction**: The Control Unit places the address of the next program instruction on the Address Bus and issues a 'MEMORY READ' command over the Control Bus. RAM sends the 'ADD' instruction back over the Data Bus to the CPU's Instruction Register.",
                                "**3. Decode**: The CU decodes the ADD opcode and determines it must retrieve two operand values from memory addresses `0x10` and `0x11`.",
                                "**4. Fetch Operands**: The CU places address `0x10` on the Address Bus to read value $5$, then address `0x11` to read value $3$ into internal CPU registers.",
                                "**5. ALU Execution**: The CU directs the ALU to add the values. The ALU performs the addition and outputs the result $8$.",
                                "**6. Store Result**: The CU writes the result $8$ over the Data Bus to address `0x12` in RAM.",
                                "**7. Output**: The CU routes the value $8$ to the display controller, lighting up pixels on the monitor to display '8'."
                            ]
                        }
                    }
                ],
                # Card 5: Memory Volatility & The RAM Workspace
                [
                    {
                        "type": "concept_explanation",
                        "title": "Primary Memory Volatility vs Permanent Storage",
                        "content": {
                            "title": "Why RAM Disappears When Power Fails",
                            "text": "Main memory (RAM) is the CPU's direct electronic workspace. It provides near-instantaneous read and write access to running code.\n\n- **Volatile Nature**: RAM requires a continuous electrical current to maintain the binary charge in its microscopic capacitors and transistors. If the electrical power cuts off for even a millisecond, all active data in RAM is instantly and permanently lost!\n- **The Non-Volatile Solution**: Secondary storage (SSDs, Hard Drives) uses magnetic or non-volatile flash traps that retain files permanently without electrical power. This is why you must periodically click 'Save' to transfer your essay from volatile RAM to permanent storage!"
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Modern Motherboard & DDR RAM Memory Modules",
                        "content": {
                            "title": "Modern Motherboard & DDR RAM Memory Modules",
                            "caption": "Dual-channel high-speed DDR RAM modules seated on a computer motherboard adjacent to the CPU socket, connected via high-speed system bus traces.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Swissbit_2GB_PC2-6400_DDR2_RAM.jpg/800px-Swissbit_2GB_PC2-6400_DDR2_RAM.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    }
                ],
                # Card 6: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Inside the CPU: Clock Cycles, Buses, and the ALU",
                        "content": {
                            "title": "How a CPU Actually Works",
                            "youtube_id": "cNN_tTXABUA",
                            "url": "https://www.youtube.com/watch?v=cNN_tTXABUA",
                            "description": "An exceptional visual journey inside the computer CPU, illustrating how registers, system buses, and logic gates execute instructions during the fetch-decode-execute cycle."
                        }
                    }
                ],
                # Card 7: Hands-on Modeling Activity
                [
                    {
                        "type": "mini_activity",
                        "title": "Hands-On Modeling: Build a Cardboard & String Von Neumann Computer",
                        "content": {
                            "title": "Physical Computer Simulation",
                            "text": "Work in small groups to build a physical tabletop model of a computer:\n1. **Cardboard Modules**: Label separate boxes as 'Keyboard', 'Control Unit', 'ALU', 'RAM Memory', and 'Monitor'.\n2. **Bus Pathways**: Use three distinct colors of yarn to connect the boxes:\n   - **Green Yarn**: Data Bus (bi-directional between all components).\n   - **Red Yarn**: Address Bus (starts strictly at CPU and points to RAM/Output).\n   - **Yellow Yarn**: Control Bus (emanates from CU to coordinate components).\n3. **Execution Run**: Use Post-It notes with numbers to physically pass values along the green string according to the teacher's clock signals!"
                        }
                    }
                ],
                # Card 8: Formative Knowledge Checks & Key Takeaways
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 1: Control Unit Function",
                        "content": {
                            "question": "Which component of the Central Processing Unit is responsible for retrieving instructions from memory and coordinating all system operations?",
                            "options": [
                                "The Arithmetic Logic Unit (ALU)",
                                "The Control Unit (CU)",
                                "The Solid-State Drive",
                                "The Video Display Adapter"
                            ],
                            "correct": "B",
                            "explanation": "The Control Unit (CU) acts as the supervisor of the CPU, fetching instructions, decoding them, and issuing timing/control signals across the system."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 2: The Stored-Program Concept",
                        "content": {
                            "question": "What is the defining principle of the John von Neumann 'stored-program' architecture?",
                            "options": [
                                "Every program must be hardwired into circuits with physical switches",
                                "Program instructions and operational data are stored together in a single shared memory workspace",
                                "Data must only be saved onto external optical discs",
                                "Input devices must execute arithmetic directly without a CPU"
                            ],
                            "correct": "B",
                            "explanation": "The stored-program concept revolutionized computing by holding both executable code instructions and active data variables in the same addressable memory unit."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 3: Address Bus Directionality",
                        "content": {
                            "question": "Why is the Address Bus uni-directional, flowing only outward from the CPU?",
                            "options": [
                                "Because data is too heavy to travel backwards",
                                "Because only the CPU determines which memory cell address or peripheral to access",
                                "To prevent monitor pixels from overheating the memory",
                                "Because primary RAM is volatile"
                            ],
                            "correct": "B",
                            "explanation": "The CPU alone decides which memory location or I/O device to read or write, so memory addresses are only transmitted out from the CPU to the system."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Lesson 3 Key Takeaways",
                        "content": {
                            "text": "1. **Information Processing Cycle**: Input $\\rightarrow$ Storage $\\rightarrow$ Processing $\\rightarrow$ Output.\n2. **Stored-Program Concept**: Instructions and data reside together in shared addressable RAM.\n3. **CPU Core Units**: ALU performs math/logic; CU decodes instructions and directs execution.\n4. **System Buses**: Data Bus (bi-directional data), Address Bus (uni-directional coordinates), Control Bus (commands/clock timing).\n5. **Memory Volatility**: RAM loses all stored data instantly when electrical power is disconnected."
                        }
                    }
                ]
            ]
        },

        # -------------------------------------------------------------
        # LESSON 4: System Performance and Data Representation
        # -------------------------------------------------------------
        {
            "unit_order": 2,
            "unit_name": "System Performance and Data Representation",
            "unit_description": "System performance bottlenecks, memory hierarchy (registers, cache, RAM, secondary storage), and data representation across positional base systems (Binary, Octal, Decimal, Hexadecimal).",
            "lesson_title": "System Performance, Architectural Relationships, and Data Representation",
            "pages": [
                # Card 1: Hook & Goals
                [
                    {
                        "type": "suggested_image",
                        "title": "Silicon Microprocessor Die & Integrated Circuit Architecture",
                        "content": {
                            "title": "Silicon Microprocessor Die & Integrated Circuit Architecture",
                            "caption": "A high-magnification photograph of a modern microprocessor silicon die, showing execution cores, caches, and memory bus interconnects.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/KL_Intel_i7_8700K_die_image.jpg/800px-KL_Intel_i7_8700K_die_image.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Performance & Number Systems",
                        "content": {
                            "title": "What We Will Master in This Lesson",
                            "goals": [
                                "Define **system performance** and explain the concept of a **hardware bottleneck**.",
                                "Analyze the **Memory Hierarchy Pyramid** (Registers $\\rightarrow$ Cache $\\rightarrow$ RAM $\\rightarrow$ Secondary Storage) in terms of latency, cost, and capacity.",
                                "Explain why computers use **binary (Base-2)** representations internally.",
                                "Perform multi-base conversions between **Decimal (Base-10)**, **Binary (Base-2)**, and **Hexadecimal (Base-16)**.",
                                "Apply binary telemetry packet decoding to embedded IoT scenarios."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Real-World Hook: The Highway Bottleneck",
                        "content": {
                            "title": "Why Fast CPUs Sometimes Feel Slow",
                            "text": "Have you ever traveled on a modern 4-lane highway at 100 km/h, only to grind to a complete halt because road construction narrowed the road into a single lane?\n\nNo matter how powerful your car's engine is, your overall travel speed is completely constrained by that single narrow lane. In computer science, this is known as a **Bottleneck**.\n\nYou can purchase the fastest 16-core CPU in the world, but if your memory bus is narrow or your hard drive is slow, your CPU will sit idle waiting for data, causing sluggish performance!"
                        }
                    }
                ],
                # Card 2: The Memory Hierarchy Pyramid
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Memory Hierarchy: Speed, Cost, and Capacity",
                        "content": {
                            "title": "The Trade-Offs of Digital Storage",
                            "text": "Computer architects organize storage into a tiered hierarchy to balance speed against cost:\n\n1. **CPU Registers**: The fastest memory in existence (under 1 nanosecond access time). Located directly inside the ALU/CU execution cores. Holds only a few bytes (e.g. accumulator).\n2. **Cache Memory (L1, L2, L3)**: High-speed static RAM (SRAM) fabricated onto the CPU die. Holds frequently used code blocks to eliminate RAM access delays.\n3. **Main Memory (System RAM)**: Dynamic RAM (DRAM) holding gigabytes of active operating system files and apps. Slower (50–100 ns) but affordable.\n4. **Secondary Storage (SSDs & Hard Drives)**: Permanent, non-volatile storage holding terabytes. Thousands of times slower to access than RAM, but retains files indefinitely without power."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "The Computer Memory Hierarchy Pyramid",
                        "content": {
                            "svg_content": SVG_MEMORY_HIERARCHY,
                            "caption": "The Memory Hierarchy Pyramid illustrating the inverse relationship between access speed / cost per byte and total storage capacity."
                        }
                    }
                ],
                # Card 3: Cache Memory & Latency Elimination
                [
                    {
                        "type": "concept_explanation",
                        "title": "Why Cache Memory Prevents the 'Von Neumann Bottleneck'",
                        "content": {
                            "title": "Bridging the CPU-Memory Speed Gap",
                            "text": "CPUs execute billions of cycles per second (GHz), but standard RAM responds in tens of nanoseconds. Without cache, a modern processor would spend 80% of its time idling, waiting for data to crawl across the system bus.\n\n- **Cache Hit**: When the CPU finds the requested data already waiting in high-speed L1/L2 cache, executing without any delay.\n- **Cache Miss**: When data is not in cache, forcing the CPU to pause and fetch it from slower main RAM.\n- Modern processors achieve cache hit rates over 95%, keeping execution pipelines fully loaded."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Hexadecimal Raw Memory Dump in Low-Level Debugging",
                        "content": {
                            "title": "Hexadecimal Raw Memory Dump in Low-Level Debugging",
                            "caption": "A memory hex dump display. Engineers and programmers use hexadecimal (Base-16) notation to compactly represent raw binary machine bytes in addressable memory.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Hex_dump.png/800px-Hex_dump.png",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    }
                ],
                # Card 4: Data Representation — Why Binary?
                [
                    {
                        "type": "concept_explanation",
                        "title": "Positional Number Systems in Computing",
                        "content": {
                            "title": "Why Computers Count in Base-2 (Binary)",
                            "text": "Computers do not understand human base-10 digits. Inside silicon chips, transistors are physical electronic switches that can only be in one of two states:\n- **Voltage Present (High / ON)** $\\longrightarrow 1$\n- **Zero Voltage (Low / OFF)** $\\longrightarrow 0$\n\nTo make long strings of binary readable for humans, computer scientists use **Hexadecimal (Base-16)** and **Octal (Base-8)** as compact shorthand notation:\n\n### The Four Standard Positional Bases\n1. **Binary (Base-2)**: Digits `0, 1`. Place values: $2^0=1, 2^1=2, 2^2=4, 2^3=8, 2^4=16, 2^5=32, \\dots$\n2. **Octal (Base-8)**: Digits `0, 1, 2, 3, 4, 5, 6, 7`. Groups binary bits into sets of 3.\n3. **Decimal (Base-10)**: Digits `0, 1, 2, 3, 4, 5, 6, 7, 8, 9`. Standard human counting.\n4. **Hexadecimal (Base-16)**: Digits `0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F`.\n   - *Letter Equivalents*: $A=10, B=11, C=12, D=13, E=14, F=15$."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Positional Number Systems & 4-Bit Nibble Grouping Visualizer",
                        "content": {
                            "svg_content": SVG_BASE_CONVERSION,
                            "caption": "Mapping of Binary (Base-2), Octal (Base-8), Decimal (Base-10), and Hexadecimal (Base-16) showing 4-bit nibble grouping."
                        }
                    }
                ],
                # Card 5: Conversion Mastery 1 — Decimal to Binary
                [
                    {
                        "type": "worked_example",
                        "title": "Conversion Walkthrough 1: Decimal to Binary & Binary to Decimal",
                        "content": {
                            "title": "Step-by-Step Conversion Algorithms",
                            "problem": "Convert decimal $37_{10}$ to binary, then verify by converting the binary result back to decimal.",
                            "steps": [
                                "**Step 1 (Repeated Division by 2)**:\n- $37 \\div 2 = 18$ with remainder **1** (LSB)\n- $18 \\div 2 = 9$ with remainder **0**\n- $9 \\div 2 = 4$ with remainder **1**\n- $4 \\div 2 = 2$ with remainder **0**\n- $2 \\div 2 = 1$ with remainder **0**\n- $1 \\div 2 = 0$ with remainder **1** (MSB)",
                                "**Step 2 (Read Remainders Bottom-to-Top)**: The binary equivalent is **$100101_2$**.",
                                "**Step 3 (Verify: Binary to Decimal Positional Sum)**:\n$$\\begin{aligned} 100101_2 &= (1 \\times 2^5) + (0 \\times 2^4) + (0 \\times 2^3) + (1 \\times 2^2) + (0 \\times 2^1) + (1 \\times 2^0) \\\\ &= 32 + 0 + 0 + 4 + 0 + 1 = 37_{10} \\end{aligned}$$"
                            ]
                        }
                    }
                ],
                # Card 6: Conversion Mastery 2 — Hexadecimal
                [
                    {
                        "type": "worked_example",
                        "title": "Conversion Walkthrough 2: Hexadecimal and Binary 4-Bit Nibbles",
                        "content": {
                            "title": "The Power of Hexadecimal Shorthand",
                            "problem": "Convert hexadecimal $1F_{16}$ to decimal, and convert binary $11110010_2$ to hexadecimal.",
                            "steps": [
                                "**Part A: Hexadecimal $1F_{16}$ to Decimal**:\n- $F$ corresponds to decimal $15$.\n- $\\text{Value} = (1 \\times 16^1) + (15 \\times 16^0) = 16 + 15 = 31_{10}$.",
                                "**Part B: Binary $11110010_2$ to Hexadecimal (4-Bit Grouping)**:\n- Split binary digits into groups of 4 from right to left: `[1111] [0010]`.\n- Right Nibble: $0010_2 = (0\\times8) + (0\\times4) + (1\\times2) + (0\\times1) = 2_{16}$.\n- Left Nibble: $1111_2 = (1\\times8) + (1\\times4) + (1\\times2) + (1\\times1) = 15 = F_{16}$.\n- Combine nibbles: **$F2_{16}$**."
                            ]
                        }
                    }
                ],
                # Card 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "How Computers Process Binary and Hexadecimal",
                        "content": {
                            "title": "Binary and Hexadecimal Number Systems Explained",
                            "youtube_id": "LpuPe81bc2w",
                            "url": "https://www.youtube.com/watch?v=LpuPe81bc2w",
                            "description": "A clear, comprehensive visual tutorial showing how binary bits map to electronic logic and how programmers use hexadecimal shorthand."
                        }
                    }
                ],
                # Card 8: Interactive Practice & Telemetry Trace
                [
                    {
                        "type": "worked_example",
                        "title": "Applied IoT Telemetry: Decoding Smart Irrigation Sensor Data",
                        "content": {
                            "title": "Decoding 8-Bit Embedded Microcontroller Packets",
                            "problem": "An automated agricultural soil moisture sensor in Machakos transmits its reading as an 8-bit binary packet: $11001101_2$. An automated irrigation valve opens if the soil dryness exceeds decimal value $200_{10}$.",
                            "steps": [
                                "**Step 1: Calculate Decimal Value of Telemetry Packet**:\n$$\\begin{aligned} 11001101_2 &= 128 + 64 + 0 + 0 + 8 + 4 + 0 + 1 \\\\ &= 205_{10} \\end{aligned}$$",
                                "**Step 2: Convert to Hexadecimal for Diagnostic Screen Display**:\n- Left 4 bits: $1100_2 = 8 + 4 = 12 = C_{16}$\n- Right 4 bits: $1101_2 = 8 + 4 + 1 = 13 = D_{16}$\n- Diagnostic Display: **$CD_{16}$**.",
                                "**Step 3: Threshold Decision Logic**:\n- Sensor Value ($205_{10}$) &gt; Threshold ($200_{10}$).\n- **Outcome**: The microcontroller triggers an actuator signal to open the irrigation valve!"
                            ]
                        }
                    }
                ],
                # Card 9: Formative Knowledge Checks & Key Takeaways
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 1: Hardware Bottlenecks",
                        "content": {
                            "question": "Which of the following best describes a computer system performance bottleneck?",
                            "options": [
                                "A high-capacity power supply that runs cool",
                                "A component that limits overall system speed because it operates significantly slower than others",
                                "An operating system utility that compresses files",
                                "A keyboard with mechanical switches"
                            ],
                            "correct": "B",
                            "explanation": "A bottleneck occurs when a slower component (like a mechanical hard drive or narrow memory bus) forces faster components (like the CPU) to pause and idle."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 2: Memory Speed Hierarchy",
                        "content": {
                            "question": "What is the correct order of computer memory from fastest access speed to slowest?",
                            "options": [
                                "Solid-State Drive $\\rightarrow$ Main RAM $\\rightarrow$ Cache $\\rightarrow$ CPU Registers",
                                "CPU Registers $\\rightarrow$ Cache Memory $\\rightarrow$ Main RAM $\\rightarrow$ Solid-State Drive",
                                "Main RAM $\\rightarrow$ CPU Registers $\\rightarrow$ Cache $\\rightarrow$ Hard Disk Drive",
                                "Cache Memory $\\rightarrow$ Main RAM $\\rightarrow$ CPU Registers $\\rightarrow$ NVMe SSD"
                            ],
                            "correct": "B",
                            "explanation": "Registers inside the CPU execute in under 1 ns, Cache SRAM takes 1-10 ns, Main RAM takes 50-100 ns, and secondary SSDs take 10-100 microseconds."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 3: Hexadecimal Symbols",
                        "content": {
                            "question": "In the hexadecimal (Base-16) number system, what decimal value is represented by the letter 'C'?",
                            "options": [
                                "10",
                                "11",
                                "12",
                                "13"
                            ],
                            "correct": "C",
                            "explanation": "In hexadecimal: A=10, B=11, C=12, D=13, E=14, F=15."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Lesson 4 Key Takeaways",
                        "content": {
                            "text": "1. **System Bottleneck**: The slowest link in the hardware chain dictates overall performance.\n2. **Memory Hierarchy**: Registers (fastest, smallest) $\\rightarrow$ Cache $\\rightarrow$ RAM $\\rightarrow$ Secondary Storage (slowest, largest).\n3. **Binary Nature**: Transistors operate as physical 2-state switches ($1 = \\text{ON}, 0 = \\text{OFF}$).\n4. **Hexadecimal Power**: Groups 4 binary bits into a single compact character ($0-9, A-F$), making addresses and byte data readable for humans."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_grade10_topic2(replace=True):
    print("=" * 80)
    print("INGESTING TOPIC 2: Computer Architecture (Grade 10 Computer Science)")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="CBC").first() or Curriculum.objects.filter(id=5).first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 10").first() or Grade.objects.filter(curriculum=curriculum, level=10).first()

    subject, _ = Subject.objects.get_or_create(
        grade=grade,
        name="Computer Science",
        defaults={"description": "Senior Secondary Computer Science Curriculum (Grade 10 CBC)"}
    )

    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=2,
        defaults={"name": "Computer Architecture", "description": "Functional organization, von Neumann model, system buses, performance, and data representation."}
    )
    if not t_created:
        topic.name = "Computer Architecture"
        topic.description = "Functional organization, von Neumann model, system buses, performance, and data representation."
        topic.save()
    print(f"[*] Resolved Topic 2: {topic.name} (ID: {topic.id})")

    if replace:
        print("[*] Replacing existing Topic 2 units, lessons, blocks, and assets...")
        existing_lessons = Lesson.objects.filter(topic=topic)
        LessonAsset.objects.filter(lesson__in=existing_lessons).delete()
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    curriculum_data = build_topic2_curriculum()
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
                    "topic_order": 2,
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
                        block_id=f"g10_cs_t2_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={"topic_order": 2, "unit_order": u_order, "page": page_idx}
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
    print(f"TOPIC 2 INGESTION COMPLETE:")
    print(f"  Units Created:   {total_units}")
    print(f"  Lessons Created: {total_lessons}")
    print(f"  Pages Created:   {total_pages}")
    print(f"  Blocks Created:  {total_blocks}")
    print(f"  Assets Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_grade10_topic2(replace=True)
