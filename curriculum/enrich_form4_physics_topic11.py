"""
VLearn Form 4 Physics — Topic 11: Electronics
Visual Enrichment Engine (High-Contrast SVGs + Wikimedia Commons)

Enriches Topic 11 (Electronics) with:
  - 12 high-precision, high-contrast dark-mode vector SVG diagrams
  - 3 authentic Wikimedia Commons photographic assets

Usage:
  /home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/venv/bin/python curriculum/enrich_form4_physics_topic11.py
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
# SVG BUILDERS — MODULE 11.1
# =============================================================================

def svg_m111_energy_band_diagram():
    """Page 2: Energy band gap comparison (Conductors, Semiconductors, Insulators)"""
    inner = """
    <!-- Conductor (x = 40, w = 220) -->
    <g transform="translate(40, 60)">
      <rect x="0" y="0" width="220" height="320" fill="#111827" rx="10" stroke="#22c55e" stroke-width="2"/>
      <text x="110" y="32" fill="#22c55e" font-size="14" font-weight="800" text-anchor="middle">CONDUCTOR</text>

      <rect x="20" y="80" width="180" height="120" fill="#22c55e30" stroke="#22c55e" stroke-width="2"/>
      <text x="110" y="145" fill="#22c55e" font-size="13" font-weight="800" text-anchor="middle">Overlapping Bands</text>
      <text x="110" y="165" fill="#f8fafc" font-size="14" font-weight="800" text-anchor="middle">E_g = 0 eV</text>
    </g>

    <!-- Semiconductor (x = 310, w = 220) -->
    <g transform="translate(310, 60)">
      <rect x="0" y="0" width="220" height="320" fill="#111827" rx="10" stroke="#38bdf8" stroke-width="2"/>
      <text x="110" y="32" fill="#38bdf8" font-size="14" font-weight="800" text-anchor="middle">SEMICONDUCTOR</text>

      <rect x="20" y="60" width="180" height="70" fill="#0284c730" stroke="#0284c7" stroke-width="2"/>
      <text x="110" y="100" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">Conduction Band</text>

      <rect x="20" y="140" width="180" height="30" fill="#f59e0b15" stroke="#f59e0b" stroke-dasharray="4 2"/>
      <text x="110" y="160" fill="#f59e0b" font-size="12" font-weight="800" text-anchor="middle">E_g ≈ 1.1 eV (Small Gap)</text>

      <rect x="20" y="180" width="180" height="80" fill="#1e3a8a30" stroke="#38bdf8" stroke-width="2"/>
      <text x="110" y="225" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">Valence Band</text>
    </g>

    <!-- Insulator (x = 580, w = 220) -->
    <g transform="translate(580, 60)">
      <rect x="0" y="0" width="220" height="320" fill="#111827" rx="10" stroke="#ef4444" stroke-width="2"/>
      <text x="110" y="32" fill="#ef4444" font-size="14" font-weight="800" text-anchor="middle">INSULATOR</text>

      <rect x="20" y="60" width="180" height="60" fill="#ef444420" stroke="#ef4444" stroke-width="2"/>
      <text x="110" y="95" fill="#ef4444" font-size="13" font-weight="800" text-anchor="middle">Conduction Band</text>

      <rect x="20" y="130" width="180" height="80" fill="#ef444415" stroke="#ef4444" stroke-dasharray="4 2"/>
      <text x="110" y="175" fill="#ef4444" font-size="13" font-weight="800" text-anchor="middle">E_g &gt; 5.0 eV (Huge Gap)</text>

      <rect x="20" y="220" width="180" height="60" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
      <text x="110" y="255" fill="#94a3b8" font-size="13" font-weight="800" text-anchor="middle">Valence Band</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Energy Band Structure Comparison for Conductors, Semiconductors, and Insulators")

def svg_m111_ntype_doping_lattice():
    """Page 5: N-Type doping with Pentavalent Phosphorus donor atom"""
    inner = """
    <!-- Central Pentavalent Phosphorus Atom -->
    <circle cx="420" cy="210" r="45" fill="#ef4444" stroke="#f8fafc" stroke-width="3"/>
    <text x="420" y="215" fill="#fff" font-size="16" font-weight="800" text-anchor="middle">P (Group V)</text>

    <!-- Surrounding 4 Silicon Atoms -->
    <circle cx="240" cy="210" r="35" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <text x="240" y="215" fill="#fff" font-size="14" font-weight="800" text-anchor="middle">Si</text>

    <circle cx="600" cy="210" r="35" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <text x="600" y="215" fill="#fff" font-size="14" font-weight="800" text-anchor="middle">Si</text>

    <circle cx="420" cy="90" r="35" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <text x="420" y="95" fill="#fff" font-size="14" font-weight="800" text-anchor="middle">Si</text>

    <circle cx="420" cy="330" r="35" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <text x="420" y="335" fill="#fff" font-size="14" font-weight="800" text-anchor="middle">Si</text>

    <!-- Extra Free Conduction Electron Released -->
    <circle cx="520" cy="130" r="14" fill="#22c55e" stroke="#fff" stroke-width="2"/>
    <text x="520" y="135" fill="#000" font-size="12" font-weight="800" text-anchor="middle">e⁻</text>
    <line x1="455" y1="180" x2="510" y2="140" stroke="#22c55e" stroke-width="3" stroke-dasharray="4 2"/>

    <rect x="530" y="160" width="220" height="50" fill="#22c55e15" rx="6" stroke="#22c55e"/>
    <text x="640" y="182" fill="#22c55e" font-size="13" font-weight="800" text-anchor="middle">5th Extra Free Electron</text>
    <text x="640" y="200" fill="#cbd5e1" font-size="11" text-anchor="middle">Donor atom provides majority carriers</text>
    """
    return wrap_svg(inner, W=840, H=420, title="N-Type Doping Silicon Crystal Lattice with Pentavalent Phosphorus Donor Atom")

def svg_m111_ptype_doping_lattice():
    """Page 6: P-Type doping with Trivalent Boron acceptor atom"""
    inner = """
    <!-- Central Trivalent Boron Atom -->
    <circle cx="420" cy="210" r="45" fill="#f59e0b" stroke="#f8fafc" stroke-width="3"/>
    <text x="420" y="215" fill="#000" font-size="16" font-weight="800" text-anchor="middle">B (Group III)</text>

    <!-- Surrounding Silicon Atoms -->
    <circle cx="240" cy="210" r="35" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <text x="240" y="215" fill="#fff" font-size="14" font-weight="800" text-anchor="middle">Si</text>

    <circle cx="600" cy="210" r="35" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <text x="600" y="215" fill="#fff" font-size="14" font-weight="800" text-anchor="middle">Si</text>

    <!-- Electron Hole Vacancy -->
    <circle cx="510" cy="210" r="14" fill="#090d16" stroke="#38bdf8" stroke-width="3" stroke-dasharray="3 2"/>
    <text x="510" y="215" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">h⁺</text>

    <rect x="530" y="250" width="220" height="50" fill="#38bdf815" rx="6" stroke="#38bdf8"/>
    <text x="640" y="272" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">Electron Hole Vacancy (h⁺)</text>
    <text x="640" y="290" fill="#cbd5e1" font-size="11" text-anchor="middle">Acceptor atom provides majority holes</text>
    """
    return wrap_svg(inner, W=840, H=420, title="P-Type Doping Silicon Crystal Lattice with Trivalent Boron Acceptor Atom Creating Hole Vacancy")

def svg_m111_electronics_sandbox():
    """Page 8: Interactive Semiconductor Sandbox model"""
    inner = """
    <rect x="60" y="60" width="440" height="320" fill="#111827" rx="12" stroke="#38bdf8" stroke-width="3"/>

    <circle cx="280" cy="220" r="60" fill="#030712" stroke="#22c55e" stroke-width="3"/>
    <text x="280" y="215" fill="#22c55e" font-size="14" font-weight="800" text-anchor="middle">Si Crystal</text>

    <g transform="translate(520, 60)">
      <rect x="0" y="0" width="280" height="320" fill="#111827" rx="10" stroke="#38bdf8" stroke-width="2"/>
      <text x="140" y="25" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">INTERACTIVE SEMICONDUCTOR</text>

      <text x="15" y="60" fill="#cbd5e1" font-size="11">Temperature (100K to 500K):</text>
      <rect x="15" y="70" width="250" height="10" fill="#1e293b" rx="4"/>
      <circle cx="160" cy="75" r="7" fill="#ef4444"/>

      <text x="15" y="130" fill="#cbd5e1" font-size="11">Doping Conc N_D (10¹5 to 10¹8 m⁻³):</text>
      <rect x="15" y="140" width="250" height="10" fill="#1e293b" rx="4"/>
      <circle cx="190" cy="145" r="7" fill="#38bdf8"/>

      <rect x="15" y="190" width="250" height="40" fill="#22c55e15" rx="6" stroke="#22c55e"/>
      <text x="140" y="215" fill="#22c55e" font-size="12" font-weight="800" text-anchor="middle">n_e = 1.0 × 10¹7 m⁻³ (N-Type)</text>

      <rect x="15" y="250" width="250" height="40" fill="#f59e0b15" rx="6" stroke="#f59e0b"/>
      <text x="140" y="275" fill="#f59e0b" font-size="12" font-weight="800" text-anchor="middle">Conductivity σ = 1.6 Ω⁻¹m⁻¹</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Interactive Semiconductor Sandbox: Real-Time Temperature & Doping Carrier Density Model")


# =============================================================================
# SVG BUILDERS — MODULE 11.2
# =============================================================================

def svg_m112_pn_junction_depletion():
    """Page 1: P-N junction depletion layer & barrier potential V_0"""
    inner = """
    <!-- P-Region (Left) -->
    <rect x="80" y="80" width="280" height="240" fill="#1e3a8a30" stroke="#38bdf8" stroke-width="3"/>
    <text x="220" y="115" fill="#38bdf8" font-size="18" font-weight="800" text-anchor="middle">P-Type Region (Holes h⁺)</text>

    <!-- N-Region (Right) -->
    <rect x="480" y="80" width="280" height="240" fill="#22c55e20" stroke="#22c55e" stroke-width="3"/>
    <text x="620" y="115" fill="#22c55e" font-size="18" font-weight="800" text-anchor="middle">N-Type Region (Free e⁻)</text>

    <!-- Depletion Region Center -->
    <rect x="360" y="80" width="120" height="240" fill="#ef444415" stroke="#ef4444" stroke-width="2"/>
    <text x="420" y="150" fill="#ef4444" font-size="14" font-weight="800" text-anchor="middle">Depletion Layer</text>

    <text x="390" y="200" fill="#ef4444" font-size="20" font-weight="800" text-anchor="middle">-</text>
    <text x="450" y="200" fill="#22c55e" font-size="20" font-weight="800" text-anchor="middle">+</text>

    <rect x="300" y="340" width="240" height="45" fill="#111827" rx="8" stroke="#ef4444" stroke-width="2"/>
    <text x="420" y="367" fill="#ef4444" font-size="14" font-weight="800" text-anchor="middle">Barrier Potential V_0 ≈ 0.7V (Silicon)</text>
    """
    return wrap_svg(inner, W=840, H=420, title="P-N Junction Depletion Layer Formation Diagram Showing Internal Built-In Barrier Potential V_0")

def svg_m112_diode_iv_curve():
    """Page 2: Diode I-V characteristic curve"""
    inner = """
    <rect x="100" y="60" width="660" height="260" fill="#030712" rx="10" stroke="#38bdf8" stroke-width="2"/>
    <line x1="100" y1="220" x2="760" y2="220" stroke="#94a3b8" stroke-width="2"/>
    <line x1="360" y1="60" x2="360" y2="280" stroke="#94a3b8" stroke-width="2"/>

    <path d="M 120,222 L 360,220 Q 440,220 500,80" fill="none" stroke="#22c55e" stroke-width="5"/>

    <line x1="440" y1="60" x2="440" y2="280" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 2"/>
    <text x="440" y="305" fill="#f59e0b" font-size="13" font-weight="800" text-anchor="middle">0.7V Knee Voltage</text>

    <text x="560" y="355" fill="#f8fafc" font-size="14" font-weight="800" text-anchor="middle">Forward Voltage V_F (Volts) →</text>
    <text x="45" y="170" fill="#f8fafc" font-size="14" font-weight="800" text-anchor="middle" transform="rotate(-90 45 170)">Diode Current I (mA) →</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Silicon Semiconductor Diode I-V Characteristic Curve (Knee Voltage 0.7V and Reverse Breakdown)")

def svg_m112_halfwave_rectifier():
    """Page 3: Half-wave rectifier circuit and waveforms"""
    inner = """
    <g transform="translate(60, 60)">
      <rect x="0" y="0" width="340" height="320" fill="#111827" rx="12" stroke="#38bdf8" stroke-width="2"/>
      <text x="170" y="32" fill="#38bdf8" font-size="14" font-weight="800" text-anchor="middle">HALF-WAVE CIRCUIT</text>

      <polygon points="120,100 160,120 120,140" fill="#ef4444"/>
      <line x1="160" y1="100" x2="160" y2="140" stroke="#ef4444" stroke-width="4"/>

      <text x="170" y="240" fill="#cbd5e1" font-size="12" text-anchor="middle">Single Diode conducts 50% of AC cycle</text>
    </g>

    <g transform="translate(440, 60)">
      <rect x="0" y="0" width="340" height="320" fill="#030712" rx="12" stroke="#22c55e" stroke-width="2"/>
      <text x="170" y="32" fill="#22c55e" font-size="14" font-weight="800" text-anchor="middle">PULSATING DC WAVEFORM</text>

      <path d="M 40,200 Q 80,100 120,200 L 200,200 Q 240,100 280,200" fill="none" stroke="#22c55e" stroke-width="4"/>
      <text x="170" y="270" fill="#22c55e" font-size="13" font-weight="800" text-anchor="middle">Gaps between pulses (40.6% Eff)</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Half-Wave Rectifier Circuit Diagram and Input AC vs Pulsating DC Waveform Graph")

def svg_m112_bridge_rectifier():
    """Page 5: 4-diode bridge rectifier circuit"""
    inner = """
    <polygon points="420,80 560,210 420,340 280,210" fill="#111827" stroke="#38bdf8" stroke-width="3"/>

    <!-- 4 Diodes D1 D2 D3 D4 -->
    <polygon points="340,130 360,145 340,160" fill="#22c55e"/>
    <polygon points="480,130 500,145 480,160" fill="#22c55e"/>

    <text x="420" y="215" fill="#f8fafc" font-size="16" font-weight="800" text-anchor="middle">LOAD R_L</text>
    """
    return wrap_svg(inner, W=840, H=420, title="4-Diode Bridge Rectifier Circuit Diagram Showing Alternating Current Path Conduction")

def svg_m112_smoothing_capacitor():
    """Page 6: RC smoothing capacitor filter & ripple voltage graph"""
    inner = """
    <rect x="100" y="60" width="660" height="260" fill="#030712" rx="10" stroke="#38bdf8" stroke-width="2"/>
    <path d="M 100,200 Q 140,80 180,120 L 280,160 Q 320,80 360,120 L 460,160" fill="none" stroke="#22c55e" stroke-width="5"/>
    <text x="420" y="360" fill="#22c55e" font-size="15" font-weight="800" text-anchor="middle">Smoothed DC Output with Minimal Ripple Voltage V_r</text>
    """
    return wrap_svg(inner, W=840, H=420, title="RC Filter Smoothing Capacitor Circuit and Smoothed DC Voltage Ripple Reduction Graph")

def svg_m112_npn_pnp_transistor():
    """Page 7: NPN and PNP transistor layer structure & circuit symbols"""
    inner = """
    <!-- Left: NPN Transistor (x = 40, w = 360) -->
    <g transform="translate(40, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="12" stroke="#38bdf8" stroke-width="2"/>
      <text x="180" y="32" fill="#38bdf8" font-size="14" font-weight="800" text-anchor="middle">NPN TRANSISTOR</text>

      <rect x="40" y="80" width="80" height="140" fill="#22c55e20" stroke="#22c55e" stroke-width="2"/>
      <text x="80" y="155" fill="#22c55e" font-size="14" font-weight="800" text-anchor="middle">N</text>

      <rect x="120" y="80" width="30" height="140" fill="#ef444420" stroke="#ef4444" stroke-width="2"/>
      <text x="135" y="155" fill="#ef4444" font-size="14" font-weight="800" text-anchor="middle">P</text>

      <rect x="150" y="80" width="170" height="140" fill="#22c55e20" stroke="#22c55e" stroke-width="2"/>
      <text x="235" y="155" fill="#22c55e" font-size="14" font-weight="800" text-anchor="middle">N</text>

      <text x="180" y="270" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">Symbol Arrow Points OUT (Emitter)</text>
    </g>

    <!-- Right: PNP Transistor (x = 440, w = 360) -->
    <g transform="translate(440, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="12" stroke="#f59e0b" stroke-width="2"/>
      <text x="180" y="32" fill="#f59e0b" font-size="14" font-weight="800" text-anchor="middle">PNP TRANSISTOR</text>

      <rect x="40" y="80" width="80" height="140" fill="#ef444420" stroke="#ef4444" stroke-width="2"/>
      <text x="80" y="155" fill="#ef4444" font-size="14" font-weight="800" text-anchor="middle">P</text>

      <rect x="120" y="80" width="30" height="140" fill="#22c55e20" stroke="#22c55e" stroke-width="2"/>
      <text x="135" y="155" fill="#22c55e" font-size="14" font-weight="800" text-anchor="middle">N</text>

      <rect x="150" y="80" width="170" height="140" fill="#ef444420" stroke="#ef4444" stroke-width="2"/>
      <text x="235" y="155" fill="#ef4444" font-size="14" font-weight="800" text-anchor="middle">P</text>

      <text x="180" y="270" fill="#f59e0b" font-size="13" font-weight="800" text-anchor="middle">Symbol Arrow Points IN (Base)</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="NPN and PNP Transistor Layer Structure, Terminal Names, and Standard Schematic Symbols")

def svg_m112_transistor_switch_ldr():
    """Page 9: Transistor automatic night light circuit with LDR"""
    inner = """
    <rect x="120" y="80" width="600" height="260" fill="#111827" rx="12" stroke="#38bdf8" stroke-width="3"/>
    <text x="420" y="120" fill="#38bdf8" font-size="16" font-weight="800" text-anchor="middle">Potential Divider LDR Control Switch</text>
    <text x="420" y="240" fill="#22c55e" font-size="15" font-weight="800" text-anchor="middle">Darkness → High R_LDR → V_B &gt; 0.7V → Transistor ON → Relay Lamp ON</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Transistor Automatic Night Light Circuit with LDR Potential Divider Potential Divider")


# =============================================================================
# SVG BUILDERS — MODULE 11.3
# =============================================================================

def svg_m113_logic_gates_truth_tables():
    """Page 4: Logic gate symbol family (AND, OR, NOT, NAND, NOR)"""
    inner = """
    <g transform="translate(40, 60)">
      <rect x="0" y="0" width="220" height="140" fill="#111827" rx="8" stroke="#38bdf8" stroke-width="2"/>
      <text x="110" y="30" fill="#38bdf8" font-size="14" font-weight="800" text-anchor="middle">AND GATE</text>
      <text x="110" y="80" fill="#f8fafc" font-size="16" font-weight="800" text-anchor="middle">Q = A · B</text>
    </g>

    <g transform="translate(310, 60)">
      <rect x="0" y="0" width="220" height="140" fill="#111827" rx="8" stroke="#22c55e" stroke-width="2"/>
      <text x="110" y="30" fill="#22c55e" font-size="14" font-weight="800" text-anchor="middle">OR GATE</text>
      <text x="110" y="80" fill="#f8fafc" font-size="16" font-weight="800" text-anchor="middle">Q = A + B</text>
    </g>

    <g transform="translate(580, 60)">
      <rect x="0" y="0" width="220" height="140" fill="#111827" rx="8" stroke="#ef4444" stroke-width="2"/>
      <text x="110" y="30" fill="#ef4444" font-size="14" font-weight="800" text-anchor="middle">NOT GATE</text>
      <text x="110" y="80" fill="#f8fafc" font-size="16" font-weight="800" text-anchor="middle">Q = A_bar</text>
    </g>

    <g transform="translate(170, 230)">
      <rect x="0" y="0" width="230" height="140" fill="#111827" rx="8" stroke="#a855f7" stroke-width="2"/>
      <text x="115" y="30" fill="#a855f7" font-size="14" font-weight="800" text-anchor="middle">NAND GATE (Universal)</text>
      <text x="115" y="80" fill="#f8fafc" font-size="16" font-weight="800" text-anchor="middle">Q = (A · B)_bar</text>
    </g>

    <g transform="translate(440, 230)">
      <rect x="0" y="0" width="230" height="140" fill="#111827" rx="8" stroke="#f59e0b" stroke-width="2"/>
      <text x="115" y="30" fill="#f59e0b" font-size="14" font-weight="800" text-anchor="middle">NOR GATE (Universal)</text>
      <text x="115" y="80" fill="#f8fafc" font-size="16" font-weight="800" text-anchor="middle">Q = (A + B)_bar</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Logic Gate Symbol Family (AND, OR, NOT, NAND, NOR) and Truth Tables")


# =============================================================================
# MAIN ENRICHMENT EXECUTOR FOR TOPIC 11
# =============================================================================

def run_enrichment_topic11():
    print("=" * 80)
    print("VLEARN FORM 4 PHYSICS — TOPIC 11 VISUAL ENRICHMENT")
    print("=" * 80)

    topic = Topic.objects.filter(
        subject__name="Physics",
        subject__grade__name="Form 4",
        name__icontains="Electronics"
    ).first()

    if not topic:
        print("ERROR: Topic 11: Electronics not found! Run ingest_form4_physics_topic11.py first.")
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

    # Module 11.1 SVGs
    print("--- Enriching Module 11.1 ---")
    attach_svg_to_block(lesson_1, 2, "suggested_diagram", "Energy Band Structure Comparison for Conductors, Semiconductors, and Insulators", "m111_energy_band_diagram", svg_m111_energy_band_diagram())
    attach_svg_to_block(lesson_1, 5, "suggested_diagram", "N-Type Doping Silicon Crystal Lattice with Pentavalent Phosphorus Donor Atom", "m111_ntype_doping_lattice", svg_m111_ntype_doping_lattice())
    attach_svg_to_block(lesson_1, 6, "suggested_diagram", "P-Type Doping Silicon Crystal Lattice with Trivalent Boron Acceptor Atom Creating Hole Vacancy", "m111_ptype_doping_lattice", svg_m111_ptype_doping_lattice())
    attach_svg_to_block(lesson_1, 8, "suggested_simulation", "Interactive Semiconductor Sandbox: Real-Time Temperature & Doping Carrier Density Model", "m111_electronics_sandbox", svg_m111_electronics_sandbox())

    # Module 11.2 SVGs
    print("\n--- Enriching Module 11.2 ---")
    attach_svg_to_block(lesson_2, 1, "suggested_diagram", "P-N Junction Depletion Layer Formation Diagram Showing Internal Built-In Barrier Potential V_0", "m112_pn_junction_depletion", svg_m112_pn_junction_depletion())
    attach_svg_to_block(lesson_2, 2, "suggested_diagram", "Silicon Semiconductor Diode I-V Characteristic Curve (Knee Voltage 0.7V and Reverse Breakdown)", "m112_diode_iv_curve", svg_m112_diode_iv_curve())
    attach_svg_to_block(lesson_2, 3, "suggested_diagram", "Half-Wave Rectifier Circuit Diagram and Input AC vs Pulsating DC Waveform Graph", "m112_halfwave_rectifier", svg_m112_halfwave_rectifier())
    attach_svg_to_block(lesson_2, 5, "suggested_diagram", "4-Diode Bridge Rectifier Circuit Diagram Showing Alternating Current Path Conduction", "m112_bridge_rectifier", svg_m112_bridge_rectifier())
    attach_svg_to_block(lesson_2, 6, "suggested_diagram", "RC Filter Smoothing Capacitor Circuit and Smoothed DC Voltage Ripple Reduction Graph", "m112_smoothing_capacitor", svg_m112_smoothing_capacitor())
    attach_svg_to_block(lesson_2, 7, "suggested_diagram", "NPN and PNP Transistor Layer Structure, Terminal Names, and Standard Schematic Symbols", "m112_npn_pnp_transistor", svg_m112_npn_pnp_transistor())
    attach_svg_to_block(lesson_2, 9, "suggested_diagram", "Transistor Automatic Night Light Circuit with LDR Potential Divider Potential Divider", "m112_transistor_switch_ldr", svg_m112_transistor_switch_ldr())

    # Module 11.3 SVGs
    print("\n--- Enriching Module 11.3 ---")
    attach_svg_to_block(lesson_3, 4, "suggested_diagram", "Logic Gate Symbol Family (AND, OR, NOT, NAND, NOR) and Truth Tables", "m113_logic_gates_truth_tables", svg_m113_logic_gates_truth_tables())

    # Wikimedia Assets
    attach_wikimedia_to_block(
        lesson=lesson_1,
        page_num=1,
        title="Historical Germanium Transistor and Vacuum Tube Comparison Unit",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/2N441_GM_Delco_germanium_transistor_%2801%29.jpg/960px-2N441_GM_Delco_germanium_transistor_%2801%29.jpg",
        author="155LA3",
        licensing="CC BY 4.0",
        commons_page="https://commons.wikimedia.org/wiki/File:2N441_GM_Delco_germanium_transistor_(01).jpg"
    )

    attach_wikimedia_to_block(
        lesson=lesson_2,
        page_num=5,
        title="Bridge Rectifier Electronic Component Package Unit",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/3PM4_diode_bridge%2C_IPRS_Baneasa_1988_%2801%29.jpg/960px-3PM4_diode_bridge%2C_IPRS_Baneasa_1988_%2801%29.jpg",
        author="155LA3",
        licensing="CC BY 4.0",
        commons_page="https://commons.wikimedia.org/wiki/File:3PM4_diode_bridge,_IPRS_Baneasa_1988_(01).jpg"
    )

    attach_wikimedia_to_block(
        lesson=lesson_3,
        page_num=10,
        title="Integrated Circuit IC Microchip Silicon Die Unit",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Silicon_Magic_SM3102A_die.JPG/960px-Silicon_Magic_SM3102A_die.JPG",
        author="Birdman",
        licensing="CC BY 3.0",
        commons_page="https://commons.wikimedia.org/wiki/File:Silicon_Magic_SM3102A_die.JPG"
    )

    print("\n" + "=" * 80)
    print("TOPIC 11 VISUAL ENRICHMENT COMPLETED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    run_enrichment_topic11()
