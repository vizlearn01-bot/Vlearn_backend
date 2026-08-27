"""
VLearn CBC Grade 10 Computer Science — Topic 5: Central Processing Unit (CPU)
Production Ingestion & Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Computer Science
Topic: Central Processing Unit (CPU) (Topic Order: 5)

Decomposed into 2 Learning Units & 2 Published Lessons:
  1. CPU Components and the Fetch–Decode–Execute Cycle (Lesson 9: CPU Components and the Fetch–Decode–Execute Cycle)
  2. CPU Performance and Types of Processing (Lesson 10: CPU Performance and Types of Processing)
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
    # Strip citation brackets like [24], [30, 31], [8]
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    # Convert bullets to standardized dashes
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
# HIGH PRECISION VECTOR SVGS FOR TOPIC 5
# =====================================================================

SVG_CPU_ARCHITECTURE_BLOCK = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 560" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="530" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Central Processing Unit (CPU) Internal Architecture</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Control Unit, Arithmetic Logic Unit, Internal Registers &amp; Motherboard System Buses</text>

  <!-- CPU Chip Outer Frame -->
  <g transform="translate(50, 90)">
    <rect width="540" height="430" rx="14" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect width="540" height="32" rx="10" fill="#0284c7"/>
    <text x="270" y="21" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">CPU CHIP (Processor Die)</text>

    <!-- Control Unit (CU) -->
    <rect x="30" y="50" width="220" height="110" rx="10" fill="#1e293b" stroke="#818cf8" stroke-width="1.5"/>
    <text x="140" y="75" font-size="13" font-weight="bold" fill="#a5b4fc" text-anchor="middle">Control Unit (CU)</text>
    <text x="140" y="95" font-size="10" fill="#cbd5e1" text-anchor="middle">• Fetches &amp; decodes code</text>
    <text x="140" y="112" font-size="10" fill="#cbd5e1" text-anchor="middle">• Issues timing &amp; control pulses</text>
    <text x="140" y="129" font-size="10" fill="#cbd5e1" text-anchor="middle">• Directs data flow</text>
    <text x="140" y="146" font-size="9" font-style="italic" fill="#94a3b8" text-anchor="middle">"The Nervous System"</text>

    <!-- Bidirectional Internal Bus between CU & ALU -->
    <line x1="250" y1="105" x2="290" y2="105" stroke="#f59e0b" stroke-width="3" stroke-dasharray="4"/>
    <polygon points="253,101 245,105 253,109" fill="#f59e0b"/>
    <polygon points="287,101 295,105 287,109" fill="#f59e0b"/>

    <!-- Arithmetic Logic Unit (ALU) -->
    <rect x="290" y="50" width="220" height="110" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="400" y="75" font-size="13" font-weight="bold" fill="#6ee7b7" text-anchor="middle">Arithmetic Logic Unit (ALU)</text>
    <text x="400" y="95" font-size="10" fill="#cbd5e1" text-anchor="middle">• Math: Addition, Subtraction</text>
    <text x="400" y="112" font-size="10" fill="#cbd5e1" text-anchor="middle">• Logic: AND, OR, NOT</text>
    <text x="400" y="129" font-size="10" fill="#cbd5e1" text-anchor="middle">• Relational comparisons (&gt;, &lt;, =)</text>
    <text x="400" y="146" font-size="9" font-style="italic" fill="#94a3b8" text-anchor="middle">"The Calculator Muscle"</text>

    <!-- Internal Buses Link to Registers -->
    <line x1="140" y1="160" x2="140" y2="195" stroke="#818cf8" stroke-width="2"/>
    <polygon points="136,190 140,198 144,190" fill="#818cf8"/>
    <line x1="400" y1="160" x2="400" y2="195" stroke="#34d399" stroke-width="2"/>
    <polygon points="396,190 400,198 404,190" fill="#34d399"/>

    <!-- CPU Dedicated Registers Container -->
    <rect x="25" y="200" width="490" height="210" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="25" y="200" width="490" height="26" rx="8" fill="#d97706"/>
    <text x="270" y="218" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">HIGH-SPEED INTERNAL CPU REGISTERS</text>

    <!-- Register Badges Grid -->
    <!-- PC -->
    <rect x="40" y="235" width="215" height="42" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <text x="50" y="253" font-size="10.5" font-weight="bold" fill="#38bdf8">PC (Program Counter)</text>
    <text x="50" y="268" font-size="9" fill="#94a3b8">Holds address of NEXT instruction</text>

    <!-- IR -->
    <rect x="285" y="235" width="215" height="42" rx="6" fill="#0f172a" stroke="#818cf8" stroke-width="1"/>
    <text x="295" y="253" font-size="10.5" font-weight="bold" fill="#a5b4fc">IR (Instruction Register)</text>
    <text x="295" y="268" font-size="9" fill="#94a3b8">Holds CURRENT instruction being decoded</text>

    <!-- MAR -->
    <rect x="40" y="285" width="215" height="42" rx="6" fill="#0f172a" stroke="#f43f5e" stroke-width="1"/>
    <text x="50" y="303" font-size="10.5" font-weight="bold" fill="#fb7185">MAR (Memory Address Reg)</text>
    <text x="50" y="318" font-size="9" fill="#94a3b8">RAM memory address to read/write</text>

    <!-- MDR -->
    <rect x="285" y="285" width="215" height="42" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
    <text x="295" y="303" font-size="10.5" font-weight="bold" fill="#34d399">MDR (Memory Data Reg)</text>
    <text x="295" y="318" font-size="9" fill="#94a3b8">Data copied from or waiting for RAM</text>

    <!-- ACC -->
    <rect x="140" y="335" width="260" height="42" rx="6" fill="#0f172a" stroke="#fbbf24" stroke-width="1.2"/>
    <text x="270" y="353" font-size="10.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">ACC (Accumulator)</text>
    <text x="270" y="368" font-size="9" fill="#cbd5e1" text-anchor="middle">Stores intermediate ALU math/logic results</text>
  </g>

  <!-- Motherboard System Buses (Right Side) -->
  <g transform="translate(620, 90)">
    <!-- RAM Box -->
    <rect x="160" y="40" width="140" height="380" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <rect x="160" y="40" width="140" height="30" rx="8" fill="#059669"/>
    <text x="230" y="60" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">SYSTEM RAM</text>
    <text x="230" y="95" font-size="10" fill="#94a3b8" text-anchor="middle">Primary Memory</text>
    <text x="230" y="115" font-size="9" fill="#64748b" text-anchor="middle">[0x000] Inst 1</text>
    <text x="230" y="135" font-size="9" fill="#64748b" text-anchor="middle">[0x001] Inst 2</text>
    <text x="230" y="155" font-size="9" fill="#64748b" text-anchor="middle">[0x002] Inst 3</text>
    <text x="230" y="180" font-size="9" fill="#38bdf8" text-anchor="middle">-----------------</text>
    <text x="230" y="205" font-size="9" fill="#64748b" text-anchor="middle">[0x150] Data: 5</text>
    <text x="230" y="225" font-size="9" fill="#64748b" text-anchor="middle">[0x151] Data: 3</text>
    <text x="230" y="245" font-size="9" fill="#64748b" text-anchor="middle">[0x152] Output: ?</text>
    <text x="230" y="380" font-size="9.5" fill="#34d399" text-anchor="middle">Volatile Storage</text>

    <!-- Address Bus (Unidirectional: CPU -> RAM) -->
    <path d="M -30,120 L 160,120" stroke="#fb7185" stroke-width="4"/>
    <polygon points="152,114 162,120 152,126" fill="#fb7185"/>
    <rect x="0" y="95" width="130" height="22" rx="4" fill="#1e293b" stroke="#fb7185" stroke-width="1"/>
    <text x="65" y="110" font-size="9.5" font-weight="bold" fill="#fb7185" text-anchor="middle">Address Bus (1-Way)</text>

    <!-- Data Bus (Bidirectional: CPU <-> RAM) -->
    <path d="M -30,220 L 160,220" stroke="#34d399" stroke-width="4"/>
    <polygon points="-22,214 -32,220 -22,226" fill="#34d399"/>
    <polygon points="152,214 162,220 152,226" fill="#34d399"/>
    <rect x="0" y="195" width="130" height="22" rx="4" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
    <text x="65" y="210" font-size="9.5" font-weight="bold" fill="#34d399" text-anchor="middle">Data Bus (2-Way)</text>

    <!-- Control Bus (Bidirectional: CPU <-> RAM) -->
    <path d="M -30,320 L 160,320" stroke="#a5b4fc" stroke-width="4"/>
    <polygon points="-22,314 -32,320 -22,326" fill="#a5b4fc"/>
    <polygon points="152,314 162,320 152,326" fill="#a5b4fc"/>
    <rect x="0" y="295" width="130" height="22" rx="4" fill="#1e293b" stroke="#a5b4fc" stroke-width="1"/>
    <text x="65" y="310" font-size="9.5" font-weight="bold" fill="#a5b4fc" text-anchor="middle">Control Bus (Read/Write)</text>
  </g>
</svg>
""")

SVG_FDE_CYCLE_DETAILED = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Fetch – Decode – Execute (FDE) Machine Cycle</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">The continuous three-stage loop executed billions of times per second by every CPU core</text>

  <!-- Step 1: FETCH -->
  <g transform="translate(40, 95)">
    <rect width="270" height="380" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect width="270" height="32" rx="8" fill="#0284c7"/>
    <text x="135" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 1: FETCH</text>
    
    <circle cx="135" cy="65" r="22" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
    <text x="135" y="72" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">1</text>

    <text x="15" y="110" font-size="10.5" font-weight="bold" fill="#38bdf8">1. Address Read:</text>
    <text x="15" y="126" font-size="9.5" fill="#cbd5e1">Address in Program Counter (PC)</text>
    <text x="15" y="140" font-size="9.5" fill="#cbd5e1">copied into MAR.</text>

    <text x="15" y="168" font-size="10.5" font-weight="bold" fill="#38bdf8">2. Read Signal Sent:</text>
    <text x="15" y="184" font-size="9.5" fill="#cbd5e1">CU sends "Read" pulse down Control</text>
    <text x="15" y="198" font-size="9.5" fill="#cbd5e1">Bus to RAM.</text>

    <text x="15" y="226" font-size="10.5" font-weight="bold" fill="#38bdf8">3. Instruction Transfer:</text>
    <text x="15" y="242" font-size="9.5" fill="#cbd5e1">Instruction travels via Data Bus into</text>
    <text x="15" y="256" font-size="9.5" fill="#cbd5e1">MDR, then copied to IR.</text>

    <text x="15" y="284" font-size="10.5" font-weight="bold" fill="#38bdf8">4. Counter Incremented:</text>
    <text x="15" y="300" font-size="9.5" fill="#cbd5e1">PC updates automatically:</text>
    <rect x="25" y="315" width="220" height="28" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
    <text x="135" y="334" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">PC = PC + 1</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <path d="M 315,280 L 340,280" stroke="#f59e0b" stroke-width="3"/>
  <polygon points="338,275 348,280 338,285" fill="#f59e0b"/>

  <!-- Step 2: DECODE -->
  <g transform="translate(345, 95)">
    <rect width="270" height="380" rx="12" fill="#0f172a" stroke="#818cf8" stroke-width="2"/>
    <rect width="270" height="32" rx="8" fill="#4f46e5"/>
    <text x="135" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 2: DECODE</text>

    <circle cx="135" cy="65" r="22" fill="#3730a3" stroke="#818cf8" stroke-width="2"/>
    <text x="135" y="72" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">2</text>

    <text x="15" y="110" font-size="10.5" font-weight="bold" fill="#a5b4fc">1. CU Inspects IR:</text>
    <text x="15" y="126" font-size="9.5" fill="#cbd5e1">Control Unit examines binary command</text>
    <text x="15" y="140" font-size="9.5" fill="#cbd5e1">held inside Instruction Register.</text>

    <text x="15" y="168" font-size="10.5" font-weight="bold" fill="#a5b4fc">2. Binary Decomposition:</text>
    <rect x="15" y="185" width="240" height="60" rx="6" fill="#1e293b" stroke="#818cf8" stroke-width="1"/>
    <text x="65" y="205" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">OPCODE</text>
    <text x="65" y="225" font-size="9" fill="#94a3b8" text-anchor="middle">Operation (ADD)</text>
    <line x1="125" y1="190" x2="125" y2="240" stroke="#64748b"/>
    <text x="185" y="205" font-size="10" font-weight="bold" fill="#f59e0b" text-anchor="middle">OPERAND</text>
    <text x="185" y="225" font-size="9" fill="#94a3b8" text-anchor="middle">Target (Addr 151)</text>

    <text x="15" y="270" font-size="10.5" font-weight="bold" fill="#a5b4fc">3. Resource Routing:</text>
    <text x="15" y="288" font-size="9.5" fill="#cbd5e1">CU prepares signal pathways to ALU,</text>
    <text x="15" y="302" font-size="9.5" fill="#cbd5e1">Registers, or Memory Controller.</text>

    <rect x="25" y="325" width="220" height="35" rx="6" fill="#1e293b"/>
    <text x="135" y="347" font-size="9" fill="#a5b4fc" text-anchor="middle">"Translates binary code to hardware intent"</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <path d="M 620,280 L 645,280" stroke="#f59e0b" stroke-width="3"/>
  <polygon points="643,275 653,280 643,285" fill="#f59e0b"/>

  <!-- Step 3: EXECUTE -->
  <g transform="translate(650, 95)">
    <rect width="270" height="380" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <rect width="270" height="32" rx="8" fill="#059669"/>
    <text x="135" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 3: EXECUTE</text>

    <circle cx="135" cy="65" r="22" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="135" y="72" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">3</text>

    <text x="15" y="110" font-size="10.5" font-weight="bold" fill="#34d399">1. Action Triggered:</text>
    <text x="15" y="126" font-size="9.5" fill="#cbd5e1">CU fires electrical control signals to</text>
    <text x="15" y="140" font-size="9.5" fill="#cbd5e1">execute the specific command.</text>

    <text x="15" y="168" font-size="10.5" font-weight="bold" fill="#34d399">2. Arithmetic / Logic:</text>
    <text x="15" y="184" font-size="9.5" fill="#cbd5e1">ALU performs calculation (e.g. 5 + 3)</text>
    <text x="15" y="198" font-size="9.5" fill="#cbd5e1">and stores result in Accumulator (ACC).</text>

    <text x="15" y="226" font-size="10.5" font-weight="bold" fill="#34d399">3. Memory Store / Read:</text>
    <text x="15" y="242" font-size="9.5" fill="#cbd5e1">If storing, result written from ACC/MDR</text>
    <text x="15" y="256" font-size="9.5" fill="#cbd5e1">back into RAM address.</text>

    <!-- Loop Back Arrow Graphic -->
    <rect x="20" y="285" width="230" height="70" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="135" y="310" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">Cycle Repeats Instantly</text>
    <text x="135" y="330" font-size="8.5" fill="#94a3b8" text-anchor="middle">Loop returns to Stage 1 at address in PC</text>
  </g>
</svg>
""")

SVG_FDE_SIMULATION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 500" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="470" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="19" font-weight="bold" fill="#38bdf8" text-anchor="middle">CPU Instruction Dry-Run Simulation: LOAD, ADD, STORE, HALT</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Tracing internal register transitions and RAM memory mutations across 4 consecutive machine cycles</text>

  <!-- Trace Table -->
  <g transform="translate(40, 90)">
    <!-- Header -->
    <rect width="880" height="32" rx="6" fill="#0284c7"/>
    <text x="40" y="21" font-size="11" font-weight="bold" fill="#ffffff">Cycle</text>
    <text x="120" y="21" font-size="11" font-weight="bold" fill="#ffffff">Instruction</text>
    <text x="210" y="21" font-size="11" font-weight="bold" fill="#ffffff">MAR</text>
    <text x="310" y="21" font-size="11" font-weight="bold" fill="#ffffff">MDR</text>
    <text x="430" y="21" font-size="11" font-weight="bold" fill="#ffffff">IR</text>
    <text x="540" y="21" font-size="11" font-weight="bold" fill="#ffffff">ACC</text>
    <text x="630" y="21" font-size="11" font-weight="bold" fill="#ffffff">PC Next</text>
    <text x="760" y="21" font-size="11" font-weight="bold" fill="#ffffff">RAM / ALU Action</text>

    <!-- Row 1 -->
    <rect y="40" width="880" height="65" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <text x="40" y="65" font-size="11" font-weight="bold" fill="#38bdf8">1</text>
    <text x="120" y="65" font-size="10.5" font-weight="bold" fill="#ffffff">LOAD 150</text>
    <text x="210" y="65" font-size="10" fill="#fb7185">100 → 150</text>
    <text x="310" y="65" font-size="10" fill="#34d399">LOAD 150 → 5</text>
    <text x="430" y="65" font-size="10" fill="#a5b4fc">LOAD 150</text>
    <text x="540" y="65" font-size="11" font-weight="bold" fill="#fbbf24">5</text>
    <text x="630" y="65" font-size="10" fill="#38bdf8">101</text>
    <text x="710" y="65" font-size="9" fill="#cbd5e1">Fetched value '5' from Addr 150</text>
    <text x="710" y="80" font-size="8.5" fill="#94a3b8">and loaded into Accumulator.</text>

    <!-- Row 2 -->
    <rect y="115" width="880" height="65" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
    <text x="40" y="140" font-size="11" font-weight="bold" fill="#10b981">2</text>
    <text x="120" y="140" font-size="10.5" font-weight="bold" fill="#ffffff">ADD 151</text>
    <text x="210" y="140" font-size="10" fill="#fb7185">101 → 151</text>
    <text x="310" y="140" font-size="10" fill="#34d399">ADD 151 → 3</text>
    <text x="430" y="140" font-size="10" fill="#a5b4fc">ADD 151</text>
    <text x="540" y="140" font-size="11" font-weight="bold" fill="#fbbf24">8</text>
    <text x="630" y="140" font-size="10" fill="#38bdf8">102</text>
    <text x="710" y="140" font-size="9" fill="#cbd5e1">ALU calculated 5 + 3 = 8.</text>
    <text x="710" y="155" font-size="8.5" fill="#94a3b8">Accumulator updated to 8.</text>

    <!-- Row 3 -->
    <rect y="190" width="880" height="65" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
    <text x="40" y="215" font-size="11" font-weight="bold" fill="#f59e0b">3</text>
    <text x="120" y="215" font-size="10.5" font-weight="bold" fill="#ffffff">STORE 152</text>
    <text x="210" y="215" font-size="10" fill="#fb7185">102 → 152</text>
    <text x="310" y="215" font-size="10" fill="#34d399">8 (to write)</text>
    <text x="430" y="215" font-size="10" fill="#a5b4fc">STORE 152</text>
    <text x="540" y="215" font-size="11" font-weight="bold" fill="#fbbf24">8</text>
    <text x="630" y="215" font-size="10" fill="#38bdf8">103</text>
    <text x="710" y="215" font-size="9" fill="#cbd5e1">Value 8 written across bus</text>
    <text x="710" y="230" font-size="8.5" fill="#94a3b8">into RAM memory address 152.</text>

    <!-- Row 4 -->
    <rect y="265" width="880" height="65" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="40" y="290" font-size="11" font-weight="bold" fill="#ef4444">4</text>
    <text x="120" y="290" font-size="10.5" font-weight="bold" fill="#ffffff">HALT</text>
    <text x="210" y="290" font-size="10" fill="#fb7185">103</text>
    <text x="310" y="290" font-size="10" fill="#34d399">HALT</text>
    <text x="430" y="290" font-size="10" fill="#a5b4fc">HALT</text>
    <text x="540" y="290" font-size="11" font-weight="bold" fill="#fbbf24">8</text>
    <text x="630" y="290" font-size="10" fill="#38bdf8">104</text>
    <text x="710" y="290" font-size="9" fill="#f87171">CU halts processor loop.</text>
    <text x="710" y="305" font-size="8.5" fill="#94a3b8">Program successfully finishes.</text>
  </g>
</svg>
""")

SVG_CPU_PERFORMANCE_FACTORS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Primary Engineering Factors Affecting CPU Performance</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Clock Speed, Processor Cores, Cache Hierarchy &amp; Word Length Architecture</text>

  <!-- 1. Clock Speed (GHz) -->
  <g transform="translate(40, 90)">
    <rect width="205" height="380" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="205" height="28" rx="8" fill="#0284c7"/>
    <text x="102" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Clock Speed (GHz)</text>

    <!-- Wave Graphic -->
    <path d="M 20,70 L 45,70 L 45,45 L 70,45 L 70,70 L 95,70 L 95,45 L 120,45 L 120,70 L 145,70 L 145,45 L 170,45 L 170,70 L 185,70" fill="none" stroke="#38bdf8" stroke-width="2"/>
    <text x="102" y="90" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Quartz Crystal Pulses</text>

    <text x="12" y="120" font-size="10" font-weight="bold" fill="#e2e8f0">• Frequency of FDE:</text>
    <text x="12" y="138" font-size="9" fill="#94a3b8">Each clock tick executes an internal micro-step.</text>

    <text x="12" y="175" font-size="10" font-weight="bold" fill="#e2e8f0">• Metric Scale:</text>
    <text x="12" y="193" font-size="9" fill="#94a3b8">1 GHz = 1 Billion cycles/sec.</text>
    <text x="12" y="210" font-size="9" fill="#38bdf8">3.5 GHz = 3.5 Billion/sec.</text>

    <rect x="10" y="270" width="185" height="85" rx="6" fill="#1e293b"/>
    <text x="18" y="295" font-size="9.5" font-weight="bold" fill="#38bdf8">Core Takeaway:</text>
    <text x="18" y="315" font-size="8.5" fill="#cbd5e1">Higher clock speed = faster single-threaded execution, but generates more heat.</text>
  </g>

  <!-- 2. Processor Cores -->
  <g transform="translate(265, 90)">
    <rect width="205" height="380" rx="10" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect width="205" height="28" rx="8" fill="#059669"/>
    <text x="102" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Processor Cores</text>

    <!-- Toll Booth Analogy Graphic -->
    <rect x="25" y="45" width="155" height="40" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
    <text x="102" y="62" font-size="9" font-weight="bold" fill="#34d399" text-anchor="middle">Parallel Toll Booths</text>
    <text x="102" y="76" font-size="8" fill="#cbd5e1" text-anchor="middle">Core 1 | Core 2 | Core 3 | Core 4</text>

    <text x="12" y="120" font-size="10" font-weight="bold" fill="#e2e8f0">• Independent Units:</text>
    <text x="12" y="138" font-size="9" fill="#94a3b8">Each core has its own ALU, CU, and registers.</text>

    <text x="12" y="175" font-size="10" font-weight="bold" fill="#e2e8f0">• True Multitasking:</text>
    <text x="12" y="193" font-size="9" fill="#94a3b8">Dual (2), Quad (4), Octa (8).</text>
    <text x="12" y="210" font-size="9" fill="#34d399">Executes instructions in parallel simultaneously.</text>

    <rect x="10" y="270" width="185" height="85" rx="6" fill="#1e293b"/>
    <text x="18" y="295" font-size="9.5" font-weight="bold" fill="#34d399">Core Takeaway:</text>
    <text x="18" y="315" font-size="8.5" fill="#cbd5e1">Requires multi-threaded software to utilize all cores effectively.</text>
  </g>

  <!-- 3. Cache Memory (L1-L3) -->
  <g transform="translate(490, 90)">
    <rect width="205" height="380" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="205" height="28" rx="8" fill="#d97706"/>
    <text x="102" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Cache Memory</text>

    <!-- Cache Hierarchy Pyramid Graphic -->
    <polygon points="102,40 50,85 154,85" fill="#f59e0b" opacity="0.4"/>
    <text x="102" y="60" font-size="8" font-weight="bold" fill="#fbbf24" text-anchor="middle">L1 (Core)</text>
    <text x="102" y="73" font-size="7.5" fill="#ffffff" text-anchor="middle">L2 (Shared Pair)</text>
    <text x="102" y="83" font-size="7.5" fill="#ffffff" text-anchor="middle">L3 (Chip-Wide)</text>

    <text x="12" y="120" font-size="10" font-weight="bold" fill="#e2e8f0">• On-Chip SRAM:</text>
    <text x="12" y="138" font-size="9" fill="#94a3b8">Bypasses slow motherboard bus trips to RAM.</text>

    <text x="12" y="175" font-size="10" font-weight="bold" fill="#e2e8f0">• Hit vs. Miss:</text>
    <text x="12" y="193" font-size="9" fill="#34d399">Cache Hit: Instant access (&lt;2ns).</text>
    <text x="12" y="210" font-size="9" fill="#fb7185">Cache Miss: Waits for RAM (~60ns).</text>

    <rect x="10" y="270" width="185" height="85" rx="6" fill="#1e293b"/>
    <text x="18" y="295" font-size="9.5" font-weight="bold" fill="#f59e0b">Core Takeaway:</text>
    <text x="18" y="315" font-size="8.5" fill="#cbd5e1">Larger cache dramatically minimizes CPU wait states (RAM latency bottleneck).</text>
  </g>

  <!-- 4. Word Length (32 vs 64) -->
  <g transform="translate(715, 90)">
    <rect width="205" height="380" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="205" height="28" rx="8" fill="#7e22ce"/>
    <text x="102" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">4. Word Length</text>

    <rect x="25" y="45" width="155" height="40" rx="6" fill="#1e293b" stroke="#a855f7" stroke-width="1"/>
    <text x="102" y="62" font-size="9.5" font-weight="bold" fill="#c084fc" text-anchor="middle">32-Bit vs. 64-Bit</text>
    <text x="102" y="76" font-size="8" fill="#94a3b8" text-anchor="middle">Register Bit Width ($2^n$)</text>

    <text x="12" y="120" font-size="10" font-weight="bold" fill="#e2e8f0">• Register Capacity:</text>
    <text x="12" y="138" font-size="9" fill="#94a3b8">Bits processed in a single cycle.</text>

    <text x="12" y="175" font-size="10" font-weight="bold" fill="#e2e8f0">• RAM Address Limits:</text>
    <text x="12" y="193" font-size="9" fill="#fb7185">32-bit: Max 4 GB RAM ($2^{32}$).</text>
    <text x="12" y="210" font-size="9" fill="#34d399">64-bit: Max 16 Exabytes ($2^{64}$).</text>

    <rect x="10" y="270" width="185" height="85" rx="6" fill="#1e293b"/>
    <text x="18" y="295" font-size="9.5" font-weight="bold" fill="#c084fc">Core Takeaway:</text>
    <text x="18" y="315" font-size="8.5" fill="#cbd5e1">64-bit handles enormous numbers and massive RAM pools for modern computing.</text>
  </g>
</svg>
""")

SVG_RISC_VS_CISC_COMPARISON = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Instruction Set Architectures: RISC vs. CISC</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Philosophical contrast between ARM (mobile efficiency) and Intel x86/AMD64 (desktop complexity)</text>

  <!-- Left: RISC -->
  <g transform="translate(40, 85)">
    <rect width="420" height="390" rx="12" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <rect width="420" height="32" rx="8" fill="#059669"/>
    <text x="210" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">RISC (Reduced Instruction Set Computer)</text>

    <rect x="25" y="45" width="370" height="70" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
    <text x="210" y="68" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">Philosophy: Simple, Uniform, 1-Cycle Commands</text>
    <text x="210" y="88" font-size="9" fill="#cbd5e1" text-anchor="middle">`LOAD R1, 150` → `LOAD R2, 151` → `ADD R1, R2` → `STORE 152, R1`</text>
    <text x="210" y="103" font-size="8.5" fill="#94a3b8" text-anchor="middle">(Requires 4 distinct, single-cycle instructions)</text>

    <text x="25" y="145" font-size="10.5" font-weight="bold" fill="#34d399">• Hardware Design:</text>
    <text x="25" y="162" font-size="9.5" fill="#cbd5e1">Simple decoding circuits, fewer transistors, cheaper production.</text>

    <text x="25" y="195" font-size="10.5" font-weight="bold" fill="#34d399">• Power &amp; Thermal Efficiency:</text>
    <text x="25" y="212" font-size="9.5" fill="#cbd5e1">Minimal electrical consumption, low thermal output, fanless.</text>

    <text x="25" y="245" font-size="10.5" font-weight="bold" fill="#34d399">• Dominant Architecture:</text>
    <text x="25" y="262" font-size="10" font-weight="bold" fill="#38bdf8">ARM Architecture, Apple Silicon (M1/M2/M3), RISC-V</text>

    <rect x="25" y="290" width="370" height="70" rx="8" fill="#1e293b"/>
    <text x="35" y="315" font-size="10.5" font-weight="bold" fill="#34d399">Typical Devices:</text>
    <text x="35" y="335" font-size="9.5" fill="#cbd5e1">Smartphones (iPhone, Android), tablets, smartwatches, IoT, MacBooks.</text>
  </g>

  <!-- Right: CISC -->
  <g transform="translate(500, 85)">
    <rect width="420" height="390" rx="12" fill="#0f172a" stroke="#818cf8" stroke-width="1.5"/>
    <rect width="420" height="32" rx="8" fill="#4f46e5"/>
    <text x="210" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">CISC (Complex Instruction Set Computer)</text>

    <rect x="25" y="45" width="370" height="70" rx="8" fill="#1e293b" stroke="#818cf8" stroke-width="1"/>
    <text x="210" y="68" font-size="11" font-weight="bold" fill="#a5b4fc" text-anchor="middle">Philosophy: Rich, Powerful, Multi-Cycle Commands</text>
    <text x="210" y="88" font-size="9" fill="#cbd5e1" text-anchor="middle">`MULT 152, 150, 151`</text>
    <text x="210" y="103" font-size="8.5" fill="#94a3b8" text-anchor="middle">(One complex instruction loads, multiplies, and stores in memory)</text>

    <text x="25" y="145" font-size="10.5" font-weight="bold" fill="#a5b4fc">• Hardware Design:</text>
    <text x="25" y="162" font-size="9.5" fill="#cbd5e1">Complex internal decoder breaks down commands into micro-ops.</text>

    <text x="25" y="195" font-size="10.5" font-weight="bold" fill="#a5b4fc">• Power &amp; Thermal Output:</text>
    <text x="25" y="212" font-size="9.5" fill="#cbd5e1">High power draw, significant heat requiring active heatsinks/fans.</text>

    <text x="25" y="245" font-size="10.5" font-weight="bold" fill="#a5b4fc">• Dominant Architecture:</text>
    <text x="25" y="262" font-size="10" font-weight="bold" fill="#f59e0b">Intel x86 / AMD64 (x86-64)</text>

    <rect x="25" y="290" width="370" height="70" rx="8" fill="#1e293b"/>
    <text x="35" y="315" font-size="10.5" font-weight="bold" fill="#a5b4fc">Typical Devices:</text>
    <text x="35" y="335" font-size="9.5" fill="#cbd5e1">High-end desktop PCs, AAA gaming rigs, enterprise data center servers.</text>
  </g>
</svg>
""")


# =====================================================================
# CURRICULUM DEFINITION: 2 UNITS, 2 PUBLISHED LESSONS, RICH CARDS
# =====================================================================

def build_topic5_curriculum():
    return [
        # -------------------------------------------------------------
        # LESSON 9: CPU Components and the Fetch–Decode–Execute Cycle
        # -------------------------------------------------------------
        {
            "unit_order": 1,
            "unit_name": "CPU Components and the Fetch–Decode–Execute Cycle",
            "unit_description": "Internal architecture of the Central Processing Unit (ALU, Control Unit, Registers, System Buses) and the mechanics and simulation of the Fetch-Decode-Execute (FDE) machine cycle.",
            "lesson_title": "CPU Components and the Fetch–Decode–Execute Cycle",
            "pages": [
                # Card 1: Hook, Chef Analogy & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Silicon Microprocessor Die",
                        "content": {
                            "title": "Silicon Microprocessor Die",
                            "caption": "A high-resolution microscopic view of a modern microprocessor silicon die, revealing millions of etched transistors forming the ALU, Control Unit, and registers.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Microprocessor_die.jpg/800px-Microprocessor_die.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: CPU Architecture & FDE Cycle",
                        "content": {
                            "title": "What We Will Master in This Lesson",
                            "goals": [
                                "Identify the primary internal components of the CPU: **Arithmetic Logic Unit (ALU)**, **Control Unit (CU)**, and **Registers**.",
                                "Distinguish between the 5 dedicated CPU registers: **PC**, **IR**, **MAR**, **MDR**, and **ACC**.",
                                "Analyze the role and directionality of the 3 motherboard system buses: **Address Bus** (unidirectional), **Data Bus** (bidirectional), and **Control Bus** (bidirectional).",
                                "Trace the step-by-step mechanics of the **Fetch–Decode–Execute (FDE) Cycle**.",
                                "Dry-run and simulate instruction execution (`LOAD`, `ADD`, `STORE`, `HALT`) tracking register mutations and RAM state."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Kitchen & Chef Analogy",
                        "content": {
                            "title": "How a Computer Processes Data Like a Professional Kitchen",
                            "text": "To understand the CPU's internal operations, let us step out of the computer and into a busy restaurant kitchen:\n\n- **Secondary Storage (The Walk-In Freezer)**: A massive cold storage room at the back. It holds hundreds of ingredient boxes permanently. However, walking there takes time, and you cannot cook inside it.\n- **Primary Memory / RAM (The Prep Counter)**: The large stainless steel table in the center. Before cooking, the assistant brings the ingredients and the printed recipe card from the freezer to the table. It is fast to reach, but if power cuts, any food left out spoils.\n- **The CPU (The Head Chef)**: Standing at the stove, reading the recipe card one line at a time, grabbing ingredients from the prep counter, and cooking.\n- **CPU Registers (The Chef's Handheld Spice Bowls)**: Tiny bowls held right next to the stove for split-second, immediate access during active mixing.\n\nInside the CPU, this cooking loop is called the **Fetch–Decode–Execute (FDE) Cycle**."
                        }
                    }
                ],
                # Card 2: Core Definitions & CPU Structure
                [
                    {
                        "type": "suggested_image",
                        "title": "Modern Multi-Core Desktop Processor & LGA Socket Interface",
                        "content": {
                            "title": "Modern Multi-Core Desktop Processor & LGA Socket Interface",
                            "caption": "A high-performance modern desktop microprocessor with integrated heat spreader (IHS) designed to interface directly with high-speed system buses via an LGA motherboard socket.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Intel_Core_i7-2600K_top.jpg/800px-Intel_Core_i7-2600K_top.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Core Definitions & CPU Internal Subsystems",
                        "content": {
                            "title": "The Three Pillars of Processor Architecture",
                            "text": "The **Central Processing Unit (CPU)** is the primary hardware component that interprets, coordinates, and executes program instructions.\n\n### 1. Arithmetic Logic Unit (ALU)\n- **Arithmetic Operations**: Addition, subtraction, multiplication, and division.\n- **Logical Operations**: Boolean evaluations (`AND`, `OR`, `NOT`) and relational comparisons (`>`, `<`, `=`).\n- *Role*: The computational 'muscle' of the CPU.\n\n### 2. Control Unit (CU)\n- **Role**: The 'nervous system' that manages, coordinates, and synchronizes all CPU activities.\n- **Operation**: Retrieves instructions from memory, decodes their binary opcodes, and emits electrical synchronization pulses along the control bus to coordinate the ALU, registers, and RAM.\n\n### 3. System Buses (Motherboard Communication Lines)\n- **Address Bus (Unidirectional)**: Carries physical memory addresses from the CPU out to RAM.\n- **Data Bus (Bidirectional)**: Carries actual data bytes and instruction codes between CPU, memory, and peripherals.\n- **Control Bus (Bidirectional)**: Transmits control commands (`Memory Read`, `Memory Write`, `Interrupt`) and clock timing pulses."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "CPU Internal Architecture Block Diagram",
                        "content": {
                            "svg_content": SVG_CPU_ARCHITECTURE_BLOCK,
                            "caption": "Block diagram of CPU internals (CU, ALU, Registers) and external system bus connections to RAM."
                        }
                    }
                ],
                # Card 3: Dedicated Registers Deep-Dive
                [
                    {
                        "type": "concept_explanation",
                        "title": "Internal CPU Registers: Dedicated Roles",
                        "content": {
                            "title": "The 5 Key Hardware Registers",
                            "text": "Registers are ultra-fast, tiny storage locations located directly inside the processor die:\n\n1. **Program Counter (PC)**: Holds the memory address of the *next* instruction scheduled to be fetched. Automatically increments ($PC = PC + 1$) after each fetch.\n2. **Instruction Register (IR)**: Holds the actual *current binary instruction* while the Control Unit decodes it.\n3. **Memory Address Register (MAR)**: Holds the RAM address currently being read from or written to.\n4. **Memory Data Register (MDR)**: Holds the data value or instruction byte just read from RAM or waiting to be written to RAM.\n5. **Accumulator (ACC)**: Holds intermediate mathematical and logical results generated by the ALU."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "How the CPU Works & Registers",
                        "content": {
                            "youtube_id": "cNN_tTXABUA",
                            "title": "Crash Course Computer Science: Instructions & Programs",
                            "description": "Exploration of how the Control Unit, ALU, and registers work together to fetch, decode, and execute instructions."
                        }
                    }
                ],
                # Card 4: Step-by-Step FDE Cycle
                [
                    {
                        "type": "step_process",
                        "title": "The Three-Stage Fetch–Decode–Execute Machine Cycle",
                        "content": {
                            "title": "Step-by-Step Mechanics of the Machine Loop",
                            "steps": [
                                "**Stage 1: FETCH**\n- CPU copies address from Program Counter (PC) to Memory Address Register (MAR).\n- Control Unit sends 'Memory Read' signal along Control Bus.\n- RAM locates address on Address Bus, places instruction onto Data Bus into MDR.\n- Instruction copied from MDR to Instruction Register (IR).\n- Program Counter increments by 1 ($PC = PC + 1$).",
                                "**Stage 2: DECODE**\n- Control Unit examines instruction inside IR.\n- Splitting command into **Opcode** (operation code, e.g., `ADD`, `LOAD`) and **Operand** (target data or memory address, e.g., `151`).\n- Prepares internal signal paths to necessary hardware units.",
                                "**Stage 3: EXECUTE**\n- Control Unit activates required functional circuits.\n- For arithmetic/logic: ALU computes result and saves to Accumulator (ACC).\n- For memory writes: Data in ACC/MDR written to RAM address.\n- Loop restarts immediately at Stage 1 with address in PC."
                            ]
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Fetch-Decode-Execute Flowchart Diagram",
                        "content": {
                            "svg_content": SVG_FDE_CYCLE_DETAILED,
                            "caption": "The cyclic three-stage pipeline of the Fetch-Decode-Execute machine loop."
                        }
                    }
                ],
                # Card 5: Instruction-Level Simulation & Dry-Run
                [
                    {
                        "type": "worked_example",
                        "title": "Instruction-Level Simulation & Dry-Run Trace",
                        "content": {
                            "title": "Tracing Machine Program Execution",
                            "problem": "Simulate the step-by-step execution of a 4-instruction program starting at address 100 with starting RAM values: Address 150 = 5, Address 151 = 3, Address 152 = 0.",
                            "steps": [
                                "**Cycle 1 (`LOAD 150` at Addr 100)**:\n- Fetch: PC=100 → MAR=100 → MDR=`LOAD 150` → IR=`LOAD 150`. PC increments to 101.\n- Decode: Opcode=`LOAD`, Operand=`150`.\n- Execute: MAR=150 → MDR=5 → ACC=5.",
                                "**Cycle 2 (`ADD 151` at Addr 101)**:\n- Fetch: PC=101 → MAR=101 → MDR=`ADD 151` → IR=`ADD 151`. PC increments to 102.\n- Decode: Opcode=`ADD`, Operand=`151`.\n- Execute: MAR=151 → MDR=3 → ALU adds ACC(5) + MDR(3) = 8 → ACC=8.",
                                "**Cycle 3 (`STORE 152` at Addr 102)**:\n- Fetch: PC=102 → MAR=102 → MDR=`STORE 152` → IR=`STORE 152`. PC increments to 103.\n- Decode: Opcode=`STORE`, Operand=`152`.\n- Execute: MAR=152 → MDR=8 → Write signal sent → RAM Address 152 is now updated to 8.",
                                "**Cycle 4 (`HALT` at Addr 103)**:\n- Fetch: PC=103 → MAR=103 → MDR=`HALT` → IR=`HALT`. PC increments to 104.\n- Decode & Execute: Opcode=`HALT` stops the machine execution loop."
                            ]
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Instruction Dry-Run Register Transition Table",
                        "content": {
                            "svg_content": SVG_FDE_SIMULATION,
                            "caption": "Step-by-step trace of register states across cycles 1 through 4 during arithmetic program execution."
                        }
                    }
                ],
                # Card 6: Knowledge Check & Key Takeaways
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 1: Next Instruction Pointer",
                        "content": {
                            "question": "Which CPU register holds the memory address of the NEXT instruction scheduled to be fetched and executed?",
                            "options": [
                                "Memory Data Register (MDR)",
                                "Instruction Register (IR)",
                                "Program Counter (PC)",
                                "Accumulator (ACC)"
                            ],
                            "correct": "C",
                            "explanation": "The Program Counter (PC) holds the address of the next instruction and increments automatically during the fetch phase."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 2: System Bus Directionality",
                        "content": {
                            "question": "Which system bus is strictly unidirectional, carrying electrical address signals only FROM the CPU TO system RAM?",
                            "options": [
                                "Data Bus",
                                "Control Bus",
                                "Address Bus",
                                "Internal Bus"
                            ],
                            "correct": "C",
                            "explanation": "The Address Bus is unidirectional because memory addresses originate exclusively from the CPU's MAR to specify which RAM cell to access."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 3: Instruction Decoding",
                        "content": {
                            "question": "During the decode stage, what two primary components does the Control Unit decompose an instruction into?",
                            "options": [
                                "Address and Bus",
                                "Opcode (operation code) and Operand (target data/address)",
                                "Volatile and Non-Volatile blocks",
                                "RAM and ROM addresses"
                            ],
                            "correct": "B",
                            "explanation": "An instruction is split into an Opcode (e.g. ADD, LOAD) specifying what action to take, and an Operand specifying the data or memory address to act on."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 4: Accumulator Register Function",
                        "content": {
                            "question": "What is the primary role of the Accumulator (ACC) register during arithmetic and logic execution?",
                            "options": [
                                "To store the IP address of the network gateway",
                                "To temporarily hold the immediate results of mathematical calculations and logical evaluations performed by the ALU",
                                "To power down unused cores in the CPU",
                                "To convert analog signals into digital video"
                            ],
                            "correct": "B",
                            "explanation": "The Accumulator (ACC) is a dedicated CPU register that holds intermediate output values generated by the Arithmetic Logic Unit (ALU) before they are written to RAM or used in subsequent calculations."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Lesson 9 Key Takeaways",
                        "content": {
                            "text": "1. **CPU Architecture**: The ALU calculates and compares; the Control Unit decodes and coordinates; registers provide zero-latency on-chip storage.\n2. **Dedicated Registers**: PC (next address), IR (current instruction), MAR (memory address), MDR (memory data buffer), ACC (intermediate calculation results).\n3. **System Buses**: Address Bus (unidirectional CPU → RAM), Data Bus (bidirectional data exchange), Control Bus (bidirectional timing and commands).\n4. **FDE Cycle**: Fetch (read from RAM via PC/MAR/MDR/IR, increment PC), Decode (CU parses opcode & operand), Execute (ALU computes or memory updates).\n5. **Simulation**: Register states update cyclically, transferring operands into the Accumulator and writing outputs back to RAM."
                        }
                    }
                ]
            ]
        },

        # -------------------------------------------------------------
        # LESSON 10: CPU Performance and Types of Processing
        # -------------------------------------------------------------
        {
            "unit_order": 2,
            "unit_name": "CPU Performance and Types of Processing",
            "unit_description": "Factors affecting CPU processing speed (clock speed, multi-core processing, cache hierarchy, word length) and Instruction Set Architectures (RISC vs. CISC paradigms).",
            "lesson_title": "CPU Performance and Types of Processing",
            "pages": [
                # Card 1: Hook, Silicon Wafer & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Multi-Core Silicon Microprocessor",
                        "content": {
                            "title": "Multi-Core Silicon Microprocessor",
                            "caption": "A quad-core processor die featuring four physical processing cores with dedicated L1/L2 caches and a shared L3 cache on a single silicon substrate.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Intel_Core_2_Quad_Q6600_Kentsfield.jpg/800px-Intel_Core_2_Quad_Q6600_Kentsfield.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Performance & Architectures",
                        "content": {
                            "title": "What We Will Master in This Lesson",
                            "goals": [
                                "Analyze how **Clock Speed (GHz)** impacts cycle execution frequency.",
                                "Explain how **Multi-Core Processors** enable true parallel processing compared to single-core task switching.",
                                "Evaluate the **Cache Memory Hierarchy (L1, L2, L3)** and the performance impact of Cache Hits vs. Cache Misses.",
                                "Explain **CPU Word Length** and why 64-bit architectures transcend the 4 GB RAM addressing limit of 32-bit systems.",
                                "Contrast **RISC** (Reduced Instruction Set Computer) and **CISC** (Complex Instruction Set Computer) design philosophies, hardware complexity, and application domains."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Four Pillars of Processor Performance",
                        "content": {
                            "title": "Why Clock Speed Alone Does Not Equal Total Speed",
                            "text": "A common misconception is that clock speed alone dictates CPU speed. In reality, overall processor performance is governed by four interdependent architectural factors:\n\n1. **Clock Speed (GHz)**: Ticks per second generated by the internal quartz crystal oscillator.\n2. **Processor Cores**: Independent physical execution units capable of simultaneous parallel computation.\n3. **Cache Memory Size (L1–L3)**: High-speed on-chip SRAM preventing bus bottlenecks to main RAM.\n4. **Word Length (32-bit vs. 64-bit)**: Register width and maximum physical memory addressing capability."
                        }
                    }
                ],
                # Card 2: Performance Factors Deep-Dive
                [
                    {
                        "type": "suggested_image",
                        "title": "Silicon Semiconductor Wafer with Integrated Circuit Processor Dies",
                        "content": {
                            "title": "Silicon Semiconductor Wafer with Integrated Circuit Processor Dies",
                            "caption": "A manufactured silicon semiconductor wafer containing hundreds of etched microchip dies before slicing and packaging into individual multi-core central processing units.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Silicon_wafer_with_microcircuits_edit.jpg/800px-Silicon_wafer_with_microcircuits_edit.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Cores, Cache, and Word Length Mechanics",
                        "content": {
                            "title": "Architectural Breakdown",
                            "text": "### 1. Clock Speed (GHz)\n- Vibrating quartz crystal produces square-wave electrical pulses.\n- $1 \\text{ GHz} = 10^9 \\text{ cycles/second}$. A $3.5 \\text{ GHz}$ CPU executes $3.5 \\text{ billion cycles/second}$.\n\n### 2. Multi-Core Architecture & The Toll Booth Analogy\n- Single-Core: One toll booth. Vehicles (instructions) wait in a single queue.\n- Quad-Core: Four toll booths. Traffic splits into 4 independent lanes, executing 4 tasks in true hardware parallel.\n\n### 3. Cache Memory Hierarchy (SRAM)\n- **L1 Cache**: Built directly into each core (tiny, e.g. 64KB, fastest, &lt;1ns).\n- **L2 Cache**: Dedicated per core or pair of cores (e.g. 512KB–2MB).\n- **L3 Cache**: Large pool shared across all cores on chip (e.g. 16MB–64MB).\n- **Cache Hit**: CPU finds required data in cache immediately.\n- **Cache Miss**: CPU stalls while retrieving data from slower main RAM across system buses.\n\n### 4. Word Length (32-Bit vs. 64-Bit)\n- 32-bit registers can address $2^{32} \\text{ bytes} = \\mathbf{4 \\text{ GB RAM maximum}}$.\n- 64-bit registers can address $2^{64} \\text{ bytes} = \\mathbf{16 \\text{ Exabytes RAM}}$, eliminating memory barriers for large datasets."
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Calculating CPU Execution Time and Clock Throughput",
                        "content": {
                            "title": "Evaluating Execution Latency Across Processor Clock Speeds",
                            "problem": "A single-core computer processor operating at 3.0 GHz ($3.0 \\times 10^9 \\text{ cycles/second}$) executes a scientific program comprising 6 billion ($6.0 \\times 10^9$) instructions. The average Cycles Per Instruction (CPI) for this workload is 1.5. Calculate the total CPU execution time in seconds.",
                            "steps": [
                                "**Step 1: Calculate Total Required CPU Clock Cycles**:\n$$\\text{Total Clock Cycles} = \\text{Instruction Count} \\times \\text{CPI}$$\n$$\\text{Total Cycles} = 6.0 \\times 10^9 \\text{ instructions} \\times 1.5 \\text{ cycles/inst} = \\mathbf{9.0 \\times 10^9 \\text{ cycles}}$$",
                                "**Step 2: Calculate CPU Execution Time ($T$)**:\n$$\\text{Execution Time } (T) = \\frac{\\text{Total Clock Cycles}}{\\text{Clock Frequency (Hz)}} = \\frac{9.0 \\times 10^9 \\text{ cycles}}{3.0 \\times 10^9 \\text{ cycles/second}} = \\mathbf{3.0 \\text{ seconds}}$$",
                                "**Step 3: Evaluate Architectural Optimization**:\nIf the system is upgraded to a modern pipelined processor running at 4.5 GHz with architectural enhancements reducing the CPI to 0.75:\n$$T_{\\text{new}} = \\frac{6.0 \\times 10^9 \\times 0.75}{4.5 \\times 10^9} = \\frac{4.5 \\times 10^9}{4.5 \\times 10^9} = \\mathbf{1.0 \\text{ second}} \\quad (3\\times \\text{ speedup})$$"
                            ]
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Worked Example: 32-Bit vs. 64-Bit Memory Address Space Calculation",
                        "content": {
                            "title": "Deriving Maximum Physical RAM Limits from Register Bit Width",
                            "problem": "Mathematically derive the maximum RAM capacity addressable by a 32-bit CPU and explain why upgrading to a 64-bit architecture eliminates system memory barriers.",
                            "steps": [
                                "**Step 1: Calculate 32-Bit Total Address Combinations**:\nA 32-bit address bus has $32$ binary lines, yielding $2^{32}$ unique byte addresses:\n$$2^{32} = 4,294,967,296 \\text{ distinct memory addresses (Bytes)}$$",
                                "**Step 2: Convert Byte Address Space to Gigabytes**:\n$$\\text{Capacity in GB} = \\frac{4,294,967,296 \\text{ B}}{1024 \\times 1024 \\times 1024 \\text{ B/GB}} = \\mathbf{4.0 \\text{ GB}}$$\n*Conclusion*: A 32-bit operating system cannot address even a single byte beyond 4 GB of RAM, regardless of how much physical RAM is inserted into the motherboard.",
                                "**Step 3: Calculate 64-Bit Address Space Capability**:\nA 64-bit address bus yields $2^{64}$ addresses:\n$$2^{64} = 18,446,744,073,709,551,616 \\text{ Bytes} = \\mathbf{16 \\text{ Exabytes (EB)}}$$\n*Conclusion*: 64-bit architectures support over 17 billion gigabytes of memory space, completely eliminating addressing bottlenecks."
                            ]
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Four Factors of CPU Speed Diagram",
                        "content": {
                            "svg_content": SVG_CPU_PERFORMANCE_FACTORS,
                            "caption": "Visual breakdown of Clock Speed, Cores (Toll Booth analogy), Cache Hierarchy, and Word Length addressing."
                        }
                    }
                ],
                # Card 3: RISC vs. CISC Architectures
                [
                    {
                        "type": "concept_explanation",
                        "title": "Instruction Set Architectures: RISC vs. CISC",
                        "content": {
                            "title": "Two Contrasting Hardware Philosophies",
                            "text": "Every processor is built on an **Instruction Set Architecture (ISA)** defining the machine commands it can execute:\n\n### RISC (Reduced Instruction Set Computer)\n- **Philosophy**: Small, uniform instruction set where each command executes in **one single clock cycle**.\n- **Design**: Simpler hardware, fewer transistors, high energy efficiency, low heat output.\n- **Architecture Examples**: **ARM**, Apple Silicon (M-series), RISC-V.\n- **Dominant Uses**: Smartphones (iPhone, Android), tablets, IoT devices, laptops.\n\n### CISC (Complex Instruction Set Computer)\n- **Philosophy**: Broad, powerful instruction set where single complex commands execute multi-step operations over **multiple clock cycles**.\n- **Design**: Complex internal micro-decoding hardware, higher transistor count, higher power draw and heat.\n- **Architecture Examples**: **Intel x86**, AMD64.\n- **Dominant Uses**: High-performance gaming desktops, engineering workstations, enterprise data centers."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "RISC vs. CISC Architectural Comparison",
                        "content": {
                            "svg_content": SVG_RISC_VS_CISC_COMPARISON,
                            "caption": "Comparison of RISC (single-cycle, low power, ARM/mobile) vs CISC (multi-cycle, complex, x86/desktop)."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "RISC vs CISC Explained",
                        "content": {
                            "youtube_id": "vkyiWp_4_iQ",
                            "title": "RISC vs CISC Architecture & Modern Processors",
                            "description": "Visual explanation comparing RISC and CISC paradigms, pipelining, power efficiency, and real-world deployment."
                        }
                    }
                ],
                # Card 4: Knowledge Check & Key Takeaways
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 1: Cache Memory Benefit",
                        "content": {
                            "question": "Why does a larger on-chip CPU cache memory improve computer performance?",
                            "options": [
                                "It increases the motherboard bus clock frequency",
                                "It stores frequently accessed instructions in high-speed SRAM, minimizing slow access cycles to main RAM",
                                "It expands the 32-bit register to 64-bit capacity",
                                "It converts CISC instructions into RISC instructions"
                            ],
                            "correct": "B",
                            "explanation": "Cache memory holds frequently used data close to CPU execution units, delivering high cache hit rates and avoiding bus latency to slower DRAM."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 2: 32-Bit Memory Limitation",
                        "content": {
                            "question": "What is the maximum theoretical RAM address space supported by a 32-bit word-length CPU architecture?",
                            "options": [
                                "512 MB",
                                "2 GB",
                                "4 GB",
                                "64 GB"
                            ],
                            "correct": "C",
                            "explanation": "A 32-bit address bus can address 2^32 distinct byte locations, which evaluates to exactly 4,294,967,296 bytes (4 GB)."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 3: RISC vs CISC Deployment",
                        "content": {
                            "question": "Which architecture is predominantly used in smartphones and mobile devices due to its single-cycle execution and superior battery power efficiency?",
                            "options": [
                                "Intel x86 CISC",
                                "ARM RISC",
                                "AMD64 CISC",
                                "Vacuum Tube Logic"
                            ],
                            "correct": "B",
                            "explanation": "ARM processors implement RISC architecture, requiring fewer transistors and minimal power, making them ideal for battery-powered smartphones and tablets."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 4: CPU Execution Performance Formula",
                        "content": {
                            "question": "If a processor has a clock frequency of 2.0 GHz and executes a task requiring 4.0 billion clock cycles, what is the total execution time?",
                            "options": [
                                "0.5 seconds",
                                "2.0 seconds",
                                "8.0 seconds",
                                "200 milliseconds"
                            ],
                            "correct": "B",
                            "explanation": "Execution time equals Total Cycles divided by Clock Frequency: (4.0 * 10^9 cycles) / (2.0 * 10^9 cycles/sec) = 2.0 seconds."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Lesson 10 Key Takeaways",
                        "content": {
                            "text": "1. **Clock Speed**: Measured in GHz (billions of cycles/second); sets the fundamental tick frequency of the FDE machine cycle.\n2. **Multi-Core**: Multiple physical ALUs/CUs on one die permit true simultaneous multi-threaded parallel execution.\n3. **Cache Hierarchy**: L1 (per core, fastest), L2 (pair/core), L3 (shared chip pool); prevents processor wait states during RAM fetches.\n4. **Word Length**: 64-bit CPUs handle double data width per operation and shatter the 4GB RAM ceiling of 32-bit systems.\n5. **RISC vs CISC**: RISC (ARM, 1-cycle simple instructions, power-efficient, mobile); CISC (x86, multi-cycle complex commands, high performance desktop/server)."
                        }
                    }
                ]
            ]
        }
    ]

# =====================================================================
# INGESTION RUNNER
# =====================================================================

def ingest_grade10_topic5(replace: bool = True):
    print("=" * 80)
    print("VLEARN CBC CURRICULUM INGESTION: GRADE 10 COMPUTER SCIENCE — TOPIC 5")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="CBC").first() or Curriculum.objects.filter(name__icontains="CBC").first() or Curriculum.objects.filter(id=5).first()
    if not curriculum:
        curriculum = Curriculum.objects.create(name="CBC", description="Kenya Competency Based Curriculum")
        print(f"[*] Created Curriculum: {curriculum.name}")
    else:
        print(f"[*] Resolved Curriculum: {curriculum.name} (ID: {curriculum.id})")

    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 10").first() or Grade.objects.filter(curriculum=curriculum, level=10).first()
    if not grade:
        grade = Grade.objects.create(curriculum=curriculum, name="Grade 10", level=10)
        print(f"[*] Created Grade: {grade.name}")
    else:
        print(f"[*] Resolved Grade: {grade.name} (ID: {grade.id})")

    subject, _ = Subject.objects.get_or_create(
        grade=grade,
        name="Computer Science",
        defaults={"description": "Senior Secondary Computer Science Curriculum (Grade 10 CBC)"}
    )
    print(f"[*] Resolved Subject: {subject.name} (ID: {subject.id})")

    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=5,
        defaults={"name": "Central Processing Unit (CPU)", "description": "Internal CPU architecture (ALU, CU, registers, system buses), the Fetch-Decode-Execute machine cycle, performance factors (clock speed, cores, cache, word length), and RISC vs CISC architectures."}
    )
    if not t_created:
        topic.name = "Central Processing Unit (CPU)"
        topic.description = "Internal CPU architecture (ALU, CU, registers, system buses), the Fetch-Decode-Execute machine cycle, performance factors (clock speed, cores, cache, word length), and RISC vs CISC architectures."
        topic.save()
    print(f"[*] Resolved Topic 5: {topic.name} (ID: {topic.id})")

    if replace:
        print("[*] Replacing existing Topic 5 units, lessons, blocks, and assets...")
        existing_lessons = Lesson.objects.filter(topic=topic)
        LessonAsset.objects.filter(lesson__in=existing_lessons).delete()
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    curriculum_data = build_topic5_curriculum()
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
                    "topic_order": 5,
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
                        block_id=f"g10_cs_t5_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={"topic_order": 5, "unit_order": u_order, "page": page_idx}
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
    print(f"TOPIC 5 INGESTION COMPLETE:")
    print(f"  Units Created:   {total_units}")
    print(f"  Lessons Created: {total_lessons}")
    print(f"  Pages Created:   {total_pages}")
    print(f"  Blocks Created:  {total_blocks}")
    print(f"  Assets Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_grade10_topic5(replace=True)
