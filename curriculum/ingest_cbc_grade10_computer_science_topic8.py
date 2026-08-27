"""
VLearn CBC Grade 10 Computer Science — Topic 8: Data Communication
Production Ingestion & Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Computer Science
Topic: Data Communication (Topic Order: 8)

Decomposed into 4 Comprehensive Learning Units & 4 Published Lessons:
  1. Basic Data Communication Concepts and Layered Models (Lesson 25)
  2. Characteristics, Components, and Diagnostic Troubleshooting (Lesson 26)
  3. Modes of Data Flow and Network Communication (Lesson 27)
  4. Significance, Historical Evolution, and Network Assessment (Lesson 28)
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
# HIGH PRECISION VECTOR SVGS FOR TOPIC 8
# =====================================================================

SVG_ANALOG_VS_DIGITAL = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Signal Representation: Analog Waveforms vs. Digital Binary Signals</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Comparing Continuous Electromagnetic Waves with Discrete Step-Like Digital States</text>

  <!-- Left Box: Analog Signal -->
  <g transform="translate(45, 90)">
    <rect width="415" height="390" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect x="15" y="15" width="385" height="30" rx="6" fill="#0284c7"/>
    <text x="207" y="35" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">ANALOG SIGNAL (Continuous Sine Wave)</text>
    
    <!-- Coordinate Axis -->
    <g transform="translate(30, 70)">
      <line x1="0" y1="120" x2="350" y2="120" stroke="#64748b" stroke-width="1.5"/>
      <line x1="30" y1="10" x2="30" y2="230" stroke="#64748b" stroke-width="1.5"/>
      <text x="350" y="135" font-size="10" fill="#94a3b8">Time (t)</text>
      <text x="20" y="20" font-size="10" fill="#94a3b8" text-anchor="end">Voltage (V)</text>
      
      <!-- Sine Wave -->
      <path d="M 30,120 Q 70,20 110,120 T 190,120 T 270,120 T 350,120" fill="none" stroke="#38bdf8" stroke-width="3"/>
      
      <!-- Labels -->
      <circle cx="70" cy="20" r="4" fill="#f59e0b"/>
      <text x="70" y="12" font-size="9" fill="#fcd34d" text-anchor="middle">Peak (+V)</text>
      <circle cx="150" cy="220" r="4" fill="#f59e0b"/>
      <text x="150" y="234" font-size="9" fill="#fcd34d" text-anchor="middle">Trough (-V)</text>
    </g>

    <!-- Characteristics Bullets -->
    <g transform="translate(25, 305)">
      <rect width="365" height="65" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="12" y="20" font-size="10" font-weight="bold" fill="#38bdf8">• Characteristics: Continuous values over time</text>
      <text x="12" y="38" font-size="9.5" fill="#cbd5e1">• Noise Impact: Prone to distortion and attenuation</text>
      <text x="12" y="54" font-size="9.5" fill="#94a3b8">• Examples: Human Voice, AM/FM Radio, Landline Audio</text>
    </g>
  </g>

  <!-- Right Box: Digital Signal -->
  <g transform="translate(500, 90)">
    <rect width="415" height="390" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect x="15" y="15" width="385" height="30" rx="6" fill="#059669"/>
    <text x="207" y="35" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">DIGITAL SIGNAL (Discrete Square Wave)</text>
    
    <!-- Coordinate Axis -->
    <g transform="translate(30, 70)">
      <line x1="0" y1="200" x2="350" y2="200" stroke="#64748b" stroke-width="1.5"/>
      <line x1="30" y1="10" x2="30" y2="220" stroke="#64748b" stroke-width="1.5"/>
      <text x="350" y="215" font-size="10" fill="#94a3b8">Time (t)</text>
      <text x="20" y="20" font-size="10" fill="#94a3b8" text-anchor="end">Voltage (V)</text>
      
      <!-- Square Wave -->
      <path d="M 30,200 L 30,60 L 90,60 L 90,200 L 150,200 L 150,60 L 210,60 L 210,200 L 270,200 L 270,60 L 330,60 L 330,200" fill="none" stroke="#34d399" stroke-width="3"/>
      
      <!-- Bit Values -->
      <text x="60" y="45" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">1 (High 5V)</text>
      <text x="120" y="190" font-size="12" font-weight="bold" fill="#f87171" text-anchor="middle">0 (Low 0V)</text>
      <text x="180" y="45" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">1 (High 5V)</text>
      <text x="240" y="190" font-size="12" font-weight="bold" fill="#f87171" text-anchor="middle">0 (Low 0V)</text>
      <text x="300" y="45" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">1 (High 5V)</text>
    </g>

    <!-- Characteristics Bullets -->
    <g transform="translate(25, 305)">
      <rect width="365" height="65" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="12" y="20" font-size="10" font-weight="bold" fill="#34d399">• Characteristics: Discrete binary states (0 and 1)</text>
      <text x="12" y="38" font-size="9.5" fill="#cbd5e1">• Noise Impact: High noise immunity, easily regenerated</text>
      <text x="12" y="54" font-size="9.5" fill="#94a3b8">• Examples: CPU Busses, SSDs, Modern LANs, HDMI</text>
    </g>
  </g>
</svg>
""")

SVG_OSI_VS_TCPIP = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Layered Network Architectures: OSI 7-Layer vs. TCP/IP 4-Layer Suite</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Mapping Protocol Data Units (PDUs), Core Responsibilities, and Internet Protocols</text>

  <!-- Left Column: OSI 7 Layers -->
  <g transform="translate(50, 90)">
    <text x="180" y="15" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">OSI 7-LAYER REFERENCE MODEL</text>
    
    <!-- 7: Application -->
    <rect x="0" y="28" width="360" height="38" rx="6" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <text x="15" y="52" font-size="11" font-weight="bold" fill="#f472b6">7. Application</text>
    <text x="345" y="52" font-size="10" fill="#cbd5e1" text-anchor="end">User Interface / Network API</text>

    <!-- 6: Presentation -->
    <rect x="0" y="70" width="360" height="38" rx="6" fill="#0f172a" stroke="#db2777" stroke-width="1.5"/>
    <text x="15" y="94" font-size="11" font-weight="bold" fill="#f472b6">6. Presentation</text>
    <text x="345" y="94" font-size="10" fill="#cbd5e1" text-anchor="end">Encryption, Compression, ASCII</text>

    <!-- 5: Session -->
    <rect x="0" y="112" width="360" height="38" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <text x="15" y="136" font-size="11" font-weight="bold" fill="#c084fc">5. Session</text>
    <text x="345" y="136" font-size="10" fill="#cbd5e1" text-anchor="end">Dialog &amp; Session Management</text>

    <!-- 4: Transport -->
    <rect x="0" y="154" width="360" height="42" rx="6" fill="#0f172a" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="15" y="176" font-size="11" font-weight="bold" fill="#60a5fa">4. Transport [Segment]</text>
    <text x="15" y="190" font-size="9.5" fill="#94a3b8">End-to-End Reliability, Flow &amp; Ports</text>

    <!-- 3: Network -->
    <rect x="0" y="200" width="360" height="42" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <text x="15" y="222" font-size="11" font-weight="bold" fill="#34d399">3. Network [Packet]</text>
    <text x="15" y="236" font-size="9.5" fill="#94a3b8">Logical IP Addressing &amp; Routing</text>

    <!-- 2: Data Link -->
    <rect x="0" y="246" width="360" height="42" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="15" y="268" font-size="11" font-weight="bold" fill="#fbbf24">2. Data Link [Frame]</text>
    <text x="15" y="282" font-size="9.5" fill="#94a3b8">MAC Addressing, Switches &amp; Framing</text>

    <!-- 1: Physical -->
    <rect x="0" y="292" width="360" height="42" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="15" y="314" font-size="11" font-weight="bold" fill="#f87171">1. Physical [Bits]</text>
    <text x="15" y="328" font-size="9.5" fill="#94a3b8">Electrical, Optical &amp; Radio Signals</text>
  </g>

  <!-- Middle Mapping Lines / Brackets -->
  <g transform="translate(420, 118)" stroke="#64748b" stroke-width="2">
    <!-- Top 3 to App -->
    <line x1="0" y1="40" x2="60" y2="40"/>
    <line x1="60" y1="40" x2="110" y2="40"/>
    <polygon points="110,40 102,36 102,44" fill="#64748b"/>

    <!-- Transport to Transport -->
    <line x1="0" y1="145" x2="110" y2="145"/>
    <polygon points="110,145 102,141 102,149" fill="#64748b"/>

    <!-- Network to Internet -->
    <line x1="0" y1="205" x2="110" y2="205"/>
    <polygon points="110,205 102,201 102,209" fill="#64748b"/>

    <!-- Data Link & Physical to Network Access -->
    <line x1="0" y1="280" x2="60" y2="280"/>
    <line x1="60" y1="280" x2="110" y2="280"/>
    <polygon points="110,280 102,276 102,284" fill="#64748b"/>
  </g>

  <!-- Right Column: TCP/IP 4 Layers -->
  <g transform="translate(545, 90)">
    <text x="180" y="15" font-size="14" font-weight="bold" fill="#34d399" text-anchor="middle">TCP/IP 4-LAYER INTERNET SUITE</text>
    
    <!-- 4: Application Layer -->
    <rect x="0" y="28" width="365" height="110" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="2"/>
    <text x="15" y="55" font-size="13" font-weight="bold" fill="#f472b6">4. Application Layer</text>
    <text x="15" y="75" font-size="10" fill="#cbd5e1">Combines Application, Presentation &amp; Session.</text>
    <rect x="15" y="85" width="335" height="42" rx="5" fill="#1e293b"/>
    <text x="25" y="103" font-size="10" font-weight="bold" fill="#38bdf8">Protocols:</text>
    <text x="25" y="118" font-size="9.5" fill="#94a3b8">HTTP, HTTPS, DNS, DHCP, SMTP, FTP, SSH</text>

    <!-- 3: Transport Layer -->
    <rect x="0" y="148" width="365" height="60" rx="8" fill="#0f172a" stroke="#3b82f6" stroke-width="2"/>
    <text x="15" y="172" font-size="13" font-weight="bold" fill="#60a5fa">3. Transport Layer</text>
    <text x="15" y="193" font-size="10" fill="#cbd5e1">Protocols: <tspan fill="#38bdf8" font-weight="bold">TCP</tspan> (Reliable) | <tspan fill="#f59e0b" font-weight="bold">UDP</tspan> (Fast Streaming)</text>

    <!-- 2: Internet Layer -->
    <rect x="0" y="218" width="365" height="55" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <text x="15" y="240" font-size="13" font-weight="bold" fill="#34d399">2. Internet Layer</text>
    <text x="15" y="258" font-size="10" fill="#cbd5e1">Protocols: <tspan fill="#34d399" font-weight="bold">IPv4, IPv6, ICMP, ARP, IPsec</tspan></text>

    <!-- 1: Network Access Layer -->
    <rect x="0" y="283" width="365" height="70" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <text x="15" y="305" font-size="13" font-weight="bold" fill="#fbbf24">1. Network Access (Link) Layer</text>
    <text x="15" y="323" font-size="10" fill="#cbd5e1">Physical medium + Data link framing hardware.</text>
    <text x="15" y="340" font-size="9.5" fill="#94a3b8">Technologies: Ethernet (802.3), Wi-Fi (802.11), Fiber</text>
  </g>

  <!-- Bottom PDU Progression Legend -->
  <g transform="translate(50, 460)">
    <rect width="860" height="35" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="20" y="22" font-size="11" font-weight="bold" fill="#38bdf8">Encapsulation PDU Flow:</text>
    <text x="190" y="22" font-size="10.5" fill="#e2e8f0">Data (App) <tspan fill="#60a5fa">➔ Segment (TCP)</tspan> <tspan fill="#34d399">➔ Packet (IP)</tspan> <tspan fill="#fbbf24">➔ Frame (MAC)</tspan> <tspan fill="#f87171">➔ Bits (Physical Wire)</tspan></text>
  </g>
</svg>
""")

SVG_COMMUNICATION_COMPONENTS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 5 Essential Components of a Data Communication System</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Interactive Hardware, Transmission Media, and Protocol Governance Model</text>

  <!-- Top Protocol Bar -->
  <g transform="translate(60, 95)">
    <rect width="840" height="60" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <text x="420" y="28" font-size="14" font-weight="bold" fill="#c084fc" text-anchor="middle">5. PROTOCOL (Agreed Rules &amp; Standards)</text>
    <text x="420" y="48" font-size="11" fill="#cbd5e1" text-anchor="middle">Governs data format, encoding, transmission rate, error detection (checksums), and acknowledgments</text>
  </g>

  <!-- Protocol Influence Arrows -->
  <g transform="translate(180, 155)" stroke="#a855f7" stroke-width="2" stroke-dasharray="4">
    <line x1="0" y1="0" x2="0" y2="40"/>
    <polygon points="-4,40 4,40 0,47" fill="#a855f7"/>
  </g>
  <g transform="translate(780, 155)" stroke="#a855f7" stroke-width="2" stroke-dasharray="4">
    <line x1="0" y1="0" x2="0" y2="40"/>
    <polygon points="-4,40 4,40 0,47" fill="#a855f7"/>
  </g>

  <!-- Sender Node (Left) -->
  <g transform="translate(60, 205)">
    <rect width="240" height="150" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="2"/>
    <rect x="15" y="15" width="210" height="28" rx="6" fill="#0284c7"/>
    <text x="120" y="34" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1. SENDER (Source)</text>
    <text x="15" y="65" font-size="10.5" font-weight="bold" fill="#38bdf8">• Role:</text>
    <text x="15" y="80" font-size="9.5" fill="#cbd5e1">Encodes and originates data</text>
    <text x="15" y="105" font-size="10.5" font-weight="bold" fill="#38bdf8">• Hardware:</text>
    <text x="15" y="120" font-size="9.5" fill="#94a3b8">PC, Smartphone, Camera, IoT Sensor</text>
  </g>

  <!-- Message Box (Center Middle) -->
  <g transform="translate(360, 205)">
    <rect width="240" height="150" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <rect x="15" y="15" width="210" height="28" rx="6" fill="#059669"/>
    <text x="120" y="34" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2. MESSAGE (Data Payload)</text>
    <text x="15" y="65" font-size="10.5" font-weight="bold" fill="#34d399">• Structure:</text>
    <text x="15" y="80" font-size="9.5" fill="#cbd5e1">Header + Encapsulated Data + Trailer</text>
    <text x="15" y="105" font-size="10.5" font-weight="bold" fill="#34d399">• Forms:</text>
    <text x="15" y="120" font-size="9.5" fill="#94a3b8">Text, Audio, Video, Binary Database Rows</text>
  </g>

  <!-- Receiver Node (Right) -->
  <g transform="translate(660, 205)">
    <rect width="240" height="150" rx="12" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect x="15" y="15" width="210" height="28" rx="6" fill="#d97706"/>
    <text x="120" y="34" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">4. RECEIVER (Sink/Dest)</text>
    <text x="15" y="65" font-size="10.5" font-weight="bold" fill="#fbbf24">• Role:</text>
    <text x="15" y="80" font-size="9.5" fill="#cbd5e1">Captures, decodes &amp; verifies data</text>
    <text x="15" y="105" font-size="10.5" font-weight="bold" fill="#fbbf24">• Hardware:</text>
    <text x="15" y="120" font-size="9.5" fill="#94a3b8">Server, Network Printer, Actuator</text>
  </g>

  <!-- Flow Arrows -->
  <g transform="translate(300, 280)">
    <line x1="0" y1="0" x2="55" y2="0" stroke="#38bdf8" stroke-width="3"/>
    <polygon points="55,-5 60,0 55,5" fill="#38bdf8"/>
  </g>
  <g transform="translate(600, 280)">
    <line x1="0" y1="0" x2="55" y2="0" stroke="#34d399" stroke-width="3"/>
    <polygon points="55,-5 60,0 55,5" fill="#34d399"/>
  </g>

  <!-- Bottom Medium Box -->
  <g transform="translate(60, 390)">
    <rect width="840" height="90" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="420" y="28" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">3. TRANSMISSION MEDIUM (Communication Channel / Physical Pathway)</text>
    <g transform="translate(30, 42)">
      <rect x="0" y="0" width="240" height="36" rx="5" fill="#1e293b"/>
      <text x="120" y="23" font-size="10" fill="#e2e8f0" text-anchor="middle">Guided: Copper Twisted-Pair (UTP)</text>
      
      <rect x="270" y="0" width="240" height="36" rx="5" fill="#1e293b"/>
      <text x="390" y="23" font-size="10" fill="#e2e8f0" text-anchor="middle">Guided: Fiber-Optic (Light Pulses)</text>
      
      <rect x="540" y="0" width="240" height="36" rx="5" fill="#1e293b"/>
      <text x="660" y="23" font-size="10" fill="#e2e8f0" text-anchor="middle">Unguided: Wireless (RF, Microwave)</text>
    </g>
  </g>
</svg>
""")

SVG_TRANSMISSION_MODES = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Data Transmission Modes: Simplex, Half-Duplex, and Full-Duplex</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Directionality, Physical Highway Analogies, and Collision Vulnerabilities</text>

  <!-- 1. Simplex Mode -->
  <g transform="translate(50, 95)">
    <rect width="860" height="110" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect x="15" y="12" width="160" height="24" rx="4" fill="#0284c7"/>
    <text x="95" y="28" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1. SIMPLEX MODE</text>
    <text x="15" y="55" font-size="10" font-weight="bold" fill="#38bdf8">One-Way Only (Uni-directional)</text>
    <text x="15" y="72" font-size="9" fill="#94a3b8">Analogy: One-way street</text>
    <text x="15" y="88" font-size="9" fill="#cbd5e1">Examples: TV Broadcast, Keyboard to CPU</text>

    <!-- Visual Pipeline -->
    <g transform="translate(230, 25)">
      <!-- Sender -->
      <rect x="0" y="10" width="110" height="45" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="55" y="36" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Transmitter</text>
      <!-- Arrow -->
      <line x1="120" y1="32" x2="490" y2="32" stroke="#38bdf8" stroke-width="4"/>
      <polygon points="490,26 505,32 490,38" fill="#38bdf8"/>
      <text x="310" y="22" font-size="10" fill="#38bdf8" font-weight="bold" text-anchor="middle">Data Stream ➔➔➔ (100% Bandwidth)</text>
      <!-- Receiver -->
      <rect x="515" y="10" width="105" height="45" rx="6" fill="#1e293b" stroke="#64748b"/>
      <text x="567" y="36" font-size="10.5" font-weight="bold" fill="#94a3b8" text-anchor="middle">Receiver</text>
    </g>
  </g>

  <!-- 2. Half-Duplex Mode -->
  <g transform="translate(50, 220)">
    <rect width="860" height="125" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="15" y="12" width="160" height="24" rx="4" fill="#d97706"/>
    <text x="95" y="28" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2. HALF-DUPLEX MODE</text>
    <text x="15" y="55" font-size="10" font-weight="bold" fill="#fbbf24">Alternating Both Ways</text>
    <text x="15" y="72" font-size="9" fill="#94a3b8">Analogy: Single-lane narrow bridge</text>
    <text x="15" y="88" font-size="9" fill="#cbd5e1">Examples: Walkie-Talkies (PTT), Legacy Hubs</text>
    <text x="15" y="104" font-size="9" fill="#ef4444">Risk: Collisions if sending simultaneously</text>

    <!-- Visual Pipeline -->
    <g transform="translate(230, 20)">
      <!-- Station A -->
      <rect x="0" y="18" width="110" height="48" rx="6" fill="#1e293b" stroke="#f59e0b"/>
      <text x="55" y="46" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">Transceiver A</text>
      <!-- Direction Arrows -->
      <line x1="120" y1="30" x2="490" y2="30" stroke="#fbbf24" stroke-width="2.5"/>
      <polygon points="490,26 500,30 490,34" fill="#fbbf24"/>
      <text x="310" y="22" font-size="9" fill="#fbbf24" text-anchor="middle">Time Slot 1: A ➔ B (Transmit)</text>

      <line x1="490" y1="55" x2="120" y2="55" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="4"/>
      <polygon points="120,51 110,55 120,59" fill="#fbbf24"/>
      <text x="310" y="70" font-size="9" fill="#fbbf24" text-anchor="middle">Time Slot 2: B ➔ A (Receive)</text>

      <!-- Station B -->
      <rect x="515" y="18" width="105" height="48" rx="6" fill="#1e293b" stroke="#f59e0b"/>
      <text x="567" y="46" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">Transceiver B</text>
    </g>
  </g>

  <!-- 3. Full-Duplex Mode -->
  <g transform="translate(50, 360)">
    <rect width="860" height="125" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect x="15" y="12" width="160" height="24" rx="4" fill="#059669"/>
    <text x="95" y="28" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">3. FULL-DUPLEX MODE</text>
    <text x="15" y="55" font-size="10" font-weight="bold" fill="#34d399">Simultaneous Both Ways</text>
    <text x="15" y="72" font-size="9" fill="#94a3b8">Analogy: Two-lane dual carriageway</text>
    <text x="15" y="88" font-size="9" fill="#cbd5e1">Examples: Mobile Phones, Switched Ethernet</text>
    <text x="15" y="104" font-size="9" fill="#34d399">Advantage: Zero wait time &amp; No collisions</text>

    <!-- Visual Pipeline -->
    <g transform="translate(230, 20)">
      <!-- Station A -->
      <rect x="0" y="18" width="110" height="48" rx="6" fill="#1e293b" stroke="#10b981"/>
      <text x="55" y="46" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">Switch Port A</text>
      
      <!-- Dedicated Tx Line -->
      <line x1="120" y1="30" x2="490" y2="30" stroke="#34d399" stroke-width="3"/>
      <polygon points="490,26 502,30 490,34" fill="#34d399"/>
      <text x="310" y="22" font-size="9.5" font-weight="bold" fill="#34d399" text-anchor="middle">Dedicated Tx Line (A ➔ B) [Concurrent]</text>

      <!-- Dedicated Rx Line -->
      <line x1="490" y1="58" x2="120" y2="58" stroke="#38bdf8" stroke-width="3"/>
      <polygon points="120,54 108,58 120,62" fill="#38bdf8"/>
      <text x="310" y="74" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Dedicated Rx Line (B ➔ A) [Concurrent]</text>

      <!-- Station B -->
      <rect x="515" y="18" width="105" height="48" rx="6" fill="#1e293b" stroke="#10b981"/>
      <text x="567" y="46" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">Switch Port B</text>
    </g>
  </g>
</svg>
""")

SVG_NETWORK_METRICS_DIAGNOSTICS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Network Performance Metrics &amp; Systematic Troubleshooting Pipeline</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Evaluating Delivery, Accuracy, Jitter, Throughput &amp; Executing 4-Step Diagnosis</text>

  <!-- Left: 5 Performance Metrics -->
  <g transform="translate(45, 95)">
    <rect width="415" height="385" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect x="15" y="15" width="385" height="28" rx="5" fill="#0284c7"/>
    <text x="207" y="34" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">5 CRITICAL PERFORMANCE METRICS</text>
    
    <!-- 1: Delivery -->
    <g transform="translate(15, 55)">
      <rect width="385" height="52" rx="6" fill="#1e293b"/>
      <text x="12" y="18" font-size="10.5" font-weight="bold" fill="#38bdf8">1. Delivery:</text>
      <text x="12" y="35" font-size="9" fill="#cbd5e1">Data must reach the exact authorized destination only.</text>
    </g>

    <!-- 2: Accuracy -->
    <g transform="translate(15, 115)">
      <rect width="385" height="52" rx="6" fill="#1e293b"/>
      <text x="12" y="18" font-size="10.5" font-weight="bold" fill="#34d399">2. Accuracy:</text>
      <text x="12" y="35" font-size="9" fill="#cbd5e1">Bit-perfect fidelity; checksums detect and correct bit-flips.</text>
    </g>

    <!-- 3: Timeliness -->
    <g transform="translate(15, 175)">
      <rect width="385" height="52" rx="6" fill="#1e293b"/>
      <text x="12" y="18" font-size="10.5" font-weight="bold" fill="#fbbf24">3. Timeliness (Latency):</text>
      <text x="12" y="35" font-size="9" fill="#cbd5e1">Data arrives in time. Late VoIP packets are dropped.</text>
    </g>

    <!-- 4: Jitter -->
    <g transform="translate(15, 235)">
      <rect width="385" height="60" rx="6" fill="#1e293b"/>
      <text x="12" y="18" font-size="10.5" font-weight="bold" fill="#ec4899">4. Jitter (Packet Delay Variation):</text>
      <text x="12" y="35" font-size="9" fill="#cbd5e1">Uneven arrival intervals cause video stutter and audio crackle.</text>
      <text x="12" y="49" font-size="8.5" fill="#f472b6">Requires playout buffering to smooth rendering.</text>
    </g>

    <!-- 5: Throughput vs Bandwidth -->
    <g transform="translate(15, 305)">
      <rect width="385" height="60" rx="6" fill="#1e293b"/>
      <text x="12" y="18" font-size="10.5" font-weight="bold" fill="#a855f7">5. Throughput vs. Bandwidth:</text>
      <text x="12" y="35" font-size="9" fill="#cbd5e1">Bandwidth = theoretical pipe width (e.g. 1 Gbps).</text>
      <text x="12" y="49" font-size="8.5" fill="#c084fc">Throughput = actual measured payload delivery rate.</text>
    </g>
  </g>

  <!-- Right: 4-Step Troubleshooting Sequence -->
  <g transform="translate(495, 95)">
    <rect width="420" height="385" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect x="15" y="15" width="390" height="28" rx="5" fill="#059669"/>
    <text x="210" y="34" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">COMMUNICATION DIAGNOSIS SEQUENCE</text>

    <!-- Step 1 -->
    <g transform="translate(15, 55)">
      <rect width="390" height="65" rx="6" fill="#1e293b" stroke="#334155"/>
      <rect x="10" y="10" width="60" height="20" rx="4" fill="#0284c7"/>
      <text x="40" y="24" font-size="9.5" font-weight="bold" fill="#ffffff" text-anchor="middle">STEP 1</text>
      <text x="80" y="25" font-size="11" font-weight="bold" fill="#38bdf8">Check Sender Local Stack</text>
      <text x="12" y="45" font-size="9.5" fill="#cbd5e1">Action: CLI command <tspan font-family="monospace" fill="#38bdf8">ping 127.0.0.1</tspan></text>
      <text x="12" y="58" font-size="8.5" fill="#94a3b8">Validates local TCP/IP stack &amp; Network Interface Card (NIC).</text>
    </g>

    <!-- Step 2 -->
    <g transform="translate(15, 130)">
      <rect width="390" height="65" rx="6" fill="#1e293b" stroke="#334155"/>
      <rect x="10" y="10" width="60" height="20" rx="4" fill="#d97706"/>
      <text x="40" y="24" font-size="9.5" font-weight="bold" fill="#ffffff" text-anchor="middle">STEP 2</text>
      <text x="80" y="25" font-size="11" font-weight="bold" fill="#fbbf24">Inspect Transmission Medium</text>
      <text x="12" y="45" font-size="9.5" fill="#cbd5e1">Action: Check Ethernet link lights / Wi-Fi RSSI signal.</text>
      <text x="12" y="58" font-size="8.5" fill="#94a3b8">Detects severed cables, unplugged ports, or RF interference.</text>
    </g>

    <!-- Step 3 -->
    <g transform="translate(15, 205)">
      <rect width="390" height="65" rx="6" fill="#1e293b" stroke="#334155"/>
      <rect x="10" y="10" width="60" height="20" rx="4" fill="#059669"/>
      <text x="40" y="24" font-size="9.5" font-weight="bold" fill="#ffffff" text-anchor="middle">STEP 3</text>
      <text x="80" y="25" font-size="11" font-weight="bold" fill="#34d399">Verify Protocol &amp; Gateway</text>
      <text x="12" y="45" font-size="9.5" fill="#cbd5e1">Action: Run <tspan font-family="monospace" fill="#34d399">ping [Default_Gateway_IP]</tspan></text>
      <text x="12" y="58" font-size="8.5" fill="#94a3b8">Verifies DHCP lease, Subnet Mask, and Router gateway.</text>
    </g>

    <!-- Step 4 -->
    <g transform="translate(15, 280)">
      <rect width="390" height="85" rx="6" fill="#1e293b" stroke="#334155"/>
      <rect x="10" y="10" width="60" height="20" rx="4" fill="#7c3aed"/>
      <text x="40" y="24" font-size="9.5" font-weight="bold" fill="#ffffff" text-anchor="middle">STEP 4</text>
      <text x="80" y="25" font-size="11" font-weight="bold" fill="#c084fc">Test End-to-End Receiver &amp; DNS</text>
      <text x="12" y="45" font-size="9.5" fill="#cbd5e1">Action: Run <tspan font-family="monospace" fill="#c084fc">ping 8.8.8.8</tspan> then <tspan font-family="monospace" fill="#c084fc">ping kcse.gov.ke</tspan></text>
      <text x="12" y="60" font-size="8.5" fill="#94a3b8">If IP succeeds but domain fails ➔ DNS server issue.</text>
      <text x="12" y="74" font-size="8.5" fill="#94a3b8">If both fail ➔ WAN / ISP upstream link failure.</text>
    </g>
  </g>
</svg>
""")

SVG_EVOLUTION_TIMELINE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Historical Evolution of Data Communication Infrastructure</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">From 19th Century Telegraphy to Modern 5G Cellular and Edge IoT Networks</text>

  <!-- Horizontal Timeline Bar -->
  <line x1="60" y1="120" x2="900" y2="120" stroke="#38bdf8" stroke-width="4"/>

  <!-- Milestone 1: 1840s Telegraph -->
  <g transform="translate(60, 90)">
    <circle cx="20" cy="30" r="10" fill="#f59e0b" stroke="#ffffff" stroke-width="2"/>
    <rect x="-10" y="45" width="160" height="150" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="70" y="68" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">1840s – 1950s</text>
    <text x="70" y="86" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Telegraph &amp; Telephony</text>
    <text x="0" y="108" font-size="8.5" fill="#cbd5e1">• Morse code pulses</text>
    <text x="0" y="124" font-size="8.5" fill="#cbd5e1">• Copper wire circuits</text>
    <text x="0" y="140" font-size="8.5" fill="#cbd5e1">• Point-to-point analog sound</text>
    <text x="0" y="165" font-size="8" fill="#94a3b8">Birth of electrical telecommunications</text>
  </g>

  <!-- Milestone 2: 1960s Modems -->
  <g transform="translate(240, 90)">
    <circle cx="20" cy="30" r="10" fill="#0ea5e9" stroke="#ffffff" stroke-width="2"/>
    <rect x="-10" y="45" width="160" height="150" rx="8" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <text x="70" y="68" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">1960s – 1980s</text>
    <text x="70" y="86" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Modems &amp; Analog Lines</text>
    <text x="0" y="108" font-size="8.5" fill="#cbd5e1">• Digital to Audio modulation</text>
    <text x="0" y="124" font-size="8.5" fill="#cbd5e1">• Mainframe terminal links</text>
    <text x="0" y="140" font-size="8.5" fill="#cbd5e1">• Speeds: 300 bps – 56 kbps</text>
    <text x="0" y="165" font-size="8" fill="#94a3b8">Bridges digital computers over telephone grid</text>
  </g>

  <!-- Milestone 3: 1980s LAN & Ethernet -->
  <g transform="translate(420, 90)">
    <circle cx="20" cy="30" r="10" fill="#10b981" stroke="#ffffff" stroke-width="2"/>
    <rect x="-10" y="45" width="160" height="150" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <text x="70" y="68" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">1980s – 1990s</text>
    <text x="70" y="86" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">LANs &amp; Ethernet</text>
    <text x="0" y="108" font-size="8.5" fill="#cbd5e1">• Coaxial &amp; Twisted-pair</text>
    <text x="0" y="124" font-size="8.5" fill="#cbd5e1">• Pure digital packet frames</text>
    <text x="0" y="140" font-size="8.5" fill="#cbd5e1">• Speeds: 10 Mbps – 100 Mbps</text>
    <text x="0" y="165" font-size="8" fill="#94a3b8">Local office workstation interconnection</text>
  </g>

  <!-- Milestone 4: 1990s Internet & Fiber -->
  <g transform="translate(600, 90)">
    <circle cx="20" cy="30" r="10" fill="#8b5cf6" stroke="#ffffff" stroke-width="2"/>
    <rect x="-10" y="45" width="160" height="150" rx="8" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.5"/>
    <text x="70" y="68" font-size="11" font-weight="bold" fill="#a78bfa" text-anchor="middle">1990s – 2010s</text>
    <text x="70" y="86" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">TCP/IP &amp; Optical Fiber</text>
    <text x="0" y="108" font-size="8.5" fill="#cbd5e1">• Global TCP/IP routing</text>
    <text x="0" y="124" font-size="8.5" fill="#cbd5e1">• Undersea fiber cables</text>
    <text x="0" y="140" font-size="8.5" fill="#cbd5e1">• Speeds: 100 Mbps – 10 Gbps</text>
    <text x="0" y="165" font-size="8" fill="#94a3b8">Birth of the World Wide Web &amp; Broadband</text>
  </g>

  <!-- Milestone 5: Present 5G & IoT -->
  <g transform="translate(775, 90)">
    <circle cx="20" cy="30" r="10" fill="#ec4899" stroke="#ffffff" stroke-width="2"/>
    <rect x="-10" y="45" width="160" height="150" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <text x="70" y="68" font-size="11" font-weight="bold" fill="#f472b6" text-anchor="middle">Present Day</text>
    <text x="70" y="86" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">5G, Satellite &amp; IoT</text>
    <text x="0" y="108" font-size="8.5" fill="#cbd5e1">• Millimeter wave 5G</text>
    <text x="0" y="124" font-size="8.5" fill="#cbd5e1">• Low-Earth Orbit satellites</text>
    <text x="0" y="140" font-size="8.5" fill="#cbd5e1">• Ultra-low latency edge IoT</text>
    <text x="0" y="165" font-size="8" fill="#94a3b8">Billions of interconnected autonomous devices</text>
  </g>

  <!-- Bottom Core Takeaway Box -->
  <g transform="translate(50, 375)">
    <rect width="860" height="110" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="430" y="28" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">TRANSFORMATION PARADIGM: ANALOG SOUND TONES TO OPTICAL PHOTONS AND RF PACKETS</text>
    <text x="30" y="55" font-size="10" fill="#cbd5e1">1. Early Phase: Adapted digital binary data to fit existing analog infrastructure (Voice audio modulation via Modems).</text>
    <text x="30" y="75" font-size="10" fill="#cbd5e1">2. Intermediate Phase: Built dedicated pure digital copper networks (Ethernet switches, Structured Cat6 Cabling).</text>
    <text x="30" y="95" font-size="10" fill="#cbd5e1">3. Modern Phase: Pure light pulses (Fiber Optics) and high-density beamformed radio spectrum (5G/Wi-Fi 7) transporting trillions of packets.</text>
  </g>
</svg>
""")

SVG_SERIAL_PARALLEL_AND_TIMING = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Data Transmission Techniques: Serial vs. Parallel &amp; Synchronization Framing</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Comparing Single-Lane Sequential Streams with Multi-Wire Buses, and Asynchronous Start/Stop Framing</text>

  <!-- Left: Serial vs Parallel Transmission -->
  <g transform="translate(45, 90)">
    <rect width="415" height="390" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect x="15" y="15" width="385" height="30" rx="6" fill="#0284c7"/>
    <text x="207" y="35" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">SERIAL vs. PARALLEL TRANSMISSION</text>
    
    <!-- Serial Subsection -->
    <g transform="translate(20, 58)">
      <text x="0" y="16" font-size="11.5" font-weight="bold" fill="#38bdf8">1. Serial (Single Wire Bitstream)</text>
      <rect x="0" y="24" width="375" height="50" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <text x="30" y="52" font-size="11" font-weight="bold" fill="#38bdf8">Tx</text>
      <line x1="55" y1="48" x2="310" y2="48" stroke="#38bdf8" stroke-width="2"/>
      <polygon points="310,44 320,48 310,52" fill="#38bdf8"/>
      <circle cx="90" cy="48" r="9" fill="#0284c7"/><text x="90" y="52" font-size="9" fill="#fff" text-anchor="middle">1</text>
      <circle cx="130" cy="48" r="9" fill="#0284c7"/><text x="130" y="52" font-size="9" fill="#fff" text-anchor="middle">0</text>
      <circle cx="170" cy="48" r="9" fill="#0284c7"/><text x="170" y="52" font-size="9" fill="#fff" text-anchor="middle">1</text>
      <circle cx="210" cy="48" r="9" fill="#0284c7"/><text x="210" y="52" font-size="9" fill="#fff" text-anchor="middle">1</text>
      <circle cx="250" cy="48" r="9" fill="#0284c7"/><text x="250" y="52" font-size="9" fill="#fff" text-anchor="middle">0</text>
      <text x="345" y="52" font-size="11" font-weight="bold" fill="#38bdf8">Rx</text>
      <text x="5" y="90" font-size="9.5" fill="#cbd5e1">&#8226; 1 bit at a time. Ideal for long distance (USB, PCIe, Ethernet).</text>
    </g>

    <!-- Parallel Subsection -->
    <g transform="translate(20, 175)">
      <text x="0" y="16" font-size="11.5" font-weight="bold" fill="#34d399">2. Parallel (Multi-Conductor Bus)</text>
      <rect x="0" y="24" width="375" height="110" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
      <text x="20" y="80" font-size="11" font-weight="bold" fill="#34d399">Tx</text>
      <line x1="45" y1="42" x2="320" y2="42" stroke="#34d399" stroke-width="1.5"/>
      <line x1="45" y1="62" x2="320" y2="62" stroke="#34d399" stroke-width="1.5"/>
      <line x1="45" y1="82" x2="320" y2="82" stroke="#34d399" stroke-width="1.5"/>
      <line x1="45" y1="102" x2="320" y2="102" stroke="#34d399" stroke-width="1.5"/>
      <text x="180" y="38" font-size="8.5" fill="#a7f3d0" text-anchor="middle">Bit 0 (1)</text>
      <text x="180" y="58" font-size="8.5" fill="#a7f3d0" text-anchor="middle">Bit 1 (0)</text>
      <text x="180" y="78" font-size="8.5" fill="#a7f3d0" text-anchor="middle">Bit 2 (1)</text>
      <text x="180" y="98" font-size="8.5" fill="#a7f3d0" text-anchor="middle">Bit 3 (1)</text>
      <text x="345" y="80" font-size="11" font-weight="bold" fill="#34d399">Rx</text>
      <text x="5" y="152" font-size="9.5" fill="#cbd5e1">&#8226; Transmits 1 byte concurrently. Suffers from clock skew over distance.</text>
    </g>
  </g>

  <!-- Right: Asynchronous vs Synchronous Framing -->
  <g transform="translate(500, 90)">
    <rect width="415" height="390" rx="12" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="15" y="15" width="385" height="30" rx="6" fill="#7e22ce"/>
    <text x="207" y="35" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">SYNCHRONIZATION &amp; FRAMING MECHANICS</text>
    
    <!-- Asynchronous Frame -->
    <g transform="translate(20, 60)">
      <text x="0" y="16" font-size="11.5" font-weight="bold" fill="#c084fc">Asynchronous Framing (Start/Stop Bits)</text>
      <g transform="translate(0, 26)">
        <rect x="0" y="0" width="55" height="42" rx="4" fill="#ef4444" stroke="#f87171"/>
        <text x="27" y="20" font-size="8.5" font-weight="bold" fill="#fff" text-anchor="middle">Start Bit</text>
        <text x="27" y="34" font-size="10" font-weight="bold" fill="#fff" text-anchor="middle">(0)</text>

        <rect x="60" y="0" width="180" height="42" rx="4" fill="#3b82f6" stroke="#60a5fa"/>
        <text x="150" y="20" font-size="9.5" font-weight="bold" fill="#fff" text-anchor="middle">7/8 Data Payload Bits</text>
        <text x="150" y="34" font-size="8.5" fill="#cbd5e1" text-anchor="middle">e.g. ASCII Character 'K'</text>

        <rect x="245" y="0" width="60" height="42" rx="4" fill="#f59e0b" stroke="#fbbf24"/>
        <text x="275" y="20" font-size="8" font-weight="bold" fill="#fff" text-anchor="middle">Parity</text>
        <text x="275" y="34" font-size="8.5" fill="#fff" text-anchor="middle">Odd/Even</text>

        <rect x="310" y="0" width="65" height="42" rx="4" fill="#10b981" stroke="#34d399"/>
        <text x="342" y="20" font-size="8.5" font-weight="bold" fill="#fff" text-anchor="middle">Stop Bit</text>
        <text x="342" y="34" font-size="10" font-weight="bold" fill="#fff" text-anchor="middle">(1)</text>
      </g>
      <text x="5" y="85" font-size="9.5" fill="#cbd5e1">&#8226; No shared clock; relies on Start/Stop bits for byte boundary detection.</text>
    </g>

    <!-- Synchronous Frame -->
    <g transform="translate(20, 185)">
      <text x="0" y="16" font-size="11.5" font-weight="bold" fill="#38bdf8">Synchronous Block Framing (Common Clock)</text>
      <g transform="translate(0, 26)">
        <rect x="0" y="0" width="70" height="42" rx="4" fill="#0284c7" stroke="#38bdf8"/>
        <text x="35" y="20" font-size="8.5" font-weight="bold" fill="#fff" text-anchor="middle">Preamble /</text>
        <text x="35" y="34" font-size="8.5" font-weight="bold" fill="#fff" text-anchor="middle">SYN bytes</text>

        <rect x="75" y="0" width="220" height="42" rx="4" fill="#1e293b" stroke="#38bdf8"/>
        <text x="185" y="20" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Continuous Data Block / Frame</text>
        <text x="185" y="34" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Hundreds to Thousands of Bytes</text>

        <rect x="300" y="0" width="75" height="42" rx="4" fill="#059669" stroke="#34d399"/>
        <text x="337" y="20" font-size="8.5" font-weight="bold" fill="#fff" text-anchor="middle">CRC</text>
        <text x="337" y="34" font-size="8.5" font-weight="bold" fill="#fff" text-anchor="middle">Checksum</text>
      </g>
      <text x="5" y="85" font-size="9.5" fill="#cbd5e1">&#8226; Locked clock signal; minimal overhead, maximum throughput (Ethernet/WAN).</text>
    </g>
  </g>
</svg>
""")

SVG_MODERN_GLOBAL_DATA_INFRASTRUCTURE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Modern Global Data Communication Architecture</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Integrated ecosystem: Subsea optical backbones, Cloud Hyperscalers, 5G Cellular, and Satellite Constellations</text>

  <!-- Top: Space Layer (Satellites) -->
  <g transform="translate(60, 95)">
    <rect width="840" height="70" rx="10" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
    <text x="420" y="24" font-size="12.5" font-weight="bold" fill="#f472b6" text-anchor="middle">SPACE LAYER: LEO &amp; GEO SATELLITE CONSTELLATIONS</text>
    <text x="420" y="45" font-size="10" fill="#cbd5e1" text-anchor="middle">Starlink &amp; O3b mPOWER Constellations • Ku/Ka Band High-Throughput Beams • Remote Rural &amp; Maritime Uplinks</text>
  </g>

  <!-- Middle Tier: Terrestrial & Cloud Core -->
  <g transform="translate(60, 180)">
    <!-- Subsea & Terrestrial Core -->
    <g transform="translate(0, 0)">
      <rect width="405" height="180" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
      <rect width="405" height="28" rx="6" fill="#0284c7"/>
      <text x="202" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">GLOBAL CORE: SUBSEA FIBER BACKBONE</text>
      <text x="15" y="52" font-size="10" font-weight="bold" fill="#38bdf8">&#8226; Undersea Cables:</text>
      <text x="135" y="52" font-size="9.5" fill="#cbd5e1">TEAMS, SEACOM, 2Africa (Mombasa landing)</text>
      <text x="15" y="76" font-size="10" font-weight="bold" fill="#38bdf8">&#8226; DWDM Optical Channels:</text>
      <text x="165" y="76" font-size="9.5" fill="#cbd5e1">100+ Tbps multi-wavelength lasers</text>
      <text x="15" y="100" font-size="10" font-weight="bold" fill="#38bdf8">&#8226; Tier 1 Transit Routing:</text>
      <text x="155" y="100" font-size="9.5" fill="#cbd5e1">BGP autonomous system interconnections</text>
      <text x="15" y="124" font-size="10" font-weight="bold" fill="#38bdf8">&#8226; National Backbones:</text>
      <text x="145" y="124" font-size="9.5" fill="#cbd5e1">NOFBI (National Optic Fibre Backbone)</text>
      <text x="15" y="152" font-size="8.5" fill="#94a3b8">Carries 99% of international data packets across oceans</text>
    </g>

    <!-- Cloud Hyperscalers & Edge CDNs -->
    <g transform="translate(435, 0)">
      <rect width="405" height="180" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
      <rect width="405" height="28" rx="6" fill="#059669"/>
      <text x="202" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">CLOUD HYPERSCALERS &amp; EDGE CDNs</text>
      <text x="15" y="52" font-size="10" font-weight="bold" fill="#34d399">&#8226; Hyperscale Data Centers:</text>
      <text x="170" y="52" font-size="9.5" fill="#cbd5e1">Server clusters (AWS, Azure, Google Cloud)</text>
      <text x="15" y="76" font-size="10" font-weight="bold" fill="#34d399">&#8226; Edge Content Delivery (CDN):</text>
      <text x="185" y="76" font-size="9.5" fill="#cbd5e1">Cached media nodes at local IXPs (KIXP)</text>
      <text x="15" y="100" font-size="10" font-weight="bold" fill="#34d399">&#8226; Sub-10ms Local Latency:</text>
      <text x="170" y="100" font-size="9.5" fill="#cbd5e1">Caches streaming video, DNS &amp; websites</text>
      <text x="15" y="124" font-size="10" font-weight="bold" fill="#34d399">&#8226; Distributed Storage:</text>
      <text x="145" y="124" font-size="9.5" fill="#cbd5e1">Multi-region database synchronization</text>
      <text x="15" y="152" font-size="8.5" fill="#94a3b8">Brings compute and video content close to end users</text>
    </g>
  </g>

  <!-- Bottom Tier: Access Networks & End Devices -->
  <g transform="translate(60, 375)">
    <rect width="840" height="115" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="840" height="26" rx="6" fill="#7e22ce"/>
    <text x="420" y="18" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">LAST-MILE ACCESS NETWORKS &amp; SMART CLIENT ENDPOINTS</text>
    
    <g transform="translate(20, 38)">
      <rect width="250" height="65" rx="6" fill="#1e293b"/>
      <text x="125" y="20" font-size="10.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">4G / 5G Cellular Towers</text>
      <text x="125" y="38" font-size="9" fill="#cbd5e1" text-anchor="middle">MIMO antennas • Beamforming</text>
      <text x="125" y="52" font-size="8.5" fill="#94a3b8" text-anchor="middle">Smartphones • Mobile Routers</text>
    </g>
    <g transform="translate(295, 38)">
      <rect width="250" height="65" rx="6" fill="#1e293b"/>
      <text x="125" y="20" font-size="10.5" font-weight="bold" fill="#34d399" text-anchor="middle">Fiber to the Home / Building (FTTH)</text>
      <text x="125" y="38" font-size="9" fill="#cbd5e1" text-anchor="middle">GPON Optical Line Terminals (OLT)</text>
      <text x="125" y="52" font-size="8.5" fill="#94a3b8" text-anchor="middle">Gigabit Home Wi-Fi 6 Routers</text>
    </g>
    <g transform="translate(570, 38)">
      <rect width="250" height="65" rx="6" fill="#1e293b"/>
      <text x="125" y="20" font-size="10.5" font-weight="bold" fill="#f472b6" text-anchor="middle">IoT &amp; Industrial Endpoints</text>
      <text x="125" y="38" font-size="9" fill="#cbd5e1" text-anchor="middle">Telemetry sensors • Smart Meters</text>
      <text x="125" y="52" font-size="8.5" fill="#94a3b8" text-anchor="middle">Automated Agricultural Drones</text>
    </g>
  </g>
</svg>
""")

# =====================================================================
# DATA STRUCTURE FOR TOPIC 8 INGESTION
# =====================================================================

TOPIC_DATA = {
    "topic_order": 8,
    "topic_name": "Data Communication",
    "learning_units": [
        # -------------------------------------------------------------
        # UNIT 1: Basic Data Communication Concepts & Layered Models
        # -------------------------------------------------------------
        {
            "unit_order": 1,
            "unit_name": "Fundamentals of Data Communication and Layered Protocol Architectures",
            "unit_description": "Foundational principles of digital transmission, analog versus digital waveforms, bit rate and baud rate calculations, and deep comparison of OSI 7-layer and TCP/IP 4-layer network models.",
            "lessons": [
                {
                    "lesson_order": 25,
                    "lesson_title": "Basic Data Communication Concepts and Layered Network Models",
                    "lesson_description": "Explore how data travels between computing systems, compare physical signals and bandwidth capacities, and master the OSI 7-layer and TCP/IP protocol suites.",
                    "pages": [
                        # Page 1: Introduction & Core Concepts
                        [
                            {
                                "block_type": "learning_goal",
                                "title": "Learning Goal: Principles of Data Communication & Layered Models",
                                "content": {
                                    "goal": "Understand the fundamental concepts of data communication, compare analog vs digital waveforms and bandwidth metrics, and analyze the OSI 7-layer and TCP/IP protocol suites."
                                }
                            },
                            {
                                "block_type": "concept_explanation",
                                "title": "Introduction to Data Communication: The Postal Service Analogy",
                                "content": {
                                    "body": """### The Digital Postal Service

Imagine writing a letter to a friend in another town. To get the message across successfully, several coordinated steps must occur:

1. **Message Encoding**: You write your message on paper using a common language representing **data** encoded into a standard human-readable format.
2. **Packet Encapsulation**: You place the paper into an envelope, write a specific destination address and return address, and seal it representing **packet encapsulation** with routing headers.
3. **Communication Channel**: You hand it to a postal courier who transports it in a truck along physical roads representing the **communication channel** or **medium** (copper, fiber, or wireless).
4. **Protocols & Routing**: The postal network sorts letters using zip codes and standard procedures representing **network protocols** and routing tables.

If you write the letter in an obscure language your friend cannot interpret, omit the address, or if the delivery truck breaks down, communication fails. 

In computer science, **data communication** is the digital postal service. It is the systematic transfer of digital data (binary bits) between two or more computing devices over a transmission channel governed by mutually agreed-upon rules known as **protocols**."""
                                }
                            },
                            {
                                "block_type": "concept_explanation",
                                "title": "Technical Core Definitions in Data Communication",
                                "content": {
                                    "body": """### Fundamental Terminology

To analyze network systems rigorously, computer scientists use precise definitions:

- **Data Communication**: The process of transferring digital data or information between two or more computing points across a physical or electromagnetic transmission medium.
- **Data**: Raw, unprocessed symbols, facts, numbers, text, or signals represented digitally inside computing hardware as binary bits (0s and 1s).
- **Signal**: An electrical voltage pulse, electromagnetic wave, or optical light burst used to propagate data through a communication channel.
- **Communication Channel**: The physical pathway or transmission medium (such as twisted-pair copper wire, optical fiber strand, or radio frequency band) over which data signals propagate.
- **Protocol**: A formal set of standardized rules, procedures, formats, and timing constraints governing how data is encapsulated, transmitted, routed, received, and acknowledged across a network.
- **Computer Network**: An interconnected collection of autonomous computing devices (servers, PCs, switches, routers, IoT devices) capable of exchanging data and sharing resources."""
                                }
                            }
                        ],

                        # Page 2: Analog vs Digital Signals, Rates & Bandwidth
                        [
                            {
                                "block_type": "suggested_diagram",
                                "title": "Analog vs. Digital Signal Waveforms",
                                "content": {
                                    "caption": "Comparing continuous analog sine waves with discrete binary square waves and voltage logic levels.",
                                    "svg_content": SVG_ANALOG_VS_DIGITAL
                                }
                            },
                            {
                                "block_type": "concept_explanation",
                                "title": "Signals, Data Rates, Baud Rates, and Bandwidth",
                                "content": {
                                    "body": """### 1. Analog vs. Digital Signals

While microprocessors process binary data internally, the physical universe transmits energy continuously.

- **Analog Signals**:
  - *Definition*: Continuous electromagnetic waveforms that vary smoothly in amplitude, frequency, or phase over time.
  - *Mathematical Form*: A continuous sine wave.
  - *Vulnerability*: Highly susceptible to electrical noise and attenuation over long distances. Amplifying an analog signal also amplifies the accumulated background noise.
  - *Examples*: Human voice acoustics, traditional AM/FM radio, analog landline telephone audio.

- **Digital Signals**:
  - *Definition*: Discrete, step-like signals that transition between a finite set of predetermined voltage levels (typically +5V or +3.3V for binary `1`, and 0V for binary `0`).
  - *Mathematical Form*: A square wave.
  - *Resilience*: High noise immunity. Digital repeaters clean and regenerate exact 1s and 0s, eliminating accumulated transmission distortion.
  - *Examples*: CPU internal buses, SATA/NVMe interfaces, Ethernet cable pulses, optical fiber light pulses.

---

### 2. Measuring Network Speed: Bit Rate, Baud Rate, and Bandwidth

- **Data Rate (Bit Rate)**:
  - The speed at which binary data bits are transmitted across a medium, measured in **bits per second (bps)**, **Megabits per second (Mbps)**, or **Gigabits per second (Gbps)**.
  - Formula: $\\text{Bit Rate} = \\text{Baud Rate} \\times \\text{Bits per Symbol}$.

- **Baud Rate (Symbol Rate)**:
  - The number of **signal state changes** (symbols) occurring on the transmission line per second.
  - In simple binary signaling where one voltage pulse represents 1 bit, $\\text{Bit Rate} = \\text{Baud Rate}$.
  - In advanced digital modulation (e.g., QAM-256), a single signal symbol shift in amplitude and phase can encode 8 bits simultaneously ($2^8 = 256$ states), making the Bit Rate $8\\times$ higher than the Baud Rate.

- **Bandwidth**:
  - *Engineering Definition*: The physical range of frequencies (measured in Hertz, Hz) that a transmission channel can pass without severe attenuation ($\\text{Bandwidth} = f_{\\text{high}} - f_{\\text{low}}$).
  - *Practical Networking Definition*: The maximum theoretical data throughput capacity of a network link (e.g., a 1 Gbps Ethernet connection). According to Shannon-Hartley and Nyquist theorems, a wider physical frequency bandwidth directly enables higher data rates."""
                                }
                            },
                            {
                                "block_type": "suggested_image",
                                "title": "Digital Signal Oscilloscope Trace",
                                "content": {
                                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Digital_signal_oscilloscope_trace.svg/1280px-Digital_signal_oscilloscope_trace.svg.png",
                                    "caption": "Oscilloscope capture showing discrete digital square pulses representing high (1) and low (0) voltage transitions.",
                                    "author": "Wikimedia Commons / Public Domain",
                                    "licensing": "CC BY-SA 3.0"
                                }
                            }
                        ],

                        # Page 3: Layered Network Models (OSI vs TCP/IP)
                        [
                            {
                                "block_type": "suggested_diagram",
                                "title": "Layered Architectures: OSI 7-Layer vs. TCP/IP 4-Layer Suite",
                                "content": {
                                    "caption": "Direct mapping between OSI 7-layer conceptual reference model and the practical TCP/IP 4-layer Internet suite.",
                                    "svg_content": SVG_OSI_VS_TCPIP
                                }
                            },
                            {
                                "block_type": "concept_explanation",
                                "title": "Deep Dive: OSI 7-Layer Reference Model vs. TCP/IP Suite",
                                "content": {
                                    "body": """### The OSI 7-Layer Reference Model

The **Open Systems Interconnection (OSI)** model is a conceptual 7-layer framework developed by ISO to standardize network communication into discrete, modular layers:

1. **Physical Layer (Layer 1)**:
   - *PDU*: **Bits**
   - *Function*: Transmits raw, unstructured bit streams over physical media (voltages, light pulses, radio frequencies). Defines pinouts, cable specs, and signal modulation.
   - *Hardware*: Ethernet cables (Cat6), repeaters, fiber transceivers, network hubs.

2. **Data Link Layer (Layer 2)**:
   - *PDU*: **Frames**
   - *Function*: Provides node-to-node transfer, physical **MAC addressing**, framing, and error detection via CRC checksums.
   - *Hardware/Protocols*: Network Interface Cards (NICs), Layer 2 Switches, Ethernet (IEEE 802.3), Wi-Fi (IEEE 802.11).

3. **Network Layer (Layer 3)**:
   - *PDU*: **Packets**
   - *Function*: Handles end-to-end logical addressing and path determination (**routing**) across multiple interconnected networks.
   - *Protocols*: **IP (IPv4/IPv6)**, ICMP (ping), OSPF, BGP, Routers.

4. **Transport Layer (Layer 4)**:
   - *PDU*: **Segments** (TCP) or **Datagrams** (UDP)
   - *Function*: Manages host-to-host process communication using **port numbers**. Provides reliability, segmentation, sequence ordering, flow control, and error recovery.
   - *Protocols*: **TCP** (connection-oriented, guaranteed delivery) and **UDP** (connectionless, high-speed streaming).

5. **Session Layer (Layer 5)**:
   - *Function*: Establishes, maintains, synchronizes, and terminates interactive sessions between client and server applications (e.g., RPC, NetBIOS).

6. **Presentation Layer (Layer 6)**:
   - *Function*: Handles data translation, character code conversion (ASCII/Unicode), data compression, and cryptographic encryption/decryption (TLS/SSL).

7. **Application Layer (Layer 7)**:
   - *Function*: Directly interfaces with end-user software applications to provide standard network services.
   - *Protocols*: **HTTP/HTTPS** (web), **DNS** (domain resolution), **SMTP/IMAP** (email), **SSH/FTP** (remote access & files).

---

### The TCP/IP 4-Layer Internet Suite

While OSI is the primary educational reference model, the modern Internet runs on the practical **TCP/IP model**, which condenses the 7 layers into 4:

| TCP/IP Layer | Corresponding OSI Layers | Core Protocols & Technologies |
| :--- | :--- | :--- |
| **4. Application** | Application (7), Presentation (6), Session (5) | HTTP, HTTPS, DNS, DHCP, SSH, SMTP |
| **3. Transport** | Transport (4) | TCP, UDP |
| **2. Internet** | Network (3) | IPv4, IPv6, ICMP, ARP |
| **1. Network Access** | Data Link (2), Physical (1) | Ethernet (802.3), Wi-Fi (802.11), Fiber Optic |"""
                                }
                            },
                            {
                                "block_type": "suggested_image",
                                "title": "OSI 7-Layer Reference Model Architecture",
                                "content": {
                                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/OSI_Model_v1.svg/800px-OSI_Model_v1.svg.png",
                                    "caption": "Figure 8.2: Architectural breakdown of the OSI 7-layer reference model demonstrating hierarchical encapsulation and protocol layers.",
                                    "author": "Wikimedia Commons",
                                    "licensing": "CC BY-SA 4.0"
                                }
                            },
                            {
                                "block_type": "suggested_video",
                                "title": "The 7 Layers of the OSI Model Explained",
                                "content": {
                                    "youtube_id": "LANW3m7Bgkw",
                                    "url": "https://www.youtube.com/watch?v=LANW3m7Bgkw",
                                    "description": "Comprehensive video breakdown of the 7 layers of the OSI model, protocol encapsulation, and how data packets travel across networks."
                                }
                            }
                        ],

                        # Page 4: Formative Knowledge Checks & Worked Problem
                        [
                            {
                                "block_type": "worked_example",
                                "title": "Worked Example: Protocol Data Unit (PDU) Encapsulation and Data Rate Calculations",
                                "content": {
                                    "problem_statement": "A student in Nairobi opens a web browser to load 'https://kicd.ac.ke'. At the same time, the local router operates at 4,800 Baud with 4 bits per symbol. (A) Calculate the channel's bit rate. (B) Trace the PDU encapsulation sequence from the web browser to the physical Cat6 wire.",
                                    "step_by_step_solution": [
                                        {
                                            "step_number": 1,
                                            "step_title": "Calculate Bit Rate from Baud Rate",
                                            "explanation": "Bit Rate = Baud Rate * Bits per Symbol = 4,800 Baud * 4 bits/symbol = 19,200 bits per second (bps) or 19.2 kbps."
                                        },
                                        {
                                            "step_number": 2,
                                            "step_title": "Trace Application to Transport Encapsulation",
                                            "explanation": "HTTP/TLS at Layer 7/4 creates application data. The Transport Layer (TCP) encapsulates this payload with source port 51234 and destination port 443, creating a **TCP Segment**."
                                        },
                                        {
                                            "step_number": 3,
                                            "step_title": "Trace Internet Layer Encapsulation",
                                            "explanation": "The Internet Layer (IP) adds source IP (192.168.1.50) and destination IP (102.219.208.5) headers, encapsulating the segment into an **IP Packet**."
                                        },
                                        {
                                            "step_number": 4,
                                            "step_title": "Trace Network Access & Physical Framing",
                                            "explanation": "The Data Link Layer adds MAC addressing and a CRC error-checking trailer, producing an **Ethernet Frame**. The Physical Layer encodes these bits into electrical differential voltages onto the Cat6 cable."
                                        }
                                    ]
                                }
                            },
                            {
                                "block_type": "key_takeaway",
                                "title": "Key Takeaway: Data Communication Foundations & Layering",
                                "content": {
                                    "text": "1. **Signals**: Analog is continuous (sine waves); Digital is discrete binary voltages (square waves) with high noise immunity.\n2. **Bit Rate vs Baud Rate**: Bit Rate (bps) = Baud Rate (symbols/sec) * Bits per Symbol.\n3. **Layered Encapsulation**: Data (Application) -> Segment (Transport/TCP) -> Packet (Internet/IP) -> Frame (Data Link/MAC) -> Bits (Physical Line)."
                                }
                            },
                            {
                                "block_type": "knowledge_check",
                                "title": "Formative Check 1: OSI Network Layer Functionality",
                                "content": {
                                    "question": "Which layer of the OSI reference model is primarily responsible for logical addressing and routing data packets across diverse networks using IP addresses?",
                                    "options": [
                                        "A) Physical Layer",
                                        "B) Data Link Layer",
                                        "C) Network Layer",
                                        "D) Presentation Layer"
                                    ],
                                    "answer": "C",
                                    "explanation": "The Network Layer (Layer 3 of OSI, corresponding to the Internet Layer in TCP/IP) manages logical addressing (IP addresses) and path determination (routing) across interconnected networks."
                                }
                            },
                            {
                                "block_type": "knowledge_check",
                                "title": "Formative Check 2: Baud Rate vs Bit Rate",
                                "content": {
                                    "question": "If a modern digital modulation system transmits at a rate of 2,400 symbols per second (Baud), and each symbol represents 4 bits of binary data, what is the resulting Bit Rate (Data Rate)?",
                                    "options": [
                                        "A) 600 bps",
                                        "B) 2,400 bps",
                                        "C) 4,800 bps",
                                        "D) 9,600 bps"
                                    ],
                                    "answer": "D",
                                    "explanation": "Data Rate (Bit Rate) = Baud Rate × Bits per Symbol. Therefore, 2,400 Baud × 4 bits/symbol = 9,600 bits per second (bps)."
                                }
                            },
                            {
                                "block_type": "knowledge_check",
                                "title": "Formative Check 3: TCP/IP Layer Mapping",
                                "content": {
                                    "question": "Which layer in the 4-layer TCP/IP protocol suite encompasses the functions of the OSI Session, Presentation, and Application layers?",
                                    "options": [
                                        "A) Application Layer",
                                        "B) Transport Layer",
                                        "C) Internet Layer",
                                        "D) Network Access Layer"
                                    ],
                                    "answer": "A",
                                    "explanation": "The TCP/IP Application Layer directly combines the responsibilities of the top three OSI layers: Application (Layer 7), Presentation (Layer 6), and Session (Layer 5)."
                                },
                                {
                                    "block_type": "knowledge_check",
                                    "title": "Formative Check 4: PDU Encapsulation Sequence",
                                    "content": {
                                        "question": "What is the correct hierarchical order of Protocol Data Units (PDUs) during the encapsulation process as data moves down from the application layer to the physical medium?",
                                        "options": [
                                            "A) Data -> Segment -> Packet -> Frame -> Bits",
                                            "B) Bits -> Frame -> Packet -> Segment -> Data",
                                            "C) Packet -> Frame -> Segment -> Data -> Bits",
                                            "D) Data -> Packet -> Segment -> Frame -> Bits"
                                        ],
                                        "answer": "A",
                                        "explanation": "As data descends the stack, the Application Layer generates Data, Transport creates Segments, Network/Internet creates Packets, Data Link creates Frames, and Physical transmits raw Bits."
                                    }
                                }
                            }
                        ]
                    ]
                }
            ]
        },

        # -------------------------------------------------------------
        # UNIT 2: Characteristics, Components & Diagnostics
        # -------------------------------------------------------------
        {
            "unit_order": 2,
            "unit_name": "System Components, Performance Metrics, and Diagnostic Troubleshooting",
            "unit_description": "Comprehensive study of the 5 essential components of data communication, critical performance metrics (delivery, accuracy, latency, jitter, throughput), and systematic 4-step diagnostic troubleshooting pipelines.",
            "lessons": [
                {
                    "lesson_order": 26,
                    "lesson_title": "Characteristics, Components, and Diagnostic Troubleshooting of Data Communication",
                    "lesson_description": "Analyze the five core components of communication systems, evaluate network performance metrics, and apply diagnostic CLI routines to resolve network faults.",
                    "pages": [
                        # Page 1: 5 Components
                        [
                            {
                                "block_type": "learning_goal",
                                "title": "Learning Goal: Components, Metrics & Diagnostic Routines",
                                "content": {
                                    "goal": "Identify the 5 core components of a data communication system, evaluate network metrics (latency, jitter, throughput), and apply the 4-step diagnostic troubleshooting sequence."
                                }
                            },
                            {
                                "block_type": "suggested_diagram",
                                "title": "The 5 Essential Components of Data Communication",
                                "content": {
                                    "caption": "Interactive breakdown of Sender, Message, Transmission Medium, Receiver, and Protocol Governance.",
                                    "svg_content": SVG_COMMUNICATION_COMPONENTS
                                }
                            },
                            {
                                "block_type": "concept_explanation",
                                "title": "The Five Essential Components of a Communication System",
                                "content": {
                                    "body": """### Core Building Blocks

For any successful data communication event to occur, five distinct components must interact concurrently:

1. **Sender (Source Device)**:
   - The originating digital computing device that creates, formats, and encodes the data.
   - *Examples*: Desktop workstations, laptops, smartphones, IoT temperature sensors, security cameras.

2. **Message (Data Payload)**:
   - The actual information, payload, or binary data being transferred.
   - *Forms*: Text documents, digital audio samples, video frame packets, database records, telemetry readings.

3. **Transmission Medium (Communication Channel)**:
   - The physical or electromagnetic pathway along which the signal propagates from the transmitter to the destination.
   - *Guided Media*: Physical conductors such as Unshielded Twisted Pair (UTP Cat6), Coaxial cables, or Optical Fiber strands.
   - *Unguided Media*: Wireless propagation through air/vacuum using Radio Frequencies (RF), Microwaves, or Infrared waves.

4. **Receiver (Destination/Sink Device)**:
   - The target hardware device that captures the incoming electromagnetic or optical signal, decodes it from line voltages or light back into binary bits, and processes it.
   - *Examples*: Web servers, network laser printers, client smartphones, robotic motor controllers.

5. **Protocol (Communication Rules)**:
   - The software algorithms and standardized regulations governing syntax (format), semantics (meaning), synchronization, and error control.
   - *Without a protocol*, two devices connected to the exact same physical cable cannot communicate, just as two humans cannot converse if one speaks Japanese and the other speaks Swahili without a common grammar."""
                                }
                            }
                        ],

                        # Page 2: Performance Metrics
                        [
                            {
                                "block_type": "suggested_diagram",
                                "title": "Network Performance Characteristics and Diagnostic Sequence",
                                "content": {
                                    "caption": "Evaluating Delivery, Accuracy, Timeliness, Jitter, and Throughput alongside the 4-step diagnostic protocol.",
                                    "svg_content": SVG_NETWORK_METRICS_DIAGNOSTICS
                                }
                            },
                            {
                                "block_type": "concept_explanation",
                                "title": "Critical Performance Characteristics of Network Systems",
                                "content": {
                                    "body": """### Evaluating Communication Quality

A network communication system is evaluated based on five foundational operational metrics:

1. **Delivery**:
   - The communication system must route the data to the correct, authorized destination and *only* to that intended destination.

2. **Accuracy**:
   - The received message must be an exact, uncorrupted binary replica of the transmitted message.
   - *Mechanism*: If electromagnetic noise alters a `0` to a `1` (a bit flip), error detection algorithms (such as Parity bits, Cyclic Redundancy Checks / CRC, or TCP Checksums) detect the anomaly and trigger automated retransmission.

3. **Timeliness (Latency)**:
   - Data must be delivered within an acceptable, predictable time frame.
   - For real-time applications such as Voice over IP (VoIP), online gaming, or tele-surgery, late-arriving packets are useless and are discarded.

4. **Jitter (Packet Delay Variation)**:
   - **Definition**: The statistical variance in packet arrival times over a network connection.
   - *Technical Impact*: If video packets are transmitted every 20ms, but arrive erratically (e.g., packet 1 after 15ms, packet 2 after 95ms, packet 3 after 20ms), the receiver experience severe buffering stutter, frozen video frames, and audio robotic distortion.
   - *Mitigation*: Receivers utilize **playout jitter buffers** to smooth playback, though large buffers introduce added latency.

5. **Throughput vs. Bandwidth**:
   - **Bandwidth**: The maximum theoretical data capacity of the physical link (e.g., 1000 Mbps Gigabit Ethernet).
   - **Throughput**: The actual, real-world rate of successful payload data delivery over the channel per unit of time.
   - *Why Throughput < Bandwidth*: Protocol packet headers (overhead), transmission errors and retransmissions, network congestion, and processing bottlenecks reduce usable throughput below the raw physical bandwidth."""
                                }
                            },
                            {
                                "block_type": "suggested_image",
                                "title": "Network Switch and Patch Panel Cabling",
                                "content": {
                                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Ethernet_cables_connected_to_a_network_switch.jpg/1280px-Ethernet_cables_connected_to_a_network_switch.jpg",
                                    "caption": "High-density enterprise Ethernet switch patch panel transmitting packetized digital data over twisted-pair copper Cat6 lines.",
                                    "author": "Wikimedia Commons / Jons",
                                    "licensing": "CC BY-SA 3.0"
                                }
                            }
                        ],

                        # Page 3: Diagnostic Troubleshooting Pipeline
                        [
                            {
                                "block_type": "concept_explanation",
                                "title": "Systematic 4-Step Network Diagnostic Sequence",
                                "content": {
                                    "body": """### The Communication Diagnostic Pipeline

When a network connection fails, computer scientists follow a disciplined, bottom-up troubleshooting methodology based on the 5 components:

```
========================================================================================
                          COMMUNICATION DIAGNOSIS PIPELINE
========================================================================================
[Step 1: Check Sender]   ➔ Verify local NIC & TCP/IP stack: ping 127.0.0.1
[Step 2: Check Medium]   ➔ Inspect physical link lights, cables, or Wi-Fi RSSI
[Step 3: Check Gateway]  ➔ Ping local router gateway: ping 192.168.1.1
[Step 4: Check Receiver] ➔ Test end-to-end IP: ping 8.8.8.8 & DNS: ping kcse.gov.ke
========================================================================================
```

#### Diagnostic Case Study: Troubleshooting a School Lab Computer

- **Symptom**: A student cannot access the KNEC examination portal from Computer Lab PC #14.

1. **Step 1 — Sender Local Loopback (`ping 127.0.0.1`)**:
   - *Result*: Fails with `Destination host unreachable`.
   - *Diagnosis*: The computer's internal network adapter (NIC) driver is disabled, corrupted, or faulty. The problem is isolated to the local host before touching any cables.

2. **Step 2 — Transmission Medium Physical Link**:
   - *Action*: Inspect the RJ45 port LED lights on the back of the PC.
   - *Result*: Port LED is completely dark (no green link light, no amber activity light).
   - *Diagnosis*: Physical cable is disconnected, damaged, or the port on the wall patch panel is dead.

3. **Step 3 — Protocol & Default Gateway Link (`ping 192.168.1.1`)**:
   - *Result*: Fails with `Request timed out`.
   - *Diagnosis*: The local PC is connected physically to the switch, but has received an invalid IP address (e.g., APIPA `169.254.x.x`) due to a failed DHCP server, or the local router is powered off.

4. **Step 4 — External WAN Receiver & DNS Resolution**:
   - *Action*: `ping 8.8.8.8` (Succeeds), followed by `ping knec.ac.ke` (Fails).
   - *Diagnosis*: Internet WAN connection is operational, but the DNS server IP configured on the PC is incorrect or unresponsive, preventing domain name lookup."""
                                }
                            },
                            {
                                "block_type": "suggested_image",
                                "title": "Digital Network Cable Continuity Tester",
                                "content": {
                                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Network_cable_tester.jpg/800px-Network_cable_tester.jpg",
                                    "caption": "Figure 8.4: Handheld RJ-45 network wire mapper and continuity tester verifying 8-pin wiring sequence and detecting split pairs.",
                                    "author": "Wikimedia Commons",
                                    "licensing": "CC BY-SA 3.0"
                                }
                            },
                            {
                                "block_type": "suggested_video",
                                "title": "Network Troubleshooting with Ping and Traceroute",
                                "content": {
                                    "youtube_id": "pA_8W9aGg2k",
                                    "url": "https://www.youtube.com/watch?v=pA_8W9aGg2k",
                                    "description": "Practical tutorial demonstrating step-by-step CLI commands (ping, ipconfig, traceroute) to diagnose network connection failures."
                                }
                            }
                        ],

                        # Page 4: Formative Knowledge Checks & Review
                        [
                            {
                                "block_type": "worked_example",
                                "title": "Worked Example: 4-Step CLI Diagnostic Troubleshooting for a Lab Connection Failure",
                                "content": {
                                    "problem_statement": "A student cannot load the school exam portal on a lab computer. Outline the 4-step systematic diagnostic sequence using terminal CLI commands and evaluate what each test reveals.",
                                    "step_by_step_solution": [
                                        {
                                            "step_number": 1,
                                            "step_title": "Step 1: Test Local TCP/IP Stack (Loopback)",
                                            "explanation": "Run 'ping 127.0.0.1'. Succeeded with 0% loss, proving the computer's OS network software and NIC drivers are functioning properly."
                                        },
                                        {
                                            "step_number": 2,
                                            "step_title": "Step 2: Test Physical Link and Default Gateway",
                                            "explanation": "Check physical Ethernet link light (solid green), then run 'ping 192.168.1.1' (default gateway router). Succeeded with 1.1ms, proving local cable, switch, and router interface are healthy."
                                        },
                                        {
                                            "step_number": 3,
                                            "step_title": "Step 3: Test External Internet Backbone Route",
                                            "explanation": "Run 'ping 8.8.8.8' (Google public DNS). Succeeded with 22ms, proving the ISP fiber uplink and WAN routing are fully operational."
                                        },
                                        {
                                            "step_number": 4,
                                            "step_title": "Step 4: Test Domain Name Resolution (DNS)",
                                            "explanation": "Run 'ping kicd.ac.ke'. Succeeded, confirming DNS server translates domain names into numerical IP addresses correctly."
                                        }
                                    ]
                                }
                            },
                            {
                                "block_type": "key_takeaway",
                                "title": "Key Takeaway: System Components & Performance Metrics",
                                "content": {
                                    "text": "1. **5 Essential Components**: Sender, Message, Transmission Medium, Receiver, and Protocol.\\n2. **Critical Performance Metrics**: Delivery (correct host), Accuracy (bit-perfect via checksums), Timeliness (latency), and Jitter (variation in arrival delay causing streaming stutter).\\n3. **Diagnostic Pipeline**: Always test from local stack (127.0.0.1) -> gateway router -> external IP (8.8.8.8) -> domain name."
                                }
                            },
                            {
                                "block_type": "knowledge_check",
                                "title": "Formative Check 1: The Role of Protocols",
                                "content": {
                                    "question": "Why is a protocol considered indispensable in a data communication system even when two computers are physically connected with high-speed fiber cables?",
                                    "options": [
                                        "A) It physically boosts electrical voltage along the wire.",
                                        "B) It establishes mutually agreed rules for data formatting, syntax, timing, and error handling so both devices interpret the data identically.",
                                        "C) It replaces the need for a physical transmission medium.",
                                        "D) It converts digital square waves into physical radio waves automatically."
                                    ],
                                    "answer": "B",
                                    "explanation": "A protocol defines the rules, formats, syntax, and synchronization governing the communication. Without a common protocol, two connected devices cannot understand the incoming signals."
                                }
                            },
                            {
                                "block_type": "knowledge_check",
                                "title": "Formative Check 2: Diagnosing High Jitter",
                                "content": {
                                    "question": "A user on a Zoom video conference reports that their audio frequently stutters and video periodically freezes and skips ahead, despite speed tests showing 50 Mbps bandwidth. Which network metric is most likely abnormal?",
                                    "options": [
                                        "A) Excessive Jitter (Packet Delay Variation)",
                                        "B) High Baud Rate",
                                        "C) Insufficient Storage Capacity",
                                        "D) Full-Duplex switching activation"
                                    ],
                                    "answer": "A",
                                    "explanation": "Jitter is the variation in packet arrival delays. High jitter causes real-time media streams to arrive unevenly, exceeding the playout buffer and resulting in stuttering, crackling, and skipped video frames."
                                }
                            },
                            {
                                "block_type": "knowledge_check",
                                "title": "Formative Check 3: Local Loopback Test",
                                "content": {
                                    "question": "What is the primary technical purpose of running the command 'ping 127.0.0.1' during network troubleshooting?",
                                    "options": [
                                        "A) To test the bandwidth speed of the ISP connection.",
                                        "B) To verify that the local computer's internal TCP/IP stack and Network Interface Card (NIC) software are functioning.",
                                        "C) To test the wireless signal reach of the regional cellular tower.",
                                        "D) To clear the browser's DNS cache."
                                    ],
                                    "answer": "B",
                                    "explanation": "The IP address 127.0.0.1 is the reserved IPv4 local loopback address. Pinging it tests the host's own internal networking stack and NIC drivers without sending packets over physical wires."
                                },
                                {
                                    "block_type": "knowledge_check",
                                    "title": "Formative Check 4: Bandwidth vs Throughput Distinction",
                                    "content": {
                                        "question": "What is the technical difference between network Bandwidth and network Throughput?",
                                        "options": [
                                            "A) Bandwidth is the maximum theoretical channel capacity, whereas Throughput is the actual measured payload transfer rate.",
                                            "B) Bandwidth applies to wireless only, while Throughput applies to fiber cables.",
                                            "C) Bandwidth measures jitter, while Throughput measures latency.",
                                            "D) Throughput is always higher than bandwidth due to data compression."
                                        ],
                                        "answer": "A",
                                        "explanation": "Bandwidth is the maximum theoretical capacity of a link (e.g. 1 Gbps), while Throughput is the real-world measured data delivery rate after accounting for packet overhead, collisions, and retransmissions."
                                    }
                                }
                            }
                        ]
                    ]
                }
            ]
        },

        # -------------------------------------------------------------
        # UNIT 3: Modes of Data Flow & Transmission Trade-offs
        # -------------------------------------------------------------
        {
            "unit_order": 3,
            "unit_name": "Modes of Data Flow and Directional Transmission Systems",
            "unit_description": "Engineering exploration of Simplex, Half-Duplex, and Full-Duplex communication modes, bandwidth allocation, collision domains, and CSMA/CD mechanisms.",
            "lessons": [
                {
                    "lesson_order": 27,
                    "lesson_title": "Modes of Data Flow and Directional Network Communication",
                    "lesson_description": "Compare Simplex, Half-Duplex, and Full-Duplex transmission modes, analyze collision risks, and evaluate real-world networking trade-offs.",
                    "pages": [
                        # Page 1: The Three Modes
                        [
                            {
                                "block_type": "learning_goal",
                                "title": "Learning Goal: Directional Transmission Modes & Collision Management",
                                "content": {
                                    "goal": "Compare the mechanics of Simplex, Half-Duplex, and Full-Duplex data transmission modes, evaluate collision management via CSMA/CD, and assess network switching trade-offs."
                                }
                            },
                            {
                                "block_type": "suggested_diagram",
                                "title": "Transmission Modes: Simplex, Half-Duplex, and Full-Duplex",
                                "content": {
                                    "caption": "Comparing unidirectional (Simplex), alternating bidirectional (Half-Duplex), and concurrent bidirectional (Full-Duplex) data flow.",
                                    "svg_content": SVG_TRANSMISSION_MODES
                                }
                            },
                            {
                                "block_type": "concept_explanation",
                                "title": "Working Principles of Data Flow Modes",
                                "content": {
                                    "body": """### Directional Modes of Transmission

Data transmission between sender and receiver is classified into three distinct directional modes:

```
========================================================================================
                               DATA FLOW DIRECTION MODES
========================================================================================
  SIMPLEX MODE              SENDER -----------------------------------------> RECEIVER
  (One-way only)            (Traffic on a one-way street)
----------------------------------------------------------------------------------------
  HALF-DUPLEX MODE          SENDER <------------------ OR ------------------> RECEIVER
  (Alternating two-way)     (Alternating traffic on a narrow single-lane bridge)
----------------------------------------------------------------------------------------
  FULL-DUPLEX MODE          SENDER <========================================> RECEIVER
  (Simultaneous two-way)    (Simultaneous traffic in both directions on a highway)
========================================================================================
```

#### 1. Simplex Mode
- **Physical Operation**: Data travels strictly in **one direction only**. One device is permanently hardwired as the transmitter, and the other is permanently dedicated as the receiver.
- **Bandwidth Utilization**: 100% of the channel's capacity is locked to one-way transmission.
- **Highway Analogy**: A one-way street where cars can only drive in one direction.
- **Real-World Examples**:
  - *Television / Radio Broadcast*: TV stations broadcast signals to home antennas; the TV cannot send data back over that RF channel.
  - *Computer Keyboard*: The keyboard sends scan codes to the motherboard, but does not receive keystroke data from the CPU.

#### 2. Half-Duplex Mode
- **Physical Operation**: Data travels in **both directions, but only one direction at a time**. Devices take turns transmitting. While Station A transmits, Station B must listen.
- **Collision Risk**: If both devices transmit at the exact same instant on a shared medium, an electrical **packet collision** occurs, corrupting the data.
- **Highway Analogy**: A single-lane narrow bridge on a two-way country road. Traffic can cross in both directions, but vehicles must yield and wait until the bridge is clear.
- **Real-World Examples**:
  - *Walkie-Talkies (Two-Way Radio)*: Operators use a "Push-to-Talk" (PTT) button and say "Over" to release the channel for the other party.
  - *Legacy Ethernet Hubs*: Hubs repeat all electrical signals to all ports, requiring the CSMA/CD protocol to handle collisions.

#### 3. Full-Duplex Mode
- **Physical Operation**: Data travels in **both directions simultaneously**. Both devices can transmit and receive data packets at the exact same instant without waiting and without collisions.
- **Implementation**: Achieved via dedicated physical transmission lines (separate Transmit Tx and Receive Rx wire pairs in Cat6 cables) or frequency division multiplexing.
- **Highway Analogy**: A multi-lane divided highway where opposing traffic flows concurrently at full speed.
- **Real-World Examples**:
  - *Telephone Conversations*: Both callers can speak and listen at the same time.
  - *Modern Switched Ethernet*: Dedicated switch ports isolate transmit and receive circuits, supporting 1 Gbps / 10 Gbps full-duplex throughput."""
                                }
                            },
                            {
                                "block_type": "suggested_video",
                                "title": "Data Transmission Modes: Simplex, Half-Duplex, and Full-Duplex Explained",
                                "content": {
                                    "youtube_id": "GLyF1A8Z-nU",
                                    "url": "https://www.youtube.com/watch?v=GLyF1A8Z-nU",
                                    "description": "Clear visual animation detailing unidirectional and bidirectional data flows across telecommunication channels."
                                }
                            }
                        ],

                        # Page 2: Comparative Trade-offs & CSMA/CD
                        [
                            {
                                "block_type": "suggested_diagram",
                                "title": "Serial vs. Parallel Transmission and Synchronization Framing",
                                "content": {
                                    "caption": "Comparing single-lane serial bitstreams with multi-conductor parallel buses and asynchronous start/stop bit framing.",
                                    "svg_content": SVG_SERIAL_PARALLEL_AND_TIMING
                                }
                            },
                            {
                                "block_type": "concept_explanation",
                                "title": "Comparative Engineering Matrix and Collision Management",
                                "content": {
                                    "body": """### Comparative Analysis of Transmission Modes

| Architectural Feature | Simplex Mode | Half-Duplex Mode | Full-Duplex Mode |
| :--- | :--- | :--- | :--- |
| **Directionality** | Unidirectional (One-way only) | Bidirectional (Alternating turns) | Bidirectional (Simultaneous) |
| **Bandwidth Allocation** | Dedicated 100% to one-way flow | Shared sequentially between Tx/Rx | Dedicated Tx and Rx channels |
| **Collision Risk** | Zero (impossible by design) | High on shared media | Zero on modern dedicated switch links |
| **Circuit Complexity & Cost** | Low (simple transmitter/receiver) | Moderate (turn-taking logic) | High (isolated transceivers & logic) |
| **Major Limitation** | No acknowledgments or feedback | Latency penalty during turnaround | Requires higher hardware capability |

---

### How Half-Duplex Networks Manage Collisions: CSMA/CD

On shared half-duplex Ethernet networks, computers coordinate access using **Carrier Sense Multiple Access with Collision Detection (CSMA/CD)**:

1. **Carrier Sense**: Before transmitting, the host listens to the wire to ensure no other device is currently sending electrical signals.
2. **Multiple Access**: Multiple devices share the exact same physical wire.
3. **Collision Detection**: If two hosts transmit simultaneously, their voltage waves combine destructively on the wire, raising the voltage beyond normal levels (a collision).
4. **Jam Signal & Exponential Backoff**: The transmitting hosts immediately detect the collision, broadcast a high-frequency **jam signal** to warn all devices, and generate a randomized exponential backoff timer before attempting to retransmit."""
                                }
                            },
                            {
                                "block_type": "suggested_image",
                                "title": "Handheld Walkie-Talkie Transceiver (Half-Duplex)",
                                "content": {
                                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Walkie-talkie.jpg/800px-Walkie-talkie.jpg",
                                    "caption": "Figure 8.6: Two-way push-to-talk (PTT) radio transceiver exemplifying half-duplex communication where parties alternate transmission turns.",
                                    "author": "Wikimedia Commons",
                                    "licensing": "CC BY-SA 3.0"
                                }
                            },
                            {
                                "block_type": "suggested_image",
                                "title": "Twisted Pair Cat6 Ethernet Cable Internal Pairs",
                                "content": {
                                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Twisted_pair_cable.jpg/1280px-Twisted_pair_cable.jpg",
                                    "caption": "Inside a Cat6 UTP cable showing 4 twisted copper wire pairs providing dedicated transmit (Tx) and receive (Rx) lines for full-duplex gigabit communication.",
                                    "author": "Wikimedia Commons / Hustoles",
                                    "licensing": "CC BY-SA 3.0"
                                }
                            }
                        ],

                        # Page 3: Formative Knowledge Checks & Worked Problem
                        [
                            {
                                "block_type": "worked_example",
                                "title": "Worked Example: Evaluating Transmission Modes for Real-World Communication Systems",
                                "content": {
                                    "problem_statement": "A municipal transit system deploys three communication channels: (A) Public electronic billboard displays showing bus arrivals; (B) Security guards communicating via handheld walkie-talkies; (C) Control dispatchers conversing with drivers over mobile VoIP phones. Classify the directional mode for each system and justify based on channel directionality and collision risk.",
                                    "step_by_step_solution": [
                                        {
                                            "step_number": 1,
                                            "step_title": "Classify Electronic Arrival Billboards",
                                            "explanation": "Data travels strictly in one direction from central dispatch to the billboard display with zero return path. Mode: **Simplex Mode**."
                                        },
                                        {
                                            "step_number": 2,
                                            "step_title": "Classify Guard Walkie-Talkies",
                                            "explanation": "Guards push a button to speak and release to listen. Communication is bidirectional but alternating on a single frequency to avoid collisions. Mode: **Half-Duplex Mode**."
                                        },
                                        {
                                            "step_number": 3,
                                            "step_title": "Classify Control Dispatcher VoIP Phones",
                                            "explanation": "Both parties can speak and listen simultaneously without waiting, utilizing separate transmit and receive channels. Mode: **Full-Duplex Mode**."
                                        }
                                    ]
                                }
                            },
                            {
                                "block_type": "key_takeaway",
                                "title": "Key Takeaway: Directional Modes & Switching Benefits",
                                "content": {
                                    "text": "1. **Simplex**: Strictly one-way (e.g., TV broadcast, keyboard); cannot receive error feedback or ACKs.\n2. **Half-Duplex**: Alternating two-way (e.g., walkie-talkies, legacy hubs); requires CSMA/CD to prevent destructive collisions.\n3. **Full-Duplex**: Concurrent simultaneous two-way (e.g., switched Ethernet, smartphones); eliminates collisions and provides dedicated throughput."
                                }
                            },
                            {
                                "block_type": "knowledge_check",
                                "title": "Formative Check 1: Identifying Transmission Modes",
                                "content": {
                                    "question": "A security guard uses a handheld walkie-talkie to communicate with the main gate. The guard must hold down a button to speak and release it to listen. What transmission mode is this?",
                                    "options": [
                                        "A) Simplex Mode",
                                        "B) Half-Duplex Mode",
                                        "C) Full-Duplex Mode",
                                        "D) Multiplex Mode"
                                    ],
                                    "answer": "B",
                                    "explanation": "Walkie-talkies operate in Half-Duplex mode because communication is bidirectional, but can only take place in one direction at a time (alternating transmission and reception)."
                                }
                            },
                            {
                                "block_type": "knowledge_check",
                                "title": "Formative Check 2: Full-Duplex Performance Advantage",
                                "content": {
                                    "question": "Why does upgrading a network from a legacy hub (half-duplex) to a modern network switch (full-duplex) dramatically improve network performance?",
                                    "options": [
                                        "A) It eliminates electrical resistance inside the copper wires.",
                                        "B) It allows all connected devices to transmit and receive data simultaneously on dedicated circuits without packet collisions.",
                                        "C) It converts digital binary pulses into analog sound waves.",
                                        "D) It changes all IP addresses to MAC addresses."
                                    ],
                                    "answer": "B",
                                    "explanation": "Full-duplex switching provides dedicated, collision-free transmit and receive pathways for each device, allowing simultaneous bidirectional data transfer and eliminating collision wait times."
                                }
                            },
                            {
                                "block_type": "knowledge_check",
                                "title": "Formative Check 3: Simplex Limitations",
                                "content": {
                                    "question": "What is the primary technical drawback of a simplex transmission channel in mission-critical computer systems?",
                                    "options": [
                                        "A) It cannot transmit at high frequencies.",
                                        "B) The receiver has no mechanism to send back receipt acknowledgments (ACKs) or error notifications to the sender.",
                                        "C) It consumes twice the electrical power of full-duplex systems.",
                                        "D) It cannot use copper wire."
                                    ],
                                    "answer": "B",
                                    "explanation": "Because simplex communication is strictly one-way, the receiving device cannot communicate back to the sender to acknowledge successful packet delivery or request retransmission of corrupted data."
                                },
                                {
                                    "block_type": "knowledge_check",
                                    "title": "Formative Check 4: CSMA/CD Collision Handling",
                                    "content": {
                                        "question": "In a half-duplex Ethernet network, what immediate action does a transmitting node take upon detecting an electrical collision?",
                                        "options": [
                                            "A) It broadcasts a jam signal to alert all nodes, then waits for a randomized backoff period before retransmitting.",
                                            "B) It immediately switches the cable from copper to optical fiber.",
                                            "C) It converts the data from digital square waves to analog voice frequencies.",
                                            "D) It powers off the network switch permanently."
                                        ],
                                        "answer": "A",
                                        "explanation": "Under CSMA/CD, detecting a collision causes the transmitting host to broadcast a jam signal ensuring all devices recognize the collision, followed by a randomized exponential backoff delay before retrying."
                                    }
                                }
                            }
                        ]
                    ]
                }
            ]
        },

        # -------------------------------------------------------------
        # UNIT 4: Evolution, Modern Infrastructure & Assessment
        # -------------------------------------------------------------
        {
            "unit_order": 4,
            "unit_name": "Evolution of Data Communication, Modern Infrastructure, and Comprehensive Assessment",
            "unit_description": "Historical milestones from the telegraph and early analog modems to optical fiber and 5G networks, real-world case scenario audits, matching matrices, and comprehensive topic review.",
            "lessons": [
                {
                    "lesson_order": 28,
                    "lesson_title": "Significance, Evolution, and Comprehensive Assessment of Data Communication",
                    "lesson_description": "Trace the technological evolution of communication infrastructure, perform network architectural audits, and complete the comprehensive topic assessment.",
                    "pages": [
                        # Page 1: Significance & Evolution
                        [
                            {
                                "block_type": "learning_goal",
                                "title": "Learning Goal: Evolution & Architectural Assessment of Communication Systems",
                                "content": {
                                    "goal": "Trace the historical evolution of data communication from the telegraph to optical fiber and 5G networks, audit real-world network architectures, and complete the comprehensive topic assessment."
                                }
                            },
                            {
                                "block_type": "suggested_diagram",
                                "title": "Historical Evolution of Data Communication Infrastructure",
                                "content": {
                                    "caption": "Milestone timeline from 19th-century telegraphy to modern optical fiber networks and 5G cellular communication.",
                                    "svg_content": SVG_EVOLUTION_TIMELINE
                                }
                            },
                            {
                                "block_type": "concept_explanation",
                                "title": "The Strategic Significance and Evolution of Data Communication",
                                "content": {
                                    "body": """### Why Data Communication Underpins Modern Society

Data communication is the technological backbone of global infrastructure:
- **Global Computational Interconnection**: Universal protocols (TCP/IP) allow diverse operating systems (Windows, Linux, iOS, Android) to interoperate seamlessly across global cloud infrastructures.
- **Resource & Distributed Computing**: Centralized cloud databases allow millions of banking and government terminals across Kenya to process transactions concurrently.
- **Industrial Automation & IoT**: Sub-millisecond data telemetry enables smart electrical grids, autonomous agricultural machinery, and automated medical monitoring.

---

### The 5 Historical Eras of Data Communication

1. **Telegraphy and Early Telephony (1840s–1950s)**:
   - *Mechanism*: Analog electrical pulses over single-wire copper lines. Samuel Morse devised Morse Code to encode alphanumeric characters into short/long electrical pulses.
   
2. **Modems & Analog Telephone Networks (1960s–1980s)**:
   - *The Challenge*: Mainframe computers generated digital binary square waves, but existing global infrastructure consisted of copper telephone lines designed for human voice (analog sound waves).
   - *The Solution — The Modem (Modulator-Demodulator)*: The sending modem modulates digital binary (`0`s and `1`s) into audible audio tones (Frequency Shift Keying / Phase Shift Keying). The receiving modem demodulates the audio back into digital binary.
   
3. **Local Area Networks (LAN) & Ethernet (1980s–1990s)**:
   - *Mechanism*: Robert Metcalfe invented **Ethernet** (IEEE 802.3), enabling local computers to exchange native digital frames over coaxial and twisted-pair cables at 10 Mbps to 100 Mbps without audio modulation.
   
4. **The Internet, TCP/IP & Undersea Optical Fiber (1990s–2010s)**:
   - *Mechanism*: Fiber-optic submarine cables (such as TEAMS and SEACOM in Mombasa) replaced copper trunks, utilizing infrared laser light pulses inside glass cores (total internal reflection) to transmit terabits of data immune to electromagnetic interference.
   
5. **Ubiquitous 5G, Low-Earth Orbit Satellites & IoT (Present)**:
   - *Mechanism*: High-frequency millimeter-wave cellular networks (5G) and LEO satellite constellations (Starlink) deliver gigabit wireless connectivity with sub-10ms latency to billions of mobile and IoT endpoints."""
                                }
                            },
                            {
                                "block_type": "suggested_image",
                                "title": "Vintage Acoustic Coupler Modem",
                                "content": {
                                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Acoustic_coupler_20041015_1309.jpg/1280px-Acoustic_coupler_20041015_1309.jpg",
                                    "caption": "Early acoustic coupler modem allowing computer binary communication by placing a telephone handset into rubber audio cups.",
                                    "author": "Wikimedia Commons / Rama",
                                    "licensing": "CC BY-SA 2.0"
                                }
                            },
                            {
                                "block_type": "suggested_video",
                                "title": "The Evolution and Global Impact of Data Communication Systems",
                                "content": {
                                    "youtube_id": "eHvyA_VwN8E",
                                    "url": "https://www.youtube.com/watch?v=eHvyA_VwN8E",
                                    "description": "Comprehensive documentary walkthrough covering telegraphy, ARPANET, submarine fiber optics, and modern cloud infrastructure."
                                }
                            }
                        ],

                        # Page 2: Challenging Architecture Scenario
                        [
                            {
                                "block_type": "suggested_diagram",
                                "title": "Modern Global Data Communication Architecture",
                                "content": {
                                    "caption": "Integrated ecosystem connecting subsea optical backbones, hyperscale cloud data centers, 5G cellular masts, and LEO satellite constellations.",
                                    "svg_content": SVG_MODERN_GLOBAL_DATA_INFRASTRUCTURE
                                }
                            },
                            {
                                "block_type": "concept_explanation",
                                "title": "Engineering Case Study: Auditing a Regional Examination Center Network",
                                "content": {
                                    "body": """### Practical Engineering Audit: Kenya Regional Examination Facility

**Scenario**: You are hired as a network architect to troubleshoot severe network failures at a regional examination center:

#### System 1: Digital Exam Grade Submission Portal
- **Problem**: 200 examiners are uploading student grade files simultaneously. The network uses legacy Ethernet hubs operating in half-duplex mode. During peak hours, uploads freeze, files become corrupted, and upload failure rates exceed 70%.
- **Root Cause Analysis**: The shared half-duplex hub architecture creates a single large **collision domain**. When 200 hosts transmit packets concurrently, electrical collisions occur continuously on the shared bus. The CSMA/CD algorithm forces devices into constant backoff cycles, causing severe packet loss and network collapse.
- **Architectural Solution**: Replace the legacy hubs with modern **Full-Duplex Gigabit Managed Switches** (Layer 2/3). This isolates each examiner's port into its own dedicated collision domain with separate transmit (Tx) and receive (Rx) lanes, eliminating collisions and enabling concurrent uploads.

---

#### System 2: High-Definition Video Surveillance Streaming
- **Problem**: Real-time HD security cameras stream exam room feeds to the monitoring control room. The feed suffers from extreme **Jitter**. Video feeds stutter, freeze for several seconds, and jump ahead unpredictably.
- **Root Cause Analysis**: Video frames are traversing congested shared network links without Quality of Service (QoS) prioritization. Packets experience erratic queuing delays across intermediate routers, causing high packet delay variation (Jitter) that overflows or empties the video decoder buffer.
- **Architectural Solution**:
  1. Implement **Quality of Service (QoS) Prioritization**: Configure router and switch queues to assign highest priority (Differentiated Services / DSCP) to video streaming traffic over routine bulk file downloads.
  2. Implement **Dedicated VLANs**: Separate surveillance video traffic onto an isolated Virtual LAN (VLAN) with guaranteed bandwidth reservation."""
                                }
                            },
                            {
                                "block_type": "suggested_image",
                                "title": "Submarine Fiber-Optic Cable Cross-Section",
                                "content": {
                                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Submarine_cable_cross_section_3D_plain.svg/1280px-Submarine_cable_cross_section_3D_plain.svg.png",
                                    "caption": "Cross-section of an undersea fiber-optic cable carrying global internet traffic via laser pulses through microscopic glass fibers.",
                                    "author": "Wikimedia Commons / Althanan",
                                    "licensing": "CC BY-SA 3.0"
                                }
                            }
                        ],

                        # Page 3: Comprehensive Practice and Assessment Library
                        [
                            {
                                "block_type": "worked_example",
                                "title": "Worked Example: Architectural Audit and Remediation for a National Examination Network",
                                "content": {
                                    "problem_statement": "An examination center with 150 upload terminals suffers from 65% packet loss and upload freezes during peak hours due to legacy half-duplex hubs. Surveillance video streams suffer severe stuttering. Prescribe an architectural remediation plan with technical justifications.",
                                    "step_by_step_solution": [
                                        {
                                            "step_number": 1,
                                            "step_title": "Diagnose Exam Upload Bottleneck",
                                            "explanation": "150 terminals sharing half-duplex hubs create a single congested collision domain. Continuous simultaneous transmissions trigger CSMA/CD backoffs and packet corruption."
                                        },
                                        {
                                            "step_number": 2,
                                            "step_title": "Implement Switched Full-Duplex Architecture",
                                            "explanation": "Replace hubs with Full-Duplex Gigabit Managed Switches. Each port gets a dedicated, collision-free transmit (Tx) and receive (Rx) circuit, eliminating collisions entirely."
                                        },
                                        {
                                            "step_number": 3,
                                            "step_title": "Remediate Surveillance Video Jitter",
                                            "explanation": "Configure Quality of Service (QoS / DSCP) prioritization on switches and routers, and isolate video traffic on a dedicated Virtual LAN (VLAN) with guaranteed bandwidth reservation."
                                        }
                                    ]
                                }
                            },
                            {
                                "block_type": "key_takeaway",
                                "title": "Key Takeaway: Evolution & Modern Network Design",
                                "content": {
                                    "text": "1. **Evolutionary Milestones**: 1840s Telegraph (Morse pulses) -> 1960s Modems (digital-to-audio modulation) -> 1980s Ethernet LANs (native digital frames) -> 1990s Subsea Fiber Optics (light pulses) -> Present 5G & LEO Satellites.\n2. **Modern Infrastructure**: Core routing uses DWDM optical backbones; access networks leverage Gigabit FTTH, Wi-Fi 6/7, and 5G cellular systems.\n3. **Network Architecture**: Full-duplex switching eliminates collision domains; QoS policies guarantee low jitter for real-time video/audio."
                                }
                            },
                            {
                                "block_type": "concept_explanation",
                                "title": "Matching Matrix: Network Protocols and the TCP/IP Suite",
                                "content": {
                                    "body": """### Protocol Mapping Exercise

Study the table below matching fundamental network protocols to their primary role and TCP/IP layer:

| Protocol Name | Core Operational Role | TCP/IP Layer |
| :--- | :--- | :--- |
| **1. IP (Internet Protocol)** | Routes data packets across diverse networks using logical IP addresses | **Internet Layer** (Layer 2) |
| **2. TCP (Transmission Control Protocol)** | Provides reliable, connection-oriented, sequenced, and error-checked delivery | **Transport Layer** (Layer 3) |
| **3. HTTP / HTTPS** | Formats and transmits hypertext web pages and secure API requests | **Application Layer** (Layer 4) |
| **4. Ethernet (IEEE 802.3)** | Governs physical signaling, MAC framing, and local hardware medium access | **Network Access Layer** (Layer 1) |

---

### True or False Conceptual Review

1. **True or False**: The TCP/IP protocol suite condenses the 7 layers of the OSI reference model into 4 functional layers.  
   *(**Answer: TRUE** — TCP/IP combines OSI Layers 5, 6, 7 into Application, and Layers 1, 2 into Network Access).*

2. **True or False**: Simplex communication allows data to flow in both directions, provided only one station transmits at a time.  
   *(**Answer: FALSE** — Simplex is strictly one-way. Alternating two-way communication is Half-Duplex).*

3. **True or False**: Real-world throughput is almost always lower than theoretical bandwidth due to packet headers, network collisions, and retransmissions.  
   *(**Answer: TRUE**).*

4. **True or False**: Fiber-optic cables propagate data as electrical current pulses through pure copper cores.  
   *(**Answer: FALSE** — Fiber-optic cables transmit infrared/visible light pulses through glass cores).*"""
                                }
                            },
                            {
                                "block_type": "knowledge_check",
                                "title": "Comprehensive Check 1: Modem Operation",
                                "content": {
                                    "question": "How does a modem enable a digital computer to transmit data over an analog copper telephone line?",
                                    "options": [
                                        "A) It converts digital square waves into light pulses transmitted along copper.",
                                        "B) It modulates the computer's digital binary signals into analog audio tones for transmission, and demodulates received tones back into digital binary.",
                                        "C) It encrypts data into hexadecimal assembly codes.",
                                        "D) It increases the physical voltage from 5V to 240V."
                                    ],
                                    "answer": "B",
                                    "explanation": "A modem (Modulator-Demodulator) modulates outgoing digital binary pulses into analog audio frequencies compatible with analog phone lines, and demodulates incoming audio tones back into digital square waves."
                                }
                            },
                            {
                                "block_type": "knowledge_check",
                                "title": "Comprehensive Check 2: Transport Protocol Selection",
                                "content": {
                                    "question": "Why do real-time video conferencing applications (such as Zoom or Microsoft Teams) typically use UDP instead of TCP at the transport layer?",
                                    "options": [
                                        "A) TCP is incompatible with modern fiber cables.",
                                        "B) UDP does not require retransmission delays for lost packets, providing lower latency and faster streaming for time-sensitive media.",
                                        "C) UDP provides hardware-level encryption.",
                                        "D) TCP cannot transmit color video frames."
                                    ],
                                    "answer": "B",
                                    "explanation": "TCP requires three-way handshakes and retransmits lost packets, which introduces latency and jitter. UDP is lightweight and connectionless, allowing real-time video streams to proceed without stuttering for old, lost packets."
                                }
                            },
                            {
                                "block_type": "knowledge_check",
                                "title": "Comprehensive Check 3: Transmission Medium Immunity",
                                "content": {
                                    "question": "Which transmission medium is completely immune to electromagnetic interference (EMI) and radio frequency interference (RFI)?",
                                    "options": [
                                        "A) Unshielded Twisted Pair (UTP Cat5e)",
                                        "B) Coaxial Cable",
                                        "C) Optical Fiber Cable",
                                        "D) Shielded Twisted Pair (STP Cat6)"
                                    ],
                                    "answer": "C",
                                    "explanation": "Optical fiber cables transmit signals as pulses of light (photons) through glass strands rather than electrical currents through metal, making them completely immune to electromagnetic and radio frequency interference."
                                },
                                {
                                    "block_type": "knowledge_check",
                                    "title": "Comprehensive Check 4: Historical Evolution Analysis",
                                    "content": {
                                        "question": "Why was the invention of the Modem (Modulator-Demodulator) essential for early digital computer communication across long distances in the 1960s?",
                                        "options": [
                                            "A) Because global telephone infrastructure was built strictly for analog audio, requiring computers to convert digital binary square waves into audio sine waves.",
                                            "B) Because modems increased electrical mains voltage from 12V to 1000V.",
                                            "C) Because modems replaced the need for copper telephone lines with optical fiber.",
                                            "D) Because early computers could only process Morse code."
                                        ],
                                        "answer": "A",
                                        "explanation": "Early telecommunications networks consisted entirely of analog voice telephone lines. Modems modulated digital binary pulses into audible sound tones for transmission and demodulated tones back into binary at the receiver."
                                    }
                                }
                            }
                        ]
                    ]
                }
            ]
        }
    ]
}

# =====================================================================
# INGESTION RUNNER
# =====================================================================

def ingest_grade10_topic8(replace=True):
    print("=" * 80)
    print("STARTING CBC GRADE 10 COMPUTER SCIENCE — TOPIC 8 INGESTION")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(id=5).first()
    if not curriculum:
        raise ValueError("Curriculum with ID=5 not found!")

    grade = Grade.objects.filter(curriculum=curriculum, level=10).first()
    if not grade:
        raise ValueError("Grade 10 not found for Curriculum ID=5!")

    subject = Subject.objects.filter(grade=grade, name__icontains="Computer").first()
    if not subject:
        raise ValueError("Subject 'Computer Science' not found for Grade 10!")

    print(f"Target Hierarchy: {curriculum.name} ➔ {grade.name} ➔ {subject.name}")

    with transaction.atomic():
        t_order = TOPIC_DATA["topic_order"]
        t_name = TOPIC_DATA["topic_name"]

        topic, created = Topic.objects.get_or_create(
            subject=subject,
            order=t_order,
            defaults={
                "name": t_name,
                "description": "Comprehensive study of data communication concepts, analog vs digital signals, OSI/TCP-IP models, directional transmission modes, and evolution."
            }
        )
        if not created and replace:
            print(f"[*] Updating existing Topic {t_order}: {t_name} (id={topic.id})")
            topic.name = t_name
            topic.save()

            # Clean existing LearningUnits under this topic
            old_units = LearningUnit.objects.filter(topic=topic)
            for u in old_units:
                lessons = Lesson.objects.filter(learning_unit=u)
                for l in lessons:
                    LessonBlock.objects.filter(lesson=l).delete()
                    LessonAsset.objects.filter(lesson=l).delete()
                lessons.delete()
            old_units.delete()
            print("  [-] Cleared old LearningUnits, Lessons, Blocks, and Assets.")
        else:
            print(f"[+] Created new Topic {t_order}: {t_name} (id={topic.id})")

        total_units = 0
        total_lessons = 0
        total_pages = 0
        total_blocks = 0
        total_assets = 0

        for unit_data in TOPIC_DATA["learning_units"]:
            u_order = unit_data["unit_order"]
            u_name = unit_data["unit_name"]
            u_desc = unit_data["unit_description"]

            unit = LearningUnit.objects.create(
                topic=topic,
                order=u_order,
                name=u_name,
                description=u_desc
            )
            total_units += 1

            for lesson_data in unit_data["lessons"]:
                l_order = lesson_data["lesson_order"]
                l_title = lesson_data["lesson_title"]
                l_desc = lesson_data["lesson_description"]
                pages = lesson_data["pages"]

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
                        "topic_order": 8,
                        "unit_order": u_order,
                        "lesson_order": l_order,
                        "description": l_desc
                    }
                )
                total_lessons += 1

                block_counter = 1
                for page_idx, blocks in enumerate(pages, start=1):
                    total_pages += 1
                    for comp_idx, b_info in enumerate(blocks, start=1):
                        b_type = b_info["block_type"]
                        b_title = b_info.get("title", f"Component {comp_idx}")
                        b_content = clean_dict(b_info.get("content", {}))

                        block = LessonBlock.objects.create(
                            lesson=lesson,
                            block_id=f"g10_cs_t8_u{u_order}_p{page_idx}_b{comp_idx}",
                            block_type=b_type,
                            component_type=b_type,
                            title=b_title,
                            content=b_content,
                            order=block_counter,
                            page_number=page_idx,
                            component_order=comp_idx,
                            page_title=b_title if comp_idx == 1 else None,
                            metadata={"topic_order": 8, "unit_order": u_order, "page": page_idx}
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

                print(f"  [+] Ingested Unit {u_order}: '{u_name}' -> Lesson {l_order}: '{l_title}' ({len(pages)} Pages, {block_counter - 1} Blocks)")

    print("=" * 80)
    print(f"TOPIC 8 INGESTION COMPLETE:")
    print(f"  Units Created:   {total_units}")
    print(f"  Lessons Created: {total_lessons}")
    print(f"  Pages Created:   {total_pages}")
    print(f"  Blocks Created:  {total_blocks}")
    print(f"  Assets Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_grade10_topic8(replace=True)
