"""
VLearn CBC Grade 10 Computer Science — Topic 3: Input/Output (I/O) Devices
Production Ingestion & Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Computer Science
Topic: Input/Output (I/O) Devices (Topic Order: 3)

Decomposed into 2 Learning Units & 2 Published Lessons:
  1. Input Devices and Data Capture (Lesson 5: Input Devices and Data Capture)
  2. Output Devices and Presenting Information (Lesson 6: Output Devices and Presenting Information)
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
# HIGH PRECISION VECTOR SVGS FOR TOPIC 3
# =====================================================================

SVG_TOUCHSCREEN_TECH = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Touch Screen Engineering: Resistive vs. Capacitive vs. Infrared</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Cross-sectional working principles, physical mechanics, and input detection methods</text>

  <!-- 1. RESISTIVE -->
  <g transform="translate(40, 85)">
    <rect width="270" height="390" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#d97706"/>
    <text x="135" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Resistive Touch Screen</text>
    
    <!-- Schematic Layers -->
    <rect x="20" y="45" width="230" height="14" rx="3" fill="#38bdf8" opacity="0.8"/>
    <text x="135" y="56" font-size="8.5" fill="#0f172a" font-weight="bold" text-anchor="middle">Flexible Polyester Layer (Conductive)</text>
    
    <!-- Spacer Dots -->
    <circle cx="50" cy="72" r="3" fill="#94a3b8"/>
    <circle cx="100" cy="72" r="3" fill="#94a3b8"/>
    <circle cx="150" cy="72" r="3" fill="#94a3b8"/>
    <circle cx="200" cy="72" r="3" fill="#94a3b8"/>
    <text x="240" y="75" font-size="8" fill="#94a3b8">Spacers</text>
    
    <rect x="20" y="85" width="230" height="16" rx="3" fill="#38bdf8" opacity="0.8"/>
    <text x="135" y="97" font-size="8.5" fill="#0f172a" font-weight="bold" text-anchor="middle">Rigid Glass Substrate (Conductive)</text>
    
    <text x="15" y="130" font-size="10" font-weight="bold" fill="#fbbf24">• How it Works:</text>
    <text x="15" y="148" font-size="9.5" fill="#cbd5e1">Physical pressure forces the flexible top sheet to touch bottom layer, completing a voltage circuit.</text>
    
    <text x="15" y="210" font-size="10" font-weight="bold" fill="#34d399">• Key Advantages:</text>
    <text x="15" y="228" font-size="9.5" fill="#cbd5e1">Works with ANY object (gloved fingers, plastic pens). Cheap &amp; water-resistant.</text>
    
    <text x="15" y="290" font-size="10" font-weight="bold" fill="#f87171">• Limitations &amp; Uses:</text>
    <text x="15" y="308" font-size="9.5" fill="#cbd5e1">No multi-touch gestures. Easily scratched.<br/>Uses: ATMs, Point-of-Sale cash registers.</text>
  </g>

  <!-- 2. CAPACITIVE -->
  <g transform="translate(345, 85)">
    <rect width="270" height="390" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#0284c7"/>
    <text x="135" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Capacitive Touch Screen</text>
    
    <!-- Schematic Layers -->
    <rect x="20" y="45" width="230" height="22" rx="3" fill="#38bdf8" opacity="0.9"/>
    <text x="135" y="60" font-size="9" fill="#0f172a" font-weight="bold" text-anchor="middle">Protective Scratch-Resistant Glass</text>
    
    <rect x="20" y="75" width="230" height="14" rx="3" fill="#0284c7"/>
    <text x="135" y="86" font-size="8.5" fill="#ffffff" font-weight="bold" text-anchor="middle">Transparent Electrostatic Grid (ITO)</text>
    
    <rect x="20" y="97" width="230" height="16" rx="3" fill="#1e293b"/>
    <text x="135" y="109" font-size="8.5" fill="#94a3b8" text-anchor="middle">Display Backlight Unit</text>
    
    <text x="15" y="135" font-size="10" font-weight="bold" fill="#38bdf8">• How it Works:</text>
    <text x="15" y="153" font-size="9.5" fill="#cbd5e1">Bare finger draws a tiny electrical charge, creating a measurable change in capacitance coordinates.</text>
    
    <text x="15" y="210" font-size="10" font-weight="bold" fill="#34d399">• Key Advantages:</text>
    <text x="15" y="228" font-size="9.5" fill="#cbd5e1">High optical clarity. Full multi-touch support (pinch-to-zoom). Durable glass front.</text>
    
    <text x="15" y="290" font-size="10" font-weight="bold" fill="#f87171">• Limitations &amp; Uses:</text>
    <text x="15" y="308" font-size="9.5" fill="#cbd5e1">Fails with non-conductive gloves/pens.<br/>Uses: Smartphones, tablets, modern laptops.</text>
  </g>

  <!-- 3. INFRARED -->
  <g transform="translate(650, 85)">
    <rect width="270" height="390" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#9333ea"/>
    <text x="135" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Infrared (IR) Touch Screen</text>
    
    <!-- Schematic Frame -->
    <rect x="20" y="45" width="230" height="60" rx="4" fill="#1e293b" stroke="#a855f7" stroke-width="1"/>
    <line x1="30" y1="55" x2="240" y2="55" stroke="#ec4899" stroke-width="1.5" stroke-dasharray="4,2"/>
    <line x1="30" y1="75" x2="240" y2="75" stroke="#ec4899" stroke-width="1.5" stroke-dasharray="4,2"/>
    <line x1="30" y1="95" x2="240" y2="95" stroke="#ec4899" stroke-width="1.5" stroke-dasharray="4,2"/>
    <text x="135" y="78" font-size="9" fill="#f472b6" font-weight="bold" text-anchor="middle">Invisible Grid of Infrared Light Beams</text>
    
    <text x="15" y="135" font-size="10" font-weight="bold" fill="#c084fc">• How it Works:</text>
    <text x="15" y="153" font-size="9.5" fill="#cbd5e1">LEDs &amp; photodiodes create an optical grid. Touching the glass interrupts light beams.</text>
    
    <text x="15" y="210" font-size="10" font-weight="bold" fill="#34d399">• Key Advantages:</text>
    <text x="15" y="228" font-size="9.5" fill="#cbd5e1">100% optical clarity (no glass coating). Works even if glass is shattered or with thick gloves.</text>
    
    <text x="15" y="290" font-size="10" font-weight="bold" fill="#f87171">• Limitations &amp; Uses:</text>
    <text x="15" y="308" font-size="9.5" fill="#cbd5e1">Dust/insects in bezel cause false triggers.<br/>Uses: Giant classroom whiteboards, kiosks.</text>
  </g>
</svg>
""")

SVG_DATA_CAPTURE_ECOSYSTEM = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Input Peripheral Ecosystem &amp; Data Capture Technologies</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Classifying direct manual keying, coordinate pointing, automated optical capture, and acoustic ADC conversion</text>

  <!-- 4 Categories -->
  <!-- 1. Manual Keying & Pointing -->
  <g transform="translate(40, 95)">
    <rect width="200" height="230" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="200" height="26" rx="6" fill="#0284c7"/>
    <text x="100" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Keying &amp; Pointing</text>
    <text x="15" y="50" font-size="10" font-weight="bold" fill="#38bdf8">Devices:</text>
    <text x="15" y="68" font-size="9" fill="#cbd5e1">• QWERTY Keyboard</text>
    <text x="15" y="86" font-size="9" fill="#cbd5e1">• Optical Mouse (LED+DSP)</text>
    <text x="15" y="104" font-size="9" fill="#cbd5e1">• Touchpad / Trackball</text>
    <text x="15" y="122" font-size="9" fill="#cbd5e1">• Joystick &amp; Gamepad</text>
    <text x="15" y="150" font-size="10" font-weight="bold" fill="#38bdf8">Working Mechanism:</text>
    <text x="15" y="168" font-size="9" fill="#e2e8f0">Physical switches and optical displacement sensors translate human motion into binary matrix scan codes.</text>
  </g>

  <!-- 2. Automated Optical Capture -->
  <g transform="translate(265, 95)">
    <rect width="200" height="230" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="200" height="26" rx="6" fill="#059669"/>
    <text x="100" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Optical Scanners</text>
    <text x="15" y="50" font-size="10" font-weight="bold" fill="#34d399">Devices:</text>
    <text x="15" y="68" font-size="9" fill="#cbd5e1">• 1D Barcode Readers</text>
    <text x="15" y="86" font-size="9" fill="#cbd5e1">• 2D QR Code Imagers</text>
    <text x="15" y="104" font-size="9" fill="#cbd5e1">• Flatbed Document Scanners</text>
    <text x="15" y="122" font-size="9" fill="#cbd5e1">• 3D LIDAR / Laser Meshes</text>
    <text x="15" y="150" font-size="10" font-weight="bold" fill="#34d399">Working Mechanism:</text>
    <text x="15" y="168" font-size="9" fill="#e2e8f0">Photodiodes &amp; CCD arrays measure light absorption/reflectance, eliminating human manual typing errors.</text>
  </g>

  <!-- 3. Acoustic & Voice Capture -->
  <g transform="translate(490, 95)">
    <rect width="200" height="230" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="200" height="26" rx="6" fill="#d97706"/>
    <text x="100" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Voice &amp; Audio ADC</text>
    <text x="15" y="50" font-size="10" font-weight="bold" fill="#fbbf24">Devices:</text>
    <text x="15" y="68" font-size="9" fill="#cbd5e1">• Dynamic &amp; Condenser Mics</text>
    <text x="15" y="86" font-size="9" fill="#cbd5e1">• Smart Assistant Voice Coils</text>
    <text x="15" y="104" font-size="9" fill="#cbd5e1">• Sound Card ADC Chips</text>
    <text x="15" y="150" font-size="10" font-weight="bold" fill="#fbbf24">Working Mechanism:</text>
    <text x="15" y="168" font-size="9" fill="#e2e8f0">Diaphragms generate variable voltages sampled at 44.1 kHz into quantized binary audio waveforms.</text>
  </g>

  <!-- 4. Environmental Sensors -->
  <g transform="translate(715, 95)">
    <rect width="205" height="230" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="205" height="26" rx="6" fill="#9333ea"/>
    <text x="102.5" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4. Automated Sensors</text>
    <text x="15" y="50" font-size="10" font-weight="bold" fill="#c084fc">Devices:</text>
    <text x="15" y="68" font-size="9" fill="#cbd5e1">• Thermocouples (Temp)</text>
    <text x="15" y="86" font-size="9" fill="#cbd5e1">• Moisture &amp; Light Sensors</text>
    <text x="15" y="104" font-size="9" fill="#cbd5e1">• RFID / NFC Badges</text>
    <text x="15" y="122" font-size="9" fill="#cbd5e1">• Biometric Fingerprint Scanners</text>
    <text x="15" y="150" font-size="10" font-weight="bold" fill="#c084fc">Working Mechanism:</text>
    <text x="15" y="168" font-size="9" fill="#e2e8f0">Autonomous environmental telemetry streamed into microcontrollers without human intervention.</text>
  </g>

  <!-- Bottom Panel: Comparison of Manual Keying vs Automated Capture -->
  <g transform="translate(40, 345)">
    <rect width="880" height="135" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="440" y="26" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">Direct Data Entry (Manual Keying) vs. Automated Data Capture (ADC)</text>
    <text x="30" y="55" font-size="10.5" fill="#e2e8f0">• <tspan fill="#f87171" font-weight="bold">Manual Keying:</tspan> Relies on humans typing keys. Average speed: 40–80 words/min; Error rate: ~1 in 300 keystrokes.</text>
    <text x="30" y="80" font-size="10.5" fill="#e2e8f0">• <tspan fill="#34d399" font-weight="bold">Automated Optical Capture (Barcode/RFID):</tspan> Scans data in milliseconds; Error rate: less than 1 in 3,000,000 scans.</text>
    <text x="30" y="105" font-size="10.5" fill="#e2e8f0">• <tspan fill="#fbbf24" font-weight="bold">Operational Impact:</tspan> Critical for modern supermarkets, airport baggage tracking, hospital patient wristbands, and banking.</text>
  </g>
</svg>
""")

SVG_LASER_PRINTER_CYCLE = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The 6-Step Electrostatic Laser Printing Cycle</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">How static electricity, laser light, toner powder, and heat fusing create permanent hard copies</text>

  <!-- Step Boxes (2 Rows of 3) -->
  <!-- Step 1: Charging -->
  <g transform="translate(40, 95)">
    <rect width="270" height="175" rx="8" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="270" height="26" rx="6" fill="#0284c7"/>
    <text x="135" y="18" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Charging the Drum</text>
    <text x="15" y="45" font-size="10" font-weight="bold" fill="#38bdf8">• Primary Corona Wire / Roller:</text>
    <text x="15" y="62" font-size="9.5" fill="#cbd5e1">Applies a uniform negative electrostatic charge across the rotating Organic Photoconductor (OPC) drum.</text>
  </g>

  <!-- Step 2: Laser Exposure -->
  <g transform="translate(345, 95)">
    <rect width="270" height="175" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="270" height="26" rx="6" fill="#dc2626"/>
    <text x="135" y="18" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Laser Exposure</text>
    <text x="15" y="45" font-size="10" font-weight="bold" fill="#f87171">• Discharging Text Areas:</text>
    <text x="15" y="62" font-size="9.5" fill="#cbd5e1">A laser beam scans the drum, neutralizing the negative charge where text or images appear, creating an invisible electrostatic image.</text>
  </g>

  <!-- Step 3: Toner Development -->
  <g transform="translate(650, 95)">
    <rect width="270" height="175" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="270" height="26" rx="6" fill="#d97706"/>
    <text x="135" y="18" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Toner Development</text>
    <text x="15" y="45" font-size="10" font-weight="bold" fill="#fbbf24">• Attracting Dry Ink:</text>
    <text x="15" y="62" font-size="9.5" fill="#cbd5e1">Negatively charged dry carbon toner powder is attracted strictly to the discharged areas of the drum.</text>
  </g>

  <!-- Step 4: Transfer -->
  <g transform="translate(40, 295)">
    <rect width="270" height="175" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="270" height="26" rx="6" fill="#059669"/>
    <text x="135" y="18" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">4. Image Transfer</text>
    <text x="15" y="45" font-size="10" font-weight="bold" fill="#34d399">• Moving Toner to Paper:</text>
    <text x="15" y="62" font-size="9.5" fill="#cbd5e1">Paper is given a strong positive charge by a transfer roller, pulling the negative toner powder off the drum onto the sheet.</text>
  </g>

  <!-- Step 5: Fusing -->
  <g transform="translate(345, 295)">
    <rect width="270" height="175" rx="8" fill="#0f172a" stroke="#f97316" stroke-width="1.5"/>
    <rect width="270" height="26" rx="6" fill="#ea580c"/>
    <text x="135" y="18" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">5. Heat &amp; Pressure Fusing</text>
    <text x="15" y="45" font-size="10" font-weight="bold" fill="#fb923c">• Permanent Bonding:</text>
    <text x="15" y="62" font-size="9.5" fill="#cbd5e1">Heated Teflon fuser rollers (~200°C) melt and press the plastic resin toner particles permanently into paper fibers.</text>
  </g>

  <!-- Step 6: Cleaning -->
  <g transform="translate(650, 295)">
    <rect width="270" height="175" rx="8" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect width="270" height="26" rx="6" fill="#7c3aed"/>
    <text x="135" y="18" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">6. Cleaning &amp; Discharge</text>
    <text x="15" y="45" font-size="10" font-weight="bold" fill="#a78bfa">• Readying Next Page:</text>
    <text x="15" y="62" font-size="9.5" fill="#cbd5e1">A rubber blade scrapes away leftover toner, and an erase lamp discharges the drum for the next page cycle.</text>
  </g>
</svg>
""")

SVG_DISPLAYS_AND_ACTUATORS = sanitize_svg("""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Output Engineering: Display Panels, Audio DAC, and Mechanical Actuators</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">How computers translate binary calculations into visual pixels, acoustic waves, and physical motion</text>

  <!-- Left: LCD/LED Display Sub-Pixel Shutter -->
  <g transform="translate(45, 95)">
    <rect width="420" height="380" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="420" height="28" rx="8" fill="#0284c7"/>
    <text x="210" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">A. Display Panel Physics (LCD &amp; LED)</text>
    
    <!-- Subpixel layers -->
    <rect x="25" y="45" width="370" height="65" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
    <rect x="35" y="55" width="40" height="45" rx="3" fill="#ef4444"/>
    <text x="55" y="82" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">R</text>
    <rect x="85" y="55" width="40" height="45" rx="3" fill="#10b981"/>
    <text x="105" y="82" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">G</text>
    <rect x="135" y="55" width="40" height="45" rx="3" fill="#38bdf8"/>
    <text x="155" y="82" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">B</text>
    <text x="280" y="75" font-size="10" font-weight="bold" fill="#38bdf8">RGB Sub-Pixel Cell</text>
    <text x="280" y="92" font-size="9" fill="#cbd5e1">256 intensity levels = 16.7M colors</text>

    <text x="25" y="135" font-size="10.5" font-weight="bold" fill="#38bdf8">• Liquid Crystal Light Shutters:</text>
    <text x="25" y="153" font-size="9.5" fill="#cbd5e1">Voltages twist liquid crystal molecules, adjusting polarization to pass or block backlight through RGB color filters.</text>

    <text x="25" y="210" font-size="10.5" font-weight="bold" fill="#34d399">• LED vs CCFL Backlight:</text>
    <text x="25" y="228" font-size="9.5" fill="#cbd5e1">Modern LED monitors replace bulky fluorescent tubes with solid-state light emitting diodes for ultra-thin, energy-efficient panels.</text>

    <rect x="25" y="280" width="370" height="80" rx="6" fill="#1e293b"/>
    <text x="35" y="305" font-size="10" font-weight="bold" fill="#38bdf8">Resolution &amp; Refresh Rate:</text>
    <text x="35" y="325" font-size="9" fill="#cbd5e1">4K (3840x2160 pixels) refreshed at 60 Hz to 144 Hz for fluid motion.</text>
  </g>

  <!-- Right: Audio DAC & Mechanical Actuators -->
  <g transform="translate(495, 95)">
    <rect width="420" height="380" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="420" height="28" rx="8" fill="#059669"/>
    <text x="210" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">B. Audio DAC &amp; Mechanical Actuators</text>

    <!-- DAC Audio -->
    <rect x="25" y="45" width="370" height="120" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
    <text x="35" y="70" font-size="11" font-weight="bold" fill="#34d399">1. Audio DAC &amp; Speaker Cone</text>
    <text x="35" y="90" font-size="9.5" fill="#e2e8f0">• <tspan fill="#38bdf8" font-weight="bold">DAC (Digital-to-Analog):</tspan> Converts binary audio numbers to varying electric currents.</text>
    <text x="35" y="112" font-size="9.5" fill="#e2e8f0">• <tspan fill="#fbbf24" font-weight="bold">Voice Coil &amp; Magnet:</tspan> Current vibrates a speaker diaphragm to generate acoustic sound pressure waves in air.</text>

    <!-- Actuators -->
    <rect x="25" y="180" width="370" height="180" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
    <text x="35" y="205" font-size="11" font-weight="bold" fill="#fbbf24">2. Robotic Actuators — Computer Limbs</text>
    <text x="35" y="228" font-size="9.5" fill="#e2e8f0">• <tspan fill="#38bdf8" font-weight="bold">Stepper / Servo Motors:</tspan> Precision angular movement in 3D printers, CNC mills, and robotic joints.</text>
    <text x="35" y="260" font-size="9.5" fill="#e2e8f0">• <tspan fill="#34d399" font-weight="bold">Solenoids:</tspan> Linear push/pull magnetic pins for automated security door locks and car starters.</text>
    <text x="35" y="292" font-size="9.5" fill="#e2e8f0">• <tspan fill="#c084fc" font-weight="bold">Pneumatic &amp; Hydraulic Valves:</tspan> Automated irrigation water gates, heavy crane pistons, and aircraft flaps.</text>
  </g>
</svg>
""")

# =====================================================================
# LESSON DATA SPECIFICATION: TOPIC 3
# =====================================================================

def build_topic3_curriculum():
    return [
        # -------------------------------------------------------------
        # LESSON 5: Input Devices and Data Capture
        # -------------------------------------------------------------
        {
            "unit_order": 1,
            "unit_name": "Input Devices and Data Capture",
            "unit_description": "Input devices as computational sensory organs, automated data capture vs manual keying, barcode and QR scanners, microphone ADC translation, and touchscreen engineering (resistive, capacitive, infrared).",
            "lesson_title": "Input Devices and Data Capture",
            "pages": [
                # Card 1: Hook & Goals
                [
                    {
                        "type": "suggested_image",
                        "title": "Internal Optical Mouse DSP Motion Tracking Mechanism",
                        "content": {
                            "title": "Internal Optical Mouse DSP Motion Tracking Mechanism",
                            "caption": "Inside an optical mouse showing the red LED illuminator, micro-lens prism, and Digital Signal Processor (DSP) optical sensor that captures thousands of surface pictures per second.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Optical_mouse_mechanism.jpg/800px-Optical_mouse_mechanism.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Input Peripherals & Data Capture",
                        "content": {
                            "title": "What We Will Master in This Lesson",
                            "goals": [
                                "Define **Input Device** and **Data Capture**.",
                                "Classify input devices into keying, pointing, scanning, audio, and touchscreen categories.",
                                "Analyze the engineering trade-offs of **Resistive**, **Capacitive**, and **Infrared** touchscreens.",
                                "Explain how **Analog-to-Digital Converters (ADCs)** translate physical sound pressure waves into digital binary audio.",
                                "Compare manual keying vs automated optical data capture (barcodes, QR codes, 3D scanners)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 'Sensory Organs' Analogy of Computing",
                        "content": {
                            "title": "Bridging the Physical and Digital Worlds",
                            "text": "Imagine your body without eyes, ears, or skin. You would be isolated from the world, unable to see light, hear voices, or feel temperature.\n\nIn a computer system, **Input Devices** serve as these sensory organs. The Central Processing Unit (CPU) understands only binary electrical pulses ($0$s and $1$s). It cannot directly read ink on paper or hear sound waves. Input devices bridge this gap by capturing physical stimuli and translating them into binary digital data streams."
                        }
                    }
                ],
                # Card 2: Keying & Pointing Devices
                [
                    {
                        "type": "concept_explanation",
                        "title": "Manual Keying and Coordinate Pointing Devices",
                        "content": {
                            "title": "From Key Matrices to Optical Mouse DSPs",
                            "text": "### 1. Keying Devices\n- **Keyboard**: Rows of keys over an electrical circuit matrix. Pressing a key sends a unique binary scan code (ASCII/Unicode) to the CPU.\n- **Numeric Keypad**: Grid of digits ($0-9$) and operators on the right side of keyboards, optimized for rapid one-handed numerical entry in banking and accounting.\n\n### 2. Pointing Devices\n- **Optical Mouse**: Shines an LED or laser onto the desk and takes thousands of microscopic pictures per second. A Digital Signal Processor (DSP) calculates surface displacement vectors, moving the screen cursor.\n- **Trackball**: Stationary base with an exposed rolling ball on top. Ideal for space-constrained desks and users with physical motor control limitations.\n- **Touchpad (Trackpad)**: Integrated laptop pad using capacitive sensing to track finger glide coordinates.\n- **Joystick & Light Pen**: Joysticks report directional pivot angles (used in flight simulators and cranes), while light pens detect screen raster beams for CAD drafting."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Essential Terminology: Input Systems",
                        "content": {
                            "title": "Core Definitions",
                            "terms": [
                                {"term": "Input Device", "definition": "A hardware peripheral used to send data and control signals into a computer for processing."},
                                {"term": "Data Capture", "definition": "The process of collecting physical or environmental data and converting it directly into digital binary form."}
                            ]
                        }
                    }
                ],
                # Card 3: Automated Data Capture Technologies
                [
                    {
                        "type": "concept_explanation",
                        "title": "Automated Scanning and Reading Devices",
                        "content": {
                            "title": "Eliminating Human Data-Entry Bottlenecks",
                            "text": "Manual typing is slow and prone to typographical errors. Automated scanning devices capture data directly from physical items:\n\n- **Flatbed Scanner**: A moving light bar illuminates documents; reflected light is focused onto Charge-Coupled Device (CCD) sensor arrays, digitizing high-resolution raster images.\n- **1D Barcode Reader**: Emits a red laser line across alternating black bars and white spaces. White spaces reflect light while black bars absorb it. A photodiode converts the reflection timings into product SKU numbers.\n- **2D QR Code Reader**: Captures two-dimensional matrix grids of black modules. Corner alignment targets allow instant decoding of URLs, contact cards, or payment IDs.\n- **3D Scanner**: Measures laser distances across thousands of points on a physical object's surface ('point cloud') to generate editable CAD 3D meshes."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Input Peripheral Classification & Data Capture Ecosystem",
                        "content": {
                            "svg_content": SVG_DATA_CAPTURE_ECOSYSTEM,
                            "caption": "Comprehensive classification of input devices showing manual keying, optical scanners, audio ADCs, and environmental telemetry sensors."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Retail Optical Barcode and QR Code Scanners",
                        "content": {
                            "title": "Retail Optical Barcode and QR Code Scanners",
                            "caption": "Handheld optical laser scanners reading product barcodes at a supermarket point of sale, converting light reflectance into instant inventory database queries.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Barcode_scanner_Symbol_LS2208.jpg/800px-Barcode_scanner_Symbol_LS2208.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    }
                ],
                # Card 4: Voice Input & ADC Mechanics
                [
                    {
                        "type": "concept_explanation",
                        "title": "Voice Input & Analog-to-Digital Converters (ADCs)",
                        "content": {
                            "title": "How Spoken Words Become Digital Code",
                            "text": "1. **Sound Wave Capture**: When you speak, vibrating air molecules hit a flexible microphone diaphragm.\n2. **Electrical Voltage Generation**: The vibrating diaphragm moves a coil near a magnet (or changes capacitance), generating a continuously fluctuating electrical voltage signal (Analog Sound).\n3. **Analog-to-Digital Converter (ADC)**: The sound card samples the voltage waveform thousands of times per second (e.g. 44,100 Hz), converting each wave height into a binary number.\n4. **Speech Recognition**: Machine learning algorithms analyze phoneme frequencies to transcribe spoken speech into text."
                        }
                    }
                ],
                # Card 5: Touch Screen Engineering
                [
                    {
                        "type": "concept_explanation",
                        "title": "Under the Hood: Touch Screen Engineering",
                        "content": {
                            "title": "Resistive vs. Capacitive vs. Infrared Mechanics",
                            "text": "Touchscreens act as both an input and output device. Their internal sensing mechanisms differ fundamentally:\n\n- **Resistive**: Two flexible conductive sheets separated by tiny spacer dots. Physical pressure pushes layers together, completing a voltage circuit. Cheap and works with gloves, but lacks multi-touch.\n- **Capacitive**: Coated glass holding a continuous electrostatic charge. A human finger draws a tiny current to that point, dropping capacitance. Enables multi-touch pinch-to-zoom, but fails with non-conductive plastic gloves.\n- **Infrared (IR)**: Frame of infrared LEDs and sensors creating an invisible light grid across the screen. Touching interrupts light beams. Works even if glass is shattered."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Touchscreen Technologies Cross-Section & Working Principles",
                        "content": {
                            "svg_content": SVG_TOUCHSCREEN_TECH,
                            "caption": "Cross-sectional engineering comparison of Resistive (conductive sheets), Capacitive (electrostatic grid), and Infrared (optical beam grid) touchscreens."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Touch Screen Technology Matrix",
                        "content": {
                            "headers": ["Technology", "Detection Principle", "Key Advantages", "Major Limitations", "Typical Applications"],
                            "rows": [
                                ["**Resistive**", "Physical pressure joins flexible sheets", "Works with gloves/pens, cheap, waterproof", "Easily scratched, no multi-touch, lower clarity", "POS terminals, factory controllers, ATMs"],
                                ["**Capacitive**", "Human finger disrupts electrostatic field", "Superb clarity, responsive, multi-touch gestures", "Fails with standard plastic gloves, cracked glass", "Smartphones, tablets, modern touch laptops"],
                                ["**Infrared (IR)**", "Finger breaks invisible optical light beams", "100% clarity, works with anything, rugged", "Dust/insects in bezel cause false clicks", "Large interactive school whiteboards, kiosks"]
                            ]
                        }
                    }
                ],
                # Card 6: Interactive Diagnostics Activity
                [
                    {
                        "type": "mini_activity",
                        "title": "Diagnostics Lab: Troubleshooting Touchscreen Malfunctions",
                        "content": {
                            "title": "Field Technician Challenge",
                            "text": "Diagnose the underlying touchscreen technology and explain the cause of failure for these 3 customer issues:\n\n1. **Case 1**: A bank ATM screen has a deep gouge on its surface, but still registers inputs if customers press firmly with their knuckles.\n2. **Case 2**: A smartphone works inside the home, but ignores all touch inputs when the user wears heavy woolen gloves in the cold.\n3. **Case 3**: An interactive whiteboard in a dusty school workshop registers phantom 'ghost clicks' in the bottom-left corner when nobody is touching it."
                        }
                    }
                ],
                # Card 7: Educational Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "How Touchscreens and Optical Barcode Scanners Work",
                        "content": {
                            "title": "Inside Touchscreens & Optical Scanners",
                            "youtube_id": "8P_53j8g_iA",
                            "url": "https://www.youtube.com/watch?v=8P_53j8g_iA",
                            "description": "An engaging visual breakdown of capacitive electrostatic tracking, resistive membrane contact, and laser barcode scanning."
                        }
                    }
                ],
                # Card 8: Application Scenario & Formative Assessment
                [
                    {
                        "type": "worked_example",
                        "title": "Real-World Engineering: Kenya Wildlife Sanctuary Project",
                        "content": {
                            "title": "Designing Peripheral Systems for National Parks",
                            "problem": "A wildlife conservancy near Tsavo needs to capture: (1) Lion border crossings, (2) Ambient temperature and humidity, (3) High-resolution bird images.",
                            "steps": [
                                "**1. Lion Border Tracking**: Install automated infrared beam trip sensors and underground seismic vibration sensors (Automated Data Capture).",
                                "**2. Temperature & Humidity**: Install digital IoT environmental sensor probes transmitting hourly binary telemetry via wireless radio (Automated Data Capture).",
                                "**3. High-Resolution Bird Identification**: Deploy motion-activated optical digital camera traps with night-vision infrared illumination (Automated Optical Capture)."
                            ]
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 1: Supermarket Scanner Efficiency",
                        "content": {
                            "question": "Why is scanning a 1D barcode at a supermarket checkout vastly superior to manual keyboard entry?",
                            "options": [
                                "Barcode scanners reduce human typographical error and process items in fractions of a second",
                                "Barcodes transmit audio signals to the cash register",
                                "Keyboards cannot enter numbers above 10",
                                "Barcode scanners do not require electricity to run"
                            ],
                            "correct": "A",
                            "explanation": "Automated optical data capture reads printed barcodes directly, eliminating manual typing errors and accelerating checkout throughput."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 2: Capacitive Touchscreen Physics",
                        "content": {
                            "question": "Why does a capacitive touchscreen fail to register input from a plastic pen cap?",
                            "options": [
                                "Plastic is too soft to break the glass layer",
                                "Plastic is an electrical insulator and cannot alter the screen's electrostatic capacitance field",
                                "The infrared light beams pass straight through plastic",
                                "The plastic cap blocks the cooling vents"
                            ],
                            "correct": "B",
                            "explanation": "Capacitive touchscreens require an electrically conductive object (like a bare finger or conductive stylus) to draw current and disrupt the electrostatic field."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 3: ADC Audio Sampling",
                        "content": {
                            "question": "What is the primary function of an Analog-to-Digital Converter (ADC) during voice recording?",
                            "options": [
                                "To amplify the physical sound waves in the room",
                                "To convert continuous electrical voltage sound waveforms into discrete binary numbers",
                                "To print spoken words on laser paper",
                                "To cool the CPU heatsink"
                            ],
                            "correct": "B",
                            "explanation": "An ADC samples the continuous analog voltage waveform from a microphone thousands of times per second and quantizes each sample into binary numbers."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Lesson 5 Key Takeaways",
                        "content": {
                            "text": "1. **Input Function**: Bridges human physical stimuli and the CPU's binary processing language.\n2. **Automated Capture**: Scanners and sensors eliminate human typographical errors and speed up data entry.\n3. **Audio Input**: Microphones and sound card ADCs sample sound wave voltages into binary audio files.\n4. **Touchscreen Technologies**: Resistive (pressure), Capacitive (electrostatic charge), Infrared (optical light grid)."
                        }
                    }
                ]
            ]
        },

        # -------------------------------------------------------------
        # LESSON 6: Output Devices and Presenting Information
        # -------------------------------------------------------------
        {
            "unit_order": 2,
            "unit_name": "Output Devices and Presenting Information",
            "unit_description": "Output peripherals as the computer's voice and limbs, soft copy vs hard copy, monitor display technologies (CRT, LCD, LED, Projectors), printing mechanics (laser, inkjet, plotters), DAC audio translation, and physical mechanical actuators.",
            "lesson_title": "Output Devices and Presenting Information",
            "pages": [
                # Card 1: Hook & Goals
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Output Devices",
                        "content": {
                            "title": "What We Will Master in This Lesson",
                            "goals": [
                                "Define **Output Device**, **Soft Copy**, and **Hard Copy**.",
                                "Distinguish between display technologies (**CRT**, **LCD**, **LED**, **Projectors**).",
                                "Analyze printing mechanics: **Inkjet** (micro-nozzles), **Laser** (electrostatic fusing), and **Plotters** (vector pens).",
                                "Explain how **Digital-to-Analog Converters (DACs)** and voice coils generate sound waves in speakers.",
                                "Define **Actuators** and analyze how computers trigger real-world physical mechanical actions."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 'Voice and Limbs' Analogy of Computing",
                        "content": {
                            "title": "Giving Form to Silent Binary Processing",
                            "text": "The CPU and RAM calculate in absolute silence, manipulating billions of binary bits per second. Without output devices, all this computation remains trapped inside silicon chips!\n\n**Output Devices** act as the computer's voice, display screen, and mechanical limbs. They translate silent binary data back into visual pixels, printed text, audible speech, or physical mechanical movement."
                        }
                    }
                ],
                # Card 2: Soft Copy vs Hard Copy Output Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Comparative Analysis: Soft Copy vs. Hard Copy Output",
                        "content": {
                            "headers": ["Feature", "Soft Copy Output (e.g. LED Monitor)", "Hard Copy Output (e.g. Laser Print)"],
                            "rows": [
                                ["**Tangibility**", "Virtual / Intangible (cannot be touched physically)", "Physical / Tangible (printed paper, card, 3D model)"],
                                ["**Permanence**", "Transient / Temporary (disappears when powered off)", "Permanent (readable indefinitely with zero power)"],
                                ["**Modification**", "Instant real-time updates and interactive animations", "Static (requires full reprinting to alter text)"],
                                ["**Power Requirement**", "Requires continuous active electrical power to display", "Requires zero electrical power once printed"],
                                ["**Distribution Cost**", "Near-zero cost to transmit globally across the internet", "Physical logistics, transport, and paper material costs"]
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Essential Terminology: Output Classifications",
                        "content": {
                            "title": "Core Output Definitions",
                            "terms": [
                                {"term": "Output Device", "definition": "A hardware peripheral that converts processed digital binary data into human-understandable or physical action."},
                                {"term": "Soft Copy", "definition": "Non-permanent, electronic output that exists temporarily on a display screen or speaker."},
                                {"term": "Hard Copy", "definition": "Tangible, permanent physical output printed on media such as paper, plastic, or fabric."}
                            ]
                        }
                    }
                ],
                # Card 3: Display Technologies (CRT, LCD, LED, Projector)
                [
                    {
                        "type": "concept_explanation",
                        "title": "Visual Displays: From Electron Guns to LED Backlights",
                        "content": {
                            "title": "The Evolution of Screen Technology",
                            "text": "### 1. CRT (Cathode Ray Tube) Monitors\nOlder, bulky box monitors. Fired beams of electrons at red, green, and blue phosphor dots. High power draw, heavy weight, and significant heat generation.\n\n### 2. LCD (Liquid Crystal Display) Monitors\nFlat, energy-efficient panels. Backlight shines through millions of pixels containing liquid crystals. When electrical currents twist the crystals, they act as microscopic shutters, blocking or passing light through color filters.\n\n### 3. LED Monitors\nAn advanced subclass of LCDs. Replaces bulky fluorescent backlights with an array of energy-efficient **Light Emitting Diodes (LEDs)**. Delivers deeper black levels, thinner panels, and superior energy efficiency.\n\n### 4. Digital Projectors\nFocus high-intensity lamps through internal lenses to project slideshows onto large auditorium walls, ideal for teaching groups of 50+ students."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "High-Definition Modern LED Display Screen",
                        "content": {
                            "title": "High-Definition Modern LED Display Screen",
                            "caption": "An ultra-thin LED monitor displaying high-contrast imagery, utilizing an array of energy-efficient solid-state light emitting diodes for backlighting.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Monitor_LED.jpg/800px-Monitor_LED.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    }
                ],
                # Card 4: Printing Mechanics (Laser, Inkjet, Plotter)
                [
                    {
                        "type": "concept_explanation",
                        "title": "Hard Copy Printing Engineering",
                        "content": {
                            "title": "How Printers Transfer Digital Text to Paper",
                            "text": "### 1. Laser Printers\n- **Mechanics**: Uses static electricity, a laser beam, fine toner powder (dry ink), and heated rollers.\n- **Strengths**: Extremely fast (30+ pages/minute), razor-sharp text, low cost-per-page for large office volumes.\n\n### 2. Inkjet Printers\n- **Mechanics**: Moves a print head with thousands of microscopic nozzles across paper, spraying tiny droplets of liquid ink.\n- **Strengths**: Exceptional high-resolution photo blending and color transitions, but higher ink replacement costs.\n\n### 3. Vector Plotters\n- **Mechanics**: Holds physical ink pens on robotic mechanical arms, drawing continuous line vectors across massive architectural sheets ($A0/A1$).\n- **Strengths**: Giant blueprints, structural maps, and CAD drawings without pixel aliasing."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Laser Printer 6-Stage Electrostatic Cycle",
                        "content": {
                            "svg_content": SVG_LASER_PRINTER_CYCLE,
                            "caption": "The 6-step electrostatic laser printing sequence: Charging, Laser Exposure, Toner Development, Transfer, Heat Fusing, and Cleaning."
                        }
                    }
                ],
                # Card 5: Audio Output & Physical Actuators
                [
                    {
                        "type": "concept_explanation",
                        "title": "Audio Transducers & Mechanical Actuators",
                        "content": {
                            "title": "From Sound Waves to Robotic Muscles",
                            "text": "### Audio Output (DAC + Speakers)\nA **Digital-to-Analog Converter (DAC)** on the sound card converts binary numbers into varying electric currents. This current passes through a wire coil attached to a speaker cone. The changing magnetic fields push and pull against a permanent magnet, vibrating the cone to create physical sound waves in air.\n\n### Actuators: The Muscles of Computing\nAn **Actuator** is an output device that converts electrical control signals from a computer into **physical mechanical motion**:\n- **Electric Motors / Steppers**: Spins robotic joints, drives conveyor belts, or adjusts camera zoom lenses.\n- **Solenoids**: Pushes or pulls a locking pin (e.g. magnetic security door locks).\n- **Hydraulic & Pneumatic Valves**: Opens and closes water pipelines in automated agricultural drip systems."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Display Pixels, Audio DAC, and Actuator Architectures",
                        "content": {
                            "svg_content": SVG_DISPLAYS_AND_ACTUATORS,
                            "caption": "Visual breakdown of LCD RGB sub-pixel shutters, DAC audio loudspeaker voice coils, and computer-controlled robotic servo actuators."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Industrial Robotic Actuator Arm on Automated Production Line",
                        "content": {
                            "title": "Industrial Robotic Actuator Arm on Automated Production Line",
                            "caption": "A computer-controlled multi-axis robotic arm with servo actuators executing precision mechanical manufacturing assembly.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/KUKA_Industrial_Robots_IR.jpg/800px-KUKA_Industrial_Robots_IR.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    }
                ],
                # Card 6: Output System Architect Activity & Troubleshooting
                [
                    {
                        "type": "mini_activity",
                        "title": "Output Architect Challenge: Designing System Peripherals",
                        "content": {
                            "title": "Matching Output Peripherals to School Requirements",
                            "text": "Recommend the ideal output device for each task and justify your choice:\n1. **Teacher**: Presenting daily biology slide decks to 45 students in a classroom $\\longrightarrow$ *Digital Multimedia Projector*.\n2. **Principal's Office**: Printing 800 student report cards every term at minimum cost $\\longrightarrow$ *High-Speed Laser Printer*.\n3. **Greenhouse**: Automatically opening roof ventilation flaps when internal temperature exceeds 30°C $\\longrightarrow$ *Electric Motor Actuator*.\n\n### Troubleshooting Diagnosis\n*A student prints a term paper on a laser printer. The page emerges, but the black text smudges off as loose powder when touched. Which component failed?*\n- **Diagnosis**: The **Fuser Unit** (heating/pressure rollers) failed to heat to ~200°C to melt the plastic toner resin into the paper fibers."
                        }
                    }
                ],
                # Card 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "How a Laser Printer Works & Audio DAC Output",
                        "content": {
                            "title": "Inside the Laser Printer & Sound Generation",
                            "youtube_id": "WB0HnXcW8qQ",
                            "url": "https://www.youtube.com/watch?v=WB0HnXcW8qQ",
                            "description": "A clear mechanical animation showing how the rotating drum, laser, toner powder, and heated fuser assemble printed pages in seconds."
                        }
                    }
                ],
                # Card 8: Automated Flood Warning System & Formative MCQs
                [
                    {
                        "type": "worked_example",
                        "title": "Applied Scenario: Kenyan Automated River Flood Warning System",
                        "content": {
                            "title": "Designing a Community Safety Output Architecture",
                            "problem": "A town along the Tana River needs an automated flood warning system connected to water level sensors.",
                            "steps": [
                                "**Output 1: Emergency Dashboard Monitor**: Displays real-time water elevation graphs inside the disaster response center (Soft Copy Visual Display).",
                                "**Output 2: Acoustic Siren**: Sound card DAC powers loud speaker horns across the village if water crosses dangerous levels (Audible Soft Copy).",
                                "**Output 3: Motorized Floodgate Actuator**: Microcontroller triggers an electric actuator motor to lower a heavy steel barrier across the main highway (Mechanical Action)."
                            ]
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 1: Soft Copy Examples",
                        "content": {
                            "question": "Which of the following is the best example of a 'Soft Copy' output?",
                            "options": [
                                "A high-resolution presentation projected onto an auditorium screen",
                                "A printed 10-page textbook chapter",
                                "An architectural blueprint drawn with a pen plotter",
                                "A laminated student ID card"
                            ],
                            "correct": "A",
                            "explanation": "Projected images and monitor screens are soft copies because they are temporary and disappear once the power is switched off."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 2: Actuator Function",
                        "content": {
                            "question": "What is the primary operational role of an actuator in a computer-controlled system?",
                            "options": [
                                "To display 4K video pixels",
                                "To convert electrical digital control signals into physical mechanical movement",
                                "To convert spoken audio into binary text",
                                "To scan barcodes on product packaging"
                            ],
                            "correct": "B",
                            "explanation": "An actuator converts electrical commands into physical mechanical motion, such as moving a robotic arm, unlocking a door, or turning a valve."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 3: Laser Printing Toner Fusing",
                        "content": {
                            "question": "If printed text rubs off a laser-printed sheet as loose black dust, which stage of the printing cycle failed?",
                            "options": [
                                "The Primary Corona charging wire",
                                "The Laser exposure scanning mirror",
                                "The Heated Teflon fuser rollers",
                                "The Paper feed stepper motor"
                            ],
                            "correct": "C",
                            "explanation": "The fuser unit applies intense heat (~200°C) and pressure to melt plastic toner resin permanently into paper fibers. If it fails to heat, toner remains dry loose powder."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Lesson 6 Key Takeaways",
                        "content": {
                            "text": "1. **Soft vs Hard Copy**: Soft copy is transient and digital; hard copy is permanent on physical media.\n2. **Displays**: LED monitors use energy-efficient diode backlighting behind liquid crystal shutters.\n3. **Laser Printing**: Uses electrostatics to attract toner, followed by heat fusing.\n4. **Audio Output**: DACs translate binary audio files into analog currents to vibrate speaker cones.\n5. **Actuators**: The mechanical limbs that translate software code into real-world physical motion."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_grade10_topic3(replace=True):
    print("=" * 80)
    print("INGESTING TOPIC 3: Input/Output (I/O) Devices (Grade 10 Computer Science)")
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
        order=3,
        defaults={"name": "Input/Output (I/O) Devices", "description": "Input peripherals, data capture technologies, output devices, display/printing mechanics, and actuators."}
    )
    if not t_created:
        topic.name = "Input/Output (I/O) Devices"
        topic.description = "Input peripherals, data capture technologies, output devices, display/printing mechanics, and actuators."
        topic.save()
    print(f"[*] Resolved Topic 3: {topic.name} (ID: {topic.id})")

    if replace:
        print("[*] Replacing existing Topic 3 units, lessons, blocks, and assets...")
        existing_lessons = Lesson.objects.filter(topic=topic)
        LessonAsset.objects.filter(lesson__in=existing_lessons).delete()
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    curriculum_data = build_topic3_curriculum()
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
                    "topic_order": 3,
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
                        block_id=f"g10_cs_t3_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={"topic_order": 3, "unit_order": u_order, "page": page_idx}
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
    print(f"TOPIC 3 INGESTION COMPLETE:")
    print(f"  Units Created:   {total_units}")
    print(f"  Lessons Created: {total_lessons}")
    print(f"  Pages Created:   {total_pages}")
    print(f"  Blocks Created:  {total_blocks}")
    print(f"  Assets Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_grade10_topic3(replace=True)
