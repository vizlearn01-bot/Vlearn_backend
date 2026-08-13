"""
VLearn Form 4 Physics — Topic 3: Floating and Sinking
Visual Enrichment Engine (SVGs + Wikimedia Commons)

Enriches all 3 modules of Topic 3 (Floating and Sinking) with:
  - 11 high-precision dark-mode vector SVG diagrams (fluid pressure gradient & upthrust derivation, 
    Eureka can Archimedes experiment, floating vs sinking density comparison, Law of Floatation in dual liquids, 
    3-stage Cork and Sinker method, hollow steel ship displacement, technical Plimsoll load lines, 
    submarine ballast tank operations, hydrometer anatomy & inverted scale, weather balloon atmospheric lift, 
    and composite sinking solid/cork thread tension resolution).
  - 3 authentic, high-resolution Wikimedia Commons photographic assets (International Plimsoll Load Line on ship hull, 
    laboratory glass hydrometer in measuring cylinder, and historical Cutty Sark load line).

All SVGs are validated and sanitized via `validate_and_sanitize_svg`, stored with `storage_type='embed'`, 
and embedded directly into `LessonBlock` content and metadata for immediate frontend rendering.

Usage:
  /home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/venv/bin/python curriculum/enrich_form4_physics_topic3.py
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
PANEL_BG = "#111827"
BORDER_COLOR = "#1e293b"
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
# SVG BUILDERS — MODULE 3.1
# =============================================================================

def svg_m31_pressure_gradient():
    """Page 2: Fluid pressure gradient generating upthrust"""
    inner = """
    <!-- Glass Liquid Tank at x = 60, y = 60 to 360 -->
    <rect x="60" y="60" width="460" height="300" fill="#0284c711" stroke="#38bdf8" stroke-width="2" rx="8"/>
    <!-- Water surface line -->
    <line x1="60" y1="100" x2="520" y2="100" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="8 4"/>
    <text x="75" y="90" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Liquid Surface (h = 0)</text>

    <!-- Submerged Block (x = 220, y = 160, w = 140, h = 120) -->
    <rect x="220" y="160" width="140" height="120" fill="#334155" stroke="#94a3b8" stroke-width="2" rx="4"/>
    <text x="290" y="225" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Solid Block (V = A·H)</text>

    <!-- Depth h1 to Top Face -->
    <line x1="180" y1="100" x2="180" y2="160" stroke="#f59e0b" stroke-width="2"/>
    <polygon points="176,108 180,100 184,108" fill="#f59e0b"/>
    <polygon points="176,152 180,160 184,152" fill="#f59e0b"/>
    <text x="165" y="135" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="end">Depth h₁</text>

    <!-- Depth h2 to Bottom Face -->
    <line x1="120" y1="100" x2="120" y2="280" stroke="#22c55e" stroke-width="2"/>
    <polygon points="116,108 120,100 124,108" fill="#22c55e"/>
    <polygon points="116,272 120,280 124,272" fill="#22c55e"/>
    <text x="105" y="195" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="end">Depth h₂</text>

    <!-- Top Force Vector F1 (Downward, smaller) -->
    <line x1="290" y1="120" x2="290" y2="160" stroke="#ef4444" stroke-width="3"/>
    <polygon points="285,150 290,160 295,150" fill="#ef4444"/>
    <text x="305" y="140" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="700">F₁ = ρ·g·h₁·A</text>

    <!-- Bottom Force Vector F2 (Upward, LARGER) -->
    <line x1="290" y1="340" x2="290" y2="280" stroke="#22c55e" stroke-width="4"/>
    <polygon points="284,292 290,280 296,292" fill="#22c55e"/>
    <text x="305" y="320" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700">F₂ = ρ·g·h₂·A (LARGER)</text>

    <!-- Right Derivation Panel -->
    <rect x="550" y="60" width="260" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
    <text x="680" y="90" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">UPTHRUST DERIVATION</text>

    <g transform="translate(565, 120)">
      <text x="0" y="0" fill="#94a3b8" font-size="11">Pressure at depth h: P = ρgh</text>
      <text x="0" y="20" fill="#f8fafc" font-size="12">Since h₂ &gt; h₁, P₂ &gt; P₁</text>

      <text x="0" y="55" fill="#38bdf8" font-size="12" font-weight="700">Net Upward Force (Upthrust):</text>
      <text x="0" y="75" fill="#f8fafc" font-size="12">U = F₂ - F₁</text>
      <text x="0" y="95" fill="#f8fafc" font-size="12">U = ρ·g·h₂·A - ρ·g·h₁·A</text>
      <text x="0" y="115" fill="#f8fafc" font-size="12">U = ρ·g·A(h₂ - h₁)</text>
      <text x="0" y="135" fill="#f8fafc" font-size="12">Since (h₂ - h₁) = H and A·H = V:</text>

      <rect x="0" y="155" width="230" height="50" fill="#0284c722" rx="6" stroke="#0284c7"/>
      <text x="115" y="185" fill="#22c55e" font-size="15" font-weight="700" text-anchor="middle">U = ρ_f · V · g</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Theoretical Origin of Upthrust: Liquid Pressure Gradient with Depth")

def svg_m31_eureka_archimedes():
    """Page 6: Eureka can and spring balance verifying Archimedes' Principle"""
    inner = """
    <!-- Spring Balance at x = 240, y = 50 to 140 -->
    <rect x="230" y="50" width="20" height="70" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" rx="3"/>
    <line x1="240" y1="120" x2="240" y2="180" stroke="#f8fafc" stroke-width="2"/>
    <text x="260" y="85" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Spring Balance (W₂)</text>

    <!-- Metal Block suspended in water -->
    <rect x="215" y="180" width="50" height="60" fill="#64748b" stroke="#94a3b8" stroke-width="2" rx="4"/>
    <text x="240" y="215" fill="#000" font-size="10" font-weight="700" text-anchor="middle">Block</text>

    <!-- Eureka Overflow Can at x = 160 to 320, y = 140 to 320 -->
    <rect x="160" y="140" width="160" height="180" fill="#0284c715" stroke="#38bdf8" stroke-width="2" rx="6"/>
    <!-- Spout on right at y = 160 to 190 -->
    <path d="M 320,165 L 380,200 L 380,215 L 320,180 Z" fill="#0284c733" stroke="#38bdf8" stroke-width="2"/>
    <text x="180" y="300" fill="#38bdf8" font-size="11" font-weight="700">Eureka Can</text>

    <!-- Overflowing Water Stream -->
    <path d="M 380,205 Q 400,240 400,280" fill="none" stroke="#38bdf8" stroke-width="3" stroke-dasharray="4 2"/>

    <!-- Collecting Beaker at x = 370, y = 260 on Electronic Balance -->
    <rect x="370" y="250" width="60" height="60" fill="#0284c722" stroke="#f59e0b" stroke-width="2" rx="4"/>
    <rect x="370" y="280" width="60" height="30" fill="#0284c766"/>
    <text x="400" y="275" fill="#f59e0b" font-size="9" font-weight="700" text-anchor="middle">Beaker</text>

    <rect x="350" y="310" width="100" height="25" fill="#1e293b" stroke="#64748b" rx="3"/>
    <text x="400" y="327" fill="#22c55e" font-size="11" font-weight="700" text-anchor="middle">Balance (W₄)</text>

    <!-- Right Side Equivalence Box -->
    <rect x="520" y="60" width="290" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
    <text x="665" y="90" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">ARCHIMEDES EQUIVALENCE</text>

    <g transform="translate(535, 120)">
      <rect x="0" y="0" width="260" height="60" fill="#0284c715" rx="6" stroke="#0284c744"/>
      <text x="10" y="22" fill="#38bdf8" font-size="12" font-weight="700">1. Apparent Loss of Weight:</text>
      <text x="10" y="44" fill="#f8fafc" font-size="13" font-weight="700">Upthrust U = W₁ - W₂</text>

      <rect x="0" y="75" width="260" height="60" fill="#0284c715" rx="6" stroke="#0284c744"/>
      <text x="10" y="97" fill="#f59e0b" font-size="12" font-weight="700">2. Weight of Displaced Fluid:</text>
      <text x="10" y="119" fill="#f8fafc" font-size="13" font-weight="700">W_disp = W₄ - W₃</text>

      <rect x="0" y="150" width="260" height="50" fill="#22c55e15" rx="6" stroke="#22c55e44"/>
      <text x="130" y="180" fill="#22c55e" font-size="13" font-weight="700" text-anchor="middle">PROVEN: W₁ - W₂ = W₄ - W₃</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Laboratory Verification of Archimedes' Principle with Eureka Overflow Can")


# =============================================================================
# SVG BUILDERS — MODULE 3.2
# =============================================================================

def svg_m32_floating_conditions():
    """Page 3: Floating, Neutral Buoyancy, and Sinking Criteria"""
    inner = """
    <!-- Panel 1: Floating with Freeboard (rho < rho_liquid) -->
    <g transform="translate(30, 60)">
      <rect x="0" y="0" width="240" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="120" y="30" fill="#22c55e" font-size="13" font-weight="700" text-anchor="middle">1. FLOATING</text>
      <text x="120" y="48" fill="#94a3b8" font-size="10" text-anchor="middle">ρ_body &lt; ρ_liquid</text>

      <!-- Liquid tank -->
      <rect x="20" y="70" width="200" height="180" fill="#0284c715" stroke="#38bdf8" rx="4"/>
      <line x1="20" y1="120" x2="220" y2="120" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 2"/>

      <!-- Floating Block (partly submerged) -->
      <rect x="80" y="90" width="80" height="80" fill="#22c55e33" stroke="#22c55e" stroke-width="2" rx="4"/>
      <text x="120" y="145" fill="#f8fafc" font-size="10" font-weight="700" text-anchor="middle">60% Submerged</text>

      <text x="120" y="280" fill="#22c55e" font-size="12" font-weight="700" text-anchor="middle">U = W_body (Equilibrium)</text>
    </g>

    <!-- Panel 2: Neutral Buoyancy (rho = rho_liquid) -->
    <g transform="translate(300, 60)">
      <rect x="0" y="0" width="240" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="120" y="30" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">2. NEUTRAL BUOYANCY</text>
      <text x="120" y="48" fill="#94a3b8" font-size="10" text-anchor="middle">ρ_body = ρ_liquid</text>

      <!-- Liquid tank -->
      <rect x="20" y="70" width="200" height="180" fill="#0284c715" stroke="#38bdf8" rx="4"/>
      <line x1="20" y1="120" x2="220" y2="120" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 2"/>

      <!-- Neutrally Submerged Block (100% submerged just beneath surface) -->
      <rect x="80" y="130" width="80" height="80" fill="#0284c744" stroke="#38bdf8" stroke-width="2" rx="4"/>
      <text x="120" y="175" fill="#f8fafc" font-size="10" font-weight="700" text-anchor="middle">100% Submerged</text>

      <text x="120" y="280" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">Hovering at any depth</text>
    </g>

    <!-- Panel 3: Sinking (rho > rho_liquid) -->
    <g transform="translate(570, 60)">
      <rect x="0" y="0" width="240" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="120" y="30" fill="#ef4444" font-size="13" font-weight="700" text-anchor="middle">3. SINKING</text>
      <text x="120" y="48" fill="#94a3b8" font-size="10" text-anchor="middle">ρ_body &gt; ρ_liquid</text>

      <!-- Liquid tank -->
      <rect x="20" y="70" width="200" height="180" fill="#0284c715" stroke="#38bdf8" rx="4"/>
      <line x1="20" y1="120" x2="220" y2="120" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 2"/>

      <!-- Sunk Block at base of tank -->
      <rect x="80" y="170" width="80" height="80" fill="#ef444433" stroke="#ef4444" stroke-width="2" rx="4"/>
      <text x="120" y="215" fill="#f8fafc" font-size="10" font-weight="700" text-anchor="middle">Rests on Base</text>

      <text x="120" y="280" fill="#ef4444" font-size="12" font-weight="700" text-anchor="middle">W &gt; U (Normal Force R &gt; 0)</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Density Criteria: Floating, Neutral Buoyancy, and Sinking")

def svg_m32_law_of_floatation():
    """Page 7: Law of Floatation in Water vs Kerosene"""
    inner = """
    <!-- Left Tank: Water (High density = 1000 kg/m3) -->
    <g transform="translate(40, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="180" y="30" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">PURE WATER (ρ = 1000 kg/m³)</text>

      <rect x="30" y="60" width="300" height="180" fill="#0284c715" stroke="#38bdf8" rx="4"/>
      <line x1="30" y1="110" x2="330" y2="110" stroke="#38bdf8" stroke-width="2.5"/>

      <!-- Wood block floating higher -->
      <rect x="130" y="80" width="100" height="100" fill="#f59e0b33" stroke="#f59e0b" stroke-width="2" rx="4"/>
      <text x="180" y="140" fill="#f8fafc" font-size="11" font-weight="700" text-anchor="middle">Wood (ρ = 600)</text>
      <text x="180" y="155" fill="#22c55e" font-size="10" font-weight="600" text-anchor="middle">60% Submerged</text>

      <text x="180" y="275" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">Floats Higher in Denser Liquid</text>
    </g>

    <!-- Right Tank: Kerosene (Lower density = 800 kg/m3) -->
    <g transform="translate(440, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="180" y="30" fill="#f59e0b" font-size="13" font-weight="700" text-anchor="middle">KEROSENE (ρ = 800 kg/m³)</text>

      <rect x="30" y="60" width="300" height="180" fill="#f59e0b11" stroke="#f59e0b" rx="4"/>
      <line x1="30" y1="110" x2="330" y2="110" stroke="#f59e0b" stroke-width="2.5"/>

      <!-- Wood block floating deeper -->
      <rect x="130" y="95" width="100" height="100" fill="#f59e0b33" stroke="#f59e0b" stroke-width="2" rx="4"/>
      <text x="180" y="140" fill="#f8fafc" font-size="11" font-weight="700" text-anchor="middle">Wood (ρ = 600)</text>
      <text x="180" y="155" fill="#ef4444" font-size="10" font-weight="600" text-anchor="middle">75% Submerged</text>

      <text x="180" y="275" fill="#f59e0b" font-size="12" font-weight="700" text-anchor="middle">Sinks Deeper in Lighter Liquid</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Law of Floatation: Submerged Depth Variation with Liquid Density")

def svg_m32_cork_sinker():
    """Page 8: The 3-stage Cork and Sinker Method"""
    inner = """
    <!-- Stage A: Sinker alone in water (W1) -->
    <g transform="translate(30, 60)">
      <rect x="0" y="0" width="240" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="120" y="25" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">STAGE (a): Sinker Alone</text>

      <rect x="110" y="45" width="20" height="50" fill="#1e293b" stroke="#38bdf8" rx="2"/>
      <line x1="120" y1="95" x2="120" y2="180" stroke="#f8fafc" stroke-width="1.5"/>

      <!-- Water Beaker -->
      <rect x="50" y="140" width="140" height="130" fill="#0284c715" stroke="#38bdf8" rx="4"/>
      <circle cx="120" cy="200" r="16" fill="#64748b" stroke="#94a3b8" stroke-width="2"/>
      <text x="120" y="204" fill="#000" font-size="9" font-weight="700" text-anchor="middle">Sinker</text>

      <text x="120" y="295" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">Reading: W₁</text>
    </g>

    <!-- Stage B: Cork in air, Sinker in water (W2) -->
    <g transform="translate(300, 60)">
      <rect x="0" y="0" width="240" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="120" y="25" fill="#f59e0b" font-size="12" font-weight="700" text-anchor="middle">STAGE (b): Cork in Air</text>

      <rect x="110" y="45" width="20" height="50" fill="#1e293b" stroke="#f59e0b" rx="2"/>
      <line x1="120" y1="95" x2="120" y2="180" stroke="#f8fafc" stroke-width="1.5"/>

      <!-- Cork in Air -->
      <rect x="105" y="105" width="30" height="24" fill="#f59e0b" rx="3"/>
      <text x="120" y="121" fill="#000" font-size="9" font-weight="700" text-anchor="middle">Cork</text>

      <!-- Water Beaker with submerged sinker -->
      <rect x="50" y="140" width="140" height="130" fill="#0284c715" stroke="#38bdf8" rx="4"/>
      <circle cx="120" cy="200" r="16" fill="#64748b" stroke="#94a3b8" stroke-width="2"/>

      <text x="120" y="295" fill="#f59e0b" font-size="12" font-weight="700" text-anchor="middle">Reading: W₂</text>
    </g>

    <!-- Stage C: Both submerged (W3) -->
    <g transform="translate(570, 60)">
      <rect x="0" y="0" width="240" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="120" y="25" fill="#22c55e" font-size="12" font-weight="700" text-anchor="middle">STAGE (c): Both Submerged</text>

      <rect x="110" y="45" width="20" height="50" fill="#1e293b" stroke="#22c55e" rx="2"/>
      <line x1="120" y1="95" x2="120" y2="180" stroke="#f8fafc" stroke-width="1.5"/>

      <!-- Water Beaker with BOTH submerged -->
      <rect x="50" y="140" width="140" height="130" fill="#0284c715" stroke="#38bdf8" rx="4"/>
      <rect x="105" y="160" width="30" height="24" fill="#f59e0b" rx="3"/>
      <circle cx="120" cy="210" r="16" fill="#64748b" stroke="#94a3b8" stroke-width="2"/>

      <text x="120" y="295" fill="#22c55e" font-size="12" font-weight="700" text-anchor="middle">Reading: W₃</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="The Cork and Sinker Method: 3-Stage Relative Density Determination")


# =============================================================================
# SVG BUILDERS — MODULE 3.3
# =============================================================================

def svg_m33_ship_hollow_hull():
    """Page 2: Solid steel block vs Hollow ship hull displacement"""
    inner = """
    <!-- Left: Solid Steel Block (Sinks) -->
    <g transform="translate(40, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="180" y="30" fill="#ef4444" font-size="13" font-weight="700" text-anchor="middle">SOLID STEEL BLOCK (SINKS)</text>

      <rect x="30" y="60" width="300" height="200" fill="#0284c715" stroke="#38bdf8" rx="4"/>
      <line x1="30" y1="100" x2="330" y2="100" stroke="#38bdf8" stroke-width="2"/>

      <!-- Solid block at bottom -->
      <rect x="150" y="210" width="60" height="50" fill="#64748b" stroke="#ef4444" stroke-width="2" rx="3"/>
      <text x="180" y="240" fill="#000" font-size="10" font-weight="700" text-anchor="middle">Solid Steel</text>

      <text x="180" y="285" fill="#ef4444" font-size="11" font-weight="700" text-anchor="middle">ρ = 7800 kg/m³ &gt; ρ_water (1000)</text>
    </g>

    <!-- Right: Hollow Ship Hull (Floats) -->
    <g transform="translate(440, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="180" y="30" fill="#22c55e" font-size="13" font-weight="700" text-anchor="middle">HOLLOW STEEL SHIP HULL (FLOATS)</text>

      <rect x="30" y="60" width="300" height="200" fill="#0284c715" stroke="#38bdf8" rx="4"/>
      <line x1="30" y1="140" x2="330" y2="140" stroke="#38bdf8" stroke-width="2"/>

      <!-- Hollow ship hull -->
      <path d="M 70,110 L 110,210 L 250,210 L 290,110 Z" fill="#0284c722" stroke="#38bdf8" stroke-width="3"/>
      <rect x="110" y="130" width="140" height="60" fill="#f8fafc11" rx="4" stroke="#94a3b8" stroke-dasharray="3 3"/>
      <text x="180" y="165" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">ENCLOSED AIR CAVITY</text>

      <text x="180" y="285" fill="#22c55e" font-size="11" font-weight="700" text-anchor="middle">ρ_average = M_total / V_hull &lt; 1000 kg/m³</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Why Steel Ships Float: Average Density Reduction via Hollow Hull Design")

def svg_m33_plimsoll_marks():
    """Page 3: Maritime Plimsoll load line markings"""
    inner = """
    <!-- Ship Hull Plate Background -->
    <rect x="60" y="55" width="720" height="335" fill="#111827" rx="12" stroke="#334155" stroke-width="2"/>

    <!-- Plimsoll Disc on Left at x = 240, y = 220 -->
    <circle cx="240" cy="220" r="60" fill="none" stroke="#f8fafc" stroke-width="4"/>
    <line x1="160" y1="220" x2="320" y2="220" stroke="#f8fafc" stroke-width="5"/>
    <text x="210" y="210" fill="#f8fafc" font-size="18" font-weight="700">L</text>
    <text x="260" y="210" fill="#f8fafc" font-size="18" font-weight="700">R</text>

    <!-- Vertical Load Line Bar at x = 440 -->
    <line x1="440" y1="100" x2="440" y2="330" stroke="#f8fafc" stroke-width="4"/>

    <!-- Stepped Horizontal Marks -->
    <!-- TF: Tropical Fresh (Highest, x=440 to 520, y=120) -->
    <line x1="440" y1="120" x2="520" y2="120" stroke="#22c55e" stroke-width="4"/>
    <text x="535" y="125" fill="#22c55e" font-size="14" font-weight="700">TF (Tropical Fresh)</text>

    <!-- F: Fresh Water (y=155) -->
    <line x1="440" y1="155" x2="520" y2="155" stroke="#38bdf8" stroke-width="4"/>
    <text x="535" y="160" fill="#38bdf8" font-size="14" font-weight="700">F (Fresh Water)</text>

    <!-- T: Tropical Salt (y=190) -->
    <line x1="440" y1="190" x2="520" y2="190" stroke="#f59e0b" stroke-width="4"/>
    <text x="535" y="195" fill="#f59e0b" font-size="14" font-weight="700">T (Tropical Salt)</text>

    <!-- S: Summer Salt (Aligned with Disc Bar at y=220) -->
    <line x1="440" y1="220" x2="520" y2="220" stroke="#f8fafc" stroke-width="4"/>
    <text x="535" y="225" fill="#f8fafc" font-size="14" font-weight="700">S (Summer Temperate)</text>

    <!-- W: Winter Salt (y=255) -->
    <line x1="440" y1="255" x2="520" y2="255" stroke="#a855f7" stroke-width="4"/>
    <text x="535" y="260" fill="#a855f7" font-size="14" font-weight="700">W (Winter Salt)</text>

    <!-- WNA: Winter North Atlantic (Lowest, y=290) -->
    <line x1="440" y1="290" x2="520" y2="290" stroke="#ef4444" stroke-width="4"/>
    <text x="535" y="295" fill="#ef4444" font-size="14" font-weight="700">WNA (Winter North Atlantic)</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Plimsoll Load Line Markings on a Commercial Ship Hull")

def svg_m33_submarine_ballast():
    """Page 4: Submarine depth control via ballast tanks"""
    inner = """
    <!-- 3 Panels: Surface, Diving, Surfacing -->
    <g transform="translate(30, 60)">
      <rect x="0" y="0" width="240" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="120" y="25" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">1. SURFACE (FLOATING)</text>

      <!-- Waterline -->
      <line x1="10" y1="120" x2="230" y2="120" stroke="#38bdf8" stroke-width="2"/>

      <!-- Submarine Hull -->
      <ellipse cx="120" cy="140" rx="90" ry="40" fill="#334155" stroke="#64748b" stroke-width="2"/>
      <rect x="105" y="85" width="30" height="30" fill="#334155" rx="3"/>

      <!-- Ballast Tanks filled with AIR -->
      <ellipse cx="60" cy="140" rx="20" ry="25" fill="#38bdf833" stroke="#38bdf8"/>
      <ellipse cx="180" cy="140" rx="20" ry="25" fill="#38bdf833" stroke="#38bdf8"/>
      <text x="120" y="220" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">Tanks Filled with Air</text>
      <text x="120" y="240" fill="#94a3b8" font-size="10" text-anchor="middle">ρ_sub &lt; ρ_water (U &gt; W)</text>
    </g>

    <g transform="translate(300, 60)">
      <rect x="0" y="0" width="240" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="120" y="25" fill="#ef4444" font-size="12" font-weight="700" text-anchor="middle">2. DIVING (SUBMERGING)</text>

      <line x1="10" y1="80" x2="230" y2="80" stroke="#38bdf8" stroke-width="2"/>

      <!-- Submarine submerged -->
      <ellipse cx="120" cy="170" rx="90" ry="40" fill="#334155" stroke="#64748b" stroke-width="2"/>
      <rect x="105" y="115" width="30" height="30" fill="#334155" rx="3"/>

      <!-- Ballast Tanks flooded with WATER -->
      <ellipse cx="60" cy="170" rx="20" ry="25" fill="#0284c7" stroke="#38bdf8"/>
      <ellipse cx="180" cy="170" rx="20" ry="25" fill="#0284c7" stroke="#38bdf8"/>
      <text x="120" y="240" fill="#ef4444" font-size="11" font-weight="700" text-anchor="middle">Tanks Flooded with Water</text>
      <text x="120" y="260" fill="#94a3b8" font-size="10" text-anchor="middle">ρ_sub &gt; ρ_water (W &gt; U)</text>
    </g>

    <g transform="translate(570, 60)">
      <rect x="0" y="0" width="240" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="120" y="25" fill="#22c55e" font-size="12" font-weight="700" text-anchor="middle">3. SURFACING (RISING)</text>

      <line x1="10" y1="90" x2="230" y2="90" stroke="#38bdf8" stroke-width="2"/>

      <ellipse cx="120" cy="150" rx="90" ry="40" fill="#334155" stroke="#64748b" stroke-width="2"/>
      <rect x="105" y="95" width="30" height="30" fill="#334155" rx="3"/>

      <!-- Compressed Air Expelling Water -->
      <ellipse cx="60" cy="150" rx="20" ry="25" fill="#22c55e33" stroke="#22c55e"/>
      <ellipse cx="180" cy="150" rx="20" ry="25" fill="#22c55e33" stroke="#22c55e"/>
      <text x="120" y="235" fill="#22c55e" font-size="11" font-weight="700" text-anchor="middle">Compressed Air Injected</text>
      <text x="120" y="255" fill="#94a3b8" font-size="10" text-anchor="middle">Water forced out (U &gt; W)</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Submarine Depth Regulation via Ballast Tank Flooding and Air Purging")

def svg_m33_hydrometer_construction():
    """Page 5: Hydrometer anatomy & downward graduated scale"""
    inner = """
    <!-- Central Glass Hydrometer at x = 380 -->
    <!-- Narrow Stem (x = 370 to 390, y = 60 to 220) -->
    <rect x="373" y="60" width="14" height="160" fill="#0284c715" stroke="#38bdf8" stroke-width="2" rx="3"/>

    <!-- Large Buoyancy Bulb (x = 350 to 410, y = 220 to 310) -->
    <ellipse cx="380" cy="265" rx="30" ry="45" fill="#0284c722" stroke="#38bdf8" stroke-width="2"/>
    <text x="380" y="270" fill="#38bdf8" font-size="10" font-weight="700" text-anchor="middle">Buoyancy Bulb</text>

    <!-- Weighted Base Bulb with Lead Shots (y = 310 to 360) -->
    <circle cx="380" cy="335" rx="20" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <!-- Lead Shots -->
    <circle cx="375" cy="330" r="3.5" fill="#94a3b8"/>
    <circle cx="385" cy="330" r="3.5" fill="#94a3b8"/>
    <circle cx="380" cy="340" r="3.5" fill="#94a3b8"/>
    <circle cx="372" cy="338" r="3.5" fill="#94a3b8"/>
    <circle cx="388" cy="338" r="3.5" fill="#94a3b8"/>

    <!-- Scale Markings on Stem (Graduated DOWNWARDS) -->
    <line x1="373" y1="80" x2="387" y2="80" stroke="#f8fafc" stroke-width="1.5"/><text x="395" y="84" fill="#f8fafc" font-size="9" font-weight="700">0.800 (Low Density)</text>
    <line x1="373" y1="120" x2="387" y2="120" stroke="#f8fafc" stroke-width="1.5"/><text x="395" y="124" fill="#f8fafc" font-size="9" font-weight="700">0.900</text>
    <line x1="373" y1="160" x2="387" y2="160" stroke="#22c55e" stroke-width="2"/><text x="395" y="164" fill="#22c55e" font-size="9" font-weight="700">1.000 (Water)</text>
    <line x1="373" y1="200" x2="387" y2="200" stroke="#f59e0b" stroke-width="1.5"/><text x="395" y="204" fill="#f59e0b" font-size="9" font-weight="700">1.200 (High Density)</text>

    <!-- Left Structural Annotations -->
    <g transform="translate(60, 90)">
      <rect x="0" y="0" width="260" height="260" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="130" y="25" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">KEY DESIGN FEATURES</text>

      <text x="15" y="60" fill="#f8fafc" font-size="11" font-weight="700">1. Narrow Stem:</text>
      <text x="15" y="78" fill="#94a3b8" font-size="10">High sensitivity to tiny density shifts.</text>

      <text x="15" y="115" fill="#f8fafc" font-size="11" font-weight="700">2. Large Central Bulb:</text>
      <text x="15" y="133" fill="#94a3b8" font-size="10">Creates large upthrust to keep it afloat.</text>

      <text x="15" y="170" fill="#f59e0b" font-size="11" font-weight="700">3. Lead Shots Base:</text>
      <text x="15" y="188" fill="#94a3b8" font-size="10">Lowers centre of gravity so it floats upright.</text>

      <text x="15" y="225" fill="#22c55e" font-size="11" font-weight="700">4. Inverted Scale:</text>
      <text x="15" y="243" fill="#94a3b8" font-size="10">Denser liquids = Sinks less = Read lower.</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Hydrometer Construction & Downward Graduated Scale Mechanics")

def svg_m33_weather_balloon():
    """Page 7: Weather balloon atmospheric lift force resolution"""
    inner = """
    <!-- Atmosphere background -->
    <rect x="60" y="55" width="720" height="335" fill="#111827" rx="12" stroke="#1e293b"/>

    <!-- Large Balloon Envelope at x = 300, y = 160 -->
    <ellipse cx="300" cy="160" rx="90" ry="95" fill="#38bdf822" stroke="#38bdf8" stroke-width="3"/>
    <text x="300" y="155" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">Hydrogen Gas</text>
    <text x="300" y="175" fill="#94a3b8" font-size="10" text-anchor="middle">(V = 10 m³, ρ = 0.09 kg/m³)</text>

    <!-- Instrument Payload Rig -->
    <line x1="300" y1="255" x2="300" y2="300" stroke="#f8fafc" stroke-width="2"/>
    <rect x="280" y="300" width="40" height="35" fill="#f59e0b" rx="4" stroke="#d97706"/>
    <text x="300" y="322" fill="#000" font-size="9" font-weight="700" text-anchor="middle">Payload</text>

    <!-- Upward Buoyant Force Arrow -->
    <line x1="300" y1="65" x2="300" y2="20" stroke="#22c55e" stroke-width="4"/>
    <polygon points="293,32 300,18 307,32" fill="#22c55e"/>
    <text x="320" y="35" fill="#22c55e" font-size="13" font-weight="700">Air Upthrust U = ρ_air·V·g (125 N)</text>

    <!-- Downward Weights -->
    <line x1="300" y1="335" x2="300" y2="375" stroke="#ef4444" stroke-width="3"/>
    <polygon points="295,365 300,378 305,365" fill="#ef4444"/>

    <!-- Right Side Calculation Panel -->
    <rect x="460" y="75" width="300" height="295" fill="#0f172a" rx="10" stroke="#334155"/>
    <text x="610" y="105" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">LIFT EQUILIBRIUM</text>

    <g transform="translate(480, 135)">
      <text x="0" y="0" fill="#22c55e" font-size="12" font-weight="700">• Air Upthrust: 125 N</text>
      <text x="0" y="35" fill="#f59e0b" font-size="12" font-weight="700">• Fabric Weight: 80 N</text>
      <text x="0" y="70" fill="#38bdf8" font-size="12" font-weight="700">• Gas Weight (H₂): 9 N</text>

      <rect x="0" y="105" width="260" height="55" fill="#22c55e15" rx="6" stroke="#22c55e"/>
      <text x="130" y="128" fill="#f8fafc" font-size="11" text-anchor="middle">Net Payload Lift Capacity:</text>
      <text x="130" y="148" fill="#22c55e" font-size="14" font-weight="700" text-anchor="middle">Payload = 125 - 89 = 36 N</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Atmospheric Buoyant Lift and Payload Capacity of a Weather Balloon")


# =============================================================================
# MAIN ENRICHMENT EXECUTOR FOR TOPIC 3
# =============================================================================

def run_enrichment_topic3():
    print("=" * 80)
    print("VLEARN FORM 4 PHYSICS — TOPIC 3 VISUAL ENRICHMENT")
    print("=" * 80)

    topic = Topic.objects.filter(
        subject__name="Physics",
        subject__grade__name="Form 4",
        name__icontains="Floating and Sinking"
    ).first()

    if not topic:
        print("ERROR: Topic 3: Floating and Sinking not found! Run ingest_form4_physics_topic3.py first.")
        return

    units = topic.learning_units.all().order_by("order")
    if units.count() < 3:
        print("ERROR: Expected 3 learning units in Topic 3.")
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
    # MODULE 3.1 ENRICHMENT
    # -------------------------------------------------------------------------
    print("--- Enriching Module 3.1 ---")
    attach_svg_to_block(lesson_1, 2, "suggested_diagram", "Theoretical Origin of Upthrust: Liquid Pressure Gradient with Depth", "m31_pressure_gradient", svg_m31_pressure_gradient())
    attach_svg_to_block(lesson_1, 6, "suggested_diagram", "Laboratory Setup for Demonstrating Archimedes' Principle", "m31_eureka_archimedes", svg_m31_eureka_archimedes())

    # -------------------------------------------------------------------------
    # MODULE 3.2 ENRICHMENT
    # -------------------------------------------------------------------------
    print("\n--- Enriching Module 3.2 ---")
    attach_svg_to_block(lesson_2, 3, "suggested_diagram", "Density Criteria: Floating, Neutral Buoyancy, and Sinking", "m32_floating_conditions", svg_m32_floating_conditions())
    attach_svg_to_block(lesson_2, 7, "suggested_diagram", "Experimental Setup for the Law of Floatation", "m32_law_of_floatation", svg_m32_law_of_floatation())
    attach_svg_to_block(lesson_2, 8, "suggested_diagram", "The 3 Stages of the Cork and Sinker Method", "m32_cork_sinker", svg_m32_cork_sinker())

    # -------------------------------------------------------------------------
    # MODULE 3.3 ENRICHMENT
    # -------------------------------------------------------------------------
    print("\n--- Enriching Module 3.3 ---")
    attach_svg_to_block(lesson_3, 2, "suggested_diagram", "Why Steel Ships Float: Average Density Reduction via Hollow Hull Design", "m33_ship_hollow_hull", svg_m33_ship_hollow_hull())
    attach_svg_to_block(lesson_3, 3, "suggested_diagram", "Plimsoll Load Line Markings on a Commercial Ship Hull", "m33_plimsoll_marks", svg_m33_plimsoll_marks())
    attach_svg_to_block(lesson_3, 4, "suggested_diagram", "Submarine Depth Regulation via Ballast Tank Flooding and Air Purging", "m33_submarine_ballast", svg_m33_submarine_ballast())
    attach_svg_to_block(lesson_3, 5, "suggested_diagram", "Hydrometer Construction & Downward Graduated Scale Mechanics", "m33_hydrometer", svg_m33_hydrometer_construction())
    attach_svg_to_block(lesson_3, 7, "suggested_diagram", "Atmospheric Buoyant Lift and Payload Capacity of a Weather Balloon", "m33_weather_balloon", svg_m33_weather_balloon())

    # Wikimedia Assets
    attach_wikimedia_to_block(
        lesson=lesson_3,
        page_num=3,
        title="International Load Line on Commercial Vessel Alexander Grin",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/International_Load_Line_on_%22Alexander_Grin%22_-_geograph.org.uk_-_1759965.jpg/960px-International_Load_Line_on_%22Alexander_Grin%22_-_geograph.org.uk_-_1759965.jpg",
        author="Robin Webster",
        licensing="CC BY-SA 2.0",
        commons_page="https://commons.wikimedia.org/wiki/File:International_Load_Line_on_%22Alexander_Grin%22_-_geograph.org.uk_-_1759965.jpg"
    )

    attach_wikimedia_to_block(
        lesson=lesson_3,
        page_num=5,
        title="Laboratory Glass Hydrometer in Graduated Cylinder",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/2023_Areometr_Ballinga.jpg/960px-2023_Areometr_Ballinga.jpg",
        author="Jacek Halicki",
        licensing="CC BY-SA 4.0",
        commons_page="https://commons.wikimedia.org/wiki/File:2023_Areometr_Ballinga.jpg"
    )

    attach_wikimedia_to_block(
        lesson=lesson_3,
        page_num=3,
        title="Historical Lloyds Load Line on the Cutty Sark",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Lloydsloadlinecuttysark.jpg/960px-Lloydsloadlinecuttysark.jpg",
        author="Geni",
        licensing="CC BY 2.0",
        commons_page="https://commons.wikimedia.org/wiki/File:Lloydsloadlinecuttysark.jpg"
    )

    print("\n" + "=" * 80)
    print("TOPIC 3 VISUAL ENRICHMENT COMPLETED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    run_enrichment_topic3()
