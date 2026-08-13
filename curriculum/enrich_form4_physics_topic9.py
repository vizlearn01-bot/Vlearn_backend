"""
VLearn Form 4 Physics — Topic 9: Photoelectric Effect
Visual Enrichment Engine (Enhanced High-Contrast SVGs + Wikimedia Commons)

Enriches Topic 9 (Photoelectric Effect) with:
  - 12 high-precision, high-contrast dark-mode vector SVG diagrams
  - 3 authentic Wikimedia Commons photographic assets

Usage:
  /home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/venv/bin/python curriculum/enrich_form4_physics_topic9.py
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
# ENHANCED SVG BUILDERS — MODULE 9.1
# =============================================================================

def svg_m91_photoelectric_circuit():
    """Page 2: Phototube experimental circuit setup"""
    inner = """
    <!-- Glass Evacuated Phototube Envelope (x = 100 to 500) -->
    <rect x="120" y="100" width="380" height="180" fill="#111827" rx="90" stroke="#38bdf8" stroke-width="3"/>
    <text x="310" y="80" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">Evacuated Quartz Envelope</text>

    <!-- Curved Emitter Cathode (x = 160) -->
    <path d="M 170,130 Q 140,190 170,250" fill="none" stroke="#ef4444" stroke-width="6"/>
    <rect x="90" y="260" width="100" height="24" fill="#ef444420" rx="4" stroke="#ef4444"/>
    <text x="140" y="276" fill="#ef4444" font-size="11" font-weight="800" text-anchor="middle">Emitter Cathode (C)</text>

    <!-- Incident Light Photons (Purple Wavy Lines) -->
    <path d="M 60,110 L 160,160 M 70,130 L 160,190 M 80,150 L 160,220" stroke="#a855f7" stroke-width="4"/>
    <text x="70" y="95" fill="#a855f7" font-size="13" font-weight="800">Incident Monochromatic Light (hf)</text>

    <!-- Collector Anode Wire (x = 440) -->
    <line x1="440" y1="140" x2="440" y2="240" stroke="#22c55e" stroke-width="6"/>
    <rect x="390" y="260" width="100" height="24" fill="#22c55e20" rx="4" stroke="#22c55e"/>
    <text x="440" y="276" fill="#22c55e" font-size="11" font-weight="800" text-anchor="middle">Collector Anode (A)</text>

    <!-- Flying Photoelectrons (Cyan Dots) -->
    <circle cx="230" cy="170" r="5" fill="#38bdf8"/>
    <circle cx="290" cy="190" r="5" fill="#38bdf8"/>
    <circle cx="360" cy="180" r="5" fill="#38bdf8"/>
    <line x1="170" y1="190" x2="430" y2="190" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6 3"/>

    <!-- External Measuring Circuit (Bottom) -->
    <rect x="580" y="100" width="220" height="240" fill="#1e293b" rx="12" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="690" cy="160" r="30" fill="#030712" stroke="#22c55e" stroke-width="2"/>
    <text x="690" y="165" fill="#22c55e" font-size="16" font-weight="800" text-anchor="middle">μA</text>

    <rect x="610" y="230" width="160" height="40" fill="#030712" rx="6" stroke="#f59e0b"/>
    <text x="690" y="255" fill="#f59e0b" font-size="13" font-weight="800" text-anchor="middle">Variable DC Source (V)</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Photoelectric Effect Experimental Phototube Circuit Setup with Variable Voltage and Microammeter")

def svg_m91_wave_vs_quantum():
    """Page 3: Classical wave theory vs Einstein quantum theory comparison"""
    inner = """
    <!-- Left Panel: Classical Wave Theory (Failures) (x = 40, w = 360) -->
    <g transform="translate(40, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="12" stroke="#ef4444" stroke-width="2"/>
      <text x="180" y="32" fill="#ef4444" font-size="14" font-weight="800" text-anchor="middle">CLASSICAL WAVE THEORY (FAILS)</text>

      <rect x="20" y="65" width="320" height="60" fill="#ef444415" rx="6" stroke="#ef4444"/>
      <text x="180" y="88" fill="#f8fafc" font-size="12" font-weight="700" text-anchor="middle">1. Predicts time delay for low intensity</text>
      <text x="180" y="108" fill="#cbd5e1" font-size="11" text-anchor="middle">Reality: Instantaneous emission (&lt; 10⁻⁹ s)</text>

      <rect x="20" y="145" width="320" height="60" fill="#ef444415" rx="6" stroke="#ef4444"/>
      <text x="180" y="168" fill="#f8fafc" font-size="12" font-weight="700" text-anchor="middle">2. Predicts K_max depends on Intensity</text>
      <text x="180" y="188" fill="#cbd5e1" font-size="11" text-anchor="middle">Reality: K_max depends ONLY on Frequency f</text>

      <rect x="20" y="225" width="320" height="60" fill="#ef444415" rx="6" stroke="#ef4444"/>
      <text x="180" y="248" fill="#f8fafc" font-size="12" font-weight="700" text-anchor="middle">3. Predicts any frequency causes emission</text>
      <text x="180" y="268" fill="#cbd5e1" font-size="11" text-anchor="middle">Reality: Zero emission if f &lt; f_0</text>
    </g>

    <!-- Right Panel: Einstein Quantum Photon Theory (x = 440, w = 360) -->
    <g transform="translate(440, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="12" stroke="#22c55e" stroke-width="2"/>
      <text x="180" y="32" fill="#22c55e" font-size="14" font-weight="800" text-anchor="middle">QUANTUM PHOTON THEORY (SUCCESS)</text>

      <rect x="20" y="65" width="320" height="60" fill="#22c55e15" rx="6" stroke="#22c55e"/>
      <text x="180" y="88" fill="#f8fafc" font-size="12" font-weight="700" text-anchor="middle">1. Photons act as concentrated energy quanta</text>
      <text x="180" y="108" fill="#cbd5e1" font-size="11" text-anchor="middle">E = h f photon energy transfer is 1-to-1</text>

      <rect x="20" y="145" width="320" height="60" fill="#22c55e15" rx="6" stroke="#22c55e"/>
      <text x="180" y="168" fill="#f8fafc" font-size="12" font-weight="700" text-anchor="middle">2. K_max = h f - Φ</text>
      <text x="180" y="188" fill="#cbd5e1" font-size="11" text-anchor="middle">Linear dependence on frequency f</text>

      <rect x="20" y="225" width="320" height="60" fill="#22c55e15" rx="6" stroke="#22c55e"/>
      <text x="180" y="248" fill="#f8fafc" font-size="12" font-weight="700" text-anchor="middle">3. Threshold Frequency f_0</text>
      <text x="180" y="268" fill="#cbd5e1" font-size="11" text-anchor="middle">Minimum photon energy needed: h f_0 = Φ</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Classical Wave Theory Predictions vs. Einstein Quantum Photon Theory Reality Comparison")

def svg_m91_work_function_potentials():
    """Page 4: Energy partition diagram (Work function vs Kinetic energy)"""
    inner = """
    <!-- Incident Photon (Top Left) -->
    <path d="M 60,80 Q 160,60 260,120" fill="none" stroke="#a855f7" stroke-width="5"/>
    <polygon points="260,120 245,110 248,128" fill="#a855f7"/>
    <rect x="60" y="135" width="180" height="35" fill="#a855f720" rx="6" stroke="#a855f7"/>
    <text x="150" y="157" fill="#a855f7" font-size="14" font-weight="800" text-anchor="middle">Incident Photon (E = h f)</text>

    <!-- Metal Surface Barrier Block (Center) -->
    <rect x="300" y="100" width="240" height="240" fill="#1e293b" rx="12" stroke="#f59e0b" stroke-width="3"/>
    <text x="420" y="130" fill="#f59e0b" font-size="15" font-weight="800" text-anchor="middle">Metal Surface Lattice</text>

    <rect x="320" y="150" width="200" height="70" fill="#f59e0b20" rx="6" stroke="#f59e0b"/>
    <text x="420" y="175" fill="#f59e0b" font-size="14" font-weight="800" text-anchor="middle">Work Function (Φ = h f_0)</text>
    <text x="420" y="198" fill="#cbd5e1" font-size="11" text-anchor="middle">Energy to escape metal binding</text>

    <!-- Emitted Photoelectron (Right) -->
    <line x1="540" y1="220" x2="740" y2="220" stroke="#38bdf8" stroke-width="5"/>
    <circle cx="740" cy="220" r="14" fill="#38bdf8" stroke="#fff" stroke-width="2"/>
    <text x="740" y="225" fill="#000" font-size="11" font-weight="800" text-anchor="middle">e⁻</text>

    <rect x="580" y="250" width="220" height="45" fill="#38bdf820" rx="6" stroke="#38bdf8"/>
    <text x="690" y="277" fill="#38bdf8" font-size="14" font-weight="800" text-anchor="middle">K_max = e V_s = h f - Φ</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Photoelectric Energy Partition: Incident Photon Energy (E = hf) vs. Metal Work Function (Φ) + Max KE")

def svg_m91_stopping_potential_iv():
    """Page 6: Photoelectric current vs voltage I-V graph"""
    inner = """
    <rect x="100" y="60" width="660" height="260" fill="#030712" rx="10" stroke="#38bdf8" stroke-width="2"/>
    <line x1="100" y1="220" x2="760" y2="220" stroke="#94a3b8" stroke-width="2"/>
    <line x1="280" y1="60" x2="280" y2="280" stroke="#94a3b8" stroke-width="2"/>

    <line x1="160" y1="60" x2="160" y2="280" stroke="#ef4444" stroke-width="3" stroke-dasharray="6 3"/>
    <text x="160" y="305" fill="#ef4444" font-size="14" font-weight="800" text-anchor="middle">-V_s (Stopping Potential)</text>

    <path d="M 160,220 Q 240,220 280,140 T 720,130" fill="none" stroke="#22c55e" stroke-width="4"/>
    <text x="600" y="115" fill="#22c55e" font-size="13" font-weight="800">High Intensity (I_2)</text>

    <path d="M 160,220 Q 240,220 280,180 T 720,175" fill="none" stroke="#38bdf8" stroke-width="4"/>
    <text x="600" y="165" fill="#38bdf8" font-size="13" font-weight="800">Low Intensity (I_1)</text>

    <text x="520" y="355" fill="#f8fafc" font-size="14" font-weight="800" text-anchor="middle">Collector Voltage V (Volts) →</text>
    <text x="45" y="170" fill="#f8fafc" font-size="14" font-weight="800" text-anchor="middle" transform="rotate(-90 45 170)">Photoelectric Current I (μA) →</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Photoelectric Current vs. Voltage Characteristic Curve Showing Stopping Potential (-V_s) and Saturation Current")

def svg_m91_photoelectric_sandbox():
    """Page 8: Interactive Photoelectric sandbox diagram model"""
    inner = """
    <rect x="80" y="80" width="400" height="280" fill="#111827" rx="12" stroke="#38bdf8" stroke-width="3"/>

    <path d="M 100,100 L 180,180" stroke="#a855f7" stroke-width="4"/>
    <rect x="180" y="140" width="15" height="100" fill="#ef4444" rx="2"/>

    <line x1="195" y1="190" x2="380" y2="190" stroke="#38bdf8" stroke-width="4" stroke-dasharray="6 3"/>

    <g transform="translate(520, 60)">
      <rect x="0" y="0" width="280" height="320" fill="#111827" rx="10" stroke="#38bdf8" stroke-width="2"/>
      <text x="140" y="25" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">INTERACTIVE QUANTUM SLIDERS</text>

      <text x="15" y="60" fill="#cbd5e1" font-size="11">Wavelength λ (200nm - 700nm):</text>
      <rect x="15" y="70" width="250" height="10" fill="#1e293b" rx="4"/>
      <circle cx="110" cy="75" r="7" fill="#a855f7"/>

      <text x="15" y="130" fill="#cbd5e1" font-size="11">Light Flux Intensity (10% - 100%):</text>
      <rect x="15" y="140" width="250" height="10" fill="#1e293b" rx="4"/>
      <circle cx="160" cy="145" r="7" fill="#22c55e"/>

      <rect x="15" y="190" width="250" height="40" fill="#22c55e15" rx="6" stroke="#22c55e"/>
      <text x="140" y="215" fill="#22c55e" font-size="12" font-weight="800" text-anchor="middle">E = 4.13 eV (Photoelectrons Emitted!)</text>

      <rect x="15" y="250" width="250" height="40" fill="#38bdf815" rx="6" stroke="#38bdf8"/>
      <text x="140" y="275" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">K_max = 1.87 eV | V_s = 1.87 V</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Interactive Photoelectric Sandbox: Real-Time Photon Energy, Work Function, and Stopping Potential Model")


# =============================================================================
# ENHANCED SVG BUILDERS — MODULE 9.2
# =============================================================================

def svg_m92_einstein_equation_flow():
    """Page 1: Einstein equation energy conservation flowchart"""
    inner = """
    <g transform="translate(60, 140)">
      <rect x="0" y="0" width="220" height="120" fill="#111827" rx="10" stroke="#a855f7" stroke-width="3"/>
      <text x="110" y="45" fill="#a855f7" font-size="15" font-weight="800" text-anchor="middle">Incident Photon</text>
      <text x="110" y="80" fill="#f8fafc" font-size="20" font-weight="800" text-anchor="middle">E = h f</text>
    </g>

    <text x="320" y="210" fill="#f8fafc" font-size="36" font-weight="800" text-anchor="middle">=</text>

    <g transform="translate(360, 140)">
      <rect x="0" y="0" width="200" height="120" fill="#111827" rx="10" stroke="#f59e0b" stroke-width="3"/>
      <text x="100" y="45" fill="#f59e0b" font-size="14" font-weight="800" text-anchor="middle">Work Function</text>
      <text x="100" y="80" fill="#f8fafc" font-size="20" font-weight="800" text-anchor="middle">Φ = h f_0</text>
    </g>

    <text x="590" y="210" fill="#f8fafc" font-size="36" font-weight="800" text-anchor="middle">+</text>

    <g transform="translate(620, 140)">
      <rect x="0" y="0" width="180" height="120" fill="#111827" rx="10" stroke="#38bdf8" stroke-width="3"/>
      <text x="90" y="45" fill="#38bdf8" font-size="14" font-weight="800" text-anchor="middle">Max Kinetic Energy</text>
      <text x="90" y="80" fill="#f8fafc" font-size="18" font-weight="800" text-anchor="middle">K_max = e V_s</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Einstein's Photoelectric Energy Conservation Equation Flowchart (hf = Φ + K_max)")

def svg_m92_millikan_graph():
    """Page 2: Millikan stopping potential vs frequency linear graph"""
    inner = """
    <rect x="100" y="60" width="660" height="260" fill="#030712" rx="10" stroke="#38bdf8" stroke-width="2"/>
    <line x1="100" y1="220" x2="760" y2="220" stroke="#94a3b8" stroke-width="2"/>
    <line x1="260" y1="60" x2="260" y2="280" stroke="#94a3b8" stroke-width="2"/>

    <line x1="260" y1="220" x2="700" y2="80" stroke="#22c55e" stroke-width="5"/>
    <line x1="260" y1="220" x2="160" y2="252" stroke="#22c55e" stroke-width="3" stroke-dasharray="4 4"/>

    <circle cx="260" cy="220" r="7" fill="#ef4444"/>
    <text x="260" y="245" fill="#ef4444" font-size="14" font-weight="800" text-anchor="middle">f_0 (Threshold Frequency)</text>

    <rect x="420" y="90" width="240" height="50" fill="#22c55e15" rx="8" stroke="#22c55e"/>
    <text x="540" y="112" fill="#22c55e" font-size="14" font-weight="800" text-anchor="middle">Slope = h / e</text>
    <text x="540" y="130" fill="#cbd5e1" font-size="11" text-anchor="middle">Universal Planck constant determination</text>

    <text x="520" y="355" fill="#f8fafc" font-size="14" font-weight="800" text-anchor="middle">Light Frequency f (Hz) →</text>
    <text x="45" y="170" fill="#f8fafc" font-size="14" font-weight="800" text-anchor="middle" transform="rotate(-90 45 170)">Stopping Potential V_s (V) →</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Millikan's Experimental Stopping Potential V_s vs. Frequency f Linear Graph Determining Planck's Constant h")

def svg_m92_vacuum_phototube():
    """Page 4: Commercial vacuum phototube structure"""
    inner = """
    <rect x="180" y="80" width="480" height="260" fill="#111827" rx="130" stroke="#38bdf8" stroke-width="3"/>
    <text x="420" y="60" fill="#38bdf8" font-size="14" font-weight="800" text-anchor="middle">Evacuated Glass Envelope</text>

    <path d="M 280,120 Q 220,210 280,300" fill="none" stroke="#ef4444" stroke-width="8"/>
    <text x="220" y="215" fill="#ef4444" font-size="13" font-weight="800" text-anchor="middle">Alkali Emitter (C)</text>

    <line x1="520" y1="130" x2="520" y2="290" stroke="#22c55e" stroke-width="6"/>
    <text x="570" y="215" fill="#22c55e" font-size="13" font-weight="800" text-anchor="middle">Collector Wire (A)</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Commercial Vacuum Phototube Structural Anatomy and Photosensitive Cathode Emitter")

def svg_m92_solar_cell_pn_junction():
    """Page 6: Solar cell semiconductor P-N junction photo-conversion"""
    inner = """
    <g transform="translate(80, 80)">
      <rect x="0" y="0" width="680" height="80" fill="#0284c7" rx="6"/>
      <text x="340" y="45" fill="#fff" font-size="16" font-weight="800" text-anchor="middle">N-Type Silicon Layer (Thin Anti-Reflective Top)</text>

      <rect x="0" y="80" width="680" height="30" fill="#f59e0b" opacity="0.8"/>
      <text x="340" y="100" fill="#000" font-size="13" font-weight="800" text-anchor="middle">P-N Junction Depletion Region (Built-In Electric Field E)</text>

      <rect x="0" y="110" width="680" height="130" fill="#1e3a8a" rx="6"/>
      <text x="340" y="185" fill="#fff" font-size="16" font-weight="800" text-anchor="middle">P-Type Silicon Base Layer</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Solar Photovoltaic Cell P-N Junction Semiconductor Layer Photo-Conversion Mechanism")


# =============================================================================
# ENHANCED SVG BUILDERS — MODULE 9.3
# =============================================================================

def svg_m93_threshold_frequency_metal_chart():
    """Page 1: Comparative work function chart for metals"""
    inner = """
    <g transform="translate(100, 80)">
      <rect x="0" y="0" width="120" height="200" fill="#22c55e" rx="6"/>
      <text x="60" y="-15" fill="#22c55e" font-size="14" font-weight="800" text-anchor="middle">Potassium (K)</text>
      <text x="60" y="100" fill="#000" font-size="14" font-weight="800" text-anchor="middle">2.26 eV</text>

      <rect x="170" y="-10" width="120" height="210" fill="#38bdf8" rx="6"/>
      <text x="230" y="-25" fill="#38bdf8" font-size="14" font-weight="800" text-anchor="middle">Sodium (Na)</text>
      <text x="230" y="100" fill="#000" font-size="14" font-weight="800" text-anchor="middle">2.28 eV</text>

      <rect x="340" y="-190" width="120" height="390" fill="#f59e0b" rx="6"/>
      <text x="400" y="-205" fill="#f59e0b" font-size="14" font-weight="800" text-anchor="middle">Zinc (Zn)</text>
      <text x="400" y="100" fill="#000" font-size="14" font-weight="800" text-anchor="middle">4.31 eV</text>

      <rect x="510" y="-280" width="120" height="480" fill="#ef4444" rx="6"/>
      <text x="570" y="-295" fill="#ef4444" font-size="14" font-weight="800" text-anchor="middle">Platinum (Pt)</text>
      <text x="570" y="100" fill="#fff" font-size="14" font-weight="800" text-anchor="middle">5.65 eV</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Comparative Work Function (Φ) and Threshold Frequency (f_0) Metal Bar Chart")

def svg_m93_photon_energy_frequency_scale():
    """Page 2: Electromagnetic spectrum photon energy scale"""
    inner = """
    <rect x="80" y="140" width="680" height="60" fill="#1e293b" rx="8" stroke="#38bdf8" stroke-width="2"/>
    <text x="140" y="175" fill="#cbd5e1" font-size="13" font-weight="700">Radio</text>
    <text x="260" y="175" fill="#cbd5e1" font-size="13" font-weight="700">IR</text>
    <text x="380" y="175" fill="#22c55e" font-size="14" font-weight="800">Visible</text>
    <text x="500" y="175" fill="#a855f7" font-size="14" font-weight="800">UV</text>
    <text x="620" y="175" fill="#ef4444" font-size="14" font-weight="800">X-Ray / Gamma</text>

    <text x="420" y="240" fill="#f8fafc" font-size="15" font-weight="800" text-anchor="middle">Increasing Photon Energy (E = h f) →</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Electromagnetic Spectrum Photon Energy (E = hf) and Frequency Gradient Scale")

def svg_m93_photocell_light_meter_circuit():
    """Page 10: Automatic street light photocell relay circuit"""
    inner = """
    <g transform="translate(60, 60)">
      <rect x="0" y="0" width="340" height="320" fill="#111827" rx="12" stroke="#f59e0b" stroke-width="2"/>
      <text x="170" y="32" fill="#f59e0b" font-size="14" font-weight="800" text-anchor="middle">DAYTIME (LIGHT ON PHOTOCELL)</text>

      <rect x="40" y="80" width="260" height="80" fill="#22c55e15" rx="8" stroke="#22c55e"/>
      <text x="170" y="115" fill="#22c55e" font-size="14" font-weight="800" text-anchor="middle">Photocurrent Conducts</text>

      <text x="170" y="220" fill="#cbd5e1" font-size="13" text-anchor="middle">Electromagnet holds relay OPEN</text>
      <text x="170" y="250" fill="#ef4444" font-size="15" font-weight="800" text-anchor="middle">Street Light OFF</text>
    </g>

    <g transform="translate(440, 60)">
      <rect x="0" y="0" width="340" height="320" fill="#111827" rx="12" stroke="#38bdf8" stroke-width="2"/>
      <text x="170" y="32" fill="#38bdf8" font-size="14" font-weight="800" text-anchor="middle">NIGHTTIME (DARKNESS)</text>

      <rect x="40" y="80" width="260" height="80" fill="#ef444415" rx="8" stroke="#ef4444"/>
      <text x="170" y="115" fill="#ef4444" font-size="14" font-weight="800" text-anchor="middle">Zero Photocurrent</text>

      <text x="170" y="220" fill="#cbd5e1" font-size="13" text-anchor="middle">Spring closes relay contact</text>
      <text x="170" y="250" fill="#22c55e" font-size="15" font-weight="800" text-anchor="middle">Street Light ON</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Automatic Street Light Photocell Relay Control Circuit Architecture")


# =============================================================================
# MAIN ENRICHMENT EXECUTOR FOR TOPIC 9
# =============================================================================

def run_enrichment_topic9():
    print("=" * 80)
    print("VLEARN FORM 4 PHYSICS — TOPIC 9 VISUAL ENRICHMENT")
    print("=" * 80)

    topic = Topic.objects.filter(
        subject__name="Physics",
        subject__grade__name="Form 4",
        name__icontains="Photoelectric"
    ).first()

    if not topic:
        print("ERROR: Topic 9: Photoelectric Effect not found! Run ingest_form4_physics_topic9.py first.")
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

    # Module 9.1 SVGs
    print("--- Enriching Module 9.1 ---")
    attach_svg_to_block(lesson_1, 2, "suggested_diagram", "Photoelectric Effect Experimental Phototube Circuit Setup with Variable Voltage and Microammeter", "m91_photoelectric_circuit", svg_m91_photoelectric_circuit())
    attach_svg_to_block(lesson_1, 3, "suggested_diagram", "Classical Wave Theory Predictions vs. Einstein Quantum Photon Theory Reality Comparison", "m91_wave_vs_quantum", svg_m91_wave_vs_quantum())
    attach_svg_to_block(lesson_1, 4, "suggested_diagram", "Photoelectric Energy Partition: Incident Photon Energy (E = hf) vs. Metal Work Function (Φ) + Max KE", "m91_work_function_potentials", svg_m91_work_function_potentials())
    attach_svg_to_block(lesson_1, 6, "suggested_diagram", "Photoelectric Current vs. Voltage Characteristic Curve Showing Stopping Potential (-V_s) and Saturation Current", "m91_stopping_potential_iv", svg_m91_stopping_potential_iv())
    attach_svg_to_block(lesson_1, 8, "suggested_simulation", "Interactive Photoelectric Sandbox: Real-Time Photon Energy, Work Function, and Stopping Potential Model", "m91_photoelectric_sandbox", svg_m91_photoelectric_sandbox())

    # Module 9.2 SVGs
    print("\n--- Enriching Module 9.2 ---")
    attach_svg_to_block(lesson_2, 1, "suggested_diagram", "Einstein's Photoelectric Energy Conservation Equation Flowchart (hf = Φ + K_max)", "m92_einstein_equation_flow", svg_m92_einstein_equation_flow())
    attach_svg_to_block(lesson_2, 2, "suggested_diagram", "Millikan's Experimental Stopping Potential V_s vs. Frequency f Linear Graph Determining Planck's Constant h", "m92_millikan_graph", svg_m92_millikan_graph())
    attach_svg_to_block(lesson_2, 4, "suggested_diagram", "Commercial Vacuum Phototube Structural Anatomy and Photosensitive Cathode Emitter", "m92_vacuum_phototube", svg_m92_vacuum_phototube())
    attach_svg_to_block(lesson_2, 6, "suggested_diagram", "Solar Photovoltaic Cell P-N Junction Semiconductor Layer Photo-Conversion Mechanism", "m92_solar_cell_pn_junction", svg_m92_solar_cell_pn_junction())

    # Module 9.3 SVGs
    print("\n--- Enriching Module 9.3 ---")
    attach_svg_to_block(lesson_3, 1, "suggested_diagram", "Comparative Work Function (Φ) and Threshold Frequency (f_0) Metal Bar Chart", "m93_threshold_frequency_metal_chart", svg_m93_threshold_frequency_metal_chart())
    attach_svg_to_block(lesson_3, 2, "suggested_diagram", "Electromagnetic Spectrum Photon Energy (E = hf) and Frequency Gradient Scale", "m93_photon_energy_frequency_scale", svg_m93_photon_energy_frequency_scale())
    attach_svg_to_block(lesson_3, 10, "suggested_diagram", "Automatic Street Light Photocell Relay Control Circuit Architecture", "m93_photocell_light_meter_circuit", svg_m93_photocell_light_meter_circuit())

    # Wikimedia Assets
    attach_wikimedia_to_block(
        lesson=lesson_1,
        page_num=1,
        title="Historical Hertz and Lenard Photoelectric Velocity Apparatus (1912)",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Hertz_Apparatus_1887.png/960px-Hertz_Apparatus_1887.png",
        author="Heinrich Hertz",
        licensing="Public domain",
        commons_page="https://commons.wikimedia.org/wiki/File:Hertz_Apparatus_1887.png"
    )

    attach_wikimedia_to_block(
        lesson=lesson_2,
        page_num=4,
        title="Commercial 90CV Vacuum Phototube Hardware Unit",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/90CV_phototube.jpg/960px-90CV_phototube.jpg",
        author="Mullard",
        licensing="Public domain",
        commons_page="https://commons.wikimedia.org/wiki/File:90CV_phototube.jpg"
    )

    attach_wikimedia_to_block(
        lesson=lesson_2,
        page_num=6,
        title="Ground-Mounted Solar Photovoltaic Panel Array",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Solar_Panel_Array_at_Kearney_NE.jpg/960px-Solar_Panel_Array_at_Kearney_NE.jpg",
        author="Wikimedia Commons Contributor",
        licensing="CC BY-SA 4.0",
        commons_page="https://commons.wikimedia.org/wiki/File:Solar_Panel_Array_at_Kearney_NE.jpg"
    )

    print("\n" + "=" * 80)
    print("TOPIC 9 VISUAL ENRICHMENT COMPLETED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    run_enrichment_topic9()
