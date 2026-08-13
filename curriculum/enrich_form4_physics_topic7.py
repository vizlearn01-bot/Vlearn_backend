"""
VLearn Form 4 Physics — Topic 7: Cathode Rays
Visual Enrichment Engine (SVGs + Wikimedia Commons)

Enriches all 3 modules of Topic 7 (Cathode Rays) with:
  - 14 high-precision dark-mode vector SVG diagrams (discharge tube pressure stages, 
    Maltese cross rectilinear propagation, electric vs magnetic deflection, interactive CRT electron sandbox, 
    J.J. Thomson e/m charge-to-mass ratio setup, complete CRT internal anatomy, electron gun assembly & grid brightness, 
    Y and X deflection plates, sawtooth time-base waveform graph, electron acceleration energy conservation, 
    CRO graticule grid trace measurement, Maltese cross lab setup, parabolic vs tangent trajectory, 
    and Lissajous figures for frequency/phase diagnostics).
  - 3 authentic Wikimedia Commons photographic assets (Crookes discharge tube, 
    oscilloscope CRT hardware tube, and oscilloscope sine wave trace display).

Usage:
  /home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/venv/bin/python curriculum/enrich_form4_physics_topic7.py
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

BG = "#0a0f1d"
TEXT_MAIN = "#f8fafc"
TEXT_MUTED = "#94a3b8"

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
            f'font-size="16" font-weight="700" text-anchor="middle" letter-spacing="0.5">{title}</text>'
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
# SVG BUILDERS — MODULE 7.1
# =============================================================================

def svg_m71_discharge_tube_pressure_stages():
    """Page 3: Gaseous discharge tube pressure stages"""
    inner = """
    <g transform="translate(40, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="10" stroke="#f59e0b" stroke-width="2"/>
      <text x="180" y="30" fill="#f59e0b" font-size="13" font-weight="700" text-anchor="middle">MODERATE PRESSURE (10 mmHg)</text>

      <rect x="30" y="80" width="300" height="120" fill="#1e293b" rx="20" stroke="#64748b" stroke-width="3"/>
      <rect x="40" y="110" width="15" height="60" fill="#ef4444" rx="2"/>
      <text x="47" y="185" fill="#ef4444" font-size="10" font-weight="800" text-anchor="middle">C(-)</text>

      <rect x="305" y="110" width="15" height="60" fill="#38bdf8" rx="2"/>
      <text x="312" y="185" fill="#38bdf8" font-size="10" font-weight="800" text-anchor="middle">A(+)</text>

      <path d="M 55,140 Q 120,110 180,140 T 305,140" fill="none" stroke="#a855f7" stroke-width="4"/>
      <path d="M 55,140 Q 120,170 180,140 T 305,140" fill="none" stroke="#f59e0b" stroke-width="4"/>

      <text x="180" y="240" fill="#a855f7" font-size="12" font-weight="700" text-anchor="middle">Gas Ionization Streamers</text>
      <text x="180" y="260" fill="#94a3b8" font-size="10" text-anchor="middle">Frequent electron-atom collisions</text>
    </g>

    <g transform="translate(440, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="10" stroke="#22c55e" stroke-width="2"/>
      <text x="180" y="30" fill="#22c55e" font-size="13" font-weight="700" text-anchor="middle">NEAR VACUUM (0.01 mmHg)</text>

      <rect x="30" y="80" width="300" height="120" fill="#030712" rx="20" stroke="#22c55e" stroke-width="3"/>
      <rect x="40" y="110" width="15" height="60" fill="#ef4444" rx="2"/>
      <text x="47" y="185" fill="#ef4444" font-size="10" font-weight="800" text-anchor="middle">C(-)</text>

      <rect x="250" y="110" width="15" height="60" fill="#38bdf8" rx="2"/>
      <text x="257" y="185" fill="#38bdf8" font-size="10" font-weight="800" text-anchor="middle">A(+)</text>

      <line x1="55" y1="140" x2="320" y2="140" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6 3"/>
      <path d="M 315,90 Q 330,140 315,190" fill="none" stroke="#22c55e" stroke-width="8"/>

      <text x="180" y="240" fill="#22c55e" font-size="12" font-weight="800" text-anchor="middle">Bright Green Fluorescence!</text>
      <text x="180" y="260" fill="#94a3b8" font-size="10" text-anchor="middle">Unimpeded cathode ray electron stream</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Gaseous Discharge Tube at Moderate Pressure vs. Near-Vacuum Cathode Ray Fluorescence")

def svg_m71_maltese_cross_rectilinear():
    """Page 5: Maltese Cross rectilinear propagation shadow experiment"""
    inner = """
    <path d="M 80,120 L 480,120 L 760,60 L 760,360 L 480,300 L 80,300 Z" fill="#1e293b" stroke="#475569" stroke-width="3" rx="12"/>

    <rect x="100" y="170" width="20" height="80" fill="#ef4444" rx="3"/>
    <text x="110" y="270" fill="#ef4444" font-size="12" font-weight="800" text-anchor="middle">Cathode (-)</text>

    <line x1="120" y1="210" x2="420" y2="210" stroke="#38bdf8" stroke-width="4"/>
    <line x1="120" y1="170" x2="420" y2="150" stroke="#38bdf8" stroke-width="2"/>
    <line x1="120" y1="250" x2="420" y2="270" stroke="#38bdf8" stroke-width="2"/>

    <g transform="translate(420, 210)">
      <polygon points="0,-40 10,-10 40,0 10,10 0,40 -10,10 -40,0 -10,-10" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
      <text x="0" y="55" fill="#f59e0b" font-size="11" font-weight="700" text-anchor="middle">Maltese Cross</text>
    </g>

    <rect x="750" y="70" width="20" height="280" fill="#22c55e" rx="4"/>

    <g transform="translate(760, 210)">
      <polygon points="0,-60 15,-15 60,0 15,15 0,60 -15,15 -60,0 -15,-15" fill="#030712" stroke="#ef4444" stroke-width="2"/>
      <text x="-40" y="5" fill="#ef4444" font-size="11" font-weight="800">SHADOW</text>
    </g>

    <text x="420" y="380" fill="#22c55e" font-size="13" font-weight="800" text-anchor="middle">
      Rectilinear Propagation: Cathode rays travel in straight lines, casting sharp shadow!
    </text>
    """
    return wrap_svg(inner, W=840, H=420, title="Maltese Cross Experiment Proving Rectilinear Propagation of Cathode Rays")

def svg_m71_electric_magnetic_deflection():
    """Page 6: Electric parabolic vs magnetic perpendicular deflection"""
    inner = """
    <g transform="translate(40, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="10" stroke="#38bdf8" stroke-width="2"/>
      <text x="180" y="30" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">ELECTRIC FIELD DEFLECTION</text>

      <rect x="60" y="70" width="180" height="20" fill="#22c55e" rx="4"/>
      <text x="150" y="85" fill="#fff" font-size="11" font-weight="800" text-anchor="middle">Positive Plate (+V)</text>

      <rect x="60" y="210" width="180" height="20" fill="#ef4444" rx="4"/>
      <text x="150" y="225" fill="#fff" font-size="11" font-weight="800" text-anchor="middle">Negative Plate (-V)</text>

      <path d="M 20,160 L 60,160 Q 150,160 240,90 L 320,30" fill="none" stroke="#38bdf8" stroke-width="4"/>
      <circle cx="240" cy="90" r="6" fill="#38bdf8"/>

      <text x="180" y="270" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">Smooth Parabolic Arc</text>
      <text x="180" y="290" fill="#94a3b8" font-size="10" text-anchor="middle">Bends toward positive plate (+)</text>
    </g>

    <g transform="translate(440, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="10" stroke="#f59e0b" stroke-width="2"/>
      <text x="180" y="30" fill="#f59e0b" font-size="13" font-weight="700" text-anchor="middle">MAGNETIC FIELD DEFLECTION (FLEMING'S LHR)</text>

      <rect x="60" y="70" width="60" height="160" fill="#ef4444" rx="4"/>
      <text x="90" y="155" fill="#fff" font-size="16" font-weight="800" text-anchor="middle">N</text>

      <rect x="240" y="70" width="60" height="160" fill="#0284c7" rx="4"/>
      <text x="270" y="155" fill="#fff" font-size="16" font-weight="800" text-anchor="middle">S</text>

      <path d="M 20,150 L 150,150 Q 200,150 220,90 L 260,30" fill="none" stroke="#f59e0b" stroke-width="4"/>

      <rect x="40" y="245" width="280" height="60" fill="#1e293b" rx="6" stroke="#f59e0b"/>
      <text x="180" y="265" fill="#f59e0b" font-size="11" font-weight="800" text-anchor="middle">Fleming's Left-Hand Rule Tip:</text>
      <text x="180" y="285" fill="#fff" font-size="10" text-anchor="middle">Current finger = OPPOSITE to electron motion!</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Electric Parabolic Deflection vs. Magnetic Perpendicular Deflection (Fleming's LHR)")

def svg_m71_crt_sandbox():
    """Page 8: Interactive CRT electron sandbox model"""
    inner = """
    <path d="M 80,140 L 280,140 L 520,70 L 520,350 L 280,280 L 80,280 Z" fill="#111827" stroke="#38bdf8" stroke-width="3" rx="12"/>

    <rect x="90" y="190" width="15" height="40" fill="#ef4444" rx="2"/>
    <text x="97" y="245" fill="#ef4444" font-size="10" font-weight="800" text-anchor="middle">Cat</text>

    <line x1="120" y1="180" x2="120" y2="240" stroke="#f59e0b" stroke-width="4" stroke-dasharray="4 2"/>
    <text x="120" y="255" fill="#f59e0b" font-size="10" font-weight="700" text-anchor="middle">Grid</text>

    <rect x="150" y="180" width="30" height="40" fill="#22c55e" rx="2"/>
    <rect x="200" y="180" width="30" height="40" fill="#22c55e" rx="2"/>
    <text x="190" y="255" fill="#22c55e" font-size="10" font-weight="700" text-anchor="middle">Anodes</text>

    <rect x="280" y="150" width="60" height="10" fill="#a855f7" rx="2"/>
    <rect x="280" y="240" width="60" height="10" fill="#a855f7" rx="2"/>

    <path d="M 105,210 L 280,210 Q 360,210 520,140" fill="none" stroke="#38bdf8" stroke-width="3"/>
    <circle cx="520" cy="140" r="6" fill="#22c55e"/>

    <g transform="translate(550, 60)">
      <rect x="0" y="0" width="250" height="320" fill="#111827" rx="10" stroke="#38bdf8" stroke-width="2"/>
      <text x="125" y="25" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">INTERACTIVE CONTROL SLIDERS</text>

      <text x="15" y="55" fill="#94a3b8" font-size="10">Heater Current If (Brightness):</text>
      <rect x="15" y="65" width="220" height="10" fill="#1e293b" rx="4"/>
      <circle cx="180" cy="70" r="7" fill="#ef4444"/>

      <text x="15" y="115" fill="#94a3b8" font-size="10">Grid Potential Vg (-100V to 0V):</text>
      <rect x="15" y="125" width="220" height="10" fill="#1e293b" rx="4"/>
      <circle cx="80" cy="130" r="7" fill="#f59e0b"/>

      <text x="15" y="175" fill="#94a3b8" font-size="10">Anode Voltage Vacc (100V to 5kV):</text>
      <rect x="15" y="185" width="220" height="10" fill="#1e293b" rx="4"/>
      <circle cx="190" cy="190" r="7" fill="#22c55e"/>

      <text x="15" y="235" fill="#94a3b8" font-size="10">Y-Plate Deflection Vy (-200V to +200V):</text>
      <rect x="15" y="245" width="220" height="10" fill="#1e293b" rx="4"/>
      <circle cx="170" cy="250" r="7" fill="#a855f7"/>

      <rect x="15" y="275" width="220" height="35" fill="#22c55e15" rx="4" stroke="#22c55e"/>
      <text x="125" y="297" fill="#22c55e" font-size="11" font-weight="800" text-anchor="middle">v = 2.97 × 10⁷ m/s</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Interactive CRT Electron Sandbox: Parameter Slider Controls and Real-Time Trajectory")

def svg_m71_thomson_em_ratio():
    """Page 9: J.J. Thomson e/m specific charge velocity selector"""
    inner = """
    <path d="M 60,160 L 780,160" stroke="#38bdf8" stroke-width="4" stroke-dasharray="8 4"/>

    <!-- Electric Deflection Plates -->
    <rect x="240" y="80" width="280" height="20" fill="#22c55e" rx="4"/>
    <text x="380" y="95" fill="#fff" font-size="12" font-weight="800" text-anchor="middle">Electric Field E (+Plate)</text>

    <rect x="240" y="280" width="280" height="20" fill="#ef4444" rx="4"/>
    <text x="380" y="295" fill="#fff" font-size="12" font-weight="800" text-anchor="middle">Electric Field E (-Plate)</text>

    <!-- Magnetic Field Helmholtz Coils (Crossed Out of Page) -->
    <circle cx="380" cy="190" r="70" fill="none" stroke="#f59e0b" stroke-width="4" stroke-dasharray="6 3"/>
    <text x="380" y="195" fill="#f59e0b" font-size="16" font-weight="800" text-anchor="middle">B Field ⊙</text>

    <!-- Balanced Straight Beam Trajectory -->
    <line x1="60" y1="190" x2="780" y2="190" stroke="#22c55e" stroke-width="5"/>
    <circle cx="780" cy="190" r="8" fill="#22c55e"/>

    <!-- Velocity Selector Formula Box -->
    <rect x="180" y="330" width="480" height="55" fill="#111827" rx="8" stroke="#38bdf8" stroke-width="2"/>
    <text x="420" y="355" fill="#38bdf8" font-size="14" font-weight="800" text-anchor="middle">Velocity Selector: eE = evB  ⇒  v = E / B</text>
    <text x="420" y="375" fill="#22c55e" font-size="13" font-weight="800" text-anchor="middle">Specific Charge e/m_e = E / (B² r) = 1.76 × 10¹¹ C/kg</text>
    """
    return wrap_svg(inner, W=840, H=420, title="J.J. Thomson Crossed Fields Velocity Selector & Specific Charge (e/m_e) Setup")


# =============================================================================
# SVG BUILDERS — MODULE 7.2
# =============================================================================

def svg_m72_crt_internal_anatomy():
    """Page 1: Complete Cathode-Ray Tube internal anatomy"""
    inner = """
    <path d="M 60,150 L 260,150 L 660,60 L 660,360 L 260,270 L 60,270 Z" fill="#111827" stroke="#475569" stroke-width="4" rx="16"/>

    <rect x="80" y="170" width="160" height="80" fill="#0284c715" rx="6" stroke="#38bdf8" stroke-dasharray="4 2"/>
    <text x="160" y="160" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">A. ELECTRON GUN</text>

    <rect x="90" y="195" width="10" height="30" fill="#ef4444"/>
    <text x="95" y="240" fill="#ef4444" font-size="9" text-anchor="middle">Cat</text>

    <line x1="120" y1="185" x2="120" y2="235" stroke="#f59e0b" stroke-width="3" stroke-dasharray="3 2"/>
    <text x="120" y="240" fill="#f59e0b" font-size="9" text-anchor="middle">Grid</text>

    <rect x="150" y="190" width="25" height="40" fill="#22c55e"/>
    <rect x="190" y="190" width="25" height="40" fill="#22c55e"/>
    <text x="182" y="240" fill="#22c55e" font-size="9" text-anchor="middle">Anodes</text>

    <rect x="280" y="100" width="180" height="220" fill="#a855f715" rx="6" stroke="#a855f7" stroke-dasharray="4 2"/>
    <text x="370" y="90" fill="#a855f7" font-size="12" font-weight="800" text-anchor="middle">B. DEFLECTION SYSTEM</text>

    <rect x="300" y="130" width="60" height="12" fill="#a855f7" rx="2"/>
    <rect x="300" y="278" width="60" height="12" fill="#a855f7" rx="2"/>
    <text x="330" y="125" fill="#a855f7" font-size="10" font-weight="700" text-anchor="middle">Y-Plates (Vertical)</text>

    <rect x="400" y="150" width="12" height="60" fill="#f59e0b" rx="2"/>
    <rect x="430" y="150" width="12" height="60" fill="#f59e0b" rx="2"/>
    <text x="421" y="140" fill="#f59e0b" font-size="10" font-weight="700" text-anchor="middle">X-Plates (TB)</text>

    <rect x="655" y="65" width="20" height="290" fill="#22c55e" rx="4"/>
    <text x="730" y="200" fill="#22c55e" font-size="12" font-weight="800" text-anchor="middle">C. PHOSPHOR</text>
    <text x="730" y="220" fill="#22c55e" font-size="12" font-weight="800" text-anchor="middle">SCREEN</text>

    <line x1="100" y1="210" x2="660" y2="210" stroke="#38bdf8" stroke-width="3"/>
    <circle cx="660" cy="210" r="7" fill="#fff"/>
    """
    return wrap_svg(inner, W=840, H=420, title="Complete Internal Assembly Anatomy of a Cathode-Ray Tube (CRT)")

def svg_m72_electron_gun_components():
    """Page 2: Electron gun assembly and grid brightness mechanism"""
    inner = """
    <g transform="translate(60, 80)">
      <rect x="0" y="0" width="220" height="280" fill="#111827" rx="10" stroke="#ef4444" stroke-width="2"/>
      <text x="110" y="30" fill="#ef4444" font-size="13" font-weight="700" text-anchor="middle">1. HEATER & CATHODE</text>

      <rect x="30" y="80" width="160" height="60" fill="#78350f" rx="6" stroke="#f59e0b"/>
      <text x="110" y="115" fill="#fff" font-size="12" font-weight="800" text-anchor="middle">6 V Heater Filament</text>

      <rect x="40" y="160" width="140" height="60" fill="#ef444422" rx="6" stroke="#ef4444"/>
      <text x="110" y="185" fill="#ef4444" font-size="12" font-weight="800" text-anchor="middle">Barium-Strontium</text>
      <text x="110" y="205" fill="#ef4444" font-size="12" font-weight="800" text-anchor="middle">Oxide Cathode</text>
    </g>

    <g transform="translate(310, 80)">
      <rect x="0" y="0" width="220" height="280" fill="#111827" rx="10" stroke="#f59e0b" stroke-width="2"/>
      <text x="110" y="30" fill="#f59e0b" font-size="13" font-weight="700" text-anchor="middle">2. CONTROL GRID (-Vg)</text>

      <rect x="30" y="80" width="160" height="120" fill="#1e293b" rx="6" stroke="#f59e0b" stroke-width="3"/>
      <circle cx="110" cy="140" r="15" fill="#030712" stroke="#f59e0b" stroke-width="2"/>
      <text x="110" y="145" fill="#f59e0b" font-size="11" font-weight="800" text-anchor="middle">Hole</text>

      <text x="110" y="235" fill="#f59e0b" font-size="12" font-weight="700" text-anchor="middle">Negative Repulsion</text>
      <text x="110" y="255" fill="#94a3b8" font-size="10" text-anchor="middle">Controls Brightness Knob!</text>
    </g>

    <g transform="translate(560, 80)">
      <rect x="0" y="0" width="220" height="280" fill="#111827" rx="10" stroke="#22c55e" stroke-width="2"/>
      <text x="110" y="30" fill="#22c55e" font-size="13" font-weight="700" text-anchor="middle">3. ANODES (+200V - 5kV)</text>

      <rect x="30" y="80" width="160" height="120" fill="#22c55e15" rx="6" stroke="#22c55e" stroke-width="2"/>
      <line x1="40" y1="140" x2="180" y2="140" stroke="#38bdf8" stroke-width="4"/>

      <text x="110" y="235" fill="#22c55e" font-size="12" font-weight="700" text-anchor="middle">Electrostatic Lens</text>
      <text x="110" y="255" fill="#94a3b8" font-size="10" text-anchor="middle">Focuses & Accelerates Beam</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Detailed Construction & Function of the CRT Electron Gun Components")

def svg_m72_y_x_deflection_plates():
    """Page 4: Y-plates and X-plates deflection geometry"""
    inner = """
    <g transform="translate(40, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="10" stroke="#a855f7" stroke-width="2"/>
      <text x="180" y="30" fill="#a855f7" font-size="13" font-weight="700" text-anchor="middle">Y-DEFLECTION PLATES (VERTICAL)</text>

      <rect x="80" y="70" width="200" height="20" fill="#a855f7" rx="4"/>
      <rect x="80" y="210" width="200" height="20" fill="#a855f7" rx="4"/>

      <line x1="40" y1="150" x2="320" y2="100" stroke="#38bdf8" stroke-width="4"/>

      <text x="180" y="260" fill="#a855f7" font-size="12" font-weight="700" text-anchor="middle">Connected to Y-Gain Control</text>
      <text x="180" y="280" fill="#94a3b8" font-size="10" text-anchor="middle">Measures Input Voltage Amplitude</text>
    </g>

    <g transform="translate(440, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="10" stroke="#f59e0b" stroke-width="2"/>
      <text x="180" y="30" fill="#f59e0b" font-size="13" font-weight="700" text-anchor="middle">X-DEFLECTION PLATES (HORIZONTAL)</text>

      <rect x="100" y="70" width="20" height="160" fill="#f59e0b" rx="4"/>
      <rect x="240" y="70" width="20" height="160" fill="#f59e0b" rx="4"/>

      <line x1="40" y1="150" x2="320" y2="150" stroke="#38bdf8" stroke-width="4"/>

      <text x="180" y="260" fill="#f59e0b" font-size="12" font-weight="700" text-anchor="middle">Connected to Time-Base Circuit</text>
      <text x="180" y="280" fill="#94a3b8" font-size="10" text-anchor="middle">Sweeps Spot Left to Right</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Orthogonal Y-Plates (Vertical Input) vs. X-Plates (Horizontal Time-Base Sweep)")

def svg_m72_sawtooth_waveform_graph():
    """Page 6: Time-base sawtooth voltage waveform graph"""
    inner = """
    <rect x="100" y="60" width="660" height="260" fill="#030712" rx="10" stroke="#38bdf8" stroke-width="2"/>
    <line x1="100" y1="190" x2="760" y2="190" stroke="#475569" stroke-width="2"/>
    <line x1="100" y1="60" x2="100" y2="320" stroke="#475569" stroke-width="2"/>

    <line x1="100" y1="300" x2="280" y2="80" stroke="#22c55e" stroke-width="4"/>
    <line x1="280" y1="80" x2="280" y2="300" stroke="#ef4444" stroke-width="3" stroke-dasharray="4 2"/>

    <line x1="280" y1="300" x2="460" y2="80" stroke="#22c55e" stroke-width="4"/>
    <line x1="460" y1="80" x2="460" y2="300" stroke="#ef4444" stroke-width="3" stroke-dasharray="4 2"/>

    <line x1="460" y1="300" x2="640" y2="80" stroke="#22c55e" stroke-width="4"/>
    <line x1="640" y1="80" x2="640" y2="300" stroke="#ef4444" stroke-width="3" stroke-dasharray="4 2"/>

    <text x="190" y="170" fill="#22c55e" font-size="12" font-weight="800">Linear Sweep (Left -> Right)</text>
    <text x="290" y="130" fill="#ef4444" font-size="11" font-weight="800">Instant Flyback</text>

    <text x="430" y="355" fill="#f8fafc" font-size="13" font-weight="700" text-anchor="middle">Time t (seconds)</text>
    <text x="45" y="190" fill="#f8fafc" font-size="13" font-weight="700" text-anchor="middle" transform="rotate(-90 45 190)">X-Plate Voltage (V)</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Time-Base Circuit Sawtooth Waveform: Linear Sweep and Instant Flyback")


# =============================================================================
# SVG BUILDERS — MODULE 7.3
# =============================================================================

def svg_m73_energy_conservation_electron_gun():
    """Page 1: Energy conservation in electron gun equation diagram"""
    inner = """
    <g transform="translate(40, 60)">
      <rect x="0" y="0" width="340" height="320" fill="#111827" rx="10" stroke="#38bdf8" stroke-width="2"/>
      <text x="170" y="30" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">1. ELECTROSTATIC WORK</text>

      <rect x="20" y="80" width="300" height="80" fill="#1e293b" rx="8" stroke="#38bdf8"/>
      <text x="170" y="125" fill="#f8fafc" font-size="20" font-weight="800" text-anchor="middle">Work = e × V</text>

      <text x="170" y="200" fill="#94a3b8" font-size="12" text-anchor="middle">e = 1.6 × 10⁻¹⁹ Coulombs</text>
      <text x="170" y="225" fill="#94a3b8" font-size="12" text-anchor="middle">V = Accelerating Voltage (Volts)</text>
    </g>

    <text x="420" y="220" fill="#22c55e" font-size="36" font-weight="800" text-anchor="middle">=</text>

    <g transform="translate(460, 60)">
      <rect x="0" y="0" width="340" height="320" fill="#111827" rx="10" stroke="#22c55e" stroke-width="2"/>
      <text x="170" y="30" fill="#22c55e" font-size="13" font-weight="700" text-anchor="middle">2. KINETIC ENERGY GAINED</text>

      <rect x="20" y="80" width="300" height="80" fill="#1e293b" rx="8" stroke="#22c55e"/>
      <text x="170" y="125" fill="#f8fafc" font-size="20" font-weight="800" text-anchor="middle">E_k = ½ m_e v²</text>

      <text x="170" y="200" fill="#94a3b8" font-size="12" text-anchor="middle">m_e = 9.1 × 10⁻³¹ kg</text>
      <text x="170" y="225" fill="#22c55e" font-size="14" font-weight="800" text-anchor="middle">v = √( 2eV / m_e )</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Conservation of Energy in the Electron Gun: Electrostatic Work to Kinetic Energy")

def svg_m73_cro_graticule_grid_trace():
    """Page 2: CRO graticule grid trace measurement"""
    inner = """
    <rect x="100" y="60" width="640" height="280" fill="#022c22" rx="16" stroke="#22c55e" stroke-width="4"/>

    <g stroke="#15803d" stroke-width="1" stroke-dasharray="2 2">
      <line x1="180" y1="60" x2="180" y2="340"/>
      <line x1="260" y1="60" x2="260" y2="340"/>
      <line x1="340" y1="60" x2="340" y2="340"/>
      <line x1="420" y1="60" x2="420" y2="340"/>
      <line x1="500" y1="60" x2="500" y2="340"/>
      <line x1="580" y1="60" x2="580" y2="340"/>
      <line x1="660" y1="60" x2="660" y2="340"/>

      <line x1="100" y1="110" x2="740" y2="110"/>
      <line x1="100" y1="160" x2="740" y2="160"/>
      <line x1="100" y1="200" x2="740" y2="200" stroke="#22c55e" stroke-width="2"/>
      <line x1="100" y1="240" x2="740" y2="240"/>
      <line x1="100" y1="290" x2="740" y2="290"/>
    </g>

    <path d="M 100,200 Q 180,60 260,200 Q 340,340 420,200 Q 500,60 580,200 Q 660,340 740,200" fill="none" stroke="#4ade80" stroke-width="4"/>

    <line x1="260" y1="100" x2="260" y2="200" stroke="#f59e0b" stroke-width="3"/>
    <text x="270" y="150" fill="#f59e0b" font-size="12" font-weight="800">Peak Height h = 2.0 cm</text>

    <line x1="100" y1="310" x2="420" y2="310" stroke="#38bdf8" stroke-width="3"/>
    <text x="260" y="330" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">Cycle Length d = 4.0 cm</text>

    <rect x="100" y="350" width="640" height="40" fill="#111827" rx="6" stroke="#1e293b"/>
    <text x="420" y="375" fill="#f8fafc" font-size="12" font-weight="700" text-anchor="middle">
      V_0 = h × Y_gain  |  Period T = d × Time-Base  |  Frequency f = 1 / T
    </text>
    """
    return wrap_svg(inner, W=840, H=420, title="CRO Graticule Screen Trace Measurements for Amplitude, Period, and Frequency")

def svg_m73_maltese_cross_lab_setup():
    """Page 9: Maltese Cross laboratory setup diagram"""
    inner = """
    <rect x="40" y="140" width="140" height="180" fill="#111827" rx="10" stroke="#ef4444" stroke-width="3"/>
    <text x="110" y="175" fill="#ef4444" font-size="14" font-weight="800" text-anchor="middle">EHT SUPPLY</text>
    <text x="110" y="200" fill="#f8fafc" font-size="13" font-weight="800" text-anchor="middle">3,000 V D.C.</text>

    <path d="M 180,180 L 260,180" fill="none" stroke="#ef4444" stroke-width="4"/>
    <path d="M 180,260 L 360,260" fill="none" stroke="#38bdf8" stroke-width="4"/>

    <path d="M 260,160 L 460,160 L 620,100 L 620,320 L 460,260 L 260,260 Z" fill="#1e293b" stroke="#64748b" stroke-width="3"/>

    <rect x="270" y="190" width="15" height="40" fill="#ef4444"/>
    <rect x="360" y="190" width="15" height="40" fill="#38bdf8"/>

    <polygon points="460,180 470,200 490,210 470,220 460,240 450,220 430,210 450,200" fill="#f59e0b"/>

    <rect x="430" y="50" width="60" height="40" fill="#ef4444" rx="4"/>
    <text x="460" y="75" fill="#fff" font-size="14" font-weight="800" text-anchor="middle">N</text>

    <rect x="620" y="100" width="15" height="220" fill="#22c55e" rx="3"/>

    <text x="420" y="380" fill="#22c55e" font-size="12" font-weight="700" text-anchor="middle">
      Maltese Cross Tube Circuit: High-voltage EHT acceleration and bar magnet deflection
    </text>
    """
    return wrap_svg(inner, W=840, H=420, title="Laboratory Maltese Cross Shadow & Magnetic Field Deflection Circuit Setup")

def svg_m73_parabolic_vs_straight_trajectory():
    """Page 11: Parabolic deflection inside parallel plates vs straight tangent exit"""
    inner = """
    <rect x="180" y="100" width="300" height="20" fill="#22c55e" rx="4"/>
    <text x="330" y="115" fill="#fff" font-size="12" font-weight="800" text-anchor="middle">Positive Plate (+V)</text>

    <rect x="180" y="300" width="300" height="20" fill="#ef4444" rx="4"/>
    <text x="330" y="315" fill="#fff" font-size="12" font-weight="800" text-anchor="middle">Negative Plate (-V)</text>

    <g stroke="#22c55e" stroke-width="1.5" stroke-dasharray="3 3">
      <line x1="230" y1="120" x2="230" y2="300"/>
      <line x1="330" y1="120" x2="330" y2="300"/>
      <line x1="430" y1="120" x2="430" y2="300"/>
    </g>

    <line x1="40" y1="210" x2="180" y2="210" stroke="#38bdf8" stroke-width="4"/>

    <path d="M 180,210 Q 330,210 480,140" fill="none" stroke="#38bdf8" stroke-width="4"/>
    <line x1="480" y1="140" x2="780" y2="0" stroke="#f59e0b" stroke-width="4"/>

    <rect x="230" y="240" width="200" height="40" fill="#111827" rx="6" stroke="#38bdf8"/>
    <text x="330" y="265" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">Region 1: Smooth Parabola</text>

    <rect x="540" y="160" width="220" height="40" fill="#111827" rx="6" stroke="#f59e0b"/>
    <text x="650" y="185" fill="#f59e0b" font-size="11" font-weight="700" text-anchor="middle">Region 2: Straight Tangent Line</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Electron Trajectory Geometry: Parabolic Arc Inside Field vs. Straight Tangent Outside")

def svg_m73_lissajous_figures():
    """Page 12: Lissajous figures on CRO screen grid"""
    inner = """
    <!-- Left Screen: 1:1 Circle / Ellipse (x = 40, w = 360) -->
    <g transform="translate(40, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#022c22" rx="12" stroke="#22c55e" stroke-width="3"/>
      <text x="180" y="30" fill="#22c55e" font-size="13" font-weight="800" text-anchor="middle">1:1 RATIO (Circle / Ellipse)</text>

      <!-- Graticule grid -->
      <line x1="180" y1="40" x2="180" y2="280" stroke="#15803d" stroke-dasharray="2 2"/>
      <line x1="20" y1="160" x2="340" y2="160" stroke="#15803d" stroke-dasharray="2 2"/>

      <!-- Circle Trace -->
      <ellipse cx="180" cy="160" rx="90" ry="90" fill="none" stroke="#4ade80" stroke-width="4"/>

      <text x="180" y="270" fill="#f8fafc" font-size="11" font-weight="700" text-anchor="middle">Equal Frequencies (f_y = f_x)</text>
      <text x="180" y="290" fill="#94a3b8" font-size="10" text-anchor="middle">Phase Shift ϕ = 90°</text>
    </g>

    <!-- Right Screen: 1:2 Figure-8 Shape (x = 440, w = 360) -->
    <g transform="translate(440, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#022c22" rx="12" stroke="#22c55e" stroke-width="3"/>
      <text x="180" y="30" fill="#22c55e" font-size="13" font-weight="800" text-anchor="middle">1:2 RATIO (Figure-Eight)</text>

      <!-- Graticule grid -->
      <line x1="180" y1="40" x2="180" y2="280" stroke="#15803d" stroke-dasharray="2 2"/>
      <line x1="20" y1="160" x2="340" y2="160" stroke="#15803d" stroke-dasharray="2 2"/>

      <!-- Figure 8 Trace -->
      <path d="M 180,160 Q 250,90 180,70 Q 110,90 180,160 Q 250,230 180,250 Q 110,230 180,160" fill="none" stroke="#4ade80" stroke-width="4"/>

      <text x="180" y="270" fill="#f8fafc" font-size="11" font-weight="700" text-anchor="middle">Double Frequency (f_y = 2 f_x)</text>
      <text x="180" y="290" fill="#94a3b8" font-size="10" text-anchor="middle">2 Vertical Loops : 1 Horizontal Loop</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Lissajous Figures on CRO Screen Grid for Phase Shift and Frequency Diagnostics")


# =============================================================================
# MAIN ENRICHMENT EXECUTOR FOR TOPIC 7
# =============================================================================

def run_enrichment_topic7():
    print("=" * 80)
    print("VLEARN FORM 4 PHYSICS — TOPIC 7 VISUAL ENRICHMENT")
    print("=" * 80)

    topic = Topic.objects.filter(
        subject__name="Physics",
        subject__grade__name="Form 4",
        name__icontains="Cathode Rays"
    ).first()

    if not topic:
        print("ERROR: Topic 7: Cathode Rays not found! Run ingest_form4_physics_topic7.py first.")
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

    # Module 7.1 SVGs
    print("--- Enriching Module 7.1 ---")
    attach_svg_to_block(lesson_1, 3, "suggested_diagram", "Gaseous Discharge Tube at Moderate Pressure vs. Near-Vacuum Cathode Ray Fluorescence", "m71_discharge_tube_pressure_stages", svg_m71_discharge_tube_pressure_stages())
    attach_svg_to_block(lesson_1, 5, "suggested_diagram", "Maltese Cross Experiment Proving Rectilinear Propagation of Cathode Rays", "m71_maltese_cross_rectilinear", svg_m71_maltese_cross_rectilinear())
    attach_svg_to_block(lesson_1, 6, "suggested_diagram", "Electric Parabolic Deflection vs. Magnetic Perpendicular Deflection (Fleming's LHR)", "m71_electric_magnetic_deflection", svg_m71_electric_magnetic_deflection())
    attach_svg_to_block(lesson_1, 8, "suggested_simulation", "Interactive CRT Electron Sandbox: Parameter Slider Controls and Real-Time Trajectory", "m71_crt_sandbox", svg_m71_crt_sandbox())
    attach_svg_to_block(lesson_1, 9, "suggested_diagram", "J.J. Thomson Crossed Fields Velocity Selector & Specific Charge (e/m_e) Setup", "m71_thomson_em_ratio", svg_m71_thomson_em_ratio())

    # Module 7.2 SVGs
    print("\n--- Enriching Module 7.2 ---")
    attach_svg_to_block(lesson_2, 1, "suggested_diagram", "Complete Internal Assembly Anatomy of a Cathode-Ray Tube (CRT)", "m72_crt_internal_anatomy", svg_m72_crt_internal_anatomy())
    attach_svg_to_block(lesson_2, 2, "suggested_diagram", "Detailed Construction & Function of the CRT Electron Gun Components", "m72_electron_gun_components", svg_m72_electron_gun_components())
    attach_svg_to_block(lesson_2, 4, "suggested_diagram", "Orthogonal Y-Plates (Vertical Input) vs. X-Plates (Horizontal Time-Base Sweep)", "m72_y_x_deflection_plates", svg_m72_y_x_deflection_plates())
    attach_svg_to_block(lesson_2, 6, "suggested_diagram", "Time-Base Circuit Sawtooth Waveform: Linear Sweep and Instant Flyback", "m72_sawtooth_waveform_graph", svg_m72_sawtooth_waveform_graph())

    # Module 7.3 SVGs
    print("\n--- Enriching Module 7.3 ---")
    attach_svg_to_block(lesson_3, 1, "suggested_diagram", "Conservation of Energy in the Electron Gun: Electrostatic Work to Kinetic Energy", "m73_energy_conservation_electron_gun", svg_m73_energy_conservation_electron_gun())
    attach_svg_to_block(lesson_3, 2, "suggested_diagram", "CRO Graticule Screen Trace Measurements for Amplitude, Period, and Frequency", "m73_cro_graticule_grid_trace", svg_m73_cro_graticule_grid_trace())
    attach_svg_to_block(lesson_3, 9, "suggested_diagram", "Laboratory Maltese Cross Shadow & Magnetic Field Deflection Circuit Setup", "m73_maltese_cross_lab_setup", svg_m73_maltese_cross_lab_setup())
    attach_svg_to_block(lesson_3, 11, "suggested_diagram", "Electron Trajectory Geometry: Parabolic Arc Inside Field vs. Straight Tangent Outside", "m73_parabolic_vs_straight_trajectory", svg_m73_parabolic_vs_straight_trajectory())
    attach_svg_to_block(lesson_3, 12, "suggested_diagram", "Lissajous Figures on CRO Screen Grid for Phase Shift and Frequency Diagnostics", "m73_lissajous_figures", svg_m73_lissajous_figures())

    # Wikimedia Assets
    attach_wikimedia_to_block(
        lesson=lesson_1,
        page_num=3,
        title="Crookes Gaseous Discharge Tube Demonstrating Cathode Rays",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Crookes_tube_-_cathode_Rays.jpg/960px-Crookes_tube_-_cathode_Rays.jpg",
        author="Wikimedia Commons Contributor",
        licensing="CC BY-SA 4.0",
        commons_page="https://commons.wikimedia.org/wiki/File:Crookes_tube_-_cathode_Rays.jpg"
    )

    attach_wikimedia_to_block(
        lesson=lesson_2,
        page_num=1,
        title="Cathode-Ray Tube Glass Hardware Construction Unit",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/D13-27_GH_%CC%A0_T_Oscilloscope_CRT_04.jpg/960px-D13-27_GH_%CC%A0_T_Oscilloscope_CRT_04.jpg",
        author="Mister_C",
        licensing="CC BY-SA 4.0",
        commons_page="https://commons.wikimedia.org/wiki/File:D13-27_GH_%CC%A0_T_Oscilloscope_CRT_04.jpg"
    )

    attach_wikimedia_to_block(
        lesson=lesson_3,
        page_num=2,
        title="Cathode-Ray Oscilloscope Screen Display Trace",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/0/06/Simple-diode-detector-AM-demodulator-oscilloscope.gif",
        author="Wikimedia Commons Contributor",
        licensing="CC0",
        commons_page="https://commons.wikimedia.org/wiki/File:Simple-diode-detector-AM-demodulator-oscilloscope.gif"
    )

    print("\n" + "=" * 80)
    print("TOPIC 7 VISUAL ENRICHMENT COMPLETED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    run_enrichment_topic7()
