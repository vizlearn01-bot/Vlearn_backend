"""
VLearn CBC Grade 10 Computer Science — Topic 10: Computer Network Elements
Production Ingestion & Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Computer Science (ID: 38)
Topic: Computer Network Elements (Topic Order: 10)

Decomposed into 4 Comprehensive Learning Units & 4 Published Lessons:
  1. Types and Geographical Scope of Computer Networks (Lesson 33: Types and Scope of Computer Networks)
  2. Network Devices, Hardware Roles, and DTE vs. DCE (Lesson 34: Network Devices and Elements)
  3. Network Evaluation Criteria, Physical Connection Setup, and Security (Lesson 35: Criteria, Connection, and Role of Networks)
  4. Network Diagnostic Protocols and Practical Troubleshooting (Lesson 36: Network Communication and Integrated Practical)
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
# HIGH PRECISION VECTOR SVGS FOR TOPIC 10
# =====================================================================

SVG_CONCENTRIC_NETWORK_SCOPES = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Classification of Computer Networks by Geographical Scope</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">From personal wearable bubbles (PAN) to global subsea internet backbones (WAN)</text>

  <!-- Left: Concentric Circles Graphic -->
  <g transform="translate(240, 290)">
    <!-- Outer Ring: WAN -->
    <circle cx="0" cy="0" r="190" fill="#0f172a" stroke="#818cf8" stroke-width="2.5" stroke-dasharray="6,4"/>
    <text x="0" y="-170" font-size="12" font-weight="bold" fill="#a5b4fc" text-anchor="middle">WAN (Wide Area Network) — Global / Continents</text>

    <!-- Ring 3: MAN -->
    <circle cx="0" cy="0" r="145" fill="#172554" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="0" y="-128" font-size="11" font-weight="bold" fill="#7dd3fc" text-anchor="middle">MAN (Metropolitan Area Network) — 10 to 50 km</text>

    <!-- Ring 2: LAN / WLAN -->
    <circle cx="0" cy="0" r="100" fill="#064e3b" stroke="#34d399" stroke-width="2.5"/>
    <text x="0" y="-82" font-size="10.5" font-weight="bold" fill="#6ee7b7" text-anchor="middle">LAN / WLAN — Within 1 km / 100 m</text>

    <!-- Inner Core: PAN -->
    <circle cx="0" cy="0" r="55" fill="#831843" stroke="#f472b6" stroke-width="2.5"/>
    <text x="0" y="-10" font-size="11" font-weight="bold" fill="#fbcfe8" text-anchor="middle">PAN</text>
    <text x="0" y="10" font-size="9" fill="#f472b6" text-anchor="middle">&lt; 10 Meters</text>
    <text x="0" y="25" font-size="8" fill="#cbd5e1" text-anchor="middle">Bluetooth / USB</text>
  </g>

  <!-- Right: Detailed Scope Cards -->
  <g transform="translate(480, 90)">
    <!-- PAN Card -->
    <g transform="translate(0, 0)">
      <rect width="440" height="85" rx="8" fill="#0f172a" stroke="#f472b6" stroke-width="1.5"/>
      <rect width="8" height="85" rx="4" fill="#ec4899"/>
      <text x="25" y="24" font-size="13" font-weight="bold" fill="#f472b6">1. PAN (Personal Area Network)</text>
      <text x="25" y="44" font-size="10" fill="#cbd5e1"><tspan font-weight="bold" fill="#94a3b8">Scope:</tspan> Within 10 meters (Single individual bubble)</text>
      <text x="25" y="60" font-size="10" fill="#cbd5e1"><tspan font-weight="bold" fill="#94a3b8">Media:</tspan> Bluetooth 5.x, NFC, Infrared, Direct USB cable</text>
      <text x="25" y="76" font-size="10" fill="#cbd5e1"><tspan font-weight="bold" fill="#94a3b8">Example:</tspan> Smartwatch syncing heart rate to phone; wireless earbuds</text>
    </g>

    <!-- LAN / WLAN Card -->
    <g transform="translate(0, 95)">
      <rect width="440" height="90" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
      <rect width="8" height="90" rx="4" fill="#10b981"/>
      <text x="25" y="24" font-size="13" font-weight="bold" fill="#34d399">2. LAN &amp; WLAN (Local Area Network)</text>
      <text x="25" y="44" font-size="10" fill="#cbd5e1"><tspan font-weight="bold" fill="#94a3b8">Scope:</tspan> Single room, lab, or building (Up to 1 km; WLAN ~100m)</text>
      <text x="25" y="60" font-size="10" fill="#cbd5e1"><tspan font-weight="bold" fill="#94a3b8">Media:</tspan> Cat6 UTP Ethernet cables, Switches, Wi-Fi 6 (802.11ax)</text>
      <text x="25" y="76" font-size="10" fill="#cbd5e1"><tspan font-weight="bold" fill="#94a3b8">Example:</tspan> School computer laboratory sharing a central laser printer</text>
    </g>

    <!-- MAN Card -->
    <g transform="translate(0, 195)">
      <rect width="440" height="90" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
      <rect width="8" height="90" rx="4" fill="#0284c7"/>
      <text x="25" y="24" font-size="13" font-weight="bold" fill="#38bdf8">3. MAN (Metropolitan Area Network)</text>
      <text x="25" y="44" font-size="10" fill="#cbd5e1"><tspan font-weight="bold" fill="#94a3b8">Scope:</tspan> 10 to 50 km (Entire town, city, or multi-building campus)</text>
      <text x="25" y="60" font-size="10" fill="#cbd5e1"><tspan font-weight="bold" fill="#94a3b8">Media:</tspan> High-speed singlemode fiber backbones, WiMAX microwave</text>
      <text x="25" y="76" font-size="10" fill="#cbd5e1"><tspan font-weight="bold" fill="#94a3b8">Example:</tspan> Municipal traffic camera network or cable TV across Mombasa</text>
    </g>

    <!-- WAN Card -->
    <g transform="translate(0, 295)">
      <rect width="440" height="90" rx="8" fill="#0f172a" stroke="#818cf8" stroke-width="1.5"/>
      <rect width="8" height="90" rx="4" fill="#6366f1"/>
      <text x="25" y="24" font-size="13" font-weight="bold" fill="#a5b4fc">4. WAN (Wide Area Network)</text>
      <text x="25" y="44" font-size="10" fill="#cbd5e1"><tspan font-weight="bold" fill="#94a3b8">Scope:</tspan> National, continental, or planetary scale</text>
      <text x="25" y="60" font-size="10" fill="#cbd5e1"><tspan font-weight="bold" fill="#94a3b8">Media:</tspan> Subsea fiber cables (TEAMS, SEACOM), Geostationary satellites</text>
      <text x="25" y="76" font-size="10" fill="#cbd5e1"><tspan font-weight="bold" fill="#94a3b8">Example:</tspan> The Global Internet connecting Kenyan schools to cloud hosts</text>
    </g>
  </g>
</svg>
""")

SVG_DTE_VS_DCE_ARCHITECTURE = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Network Hardware Roles: DTE (Data Terminal) vs. DCE (Circuit-Terminating)</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">The fundamental communication pipeline separating source/sink endpoints from line modulators</text>

  <!-- Left Side: Source Site -->
  <g transform="translate(50, 95)">
    <rect width="380" height="240" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <text x="190" y="26" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">Local Subscriber Site A</text>

    <!-- DTE 1 -->
    <rect x="20" y="45" width="150" height="170" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="20" y="45" width="150" height="26" rx="6" fill="#0284c7"/>
    <text x="95" y="62" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">DTE (Source / Sink)</text>
    <text x="95" y="95" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Computer / Server</text>
    <text x="95" y="120" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; Generates digital bits</text>
    <text x="95" y="138" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; Originates payload</text>
    <text x="95" y="156" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; Unaware of line physics</text>
    <rect x="35" y="175" width="120" height="25" rx="4" fill="#0f172a" stroke="#38bdf8"/>
    <text x="95" y="191" font-size="9" fill="#7dd3fc" text-anchor="middle">10110010 (Digital)</text>

    <!-- Arrow DTE to DCE -->
    <line x1="170" y1="130" x2="205" y2="130" stroke="#38bdf8" stroke-width="2.5"/>
    <polygon points="205,126 215,130 205,134" fill="#38bdf8"/>

    <!-- DCE 1 -->
    <rect x="215" y="45" width="145" height="170" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect x="215" y="45" width="145" height="26" rx="6" fill="#059669"/>
    <text x="287" y="62" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">DCE (Interface)</text>
    <text x="287" y="95" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">Modem / CSU / NIC</text>
    <text x="287" y="120" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; Modulates / Encodes</text>
    <text x="287" y="138" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; Line clocking &amp; sync</text>
    <text x="287" y="156" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; Physical layer bridge</text>
    <rect x="228" y="175" width="120" height="25" rx="4" fill="#0f172a" stroke="#10b981"/>
    <text x="287" y="191" font-size="9" fill="#6ee7b7" text-anchor="middle">Modulated Waves ~~~</text>
  </g>

  <!-- Middle: Transmission Medium -->
  <g transform="translate(430, 160)">
    <rect x="0" y="20" width="100" height="70" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <text x="50" y="45" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">PHYSICAL</text>
    <text x="50" y="60" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">CARRIER</text>
    <text x="50" y="76" font-size="8" fill="#cbd5e1" text-anchor="middle">Fiber / Copper / Air</text>
    <line x1="-50" y1="55" x2="0" y2="55" stroke="#f59e0b" stroke-width="3" stroke-dasharray="4"/>
    <line x1="100" y1="55" x2="150" y2="55" stroke="#f59e0b" stroke-width="3" stroke-dasharray="4"/>
  </g>

  <!-- Right Side: Destination Site -->
  <g transform="translate(530, 95)">
    <rect width="380" height="240" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <text x="190" y="26" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">Remote Subscriber Site B</text>

    <!-- DCE 2 -->
    <rect x="20" y="45" width="145" height="170" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect x="20" y="45" width="145" height="26" rx="6" fill="#059669"/>
    <text x="92" y="62" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">DCE (Interface)</text>
    <text x="92" y="95" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">Modem / Demodulator</text>
    <text x="92" y="120" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; Demodulates signals</text>
    <text x="92" y="138" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; Extracts clean bits</text>
    <text x="92" y="156" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; Feeds DTE bus</text>
    <rect x="33" y="175" width="120" height="25" rx="4" fill="#0f172a" stroke="#10b981"/>
    <text x="92" y="191" font-size="9" fill="#6ee7b7" text-anchor="middle">10110010 (Bits)</text>

    <!-- Arrow DCE to DTE -->
    <line x1="165" y1="130" x2="200" y2="130" stroke="#38bdf8" stroke-width="2.5"/>
    <polygon points="200,126 210,130 200,134" fill="#38bdf8"/>

    <!-- DTE 2 -->
    <rect x="210" y="45" width="150" height="170" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="210" y="45" width="150" height="26" rx="6" fill="#0284c7"/>
    <text x="285" y="62" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">DTE (Destination)</text>
    <text x="285" y="95" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Web Server / PC</text>
    <text x="285" y="120" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; Consumes data frames</text>
    <text x="285" y="138" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; Delivers to App layer</text>
    <text x="285" y="156" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; Database / Print queue</text>
    <rect x="225" y="175" width="120" height="25" rx="4" fill="#0f172a" stroke="#38bdf8"/>
    <text x="285" y="191" font-size="9" fill="#7dd3fc" text-anchor="middle">Processed Payload</text>
  </g>

  <!-- Bottom Comparison Summary Bar -->
  <g transform="translate(50, 355)">
    <rect width="860" height="130" rx="10" fill="#0f172a" stroke="#64748b" stroke-width="1"/>
    <text x="20" y="28" font-size="12" font-weight="bold" fill="#f59e0b">Summary Table: DTE vs. DCE Differentiation</text>
    <line x1="20" y1="38" x2="840" y2="38" stroke="#334155" stroke-width="1"/>
    
    <text x="30" y="60" font-size="10" font-weight="bold" fill="#38bdf8">Attribute</text>
    <text x="220" y="60" font-size="10" font-weight="bold" fill="#38bdf8">DTE (Data Terminal Equipment)</text>
    <text x="560" y="60" font-size="10" font-weight="bold" fill="#10b981">DCE (Data Circuit-terminating Equipment)</text>

    <text x="30" y="82" font-size="9.5" fill="#94a3b8">Primary Role:</text>
    <text x="220" y="82" font-size="9.5" fill="#cbd5e1">Creates, processes, or consumes application data</text>
    <text x="560" y="82" font-size="9.5" fill="#cbd5e1">Converts, modulates, and clocks data for transmission line</text>

    <text x="30" y="104" font-size="9.5" fill="#94a3b8">Physical Placement:</text>
    <text x="220" y="104" font-size="9.5" fill="#cbd5e1">At user end-points (desktops, servers, terminals)</text>
    <text x="560" y="104" font-size="9.5" fill="#cbd5e1">Between DTE and the physical telecom network</text>

    <text x="30" y="122" font-size="9.5" fill="#94a3b8">Typical Devices:</text>
    <text x="220" y="122" font-size="9.5" fill="#cbd5e1">PCs, Laptops, Network Printers, Database Servers</text>
    <text x="560" y="122" font-size="9.5" fill="#cbd5e1">Modems (DSL/Cable), CSU/DSU, Optical Transceivers, NICs</text>
  </g>
</svg>
""")

SVG_HUB_VS_SWITCH_VS_ROUTER = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Network Mechanics: Hub vs. Switch vs. Router</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Collision domains, addressing layers (Physical vs. MAC vs. IP), and forwarding intelligence</text>

  <!-- 1. HUB (Layer 1) -->
  <g transform="translate(40, 95)">
    <rect width="270" height="385" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#dc2626"/>
    <text x="135" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. HUB (Layer 1 Physical)</text>

    <rect x="15" y="40" width="240" height="60" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="135" y="62" font-size="10.5" font-weight="bold" fill="#f87171" text-anchor="middle">Blind Electrical Repeater</text>
    <text x="135" y="82" font-size="8.5" fill="#fca5a5" text-anchor="middle">Replicates incoming bits out ALL ports</text>

    <text x="15" y="125" font-size="10" font-weight="bold" fill="#f87171">&#8226; Addressing Used: NONE</text>
    <text x="15" y="145" font-size="9" fill="#cbd5e1">Cannot read MAC or IP addresses.</text>

    <text x="15" y="175" font-size="10" font-weight="bold" fill="#f87171">&#8226; Collision Domain: 1 Shared Domain</text>
    <text x="15" y="195" font-size="9" fill="#cbd5e1">If 2 devices transmit simultaneously, signals collide and corrupt. Half-duplex only.</text>

    <text x="15" y="235" font-size="10" font-weight="bold" fill="#f87171">&#8226; Security &amp; Efficiency:</text>
    <text x="15" y="255" font-size="9" fill="#cbd5e1">Extremely poor. Every computer receives every frame, wasting bandwidth.</text>

    <rect x="15" y="300" width="240" height="65" rx="6" fill="#1e293b"/>
    <text x="25" y="322" font-size="9.5" font-weight="bold" fill="#f87171">Status: Legacy / Obsolete</text>
    <text x="25" y="342" font-size="8.5" fill="#94a3b8">Replaced entirely by modern multi-port LAN switches.</text>
  </g>

  <!-- 2. SWITCH (Layer 2) -->
  <g transform="translate(345, 95)">
    <rect width="270" height="385" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#0284c7"/>
    <text x="135" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. SWITCH (Layer 2 Data Link)</text>

    <rect x="15" y="40" width="240" height="60" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="135" y="62" font-size="10.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Intelligent Local Forwarder</text>
    <text x="135" y="82" font-size="8.5" fill="#7dd3fc" text-anchor="middle">Maintains dynamic MAC Address Table</text>

    <text x="15" y="125" font-size="10" font-weight="bold" fill="#38bdf8">&#8226; Addressing Used: MAC Address</text>
    <text x="15" y="145" font-size="9" fill="#cbd5e1">Hardware burn-in address (48-bit hex).</text>

    <text x="15" y="175" font-size="10" font-weight="bold" fill="#38bdf8">&#8226; Collision Domain: Isolated / Port</text>
    <text x="15" y="195" font-size="9" fill="#cbd5e1">Each port is a separate collision domain. Simultaneous Full-Duplex TX/RX.</text>

    <text x="15" y="235" font-size="10" font-weight="bold" fill="#38bdf8">&#8226; Boundary Limitation:</text>
    <text x="15" y="255" font-size="9" fill="#cbd5e1">Forwards frames ONLY within the local LAN segment; cannot cross subnets.</text>

    <rect x="15" y="300" width="240" height="65" rx="6" fill="#1e293b"/>
    <text x="25" y="322" font-size="9.5" font-weight="bold" fill="#38bdf8">Primary LAN Workhorse</text>
    <text x="25" y="342" font-size="8.5" fill="#94a3b8">Connects PCs, printers, and servers inside classrooms and offices.</text>
  </g>

  <!-- 3. ROUTER (Layer 3) -->
  <g transform="translate(650, 95)">
    <rect width="270" height="385" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#059669"/>
    <text x="135" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. ROUTER (Layer 3 Network)</text>

    <rect x="15" y="40" width="240" height="60" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="135" y="62" font-size="10.5" font-weight="bold" fill="#34d399" text-anchor="middle">Inter-Network Pathfinding</text>
    <text x="135" y="82" font-size="8.5" fill="#6ee7b7" text-anchor="middle">Uses Routing Tables &amp; IP Gateways</text>

    <text x="15" y="125" font-size="10" font-weight="bold" fill="#34d399">&#8226; Addressing Used: IP Address</text>
    <text x="15" y="145" font-size="9" fill="#cbd5e1">Logical addresses (IPv4 / IPv6).</text>

    <text x="15" y="175" font-size="10" font-weight="bold" fill="#34d399">&#8226; Broadcast Domain: Breaks Domain</text>
    <text x="15" y="195" font-size="9" fill="#cbd5e1">Stops local broadcast noise from spreading across the wide area network.</text>

    <text x="15" y="235" font-size="10" font-weight="bold" fill="#34d399">&#8226; Internet Gateway:</text>
    <text x="15" y="255" font-size="9" fill="#cbd5e1">Determines optimal path (hops) to route packets across distinct networks.</text>

    <rect x="15" y="300" width="240" height="65" rx="6" fill="#1e293b"/>
    <text x="25" y="322" font-size="9.5" font-weight="bold" fill="#34d399">Global Gateway Core</text>
    <text x="25" y="342" font-size="8.5" fill="#94a3b8">Bridges local LANs to ISP uplinks and the global Internet WAN.</text>
  </g>
</svg>
""")

SVG_PHYSICAL_CONNECTION_AND_LEDS = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Physical Network Connection &amp; Hardware Verification Protocol</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Step-by-step procedure: Physical RJ-45 Seating, Port LED Diagnostics, and IP Verification</text>

  <!-- Step 1: Physical Link -->
  <g transform="translate(45, 95)">
    <rect width="265" height="385" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="265" height="28" rx="8" fill="#0284c7"/>
    <text x="132" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Step 1: Physical Link</text>
    
    <!-- RJ-45 Plug Graphic -->
    <rect x="50" y="45" width="165" height="85" rx="8" fill="#1e293b" stroke="#38bdf8"/>
    <rect x="75" y="55" width="115" height="40" rx="4" fill="#0f172a" stroke="#94a3b8"/>
    <rect x="85" y="60" width="10" height="15" fill="#f59e0b"/>
    <rect x="100" y="60" width="10" height="15" fill="#f59e0b"/>
    <rect x="115" y="60" width="10" height="15" fill="#f59e0b"/>
    <rect x="130" y="60" width="10" height="15" fill="#f59e0b"/>
    <rect x="145" y="60" width="10" height="15" fill="#f59e0b"/>
    <rect x="160" y="60" width="10" height="15" fill="#f59e0b"/>
    <text x="132" y="115" font-size="9" fill="#38bdf8" text-anchor="middle">RJ-45 8P8C Connector &amp; Cat6</text>

    <text x="15" y="155" font-size="10" font-weight="bold" fill="#38bdf8">&#8226; Action Protocol:</text>
    <text x="15" y="175" font-size="9.5" fill="#cbd5e1">1. Inspect 8 gold-plated pins for corrosion.</text>
    <text x="15" y="195" font-size="9.5" fill="#cbd5e1">2. Seat RJ-45 connector firmly into NIC.</text>
    <text x="15" y="215" font-size="9.5" fill="#cbd5e1">3. Listen for distinct audible CLICK locking plastic retaining latch.</text>
    <text x="15" y="245" font-size="9.5" fill="#cbd5e1">4. Plug opposite end into classroom switch port or wall socket.</text>
    
    <rect x="15" y="300" width="235" height="65" rx="6" fill="#1e293b"/>
    <text x="25" y="322" font-size="9.5" font-weight="bold" fill="#38bdf8">Hardware Standard:</text>
    <text x="25" y="342" font-size="8.5" fill="#94a3b8">Category 6 UTP (Gigabit 1000BASE-T)</text>
  </g>

  <!-- Step 2: Port LED Diagnostics -->
  <g transform="translate(345, 95)">
    <rect width="270" height="385" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#059669"/>
    <text x="135" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Step 2: LED Port Diagnostics</text>

    <!-- NIC Port with LEDs Graphic -->
    <rect x="40" y="45" width="190" height="85" rx="8" fill="#1e293b" stroke="#10b981"/>
    <rect x="65" y="55" width="140" height="40" rx="4" fill="#000000"/>
    
    <!-- Link LED (Green) -->
    <circle cx="85" cy="110" r="7" fill="#22c55e" stroke="#15803d" stroke-width="1.5"/>
    <text x="98" y="114" font-size="8.5" font-weight="bold" fill="#4ade80">LINK (Solid)</text>

    <!-- Activity LED (Amber) -->
    <circle cx="165" cy="110" r="7" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
    <text x="178" y="114" font-size="8.5" font-weight="bold" fill="#fbbf24">ACT (Blink)</text>

    <text x="15" y="155" font-size="10" font-weight="bold" fill="#34d399">&#8226; Link LED (Solid Green):</text>
    <text x="15" y="175" font-size="9.5" fill="#cbd5e1">Confirms physical electrical carrier link is active with switch at 1 Gbps.</text>

    <text x="15" y="210" font-size="10" font-weight="bold" fill="#fbbf24">&#8226; Activity LED (Flashing Amber):</text>
    <text x="15" y="230" font-size="9.5" fill="#cbd5e1">Indicates active data packets (frames) moving across the wire.</text>

    <rect x="15" y="280" width="240" height="85" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="25" y="302" font-size="9.5" font-weight="bold" fill="#f87171">Diagnostic Red Flag:</text>
    <text x="25" y="322" font-size="8.5" fill="#fca5a5">&#8226; LEDs OFF = Broken cable or dead port.</text>
    <text x="25" y="342" font-size="8.5" fill="#fca5a5">&#8226; Fast Amber loop = Duplex mismatch.</text>
  </g>

  <!-- Step 3: Logical OS Verification -->
  <g transform="translate(650, 95)">
    <rect width="265" height="385" rx="10" fill="#0f172a" stroke="#818cf8" stroke-width="1.5"/>
    <rect width="265" height="28" rx="8" fill="#6366f1"/>
    <text x="132" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Step 3: Software IP Check</text>

    <!-- Terminal Box Graphic -->
    <rect x="15" y="45" width="235" height="110" rx="6" fill="#000000" stroke="#334155"/>
    <text x="25" y="65" font-family="monospace" font-size="9" fill="#4ade80">C:\&gt; ipconfig</text>
    <text x="25" y="82" font-family="monospace" font-size="8" fill="#94a3b8">IPv4 Address: 192.168.1.45</text>
    <text x="25" y="98" font-family="monospace" font-size="8" fill="#94a3b8">Subnet Mask: 255.255.255.0</text>
    <text x="25" y="114" font-family="monospace" font-size="8" fill="#94a3b8">Default Gateway: 192.168.1.1</text>
    <text x="25" y="138" font-family="monospace" font-size="8" fill="#38bdf8">DHCP Handshake: SUCCESS</text>

    <text x="15" y="175" font-size="10" font-weight="bold" fill="#a5b4fc">&#8226; Verification Commands:</text>
    <text x="15" y="195" font-size="9.5" fill="#cbd5e1">Windows: <tspan font-family="monospace" fill="#38bdf8">ipconfig /all</tspan></text>
    <text x="15" y="215" font-size="9.5" fill="#cbd5e1">Linux / macOS: <tspan font-family="monospace" fill="#38bdf8">ip addr</tspan> or <tspan font-family="monospace" fill="#38bdf8">ifconfig</tspan></text>

    <text x="15" y="245" font-size="10" font-weight="bold" fill="#a5b4fc">&#8226; Key Parameters to Verify:</text>
    <text x="15" y="265" font-size="9" fill="#cbd5e1">&#8226; Valid Private IP (e.g., 192.168.x.x)</text>
    <text x="15" y="283" font-size="9" fill="#cbd5e1">&#8226; Non-APIPA address (not 169.254.x.x)</text>
    <text x="15" y="301" font-size="9" fill="#cbd5e1">&#8226; Accessible Default Gateway IP</text>

    <rect x="15" y="325" width="235" height="45" rx="6" fill="#1e293b"/>
    <text x="25" y="345" font-size="9" fill="#34d399">&#10003; Node is ready for network communication</text>
  </g>
</svg>
""")

SVG_TROUBLESHOOTING_FLOWCHART = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Structured 4-Step Network Diagnostic Sequence Flowchart</text>
  <text x="480" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Systematic troubleshooting algorithm to isolate OS, local wire, router gateway, ISP, or DNS faults</text>

  <!-- Step 1 Box -->
  <g transform="translate(45, 90)">
    <rect width="190" height="110" rx="8" fill="#0f172a" stroke="#0ea5e9" stroke-width="2"/>
    <rect width="190" height="24" rx="6" fill="#0284c7"/>
    <text x="95" y="17" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Step 1: Ping Localhost</text>
    <text x="95" y="48" font-family="monospace" font-size="10.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">ping 127.0.0.1</text>
    <text x="95" y="68" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Tests internal OS</text>
    <text x="95" y="82" font-size="8.5" fill="#cbd5e1" text-anchor="middle">TCP/IP protocol stack</text>
    <text x="95" y="98" font-size="8" fill="#94a3b8" text-anchor="middle">(No wire transmission)</text>
  </g>

  <!-- Step 1 Failure Branch -->
  <g transform="translate(140, 200)">
    <line x1="0" y1="0" x2="0" y2="40" stroke="#ef4444" stroke-width="2"/>
    <polygon points="-4,40 4,40 0,47" fill="#ef4444"/>
    <text x="8" y="25" font-size="9" font-weight="bold" fill="#f87171">FAILS</text>
    <rect x="-80" y="47" width="160" height="55" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="0" y="66" font-size="9" font-weight="bold" fill="#f87171" text-anchor="middle">Fault: OS Network Stack</text>
    <text x="0" y="82" font-size="8" fill="#cbd5e1" text-anchor="middle">Reinstall NIC driver or</text>
    <text x="0" y="94" font-size="8" fill="#cbd5e1" text-anchor="middle">reset OS TCP/IP stack</text>
  </g>

  <!-- Arrow Step 1 -> Step 2 -->
  <g transform="translate(235, 145)">
    <line x1="0" y1="0" x2="35" y2="0" stroke="#10b981" stroke-width="2.5"/>
    <polygon points="35,-4 42,0 35,4" fill="#10b981"/>
    <text x="18" y="-7" font-size="8.5" font-weight="bold" fill="#34d399" text-anchor="middle">PASS</text>
  </g>

  <!-- Step 2 Box -->
  <g transform="translate(277, 90)">
    <rect width="190" height="110" rx="8" fill="#0f172a" stroke="#0ea5e9" stroke-width="2"/>
    <rect width="190" height="24" rx="6" fill="#0284c7"/>
    <text x="95" y="17" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Step 2: Ping Gateway</text>
    <text x="95" y="48" font-family="monospace" font-size="10.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">ping 192.168.1.1</text>
    <text x="95" y="68" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Tests physical cable, local</text>
    <text x="95" y="82" font-size="8.5" fill="#cbd5e1" text-anchor="middle">switch &amp; router interface</text>
    <text x="95" y="98" font-size="8" fill="#94a3b8" text-anchor="middle">(Local LAN hop)</text>
  </g>

  <!-- Step 2 Failure Branch -->
  <g transform="translate(372, 200)">
    <line x1="0" y1="0" x2="0" y2="40" stroke="#ef4444" stroke-width="2"/>
    <polygon points="-4,40 4,40 0,47" fill="#ef4444"/>
    <text x="8" y="25" font-size="9" font-weight="bold" fill="#f87171">FAILS</text>
    <rect x="-80" y="47" width="160" height="55" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="0" y="66" font-size="9" font-weight="bold" fill="#f87171" text-anchor="middle">Fault: Local LAN / Wire</text>
    <text x="0" y="82" font-size="8" fill="#cbd5e1" text-anchor="middle">Inspect RJ-45 cable, switch</text>
    <text x="0" y="94" font-size="8" fill="#cbd5e1" text-anchor="middle">power, or subnet IP mask</text>
  </g>

  <!-- Arrow Step 2 -> Step 3 -->
  <g transform="translate(467, 145)">
    <line x1="0" y1="0" x2="35" y2="0" stroke="#10b981" stroke-width="2.5"/>
    <polygon points="35,-4 42,0 35,4" fill="#10b981"/>
    <text x="18" y="-7" font-size="8.5" font-weight="bold" fill="#34d399" text-anchor="middle">PASS</text>
  </g>

  <!-- Step 3 Box -->
  <g transform="translate(509, 90)">
    <rect width="190" height="110" rx="8" fill="#0f172a" stroke="#0ea5e9" stroke-width="2"/>
    <rect width="190" height="24" rx="6" fill="#0284c7"/>
    <text x="95" y="17" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Step 3: Ping External IP</text>
    <text x="95" y="48" font-family="monospace" font-size="10.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">ping 8.8.8.8</text>
    <text x="95" y="68" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Tests router WAN port,</text>
    <text x="95" y="82" font-size="8.5" fill="#cbd5e1" text-anchor="middle">modem uplink &amp; ISP routing</text>
    <text x="95" y="98" font-size="8" fill="#94a3b8" text-anchor="middle">(Global Internet path)</text>
  </g>

  <!-- Step 3 Failure Branch -->
  <g transform="translate(604, 200)">
    <line x1="0" y1="0" x2="0" y2="40" stroke="#ef4444" stroke-width="2"/>
    <polygon points="-4,40 4,40 0,47" fill="#ef4444"/>
    <text x="8" y="25" font-size="9" font-weight="bold" fill="#f87171">FAILS</text>
    <rect x="-80" y="47" width="160" height="55" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="0" y="66" font-size="9" font-weight="bold" fill="#f87171" text-anchor="middle">Fault: ISP / WAN Uplink</text>
    <text x="0" y="82" font-size="8" fill="#cbd5e1" text-anchor="middle">Modem offline, fiber cut,</text>
    <text x="0" y="94" font-size="8" fill="#cbd5e1" text-anchor="middle">or ISP subscription outage</text>
  </g>

  <!-- Arrow Step 3 -> Step 4 -->
  <g transform="translate(699, 145)">
    <line x1="0" y1="0" x2="35" y2="0" stroke="#10b981" stroke-width="2.5"/>
    <polygon points="35,-4 42,0 35,4" fill="#10b981"/>
    <text x="18" y="-7" font-size="8.5" font-weight="bold" fill="#34d399" text-anchor="middle">PASS</text>
  </g>

  <!-- Step 4 Box -->
  <g transform="translate(741, 90)">
    <rect width="180" height="110" rx="8" fill="#0f172a" stroke="#0ea5e9" stroke-width="2"/>
    <rect width="180" height="24" rx="6" fill="#0284c7"/>
    <text x="90" y="17" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Step 4: Ping Domain</text>
    <text x="90" y="48" font-family="monospace" font-size="10.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">ping google.com</text>
    <text x="90" y="68" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Tests DNS Name Resolution</text>
    <text x="90" y="82" font-size="8.5" fill="#cbd5e1" text-anchor="middle">(Hostname to IP mapping)</text>
    <text x="90" y="98" font-size="8" fill="#94a3b8" text-anchor="middle">(google.com -&gt; IP)</text>
  </g>

  <!-- Step 4 Failure Branch -->
  <g transform="translate(831, 200)">
    <line x1="0" y1="0" x2="0" y2="40" stroke="#ef4444" stroke-width="2"/>
    <polygon points="-4,40 4,40 0,47" fill="#ef4444"/>
    <text x="8" y="25" font-size="9" font-weight="bold" fill="#f87171">FAILS</text>
    <rect x="-80" y="47" width="160" height="55" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="0" y="66" font-size="9" font-weight="bold" fill="#f87171" text-anchor="middle">Fault: DNS Configuration</text>
    <text x="0" y="82" font-size="8" fill="#cbd5e1" text-anchor="middle">Connected to internet, but</text>
    <text x="0" y="94" font-size="8" fill="#cbd5e1" text-anchor="middle">DNS server IP is wrong/down</text>
  </g>

  <!-- Bottom Success Box -->
  <g transform="translate(45, 395)">
    <rect width="875" height="90" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <text x="25" y="28" font-size="12" font-weight="bold" fill="#34d399">&#10003; Diagnostic Rule Summary:</text>
    <text x="25" y="50" font-size="9.5" fill="#cbd5e1">1. If you can ping <tspan font-family="monospace" fill="#38bdf8">8.8.8.8</tspan> but CANNOT ping <tspan font-family="monospace" fill="#38bdf8">google.com</tspan>, your physical and IP routing are 100% perfect; simply update your DNS settings.</text>
    <text x="25" y="70" font-size="9.5" fill="#cbd5e1">2. If you CANNOT ping <tspan font-family="monospace" fill="#38bdf8">192.168.1.1</tspan>, do NOT call your ISP—the fault is physically inside your local room (cable, switch, or NIC).</text>
  </g>
</svg>
""")

SVG_MAASAI_MARA_ECO_LODGE_TOPOLOGY = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Real-World Case Study: Maasai Mara Safari Eco-Lodge Network Architecture</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Hybrid Remote Topology: Solar Power, Starlink Satellite WAN Uplink, Core Switch, and 200m Mesh WLAN</text>

  <!-- Left: Main Reception Office (Solar & Wired LAN) -->
  <g transform="translate(45, 95)">
    <rect width="360" height="385" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="360" height="28" rx="8" fill="#0284c7"/>
    <text x="180" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Main Reception Office (Wired LAN)</text>

    <!-- Solar Inverter / UPS -->
    <rect x="20" y="45" width="150" height="50" rx="6" fill="#1e293b" stroke="#f59e0b"/>
    <text x="95" y="67" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">Solar Array &amp; UPS</text>
    <text x="95" y="83" font-size="8" fill="#cbd5e1" text-anchor="middle">Clean 24/7 Power</text>

    <!-- Satellite Dish Modem -->
    <rect x="190" y="45" width="150" height="50" rx="6" fill="#1e293b" stroke="#818cf8"/>
    <text x="265" y="67" font-size="10" font-weight="bold" fill="#a5b4fc" text-anchor="middle">Satellite Dish (DCE)</text>
    <text x="265" y="83" font-size="8" fill="#cbd5e1" text-anchor="middle">Low-Earth Orbit WAN</text>

    <!-- Core Gateway Router -->
    <rect x="75" y="115" width="210" height="55" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="180" y="137" font-size="10.5" font-weight="bold" fill="#34d399" text-anchor="middle">Core Gateway Router</text>
    <text x="180" y="155" font-size="8.5" fill="#cbd5e1" text-anchor="middle">DHCP Server + Firewall + Bandwidth Limiter</text>

    <!-- Core LAN Switch -->
    <rect x="75" y="190" width="210" height="50" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="180" y="212" font-size="10.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">24-Port Gigabit PoE Switch</text>
    <text x="180" y="228" font-size="8.5" fill="#cbd5e1" text-anchor="middle">PoE feeds remote Access Points</text>

    <!-- DTE Clients in Office -->
    <rect x="20" y="260" width="150" height="105" rx="6" fill="#1e293b"/>
    <text x="95" y="280" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">5x Admin DTE PCs</text>
    <text x="95" y="300" font-size="8" fill="#cbd5e1" text-anchor="middle">&#8226; Booking Management</text>
    <text x="95" y="318" font-size="8" fill="#cbd5e1" text-anchor="middle">&#8226; Guest Registration</text>
    <text x="95" y="336" font-size="8" fill="#cbd5e1" text-anchor="middle">&#8226; Safari Scheduling</text>

    <rect x="190" y="260" width="150" height="105" rx="6" fill="#1e293b"/>
    <text x="265" y="280" font-size="9.5" font-weight="bold" fill="#34d399" text-anchor="middle">2x Network Printers</text>
    <text x="265" y="300" font-size="8" fill="#cbd5e1" text-anchor="middle">&#8226; Shared Resource</text>
    <text x="265" y="318" font-size="8" fill="#cbd5e1" text-anchor="middle">&#8226; Invoicing &amp; Receipts</text>
    <text x="265" y="336" font-size="8" fill="#cbd5e1" text-anchor="middle">&#8226; Read-Only Access Control</text>
  </g>

  <!-- Right: 12 Guest Cabins across 200m Wilderness -->
  <g transform="translate(435, 95)">
    <rect width="480" height="385" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="480" height="28" rx="8" fill="#059669"/>
    <text x="240" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">12 Guest Cabins Distribution (200m Radius WLAN)</text>

    <!-- Distribution Backbone -->
    <g transform="translate(20, 45)">
      <rect width="440" height="65" rx="8" fill="#1e293b" stroke="#34d399"/>
      <text x="220" y="24" font-size="10.5" font-weight="bold" fill="#34d399" text-anchor="middle">Outdoor Ruggedized High-Gain Access Points (PoE-Powered)</text>
      <text x="220" y="44" font-size="9" fill="#cbd5e1" text-anchor="middle">Directional beamforming radio transmitters broadcasting Dual-Band (2.4 GHz + 5 GHz Wi-Fi 6)</text>
    </g>

    <!-- Cabin Cluster 1 -->
    <g transform="translate(20, 125)">
      <rect width="210" height="110" rx="8" fill="#1e293b" stroke="#64748b"/>
      <text x="105" y="24" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">North Sector (Cabins 1–6)</text>
      <text x="105" y="46" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; WAP 1 (PoE via shielded Cat6)</text>
      <text x="105" y="64" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; Isolated "Guest Wi-Fi" VLAN</text>
      <text x="105" y="82" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; Client isolation enabled</text>
      <text x="105" y="100" font-size="8" fill="#94a3b8" text-anchor="middle">(Prevents guest-to-guest snooping)</text>
    </g>

    <!-- Cabin Cluster 2 -->
    <g transform="translate(250, 125)">
      <rect width="210" height="110" rx="8" fill="#1e293b" stroke="#64748b"/>
      <text x="105" y="24" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">South Sector (Cabins 7–12)</text>
      <text x="105" y="46" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; WAP 2 (PoE via shielded Cat6)</text>
      <text x="105" y="64" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; Roaming mesh handover</text>
      <text x="105" y="82" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; 5 Mbps bandwidth limit / device</text>
      <text x="105" y="100" font-size="8" fill="#94a3b8" text-anchor="middle">(Prevents satellite link choking)</text>
    </g>

    <!-- Architectural Key Solutions Table -->
    <g transform="translate(20, 250)">
      <rect width="440" height="120" rx="8" fill="#0f172a" stroke="#334155"/>
      <text x="15" y="22" font-size="10" font-weight="bold" fill="#38bdf8">Engineering Solutions for Remote Maasai Mara Challenges:</text>
      <text x="15" y="42" font-size="8.5" fill="#cbd5e1"><tspan font-weight="bold" fill="#fbbf24">1. No Terrestrial Fiber:</tspan> High-throughput Satellite WAN uplink (Starlink / O3b).</text>
      <text x="15" y="62" font-size="8.5" fill="#cbd5e1"><tspan font-weight="bold" fill="#fbbf24">2. Unstable Grid:</tspan> Solar PV array + Lithium battery bank + Pure Sine Wave Inverter.</text>
      <text x="15" y="82" font-size="8.5" fill="#cbd5e1"><tspan font-weight="bold" fill="#fbbf24">3. Security:</tspan> VLAN segregation (Office Admin VLAN vs. Isolated Guest Wi-Fi).</text>
      <text x="15" y="102" font-size="8.5" fill="#cbd5e1"><tspan font-weight="bold" fill="#fbbf24">4. Resource Sharing:</tspan> Shared network billing printers restricted via password ACLs.</text>
    </g>
  </g>
</svg>
""")

SVG_TOPOLOGIES_STAR_BUS_RING_MESH = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Physical &amp; Logical Network Topologies</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Comparative Architecture: Star, Bus, Ring, and Full Mesh Topologies with Fault Tolerance Analysis</text>

  <!-- 1. Star Topology -->
  <g transform="translate(45, 90)">
    <rect width="205" height="390" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="205" height="28" rx="6" fill="#0284c7"/>
    <text x="102" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1. STAR TOPOLOGY</text>

    <!-- Star Graphic -->
    <g transform="translate(10, 40)">
      <rect width="185" height="130" rx="6" fill="#1e293b"/>
      <!-- Central Switch -->
      <circle cx="92" cy="65" r="16" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="92" y="69" font-size="8" font-weight="bold" fill="#fff" text-anchor="middle">Switch</text>

      <!-- Spokes -->
      <line x1="92" y1="49" x2="92" y2="20" stroke="#38bdf8" stroke-width="2"/>
      <rect x="77" y="10" width="30" height="18" rx="3" fill="#0f172a" stroke="#38bdf8"/><text x="92" y="22" font-size="7" fill="#fff" text-anchor="middle">PC 1</text>

      <line x1="108" y1="65" x2="155" y2="65" stroke="#38bdf8" stroke-width="2"/>
      <rect x="145" y="56" width="30" height="18" rx="3" fill="#0f172a" stroke="#38bdf8"/><text x="160" y="68" font-size="7" fill="#fff" text-anchor="middle">PC 2</text>

      <line x1="92" y1="81" x2="92" y2="110" stroke="#38bdf8" stroke-width="2"/>
      <rect x="77" y="102" width="30" height="18" rx="3" fill="#0f172a" stroke="#38bdf8"/><text x="92" y="114" font-size="7" fill="#fff" text-anchor="middle">PC 3</text>

      <line x1="76" y1="65" x2="30" y2="65" stroke="#38bdf8" stroke-width="2"/>
      <rect x="15" y="56" width="30" height="18" rx="3" fill="#0f172a" stroke="#38bdf8"/><text x="30" y="68" font-size="7" fill="#fff" text-anchor="middle">PC 4</text>
    </g>

    <g transform="translate(10, 185)">
      <text x="0" y="15" font-size="9.5" font-weight="bold" fill="#38bdf8">&#10003; Strengths:</text>
      <text x="0" y="30" font-size="8.5" fill="#cbd5e1">&#8226; Single cable break does</text>
      <text x="0" y="42" font-size="8.5" fill="#cbd5e1">  not take down network.</text>
      <text x="0" y="56" font-size="8.5" fill="#cbd5e1">&#8226; Easy to add new hosts.</text>
      <text x="0" y="78" font-size="9.5" font-weight="bold" fill="#f87171">&#9888; Vulnerability:</text>
      <text x="0" y="93" font-size="8.5" fill="#cbd5e1">&#8226; Central switch is a single</text>
      <text x="0" y="105" font-size="8.5" fill="#cbd5e1">  point of failure (SPoF).</text>
      <text x="0" y="125" font-size="8" fill="#94a3b8">Standard in 99% modern LANs</text>
    </g>
  </g>

  <!-- 2. Bus Topology -->
  <g transform="translate(265, 90)">
    <rect width="205" height="390" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="205" height="28" rx="6" fill="#d97706"/>
    <text x="102" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2. BUS TOPOLOGY</text>

    <!-- Bus Graphic -->
    <g transform="translate(10, 40)">
      <rect width="185" height="130" rx="6" fill="#1e293b"/>
      <!-- Main Trunk -->
      <line x1="20" y1="65" x2="165" y2="65" stroke="#fbbf24" stroke-width="4"/>
      <!-- Terminators -->
      <rect x="15" y="55" width="8" height="20" fill="#ef4444"/><text x="19" y="85" font-size="6" fill="#fca5a5" text-anchor="middle">Term</text>
      <rect x="162" y="55" width="8" height="20" fill="#ef4444"/><text x="166" y="85" font-size="6" fill="#fca5a5" text-anchor="middle">Term</text>
      
      <!-- Drop Lines -->
      <line x1="50" y1="65" x2="50" y2="25" stroke="#fbbf24" stroke-width="2"/>
      <rect x="35" y="10" width="30" height="16" rx="2" fill="#0f172a" stroke="#fbbf24"/><text x="50" y="22" font-size="7" fill="#fff" text-anchor="middle">PC 1</text>

      <line x1="95" y1="65" x2="95" y2="105" stroke="#fbbf24" stroke-width="2"/>
      <rect x="80" y="102" width="30" height="16" rx="2" fill="#0f172a" stroke="#fbbf24"/><text x="95" y="114" font-size="7" fill="#fff" text-anchor="middle">PC 2</text>

      <line x1="140" y1="65" x2="140" y2="25" stroke="#fbbf24" stroke-width="2"/>
      <rect x="125" y="10" width="30" height="16" rx="2" fill="#0f172a" stroke="#fbbf24"/><text x="140" y="22" font-size="7" fill="#fff" text-anchor="middle">PC 3</text>
    </g>

    <g transform="translate(10, 185)">
      <text x="0" y="15" font-size="9.5" font-weight="bold" fill="#fbbf24">&#10003; Strengths:</text>
      <text x="0" y="30" font-size="8.5" fill="#cbd5e1">&#8226; Minimal cabling required.</text>
      <text x="0" y="42" font-size="8.5" fill="#cbd5e1">&#8226; Cheap for small setups.</text>
      <text x="0" y="78" font-size="9.5" font-weight="bold" fill="#f87171">&#9888; Vulnerability:</text>
      <text x="0" y="93" font-size="8.5" fill="#cbd5e1">&#8226; Main cable break halts</text>
      <text x="0" y="105" font-size="8.5" fill="#cbd5e1">  entire network (reflection).</text>
      <text x="0" y="125" font-size="8" fill="#94a3b8">Legacy 10BASE2 Coaxial</text>
    </g>
  </g>

  <!-- 3. Ring Topology -->
  <g transform="translate(485, 90)">
    <rect width="205" height="390" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="205" height="28" rx="6" fill="#7e22ce"/>
    <text x="102" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">3. RING TOPOLOGY</text>

    <!-- Ring Graphic -->
    <g transform="translate(10, 40)">
      <rect width="185" height="130" rx="6" fill="#1e293b"/>
      <circle cx="92" cy="65" r="42" fill="none" stroke="#c084fc" stroke-width="2.5" stroke-dasharray="4"/>
      
      <rect x="77" y="12" width="30" height="18" rx="3" fill="#7e22ce" stroke="#c084fc"/><text x="92" y="24" font-size="7" fill="#fff" text-anchor="middle">Node A</text>
      <rect x="135" y="56" width="30" height="18" rx="3" fill="#7e22ce" stroke="#c084fc"/><text x="150" y="68" font-size="7" fill="#fff" text-anchor="middle">Node B</text>
      <rect x="77" y="100" width="30" height="18" rx="3" fill="#7e22ce" stroke="#c084fc"/><text x="92" y="112" font-size="7" fill="#fff" text-anchor="middle">Node C</text>
      <rect x="18" y="56" width="30" height="18" rx="3" fill="#7e22ce" stroke="#c084fc"/><text x="33" y="68" font-size="7" fill="#fff" text-anchor="middle">Node D</text>
    </g>

    <g transform="translate(10, 185)">
      <text x="0" y="15" font-size="9.5" font-weight="bold" fill="#c084fc">&#10003; Strengths:</text>
      <text x="0" y="30" font-size="8.5" fill="#cbd5e1">&#8226; Token passing prevents</text>
      <text x="0" y="42" font-size="8.5" fill="#cbd5e1">  packet collisions.</text>
      <text x="0" y="56" font-size="8.5" fill="#cbd5e1">&#8226; Deterministic throughput.</text>
      <text x="0" y="78" font-size="9.5" font-weight="bold" fill="#f87171">&#9888; Vulnerability:</text>
      <text x="0" y="93" font-size="8.5" fill="#cbd5e1">&#8226; One broken node breaks</text>
      <text x="0" y="105" font-size="8.5" fill="#cbd5e1">  ring (solved by Dual FDDI).</text>
      <text x="0" y="125" font-size="8" fill="#94a3b8">Token Ring / Metro FDDI</text>
    </g>
  </g>

  <!-- 4. Mesh Topology -->
  <g transform="translate(705, 90)">
    <rect width="210" height="390" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="210" height="28" rx="6" fill="#059669"/>
    <text x="105" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">4. FULL MESH TOPOLOGY</text>

    <!-- Mesh Graphic -->
    <g transform="translate(10, 40)">
      <rect width="190" height="130" rx="6" fill="#1e293b"/>
      <!-- Lines interconnecting all 4 nodes -->
      <line x1="45" y1="30" x2="145" y2="30" stroke="#34d399" stroke-width="1.5"/>
      <line x1="45" y1="100" x2="145" y2="100" stroke="#34d399" stroke-width="1.5"/>
      <line x1="45" y1="30" x2="45" y2="100" stroke="#34d399" stroke-width="1.5"/>
      <line x1="145" y1="30" x2="145" y2="100" stroke="#34d399" stroke-width="1.5"/>
      <line x1="45" y1="30" x2="145" y2="100" stroke="#34d399" stroke-width="1.5"/>
      <line x1="45" y1="100" x2="145" y2="30" stroke="#34d399" stroke-width="1.5"/>

      <circle cx="45" cy="30" r="12" fill="#059669" stroke="#34d399"/><text x="45" y="34" font-size="7" fill="#fff" text-anchor="middle">N1</text>
      <circle cx="145" cy="30" r="12" fill="#059669" stroke="#34d399"/><text x="145" y="34" font-size="7" fill="#fff" text-anchor="middle">N2</text>
      <circle cx="145" cy="100" r="12" fill="#059669" stroke="#34d399"/><text x="145" y="104" font-size="7" fill="#fff" text-anchor="middle">N3</text>
      <circle cx="45" cy="100" r="12" fill="#059669" stroke="#34d399"/><text x="45" y="104" font-size="7" fill="#fff" text-anchor="middle">N4</text>
    </g>

    <g transform="translate(10, 185)">
      <text x="0" y="15" font-size="9.5" font-weight="bold" fill="#34d399">&#10003; Strengths:</text>
      <text x="0" y="30" font-size="8.5" fill="#cbd5e1">&#8226; Maximum fault tolerance</text>
      <text x="0" y="42" font-size="8.5" fill="#cbd5e1">  (Multiple alternate routes).</text>
      <text x="0" y="56" font-size="8.5" fill="#cbd5e1">&#8226; Formula: N(N-1)/2 links.</text>
      <text x="0" y="78" font-size="9.5" font-weight="bold" fill="#f87171">&#9888; Vulnerability:</text>
      <text x="0" y="93" font-size="8.5" fill="#cbd5e1">&#8226; Extremely expensive</text>
      <text x="0" y="105" font-size="8.5" fill="#cbd5e1">  cable &amp; port overhead.</text>
      <text x="0" y="125" font-size="8" fill="#94a3b8">Internet WAN Core &amp; Military</text>
    </g>
  </g>
</svg>
""")

SVG_NETWORK_SECURITY_DEFENSE_IN_DEPTH = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Enterprise Network Security: Defense-in-Depth Model</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Layered Security Controls across Perimeter, Internal Network, Host Systems, and Cryptographic Data Layers</text>

  <!-- Layer 1: Perimeter Defense -->
  <g transform="translate(45, 95)">
    <rect width="205" height="385" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="205" height="28" rx="6" fill="#dc2626"/>
    <text x="102" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. PERIMETER LAYER</text>

    <g transform="translate(12, 45)">
      <rect width="180" height="85" rx="6" fill="#1e293b" stroke="#f87171"/>
      <text x="90" y="20" font-size="10" font-weight="bold" fill="#fca5a5" text-anchor="middle">Next-Gen Firewall (NGFW)</text>
      <text x="10" y="40" font-size="8.5" fill="#cbd5e1">&#8226; Stateful Packet Inspection</text>
      <text x="10" y="56" font-size="8.5" fill="#cbd5e1">&#8226; Edge NAT IP Masquerading</text>
      <text x="10" y="72" font-size="8.5" fill="#cbd5e1">&#8226; DDoS Mitigation Scrubbing</text>
    </g>

    <g transform="translate(12, 145)">
      <text x="0" y="15" font-size="9.5" font-weight="bold" fill="#fca5a5">&#128737; Boundary Rules:</text>
      <text x="0" y="32" font-size="8.5" fill="#cbd5e1">Default Deny-All inbound traffic policy.</text>
      <text x="0" y="55" font-size="9.5" font-weight="bold" fill="#fca5a5">&#128274; DMZ Demilitarized Zone:</text>
      <text x="0" y="72" font-size="8.5" fill="#cbd5e1">Isolates public web servers from internal database core.</text>
    </g>
  </g>

  <!-- Layer 2: Internal Network Layer -->
  <g transform="translate(265, 95)">
    <rect width="205" height="385" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="205" height="28" rx="6" fill="#d97706"/>
    <text x="102" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. NETWORK SEGMENT</text>

    <g transform="translate(12, 45)">
      <rect width="180" height="85" rx="6" fill="#1e293b" stroke="#fbbf24"/>
      <text x="90" y="20" font-size="10" font-weight="bold" fill="#fde68a" text-anchor="middle">VLANs &amp; Access Control</text>
      <text x="10" y="40" font-size="8.5" fill="#cbd5e1">&#8226; 802.1Q Virtual LANs</text>
      <text x="10" y="56" font-size="8.5" fill="#cbd5e1">&#8226; Switch Port Security (MAC)</text>
      <text x="10" y="72" font-size="8.5" fill="#cbd5e1">&#8226; IDS/IPS Threat Sensors</text>
    </g>

    <g transform="translate(12, 145)">
      <text x="0" y="15" font-size="9.5" font-weight="bold" fill="#fde68a">&#128161; Micro-Segmentation:</text>
      <text x="0" y="32" font-size="8.5" fill="#cbd5e1">Finance, HR, and Guest Wi-Fi isolated into separate broadcast domains.</text>
      <text x="0" y="65" font-size="8.5" fill="#cbd5e1">Prevents lateral malware movement across internal PCs.</text>
    </g>
  </g>

  <!-- Layer 3: Host & NOS Layer -->
  <g transform="translate(485, 95)">
    <rect width="205" height="385" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="205" height="28" rx="6" fill="#0284c7"/>
    <text x="102" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. HOST &amp; NOS LAYER</text>

    <g transform="translate(12, 45)">
      <rect width="180" height="85" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="90" y="20" font-size="10" font-weight="bold" fill="#7dd3fc" text-anchor="middle">Active Directory &amp; RBAC</text>
      <text x="10" y="40" font-size="8.5" fill="#cbd5e1">&#8226; Centralized LDAP / Kerberos</text>
      <text x="10" y="56" font-size="8.5" fill="#cbd5e1">&#8226; Role-Based Access Control</text>
      <text x="10" y="72" font-size="8.5" fill="#cbd5e1">&#8226; Multi-Factor Auth (MFA)</text>
    </g>

    <g transform="translate(12, 145)">
      <text x="0" y="15" font-size="9.5" font-weight="bold" fill="#7dd3fc">&#128271; Least Privilege Rule:</text>
      <text x="0" y="32" font-size="8.5" fill="#cbd5e1">Users only receive minimum permissions needed for job duties.</text>
      <text x="0" y="65" font-size="8.5" fill="#cbd5e1">Endpoint Antivirus &amp; Patch Management agents active.</text>
    </g>
  </g>

  <!-- Layer 4: Data & Cryptography Layer -->
  <g transform="translate(705, 95)">
    <rect width="210" height="385" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="210" height="28" rx="6" fill="#059669"/>
    <text x="105" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4. DATA &amp; CRYPTO LAYER</text>

    <g transform="translate(12, 45)">
      <rect width="185" height="85" rx="6" fill="#1e293b" stroke="#34d399"/>
      <text x="92" y="20" font-size="10" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Encryption &amp; Backups</text>
      <text x="10" y="40" font-size="8.5" fill="#cbd5e1">&#8226; TLS 1.3 Data in Transit</text>
      <text x="10" y="56" font-size="8.5" fill="#cbd5e1">&#8226; AES-256 Data at Rest</text>
      <text x="10" y="72" font-size="8.5" fill="#cbd5e1">&#8226; 3-2-1 Immutable Backups</text>
    </g>

    <g transform="translate(12, 145)">
      <text x="0" y="15" font-size="9.5" font-weight="bold" fill="#a7f3d0">&#128272; Cryptographic Protection:</text>
      <text x="0" y="32" font-size="8.5" fill="#cbd5e1">Even if hard drive or wire packets are intercepted, payload is unreadable.</text>
      <text x="0" y="65" font-size="8.5" fill="#cbd5e1">Air-gapped offline cloud backups defend against ransomware.</text>
    </g>
  </g>
</svg>
""")

# =====================================================================
# CURRICULUM DEFINITIONS FOR GRADE 10 TOPIC 10
# =====================================================================

def build_topic10_curriculum():
    return [
        # =====================================================================
        # LEARNING UNIT 1: Types and Geographical Scope of Computer Networks
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Types and Geographical Scope of Computer Networks",
            "unit_description": "Geographical classifications of computer networks: Personal Area Networks (PAN), Local Area Networks (LAN), Wireless LANs (WLAN), Metropolitan Area Networks (MAN), and Wide Area Networks (WAN).",
            "lesson_title": "Types and Geographical Scope of Computer Networks",
            "pages": [
                # Page 1: Introduction & "Social Circles" Analogy
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Classifying Networks by Geographical Reach",
                        "content": {
                            "goal": "Define a computer network and master the classification hierarchy of networks according to geographical scope: PAN, LAN, WLAN, MAN, and WAN."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Introduction & The 'Social Circles' Analogy",
                        "content": {
                            "markdown": """### **The 'Social Circles' Analogy**
Imagine your personal circles of human communication:
- **Your Immediate Physical Bubble**: You connect your smartphone directly to your wireless headphones or sync your smartwatch with your wrist. This is an intimate, short-range bubble that moves everywhere you go.
- **Your Home or Classroom Circle**: Everyone inside the room can share the same printer, play local games together, or chat with one another over a local system.
- **Your Neighborhood or City Circle**: Municipal systems, local county offices, or university campuses that interconnect multiple school buildings scattered across an entire town.
- **Your Global Circle**: You can instantly send an email to a cousin in another country, stream a video hosted on a server in North America, or access websites across the globe.

In computer networking, digital networks are classified into distinct categories based on this exact sliding scale of **geographical scope**.

### **Core Definitions**
- **Computer Network**: A collection of interconnected digital devices (nodes) that communicate with one another using standardized protocols to share resources, transfer data, and facilitate services.
- **Personal Area Network (PAN)**: A small network organized around an individual person, typically within a range of a few meters (under 10 meters), to connect personal peripheral devices.
- **Local Area Network (LAN)**: A network that interconnects computers and devices within a highly limited geographical area, such as a single office, home, or school computer laboratory.
- **Wireless Local Area Network (WLAN)**: A localized network (LAN) that utilizes high-frequency radio waves (such as Wi-Fi) rather than physical cables to connect devices over distances of up to 100 meters.
- **Metropolitan Area Network (MAN)**: A high-speed network that covers a larger geographical area than a LAN—such as an entire city, town, or university campus (10 to 50 km)—and often interconnects multiple LANs.
- **Wide Area Network (WAN)**: A massive network that spans a large geographical distance, crossing cities, national boundaries, or entire continents. The **Internet** is the world's largest and most famous example of a WAN."""
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Concentric Scopes of Computer Networks",
                        "content": {
                            "svg_content": SVG_CONCENTRIC_NETWORK_SCOPES,
                            "caption": "Figure 10.1: Concentric diagram illustrating the expanding geographical boundaries of PAN, LAN/WLAN, MAN, and WAN with their respective transmission media and real-world applications."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "School Computer Laboratory Local Area Network (LAN)",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Computer_lab_LAN.jpg/800px-Computer_lab_LAN.jpg",
                            "caption": "Figure 10.2: Modern computer laboratory LAN setup showing desktop workstations interconnected via structured twisted pair Ethernet cables.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Scope-Based Network Classification",
                        "content": {
                            "text": "Networks are classified primarily by their geographical coverage: PAN (<10m, Bluetooth), LAN/WLAN (<1km/100m, Ethernet/Wi-Fi), MAN (10-50km, City Fiber), and WAN (Global, Satellites and Subsea Cables)."
                        }
                    }
                ],

                # Page 2: Comparative Matrix of Geographical Scopes
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Comparative Metrics Across Network Types",
                        "content": {
                            "goal": "Evaluate the technical trade-offs between PAN, LAN, WLAN, MAN, and WAN in terms of transmission media, data transfer speeds, ownership, and maintenance costs."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Comparative Matrix: Geographical Network Scopes",
                        "content": {
                            "markdown": """### **Geographical Network Scope Matrix**

| Network Type | Geographical Range | Primary Transmission Media | Typical Ownership | Real-World Example |
| :--- | :--- | :--- | :--- | :--- |
| **PAN** | Within 10 meters | Bluetooth, USB cables, NFC, Infrared | Individual person | Syncing a smartphone with wireless earbuds or a car dashboard. |
| **LAN** | Within 1 kilometer (e.g., single school building) | Copper UTP (Ethernet), local fiber-optics | Single organization (private school, hospital, bank branch) | A school computer laboratory where 40 PCs share a central laser printer. |
| **WLAN** | Within 100 meters | High-frequency radio waves (Wi-Fi 802.11ax/ac) | Single organization or homeowner | Students connecting their laptops and tablets to the school's "Student Wi-Fi" SSID. |
| **MAN** | 10 to 50 kilometers (city scale) | High-speed singlemode fiber backbones, microwave links | Telecom consortiums, municipal city governments, cable operators | A municipal traffic monitoring camera grid across Nairobi or Mombasa. |
| **WAN** | Country, continental, or global scale | Satellites, subsea fiber-optic cables, leased telecom circuits | Distributed public and private telecom giants | The global Internet, connecting school LANs across Kenya to worldwide cloud servers. |

### **Key Technical Trade-offs**
1. **Bandwidth vs. Cost**: LANs offer extremely high local bandwidth (1 Gbps to 10 Gbps) at low installation cost, whereas WAN links across continents require massive infrastructure investment and recurring telecom subscription fees.
2. **Error Rates & Propagation Delay**: PANs and LANs experience near-zero latency (<1 ms) and extremely low error rates. WANs suffer from higher propagation delay (e.g., 500 ms round-trip for geostationary satellite hops) due to physical distance."""
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Network Topologies: Star, Bus, Ring, and Mesh",
                        "content": {
                            "svg_content": SVG_TOPOLOGIES_STAR_BUS_RING_MESH,
                            "caption": "Figure 10.3: Comparative topologies: Star (central switch), Bus (trunk with terminators), Ring (token passing), and Full Mesh (N(N-1)/2 links)."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Global Subsea Fiber-Optic Cable Infrastructure (WAN)",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Wide_Area_Network_concept.svg/800px-Wide_Area_Network_concept.svg.png",
                            "caption": "Figure 10.4: Conceptual representation of a Wide Area Network (WAN) interconnecting regional LANs and MANs across national boundaries via high-capacity undersea cable backbones.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Computer Networks: PAN, LAN, MAN, and WAN Explained",
                        "content": {
                            "youtube_id": "JH4F_Z_xWl8",
                            "url": "https://www.youtube.com/watch?v=JH4F_Z_xWl8",
                            "description": "A visual breakdown of the different network classifications, exploring how geographical scale influences hardware choices and data transmission media."
                        }
                    }
                ],

                # Page 3: Formative Knowledge Checks (Lesson 33)
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Classifying Network Scopes for an International NGO",
                        "content": {
                            "problem_statement": "An international conservation NGO operating in Kenya requires communication across four distinct environments: (1) A field officer syncing a GPS smartwatch to a tablet in the field; (2) 40 workstations and 3 printers inside the Nairobi headquarters office; (3) 8 municipal research branches connected across Nairobi County over dark fiber; (4) The headquarters connecting to research field stations in Kenya, Tanzania, and Uganda. Classify each network scope and state the typical transmission technology used.",
                            "step_by_step_solution": [
                                {
                                    "step_number": 1,
                                    "step_title": "Classify Field Watch-to-Tablet Link",
                                    "explanation": "Distance is under 10 meters around a single user. Classification: **Personal Area Network (PAN)** using Bluetooth or Wi-Fi Direct."
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Classify Nairobi Headquarters Office",
                                    "explanation": "Devices are contained within a single building/floor. Classification: **Local Area Network (LAN)** using Cat6 Gigabit Ethernet and Wi-Fi 6 WLAN."
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Classify 8 Municipal Branches across Nairobi County",
                                    "explanation": "Interconnects corporate facilities across a 30 km urban municipal radius. Classification: **Metropolitan Area Network (MAN)** using leased dark fiber-optic ring."
                                },
                                {
                                    "step_number": 4,
                                    "step_title": "Classify Multi-National Cross-Border Network",
                                    "explanation": "Spans across international boundaries and long distances. Classification: **Wide Area Network (WAN)** using telecommunication carrier subsea/terrestrial fiber and satellite backbones."
                                }
                            ]
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 1: Personal Area Network Identification",
                        "content": {
                            "question": "Which network type is most suitable for wirelessly syncing a fitness smartwatch to a smartphone inside a user's pocket?",
                            "options": [
                                "Wide Area Network (WAN)",
                                "Metropolitan Area Network (MAN)",
                                "Personal Area Network (PAN)",
                                "Wireless Access Gateway"
                            ],
                            "correct_answer": "Personal Area Network (PAN)",
                            "explanation": "A Personal Area Network (PAN) operates within an intimate personal radius of under 10 meters, utilizing short-range protocols like Bluetooth or NFC to interconnect personal wearable devices."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 2: Municipal Network Classification",
                        "content": {
                            "question": "A fiber-optic network connecting 15 municipal county government branch offices across the city of Kisumu (spanning 25 km) is classified as a:",
                            "options": [
                                "Local Area Network (LAN)",
                                "Personal Area Network (PAN)",
                                "Metropolitan Area Network (MAN)",
                                "Wide Area Network (WAN)"
                            ],
                            "correct_answer": "Metropolitan Area Network (MAN)",
                            "explanation": "A Metropolitan Area Network (MAN) spans an entire municipality or urban district (typically 10 to 50 km), interconnecting multiple corporate or government LANs over a shared high-speed fiber backbone."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 3: The World's Largest WAN",
                        "content": {
                            "question": "Which of the following networks is the world's most prominent example of a Wide Area Network (WAN)?",
                            "options": [
                                "A school computer laboratory intranet",
                                "The Global Internet",
                                "A university campus Wi-Fi network",
                                "A Bluetooth mesh of smart home lights"
                            ],
                            "correct_answer": "The Global Internet",
                            "explanation": "The Internet is the ultimate Wide Area Network (WAN), spanning continents and countries by interconnecting millions of public, private, academic, and government networks."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 4: WLAN Transmission Characteristics",
                        "content": {
                            "question": "What is the primary physical transmission medium utilized by a Wireless Local Area Network (WLAN)?",
                            "options": [
                                "Category 6 Unshielded Twisted Pair (UTP) copper cables",
                                "High-frequency Radio Frequency (RF) waves (Wi-Fi)",
                                "Infrared line-of-sight laser beams",
                                "Subsea singlemode glass fiber-optics"
                            ],
                            "correct_answer": "High-frequency Radio Frequency (RF) waves (Wi-Fi)",
                            "explanation": "WLANs utilize unguided radio frequency waves (such as 2.4 GHz, 5 GHz, or 6 GHz Wi-Fi bands) to allow mobile devices to communicate without physical wires over ranges of up to 100 meters."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LEARNING UNIT 2: Network Devices, Hardware Roles, and DTE vs. DCE
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Network Devices, Hardware Roles, and DTE vs. DCE",
            "unit_description": "Architectural elements of computer networks: DTE vs DCE, Network Interface Cards, Hubs, Switches, Routers, Modems, Repeaters, Bridges, and Gateways.",
            "lesson_title": "Network Devices, Hardware Roles, and DTE vs. DCE",
            "pages": [
                # Page 1: Logistics Analogy & Core Node Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Active Network Hardware Infrastructure",
                        "content": {
                            "goal": "Identify and distinguish the core hardware devices that enable computer communication, differentiating endpoints, physical adapters, and intelligent switching nodes."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 'Global Cargo Logistics' Analogy & Core Definitions",
                        "content": {
                            "markdown": """### **The 'Global Cargo Logistics' Analogy**
Imagine a complex global shipping and logistics network:
- **Factories and Warehouses**: The factories that manufacture products and the warehouses that unbox them represent the endpoints—the source and destination of all goods.
- **Loading Docks & Container Adapters**: Specialized equipment that packs raw factory goods into standardized shipping containers.
- **Local Mailroom Clerks vs. Intelligent Sorting Facilities**: A blind mail clerk shouts out every name in a crowded room, whereas a smart sorting facility reads barcode destination labels and sends containers *strictly* down the conveyor belt for that specific delivery truck.
- **Inter-City Highway Couriers**: Navigation dispatchers who use highway route maps to move containers across distinct cities.

In computer networking, data packets are the cargo, and specialized **network devices** act as this logistics infrastructure!

### **Core Device Definitions**
- **Node**: Any physical electronic device connected to a network capable of generating, receiving, or forwarding data packets.
- **Client**: A computer or terminal device (such as a desktop PC, laptop, or smartphone) that requests resources, data, or services from a central system.
- **Server**: A dedicated, high-performance computer that hosts databases, websites, files, or print queues, serving them to authorized client devices upon request.
- **Network Interface Card (NIC)**: The hardware controller and physical port (e.g., Ethernet port or Wi-Fi chip) that connects a computer to the transmission medium, containing a permanent hardware MAC address.
- **Wireless Access Point (WAP)**: A wireless transceiver device that broadcasts radio signals, bridging wireless WLAN devices onto a wired local network backbone."""
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Enterprise Network Switch and Patch Panel",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Network_switch.jpg/800px-Network_switch.jpg",
                            "caption": "Figure 10.3: High-density 24-port enterprise network switch used in server rooms to interconnect local workstations with dedicated full-duplex Gigabit links.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    }
                ],

                # Page 2: Technical Deep Dive: DTE vs. DCE
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: DTE vs. DCE Architectural Roles",
                        "content": {
                            "goal": "Master the technical distinction between Data Terminal Equipment (DTE) and Data Circuit-terminating Equipment (DCE) in the data communication pipeline."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Technical Deep Dive: DTE vs. DCE Architecture",
                        "content": {
                            "markdown": """### **DTE vs. DCE: The Two Halves of Network Hardware**
All hardware components in a telecommunication link are categorized into two fundamental classes based on their position in the data stream:

```
+------------+       +------------+                +------------+       +------------+
| DTE Device | ----> | DCE Device | ===( Medium )==| DCE Device | ----> | DTE Device |
| (Computer) |       |  (Modem)   |                |  (Modem)   |       | (Computer) |
+------------+       +------------+                +------------+       +------------+
```

#### **1. DTE (Data Terminal Equipment)**
- **Role**: The **end-user devices** that act as the ultimate source (generator) or sink (consumer) of digital data.
- **Characteristics**: DTE devices operate at the higher software and application layers. They process binary data but do not have built-in capabilities to directly modulate analog transmission lines or handle long-distance line clock synchronization.
- **Examples**: Desktop computers, laptops, file servers, network laser printers, database servers, and IP security cameras.

#### **2. DCE (Data Circuit-terminating Equipment)**
- **Role**: The **interface devices** that sit directly between the DTE and the physical transmission medium.
- **Characteristics**: The DCE takes raw digital bits from the DTE, encodes/modulates them into signals compatible with the physical line (such as analog audio frequencies on copper or light pulses on fiber), and provides clock synchronization signals.
- **Examples**: Modems (Modulator-Demodulator), CSU/DSU (Channel Service Unit/Data Service Unit) boxes, optical transceivers, and Network Interface Cards (NICs)."""
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "DTE vs. DCE Communication Pipeline",
                        "content": {
                            "svg_content": SVG_DTE_VS_DCE_ARCHITECTURE,
                            "caption": "Figure 10.4: Architectural pipeline illustrating how DTE devices (computers) pass digital payloads to DCE devices (modems/transceivers) for physical signal encoding across carrier media."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "DTE vs DCE Devices Explained Simply",
                        "content": {
                            "youtube_id": "k2GjUa3W7OQ",
                            "description": "Clear animated explanation of the electrical and logical differences between Data Terminal Equipment and Data Circuit-terminating Equipment."
                        }
                    }
                ],

                # Page 3: Active Device Mechanics: Hubs vs. Switches vs. Routers
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Hubs, Switches, and Routers Compared",
                        "content": {
                            "goal": "Compare the internal packet-handling mechanisms, collision domain isolation, and OSI layer operations of Hubs, Switches, and Routers."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Comparative Mechanics: Hubs vs. Switches vs. Routers",
                        "content": {
                            "markdown": """### **Active Network Devices Compared**

#### **1. Hub (Layer 1 - Physical Broadcasting)**
- **Operation**: A hub is an unmanaged, "dumb" electronic repeater. When an electrical signal arrives on Port 1, the hub blindly amplifies and retransmits it out of **all other ports**.
- **Collision Domain**: All connected devices share a **single collision domain**. If two computers transmit simultaneously, their electrical signals collide and destroy the data frames. Only one device can transmit at a time (Half-Duplex).
- **Efficiency**: Very low. Every device is forced to process frames not meant for it, creating severe bandwidth congestion.

#### **2. Switch (Layer 2 - MAC Address Forwarding)**
- **Operation**: A switch maintains an internal **MAC Address Table** (CAM Table). When a frame arrives, the switch inspects the destination hardware MAC address (e.g., `00:0a:95:9d:68:16`) and forwards the frame **strictly to the designated target port**.
- **Collision Domain**: Every single port is an **isolated collision domain**. Multiple devices can send and receive simultaneously at full speed without collisions (Full-Duplex).
- **Limitation**: Operates only within the local network segment (LAN); cannot route across different subnets or to the internet.

#### **3. Router (Layer 3 - Logical IP Routing)**
- **Operation**: A router operates at the Network Layer using **logical IP addresses** (e.g., `192.168.1.1` or `142.250.190.46`). It maintains internal **Routing Tables** to calculate the fastest, most efficient multi-hop path across distinct networks.
- **Broadcast Isolation**: Routers block local broadcast traffic from escaping into the WAN, preventing broadcast storms from flooding global links.
- **Role**: Acts as the default gateway connecting private local LANs to external ISP backbones."""
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Collision Domains & Logic: Hub vs. Switch vs. Router",
                        "content": {
                            "svg_content": SVG_HUB_VS_SWITCH_VS_ROUTER,
                            "caption": "Figure 10.5: Detailed architectural comparison showing how Hubs broadcast at Layer 1, Switches isolate collisions at Layer 2 using MAC tables, and Routers interconnect networks at Layer 3 using IP tables."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Hub vs Switch vs Router Animation",
                        "content": {
                            "youtube_id": "1z0ULvg_pW8",
                            "description": "An intuitive 3D animation explaining how frames and packets traverse hubs, switches, and routers in modern networks."
                        }
                    }
                ],

                # Page 4: Specialized Network Elements: Repeaters, Bridges, Gateways
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Specialized Interconnection Hardware",
                        "content": {
                            "goal": "Identify the distinct functions of Repeaters, Bridges, and Protocol Gateways in expanding and linking heterogeneous network segments."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Specialized Network Elements: Repeaters, Bridges, and Gateways",
                        "content": {
                            "markdown": """### **Specialized Interconnection Hardware**

| Device | Layer | Primary Function | Key Requirement | Real-World Application |
| :--- | :--- | :--- | :--- | :--- |
| **Repeater** | Layer 1 (Physical) | Regenerates, cleans, and amplifies attenuated electrical/optical signals over extended cable runs. | Operates on raw physical signals; protocol-agnostic. | Extending Ethernet copper runs beyond the standard 100-meter UTP limit or undersea fiber lines. |
| **Bridge** | Layer 2 (Data Link) | Connects two separate local network segments running the **same communication protocol**, filtering traffic by MAC address. | Both segments must use identical protocol suites (e.g., Ethernet to Ethernet). | Splitting a congested school lab into two quieter sub-segments to halve collision traffic. |
| **Gateway** | Layers 4-7 (Application) | Translates and converts data between two completely **different, incompatible communication protocols**. | Performs full protocol conversion and header translation. | Connecting an old legacy industrial SNA mainframe system to a modern IP-based Ethernet cloud. |

### **Summary of Network Hardware Hierarchy**
- **To amplify signal distance**: Use a **Repeater**.
- **To connect identical networks**: Use a **Bridge**.
- **To switch local devices by MAC**: Use a **Switch**.
- **To route between IP subnets**: Use a **Router**.
- **To translate incompatible protocols**: Use a **Gateway**."""
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Modular Enterprise Router Hardware",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Cisco_router.jpg/800px-Cisco_router.jpg",
                            "caption": "Figure 10.6: Enterprise modular router equipped with Gigabit Ethernet interfaces and serial WAN ports for interconnecting remote corporate branches.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    }
                ],

                # Page 5: Formative Knowledge Checks (Lesson 34)
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Packet Flow Trace Through DTE, DCE, Switches, Routers, and Gateways",
                        "content": {
                            "problem_statement": "A workstation (DTE 1) in a school computer lab sends a print job to a legacy mainframe print server operating on an SNA mainframe protocol located in the administrative block across a routed WAN link. Trace how the packet moves through DTEs, DCEs, switches, routers, and gateways.",
                            "step_by_step_solution": [
                                {
                                    "step_number": 1,
                                    "step_title": "Data Generation at Source DTE and DCE Encoding",
                                    "explanation": "The user workstation (DTE) creates the raw digital print data. The internal NIC (DCE) encodes the bits into electrical differential signals onto the Cat6 patch cable."
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Intelligent Layer 2 Switching",
                                    "explanation": "The classroom switch reads the destination MAC address. It forwards the frame strictly out of the uplink port connected to the local router without broadcasting to other PCs."
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Layer 3 Routing Across Networks",
                                    "explanation": "The router strips the Layer 2 Ethernet frame, inspects the destination IP address, determines the optimal WAN path in its routing table, and forwards the packet to the remote admin router."
                                },
                                {
                                    "step_number": 4,
                                    "step_title": "Protocol Translation at Gateway & Destination DTE",
                                    "explanation": "Because the legacy mainframe print server uses SNA while the network uses TCP/IP, a Network Gateway translates the packet syntax. The print server (destination DTE) receives and processes the print job."
                                }
                            ]
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Network Hardware Roles & Collision Isolation",
                        "content": {
                            "text": "1. **DTE vs DCE**: DTEs (PCs, servers) generate/consume raw application data; DCEs (NICs, modems) interface DTEs to physical carrier lines.\\n2. **Hubs vs Switches vs Routers**: Hubs share a single collision domain; Switches isolate collision domains per port via MAC tables; Routers route packets between distinct IP networks.\\n3. **Gateways**: Provide crucial protocol translation between incompatible network architectures."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 1: DTE vs DCE Classification",
                        "content": {
                            "question": "Which of the following devices is classified as Data Terminal Equipment (DTE)?",
                            "options": [
                                "A dedicated high-performance database server",
                                "A high-speed ADSL telephone modem",
                                "An optical fiber transceiver CSU/DSU",
                                "A line clocking synchronization interface"
                            ],
                            "correct_answer": "A dedicated high-performance database server",
                            "explanation": "A database server is an endpoint that generates and processes application data, making it a DTE (Data Terminal Equipment). Modems and transceivers are DCE devices that interface DTEs to the physical transmission line."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 2: Switch vs Hub Efficiency",
                        "content": {
                            "question": "Why does replacing a network hub with an intelligent network switch dramatically improve network throughput and eliminate collisions?",
                            "options": [
                                "A switch modulates analog voice carrier waves into digital light pulses.",
                                "A switch maintains a MAC address table and forwards frames strictly to the designated destination port.",
                                "A switch translates incompatible mainframe protocols into modern IP packets.",
                                "A switch acts as a passive electrical splitter for all connected nodes."
                            ],
                            "correct_answer": "A switch maintains a MAC address table and forwards frames strictly to the designated destination port.",
                            "explanation": "Unlike a hub which blindly broadcasts incoming bits out of every port causing collisions, a switch reads the target MAC address and creates a private, isolated point-to-point connection between sender and receiver."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 3: Layer 3 Pathfinding Device",
                        "content": {
                            "question": "Which layer-3 network device inspects logical IP addresses and consults internal routing tables to forward packets across different networks?",
                            "options": [
                                "Physical Hub",
                                "LAN Switch",
                                "Network Router",
                                "Passive Patch Panel"
                            ],
                            "correct_answer": "Network Router",
                            "explanation": "A router operates at Layer 3 (Network Layer), reading IP addresses to find the optimal path across distinct networks and directing traffic between local LANs and the internet."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 4: Translating Incompatible Protocols",
                        "content": {
                            "question": "What specialized network device is required when interconnecting two networks that operate on completely different communication protocols?",
                            "options": [
                                "Gateway",
                                "Repeater",
                                "Simple Bridge",
                                "Passive Hub"
                            ],
                            "correct_answer": "Gateway",
                            "explanation": "A Gateway acts as a protocol translator, unpackaging frames from one protocol suite and repackaging them into the syntax and format expected by the receiving network."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LEARNING UNIT 3: Network Evaluation Criteria, Connection Setup, and Security
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Network Evaluation Criteria, Physical Connection Setup, and Security",
            "unit_description": "Evaluating network performance, reliability, scalability, and security; step-by-step physical cabling and software IP configuration; access control lists and ethical resource sharing.",
            "lesson_title": "Network Evaluation Criteria, Connection Setup, and Security",
            "pages": [
                # Page 1: Restaurant Analogy & Evaluation Criteria
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Criteria for Evaluating Computer Networks",
                        "content": {
                            "goal": "Evaluate network designs against core engineering metrics: performance (speed/bandwidth), reliability (uptime/error rates), scalability, security, and resource sharing."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 'Restaurant Inspection' Analogy & Core Criteria",
                        "content": {
                            "markdown": """### **The 'Restaurant Inspection' Analogy**
Imagine dining at a premier restaurant in Nairobi. To determine whether the restaurant is high-quality, you systematically inspect several criteria:
- **Speed**: How quickly does the waiter deliver your food after placing the order?
- **Reliability**: Is the kitchen consistent, or do they occasionally serve cold or burnt food?
- **Security**: Does the restaurant have security guards and safes to protect your personal belongings?
- **Scalability**: If a tourist bus arrives with 50 hungry diners, can the kitchen expand smoothly without collapsing?

Evaluating a computer network requires the exact same engineering rigor!

### **The 4 Fundamental Network Evaluation Criteria**
1. **Performance**: The speed and capacity of the network, measured through:
   - **Throughput**: The actual volume of data successfully delivered per second (e.g., 940 Mbps on a 1 Gbps link).
   - **Bandwidth**: The maximum theoretical carrying capacity of the transmission medium.
   - **Latency & Round-Trip Time (RTT)**: The time delay taken for a packet to travel from source to destination.
2. **Reliability**: The consistency with which a network remains operational without failure:
   - **Mean Time Between Failures (MTBF)** and uptime percentage (e.g., "Five Nines" = 99.999% uptime).
   - Low packet loss and automatic link failover mechanisms.
3. **Scalability**: The capacity of the network architecture to grow—adding new classrooms, workstations, or servers—without requiring an expensive overhaul of existing hardware.
4. **Security & Resource Sharing**: Protecting shared data drives and peripherals from unauthorized access, malware propagation, or data tampering."""
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Network Evaluation Metrics",
                        "content": {
                            "text": "A robust network balances high throughput and low latency (Performance), high uptime and low packet loss (Reliability), modular expansion (Scalability), and role-based permissions (Security)."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Network Security, Firewalls, and Access Control Explained",
                        "content": {
                            "youtube_id": "5p3s8j0Q8F4",
                            "url": "https://www.youtube.com/watch?v=5p3s8j0Q8F4",
                            "description": "Comprehensive overview of enterprise defense-in-depth, ACL permissions, and network segmentation."
                        }
                    }
                ],

                # Page 2: Step-by-Step Connection Guide & LED Diagnostics
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Setting Up and Verifying a Wired Connection",
                        "content": {
                            "goal": "Master the hands-on procedure for physically terminating and connecting an Ethernet patch cable, reading hardware LED status lights, and executing IP configuration commands."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Step-by-Step Connection Setup & Diagnostic Protocol",
                        "content": {
                            "markdown": """### **Step-by-Step Practical Connection Guide**

Connecting a workstation to a local network follows a three-stage sequence:

```
[ Step 1: Physical Link ] ---> [ Step 2: LED Port Check ] ---> [ Step 3: IP Address Configuration ]
```

#### **Step 1: Physical Cable Link**
1. Obtain a certified Category 6 (Cat6) Unshielded Twisted Pair (UTP) patch cable with undamaged RJ-45 modular connectors.
2. Align the connector with the computer's Ethernet NIC port and push firmly until the plastic locking tab engages with a clear, audible **click**.
3. Connect the opposite RJ-45 plug into an active wall socket or switch port.

#### **Step 2: Hardware LED Status Diagnostics**
Observe the two indicator LED lights built directly into the computer's Ethernet port:
- **Link LED (Solid Green)**: Confirms that an electrical connection has been established between the NIC and the switch. If this LED is dark/OFF, the cable is unplugged, cut, or the switch port lacks power.
- **Activity LED (Flashing Amber)**: Confirms that data frames (transmissions and receptions) are actively moving across the physical link.

#### **Step 3: Logical OS Network Verification**
Open the Operating System command prompt and inspect the assigned IP parameters:
- **Windows**: Run `ipconfig /all`
- **Linux / macOS**: Run `ip addr` or `ifconfig`

Ensure the Dynamic Host Configuration Protocol (DHCP) server has assigned:
- A valid **IPv4 Address** (e.g., `192.168.1.45`).
- A matching **Subnet Mask** (e.g., `255.255.255.0`).
- The correct **Default Gateway IP** (e.g., `192.168.1.1`).
*(Note: An address starting with `169.254.x.x` indicates an APIPA failure—the computer failed to reach a DHCP server!)*"""
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Physical Connection & Hardware LED Diagnostics",
                        "content": {
                            "svg_content": SVG_PHYSICAL_CONNECTION_AND_LEDS,
                            "caption": "Figure 10.7: Physical connection workflow showing RJ-45 8P8C seating, NIC Link/Activity LED diagnostic indicators, and OS IP verification terminal output."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "RJ-45 Ethernet Patch Cables and Wall Jacks",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Ethernet_cables_connected_to_a_patch_panel.jpg/800px-Ethernet_cables_connected_to_a_patch_panel.jpg",
                            "caption": "Figure 10.8: Neatly dressed Cat6 patch cables terminated into an enterprise patch panel, providing clean physical links between wall jacks and network switches.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    }
                ],

                # Page 3: Security, Access Control Lists (ACLs), and Ethical Resource Sharing
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Network Resource Security and Ethics",
                        "content": {
                            "goal": "Configure Access Control Levels (ACLs), user authentication policies, and antivirus defenses to secure shared network resources in an organizational environment."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Security, Access Control Lists, and Ethical Resource Sharing",
                        "content": {
                            "markdown": """### **Securing Shared Network Resources**
Resource sharing (sharing high-speed printers, cloud databases, and storage folders) provides massive cost savings, but exposes organizations to security risks if unprotected.

#### **1. User Authentication**
- Every individual must log in with unique, non-shared credentials (username and strong password or multi-factor token).
- Anonymous "guest" shares must be strictly disabled on sensitive organizational directories.

#### **2. Access Control Levels (ACLs)**
Directories and files must be configured according to the **Principle of Least Privilege**:
- **Read-Only**: Users can view and open files (e.g., student access to assignment handouts and syllabi) but cannot edit, overwrite, or delete them.
- **Read-Write**: Users can create, edit, and save modifications (e.g., a teacher editing grade rubrics in their private departmental folder).
- **Full Control / Administrative**: Reserved strictly for network administrators to change permissions, ownership, and directory structures.

#### **3. Network Antivirus and Firewall Shields**
- Active firewall rules block unauthorized external port scans and worm self-replication across open SMB/NFS file shares.
- Real-time endpoint antivirus scans incoming and outgoing files across shared network folders."""
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Enterprise Network Security: Defense-in-Depth Model",
                        "content": {
                            "svg_content": SVG_NETWORK_SECURITY_DEFENSE_IN_DEPTH,
                            "caption": "Figure 10.9: Multi-layered security framework spanning Perimeter Firewalls, Network VLANs, Host Active Directory RBAC, and Data Cryptography."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Enterprise Hardware Next-Generation Firewall Appliance",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Fortinet_FortiGate_firewall.jpg/800px-Fortinet_FortiGate_firewall.jpg",
                            "caption": "Figure 10.10: Rack-mounted hardware security firewall appliance providing stateful packet inspection and perimeter intrusion protection.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Safe Resource Sharing",
                        "content": {
                            "text": "Network resource sharing must always be guarded by strong user authentication, strict Read-Only or Read-Write Access Control Levels (ACLs), and active firewall inspection."
                        }
                    }
                ],

                # Page 4: Formative Knowledge Checks (Lesson 35)
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Setting Up and Auditing a Secure Lab Network Connection",
                        "content": {
                            "problem_statement": "A technician is connecting a new computer to the school network. After plugging in the Cat6 cable, the NIC Link LED turns solid green and Activity LED blinks amber. The technician runs 'ipconfig' and sees IP: 169.254.12.8, Subnet: 255.255.0.0, Gateway: [Blank]. The student cannot open the shared school files. Diagnose the issue and outline the remediation steps.",
                            "step_by_step_solution": [
                                {
                                    "step_number": 1,
                                    "step_title": "Evaluate Physical Layer (Layer 1)",
                                    "explanation": "Solid green Link LED and blinking amber Activity LED confirm that physical Layer 1 electrical connection between NIC and switch is 100% healthy."
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Diagnose Logical IP Assignment (Layer 3)",
                                    "explanation": "The address starting with 169.254.x.x is an Automatic Private IP Addressing (APIPA) address. This proves the computer failed to receive an IP lease from the DHCP server (DHCP failure or VLAN misconfiguration)."
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Remediation & Security Verification",
                                    "explanation": "Check switch port VLAN configuration and restart DHCP client with 'ipconfig /renew'. Once an address in the 192.168.1.x range is received, verify file share access permissions (Read-Only ACLs)."
                                }
                            ]
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 1: Hardware LED State Interpretation",
                        "content": {
                            "question": "A student plugs an Ethernet cable into a lab computer, but the Link LED on the NIC remains completely dark (OFF). What does this indicate?",
                            "options": [
                                "The computer has an incorrect DNS server IP configured.",
                                "A physical link failure exists (e.g., broken cable, unplugged switch, or damaged port).",
                                "The computer is downloading data too quickly for the LED to blink.",
                                "The DHCP server has assigned an APIPA address."
                            ],
                            "correct_answer": "A physical link failure exists (e.g., broken cable, unplugged switch, or damaged port).",
                            "explanation": "A dark/unlit Link LED indicates that no electrical circuit has been closed between the NIC and the switch at the physical layer (Layer 1). The cable must be reseated or replaced."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 2: Purpose of Access Control Levels (ACLs)",
                        "content": {
                            "question": "What is the primary function of configuring Access Control Levels (ACLs) on a shared school file server?",
                            "options": [
                                "To increase the physical signal propagation speed through copper wires.",
                                "To restrict directory permissions so students have Read-Only access while preventing unauthorized editing or deletion.",
                                "To automate the computer BIOS boot order sequence.",
                                "To modulate analog radio signals onto optical fiber cables."
                            ],
                            "correct_answer": "To restrict directory permissions so students have Read-Only access while preventing unauthorized editing or deletion.",
                            "explanation": "Access Control Levels (ACLs) enforce security policies by granting specific permission levels (Read-Only, Read-Write, Full Control) based on user authentication roles."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 3: IP Verification Command in Windows",
                        "content": {
                            "question": "Which command line utility is used in Windows to display the current IP address, subnet mask, and default gateway assigned to the network adapter?",
                            "options": [
                                "ping -t",
                                "ipconfig",
                                "traceroute",
                                "format C:"
                            ],
                            "correct_answer": "ipconfig",
                            "explanation": "`ipconfig` (or `ipconfig /all`) is the standard Windows command used to inspect network adapter TCP/IP settings, DHCP lease status, and MAC hardware addresses."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 4: Network Scalability Defined",
                        "content": {
                            "question": "Which term describes the capability of a computer network to seamlessly expand by adding more users, devices, and nodes without requiring a complete structural redesign?",
                            "options": [
                                "Attenuation",
                                "Scalability",
                                "Latency",
                                "Modulation"
                            ],
                            "correct_answer": "Scalability",
                            "explanation": "Scalability is the architectural property that allows a network to grow in user capacity, node count, and geographical reach gracefully with minimal additional overhead."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LEARNING UNIT 4: Network Diagnostic Protocols and Practical Troubleshooting
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Network Diagnostic Protocols and Practical Troubleshooting",
            "unit_description": "Structured four-step ping diagnostic sequence, troubleshooting flowcharts, ICMP packet traces, and real-world case study architecture (Maasai Mara Safari Eco-Lodge).",
            "lesson_title": "Network Diagnostic Protocols and Practical Troubleshooting",
            "pages": [
                # Page 1: The Structured 4-Step Diagnostic Sequence
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Systematic Network Troubleshooting",
                        "content": {
                            "goal": "Execute the standard four-step command line ping diagnostic sequence to isolate software protocol, physical cable, gateway router, ISP link, and DNS failures."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 4-Step Network Diagnostic Sequence",
                        "content": {
                            "markdown": """### **Structured Troubleshooting vs. Guesswork**
When a network connection fails, experienced network technicians never guess. They execute a structured, sequential diagnostic protocol to pinpoint the exact layer of failure:

```
[ Step 1: Ping Localhost ] ---> [ Step 2: Ping Gateway ] ---> [ Step 3: Ping External IP ] ---> [ Step 4: Test DNS ]
```

---

#### **Step 1: Test Local Host TCP/IP Stack**
- **Action**: Execute `ping 127.0.0.1` (the standard IPv4 loopback address).
- **Meaning**: Tests the computer's internal operating system networking software stack without putting electrical signals onto the physical cable.
- **Diagnostic Result**: If this ping fails, the computer's own OS network drivers are corrupt, disabled, or missing.

#### **Step 2: Test Physical Local Link to Default Gateway**
- **Action**: Execute `ping 192.168.1.1` (the IP address of the local router / default gateway).
- **Meaning**: Sends an ICMP Echo Request down the physical Ethernet cable, through the switch, to the router's local interface.
- **Diagnostic Result**: If this fails, the fault is inside the local room (e.g., loose cable, damaged switch port, or wrong subnet mask).

#### **Step 3: Test External Internet Backbone Route**
- **Action**: Execute `ping 8.8.8.8` (Google's reliable public DNS server IP).
- **Meaning**: Sends packets past the local router, through the modem and ISP uplink, onto the global internet WAN.
- **Diagnostic Result**: If Step 2 succeeded but Step 3 fails, your local LAN is fine, but the ISP internet uplink is down or the modem has lost signal.

#### **Step 4: Test Domain Name Resolution (DNS)**
- **Action**: Execute `ping google.com`.
- **Meaning**: Tests whether the network can translate the human-readable domain name (`google.com`) into its numerical IP address (`142.250.190.46`).
- **Diagnostic Result**: If Step 3 succeeded (`ping 8.8.8.8`) but Step 4 fails (`ping google.com`), the internet connection is 100% active, but the computer has an incorrect or offline DNS server configured!"""
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Diagnostic Sequence Flowchart & Failure Matrix",
                        "content": {
                            "svg_content": SVG_TROUBLESHOOTING_FLOWCHART,
                            "caption": "Figure 10.9: Structured network diagnostic sequence flowchart showing exact test commands and corresponding hardware/software failure conclusions."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "How to Use Ping, Traceroute, and DNS Diagnostics",
                        "content": {
                            "youtube_id": "0_q6FODVys8",
                            "description": "Hands-on tutorial demonstrating practical network troubleshooting using ping, ipconfig, and traceroute on the command line."
                        }
                    }
                ],

                # Page 2: Step-by-Step Worked Example: Diagnostic Trace Problem
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Analyzing Network Diagnostic Output",
                        "content": {
                            "goal": "Analyze real-world terminal output from ping and traceroute commands to diagnose root causes of connectivity failures."
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Step-by-Step Worked Example: Diagnosing a Laboratory Network Failure",
                        "content": {
                            "problem_statement": """A Grade 10 student in a Nairobi high school opens a web browser to access an educational portal at 'www.kicd.ac.ke', but the browser displays 'Server Not Found / DNS Probe Finished No Internet'.
The student opens the terminal and executes the four-step diagnostic sequence. Analyze the output below and isolate the exact fault:

1. `ping 127.0.0.1` -> 4 packets transmitted, 4 received, 0% packet loss (Time: 0.1ms).
2. `ping 192.168.1.1` -> 4 packets transmitted, 4 received, 0% packet loss (Time: 1.2ms).
3. `ping 8.8.8.8` -> 4 packets transmitted, 4 received, 0% packet loss (Time: 24ms).
4. `ping kicd.ac.ke` -> 'Ping request could not find host kicd.ac.ke. Please check the name and try again.'""",
                            "step_by_step_solution": [
                                {
                                    "step_number": 1,
                                    "step_title": "Analyze Step 1 (Loopback Ping)",
                                    "explanation": "`ping 127.0.0.1` succeeded with 0% loss. This proves that the workstation's local operating system TCP/IP stack and network interface drivers are completely healthy."
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Analyze Step 2 (Gateway Ping)",
                                    "explanation": "`ping 192.168.1.1` succeeded with 1.2ms latency. This proves that the physical Ethernet cable, RJ-45 connectors, classroom switch, and local router port are fully operational."
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Analyze Step 3 (External IP Ping)",
                                    "explanation": "`ping 8.8.8.8` succeeded with 24ms latency. This proves that the school's ISP connection, fiber modem, and global internet routing are 100% active."
                                },
                                {
                                    "step_number": 4,
                                    "step_title": "Analyze Step 4 (Domain Name Resolution)",
                                    "explanation": "Because numerical internet routing works (`8.8.8.8` succeeds) but human-readable domain names fail (`kicd.ac.ke` cannot be found), the fault is exclusively a **DNS Configuration Failure**."
                                },
                                {
                                    "step_number": 5,
                                    "step_title": "Prescribe Corrective Action",
                                    "explanation": "Open network adapter properties and replace the corrupted DNS IP with a working DNS server (e.g., Primary: `8.8.8.8`, Secondary: `1.1.1.1`). Re-test by pinging `kicd.ac.ke`."
                                }
                            ]
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Wireshark Network Protocol Packet Capture Interface",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Wireshark_packet_capture.png/800px-Wireshark_packet_capture.png",
                            "caption": "Figure 10.11: Wireshark packet analyzer displaying live ICMP echo request and reply frames during a network ping diagnostic.",
                            "author": "Wikimedia Commons",
                            "licensing": "GPLv2"
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: The DNS Diagnostic Golden Rule",
                        "content": {
                            "text": "If numerical pings to public IPs (e.g. 8.8.8.8) succeed while named pings (e.g. google.com) fail, the physical and routing infrastructure is completely intact; only the DNS server address needs remediation."
                        }
                    }
                ],

                # Page 3: Real-World Case Study: Maasai Mara Safari Eco-Lodge
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Integrated Real-World Network Engineering",
                        "content": {
                            "goal": "Synthesize network classifications, device selection, power constraints, and security models to architect a complete remote network for an off-grid tourist lodge."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Case Study: The Maasai Mara Tourist Eco-Lodge Network",
                        "content": {
                            "markdown": """### **The Scenario: Maasai Mara Eco-Lodge**
A remote luxury safari eco-lodge located in the Maasai Mara wilderness requires a modern, highly reliable computer network:
- **Main Reception Office**: Houses 5 administrative computers and 2 shared billing printers, powered by a local solar array and lithium backup batteries.
- **12 Individual Guest Cabins**: Scattered across a 200-meter radius in the bush. Guests expect reliable Wi-Fi for messaging and browsing.
- **Internet Uplink**: Located in a remote valley with no physical copper or telecom fiber lines. The nearest cellular mast is 40 km away across the savannah.

---

### **Comprehensive Engineering Blueprint**

#### **1. Network Scopes Deployed**
- **LAN (Main Office)**: High-speed wired Category 6 Ethernet connects administrative PCs and billing printers to a central 24-Port Gigabit PoE Switch.
- **WLAN (Guest Cabins)**: Long-range, ruggedized outdoor Wireless Access Points (WAPs) deploy a 200-meter Wi-Fi mesh across the guest cabins.
- **WAN (Internet Uplink)**: A Low-Earth Orbit (LEO) Satellite terminal (e.g. Starlink Business) provides high-bandwidth, low-latency satellite internet connectivity.

#### **2. Active Hardware Deployment**
- **DTE Elements**: 5 Admin PCs, 2 Network Laser Printers, Guest smartphones/laptops.
- **DCE Elements**: Satellite Modem & Dish transceiver, Switch PoE ports, Workstation NICs.
- **Layer 2 PoE Switch**: Powers remote outdoor access points over the Ethernet cable (eliminating separate high-voltage trenching to each pole).
- **Layer 3 Gateway Router & Firewall**: Segregates the network into isolated Virtual LANs (VLANs).

#### **3. Security & Resource Sharing Policies**
- **VLAN Isolation**: Admin Office devices reside on a private management VLAN (`192.168.10.0/24`), completely isolated from the Guest Wi-Fi VLAN (`192.168.20.0/24`). Guests cannot scan or access reception files or printers.
- **Client Isolation**: Guest devices on Wi-Fi cannot see or communicate with other guest devices.
- **Access Control Levels (ACLs)**: Reception staff have Read-Write access to guest billing databases; booking staff have Read-Only access.
- **Bandwidth Shaping**: Each guest device is throttled to 5 Mbps to prevent a single guest from consuming the entire satellite uplink."""
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Maasai Mara Eco-Lodge Integrated Network Architecture",
                        "content": {
                            "svg_content": SVG_MAASAI_MARA_ECO_LODGE_TOPOLOGY,
                            "caption": "Figure 10.10: Complete architectural topology for the remote Maasai Mara Eco-Lodge, illustrating solar power, Starlink satellite WAN uplink, core router, office LAN, and 200m outdoor mesh WLAN."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Handheld Wiremap Continuity Cable Tester",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Network_cable_tester.jpg/800px-Network_cable_tester.jpg",
                            "caption": "Figure 10.12: Digital wiremap tester diagnosing continuity, open circuits, and split pairs on RJ-45 Ethernet cables.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    }
                ],

                # Page 4: Summative Assessment & Comprehensive Practice
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative Check 1: Loopback Address Identification",
                        "content": {
                            "question": "Which special diagnostic IP address tests a computer's internal TCP/IP software stack without broadcasting any electrical signals onto the physical cable?",
                            "options": [
                                "192.168.1.1",
                                "127.0.0.1",
                                "8.8.8.8",
                                "255.255.255.255"
                            ],
                            "correct_answer": "127.0.0.1",
                            "explanation": "`127.0.0.1` is the standardized IPv4 loopback address that routes packets internally within the local OS network driver to verify the health of the TCP/IP stack."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative Check 2: Gateway Failure Isolation",
                        "content": {
                            "question": "If executing `ping 127.0.0.1` succeeds but `ping 192.168.1.1` (the default gateway) returns 'Destination Host Unreachable', where is the failure located?",
                            "options": [
                                "The computer's operating system network stack is corrupted.",
                                "A local physical link or configuration fault exists between the computer, patch cable, and the local router.",
                                "Google's public DNS servers in North America are offline.",
                                "The domain registrar has suspended the website URL."
                            ],
                            "correct_answer": "A local physical link or configuration fault exists between the computer, patch cable, and the local router.",
                            "explanation": "Because loopback succeeds, the OS is fine. Failing to reach the default gateway (`192.168.1.1`) proves the fault is strictly on the local room's physical cable, switch port, or subnet configuration."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative Check 3: Satellite WAN Justification",
                        "content": {
                            "question": "Why is a Satellite transceiver the most viable WAN uplink technology for an off-grid lodge located deep inside the Maasai Mara wilderness?",
                            "options": [
                                "Satellite links require standard unshielded twisted pair copper cables buried across the plains.",
                                "Satellite signals provide global wide-area coverage from orbit, bypassing the need for physical terrestrial fiber trenches or nearby cellular masts.",
                                "Satellite modems eliminate the requirement for Access Control Levels (ACLs).",
                                "Satellite dishes operate exclusively within a 10-meter Personal Area Network radius."
                            ],
                            "correct_answer": "Satellite signals provide global wide-area coverage from orbit, bypassing the need for physical terrestrial fiber trenches or nearby cellular masts.",
                            "explanation": "In remote geographic regions lacking terrestrial telecommunication infrastructure (cables or cell towers), satellite communication is the premier WAN uplink solution because it connects directly to orbiting spacecraft."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative Check 4: Network Device Matching",
                        "content": {
                            "question": "Match the network device with its correct operational layer: (1) Switch, (2) Router, (3) Hub.",
                            "options": [
                                "(1) Layer 1 Physical, (2) Layer 2 Data Link, (3) Layer 3 Network",
                                "(1) Layer 2 Data Link (MAC), (2) Layer 3 Network (IP), (3) Layer 1 Physical (Bits)",
                                "(1) Layer 3 Network, (2) Layer 1 Physical, (3) Layer 2 Data Link",
                                "(1) Layer 7 Application, (2) Layer 2 Data Link, (3) Layer 4 Transport"
                            ],
                            "correct_answer": "(1) Layer 2 Data Link (MAC), (2) Layer 3 Network (IP), (3) Layer 1 Physical (Bits)",
                            "explanation": "Switches forward frames by hardware MAC address at Layer 2, Routers route packets by logical IP address at Layer 3, and Hubs blindly repeat electrical bits at Layer 1."
                        }
                    }
                ]
            ]
        }
    ]

# =====================================================================
# INGESTION EXECUTOR
# =====================================================================

def ingest_grade10_topic10(replace: bool = True):
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 10 Computer Science — Topic 10")
    print("Topic: Computer Network Elements")
    print("=" * 80)

    curriculum = Curriculum.objects.get(id=5)
    grade = Grade.objects.get(curriculum=curriculum, level=10)
    subject, _ = Subject.objects.get_or_create(grade=grade, name="Computer Science")

    with transaction.atomic():
        topic, created = Topic.objects.get_or_create(
            subject=subject,
            order=10,
            defaults={
                "name": "Computer Network Elements",
                "description": "Comprehensive structural analysis of computer networks: geographical scopes (PAN, LAN, WLAN, MAN, WAN), active hardware devices (DTE vs DCE, Switches, Routers, Modems, Gateways), performance criteria, physical connection protocols, and structured diagnostic troubleshooting sequences."
            }
        )

        if not created and replace:
            print(f"[*] Topic 10 already exists (ID: {topic.id}). Performing clean replacement of units and lessons...")
            topic.learning_units.all().delete()
            topic.lessons.all().delete()
            topic.name = "Computer Network Elements"
            topic.description = "Comprehensive structural analysis of computer networks: geographical scopes (PAN, LAN, WLAN, MAN, WAN), active hardware devices (DTE vs DCE, Switches, Routers, Modems, Gateways), performance criteria, physical connection protocols, and structured diagnostic troubleshooting sequences."
            topic.save()

        curriculum_data = build_topic10_curriculum()

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
                    "topic_order": 10,
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
                        block_id=f"g10_cs_t10_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={"topic_order": 10, "unit_order": u_order, "page": page_idx}
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
    print(f"TOPIC 10 INGESTION COMPLETE:")
    print(f"  Units Created:   {total_units}")
    print(f"  Lessons Created: {total_lessons}")
    print(f"  Pages Created:   {total_pages}")
    print(f"  Blocks Created:  {total_blocks}")
    print(f"  Assets Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_grade10_topic10(replace=True)
