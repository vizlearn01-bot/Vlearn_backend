"""
VLearn CBC Grade 10 Computer Science — Topic 6: Operating Systems (OS)
Production Ingestion & Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Computer Science
Topic: Operating Systems (OS) (Topic Order: 6)

Decomposed into 3 Comprehensive Learning Units & 3 Published Lessons:
  1. Operating System Architecture and Process Management (Lesson 1: OS Purpose, Interfaces, and Process & CPU Scheduling)
  2. Memory, File Systems, and Peripheral Device Management (Lesson 2: Memory Management, File Systems, and Peripheral Devices)
  3. Security, Maintenance, Installation & Diagnostics (Lesson 3: OS Security, Utilities, Installation, and Diagnostics)
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
# HIGH PRECISION VECTOR SVGS FOR TOPIC 6
# =====================================================================

SVG_OS_LAYERED_MODEL = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Layered Architecture of a Computer System: The OS as the Core Mediator</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Hardware Abstraction, System Call Interface, and User-Application Interaction</text>

  <!-- Layer 4: Human User (Top) -->
  <g transform="translate(60, 95)">
    <rect width="840" height="60" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <text x="420" y="28" font-size="14" font-weight="bold" fill="#c084fc" text-anchor="middle">1. HUMAN USERS</text>
    <text x="420" y="48" font-size="11" fill="#e2e8f0" text-anchor="middle">End Users • System Administrators • Programmers • Operators</text>
  </g>

  <!-- Transition Arrow 1 -->
  <g transform="translate(480, 155)">
    <line x1="0" y1="0" x2="0" y2="25" stroke="#a855f7" stroke-width="3" stroke-dasharray="4"/>
    <polygon points="-5,25 5,25 0,32" fill="#a855f7"/>
    <text x="70" y="18" font-size="10.5" fill="#94a3b8" text-anchor="start">GUI / CLI Interaction</text>
  </g>

  <!-- Layer 3: Application Software -->
  <g transform="translate(60, 190)">
    <rect width="840" height="65" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="420" y="26" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">2. APPLICATION SOFTWARE</text>
    <text x="420" y="48" font-size="11" fill="#cbd5e1" text-anchor="middle">Web Browsers (Chrome, Firefox) • Word Processors • Compilers • Video Games • Databases</text>
  </g>

  <!-- Transition Arrow 2 -->
  <g transform="translate(480, 255)">
    <line x1="0" y1="0" x2="0" y2="25" stroke="#38bdf8" stroke-width="3"/>
    <polygon points="-5,25 5,25 0,32" fill="#38bdf8"/>
    <text x="70" y="18" font-size="10.5" font-weight="bold" fill="#38bdf8" text-anchor="start">System Calls (API: open, read, fork, write)</text>
  </g>

  <!-- Layer 2: Operating System Kernel -->
  <g transform="translate(60, 290)">
    <rect width="840" height="85" rx="10" fill="#0369a1" stroke="#0ea5e9" stroke-width="2"/>
    <text x="420" y="25" font-size="15" font-weight="bold" fill="#ffffff" text-anchor="middle">3. OPERATING SYSTEM (KERNEL &amp; SYSTEM SERVICES)</text>
    
    <!-- Sub-managers -->
    <g transform="translate(20, 38)">
      <rect x="0" y="0" width="185" height="35" rx="6" fill="#0c4a6e"/>
      <text x="92" y="22" font-size="10.5" font-weight="bold" fill="#7dd3fc" text-anchor="middle">Process Scheduler</text>
      
      <rect x="200" y="0" width="185" height="35" rx="6" fill="#0c4a6e"/>
      <text x="292" y="22" font-size="10.5" font-weight="bold" fill="#7dd3fc" text-anchor="middle">Memory Manager</text>

      <rect x="400" y="0" width="185" height="35" rx="6" fill="#0c4a6e"/>
      <text x="492" y="22" font-size="10.5" font-weight="bold" fill="#7dd3fc" text-anchor="middle">File System Manager</text>

      <rect x="600" y="0" width="185" height="35" rx="6" fill="#0c4a6e"/>
      <text x="692" y="22" font-size="10.5" font-weight="bold" fill="#7dd3fc" text-anchor="middle">I/O &amp; Device Drivers</text>
    </g>
  </g>

  <!-- Transition Arrow 3 -->
  <g transform="translate(480, 375)">
    <line x1="0" y1="0" x2="0" y2="25" stroke="#34d399" stroke-width="3"/>
    <polygon points="-5,25 5,25 0,32" fill="#34d399"/>
    <text x="70" y="18" font-size="10.5" font-weight="bold" fill="#34d399" text-anchor="start">Device Drivers &amp; Memory Bus Control</text>
  </g>

  <!-- Layer 1: Physical Hardware (Bottom) -->
  <g transform="translate(60, 410)">
    <rect width="840" height="75" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <text x="420" y="26" font-size="14" font-weight="bold" fill="#34d399" text-anchor="middle">4. PHYSICAL HARDWARE INFRASTRUCTURE</text>
    <text x="420" y="52" font-size="11" fill="#94a3b8" text-anchor="middle">Central Processing Unit (CPU) • Primary RAM • Secondary Storage (SSD/HDD) • GPU • Network &amp; Peripherals</text>
  </g>
</svg>
""")

SVG_CLI_VS_GUI = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 500" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="470" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">User Interface Paradigms: Command-Line (CLI) vs. Graphical (GUI)</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Mechanical trade-offs, resource consumption, and administrative use-cases</text>

  <!-- Left: Command Line Interface -->
  <g transform="translate(40, 85)">
    <rect width="420" height="375" rx="12" fill="#020617" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="420" height="32" rx="8" fill="#0369a1"/>
    <text x="210" y="21" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">Command-Line Interface (CLI)</text>
    
    <!-- Terminal window simulation -->
    <rect x="15" y="45" width="390" height="130" rx="6" fill="#000000" stroke="#1e293b" stroke-width="1"/>
    <text x="25" y="70" font-family="monospace" font-size="11" fill="#4ade80">student@vlearn-linux:~$</text>
    <text x="185" y="70" font-family="monospace" font-size="11" fill="#f8fafc">mkdir CS_Projects</text>
    <text x="25" y="92" font-family="monospace" font-size="11" fill="#4ade80">student@vlearn-linux:~$</text>
    <text x="185" y="92" font-family="monospace" font-size="11" fill="#f8fafc">cd CS_Projects &amp;&amp; ls -la</text>
    <text x="25" y="114" font-family="monospace" font-size="10.5" fill="#94a3b8">total 0  drwxr-xr-x  2 student  4096 Aug 27 .</text>
    <text x="25" y="136" font-family="monospace" font-size="11" fill="#4ade80">student@vlearn-linux:~$</text>
    <text x="185" y="136" font-family="monospace" font-size="11" fill="#38bdf8">python3 solver.py</text>
    <rect x="310" y="125" width="8" height="14" fill="#38bdf8"/>

    <!-- Properties -->
    <text x="20" y="200" font-size="11.5" font-weight="bold" fill="#38bdf8">Key Characteristics &amp; Strengths:</text>
    <text x="20" y="222" font-size="10" fill="#e2e8f0">• Minimal Overhead: Consumes near-zero RAM and CPU cycles.</text>
    <text x="20" y="242" font-size="10" fill="#e2e8f0">• Scripting &amp; Automation: Easily chained via bash/shell scripts.</text>
    <text x="20" y="262" font-size="10" fill="#e2e8f0">• Remote Administration: Ultra-fast over low-bandwidth SSH links.</text>

    <text x="20" y="295" font-size="11.5" font-weight="bold" fill="#f87171">Limitations &amp; Demands:</text>
    <text x="20" y="317" font-size="10" fill="#cbd5e1">• Steep Learning Curve: Requires memorizing commands &amp; syntax.</text>
    <text x="20" y="337" font-size="10" fill="#cbd5e1">• No Visual Feedback: Non-interactive visual cues.</text>
    <text x="20" y="357" font-size="10" fill="#94a3b8">Primary Use: Servers, Cloud VM Containers, Embedded Systems.</text>
  </g>

  <!-- Right: Graphical User Interface -->
  <g transform="translate(500, 85)">
    <rect width="420" height="375" rx="12" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="420" height="32" rx="8" fill="#7e22ce"/>
    <text x="210" y="21" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">Graphical User Interface (GUI) — WIMP</text>
    
    <!-- GUI desktop simulation -->
    <rect x="15" y="45" width="390" height="130" rx="6" fill="#1e1b4b" stroke="#312e81" stroke-width="1"/>
    
    <!-- Window 1 -->
    <rect x="30" y="55" width="160" height="90" rx="5" fill="#1e293b" stroke="#6366f1" stroke-width="1.5"/>
    <rect x="30" y="55" width="160" height="16" rx="4" fill="#4f46e5"/>
    <text x="40" y="67" font-size="8.5" fill="#ffffff">📁 File Explorer</text>
    <circle cx="178" cy="63" r="3" fill="#ef4444"/>
    
    <!-- Icons inside Window -->
    <rect x="40" y="80" width="22" height="20" rx="3" fill="#f59e0b"/>
    <text x="68" y="95" font-size="8.5" fill="#cbd5e1">Documents</text>
    <rect x="40" y="110" width="22" height="20" rx="3" fill="#38bdf8"/>
    <text x="68" y="125" font-size="8.5" fill="#cbd5e1">Projects</text>

    <!-- Cursor Pointer -->
    <polygon points="260,85 260,105 267,99 275,108 279,104 271,95 280,95" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>

    <!-- Properties -->
    <text x="20" y="200" font-size="11.5" font-weight="bold" fill="#c084fc">Key Characteristics &amp; Strengths:</text>
    <text x="20" y="222" font-size="10" fill="#e2e8f0">• WIMP Metaphor: Windows, Icons, Menus, Pointer navigation.</text>
    <text x="20" y="242" font-size="10" fill="#e2e8f0">• Intuitive Usability: No syntax memorization needed; point &amp; click.</text>
    <text x="20" y="262" font-size="10" fill="#e2e8f0">• Direct Visual Feedback: WYSIWYG editing and live previews.</text>

    <text x="20" y="295" font-size="11.5" font-weight="bold" fill="#f87171">Limitations &amp; Demands:</text>
    <text x="20" y="317" font-size="10" fill="#cbd5e1">• High System Footprint: Consumes hundreds of MBs of RAM &amp; GPU power.</text>
    <text x="20" y="337" font-size="10" fill="#cbd5e1">• Difficult to automate repetitive complex workflows.</text>
    <text x="20" y="357" font-size="10" fill="#94a3b8">Primary Use: Desktop PCs, Laptops, Mobile Smartphones, Tablets.</text>
  </g>
</svg>
""")

SVG_PROCESS_STATE_MACHINE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="450" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Process Management: The 5-State Process Transition Model</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">How the Operating System Scheduler orchestrates CPU execution, I/O waits, and time-slicing</text>

  <!-- State 1: NEW -->
  <g transform="translate(60, 210)">
    <circle cx="50" cy="50" r="45" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
    <text x="50" y="48" font-size="13" font-weight="bold" fill="#94a3b8" text-anchor="middle">NEW</text>
    <text x="50" y="65" font-size="9" fill="#64748b" text-anchor="middle">Created</text>
  </g>

  <!-- Arrow: New -> Ready -->
  <g transform="translate(160, 260)">
    <line x1="0" y1="0" x2="80" y2="0" stroke="#38bdf8" stroke-width="2.5"/>
    <polygon points="80,-5 90,0 80,5" fill="#38bdf8"/>
    <text x="45" y="-8" font-size="10" fill="#38bdf8" text-anchor="middle">Admitted</text>
  </g>

  <!-- State 2: READY (In RAM) -->
  <g transform="translate(255, 205)">
    <rect width="130" height="110" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="2.5"/>
    <rect width="130" height="26" rx="8" fill="#0284c7"/>
    <text x="65" y="18" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">READY</text>
    <text x="65" y="55" font-size="9.5" fill="#e2e8f0" text-anchor="middle">Loaded in RAM</text>
    <text x="65" y="73" font-size="9" fill="#94a3b8" text-anchor="middle">Waiting in Queue</text>
    <text x="65" y="92" font-size="9" fill="#38bdf8" text-anchor="middle">for CPU time-slice</text>
  </g>

  <!-- Forward Arrow: Ready -> Running (Dispatch) -->
  <g transform="translate(390, 235)">
    <line x1="0" y1="0" x2="160" y2="0" stroke="#10b981" stroke-width="2.5"/>
    <polygon points="160,-5 170,0 160,5" fill="#10b981"/>
    <text x="80" y="-8" font-size="10.5" font-weight="bold" fill="#34d399" text-anchor="middle">Scheduler Dispatch</text>
  </g>

  <!-- Backward Arrow: Running -> Ready (Interrupt / Time-slice timeout) -->
  <g transform="translate(390, 285)">
    <line x1="170" y1="0" x2="10" y2="0" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="5"/>
    <polygon points="10,-5 0,0 10,5" fill="#f59e0b"/>
    <text x="85" y="16" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">Time-slice Timeout (Preemption)</text>
  </g>

  <!-- State 3: RUNNING (On CPU) -->
  <g transform="translate(565, 205)">
    <rect width="135" height="110" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="2.5"/>
    <rect width="135" height="26" rx="8" fill="#059669"/>
    <text x="67" y="18" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">RUNNING</text>
    <text x="67" y="55" font-size="9.5" font-weight="bold" fill="#34d399" text-anchor="middle">CPU Core Active</text>
    <text x="67" y="75" font-size="9" fill="#e2e8f0" text-anchor="middle">Executing instructions</text>
    <text x="67" y="95" font-size="8.5" fill="#94a3b8" text-anchor="middle">1 process per core</text>
  </g>

  <!-- Arrow: Running -> Terminated -->
  <g transform="translate(705, 260)">
    <line x1="0" y1="0" x2="80" y2="0" stroke="#ef4444" stroke-width="2.5"/>
    <polygon points="80,-5 90,0 80,5" fill="#ef4444"/>
    <text x="45" y="-8" font-size="10" fill="#f87171" text-anchor="middle">Exit / Finish</text>
  </g>

  <!-- State 5: TERMINATED -->
  <g transform="translate(800, 210)">
    <circle cx="50" cy="50" r="45" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <text x="50" y="48" font-size="11.5" font-weight="bold" fill="#f87171" text-anchor="middle">TERMINATED</text>
    <text x="50" y="65" font-size="9" fill="#94a3b8" text-anchor="middle">Memory Freed</text>
  </g>

  <!-- State 4: WAITING / BLOCKED (Bottom) -->
  <g transform="translate(410, 360)">
    <rect width="145" height="90" rx="12" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
    <rect width="145" height="24" rx="8" fill="#ca8a04"/>
    <text x="72" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">BLOCKED / WAITING</text>
    <text x="72" y="48" font-size="9" fill="#e2e8f0" text-anchor="middle">Waiting for I/O Event</text>
    <text x="72" y="66" font-size="8.5" fill="#94a3b8" text-anchor="middle">(Disk, Keyboard, Network)</text>
  </g>

  <!-- Curved Arrow: Running -> Blocked -->
  <path d="M 610 320 Q 610 405 565 405" fill="none" stroke="#eab308" stroke-width="2.5"/>
  <polygon points="568,400 558,405 568,410" fill="#eab308"/>
  <text x="645" y="375" font-size="9.5" fill="#fbbf24" text-anchor="middle">I/O Request / Wait</text>

  <!-- Curved Arrow: Blocked -> Ready -->
  <path d="M 405 405 Q 320 405 320 320" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
  <polygon points="315,322 320,312 325,322" fill="#38bdf8"/>
  <text x="315" y="435" font-size="9.5" fill="#38bdf8" text-anchor="middle">I/O Operation Completed</text>
</svg>
""")

SVG_VIRTUAL_MEMORY_PAGING = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Virtual Memory, Paging, and Disk Thrashing Mechanics</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Mapping virtual pages to physical RAM frames and handling secondary drive swap files</text>

  <!-- Column 1: Virtual Address Space (Application View) -->
  <g transform="translate(45, 90)">
    <rect width="240" height="390" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="240" height="28" rx="6" fill="#7e22ce"/>
    <text x="120" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Virtual Address Space (Process)</text>
    
    <g transform="translate(20, 45)">
      <rect x="0" y="0" width="200" height="45" rx="6" fill="#1e1b4b" stroke="#a855f7" stroke-width="1"/>
      <text x="100" y="27" font-size="11" font-weight="bold" fill="#c084fc" text-anchor="middle">Page 0 (Code Segment)</text>
      
      <rect x="0" y="60" width="200" height="45" rx="6" fill="#1e1b4b" stroke="#a855f7" stroke-width="1"/>
      <text x="100" y="87" font-size="11" font-weight="bold" fill="#c084fc" text-anchor="middle">Page 1 (Active Data)</text>

      <rect x="0" y="120" width="200" height="45" rx="6" fill="#1e1b4b" stroke="#a855f7" stroke-width="1"/>
      <text x="100" y="147" font-size="11" font-weight="bold" fill="#c084fc" text-anchor="middle">Page 2 (Idle Background)</text>

      <rect x="0" y="180" width="200" height="45" rx="6" fill="#1e1b4b" stroke="#a855f7" stroke-width="1"/>
      <text x="100" y="207" font-size="11" font-weight="bold" fill="#c084fc" text-anchor="middle">Page 3 (Idle Texture Assets)</text>

      <rect x="0" y="240" width="200" height="45" rx="6" fill="#1e1b4b" stroke="#a855f7" stroke-width="1"/>
      <text x="100" y="267" font-size="11" font-weight="bold" fill="#c084fc" text-anchor="middle">Page 4 (Stack / Heap)</text>
    </g>
  </g>

  <!-- Middle: OS Page Table Mapping -->
  <g transform="translate(320, 110)">
    <rect width="180" height="180" rx="10" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="90" y="25" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">OS PAGE TABLE</text>
    <line x1="10" y1="35" x2="170" y2="35" stroke="#38bdf8" stroke-width="1"/>
    
    <text x="20" y="58" font-family="monospace" font-size="10" fill="#ffffff">Page 0 -&gt; Frame 2 (RAM)</text>
    <text x="20" y="82" font-family="monospace" font-size="10" fill="#ffffff">Page 1 -&gt; Frame 5 (RAM)</text>
    <text x="20" y="106" font-family="monospace" font-size="10" fill="#fca5a5">Page 2 -&gt; Swap File</text>
    <text x="20" y="130" font-family="monospace" font-size="10" fill="#fca5a5">Page 3 -&gt; Swap File</text>
    <text x="20" y="154" font-family="monospace" font-size="10" fill="#ffffff">Page 4 -&gt; Frame 0 (RAM)</text>
  </g>

  <!-- Mapping Connectors -->
  <line x1="285" y1="155" x2="320" y2="155" stroke="#38bdf8" stroke-width="2"/>
  <line x1="285" y1="215" x2="320" y2="180" stroke="#38bdf8" stroke-width="2"/>
  <line x1="285" y1="275" x2="320" y2="205" stroke="#ef4444" stroke-width="2"/>
  <line x1="285" y1="335" x2="320" y2="230" stroke="#ef4444" stroke-width="2"/>

  <!-- Column 3 Top: Fast Physical RAM -->
  <g transform="translate(540, 90)">
    <rect width="375" height="175" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <rect width="375" height="28" rx="6" fill="#059669"/>
    <text x="187" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">PHYSICAL RAM (Fast Semiconductor Memory, &lt; 15 ns)</text>
    
    <g transform="translate(15, 40)">
      <rect x="0" y="0" width="105" height="50" rx="5" fill="#064e3b" stroke="#34d399" stroke-width="1"/>
      <text x="52" y="28" font-size="10" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Frame 0: Page 4</text>

      <rect x="120" y="0" width="105" height="50" rx="5" fill="#064e3b" stroke="#34d399" stroke-width="1"/>
      <text x="172" y="28" font-size="10" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Frame 2: Page 0</text>

      <rect x="240" y="0" width="105" height="50" rx="5" fill="#064e3b" stroke="#34d399" stroke-width="1"/>
      <text x="292" y="28" font-size="10" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Frame 5: Page 1</text>
      
      <text x="172" y="85" font-size="10" fill="#6ee7b7" text-anchor="middle">&#10003; Active working set running at full CPU bus speeds</text>
    </g>
  </g>

  <!-- Column 3 Bottom: Secondary Storage Swap / Pagefile -->
  <g transform="translate(540, 285)">
    <rect width="375" height="195" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <rect width="375" height="28" rx="6" fill="#b91c1c"/>
    <text x="187" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">SWAP / PAGE FILE ON DISK (Slow Magnetic/SSD Storage)</text>
    
    <g transform="translate(15, 38)">
      <rect x="0" y="0" width="165" height="40" rx="5" fill="#450a0a" stroke="#f87171" stroke-width="1"/>
      <text x="82" y="24" font-size="10" font-weight="bold" fill="#fca5a5" text-anchor="middle">Swap Slot 1: Page 2</text>

      <rect x="180" y="0" width="165" height="40" rx="5" fill="#450a0a" stroke="#f87171" stroke-width="1"/>
      <text x="262" y="24" font-size="10" font-weight="bold" fill="#fca5a5" text-anchor="middle">Swap Slot 2: Page 3</text>
    </g>

    <!-- Thrashing Warning Box -->
    <g transform="translate(15, 90)">
      <rect width="345" height="55" rx="6" fill="#1e1b4b" stroke="#fbbf24" stroke-width="1.5"/>
      <text x="172" y="22" font-size="10.5" font-weight="bold" fill="#fde047" text-anchor="middle">&#9888; THE DISK THRASHING TRAP</text>
      <text x="172" y="42" font-size="9" fill="#e2e8f0" text-anchor="middle">When RAM is full, OS spends 99% time swapping pages &amp; 0% executing!</text>
    </g>
  </g>
</svg>
""")

SVG_DIRECTORY_TREE_PERMISSIONS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 500" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="470" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">File System Hierarchy &amp; Access Control Lists (ACL)</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Directory tree path navigation and standard multi-user Read/Write/Execute permissions</text>

  <!-- Left: Directory Tree Structure -->
  <g transform="translate(40, 85)">
    <rect width="430" height="375" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="430" height="30" rx="8" fill="#0284c7"/>
    <text x="215" y="20" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">Hierarchical Directory Tree (Linux &amp; Windows)</text>
    
    <!-- Tree nodes -->
    <g transform="translate(25, 45)">
      <!-- Root -->
      <rect x="0" y="0" width="130" height="28" rx="5" fill="#0369a1"/>
      <text x="65" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Root: / (or C:\\\\)</text>
      
      <line x1="65" y1="28" x2="65" y2="60" stroke="#38bdf8" stroke-width="2"/>
      <line x1="65" y1="60" x2="180" y2="60" stroke="#38bdf8" stroke-width="2"/>

      <!-- Branches -->
      <rect x="20" y="70" width="90" height="25" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <text x="65" y="87" font-size="10" fill="#38bdf8" text-anchor="middle">&#128193; /etc</text>

      <rect x="130" y="70" width="90" height="25" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <text x="175" y="87" font-size="10" fill="#38bdf8" text-anchor="middle">&#128193; /bin</text>

      <rect x="240" y="70" width="90" height="25" rx="4" fill="#0369a1"/>
      <text x="285" y="87" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">&#128193; /home</text>

      <!-- Sub branch under home -->
      <line x1="285" y1="95" x2="285" y2="125" stroke="#38bdf8" stroke-width="2"/>
      <rect x="235" y="125" width="100" height="25" rx="4" fill="#0369a1"/>
      <text x="285" y="142" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">&#128193; /student</text>

      <line x1="285" y1="150" x2="285" y2="180" stroke="#38bdf8" stroke-width="2"/>
      <rect x="220" y="180" width="130" height="30" rx="4" fill="#1e1b4b" stroke="#a855f7" stroke-width="1.5"/>
      <text x="285" y="200" font-size="10.5" font-weight="bold" fill="#c084fc" text-anchor="middle">&#128196; homework.py</text>
    </g>

    <!-- Path comparison -->
    <g transform="translate(20, 275)">
      <text x="0" y="15" font-size="10.5" font-weight="bold" fill="#38bdf8">Absolute Path (from Root):</text>
      <text x="0" y="33" font-family="monospace" font-size="10" fill="#a7f3d0">/home/student/homework.py</text>

      <text x="0" y="60" font-size="10.5" font-weight="bold" fill="#fbbf24">Relative Path (from /home):</text>
      <text x="0" y="78" font-family="monospace" font-size="10" fill="#fde047">./student/homework.py</text>
    </g>
  </g>

  <!-- Right: Access Control Permissions (rwx) -->
  <g transform="translate(490, 85)">
    <rect width="430" height="375" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="430" height="30" rx="8" fill="#059669"/>
    <text x="215" y="20" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">Access Control Flags: Read, Write, Execute</text>
    
    <!-- Permission Matrix Table -->
    <g transform="translate(15, 45)">
      <rect width="400" height="150" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      
      <!-- Table Header -->
      <rect width="400" height="28" rx="6" fill="#0f172a"/>
      <text x="50" y="19" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Permission</text>
      <text x="120" y="19" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Symbol</text>
      <text x="180" y="19" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Bit Value</text>
      <text x="295" y="19" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Allowed Operation</text>

      <!-- Row 1: Read -->
      <text x="50" y="55" font-size="10" fill="#ffffff" text-anchor="middle">Read</text>
      <text x="120" y="55" font-family="monospace" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">r</text>
      <text x="180" y="55" font-size="10" fill="#cbd5e1" text-anchor="middle">4 (2&#178;)</text>
      <text x="295" y="55" font-size="9.5" fill="#cbd5e1" text-anchor="middle">View file contents / List directory</text>

      <!-- Row 2: Write -->
      <text x="50" y="90" font-size="10" fill="#ffffff" text-anchor="middle">Write</text>
      <text x="120" y="90" font-family="monospace" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">w</text>
      <text x="180" y="90" font-size="10" fill="#cbd5e1" text-anchor="middle">2 (2&#185;)</text>
      <text x="295" y="90" font-size="9.5" fill="#cbd5e1" text-anchor="middle">Modify, append, delete file contents</text>

      <!-- Row 3: Execute -->
      <text x="50" y="125" font-size="10" fill="#ffffff" text-anchor="middle">Execute</text>
      <text x="120" y="125" font-family="monospace" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">x</text>
      <text x="180" y="125" font-size="10" fill="#cbd5e1" text-anchor="middle">1 (2&#8304;)</text>
      <text x="295" y="125" font-size="9.5" fill="#cbd5e1" text-anchor="middle">Run script / execute binary process</text>
    </g>

    <!-- File System Comparison Box -->
    <g transform="translate(15, 210)">
      <rect width="400" height="145" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="200" y="24" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">File System Standard Comparison</text>
      <text x="15" y="50" font-size="9.5" fill="#e2e8f0">&#8226; <tspan font-weight="bold" fill="#fbbf24">FAT32</tspan>: High universal compatibility; <tspan fill="#f87171" font-weight="bold">Max file size 4GB</tspan>.</text>
      <text x="15" y="75" font-size="9.5" fill="#e2e8f0">&#8226; <tspan font-weight="bold" fill="#38bdf8">NTFS</tspan>: Windows native; supports journaling, encryption &amp; ACLs.</text>
      <text x="15" y="100" font-size="9.5" fill="#e2e8f0">&#8226; <tspan font-weight="bold" fill="#34d399">ext4</tspan>: Linux standard; high performance, robust indexing.</text>
      <text x="15" y="125" font-size="9.5" fill="#e2e8f0">&#8226; <tspan font-weight="bold" fill="#c084fc">APFS</tspan>: Apple macOS/iOS native; optimized for SSD flash drives.</text>
    </g>
  </g>
</svg>
""")

SVG_BOOTSTRAP_AND_INSTALL = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Computer Bootstrapping Sequence &amp; OS Installation Flow</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">From cold electrical power-on (BIOS/UEFI) to kernel space and storage partitioning</text>

  <!-- Left: Bootstrapping Sequence (4 Stages) -->
  <g transform="translate(40, 85)">
    <rect width="420" height="390" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="420" height="30" rx="8" fill="#0284c7"/>
    <text x="210" y="20" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Stage 1 to 4: The Boot Sequence (Startup)</text>

    <!-- Step 1 -->
    <g transform="translate(20, 45)">
      <rect width="380" height="60" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <circle cx="25" cy="30" r="14" fill="#0284c7"/>
      <text x="25" y="35" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1</text>
      <text x="50" y="24" font-size="11" font-weight="bold" fill="#38bdf8">Power-On &amp; ROM BIOS / UEFI</text>
      <text x="50" y="42" font-size="9" fill="#cbd5e1">Motherboard delivers power; CPU reads permanent firmware in ROM.</text>
    </g>

    <!-- Step 2 -->
    <g transform="translate(20, 115)">
      <rect width="380" height="60" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <circle cx="25" cy="30" r="14" fill="#0284c7"/>
      <text x="25" y="35" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2</text>
      <text x="50" y="24" font-size="11" font-weight="bold" fill="#38bdf8">POST (Power-On Self-Test)</text>
      <text x="50" y="42" font-size="9" fill="#cbd5e1">BIOS tests RAM, keyboard, graphics card, and storage integrity.</text>
    </g>

    <!-- Step 3 -->
    <g transform="translate(20, 185)">
      <rect width="380" height="60" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <circle cx="25" cy="30" r="14" fill="#0284c7"/>
      <text x="25" y="35" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3</text>
      <text x="50" y="24" font-size="11" font-weight="bold" fill="#38bdf8">Bootloader Execution</text>
      <text x="50" y="42" font-size="9" fill="#cbd5e1">BIOS locates boot device (SSD/USB) &amp; loads tiny bootloader into RAM.</text>
    </g>

    <!-- Step 4 -->
    <g transform="translate(20, 255)">
      <rect width="380" height="60" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
      <circle cx="25" cy="30" r="14" fill="#059669"/>
      <text x="25" y="35" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">4</text>
      <text x="50" y="24" font-size="11" font-weight="bold" fill="#34d399">Kernel Init &amp; User Space</text>
      <text x="50" y="42" font-size="9" fill="#cbd5e1">OS Kernel loads into memory, initializes drivers, and presents Login UI.</text>
    </g>
  </g>

  <!-- Right: OS Installation Pipeline -->
  <g transform="translate(500, 85)">
    <rect width="420" height="390" rx="12" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="420" height="30" rx="8" fill="#7e22ce"/>
    <text x="210" y="20" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Clean OS Installation Lifecycle</text>

    <!-- Phase 1 -->
    <g transform="translate(20, 45)">
      <rect width="380" height="60" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1"/>
      <text x="15" y="22" font-size="10.5" font-weight="bold" fill="#c084fc">Phase 1: Pre-Install &amp; 3-2-1 Backup</text>
      <text x="15" y="42" font-size="9" fill="#e2e8f0">&#8226; Verify CPU/RAM hardware requirements.</text>
      <text x="15" y="55" font-size="9" fill="#e2e8f0">&#8226; Backup crucial user data (3 copies, 2 media, 1 offsite).</text>
    </g>

    <!-- Phase 2 -->
    <g transform="translate(20, 115)">
      <rect width="380" height="60" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1"/>
      <text x="15" y="22" font-size="10.5" font-weight="bold" fill="#c084fc">Phase 2: Boot from Installation Media</text>
      <text x="15" y="42" font-size="9" fill="#e2e8f0">&#8226; Create bootable USB media.</text>
      <text x="15" y="55" font-size="9" fill="#e2e8f0">&#8226; Change BIOS boot order to prioritize USB drive.</text>
    </g>

    <!-- Phase 3 -->
    <g transform="translate(20, 185)">
      <rect width="380" height="60" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1"/>
      <text x="15" y="22" font-size="10.5" font-weight="bold" fill="#c084fc">Phase 3: Storage Partitioning &amp; Formatting</text>
      <text x="15" y="42" font-size="9" fill="#e2e8f0">&#8226; Partition drive (system partition vs data partition).</text>
      <text x="15" y="55" font-size="9" fill="#e2e8f0">&#8226; Format with target file system (NTFS / ext4).</text>
    </g>

    <!-- Phase 4 -->
    <g transform="translate(20, 255)">
      <rect width="380" height="60" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
      <text x="15" y="22" font-size="10.5" font-weight="bold" fill="#34d399">Phase 4: File Extraction &amp; Account Setup</text>
      <text x="15" y="42" font-size="9" fill="#e2e8f0">&#8226; Decompress OS system files into root directory.</text>
      <text x="15" y="55" font-size="9" fill="#e2e8f0">&#8226; Configure admin user credentials, timezone &amp; security.</text>
    </g>
  </g>
</svg>
""")

SVG_SECURITY_AND_MAINTENANCE_ECOSYSTEM = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Operating System Security Architecture &amp; System Utilities Ecosystem</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Defensive security layers, access privilege controls, and proactive storage/diagnostic maintenance tools</text>

  <!-- Left: OS Security Architecture (4 Pillars) -->
  <g transform="translate(40, 85)">
    <rect width="420" height="390" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="420" height="30" rx="8" fill="#0284c7"/>
    <text x="210" y="20" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">OS Multi-Layered Security Architecture</text>

    <!-- Security Pillar 1: User Privilege Separation -->
    <g transform="translate(20, 45)">
      <rect width="380" height="65" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <circle cx="28" cy="32" r="14" fill="#0284c7"/>
      <text x="28" y="37" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1</text>
      <text x="55" y="24" font-size="11" font-weight="bold" fill="#38bdf8">User Account Control &amp; Least Privilege</text>
      <text x="55" y="42" font-size="9" fill="#cbd5e1">Separates Standard Users from root/admin; prompts for elevation</text>
      <text x="55" y="56" font-size="8.5" fill="#94a3b8">(UAC in Windows / sudo in Linux) to block unauthorized changes.</text>
    </g>

    <!-- Security Pillar 2: Firewall Protection -->
    <g transform="translate(20, 120)">
      <rect width="380" height="65" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <circle cx="28" cy="32" r="14" fill="#0284c7"/>
      <text x="28" y="37" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2</text>
      <text x="55" y="24" font-size="11" font-weight="bold" fill="#38bdf8">Built-in Network Packet Firewall</text>
      <text x="55" y="42" font-size="9" fill="#cbd5e1">Monitors incoming &amp; outgoing IP traffic, blocking suspicious ports,</text>
      <text x="55" y="56" font-size="8.5" fill="#94a3b8">unauthorized inbound connections, and network-based intrusion attempts.</text>
    </g>

    <!-- Security Pillar 3: Antivirus & Real-Time Malware Engine -->
    <g transform="translate(20, 195)">
      <rect width="380" height="65" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <circle cx="28" cy="32" r="14" fill="#0284c7"/>
      <text x="28" y="37" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3</text>
      <text x="55" y="24" font-size="11" font-weight="bold" fill="#38bdf8">Real-Time Antivirus &amp; Heuristic Scanner</text>
      <text x="55" y="42" font-size="9" fill="#cbd5e1">Scans files against known malware signatures and monitors memory</text>
      <text x="55" y="56" font-size="8.5" fill="#94a3b8">for zero-day suspicious behavioral anomalies (ransomware/trojans).</text>
    </g>

    <!-- Security Pillar 4: Data Encryption -->
    <g transform="translate(20, 270)">
      <rect width="380" height="65" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
      <circle cx="28" cy="32" r="14" fill="#059669"/>
      <text x="28" y="37" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">4</text>
      <text x="55" y="24" font-size="11" font-weight="bold" fill="#34d399">Full-Disk Encryption &amp; File ACLs</text>
      <text x="55" y="42" font-size="9" fill="#cbd5e1">Encrypts volume storage sectors (BitLocker / LUKS) and restricts file</text>
      <text x="55" y="56" font-size="8.5" fill="#94a3b8">access through granular multi-user permissions (Read/Write/Execute).</text>
    </g>
  </g>

  <!-- Right: System Utilities & Diagnostics (4 Pillars) -->
  <g transform="translate(500, 85)">
    <rect width="420" height="390" rx="12" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="420" height="30" rx="8" fill="#7e22ce"/>
    <text x="210" y="20" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">System Maintenance &amp; Diagnostic Utilities</text>

    <!-- Utility 1: Disk Defragmenter & TRIM -->
    <g transform="translate(20, 45)">
      <rect width="380" height="65" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1"/>
      <text x="15" y="22" font-size="10.5" font-weight="bold" fill="#c084fc">1. Disk Defragmenter &amp; SSD TRIM</text>
      <text x="15" y="40" font-size="9" fill="#e2e8f0">&#8226; HDDs: Reorganizes non-contiguous clusters for fast sequential reads.</text>
      <text x="15" y="55" font-size="9" fill="#e2e8f0">&#8226; SSDs: Executes TRIM commands to erase stale NAND memory blocks.</text>
    </g>

    <!-- Utility 2: Disk Cleanup -->
    <g transform="translate(20, 120)">
      <rect width="380" height="65" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1"/>
      <text x="15" y="22" font-size="10.5" font-weight="bold" fill="#c084fc">2. Disk Cleanup &amp; Cache Purge</text>
      <text x="15" y="40" font-size="9" fill="#e2e8f0">&#8226; Detects temporary internet files, recycle bin data, and old update logs.</text>
      <text x="15" y="55" font-size="9" fill="#e2e8f0">&#8226; Safely frees gigabytes of storage capacity without touching user documents.</text>
    </g>

    <!-- Utility 3: Task Manager & Resource Telemetry -->
    <g transform="translate(20, 195)">
      <rect width="380" height="65" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1"/>
      <text x="15" y="22" font-size="10.5" font-weight="bold" fill="#c084fc">3. Resource Monitor / Task Manager</text>
      <text x="15" y="40" font-size="9" fill="#e2e8f0">&#8226; Real-time telemetry on CPU %, RAM footprint, disk I/O, &amp; network traffic.</text>
      <text x="15" y="55" font-size="9" fill="#e2e8f0">&#8226; Enables immediate termination of frozen or rogue runaway processes.</text>
    </g>

    <!-- Utility 4: Update & Patch Management -->
    <g transform="translate(20, 270)">
      <rect width="380" height="65" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
      <text x="15" y="22" font-size="10.5" font-weight="bold" fill="#34d399">4. System Update &amp; Security Patching</text>
      <text x="15" y="40" font-size="9" fill="#e2e8f0">&#8226; Downloads and applies OS kernel patches for discovered zero-day exploits.</text>
      <text x="15" y="55" font-size="9" fill="#e2e8f0">&#8226; Updates device drivers to ensure continuous hardware stability &amp; speed.</text>
    </g>
  </g>
</svg>
""")

# =====================================================================
# CURRICULUM DEFINITIONS FOR GRADE 10 TOPIC 6
# =====================================================================

def build_topic6_curriculum():
    return [
        # =====================================================================
        # LEARNING UNIT 1: Operating System Architecture and Process Management
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Operating System Architecture and Process Management",
            "unit_description": "Core purpose of the operating system as the system coordinator, user interface models (CLI vs GUI), process lifecycles, and CPU scheduling algorithms.",
            "lesson_title": "Operating System Purpose, User Interfaces, and Process Management",
            "pages": [
                # Page 1: OS Role & Layered Architecture
                [
                    {
                        "type": "suggested_image",
                        "title": "Linux Command-Line Bash Terminal Interface",
                        "content": {
                            "title": "Linux Command-Line Bash Terminal Interface",
                            "caption": "A Linux terminal emulator running htop process monitor, demonstrating text-based Command Line Interface (CLI) process management and memory allocation.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Linux_Terminal_running_htop.png/800px-Linux_Terminal_running_htop.png",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: The Operating System as System Coordinator",
                        "content": {
                            "goal": "Understand the fundamental purpose of the Operating System (OS) as the computer's resource manager and explore its layered position between hardware, applications, and users."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 'Government' Analogy and Core OS Functions",
                        "content": {
                            "markdown": """### **The 'Government' Analogy**
Imagine a modern nation with highways, electrical grids, water pipelines, and millions of active citizens. If there were no governing body to establish traffic regulations, distribute electricity, or enforce law and order, total chaos and gridlock would ensue.

The **Operating System (OS)** acts as the **government of your computer**.
- **Physical Hardware** (CPU, RAM, Storage Drives, Network Cards) represents the nation's physical infrastructure.
- **Application Software** (Web browsers, text editors, games, database engines) represents the citizens.
- **The Operating System** does not produce its own commercial goods (like authoring a spreadsheet or rendering a 3D game); instead, it maintains a stable, organized, and secure environment, managing physical resources fairly so that multiple applications run smoothly without crashing into one another.

### **Core Responsibilities of the OS Kernel**
The **Kernel** is the central, core program of the operating system that resides permanently in RAM from startup to shutdown. Its primary responsibilities include:
1. **Process Management**: Allocating CPU execution time slices to active programs.
2. **Memory Management**: Assigning isolated physical and virtual memory spaces to running processes.
3. **File and Storage Management**: Structuring raw storage sectors into navigable directory hierarchies.
4. **Device Management**: Translating generalized software requests into device-specific electrical commands via device drivers.
5. **Security and Access Control**: Authenticating users and enforcing file permissions."""
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Layered Architecture of a Computer System",
                        "content": {
                            "svg_content": SVG_OS_LAYERED_MODEL,
                            "caption": "Figure 6.1: Concentric and layered view of computer architecture showing how applications must communicate with physical hardware exclusively through the OS Kernel via System Calls."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Crash Course Computer Science: Operating Systems",
                        "content": {
                            "youtube_id": "26QPDBe-NB8",
                            "description": "An engaging overview of the historical evolution and fundamental mechanics of Operating Systems, from early batch processing to modern multitasking kernels."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: OS Kernel and Abstraction Layer",
                        "content": {
                            "question": "Why must application software interact with computer hardware through the OS Kernel via system calls rather than directly accessing physical chips?",
                            "options": [
                                "To prevent applications from communicating over network cables.",
                                "The OS kernel provides a secure abstraction layer, preventing programs from corrupting memory or conflicting over hardware resources.",
                                "Because modern CPU registers cannot execute arithmetic logic.",
                                "To force all applications to operate strictly within text-only terminal interfaces."
                            ],
                            "correct_answer": 1,
                            "explanation": "The OS Kernel acts as the central resource coordinator. Requiring programs to make System Calls ensures memory protection, prevents hardware resource conflicts, and provides stable device abstraction."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Operating System Purpose",
                        "content": {
                            "text": "The Operating System is the indispensable system software that acts as an abstraction layer between hardware and user applications, coordinating process scheduling, memory boundaries, and device communications."
                        }
                    }
                ],

                # Page 2: User Interfaces: CLI vs GUI
                [
                    {
                        "type": "suggested_image",
                        "title": "Modern Graphical User Interface (GUI) Desktop Environment",
                        "content": {
                            "title": "Modern Graphical User Interface (GUI) Desktop Environment",
                            "caption": "A modern Graphical User Interface (GUI) desktop environment providing intuitive WIMP (Windows, Icons, Menus, Pointer) interaction for end-users.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/GNOME_40_desktop.png/800px-GNOME_40_desktop.png",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: User Interface Paradigms",
                        "content": {
                            "goal": "Compare Command-Line Interfaces (CLI) and Graphical User Interfaces (GUI), analyzing their mechanics, resource trade-offs, and appropriate use-cases."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Interacting with the System: CLI vs. GUI",
                        "content": {
                            "markdown": """To interact with an operating system and issue instructions, human users require a **User Interface (UI)**. Modern systems utilize two dominant paradigms:

### **1. Command-Line Interface (CLI)**
A text-based interface where the user types explicit text commands into a terminal shell prompt (e.g., `mkdir my_folder`, `ls -la`, `rm report.txt`).
- **Mechanics**: The shell parses the text command, validates the syntax, and makes a direct system call to the kernel.
- **Advantages**:
  - **Ultra-Low Resource Footprint**: Consumes near-zero RAM and negligible CPU cycles.
  - **Scriptable Automation**: Complex chains of commands can be saved as shell scripts (`.sh` or `.bat`) and run automatically.
  - **Remote Administration**: Ideal for managing remote servers or cloud containers over low-bandwidth connections (e.g., via SSH).
- **Disadvantages**:
  - Steep learning curve requiring memorization of precise vocabulary and syntax.
  - Minimal visual feedback; errors can lead to unintended modifications if commands are typed incorrectly.

---

### **2. Graphical User Interface (GUI)**
A visual interface built around the **WIMP (Windows, Icons, Menus, Pointer)** paradigm.
- **Mechanics**: Users interact with visual representations of files and programs using pointing devices (mouse, touchpad, touchscreen).
- **Advantages**:
  - Highly intuitive; users do not need to memorize commands.
  - Instant visual feedback (progress bars, directory folders, window resizing).
  - Enables rich multimedia multitasking and drag-and-drop workflows.
- **Disadvantages**:
  - **High Resource Overhead**: Consumes significant amounts of RAM, storage, and GPU/CPU power simply to render the visual desktop environment."""
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "CLI vs. GUI Architectural Comparison",
                        "content": {
                            "svg_content": SVG_CLI_VS_GUI,
                            "caption": "Figure 6.2: Structural and visual comparison between the high-efficiency text terminal (CLI) and the user-friendly WIMP environment (GUI)."
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Real-World Selection: Cloud Server vs. Graphic Designer Workstation",
                        "content": {
                            "scenario": "Deciding which interface paradigm to deploy in two real-world computing environments.",
                            "steps": [
                                {
                                    "step": "Scenario A: High-Density Cloud Web Server",
                                    "explanation": "A cloud server hosting an e-commerce API with 1GB RAM needs maximum performance. Decision: Deploy a headless Linux server using a CLI. Allocating 400MB of RAM to a GUI would waste 40% of the server's memory just rendering windows nobody will ever look at."
                                },
                                {
                                    "step": "Scenario B: Multimedia Graphic Design Workstation",
                                    "explanation": "A digital artist creating vector illustrations and editing video. Decision: Deploy a modern GUI (such as macOS or Windows). The visual feedback of canvas layers, color palettes, and pointer precision is essential for creative productivity."
                                }
                            ]
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Interface Paradigms",
                        "content": {
                            "question": "Why is a Command-Line Interface (CLI) often preferred over a Graphical User Interface (GUI) when managing enterprise cloud servers?",
                            "options": [
                                "CLI provides richer 3D graphics rendering capabilities.",
                                "CLI consumes near-zero memory and CPU cycles, freeing all system resources for application workloads and remote scripting.",
                                "CLI automatically corrects syntax errors made by the operator.",
                                "CLI bypasses the OS kernel and writes directly to physical storage platters."
                            ],
                            "correct_answer": 1,
                            "explanation": "CLIs are lightweight text environments that do not require graphics processing or large windowing frameworks, making them fast, highly scriptable, and resource-efficient for server infrastructure."
                        }
                    }
                ],

                # Page 3: Process Lifecycle & CPU Scheduling
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Process Management and CPU Scheduling",
                        "content": {
                            "goal": "Differentiate between a passive program and an active process, and master the 5-state process lifecycle and CPU time-slicing mechanics."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Programs, Processes, and Multitasking",
                        "content": {
                            "markdown": """### **What is a Process?**
- **Program**: A static, passive collection of instructions stored on secondary storage (like a recipe printed in a cookbook).
- **Process**: An active, running instance of a program loaded into RAM, allocated system resources, and actively being executed by the CPU (like the chef actively cooking the recipe in the kitchen).

### **The Illusion of Multitasking**
On a single CPU core, the processor can only execute **one single instruction at any split second**. Modern operating systems create the **illusion of simultaneity** through **CPU Scheduling and Time-Slicing**:
- The OS scheduler assigns each active process a tiny fraction of time on the CPU (e.g., 10 to 50 milliseconds, known as a **quantum**).
- When the time slice expires, the OS performs a **context switch**, saving the current process's register states in its **Process Control Block (PCB)**, and loading the next process from RAM.
- This switching occurs hundreds of times per second, making multiple applications appear to run simultaneously to human observers.

### **The Core Process States**
1. **New**: The process is being created and loaded into memory from storage.
2. **Ready**: The process is in RAM, fully prepared to execute, and waiting in the queue for its turn on the CPU.
3. **Running**: The CPU is actively executing the process's instructions.
4. **Blocked / Waiting**: The process cannot continue because it is waiting for an external event (e.g., waiting for user keyboard input, reading a file from a slow disk, or waiting for network packets).
5. **Terminated**: The process has finished execution, and the OS reclaims its allocated RAM and resources."""
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "5-State Process Transition Diagram",
                        "content": {
                            "svg_content": SVG_PROCESS_STATE_MACHINE,
                            "caption": "Figure 6.3: State transition machine illustrating how the CPU scheduler moves processes between Ready, Running, and Blocked states via dispatch, timeouts, and I/O interrupts."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Lifecycle Trace of a Text Editor Process",
                        "content": {
                            "steps": [
                                "1. Launch: User double-clicks the text editor icon; the OS loads the program binary from SSD into RAM (State: New -> Ready).",
                                "2. Dispatch: The CPU scheduler selects the text editor from the Ready queue and assigns it to Core 0 (State: Ready -> Running).",
                                "3. I/O Block: The editor needs user input and halts execution while waiting for a key press (State: Running -> Blocked/Waiting).",
                                "4. I/O Interrupt: The user types a key; the keyboard controller fires an interrupt, signaling the OS that data is ready (State: Blocked -> Ready).",
                                "5. Preemption: During heavy computing, the editor's time slice expires; the OS swaps it out to let background tasks run (State: Running -> Ready).",
                                "6. Termination: User clicks 'Exit'; the OS flushes file buffers, closes open handles, and frees RAM allocations (State: Terminated)."
                            ]
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Multitasking and Time-Slicing",
                        "content": {
                            "question": "What mechanism enables a single CPU core to run multiple applications simultaneously from the user's perspective?",
                            "options": [
                                "Increasing the physical RPM of the secondary hard drive platters.",
                                "Rapid CPU time-slicing and context switching, executing small time slices for each ready process.",
                                "Merging all running software code into a single ROM chip.",
                                "Disabling hardware interrupts during program execution."
                            ],
                            "correct_answer": 1,
                            "explanation": "The operating system schedules processes into rapid time slices (quanta). By context-switching between processes hundreds of times per second, the CPU creates the illusion of simultaneous multitasking."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Process State Transitions",
                        "content": {
                            "question": "When a running process makes a request to read a large file from a slow hard drive, which state transition occurs immediately?",
                            "options": [
                                "Running -> Ready",
                                "Running -> Blocked / Waiting",
                                "Running -> Terminated",
                                "Blocked -> Running"
                            ],
                            "correct_answer": 1,
                            "explanation": "Because secondary storage is thousands of times slower than the CPU, the OS immediately moves the process from Running to Blocked/Waiting so that the CPU can execute other Ready processes instead of sitting idle."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Process Lifecycle",
                        "content": {
                            "text": "A process is an active program in RAM. The OS scheduler orchestrates high-throughput multitasking by cycling processes through Ready, Running, and Blocked states via rapid CPU time-slicing."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LEARNING UNIT 2: Memory, File Systems, and Peripheral Device Management
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Memory, File Systems, and Peripheral Device Management",
            "unit_description": "Physical and virtual memory management, paging mechanisms, hierarchical directory trees, file systems (FAT32, NTFS, ext4), and device driver abstraction.",
            "lesson_title": "Memory Management, File Systems, and Peripheral Devices",
            "pages": [
                # Page 1: Memory Allocation & Protection
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Memory Allocation and Protection",
                        "content": {
                            "goal": "Understand how the Operating System allocates physical RAM, protects memory boundaries between processes, and handles segmentation faults."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Memory Allocation & Process Isolation",
                        "content": {
                            "markdown": """### **Memory Allocation**
When a program is launched, the Operating System allocates a contiguous or paged segment of physical RAM to hold its machine code, global variables, heap (dynamically allocated memory), and stack (function call frames).

### **Memory Protection: The Guard Rail**
In a multi-user, multitasking environment, multiple applications reside in RAM simultaneously. The OS Memory Manager must strictly enforce **Memory Protection**:
- Each process is assigned strict base and limit address bounds.
- **Process Isolation**: Process A (e.g., your web browser) is strictly prohibited from reading or writing into the memory segment assigned to Process B (e.g., your password manager or banking app).
- **The Segmentation Fault**: If Process A attempts to access an address outside its permitted boundary, the CPU hardware catches the violation and triggers a trap. The OS kernel immediately halts Process A, displaying a **'Segmentation Fault'**, **'General Protection Fault'**, or crash dialog to protect system integrity."""
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Why Memory Protection is Critical for System Security",
                        "content": {
                            "scenario": "A poorly coded application attempts to write data beyond its allocated memory array.",
                            "steps": [
                                {
                                    "step": "1. Array Index Out of Bounds",
                                    "explanation": "A program creates an array of 10 integers in RAM but tries to write to index 10,000, which points directly into the RAM space allocated to the OS Kernel."
                                },
                                {
                                    "step": "2. Hardware MMU Interception",
                                    "explanation": "The CPU's Memory Management Unit (MMU) detects that the target address exceeds the limit register for that application process."
                                },
                                {
                                    "step": "3. OS Kernel Intervention",
                                    "explanation": "The OS terminates the offending application immediately, preventing it from corrupting kernel data or crashing the entire computer."
                                }
                            ]
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Memory Protection",
                        "content": {
                            "question": "What happens when an application attempts to write data to a RAM memory address allocated to another running program?",
                            "options": [
                                "The OS merges the two programs into a single shared process.",
                                "The computer automatically upgrades physical RAM capacity.",
                                "The OS halts the offending program immediately, throwing a Segmentation Fault or crash error.",
                                "The second program is deleted permanently from secondary storage."
                            ],
                            "correct_answer": 2,
                            "explanation": "The OS strictly isolates memory address spaces. Any attempt to write across another program's boundary triggers a segmentation fault and causes the kernel to terminate the offending process to protect system stability."
                        }
                    }
                ],

                # Page 2: Virtual Memory & Paging
                [
                    {
                        "type": "suggested_image",
                        "title": "Disk Partitioning and Virtual Memory Swap Configuration",
                        "content": {
                            "title": "Disk Partitioning and Virtual Memory Swap Configuration",
                            "caption": "A disk partitioning management tool showing active primary ext4/NTFS file systems alongside designated virtual memory swap partition space on secondary storage.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/GParted_partition_editor.png/800px-GParted_partition_editor.png",
                            "author": "Wikimedia Commons",
                            "licensing": "GPL"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Virtual Memory and Disk Thrashing",
                        "content": {
                            "goal": "Analyze the mechanics of virtual memory, understand how paging overcomes physical RAM limitations, and diagnose disk thrashing."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Virtual Memory, Paging, and Disk Thrashing",
                        "content": {
                            "markdown": """### **The RAM Scarcity Problem**
What happens if your computer has 8 GB of physical RAM, but you open multiple applications that collectively require 14 GB of memory? Under pure physical allocation, the computer would fail to launch the programs.

### **How Virtual Memory Works**
**Virtual Memory** is a memory management technique where the OS reserves a hidden, dedicated portion of secondary storage (an SSD or HDD) to act as an extension of physical RAM. This file is called a **Swap File** (Linux) or **Pagefile** (Windows).

- **Paging**: The OS divides a process's virtual address space into fixed-size memory blocks called **pages** (typically 4 KB). Physical RAM is divided into matching blocks called **frames**.
- **The Page Table**: The OS maintains an internal index (Page Table) mapping virtual pages to physical RAM frames or secondary swap locations.
- **Page Fault**: When the CPU requests an instruction from a page that is currently sitting on the secondary drive swap file, a **page fault** occurs. The OS pauses the process, reads the required page from disk into a free RAM frame, updates the Page Table, and resumes execution.

### **The Danger: Disk Thrashing**
Because secondary drives (even fast NVMe SSDs) are hundreds of times slower than physical silicon RAM, excessive page swapping severely degrades performance.
- When RAM is completely saturated, the OS spends virtually 100% of its CPU cycles swapping pages back and forth between RAM and disk, and 0% executing actual user code.
- This state of catastrophic performance collapse is called **Disk Thrashing**. The computer freezes, user input lags by minutes, and the storage activity light blinks continuously."""
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Virtual Memory and Paging Architecture",
                        "content": {
                            "svg_content": SVG_VIRTUAL_MEMORY_PAGING,
                            "caption": "Figure 6.4: The Virtual Memory architecture showing how the OS Page Table maps virtual process pages to fast RAM frames and slow secondary storage swap slots."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Crash Course: Memory and Storage Management",
                        "content": {
                            "youtube_id": "TQCr9RV7twk",
                            "description": "Exploration of primary vs secondary storage hierarchies, address translation, and virtual memory paging in modern computing architectures."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Virtual Memory and Thrashing",
                        "content": {
                            "question": "What is the primary cause of 'disk thrashing' in a computer system?",
                            "options": [
                                "The computer's magnetic read/write head has physically collided with the platter.",
                                "Physical RAM is exhausted, forcing the OS to spend almost all its time swapping memory pages between RAM and secondary storage.",
                                "The CPU clock speed has exceeded its thermal limit.",
                                "The file system has run out of directory tree inode entries."
                            ],
                            "correct_answer": 1,
                            "explanation": "Disk thrashing occurs when physical RAM is insufficient for the active working sets, causing the OS to constantly read and write memory pages to the slow swap file on the secondary drive."
                        }
                    }
                ],

                # Page 3: File Systems & Directory Trees
                [
                    {
                        "type": "suggested_image",
                        "title": "Hierarchical File Manager Directory and Folder Tree",
                        "content": {
                            "title": "Hierarchical File Manager Directory and Folder Tree",
                            "caption": "A graphical file system browser displaying a hierarchical directory tree structure with file path locations, metadata attributes, and access permissions.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Nautilus_file_manager.png/800px-Nautilus_file_manager.png",
                            "author": "Wikimedia Commons",
                            "licensing": "GPL"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: File Systems and Path Hierarchies",
                        "content": {
                            "goal": "Master the hierarchical directory tree structure, absolute vs relative paths, and compare major file systems including FAT32, NTFS, and ext4."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Hierarchical File Systems and Path Navigation",
                        "content": {
                            "markdown": """### **What is a File System?**
A **File System** is the internal structure and database format an operating system uses to organize, name, store, locate, and retrieve files on a physical storage drive. Without a file system, drive storage would simply be a massive, undifferentiated sequence of raw bytes.

### **The Hierarchical Directory Tree**
Operating systems organize files into an inverted tree structure:
- **Root Directory**: The top-most container of the drive hierarchy.
  - Windows denotes the root by drive letter (e.g., `C:\\\\` or `D:\\\\`).
  - Unix/Linux denotes the root with a single forward slash (`/`).
- **Directories (Folders)**: Containers used to group related files and subdirectories.
- **Absolute Path**: The complete, unbroken path starting from the Root Directory all the way to the specific file (e.g., `/home/student/projects/main.py` or `C:\\\\Users\\\\Student\\\\Documents\\\\report.docx`).
- **Relative Path**: A path that describes a file's location relative to the user's **Current Working Directory (CWD)** (e.g., `./projects/main.py` or `../notes.txt`).

---

### **Comparing Major File System Formats**
1. **FAT32 (File Allocation Table 32)**:
   - High compatibility across Windows, macOS, Linux, and gaming consoles.
   - **Critical Limitation**: Cannot store any single file larger than **4 Gigabytes (4 GB)**.
2. **NTFS (New Technology File System)**:
   - Default native file system for modern Microsoft Windows.
   - Supports files up to 16 Exabytes, file journaling (prevents corruption during sudden power loss), file-level encryption, and Access Control Lists.
3. **ext4 (Fourth Extended File System)**:
   - Standard default file system for Linux distributions; highly reliable and optimized for high-performance file indexing.
4. **APFS (Apple File System)**:
   - Native format for macOS and iOS; specially optimized for solid-state flash storage with instant file cloning."""
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Directory Tree Hierarchy and Permissions Matrix",
                        "content": {
                            "svg_content": SVG_DIRECTORY_TREE_PERMISSIONS,
                            "caption": "Figure 6.5: Hierarchical directory tree navigation alongside the Access Control List (ACL) permission system and file format specifications."
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Calculating Path Traversal and Troubleshooting File Size Limits",
                        "content": {
                            "scenario": "A student attempts to copy a 6.2 GB 4K video recording onto an external USB flash drive formatted with FAT32.",
                            "steps": [
                                {
                                    "step": "1. The Error Message",
                                    "explanation": "The OS displays: 'The file is too large for the destination file system', despite the USB drive having 28 GB of free space."
                                },
                                {
                                    "step": "2. Diagnosing the Cause",
                                    "explanation": "FAT32 uses a 32-bit field for file size in its allocation table, imposing a hard limit of 2³² - 1 bytes (exactly 4,294,967,295 bytes ≈ 4 GB)."
                                },
                                {
                                    "step": "3. The Solution",
                                    "explanation": "Reformat the flash drive with NTFS or exFAT, which support massive file sizes well beyond hundreds of terabytes."
                                }
                            ]
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: File Systems",
                        "content": {
                            "question": "Which of the following file systems has an architectural limitation that prevents storing an individual file larger than 4 GB?",
                            "options": [
                                "NTFS",
                                "ext4",
                                "FAT32",
                                "APFS"
                            ],
                            "correct_answer": 2,
                            "explanation": "FAT32 has a maximum single-file size limit of 4 GB (2³² bytes - 1), making it unable to store large modern video files or disk images."
                        }
                    }
                ],

                # Page 4: Device Drivers & Spooling
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Device Drivers, Buffering, and Spooling",
                        "content": {
                            "goal": "Explain how device drivers provide hardware abstraction and understand how buffering and spooling bridge massive CPU-to-peripheral speed gaps."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Device Drivers, Buffering, and Spooling",
                        "content": {
                            "markdown": """### **The Hardware Abstraction Challenge**
There are thousands of different printers, graphics cards, keyboards, and network adapters manufactured worldwide. The OS kernel cannot contain built-in hardcoded instructions for every specific electronic chip.

### **The Role of a Device Driver**
A **Device Driver** is a specialized software translation program written by the hardware manufacturer.
- It sits between the Operating System and the physical hardware peripheral.
- It translates generic OS commands (e.g., 'draw a circle at coordinate (100, 200)' or 'print this bitmap') into the precise register writes and electrical signals required by that specific hardware model.

---

### **Bridging the Speed Gap: Buffering and Spooling**
A modern CPU can compute billions of instructions per second, while a mechanical peripheral like a printer can only process a few pages per minute. If the CPU had to wait for the printer to finish physically printing each line, the entire computer would freeze.

- **Buffering**: Storing temporary data in RAM to smooth out speed differences between devices transmitting data at varying rates.
- **Spooling (Simultaneous Peripheral Operations On-Line)**:
  - The OS intercepts the print job and writes the entire document to a temporary **spool queue** in RAM or on secondary storage in milliseconds.
  - The CPU is immediately freed to return to running user applications.
  - The printer slowly drains the print jobs from the spool queue at its own mechanical pace in the background."""
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "The Spooling Lifecycle for a 100-Page Document",
                        "content": {
                            "steps": [
                                "1. Application Print Call: The user clicks 'Print 100 Pages' in a word processor.",
                                "2. Driver Translation: The printer driver converts document pages into standard printer description language (e.g., PostScript).",
                                "3. Spool Queuing: The OS writes the entire 50MB print job into the disk/RAM print spooler within 200 milliseconds.",
                                "4. CPU Release: The word processor unfreezes immediately, and the user continues editing other documents.",
                                "5. Background De-spooling: The print spooler daemon feeds pages one by one to the printer hardware as each page completes."
                            ]
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Device Management",
                        "content": {
                            "question": "What is the primary function of Print Spooling in an operating system?",
                            "options": [
                                "To compress the document so it takes up less paper.",
                                "To hold print jobs in a temporary queue, allowing the fast CPU to proceed with other tasks while the slow printer outputs pages in the background.",
                                "To encrypt the document so only the printer manufacturer can read it.",
                                "To convert vector graphic fonts into raw binary machine code for the CPU."
                            ],
                            "correct_answer": 1,
                            "explanation": "Print spooling decouples the high-speed CPU from the slow mechanical printer by holding jobs in a queue, freeing the computer immediately for other user tasks."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Device & Storage Management",
                        "content": {
                            "text": "Device drivers provide hardware abstraction so the OS can communicate with diverse peripherals, while spooling and buffering bridge speed disparities between ultra-fast processors and slow physical I/O devices."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LEARNING UNIT 3: Security, Maintenance, Installation & Diagnostics
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Security, Maintenance, Installation and Diagnostics",
            "unit_description": "Multi-user access control lists (ACLs), essential utility software, bootstrapping and OS installation workflow, troubleshooting methodology, and software licensing ethics.",
            "lesson_title": "OS Security, Maintenance Utilities, Installation, and Diagnostics",
            "pages": [
                # Page 1: Multi-User Security & Access Control
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Multi-User Security and Access Control Lists",
                        "content": {
                            "goal": "Differentiate between authentication and authorization, and apply Access Control Lists (ACLs) with Read, Write, and Execute permissions."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Authentication, Authorization, and Access Control Lists",
                        "content": {
                            "markdown": """### **Multi-User Operating System Security**
Modern operating systems are built from the ground up to support multiple independent users securely on a single physical computer.

### **1. Authentication vs. Authorization**
- **Authentication**: Verifying the **identity** of the person attempting to log in ('Are you really who you claim to be?').
  - Methods: Passwords, PIN codes, cryptographic keys, two-factor authentication (2FA), and biometric scans (fingerprints, facial recognition).
- **Authorization**: Regulating what an authenticated user is **allowed to do** ('Do you have permission to open, edit, or delete this file?').

### **2. Access Control Lists (ACLs) & Permission Triads**
Every file and directory on a disk contains security metadata specifying permissions for three categories of users:
1. **Owner / User (u)**: The individual account that created the file.
2. **Group (g)**: A collection of users sharing common access needs (e.g., 'Teachers', 'Students', 'Finance').
3. **Others / World (o)**: Any other authenticated account on the computer system.

### **The Three Standard Permission Flags**
- **Read (r - Octal value 4)**: Allows viewing the file's contents or listing a directory.
- **Write (w - Octal value 2)**: Allows editing, modifying, appending to, or deleting the file.
- **Execute (x - Octal value 1)**: Allows running the file as a program binary or executable script."""
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Designing a School Exam File Permission Matrix",
                        "content": {
                            "scenario": "Setting file permissions on `final_exam_questions.pdf` located on a shared school computer.",
                            "steps": [
                                {
                                    "step": "Owner (Teacher)",
                                    "explanation": "Permission: Read + Write (r w -). The teacher can view and edit the exam questions."
                                },
                                {
                                    "step": "Group (Staff)",
                                    "explanation": "Permission: Read Only (r - -). Other teachers can view the exam for moderation, but cannot alter the content."
                                },
                                {
                                    "step": "Others (Students)",
                                    "explanation": "Permission: No Access (- - -). Students are blocked completely from reading, writing, or executing the file."
                                }
                            ]
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Permissions and Security",
                        "content": {
                            "question": "What is the key difference between authentication and authorization in OS security?",
                            "options": [
                                "Authentication checks if a hard drive is formatted, while authorization checks if the CPU is running.",
                                "Authentication verifies user identity (who you are), while authorization determines user permissions (what you are allowed to access).",
                                "Authentication is used only in CLI, while authorization is used only in GUI.",
                                "Authentication deletes temporary files, while authorization defragments the disk."
                            ],
                            "correct_answer": 1,
                            "explanation": "Authentication validates identity (e.g., via password or biometric scan), while authorization determines access rights and permissions via Access Control Lists."
                        }
                    }
                ],

                # Page 2: System Utilities & Maintenance
                [
                    {
                        "type": "suggested_image",
                        "title": "Operating System Task Manager and Resource Monitor",
                        "content": {
                            "title": "Operating System Task Manager and Resource Monitor",
                            "caption": "An operating system diagnostic system monitor displaying live CPU utilization graphs, RAM memory footprints, and real-time active task management.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Ksysguard_process_table.png/800px-Ksysguard_process_table.png",
                            "author": "Wikimedia Commons",
                            "licensing": "GPL"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Operating System Utilities and Disk Optimization",
                        "content": {
                            "goal": "Evaluate the functions of disk defragmenters, disk cleanup tools, and resource monitors, understanding HDD mechanical alignment vs SSD wear mechanics."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Utility Software: Maintenance and Optimization",
                        "content": {
                            "markdown": """### **What is Utility Software?**
Utility software consists of specialized system programs that assist the operating system in analyzing, configuring, optimizing, and maintaining computer hardware and storage.

### **1. Disk Defragmenter (HDDs vs. SSDs)**
- **The HDD Problem**: On magnetic Hard Disk Drives (HDDs), files are written across spinning platters. Over time, as files are created and deleted, pieces of a single file become scattered (**fragmented**) across non-contiguous sectors. The mechanical read head must constantly jump around, dramatically slowing down read times.
- **The Defrag Solution**: A **Disk Defragmenter** reorganizes scattered file clusters into contiguous, sequential sectors so the mechanical head can read files in a single, smooth sweep.
- **CRITICAL WARNING FOR SSDs**:
  - **Never defragment a Solid State Drive (SSD)**.
  - SSDs have no physical moving read heads, so fragmentation causes zero read delay (random access time is virtually instantaneous).
  - Defragmenting writes gigabytes of unnecessary data, rapidly wearing out the SSD's microscopic NAND flash oxide gates and shortening the drive's lifespan.

---

### **2. Disk Cleanup**
Scans drives for unnecessary temporary internet caches, dump files, error logs, and leftover update packages, safely purging them to recover storage capacity.

### **3. Resource Monitor / Task Manager**
A real-time diagnostic window providing telemetry on CPU utilization percentage, RAM consumption, disk read/write transfer rates, and network bandwidth usage to pinpoint system bottlenecks."""
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "OS Security Architecture and System Utilities Ecosystem",
                        "content": {
                            "svg_content": SVG_SECURITY_AND_MAINTENANCE_ECOSYSTEM,
                            "caption": "Figure 6.5: Multi-layer defensive security model (UAC, Firewall, Antivirus, Encryption) and proactive storage/diagnostic maintenance tools."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Disk Defragmentation",
                        "content": {
                            "question": "Why should you NEVER run a disk defragmentation utility on a Solid State Drive (SSD)?",
                            "options": [
                                "SSDs cannot store files larger than 4GB when defragmented.",
                                "SSDs have instantaneous electronic access with no moving read heads, and defragmenting causes excessive write cycles that degrade flash memory cells.",
                                "Defragmenting an SSD erases the BIOS bootloader from ROM.",
                                "SSDs only operate using Command-Line Interfaces."
                            ],
                            "correct_answer": 1,
                            "explanation": "SSDs access all memory cells in nanoseconds without mechanical seek penalties; defragmenting causes unnecessary write wear that shortens the lifespan of NAND flash cells."
                        }
                    }
                ],

                # Page 3: Bootstrapping & OS Installation
                [
                    {
                        "type": "suggested_image",
                        "title": "UEFI BIOS Motherboard Firmware Setup Interface",
                        "content": {
                            "title": "UEFI BIOS Motherboard Firmware Setup Interface",
                            "caption": "A modern UEFI BIOS firmware setup utility interface, managing low-level hardware configuration, POST diagnostic tests, and boot order priority prior to OS bootstrap.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Aptio_Setup_Utility_UEFI.jpg/800px-Aptio_Setup_Utility_UEFI.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Bootstrapping and OS Installation Sequence",
                        "content": {
                            "goal": "Master the step-by-step computer boot sequence (POST, BIOS/UEFI, Bootloader, Kernel) and the storage partitioning process during OS installation."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Boot Sequence and Clean OS Installation",
                        "content": {
                            "markdown": """### **The Computer Bootstrapping Sequence**
When a computer is powered on, physical RAM is completely empty, and the CPU has no instructions in memory. The startup process follows four essential stages:

1. **Power-On & ROM BIOS / UEFI**:
   - Power flows to the motherboard. The CPU automatically executes firmware permanently stored inside the non-volatile **ROM / Flash memory** (the BIOS or modern UEFI).
2. **POST (Power-On Self-Test)**:
   - The BIOS tests critical hardware components (RAM chips, GPU, system timer, keyboard, storage bus) to ensure the system is operational. If an error occurs, it emits diagnostic beep codes or error messages.
3. **Bootloader Execution**:
   - The BIOS reads its configured boot priority list (e.g., USB drive -> SSD -> Network), locates the designated boot device, and loads a tiny initial startup program called the **Bootloader** (e.g., GRUB, Windows Boot Manager) into RAM.
4. **Kernel Initialization**:
   - The bootloader loads the main OS Kernel into RAM, initializes core device drivers, launches background system services, and displays the user login screen.

---

### **The OS Installation Lifecycle**
1. **Pre-Installation Verification**: Check hardware compatibility (CPU architecture, RAM, storage) and enforce the **3-2-1 Backup Rule** (3 copies of critical data on 2 different media types with 1 copy off-site) to prevent data loss.
2. **Boot from Installation Media**: Configure BIOS/UEFI boot order to boot from a prepared installation USB drive.
3. **Drive Partitioning & Formatting**: Divide physical storage into logical partitions (e.g., System `C:\\\\` partition and Data `D:\\\\` partition) and format with a robust file system (NTFS or ext4).
4. **File Extraction & Account Setup**: The installer decompresses system files onto the storage drive and prompts for administrator credentials and localized system settings."""
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Boot Sequence and OS Installation Pipeline",
                        "content": {
                            "svg_content": SVG_BOOTSTRAP_AND_INSTALL,
                            "caption": "Figure 6.6: Chronological flow of the computer boot sequence from BIOS/UEFI POST to kernel execution, alongside the clean OS installation pipeline."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "The Boot Sequence & Operating System Installation Fundamentals",
                        "content": {
                            "youtube_id": "KN8YgJnShPM",
                            "description": "Step-by-step visual demonstration of the computer boot sequence from power-on and POST through BIOS/UEFI handoff, bootloader, kernel initialization, and operating system diagnostic maintenance."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: The Boot Sequence",
                        "content": {
                            "question": "Which component executes first immediately after power is applied to a computer's motherboard?",
                            "options": [
                                "The Word Processor application loaded in RAM",
                                "The BIOS / UEFI firmware stored in permanent ROM",
                                "The web browser cached on the secondary SSD",
                                "The printer spooler daemon"
                            ],
                            "correct_answer": 1,
                            "explanation": "Because RAM is volatile and blank at startup, the CPU executes the hardwired BIOS/UEFI firmware sitting in motherboard ROM to initialize hardware and run the POST test."
                        }
                    }
                ],

                # Page 4: Integrated Diagnostics, Open-Source Ethics & Assessment Library
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: System Diagnostics, Software Licensing & Unit Assessment",
                        "content": {
                            "goal": "Apply integrated OS troubleshooting to diagnose computer slowdowns, evaluate proprietary vs open-source software ethics, and complete the unit assessment library."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Troubleshooting, Software Licensing, and Cyber Ethics",
                        "content": {
                            "markdown": """### **Integrated System Diagnostics: The Sluggish PC**
When a computer becomes severely unresponsive, an IT professional diagnoses the issue systematically across the core OS subsystems:
1. **Check Memory Management**: Open the **Resource Monitor**. If RAM usage is at 99%, the OS is trapped in a **virtual memory disk thrashing loop**, swapping pages continuously to disk. Solution: Close background applications or install more physical RAM.
2. **Check Process Management**: Check CPU utilization by process. If a single rogue background process is consuming 100% of a core, it may be stuck in an infinite loop. Solution: End the process task.
3. **Check Storage Subsystem**: If the mechanical HDD activity light is continuously solid and files take minutes to open, check for severe **file fragmentation**. Solution: Run Disk Defragmenter (HDDs only).

---

### **Software Licensing and Digital Ethics**
- **Proprietary Software (Closed Source)**:
  - Commercial software licensed under restrictive terms (e.g., Microsoft Windows, macOS).
  - Users are legally prohibited from viewing, modifying, or redistributing the underlying source code.
- **Open-Source Software**:
  - Software distributed with licensing (e.g., GNU GPL, MIT, Apache) that grants users complete freedom to inspect, edit, modify, improve, and redistribute the source code (e.g., Linux Kernel, Ubuntu, Android OS).
- **Software Patching & Cyber Hygiene**:
  - Regularly installing operating system security updates and security patches is a fundamental ethical duty. Unpatched systems can be compromised by malware and weaponized into botnets to launch distributed attacks on others."""
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Challenging Scenario: The Mount Kenya Weather Station OS",
                        "content": {
                            "scenario": "A solar-powered meteorological station on Mount Kenya has a low-power microcontroller with only 256MB of RAM and slow flash storage. It must record hourly weather data and transmit logs daily via satellite.",
                            "steps": [
                                {
                                    "step": "1. User Interface Decision",
                                    "explanation": "Must use a headless Command-Line Interface (CLI) or background daemon. A GUI would consume all 256MB of RAM simply rendering visual window borders, leaving no memory for data logging."
                                },
                                {
                                    "step": "2. Storage Management Configuration",
                                    "explanation": "Configure automatic log rotation and compression. Old text files must be archived into compressed `.tar.gz` formats and automatically purged after 60 days to prevent filling the limited flash storage."
                                },
                                {
                                    "step": "3. Process Lifecycle for Satellite Transmission",
                                    "explanation": "The satellite transmitter process sits in the 'Blocked/Waiting' state for 23 hours and 59 minutes waiting for a daily timer interrupt. When the timer fires, it transitions to 'Ready', gets scheduled to 'Running' to send the data burst, and returns to 'Waiting'."
                                }
                            ]
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Comprehensive Check: Topic 6 Assessment",
                        "content": {
                            "question": "What is the primary freedom provided to computer scientists and developers by Open-Source operating systems like Linux?",
                            "options": [
                                "The computer hardware runs without requiring electricity.",
                                "Users have the legal right to inspect, modify, and redistribute the operating system's source code.",
                                "It completely eliminates the need for device drivers.",
                                "It prevents the CPU from needing a time-slice scheduler."
                            ],
                            "correct_answer": 1,
                            "explanation": "Open-source licensing guarantees the freedom to view, study, modify, and redistribute the underlying source code, fostering global collaboration and transparency."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 6 Summary & Core Competencies",
                        "content": {
                            "text": "The Operating System coordinates all hardware infrastructure, process scheduling, memory virtualization, file systems, device drivers, and user security. Mastering OS concepts enables computer scientists to build responsive, robust, and secure digital systems."
                        }
                    }
                ]
            ]
        }
    ]

# =====================================================================
# INGESTION RUNNER
# =====================================================================

def ingest_grade10_topic6(replace: bool = True):
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 10 Computer Science — Topic 6: Operating Systems")
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
        order=6,
        defaults={
            "name": "Operating Systems (OS)",
            "description": "Role of the operating system, process management, memory allocation, virtual memory, file systems, device drivers, user security, maintenance utilities, and OS installation."
        }
    )
    if not t_created:
        topic.name = "Operating Systems (OS)"
        topic.description = "Role of the operating system, process management, memory allocation, virtual memory, file systems, device drivers, user security, maintenance utilities, and OS installation."
        topic.save()
    print(f"[*] Resolved Topic 6: {topic.name} (ID: {topic.id})")

    if replace:
        print("[*] Replacing existing Topic 6 units, lessons, blocks, and assets...")
        existing_lessons = Lesson.objects.filter(topic=topic)
        LessonAsset.objects.filter(lesson__in=existing_lessons).delete()
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    curriculum_data = build_topic6_curriculum()
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
                    "topic_order": 6,
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
                        block_id=f"g10_cs_t6_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={"topic_order": 6, "unit_order": u_order, "page": page_idx}
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
    print(f"TOPIC 6 INGESTION COMPLETE:")
    print(f"  Units Created:   {total_units}")
    print(f"  Lessons Created: {total_lessons}")
    print(f"  Pages Created:   {total_pages}")
    print(f"  Blocks Created:  {total_blocks}")
    print(f"  Assets Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_grade10_topic6(replace=True)
