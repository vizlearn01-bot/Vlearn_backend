"""
VLearn CBC Grade 10 Computer Science — Topic 9: Data Transmission Media
Production Ingestion & Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Computer Science
Topic: Data Transmission Media (Topic Order: 9)

Decomposed into 4 Comprehensive Learning Units & 4 Published Lessons:
  1. Transmission Concepts, Signals, and Guided Physical Media (Lesson 1: Data Transmission Concepts and Guided Media)
  2. Unguided (Wireless) Media and Environmental Transmission Factors (Lesson 2: Wireless Media Technologies and Transmission Degradation)
  3. Hardware Network Interfaces and Connection Protocols (Lesson 3: Hardware Interfaces, NICs, and Physical Connection Protocols)
  4. Media Selection Architecture, Case Studies, and Assessment (Lesson 4: Transmission Media Selection, Case Studies, and Network Architecture)
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
# HIGH PRECISION VECTOR SVGS FOR TOPIC 9 (DARK THEME 960x520)
# =====================================================================

SVG_GUIDED_MEDIA_CROSS_SECTIONS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Guided Transmission Media: Physical Architecture &amp; Cross-Sections</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Internal Layering, Shielding Mechanics, and Differential Signaling in Copper and Optical Fibers</text>

  <!-- Panel 1: Twisted Pair (UTP / STP) -->
  <g transform="translate(45, 90)">
    <rect width="270" height="390" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="270" height="32" rx="8" fill="#0284c7"/>
    <text x="135" y="21" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Twisted-Pair (UTP / STP)</text>

    <!-- Cable Graphic -->
    <g transform="translate(25, 45)">
      <!-- Outer Jacket -->
      <rect x="0" y="0" width="220" height="36" rx="6" fill="#0369a1" stroke="#38bdf8" stroke-width="1"/>
      <text x="110" y="22" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Outer PVC / LSZH Jacket</text>
      
      <!-- Shielding (STP) -->
      <rect x="15" y="44" width="190" height="32" rx="4" fill="#334155" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3"/>
      <text x="110" y="64" font-size="9.5" fill="#cbd5e1" text-anchor="middle">Foil Shield &amp; Braided Mesh (STP)</text>

      <!-- Twisted Pair Strands -->
      <g transform="translate(20, 84)">
        <rect x="0" y="0" width="180" height="24" rx="4" fill="#1e1b4b" stroke="#818cf8" stroke-width="1"/>
        <circle cx="20" cy="12" r="6" fill="#f97316"/>
        <circle cx="45" cy="12" r="6" fill="#ffffff" stroke="#f97316" stroke-width="2"/>
        <text x="110" y="16" font-size="9" fill="#c7d2fe" text-anchor="middle">Pair 1: Orange / Orange-White</text>

        <rect x="0" y="28" width="180" height="24" rx="4" fill="#1e1b4b" stroke="#818cf8" stroke-width="1"/>
        <circle cx="20" cy="40" r="6" fill="#22c55e"/>
        <circle cx="45" cy="40" r="6" fill="#ffffff" stroke="#22c55e" stroke-width="2"/>
        <text x="110" y="44" font-size="9" fill="#c7d2fe" text-anchor="middle">Pair 2: Green / Green-White</text>
      </g>
    </g>

    <!-- Bullets -->
    <g transform="translate(15, 205)">
      <text x="0" y="15" font-size="10.5" font-weight="bold" fill="#38bdf8">&#9889; Physics of Twisting:</text>
      <text x="0" y="32" font-size="9" fill="#e2e8f0">&#8226; Cancels Electromagnetic Interference (EMI).</text>
      <text x="0" y="48" font-size="9" fill="#e2e8f0">&#8226; Equal noise induced on both wires cancels</text>
      <text x="0" y="62" font-size="9" fill="#e2e8f0">  out via differential voltage receiver.</text>
      
      <text x="0" y="85" font-size="10.5" font-weight="bold" fill="#34d399">&#128268; Standard Connector:</text>
      <text x="0" y="102" font-size="9" fill="#a7f3d0">&#8226; RJ-45 (8-pin modular click-latch plug).</text>
      <text x="0" y="118" font-size="9" fill="#cbd5e1">&#8226; Max segment: 100 meters (Cat5e / Cat6).</text>
      <text x="0" y="134" font-size="9" fill="#cbd5e1">&#8226; Typical speed: 10 Mbps - 10 Gbps.</text>
    </g>
  </g>

  <!-- Panel 2: Coaxial Cable -->
  <g transform="translate(345, 90)">
    <rect width="270" height="390" rx="12" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="270" height="32" rx="8" fill="#7e22ce"/>
    <text x="135" y="21" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Coaxial Cable (Concentric)</text>

    <!-- Coaxial Layer Cutaway -->
    <g transform="translate(25, 45)">
      <rect x="0" y="0" width="220" height="30" rx="5" fill="#475569" stroke="#94a3b8" stroke-width="1"/>
      <text x="110" y="19" font-size="9.5" fill="#ffffff" text-anchor="middle">1. Outer Plastic Jacket</text>

      <rect x="15" y="36" width="190" height="28" rx="4" fill="#334155" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="2"/>
      <text x="110" y="54" font-size="9.5" fill="#cbd5e1" text-anchor="middle">2. Metallic Braided Shield (Ground)</text>

      <rect x="30" y="70" width="160" height="28" rx="4" fill="#1e293b" stroke="#a855f7" stroke-width="1"/>
      <text x="110" y="88" font-size="9.5" fill="#c084fc" text-anchor="middle">3. Dielectric Plastic Insulator</text>

      <rect x="50" y="104" width="120" height="26" rx="4" fill="#b45309" stroke="#f59e0b" stroke-width="1"/>
      <text x="110" y="121" font-size="9.5" font-weight="bold" fill="#fef3c7" text-anchor="middle">4. Solid Copper Core</text>
    </g>

    <!-- Bullets -->
    <g transform="translate(15, 205)">
      <text x="0" y="15" font-size="10.5" font-weight="bold" fill="#c084fc">&#9889; Coaxial Symmetry Advantage:</text>
      <text x="0" y="32" font-size="9" fill="#e2e8f0">&#8226; Shared geometric axis confines signal.</text>
      <text x="0" y="48" font-size="9" fill="#e2e8f0">&#8226; Excellent noise immunity &amp; longer reach</text>
      <text x="0" y="62" font-size="9" fill="#e2e8f0">  (185m - 500m) than basic UTP.</text>
      
      <text x="0" y="85" font-size="10.5" font-weight="bold" fill="#34d399">&#128268; Connectors &amp; Application:</text>
      <text x="0" y="102" font-size="9" fill="#a7f3d0">&#8226; BNC (Bayonet Neill-Concelman) / F-Type.</text>
      <text x="0" y="118" font-size="9" fill="#cbd5e1">&#8226; Cable TV (CATV), broadband modems.</text>
      <text x="0" y="134" font-size="9" fill="#cbd5e1">&#8226; Stiffer, bulkier, higher installation cost.</text>
    </g>
  </g>

  <!-- Panel 3: Fiber-Optic Cable -->
  <g transform="translate(645, 90)">
    <rect width="270" height="390" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="270" height="32" rx="8" fill="#059669"/>
    <text x="135" y="21" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Fiber-Optic Cable (Light Waves)</text>

    <!-- Fiber Graphic showing TIR -->
    <g transform="translate(15, 45)">
      <!-- Cladding boundary -->
      <rect x="0" y="0" width="240" height="75" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="1.5"/>
      <text x="120" y="17" font-size="9" fill="#a7f3d0" text-anchor="middle">Glass Cladding (Lower Refractive Index n₂)</text>
      
      <!-- Core -->
      <rect x="10" y="24" width="220" height="28" rx="3" fill="#022c22"/>
      <!-- Light Ray Bouncing (TIR) -->
      <polyline points="15,38 65,26 115,50 165,26 215,50 225,38" fill="none" stroke="#facc15" stroke-width="2.5" stroke-linecap="round"/>
      <text x="120" y="42" font-size="9" font-weight="bold" fill="#fef08a" text-anchor="middle">Light Core (Index n₁ &gt; n₂)</text>

      <text x="120" y="68" font-size="8.5" fill="#a7f3d0" text-anchor="middle">Total Internal Reflection (TIR)</text>
    </g>

    <!-- Bullets -->
    <g transform="translate(15, 140)">
      <text x="0" y="15" font-size="10.5" font-weight="bold" fill="#34d399">&#9889; Optical Physics &amp; Immunity:</text>
      <text x="0" y="32" font-size="9" fill="#e2e8f0">&#8226; Photons replace electrical electrons.</text>
      <text x="0" y="48" font-size="9" fill="#34d399" font-weight="bold">&#8226; 100% IMMUNE to EMI, RFI, &amp; Lightning!</text>
      <text x="0" y="64" font-size="9" fill="#e2e8f0">&#8226; Near-zero attenuation over tens of km.</text>
      
      <text x="0" y="87" font-size="10.5" font-weight="bold" fill="#38bdf8">&#127760; Single-Mode vs Multi-Mode:</text>
      <text x="0" y="104" font-size="9" fill="#cbd5e1">&#8226; Single-Mode (9µm core, Laser): up to 100km.</text>
      <text x="0" y="120" font-size="9" fill="#cbd5e1">&#8226; Multi-Mode (50µm core, LED): up to 2km.</text>
      <text x="0" y="136" font-size="9" fill="#cbd5e1">&#8226; Speed: 100 Gbps+ backbone capacity.</text>
      <text x="0" y="152" font-size="9" fill="#f87171">&#8226; Fragile glass; requires fusion splicing.</text>
    </g>
  </g>
</svg>
""")

SVG_SIGNAL_ENCODING_MODULATION = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Signal Fundamentals: Analog vs. Digital &amp; Carrier Modulation</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Waveform Physics, Binary Encoding, and Amplitude / Frequency / Phase Modulation (AM, FM, PM)</text>

  <!-- Left: Analog vs Digital Waveforms -->
  <g transform="translate(45, 90)">
    <rect width="420" height="390" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="420" height="32" rx="8" fill="#0284c7"/>
    <text x="210" y="21" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">Continuous Analog vs. Discrete Digital Signals</text>

    <!-- Analog Waveform Box -->
    <g transform="translate(20, 45)">
      <rect width="380" height="110" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="15" y="20" font-size="11" font-weight="bold" fill="#38bdf8">Analog Signal (Continuous Sine Wave):</text>
      <text x="15" y="34" font-size="9" fill="#94a3b8">Smooth variation in amplitude and frequency over time (Voice, Sound, Radio)</text>
      
      <!-- Sine Wave Path -->
      <path d="M 30,75 Q 55,45 80,75 T 130,75 T 180,75 T 230,75 T 280,75 T 330,75" fill="none" stroke="#38bdf8" stroke-width="3"/>
      <line x1="25" y1="75" x2="355" y2="75" stroke="#64748b" stroke-width="1" stroke-dasharray="3"/>
    </g>

    <!-- Digital Waveform Box -->
    <g transform="translate(20, 168)">
      <rect width="380" height="110" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="15" y="20" font-size="11" font-weight="bold" fill="#34d399">Digital Signal (Discrete Binary Pulses):</text>
      <text x="15" y="34" font-size="9" fill="#94a3b8">Sharp voltage transitions (5V = Binary 1, 0V = Binary 0)</text>

      <!-- Square Wave Path -->
      <path d="M 30,85 L 55,85 L 55,50 L 95,50 L 95,85 L 135,85 L 135,50 L 175,50 L 175,85 L 215,85 L 215,50 L 255,50 L 255,85 L 340,85" fill="none" stroke="#34d399" stroke-width="3"/>
      <text x="75" y="45" font-family="monospace" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">1 (5V)</text>
      <text x="115" y="98" font-family="monospace" font-size="10" font-weight="bold" fill="#94a3b8" text-anchor="middle">0 (0V)</text>
      <text x="155" y="45" font-family="monospace" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">1</text>
      <text x="195" y="98" font-family="monospace" font-size="10" font-weight="bold" fill="#94a3b8" text-anchor="middle">0</text>
      <text x="235" y="45" font-family="monospace" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">1</text>
    </g>

    <!-- Key Definitions -->
    <g transform="translate(20, 290)">
      <text x="0" y="15" font-size="10.5" font-weight="bold" fill="#e2e8f0">&#128218; Core Definitions:</text>
      <text x="0" y="34" font-size="9.5" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#38bdf8">Encoding</tspan>: Converting raw data bits into physical pulses.</text>
      <text x="0" y="52" font-size="9.5" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#38bdf8">Modem (Modulator/Demodulator)</tspan>: Interfaces digital computers</text>
      <text x="0" y="68" font-size="9.5" fill="#cbd5e1">  with continuous analog transmission channels.</text>
    </g>
  </g>

  <!-- Right: Modulation Techniques (AM, FM, PM) -->
  <g transform="translate(495, 90)">
    <rect width="420" height="390" rx="12" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="420" height="32" rx="8" fill="#7e22ce"/>
    <text x="210" y="21" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">Modulation: Superimposing Data on Carrier Waves</text>

    <!-- AM -->
    <g transform="translate(20, 42)">
      <rect width="380" height="68" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="15" y="18" font-size="10" font-weight="bold" fill="#f472b6">1. Amplitude Modulation (AM):</text>
      <text x="15" y="32" font-size="8.5" fill="#94a3b8">Height (voltage peak) varies with binary bits; frequency remains constant.</text>
      <path d="M 30,52 Q 40,38 50,52 T 70,52 Q 80,44 90,52 T 110,52 Q 120,38 130,52 T 150,52" fill="none" stroke="#f472b6" stroke-width="2"/>
      <text x="200" y="52" font-size="9" fill="#fbcfe8">Bit 1 = High Peak | Bit 0 = Low Peak</text>
    </g>

    <!-- FM -->
    <g transform="translate(20, 118)">
      <rect width="380" height="68" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="15" y="18" font-size="10" font-weight="bold" fill="#38bdf8">2. Frequency Modulation (FM):</text>
      <text x="15" y="32" font-size="8.5" fill="#94a3b8">Wave cycle density (Hertz) varies; amplitude remains constant.</text>
      <path d="M 30,52 Q 35,42 40,52 T 50,52 T 60,52 Q 75,42 90,52 T 120,52 Q 125,42 130,52 T 140,52" fill="none" stroke="#38bdf8" stroke-width="2"/>
      <text x="200" y="52" font-size="9" fill="#bae6fd">Bit 1 = Dense Waves | Bit 0 = Sparse Waves</text>
    </g>

    <!-- PM -->
    <g transform="translate(20, 194)">
      <rect width="380" height="68" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="15" y="18" font-size="10" font-weight="bold" fill="#34d399">3. Phase Modulation (PM / PSK):</text>
      <text x="15" y="32" font-size="8.5" fill="#94a3b8">Wave direction flips abruptly (180° shift) when bit changes from 0 to 1.</text>
      <path d="M 30,52 Q 40,40 50,52 T 70,52 L 70,40 Q 80,52 90,40 T 110,40" fill="none" stroke="#34d399" stroke-width="2"/>
      <text x="200" y="52" font-size="9" fill="#a7f3d0">Phase Shift indicates Bit Transition</text>
    </g>

    <!-- Bandwidth Callout -->
    <g transform="translate(20, 272)">
      <rect width="380" height="95" rx="8" fill="#1e1b4b" stroke="#818cf8" stroke-width="1.5"/>
      <text x="190" y="22" font-size="11" font-weight="bold" fill="#c7d2fe" text-anchor="middle">&#128640; Bandwidth vs. Data Rate Metric</text>
      <text x="15" y="44" font-size="9.5" fill="#e2e8f0">&#8226; <tspan font-weight="bold" fill="#38bdf8">Bandwidth (Hz)</tspan>: Range of frequencies the medium can carry.</text>
      <text x="15" y="62" font-size="9.5" fill="#e2e8f0">&#8226; <tspan font-weight="bold" fill="#34d399">Throughput (bps)</tspan>: Actual payload data delivered per second.</text>
      <text x="15" y="80" font-size="9.5" fill="#cbd5e1">&#8226; Higher carrier frequencies = higher data transmission capacity.</text>
    </g>
  </g>
</svg>
""")

SVG_ELECTROMAGNETIC_SPECTRUM_WIRELESS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Electromagnetic Spectrum &amp; Unguided Wireless Media</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Frequency Bands, Propagation Physics, and Wi-Fi Non-Overlapping Channels</text>

  <!-- Spectrum Bar (Top Half) -->
  <g transform="translate(45, 85)">
    <rect width="870" height="150" rx="12" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="435" y="24" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Electromagnetic Spectrum Partition for Telecommunications</text>

    <!-- Band 1: Radio Waves -->
    <g transform="translate(15, 38)">
      <rect width="260" height="95" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <rect width="260" height="22" rx="6" fill="#0369a1"/>
      <text x="130" y="15" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Radio Waves (3 kHz – 1 GHz)</text>
      <text x="10" y="38" font-size="9" fill="#38bdf8" font-weight="bold">&#8226; Omnidirectional Propagation</text>
      <text x="10" y="52" font-size="8.5" fill="#cbd5e1">&#8226; Penetrates walls &amp; obstacles well.</text>
      <text x="10" y="66" font-size="8.5" fill="#cbd5e1">&#8226; Applications: AM/FM Radio, Bluetooth,</text>
      <text x="10" y="80" font-size="8.5" fill="#cbd5e1">  VHF/UHF Two-Way Radio, Cellular 2G/3G.</text>
    </g>

    <!-- Band 2: Microwaves -->
    <g transform="translate(290, 38)">
      <rect width="280" height="95" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
      <rect width="280" height="22" rx="6" fill="#b45309"/>
      <text x="140" y="15" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Microwaves (1 GHz – 300 GHz)</text>
      <text x="10" y="38" font-size="9" fill="#fbbf24" font-weight="bold">&#8226; Line-of-Sight (LoS) Straight Beam</text>
      <text x="10" y="52" font-size="8.5" fill="#cbd5e1">&#8226; Blocked by hills, Earth's curvature, rain.</text>
      <text x="10" y="66" font-size="8.5" fill="#cbd5e1">&#8226; Wi-Fi (2.4 GHz, 5 GHz, 6 GHz), 4G/5G,</text>
      <text x="10" y="80" font-size="8.5" fill="#cbd5e1">  Terrestrial Dish Relays, Satellite (GEO/LEO).</text>
    </g>

    <!-- Band 3: Infrared -->
    <g transform="translate(585, 38)">
      <rect width="270" height="95" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
      <rect width="270" height="22" rx="6" fill="#b91c1c"/>
      <text x="135" y="15" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Infrared (300 GHz – 400 THz)</text>
      <text x="10" y="38" font-size="9" fill="#f87171" font-weight="bold">&#8226; Short-Range, Zero Wall Penetration</text>
      <text x="10" y="52" font-size="8.5" fill="#cbd5e1">&#8226; Completely stopped by walls/doors.</text>
      <text x="10" y="66" font-size="8.5" fill="#cbd5e1">&#8226; High Security: Contained inside room.</text>
      <text x="10" y="80" font-size="8.5" fill="#cbd5e1">&#8226; TV Remotes, short-range optical sensors.</text>
    </g>
  </g>

  <!-- Bottom Left: Wi-Fi 2.4 GHz Channel Overlap -->
  <g transform="translate(45, 250)">
    <rect width="425" height="230" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="425" height="28" rx="8" fill="#0284c7"/>
    <text x="212" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2.4 GHz Wi-Fi Spectrum: Non-Overlapping Channels</text>

    <!-- Channel Domes -->
    <g transform="translate(20, 40)">
      <!-- Channel 1 -->
      <path d="M 10,75 Q 50,20 90,75" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="2"/>
      <text x="50" y="65" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Ch 1</text>

      <!-- Channel 6 -->
      <path d="M 150,75 Q 190,20 230,75" fill="#34d399" fill-opacity="0.25" stroke="#34d399" stroke-width="2"/>
      <text x="190" y="65" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">Ch 6</text>

      <!-- Channel 11 -->
      <path d="M 290,75 Q 330,20 370,75" fill="#a855f7" fill-opacity="0.25" stroke="#a855f7" stroke-width="2"/>
      <text x="330" y="65" font-size="10" font-weight="bold" fill="#c084fc" text-anchor="middle">Ch 11</text>

      <!-- Baseline -->
      <line x1="5" y1="75" x2="380" y2="75" stroke="#64748b" stroke-width="1.5"/>
      <text x="192" y="92" font-size="9" fill="#94a3b8" text-anchor="middle">2.400 GHz ──────────────────────────────── 2.483 GHz</text>
    </g>

    <!-- Notes -->
    <g transform="translate(15, 145)">
      <text x="0" y="12" font-size="9.5" font-weight="bold" fill="#fbbf24">&#9888; The Co-Channel Interference Rule:</text>
      <text x="0" y="28" font-size="8.5" fill="#e2e8f0">&#8226; In 2.4 GHz, only channels 1, 6, and 11 do not overlap.</text>
      <text x="0" y="42" font-size="8.5" fill="#e2e8f0">&#8226; Intermediate channels (2-5, 7-10) cause severe packet collisions.</text>
      <text x="0" y="56" font-size="8.5" fill="#38bdf8">&#8226; 5 GHz / 6 GHz bands provide 24+ non-overlapping channels.</text>
    </g>
  </g>

  <!-- Bottom Right: Satellite Orbits: GEO vs LEO -->
  <g transform="translate(490, 250)">
    <rect width="425" height="230" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="425" height="28" rx="8" fill="#059669"/>
    <text x="212" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Satellite Microwave Architecture: GEO vs. LEO</text>

    <!-- Diagram Graphics -->
    <g transform="translate(20, 38)">
      <!-- Earth -->
      <circle cx="45" cy="50" r="30" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="45" y="54" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Earth</text>

      <!-- LEO Orbit -->
      <ellipse cx="45" cy="50" rx="65" ry="40" fill="none" stroke="#34d399" stroke-width="1.5" stroke-dasharray="3"/>
      <rect x="100" y="30" width="14" height="10" rx="2" fill="#34d399"/>
      <text x="140" y="38" font-size="8.5" font-weight="bold" fill="#34d399">LEO: 500-1200 km (Starlink)</text>
      <text x="140" y="50" font-size="8" fill="#a7f3d0">Latency: ~25 - 40 ms (Constellations)</text>

      <!-- GEO Orbit -->
      <ellipse cx="45" cy="50" rx="145" ry="45" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3"/>
      <rect x="180" y="80" width="16" height="12" rx="2" fill="#f59e0b"/>
      <text x="205" y="88" font-size="8.5" font-weight="bold" fill="#f59e0b">GEO: 35,786 km (Equatorial)</text>
      <text x="205" y="100" font-size="8" fill="#fde68a">Latency: ~500 - 600 ms (Stationary)</text>
    </g>

    <!-- Transponder Explanation -->
    <g transform="translate(15, 155)">
      <text x="0" y="12" font-size="9.5" font-weight="bold" fill="#ffffff">&#128225; Satellite Transponder Function:</text>
      <text x="0" y="28" font-size="8.5" fill="#cbd5e1">&#8226; Uplink: Ground station beams signal up to satellite transponder.</text>
      <text x="0" y="42" font-size="8.5" fill="#cbd5e1">&#8226; Transponder amplifies signal &amp; converts it to downlink frequency.</text>
      <text x="0" y="56" font-size="8.5" fill="#cbd5e1">&#8226; Downlink: Beamed across continental footprints to user terminals.</text>
    </g>
  </g>
</svg>
""")

SVG_TRANSMISSION_DEGRADATION_FACTORS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">5 Key Environmental Degradation Factors in Network Transmission</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Physical Mechanisms Causing Attenuation, Absorption, Interference, and Jitter</text>

  <!-- 5 Columns / Cards -->
  <!-- Card 1: Attenuation -->
  <g transform="translate(40, 90)">
    <rect width="165" height="390" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="165" height="28" rx="6" fill="#0284c7"/>
    <text x="82" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Attenuation</text>
    
    <!-- Graphic -->
    <g transform="translate(10, 38)">
      <rect width="145" height="70" rx="5" fill="#1e293b"/>
      <path d="M 15,55 Q 35,20 55,55 Q 75,35 95,55 Q 115,48 135,55" fill="none" stroke="#38bdf8" stroke-width="2"/>
      <text x="72" y="66" font-size="8" fill="#94a3b8" text-anchor="middle">Signal amplitude fades</text>
    </g>

    <text x="10" y="125" font-size="9.5" font-weight="bold" fill="#38bdf8">Mechanism:</text>
    <text x="10" y="140" font-size="8.5" fill="#cbd5e1">Loss of signal strength</text>
    <text x="10" y="153" font-size="8.5" fill="#cbd5e1">(voltage/photons) over</text>
    <text x="10" y="166" font-size="8.5" fill="#cbd5e1">distance as wave disperses</text>
    <text x="10" y="179" font-size="8.5" fill="#cbd5e1">or energy turns to heat.</text>

    <text x="10" y="202" font-size="9.5" font-weight="bold" fill="#34d399">Countermeasure:</text>
    <text x="10" y="217" font-size="8.5" fill="#a7f3d0">&#8226; Repeaters &amp; Amplifiers.</text>
    <text x="10" y="230" font-size="8.5" fill="#a7f3d0">&#8226; Respect max length</text>
    <text x="10" y="243" font-size="8.5" fill="#a7f3d0">  (100m for UTP).</text>
  </g>

  <!-- Card 2: Obstacles & Absorption -->
  <g transform="translate(220, 90)">
    <rect width="165" height="390" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="165" height="28" rx="6" fill="#b45309"/>
    <text x="82" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Obstacles</text>

    <!-- Graphic -->
    <g transform="translate(10, 38)">
      <rect width="145" height="70" rx="5" fill="#1e293b"/>
      <line x1="15" y1="35" x2="60" y2="35" stroke="#fbbf24" stroke-width="3"/>
      <rect x="65" y="15" width="20" height="42" fill="#64748b"/>
      <line x1="90" y1="35" x2="135" y2="35" stroke="#fbbf24" stroke-width="1" stroke-dasharray="2"/>
      <text x="75" y="66" font-size="8" fill="#fde68a" text-anchor="middle">Solid Wall Barrier</text>
    </g>

    <text x="10" y="125" font-size="9.5" font-weight="bold" fill="#fbbf24">Absorption Index:</text>
    <text x="10" y="140" font-size="8.5" fill="#f87171">&#8226; Concrete / Stone: Severe</text>
    <text x="10" y="153" font-size="8.5" fill="#f87171">&#8226; Metal / Steel: Blocks 100%</text>
    <text x="10" y="166" font-size="8.5" fill="#fbbf24">&#8226; Water / People: Moderate</text>
    <text x="10" y="179" font-size="8.5" fill="#34d399">&#8226; Wood / Drywall: Low</text>

    <text x="10" y="202" font-size="9.5" font-weight="bold" fill="#34d399">Countermeasure:</text>
    <text x="10" y="217" font-size="8.5" fill="#a7f3d0">&#8226; Mesh Wi-Fi Nodes.</text>
    <text x="10" y="230" font-size="8.5" fill="#a7f3d0">&#8226; High-gain antennas.</text>
  </g>

  <!-- Card 3: Frequency Interference -->
  <g transform="translate(400, 90)">
    <rect width="165" height="390" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="165" height="28" rx="6" fill="#b91c1c"/>
    <text x="82" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Interference (EMI)</text>

    <!-- Graphic -->
    <g transform="translate(10, 38)">
      <rect width="145" height="70" rx="5" fill="#1e293b"/>
      <path d="M 15,35 Q 35,15 55,35 Q 75,55 95,35 Q 115,15 135,35" fill="none" stroke="#f87171" stroke-width="2"/>
      <path d="M 15,38 L 45,20 L 75,45 L 105,18 L 135,40" fill="none" stroke="#fde047" stroke-width="1.5"/>
      <text x="72" y="66" font-size="8" fill="#fca5a5" text-anchor="middle">Noise Collisions</text>
    </g>

    <text x="10" y="125" font-size="9.5" font-weight="bold" fill="#f87171">Sources of Noise:</text>
    <text x="10" y="140" font-size="8.5" fill="#cbd5e1">&#8226; Microwave ovens (2.4GHz)</text>
    <text x="10" y="153" font-size="8.5" fill="#cbd5e1">&#8226; High-voltage power lines</text>
    <text x="10" y="166" font-size="8.5" fill="#cbd5e1">&#8226; Electric motors &amp; generators</text>
    <text x="10" y="179" font-size="8.5" fill="#cbd5e1">&#8226; Adjacent Wi-Fi routers</text>

    <text x="10" y="202" font-size="9.5" font-weight="bold" fill="#34d399">Countermeasure:</text>
    <text x="10" y="217" font-size="8.5" fill="#a7f3d0">&#8226; STP shielding or Fiber.</text>
    <text x="10" y="230" font-size="8.5" fill="#a7f3d0">&#8226; Switch to 5GHz band.</text>
  </g>

  <!-- Card 4: Weather & Rain Fade -->
  <g transform="translate(580, 90)">
    <rect width="165" height="390" rx="10" fill="#0f172a" stroke="#818cf8" stroke-width="1.5"/>
    <rect width="165" height="28" rx="6" fill="#4338ca"/>
    <text x="82" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4. Weather (Rain Fade)</text>

    <!-- Graphic -->
    <g transform="translate(10, 38)">
      <rect width="145" height="70" rx="5" fill="#1e293b"/>
      <line x1="30" y1="20" x2="30" y2="40" stroke="#93c5fd" stroke-width="2" stroke-dasharray="3"/>
      <line x1="60" y1="15" x2="60" y2="35" stroke="#93c5fd" stroke-width="2" stroke-dasharray="3"/>
      <line x1="90" y1="25" x2="90" y2="45" stroke="#93c5fd" stroke-width="2" stroke-dasharray="3"/>
      <line x1="120" y1="18" x2="120" y2="38" stroke="#93c5fd" stroke-width="2" stroke-dasharray="3"/>
      <text x="72" y="66" font-size="8" fill="#bfdbfe" text-anchor="middle">Atmospheric Dropouts</text>
    </g>

    <text x="10" y="125" font-size="9.5" font-weight="bold" fill="#818cf8">Vulnerable Links:</text>
    <text x="10" y="140" font-size="8.5" fill="#cbd5e1">&#8226; Satellite dishes (Ku/Ka band)</text>
    <text x="10" y="153" font-size="8.5" fill="#cbd5e1">&#8226; Terrestrial microwave links</text>
    <text x="10" y="166" font-size="8.5" fill="#cbd5e1">&#8226; High-density water drops</text>
    <text x="10" y="179" font-size="8.5" fill="#cbd5e1">  absorb &amp; scatter radio beam.</text>

    <text x="10" y="202" font-size="9.5" font-weight="bold" fill="#34d399">Countermeasure:</text>
    <text x="10" y="217" font-size="8.5" fill="#a7f3d0">&#8226; Adaptive power transmit.</text>
    <text x="10" y="230" font-size="8.5" fill="#a7f3d0">&#8226; Lower frequency carrier.</text>
  </g>

  <!-- Card 5: Multi-path Distortion -->
  <g transform="translate(760, 90)">
    <rect width="165" height="390" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="165" height="28" rx="6" fill="#059669"/>
    <text x="82" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">5. Multi-path Echo</text>

    <!-- Graphic -->
    <g transform="translate(10, 38)">
      <rect width="145" height="70" rx="5" fill="#1e293b"/>
      <!-- Direct Ray -->
      <line x1="15" y1="40" x2="130" y2="40" stroke="#34d399" stroke-width="2"/>
      <!-- Reflected Ray -->
      <polyline points="15,40 72,18 130,40" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="2"/>
      <text x="72" y="66" font-size="8" fill="#6ee7b7" text-anchor="middle">Direct + Bounced Waves</text>
    </g>

    <text x="10" y="125" font-size="9.5" font-weight="bold" fill="#34d399">Mechanism:</text>
    <text x="10" y="140" font-size="8.5" fill="#cbd5e1">&#8226; Waves bounce off metal,</text>
    <text x="10" y="153" font-size="8.5" fill="#cbd5e1">  floors, glass, and furniture.</text>
    <text x="10" y="166" font-size="8.5" fill="#cbd5e1">&#8226; Multiple copies arrive</text>
    <text x="10" y="179" font-size="8.5" fill="#cbd5e1">  with microsecond delay.</text>

    <text x="10" y="202" font-size="9.5" font-weight="bold" fill="#34d399">Countermeasure:</text>
    <text x="10" y="217" font-size="8.5" fill="#a7f3d0">&#8226; MIMO (Multiple-Input</text>
    <text x="10" y="230" font-size="8.5" fill="#a7f3d0">  Multiple-Output) Wi-Fi.</text>
  </g>
</svg>
""")

SVG_HARDWARE_CONNECTION_PROTOCOL = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Hardware Interface Architecture &amp; Physical Installation Protocol</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Network Interface Cards (NIC), Motherboard Bus Integration, and 4-Step Engineering Protocol</text>

  <!-- Left: NIC Architecture & Connector -->
  <g transform="translate(45, 90)">
    <rect width="420" height="390" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="420" height="30" rx="8" fill="#0284c7"/>
    <text x="210" y="20" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Network Interface Card (NIC) Internal Architecture</text>

    <!-- PCI-e NIC Diagram -->
    <g transform="translate(20, 45)">
      <rect width="380" height="150" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      
      <!-- PCB Board -->
      <rect x="15" y="15" width="350" height="90" rx="5" fill="#065f46" stroke="#34d399" stroke-width="1"/>
      
      <!-- Controller Chip (MAC/PHY) -->
      <rect x="40" y="30" width="80" height="60" rx="4" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
      <text x="80" y="55" font-size="9" font-weight="bold" fill="#fbbf24" text-anchor="middle">PHY / MAC</text>
      <text x="80" y="70" font-size="8" fill="#fde68a" text-anchor="middle">Controller Chip</text>

      <!-- RJ-45 Female Socket -->
      <rect x="270" y="25" width="70" height="70" rx="4" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
      <rect x="285" y="45" width="40" height="35" fill="#0f172a"/>
      <text x="305" y="38" font-size="8.5" font-weight="bold" fill="#ffffff" text-anchor="middle">RJ-45 Port</text>
      
      <!-- Status LEDs -->
      <circle cx="280" cy="35" r="3.5" fill="#22c55e"/>
      <circle cx="330" cy="35" r="3.5" fill="#f59e0b"/>

      <!-- PCIe Gold Fingers -->
      <rect x="140" y="105" width="100" height="20" fill="#f59e0b" stroke="#d97706" stroke-width="1"/>
      <text x="190" y="120" font-size="8.5" font-weight="bold" fill="#000000" text-anchor="middle">PCIe Motherboard Bus</text>
    </g>

    <!-- Diagnostics and LED indicators -->
    <g transform="translate(20, 215)">
      <text x="0" y="15" font-size="11" font-weight="bold" fill="#38bdf8">&#128161; Port LED Status Indicators:</text>
      <text x="0" y="34" font-size="9.5" fill="#e2e8f0">&#8226; <tspan font-weight="bold" fill="#22c55e">Steady Green LED</tspan>: Valid Physical Link Established (Carrier detected).</text>
      <text x="0" y="52" font-size="9.5" fill="#e2e8f0">&#8226; <tspan font-weight="bold" fill="#f59e0b">Flashing Amber LED</tspan>: Active Packet Transmission / Frame Processing.</text>
      <text x="0" y="70" font-size="9.5" fill="#f87171">&#8226; <tspan font-weight="bold" fill="#f87171">Unlit (Dark) LED</tspan>: Cable disconnected, broken pin, or powered-off switch.</text>

      <text x="0" y="100" font-size="10.5" font-weight="bold" fill="#34d399">&#128737; Wireless NIC:</text>
      <text x="0" y="118" font-size="9" fill="#cbd5e1">Transceiver converts system packets into RF modulated wave pulses.</text>
    </g>
  </g>

  <!-- Right: 4-Step Connection Planning Protocol -->
  <g transform="translate(495, 90)">
    <rect width="420" height="390" rx="12" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="420" height="30" rx="8" fill="#7e22ce"/>
    <text x="210" y="20" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Physical Installation &amp; Commissioning Protocol</text>

    <!-- Step 1 -->
    <g transform="translate(20, 42)">
      <rect width="380" height="65" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <circle cx="25" cy="32" r="14" fill="#0284c7"/>
      <text x="25" y="37" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1</text>
      <text x="50" y="24" font-size="11" font-weight="bold" fill="#38bdf8">Step 1: Interface &amp; Speed Audit</text>
      <text x="50" y="42" font-size="8.8" fill="#cbd5e1">Verify host has matching NIC (e.g. 10 GbE PCIe card for Cat6a / SFP+ for Fiber).</text>
    </g>

    <!-- Step 2 -->
    <g transform="translate(20, 118)">
      <rect width="380" height="65" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <circle cx="25" cy="32" r="14" fill="#0284c7"/>
      <text x="25" y="37" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2</text>
      <text x="50" y="24" font-size="11" font-weight="bold" fill="#38bdf8">Step 2: Safe Cable Pathing</text>
      <text x="50" y="42" font-size="8.8" fill="#cbd5e1">Route away from heavy power conduits, HVAC motors, and fluorescent lights (EMI).</text>
    </g>

    <!-- Step 3 -->
    <g transform="translate(20, 194)">
      <rect width="380" height="65" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <circle cx="25" cy="32" r="14" fill="#0284c7"/>
      <text x="25" y="37" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3</text>
      <text x="50" y="24" font-size="11" font-weight="bold" fill="#38bdf8">Step 3: Mechanical Snap &amp; Latch</text>
      <text x="50" y="42" font-size="8.8" fill="#cbd5e1">Insert plug until plastic click-tab locks securely; prevents loose contact jitter.</text>
    </g>

    <!-- Step 4 -->
    <g transform="translate(20, 270)">
      <rect width="380" height="65" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
      <circle cx="25" cy="32" r="14" fill="#059669"/>
      <text x="25" y="37" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">4</text>
      <text x="50" y="24" font-size="11" font-weight="bold" fill="#34d399">Step 4: Link &amp; Throughput Verification</text>
      <text x="50" y="42" font-size="8.8" fill="#cbd5e1">Inspect LED indicators, test link duplex, run ping tests &amp; check packet loss.</text>
    </g>
  </g>
</svg>
""")

SVG_MEDIA_SELECTION_DECISION_TREE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Engineering Decision Tree: Transmission Media Selection</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Systematic Branching for Distance, EMI Environment, Mobility, Bandwidth, and Total Cost of Ownership</text>

  <!-- Start Node -->
  <g transform="translate(380, 90)">
    <rect width="200" height="38" rx="8" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="100" y="24" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Start: Media Selection Audit</text>
  </g>

  <!-- Arrow down to Decision 1 -->
  <line x1="480" y1="128" x2="480" y2="155" stroke="#38bdf8" stroke-width="2"/>
  <polygon points="475,155 485,155 480,162" fill="#38bdf8"/>

  <!-- Decision 1: Mobility Needed? -->
  <g transform="translate(360, 165)">
    <polygon points="120,0 240,30 120,60 0,30" fill="#1e1b4b" stroke="#818cf8" stroke-width="1.5"/>
    <text x="120" y="27" font-size="10.5" font-weight="bold" fill="#c7d2fe" text-anchor="middle">Is Device Mobile /</text>
    <text x="120" y="42" font-size="10" fill="#c7d2fe" text-anchor="middle">Cables Impossible?</text>
  </g>

  <!-- Branch YES (Mobile -> Wireless) -->
  <line x1="600" y1="195" x2="720" y2="195" stroke="#34d399" stroke-width="2"/>
  <text x="645" y="188" font-size="10" font-weight="bold" fill="#34d399">YES</text>
  
  <g transform="translate(720, 165)">
    <rect width="190" height="65" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="1.5"/>
    <text x="95" y="20" font-size="10.5" font-weight="bold" fill="#34d399" text-anchor="middle">CHOOSE WIRELESS</text>
    <text x="95" y="36" font-size="8.5" fill="#a7f3d0" text-anchor="middle">&#8226; &lt; 100m: Wi-Fi 6 / Bluetooth</text>
    <text x="95" y="50" font-size="8.5" fill="#a7f3d0" text-anchor="middle">&#8226; &gt; 1km: Microwave LoS / Satellite</text>
  </g>

  <!-- Branch NO (Wired path) -->
  <line x1="480" y1="225" x2="480" y2="255" stroke="#f59e0b" stroke-width="2"/>
  <polygon points="475,255 485,255 480,262" fill="#f59e0b"/>
  <text x="495" y="245" font-size="10" font-weight="bold" fill="#f59e0b">NO (Fixed)</text>

  <!-- Decision 2: Distance > 100m? -->
  <g transform="translate(360, 265)">
    <polygon points="120,0 240,30 120,60 0,30" fill="#1e1b4b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="120" y="27" font-size="10.5" font-weight="bold" fill="#fde68a" text-anchor="middle">Is Segment Distance</text>
    <text x="120" y="42" font-size="10" fill="#fde68a" text-anchor="middle">&gt; 100 Meters?</text>
  </g>

  <!-- Branch YES (>100m -> Fiber Optic) -->
  <line x1="600" y1="295" x2="720" y2="295" stroke="#34d399" stroke-width="2"/>
  <text x="645" y="288" font-size="10" font-weight="bold" fill="#34d399">YES</text>

  <g transform="translate(720, 265)">
    <rect width="190" height="65" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="1.5"/>
    <text x="95" y="20" font-size="10.5" font-weight="bold" fill="#34d399" text-anchor="middle">CHOOSE FIBER-OPTIC</text>
    <text x="95" y="36" font-size="8.5" fill="#a7f3d0" text-anchor="middle">&#8226; Multi-Mode: 100m - 2 km</text>
    <text x="95" y="50" font-size="8.5" fill="#a7f3d0" text-anchor="middle">&#8226; Single-Mode: 2 km - 100 km</text>
  </g>

  <!-- Branch NO (<=100m) -->
  <line x1="480" y1="325" x2="480" y2="355" stroke="#38bdf8" stroke-width="2"/>
  <polygon points="475,355 485,355 480,362" fill="#38bdf8"/>
  <text x="495" y="345" font-size="10" font-weight="bold" fill="#38bdf8">NO (≤100m)</text>

  <!-- Decision 3: Heavy EMI / Generators Present? -->
  <g transform="translate(360, 365)">
    <polygon points="120,0 240,30 120,60 0,30" fill="#1e1b4b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="120" y="27" font-size="10.5" font-weight="bold" fill="#fca5a5" text-anchor="middle">Heavy EMI / Industrial</text>
    <text x="120" y="42" font-size="10" fill="#fca5a5" text-anchor="middle">Motors Present?</text>
  </g>

  <!-- Branch YES (Heavy EMI -> STP or Fiber) -->
  <line x1="600" y1="395" x2="720" y2="395" stroke="#ef4444" stroke-width="2"/>
  <text x="645" y="388" font-size="10" font-weight="bold" fill="#ef4444">YES</text>

  <g transform="translate(720, 365)">
    <rect width="190" height="65" rx="8" fill="#450a0a" stroke="#f87171" stroke-width="1.5"/>
    <text x="95" y="20" font-size="10.5" font-weight="bold" fill="#fca5a5" text-anchor="middle">CHOOSE STP OR FIBER</text>
    <text x="95" y="36" font-size="8.5" fill="#fecaca" text-anchor="middle">&#8226; STP: Foil shields block motors.</text>
    <text x="95" y="50" font-size="8.5" fill="#fecaca" text-anchor="middle">&#8226; Fiber: 100% total immunity.</text>
  </g>

  <!-- Branch NO (Clean Environment -> UTP) -->
  <line x1="360" y1="395" x2="240" y2="395" stroke="#34d399" stroke-width="2"/>
  <text x="280" y="388" font-size="10" font-weight="bold" fill="#34d399">NO</text>

  <g transform="translate(50, 365)">
    <rect width="190" height="65" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="1.5"/>
    <text x="95" y="20" font-size="10.5" font-weight="bold" fill="#34d399" text-anchor="middle">CHOOSE UTP (Cat5e/6)</text>
    <text x="95" y="36" font-size="8.5" fill="#a7f3d0" text-anchor="middle">&#8226; Standard office desktops.</text>
    <text x="95" y="50" font-size="8.5" fill="#a7f3d0" text-anchor="middle">&#8226; Lowest cost, high flexibility.</text>
  </g>

  <!-- Summary Legend Footer -->
  <g transform="translate(50, 460)">
    <text x="0" y="0" font-size="9" fill="#94a3b8">Key Tradeoff: Fiber offers infinite bandwidth &amp; zero EMI but has high initial fusion cost • UTP offers lowest TCO under 100m • Wireless enables universal user mobility.</text>
  </g>
</svg>
""")

SVG_ETHERNET_PINOUT_AND_TRANSCEIVERS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Ethernet RJ-45 Color Pinouts (T568A vs. T568B) &amp; Optical Transceivers</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Straight-Through vs. Crossover Wiring Standards and Hot-Swappable SFP+ Optical Modules</text>

  <!-- Left: T568A vs T568B Pinout Standards -->
  <g transform="translate(45, 90)">
    <rect width="420" height="390" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="420" height="30" rx="8" fill="#0284c7"/>
    <text x="210" y="20" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">TIA/EIA-568A vs. TIA/EIA-568B RJ-45 PINOUTS</text>

    <!-- T568A Column -->
    <g transform="translate(20, 45)">
      <rect width="180" height="230" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="90" y="22" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">T568A Standard</text>
      <text x="15" y="45" font-size="8.5" fill="#e2e8f0">1. White/Green</text>
      <text x="15" y="65" font-size="8.5" fill="#22c55e">2. Green</text>
      <text x="15" y="85" font-size="8.5" fill="#e2e8f0">3. White/Orange</text>
      <text x="15" y="105" font-size="8.5" fill="#3b82f6">4. Blue</text>
      <text x="15" y="125" font-size="8.5" fill="#e2e8f0">5. White/Blue</text>
      <text x="15" y="145" font-size="8.5" fill="#f97316">6. Orange</text>
      <text x="15" y="165" font-size="8.5" fill="#e2e8f0">7. White/Brown</text>
      <text x="15" y="185" font-size="8.5" fill="#a16207">8. Brown</text>
      <text x="90" y="215" font-size="8" fill="#94a3b8" text-anchor="middle">US Govt standard</text>
    </g>

    <!-- T568B Column -->
    <g transform="translate(220, 45)">
      <rect width="180" height="230" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="90" y="22" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">T568B Standard (Global)</text>
      <text x="15" y="45" font-size="8.5" fill="#e2e8f0">1. White/Orange</text>
      <text x="15" y="65" font-size="8.5" fill="#f97316">2. Orange</text>
      <text x="15" y="85" font-size="8.5" fill="#e2e8f0">3. White/Green</text>
      <text x="15" y="105" font-size="8.5" fill="#3b82f6">4. Blue</text>
      <text x="15" y="125" font-size="8.5" fill="#e2e8f0">5. White/Blue</text>
      <text x="15" y="145" font-size="8.5" fill="#22c55e">6. Green</text>
      <text x="15" y="165" font-size="8.5" fill="#e2e8f0">7. White/Brown</text>
      <text x="15" y="185" font-size="8.5" fill="#a16207">8. Brown</text>
      <text x="90" y="215" font-size="8" fill="#38bdf8" text-anchor="middle">Commercial standard</text>
    </g>

    <!-- Bottom Cable Rule -->
    <g transform="translate(20, 290)">
      <rect width="380" height="85" rx="6" fill="#1e1b4b" stroke="#818cf8" stroke-width="1"/>
      <text x="190" y="20" font-size="10.5" font-weight="bold" fill="#c7d2fe" text-anchor="middle">Cable Construction Rules</text>
      <text x="10" y="40" font-size="9" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#38bdf8">Straight-Through (568B to 568B)</tspan>: PC to Switch, Switch to Router.</text>
      <text x="10" y="58" font-size="9" fill="#f59e0b">&#8226; <tspan font-weight="bold" fill="#fbbf24">Crossover (568A to 568B)</tspan>: PC to PC, Switch to Switch.</text>
      <text x="10" y="74" font-size="8.5" fill="#94a3b8">&#8226; Modern Gigabit ports use Auto-MDIX to detect cable type automatically.</text>
    </g>
  </g>

  <!-- Right: SFP+ Optical Transceiver & Fiber Modules -->
  <g transform="translate(495, 90)">
    <rect width="420" height="390" rx="12" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="420" height="30" rx="8" fill="#7e22ce"/>
    <text x="210" y="20" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">SFP / SFP+ OPTICAL TRANSCEIVER MODULES</text>

    <!-- Graphic -->
    <g transform="translate(30, 50)">
      <rect width="360" height="130" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="1.5"/>
      <!-- SFP Body -->
      <rect x="25" y="30" width="220" height="70" rx="6" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
      <rect x="25" y="30" width="60" height="70" rx="4" fill="#334155"/>
      <circle cx="55" cy="50" r="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
      <circle cx="55" cy="80" r="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="55" y="53" font-size="7" fill="#38bdf8" text-anchor="middle">Tx (Laser)</text>
      <text x="55" y="83" font-size="7" fill="#38bdf8" text-anchor="middle">Rx (Photo)</text>
      <text x="155" y="60" font-size="10.5" font-weight="bold" fill="#ffffff">10G SFP+ Optical Module</text>
      <text x="155" y="78" font-size="8.5" fill="#cbd5e1">1310nm Single-Mode 10km</text>

      <!-- Duplex LC Fiber Connector -->
      <rect x="265" y="42" width="70" height="46" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="300" y="68" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">LC Duplex</text>
    </g>

    <!-- Transceiver Properties -->
    <g transform="translate(30, 200)">
      <text x="0" y="15" font-size="11" font-weight="bold" fill="#c084fc">&#128737; Optical Transceiver Engineering:</text>
      <text x="0" y="35" font-size="9.5" fill="#e2e8f0">&#8226; Hot-Swappable: Can be inserted or removed without powering down switch.</text>
      <text x="0" y="55" font-size="9.5" fill="#e2e8f0">&#8226; Conversion: Changes electrical bus signals into laser pulses &amp; vice versa.</text>
      <text x="0" y="75" font-size="9.5" fill="#e2e8f0">&#8226; Form Factors: SFP (1 Gbps), SFP+ (10 Gbps), QSFP28 (100 Gbps).</text>
      <text x="0" y="95" font-size="9.5" fill="#e2e8f0">&#8226; Connector Standard: Duplex LC (Lucent Connector) with push-pull latch.</text>
      <text x="0" y="115" font-size="9" fill="#94a3b8">&#8226; Used in core switches, server racks, and long-distance fiber uplinks.</text>
    </g>
  </g>
</svg>
""")

SVG_STRUCTURED_CABLING_CAMPUS_TOPOLOGY = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">ANSI/TIA-568 Structured Cabling Architecture</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Hierarchical Subsystems: Campus Backbone (MDF), Floor Distribution (IDF), Horizontal UTP, and Work Area Outlets</text>

  <!-- Left: Campus Backbone (MDF in Server Room) -->
  <g transform="translate(45, 95)">
    <rect width="260" height="385" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="260" height="28" rx="6" fill="#0284c7"/>
    <text x="130" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1. MAIN CROSS-CONNECT (MDF)</text>
    
    <g transform="translate(15, 45)">
      <rect width="230" height="110" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <text x="115" y="22" font-size="10.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Central Server Room</text>
      <text x="15" y="45" font-size="9" fill="#cbd5e1">&#8226; Core Layer 3 Switch &amp; Routers</text>
      <text x="15" y="65" font-size="9" fill="#cbd5e1">&#8226; Enterprise Servers &amp; Firewalls</text>
      <text x="15" y="85" font-size="9" fill="#cbd5e1">&#8226; Fiber Patch Panel Enclosure</text>
    </g>

    <g transform="translate(15, 170)">
      <text x="0" y="15" font-size="10" font-weight="bold" fill="#38bdf8">&#127760; Entrance Facility:</text>
      <text x="0" y="32" font-size="8.5" fill="#cbd5e1">ISP WAN Fiber demarcation point (NOFBI / Safaricom).</text>
      <text x="0" y="55" font-size="10" font-weight="bold" fill="#38bdf8">&#9889; UPS Power Backup:</text>
      <text x="0" y="72" font-size="8.5" fill="#cbd5e1">Dual online UPS units with diesel generator tie-in.</text>
    </g>
  </g>

  <!-- Middle: Backbone & IDF Distribution -->
  <g transform="translate(335, 95)">
    <rect width="290" height="385" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="290" height="28" rx="6" fill="#059669"/>
    <text x="145" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2. BACKBONE &amp; IDF CLOSETS</text>

    <g transform="translate(15, 45)">
      <rect width="260" height="75" rx="6" fill="#1e1b4b" stroke="#818cf8" stroke-width="1"/>
      <text x="130" y="20" font-size="10.5" font-weight="bold" fill="#c7d2fe" text-anchor="middle">Inter-Building Fiber Backbone</text>
      <text x="10" y="40" font-size="8.5" fill="#e2e8f0">&#8226; Singlemode/Multimode 10G/40G Fiber</text>
      <text x="10" y="58" font-size="8.5" fill="#e2e8f0">&#8226; Underground armored conduit (immune to lightning)</text>
    </g>

    <g transform="translate(15, 135)">
      <rect width="260" height="110" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
      <text x="130" y="22" font-size="10.5" font-weight="bold" fill="#34d399" text-anchor="middle">Intermediate Cross-Connect (IDF)</text>
      <text x="10" y="45" font-size="9" fill="#cbd5e1">&#8226; Floor Telecommunications Closet</text>
      <text x="10" y="65" font-size="9" fill="#cbd5e1">&#8226; 24/48-Port Cat6 Patch Panels</text>
      <text x="10" y="85" font-size="9" fill="#cbd5e1">&#8226; PoE+ Access Switches for Wi-Fi APs</text>
    </g>

    <g transform="translate(15, 260)">
      <text x="0" y="15" font-size="10" font-weight="bold" fill="#34d399">&#128207; 90-Meter Permanent Link Rule:</text>
      <text x="0" y="32" font-size="8.5" fill="#cbd5e1">Max solid copper run from patch panel to wall jack is 90 meters (+10m patch cords = 100m channel).</text>
    </g>
  </g>

  <!-- Right: Horizontal Cabling & Work Areas -->
  <g transform="translate(655, 95)">
    <rect width="260" height="385" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="260" height="28" rx="6" fill="#7e22ce"/>
    <text x="130" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">3. HORIZONTAL &amp; WORK AREA</text>

    <g transform="translate(15, 45)">
      <rect width="230" height="110" rx="6" fill="#1e293b" stroke="#c084fc" stroke-width="1"/>
      <text x="115" y="22" font-size="10.5" font-weight="bold" fill="#c084fc" text-anchor="middle">Horizontal Cat6 Runs</text>
      <text x="10" y="45" font-size="9" fill="#cbd5e1">&#8226; Ceiling cable trays / Wall raceways</text>
      <text x="10" y="65" font-size="9" fill="#cbd5e1">&#8226; Solid-core 100% pure copper</text>
      <text x="10" y="85" font-size="9" fill="#cbd5e1">&#8226; Strict 4-pair twist preservation</text>
    </g>

    <g transform="translate(15, 170)">
      <rect width="230" height="95" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
      <text x="115" y="22" font-size="10.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">Work Area Outlets (WAO)</text>
      <text x="10" y="45" font-size="9" fill="#cbd5e1">&#8226; Dual RJ-45 Wall Faceplates</text>
      <text x="10" y="65" font-size="9" fill="#cbd5e1">&#8226; Stranded flexible patch cords</text>
      <text x="10" y="85" font-size="9" fill="#cbd5e1">&#8226; Connects PCs, Printers, VoIP phones</text>
    </g>

    <g transform="translate(15, 280)">
      <text x="0" y="15" font-size="9" fill="#94a3b8">&#10003; Full TIA-568 compliance guarantees 10 Gbps capability and simplified maintenance.</text>
    </g>
  </g>
</svg>
""")

# =====================================================================
# CURRICULUM DEFINITIONS FOR GRADE 10 TOPIC 9
# =====================================================================

def build_topic9_curriculum():
    return [
        # =====================================================================
        # LEARNING UNIT 1: Transmission Concepts, Signals, and Guided Media
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Transmission Concepts, Signals, and Guided Physical Media",
            "unit_description": "Foundational physics of transmission media, analog vs. digital signals, modulation techniques, and guided physical cabling including UTP, STP, coaxial, and fiber-optics.",
            "lesson_title": "Data Transmission Concepts and Guided Media",
            "pages": [
                # Page 1: Transmission Pathways & The Water Pipeline Analogy
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Transmission Pathways & Signals",
                        "content": {
                            "goal": "Understand how digital information travels between computing devices, master the distinction between guided and unguided transmission media, and analyze core metrics including bandwidth and signal encoding."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 'Water Pipeline' Analogy: Guided vs. Unguided Media",
                        "content": {
                            "text": "Imagine a municipal clean water system. To deliver clean water from a high-capacity central reservoir to hundreds of individual homes, the city lays down an intricate network of heavy steel mains and copper pipes. These pipes confine, direct, and guide the physical flow of water along a very specific, bounded geometric path directly to each tap.\n\nHowever, if you want to water a large open park or lawn, you do not lay down fixed copper pipes to every square inch of grass. Instead, you turn on an overhead sprinkler. The sprinkler sprays water droplets freely through the open air, distributing them across a broad physical space without a physical pipe guiding every drop.\n\nIn computer networking, **transmission media** represent these physical pathways. They are the channels that carry data signals from a sender to a receiver. We divide them into two primary categories based on how they control these signals:\n\n- **Guided Media (Wired)**: Physical wires or optical glass fibers that physically bound, shield, and guide data signals along a specific, bounded path (like water pipes).\n- **Unguided Media (Wireless)**: Electromagnetic waves propagated through the air, vacuum, or water, dispersing signals across a broad physical space (like water sprinklers)."
                        }
                    },
                    {
                        "type": "core_definitions",
                        "title": "Core Technical Definitions",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Transmission Medium",
                                    "definition": "The physical pathway or electromagnetic environment through which data signals are propagated from a sender to a receiver in a communication system."
                                },
                                {
                                    "term": "Guided Medium",
                                    "definition": "A transmission medium where physical boundaries (such as copper wires or silica glass fibers) confine and guide electromagnetic waves along a specific geometric path."
                                },
                                {
                                    "term": "Signal",
                                    "definition": "An electromagnetic or electrical representation of raw data (such as varying voltages, light pulses, or radio frequencies) suitable for transmission."
                                },
                                {
                                    "term": "Bandwidth",
                                    "definition": "The maximum capacity of a transmission medium to carry data over a given unit of time, typically measured in bits per second (bps, Mbps, Gbps) or frequency range (Hertz)."
                                }
                            ]
                        }
                    }
                ],

                # Page 2: Signal Foundations & Modulation
                [
                    {
                        "type": "concept_explanation",
                        "title": "Understanding Signals: Continuous Analog vs. Discrete Digital",
                        "content": {
                            "text": "Before raw data can travel across any physical or wireless medium, it must be encoded into a signal. Computing systems utilize two primary types of signals:\n\n- **Analog Signals**: Continuous electromagnetic waves that vary smoothly in amplitude and frequency over time (such as acoustic sound waves, analog radio broadcasts, or traditional telephone copper currents).\n- **Digital Signals**: Discrete, discontinuous pulses representing binary 0s and 1s. They transition sharply between distinct voltage levels (e.g., $0\\text{V}$ for binary '0' and $+5\\text{V}$ for binary '1').\n\n```\nAnalog Waveform:   ~\\_/\\_/\\_  (Continuous, smooth sine waves)\nDigital Waveform:  |_|\\_|_|\\_  (Discontinuous, sharp square pulses)\n```\n\nTo transmit digital data over continuous analog media (such as long-distance telephone lines, cable lines, or open airwaves), computers must perform **encoding** and **modulation**."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Signal Waveforms & Carrier Modulation Techniques",
                        "content": {
                            "caption": "Comparison of continuous analog sine waves vs. discrete digital square pulses, accompanied by Amplitude (AM), Frequency (FM), and Phase Modulation (PM) mechanisms.",
                            "svg_content": SVG_SIGNAL_ENCODING_MODULATION
                        }
                    },
                    {
                        "type": "deep_dive",
                        "title": "Deep Dive: Carrier Modulation Mechanics (AM, FM, PM)",
                        "content": {
                            "text": "Modulation is the process of altering a high-frequency carrier wave to superimpose digital binary data onto it:\n\n- **Amplitude Modulation (AM)**: The height (peak voltage) of the carrier wave is varied in accordance with the binary data bits, while frequency and phase remain fixed.\n- **Frequency Modulation (FM)**: The frequency (number of wave cycles per second in Hertz) is varied. Binary 1 is represented by dense high-frequency cycles, while binary 0 is represented by lower frequency cycles.\n- **Phase Modulation (PM / PSK)**: The phase (the starting angle of the wave) is abruptly shifted (e.g., a $180^\\circ$ reversal) whenever the data transitions from 0 to 1 or vice-versa.\n\nAt the receiving end, a **Demodulator** (inside a Modem) strips the carrier wave away, reconstructing the original stream of binary 1s and 0s."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Signals & Modulation",
                        "content": {
                            "question": "Which process converts a high-frequency analog carrier wave by varying its amplitude, frequency, or phase to superimpose digital computer data onto it?",
                            "options": [
                                "Modulation",
                                "Attenuation",
                                "Refraction",
                                "Crosstalk"
                            ],
                            "correct_answer": "Modulation",
                            "explanation": "Modulation modifies a continuous carrier wave's properties (AM, FM, or PM) so that digital data pulses can travel over analog transmission channels. Demodulation reverses this at the receiver."
                        }
                    }
                ],

                # Page 3: Guided Media Engineering: Twisted-Pair & Coaxial
                [
                    {
                        "type": "concept_explanation",
                        "title": "Guided Media Engineering: Twisted-Pair & Coaxial Cables",
                        "content": {
                            "text": "Guided transmission media utilize physical metallic conductors or optical waveguides to direct electrical currents or light pulses along fixed paths.\n\n### 1. Twisted-Pair Cabling (UTP & STP)\nTwisted-pair cabling is the universal standard for Local Area Networks (LANs). It consists of color-coded insulated copper wire strands twisted into pairs.\n\n- **The Physics of Twisting**: When electrical current flows through a wire, it radiates a small electromagnetic field that induces unwanted electrical noise (**crosstalk**) in nearby wires. By twisting the two wires of a pair tightly together, any external electromagnetic interference affects both wires identically. Network receivers measure only the *difference* in voltage between the pair (differential signaling), causing the identical noise on both wires to cancel out completely.\n- **UTP (Unshielded Twisted Pair)**: Consists of twisted pairs enclosed only in a flexible plastic jacket. It is inexpensive, lightweight, and easy to terminate, but susceptible to strong electromagnetic noise. Standard in office LANs (Cat5e, Cat6, Cat6a).\n- **STP (Shielded Twisted Pair)**: Wraps each twisted pair in individual metallic foil shields, with an outer braided metal mesh. It provides superior protection against heavy industrial electromagnetic interference (EMI) from heavy generators and motors, but is thicker, stiffer, and more expensive.\n- **Connector**: Standardized with **RJ-45 (Registered Jack 45)** modular click-latching plugs containing 8 gold-plated contact pins.\n\n### 2. Coaxial Cabling\nCoaxial cable features a concentric four-layer physical design:\n1. **Central Core**: Solid or stranded copper conductor carrying high-frequency electrical signals.\n2. **Dielectric Insulator**: Thick plastic spacer maintaining constant separation.\n3. **Braided Metallic Shield**: Woven mesh that blocks external EMI and serves as electrical ground.\n4. **Outer PVC Jacket**: Tough protective exterior sheath.\n\nBecause the central core and shield share the exact same geometric axis (*co-axial*), external noise is shielded and high frequencies are trapped inside the dielectric. Standard in Cable TV (CATV), broadband cable modems, and legacy Ethernet (using BNC and F-type connectors)."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Guided Media Cross-Sections & Internal Layering",
                        "content": {
                            "caption": "Cross-sectional engineering diagrams of Shielded Twisted Pair (STP), Coaxial Cable concentric layers, and Fiber-Optic Total Internal Reflection.",
                            "svg_content": SVG_GUIDED_MEDIA_CROSS_SECTIONS
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Unshielded Twisted Pair (UTP) Network Cable",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/UTP_cable.jpg/800px-UTP_cable.jpg",
                            "caption": "Cat5e Unshielded Twisted Pair (UTP) network cable displaying four color-coded twisted pairs stripped from the outer jacket.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Twisted Pair, Coaxial & Fiber Optic Cables Explained",
                        "content": {
                            "youtube_id": "w_qK857nQG8",
                            "url": "https://www.youtube.com/watch?v=w_qK857nQG8",
                            "description": "Comprehensive engineering overview explaining how UTP, STP, Coaxial, and Optical Fiber cables function and their physical performance limits."
                        }
                    }
                ],

                # Page 4: Optical Transmission: Fiber-Optics
                [
                    {
                        "type": "concept_explanation",
                        "title": "Optical Transmission: Fiber-Optics & Total Internal Reflection",
                        "content": {
                            "text": "Fiber-optic cabling transmits digital information as microscopic pulses of light (photons) rather than electrical current (electrons). It represents the highest-performance guided transmission medium in modern computer science.\n\n### The Physics of Total Internal Reflection (TIR)\nAt the center of a fiber-optic cable is a microscopically thin **Core** made of ultra-pure silica glass. Surrounding the core is a glass **Cladding** layer manufactured with a slightly lower refractive index ($n_2 < n_1$).\n\nWhen a laser or LED injects light into the core at an angle shallower than the critical angle, the light hits the core-cladding boundary and is reflected 100% back into the core without escaping. This optical phenomenon is **Total Internal Reflection** (TIR). It allows light pulses to travel through curved glass strands over tens of kilometers with minimal loss.\n\n### Key Advantages of Fiber-Optics:\n- **100% Immune to EMI / RFI**: Because photons carry no electrical charge, fiber cables are completely unaffected by high-voltage lines, heavy industrial motors, radio transmitters, or atmospheric lightning strikes.\n- **Immense Bandwidth**: Supports data rates exceeding $100\\text{ Gbps}$ to $800\\text{ Gbps}$ per strand using wavelength division multiplexing.\n- **Extended Reach**: Carries signals up to $100\\text{ km}$ without intermediate signal regenerators (repeaters).\n\n### Single-Mode vs. Multi-Mode Fiber:\n- **Single-Mode Fiber (SMF)**: Extremely narrow core (~$9\\,\\mu\\text{m}$) using single-wavelength lasers. Light travels along a single direct path, eliminating modal dispersion. Spans distances up to $100\\text{ km}$; standard for long-haul telecommunications and subsea continental backbones.\n- **Multi-Mode Fiber (MMF)**: Wider core (~$50 - 62.5\\,\\mu\\text{m}$) utilizing economical LED transmitters. Multiple light rays bounce down the core simultaneously along different reflection angles. Effective for distances up to $2\\text{ km}$ inside enterprise data centers and campus backbones."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Illuminated Multi-Strand Optical Fiber Cable Bundle",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Fiber_optic_illuminated.jpg/800px-Fiber_optic_illuminated.jpg",
                            "caption": "Figure 9.3: Bundle of illuminated glass optical fibers demonstrating total internal reflection and high-bandwidth light transmission.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Optical Transmission Trace Problem",
                        "content": {
                            "scenario": "A campus network engineer is designing a backbone link between two university buildings located 1.2 kilometers apart. The backbone must support 10 Gbps throughput without repeaters.",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Evaluate Copper Twisted-Pair (UTP / STP)",
                                    "description": "Standard Cat6/Cat6a UTP has an absolute physical segment distance limit of 100 meters due to copper attenuation. At 1,200 meters, signal loss is total. Copper UTP is ruled out."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Evaluate Multi-Mode Optical Fiber (MMF)",
                                    "description": "Multi-Mode fiber (OM3/OM4) comfortably supports 10 Gbps up to 300 - 550 meters, and standard 1 Gbps up to 2,000 meters. However, at 10 Gbps over 1.2 km, modal dispersion causes pulse overlap."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Select Single-Mode Optical Fiber (SMF)",
                                    "description": "Single-Mode fiber with a 1310nm laser transceiver easily spans up to 10 km at 10 Gbps with near-zero dispersion, providing future-proof expansion to 40 Gbps or 100 Gbps. SMF is the correct engineering choice."
                                }
                            ],
                            "conclusion": "Single-Mode Fiber (SMF) is selected due to its ability to handle 10+ Gbps over 1.2 km without intermediate repeaters while remaining 100% immune to outdoor lightning and electromagnetic noise."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Fiber-Optic Physics",
                        "content": {
                            "question": "Which optical phenomenon allows light pulses to travel down a glass fiber core for kilometers without escaping into the cladding?",
                            "options": [
                                "Total Internal Reflection",
                                "Electrostatic Induction",
                                "Amplitude Modulation",
                                "Magnetic Flux Permeability"
                            ],
                            "correct_answer": "Total Internal Reflection",
                            "explanation": "Total Internal Reflection occurs when light inside a denser medium (glass core) hits the boundary of a less dense medium (cladding) at an angle greater than the critical angle, reflecting 100% of the light back into the core."
                        }
                    }
                ],

                # Page 5: Comparative Synthesis & Interactive Selection Lab
                [
                    {
                        "type": "comparison_table",
                        "title": "Comparative Synthesis: Guided Transmission Media",
                        "content": {
                            "headers": ["Attribute", "Twisted-Pair (UTP)", "Shielded Twisted Pair (STP)", "Coaxial Cable", "Fiber-Optic (SMF/MMF)"],
                            "rows": [
                                ["Data Rate (Typical)", "10 Mbps – 10 Gbps", "100 Mbps – 10 Gbps", "10 Mbps – 100 Mbps", "10 Gbps – 100+ Gbps"],
                                ["Max Segment Length", "100 meters (Cat6)", "100 meters (Cat6a)", "185m (Thin) – 500m (Thick)", "2 km (MMF) to 100 km (SMF)"],
                                ["EMI / Noise Resistance", "Low (Susceptible to noise)", "High (Foil/Braid shielded)", "Moderate to High", "Absolute (100% Immune)"],
                                ["Physical Flexibility", "High (Easy to route)", "Moderate (Stiffer)", "Low to Moderate (Stiff)", "Low (Fragile glass core)"],
                                ["Installation Cost", "Very Low (Inexpensive)", "Moderate", "Moderate", "High (Requires fusion splicers)"],
                                ["Primary Connector", "RJ-45 (8-pin)", "RJ-45 (Shielded)", "BNC / F-Type", "SC, LC, ST Optical Plugs"]
                            ]
                        }
                    },
                    {
                        "type": "scenario_practice",
                        "title": "Interactive Class Activity: The Nairobi Hospital Media Selector",
                        "content": {
                            "scenario": "A regional hospital in Nairobi is deploying three distinct network subsystems. You must select the ideal guided medium for each link:",
                            "cases": [
                                {
                                    "subsystem": "Subsystem 1: MRI Imaging Room to Server Room (50m)",
                                    "environment": "Massive electromagnetic fields produced by high-voltage MRI superconducting magnets.",
                                    "recommended_medium": "STP (Shielded Twisted Pair) or Fiber-Optic Cable",
                                    "rationale": "High-voltage MRI equipment produces intense EMI that corrupts standard UTP. STP's metallic foil shields or Fiber-Optic non-metallic glass completely eliminates interference."
                                },
                                {
                                    "subsystem": "Subsystem 2: Inter-Building Core Backbone (800m)",
                                    "environment": "Spans 800 meters across open outdoor terrain between hospital wings.",
                                    "recommended_medium": "Single-Mode or Multi-Mode Fiber-Optic Cable",
                                    "rationale": "800m exceeds copper's 100m distance limit by 8x. Fiber easily handles 800m with zero attenuation and protects against outdoor lightning strikes."
                                },
                                {
                                    "subsystem": "Subsystem 3: Administrative Desktop Workstations (20m)",
                                    "environment": "Standard office cubicles connecting 40 desktop computers to switches on a tight budget.",
                                    "recommended_medium": "UTP (Unshielded Twisted Pair - Cat6)",
                                    "rationale": "Distances are well under 100m, electromagnetic noise is low, and UTP offers the lowest cable and termination costs."
                                }
                            ]
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Guided Media Properties",
                        "content": {
                            "text": "1. **Twisted-Pair (UTP/STP)**: Relies on differential signaling to cancel EMI/crosstalk; 100m segment limit.\\n2. **Coaxial**: Four concentric layers; high noise immunity for broadband/CATV.\\n3. **Fiber-Optics**: 100% immune to EMI and lightning surges; operates via Total Internal Reflection for gigabit/terabit speeds across kilometers."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Media Distance Limits",
                        "content": {
                            "question": "What is the standardized maximum segment length for standard Cat6 Unshielded Twisted Pair (UTP) Ethernet cabling before attenuation requires a repeater or switch?",
                            "options": [
                                "100 meters",
                                "500 meters",
                                "1,000 meters",
                                "10 kilometers"
                            ],
                            "correct_answer": "100 meters",
                            "explanation": "Ethernet standards (TIA/EIA-568) specify a strict 100-meter maximum channel length for twisted-pair copper cables (90m solid horizontal run + 10m patch cables) to prevent signal attenuation and timing errors."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Guided Media Physical Connectors",
                        "content": {
                            "question": "Which connector standard features 8 gold-plated pins and a plastic click-latch mechanism to connect twisted-pair Ethernet cables to network cards?",
                            "options": [
                                "RJ-45",
                                "BNC",
                                "F-Type",
                                "VGA"
                            ],
                            "correct_answer": "RJ-45",
                            "explanation": "The RJ-45 (Registered Jack 45) connector is the standard modular plug used for 4-pair (8-wire) twisted-pair Ethernet networks."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LEARNING UNIT 2: Unguided (Wireless) Media and Environmental Factors
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Unguided (Wireless) Media and Environmental Transmission Factors",
            "unit_description": "Electromagnetic spectrum allocation, radio waves, microwaves, satellite architectures (GEO vs LEO), infrared transmission, and the 5 critical factors that degrade wireless signals.",
            "lesson_title": "Wireless Media Technologies and Transmission Degradation",
            "pages": [
                # Page 1: The Electromagnetic Spectrum & Wireless Paradigms
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Wireless Media & Propagation Mechanics",
                        "content": {
                            "goal": "Examine how unguided media propagate electromagnetic waves through the air, compare Radio, Microwave, and Infrared technologies, and analyze environmental factors causing signal degradation."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 'Airwave Highway' Analogy & Unguided Media",
                        "content": {
                            "text": "Imagine a crowded stadium filled with 50,000 spectators. If everyone tried to shout messages across the field at the same time on the same acoustic frequency, the result would be a chaotic wall of noise where no individual voice could be decoded.\n\nTo prevent this, human civilization divides the airspace. We assign radio stations to distinct carrier frequencies and allow different groups to communicate using focused light signals (like flashlights) that do not interfere with acoustic audio waves.\n\nIn computer networking, **unguided media** transmit electromagnetic waves through the air, vacuum, or water without physical conductors. Instead of being confined inside a physical pipe, wireless waves radiate outwards through the open environment. To keep wireless communications organized, national and international regulatory bodies partition the **Electromagnetic Spectrum** into distinct frequency bands:\n\n- **Radio Waves (3 kHz – 1 GHz)**: Low to medium frequency waves that propagate omnidirectionally (in all directions). They penetrate non-metallic walls effectively, making them ideal for broadcast radio, mobile cellular networks, and Personal Area Networks (Bluetooth).\n- **Microwaves (1 GHz – 300 GHz)**: High-frequency waves that travel in narrow, focused, straight-line beams (**Line-of-Sight**). They cannot penetrate solid terrain or bend around Earth's curvature. Powers local Wi-Fi (2.4 GHz, 5 GHz), terrestrial dish relays, and satellite links.\n- **Infrared Waves (300 GHz – 400 THz)**: Very high frequency optical signals that cannot penetrate opaque solid objects. Strictly short-range line-of-sight."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "The Electromagnetic Spectrum & Wireless Channel Allocation",
                        "content": {
                            "caption": "Frequency band partitioning from Radio Waves to Infrared, detailing Wi-Fi 2.4 GHz non-overlapping channels (1, 6, 11) and Satellite GEO vs. LEO orbital mechanics.",
                            "svg_content": SVG_ELECTROMAGNETIC_SPECTRUM_WIRELESS
                        }
                    },
                    {
                        "type": "deep_dive",
                        "title": "Deep Dive: Wi-Fi Channel Overlap on 2.4 GHz vs 5 GHz Bands",
                        "content": {
                            "text": "In the $2.4\\text{ GHz}$ Wi-Fi band ($2.400 - 2.4835\\text{ GHz}$), channels are spaced only $5\\text{ MHz}$ apart, but a standard Wi-Fi channel requires $20\\text{ MHz}$ of bandwidth. As a result, adjacent channels overlap heavily.\n\n- **The Non-Overlapping Rule**: Only **Channels 1, 6, and 11** do not overlap. If two neighboring wireless routers use Channel 1 and Channel 2, their signals collide destructively (**adjacent-channel interference**).\n- **The 5 GHz Advantage**: The $5\\text{ GHz}$ band provides a much wider spectrum containing 24+ discrete non-overlapping $20\\text{ MHz}$ channels, enabling vastly higher throughput and zero channel contention in dense deployments."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Enterprise Dual-Band Wireless Access Point (WAP)",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Wireless_access_point.jpg/800px-Wireless_access_point.jpg",
                            "caption": "Figure 9.5: Ceiling-mounted dual-band Wi-Fi access point radiating 2.4 GHz and 5 GHz unguided radio waves.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "How Radio Waves and Wireless Networks Work",
                        "content": {
                            "youtube_id": "BGN_9zV2o64",
                            "url": "https://www.youtube.com/watch?v=BGN_9zV2o64",
                            "description": "Educational guide to the electromagnetic spectrum, RF propagation, Wi-Fi channel allocation, and antenna physics."
                        }
                    }
                ],

                # Page 2: Directional Wireless: Microwaves & Satellite Systems
                [
                    {
                        "type": "concept_explanation",
                        "title": "Directional Microwaves & Satellite Systems",
                        "content": {
                            "text": "Because high-frequency microwaves ($1\\text{ GHz} - 300\\text{ GHz}$) travel in straight lines, they require specialized transmission architectures.\n\n### 1. Terrestrial Microwave Relays\nTerrestrial microwave communication uses high-gain parabolic dish antennas mounted atop high towers or mountain summits. \n- **Line-of-Sight (LoS)**: The sending and receiving dishes must be aimed directly at each other with an unobstructed visual path.\n- **Earth's Curvature Limit**: Because the Earth is spherical, straight microwave beams shoot off into space over long distances. To span hundreds of kilometers across continents, engineers construct **repeater relay stations** every $40 - 50\\text{ km}$ to capture, amplify, and re-transmit the signal.\n\n### 2. Satellite Microwave Systems\nSatellites act as high-altitude microwave relay towers orbiting in space. Ground stations beam high-frequency signals up to the satellite (**Uplink**). The satellite's onboard **transponder** receives the weak signal, amplifies it, converts it to a different frequency to avoid feedback loops, and beams it back down (**Downlink**) over a broad continental coverage area (footprint).\n\n- **Geostationary Earth Orbit (GEO)**: Satellites orbit at exactly $35,786\\text{ km}$ above the equator, orbiting at the same speed as Earth's rotation. They remain fixed relative to ground stations, allowing permanent dish alignment. However, the $70,000+\\text{ km}$ round trip introduces high latency (~$500 - 600\\text{ ms}$).\n- **Low Earth Orbit (LEO)**: Constellations of hundreds or thousands of small satellites orbit close to Earth ($500 - 1,200\\text{ km}$, e.g. Starlink). They deliver high-speed broadband with low latency (~$25 - 40\\text{ ms}$), but ground dishes must dynamically track moving satellites across the sky."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Microwave Relay Communication Tower",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Microwave_relay_tower.jpg/800px-Microwave_relay_tower.jpg",
                            "caption": "Terrestrial telecommunication tower equipped with directional parabolic drum antennas for line-of-sight microwave links.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Satellite Latency",
                        "content": {
                            "question": "Why do Geostationary Orbit (GEO) satellite connections experience significantly higher latency (~500ms) than Low Earth Orbit (LEO) constellations?",
                            "options": [
                                "GEO satellites orbit at 35,786 km, meaning radio waves must travel vast physical distances to space and back.",
                                "GEO satellite signals travel through glass optical fiber cables in space.",
                                "GEO transponders operate exclusively on low-frequency sound waves.",
                                "GEO satellite antennas suffer from total internal reflection inside the ionosphere."
                            ],
                            "correct_answer": "GEO satellites orbit at 35,786 km, meaning radio waves must travel vast physical distances to space and back.",
                            "explanation": "Electromagnetic waves travel at the speed of light (~300,000 km/s). Traveling over 35,000 km up and 35,000 km down adds roughly 240ms of one-way physical transit time, resulting in ~500ms round-trip latency."
                        }
                    }
                ],

                # Page 3: Infrared Communication & Physical Mechanics
                [
                    {
                        "type": "concept_explanation",
                        "title": "Infrared (IR) Transmission & Security Containment",
                        "content": {
                            "text": "Infrared transmission utilizes electromagnetic frequencies between $300\\text{ GHz}$ and $400\\text{ THz}$ (just below the visible red light spectrum).\n\n### Physical Mechanics\n- **Transmitter**: A high-efficiency Light Emitting Diode (LED) flashes coded pulses of invisible infrared light.\n- **Receiver**: A silicon photodiode detects the incoming light pulses and translates them back into digital electrical signals.\n\n### The 'Obstacle Wall' & Physical Security Advantage\nUnlike radio waves, infrared light cannot penetrate opaque, solid objects such as drywall, concrete walls, wooden doors, or metal cabinetry. \n\nWhile this prevents infrared from functioning between different rooms, it offers an exceptional **cybersecurity advantage** in confidential military, medical, and banking boardrooms. An infrared wireless data transmission cannot leak through the walls or windows into an adjacent corridor, making eavesdropping by unauthorized external parties physically impossible without direct line-of-sight access inside the room."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Infrared Properties",
                        "content": {
                            "question": "What primary physical property makes Infrared (IR) transmission inherently secure against external eavesdropping in a closed boardroom?",
                            "options": [
                                "Infrared waves cannot penetrate solid opaque walls, preventing signals from leaking outside.",
                                "Infrared waves travel through magnetic conductors.",
                                "Infrared signals operate on high-voltage copper cables.",
                                "Infrared transmitters encrypt data automatically using single-mode glass."
                            ],
                            "correct_answer": "Infrared waves cannot penetrate solid opaque walls, preventing signals from leaking outside.",
                            "explanation": "Because infrared light is completely blocked by opaque physical boundaries (walls, doors), the signal remains strictly contained inside the physical room."
                        }
                    }
                ],

                # Page 4: Diagnostic Guide: 5 Environmental Degradation Factors
                [
                    {
                        "type": "concept_explanation",
                        "title": "Diagnostic Guide: 5 Key Factors Affecting Wireless Transmission",
                        "content": {
                            "text": "Network engineers must analyze five major physical and environmental phenomena that degrade unguided signals over distance:\n\n1. **Attenuation (Distance)**: As electromagnetic waves radiate outward from an antenna, signal power drops off rapidly (following the inverse-square law). Signal amplitude decreases over distance, requiring repeaters or high-gain antennas.\n2. **Obstacles & Material Absorption**: Physical materials absorb or reflect radio frequencies:\n   - *High Absorption (Blocks Wi-Fi)*: Reinforced concrete, brick masonry, metal filing cabinets, mirrors, and dense human bodies (water content).\n   - *Low Absorption (Passes Wi-Fi)*: Drywall, interior wooden doors, and clear glass windows.\n3. **Frequency Interference (EMI / Co-channel Noise)**: Unwanted electrical noise from overlapping radio sources. Common household microwave ovens, 2.4 GHz cordless phones, and baby monitors radiate noise in the 2.4 GHz band, causing severe Wi-Fi packet drops.\n4. **Weather & Atmospheric Absorption (Rain Fade)**: Rain, heavy fog, and dust storms absorb and scatter high-frequency microwave and satellite signals, causing temporary signal dropouts known as **rain fade**.\n5. **Multi-path Distortion (Echo Interference)**: Wireless signals reflect off metal ceilings, polished floors, and furniture, arriving at the receiver antenna over slightly different paths with microsecond timing delays, creating constructive and destructive interference."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "5 Key Environmental Transmission Degradation Factors",
                        "content": {
                            "caption": "Detailed technical breakdown of Attenuation, Obstacle Absorption, Frequency Interference, Rain Fade, and Multi-path Echo Distortion with engineering countermeasures.",
                            "svg_content": SVG_TRANSMISSION_DEGRADATION_FACTORS
                        }
                    }
                ],

                # Page 5: Wireless Troubleshooting & Mastery Check
                [
                    {
                        "type": "scenario_practice",
                        "title": "Troubleshooting Scenario: School Wi-Fi Connectivity Failure",
                        "content": {
                            "scenario": "A secondary school in Nakuru installs a Wi-Fi access point in the main staffroom. Teachers in the adjacent science laboratory report frequent disconnections whenever the laboratory microwave is used, and students in the outdoor courtyard 60m away across two brick walls get zero signal.",
                            "cases": [
                                {
                                    "subsystem": "Problem 1: Disconnections during Microwave Usage",
                                    "environment": "Staffroom microwave oven operates on the 2.4 GHz frequency.",
                                    "recommended_medium": "Migrate Access Point to 5 GHz Wi-Fi Band",
                                    "rationale": "Microwave ovens emit substantial electromagnetic radiation at 2.45 GHz. Switching teacher laptops to the 5 GHz band avoids this interference completely."
                                },
                                {
                                    "subsystem": "Problem 2: Zero Signal in Courtyard (60m + 2 Brick Walls)",
                                    "environment": "Signal must penetrate two thick masonry brick walls and 60 meters of air.",
                                    "recommended_medium": "Deploy an Outdoor Access Point linked via Cat6 Ethernet cable",
                                    "rationale": "Brick masonry absorbs over 70% of RF energy per wall. Running a wired Cat6 cable to an outdoor PoE access point provides clean line-of-sight coverage to the courtyard."
                                }
                            ]
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Calculating Free Space Path Loss and Rain Fade in a Microwave Link",
                        "content": {
                            "scenario": "A telecom provider establishes a 10 km Line-of-Sight microwave link at 11 GHz between two county offices in Kisumu. During a severe tropical thunderstorm with heavy rain, the signal drops below the receiver sensitivity threshold of -75 dBm. Determine the factors contributing to signal degradation and explain how to mitigate rain fade.",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Analyze Free Space Path Loss (FSPL)",
                                    "description": "As high-frequency electromagnetic waves radiate through space, signal power diminishes inversely with the square of the distance (geometric spreading), reducing base signal power."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Analyze Rain Attenuation (Rain Fade)",
                                    "description": "At frequencies above 10 GHz, rain droplets match the physical wavelength of the microwave beam, causing intense dielectric absorption and Rayleigh scattering."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Formulate Engineering Mitigation Strategy",
                                    "description": "Increase transmit power with Automatic Transmit Power Control (ATPC), install higher-gain parabolic dish antennas to increase link fade margin, or deploy redundant lower-frequency (e.g. 5 GHz) backup links."
                                }
                            ],
                            "conclusion": "Rain fade at 11 GHz is mitigated by increasing antenna gain and provisioning an adequate link fade margin (+15 to +20 dB)."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Wireless Propagation & Environmental Vulnerabilities",
                        "content": {
                            "text": "1. **Electromagnetic Spectrum**: Radio waves propagate omnidirectionally and penetrate walls; Microwaves require direct Line-of-Sight; Infrared cannot penetrate opaque obstacles.\\n2. **5 Degradation Factors**: Attenuation (distance signal loss), Obstacle Shadowing, Interference (e.g., 2.4 GHz microwave ovens/Bluetooth), Weather (Rain Fade at >10 GHz), and Multi-path fading."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Microwave Oven Interference",
                        "content": {
                            "question": "Why does an operating household microwave oven frequently disrupt standard 2.4 GHz Wi-Fi network traffic?",
                            "options": [
                                "Microwave ovens heat water by emitting high-power electromagnetic radiation on the exact same 2.4 GHz frequency band.",
                                "Microwave ovens physically cut the fiber optic cable.",
                                "Microwave ovens absorb infrared light from the router.",
                                "Microwave ovens convert digital signals to BNC coaxial cables."
                            ],
                            "correct_answer": "Microwave ovens heat water by emitting high-power electromagnetic radiation on the exact same 2.4 GHz frequency band.",
                            "explanation": "Microwave ovens operate at approximately 2.45 GHz. Imperfect door seals leak stray RF noise that collides with 2.4 GHz Wi-Fi packets, causing severe frame drops."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Weather Degradation",
                        "content": {
                            "question": "What specific telecommunications phenomenon describes the temporary loss of satellite and microwave dish signals during torrential downpours?",
                            "options": [
                                "Rain Fade",
                                "Differential Signaling",
                                "Modal Dispersion",
                                "Total Internal Reflection"
                            ],
                            "correct_answer": "Rain Fade",
                            "explanation": "Rain fade occurs when raindrops absorb and scatter high-frequency microwave and satellite signals (especially Ku and Ka bands) in the atmosphere."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LEARNING UNIT 3: Hardware Interfaces and Connection Protocols
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Hardware Network Interfaces and Connection Protocols",
            "unit_description": "Network Interface Cards (NICs), physical connectors (RJ-45, BNC, Optical LC/SC), and the standardized 4-step engineering protocol for physical connection and link verification.",
            "lesson_title": "Hardware Interfaces, NICs, and Physical Connection Protocols",
            "pages": [
                # Page 1: The Universal Adapter Principle & NICs
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Hardware Interfaces & Installation Protocols",
                        "content": {
                            "goal": "Master the hardware architecture of Network Interface Cards (NICs), understand physical connector specifications, and apply the 4-step connection planning protocol to install and verify network links."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 'Universal Adapter' Principle & Network Interfaces",
                        "content": {
                            "text": "If you travel to another country, your electrical appliances cannot plug into the wall sockets if the physical pins do not match. To power your laptop, you need an adapter that interfaces your plug's physical layout to the wall socket's pin configuration.\n\nIn computer networking, a **network interface** acts as this vital adapter. To connect a computer system to a physical cable or wireless channel, the host device must possess specialized controller hardware that translates internal system data (transferred over motherboard PCIe buses) into external transmission signals.\n\n### Network Interface Card (NIC) Hardware Components:\n- **Wired NIC**: Built into motherboards or installed via PCIe expansion slots. Features a female **RJ-45 Ethernet port**, physical layer transceiver (PHY chip), media access controller (MAC chip), and status LEDs.\n- **Wireless NIC (Wi-Fi Adapter)**: Features internal or external radio antennas and a dedicated RF transceiver chip that modulates/demodulates packet data onto radio carrier waves.\n- **Optical Transceiver (SFP / SFP+)**: Small Form-factor Pluggable modular interface that houses laser diodes and photodiode receivers to connect fiber-optic patch cords to switches."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Hardware Interface Architecture & Installation Protocol",
                        "content": {
                            "caption": "Internal architecture of a PCIe Network Interface Card with PHY/MAC controller chips, RJ-45 status LEDs, and the 4-Step Connection Planning Protocol.",
                            "svg_content": SVG_HARDWARE_CONNECTION_PROTOCOL
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "PCI Ethernet Network Interface Card (NIC)",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Ethernet_NIC_D-Link_DFE-530TX.jpg/800px-Ethernet_NIC_D-Link_DFE-530TX.jpg",
                            "caption": "PCI Fast Ethernet Network Interface Card showing RJ-45 port, controller IC, crystal oscillator, and link indicator LEDs.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Network Interface Cards (NICs), MAC Addressing & Transceivers",
                        "content": {
                            "youtube_id": "a_c35pG2F94",
                            "url": "https://www.youtube.com/watch?v=a_c35pG2F94",
                            "description": "Hardware breakdown explaining NIC controller architecture, Layer 2 MAC addresses, PHY chips, and transceiver interfaces."
                        }
                    }
                ],

                # Page 2: Engineering Protocol: 4-Step Connection Planning
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Ethernet RJ-45 Color Pinouts (T568A vs. T568B) & Optical Transceivers",
                        "content": {
                            "caption": "TIA/EIA-568A and T568B RJ-45 8-pin color sequences, Straight-Through vs. Crossover wiring, and hot-swappable SFP+ optical transceiver modules.",
                            "svg_content": SVG_ETHERNET_PINOUT_AND_TRANSCEIVERS
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "System Design: The 4-Step Connection Planning Protocol",
                        "content": {
                            "text": "To guarantee reliable, certified physical network installations, network engineers follow a strict four-step commissioning procedure:\n\n```\n[ Step 1: Interface Audit ] ---> [ Step 2: Cable/Link Pathing ] ---> [ Step 3: Mechanical Snap & Latch ] ---> [ Step 4: Link & Signal Testing ]\n```\n\n1. **Step 1: Interface & Speed Audit**\n   - Verify that the Data Terminal Equipment (DTE) possesses a compatible NIC matching the transmission medium (e.g., verifying a server has a $10\\text{ GbE}$ RJ-45 or SFP+ fiber card before routing Cat6a or OM4 fiber).\n2. **Step 2: Cable & Link Pathing**\n   - Plan cable raceways away from high-voltage electrical conduits, elevator motors, air-conditioning compressors, and fluorescent ballasts to avoid electromagnetic noise induction.\n   - Ensure bend radius limits are respected (especially for fiber-optic cables to avoid micro-fractures in the glass core).\n3. **Step 3: Mechanical Snap & Latching**\n   - Firmly insert the RJ-45 or optical connector into the port until the plastic retaining clip clicks audibly into place. This prevents loose physical contact that leads to intermittent disconnections and packet jitter.\n4. **Step 4: Link Verification & Signal Testing**\n   - Observe hardware LED indicators:\n     - **Steady Green LED**: Physical Layer 1 link established with carrier signal detected.\n     - **Flashing Amber/Green LED**: Active frame transmission / data activity.\n     - **Unlit LED**: Physical open circuit, severed wire, bad crimp, or powered-down remote switch.\n   - Perform end-to-end ping diagnostics, duplex validation, and packet-loss audits."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Small Form-Factor Pluggable (SFP) Optical Transceiver Module",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/SFP_transceiver.jpg/800px-SFP_transceiver.jpg",
                            "caption": "Figure 9.7: Hot-swappable 10G SFP+ optical transceiver module converting electronic signals into high-speed laser pulses for fiber links.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "deep_dive",
                        "title": "Deep Dive: RJ-45 Pinout Wiring Standards (T568A vs T568B)",
                        "content": {
                            "text": "Ethernet twisted-pair cables are terminated according to two standardized color codes specified by ANSI/TIA-568:\n\n- **T568B (Most Common Standard)**:\n  - Pin 1: White/Orange | Pin 2: Orange\n  - Pin 3: White/Green  | Pin 4: Blue\n  - Pin 5: White/Blue   | Pin 6: Green\n  - Pin 7: White/Brown  | Pin 8: Brown\n- **Straight-Through Cable**: Both ends terminated with T568B. Used to connect unlike devices (e.g., PC to Switch).\n- **Crossover Cable**: One end T568A, other end T568B. Historically used to connect like devices (e.g., PC to PC). Modern NICs support **Auto-MDIX**, which automatically detects and configures transmit/receive pairs."
                        }
                    }
                ],

                # Page 3: Step-by-Step Diagnostic Lab
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Network Physical Layer Diagnostic Walkthrough",
                        "content": {
                            "scenario": "A newly installed desktop computer in a school computer lab cannot connect to the internet. The network wall jack is connected to the central switch room.",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Physical LED Inspection",
                                    "description": "Inspect the RJ-45 port on the rear of the PC. The Link LED is completely unlit (dark), indicating that no electrical carrier signal is reaching the NIC from the switch."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Cable Integrity & Patch Swap",
                                    "description": "Swap the 2-meter patch cable between the PC and the wall jack with a known working certified Cat6 cable. The Link LED remains unlit."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Structured Cabling Continuity Test",
                                    "description": "Plug a hardware cable tester into the wall jack and the patch panel port in the server room. The tester reveals an open circuit on Pin 3 and Pin 6 (Green pair). Inspection of the wall punchdown block reveals a severed copper wire."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Re-termination & Verification",
                                    "description": "Re-punch the wire into the keystone jack according to T568B standard. Reconnect the patch cable. The NIC Link LED turns steady green, the Activity LED blinks amber, and the computer receives an IP address via DHCP."
                                }
                            ],
                            "conclusion": "The fault was isolated to a severed wire on Pin 3/6 at the wall punchdown block. Re-termination restored full physical Layer 1 connectivity."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Port Status LEDs",
                        "content": {
                            "question": "What does a steady green LED light on a computer's wired Ethernet port signify?",
                            "options": [
                                "A valid physical Layer 1 link and carrier connection is established with the switch.",
                                "The computer's hard drive is 100% full.",
                                "A virus has been detected on the network card.",
                                "The network cable is running on single-mode optical laser mode."
                            ],
                            "correct_answer": "A valid physical Layer 1 link and carrier connection is established with the switch.",
                            "explanation": "A steady green link light confirms electrical carrier connectivity between the local NIC and the remote switch port."
                        }
                    }
                ],

                # Page 4: Connection Standards & Formative Mastery
                [
                    {
                        "type": "comparison_table",
                        "title": "Hardware Connectors Comparison",
                        "content": {
                            "headers": ["Connector Type", "Supported Media", "Coupling Mechanism", "Typical Applications"],
                            "rows": [
                                ["RJ-45 Plug", "Twisted-Pair (Cat5e/6/6a)", "Plastic click-tab latch", "Standard PC LANs, switches, routers"],
                                ["BNC Connector", "Coaxial Cable (RG-58)", "Bayonet twist-lock pin", "Legacy 10BASE2 Ethernet, CCTV video"],
                                ["F-Type Connector", "Coaxial Cable (RG-6)", "Threaded screw-on collar", "Cable TV (CATV), Satellite LNB dishes"],
                                ["LC / SC Connector", "Fiber-Optic (SMF/MMF)", "Push-pull click latch", "Enterprise switch uplinks, data centers"]
                            ]
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Physical Interface Standards & Verification",
                        "content": {
                            "text": "1. **NIC Controller Hardware**: Converts internal system data to transmission line voltages/photons via PHY/MAC chips with permanent hardware MAC addresses.\\n2. **Connector Standards**: RJ-45 (8P8C for UTP/STP), BNC (bayonet lock for coaxial), SC/LC (push-pull latch for fiber optics).\\n3. **Structured 4-Step Protocol**: Planning -> Inspection -> Seating (audible click) -> Verification (solid green Link LED + DHCP IP assignment)."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Connector Matching",
                        "content": {
                            "question": "Which connector utilizes a bayonet twist-lock mechanism to attach coaxial cables in CCTV and legacy Ethernet systems?",
                            "options": [
                                "BNC Connector",
                                "RJ-45 Plug",
                                "USB Type-C",
                                "VGA Connector"
                            ],
                            "correct_answer": "BNC Connector",
                            "explanation": "The BNC (Bayonet Neill-Concelman) connector uses a circular bayonet locking mechanism to secure coaxial cable terminations."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Installation Protocols",
                        "content": {
                            "question": "Why is it critical to route copper network cables away from high-voltage electrical conduits and heavy air-conditioning motors during installation?",
                            "options": [
                                "To prevent electromagnetic interference (EMI) from inducing noise and corrupting data packets.",
                                "To stop the copper wires from becoming fiber-optic strands.",
                                "To increase the physical weight of the network cable.",
                                "To disable the router's DHCP server."
                            ],
                            "correct_answer": "To prevent electromagnetic interference (EMI) from inducing noise and corrupting data packets.",
                            "explanation": "High-voltage lines and electric motors radiate strong electromagnetic fields that induce electrical noise (EMI) in copper cables, leading to packet corruption and retransmissions."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LEARNING UNIT 4: Media Selection Architecture, Case Studies, Assessment
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Transmission Media Selection, Case Studies, and Assessment",
            "unit_description": "Network reliability and scalability metrics, comprehensive engineering case study on Mount Kenya, the Lake Naivasha challenge, and the complete Topic 9 assessment library.",
            "lesson_title": "Transmission Media Selection, Case Studies, and Network Architecture",
            "pages": [
                # Page 1: Network Scalability, Reliability & Economics
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Media Selection & System Architecture",
                        "content": {
                            "goal": "Synthesize the engineering criteria for selecting transmission media, evaluate real-world trade-offs in challenging environmental case studies, and complete the Topic 9 assessment suite."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 'Highway Expansion' Analogy & Infrastructure Metrics",
                        "content": {
                            "text": "Imagine building a highway between two rapidly growing industrial cities. If you pave a narrow, single-lane dirt track, heavy transport trucks will struggle to move, creating massive gridlocks as soon as trade scales up. If you invest early in a wide, multi-lane reinforced concrete expressway, traffic flows smoothly, allowing new business depots and factories to connect seamlessly along the corridor.\n\nIn computer systems, **transmission media** dictate the ultimate performance, reliability, and expansion capacity of the entire network:\n\n- **Reliability**: The ability of a transmission medium to maintain stable, error-free signal delivery under challenging environmental conditions (such as extreme temperature, rain, mechanical vibration, and electromagnetic interference).\n- **Scalability**: The ease with which a transmission medium can support increases in data load, user connections, or geographical distance without requiring a costly and disruptive overhaul of the physical cabling plant."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Enterprise Server Room High-Density Fiber Optic Cabling",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Data_center_fiber_cabling.jpg/800px-Data_center_fiber_cabling.jpg",
                            "caption": "Figure 9.9: High-density fiber optic and Cat6 cabling organized inside an enterprise data center rack.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "deep_dive",
                        "title": "Deep Dive: Total Cost of Ownership (TCO) in Media Selection",
                        "content": {
                            "text": "When choosing transmission media, engineers must evaluate both initial Capital Expenditure (CapEx) and ongoing Operational Expenditure (OpEx):\n\n- **UTP Copper**: Lowest initial CapEx (cheap cables and RJ-45 jacks), but limited to 100m and vulnerable to electrical surges and lightning.\n- **Fiber-Optics**: Higher initial CapEx (requires specialized fusion splicers and optical transceivers), but virtually zero ongoing maintenance, immunity to electrical surges, and unlimited bandwidth upgrades simply by changing endpoint lasers.\n- **Wireless (Wi-Fi / Microwave)**: Eliminates trenching and cabling CapEx over difficult terrain, but requires ongoing management of RF interference, channel congestion, and weather degradation."
                        }
                    }
                ],

                # Page 2: Engineering Decision Tree
                [
                    {
                        "type": "suggested_diagram",
                        "title": "ANSI/TIA-568 Structured Cabling Campus Architecture",
                        "content": {
                            "caption": "Hierarchical subsystems connecting Main Cross-Connect (MDF), Floor Distribution (IDF), Horizontal UTP, and Work Area Outlets.",
                            "svg_content": SVG_STRUCTURED_CABLING_CAMPUS_TOPOLOGY
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Structured Cabling Telecommunications Distribution Rack (IDF)",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Structured_cabling_rack.jpg/800px-Structured_cabling_rack.jpg",
                            "caption": "Figure 9.10: Intermediate Distribution Frame (IDF) rack with patch panels and vertical cable managers implementing structured cabling standards.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Engineering Decision Framework for Media Selection",
                        "content": {
                            "text": "To choose the optimal transmission medium for any networking project, engineers evaluate a structured decision tree based on four fundamental constraints:\n\n1. **Distance**: Is the required link length $\\le 100\\text{ meters}$ (copper UTP/STP), $100\\text{m} - 2\\text{ km}$ (Multi-Mode Fiber), $2\\text{ km} - 100\\text{ km}$ (Single-Mode Fiber / Terrestrial Microwave), or inter-continental (Satellite / Subsea Fiber)?\n2. **Electromagnetic Noise Environment**: Are heavy generators, industrial motors, or high-voltage power lines present? (If yes $\\rightarrow$ Shielded STP or 100% immune Fiber-Optic).\n3. **Mobility & Physical Terrain**: Must client devices move freely (Wi-Fi / Cellular), or is physical trenching through mountains/water impossible (Microwave / Satellite)?\n4. **Bandwidth & Budget**: Does the application require standard office internet ($1\\text{ Gbps}$ UTP) or high-capacity data center backbones ($100+\\text{ Gbps}$ Optical Fiber)?"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Transmission Media Engineering Decision Tree",
                        "content": {
                            "caption": "Step-by-step decision tree guiding network architects through Distance, EMI Environment, Mobility, Bandwidth, and Budget constraints.",
                            "svg_content": SVG_MEDIA_SELECTION_DECISION_TREE
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Network Cabling & Media Selection Explained",
                        "content": {
                            "youtube_id": "1z0Z8FFAM6I",
                            "url": "https://www.youtube.com/watch?v=1z0Z8FFAM6I",
                            "description": "Engineering walkthrough on choosing between UTP, STP, Coaxial, Fiber Optic, and Wireless links based on environmental constraints."
                        }
                    }
                ],

                # Page 3: Comprehensive Case Study: Mount Kenya Research Station
                [
                    {
                        "type": "scenario_practice",
                        "title": "Case Study: The Mount Kenya High-Altitude Research Station",
                        "content": {
                            "scenario": "An international climate monitoring organization is deploying a high-altitude research station on the slopes of Mount Kenya. The station requires three distinct communication links:",
                            "cases": [
                                {
                                    "subsystem": "Link A: Internal Research Laboratory (50m)",
                                    "environment": "Connects 12 high-performance sensor computers to a central server inside a laboratory powered by heavy, noisy diesel electrical generators.",
                                    "recommended_medium": "STP (Shielded Twisted Pair - Cat6a)",
                                    "rationale": "The heavy diesel generators generate significant electromagnetic fields (EMI). Standard UTP would suffer from packet corruption. STP provides metallic foil shielding around pairs to block generator crosstalk at an economical cost for 50m."
                                },
                                {
                                    "subsystem": "Link B: Laboratory to Wind-Monitoring Ridge (250m)",
                                    "environment": "Connects the lab to an outdoor anemometer tower 250m up a steep, rocky ridge. The outdoor path experiences frequent lightning storms and heavy cloud cover.",
                                    "recommended_medium": "Single-Mode / Multi-Mode Fiber-Optic Cable",
                                    "rationale": "Copper cables would act as a massive lightning rod, conducting catastrophic electrical surges into the server room. Wireless microwave would suffer from dense cloud/ice fade. Non-conductive glass fiber is 100% immune to lightning surges and spans 250m with near-zero attenuation."
                                },
                                {
                                    "subsystem": "Link C: Mount Kenya Station to Base Office in Nanyuki (15 km)",
                                    "environment": "Connects the mountain lab to the regional logistics office 15km away across protected national forest canopy.",
                                    "recommended_medium": "Terrestrial Microwave Link (Line-of-Sight Dishes)",
                                    "rationale": "Digging a 15km physical trench through protected Mount Kenya National Park to lay fiber is environmentally prohibited and financially impossible. Directional parabolic microwave dishes mounted on towers create a high-throughput line-of-sight link over the forest canopy."
                                }
                            ]
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Mount Kenya Lightning Protection",
                        "content": {
                            "question": "Why is Fiber-Optic cabling the only safe choice for connecting outdoor sensor towers in areas with severe lightning storms?",
                            "options": [
                                "Glass optical fiber is non-metallic and non-conductive, preventing lightning surges from entering building electronics.",
                                "Fiber cables absorb lightning energy to boost battery storage.",
                                "Fiber optics convert lightning bolts into microwave signals.",
                                "Fiber optic jackets are made of copper mesh."
                            ],
                            "correct_answer": "Glass optical fiber is non-metallic and non-conductive, preventing lightning surges from entering building electronics.",
                            "explanation": "Because optical fibers are made of non-conductive silica glass, they cannot conduct electrical currents, protecting sensitive laboratory equipment from catastrophic lightning surge damage."
                        }
                    }
                ],

                # Page 4: Challenging Application Scenario: Lake Naivasha Fishery
                [
                    {
                        "type": "scenario_practice",
                        "title": "Challenging Application Scenario: Lake Naivasha Fishery & Flower Farm",
                        "content": {
                            "scenario": "A commercial fishery and flower enterprise on Lake Naivasha requires an engineered networking blueprint for three distinct operational zones:",
                            "cases": [
                                {
                                    "subsystem": "Link 1: Floating Sensor Docks (50m Offshore)",
                                    "environment": "Automated water-quality probes mounted on floating docks that bob up and down with water currents and wave motion.",
                                    "recommended_medium": "Unguided Wi-Fi / Outdoor Wireless Mesh",
                                    "rationale": "Continuous physical movement and wave currents would bend, fatigue, and snap underwater physical cables. Directional outdoor Wi-Fi comfortably spans 50m over water without physical strain."
                                },
                                {
                                    "subsystem": "Link 2: Lakeside Processing Plant (100m)",
                                    "environment": "Connects packing line scales to the server room inside a metal-roofed warehouse with high-voltage sorting motors and conveyors.",
                                    "recommended_medium": "STP (Shielded Twisted Pair) or Fiber-Optic Cable",
                                    "rationale": "High-voltage electric motors and conveyor belts emit heavy electromagnetic noise. Shielded STP or Fiber-Optic cabling prevents motor EMI from corrupting sensor packet streams."
                                },
                                {
                                    "subsystem": "Link 3: Farm to Corporate Headquarters in Nairobi (80 km)",
                                    "environment": "Long-distance data connection spanning 80 kilometers across the Great Rift Valley escarpment.",
                                    "recommended_medium": "Telecommunication Carrier Optical Fiber / Microwave / LEO Satellite",
                                    "rationale": "Spanning 80km across mountain escarpments requires leasing commercial carrier fiber-optic backbones or deploying satellite broadband terminals."
                                }
                            ]
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Moving Floating Platforms",
                        "content": {
                            "question": "Which transmission medium is best suited for connecting moving floating sensor docks 50 meters offshore without risk of cable fatigue?",
                            "options": [
                                "Outdoor Wireless (Wi-Fi / Radio)",
                                "Stiff Coaxial Cable",
                                "Buried Copper UTP",
                                "Armored Lead Pipe"
                            ],
                            "correct_answer": "Outdoor Wireless (Wi-Fi / Radio)",
                            "explanation": "Wireless transmission eliminates physical cables that would suffer mechanical wear, fatigue, and eventual snapping due to continuous wave movement."
                        }
                    }
                ],

                # Page 5: Summative Assessment Library
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Multi-Building Campus Transmission Media Selection & TCO Analysis",
                        "content": {
                            "problem_statement": "A university in Eldoret is constructing three new facilities: (A) A 60m indoor student lab with 50 desktop PCs; (B) An inter-building backbone link spanning 1.5 km across campus roads; (C) An agricultural weather monitoring station 5 km away on a hilltop. Determine the optimal transmission medium, connector type, and justify based on distance, EMI, bandwidth, and total cost of ownership.",
                            "step_by_step_solution": [
                                {
                                    "step_number": 1,
                                    "step_title": "Evaluate Link A (Indoor Student Lab, 60m)",
                                    "explanation": "Distance is 60m (<= 100m) and indoor noise is normal. Select Cat6 Unshielded Twisted Pair (UTP) with RJ-45 connectors. Provides 1 Gbps throughput at minimum cable and termination cost."
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Evaluate Link B (Inter-Building Backbone, 1.5 km)",
                                    "explanation": "Distance is 1,500m (exceeds copper's 100m limit) and runs outdoors subject to lightning storms. Select Single-Mode Fiber-Optic Cable (SMF) with LC connectors. Provides 10+ Gbps bandwidth, zero attenuation over 1.5 km, and 100% electrical lightning immunity."
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Evaluate Link C (Hilltop Weather Station, 5 km)",
                                    "explanation": "Physical trenching 5 km over rugged terrain is cost-prohibitive. Select Terrestrial Microwave Link (Directional Parabolic Dishes) on 5 GHz. Provides reliable line-of-sight connectivity over 5 km without physical cable deployment expenses."
                                }
                            ]
                        }
                    },
                    {
                        "type": "summary_card",
                        "title": "Topic 9 Comprehensive Summary",
                        "content": {
                            "summary": "Data transmission media form the physical foundation of all digital communication. Guided media (UTP, STP, Coaxial, Fiber-Optics) physically channel electrical voltages or light pulses along fixed paths, with Fiber-Optic Total Internal Reflection offering 100% EMI immunity and the highest bandwidth. Unguided media (Radio, Microwave, Infrared) propagate electromagnetic waves through the air, governed by Line-of-Sight principles and vulnerable to attenuation, obstacles, interference, rain fade, and multi-path reflection. Network engineers select media by balancing distance, electromagnetic noise, mobility, bandwidth, and total cost of ownership."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 1: Differential Signaling in UTP",
                        "content": {
                            "question": "Why are copper wire strands twisted in pairs inside UTP network cables?",
                            "options": [
                                "To cancel out electromagnetic interference and crosstalk via differential voltage signaling.",
                                "To make the cable flexible enough to tie into knots.",
                                "To allow laser light pulses to travel faster through the copper.",
                                "To increase the electrical resistance of the wire."
                            ],
                            "correct_answer": "To cancel out electromagnetic interference and crosstalk via differential voltage signaling.",
                            "explanation": "Twisting wires causes external noise to be induced equally on both conductors. The receiver calculates the difference between the two wires, cancelling out the common noise."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 2: Coaxial Physical Construction",
                        "content": {
                            "question": "Which guided medium features a concentric design with a central copper core, dielectric insulator, braided metallic shield, and outer protective jacket?",
                            "options": [
                                "Coaxial Cable",
                                "Unshielded Twisted Pair",
                                "Multi-Mode Optical Fiber",
                                "Infrared Transceiver"
                            ],
                            "correct_answer": "Coaxial Cable",
                            "explanation": "Coaxial cable is constructed of four concentric layers sharing a single geometric axis, providing good noise immunity for cable television and broadband modems."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 3: Definition of Scalability",
                        "content": {
                            "question": "What is meant by the 'Scalability' of a transmission medium in computer networking?",
                            "options": [
                                "The ease with which a medium can accommodate increases in data load and user connections without requiring a complete cabling overhaul.",
                                "The physical weight of the cable per kilometer.",
                                "The time it takes to strip the outer PVC jacket.",
                                "The maximum number of times a cable can be bent before breaking."
                            ],
                            "correct_answer": "The ease with which a medium can accommodate increases in data load and user connections without requiring a complete cabling overhaul.",
                            "explanation": "Scalability refers to an infrastructure's capacity to handle growing traffic, bandwidth demands, and user devices seamlessly over time."
                        }
                    }
                ]
            ]
        }
    ]

# =====================================================================
# INGESTION EXECUTOR
# =====================================================================

def ingest_grade10_topic9(replace: bool = True):
    print("=" * 80)
    print("STARTING CBC GRADE 10 COMPUTER SCIENCE — TOPIC 9 INGESTION")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(id=5).first()
    if not curriculum:
        curriculum = Curriculum.objects.filter(name__icontains="CBC").first()
    print(f"[+] Curriculum: {curriculum} (ID: {curriculum.id if curriculum else 'None'})")

    grade = Grade.objects.filter(curriculum=curriculum, level=10).first()
    print(f"[+] Grade: {grade} (ID: {grade.id if grade else 'None'})")

    subject = Subject.objects.filter(grade=grade, name__icontains="Computer Science").first()
    print(f"[+] Subject: {subject} (ID: {subject.id if subject else 'None'})")

    if not subject:
        print("[!] ERROR: Grade 10 Computer Science subject not found!")
        return

    topic, created = Topic.objects.get_or_create(
        subject=subject,
        order=9,
        defaults={
            "name": "Data Transmission Media",
            "description": "Physics and application of guided media (physical cables), unguided media (wireless signals), factors degrading transmissions, and media selection criteria."
        }
    )
    if not created:
        topic.name = "Data Transmission Media"
        topic.description = "Physics and application of guided media (physical cables), unguided media (wireless signals), factors degrading transmissions, and media selection criteria."
        topic.save()
    print(f"[+] Topic: {topic.name} (Order: {topic.order}, ID: {topic.id})")

    if replace:
        print(f"[-] Purging existing learning units and lessons for Topic {topic.order}...")
        for u in topic.learning_units.all():
            for l in u.lessons.all():
                l.blocks.all().delete()
                l.assets.all().delete()
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    curriculum_data = build_topic9_curriculum()
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
                    "topic_order": 9,
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
                        block_id=f"g10_cs_t9_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={"topic_order": 9, "unit_order": u_order, "page": page_idx}
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
    print("TOPIC 9 INGESTION COMPLETE:")
    print(f"  Units Created:   {total_units}")
    print(f"  Lessons Created: {total_lessons}")
    print(f"  Pages Created:   {total_pages}")
    print(f"  Blocks Created:  {total_blocks}")
    print(f"  Assets Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_grade10_topic9(replace=True)
