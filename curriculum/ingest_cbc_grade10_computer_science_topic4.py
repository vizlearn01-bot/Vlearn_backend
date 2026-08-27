"""
VLearn CBC Grade 10 Computer Science — Topic 4: Computer Storage
Production Ingestion & Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Computer Science
Topic: Computer Storage (Topic Order: 4)

Decomposed into 2 Learning Units & 2 Published Lessons:
  1. Storage Concepts and Storage Media (Lesson 7: Storage Concepts and Storage Media)
  2. Data Organization, Capacity, and Storage Management (Lesson 8: Data Organization, Capacity, and Storage Management)
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
# HIGH PRECISION VECTOR SVGS FOR TOPIC 4
# =====================================================================

SVG_DRAM_VS_SRAM = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Primary Storage Semiconductor Physics: DRAM vs. SRAM</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Circuit architecture, charge storage mechanisms, and refresh cycle requirements</text>

  <!-- Left Column: DRAM -->
  <g transform="translate(40, 85)">
    <rect width="420" height="390" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="420" height="30" rx="8" fill="#0284c7"/>
    <text x="210" y="20" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">Dynamic RAM (DRAM) — 1T-1C Memory Cell</text>
    
    <!-- DRAM Circuit Box -->
    <rect x="30" y="45" width="360" height="120" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
    <circle cx="120" cy="105" r="25" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="120" y="102" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Access</text>
    <text x="120" y="115" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Transistor</text>
    
    <line x1="145" y1="105" x2="240" y2="105" stroke="#38bdf8" stroke-width="2"/>
    <rect x="240" y="80" width="120" height="50" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="300" y="102" font-size="10" font-weight="bold" fill="#f87171" text-anchor="middle">Capacitor (Bit Store)</text>
    <text x="300" y="118" font-size="8.5" fill="#e2e8f0" text-anchor="middle">⚡ Leaks charge!</text>
    
    <text x="25" y="190" font-size="11" font-weight="bold" fill="#38bdf8">• The Refresh Bottleneck:</text>
    <text x="25" y="208" font-size="9.5" fill="#cbd5e1">The microscopic capacitor leaks electrical charge in milliseconds. Must be periodically read and rewritten hundreds of times per second.</text>
    
    <text x="25" y="260" font-size="11" font-weight="bold" fill="#34d399">• Advantages &amp; Density:</text>
    <text x="25" y="278" font-size="9.5" fill="#cbd5e1">Only 1 transistor + 1 capacitor per bit. Ultra-high density, extremely cheap per GB.</text>
    
    <text x="25" y="325" font-size="11" font-weight="bold" fill="#fbbf24">• Role in Systems:</text>
    <text x="25" y="343" font-size="9.5" fill="#cbd5e1">Main System Memory (e.g. 8GB - 64GB DDR4/DDR5 RAM).</text>
  </g>

  <!-- Right Column: SRAM -->
  <g transform="translate(500, 85)">
    <rect width="420" height="390" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="420" height="30" rx="8" fill="#059669"/>
    <text x="210" y="20" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">Static RAM (SRAM) — 6-Transistor Flip-Flop</text>
    
    <!-- SRAM Circuit Box -->
    <rect x="30" y="45" width="360" height="120" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
    <rect x="60" y="65" width="130" height="75" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <text x="125" y="95" font-size="9.5" font-weight="bold" fill="#34d399" text-anchor="middle">Inverter 1 (T1, T2)</text>
    <text x="125" y="112" font-size="8.5" fill="#94a3b8" text-anchor="middle">Cross-Coupled</text>
    
    <line x1="190" y1="102" x2="230" y2="102" stroke="#34d399" stroke-width="2"/>
    <rect x="230" y="65" width="130" height="75" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <text x="295" y="95" font-size="9.5" font-weight="bold" fill="#34d399" text-anchor="middle">Inverter 2 (T3, T4)</text>
    <text x="295" y="112" font-size="8.5" fill="#94a3b8" text-anchor="middle">Latch Circuit</text>
    
    <text x="25" y="190" font-size="11" font-weight="bold" fill="#34d399">• Zero Refreshing Required:</text>
    <text x="25" y="208" font-size="9.5" fill="#cbd5e1">Uses a cross-coupled bistable latch. As long as power is applied, voltage stays locked without leaking.</text>
    
    <text x="25" y="260" font-size="11" font-weight="bold" fill="#38bdf8">• Extreme Speed &amp; Trade-Offs:</text>
    <text x="25" y="278" font-size="9.5" fill="#cbd5e1">Near-zero latency (&lt; 2 ns). Requires 4 to 6 transistors per bit, making it expensive and low-density.</text>
    
    <text x="25" y="325" font-size="11" font-weight="bold" fill="#fbbf24">• Role in Systems:</text>
    <text x="25" y="343" font-size="9.5" fill="#cbd5e1">CPU Cache Memory (L1, L2, L3 Caches inside processor die).</text>
  </g>
</svg>
""")

SVG_OPTICAL_WAVELENGTHS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Optical Storage: Laser Wavelength Physics &amp; Pit Density</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Why Blu-ray holds 70x more data than a Compact Disc on the exact same physical diameter</text>

  <!-- 1. Compact Disc (CD) -->
  <g transform="translate(40, 95)">
    <rect width="270" height="380" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#dc2626"/>
    <text x="135" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Compact Disc (CD) — 700 MB</text>
    
    <!-- Laser Beam Graphic -->
    <polygon points="135,45 80,120 190,120" fill="#ef4444" opacity="0.3"/>
    <line x1="135" y1="45" x2="135" y2="120" stroke="#ef4444" stroke-width="3"/>
    <text x="135" y="140" font-size="10.5" font-weight="bold" fill="#f87171" text-anchor="middle">Red Laser: λ = 780 nm</text>
    
    <text x="15" y="180" font-size="10" font-weight="bold" fill="#f87171">• Track Pitch: 1.60 µm</text>
    <text x="15" y="205" font-size="10" font-weight="bold" fill="#f87171">• Minimum Pit Length: 0.83 µm</text>
    <text x="15" y="235" font-size="9.5" fill="#cbd5e1">Longer wavelength creates a wider beam spot, requiring large pits spaced far apart.</text>
    
    <rect x="15" y="280" width="240" height="70" rx="6" fill="#1e293b"/>
    <text x="25" y="305" font-size="10" font-weight="bold" fill="#f87171">Capacity: ~700 MB</text>
    <text x="25" y="325" font-size="9" fill="#94a3b8">Standard audio albums, older software</text>
  </g>

  <!-- 2. DVD -->
  <g transform="translate(345, 95)">
    <rect width="270" height="380" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#d97706"/>
    <text x="135" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">DVD — 4.7 GB (7x CD)</text>
    
    <!-- Laser Beam Graphic -->
    <polygon points="135,45 95,120 175,120" fill="#f59e0b" opacity="0.3"/>
    <line x1="135" y1="45" x2="135" y2="120" stroke="#f59e0b" stroke-width="2.5"/>
    <text x="135" y="140" font-size="10.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">Red Laser: λ = 650 nm</text>
    
    <text x="15" y="180" font-size="10" font-weight="bold" fill="#fbbf24">• Track Pitch: 0.74 µm</text>
    <text x="15" y="205" font-size="10" font-weight="bold" fill="#fbbf24">• Minimum Pit Length: 0.40 µm</text>
    <text x="15" y="235" font-size="9.5" fill="#cbd5e1">Shorter red wavelength allows smaller beam spot, doubling track density along spiral.</text>
    
    <rect x="15" y="280" width="240" height="70" rx="6" fill="#1e293b"/>
    <text x="25" y="305" font-size="10" font-weight="bold" fill="#fbbf24">Capacity: 4.7 GB – 8.5 GB</text>
    <text x="25" y="325" font-size="9" fill="#94a3b8">Standard-definition movies, PC games</text>
  </g>

  <!-- 3. Blu-ray Disc -->
  <g transform="translate(650, 95)">
    <rect width="270" height="380" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#0284c7"/>
    <text x="135" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Blu-ray Disc (BD) — 25–50 GB</text>
    
    <!-- Laser Beam Graphic -->
    <polygon points="135,45 115,120 155,120" fill="#38bdf8" opacity="0.4"/>
    <line x1="135" y1="45" x2="135" y2="120" stroke="#38bdf8" stroke-width="2"/>
    <text x="135" y="140" font-size="10.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Blue-Violet: λ = 405 nm</text>
    
    <text x="15" y="180" font-size="10" font-weight="bold" fill="#38bdf8">• Track Pitch: 0.32 µm</text>
    <text x="15" y="205" font-size="10" font-weight="bold" fill="#38bdf8">• Minimum Pit Length: 0.15 µm</text>
    <text x="15" y="235" font-size="9.5" fill="#cbd5e1">Ultra-short blue-violet wavelength focuses into a microscopic pinpoint, packing 70x more data.</text>
    
    <rect x="15" y="280" width="240" height="70" rx="6" fill="#1e293b"/>
    <text x="25" y="305" font-size="10" font-weight="bold" fill="#38bdf8">Capacity: 25 GB – 50 GB</text>
    <text x="25" y="325" font-size="9" fill="#94a3b8">4K Ultra HD movies, modern console games</text>
  </g>
</svg>
""")

SVG_BACKUP_AND_TREE = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Data Organization &amp; The 3-2-1 Professional Backup Strategy</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Hierarchical directory file trees paired with resilient multi-tier data protection</text>

  <!-- Left Side: Directory Tree -->
  <g transform="translate(40, 95)">
    <rect width="420" height="380" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="420" height="28" rx="8" fill="#0284c7"/>
    <text x="210" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Hierarchical Directory Tree Structure</text>
    
    <text x="25" y="55" font-size="11" font-family="monospace" fill="#38bdf8">Root Directory (/ or C:\)</text>
    <text x="45" y="80" font-size="10" font-family="monospace" fill="#e2e8f0">├── Documents/</text>
    <text x="65" y="105" font-size="10" font-family="monospace" fill="#34d399">│    ├── ComputerScience/</text>
    <text x="85" y="130" font-size="10" font-family="monospace" fill="#cbd5e1">│    │    ├── Topic4_Storage.docx</text>
    <text x="85" y="155" font-size="10" font-family="monospace" fill="#cbd5e1">│    │    └── binary_calc.py</text>
    <text x="65" y="180" font-size="10" font-family="monospace" fill="#34d399">│    └── Term1_Budget.xlsx</text>
    <text x="45" y="205" font-size="10" font-family="monospace" fill="#e2e8f0">└── Media/</text>
    <text x="65" y="230" font-size="10" font-family="monospace" fill="#fbbf24">     ├── diagram.svg</text>
    <text x="65" y="255" font-size="10" font-family="monospace" fill="#fbbf24">     └── lecture.mp4</text>
    
    <rect x="20" y="290" width="380" height="70" rx="6" fill="#1e293b"/>
    <text x="30" y="315" font-size="10" font-weight="bold" fill="#38bdf8">File Extensions Matter:</text>
    <text x="30" y="335" font-size="9" fill="#cbd5e1">Extensions (.py, .docx, .svg) tell the OS kernel which application must launch to decode that file's binary stream.</text>
  </g>

  <!-- Right Side: The 3-2-1 Backup Rule -->
  <g transform="translate(500, 95)">
    <rect width="420" height="380" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="420" height="28" rx="8" fill="#059669"/>
    <text x="210" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">The 3-2-1 Golden Backup Strategy</text>
    
    <!-- Tier 1: 3 Copies -->
    <rect x="25" y="45" width="370" height="85" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="40" y="70" font-size="12" font-weight="bold" fill="#34d399">3 Copies of Critical Data</text>
    <text x="40" y="90" font-size="9.5" fill="#e2e8f0">• 1 Primary Working Copy + 2 Independent Backups.</text>
    <text x="40" y="110" font-size="9" fill="#94a3b8">Prevents single-point failure if a working drive crashes.</text>
    
    <!-- Tier 2: 2 Different Media Types -->
    <rect x="25" y="145" width="370" height="85" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="40" y="170" font-size="12" font-weight="bold" fill="#38bdf8">2 Different Types of Media</text>
    <text x="40" y="190" font-size="9.5" fill="#e2e8f0">• Example: Local Solid-State NVMe + External Optical/Magnetic Drive.</text>
    <text x="40" y="210" font-size="9" fill="#94a3b8">Protects against technology-specific firmware or controller failures.</text>
    
    <!-- Tier 3: 1 Off-Site Copy -->
    <rect x="25" y="245" width="370" height="85" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="40" y="270" font-size="12" font-weight="bold" fill="#fbbf24">1 Copy Stored Off-Site (Cloud Storage)</text>
    <text x="40" y="290" font-size="9.5" fill="#e2e8f0">• Remote encrypted cloud server data center.</text>
    <text x="40" y="310" font-size="9" fill="#94a3b8">Survives local physical disasters (building fire, flood, or hardware theft).</text>
  </g>
</svg>
""")

SVG_METRIC_AND_DEFRAG = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Storage Capacity Metric Scale &amp; Disk Defragmentation Physics</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Base-2 binary multipliers (1024) paired with HDD physical sector fragmentation mechanics</text>

  <!-- Left: Binary Metric Ladder -->
  <g transform="translate(45, 95)">
    <rect width="420" height="380" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="420" height="28" rx="8" fill="#0284c7"/>
    <text x="210" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">The 1024 Binary Metric Scale Ladder</text>
    
    <g transform="translate(20, 45)">
      <rect y="0" width="380" height="36" rx="4" fill="#1e293b"/>
      <text x="15" y="22" font-size="10" font-weight="bold" fill="#38bdf8">1 Bit (b)</text>
      <text x="130" y="22" font-size="9" fill="#cbd5e1">Single binary digit ($0$ or $1$)</text>

      <rect y="42" width="380" height="36" rx="4" fill="#1e293b"/>
      <text x="15" y="64" font-size="10" font-weight="bold" fill="#38bdf8">1 Byte (B)</text>
      <text x="130" y="64" font-size="9" fill="#cbd5e1">8 bits (Stores 1 text character)</text>

      <rect y="84" width="380" height="36" rx="4" fill="#1e293b"/>
      <text x="15" y="106" font-size="10" font-weight="bold" fill="#38bdf8">1 Kilobyte (KB)</text>
      <text x="130" y="106" font-size="9" fill="#cbd5e1">1024 Bytes ($2^{10}$ Bytes)</text>

      <rect y="126" width="380" height="36" rx="4" fill="#1e293b"/>
      <text x="15" y="148" font-size="10" font-weight="bold" fill="#38bdf8">1 Megabyte (MB)</text>
      <text x="130" y="148" font-size="9" fill="#cbd5e1">1024 KB ($2^{20}$ Bytes)</text>

      <rect y="168" width="380" height="36" rx="4" fill="#1e293b"/>
      <text x="15" y="190" font-size="10" font-weight="bold" fill="#38bdf8">1 Gigabyte (GB)</text>
      <text x="130" y="190" font-size="9" fill="#cbd5e1">1024 MB ($2^{30}$ Bytes)</text>

      <rect y="210" width="380" height="36" rx="4" fill="#1e293b"/>
      <text x="15" y="232" font-size="10" font-weight="bold" fill="#38bdf8">1 Terabyte (TB)</text>
      <text x="130" y="232" font-size="9" fill="#cbd5e1">1024 GB ($2^{40}$ Bytes)</text>

      <rect y="252" width="380" height="36" rx="4" fill="#1e293b"/>
      <text x="15" y="274" font-size="10" font-weight="bold" fill="#38bdf8">1 Petabyte (PB)</text>
      <text x="130" y="274" font-size="9" fill="#cbd5e1">1024 TB ($2^{50}$ Bytes)</text>
    </g>

    <text x="210" y="360" font-size="10.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">Rule: Multiply by 1024 Going Down; Divide Going Up</text>
  </g>

  <!-- Right: HDD Defrag vs SSD Wear Leveling -->
  <g transform="translate(495, 95)">
    <rect width="420" height="380" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="420" height="28" rx="8" fill="#059669"/>
    <text x="210" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">HDD Fragmentation vs. SSD Wear-Leveling</text>

    <!-- HDD -->
    <rect x="25" y="45" width="370" height="135" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
    <text x="35" y="70" font-size="11" font-weight="bold" fill="#fbbf24">1. Magnetic HDD Fragmentation</text>
    <text x="35" y="92" font-size="9.5" fill="#cbd5e1">• Over time, files split into non-contiguous sectors.</text>
    <text x="35" y="112" font-size="9.5" fill="#cbd5e1">• Mechanical read/write head must jump across spinning platters, causing high access latency.</text>
    <text x="35" y="132" font-size="9.5" fill="#34d399">• <tspan font-weight="bold">Fix:</tspan> Run Disk Defragmenter to group file pieces into adjacent physical tracks.</text>

    <!-- SSD -->
    <rect x="25" y="195" width="370" height="165" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
    <text x="35" y="220" font-size="11" font-weight="bold" fill="#f87171">2. Why You Must NEVER Defragment an SSD!</text>
    <text x="35" y="242" font-size="9.5" fill="#cbd5e1">• Solid-state drives have zero moving heads; accessing scattered semiconductor blocks takes equal time (&lt; 0.1 ms).</text>
    <text x="35" y="275" font-size="9.5" fill="#f87171">• Defragmenting forces thousands of unnecessary write cycles that degrade NAND flash oxide layers.</text>
    <text x="35" y="308" font-size="9.5" fill="#38bdf8">• <tspan font-weight="bold">SSD Solution:</tspan> TRIM commands and automatic Wear-Leveling algorithms manage flash health safely.</text>
  </g>
</svg>
""")

# =====================================================================
# LESSON DATA SPECIFICATION: TOPIC 4
# =====================================================================

def build_topic4_curriculum():
    return [
        # -------------------------------------------------------------
        # LESSON 7: Storage Concepts and Storage Media
        # -------------------------------------------------------------
        {
            "unit_order": 1,
            "unit_name": "Storage Concepts and Storage Media",
            "unit_description": "Primary storage vs secondary auxiliary storage, RAM technologies (DRAM 1T-1C charge leaks vs SRAM flip-flop cache), ROM bootstrap POST sequence, magnetic HDDs, optical media laser wavelengths (CD, DVD, Blu-ray), NAND flash SSDs, and cloud storage.",
            "lesson_title": "Storage Concepts and Storage Media",
            "pages": [
                # Card 1: Hook & Goals
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Storage Concepts & Media",
                        "content": {
                            "title": "What We Will Master in This Lesson",
                            "goals": [
                                "Define **Storage**, **Primary Storage (Main Memory)**, and **Secondary Storage**.",
                                "Analyze the semiconductor physics of **DRAM** (refresh cycles) vs. **SRAM** (static flip-flops).",
                                "Explain the bootstrap **POST (Power-On Self-Test)** sequence stored in motherboard **ROM BIOS/UEFI**.",
                                "Examine secondary media physics: **Magnetic HDDs** (spinning platters), **Optical Discs** (laser wavelengths), and **Solid-State NAND Flash** (floating gate transistors).",
                                "Analyze remote cloud storage security: data mirroring redundancy and encryption."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 'Study Desk vs. Filing Cabinet' Analogy",
                        "content": {
                            "title": "Working Workspace vs Long-Term Archiving",
                            "text": "Imagine sitting at a small study desk. To write your term paper, you have two open reference textbooks right in front of you. You can read and write in them instantly because they are right on your desktop. However, the desk is small; it cannot hold 50 books.\n\nIn the corner of the room stands a large metal **Filing Cabinet** holding hundreds of files. Walking over to search for a folder takes minutes, but when you switch off the classroom lights and go home, everything safely locked in the filing cabinet remains forever.\n\n- **Primary Storage (Main RAM)** is your fast, temporary **Study Desk** (holds active code; volatile).\n- **Secondary Storage (SSD/HDD)** is your permanent, high-capacity **Filing Cabinet** (non-volatile)."
                        }
                    }
                ],
                # Card 2: RAM Engineering — DRAM vs SRAM
                [
                    {
                        "type": "concept_explanation",
                        "title": "Under the Hood: DRAM vs. SRAM Semiconductor Physics",
                        "content": {
                            "title": "Capacitor Charge Leaks vs Bistable Transistor Latches",
                            "text": "All RAM is volatile, but the semiconductor circuits used for system memory vs CPU cache are radically different:\n\n### 1. Dynamic RAM (DRAM)\n- **Circuit Architecture**: 1 Transistor + 1 Microscopic Capacitor per bit.\n- **The Charge Leak Problem**: Microscopic capacitors behave like tiny buckets with pinholes: their electrical charge leaks away in milliseconds. DRAM must be **periodically refreshed** (read and recharged) hundreds of times per second.\n- **Role**: High density and low cost make DRAM ideal for **Main System RAM** (8GB to 64GB).\n\n### 2. Static RAM (SRAM)\n- **Circuit Architecture**: 4 to 6 interconnected transistors forming a cross-coupled **flip-flop latch**.\n- **No Refresh Needed**: The circuit locks its voltage state indefinitely as long as power flows.\n- **Role**: Near-instant access (&lt; 2 ns) makes SRAM ideal for **CPU Cache Memory (L1/L2/L3)**."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Semiconductor Circuit Schematics: DRAM vs. SRAM",
                        "content": {
                            "svg_content": SVG_DRAM_VS_SRAM,
                            "caption": "Comparison of DRAM's 1-Transistor 1-Capacitor leaky memory cell against SRAM's 6-Transistor static flip-flop latch."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "DRAM vs. SRAM Engineering Comparison",
                        "content": {
                            "headers": ["Characteristic", "Dynamic RAM (DRAM)", "Static RAM (SRAM)"],
                            "rows": [
                                ["**Components per Bit**", "1 Transistor + 1 Capacitor (1T-1C)", "4 to 6 Transistors (Flip-Flop)"],
                                ["**Refresh Cycle Needed?**", "Yes (hundreds of times per second)", "No (holds state statically without refresh)"],
                                ["**Access Speed**", "Moderate (50 – 80 nanoseconds)", "Extreme (&lt; 2 nanoseconds)"],
                                ["**Cost & Density**", "Very cheap per gigabyte, high density", "Expensive per megabyte, low density"],
                                ["**Primary Application**", "Main System Memory (DDR4/DDR5 modules)", "CPU Cache Memory (L1, L2, L3 on-die)"]
                            ]
                        }
                    }
                ],
                # Card 3: ROM Technologies & The Bootstrap Sequence
                [
                    {
                        "type": "concept_explanation",
                        "title": "ROM Technologies and the Bootstrapping POST Sequence",
                        "content": {
                            "title": "How a Computer Wakes Up From Complete Blackness",
                            "text": "When you turn on a computer, the CPU starts with empty registers and blank RAM. How does it know how to load the Operating System?\n\n- **Read-Only Memory (ROM)** is non-volatile chip memory holding the **BIOS / UEFI firmware**.\n- **The POST (Power-On Self-Test)**: The CPU immediately executes firmware in ROM to verify that RAM modules, system clocks, graphics adapters, and storage drives are functioning properly.\n- **Bootloader Handoff**: Once POST passes, the BIOS locates the boot drive (SSD/HDD), loads the OS bootloader into RAM, and hands over control.\n\n### Evolution of ROM Types\n1. **PROM (Programmable ROM)**: Manufactured blank; written once by blowing microscopic internal fuses with a chip burner.\n2. **EPROM (Erasable PROM)**: Features a transparent quartz window; erased by exposing the chip to intense ultraviolet (UV) light.\n3. **EEPROM (Electrically Erasable PROM)**: Erased and rewritten electronically byte-by-byte in motherboard flash updates ('Flashing the BIOS')."
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Step-by-Step Computational Trace: The POST Bootstrap Sequence & Memory Handoff",
                        "content": {
                            "title": "Tracing Computer Initialization from Cold Power-On",
                            "problem": "Trace the step-by-step diagnostic and memory allocation execution flow when an operator presses the computer power button.",
                            "steps": [
                                "**Step 1: Power Good Signal & CPU Reset**:\nPower supply stabilizes and sends a +5V 'Power Good' signal to the motherboard. The CPU Program Counter (PC) initializes to the hardcoded reset vector address (`0xFFFF0`) mapped to motherboard ROM BIOS/UEFI.",
                                "**Step 2: Power-On Self-Test (POST) Execution**:\nThe CPU executes diagnostic firmware in ROM: checks CPU registers, tests RAM integrity by writing and reading test bit patterns, verifies system timer clocks, and initializes GPU display controllers.",
                                "**Step 3: Boot Device Priority Search**:\nBIOS/UEFI checks configured boot order (NVMe SSD, SATA HDD, USB drive) and reads the Master Boot Record (MBR) or EFI System Partition.",
                                "**Step 4: Bootloader RAM Loading & Kernel Handoff**:\nThe tiny secondary bootloader program is copied from storage into system RAM at address `0x7C00`. The CPU jumps execution to this RAM address, which then initializes the OS Kernel."
                            ]
                        }
                    }
                ],
                # Card 4: Magnetic Storage (Hard Disk Drives)
                [
                    {
                        "type": "concept_explanation",
                        "title": "Magnetic Storage: Hard Disk Drives (HDD)",
                        "content": {
                            "title": "Spinning Platters and Aerodynamic Floating Heads",
                            "text": "Hard Disk Drives store data by magnetizing microscopic cobalt alloy grains on spinning aluminum or glass **platters**:\n\n- **Physical Mechanics**: Platters spin at speeds up to 7,200 Revolutions Per Minute (RPM). A tiny electromagnetic **read/write head** on an actuator arm glides nanometers above the surface, floating on a cushion of air.\n- **Writing**: Electric current through the head's coil creates a localized magnetic field, aligning magnetic particles in binary orientations ($0$ or $1$).\n- **Reading**: Moving magnetic fields induce tiny currents in the head coil.\n- **The Head Crash Vulnerability**: Because the head floats mere nanometers above high-speed platters, physical shocks, drops, or dust particles can cause the head to scrape the magnetic coating, destroying data permanently."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Disassembled Magnetic Hard Disk Drive Internals",
                        "content": {
                            "title": "Disassembled Magnetic Hard Disk Drive Internals",
                            "caption": "An open hard disk drive showing mirror-polished magnetic platters, the spindle motor, and the actuator arm carrying the delicate read/write head.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Laptop-hard-drive-exposed.jpg/800px-Laptop-hard-drive-exposed.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    }
                ],
                # Card 5: Optical Media & Laser Wavelength Physics
                [
                    {
                        "type": "concept_explanation",
                        "title": "Optical Media: Laser Wavelengths, Pits, and Lands",
                        "content": {
                            "title": "Why Blu-ray Packs 70x More Data Than a CD",
                            "text": "Optical discs (CD, DVD, Blu-ray) store binary data along a microscopic spiral track as physical depressions (**pits**) and flat reflective surfaces (**lands**).\n\n- **Reading Pits & Lands**: A laser beam reflects off flat lands straight back to a photodiode sensor ($1$). When it strikes a pit, light scatters ($0$).\n- **The Laser Wavelength Law**: The diameter of a focused laser spot is directly proportional to its wavelength ($\\lambda$):\n  - **CD (780 nm Red Laser)** $\\longrightarrow$ Broad beam spot $\\longrightarrow$ Large pits $\\longrightarrow$ **700 MB**.\n  - **DVD (650 nm Red Laser)** $\\longrightarrow$ Medium beam spot $\\longrightarrow$ Medium pits $\\longrightarrow$ **4.7 GB**.\n  - **Blu-ray (405 nm Blue-Violet Laser)** $\\longrightarrow$ Microscopic pinpoint $\\longrightarrow$ Ultra-dense pits $\\longrightarrow$ **25 GB to 50 GB** on the exact same disc size!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Optical Storage Laser Wavelengths & Pit Density",
                        "content": {
                            "svg_content": SVG_OPTICAL_WAVELENGTHS,
                            "caption": "Comparison of CD (780nm Red), DVD (650nm Red), and Blu-ray (405nm Blue-Violet) laser spot sizes and spiral track densities."
                        }
                    }
                ],
                # Card 6: Solid-State Flash Media & Floating Gate Transistors
                [
                    {
                        "type": "concept_explanation",
                        "title": "Solid-State Drives (SSD) & NAND Flash Memory",
                        "content": {
                            "title": "Trapping Electrons in Floating Gate Transistors",
                            "text": "Solid-State Drives have **no moving parts**. They store binary data electronically inside semiconductor **floating-gate transistors**:\n\n- **Programming (Writing)**: A high voltage forces electrons to tunnel through an insulating oxide layer into a 'floating gate' trap, where they remain locked without electrical power.\n- **Reading**: Trapped electrons create an electrostatic field that blocks electrical current through the transistor channel, reading as binary $0$.\n- **Advantages**: Shock-resistant (no head crashes), silent, low power draw, and access times 1,000x faster than spinning mechanical hard drives.\n- **Write Endurance (TBW)**: Forcing electrons through oxide layers degrades the insulation over thousands of cycles. Modern SSD controllers use **wear leveling** algorithms to distribute write cycles evenly across all memory blocks."
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Calculating Solid-State Drive (SSD) Lifespan and Terabytes Written (TBW)",
                        "content": {
                            "title": "Estimating Flash Drive Write Endurance",
                            "problem": "A video workstation writes an average of 80 GB of video footage per day onto a 500 GB NVMe SSD. The manufacturer rates the drive with an endurance rating of 300 TBW (Terabytes Written). Calculate the estimated operating lifespan of the SSD before wear-out.",
                            "steps": [
                                "**Step 1: Convert Drive Endurance from TB to GB**:\n$$\\text{Total Endurance in GB} = 300 \\text{ TB} \\times 1024 \\text{ GB/TB} = 307,200 \\text{ GB}$$",
                                "**Step 2: Calculate Total Expected Operating Days**:\n$$\\text{Lifespan (Days)} = \\frac{307,200 \\text{ GB}}{80 \\text{ GB/day}} = 3,840 \\text{ days}$$",
                                "**Step 3: Convert Days to Operating Years**:\n$$\\text{Lifespan (Years)} = \\frac{3,840 \\text{ days}}{365 \\text{ days/year}} = \\mathbf{10.52 \\text{ years}}$$\n*Conclusion*: With intelligent wear-leveling spreading writes across all flash blocks, the SSD will comfortably operate for over 10 years."
                            ]
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "High-Speed M.2 NVMe Solid State Drive (SSD)",
                        "content": {
                            "title": "High-Speed M.2 NVMe Solid State Drive (SSD)",
                            "caption": "An M.2 NVMe Solid State Drive showing the central flash memory controller chip and dense black NAND flash silicon packages.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Samsung_SSD_970_EVO_Plus_250GB.jpg/800px-Samsung_SSD_970_EVO_Plus_250GB.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    }
                ],
                # Card 7: Cloud Storage Infrastructure & Security
                [
                    {
                        "type": "concept_explanation",
                        "title": "Cloud Storage: Infrastructure, Redundancy, and Security",
                        "content": {
                            "title": "How Remote Server Farms Keep Your Files Safe",
                            "text": "Cloud storage (e.g. Google Drive, OneDrive) saves files onto remote server farms connected via the internet:\n\n- **Client-Server Flow**: Dragging a file to cloud storage sends HTTPS data packets across the internet to enterprise storage arrays.\n- **Data Redundancy**: Providers mirror (replicate) files across multiple independent drives and different geographical data centers. If an entire server building loses power, another replica takes over instantly.\n- **Multi-Layer Encryption**: Data is encrypted **in transit** (SSL/TLS) to prevent wiretapping and **at rest** (AES-256) on physical server disks.\n- **Physical Data Center Security**: Armed guards, biometric scanners, automated fire suppression, and backup diesel generators ensure 99.999% uptime."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Modern Cloud Data Center Enterprise Server Racks",
                        "content": {
                            "title": "Modern Cloud Data Center Enterprise Server Racks",
                            "caption": "A high-density enterprise cloud data center featuring rows of server racks with redundant power supplies, fiber-optic networking, and climate control.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Datacenter_wikimedia_01.jpg/800px-Datacenter_wikimedia_01.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    }
                ],
                # Card 8: Educational Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Computer Storage Explained: RAM, SSDs, and Hard Drives",
                        "content": {
                            "title": "How Computer Memory and Storage Work",
                            "youtube_id": "p3q5zWCw8J4",
                            "url": "https://www.youtube.com/watch?v=p3q5zWCw8J4",
                            "description": "A comprehensive visual breakdown comparing volatile DRAM memory, magnetic HDD spinning platters, and solid-state NAND flash floating gates."
                        }
                    }
                ],
                # Card 9: Formative Knowledge Checks & Key Takeaways
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 1: DRAM Refresh Cycle",
                        "content": {
                            "question": "Why does Dynamic RAM (DRAM) require periodic refreshing hundreds of times per second?",
                            "options": [
                                "The magnetic platters slow down if not spun by electric pulses",
                                "Its microscopic capacitors leak their electrical charge over time and must be recharged",
                                "To clear user passwords from the BIOS firmware",
                                "Because solid-state floating gates melt at room temperature"
                            ],
                            "correct": "B",
                            "explanation": "DRAM stores each bit in a microscopic capacitor that steadily leaks charge. Without periodic refresh cycles, stored binary data would decay into zeros."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 2: Blu-ray Capacity Advantage",
                        "content": {
                            "question": "How does a Blu-ray disc store significantly more data than a standard DVD on the exact same physical disc size?",
                            "options": [
                                "Blu-ray uses double-sided magnetic heads that spin at 7200 RPM",
                                "Blu-ray uses a shorter wavelength blue-violet laser (405 nm), focusing into a much smaller pinpoint that packs pits tightly together",
                                "Blu-ray discs do not use pits and lands",
                                "Blu-ray uses static RAM flip-flops embedded in plastic"
                            ],
                            "correct": "B",
                            "explanation": "The 405 nm blue-violet laser has a shorter wavelength than a DVD's 650 nm red laser, allowing microscopic pits and tracks to be packed with 5x higher density."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 3: POST Boot Sequence",
                        "content": {
                            "question": "What critical diagnostic process occurs during the initial bootstrap phase when a computer is powered on?",
                            "options": [
                                "The computer copies all hard drive files into the cloud",
                                "Motherboard ROM executes the Power-On Self-Test (POST) to verify that RAM, CPU registers, and hardware are functional",
                                "The CPU defragments the operating system partition",
                                "The monitor discharges all static electricity"
                            ],
                            "correct": "B",
                            "explanation": "The POST (Power-On Self-Test) stored in ROM BIOS/UEFI checks system hardware integrity before loading the OS bootloader into RAM."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 4: Solid-State Flash Endurance & Wear Leveling",
                        "content": {
                            "question": "What is the primary function of wear-leveling algorithms in Solid-State Drive (SSD) controllers?",
                            "options": [
                                "To spin the magnetic platters at uniform rotational speeds",
                                "To distribute data write and erase cycles evenly across all NAND flash memory blocks to prevent premature cell failure",
                                "To compress video files before writing to optical discs",
                                "To continuously refresh DRAM capacitors to prevent bit leakage"
                            ],
                            "correct": "B",
                            "explanation": "Because NAND flash floating-gate oxide layers degrade after repeated program/erase cycles, wear-leveling algorithms ensure write cycles are evenly distributed across all physical blocks, maximizing the drive's operating lifespan."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Lesson 7 Key Takeaways",
                        "content": {
                            "text": "1. **Primary vs Secondary**: RAM is fast, volatile working memory; SSD/HDD is permanent, non-volatile auxiliary storage.\n2. **DRAM vs SRAM**: DRAM (1T-1C, leaks charge, needs refresh, cheap main RAM); SRAM (6T flip-flop, static, ultra-fast CPU cache).\n3. **Booting**: ROM holds BIOS/UEFI firmware executing the POST hardware self-test.\n4. **Optical Media**: Shorter laser wavelengths (Blu-ray 405nm) allow denser pit spacing.\n5. **SSDs**: Uses NAND flash floating gates; wear leveling ensures even cell write distribution."
                        }
                    }
                ]
            ]
        },

        # -------------------------------------------------------------
        # LESSON 8: Data Organization, Capacity, and Storage Management
        # -------------------------------------------------------------
        {
            "unit_order": 2,
            "unit_name": "Data Organization, Capacity, and Storage Management",
            "unit_description": "Metric units of storage (bit, byte, KB, MB, GB, TB, PB with base-2 1024 math), multi-step capacity allocation calculations, network transfer bandwidth math, file directory trees, disk cleanup, HDD defragmentation vs SSD safety, and the 3-2-1 backup strategy.",
            "lesson_title": "Data Organization, Capacity, and Storage Management",
            "pages": [
                # Card 1: Hook & Metric Units
                [
                    {
                        "type": "suggested_image",
                        "title": "Enterprise Server Rack with Redundant Disk Array Enclosures",
                        "content": {
                            "title": "Enterprise Server Rack with Redundant Disk Array Enclosures",
                            "caption": "An enterprise storage server rack housing hot-swappable enterprise magnetic drive bays configured in redundant RAID arrays for continuous mission-critical data protection.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Server_rack_with_disk_enclosure.jpg/800px-Server_rack_with_disk_enclosure.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Storage Math & Management",
                        "content": {
                            "title": "What We Will Master in This Lesson",
                            "goals": [
                                "Master the binary metric storage scale (**Bit**, **Byte**, **KB**, **MB**, **GB**, **TB**, **PB**) using powers of 2 ($1024$).",
                                "Perform multi-step storage capacity conversions and file capacity allocation calculations.",
                                "Calculate network bandwidth file transfer times distinguishing between Bytes ($B$) and bits ($b$).",
                                "Explain hierarchical directory trees and file extension associations.",
                                "Evaluate storage maintenance utilities (**Disk Cleanup**, **Defragmentation** on HDD vs. why never on SSD).",
                                "Apply the **3-2-1 Professional Backup Strategy** to institutional data security scenarios."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Metric Units of Digital Storage",
                        "content": {
                            "title": "Powers of 2 vs. Decimal Confusion",
                            "text": "In computer science, memory is physically addressed using binary lines ($2^n$). Therefore, binary metric prefixes scale by **1024** ($2^{10}$) rather than 1,000:\n\n- **Bit (b)**: Smallest binary unit ($0$ or $1$).\n- **Byte (B)**: Group of **8 bits** (stores 1 text character, e.g. 'A' = `01000001`).\n- **Kilobyte (KB)**: $1024 \\text{ Bytes}$ ($2^{10}$ Bytes).\n- **Megabyte (MB)**: $1024 \\text{ Kilobytes}$ ($2^{20}$ Bytes).\n- **Gigabyte (GB)**: $1024 \\text{ Megabytes}$ ($2^{30}$ Bytes).\n- **Terabyte (TB)**: $1024 \\text{ Gigabytes}$ ($2^{40}$ Bytes).\n- **Petabyte (PB)**: $1024 \\text{ Terabytes}$ ($2^{50}$ Bytes).\n\n### The Golden Conversion Rule\n- **Larger Unit $\\longrightarrow$ Smaller Unit**: **Multiply** by $1024$ (e.g. $\\text{GB} \\rightarrow \\text{MB}$).\n- **Smaller Unit $\\longrightarrow$ Larger Unit**: **Divide** by $1024$ (e.g. $\\text{KB} \\rightarrow \\text{MB}$)."
                        }
                    }
                ],
                # Card 2: Storage Arithmetic Walkthroughs
                [
                    {
                        "type": "worked_example",
                        "title": "Storage Arithmetic Walkthroughs: Multi-Step & Capacity",
                        "content": {
                            "title": "Solving Real-World Storage Math Problems",
                            "problem": "Problem A: Convert 3.5 GB into Kilobytes (KB).\nProblem B: How many 4.5 MB photos can fit onto a freshly formatted 16 GB USB flash drive?",
                            "steps": [
                                "**Problem A Solution (Multi-Step Conversion)**:\n1. Convert GB to MB: $3.5 \\text{ GB} \\times 1024 = 3,584 \\text{ MB}$.\n2. Convert MB to KB: $3,584 \\text{ MB} \\times 1024 = \\mathbf{3,670,016 \\text{ KB}}$.",
                                "**Problem B Solution (Capacity Allocation)**:\n1. Convert flash drive capacity to MB: $16 \\text{ GB} \\times 1024 = 16,384 \\text{ MB}$.\n2. Divide total MB by size per photo: $\\frac{16,384 \\text{ MB}}{4.5 \\text{ MB}} = 3640.888...$\n3. Round down to whole integers: **3,640 complete photos** (files cannot be stored as partial fractions)."
                            ]
                        }
                    }
                ],
                # Card 3: Network Bandwidth Transfer Time
                [
                    {
                        "type": "worked_example",
                        "title": "Network Transfer Time: Bytes vs. Bits Bandwidth Math",
                        "content": {
                            "title": "Calculating Download and Streaming Times",
                            "problem": "How long will it take to download a 120 MB application over a stable 16 Mbps (Megabits per second) internet connection?",
                            "steps": [
                                "**Critical Concept**: File sizes are measured in **Bytes (capital B)**, but internet bandwidth speeds are measured in **bits (lowercase b)**!",
                                "**Step 1: Convert File Size from Megabytes to Megabits**:\n$$\\text{Size in Mb} = 120 \\text{ MB} \\times 8 \\text{ bits/Byte} = 960 \\text{ Megabits (Mb)}$$",
                                "**Step 2: Divide by Connection Bandwidth**:\n$$\\text{Download Time} = \\frac{960 \\text{ Mb}}{16 \\text{ Mbps}} = \\mathbf{60 \\text{ seconds (1.0 minute)}}$$"
                            ]
                        }
                    }
                ],
                # Card 4: Data Organization & Directory Trees
                [
                    {
                        "type": "concept_explanation",
                        "title": "Data Organization: Files, Extensions, and Hierarchical Trees",
                        "content": {
                            "title": "How Operating Systems Organize Data Sectors",
                            "text": "Operating systems organize physical drive sectors into logical structures:\n\n- **File**: A named collection of related data. Every file has a **file extension** (e.g. `.py`, `.docx`, `.svg`, `.mp4`) that informs the OS which application must decode its binary format.\n- **Folder (Directory)**: A virtual container grouping files and subfolders into a hierarchical 'tree structure' originating from the **Root Directory** (`/` on Linux/Mac or `C:\\` on Windows)."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Directory File Trees & The 3-2-1 Backup Strategy",
                        "content": {
                            "svg_content": SVG_BACKUP_AND_TREE,
                            "caption": "Hierarchical directory root tree organization paired with the 3-2-1 Professional Backup Strategy."
                        }
                    }
                ],
                # Card 5: Storage Utilities (Cleanup & Defrag)
                [
                    {
                        "type": "concept_explanation",
                        "title": "Storage Maintenance: Disk Cleanup & Defragmentation",
                        "content": {
                            "title": "Keeping Drives Fast and Healthy",
                            "text": "### 1. Disk Cleanup\nA system maintenance utility that scans drives for temporary cache files, abandoned installer packages, and Recycle Bin items, safely deleting them to reclaim valuable space.\n\n### 2. Disk Defragmentation (HDDs ONLY)\n- Over time, files written to magnetic spinning platters become broken into non-continuous fragments scattered across different sectors.\n- The mechanical drive head has to physically hop around the platter to read a single file, causing severe lag.\n- **Defragmentation** reorganizes scattered file clusters into contiguous physical sectors, minimizing mechanical head movement and restoring speed.\n\n### CRITICAL CAUTION: NEVER Defragment a Solid-State Drive (SSD)!\nSSDs have zero moving heads; accessing scattered semiconductor cells takes the exact same speed. Defragmenting an SSD forces thousands of unnecessary write cycles, wearing down the delicate oxide layers of flash cells and **permanently shortening the drive's lifespan**!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Binary Metric Scale & Disk Defragmentation Mechanics",
                        "content": {
                            "svg_content": SVG_METRIC_AND_DEFRAG,
                            "caption": "Binary metric prefix ladder ($1024$) and comparative breakdown of HDD platter defragmentation vs SSD wear-leveling."
                        }
                    }
                ],
                # Card 6: The 3-2-1 Backup Strategy & Precautions
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 3-2-1 Professional Backup Rule & Drive Handling",
                        "content": {
                            "title": "The Industry Standard for Data Protection",
                            "text": "A **Backup** is an independent duplicate copy of active data stored on a separate physical medium.\n\n### The 3-2-1 Golden Rule\n- **3 Copies of Data**: Maintain the active primary file and at least 2 independent backup copies.\n- **2 Different Storage Media**: Store backups on 2 different hardware formats (e.g. local NVMe SSD + external magnetic/optical drive) to protect against media-specific controller failures.\n- **1 Off-Site Location**: Keep at least 1 backup physically outside the building (e.g. encrypted cloud storage). If a fire, flood, or theft destroys local equipment, the cloud copy remains 100% safe.\n\n### Storage Peripheral Handling Precautions\n1. **Always Safely Eject (Unmount)**: OS write-caching holds data in temporary RAM buffers. Unplugging prematurely corrupts the file allocation table!\n2. **Magnetic Shielding**: Keep HDDs away from heavy speaker magnets to prevent scrambling magnetic platter particles.\n3. **Environmental Care**: Protect devices from moisture, excessive heat, and dust accumulation."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Enterprise Automated Tape Library for Long-Term Archiving",
                        "content": {
                            "title": "Enterprise Automated Tape Library for Long-Term Archiving",
                            "caption": "An automated robotic magnetic tape library in an enterprise data center, managing petabytes of offline archival storage as part of a 3-2-1 backup strategy.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/StorageTek_Tape_Library.jpg/800px-StorageTek_Tape_Library.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    }
                ],
                # Card 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "File Systems, Disk Defragmentation & 3-2-1 Backups",
                        "content": {
                            "title": "File Systems, Defrag, and Backup Rules",
                            "youtube_id": "KN8YgJnShPM",
                            "url": "https://www.youtube.com/watch?v=KN8YgJnShPM",
                            "description": "An engaging visual guide showing how files fragment on spinning hard drives, why SSDs don't need defrag, and how the 3-2-1 backup rule prevents data disaster."
                        }
                    }
                ],
                # Card 8: National Exam Backup Scenario & Summative Assessment
                [
                    {
                        "type": "worked_example",
                        "title": "Summative Scenario: National Examination Council Backup Architecture",
                        "content": {
                            "title": "Securing 10,000 Scanned Exam Scripts",
                            "problem": "KNEC needs to store and safeguard scanned exam scripts for 10,000 candidates. Each student's scanned PDF script averages 2 MB in size.",
                            "steps": [
                                "**Step 1: Calculate Total Primary Storage Required**:\n$$\\text{Total Size} = 10,000 \\times 2 \\text{ MB} = 20,000 \\text{ MB}$$\n$$\\text{In Gigabytes} = \\frac{20,000 \\text{ MB}}{1024 \\text{ MB/GB}} = \\mathbf{19.53 \\text{ GB}}$$",
                                "**Step 2: Formulate 3-2-1 Backup Strategy**:\n- **Copy 1 (Active)**: Local high-speed NVMe SSD server in the central examination hall.\n- **Copy 2 (On-Site Backup)**: External high-capacity magnetic HDD array stored in a fireproof on-site vault.\n- **Copy 3 (Off-Site Backup)**: AES-256 encrypted cloud storage repository mirrored across secondary government data centers in Nairobi and Mombasa."
                            ]
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 1: SSD Defragmentation Rule",
                        "content": {
                            "question": "Why should users NEVER perform disk defragmentation on a Solid-State Drive (SSD)?",
                            "options": [
                                "SSDs have no moving read heads and defragmenting causes unnecessary write cycles that wear down flash memory cells",
                                "Defragmenting an SSD converts binary bits into octal",
                                "SSDs only support floppy disk utilities",
                                "Defragmenting reverses the magnetic polarity of the flash controller"
                            ],
                            "correct": "A",
                            "explanation": "SSDs access all memory cells in equal time without mechanical seek lag. Defragmenting forces thousands of unnecessary writes, wearing down the oxide layers of NAND flash cells."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 2: 3-2-1 Backup Rule",
                        "content": {
                            "question": "According to the 3-2-1 backup strategy, why must at least ONE backup copy be kept off-site in the cloud?",
                            "options": [
                                "To speed up local printer spooling",
                                "To protect against local physical disasters such as building fires, floods, or hardware theft",
                                "Because cloud files are converted directly into ROM",
                                "To eliminate the need for primary RAM"
                            ],
                            "correct": "B",
                            "explanation": "An off-site backup guarantees data recovery even if a catastrophic local event (fire, flood, theft) destroys all on-site computers and local drives."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 3: Binary Scale Conversion",
                        "content": {
                            "question": "How many Megabytes (MB) are in 4 Gigabytes (GB) using binary powers of 2?",
                            "options": [
                                "4,000 MB",
                                "4,096 MB",
                                "40,000 MB",
                                "32,768 MB"
                            ],
                            "correct": "B",
                            "explanation": "$4 \\text{ GB} \\times 1024 \\text{ MB/GB} = 4,096 \\text{ MB}$."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 4: Network Bandwidth vs Storage Capacity Units",
                        "content": {
                            "question": "When calculating file download times across a network, what essential unit conversion factor must be applied between Megabytes (MB) and Megabits (Mb)?",
                            "options": [
                                "Divide by 1024 because network packets use base-2 arithmetic",
                                "Multiply file Megabytes by 8 because there are 8 bits in each Byte",
                                "Multiply by 100 because bandwidth is measured in percentages",
                                "No conversion is needed because 1 Megabyte equals 1 Megabit"
                            ],
                            "correct": "B",
                            "explanation": "Storage capacity and file sizes are measured in Bytes (B), whereas transmission bandwidth speeds are measured in bits (b). Since 1 Byte = 8 bits, file sizes in MB must be multiplied by 8 to convert to Mb before calculating transfer time."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Lesson 8 Key Takeaways",
                        "content": {
                            "text": "1. **Binary Metric Scale**: Scale by $1024$ ($2^{10}$): Byte $\\rightarrow$ KB $\\rightarrow$ MB $\\rightarrow$ GB $\\rightarrow$ TB $\\rightarrow$ PB.\n2. **Bandwidth Transfer Math**: $1 \\text{ Byte} = 8 \\text{ bits}$; always convert MB to Mb before dividing by Mbps.\n3. **Drive Maintenance**: Run Disk Cleanup to clear temporary junk; defragment magnetic HDDs but NEVER defragment SSDs.\n4. **3-2-1 Backup Rule**: 3 total copies $\\longrightarrow$ 2 different media formats $\\longrightarrow$ 1 off-site cloud copy."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_grade10_topic4(replace=True):
    print("=" * 80)
    print("INGESTING TOPIC 4: Computer Storage (Grade 10 Computer Science)")
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
        order=4,
        defaults={"name": "Computer Storage", "description": "Primary storage (RAM, ROM), secondary storage (HDD, optical, SSD), cloud storage, capacity math, and backup management."}
    )
    if not t_created:
        topic.name = "Computer Storage"
        topic.description = "Primary storage (RAM, ROM), secondary storage (HDD, optical, SSD), cloud storage, capacity math, and backup management."
        topic.save()
    print(f"[*] Resolved Topic 4: {topic.name} (ID: {topic.id})")

    if replace:
        print("[*] Replacing existing Topic 4 units, lessons, blocks, and assets...")
        existing_lessons = Lesson.objects.filter(topic=topic)
        LessonAsset.objects.filter(lesson__in=existing_lessons).delete()
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    curriculum_data = build_topic4_curriculum()
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
                    "topic_order": 4,
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
                        block_id=f"g10_cs_t4_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={"topic_order": 4, "unit_order": u_order, "page": page_idx}
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
    print(f"TOPIC 4 INGESTION COMPLETE:")
    print(f"  Units Created:   {total_units}")
    print(f"  Lessons Created: {total_lessons}")
    print(f"  Pages Created:   {total_pages}")
    print(f"  Blocks Created:  {total_blocks}")
    print(f"  Assets Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_grade10_topic4(replace=True)
