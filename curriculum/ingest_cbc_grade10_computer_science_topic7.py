"""
VLearn CBC Grade 10 Computer Science — Topic 7: Computer Setup
Production Ingestion & Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (Level: 10)
Subject: Computer Science
Topic: Computer Setup (Topic Order: 7)

Decomposed into 2 Comprehensive Learning Units & 2 Published Lessons:
  1. Computer Ports, Cables, and Peripheral Connections (Lesson 1: Computer Ports, Cables, and Peripheral Connections)
  2. Setting Up, Testing, and Troubleshooting a Computer System (Lesson 2: Setting Up, Testing, and Troubleshooting a Computer System)
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
# HIGH PRECISION RESPONSIVE VECTOR SVGS (viewBox="0 0 960 520")
# =====================================================================

SVG_PORT_TAXONOMY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Computer Chassis Port Profiles &amp; Mechanical Keying</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Visual geometry, pin arrangements, orientation standards, and signaling types</text>

  <!-- Port 1: USB Type-A -->
  <g transform="translate(45, 95)">
    <rect width="160" height="180" rx="10" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
    <rect width="160" height="26" rx="6" fill="#0284c7"/>
    <text x="80" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">USB Type-A</text>
    
    <!-- Port drawing -->
    <rect x="35" y="45" width="90" height="45" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <rect x="37" y="47" width="86" height="20" fill="#0284c7"/>
    <text x="80" y="61" font-size="8.5" fill="#ffffff" text-anchor="middle">Keyed Insert</text>
    
    <text x="80" y="110" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Rectangular</text>
    <text x="80" y="128" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Keyed (One-way)</text>
    <text x="80" y="146" font-size="8.5" fill="#e2e8f0" text-anchor="middle">USB 2.0 / 3.0 / 3.2</text>
    <text x="80" y="164" font-size="8" fill="#94a3b8" text-anchor="middle">Mouse / Keys / Flash</text>
  </g>

  <!-- Port 2: USB Type-C -->
  <g transform="translate(225, 95)">
    <rect width="160" height="180" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="160" height="26" rx="6" fill="#059669"/>
    <text x="80" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">USB Type-C</text>
    
    <!-- Port drawing -->
    <rect x="45" y="52" width="70" height="30" rx="14" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <rect x="58" y="62" width="44" height="10" rx="3" fill="#059669"/>
    
    <text x="80" y="110" font-size="9.5" font-weight="bold" fill="#34d399" text-anchor="middle">Rounded Oval</text>
    <text x="80" y="128" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#10003; 100% Reversible</text>
    <text x="80" y="146" font-size="8.5" fill="#e2e8f0" text-anchor="middle">Up to 40 Gbps / 240W</text>
    <text x="80" y="164" font-size="8" fill="#94a3b8" text-anchor="middle">Data / Power / Video</text>
  </g>

  <!-- Port 3: HDMI -->
  <g transform="translate(405, 95)">
    <rect width="160" height="180" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="160" height="26" rx="6" fill="#7e22ce"/>
    <text x="80" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">HDMI (Type-A)</text>
    
    <!-- Port drawing -->
    <polygon points="40,50 120,50 120,70 108,82 52,82 40,70" fill="#1e293b" stroke="#c084fc" stroke-width="2"/>
    <rect x="52" y="60" width="56" height="12" fill="#7e22ce"/>
    
    <text x="80" y="110" font-size="9.5" font-weight="bold" fill="#c084fc" text-anchor="middle">Trapezoidal</text>
    <text x="80" y="128" font-size="8.5" fill="#cbd5e1" text-anchor="middle">19 Pins Digital</text>
    <text x="80" y="146" font-size="8.5" fill="#e2e8f0" text-anchor="middle">Uncompressed A/V</text>
    <text x="80" y="164" font-size="8" fill="#94a3b8" text-anchor="middle">Monitors / TVs / Projectors</text>
  </g>

  <!-- Port 4: DisplayPort -->
  <g transform="translate(585, 95)">
    <rect width="160" height="180" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="160" height="26" rx="6" fill="#d97706"/>
    <text x="80" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">DisplayPort (DP)</text>
    
    <!-- Port drawing -->
    <polygon points="40,50 120,50 120,68 108,82 40,82" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
    <rect x="52" y="60" width="56" height="12" fill="#d97706"/>
    
    <text x="80" y="110" font-size="9.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">Asymmetric Bevel</text>
    <text x="80" y="128" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Mechanical Lock Latch</text>
    <text x="80" y="146" font-size="8.5" fill="#e2e8f0" text-anchor="middle">Packetized Video + Audio</text>
    <text x="80" y="164" font-size="8" fill="#94a3b8" text-anchor="middle">Pro GPUs / Daisy Chain</text>
  </g>

  <!-- Port 5: Ethernet RJ-45 -->
  <g transform="translate(765, 95)">
    <rect width="150" height="180" rx="10" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <rect width="150" height="26" rx="6" fill="#be185d"/>
    <text x="75" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Ethernet (RJ-45)</text>
    
    <!-- Port drawing -->
    <rect x="40" y="48" width="70" height="38" rx="3" fill="#1e293b" stroke="#f472b6" stroke-width="2"/>
    <rect x="55" y="48" width="40" height="12" fill="#0f172a"/>
    <line x1="45" y1="78" x2="105" y2="78" stroke="#fbbf24" stroke-width="3" stroke-dasharray="4"/>
    
    <text x="75" y="110" font-size="9.5" font-weight="bold" fill="#f472b6" text-anchor="middle">Square Modular</text>
    <text x="75" y="128" font-size="8.5" fill="#cbd5e1" text-anchor="middle">8P8C Spring Latch</text>
    <text x="75" y="146" font-size="8.5" fill="#e2e8f0" text-anchor="middle">1 Gbps - 10 Gbps LAN</text>
    <text x="75" y="164" font-size="8" fill="#94a3b8" text-anchor="middle">Routers / Switches</text>
  </g>

  <!-- Lower Panel: Legacy & Auxiliary Interfaces -->
  <g transform="translate(45, 295)">
    <rect width="870" height="190" rx="12" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <rect width="870" height="26" rx="6" fill="#1e293b"/>
    <text x="435" y="18" font-size="11.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Legacy Video, Analog Audio, and High-Voltage PSU Power Interfaces</text>

    <!-- Legacy VGA -->
    <g transform="translate(30, 40)">
      <rect width="240" height="130" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <text x="120" y="22" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">VGA (D-Sub 15)</text>
      <text x="120" y="42" font-size="9" fill="#94a3b8" text-anchor="middle">Blue Trapezoid • 15 Analog Pins</text>
      <text x="120" y="62" font-size="9" fill="#cbd5e1" text-anchor="middle">• Video only (NO Audio signal)</text>
      <text x="120" y="80" font-size="9" fill="#cbd5e1" text-anchor="middle">• Analog signal degrades over distance</text>
      <text x="120" y="98" font-size="9" fill="#cbd5e1" text-anchor="middle">• Dual thumb screws for securing</text>
      <text x="120" y="116" font-size="8.5" fill="#f87171" text-anchor="middle">Legacy standard (max 1080p optimal)</text>
    </g>

    <!-- Audio 3.5mm TRS Jacks -->
    <g transform="translate(315, 40)">
      <rect width="250" height="130" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
      <text x="125" y="22" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">3.5mm Color-Coded Audio</text>
      
      <circle cx="45" cy="50" r="10" fill="#84cc16"/>
      <text x="65" y="54" font-size="9" font-weight="bold" fill="#a3e635">Lime Green: Stereo Out / Headphone</text>
      
      <circle cx="45" cy="80" r="10" fill="#f43f5e"/>
      <text x="65" y="84" font-size="9" font-weight="bold" fill="#fb7185">Pink: Microphone In (Mono/Stereo)</text>
      
      <circle cx="45" cy="110" r="10" fill="#0ea5e9"/>
      <text x="65" y="114" font-size="9" font-weight="bold" fill="#38bdf8">Light Blue: Line In (Auxiliary Audio)</text>
    </g>

    <!-- Power IEC C14 / C13 -->
    <g transform="translate(605, 40)">
      <rect width="235" height="130" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
      <text x="117" y="22" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">IEC C14 / C13 Power Socket</text>
      <text x="117" y="42" font-size="9" fill="#94a3b8" text-anchor="middle">High Voltage AC Mains Interface</text>
      <text x="117" y="65" font-size="9" fill="#cbd5e1" text-anchor="middle">• 3 Heavy Copper Pins: L, N, Ground</text>
      <text x="117" y="85" font-size="9" fill="#cbd5e1" text-anchor="middle">• Ground protects from electric shock</text>
      <text x="117" y="105" font-size="9" fill="#cbd5e1" text-anchor="middle">• Always route via Surge Protector/UPS</text>
    </g>
  </g>
</svg>
""")

SVG_USB_FAMILY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The USB Connector Ecosystem: Evolution, Mechanics, and Speed Tiers</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Comparing physical form factors, pin keyed mechanics, and multi-gigabit throughput</text>

  <!-- Type-A -->
  <g transform="translate(45, 95)">
    <rect width="200" height="230" rx="10" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
    <rect width="200" height="30" rx="6" fill="#0284c7"/>
    <text x="100" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">USB Type-A (Standard)</text>
    
    <rect x="50" y="55" width="100" height="50" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <rect x="52" y="57" width="96" height="22" fill="#0284c7"/>
    <text x="100" y="72" font-size="9" fill="#ffffff" text-anchor="middle">4 / 9 Pins Keyed</text>

    <text x="15" y="130" font-size="9.5" font-weight="bold" fill="#38bdf8">Form:</text>
    <text x="55" y="130" font-size="9.5" fill="#e2e8f0">Flat rectangular</text>
    
    <text x="15" y="155" font-size="9.5" font-weight="bold" fill="#38bdf8">Keying:</text>
    <text x="65" y="155" font-size="9.5" fill="#f87171">Strictly 1 orientation</text>

    <text x="15" y="180" font-size="9.5" font-weight="bold" fill="#38bdf8">Speed:</text>
    <text x="60" y="180" font-size="9.5" fill="#e2e8f0">480 Mbps to 10 Gbps</text>

    <text x="15" y="205" font-size="9.5" font-weight="bold" fill="#38bdf8">Devices:</text>
    <text x="68" y="205" font-size="9" fill="#cbd5e1">PC chassis, mice, flash</text>
  </g>

  <!-- Type-B -->
  <g transform="translate(270, 95)">
    <rect width="200" height="230" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="200" height="30" rx="6" fill="#7e22ce"/>
    <text x="100" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">USB Type-B (Square)</text>
    
    <polygon points="65,55 135,55 145,70 145,105 55,105 55,70" fill="#1e293b" stroke="#c084fc" stroke-width="2"/>
    <rect x="75" y="70" width="50" height="20" rx="2" fill="#7e22ce"/>
    <text x="100" y="84" font-size="9" fill="#ffffff" text-anchor="middle">Chamfered</text>

    <text x="15" y="130" font-size="9.5" font-weight="bold" fill="#c084fc">Form:</text>
    <text x="55" y="130" font-size="9.5" fill="#e2e8f0">Square with angled top</text>
    
    <text x="15" y="155" font-size="9.5" font-weight="bold" fill="#c084fc">Keying:</text>
    <text x="65" y="155" font-size="9.5" fill="#f87171">Keyed by bevels</text>

    <text x="15" y="180" font-size="9.5" font-weight="bold" fill="#c084fc">Speed:</text>
    <text x="60" y="180" font-size="9.5" fill="#e2e8f0">USB 2.0 / USB 3.0 B</text>

    <text x="15" y="205" font-size="9.5" font-weight="bold" fill="#c084fc">Devices:</text>
    <text x="68" y="205" font-size="9" fill="#cbd5e1">Printers, audio mixers</text>
  </g>

  <!-- Micro-B -->
  <g transform="translate(495, 95)">
    <rect width="200" height="230" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="200" height="30" rx="6" fill="#d97706"/>
    <text x="100" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">USB Micro-B</text>
    
    <polygon points="65,60 135,60 145,85 145,95 55,95 55,85" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
    <text x="100" y="82" font-size="8.5" fill="#ffffff" text-anchor="middle">Trapezoid Tab</text>

    <text x="15" y="130" font-size="9.5" font-weight="bold" fill="#fbbf24">Form:</text>
    <text x="55" y="130" font-size="9.5" fill="#e2e8f0">Compact trapezoidal</text>
    
    <text x="15" y="155" font-size="9.5" font-weight="bold" fill="#fbbf24">Keying:</text>
    <text x="65" y="155" font-size="9.5" fill="#f87171">Fragile angled clips</text>

    <text x="15" y="180" font-size="9.5" font-weight="bold" fill="#fbbf24">Speed:</text>
    <text x="60" y="180" font-size="9.5" fill="#e2e8f0">480 Mbps (USB 2.0)</text>

    <text x="15" y="205" font-size="9.5" font-weight="bold" fill="#fbbf24">Devices:</text>
    <text x="68" y="205" font-size="9" fill="#cbd5e1">Old phones, micro-boards</text>
  </g>

  <!-- Type-C -->
  <g transform="translate(720, 95)">
    <rect width="195" height="230" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="195" height="30" rx="6" fill="#059669"/>
    <text x="97" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">USB Type-C (Universal)</text>
    
    <rect x="55" y="62" width="85" height="38" rx="19" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <rect x="68" y="74" width="58" height="14" rx="4" fill="#059669"/>
    <text x="97" y="85" font-size="8.5" fill="#ffffff" text-anchor="middle">24-Pin Reversible</text>

    <text x="15" y="130" font-size="9.5" font-weight="bold" fill="#34d399">Form:</text>
    <text x="55" y="130" font-size="9.5" fill="#e2e8f0">Symmetrical oval</text>
    
    <text x="15" y="155" font-size="9.5" font-weight="bold" fill="#34d399">Keying:</text>
    <text x="65" y="155" font-size="9.5" fill="#34d399">&#10003; 100% Reversible</text>

    <text x="15" y="180" font-size="9.5" font-weight="bold" fill="#34d399">Speed:</text>
    <text x="60" y="180" font-size="9.5" fill="#e2e8f0">40 Gbps / USB4 / DP</text>

    <text x="15" y="205" font-size="9.5" font-weight="bold" fill="#34d399">Devices:</text>
    <text x="68" y="205" font-size="9" fill="#cbd5e1">Laptops, phones, NVMe</text>
  </g>

  <!-- Lower Speed Tier Comparison Bar -->
  <g transform="translate(45, 345)">
    <rect width="870" height="145" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="435" y="26" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">USB Protocol Generation &amp; Maximum Bandwidth Comparison</text>
    
    <!-- Speed Bar 1: USB 2.0 -->
    <g transform="translate(20, 45)">
      <rect width="180" height="30" rx="4" fill="#334155"/>
      <rect width="20" height="30" rx="4" fill="#64748b"/>
      <text x="190" y="20" font-size="10" fill="#e2e8f0"><tspan font-weight="bold">USB 2.0</tspan>: 480 Mbps (Black/White insert)</text>
    </g>

    <!-- Speed Bar 2: USB 3.0 / 3.2 Gen 1 -->
    <g transform="translate(20, 80)">
      <rect width="380" height="30" rx="4" fill="#0369a1"/>
      <text x="395" y="20" font-size="10" fill="#e2e8f0"><tspan font-weight="bold" fill="#38bdf8">USB 3.0 / 3.2 Gen 1</tspan>: 5 Gbps (Blue insert, "SS" icon)</text>
    </g>

    <!-- Speed Bar 3: USB4 / Thunderbolt 4 -->
    <g transform="translate(20, 115)">
      <rect width="680" height="22" rx="4" fill="#10b981"/>
      <text x="695" y="16" font-size="10" font-weight="bold" fill="#34d399">USB4 / Thunderbolt 4: 40 Gbps + 240W Power</text>
    </g>
  </g>
</svg>
""")

SVG_ANALOG_VS_DIGITAL_VIDEO = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Display Interfaces: Analog VGA vs. Digital HDMI &amp; DisplayPort</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Signaling waveforms, pin architecture, audio transport, and electromagnetic degradation</text>

  <!-- Left: Analog VGA Signal -->
  <g transform="translate(45, 90)">
    <rect width="415" height="390" rx="12" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
    <rect width="415" height="30" rx="8" fill="#0284c7"/>
    <text x="207" y="20" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Analog Signaling — VGA (Video Graphics Array)</text>

    <!-- VGA Connector Diagram -->
    <g transform="translate(130, 45)">
      <polygon points="10,0 145,0 135,45 20,45" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
      <circle cx="35" cy="12" r="3" fill="#38bdf8"/><circle cx="55" cy="12" r="3" fill="#38bdf8"/><circle cx="75" cy="12" r="3" fill="#38bdf8"/><circle cx="95" cy="12" r="3" fill="#38bdf8"/><circle cx="115" cy="12" r="3" fill="#38bdf8"/>
      <circle cx="40" cy="24" r="3" fill="#38bdf8"/><circle cx="60" cy="24" r="3" fill="#38bdf8"/><circle cx="80" cy="24" r="3" fill="#38bdf8"/><circle cx="100" cy="24" r="3" fill="#38bdf8"/><circle cx="120" cy="24" r="3" fill="#38bdf8"/>
      <circle cx="45" cy="36" r="3" fill="#38bdf8"/><circle cx="65" cy="36" r="3" fill="#38bdf8"/><circle cx="85" cy="36" r="3" fill="#38bdf8"/><circle cx="105" cy="36" r="3" fill="#38bdf8"/>
    </g>

    <!-- Analog Waveform Box -->
    <g transform="translate(20, 105)">
      <rect width="375" height="90" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="187" y="18" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Continuous Voltage Waveform (RGB Analog)</text>
      
      <path d="M 30 55 Q 60 25 90 55 T 150 55 T 210 55 T 270 55 T 330 55" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
      <line x1="30" y1="55" x2="350" y2="55" stroke="#64748b" stroke-width="1" stroke-dasharray="3"/>
    </g>

    <!-- Characteristics -->
    <g transform="translate(20, 210)">
      <text x="0" y="15" font-size="11" font-weight="bold" fill="#38bdf8">&#9658; Technical Characteristics:</text>
      <text x="10" y="36" font-size="9.5" fill="#e2e8f0">&#8226; Transmits continuous electrical voltages for R, G, B channels.</text>
      <text x="10" y="56" font-size="9.5" fill="#e2e8f0">&#8226; <tspan font-weight="bold" fill="#f87171">Zero Audio Transport</tspan>: Requires separate 3.5mm line.</text>
      <text x="10" y="76" font-size="9.5" fill="#e2e8f0">&#8226; Signal degrades over long cables, causing ghosting &amp; blur.</text>
      <text x="10" y="96" font-size="9.5" fill="#e2e8f0">&#8226; Requires manual clock/phase synchronization on LCDs.</text>
      <text x="10" y="116" font-size="9.5" fill="#cbd5e1">&#8226; Retained on older CRT monitors &amp; legacy school projectors.</text>
    </g>
  </g>

  <!-- Right: Digital HDMI & DP Signal -->
  <g transform="translate(500, 90)">
    <rect width="415" height="390" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="415" height="30" rx="8" fill="#059669"/>
    <text x="207" y="20" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Digital Signaling — HDMI &amp; DisplayPort</text>

    <!-- HDMI Connector Diagram -->
    <g transform="translate(130, 45)">
      <polygon points="10,0 145,0 145,30 135,45 20,45 10,30" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
      <rect x="25" y="15" width="105" height="15" fill="#059669"/>
      <text x="77" y="26" font-size="8" fill="#ffffff" text-anchor="middle">19 Gold Digital Contacts</text>
    </g>

    <!-- Digital Waveform Box -->
    <g transform="translate(20, 105)">
      <rect width="375" height="90" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="187" y="18" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">Discrete Binary Square Waveform (TMDS / Micro-Packets)</text>
      
      <path d="M 30 70 L 60 70 L 60 35 L 100 35 L 100 70 L 140 70 L 140 35 L 200 35 L 200 70 L 250 70 L 250 35 L 310 35 L 310 70 L 350 70" fill="none" stroke="#34d399" stroke-width="2.5"/>
      <text x="80" y="30" font-size="9" font-family="monospace" fill="#a7f3d0">1</text>
      <text x="120" y="65" font-size="9" font-family="monospace" fill="#94a3b8">0</text>
      <text x="170" y="30" font-size="9" font-family="monospace" fill="#a7f3d0">1</text>
      <text x="225" y="65" font-size="9" font-family="monospace" fill="#94a3b8">0</text>
      <text x="280" y="30" font-size="9" font-family="monospace" fill="#a7f3d0">1</text>
    </g>

    <!-- Characteristics -->
    <g transform="translate(20, 210)">
      <text x="0" y="15" font-size="11" font-weight="bold" fill="#34d399">&#9658; Technical Characteristics:</text>
      <text x="10" y="36" font-size="9.5" fill="#e2e8f0">&#8226; Transmits discrete binary bitstreams (1s and 0s).</text>
      <text x="10" y="56" font-size="9.5" fill="#e2e8f0">&#8226; <tspan font-weight="bold" fill="#34d399">&#10003; Integrated Audio</tspan>: 8-channel uncompressed audio &amp; video.</text>
      <text x="10" y="76" font-size="9.5" fill="#e2e8f0">&#8226; Immune to moderate noise; pixel-perfect rendition up to 8K.</text>
      <text x="10" y="96" font-size="9.5" fill="#e2e8f0">&#8226; DisplayPort supports Multi-Stream Transport (daisy chaining).</text>
      <text x="10" y="116" font-size="9.5" fill="#cbd5e1">&#8226; Modern standard for all PCs, monitors, and graphics cards.</text>
    </g>
  </g>
</svg>
""")

SVG_WORKSTATION_ASSEMBLY_PIPELINE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Professional Workstation Setup &amp; Assembly Pipeline</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Step-by-step physical connection sequence, electrical safety, and post-assembly verification</text>

  <!-- Row 1: Steps 1 to 4 -->
  <g transform="translate(45, 95)">
    <!-- Step 1 -->
    <g transform="translate(0, 0)">
      <rect width="195" height="165" rx="10" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
      <rect width="195" height="26" rx="6" fill="#0284c7"/>
      <text x="97" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Unpack &amp; Position</text>
      <text x="15" y="50" font-size="9.5" fill="#cbd5e1">&#8226; Level, stable desk</text>
      <text x="15" y="70" font-size="9.5" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#38bdf8">10-15cm clearance</tspan></text>
      <text x="25" y="85" font-size="8.5" fill="#94a3b8">for airflow exhaust</text>
      <text x="15" y="105" font-size="9.5" fill="#cbd5e1">&#8226; Away from water/sun</text>
      <text x="15" y="130" font-size="8.5" fill="#f87171">&#9888; Prevent thermal choke</text>
    </g>

    <!-- Arrow 1-2 -->
    <polygon points="202,82 215,82 215,88 223,79 215,70 215,76 202,76" fill="#38bdf8"/>

    <!-- Step 2 -->
    <g transform="translate(225, 0)">
      <rect width="195" height="165" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
      <rect width="195" height="26" rx="6" fill="#7e22ce"/>
      <text x="97" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Connect Video</text>
      <text x="15" y="50" font-size="9.5" fill="#cbd5e1">&#8226; Locate GPU vs Mobo</text>
      <text x="15" y="70" font-size="9.5" font-weight="bold" fill="#c084fc">&#8226; Use Dedicated GPU</text>
      <text x="25" y="85" font-size="8.5" fill="#94a3b8">horizontal ports below</text>
      <text x="15" y="105" font-size="9.5" fill="#cbd5e1">&#8226; HDMI / DP / VGA</text>
      <text x="15" y="130" font-size="8.5" fill="#fbbf24">&#10003; Hand-tighten screws</text>
    </g>

    <!-- Arrow 2-3 -->
    <polygon points="427,82 440,82 440,88 448,79 440,70 440,76 427,76" fill="#38bdf8"/>

    <!-- Step 3 -->
    <g transform="translate(450, 0)">
      <rect width="195" height="165" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
      <rect width="195" height="26" rx="6" fill="#059669"/>
      <text x="97" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Connect Input &amp; Audio</text>
      <text x="15" y="50" font-size="9.5" fill="#cbd5e1">&#8226; Keyboard &amp; Mouse</text>
      <text x="25" y="65" font-size="8.5" fill="#94a3b8">to rear USB-A ports</text>
      <text x="15" y="85" font-size="9.5" fill="#cbd5e1">&#8226; Reserve front ports</text>
      <text x="25" y="100" font-size="8.5" fill="#94a3b8">for temporary flash</text>
      <text x="15" y="120" font-size="9.5" fill="#34d399">&#8226; Lime green audio jack</text>
    </g>

    <!-- Arrow 3-4 -->
    <polygon points="652,82 665,82 665,88 673,79 665,70 665,76 652,76" fill="#38bdf8"/>

    <!-- Step 4 -->
    <g transform="translate(675, 0)">
      <rect width="195" height="165" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
      <rect width="195" height="26" rx="6" fill="#d97706"/>
      <text x="97" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4. Connect Network</text>
      <text x="15" y="50" font-size="9.5" fill="#cbd5e1">&#8226; RJ-45 Ethernet Cable</text>
      <text x="15" y="70" font-size="9.5" fill="#cbd5e1">&#8226; Push until <tspan font-weight="bold" fill="#fbbf24">"CLICK"</tspan></text>
      <text x="25" y="85" font-size="8.5" fill="#94a3b8">locks retention clip</text>
      <text x="15" y="105" font-size="9.5" fill="#cbd5e1">&#8226; Other end to Router/LAN</text>
      <text x="15" y="130" font-size="8.5" fill="#a7f3d0">&#10003; Full duplex wired link</text>
    </g>
  </g>

  <!-- Transition Arrow Down from Step 4 to Step 5 -->
  <polygon points="772,268 772,285 766,285 775,295 784,285 778,285 778,268" fill="#38bdf8"/>

  <!-- Row 2: Steps 5 to 8 (Right to Left) -->
  <g transform="translate(45, 305)">
    <!-- Step 8 (Final) -->
    <g transform="translate(0, 0)">
      <rect width="195" height="165" rx="10" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
      <rect width="195" height="26" rx="6" fill="#0891b2"/>
      <text x="97" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">8. Safe Shutdown</text>
      <text x="15" y="50" font-size="9.5" fill="#cbd5e1">&#8226; OS Menu -> Shut Down</text>
      <text x="15" y="70" font-size="9.5" font-weight="bold" fill="#67e8f9">&#8226; Flushes RAM to disk</text>
      <text x="15" y="90" font-size="9.5" fill="#cbd5e1">&#8226; Closes active databases</text>
      <text x="15" y="110" font-size="9.5" fill="#cbd5e1">&#8226; Parks disk heads</text>
      <text x="15" y="130" font-size="8.5" fill="#f87171">&#9888; Never pull power cord!</text>
    </g>

    <!-- Arrow 7-8 (Leftwards) -->
    <polygon points="220,82 207,82 207,76 199,85 207,94 207,88 220,88" fill="#38bdf8"/>

    <!-- Step 7 -->
    <g transform="translate(225, 0)">
      <rect width="195" height="165" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
      <rect width="195" height="26" rx="6" fill="#059669"/>
      <text x="97" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">7. Subsystem Test</text>
      <text x="15" y="50" font-size="9.5" fill="#cbd5e1">&#8226; Display sharpness test</text>
      <text x="15" y="70" font-size="9.5" fill="#cbd5e1">&#8226; Keyboard key sweep</text>
      <text x="15" y="90" font-size="9.5" fill="#cbd5e1">&#8226; Audio channel check</text>
      <text x="15" y="110" font-size="9.5" fill="#cbd5e1">&#8226; CLI ping gateway test</text>
      <text x="15" y="130" font-size="8.5" fill="#34d399">&#10003; 100% Verified Ready</text>
    </g>

    <!-- Arrow 6-7 (Leftwards) -->
    <polygon points="445,82 432,82 432,76 424,85 432,94 432,88 445,88" fill="#38bdf8"/>

    <!-- Step 6 -->
    <g transform="translate(450, 0)">
      <rect width="195" height="165" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
      <rect width="195" height="26" rx="6" fill="#7e22ce"/>
      <text x="97" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">6. Initial Boot Sequence</text>
      <text x="15" y="50" font-size="9.5" fill="#cbd5e1">&#8226; Turn on Surge Protector</text>
      <text x="15" y="70" font-size="9.5" font-weight="bold" fill="#c084fc">&#8226; Power on Monitor 1st</text>
      <text x="15" y="90" font-size="9.5" fill="#cbd5e1">&#8226; Power on Tower 2nd</text>
      <text x="15" y="110" font-size="9.5" fill="#cbd5e1">&#8226; Observe fan &amp; LED activity</text>
      <text x="15" y="130" font-size="8.5" fill="#cbd5e1">&#8226; Verify BIOS POST screen</text>
    </g>

    <!-- Arrow 5-6 (Leftwards) -->
    <polygon points="670,82 657,82 657,76 649,85 657,94 657,88 670,88" fill="#38bdf8"/>

    <!-- Step 5 -->
    <g transform="translate(675, 0)">
      <rect width="195" height="165" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
      <rect width="195" height="26" rx="6" fill="#b91c1c"/>
      <text x="97" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">5. Connect Power Safety</text>
      <text x="15" y="50" font-size="9.5" fill="#cbd5e1">&#8226; IEC C13 cable to PSU</text>
      <text x="15" y="70" font-size="9.5" fill="#cbd5e1">&#8226; Monitor power adapter</text>
      <text x="15" y="90" font-size="9.5" font-weight="bold" fill="#f87171">&#8226; Surge Protector / UPS</text>
      <text x="25" y="105" font-size="8.5" fill="#94a3b8">absorbs voltage spikes</text>
      <text x="15" y="130" font-size="8.5" fill="#fde047">&#9888; Protect motherboard</text>
    </g>
  </g>
</svg>
""")

SVG_GPU_TRAP_TROUBLESHOOTING = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Workstation Diagnostics: The "Dedicated GPU Video Trap"</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Why motherboard display ports become inactive when a dedicated graphics card is installed</text>

  <!-- Left: Rear Chassis Backplate -->
  <g transform="translate(50, 95)">
    <rect width="360" height="390" rx="12" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
    <rect width="360" height="30" rx="8" fill="#334155"/>
    <text x="180" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Rear Desktop Chassis (Back I/O Shield)</text>

    <!-- Motherboard I/O Area (Top) -->
    <g transform="translate(20, 45)">
      <rect width="320" height="150" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="2" stroke-dasharray="4"/>
      <text x="160" y="22" font-size="11" font-weight="bold" fill="#f87171" text-anchor="middle">Integrated Motherboard I/O (Top)</text>
      
      <!-- Ports -->
      <circle cx="50" cy="55" r="14" fill="#64748b"/><text x="50" y="60" font-size="8" fill="#fff" text-anchor="middle">PS/2</text>
      <rect x="80" y="43" width="30" height="24" rx="3" fill="#0369a1"/><text x="95" y="58" font-size="7.5" fill="#fff" text-anchor="middle">USB</text>
      
      <!-- Disabled Motherboard Video Ports -->
      <g transform="translate(140, 40)">
        <polygon points="5,0 75,0 68,25 12,25" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="40" y="16" font-size="8" fill="#ffffff" text-anchor="middle">VGA Port</text>
        <polygon points="5,35 75,35 75,50 68,60 12,60 5,50" fill="#7e22ce" stroke="#c084fc" stroke-width="1.5"/>
        <text x="40" y="50" font-size="8" fill="#ffffff" text-anchor="middle">HDMI Port</text>
      </g>

      <!-- Big Red X over Mobo Video -->
      <g transform="translate(240, 50)">
        <circle cx="30" cy="30" r="22" fill="#ef4444"/>
        <text x="30" y="37" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">&#10007;</text>
      </g>
      
      <text x="160" y="125" font-size="9.5" font-weight="bold" fill="#fca5a5" text-anchor="middle">&#9888; AUTOMATICALLY DEACTIVATED BY BIOS</text>
      <text x="160" y="140" font-size="8.5" fill="#94a3b8" text-anchor="middle">Connecting here gives "No Signal Detected" screen</text>
    </g>

    <!-- Dedicated GPU PCI-Express Slot (Bottom) -->
    <g transform="translate(20, 220)">
      <rect width="320" height="145" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
      <text x="160" y="22" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">Dedicated Graphics Card (PCI-e Expansion)</text>
      
      <!-- GPU Horizontal Ports -->
      <g transform="translate(30, 45)">
        <polygon points="0,5 60,5 60,20 54,28 6,28 0,20" fill="#7e22ce" stroke="#c084fc" stroke-width="1.5"/>
        <text x="30" y="18" font-size="7.5" fill="#fff" text-anchor="middle">HDMI</text>

        <polygon points="75,5 135,5 135,20 125,28 75,28" fill="#d97706" stroke="#fbbf24" stroke-width="1.5"/>
        <text x="105" y="18" font-size="7.5" fill="#fff" text-anchor="middle">DP 1</text>

        <polygon points="150,5 210,5 210,20 200,28 150,28" fill="#d97706" stroke="#fbbf24" stroke-width="1.5"/>
        <text x="180" y="18" font-size="7.5" fill="#fff" text-anchor="middle">DP 2</text>
      </g>

      <!-- Big Green Check -->
      <g transform="translate(245, 40)">
        <circle cx="25" cy="25" r="18" fill="#10b981"/>
        <text x="25" y="32" font-size="18" font-weight="bold" fill="#ffffff" text-anchor="middle">&#10003;</text>
      </g>

      <text x="160" y="105" font-size="9.5" font-weight="bold" fill="#34d399" text-anchor="middle">&#10003; PLUG DISPLAY CABLES HERE!</text>
      <text x="160" y="125" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Direct hardware connection to high-speed GPU VRAM</text>
    </g>
  </g>

  <!-- Right: Diagnostic Flowchart -->
  <g transform="translate(445, 95)">
    <rect width="470" height="390" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="470" height="30" rx="8" fill="#0369a1"/>
    <text x="235" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Systematic "No Signal Detected" Troubleshooting Logic</text>

    <!-- Node 1 -->
    <g transform="translate(25, 45)">
      <rect width="420" height="40" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <text x="210" y="24" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Step 1: Check Physical Monitor Power LED (Solid Blue / Orange)</text>
    </g>

    <!-- Arrow down -->
    <line x1="235" y1="85" x2="235" y2="105" stroke="#38bdf8" stroke-width="2"/>

    <!-- Node 2 -->
    <g transform="translate(25, 105)">
      <rect width="420" height="40" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <text x="210" y="24" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Step 2: Verify Cable Seating &amp; Screws at Both Monitor and PC</text>
    </g>

    <!-- Arrow down -->
    <line x1="235" y1="145" x2="235" y2="165" stroke="#38bdf8" stroke-width="2"/>

    <!-- Node 3: GPU Check -->
    <g transform="translate(25, 165)">
      <rect width="420" height="55" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="210" y="22" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">Step 3: Is Video Cable in Motherboard or Dedicated GPU?</text>
      <text x="210" y="42" font-size="9" fill="#e2e8f0" text-anchor="middle">If connected to vertical top ports, move to horizontal GPU ports!</text>
    </g>

    <!-- Arrow down -->
    <line x1="235" y1="220" x2="235" y2="240" stroke="#38bdf8" stroke-width="2"/>

    <!-- Node 4: Input Channel -->
    <g transform="translate(25, 240)">
      <rect width="420" height="45" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <text x="210" y="20" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Step 4: Cycle Monitor Input Source Menu</text>
      <text x="210" y="36" font-size="8.5" fill="#94a3b8" text-anchor="middle">Ensure channel matches active port (HDMI 1, HDMI 2, or DP)</text>
    </g>

    <!-- Resolution Box -->
    <g transform="translate(25, 305)">
      <rect width="420" height="65" rx="8" fill="#1e1b4b" stroke="#10b981" stroke-width="1.5"/>
      <text x="210" y="24" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">&#10003; SYSTEM OPERATIONAL RESOLUTION</text>
      <text x="210" y="46" font-size="9" fill="#e2e8f0" text-anchor="middle">Signal syncs -> Native panel resolution detected -> BIOS/OS displays</text>
    </g>
  </g>
</svg>
""")

# =====================================================================
# CURRICULUM DEFINITIONS FOR GRADE 10 TOPIC 7
# =====================================================================

def build_topic7_curriculum():
    return [
        # =====================================================================
        # LEARNING UNIT 1: Computer Ports, Cables, and Peripheral Connections
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Computer Ports, Cables, and Peripheral Connections",
            "unit_description": "Mechanical and electrical characteristics of computer interfaces, Universal Serial Bus (USB) standards, digital and analog display ports, network connections, color-coded audio jacks, and cable matching protocols.",
            "lesson_title": "Computer Ports, Cables, and Peripheral Connections",
            "pages": [
                # Page 1: Introduction, Analogy & Technical Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Computer Connection Interfaces",
                        "content": {
                            "goal": "Master the physical geometry, electrical signaling, and mechanical keying of computer ports, cables, and peripheral connectors to configure workstations safely and reliably."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "1. Introduction & The 'Interstate Interchange' Analogy",
                        "content": {
                            "text": "Imagine a bustling city. The city itself houses industrial factories, corporate offices, and central distribution warehouses (representing the CPU, RAM, and internal storage of the computer system unit).\n\nHowever, for this city to thrive, it must continuously import raw materials and export manufactured goods through specialized transport hubs:\n- A heavy cargo seaport for massive freight shipping containers (representing high-speed secondary data storage arrays).\n- A dedicated passenger train terminal for commuters (representing high-bandwidth display feeds).\n- Local delivery bays for postal vans (representing low-bandwidth input devices like keyboards and mice).\n\nIn computer architecture, these transport hubs are the **ports**. The multi-lane highways leading into them are the **cables**, and the standardized delivery vehicles are the **connectors**.\n\nIf you steer a 10,000-ton cargo freighter into a shallow postal delivery bay, the entire infrastructure is crushed. In the same way, attempting to force an incompatible cable into a computer port bends microscopic contact pins, short-circuits electrical traces, and destroys expensive motherboard components."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "2. Core Technical Definitions",
                        "content": {
                            "text": "To master computer setup, computer scientists use precise hardware terminology:\n\n- **Port**: A physical socket, receptacle, or interface mounted on a computer's chassis or motherboard where external devices connect to exchange digital data, electrical power, or analog signals.\n- **Cable**: A physical bundle of insulated copper wires or optical glass fibers enclosed in a protective jacket that transmits electrical current or modulated light pulses between system components.\n- **Connector**: The specialized plug or male termination at the end of a cable designed to mate mechanically and electrically with a complementary port socket.\n- **Peripheral**: Any external hardware device that interfaces with the computer system to provide input, output, secondary storage, or communication facilities (e.g., keyboards, mice, monitors, external NVMe drives, printers).\n- **Interface**: The shared physical, electrical, and logical boundary across which two independent computing subsystems exchange information."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Chassis Port Profiles and Connector Geometries",
                        "content": {
                            "caption": "Comprehensive architectural layout of common computer ports: USB Type-A, USB Type-C, HDMI, DisplayPort, Ethernet RJ-45, VGA, 3.5mm audio jacks, and IEC C14 power sockets.",
                            "svg_content": SVG_PORT_TAXONOMY
                        }
                    }
                ],

                # Page 2: Universal Serial Bus (USB) Standards & Ecosystem
                [
                    {
                        "type": "concept_explanation",
                        "title": "3. The Universal Serial Bus (USB) Standard Ecosystem",
                        "content": {
                            "text": "Before the invention of the Universal Serial Bus (USB) in the mid-1990s, connecting peripherals required a confusing array of incompatible, bulky interfaces (e.g., PS/2 for keyboards, DB-25 Parallel for printers, and RS-232 Serial for modems). USB consolidated these single-purpose interfaces into a single, high-speed, hot-swappable communication bus.\n\n### **A. USB Connector Form Factors**\n1. **USB Type-A**: The classic rectangular connector found on desktop towers and laptops. It contains a rigid plastic block inside that makes it **strictly keyed** (it can only be inserted in one orientation). Attempting to force it upside down breaks the central substrate.\n2. **USB Type-B**: A square-shaped connector with beveled upper corners. Its sturdy design is commonly used on high-vibration office equipment such as printers, scanners, and professional studio audio interfaces.\n3. **USB Micro-B**: A miniaturized, trapezoidal plug widely used on older smartphones and portable external hard drives. Its delicate spring clips are prone to mechanical fatigue.\n4. **USB Type-C (USB-C)**: The modern universal standard. Featuring a symmetrical 24-pin oval profile, it is **100% reversible** (plugs in right-side-up or upside-down). USB-C supports high-speed data, DisplayPort Alternate Mode video signaling, and up to **240W of Power Delivery (PD)** to power entire laptops over a single thin cable."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "4. USB Signaling Speeds & Generation Color Codes",
                        "content": {
                            "text": "USB throughput has evolved by orders of magnitude across hardware generations:\n\n- **USB 2.0 (High-Speed)**: Operates at a theoretical signaling rate of **480 Mbps** (approx. 40 MB/s real throughput). Ports and cables typically feature **black or white plastic inserts**.\n- **USB 3.0 / 3.1 / 3.2 Gen 1 (SuperSpeed)**: Operates at **5 Gbps** (over 10x faster than USB 2.0). Standardized by **vibrant blue plastic inserts** or an embossed 'SS' (SuperSpeed) logo.\n- **USB 3.2 Gen 2x2**: Operates at **20 Gbps**, frequently identified by **red or teal plastic inserts**.\n- **USB4 & Thunderbolt 4**: Leverages the Type-C physical connector to deliver up to **40 Gbps** of bidirectional bandwidth, dynamic PCIe data tunneling, and multi-monitor 4K/8K video feeds."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "The USB Connector Family & Speed Tiers",
                        "content": {
                            "caption": "Mechanical cross-sections of USB Type-A, Type-B, Micro-B, and Type-C connectors alongside bandwidth progression from 480 Mbps to 40 Gbps.",
                            "svg_content": SVG_USB_FAMILY
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Physical USB Form Factors",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/USB_types_2.jpg/800px-USB_types_2.jpg",
                            "caption": "Physical comparison of standard USB connectors: Type-A, Type-B, Mini-B, Micro-B, and reversible Type-C.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    }
                ],

                # Page 3: Video Interfaces: Analog VGA vs Digital HDMI & DisplayPort
                [
                    {
                        "type": "concept_explanation",
                        "title": "5. Video Interfaces: Analog vs. Digital Display Feeds",
                        "content": {
                            "text": "Display interfaces transmit massive streams of pixel rendering data from the graphics processing unit (GPU) to visual output devices (monitors, projectors, and televisions).\n\n### **A. VGA (Video Graphics Array)**\n- **Technology**: Legacy **purely analog** interface introduced by IBM in 1987. Standardized with a **blue** chassis connector.\n- **Physical Pinout**: A trapezoidal D-subminiature connector containing **15 pins** arranged in three rows of five. Secured to the chassis using two threaded thumb screws.\n- **Limitations**: Transmits continuous electrical voltage fluctuations. It suffers from electromagnetic interference, signal ghosting, and pixel blur at resolutions above 1080p. Crucially, **VGA carries zero audio signals**.\n\n### **B. HDMI (High-Definition Multimedia Interface)**\n- **Technology**: The global consumer entertainment and computing standard. It is **100% digital**.\n- **Signal Architecture**: Simultaneously transmits **uncompressed digital video and up to 8-channel digital audio** across a single cable using Transition Minimized Differential Signaling (TMDS).\n- **Physical Pinout**: A flat trapezoidal connector with **19 gold-plated pins**. It is keyed by its angled lower corners.\n\n### **C. DisplayPort (DP)**\n- **Technology**: The professional computing standard engineered for high-refresh-rate gaming monitors and multi-display workstations.\n- **Signal Architecture**: Transmits data in **packetized micro-packets** (similar to Ethernet networks). Supports **Multi-Stream Transport (MST)**, allowing multiple monitors to be daisy-chained from a single GPU port.\n- **Physical Pinout**: An asymmetric rectangular plug with one 45-degree beveled corner. Features a **mechanical latching lock clip**—users must press a spring-loaded release button on the connector shell to unplug it safely without ripping the socket from the circuit board."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Analog vs. Digital Video Signal Architecture",
                        "content": {
                            "caption": "Side-by-side comparison of 15-pin analog VGA (continuous voltage wave) vs 19-pin digital HDMI/DisplayPort (discrete binary pulse stream).",
                            "svg_content": SVG_ANALOG_VS_DIGITAL_VIDEO
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Standard HDMI Male Plug and Female Chassis Connector",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/HDMI_connector-male_and_socket-female.jpg/800px-HDMI_connector-male_and_socket-female.jpg",
                            "caption": "Figure 7.2: Standard 19-pin HDMI Type-A male cable connector plug and female chassis port socket.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "HDMI vs DisplayPort vs DVI vs VGA Explained",
                        "content": {
                            "url": "https://www.youtube.com/watch?v=f38sotYHqtA",
                            "youtube_id": "f38sotYHqtA",
                            "description": "Comprehensive video breakdown of display interface architectures, signaling bandwidth, refresh rates, and mechanical latching mechanisms."
                        }
                    }
                ],

                # Page 4: Network, Audio, Power & Cable-Matching Lab
                [
                    {
                        "type": "concept_explanation",
                        "title": "6. Network, Color-Coded Audio, and Mains Power Interfaces",
                        "content": {
                            "text": "### **A. Network Interface: Ethernet (RJ-45 / 8P8C)**\nEthernet cables connect computers to Local Area Networks (LAN) and high-speed broadband routers. The RJ-45 connector contains **8 copper contact pins** that mate with an 8-position 8-contact (8P8C) modular jack. It features a flexible plastic **spring-retention clip** that makes an audible **click** when fully locked into place, preventing accidental disconnections.\n\n### **B. Audio Interfaces: 3.5mm TRS Color Standards**\nDesktop motherboards use the international PC 99 color-coding standard for 3.5mm miniature analog audio jacks:\n- 🟢 **Lime Green (Line-Out)**: Primary stereo audio output for headphones or desktop desktop speakers.\n- 🔴 **Pink (Mic-In)**: Input for mono or stereo condenser microphones.\n- 🔵 **Light Blue (Line-In)**: High-level auxiliary audio input from external mixers, synthesizers, or sound decks.\n\n### **C. High-Voltage Power: IEC C14 / C13 Interface**\nDesktop Power Supply Units (PSU) interface with mains electricity through a heavy-duty **IEC C14 male socket** that receives an **IEC C13 female cord plug**. It features three robust copper pins:\n1. **Line (Live)**: Carries high-voltage alternating current (240V in Kenya).\n2. **Neutral**: Completes the return electrical circuit.\n3. **Earth (Ground)**: Shunts stray fault currents directly into the building's grounding rod, preventing fatal electrical shocks if an internal wire touches the metal chassis."
                        }
                    },
                    {
                        "type": "interactive_table",
                        "title": "Comprehensive Workstation Interface Matrix",
                        "content": {
                            "headers": ["Port Interface", "Mechanical Geometry", "Signal Types", "Keying Type", "Primary Peripheral Target"],
                            "rows": [
                                ["USB Type-A", "Flat rectangle with solid insert", "DC Power (5V) + Digital Data", "Keyed (1 orientation)", "Keyboard, Mouse, Flash Drives, Webcams"],
                                ["USB Type-C", "Symmetrical rounded oval (tiny)", "High-Speed Data, 240W Power, Video", "100% Reversible", "Modern Laptops, Smartphones, Fast NVMe SSDs"],
                                ["VGA (D-Sub)", "Blue trapezoid with 15 pinholes", "Analog RGB Video (No Audio)", "Keyed + Dual Screws", "Legacy CRT/LCD Monitors, Classroom Projectors"],
                                ["HDMI", "Flat trapezoid with 19 gold contacts", "Uncompressed Digital Video + Multi-channel Audio", "Keyed (Beveled)", "High-Definition Displays, Smart TVs, Projectors"],
                                ["DisplayPort", "Asymmetric rectangle with 1 bevel", "Packetized Digital Video + Audio", "Keyed + Locking Button", "Professional Graphics Displays, Daisy-Chained Monitors"],
                                ["Ethernet (RJ-45)", "Square modular with 8 copper pins", "Full-Duplex Packetized LAN Data", "Keyed (Spring clip)", "Broadband Modems, Network Switches, Routers"],
                                ["3.5mm Lime Green", "Miniature cylindrical TRS jack", "Analog Stereo Audio (Line-Out)", "Reversible rotation", "Headphones, 2.1 Desktop Audio Speakers"],
                                ["IEC C14 Socket", "3-Prong trapezoidal male socket", "240V AC Mains Electrical Power", "Keyed (3-Pin Earth)", "Wall Mains Supply via Surge Protector / UPS"]
                            ]
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Selecting Workstation Cables and Matching Interfaces",
                        "content": {
                            "problem_statement": "An office worker is setting up a new desktop workstation with a dual-monitor setup (one 4K 144Hz monitor, one 1080p 60Hz monitor), a wired keyboard, a wireless mouse receiver, analog stereo desktop speakers, and a high-speed Gigabit LAN connection. The desktop tower has 4 USB 3.0 Type-A ports, 1 USB-C port, 1 HDMI 2.1 port, 1 DisplayPort 1.4 port, an RJ-45 Ethernet port, and three 3.5mm audio jacks (Lime Green, Pink, Light Blue). Determine the exact cable/connector type and port assignment for each device.",
                            "step_by_step_solution": [
                                {
                                    "step_number": 1,
                                    "step_title": "Assign Display Connections for High-Refresh and Secondary Monitors",
                                    "explanation": "Connect the 4K 144Hz monitor via DisplayPort 1.4 to utilize DisplayPort's high-bandwidth packetized transmission and locking latch clip. Connect the secondary 1080p 60Hz monitor using the HDMI 2.1 cable."
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Assign USB Input Peripherals",
                                    "explanation": "Insert the wired keyboard and wireless mouse USB receiver into the rear USB 3.0 Type-A ports. This reserves the front-panel USB ports and rear high-speed USB-C port for external flash drives or high-speed NVMe storage."
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Assign Audio Output Interface",
                                    "explanation": "Plug the 3.5mm analog audio plug from the desktop speakers strictly into the Lime Green Line-Out jack (PC 99 standard for stereo output), avoiding the Pink microphone port."
                                },
                                {
                                    "step_number": 4,
                                    "step_title": "Assign Network Interface",
                                    "explanation": "Connect the Cat6 Ethernet patch cable into the RJ-45 modular 8P8C jack on the computer and push until the plastic retention spring-clip makes an audible click."
                                }
                            ]
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Peripheral Interfacing Best Practices",
                        "content": {
                            "text": "1. **USB Diversity**: Type-A is keyed for standard peripherals; Type-C is symmetrical, reversible, and supports up to 240W power and 40 Gbps video/data.\n2. **Display Interfaces**: VGA is legacy analog (video only, no audio); HDMI and DisplayPort are pure digital carrying multi-channel audio and ultra-high resolution video.\n3. **Audio Standards**: Follow the PC 99 standard (Lime Green = Line-Out, Pink = Mic-In, Light Blue = Line-In).\n4. **Physical Care**: Never force a keyed connector into a port. Align keyed shapes and press DisplayPort release latches before unplugging."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Assessment: Ports, Cables & Interfacing",
                        "content": {
                            "questions": [
                                {
                                    "question": "Which of the following ports features a completely symmetrical, reversible design and can deliver up to 240W of power, 40 Gbps data, and video simultaneously?",
                                    "options": [
                                        "A) USB Type-A",
                                        "B) USB Type-C",
                                        "C) DisplayPort",
                                        "D) VGA (D-Sub 15)"
                                    ],
                                    "answer": "B) USB Type-C",
                                    "explanation": "USB Type-C features a symmetrical 24-pin oval profile that allows reversible insertion and supports USB4 data rates (up to 40 Gbps), DisplayPort video, and USB Power Delivery up to 240W."
                                },
                                {
                                    "question": "A student connects a computer to a monitor using a blue 15-pin VGA cable. They notice that high-definition video works, but there is no sound from the monitor's built-in speakers. What is the technical cause?",
                                    "options": [
                                        "A) The VGA thumb screws are not tightened fully.",
                                        "B) VGA is a pure analog video standard that carries zero audio signals.",
                                        "C) The monitor requires a USB 3.0 blue insert cable for sound.",
                                        "D) The operating system sound drivers only support HDMI ports."
                                    ],
                                    "answer": "B) VGA is a pure analog video standard that carries zero audio signals.",
                                    "explanation": "VGA carries only analog RGB video signals and horizontal/vertical sync; it has no pins or protocol for transmitting audio. Audio requires a separate 3.5mm stereo cable or a digital interface like HDMI/DisplayPort."
                                },
                                {
                                    "question": "What is the primary operational advantage of DisplayPort's mechanical latching clip?",
                                    "options": [
                                        "A) It increases data transmission speeds by 50%.",
                                        "B) It grounds high-voltage static charges from the monitor.",
                                        "C) It prevents accidental cable disconnection by locking the plug into the chassis until the release button is pressed.",
                                        "D) It converts digital video into analog signals automatically."
                                    ],
                                    "answer": "C) It prevents accidental cable disconnection by locking the plug into the chassis until the release button is pressed.",
                                    "explanation": "DisplayPort connectors feature physical locking hooks that engage inside the chassis port socket, requiring users to depress the release button on the plug housing to disconnect safely."
                                },
                                {
                                    "question": "When connecting standard analog speakers or headphones to a desktop computer chassis, which color-coded 3.5mm jack must be selected?",
                                    "options": [
                                        "A) Pink",
                                        "B) Light Blue",
                                        "C) Lime Green",
                                        "D) Orange"
                                    ],
                                    "answer": "C) Lime Green",
                                    "explanation": "Under the PC 99 standard, Lime Green designates the main Stereo Line-Out / Headphone channel, Pink designates Microphone-In, and Light Blue designates Line-In."
                                }
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LEARNING UNIT 2: Workstation Assembly, Testing Protocols, and Diagnostics
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Workstation Assembly, Testing Protocols, and Diagnostics",
            "unit_description": "Systematic 8-step workstation setup procedure, electrical safety, surge suppression, post-boot subsystem testing, and hardware fault isolation.",
            "lesson_title": "Setting Up, Testing, and Troubleshooting a Computer System",
            "pages": [
                # Page 1: The Step-by-Step Setup Protocol & Electrical Safety
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Workstation Setup and Electrical Protection",
                        "content": {
                            "goal": "Execute the professional step-by-step procedure for assembling a desktop workstation safely, safeguarding sensitive silicon circuits against electrical surges, and following proper power-up sequences."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "1. Introduction & The 'Building Inspection' Analogy",
                        "content": {
                            "text": "Imagine constructing a modern residential house. Once the brick walls are raised and the roof is tiled, you cannot simply move in immediately. You must systematically lay the plumbing, run electrical conduits, connect to the municipal water main, and turn on the circuit breaker panel. Crucially, before occupancy, an inspector tests the faucets for leaks, tests sockets for voltage grounding, and confirms the fire alarms trigger.\n\nSetting up a computer system follows the exact same logical pipeline. Physically unboxing components is only the prelude. To build a robust, safe workstation, you must follow a structured, sequential protocol to mate connectors, establish clean electrical power, initialize system software, and verify every hardware subsystem without causing electrical damage or data corruption."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "2. The Professional 8-Step System Setup Pipeline",
                        "content": {
                            "text": "To prevent physical damage, electrical shorts, or confusing troubleshooting loops, workstation assembly must strictly follow an ordered pipeline:\n\n1. **Step 1: Unpack & Environmental Placement**: Inspect all components for shipping defects. Place the tower and monitor on a level, sturdy desk with at least **10 to 15 cm of ventilation clearance** around all cooling fan exhausts. Keep away from direct sunlight, liquids, and unshielded magnets.\n2. **Step 2: Connect Video Output**: Connect the monitor to the computer tower using HDMI, DisplayPort, or VGA. **Crucial Rule**: If the system contains a dedicated graphics card (GPU), connect the cable to the horizontal GPU ports at the bottom, *not* the vertical motherboard ports at the top.\n3. **Step 3: Connect Input & Audio Devices**: Plug the keyboard and mouse into rear USB Type-A ports (saving convenient front ports for temporary thumb drives). Plug headphones into the lime-green 3.5mm jack.\n4. **Step 4: Connect Wired Network**: Insert the RJ-45 Ethernet cable into the computer's network socket until the plastic retention tab makes an audible **click**. Connect the other end to the LAN switch/router.\n5. **Step 5: Connect Mains Power Safely**: Connect the IEC C13 cable to the computer's Power Supply Unit (PSU) and the monitor's power adapter. Plug all plugs into a **Surge Protector** or **Uninterruptible Power Supply (UPS)** rather than bare wall outlets.\n6. **Step 6: Power-On Sequence**: Switch on the surge protector. Press the **monitor power button first**, followed by the **computer tower power button**. This ensures display synchronization occurs before the BIOS splash screen flashes.\n7. **Step 7: Software Initialization & Driver Verification**: Complete the operating system initial setup wizard (regional timezone, user accounts). Check Device Manager to ensure all peripheral drivers are loaded.\n8. **Step 8: Safe Software-Guided Shutdown**: When finished, always shut down via the operating system menu to flush file system buffers and protect storage drives."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "The Workstation Assembly Pipeline Flowchart",
                        "content": {
                            "caption": "Step-by-step visual pipeline guiding the assembly technician from environmental unboxing through video interfacing, power safety, and initial boot.",
                            "svg_content": SVG_WORKSTATION_ASSEMBLY_PIPELINE
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "How to Assemble and Set Up a Desktop Computer Workstation",
                        "content": {
                            "url": "https://www.youtube.com/watch?v=8M_3r_Y8Z68",
                            "youtube_id": "8M_3r_Y8Z68",
                            "description": "Step-by-step visual demonstration of assembling a desktop PC workstation, connecting peripherals, surge protection, and initial boot testing."
                        }
                    }
                ],

                # Page 2: Electrical Protection & Power Sequencing Under the Hood
                [
                    {
                        "type": "concept_explanation",
                        "title": "3. Electrical Safety & Grid Fluctuation Protection",
                        "content": {
                            "text": "Computers operate on microscopic silicon transistors etched with conductive channels just nanometers wide. Sudden electrical disturbances on the power grid can instantly vaporize these delicate circuit paths.\n\n### **A. Surge Protectors (Metal Oxide Varistors - MOVs)**\nKenya's electrical grid can experience sudden high-voltage transients (surges or spikes) caused by lightning strikes or grid switching. A standard **surge protector** contains Metal Oxide Varistors (MOVs) that act as voltage-sensitive valves. When voltage exceeds safe thresholds, the MOV instantly redirects the excess energy to the earth ground wire, sacrificing its internal components to shield the computer's power supply and motherboard.\n\n### **B. Uninterruptible Power Supplies (UPS)**\nA UPS contains an internal rechargeable lead-acid or lithium-ion battery, an AC-to-DC charger, and a DC-to-AC inverter. During brownouts (voltage drops) or total blackouts, the UPS switches to battery power in under **10 milliseconds**. This gives users sufficient time to save unsaved documents and perform a graceful system shutdown.\n\n### **C. The Mechanics of Safe Shutdown**\nNever cut power by flipping the surge protector switch or holding down the physical case button while the operating system is running!\n\n**Under-the-Hood Operations During Safe Shutdown**:\n1. **Flushing Disk Caches**: The OS forces all unwritten data sitting in volatile RAM write-buffers to be committed permanently to non-volatile SSD/HDD sectors.\n2. **Closing File Handles & Registry Logs**: The file system closes open database journals and system registries to prevent data corruption.\n3. **Terminating Background Services**: System daemons and user applications receive `SIGTERM` signals to cleanly save state.\n4. **Parking Mechanical Drive Heads**: Hard disk drives safely retract magnetic read/write heads to the landing ramp, preventing catastrophic platter head-crashes."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Computer Power Supply Unit and Power Connections",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/ATX_Power_Supply_Unit.jpg/800px-ATX_Power_Supply_Unit.jpg",
                            "caption": "An ATX desktop power supply unit showing the IEC C14 power inlet socket, exhaust fan grill, and power switch.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    }
                ],

                # Page 3: Workstation Subsystem Testing & Verification Protocol
                [
                    {
                        "type": "concept_explanation",
                        "title": "4. Workstation Subsystem Verification Checklist",
                        "content": {
                            "text": "Once a newly assembled computer boots into the operating system, a computer scientist must execute a structured diagnostic audit before commissioning the workstation for production use:\n\n```\n========================================================================================\n                             HARDWARE VERIFICATION CHECKLIST\n========================================================================================\n[  ] Display Audit  -> Verify resolution matches native panel and colors are accurate.\n[  ] Input Test     -> Verify every key on keyboard registers and mouse tracks smoothly.\n[  ] Audio Test     -> Play stereo sound file to verify left and right channels operate.\n[  ] Network Audit  -> Ping a local gateway to verify DHCP IP lease and DNS resolution.\n[  ] Safe Shutdown  -> Close all processes and execute software-guided power-down.\n========================================================================================\n```\n\n### **Detailed Diagnostic Procedures**:\n1. **Display Audit**: Inspect on-screen typography. If fonts appear blurry, jagged, or stretched, navigate to OS Display Settings and configure the resolution to match the monitor's native panel hardware (e.g., 1920x1080 @ 60Hz).\n2. **Input Device Audit**: Open a text editor. Sequentially press every key on the keyboard (including function keys and numpad) to verify keystroke registration. Move the mouse in circular trajectories to confirm optical tracking without stuttering.\n3. **Audio Subsystem Test**: Play a stereo test tone. Confirm clean acoustic separation across the left and right speakers without crackling, hum, or channel swapping.\n4. **Network Connectivity Audit**: Open the Command Line Interface (CLI) and issue an ICMP echo ping command:\n   ```bash\n   ping 8.8.8.8 -c 4\n   ```\n   Confirm zero packet loss and low latency (< 50ms) to verify operational network stack and gateway routing."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Desktop Computer Motherboard Rear I/O Panel",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Motherboard_I_O_panel.jpg/800px-Motherboard_I_O_panel.jpg",
                            "caption": "Figure 7.5: Rear I/O panel of a desktop computer motherboard illustrating USB, display, Ethernet, and 3.5mm analog audio jacks.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "5. Workstation Diagnostics Case Study: The Dedicated GPU Trap",
                        "content": {
                            "text": "### **Troubleshooting Case: 'The Silent Screen'**\n- **Symptom**: In a school computer lab, a newly assembled workstation powers on. The blue chassis power LED glows, cooling fans spin rapidly, but the monitor displays **'No Signal Detected'** and enters orange sleep mode.\n\n### **Fault Isolation Analysis**:\n- **Check 1: Physical Power**: Verify monitor power cord is plugged in and monitor power button is turned on.\n- **Check 2: Cable Seating**: Check that both ends of the HDMI/DP cable are firmly pushed in.\n- **Check 3: The Dedicated GPU Trap (Root Cause)**: Look at the rear panel of the computer. The user plugged the HDMI cable into the vertical motherboard port. When a motherboard detects a dedicated graphics card in its PCI-Express slot, it **automatically disables integrated motherboard video ports**. The video cable must be moved down to the horizontal ports on the dedicated GPU!\n- **Check 4: Monitor Input Channel**: Use the monitor's physical OSD buttons to select the active input port (e.g., HDMI-1 instead of Auto/VGA)."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Dedicated GPU Video Port Trap & Diagnostic Flow",
                        "content": {
                            "caption": "Back I/O shield breakdown illustrating why vertical motherboard display ports are deactivated when a dedicated graphics card is installed.",
                            "svg_content": SVG_GPU_TRAP_TROUBLESHOOTING
                        }
                    }
                ],

                # Page 4: Formative Assessment & Hands-on Diagnostic Scenarios
                [
                    {
                        "type": "worked_example",
                        "title": "Diagnostic Report: Chief IT Inspector Lab Audit",
                        "content": {
                            "scenario": "As the Lead Computer Science Technician, you inspect three malfunctioning student workstations in the computer laboratory. Provide root-cause diagnoses and immediate corrective actions.",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "step_title": "Workstation A: Tower boots, monitor shows 'Check Signal Cable'",
                                    "explanation": "Diagnosis: The student plugged the monitor's VGA cable into the vertical motherboard video output while a dedicated GPU is installed in the PCI-e expansion slot.\nAction: Power down the system, move the video cable to the horizontal display ports on the dedicated graphics card, hand-tighten the thumb screws, and reboot."
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Workstation B: HDMI display works, but all text is blurry and circles are stretched into ovals",
                                    "explanation": "Diagnosis: The operating system video driver is outputting at a non-native aspect ratio (e.g., 1024x768 stretched onto a 16:9 1080p widescreen panel).\nAction: Right-click the desktop, open Display Settings, and set Resolution to 1920x1080 (Recommended/Native). Install the official GPU manufacturer drivers if the native resolution option is missing."
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Workstation C: Student headphones plugged into the pink port have no audio in tutorials",
                                    "explanation": "Diagnosis: The pink 3.5mm jack is reserved exclusively for microphone audio input under the PC 99 standard.\nAction: Unplug the 3.5mm headphone jack from the pink port and insert it into the lime-green Stereo Line-Out port."
                                }
                            ]
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Safe Setup & Diagnostic Protocols",
                        "content": {
                            "text": "1. **Structured 8-Step Setup**: Follow the sequential protocol from unboxing and video connection through mains surge protection, powering monitor first, then host tower.\n2. **Electrical Safety**: Always use a Surge Protector (MOVs for spike diversion) or a UPS (battery backup). Never perform an abrupt hard power cut.\n3. **Dedicated GPU Rule**: When a dedicated graphics card is present, always plug video cables into the lower horizontal GPU ports, not the motherboard ports.\n4. **Post-Boot Audit**: Methodically verify display resolution, input tracking, stereo audio separation, and network connectivity via ping."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Assessment: Setup, Safety & Troubleshooting",
                        "content": {
                            "questions": [
                                {
                                    "question": "Where should a monitor's display cable be connected if the computer tower contains an installed dedicated graphics card?",
                                    "options": [
                                        "A) Into the vertical display ports on the motherboard I/O shield",
                                        "B) Into the horizontal display ports on the dedicated graphics card",
                                        "C) Into any available blue USB 3.0 port",
                                        "D) Into the power supply unit's IEC C14 connector"
                                    ],
                                    "answer": "B) Into the horizontal display ports on the dedicated graphics card",
                                    "explanation": "When a dedicated graphics card is installed, the system BIOS deactivates the integrated motherboard video outputs to route all graphical processing through the dedicated GPU."
                                },
                                {
                                    "question": "Why is it dangerous to turn off a computer by abruptly pulling the power cable or switching off the wall socket while the OS is running?",
                                    "options": [
                                        "A) It permanently demagnetizes the monitor's LCD backlight.",
                                        "B) It causes unwritten RAM write-buffers to be lost, corrupting open files and system registry databases.",
                                        "C) It reverses the polarity of the Ethernet network controller.",
                                        "D) It increases power consumption on the next bootup cycle."
                                    ],
                                    "answer": "B) It causes unwritten RAM write-buffers to be lost, corrupting open files and system registry databases.",
                                    "explanation": "A safe shutdown gives the OS time to flush RAM caches to disk, close open database/file handles, and park mechanical heads. Abrupt power loss risks severe file system corruption."
                                },
                                {
                                    "question": "What is the primary function of a Surge Protector in a computer workstation setup?",
                                    "options": [
                                        "A) It converts digital video signals into analog audio.",
                                        "B) It absorbs sudden voltage spikes from the mains grid, protecting delicate motherboard circuits from electrical destruction.",
                                        "C) It speeds up the CPU clock frequency during heavy computational loads.",
                                        "D) It provides 4 hours of battery backup during a power blackout."
                                    ],
                                    "answer": "B) It absorbs sudden voltage spikes from the mains grid, protecting delicate motherboard circuits from electrical destruction.",
                                    "explanation": "Surge protectors utilize internal Metal Oxide Varistors (MOVs) to clamp and divert transient high-voltage spikes to ground, preventing damage to sensitive electronic components."
                                },
                                {
                                    "question": "Why is it recommended to leave a minimum of 10 to 15 centimeters of clearance around the computer tower's exhaust fans?",
                                    "options": [
                                        "A) To allow optical wireless signals to bounce off walls.",
                                        "B) To maintain adequate airflow circulation and prevent thermal throttling or heat damage to the CPU and PSU.",
                                        "C) To prevent electromagnetic interference from touching the desk.",
                                        "D) To comply with monitor cable length standards."
                                    ],
                                    "answer": "B) To maintain adequate airflow circulation and prevent thermal throttling or heat damage to the CPU and PSU.",
                                    "explanation": "Restricting exhaust clearance traps hot air inside the chassis, causing internal temperatures to rise, leading to CPU thermal throttling, system instability, and component degradation."
                                }
                            ]
                        }
                    }
                ]
            ]
        }
    ]

# =====================================================================
# INGESTION EXECUTOR
# =====================================================================

def ingest_grade10_topic7(replace: bool = True):
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 10 Computer Science — Topic 7: Computer Setup")
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
        order=7,
        defaults={
            "name": "Computer Setup",
            "description": "Physical and logical setup of computer systems: identification of ports and cables, peripheral connections, workstation assembly sequence, power safety, functional testing, and troubleshooting."
        }
    )
    if not t_created:
        topic.name = "Computer Setup"
        topic.description = "Physical and logical setup of computer systems: identification of ports and cables, peripheral connections, workstation assembly sequence, power safety, functional testing, and troubleshooting."
        topic.save()
    print(f"[*] Resolved Topic 7: {topic.name} (ID: {topic.id})")

    if replace:
        print("[*] Replacing existing Topic 7 units, lessons, blocks, and assets...")
        existing_lessons = Lesson.objects.filter(topic=topic)
        LessonAsset.objects.filter(lesson__in=existing_lessons).delete()
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    curriculum_data = build_topic7_curriculum()
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
                    "topic_order": 7,
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

                    if b_type == "knowledge_check" and "questions" in b_content and isinstance(b_content["questions"], list):
                        for q_idx, q_item in enumerate(b_content["questions"], start=1):
                            q_content = {
                                "question": q_item.get("question", ""),
                                "options": q_item.get("options", []),
                                "correct": q_item.get("answer", "")[0] if q_item.get("answer") else "A",
                                "answer": q_item.get("answer", ""),
                                "explanation": q_item.get("explanation", "")
                            }
                            block = LessonBlock.objects.create(
                                lesson=lesson,
                                block_id=f"g10_cs_t7_u{u_order}_p{page_idx}_mcq{q_idx}",
                                block_type="knowledge_check",
                                component_type="knowledge_check",
                                title=f"Knowledge Check {q_idx}: {b_title}",
                                content=q_content,
                                order=block_counter,
                                page_number=page_idx,
                                component_order=comp_idx + q_idx - 1,
                                page_title=b_title if comp_idx == 1 and q_idx == 1 else None,
                                metadata={"topic_order": 7, "unit_order": u_order, "page": page_idx}
                            )
                            block_counter += 1
                            total_blocks += 1
                        continue

                    block = LessonBlock.objects.create(
                        lesson=lesson,
                        block_id=f"g10_cs_t7_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={"topic_order": 7, "unit_order": u_order, "page": page_idx}
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
    print("TOPIC 7 INGESTION COMPLETE:")
    print(f"  Units Created:   {total_units}")
    print(f"  Lessons Created: {total_lessons}")
    print(f"  Pages Created:   {total_pages}")
    print(f"  Blocks Created:  {total_blocks}")
    print(f"  Assets Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_grade10_topic7(replace=True)
