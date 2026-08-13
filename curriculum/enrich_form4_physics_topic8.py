"""
VLearn Form 4 Physics — Topic 8: X-Rays
Visual Enrichment Engine (Enhanced High-Contrast SVGs + Wikimedia Commons)

Enriches Topic 8 (X-Rays) with:
  - 12 high-precision, high-contrast dark-mode vector SVG diagrams
  - 3 authentic Wikimedia Commons photographic assets

Usage:
  /home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/venv/bin/python curriculum/enrich_form4_physics_topic8.py
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)
from curriculum.media_orchestration.visual_intelligence.svg_sanitizer import validate_and_sanitize_svg

BG = "#090d16"
TEXT_MAIN = "#f8fafc"
TEXT_MUTED = "#cbd5e1"

def clean_svg(svg_code: str) -> str:
    is_valid, sanitized, err = validate_and_sanitize_svg(svg_code)
    if is_valid:
        return sanitized
    print(f"  [Warning] SVG Sanitization warning: {err}")
    return svg_code

def wrap_svg(inner_content, W=840, H=420, title=""):
    title_svg = ""
    if title:
        title_svg = (
            f'<text x="{W//2}" y="32" fill="{TEXT_MAIN}" font-family="system-ui, -apple-system, sans-serif" '
            f'font-size="16" font-weight="800" text-anchor="middle" letter-spacing="0.5">{title}</text>'
        )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" height="100%">'
        f'<rect width="{W}" height="{H}" fill="{BG}" rx="16"/>'
        f'{title_svg}'
        f'{inner_content}'
        f'</svg>'
    )

def attach_svg_to_block(lesson, page_num, block_type, title, filename_base, svg_str):
    sanitized = clean_svg(svg_str)
    
    block = LessonBlock.objects.filter(
        lesson=lesson,
        page_number=page_num,
        block_type=block_type
    ).first()

    if not block:
        block = LessonBlock.objects.create(
            lesson=lesson,
            page_number=page_num,
            page_title=title,
            title=title,
            block_type=block_type,
            component_type=block_type,
            component_order=15,
            order=page_num * 10,
            metadata={"svg_content": sanitized},
            content={"text": title, "svg_content": sanitized, "svg": sanitized}
        )
    else:
        block.title = title
        if not block.metadata:
            block.metadata = {}
        block.metadata["svg_content"] = sanitized
        if not isinstance(block.content, dict):
            block.content = {}
        block.content["svg_content"] = sanitized
        block.content["svg"] = sanitized
        block.save()

    asset = LessonAsset.objects.filter(lesson=lesson, blocks=block, source_type="ai_generated").first()
    if not asset:
        asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="diagram",
            source_type="ai_generated",
            storage_type="embed",
            status="approved",
            title=title,
            description=f"Sanitized vector diagram: {title}",
            metadata={"svg_content": sanitized}
        )
        block.assets.add(asset)
    else:
        asset.title = title
        asset.storage_type = "embed"
        asset.metadata = {**(asset.metadata or {}), "svg_content": sanitized}
        asset.save()

    print(f"  [Page {page_num:2d}] SVG attached: '{title[:50]}' (Asset ID: {asset.id})")
    return asset

def attach_wikimedia_to_block(lesson, page_num, title, verified_url, author, licensing, commons_page):
    block = LessonBlock.objects.filter(
        lesson=lesson,
        page_number=page_num,
        block_type="suggested_image"
    ).first()

    if not block:
        block = LessonBlock.objects.create(
            lesson=lesson,
            page_number=page_num,
            page_title=title,
            title=title,
            block_type="suggested_image",
            component_type="suggested_image",
            component_order=20,
            order=page_num * 10 + 5,
            content={"text": title, "resolved_image_url": verified_url, "url": verified_url}
        )
    else:
        block.title = title
        if not isinstance(block.content, dict):
            block.content = {}
        block.content["resolved_image_url"] = verified_url
        block.content["url"] = verified_url
        block.save()

    meta = {
        "author": author,
        "licensing": licensing,
        "commons_page_url": commons_page,
    }
    asset = LessonAsset.objects.filter(lesson=lesson, blocks=block, source_type="external").first()
    if not asset:
        asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="image",
            source_type="external",
            storage_type="url",
            status="approved",
            title=title,
            description=f"Wikimedia Commons photographic asset: {title}",
            url=verified_url,
            metadata=meta
        )
        block.assets.add(asset)
    else:
        asset.title = title
        asset.url = verified_url
        asset.metadata = meta
        asset.save()
    print(f"  [Page {page_num:2d}] Wikimedia attached: '{title[:50]}' (Asset ID: {asset.id})")
    return asset


# =============================================================================
# ENHANCED SVG BUILDERS — MODULE 8.1
# =============================================================================

def svg_m81_coolidge_tube_schematic():
    """Page 2: Modern Coolidge X-Ray Tube construction schematic"""
    inner = """
    <!-- Outer Glass Tube Envelope -->
    <path d="M 60,150 L 220,150 L 260,100 L 580,100 L 620,150 L 780,150 L 780,270 L 620,270 L 580,320 L 260,320 L 220,270 L 60,270 Z" fill="#111827" stroke="#38bdf8" stroke-width="3"/>
    <text x="420" y="80" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">Evacuated Glass Envelope (&lt; 10⁻⁶ mmHg Vacuum)</text>

    <!-- Cathode Filament & Focusing Cup -->
    <rect x="80" y="180" width="50" height="60" fill="#1e293b" rx="4" stroke="#f59e0b" stroke-width="2"/>
    <path d="M 130,200 L 160,200 L 160,220 L 130,220" fill="none" stroke="#ef4444" stroke-width="4"/>
    <path d="M 170,180 Q 150,210 170,240" fill="none" stroke="#f59e0b" stroke-width="4"/>
    <rect x="70" y="255" width="120" height="24" fill="#ef444420" rx="4" stroke="#ef4444"/>
    <text x="130" y="271" fill="#ef4444" font-size="11" font-weight="800" text-anchor="middle">Filament Cathode (6V)</text>

    <!-- Electron Beam Stream -->
    <line x1="170" y1="210" x2="620" y2="210" stroke="#38bdf8" stroke-width="5" stroke-dasharray="8 4"/>
    <text x="390" y="195" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">Accelerated Electrons (e⁻) →</text>

    <!-- Slanted Tungsten Target Anode Block -->
    <polygon points="620,160 660,200 660,260 620,260" fill="#78350f" stroke="#f59e0b" stroke-width="2"/>
    <polygon points="620,185 640,205 640,235 620,235" fill="#eab308"/>
    <rect x="580" y="280" width="130" height="24" fill="#f59e0b20" rx="4" stroke="#f59e0b"/>
    <text x="645" y="296" fill="#f59e0b" font-size="11" font-weight="800" text-anchor="middle">Tungsten Target (45° Angle)</text>

    <!-- Solid Copper Cooling Stem & Radiator Fins -->
    <rect x="660" y="180" width="80" height="60" fill="#b45309" rx="2"/>
    <line x1="740" y1="160" x2="740" y2="260" stroke="#b45309" stroke-width="6"/>
    <line x1="755" y1="160" x2="755" y2="260" stroke="#b45309" stroke-width="6"/>
    <line x1="770" y1="160" x2="770" y2="260" stroke="#b45309" stroke-width="6"/>
    <text x="755" y="280" fill="#b45309" font-size="11" font-weight="800" text-anchor="middle">Copper Fins</text>

    <!-- Emitted X-Ray Beam Photons -->
    <path d="M 630,210 Q 620,260 640,310 T 630,360" fill="none" stroke="#eab308" stroke-width="4"/>
    <path d="M 640,210 Q 630,260 650,310 T 640,360" fill="none" stroke="#eab308" stroke-width="4"/>
    <polygon points="630,360 622,345 638,345" fill="#eab308"/>
    <rect x="570" y="375" width="150" height="26" fill="#eab30820" rx="6" stroke="#eab308"/>
    <text x="645" y="392" fill="#eab308" font-size="12" font-weight="800" text-anchor="middle">Emitted X-Ray Beam Photons</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Modern Coolidge X-Ray Tube Construction: Cathode, Tungsten Target, and Cooling Fins")

def svg_m81_anode_cooling_mechanism():
    """Page 3: Anode energy dissipation and copper oil cooling circulator"""
    inner = """
    <!-- Left Panel: Tungsten Target Anode Block (x = 40, w = 360) -->
    <g transform="translate(40, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="12" stroke="#f59e0b" stroke-width="2"/>
      <text x="180" y="32" fill="#f59e0b" font-size="14" font-weight="800" text-anchor="middle">TUNGSTEN TARGET ANODE (Z = 74)</text>

      <polygon points="60,80 120,80 160,200 100,200" fill="#eab308" stroke="#f59e0b" stroke-width="2"/>
      <text x="110" y="145" fill="#000" font-size="13" font-weight="800" text-anchor="middle">Tungsten (3422°C)</text>

      <rect x="120" y="100" width="200" height="80" fill="#b45309" rx="4"/>
      <text x="220" y="145" fill="#fff" font-size="13" font-weight="800" text-anchor="middle">Solid Copper Stem</text>

      <rect x="20" y="220" width="320" height="70" fill="#1e293b" rx="8" stroke="#f59e0b"/>
      <text x="180" y="245" fill="#f8fafc" font-size="13" font-weight="800" text-anchor="middle">High Atomic Number (Z = 74)</text>
      <text x="180" y="270" fill="#cbd5e1" font-size="11" text-anchor="middle">High Z maximizes electron deceleration energy loss</text>
    </g>

    <!-- Right Panel: Circulating Cooling Oil System (x = 440, w = 360) -->
    <g transform="translate(440, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="12" stroke="#38bdf8" stroke-width="2"/>
      <text x="180" y="32" fill="#38bdf8" font-size="14" font-weight="800" text-anchor="middle">OIL HEAT EXCHANGER CIRCULATOR</text>

      <rect x="40" y="70" width="280" height="150" fill="#0284c715" rx="10" stroke="#0284c7" stroke-width="2"/>

      <path d="M 60,100 L 300,100 L 300,190 L 60,190 Z" fill="none" stroke="#0284c7" stroke-width="6"/>
      <path d="M 100,100 L 120,85 M 220,100 L 240,85 M 260,190 L 240,205" fill="none" stroke="#38bdf8" stroke-width="4"/>

      <text x="180" y="145" fill="#38bdf8" font-size="15" font-weight="800" text-anchor="middle">Continuous Oil Pump</text>

      <rect x="20" y="235" width="320" height="55" fill="#22c55e15" rx="8" stroke="#22c55e"/>
      <text x="180" y="258" fill="#22c55e" font-size="13" font-weight="800" text-anchor="middle">Rapid Thermal Conduction</text>
      <text x="180" y="278" fill="#cbd5e1" font-size="11" text-anchor="middle">Prevents target melting under 99% thermal load</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Target Anode Material Selection and Circulating Oil Thermal Heat Dissipation System")

def svg_m81_energy_conversion_pie():
    """Page 4: Energy partition pie chart (99% Heat vs 1% X-Rays)"""
    inner = """
    <!-- Left Side: Pie Chart (x = 220, y = 210, r = 130) -->
    <g transform="translate(220, 210)">
      <path d="M 0,0 L 130,0 A 130,130 0 1,1 129.8,-7.4 Z" fill="#ef4444" stroke="#7f1d1d" stroke-width="3"/>
      <path d="M 0,0 L 129.8,-7.4 A 130,130 0 0,1 130,0 Z" fill="#22c55e" stroke="#14532d" stroke-width="3"/>
      
      <circle cx="0" cy="0" r="45" fill="#090d16" stroke="#f8fafc" stroke-width="2"/>
      <text x="0" y="8" fill="#f8fafc" font-size="15" font-weight="800" text-anchor="middle">E_k</text>
    </g>

    <!-- Right Side: Detailed Breakdown (x = 440, w = 360) -->
    <g transform="translate(440, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="12" stroke="#475569" stroke-width="2"/>
      <text x="180" y="32" fill="#f8fafc" font-size="14" font-weight="800" text-anchor="middle">ENERGY CONVERSION EFFICIENCY</text>

      <rect x="25" y="65" width="22" height="22" fill="#ef4444" rx="4"/>
      <text x="60" y="82" fill="#ef4444" font-size="15" font-weight="800">&gt; 99% THERMAL HEAT</text>
      <text x="60" y="104" fill="#cbd5e1" font-size="12">Anode lattice vibrations &amp; heat loss</text>

      <rect x="25" y="145" width="22" height="22" fill="#22c55e" rx="4"/>
      <text x="60" y="162" fill="#22c55e" font-size="15" font-weight="800">&lt; 1% X-RAY PHOTONS</text>
      <text x="60" y="184" fill="#cbd5e1" font-size="12">Useful Bremsstrahlung &amp; characteristic rays</text>

      <rect x="20" y="230" width="320" height="60" fill="#1e293b" rx="8" stroke="#22c55e"/>
      <text x="180" y="255" fill="#22c55e" font-size="13" font-weight="800" text-anchor="middle">Max X-Ray Photon Energy Formula</text>
      <text x="180" y="276" fill="#f8fafc" font-size="13" font-weight="700" text-anchor="middle">e V_acc = h f_max = hc / λ_min</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="X-Ray Tube Energy Partition: Over 99% Thermal Heat Loss vs. Under 1% X-Ray Photons")

def svg_m81_intensity_vs_hardness():
    """Page 7: Independent controls (Hardness vs Intensity)"""
    inner = """
    <!-- Left Panel: Hardness Control (Accelerating Voltage V_acc) (x = 40, w = 360) -->
    <g transform="translate(40, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="12" stroke="#38bdf8" stroke-width="2"/>
      <text x="180" y="32" fill="#38bdf8" font-size="14" font-weight="800" text-anchor="middle">1. HARDNESS / QUALITY CONTROL</text>

      <circle cx="180" cy="115" r="52" fill="#1e293b" stroke="#38bdf8" stroke-width="4"/>
      <line x1="180" y1="115" x2="215" y2="85" stroke="#38bdf8" stroke-width="5"/>
      <text x="180" y="190" fill="#fff" font-size="14" font-weight="800" text-anchor="middle">Accelerating Voltage V_acc (kV)</text>

      <rect x="20" y="225" width="320" height="65" fill="#0284c715" rx="8" stroke="#0284c7"/>
      <text x="180" y="248" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">Controls Photon Energy &amp; Frequency!</text>
      <text x="180" y="270" fill="#cbd5e1" font-size="11" text-anchor="middle">Higher kV = Shorter λ_min = Deeper Penetration</text>
    </g>

    <!-- Right Panel: Intensity Control (Filament Heating Current If) (x = 440, w = 360) -->
    <g transform="translate(440, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="12" stroke="#f59e0b" stroke-width="2"/>
      <text x="180" y="32" fill="#f59e0b" font-size="14" font-weight="800" text-anchor="middle">2. INTENSITY / QUANTITY CONTROL</text>

      <circle cx="180" cy="115" r="52" fill="#1e293b" stroke="#f59e0b" stroke-width="4"/>
      <line x1="180" y1="115" x2="145" y2="85" stroke="#f59e0b" stroke-width="5"/>
      <text x="180" y="190" fill="#fff" font-size="14" font-weight="800" text-anchor="middle">Filament Current I_f (mA)</text>

      <rect x="20" y="225" width="320" height="65" fill="#f59e0b15" rx="8" stroke="#f59e0b"/>
      <text x="180" y="248" fill="#f59e0b" font-size="13" font-weight="800" text-anchor="middle">Controls Beam Density &amp; Count!</text>
      <text x="180" y="270" fill="#cbd5e1" font-size="11" text-anchor="middle">Higher mA = More electrons/sec = Brighter beam</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Independent X-Ray Control Mechanisms: Accelerating Voltage (Hardness) vs. Filament Current (Intensity)")

def svg_m81_xray_sandbox():
    """Page 8: Interactive X-Ray sandbox diagram model"""
    inner = """
    <rect x="80" y="80" width="400" height="280" fill="#111827" rx="12" stroke="#38bdf8" stroke-width="3"/>

    <rect x="90" y="190" width="20" height="40" fill="#ef4444" rx="2"/>
    <text x="100" y="245" fill="#ef4444" font-size="11" font-weight="800" text-anchor="middle">Filament</text>

    <line x1="110" y1="210" x2="400" y2="210" stroke="#38bdf8" stroke-width="4" stroke-dasharray="6 3"/>

    <polygon points="400,180 430,210 430,240 400,240" fill="#f59e0b"/>
    <rect x="430" y="195" width="40" height="30" fill="#b45309"/>

    <path d="M 415,210 Q 405,260 425,310" fill="none" stroke="#f59e0b" stroke-width="3"/>
    <path d="M 425,210 Q 415,260 435,310" fill="none" stroke="#f59e0b" stroke-width="3"/>

    <g transform="translate(520, 60)">
      <rect x="0" y="0" width="280" height="320" fill="#111827" rx="10" stroke="#38bdf8" stroke-width="2"/>
      <text x="140" y="25" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">INTERACTIVE X-RAY SLIDERS</text>

      <text x="15" y="60" fill="#cbd5e1" font-size="11">Filament Current I_f (mA):</text>
      <rect x="15" y="70" width="250" height="10" fill="#1e293b" rx="4"/>
      <circle cx="180" cy="75" r="7" fill="#ef4444"/>

      <text x="15" y="130" fill="#cbd5e1" font-size="11">Anode Voltage V_acc (10kV - 150kV):</text>
      <rect x="15" y="140" width="250" height="10" fill="#1e293b" rx="4"/>
      <circle cx="190" cy="145" r="7" fill="#38bdf8"/>

      <rect x="15" y="190" width="250" height="40" fill="#22c55e15" rx="6" stroke="#22c55e"/>
      <text x="140" y="215" fill="#22c55e" font-size="12" font-weight="800" text-anchor="middle">λ_min = 0.0155 nm (Hard X-Ray)</text>

      <rect x="15" y="250" width="250" height="40" fill="#f59e0b15" rx="6" stroke="#f59e0b"/>
      <text x="140" y="275" fill="#f59e0b" font-size="12" font-weight="800" text-anchor="middle">f_max = 1.93 × 10¹⁹ Hz</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Interactive X-Ray Tube Sandbox: Real-Time Spectrum and Cutoff Wavelength Model")


# =============================================================================
# ENHANCED SVG BUILDERS — MODULE 8.2
# =============================================================================

def svg_m82_continuous_spectrum():
    """Page 1: Bremsstrahlung continuous spectrum graph"""
    inner = """
    <rect x="100" y="60" width="660" height="260" fill="#030712" rx="10" stroke="#38bdf8" stroke-width="2"/>
    <line x1="100" y1="280" x2="760" y2="280" stroke="#94a3b8" stroke-width="2"/>
    <line x1="100" y1="60" x2="100" y2="280" stroke="#94a3b8" stroke-width="2"/>

    <line x1="200" y1="60" x2="200" y2="280" stroke="#ef4444" stroke-width="3" stroke-dasharray="6 3"/>
    <rect x="135" y="295" width="130" height="24" fill="#ef444420" rx="4" stroke="#ef4444"/>
    <text x="200" y="311" fill="#ef4444" font-size="12" font-weight="800" text-anchor="middle">λ_min (Cutoff)</text>

    <path d="M 200,280 Q 280,80 400,160 T 720,270" fill="none" stroke="#38bdf8" stroke-width="5"/>

    <rect x="300" y="90" width="220" height="50" fill="#0284c720" rx="6" stroke="#0284c7"/>
    <text x="410" y="112" fill="#38bdf8" font-size="14" font-weight="800" text-anchor="middle">Bremsstrahlung Curve</text>
    <text x="410" y="130" fill="#cbd5e1" font-size="11" text-anchor="middle">Continuous nuclear braking radiation spread</text>

    <text x="430" y="360" fill="#f8fafc" font-size="14" font-weight="800" text-anchor="middle">Wavelength λ (nm) →</text>
    <text x="45" y="170" fill="#f8fafc" font-size="14" font-weight="800" text-anchor="middle" transform="rotate(-90 45 170)">X-Ray Intensity I →</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Bremsstrahlung Continuous X-Ray Intensity vs. Wavelength Graph Showing Cutoff Wavelength")

def svg_m82_characteristic_peaks():
    """Page 2: Characteristic peaks and atomic shell transitions"""
    inner = """
    <!-- Left Panel: Spectrum Graph with Sharp Peaks (x = 40, w = 360) -->
    <g transform="translate(40, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#030712" rx="10" stroke="#22c55e" stroke-width="2"/>

      <path d="M 60,260 Q 120,180 180,220 T 320,250" fill="none" stroke="#38bdf8" stroke-width="3"/>

      <line x1="140" y1="220" x2="140" y2="50" stroke="#22c55e" stroke-width="4"/>
      <text x="140" y="40" fill="#22c55e" font-size="13" font-weight="800" text-anchor="middle">K_β Peak</text>

      <line x1="170" y1="210" x2="170" y2="80" stroke="#22c55e" stroke-width="4"/>
      <text x="170" y="70" fill="#22c55e" font-size="13" font-weight="800" text-anchor="middle">K_α Peak</text>

      <text x="180" y="295" fill="#22c55e" font-size="12" font-weight="800" text-anchor="middle">Characteristic Discrete Peaks</text>
    </g>

    <!-- Right Panel: Atomic Energy Levels (x = 440, w = 360) -->
    <g transform="translate(440, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="10" stroke="#f59e0b" stroke-width="2"/>
      <text x="180" y="32" fill="#f59e0b" font-size="14" font-weight="800" text-anchor="middle">ATOMIC SHELL TRANSITIONS</text>

      <line x1="60" y1="80" x2="300" y2="80" stroke="#a855f7" stroke-width="4"/>
      <text x="325" y="85" fill="#a855f7" font-size="13" font-weight="800">M-Shell</text>

      <line x1="60" y1="150" x2="300" y2="150" stroke="#38bdf8" stroke-width="4"/>
      <text x="325" y="155" fill="#38bdf8" font-size="13" font-weight="800">L-Shell</text>

      <line x1="60" y1="250" x2="300" y2="250" stroke="#ef4444" stroke-width="4"/>
      <text x="325" y="255" fill="#ef4444" font-size="13" font-weight="800">K-Shell</text>

      <line x1="180" y1="150" x2="180" y2="250" stroke="#22c55e" stroke-width="5"/>
      <polygon points="180,250 172,235 188,235" fill="#22c55e"/>

      <rect x="40" y="275" width="280" height="32" fill="#22c55e15" rx="6" stroke="#22c55e"/>
      <text x="180" y="296" fill="#22c55e" font-size="13" font-weight="800" text-anchor="middle">Photon h f = E_L - E_K</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Inner Shell K-Shell and L-Shell Electronic Transition Energy Level Diagram")

def svg_m82_attenuation_exponential():
    """Page 4: Exponential attenuation curves through lead vs bone vs tissue"""
    inner = """
    <rect x="100" y="60" width="660" height="260" fill="#030712" rx="10" stroke="#38bdf8" stroke-width="2"/>
    <line x1="100" y1="280" x2="760" y2="280" stroke="#94a3b8" stroke-width="2"/>
    <line x1="100" y1="60" x2="100" y2="280" stroke="#94a3b8" stroke-width="2"/>

    <path d="M 100,80 Q 300,120 720,200" fill="none" stroke="#22c55e" stroke-width="4"/>
    <text x="600" y="180" fill="#22c55e" font-size="13" font-weight="800">Soft Tissue (Low μ)</text>

    <path d="M 100,80 Q 250,180 720,250" fill="none" stroke="#f59e0b" stroke-width="4"/>
    <text x="500" y="230" fill="#f59e0b" font-size="13" font-weight="800">Dense Bone (Medium μ)</text>

    <path d="M 100,80 Q 150,260 720,278" fill="none" stroke="#ef4444" stroke-width="5"/>
    <text x="220" y="240" fill="#ef4444" font-size="13" font-weight="800">Lead Shielding (High μ)</text>

    <text x="430" y="360" fill="#f8fafc" font-size="14" font-weight="800" text-anchor="middle">Material Thickness x (cm) →</text>
    <text x="45" y="170" fill="#f8fafc" font-size="14" font-weight="800" text-anchor="middle" transform="rotate(-90 45 170)">Transmitted Intensity I →</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Exponential X-Ray Attenuation Curves (I = I_0 e^-μx) for Lead, Bone, and Soft Tissue")

def svg_m82_bragg_crystallography():
    """Page 8: Bragg's law crystallography diffraction geometry"""
    inner = """
    <line x1="100" y1="140" x2="740" y2="140" stroke="#94a3b8" stroke-dasharray="4 4" stroke-width="2"/>
    <circle cx="160" cy="140" r="12" fill="#38bdf8"/>
    <circle cx="320" cy="140" r="12" fill="#38bdf8"/>
    <circle cx="480" cy="140" r="12" fill="#38bdf8"/>
    <circle cx="640" cy="140" r="12" fill="#38bdf8"/>

    <line x1="100" y1="260" x2="740" y2="260" stroke="#94a3b8" stroke-dasharray="4 4" stroke-width="2"/>
    <circle cx="160" cy="260" r="12" fill="#38bdf8"/>
    <circle cx="320" cy="260" r="12" fill="#38bdf8"/>
    <circle cx="480" cy="260" r="12" fill="#38bdf8"/>
    <circle cx="640" cy="260" r="12" fill="#38bdf8"/>

    <line x1="120" y1="140" x2="120" y2="260" stroke="#f59e0b" stroke-width="4"/>
    <text x="95" y="205" fill="#f59e0b" font-size="16" font-weight="800">d</text>

    <line x1="140" y1="40" x2="320" y2="140" stroke="#22c55e" stroke-width="4"/>
    <line x1="320" y1="140" x2="500" y2="40" stroke="#22c55e" stroke-width="4"/>

    <line x1="100" y1="40" x2="320" y2="260" stroke="#22c55e" stroke-width="4"/>
    <line x1="320" y1="260" x2="540" y2="40" stroke="#22c55e" stroke-width="4"/>

    <rect x="220" y="330" width="400" height="55" fill="#111827" rx="8" stroke="#22c55e" stroke-width="2"/>
    <text x="420" y="365" fill="#22c55e" font-size="18" font-weight="800" text-anchor="middle">Bragg's Law: 2 d sin θ = n λ</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Bragg's Law X-Ray Crystal Lattice Diffraction Geometry (2d sin θ = n λ)")


# =============================================================================
# ENHANCED SVG BUILDERS — MODULE 8.3
# =============================================================================

def svg_m83_duane_hunt_graph():
    """Page 1: Duane-Hunt inverse graph between V and lambda_min"""
    inner = """
    <rect x="100" y="60" width="660" height="260" fill="#030712" rx="10" stroke="#38bdf8" stroke-width="2"/>
    <line x1="100" y1="280" x2="760" y2="280" stroke="#94a3b8" stroke-width="2"/>
    <line x1="100" y1="60" x2="100" y2="280" stroke="#94a3b8" stroke-width="2"/>

    <path d="M 140,80 Q 240,240 720,265" fill="none" stroke="#22c55e" stroke-width="5"/>

    <rect x="300" y="110" width="300" height="50" fill="#22c55e15" rx="8" stroke="#22c55e"/>
    <text x="450" y="132" fill="#22c55e" font-size="16" font-weight="800" text-anchor="middle">λ_min = hc / (e V_acc)</text>
    <text x="450" y="152" fill="#cbd5e1" font-size="12" text-anchor="middle">Inverse proportional relationship curve</text>

    <text x="430" y="360" fill="#f8fafc" font-size="14" font-weight="800" text-anchor="middle">Accelerating Voltage V_acc (kV) →</text>
    <text x="45" y="170" fill="#f8fafc" font-size="14" font-weight="800" text-anchor="middle" transform="rotate(-90 45 170)">Cutoff Wavelength λ_min →</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Duane-Hunt Law: Inverse Relationship Between Accelerating Voltage and Cutoff Wavelength")

def svg_m83_anode_cooling_circuit():
    """Page 6: Thermal heat exchanger calculation diagram"""
    inner = """
    <g transform="translate(60, 60)">
      <rect x="0" y="0" width="340" height="320" fill="#111827" rx="12" stroke="#ef4444" stroke-width="2"/>
      <text x="170" y="32" fill="#ef4444" font-size="14" font-weight="800" text-anchor="middle">1. INPUT ELECTRICAL POWER</text>

      <rect x="20" y="80" width="300" height="80" fill="#1e293b" rx="8" stroke="#ef4444"/>
      <text x="170" y="125" fill="#f8fafc" font-size="20" font-weight="800" text-anchor="middle">P_in = I × V_acc</text>

      <text x="170" y="200" fill="#cbd5e1" font-size="13" text-anchor="middle">Example: 20 mA × 60 kV</text>
      <text x="170" y="228" fill="#ef4444" font-size="18" font-weight="800" text-anchor="middle">= 1,200 Watts</text>
    </g>

    <text x="420" y="220" fill="#f59e0b" font-size="42" font-weight="800" text-anchor="middle">→</text>

    <g transform="translate(460, 60)">
      <rect x="0" y="0" width="340" height="320" fill="#111827" rx="12" stroke="#22c55e" stroke-width="2"/>
      <text x="170" y="32" fill="#22c55e" font-size="14" font-weight="800" text-anchor="middle">2. THERMAL HEAT GENERATION</text>

      <rect x="20" y="80" width="300" height="80" fill="#1e293b" rx="8" stroke="#22c55e"/>
      <text x="170" y="125" fill="#f8fafc" font-size="20" font-weight="800" text-anchor="middle">P_heat = 0.99 × P_in</text>

      <text x="170" y="200" fill="#cbd5e1" font-size="13" text-anchor="middle">Heat Rate = 0.99 × 1,200 W</text>
      <text x="170" y="228" fill="#22c55e" font-size="18" font-weight="800" text-anchor="middle">= 1,188 Watts (J/s)</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Anode Target Thermal Heat Generation Rate Calculation Diagram")

def svg_m83_radiation_safety_shielding():
    """Page 10: Medical radiation safety lead apron and film badge dosimeter"""
    inner = """
    <!-- Left Panel: Lead Apron & Lead-Glass Shield (x = 40, w = 360) -->
    <g transform="translate(40, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="12" stroke="#38bdf8" stroke-width="2"/>
      <text x="180" y="32" fill="#38bdf8" font-size="14" font-weight="800" text-anchor="middle">PROTECTIVE SHIELDING</text>

      <path d="M 120,80 L 240,80 L 260,140 L 220,140 L 220,260 L 140,260 L 140,140 L 100,140 Z" fill="#475569" stroke="#cbd5e1" stroke-width="3"/>
      <text x="180" y="180" fill="#fff" font-size="14" font-weight="800" text-anchor="middle">Lead Apron</text>
      <text x="180" y="202" fill="#cbd5e1" font-size="12" text-anchor="middle">(0.5mm Lead Equivalent)</text>

      <rect x="20" y="270" width="320" height="35" fill="#0284c715" rx="6" stroke="#0284c7"/>
      <text x="180" y="292" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">Lead absorbs X-rays via photoelectric effect</text>
    </g>

    <!-- Right Panel: Film Badge Dosimeter (x = 440, w = 360) -->
    <g transform="translate(440, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="12" stroke="#f59e0b" stroke-width="2"/>
      <text x="180" y="32" fill="#f59e0b" font-size="14" font-weight="800" text-anchor="middle">FILM BADGE DOSIMETER</text>

      <rect x="100" y="70" width="160" height="180" fill="#1e293b" rx="10" stroke="#f59e0b" stroke-width="3"/>
      <rect x="130" y="100" width="100" height="60" fill="#030712" rx="4"/>
      <text x="180" y="135" fill="#22c55e" font-size="13" font-weight="800" text-anchor="middle">Film Packet</text>

      <rect x="130" y="180" width="40" height="40" fill="#94a3b8" rx="2"/>
      <text x="150" y="205" fill="#000" font-size="11" font-weight="800" text-anchor="middle">Lead</text>

      <rect x="190" y="180" width="40" height="40" fill="#f59e0b" rx="2"/>
      <text x="210" y="205" fill="#000" font-size="11" font-weight="800" text-anchor="middle">Cu</text>

      <rect x="20" y="270" width="320" height="35" fill="#f59e0b15" rx="6" stroke="#f59e0b"/>
      <text x="180" y="292" fill="#f59e0b" font-size="12" font-weight="800" text-anchor="middle">Monitors cumulative monthly radiation dose</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Medical Radiation Safety Protection: Lead Apron and Film Badge Dosimeter Internal Construction")


# =============================================================================
# MAIN ENRICHMENT EXECUTOR FOR TOPIC 8
# =============================================================================

def run_enrichment_topic8():
    print("=" * 80)
    print("VLEARN FORM 4 PHYSICS — TOPIC 8 VISUAL ENRICHMENT")
    print("=" * 80)

    topic = Topic.objects.filter(
        subject__name="Physics",
        subject__grade__name="Form 4",
        name__icontains="X-Rays"
    ).first()

    if not topic:
        print("ERROR: Topic 8: X-Rays not found! Run ingest_form4_physics_topic8.py first.")
        return

    units = topic.learning_units.all().order_by("order")
    unit_1 = units[0]
    unit_2 = units[1]
    unit_3 = units[2]

    lesson_1 = unit_1.lessons.first()
    lesson_2 = unit_2.lessons.first()
    lesson_3 = unit_3.lessons.first()

    print(f"Enriching Lesson 1 (ID: {lesson_1.id}): '{lesson_1.title}'")
    print(f"Enriching Lesson 2 (ID: {lesson_2.id}): '{lesson_2.title}'")
    print(f"Enriching Lesson 3 (ID: {lesson_3.id}): '{lesson_3.title}'\n")

    # Module 8.1 SVGs
    print("--- Enriching Module 8.1 ---")
    attach_svg_to_block(lesson_1, 2, "suggested_diagram", "Modern Coolidge X-Ray Tube Construction: Cathode, Tungsten Target, and Cooling Fins", "m81_coolidge_tube_schematic", svg_m81_coolidge_tube_schematic())
    attach_svg_to_block(lesson_1, 3, "suggested_diagram", "Target Anode Material Selection and Circulating Oil Thermal Heat Dissipation System", "m81_anode_cooling_mechanism", svg_m81_anode_cooling_mechanism())
    attach_svg_to_block(lesson_1, 4, "suggested_diagram", "X-Ray Tube Energy Partition: Over 99% Thermal Heat Loss vs. Under 1% X-Ray Photons", "m81_energy_conversion_pie", svg_m81_energy_conversion_pie())
    attach_svg_to_block(lesson_1, 7, "suggested_diagram", "Independent X-Ray Control Mechanisms: Accelerating Voltage (Hardness) vs. Filament Current (Intensity)", "m81_intensity_vs_hardness", svg_m81_intensity_vs_hardness())
    attach_svg_to_block(lesson_1, 8, "suggested_simulation", "Interactive X-Ray Tube Sandbox: Real-Time Spectrum and Cutoff Wavelength Model", "m81_xray_sandbox", svg_m81_xray_sandbox())

    # Module 8.2 SVGs
    print("\n--- Enriching Module 8.2 ---")
    attach_svg_to_block(lesson_2, 1, "suggested_diagram", "Bremsstrahlung Continuous X-Ray Intensity vs. Wavelength Graph Showing Cutoff Wavelength", "m82_continuous_spectrum", svg_m82_continuous_spectrum())
    attach_svg_to_block(lesson_2, 2, "suggested_diagram", "Inner Shell K-Shell and L-Shell Electronic Transition Energy Level Diagram", "m82_characteristic_peaks", svg_m82_characteristic_peaks())
    attach_svg_to_block(lesson_2, 4, "suggested_diagram", "Exponential X-Ray Attenuation Curves (I = I_0 e^-μx) for Lead, Bone, and Soft Tissue", "m82_attenuation_exponential", svg_m82_attenuation_exponential())
    attach_svg_to_block(lesson_2, 8, "suggested_diagram", "Bragg's Law X-Ray Crystal Lattice Diffraction Geometry (2d sin θ = n λ)", "m82_bragg_crystallography", svg_m82_bragg_crystallography())

    # Module 8.3 SVGs
    print("\n--- Enriching Module 8.3 ---")
    attach_svg_to_block(lesson_3, 1, "suggested_diagram", "Duane-Hunt Law: Inverse Relationship Between Accelerating Voltage and Cutoff Wavelength", "m83_duane_hunt_graph", svg_m83_duane_hunt_graph())
    attach_svg_to_block(lesson_3, 6, "suggested_diagram", "Anode Target Thermal Heat Generation Rate Calculation Diagram", "m83_anode_cooling_circuit", svg_m83_anode_cooling_circuit())
    attach_svg_to_block(lesson_3, 10, "suggested_diagram", "Medical Radiation Safety Protection: Lead Apron and Film Badge Dosimeter Internal Construction", "m83_radiation_safety_shielding", svg_m83_radiation_safety_shielding())

    # Wikimedia Assets
    attach_wikimedia_to_block(
        lesson=lesson_1,
        page_num=1,
        title="Historical Röntgen X-Ray Shadowgraph of Bertha Röntgen's Hand (1895)",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/First_medical_X-ray_by_Wilhelm_R%C3%B6ntgen_of_his_wife_Anna_Bertha_Ludwig%27s_hand_-_18951222.jpg/960px-First_medical_X-ray_by_Wilhelm_R%C3%B6ntgen_of_his_wife_Anna_Bertha_Ludwig%27s_hand_-_18951222.jpg",
        author="Wilhelm Röntgen",
        licensing="Public domain",
        commons_page="https://commons.wikimedia.org/wiki/File:First_medical_X-ray_by_Wilhelm_R%C3%B6ntgen_of_his_wife_Anna_Bertha_Ludwig%27s_hand_-_18951222.jpg"
    )

    attach_wikimedia_to_block(
        lesson=lesson_1,
        page_num=2,
        title="Coolidge X-Ray Tube Glass Hardware Construction Unit",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/X-ray_tube_a_later_version_of_the_Coolidge_X-ray_tube._Wellcome_M0015850.jpg/960px-X-ray_tube_a_later_version_of_the_Coolidge_X-ray_tube._Wellcome_M0015850.jpg",
        author="Wellcome Collection",
        licensing="CC BY 4.0",
        commons_page="https://commons.wikimedia.org/wiki/File:X-ray_tube_a_later_version_of_the_Coolidge_X-ray_tube._Wellcome_M0015850.jpg"
    )

    attach_wikimedia_to_block(
        lesson=lesson_2,
        page_num=5,
        title="Medical Chest Radiography X-Ray Film Image",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Normal_posteroanterior_%28PA%29_chest_radiograph_%28X-ray%29.jpg/960px-Normal_posteroanterior_%28PA%29_chest_radiograph_%28X-ray%29.jpg",
        author="Wikimedia Commons Contributor",
        licensing="CC0",
        commons_page="https://commons.wikimedia.org/wiki/File:Normal_posteroanterior_%28PA%29_chest_radiograph_%28X-ray%29.jpg"
    )

    print("\n" + "=" * 80)
    print("TOPIC 8 VISUAL ENRICHMENT COMPLETED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    run_enrichment_topic8()
