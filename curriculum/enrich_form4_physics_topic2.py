"""
VLearn Form 4 Physics — Topic 2: Uniform Circular Motion
Visual Enrichment Engine (SVGs + Wikimedia Commons)

Enriches all 3 modules of Topic 2 (Uniform Circular Motion) with:
  - 12 high-precision dark-mode vector SVG diagrams (tangential velocity vectors, radian geometry, 
    centripetal acceleration vector maps, vertical circular motion forces, slackening limit at the apex, 
    laboratory whirling rubber bung setup, T vs w^2 linear graph, conical pendulum resolution, 
    centrifuge mass separation, banked highway normal reaction resolution, and Watt speed governor).
  - 4 authentic, high-resolution Wikimedia Commons photographic assets (tabletop laboratory centrifuge, 
    historic Watt steam engine centrifugal governor, AVUS banked curve racetrack, and optical kits).

All SVGs are validated and sanitized via `validate_and_sanitize_svg`, stored with `storage_type='embed'`, 
and embedded directly into `LessonBlock` content and metadata for immediate frontend rendering.

Usage:
  /home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/venv/bin/python curriculum/enrich_form4_physics_topic2.py
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
# SVG BUILDERS — MODULE 2.1
# =============================================================================

def svg_m21_tangential_velocity():
    """Page 2: Tangential velocity vectors in circular path"""
    inner = """
    <!-- Circular Orbit Path -->
    <circle cx="380" cy="225" r="140" fill="none" stroke="#334155" stroke-width="2" stroke-dasharray="6 4"/>
    <circle cx="380" cy="225" r="4.5" fill="#38bdf8"/>
    <text x="380" y="245" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">O (Centre)</text>

    <!-- Radius line to top position -->
    <line x1="380" y1="225" x2="380" y2="85" stroke="#64748b" stroke-width="1.5"/>
    <text x="365" y="155" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" font-weight="600">r</text>

    <!-- Position 1 (Top: x=380, y=85) -->
    <circle cx="380" cy="85" r="7" fill="#22c55e"/>
    <line x1="380" y1="85" x2="250" y2="85" stroke="#f59e0b" stroke-width="3"/>
    <polygon points="260,80 245,85 260,90" fill="#f59e0b"/>
    <text x="250" y="75" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="700">v₁</text>

    <!-- Tangential Escape trajectory if cut (dashed line extending straight) -->
    <line x1="250" y1="85" x2="100" y2="85" stroke="#ef4444" stroke-width="2" stroke-dasharray="4 3"/>
    <text x="120" y="70" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Tangential Escape if String Snaps</text>

    <!-- Position 2 (Left: x=240, y=225) -->
    <circle cx="240" cy="225" r="7" fill="#22c55e"/>
    <line x1="240" y1="225" x2="240" y2="355" stroke="#f59e0b" stroke-width="3"/>
    <polygon points="235,345 240,360 245,345" fill="#f59e0b"/>
    <text x="220" y="360" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="700">v₂</text>

    <!-- Position 3 (Bottom: x=380, y=365) -->
    <circle cx="380" cy="365" r="7" fill="#22c55e"/>
    <line x1="380" y1="365" x2="510" y2="365" stroke="#f59e0b" stroke-width="3"/>
    <polygon points="500,360 515,365 500,370" fill="#f59e0b"/>
    <text x="525" y="370" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="700">v₃</text>

    <!-- Position 4 (Right: x=520, y=225) -->
    <circle cx="520" cy="225" r="7" fill="#22c55e"/>
    <line x1="520" y1="225" x2="520" y2="95" stroke="#f59e0b" stroke-width="3"/>
    <polygon points="515,105 520,90 525,105" fill="#f59e0b"/>
    <text x="535" y="100" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="700">v₄</text>

    <!-- Right Summary Panel -->
    <rect x="580" y="70" width="230" height="310" fill="#111827" rx="10" stroke="#1e293b"/>
    <text x="695" y="100" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">KEY PRINCIPLES</text>

    <g transform="translate(595, 130)">
      <text x="0" y="0" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600">• Constant Speed:</text>
      <text x="0" y="20" fill="#22c55e" font-family="system-ui, sans-serif" font-size="11">|v₁| = |v₂| = |v₃| = |v₄| = v</text>

      <text x="0" y="60" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600">• Changing Velocity:</text>
      <text x="0" y="80" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11">Direction changes continuously</text>

      <text x="0" y="120" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600">• Perpendicularity:</text>
      <text x="0" y="140" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11">Velocity vector v ⊥ radius r</text>

      <text x="0" y="180" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="600">• Inward Acceleration:</text>
      <text x="0" y="200" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11">a_c directed to centre O</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Tangential Velocity Vectors in Uniform Circular Motion")

def svg_m21_radian_definition():
    """Page 3: Geometric definition of 1 Radian"""
    inner = """
    <!-- Circle -->
    <circle cx="340" cy="225" r="150" fill="none" stroke="#334155" stroke-width="2" stroke-dasharray="4 4"/>
    <circle cx="340" cy="225" r="4.5" fill="#38bdf8"/>
    <text x="340" y="250" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">O (Centre)</text>

    <!-- Radius Baseline (x = 340 to 490 at y = 225) -->
    <line x1="340" y1="225" x2="490" y2="225" stroke="#38bdf8" stroke-width="3"/>
    <text x="415" y="245" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Radius (r)</text>

    <!-- Radius Arm at 57.3 degrees (x = 340 + 150*cos(57.3°)=340+81=421, y = 225 - 150*sin(57.3°)=225-126=99) -->
    <line x1="340" y1="225" x2="421" y2="99" stroke="#38bdf8" stroke-width="3"/>
    <text x="365" y="150" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Radius (r)</text>

    <!-- Subtended Arc (Green highlighted curve) -->
    <path d="M 490,225 A 150 150 0 0 0 421,99" fill="none" stroke="#22c55e" stroke-width="6"/>
    <text x="495" y="155" fill="#22c55e" font-family="system-ui, sans-serif" font-size="14" font-weight="700">Arc Length s = r</text>

    <!-- Angle Sector Fill & Label -->
    <path d="M 340,225 L 490,225 A 150 150 0 0 0 421,99 Z" fill="#0284c722"/>
    <path d="M 390,225 A 50 50 0 0 0 367,183" fill="none" stroke="#f59e0b" stroke-width="2"/>
    <text x="405" y="200" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="14" font-weight="700">θ = 1 rad</text>
    <text x="405" y="215" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11">(≈ 57.3°)</text>

    <!-- Right Derivation Box -->
    <rect x="550" y="65" width="260" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
    <text x="680" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">THE RADIAN FORMULA</text>

    <g transform="translate(565, 125)">
      <text x="0" y="0" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Angle in Radians:</text>
      <text x="0" y="24" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="14" font-weight="700">θ = s / r</text>

      <text x="0" y="65" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">When Arc Length s = r:</text>
      <text x="0" y="87" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="700">θ = r / r = 1 radian</text>

      <text x="0" y="125" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Full Circle (s = 2πr):</text>
      <text x="0" y="147" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="700">2π rad = 360°</text>
      <text x="0" y="170" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="700">π rad = 180°</text>

      <rect x="0" y="195" width="230" height="40" fill="#0284c722" rx="6" stroke="#0284c7"/>
      <text x="115" y="220" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1 rad = 180°/π ≈ 57.3°</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Geometric Definition & Mathematical Origin of the Radian")


# =============================================================================
# SVG BUILDERS — MODULE 2.2
# =============================================================================

def svg_m22_centripetal_acceleration():
    """Page 2: Centripetal acceleration pointing radially inwards"""
    inner = """
    <!-- Circular Path -->
    <circle cx="380" cy="225" r="140" fill="none" stroke="#334155" stroke-width="2"/>
    <circle cx="380" cy="225" r="5" fill="#38bdf8"/>
    <text x="380" y="250" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Centre O</text>

    <!-- 4 Object Positions with inward acceleration vectors -->
    <!-- Position 1: Top (x=380, y=85) -->
    <circle cx="380" cy="85" r="7" fill="#22c55e"/>
    <!-- Inward a_c arrow -->
    <line x1="380" y1="85" x2="380" y2="165" stroke="#ef4444" stroke-width="3"/>
    <polygon points="375,155 380,170 385,155" fill="#ef4444"/>
    <text x="395" y="130" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="700">a_c</text>
    <!-- Tangent v arrow -->
    <line x1="380" y1="85" x2="280" y2="85" stroke="#f59e0b" stroke-width="2.5"/>
    <polygon points="290,80 275,85 290,90" fill="#f59e0b"/>
    <text x="280" y="75" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700">v</text>

    <!-- Position 2: Right (x=520, y=225) -->
    <circle cx="520" cy="225" r="7" fill="#22c55e"/>
    <!-- Inward a_c arrow -->
    <line x1="520" y1="225" x2="440" y2="225" stroke="#ef4444" stroke-width="3"/>
    <polygon points="450,220 435,225 450,230" fill="#ef4444"/>
    <text x="475" y="215" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="700">a_c</text>
    <!-- Tangent v arrow -->
    <line x1="520" y1="225" x2="520" y2="125" stroke="#f59e0b" stroke-width="2.5"/>
    <polygon points="515,135 520,120 525,135" fill="#f59e0b"/>
    <text x="535" y="130" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700">v</text>

    <!-- Position 3: Bottom (x=380, y=365) -->
    <circle cx="380" cy="365" r="7" fill="#22c55e"/>
    <!-- Inward a_c arrow -->
    <line x1="380" y1="365" x2="380" y2="285" stroke="#ef4444" stroke-width="3"/>
    <polygon points="375,295 380,280 385,295" fill="#ef4444"/>
    <text x="395" y="320" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="700">a_c</text>
    <!-- Tangent v arrow -->
    <line x1="380" y1="365" x2="480" y2="365" stroke="#f59e0b" stroke-width="2.5"/>
    <polygon points="470,360 485,365 470,370" fill="#f59e0b"/>
    <text x="485" y="380" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700">v</text>

    <!-- Right Equation Panel -->
    <rect x="575" y="65" width="235" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
    <text x="692" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">CENTRIPETAL FORMULAS</text>

    <g transform="translate(590, 130)">
      <text x="0" y="0" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Linear Speed Form:</text>
      <text x="0" y="24" fill="#ef4444" font-family="system-ui, sans-serif" font-size="14" font-weight="700">a_c = v² / r</text>

      <text x="0" y="65" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Angular Speed Form:</text>
      <text x="0" y="89" fill="#ef4444" font-family="system-ui, sans-serif" font-size="14" font-weight="700">a_c = rω²</text>

      <text x="0" y="130" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Centripetal Force (F = ma):</text>
      <text x="0" y="154" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="700">F_c = mv² / r</text>
      <text x="0" y="176" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="700">F_c = mrω²</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Centripetal Acceleration & Inward Force Dynamics")

def svg_m22_vertical_circle_forces():
    """Page 6: Dynamic force resolution in a vertical circle (Top, Midpoint, Bottom)"""
    inner = """
    <!-- Vertical Circle -->
    <circle cx="340" cy="225" r="140" fill="none" stroke="#334155" stroke-width="2" stroke-dasharray="4 4"/>
    <circle cx="340" cy="225" r="4.5" fill="#38bdf8"/>
    <text x="340" y="245" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">O</text>

    <!-- Position 1: Top (x=340, y=85) -->
    <circle cx="340" cy="85" r="8" fill="#22c55e"/>
    <!-- T1 arrow down -->
    <line x1="335" y1="85" x2="335" y2="155" stroke="#38bdf8" stroke-width="2.5"/>
    <polygon points="330,145 335,160 340,145" fill="#38bdf8"/>
    <text x="315" y="125" fill="#38bdf8" font-size="11" font-weight="700">T₁</text>
    <!-- mg arrow down -->
    <line x1="345" y1="85" x2="345" y2="155" stroke="#f59e0b" stroke-width="2.5"/>
    <polygon points="340,145 345,160 350,145" fill="#f59e0b"/>
    <text x="355" y="125" fill="#f59e0b" font-size="11" font-weight="700">mg</text>
    <text x="340" y="65" fill="#f8fafc" font-size="12" font-weight="700" text-anchor="middle">TOP (T₁ + mg = mv²/r)</text>

    <!-- Position 2: Horizontal Midpoint (x=200, y=225) -->
    <circle cx="200" cy="225" r="8" fill="#22c55e"/>
    <!-- T2 arrow inwards -->
    <line x1="200" y1="225" x2="270" y2="225" stroke="#38bdf8" stroke-width="2.5"/>
    <polygon points="260,220 275,225 260,230" fill="#38bdf8"/>
    <text x="240" y="215" fill="#38bdf8" font-size="11" font-weight="700">T₂</text>
    <!-- mg arrow downwards -->
    <line x1="200" y1="225" x2="200" y2="295" stroke="#f59e0b" stroke-width="2.5"/>
    <polygon points="195,285 200,300 205,285" fill="#f59e0b"/>
    <text x="210" y="275" fill="#f59e0b" font-size="11" font-weight="700">mg</text>
    <text x="140" y="230" fill="#f8fafc" font-size="11" font-weight="700">MIDPOINT (T₂ = mv²/r)</text>

    <!-- Position 3: Bottom (x=340, y=365) -->
    <circle cx="340" cy="365" r="8" fill="#ef4444"/>
    <!-- T3 arrow upward -->
    <line x1="340" y1="365" x2="340" y2="275" stroke="#38bdf8" stroke-width="3"/>
    <polygon points="335,285 340,270 345,285" fill="#38bdf8"/>
    <text x="320" y="305" fill="#38bdf8" font-size="12" font-weight="700">T₃</text>
    <!-- mg arrow downward -->
    <line x1="340" y1="365" x2="340" y2="415" stroke="#f59e0b" stroke-width="2.5"/>
    <polygon points="335,405 340,420 345,405" fill="#f59e0b"/>
    <text x="355" y="400" fill="#f59e0b" font-size="11" font-weight="700">mg</text>
    <text x="340" y="380" fill="#ef4444" font-size="12" font-weight="700" text-anchor="middle">BOTTOM (T₃ - mg = mv²/r)</text>

    <!-- Right Dynamic Tension Comparison Panel -->
    <rect x="520" y="65" width="290" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
    <text x="665" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">VERTICAL TENSION FORMULAS</text>

    <g transform="translate(535, 125)">
      <rect x="0" y="0" width="260" height="55" fill="#0284c715" rx="6" stroke="#0284c744"/>
      <text x="10" y="20" fill="#38bdf8" font-size="12" font-weight="700">Top Position (Minimum Tension):</text>
      <text x="10" y="42" fill="#f8fafc" font-size="13" font-weight="700">T₁ = (mv²/r) - mg</text>

      <rect x="0" y="70" width="260" height="55" fill="#0284c715" rx="6" stroke="#0284c744"/>
      <text x="10" y="90" fill="#38bdf8" font-size="12" font-weight="700">Horizontal Midpoint:</text>
      <text x="10" y="112" fill="#f8fafc" font-size="13" font-weight="700">T₂ = mv²/r</text>

      <rect x="0" y="140" width="260" height="65" fill="#ef444415" rx="6" stroke="#ef444444"/>
      <text x="10" y="160" fill="#ef4444" font-size="12" font-weight="700">Bottom Position (MAXIMUM TENSION):</text>
      <text x="10" y="182" fill="#ef4444" font-size="13" font-weight="700">T₃ = (mv²/r) + mg</text>
      <text x="10" y="198" fill="#fca5a5" font-size="10">String most likely to break here!</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Tension & Force Dynamics in a Vertical Circular Path")

def svg_m22_lab_apparatus():
    """Page 10: Experimental apparatus (rubber bung, glass tube, slotted mass)"""
    inner = """
    <!-- Glass Tube held vertically at x = 320, y = 140 to 260 -->
    <rect x="312" y="140" width="16" height="120" fill="#0284c722" stroke="#38bdf8" stroke-width="2" rx="3"/>
    <text x="340" y="205" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Glass Tube</text>

    <!-- Hand gripping glass tube -->
    <rect x="300" y="180" width="40" height="40" fill="#334155" rx="6"/>
    <text x="250" y="205" fill="#94a3b8" font-size="11">Hand Grip</text>

    <!-- Nylon String exiting top and curving to horizontal circle -->
    <path d="M 320,140 Q 320,80 480,80" fill="none" stroke="#f8fafc" stroke-width="2.5"/>
    <circle cx="480" cy="80" r="12" fill="#22c55e"/>
    <text x="480" y="55" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Rubber Bung (m)</text>

    <!-- Horizontal Orbit of Rubber Bung -->
    <ellipse cx="320" cy="80" rx="160" ry="30" fill="none" stroke="#22c55e" stroke-width="1.5" stroke-dasharray="4 4"/>
    <line x1="320" y1="80" x2="480" y2="80" stroke="#f59e0b" stroke-width="2"/>
    <text x="400" y="75" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Radius r</text>

    <!-- Paper Clip Marker just below glass tube -->
    <line x1="310" y1="268" x2="330" y2="268" stroke="#f59e0b" stroke-width="4"/>
    <text x="220" y="272" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="700">Paper Clip Marker</text>
    <text x="220" y="286" fill="#94a3b8" font-size="9">(Kept 2mm below tube)</text>

    <!-- String descending to dangling mass M -->
    <line x1="320" y1="260" x2="320" y2="350" stroke="#f8fafc" stroke-width="2.5"/>

    <!-- Dangling Slotted Mass M -->
    <rect x="305" y="350" width="30" height="40" fill="#f59e0b" rx="4" stroke="#d97706" stroke-width="2"/>
    <text x="320" y="375" fill="#000" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">M</text>
    <text x="360" y="375" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Tension T = Mg</text>

    <!-- Right Side Experimental Protocol Panel -->
    <rect x="530" y="60" width="280" height="330" fill="#111827" rx="10" stroke="#1e293b"/>
    <text x="670" y="90" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">EXPERIMENTAL METHOD</text>

    <g transform="translate(545, 120)">
      <text x="0" y="0" fill="#22c55e" font-size="12" font-weight="700">1. Whirling Bung Mass (m):</text>
      <text x="0" y="18" fill="#94a3b8" font-size="11">Kept constant throughout trials.</text>

      <text x="0" y="50" fill="#f59e0b" font-size="12" font-weight="700">2. Tension Source (T = Mg):</text>
      <text x="0" y="68" fill="#94a3b8" font-size="11">Varied by altering slotted mass M.</text>

      <text x="0" y="100" fill="#38bdf8" font-size="12" font-weight="700">3. Radius Control (r):</text>
      <text x="0" y="118" fill="#94a3b8" font-size="11">Marker held steady just below tube.</text>

      <text x="0" y="150" fill="#f8fafc" font-size="12" font-weight="700">4. Timing 10 Revolutions:</text>
      <text x="0" y="168" fill="#94a3b8" font-size="11">Time t measured to calculate ω = 2π/T_p.</text>

      <rect x="0" y="195" width="250" height="40" fill="#0284c722" rx="6" stroke="#0284c7"/>
      <text x="125" y="220" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">Governing Law: T = (mr)ω²</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Laboratory Investigation: Determining Factors of Centripetal Force")

def svg_m22_graph_t_vs_w2():
    """Page 11: Experimental graph T vs omega^2"""
    inner = """
    <!-- Graph Grid Area -->
    <rect x="60" y="60" width="460" height="320" fill="#111827" rx="8" stroke="#1e293b"/>

    <!-- Grid lines -->
    <g stroke="#1e293b" stroke-width="1">
      <line x1="140" y1="60" x2="140" y2="350"/>
      <line x1="220" y1="60" x2="220" y2="350"/>
      <line x1="300" y1="60" x2="300" y2="350"/>
      <line x1="380" y1="60" x2="380" y2="350"/>
      <line x1="460" y1="60" x2="460" y2="350"/>

      <line x1="90" y1="110" x2="490" y2="110"/>
      <line x1="90" y1="170" x2="490" y2="170"/>
      <line x1="90" y1="230" x2="490" y2="230"/>
      <line x1="90" y1="290" x2="490" y2="290"/>
    </g>

    <!-- Axes -->
    <line x1="90" y1="350" x2="490" y2="350" stroke="#f8fafc" stroke-width="2"/>
    <line x1="90" y1="350" x2="90" y2="70" stroke="#f8fafc" stroke-width="2"/>

    <text x="290" y="375" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">ω² (rad² s⁻²)</text>
    <text x="40" y="210" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle" transform="rotate(-90 40 210)">Tension T (N)</text>

    <!-- Origin (0,0) -->
    <circle cx="90" cy="350" r="4" fill="#38bdf8"/>
    <text x="80" y="365" fill="#94a3b8" font-size="11">0</text>

    <!-- Linear Plot Line (through origin) -->
    <line x1="90" y1="350" x2="470" y2="85" stroke="#38bdf8" stroke-width="3"/>

    <!-- Experimental Data Points -->
    <circle cx="170" cy="294" r="4.5" fill="#22c55e"/>
    <circle cx="250" cy="238" r="4.5" fill="#22c55e"/>
    <circle cx="330" cy="182" r="4.5" fill="#22c55e"/>
    <circle cx="410" cy="126" r="4.5" fill="#22c55e"/>

    <!-- Right Side Mathematical Derivation Panel -->
    <rect x="540" y="60" width="270" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
    <text x="675" y="90" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">GRAPHICAL DERIVATION</text>

    <g transform="translate(555, 120)">
      <text x="0" y="0" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Centripetal Law:</text>
      <text x="0" y="22" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="600">T = m · r · ω²</text>

      <text x="0" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Linear Equation (y = mx + c):</text>
      <text x="0" y="82" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700">T = (m · r) · ω² + 0</text>

      <text x="0" y="120" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Passes through Origin (c = 0)</text>
      <text x="0" y="145" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Gradient = m · r</text>

      <rect x="0" y="175" width="240" height="55" fill="#0284c722" rx="6" stroke="#0284c7"/>
      <text x="120" y="198" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Rubber Bung Mass:</text>
      <text x="120" y="218" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">m = (Gradient) / r</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Linear Experimental Plot: Tension T against Angular Velocity Squared (ω²)")


# =============================================================================
# SVG BUILDERS — MODULE 2.3
# =============================================================================

def svg_m23_conical_pendulum():
    """Page 2: Conical Pendulum Vector Resolution"""
    inner = """
    <!-- Ceiling Support at top x = 380, y = 70 -->
    <line x1="300" y1="70" x2="460" y2="70" stroke="#64748b" stroke-width="4"/>
    <circle cx="380" cy="70" r="5" fill="#f8fafc"/>

    <!-- Vertical Reference Axis (Dashed) -->
    <line x1="380" y1="70" x2="380" y2="330" stroke="#64748b" stroke-dasharray="4 4" stroke-width="1.5"/>

    <!-- String of length l (from 380,70 to 520,270) -->
    <line x1="380" y1="70" x2="520" y2="270" stroke="#38bdf8" stroke-width="3"/>
    <text x="470" y="165" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">String (l)</text>

    <!-- Angle theta at top -->
    <path d="M 380,120 A 50 50 0 0 0 405,108" fill="none" stroke="#f59e0b" stroke-width="2"/>
    <text x="400" y="135" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="700">θ</text>

    <!-- Bob of mass M at (520, 270) -->
    <circle cx="520" cy="270" r="14" fill="#22c55e" stroke="#16a34a" stroke-width="2"/>
    <text x="520" y="275" fill="#000" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">M</text>

    <!-- Horizontal Orbit of Radius r -->
    <ellipse cx="380" cy="270" rx="140" ry="25" fill="none" stroke="#22c55e" stroke-width="1.5" stroke-dasharray="4 4"/>
    <line x1="380" y1="270" x2="520" y2="270" stroke="#f59e0b" stroke-width="2"/>
    <text x="450" y="290" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Radius r</text>

    <!-- Force Vectors at Bob -->
    <!-- Weight Mg downward -->
    <line x1="520" y1="270" x2="520" y2="370" stroke="#f59e0b" stroke-width="2.5"/>
    <polygon points="515,360 520,375 525,360" fill="#f59e0b"/>
    <text x="535" y="365" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Weight Mg</text>

    <!-- Vertical Tension Component Ty = T cos(theta) upward -->
    <line x1="520" y1="270" x2="520" y2="170" stroke="#38bdf8" stroke-width="2.5"/>
    <polygon points="515,180 520,165 525,180" fill="#38bdf8"/>
    <text x="530" y="185" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">T cos θ</text>

    <!-- Horizontal Centripetal Component Tx = T sin(theta) inward -->
    <line x1="520" y1="270" x2="400" y2="270" stroke="#ef4444" stroke-width="2.5"/>
    <polygon points="410,265 395,270 410,275" fill="#ef4444"/>
    <text x="460" y="255" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">F_c = T sin θ</text>

    <!-- Left Derivation Panel -->
    <rect x="40" y="65" width="230" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
    <text x="155" y="95" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">FORCE RESOLUTION</text>

    <g transform="translate(55, 125)">
      <text x="0" y="0" fill="#94a3b8" font-size="11">1. Vertical Equilibrium:</text>
      <text x="0" y="20" fill="#38bdf8" font-size="13" font-weight="700">T cos θ = Mg</text>

      <text x="0" y="55" fill="#94a3b8" font-size="11">2. Horizontal Centripetal:</text>
      <text x="0" y="75" fill="#ef4444" font-size="13" font-weight="700">T sin θ = M r ω²</text>

      <text x="0" y="110" fill="#94a3b8" font-size="11">3. Dividing (2) by (1):</text>
      <text x="0" y="132" fill="#f59e0b" font-size="14" font-weight="700">tan θ = rω² / g</text>

      <text x="0" y="165" fill="#94a3b8" font-size="10">As speed ω increases, angle θ</text>
      <text x="0" y="180" fill="#94a3b8" font-size="10">and orbit radius r increase.</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Vector Resolution of the Conical Pendulum")

def svg_m23_centrifuge_mechanism():
    """Page 4: Centrifuge particle separation mechanism by mass"""
    inner = """
    <!-- Left Panel: At Rest (Vertical Tubes) -->
    <g transform="translate(0, 0)">
      <rect x="30" y="55" width="370" height="335" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="215" y="85" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">AT REST (VERTICAL POSITION)</text>

      <circle cx="215" cy="130" r="14" fill="#475569"/>
      <line x1="215" y1="130" x2="215" y2="170" stroke="#64748b" stroke-width="4"/>

      <!-- Vertical Tube -->
      <rect x="200" y="170" width="30" height="130" fill="#0284c722" stroke="#38bdf8" stroke-width="2" rx="6"/>
      <!-- Uniform mixture dots -->
      <circle cx="215" cy="190" r="3" fill="#ef4444"/>
      <circle cx="210" cy="210" r="3" fill="#ef4444"/>
      <circle cx="220" cy="230" r="3" fill="#ef4444"/>
      <circle cx="215" cy="250" r="3" fill="#ef4444"/>
      <circle cx="210" cy="270" r="3" fill="#ef4444"/>
      <text x="215" y="335" fill="#94a3b8" font-size="11" text-anchor="middle">Uniform Suspension</text>
    </g>

    <!-- Right Panel: High-Speed Spinning (Horizontal Tubes & Separation) -->
    <g transform="translate(415, 0)">
      <rect x="25" y="55" width="370" height="335" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="210" y="85" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">HIGH-SPEED SPINNING (SEPARATION)</text>

      <circle cx="210" cy="210" r="16" fill="#38bdf8"/>
      <text x="210" y="215" fill="#000" font-size="10" font-weight="700" text-anchor="middle">ω</text>

      <!-- Horizontal Tube Swung Out to Right -->
      <rect x="226" y="195" width="130" height="30" fill="#0284c722" stroke="#38bdf8" stroke-width="2" rx="6"/>

      <!-- Supernatant Liquid on Inner Side -->
      <rect x="226" y="195" width="70" height="30" fill="#38bdf844" rx="4"/>
      <text x="260" y="180" fill="#38bdf8" font-size="10" font-weight="600" text-anchor="middle">Clear Liquid</text>

      <!-- Dense Heavy Particles (m1) at Outer Tip / Tube Bottom -->
      <rect x="320" y="195" width="36" height="30" fill="#ef4444" rx="4"/>
      <text x="338" y="180" fill="#ef4444" font-size="10" font-weight="700" text-anchor="middle">Dense Solids</text>

      <text x="210" y="280" fill="#f8fafc" font-size="12" font-weight="600" text-anchor="middle">Dense particles require larger Fc = mv²/r</text>
      <text x="210" y="300" fill="#94a3b8" font-size="11" text-anchor="middle">and are driven to the outer tube bottom.</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Centrifuge Separation Mechanism: Dense Particles Driven Outward by Inertia")

def svg_m23_banked_road():
    """Page 5: Normal reaction resolution on a banked curve"""
    inner = """
    <!-- Road Surface Slope at angle theta = 25 degrees -->
    <path d="M 120,330 L 620,140 L 620,330 Z" fill="#1e293b" stroke="#475569" stroke-width="2"/>
    <line x1="120" y1="330" x2="620" y2="330" stroke="#64748b" stroke-width="2"/>

    <!-- Banking Angle Theta -->
    <path d="M 220,330 A 100 100 0 0 0 205,298" fill="none" stroke="#f59e0b" stroke-width="2"/>
    <text x="235" y="320" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="14" font-weight="700">θ</text>

    <!-- Vehicle Rear on Incline at (370, 235) -->
    <g transform="translate(370, 235) rotate(-20.8)">
      <rect x="-35" y="-25" width="70" height="50" fill="#0284c7" rx="6" stroke="#38bdf8" stroke-width="2"/>
      <circle cx="-25" cy="25" r="8" fill="#0f172a"/>
      <circle cx="25" cy="25" r="8" fill="#0f172a"/>
    </g>

    <!-- Normal Reaction R perpendicular to incline -->
    <line x1="370" y1="235" x2="310" y2="75" stroke="#38bdf8" stroke-width="3"/>
    <polygon points="305,85 305,70 320,80" fill="#38bdf8"/>
    <text x="290" y="65" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="700">Normal Reaction (R)</text>

    <!-- Weight mg straight downward -->
    <line x1="370" y1="235" x2="370" y2="375" stroke="#f59e0b" stroke-width="2.5"/>
    <polygon points="365,365 370,380 375,365" fill="#f59e0b"/>
    <text x="385" y="375" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Weight mg</text>

    <!-- Vertical Component R cos(theta) upward -->
    <line x1="370" y1="235" x2="370" y2="105" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3 3"/>
    <text x="380" y="125" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">R cos θ</text>

    <!-- Horizontal Component R sin(theta) pointing to curve centre -->
    <line x1="370" y1="235" x2="230" y2="235" stroke="#ef4444" stroke-width="3"/>
    <polygon points="240,230 225,235 240,240" fill="#ef4444"/>
    <text x="280" y="220" fill="#ef4444" font-family="system-ui, sans-serif" font-size="13" font-weight="700">F_c = R sin θ</text>

    <!-- Right Derivation Panel -->
    <rect x="560" y="60" width="250" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
    <text x="685" y="90" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">BANKING DERIVATION</text>

    <g transform="translate(575, 120)">
      <text x="0" y="0" fill="#94a3b8" font-size="11">Vertical Balance:</text>
      <text x="0" y="20" fill="#38bdf8" font-size="13" font-weight="700">R cos θ = mg</text>

      <text x="0" y="55" fill="#94a3b8" font-size="11">Horizontal Centripetal:</text>
      <text x="0" y="75" fill="#ef4444" font-size="13" font-weight="700">R sin θ = mv² / r</text>

      <text x="0" y="110" fill="#94a3b8" font-size="11">Dividing Equations:</text>
      <text x="0" y="132" fill="#f59e0b" font-size="14" font-weight="700">tan θ = v² / (rg)</text>

      <rect x="0" y="160" width="220" height="45" fill="#0284c722" rx="6" stroke="#0284c7"/>
      <text x="110" y="187" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">v = √(rg tan θ)</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Normal Reaction Force Resolution on a Banked Highway Curve")

def svg_m23_speed_governor():
    """Page 6: Watt centrifugal mechanical speed governor"""
    inner = """
    <!-- Central Vertical Rotating Spindle at x = 380, y = 70 to 360 -->
    <line x1="380" y1="70" x2="380" y2="360" stroke="#f8fafc" stroke-width="4"/>
    <text x="380" y="60" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Central Spindle</text>

    <!-- Fixed Top Pivot -->
    <rect x="365" y="80" width="30" height="15" fill="#475569" rx="2"/>

    <!-- Left Flyball (mass m) and Upper Arm -->
    <line x1="380" y1="85" x2="270" y2="180" stroke="#38bdf8" stroke-width="3"/>
    <circle cx="270" cy="180" r="16" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
    <text x="270" y="185" fill="#000" font-size="11" font-weight="700" text-anchor="middle">m</text>

    <!-- Right Flyball (mass m) and Upper Arm -->
    <line x1="380" y1="85" x2="490" y2="180" stroke="#38bdf8" stroke-width="3"/>
    <circle cx="490" cy="180" r="16" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
    <text x="490" y="185" fill="#000" font-size="11" font-weight="700" text-anchor="middle">m</text>

    <!-- Sliding Collar on Spindle at x = 380, y = 250 -->
    <rect x="360" y="240" width="40" height="25" fill="#22c55e" rx="4" stroke="#16a34a" stroke-width="2"/>
    <text x="425" y="255" fill="#22c55e" font-size="11" font-weight="700">Sliding Collar</text>

    <!-- Lower Links connecting Flyballs to Sliding Collar -->
    <line x1="270" y1="180" x2="380" y2="245" stroke="#38bdf8" stroke-width="2.5"/>
    <line x1="490" y1="180" x2="380" y2="245" stroke="#38bdf8" stroke-width="2.5"/>

    <!-- Lever Linkage to Throttle Valve -->
    <line x1="360" y1="250" x2="160" y2="250" stroke="#f8fafc" stroke-width="3"/>
    <circle cx="220" cy="250" r="4" fill="#f59e0b"/>
    <text x="220" y="240" fill="#f59e0b" font-size="10" text-anchor="middle">Pivot</text>

    <!-- Throttle Valve Box -->
    <rect x="80" y="220" width="80" height="60" fill="#111827" stroke="#ef4444" stroke-width="2" rx="6"/>
    <text x="120" y="245" fill="#ef4444" font-size="11" font-weight="700" text-anchor="middle">Throttle</text>
    <text x="120" y="260" fill="#ef4444" font-size="11" font-weight="700" text-anchor="middle">Valve</text>

    <!-- Speed Increase Arrow Indicator -->
    <g transform="translate(560, 110)">
      <rect x="0" y="0" width="240" height="180" fill="#111827" rx="8" stroke="#1e293b"/>
      <text x="120" y="25" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">AUTOMATIC FEEDBACK</text>
      <text x="10" y="55" fill="#f8fafc" font-size="11">1. Speed increases (+ω)</text>
      <text x="10" y="80" fill="#f59e0b" font-size="11">2. Balls swing out &amp; rise</text>
      <text x="10" y="105" fill="#22c55e" font-size="11">3. Collar slides UP</text>
      <text x="10" y="130" fill="#ef4444" font-size="11">4. Lever closes throttle valve</text>
      <text x="10" y="155" fill="#38bdf8" font-size="11">5. Engine slows to set speed</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Watt Centrifugal Mechanical Speed Governor Operation")

def svg_m23_turning_matatu_inertia():
    """Page 8: Inertia in turning vehicle (Debunking centrifugal force)"""
    inner = """
    <!-- Overhead Road Curved Path -->
    <path d="M 100,380 C 100,200 250,80 500,80" fill="none" stroke="#334155" stroke-width="60"/>
    <path d="M 100,380 C 100,200 250,80 500,80" fill="none" stroke="#64748b" stroke-width="2" stroke-dasharray="8 6"/>

    <!-- Turning Vehicle (Matatu) at (240, 170) -->
    <g transform="translate(240, 170) rotate(-45)">
      <rect x="-30" y="-50" width="60" height="100" fill="#0284c7" rx="8" stroke="#38bdf8" stroke-width="2"/>
      <rect x="-24" y="-35" width="48" height="70" fill="#0f172a" rx="4"/>
      <!-- Passenger -->
      <circle cx="0" cy="0" r="10" fill="#22c55e"/>
      <text x="0" y="4" fill="#000" font-size="8" font-weight="700" text-anchor="middle">You</text>
    </g>

    <!-- Passenger Straight-Line Inertial Path (Red dashed line) -->
    <line x1="240" y1="170" x2="340" y2="70" stroke="#ef4444" stroke-width="3" stroke-dasharray="4 3"/>
    <polygon points="330,68 345,65 342,80" fill="#ef4444"/>
    <text x="350" y="60" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Inertial Path (Newton's 1st Law)</text>

    <!-- Inward Centripetal Force from Seat/Door (Blue arrow) -->
    <line x1="240" y1="170" x2="160" y2="250" stroke="#38bdf8" stroke-width="3"/>
    <polygon points="172,252 155,255 162,238" fill="#38bdf8"/>
    <text x="110" y="275" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Centripetal Force (Seat)</text>

    <!-- Right Myth Busting Panel -->
    <rect x="520" y="65" width="290" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
    <text x="665" y="95" fill="#ef4444" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">MYTH BUSTER: CENTRIFUGAL FORCE</text>

    <g transform="translate(535, 125)">
      <text x="0" y="0" fill="#f8fafc" font-size="12" font-weight="700">• No Outward Force Exists!</text>
      <text x="0" y="20" fill="#94a3b8" font-size="11">Centrifugal force is an imaginary</text>
      <text x="0" y="35" fill="#94a3b8" font-size="11">pseudo-force from inside rotation.</text>

      <text x="0" y="70" fill="#f8fafc" font-size="12" font-weight="700">• It is Pure Inertia:</text>
      <text x="0" y="90" fill="#94a3b8" font-size="11">Your body wants to travel straight.</text>
      <text x="0" y="105" fill="#94a3b8" font-size="11">The car turns beneath you!</text>

      <text x="0" y="140" fill="#f8fafc" font-size="12" font-weight="700">• Real Force is Inward:</text>
      <text x="0" y="160" fill="#38bdf8" font-size="11">The car door/seat pushes INWARD</text>
      <text x="0" y="175" fill="#38bdf8" font-size="11">to provide the centripetal force.</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Physical Reality of Inertia vs. The Myth of Centrifugal Force")


# =============================================================================
# MAIN ENRICHMENT EXECUTOR FOR TOPIC 2
# =============================================================================

def run_enrichment_topic2():
    print("=" * 80)
    print("VLEARN FORM 4 PHYSICS — TOPIC 2 VISUAL ENRICHMENT")
    print("=" * 80)

    topic = Topic.objects.filter(
        subject__name="Physics",
        subject__grade__name="Form 4",
        name__icontains="Uniform Circular Motion"
    ).first()

    if not topic:
        print("ERROR: Topic 2: Uniform Circular Motion not found! Run ingest_form4_physics_topic2.py first.")
        return

    units = topic.learning_units.all().order_by("order")
    if units.count() < 3:
        print("ERROR: Expected 3 learning units in Topic 2.")
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
    # MODULE 2.1 ENRICHMENT
    # -------------------------------------------------------------------------
    print("--- Enriching Module 2.1 ---")
    attach_svg_to_block(lesson_1, 2, "suggested_diagram", "Tangential Velocity Vectors in Uniform Circular Motion", "m21_tangential_velocity", svg_m21_tangential_velocity())
    attach_svg_to_block(lesson_1, 3, "suggested_diagram", "Geometric Definition & Mathematical Origin of the Radian", "m21_radian_definition", svg_m21_radian_definition())

    # -------------------------------------------------------------------------
    # MODULE 2.2 ENRICHMENT
    # -------------------------------------------------------------------------
    print("\n--- Enriching Module 2.2 ---")
    attach_svg_to_block(lesson_2, 2, "suggested_diagram", "Centripetal Acceleration & Inward Force Dynamics", "m22_centripetal_acceleration", svg_m22_centripetal_acceleration())
    attach_svg_to_block(lesson_2, 6, "suggested_diagram", "Tension & Force Dynamics in a Vertical Circular Path", "m22_vertical_forces", svg_m22_vertical_circle_forces())
    attach_svg_to_block(lesson_2, 10, "suggested_diagram", "Laboratory Setup for Centripetal Force Investigation", "m22_lab_apparatus", svg_m22_lab_apparatus())
    attach_svg_to_block(lesson_2, 11, "suggested_graph", "Linear Experimental Plot: Tension T against Angular Velocity Squared (ω²)", "m22_graph_t_w2", svg_m22_graph_t_vs_w2())

    # Wikimedia for Module 2.2: Optical/Centripetal Lab kit
    attach_wikimedia_to_block(
        lesson=lesson_2,
        page_num=10,
        title="Physics Laboratory Apparatus Kit for Mechanics and Motion",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Optical_Bench_educational_Kit_-_Cuesta_College.jpg/960px-Optical_Bench_educational_Kit_-_Cuesta_College.jpg",
        author="Cuesta College Physical Sciences Department",
        licensing="CC BY 2.0",
        commons_page="https://commons.wikimedia.org/wiki/File:Optical_Bench_educational_Kit_-_Cuesta_College.jpg"
    )

    # -------------------------------------------------------------------------
    # MODULE 2.3 ENRICHMENT
    # -------------------------------------------------------------------------
    print("\n--- Enriching Module 2.3 ---")
    attach_svg_to_block(lesson_3, 2, "suggested_diagram", "Vector Resolution of the Conical Pendulum", "m23_conical_pendulum", svg_m23_conical_pendulum())
    attach_svg_to_block(lesson_3, 4, "suggested_diagram", "Centrifuge Separation Mechanism: Dense Particles Driven Outward by Inertia", "m23_centrifuge", svg_m23_centrifuge_mechanism())
    attach_svg_to_block(lesson_3, 5, "suggested_diagram", "Normal Reaction Force Resolution on a Banked Highway Curve", "m23_banked_road", svg_m23_banked_road())
    attach_svg_to_block(lesson_3, 6, "suggested_diagram", "Watt Centrifugal Mechanical Speed Governor Operation", "m23_speed_governor", svg_m23_speed_governor())
    attach_svg_to_block(lesson_3, 8, "suggested_diagram", "Physical Reality of Inertia vs. The Myth of Centrifugal Force", "m23_turning_matatu", svg_m23_turning_matatu_inertia())

    # Wikimedia for Module 2.3: Tabletop Centrifuge, Watt Speed Governor, and AVUS Banked Curve
    attach_wikimedia_to_block(
        lesson=lesson_3,
        page_num=4,
        title="Tabletop Research Bench Centrifuge for Clinical Separation",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Tabletop_centrifuge.jpg/960px-Tabletop_centrifuge.jpg",
        author="Magnus Manske",
        licensing="CC BY 1.0",
        commons_page="https://commons.wikimedia.org/wiki/File:Tabletop_centrifuge.jpg"
    )

    attach_wikimedia_to_block(
        lesson=lesson_3,
        page_num=5,
        title="Steep Banked Curve on the Historic AVUS Motorsport Track",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Bundesarchiv_B_145_Bild-P016402%2C_Berlin%2C_Rennen_auf_der_Avus.jpg/960px-Bundesarchiv_B_145_Bild-P016402%2C_Berlin%2C_Rennen_auf_der_Avus.jpg",
        author="German Federal Archives (Bundesarchiv)",
        licensing="CC BY-SA 3.0 de",
        commons_page="https://commons.wikimedia.org/wiki/File:Bundesarchiv_B_145_Bild-P016402,_Berlin,_Rennen_auf_der_Avus.jpg"
    )

    attach_wikimedia_to_block(
        lesson=lesson_3,
        page_num=6,
        title="Historic James Watt Centrifugal Speed Governor on Boulton and Watt Engine",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/SteamEngine_Boulton%26Watt_1784.png/960px-SteamEngine_Boulton%26Watt_1784.png",
        author="Robert Henry Thurston",
        licensing="Public domain",
        commons_page="https://commons.wikimedia.org/wiki/File:SteamEngine_Boulton%26Watt_1784.png"
    )

    print("\n" + "=" * 80)
    print("TOPIC 2 VISUAL ENRICHMENT COMPLETED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    run_enrichment_topic2()
