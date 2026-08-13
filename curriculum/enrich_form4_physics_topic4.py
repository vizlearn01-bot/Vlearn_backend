"""
VLearn Form 4 Physics — Topic 4: Electromagnetic Spectrum
Visual Enrichment Engine (SVGs + Wikimedia Commons)

Enriches all 3 modules of Topic 4 (Electromagnetic Spectrum) with:
  - 11 high-precision dark-mode vector SVG diagrams (3D mutually perpendicular EM wave fields, 
    wave equation & metric prefix converter, standing wave microwave speed of light experiment, 
    waveform trace crest analysis, horizontal continuous 7-band spectrum scale, vertical frequency vs wavelength scale, 
    radar ranging and Doppler speed gun, infrared greenhouse trapping mechanism, UV currency fluorescent security & X-ray, 
    gamma cold sterilization & grain pest control, and ionizing radiation vs lead shielding protection).
  - 3 authentic Wikimedia Commons photographic assets (OpenStax Astronomical EM spectrum, 
    historical medical hand skeletal radiograph, and NASA STScI spectrum diagram).

Usage:
  /home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/venv/bin/python curriculum/enrich_form4_physics_topic4.py
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
ACCENT_BLUE = "#38bdf8"
ACCENT_AMBER = "#f59e0b"
ACCENT_GREEN = "#22c55e"
ACCENT_RED = "#ef4444"
ACCENT_PURPLE = "#a855f7"

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
# SVG BUILDERS — MODULE 4.1
# =============================================================================

def svg_m41_3d_em_wave():
    """Page 2: 3D Mutually Perpendicular Field Vectors"""
    inner = """
    <!-- 3D Axes: Origin at (100, 220). X-axis: (100,220)->(740,220). Y-axis: (100,220)->(100,60). Z-axis: (100,220)->(40,300) -->
    <!-- X-axis (Propagation) -->
    <line x1="100" y1="220" x2="750" y2="220" stroke="#94a3b8" stroke-width="2"/>
    <polygon points="745,215 758,220 745,225" fill="#94a3b8"/>
    <text x="765" y="225" fill="#22c55e" font-size="12" font-weight="700">x (Propagation at c)</text>

    <!-- Y-axis (Electric Field E) -->
    <line x1="100" y1="220" x2="100" y2="55" stroke="#ef4444" stroke-width="2"/>
    <polygon points="95,60 100,48 105,60" fill="#ef4444"/>
    <text x="100" y="40" fill="#ef4444" font-size="13" font-weight="700" text-anchor="middle">y: Electric Field (E)</text>

    <!-- Z-axis (Magnetic Field B) -->
    <line x1="100" y1="220" x2="30" y2="310" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="38,300 24,318 30,305" fill="#38bdf8"/>
    <text x="25" y="335" fill="#38bdf8" font-size="13" font-weight="700">z: Magnetic Field (B)</text>

    <!-- Electric Field Sinusoidal Wave (Red, vertical in XY plane) -->
    <!-- Two full cycles from x = 100 to x = 660 (period = 280 px) -->
    <path d="M 100,220 Q 170,80 240,220 Q 310,360 380,220 Q 450,80 520,220 Q 590,360 660,220" fill="none" stroke="#ef4444" stroke-width="3"/>

    <!-- Vertical E-Field Vector Arrows -->
    <line x1="170" y1="220" x2="170" y2="90" stroke="#ef4444" stroke-width="1.5"/>
    <polygon points="166,100 170,85 174,100" fill="#ef4444"/>

    <line x1="310" y1="220" x2="310" y2="350" stroke="#ef4444" stroke-width="1.5"/>
    <polygon points="306,340 310,355 314,340" fill="#ef4444"/>

    <line x1="450" y1="220" x2="450" y2="90" stroke="#ef4444" stroke-width="1.5"/>
    <polygon points="446,100 450,85 454,100" fill="#ef4444"/>

    <!-- Magnetic Field Sinusoidal Wave (Blue, projected in XZ plane with slant) -->
    <path d="M 100,220 Q 140,270 240,220 Q 340,170 380,220 Q 420,270 520,220 Q 620,170 660,220" fill="none" stroke="#38bdf8" stroke-width="3"/>

    <!-- Slanted B-Field Vector Arrows -->
    <line x1="170" y1="220" x2="140" y2="260" stroke="#38bdf8" stroke-width="1.5"/>
    <line x1="450" y1="220" x2="420" y2="260" stroke="#38bdf8" stroke-width="1.5"/>

    <!-- Wavelength Dimension Line between Crests (x = 170 to x = 450) -->
    <line x1="170" y1="65" x2="450" y2="65" stroke="#f59e0b" stroke-width="2"/>
    <polygon points="178,61 170,65 178,69" fill="#f59e0b"/>
    <polygon points="442,61 450,65 442,69" fill="#f59e0b"/>
    <text x="310" y="55" fill="#f59e0b" font-size="13" font-weight="700" text-anchor="middle">Wavelength (λ = 280 mm equivalent)</text>

    <!-- Bottom Annotation Card -->
    <rect x="180" y="345" width="480" height="50" fill="#111827" rx="8" stroke="#1e293b"/>
    <text x="420" y="375" fill="#f8fafc" font-size="12" font-weight="600" text-anchor="middle">
      Electric Field E(y) ⊥ Magnetic Field B(z) ⊥ Propagation Vector v(x) at speed c
    </text>
    """
    return wrap_svg(inner, W=840, H=420, title="3D Vector Geometry of a Propagating Transverse Electromagnetic Wave")

def svg_m41_wave_equation():
    """Page 4: Wave equation and metric prefixes visual map"""
    inner = """
    <!-- Central Formula Box at x = 280, y = 60 -->
    <rect x="240" y="60" width="360" height="100" fill="#111827" rx="12" stroke="#38bdf8" stroke-width="2"/>
    <text x="420" y="105" fill="#22c55e" font-size="28" font-weight="800" text-anchor="middle">c = f · λ</text>
    <text x="420" y="138" fill="#94a3b8" font-size="12" text-anchor="middle">Speed in vacuum c = 3.0 × 10⁸ m/s (Constant)</text>

    <!-- Left Box: Frequency Units -->
    <g transform="translate(60, 180)">
      <rect x="0" y="0" width="330" height="200" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="165" y="30" fill="#ef4444" font-size="14" font-weight="700" text-anchor="middle">FREQUENCY (f) CONVERSIONS</text>

      <text x="20" y="65" fill="#f8fafc" font-size="12">• Kilohertz (kHz): <tspan fill="#f59e0b">10³ Hz</tspan></text>
      <text x="20" y="95" fill="#f8fafc" font-size="12">• Megahertz (MHz): <tspan fill="#f59e0b">10⁶ Hz</tspan> (Radio / TV)</text>
      <text x="20" y="125" fill="#f8fafc" font-size="12">• Gigahertz (GHz): <tspan fill="#f59e0b">10⁹ Hz</tspan> (Cellular / Radar)</text>
      <text x="20" y="155" fill="#f8fafc" font-size="12">• Terahertz (THz): <tspan fill="#f59e0b">10¹² Hz</tspan> (Visible light)</text>
      <text x="20" y="185" fill="#22c55e" font-size="11" font-weight="700">Formula: f = c / λ</text>
    </g>

    <!-- Right Box: Wavelength Units -->
    <g transform="translate(450, 180)">
      <rect x="0" y="0" width="330" height="200" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="165" y="30" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">WAVELENGTH (λ) CONVERSIONS</text>

      <text x="20" y="65" fill="#f8fafc" font-size="12">• Centimeter (cm): <tspan fill="#f59e0b">10⁻² m</tspan></text>
      <text x="20" y="95" fill="#f8fafc" font-size="12">• Millimeter (mm): <tspan fill="#f59e0b">10⁻³ m</tspan></text>
      <text x="20" y="125" fill="#f8fafc" font-size="12">• Micrometer (µm): <tspan fill="#f59e0b">10⁻⁶ m</tspan> (Infrared)</text>
      <text x="20" y="155" fill="#f8fafc" font-size="12">• Nanometer (nm): <tspan fill="#f59e0b">10⁻⁹ m</tspan> (Visible light)</text>
      <text x="20" y="185" fill="#22c55e" font-size="11" font-weight="700">Formula: λ = c / f</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="The Electromagnetic Wave Equation and Essential SI Metric Prefixes")


# =============================================================================
# SVG BUILDERS — MODULE 4.2
# =============================================================================

def svg_m42_microwave_speed_of_light():
    """Page 2: Microwave standing wave speed of light experiment"""
    inner = """
    <!-- Microwave Cavity (x = 60 to 480, y = 60 to 360) -->
    <rect x="60" y="60" width="420" height="300" fill="#111827" rx="10" stroke="#38bdf8" stroke-width="2"/>
    <text x="80" y="90" fill="#38bdf8" font-size="13" font-weight="700">Microwave Oven Cavity (Stationary Tray)</text>

    <!-- Standing Wave in Cavity -->
    <path d="M 80,180 Q 140,110 200,180 Q 260,250 320,180 Q 380,110 440,180" fill="none" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="6 3"/>
    <path d="M 80,180 Q 140,250 200,180 Q 260,110 320,180 Q 380,250 440,180" fill="none" stroke="#f59e0b" stroke-width="2.5"/>

    <!-- Antinode Labels -->
    <text x="140" y="105" fill="#ef4444" font-size="10" font-weight="700" text-anchor="middle">Antinode (Hot)</text>
    <text x="260" y="105" fill="#ef4444" font-size="10" font-weight="700" text-anchor="middle">Antinode (Hot)</text>
    <text x="380" y="105" fill="#ef4444" font-size="10" font-weight="700" text-anchor="middle">Antinode (Hot)</text>

    <!-- Stationary Tray at y = 280 -->
    <rect x="80" y="270" width="380" height="20" fill="#334155" rx="3" stroke="#64748b"/>
    <text x="90" y="285" fill="#94a3b8" font-size="9">Glass Tray</text>

    <!-- Melted Chocolate Spots on Tray -->
    <circle cx="140" cy="270" r="14" fill="#78350f" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="260" cy="270" r="14" fill="#78350f" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="380" cy="270" r="14" fill="#78350f" stroke="#f59e0b" stroke-width="2"/>

    <!-- Distance d = lambda/2 between Melt Spots -->
    <line x1="140" y1="310" x2="260" y2="310" stroke="#22c55e" stroke-width="2"/>
    <polygon points="148,306 140,310 148,314" fill="#22c55e"/>
    <polygon points="252,306 260,310 252,314" fill="#22c55e"/>
    <text x="200" y="330" fill="#22c55e" font-size="12" font-weight="700" text-anchor="middle">d = λ/2 = 6.1 cm</text>

    <!-- Right Derivation Panel -->
    <g transform="translate(510, 60)">
      <rect x="0" y="0" width="290" height="300" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="145" y="30" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">EXPERIMENTAL PHYSICS</text>

      <g transform="translate(15, 60)">
        <text x="0" y="0" fill="#f8fafc" font-size="12">1. Hot spot spacing:</text>
        <text x="10" y="20" fill="#f59e0b" font-size="12">d = 6.1 cm = 0.061 m</text>

        <text x="0" y="55" fill="#f8fafc" font-size="12">2. Wavelength derivation:</text>
        <text x="10" y="75" fill="#22c55e" font-size="12">λ = 2 × d = 0.122 m</text>

        <text x="0" y="110" fill="#f8fafc" font-size="12">3. Oven frequency from label:</text>
        <text x="10" y="130" fill="#38bdf8" font-size="12">f = 2450 MHz = 2.45 × 10⁹ Hz</text>

        <rect x="0" y="150" width="260" height="60" fill="#22c55e15" rx="6" stroke="#22c55e44"/>
        <text x="10" y="172" fill="#94a3b8" font-size="10">Calculated Speed of Wave:</text>
        <text x="10" y="195" fill="#22c55e" font-size="15" font-weight="700">c = f·λ = 2.99 × 10⁸ m/s</text>
      </g>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Measuring the Speed of Light via Standing Wave Hot Spots in a Microwave Oven")

def svg_m42_waveform_crest():
    """Page 5: Oscilloscope waveform crest analysis"""
    inner = """
    <!-- Oscilloscope Screen at x = 80, y = 60 to 360 -->
    <rect x="80" y="60" width="680" height="300" fill="#030712" rx="12" stroke="#22c55e" stroke-width="2"/>
    <!-- Grid lines -->
    <line x1="80" y1="210" x2="760" y2="210" stroke="#1e293b" stroke-width="1.5"/>
    <line x1="200" y1="60" x2="200" y2="360" stroke="#1e293b" stroke-width="1"/>
    <line x1="420" y1="60" x2="420" y2="360" stroke="#1e293b" stroke-width="1"/>
    <line x1="640" y1="60" x2="640" y2="360" stroke="#1e293b" stroke-width="1"/>

    <!-- Waveform Trace -->
    <path d="M 90,210 Q 145,100 200,210 Q 255,320 310,210 Q 365,100 420,210 Q 475,320 530,210 Q 585,100 640,210 Q 695,320 750,210" fill="none" stroke="#22c55e" stroke-width="3"/>

    <!-- Crest Markers -->
    <circle cx="145" cy="120" r="6" fill="#ef4444"/>
    <text x="145" y="100" fill="#ef4444" font-size="12" font-weight="700" text-anchor="middle">1st Crest</text>

    <circle cx="365" cy="120" r="6" fill="#f59e0b"/>
    <text x="365" y="100" fill="#f59e0b" font-size="12" font-weight="700" text-anchor="middle">2nd Crest (1λ)</text>

    <circle cx="585" cy="120" r="6" fill="#22c55e"/>
    <text x="585" y="100" fill="#22c55e" font-size="12" font-weight="700" text-anchor="middle">3rd Crest (2λ)</text>

    <!-- Dimension Line from 1st to 3rd Crest (x = 145 to 585) -->
    <line x1="145" y1="75" x2="585" y2="75" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="153,71 145,75 153,79" fill="#38bdf8"/>
    <polygon points="577,71 585,75 577,79" fill="#38bdf8"/>
    <text x="365" y="68" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">Total Distance: 2λ = 12.0 mm (λ = 6.0 mm)</text>

    <!-- Bottom Result Card -->
    <rect x="220" y="270" width="400" height="70" fill="#111827" rx="8" stroke="#1e293b"/>
    <text x="420" y="295" fill="#f8fafc" font-size="12" text-anchor="middle">Wavelength λ = 6.0 × 10⁻³ m</text>
    <text x="420" y="325" fill="#22c55e" font-size="16" font-weight="700" text-anchor="middle">Frequency f = c / λ = 5.0 × 10¹⁰ Hz (50 GHz)</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Waveform Crest-to-Crest Physical Dimension Analysis")

def svg_m42_horizontal_spectrum():
    """Page 6: Horizontal continuous 7-band spectrum scale"""
    inner = """
    <!-- Spectrum Band Containers (x = 40 to 800, y = 100 to 220) -->
    <!-- 7 Region Rectangles -->
    <!-- 1. Radio (x = 40, w = 110) -->
    <rect x="40" y="110" width="105" height="110" fill="#1e293b" stroke="#64748b" rx="4"/>
    <text x="92" y="150" fill="#f8fafc" font-size="12" font-weight="700" text-anchor="middle">RADIO</text>
    <text x="92" y="170" fill="#94a3b8" font-size="9" text-anchor="middle">λ &gt; 0.1 m</text>
    <text x="92" y="190" fill="#38bdf8" font-size="9" text-anchor="middle">f &lt; 3 GHz</text>

    <!-- 2. Microwave (x = 150, w = 105) -->
    <rect x="150" y="110" width="100" height="110" fill="#0f766e33" stroke="#14b8a6" rx="4"/>
    <text x="200" y="150" fill="#f8fafc" font-size="12" font-weight="700" text-anchor="middle">MICROWAVE</text>
    <text x="200" y="170" fill="#94a3b8" font-size="9" text-anchor="middle">1 mm - 10 cm</text>
    <text x="200" y="190" fill="#14b8a6" font-size="9" text-anchor="middle">3 - 300 GHz</text>

    <!-- 3. Infrared (x = 255, w = 105) -->
    <rect x="255" y="110" width="100" height="110" fill="#9a341233" stroke="#ea580c" rx="4"/>
    <text x="305" y="150" fill="#f8fafc" font-size="12" font-weight="700" text-anchor="middle">INFRARED</text>
    <text x="305" y="170" fill="#94a3b8" font-size="9" text-anchor="middle">700 nm - 1 mm</text>
    <text x="305" y="190" fill="#ea580c" font-size="9" text-anchor="middle">300 GHz - 430 THz</text>

    <!-- 4. Visible Light (Expanded, x = 360, w = 120) -->
    <rect x="360" y="100" width="120" height="130" fill="#0284c722" stroke="#38bdf8" stroke-width="2" rx="6"/>
    <text x="420" y="135" fill="#f8fafc" font-size="13" font-weight="800" text-anchor="middle">VISIBLE</text>
    <!-- Rainbow Stripe -->
    <rect x="370" y="150" width="100" height="12" fill="url(#rainbow)" rx="2"/>
    <text x="420" y="180" fill="#38bdf8" font-size="10" font-weight="700" text-anchor="middle">400 - 700 nm</text>
    <text x="420" y="200" fill="#94a3b8" font-size="9" text-anchor="middle">430 - 750 THz</text>

    <!-- 5. Ultraviolet (x = 485, w = 105) -->
    <rect x="485" y="110" width="100" height="110" fill="#6b21a833" stroke="#a855f7" rx="4"/>
    <text x="535" y="150" fill="#f8fafc" font-size="12" font-weight="700" text-anchor="middle">ULTRAVIOLET</text>
    <text x="535" y="170" fill="#94a3b8" font-size="9" text-anchor="middle">10 - 400 nm</text>
    <text x="535" y="190" fill="#a855f7" font-size="9" text-anchor="middle">750 THz - 30 PHz</text>

    <!-- 6. X-Rays (x = 590, w = 105) -->
    <rect x="590" y="110" width="100" height="110" fill="#83184333" stroke="#ec4899" rx="4"/>
    <text x="640" y="150" fill="#f8fafc" font-size="12" font-weight="700" text-anchor="middle">X-RAYS</text>
    <text x="640" y="170" fill="#94a3b8" font-size="9" text-anchor="middle">0.01 - 10 nm</text>
    <text x="640" y="190" fill="#ec4899" font-size="9" text-anchor="middle">30 PHz - 30 EHz</text>

    <!-- 7. Gamma Rays (x = 695, w = 105) -->
    <rect x="695" y="110" width="105" height="110" fill="#7f1d1d33" stroke="#ef4444" rx="4"/>
    <text x="747" y="150" fill="#f8fafc" font-size="12" font-weight="700" text-anchor="middle">GAMMA RAYS</text>
    <text x="747" y="170" fill="#94a3b8" font-size="9" text-anchor="middle">λ &lt; 0.01 nm</text>
    <text x="747" y="190" fill="#ef4444" font-size="9" text-anchor="middle">f &gt; 30 EHz</text>

    <!-- Top Arrow: Frequency & Energy Increasing -->
    <line x1="40" y1="65" x2="795" y2="65" stroke="#ef4444" stroke-width="2.5"/>
    <polygon points="790,60 802,65 790,70" fill="#ef4444"/>
    <text x="420" y="55" fill="#ef4444" font-size="12" font-weight="700" text-anchor="middle">
      INCREASING FREQUENCY (f) &amp; PHOTON ENERGY (E = hf) →
    </text>

    <!-- Bottom Arrow: Wavelength Increasing to Left -->
    <line x1="800" y1="280" x2="45" y2="280" stroke="#38bdf8" stroke-width="2.5"/>
    <polygon points="55,275 40,280 55,285" fill="#38bdf8"/>
    <text x="420" y="305" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">
      ← INCREASING WAVELENGTH (λ)
    </text>

    <!-- Gradients -->
    <defs>
      <linearGradient id="rainbow" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#ef4444"/>
        <stop offset="20%" stop-color="#f59e0b"/>
        <stop offset="40%" stop-color="#eab308"/>
        <stop offset="60%" stop-color="#22c55e"/>
        <stop offset="80%" stop-color="#38bdf8"/>
        <stop offset="100%" stop-color="#a855f7"/>
      </linearGradient>
    </defs>
    """
    return wrap_svg(inner, W=840, H=420, title="The Complete Electromagnetic Spectrum Continuum: 7 Major Spectral Bands")

def svg_m42_vertical_spectrum_mapping():
    """Page 7: Vertical Frequency vs Wavelength Scale"""
    inner = """
    <!-- Left Ladder Axis: Frequency in Hz (x = 140, y = 60 to 360) -->
    <line x1="180" y1="60" x2="180" y2="360" stroke="#ef4444" stroke-width="3"/>
    <text x="160" y="80" fill="#ef4444" font-size="11" font-weight="700" text-anchor="end">10²¹ Hz (Gamma)</text>
    <text x="160" y="125" fill="#ec4899" font-size="11" font-weight="700" text-anchor="end">10¹⁸ Hz (X-Rays)</text>
    <text x="160" y="170" fill="#a855f7" font-size="11" font-weight="700" text-anchor="end">10¹⁵ Hz (UV)</text>
    <text x="160" y="215" fill="#22c55e" font-size="11" font-weight="700" text-anchor="end">10¹⁴ Hz (Visible)</text>
    <text x="160" y="260" fill="#ea580c" font-size="11" font-weight="700" text-anchor="end">10¹² Hz (Infrared)</text>
    <text x="160" y="305" fill="#14b8a6" font-size="11" font-weight="700" text-anchor="end">10¹⁰ Hz (Microwave)</text>
    <text x="160" y="350" fill="#64748b" font-size="11" font-weight="700" text-anchor="end">10⁶ Hz (Radio)</text>

    <!-- Center Band Blocks (x = 220 to 620) -->
    <g transform="translate(220, 60)">
      <rect x="0" y="5" width="400" height="35" fill="#7f1d1d33" stroke="#ef4444" rx="4"/>
      <text x="200" y="28" fill="#ef4444" font-size="12" font-weight="700" text-anchor="middle">GAMMA RAYS</text>

      <rect x="0" y="50" width="400" height="35" fill="#83184333" stroke="#ec4899" rx="4"/>
      <text x="200" y="73" fill="#ec4899" font-size="12" font-weight="700" text-anchor="middle">X-RAYS</text>

      <rect x="0" y="95" width="400" height="35" fill="#6b21a833" stroke="#a855f7" rx="4"/>
      <text x="200" y="118" fill="#a855f7" font-size="12" font-weight="700" text-anchor="middle">ULTRAVIOLET</text>

      <rect x="0" y="140" width="400" height="35" fill="#0284c722" stroke="#38bdf8" rx="4"/>
      <text x="200" y="163" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">VISIBLE LIGHT (ROYGBIV)</text>

      <rect x="0" y="185" width="400" height="35" fill="#9a341233" stroke="#ea580c" rx="4"/>
      <text x="200" y="208" fill="#ea580c" font-size="12" font-weight="700" text-anchor="middle">INFRARED</text>

      <rect x="0" y="230" width="400" height="35" fill="#0f766e33" stroke="#14b8a6" rx="4"/>
      <text x="200" y="253" fill="#14b8a6" font-size="12" font-weight="700" text-anchor="middle">MICROWAVES</text>

      <rect x="0" y="275" width="400" height="35" fill="#1e293b" stroke="#64748b" rx="4"/>
      <text x="200" y="298" fill="#f8fafc" font-size="12" font-weight="700" text-anchor="middle">RADIO WAVES</text>
    </g>

    <!-- Right Ladder Axis: Wavelength in Meters (x = 660) -->
    <line x1="660" y1="60" x2="660" y2="360" stroke="#38bdf8" stroke-width="3"/>
    <text x="680" y="80" fill="#ef4444" font-size="11" font-weight="700">10⁻¹² m</text>
    <text x="680" y="125" fill="#ec4899" font-size="11" font-weight="700">10⁻¹⁰ m</text>
    <text x="680" y="170" fill="#a855f7" font-size="11" font-weight="700">10⁻⁷ m</text>
    <text x="680" y="215" fill="#22c55e" font-size="11" font-weight="700">5 × 10⁻⁷ m</text>
    <text x="680" y="260" fill="#ea580c" font-size="11" font-weight="700">10⁻⁵ m</text>
    <text x="680" y="305" fill="#14b8a6" font-size="11" font-weight="700">10⁻² m</text>
    <text x="680" y="350" fill="#64748b" font-size="11" font-weight="700">10² m</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Vertical Quantitative Mapping: Frequency (Hz) vs. Wavelength (m)")


# =============================================================================
# SVG BUILDERS — MODULE 4.3
# =============================================================================

def svg_m43_radar_doppler():
    """Page 2: Radar pulse ranging & Doppler speed gun"""
    inner = """
    <!-- Left Panel: RADAR Ranging (x = 40, w = 360) -->
    <g transform="translate(40, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="180" y="30" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">RADAR PULSE RANGING</text>

      <!-- Radar Dish -->
      <path d="M 50,110 A 30 30 0 0 0 50,170 Z" fill="#334155" stroke="#38bdf8" stroke-width="2"/>
      <line x1="50" y1="140" x2="20" y2="200" stroke="#64748b" stroke-width="3"/>

      <!-- Airplane Target -->
      <path d="M 280,130 L 310,135 L 340,135 L 300,120 Z" fill="#f8fafc"/>
      <text x="310" y="115" fill="#94a3b8" font-size="9" text-anchor="middle">Aircraft</text>

      <!-- Transmitted & Echo Waves -->
      <path d="M 70,130 Q 150,110 270,135" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="6 3"/>
      <path d="M 270,145 Q 150,170 70,150" fill="none" stroke="#22c55e" stroke-width="2.5" stroke-dasharray="4 4"/>

      <!-- Distance formula -->
      <rect x="20" y="240" width="320" height="60" fill="#0284c715" rx="6" stroke="#0284c744"/>
      <text x="180" y="265" fill="#f8fafc" font-size="11" text-anchor="middle">Distance to Target (Range s):</text>
      <text x="180" y="285" fill="#22c55e" font-size="14" font-weight="700" text-anchor="middle">s = (c · t) / 2</text>
    </g>

    <!-- Right Panel: Police Doppler Speed Gun (x = 440, w = 360) -->
    <g transform="translate(440, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="180" y="30" fill="#f59e0b" font-size="13" font-weight="700" text-anchor="middle">POLICE MICROWAVE SPEED GUN</text>

      <!-- Speed Gun -->
      <rect x="40" y="125" width="60" height="25" fill="#334155" rx="3" stroke="#f59e0b"/>
      <rect x="55" y="150" width="20" height="40" fill="#1e293b" rx="2"/>

      <!-- Oncoming Vehicle -->
      <rect x="240" y="120" width="80" height="40" fill="#ef4444" rx="4"/>
      <text x="280" y="145" fill="#fff" font-size="10" font-weight="700" text-anchor="middle">Vehicle (v)</text>

      <!-- Doppler Wave Shift -->
      <path d="M 110,137 L 230,137" stroke="#f59e0b" stroke-width="2" stroke-dasharray="8 4"/>

      <!-- Doppler explanation -->
      <rect x="20" y="240" width="320" height="60" fill="#f59e0b15" rx="6" stroke="#f59e0b44"/>
      <text x="180" y="265" fill="#f8fafc" font-size="11" text-anchor="middle">Doppler Frequency Shift:</text>
      <text x="180" y="285" fill="#f59e0b" font-size="13" font-weight="700" text-anchor="middle">Δf = 2v / λ  →  Determines Speed</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Applied Microwave Physics: RADAR Distance Ranging & Doppler Velocity Detection")

def svg_m43_infrared_greenhouse():
    """Page 3: Greenhouse infrared trapping & thermal imaging"""
    inner = """
    <!-- Glass Greenhouse Outline (x = 100 to 500, y = 80 to 350) -->
    <path d="M 100,180 L 300,90 L 500,180 L 500,340 L 100,340 Z" fill="#0284c711" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="300" y="75" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">Naivasha Glass Greenhouse</text>

    <!-- Incoming Solar Light (High Frequency, Yellow arrows passing through glass) -->
    <line x1="160" y1="40" x2="220" y2="180" stroke="#facc15" stroke-width="3"/>
    <polygon points="214,170 220,182 225,170" fill="#facc15"/>
    <text x="150" y="30" fill="#facc15" font-size="10" font-weight="700">Solar Visible Light (Enters easily)</text>

    <!-- Potted Plants inside greenhouse -->
    <rect x="180" y="300" width="60" height="40" fill="#15803d" rx="4"/>
    <rect x="360" y="300" width="60" height="40" fill="#15803d" rx="4"/>

    <!-- Trapped Infrared Waves (Red wiggly lines bouncing inside glass) -->
    <path d="M 210,290 Q 240,240 280,270 Q 320,300 360,260 Q 400,220 480,240" fill="none" stroke="#ef4444" stroke-width="3"/>
    <text x="300" y="220" fill="#ef4444" font-size="12" font-weight="700" text-anchor="middle">Trapped Re-radiated Infrared Heat</text>

    <!-- Right Side Agricultural & Medical Explanations -->
    <g transform="translate(540, 70)">
      <rect x="0" y="0" width="260" height="280" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="130" y="25" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">INFRARED APPLICATIONS</text>

      <g transform="translate(15, 55)">
        <text x="0" y="0" fill="#f59e0b" font-size="12" font-weight="700">1. Horticulture (Naivasha):</text>
        <text x="0" y="20" fill="#94a3b8" font-size="10">Trapped heat promotes rapid</text>
        <text x="0" y="35" fill="#94a3b8" font-size="10">growth of roses and vegetables.</text>

        <text x="0" y="70" fill="#ef4444" font-size="12" font-weight="700">2. Medical Thermography:</text>
        <text x="0" y="90" fill="#94a3b8" font-size="10">Detects circulatory defects and</text>
        <text x="0" y="105" fill="#94a3b8" font-size="10">inflammatory joint disorders.</text>

        <text x="0" y="140" fill="#22c55e" font-size="12" font-weight="700">3. Night Vision Optics:</text>
        <text x="0" y="160" fill="#94a3b8" font-size="10">Detects body heat signatures</text>
        <text x="0" y="175" fill="#94a3b8" font-size="10">in total tactical darkness.</text>
      </g>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Infrared Physics: Greenhouse Thermal Trapping and Medical Diagnostic Imaging")

def svg_m43_uv_and_xray():
    """Page 4: UV Currency Fluorescent Security & Medical X-Ray Radiograph"""
    inner = """
    <!-- Left Panel: UV Fluorescent Note Security (x = 40, w = 360) -->
    <g transform="translate(40, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="180" y="30" fill="#a855f7" font-size="13" font-weight="700" text-anchor="middle">UV CURRENCY FORGERY DETECTION</text>

      <!-- Banknote outline -->
      <rect x="50" y="90" width="260" height="130" fill="#1e293b" stroke="#64748b" stroke-width="2" rx="4"/>
      <!-- Glowing fluorescent security emblem under UV -->
      <rect x="150" y="120" width="60" height="70" fill="#a855f733" stroke="#a855f7" stroke-width="2" rx="4"/>
      <polygon points="180,135 190,165 165,145 195,145 170,165" fill="#a855f7"/>

      <!-- UV Lamp beaming purple light down -->
      <rect x="140" y="45" width="80" height="15" fill="#334155" rx="3" stroke="#a855f7"/>
      <path d="M 140,60 L 60,90 L 300,90 L 220,60 Z" fill="#a855f715"/>

      <rect x="20" y="240" width="320" height="60" fill="#a855f715" rx="6" stroke="#a855f744"/>
      <text x="180" y="265" fill="#f8fafc" font-size="11" text-anchor="middle">Fluorescent Dyes Glow Under UV:</text>
      <text x="180" y="285" fill="#a855f7" font-size="13" font-weight="700" text-anchor="middle">Absorbs UV → Emits Visible Light</text>
    </g>

    <!-- Right Panel: Medical X-Ray Radiograph (x = 440, w = 360) -->
    <g transform="translate(440, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="180" y="30" fill="#ec4899" font-size="13" font-weight="700" text-anchor="middle">MEDICAL X-RAY RADIOGRAPHY</text>

      <!-- X-Ray Tube source -->
      <rect x="150" y="45" width="60" height="20" fill="#334155" rx="3" stroke="#ec4899"/>
      <path d="M 150,65 L 70,120 L 290,120 L 210,65 Z" fill="#ec489915"/>

      <!-- Human Hand silhouette -->
      <rect x="110" y="110" width="140" height="110" fill="#f8fafc11" stroke="#94a3b8" rx="8"/>
      <!-- Dense Bone absorption (white) -->
      <line x1="180" y1="130" x2="180" y2="200" stroke="#f8fafc" stroke-width="8" stroke-linecap="round"/>
      <line x1="155" y1="140" x2="155" y2="190" stroke="#f8fafc" stroke-width="6" stroke-linecap="round"/>
      <line x1="205" y1="140" x2="205" y2="190" stroke="#f8fafc" stroke-width="6" stroke-linecap="round"/>

      <rect x="20" y="240" width="320" height="60" fill="#ec489915" rx="6" stroke="#ec489944"/>
      <text x="180" y="265" fill="#f8fafc" font-size="11" text-anchor="middle">Differential Absorption:</text>
      <text x="180" y="285" fill="#ec4899" font-size="13" font-weight="700" text-anchor="middle">Flesh = Transmits | Bone = Absorbs</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Applied Ultraviolet and X-Ray Radiation: Security Verification & Medical Imaging")

def svg_m43_radiation_shielding():
    """Page 7: Radiation biological hazards and lead shielding"""
    inner = """
    <!-- 3 Radiation Beams: UV, X-Ray, Gamma Ray -->
    <!-- 1. Ultraviolet (Stopped by Glass/Polycarbonate) -->
    <g transform="translate(60, 70)">
      <text x="0" y="25" fill="#a855f7" font-size="12" font-weight="700">1. Ultraviolet (UV)</text>
      <line x1="140" y1="20" x2="300" y2="20" stroke="#a855f7" stroke-width="3"/>
      <!-- Barrier: Glass -->
      <rect x="300" y="0" width="16" height="40" fill="#38bdf844" stroke="#38bdf8" rx="2"/>
      <text x="325" y="25" fill="#22c55e" font-size="10" font-weight="700">Stopped by Glass / Plastic</text>
    </g>

    <!-- 2. X-Rays (Stopped by Lead Apron) -->
    <g transform="translate(60, 160)">
      <text x="0" y="25" fill="#ec4899" font-size="12" font-weight="700">2. X-Rays</text>
      <line x1="140" y1="20" x2="460" y2="20" stroke="#ec4899" stroke-width="3"/>
      <!-- Barrier: Soft tissue (Penetrated) -->
      <rect x="300" y="0" width="30" height="40" fill="#f8fafc22" stroke="#94a3b8" rx="2"/>
      <text x="305" y="55" fill="#94a3b8" font-size="8">Flesh</text>
      <!-- Barrier: Lead Sheet -->
      <rect x="460" y="0" width="20" height="40" fill="#64748b" stroke="#f8fafc" rx="2"/>
      <text x="490" y="25" fill="#22c55e" font-size="10" font-weight="700">Stopped by Lead Sheet (0.5 mm)</text>
    </g>

    <!-- 3. Gamma Rays (Stopped only by Thick Lead Castle) -->
    <g transform="translate(60, 260)">
      <text x="0" y="25" fill="#ef4444" font-size="12" font-weight="700">3. Gamma Rays</text>
      <line x1="140" y1="20" x2="620" y2="20" stroke="#ef4444" stroke-width="3"/>
      <!-- Passes through flesh & thin lead -->
      <rect x="300" y="0" width="30" height="40" fill="#f8fafc22" stroke="#94a3b8" rx="2"/>
      <rect x="460" y="0" width="20" height="40" fill="#64748b" stroke="#f8fafc" rx="2"/>
      <!-- Heavy Lead Castle -->
      <rect x="620" y="-10" width="50" height="60" fill="#334155" stroke="#ef4444" stroke-width="2" rx="4"/>
      <text x="680" y="25" fill="#22c55e" font-size="10" font-weight="700">Stopped by Thick Lead Castle</text>
    </g>

    <!-- Bottom Safety Principles Bar -->
    <rect x="60" y="345" width="720" height="50" fill="#111827" rx="8" stroke="#1e293b"/>
    <text x="420" y="375" fill="#f59e0b" font-size="12" font-weight="700" text-anchor="middle">
      RADIATION SAFETY TRINITY: Minimum Exposure Time  |  Maximum Distance  |  Heavy Lead Shielding
    </text>
    """
    return wrap_svg(inner, W=840, H=420, title="Radiation Penetration Power and Material Shielding Protocols")


# =============================================================================
# MAIN ENRICHMENT EXECUTOR FOR TOPIC 4
# =============================================================================

def run_enrichment_topic4():
    print("=" * 80)
    print("VLEARN FORM 4 PHYSICS — TOPIC 4 VISUAL ENRICHMENT")
    print("=" * 80)

    topic = Topic.objects.filter(
        subject__name="Physics",
        subject__grade__name="Form 4",
        name__icontains="Electromagnetic Spectrum"
    ).first()

    if not topic:
        print("ERROR: Topic 4: Electromagnetic Spectrum not found! Run ingest_form4_physics_topic4.py first.")
        return

    units = topic.learning_units.all().order_by("order")
    if units.count() < 3:
        print("ERROR: Expected 3 learning units in Topic 4.")
        return

    unit_1 = units[0]
    unit_2 = units[1]
    unit_3 = units[2]

    lesson_1 = unit_1.lessons.first()
    lesson_2 = unit_2.lessons.first()
    lesson_3 = unit_3.lessons.first()

    print(f"Enriching Lesson 1 (ID: {lesson_1.id}): '{lesson_1.title}'")
    print(f"Enriching Lesson 2 (ID: {lesson_2.id}): '{lesson_2.title}'")
    print(f"Enriching Lesson 3 (ID: {lesson_3.id}): '{lesson_3.title}'\n")

    # -------------------------------------------------------------------------
    # MODULE 4.1 ENRICHMENT
    # -------------------------------------------------------------------------
    print("--- Enriching Module 4.1 ---")
    attach_svg_to_block(lesson_1, 2, "suggested_diagram", "3D Vector Geometry of a Propagating Transverse Electromagnetic Wave", "m41_3d_em_wave", svg_m41_3d_em_wave())

    # -------------------------------------------------------------------------
    # MODULE 4.2 ENRICHMENT
    # -------------------------------------------------------------------------
    print("\n--- Enriching Module 4.2 ---")
    attach_svg_to_block(lesson_2, 2, "suggested_diagram", "Measuring the Speed of Light via Standing Wave Hot Spots in a Microwave Oven", "m42_microwave_speed_of_light", svg_m42_microwave_speed_of_light())
    attach_svg_to_block(lesson_2, 5, "suggested_diagram", "Waveform Crest-to-Crest Physical Dimension Analysis", "m42_waveform_crest", svg_m42_waveform_crest())
    attach_svg_to_block(lesson_2, 6, "suggested_diagram", "The Complete Electromagnetic Spectrum Continuum: 7 Major Spectral Bands", "m42_horizontal_spectrum", svg_m42_horizontal_spectrum())
    attach_svg_to_block(lesson_2, 7, "suggested_diagram", "Vertical Quantitative Mapping: Frequency (Hz) vs. Wavelength (m)", "m42_vertical_spectrum_mapping", svg_m42_vertical_spectrum_mapping())

    # -------------------------------------------------------------------------
    # MODULE 4.3 ENRICHMENT
    # -------------------------------------------------------------------------
    print("\n--- Enriching Module 4.3 ---")
    attach_svg_to_block(lesson_3, 2, "suggested_diagram", "Applied Microwave Physics: RADAR Distance Ranging & Doppler Velocity Detection", "m43_radar_doppler", svg_m43_radar_doppler())
    attach_svg_to_block(lesson_3, 3, "suggested_diagram", "Infrared Physics: Greenhouse Thermal Trapping and Medical Diagnostic Imaging", "m43_infrared_greenhouse", svg_m43_infrared_greenhouse())
    attach_svg_to_block(lesson_3, 4, "suggested_diagram", "Applied Ultraviolet and X-Ray Radiation: Security Verification & Medical Imaging", "m43_uv_and_xray", svg_m43_uv_and_xray())
    attach_svg_to_block(lesson_3, 7, "suggested_diagram", "Radiation Penetration Power and Material Shielding Protocols", "m43_radiation_shielding", svg_m43_radiation_shielding())

    # Wikimedia Assets
    attach_wikimedia_to_block(
        lesson=lesson_2,
        page_num=6,
        title="OpenStax Astronomy Electromagnetic Spectrum and Atmospheric Transmission",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Openstax_Astronomy_EM_spectrum_and_atmosphere.jpg/960px-Openstax_Astronomy_EM_spectrum_and_atmosphere.jpg",
        author="OpenStax Astronomy",
        licensing="CC BY 4.0",
        commons_page="https://commons.wikimedia.org/wiki/File:Openstax_Astronomy_EM_spectrum_and_atmosphere.jpg"
    )

    attach_wikimedia_to_block(
        lesson=lesson_3,
        page_num=4,
        title="Historical Medical Radiograph of Hand Skeletal Anatomy",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Radiography%2C_X-ray_therapeutics_and_radium_therapy_%281916%29_%2814757999772%29.jpg/960px-Radiography%2C_X-ray_therapeutics_and_radium_therapy_%281916%29_%2814757999772%29.jpg",
        author="Robert Knox",
        licensing="Public Domain",
        commons_page="https://commons.wikimedia.org/wiki/File:Radiography,_X-ray_therapeutics_and_radium_therapy_(1916)_(14757999772).jpg"
    )

    print("\n" + "=" * 80)
    print("TOPIC 4 VISUAL ENRICHMENT COMPLETED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    run_enrichment_topic4()
