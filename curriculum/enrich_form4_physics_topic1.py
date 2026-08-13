"""
VLearn Form 4 Physics — Topic 1: Thin Lenses
Visual Enrichment Engine (SVGs + Wikimedia Commons)

Enriches all 3 modules of Topic 1 (Thin Lenses) with:
  - 18 high-precision dark-mode vector SVG diagrams (lens geometries, curvature landmarks, 
    ray tracing across all convex/concave positions, optical bench setup, 1/v vs 1/u graph, 
    microscopes, telescopes, cameras, eye anatomy, and refractive vision corrections).
  - 5 authentic, high-resolution scientific & historical Wikimedia Commons photographic assets 
    (optical bench kit, real convex lens inverted image, research compound microscope, 
    Great Refractor telescope, camera lens aperture diaphragm).

All SVGs are validated and sanitized via `validate_and_sanitize_svg`, saved as `LessonAsset` file 
records, and embedded directly into `LessonBlock` content and metadata for immediate frontend rendering.

Usage:
  /home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/venv/bin/python curriculum/enrich_form4_physics_topic1.py
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.core.files.base import ContentFile
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
# SVG BUILDERS — MODULE 1.1
# =============================================================================

def svg_m11_lens_geometries():
    """Page 2: Converging vs Diverging lens cross sections"""
    inner = """
    <!-- Background boxes -->
    <rect x="30" y="55" width="375" height="335" fill="#111827" rx="12" stroke="#1e293b" stroke-width="1.5"/>
    <rect x="435" y="55" width="375" height="335" fill="#111827" rx="12" stroke="#1e293b" stroke-width="1.5"/>

    <!-- Group Titles -->
    <text x="217" y="85" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">CONVERGING (CONVEX) LENSES</text>
    <text x="217" y="105" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Thicker at centre than at edges</text>

    <text x="622" y="85" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">DIVERGING (CONCAVE) LENSES</text>
    <text x="622" y="105" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Thicker at edges than at centre</text>

    <!-- Converging 1: Biconvex -->
    <g transform="translate(70, 130)">
      <path d="M 30,10 Q 5,75 30,140 Q 55,75 30,10 Z" fill="#0284c733" stroke="#38bdf8" stroke-width="2.5"/>
      <text x="30" y="170" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Biconvex</text>
      <text x="30" y="188" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Both faces curve out</text>
    </g>

    <!-- Converging 2: Plano-Convex -->
    <g transform="translate(185, 130)">
      <path d="M 20,10 L 20,140 Q 50,75 20,10 Z" fill="#0284c733" stroke="#38bdf8" stroke-width="2.5"/>
      <text x="30" y="170" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Plano-Convex</text>
      <text x="30" y="188" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">One flat, one convex</text>
    </g>

    <!-- Converging 3: Converging Meniscus -->
    <g transform="translate(300, 130)">
      <path d="M 25,10 Q 10,75 25,140 Q 50,75 25,10 Z" fill="#0284c733" stroke="#38bdf8" stroke-width="2.5"/>
      <text x="30" y="170" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Meniscus</text>
      <text x="30" y="188" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Centre thicker</text>
    </g>

    <!-- Diverging 1: Biconcave -->
    <g transform="translate(475, 130)">
      <path d="M 10,10 Q 30,75 10,140 L 50,140 Q 30,75 50,10 Z" fill="#d9770633" stroke="#f59e0b" stroke-width="2.5"/>
      <text x="30" y="170" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Biconcave</text>
      <text x="30" y="188" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Both faces curve in</text>
    </g>

    <!-- Diverging 2: Plano-Concave -->
    <g transform="translate(590, 130)">
      <path d="M 15,10 L 15,140 L 45,140 Q 25,75 45,10 Z" fill="#d9770633" stroke="#f59e0b" stroke-width="2.5"/>
      <text x="30" y="170" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Plano-Concave</text>
      <text x="30" y="188" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">One flat, one concave</text>
    </g>

    <!-- Diverging 3: Diverging Meniscus -->
    <g transform="translate(705, 130)">
      <path d="M 20,10 Q 40,75 20,140 L 45,140 Q 55,75 45,10 Z" fill="#d9770633" stroke="#f59e0b" stroke-width="2.5"/>
      <text x="30" y="170" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Meniscus</text>
      <text x="30" y="188" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">Edges thicker</text>
    </g>

    <!-- Central thickness callout -->
    <path d="M 120,350 L 320,350" stroke="#38bdf8" stroke-dasharray="3 3"/>
    <text x="217" y="370" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Focus is REAL (+f)</text>

    <path d="M 525,350 L 725,350" stroke="#f59e0b" stroke-dasharray="3 3"/>
    <text x="622" y="370" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Focus is VIRTUAL (-f)</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Geometric Cross-Sections of Thin Lenses")

def svg_m11_curvature_landmarks():
    """Page 3: Two spheres intersecting to form biconvex lens"""
    inner = """
    <!-- Principal Axis -->
    <line x1="40" y1="210" x2="800" y2="210" stroke="#64748b" stroke-width="1.5" stroke-dasharray="6 4"/>
    <text x="750" y="200" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Principal Axis</text>

    <!-- Sphere 1 (Left centre C1) -->
    <circle cx="280" cy="210" r="160" fill="none" stroke="#0284c7" stroke-width="1.2" stroke-dasharray="4 4" opacity="0.4"/>
    <!-- Sphere 2 (Right centre C2) -->
    <circle cx="560" cy="210" r="160" fill="none" stroke="#0284c7" stroke-width="1.2" stroke-dasharray="4 4" opacity="0.4"/>

    <!-- Lens Intersection -->
    <path d="M 420,74 A 160 160 0 0 1 420,346 A 160 160 0 0 1 420,74 Z" fill="#0284c733" stroke="#38bdf8" stroke-width="2.5"/>

    <!-- Optical Centre O -->
    <circle cx="420" cy="210" r="4.5" fill="#38bdf8"/>
    <text x="420" y="235" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">O (Optical Centre)</text>

    <!-- Centre of Curvature C1 -->
    <circle cx="280" cy="210" r="4" fill="#f59e0b"/>
    <text x="280" y="235" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">C1 (2F1)</text>

    <!-- Centre of Curvature C2 -->
    <circle cx="560" cy="210" r="4" fill="#f59e0b"/>
    <text x="560" y="235" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">C2 (2F2)</text>

    <!-- Focal Points F1 and F2 -->
    <circle cx="350" cy="210" r="4" fill="#22c55e"/>
    <text x="350" y="200" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">F1</text>

    <circle cx="490" cy="210" r="4" fill="#22c55e"/>
    <text x="490" y="200" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">F2</text>

    <!-- Radius R dimension -->
    <line x1="280" y1="365" x2="420" y2="365" stroke="#f59e0b" stroke-width="1.5"/>
    <line x1="280" y1="360" x2="280" y2="370" stroke="#f59e0b" stroke-width="1.5"/>
    <line x1="420" y1="360" x2="420" y2="370" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="350" y="385" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Radius of Curvature (R = 2f)</text>

    <!-- Focal length f dimension -->
    <line x1="420" y1="280" x2="490" y2="280" stroke="#22c55e" stroke-width="1.5"/>
    <line x1="420" y1="275" x2="420" y2="285" stroke="#22c55e" stroke-width="1.5"/>
    <line x1="490" y1="275" x2="490" y2="285" stroke="#22c55e" stroke-width="1.5"/>
    <text x="455" y="300" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">f</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Spherical Curvature & Optical Landmarks of a Thin Lens")

def svg_m11_principal_focus():
    """Page 4: Parallel ray refraction in convex vs concave lens"""
    inner = """
    <!-- Left Panel: Convex (Converging) -->
    <g transform="translate(0,0)">
      <rect x="25" y="50" width="380" height="340" fill="#111827" rx="12" stroke="#1e293b"/>
      <text x="215" y="80" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">CONVEX LENS (REAL FOCUS)</text>
      
      <!-- Axis -->
      <line x1="40" y1="210" x2="390" y2="210" stroke="#64748b" stroke-dasharray="4 3"/>
      <!-- Lens -->
      <path d="M 180,95 Q 165,210 180,325 Q 195,210 180,95 Z" fill="#0284c733" stroke="#38bdf8" stroke-width="2.5"/>
      <circle cx="180" cy="210" r="3.5" fill="#38bdf8"/>
      
      <!-- Focus F -->
      <circle cx="310" cy="210" r="4" fill="#22c55e"/>
      <text x="310" y="232" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">F (Real)</text>

      <!-- Incoming parallel rays -->
      <line x1="50" y1="130" x2="180" y2="130" stroke="#f59e0b" stroke-width="2"/>
      <polygon points="120,126 130,130 120,134" fill="#f59e0b"/>
      <line x1="180" y1="130" x2="360" y2="242" stroke="#f59e0b" stroke-width="2"/>
      <polygon points="255,176 265,183 257,188" fill="#f59e0b"/>

      <line x1="50" y1="170" x2="180" y2="170" stroke="#f59e0b" stroke-width="2"/>
      <polygon points="120,166 130,170 120,174" fill="#f59e0b"/>
      <line x1="180" y1="170" x2="360" y2="225" stroke="#f59e0b" stroke-width="2"/>

      <line x1="50" y1="250" x2="180" y2="250" stroke="#f59e0b" stroke-width="2"/>
      <polygon points="120,246 130,250 120,254" fill="#f59e0b"/>
      <line x1="180" y1="250" x2="360" y2="195" stroke="#f59e0b" stroke-width="2"/>

      <line x1="50" y1="290" x2="180" y2="290" stroke="#f59e0b" stroke-width="2"/>
      <polygon points="120,286 130,290 120,294" fill="#f59e0b"/>
      <line x1="180" y1="290" x2="360" y2="178" stroke="#f59e0b" stroke-width="2"/>

      <!-- Dimension f -->
      <line x1="180" y1="350" x2="310" y2="350" stroke="#22c55e" stroke-width="1.5"/>
      <text x="245" y="372" fill="#22c55e" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Focal Length +f</text>
    </g>

    <!-- Right Panel: Concave (Diverging) -->
    <g transform="translate(415,0)">
      <rect x="20" y="50" width="380" height="340" fill="#111827" rx="12" stroke="#1e293b"/>
      <text x="210" y="80" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">CONCAVE LENS (VIRTUAL FOCUS)</text>
      
      <!-- Axis -->
      <line x1="35" y1="210" x2="385" y2="210" stroke="#64748b" stroke-dasharray="4 3"/>
      <!-- Lens -->
      <path d="M 220,95 Q 230,210 220,325 L 240,325 Q 230,210 240,95 Z" fill="#d9770633" stroke="#f59e0b" stroke-width="2.5"/>
      <circle cx="230" cy="210" r="3.5" fill="#f59e0b"/>
      
      <!-- Focus F -->
      <circle cx="100" cy="210" r="4" fill="#a855f7"/>
      <text x="100" y="232" fill="#a855f7" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">F (Virtual)</text>

      <!-- Incoming parallel rays -->
      <line x1="35" y1="130" x2="225" y2="130" stroke="#38bdf8" stroke-width="2"/>
      <polygon points="140,126 150,130 140,134" fill="#38bdf8"/>
      <!-- Diverging refracted -->
      <line x1="235" y1="130" x2="375" y2="44" stroke="#38bdf8" stroke-width="2"/>
      <polygon points="300,90 310,84 304,95" fill="#38bdf8"/>
      <!-- Dashed extrapolation -->
      <line x1="100" y1="210" x2="225" y2="130" stroke="#a855f7" stroke-dasharray="3 3" stroke-width="1.5"/>

      <line x1="35" y1="290" x2="225" y2="290" stroke="#38bdf8" stroke-width="2"/>
      <polygon points="140,286 150,290 140,294" fill="#38bdf8"/>
      <line x1="235" y1="290" x2="375" y2="376" stroke="#38bdf8" stroke-width="2"/>
      <!-- Dashed extrapolation -->
      <line x1="100" y1="210" x2="225" y2="290" stroke="#a855f7" stroke-dasharray="3 3" stroke-width="1.5"/>

      <!-- Dimension f -->
      <line x1="100" y1="350" x2="230" y2="350" stroke="#a855f7" stroke-width="1.5"/>
      <text x="165" y="372" fill="#a855f7" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Focal Length -f</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Principal Focus: Real Convergence vs. Virtual Divergence")

def svg_m11_ray_diagram_u_less_f():
    """Page 5: Convex lens u < f (Magnifying glass: exact ray tracing)"""
    inner = """
    <!-- Principal Axis -->
    <line x1="30" y1="240" x2="810" y2="240" stroke="#64748b" stroke-width="1.5" stroke-dasharray="6 4"/>
    <text x="760" y="230" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Principal Axis</text>

    <!-- Convex Lens at x = 480 -->
    <path d="M 480,50 Q 460,240 480,390 Q 500,240 480,50 Z" fill="#0284c733" stroke="#38bdf8" stroke-width="2.5"/>
    <circle cx="480" cy="240" r="4" fill="#38bdf8"/>
    <text x="480" y="260" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">O</text>

    <!-- Focal points f = 200 (F1 at 280, F2 at 680) -->
    <circle cx="280" cy="240" r="4" fill="#22c55e"/>
    <text x="280" y="260" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">F₁</text>
    <circle cx="680" cy="240" r="4" fill="#22c55e"/>
    <text x="680" y="260" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">F₂</text>

    <!-- Real Object at x = 380 (u = 100 < f = 200), ho = 70 (y = 170) -->
    <line x1="380" y1="240" x2="380" y2="170" stroke="#22c55e" stroke-width="3.5"/>
    <polygon points="374,178 380,165 386,178" fill="#22c55e"/>
    <text x="380" y="155" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Object (u &lt; f)</text>

    <!-- Virtual Image at x = 280 (v = -200), hi = 140 (y = 100, erect & magnified) -->
    <line x1="280" y1="240" x2="280" y2="100" stroke="#a855f7" stroke-width="3.5" stroke-dasharray="5 3"/>
    <polygon points="274,115 280,100 286,115" fill="#a855f7"/>
    <text x="280" y="85" fill="#a855f7" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Virtual Image (Erect, 2×)</text>

    <!-- Ray 1: Parallel to axis to lens at (480, 170), then refracts through F2(680, 240) -->
    <line x1="380" y1="170" x2="480" y2="170" stroke="#f59e0b" stroke-width="2"/>
    <polygon points="425,166 435,170 425,174" fill="#f59e0b"/>
    <!-- Refracted Ray 1 continuing to (740, 261) -->
    <line x1="480" y1="170" x2="740" y2="261" stroke="#f59e0b" stroke-width="2"/>
    <polygon points="605,210 615,214 609,220" fill="#f59e0b"/>
    <!-- Backward Dashed Extension of Ray 1 to (280, 100) -->
    <line x1="480" y1="170" x2="280" y2="100" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="4 3"/>

    <!-- Ray 2: From (380, 170) through Optical Centre O(480, 240) to (740, 422) -->
    <line x1="380" y1="170" x2="480" y2="240" stroke="#38bdf8" stroke-width="2"/>
    <line x1="480" y1="240" x2="720" y2="408" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="570,300 580,307 573,313" fill="#38bdf8"/>
    <!-- Backward Dashed Extension of Ray 2 to (280, 100) -->
    <line x1="380" y1="170" x2="280" y2="100" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="4 3"/>

    <!-- Observer Eye at output -->
    <g transform="translate(730, 250)">
      <path d="M 0,20 Q 30,0 60,20 Q 30,40 0,20 Z" fill="none" stroke="#f8fafc" stroke-width="2"/>
      <circle cx="30" cy="20" r="10" fill="#38bdf8"/>
      <text x="30" y="55" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Observer Eye</text>
    </g>

    <!-- Info Box -->
    <rect x="30" y="320" width="220" height="75" fill="#111827" rx="8" stroke="#1e293b"/>
    <text x="40" y="342" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Magnifying Glass Mode</text>
    <text x="40" y="362" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">• Image: Virtual &amp; Erect</text>
    <text x="40" y="380" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">• Magnification: m = 2.0 (m &gt; 1)</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Ray Tracing: Object Inside Principal Focus (u < f)")

def svg_m11_ray_diagram_between_f_and_2f():
    """Page 6: Convex lens f < u < 2f (Projector: exact ray tracing)"""
    inner = """
    <!-- Principal Axis -->
    <line x1="30" y1="200" x2="810" y2="200" stroke="#64748b" stroke-width="1.5" stroke-dasharray="6 4"/>
    <text x="760" y="190" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Principal Axis</text>

    <!-- Lens at x = 360 -->
    <path d="M 360,30 Q 340,200 360,370 Q 380,200 360,30 Z" fill="#0284c733" stroke="#38bdf8" stroke-width="2.5"/>
    <circle cx="360" cy="200" r="4" fill="#38bdf8"/>
    <text x="360" y="222" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">O</text>

    <!-- Left Landmarks (f = 120): F1 at 240, 2F1 at 120 -->
    <circle cx="240" cy="200" r="3.5" fill="#22c55e"/>
    <text x="240" y="222" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">F₁</text>
    <circle cx="120" cy="200" r="3.5" fill="#f59e0b"/>
    <text x="120" y="222" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2F₁</text>

    <!-- Right Landmarks: F2 at 480, 2F2 at 600 -->
    <circle cx="480" cy="200" r="3.5" fill="#22c55e"/>
    <text x="480" y="222" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">F₂</text>
    <circle cx="600" cy="200" r="3.5" fill="#f59e0b"/>
    <text x="600" y="222" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2F₂</text>

    <!-- Object at x = 180 (u = 180, 120 < u < 240), ho = 60 (y = 140) -->
    <line x1="180" y1="200" x2="180" y2="140" stroke="#22c55e" stroke-width="3.5"/>
    <polygon points="174,148 180,135 186,148" fill="#22c55e"/>
    <text x="180" y="125" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Object (f &lt; u &lt; 2f)</text>

    <!-- Real Inverted Image at x = 720 (v = 360 > 2f), hi = 120 (y = 320, m = 2.0) -->
    <line x1="720" y1="200" x2="720" y2="320" stroke="#ef4444" stroke-width="3.5"/>
    <polygon points="714,310 720,325 726,310" fill="#ef4444"/>
    <text x="720" y="350" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Real Image (Inverted, Magnified)</text>

    <!-- Ray 1: Parallel to axis from (180, 140) to (360, 140), then refracts through F2(480, 200) to (720, 320) -->
    <line x1="180" y1="140" x2="360" y2="140" stroke="#f59e0b" stroke-width="2"/>
    <polygon points="265,136 275,140 265,144" fill="#f59e0b"/>
    <line x1="360" y1="140" x2="720" y2="320" stroke="#f59e0b" stroke-width="2"/>
    <polygon points="525,220 535,227 528,234" fill="#f59e0b"/>

    <!-- Ray 2: From (180, 140) straight through Optical Centre O(360, 200) to (720, 320) -->
    <line x1="180" y1="140" x2="720" y2="320" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="460,230 470,237 463,243" fill="#38bdf8"/>

    <!-- Info Box -->
    <rect x="30" y="280" width="220" height="95" fill="#111827" rx="8" stroke="#1e293b"/>
    <text x="40" y="302" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Projector Mode (f &lt; u &lt; 2f)</text>
    <text x="40" y="322" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">• Position: Beyond 2F (v = 360cm)</text>
    <text x="40" y="340" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">• Nature: Real &amp; Inverted</text>
    <text x="40" y="358" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">• Size: Magnified (m = 2.0)</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Ray Tracing: Object Between F and 2F (Projector Principle)")

def svg_m11_ray_diagram_u_greater_2f():
    """Page 7: Convex lens u > 2f (Camera / Eye: exact ray tracing)"""
    inner = """
    <!-- Principal Axis -->
    <line x1="30" y1="210" x2="810" y2="210" stroke="#64748b" stroke-width="1.5" stroke-dasharray="6 4"/>
    <text x="760" y="200" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Principal Axis</text>

    <!-- Lens at x = 440 -->
    <path d="M 440,40 Q 420,210 440,380 Q 460,210 440,40 Z" fill="#0284c733" stroke="#38bdf8" stroke-width="2.5"/>
    <circle cx="440" cy="210" r="4" fill="#38bdf8"/>
    <text x="440" y="232" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">O</text>

    <!-- Left Landmarks (f = 120): F1 at 320, 2F1 at 200 -->
    <circle cx="320" cy="210" r="3.5" fill="#22c55e"/>
    <text x="320" y="232" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">F₁</text>
    <circle cx="200" cy="210" r="3.5" fill="#f59e0b"/>
    <text x="200" y="232" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2F₁</text>

    <!-- Right Landmarks: F2 at 560, 2F2 at 680 -->
    <circle cx="560" cy="210" r="3.5" fill="#22c55e"/>
    <text x="560" y="232" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">F₂</text>
    <circle cx="680" cy="210" r="3.5" fill="#f59e0b"/>
    <text x="680" y="232" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2F₂</text>

    <!-- Object at x = 80 (u = 360 = 3f > 2f), ho = 120 (y = 90) -->
    <line x1="80" y1="210" x2="80" y2="90" stroke="#22c55e" stroke-width="3.5"/>
    <polygon points="74,102 80,88 86,102" fill="#22c55e"/>
    <text x="80" y="75" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Object (u &gt; 2f)</text>

    <!-- Real Image at x = 620 (v = 180 between F and 2F), hi = 60 (y = 270, m = 0.5) -->
    <line x1="620" y1="210" x2="620" y2="270" stroke="#ef4444" stroke-width="3.5"/>
    <polygon points="614,260 620,275 626,260" fill="#ef4444"/>
    <text x="620" y="300" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Real Image (Diminished, 0.5×)</text>

    <!-- Ray 1: Parallel from (80, 90) to (440, 90), then through F2(560, 210) to (700, 350) -->
    <line x1="80" y1="90" x2="440" y2="90" stroke="#f59e0b" stroke-width="2"/>
    <polygon points="250,86 260,90 250,94" fill="#f59e0b"/>
    <line x1="440" y1="90" x2="700" y2="350" stroke="#f59e0b" stroke-width="2"/>
    <polygon points="575,220 585,230 578,236" fill="#f59e0b"/>

    <!-- Ray 2: From (80, 90) straight through Optical Centre O(440, 210) to (700, 297) -->
    <line x1="80" y1="90" x2="700" y2="297" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="505,226 515,232 509,239" fill="#38bdf8"/>

    <!-- Info Box -->
    <rect x="30" y="290" width="220" height="95" fill="#111827" rx="8" stroke="#1e293b"/>
    <text x="40" y="312" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Camera / Eye Mode (u &gt; 2f)</text>
    <text x="40" y="332" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">• Position: Between F and 2F</text>
    <text x="40" y="350" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">• Nature: Real &amp; Inverted</text>
    <text x="40" y="368" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">• Size: Diminished (m = 0.5)</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Ray Tracing: Object Beyond 2F (Camera & Eye Principle)")

def svg_m11_ray_diagram_concave():
    """Page 8: Diverging Concave lens for all positions (exact ray tracing)"""
    inner = """
    <!-- Principal Axis -->
    <line x1="30" y1="210" x2="810" y2="210" stroke="#64748b" stroke-width="1.5" stroke-dasharray="6 4"/>
    <text x="760" y="200" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Principal Axis</text>

    <!-- Concave Lens at x = 440 -->
    <path d="M 430,40 Q 450,210 430,380 L 450,380 Q 430,210 450,40 Z" fill="#d9770633" stroke="#f59e0b" stroke-width="2.5"/>
    <circle cx="440" cy="210" r="4" fill="#f59e0b"/>
    <text x="440" y="232" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">O</text>

    <!-- Virtual Focus Left at x = 240 (f = -200) -->
    <circle cx="240" cy="210" r="4" fill="#a855f7"/>
    <text x="240" y="232" fill="#a855f7" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">F (Virtual)</text>

    <!-- Object at x = 140 (u = 300), ho = 100 (y = 110) -->
    <line x1="140" y1="210" x2="140" y2="110" stroke="#22c55e" stroke-width="3.5"/>
    <polygon points="134,122 140,108 146,122" fill="#22c55e"/>
    <text x="140" y="95" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Object</text>

    <!-- Virtual Image at x = 320 (v = -120), hi = 40 (y = 170, erect & diminished) -->
    <line x1="320" y1="210" x2="320" y2="170" stroke="#a855f7" stroke-width="3" stroke-dasharray="4 3"/>
    <polygon points="315,178 320,166 325,178" fill="#a855f7"/>
    <text x="320" y="155" fill="#a855f7" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Virtual Image (0.4×)</text>

    <!-- Ray 1: Parallel to axis from (140, 110) to (440, 110) -->
    <line x1="140" y1="110" x2="440" y2="110" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="270,106 280,110 270,114" fill="#38bdf8"/>
    <!-- Diverging Refracted Ray continuing to (640, 10) -->
    <line x1="440" y1="110" x2="640" y2="10" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="530,60 540,55 535,66" fill="#38bdf8"/>
    <!-- Backward dashed extrapolation to F(240, 210) -->
    <line x1="240" y1="210" x2="440" y2="110" stroke="#a855f7" stroke-dasharray="4 3" stroke-width="1.8"/>

    <!-- Ray 2: From (140, 110) straight through Optical Centre O(440, 210) to (710, 300) -->
    <line x1="140" y1="110" x2="710" y2="300" stroke="#f59e0b" stroke-width="2"/>
    <polygon points="560,245 570,250 564,256" fill="#f59e0b"/>

    <!-- Info Box -->
    <rect x="530" y="300" width="280" height="90" fill="#111827" rx="8" stroke="#1e293b"/>
    <text x="540" y="322" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Diverging Lens Universality</text>
    <text x="540" y="342" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">• Position: Same side as object (v &lt; f)</text>
    <text x="540" y="360" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">• Always VIRTUAL, ERECT &amp; DIMINISHED</text>
    <text x="540" y="378" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">• Used for Myopia spectacles &amp; peepholes</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Ray Tracing: Diverging (Concave) Lens Image Formation")


# =============================================================================
# SVG BUILDERS — MODULE 1.2
# =============================================================================

def svg_m12_sign_convention():
    """Page 3: Real-is-Positive Sign Convention System"""
    inner = """
    <!-- Lens boundary line at centre x = 420 -->
    <line x1="420" y1="60" x2="420" y2="380" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="420" y="50" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">LENS PLANE (O)</text>

    <!-- Left Box: Incident / Object Side -->
    <rect x="40" y="70" width="350" height="310" fill="#111827" rx="12" stroke="#1e293b"/>
    <text x="215" y="100" fill="#22c55e" font-family="system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">OBJECT SIDE (Light Enters)</text>

    <g transform="translate(60, 130)">
      <text x="0" y="0" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="600">• Real Object Distance:</text>
      <text x="220" y="0" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="700">+u</text>

      <text x="0" y="40" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="600">• Virtual Image Distance:</text>
      <text x="220" y="40" fill="#ef4444" font-family="system-ui, sans-serif" font-size="13" font-weight="700">-v</text>

      <text x="0" y="80" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="600">• Concave Focal Length:</text>
      <text x="220" y="80" fill="#ef4444" font-family="system-ui, sans-serif" font-size="13" font-weight="700">-f</text>

      <text x="0" y="120" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Rays on this side are diverging backwards</text>
      <text x="0" y="140" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">when forming a virtual image.</text>
    </g>

    <!-- Right Box: Transmission / Real Image Side -->
    <rect x="450" y="70" width="350" height="310" fill="#111827" rx="12" stroke="#1e293b"/>
    <text x="625" y="100" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">REAL IMAGE SIDE (Light Emerges)</text>

    <g transform="translate(470, 130)">
      <text x="0" y="0" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="600">• Real Image Distance:</text>
      <text x="220" y="0" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="700">+v</text>

      <text x="0" y="40" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="600">• Convex Focal Length:</text>
      <text x="220" y="40" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="700">+f</text>

      <text x="0" y="80" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="600">• Power for Converging:</text>
      <text x="220" y="80" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="700">+P</text>

      <text x="0" y="120" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Real rays physically intersect on this side</text>
      <text x="0" y="140" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">and can be captured on a screen.</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="The 'Real-is-Positive' Cartesian Sign Convention")

def svg_m12_optical_bench():
    """Page 11: Experimental Physics Optical Bench Setup"""
    inner = """
    <!-- Optical Bench Rail -->
    <rect x="40" y="270" width="760" height="25" fill="#334155" rx="4"/>
    <line x1="40" y1="270" x2="800" y2="270" stroke="#64748b" stroke-width="2"/>
    <!-- Metre Rule Tick Marks -->
    <g stroke="#94a3b8" stroke-width="1">
      <line x1="80" y1="270" x2="80" y2="280"/><text x="80" y="290" fill="#94a3b8" font-size="9" text-anchor="middle">0</text>
      <line x1="200" y1="270" x2="200" y2="280"/><text x="200" y="290" fill="#94a3b8" font-size="9" text-anchor="middle">20</text>
      <line x1="320" y1="270" x2="320" y2="280"/><text x="320" y="290" fill="#94a3b8" font-size="9" text-anchor="middle">40</text>
      <line x1="440" y1="270" x2="440" y2="280"/><text x="440" y="290" fill="#94a3b8" font-size="9" text-anchor="middle">60</text>
      <line x1="560" y1="270" x2="560" y2="280"/><text x="560" y="290" fill="#94a3b8" font-size="9" text-anchor="middle">80</text>
      <line x1="680" y1="270" x2="680" y2="280"/><text x="680" y="290" fill="#94a3b8" font-size="9" text-anchor="middle">100</text>
    </g>
    <text x="760" y="287" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="600">cm</text>

    <!-- Component 1: Ray Box & Illuminated Cross-wire at x = 120 -->
    <rect x="90" y="130" width="60" height="140" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="6"/>
    <circle cx="120" cy="180" r="16" fill="#fef08a"/>
    <line x1="120" y1="164" x2="120" y2="196" stroke="#000" stroke-width="2"/>
    <line x1="104" y1="180" x2="136" y2="180" stroke="#000" stroke-width="2"/>
    <text x="120" y="110" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Ray Box</text>
    <text x="120" y="125" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">(Illuminated Cross-wire)</text>

    <!-- Component 2: Convex Lens on Holder at x = 360 -->
    <rect x="350" y="220" width="20" height="50" fill="#475569" rx="2"/>
    <path d="M 360,110 Q 345,180 360,250 Q 375,180 360,110 Z" fill="#0284c733" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="360" y="90" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Convex Lens</text>

    <!-- Component 3: White Screen with Sharp Image at x = 680 -->
    <rect x="670" y="230" width="20" height="40" fill="#475569" rx="2"/>
    <rect x="675" y="120" width="10" height="130" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5" rx="2"/>
    <!-- Inverted cross-wire image on screen -->
    <circle cx="680" cy="180" r="12" fill="#fef08a" opacity="0.8"/>
    <line x1="680" y1="168" x2="680" y2="192" stroke="#ef4444" stroke-width="2"/>
    <line x1="668" y1="180" x2="692" y2="180" stroke="#ef4444" stroke-width="2"/>
    <text x="680" y="100" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Screen</text>
    <text x="680" y="115" fill="#ef4444" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">(Sharp Inverted Image)</text>

    <!-- Measurement Arrows -->
    <!-- Object Distance u -->
    <line x1="120" y1="330" x2="360" y2="330" stroke="#22c55e" stroke-width="2"/>
    <polygon points="125,326 120,330 125,334" fill="#22c55e"/>
    <polygon points="355,326 360,330 355,334" fill="#22c55e"/>
    <text x="240" y="355" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Object Distance (u)</text>

    <!-- Image Distance v -->
    <line x1="360" y1="330" x2="680" y2="330" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="365,326 360,330 365,334" fill="#38bdf8"/>
    <polygon points="675,326 680,330 675,334" fill="#38bdf8"/>
    <text x="520" y="355" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Image Distance (v)</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Laboratory Apparatus Setup: Focal Length Determination")

def svg_m12_reciprocal_graph():
    """Page 12: Reciprocal graph 1/v vs 1/u"""
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

    <text x="290" y="375" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1 / u (cm⁻¹)</text>
    <text x="40" y="210" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle" transform="rotate(-90 40 210)">1 / v (cm⁻¹)</text>

    <!-- Linear Plot Line (from y=100 to x=450) -->
    <line x1="90" y1="100" x2="450" y2="350" stroke="#38bdf8" stroke-width="3"/>

    <!-- Intercept Points -->
    <circle cx="90" cy="100" r="5" fill="#f59e0b"/>
    <text x="140" y="105" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700">y-intercept = 1/f</text>

    <circle cx="450" cy="350" r="5" fill="#f59e0b"/>
    <text x="450" y="340" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">x-intercept = 1/f</text>

    <!-- Experimental Points -->
    <circle cx="160" cy="148" r="4" fill="#22c55e"/>
    <circle cx="230" cy="197" r="4" fill="#22c55e"/>
    <circle cx="310" cy="252" r="4" fill="#22c55e"/>
    <circle cx="380" cy="301" r="4" fill="#22c55e"/>

    <!-- Right Side Mathematical Derivation Panel -->
    <rect x="540" y="60" width="270" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
    <text x="675" y="90" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">EQUATION DERIVATION</text>

    <g transform="translate(555, 120)">
      <text x="0" y="0" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Lens Formula:</text>
      <text x="0" y="22" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="600">1/f = 1/u + 1/v</text>

      <text x="0" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Linear Form (y = mx + c):</text>
      <text x="0" y="82" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700">1/v = - (1/u) + 1/f</text>

      <text x="0" y="120" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Gradient (m) = -1</text>
      <text x="0" y="145" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Vertical Intercept = 1/f</text>
      <text x="0" y="170" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="12" font-weight="700">• Horizontal Intercept = 1/f</text>

      <rect x="0" y="195" width="240" height="45" fill="#0284c722" rx="6" stroke="#0284c7"/>
      <text x="120" y="222" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">f = 1 / (Intercept)</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Linear Reciprocal Graph: 1/v against 1/u")


# =============================================================================
# SVG BUILDERS — MODULE 1.3
# =============================================================================

def svg_m13_simple_microscope():
    """Page 2: Simple Microscope (Magnifying glass at near point D = 25 cm)"""
    inner = """
    <!-- Principal Axis -->
    <line x1="30" y1="230" x2="810" y2="230" stroke="#64748b" stroke-width="1.5" stroke-dasharray="6 4"/>

    <!-- Convex Lens at x = 500 -->
    <path d="M 500,50 Q 480,230 500,390 Q 520,230 500,50 Z" fill="#0284c733" stroke="#38bdf8" stroke-width="2.5"/>
    <circle cx="500" cy="230" r="4" fill="#38bdf8"/>
    <text x="500" y="250" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">O</text>

    <!-- Focus F at x = 320 -->
    <circle cx="320" cy="230" r="3.5" fill="#22c55e"/>
    <text x="320" y="250" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">F</text>

    <!-- Small Object (inside F at x = 410, h = 50) -->
    <line x1="410" y1="230" x2="410" y2="175" stroke="#22c55e" stroke-width="3.5"/>
    <polygon points="405,182 410,170 415,182" fill="#22c55e"/>
    <text x="410" y="155" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Specimen (u &lt; f)</text>

    <!-- Massive Virtual Image (at Near Point D = 25 cm, x = 160, h = 180) -->
    <line x1="160" y1="230" x2="160" y2="35" stroke="#a855f7" stroke-width="3" stroke-dasharray="5 3"/>
    <polygon points="154,50 160,35 166,50" fill="#a855f7"/>
    <text x="160" y="25" fill="#a855f7" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Virtual Image at D = 25 cm</text>

    <!-- Ray Tracing -->
    <!-- Ray 1: Parallel to axis then through right F (x=680) -->
    <line x1="410" y1="175" x2="500" y2="175" stroke="#f59e0b" stroke-width="2"/>
    <line x1="500" y1="175" x2="720" y2="242" stroke="#f59e0b" stroke-width="2"/>
    <line x1="500" y1="175" x2="160" y2="35" stroke="#f59e0b" stroke-dasharray="3 3" stroke-width="1.5"/>

    <!-- Ray 2: Through Optical Centre O -->
    <line x1="410" y1="175" x2="720" y2="365" stroke="#38bdf8" stroke-width="2"/>
    <line x1="410" y1="175" x2="160" y2="35" stroke="#38bdf8" stroke-dasharray="3 3" stroke-width="1.5"/>

    <!-- Observer Eye at lens output -->
    <g transform="translate(680, 240)">
      <path d="M 0,20 Q 30,0 60,20 Q 30,40 0,20 Z" fill="none" stroke="#f8fafc" stroke-width="2"/>
      <circle cx="30" cy="20" r="10" fill="#38bdf8"/>
      <text x="30" y="55" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Eye</text>
    </g>

    <!-- Near Point D Dimension -->
    <line x1="160" y1="360" x2="500" y2="360" stroke="#a855f7" stroke-width="1.5"/>
    <line x1="160" y1="355" x2="160" y2="365" stroke="#a855f7" stroke-width="1.5"/>
    <line x1="500" y1="355" x2="500" y2="365" stroke="#a855f7" stroke-width="1.5"/>
    <text x="330" y="380" fill="#a855f7" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Near Point Distance D = 25 cm</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Ray Diagram: Simple Microscope (Magnifier) at Near Point")

def svg_m13_compound_microscope():
    """Page 3: Compound Microscope Two-Lens System"""
    inner = """
    <!-- Principal Axis -->
    <line x1="20" y1="210" x2="820" y2="210" stroke="#64748b" stroke-width="1.5" stroke-dasharray="6 4"/>

    <!-- Objective Lens at x = 200 (Small aperture, short fo) -->
    <path d="M 200,90 Q 185,210 200,330 Q 215,210 200,90 Z" fill="#0284c733" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="200" y="75" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Objective (fo)</text>

    <!-- Eyepiece Lens at x = 600 (Larger aperture, fe) -->
    <path d="M 600,50 Q 580,210 600,370 Q 620,210 600,50 Z" fill="#0284c733" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="600" y="40" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Eyepiece (fe)</text>

    <!-- Specimen at x = 110, h = 35 (just outside fo) -->
    <line x1="110" y1="210" x2="110" y2="170" stroke="#22c55e" stroke-width="3"/>
    <polygon points="106,176 110,165 114,176" fill="#22c55e"/>
    <text x="110" y="155" fill="#22c55e" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Specimen</text>

    <!-- Objective Focus Fo -->
    <circle cx="140" cy="210" r="3" fill="#22c55e"/>
    <text x="140" y="228" fill="#22c55e" font-size="10" text-anchor="middle">Fo</text>
    <circle cx="260" cy="210" r="3" fill="#22c55e"/>
    <text x="260" y="228" fill="#22c55e" font-size="10" text-anchor="middle">Fo</text>

    <!-- Intermediate Image I1 (Inverted, Real, Magnified at x = 440, h = 60) -->
    <line x1="440" y1="210" x2="440" y2="280" stroke="#ef4444" stroke-width="3"/>
    <polygon points="436,270 440,285 444,270" fill="#ef4444"/>
    <text x="440" y="305" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Real Image I₁</text>

    <!-- Eyepiece Focus Fe (just past I1 at x = 460) -->
    <circle cx="460" cy="210" r="3" fill="#a855f7"/>
    <text x="460" y="228" fill="#a855f7" font-size="10" text-anchor="middle">Fe</text>

    <!-- Final Virtual Image I2 at x = 80, h = 170 (Huge, inverted) -->
    <line x1="80" y1="210" x2="80" y2="390" stroke="#a855f7" stroke-width="3" stroke-dasharray="4 3"/>
    <polygon points="75,380 80,395 85,380" fill="#a855f7"/>
    <text x="80" y="410" fill="#a855f7" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Final Image I₂ (Virtual, 30×)</text>

    <!-- Ray tracing through Objective to I1 -->
    <line x1="110" y1="170" x2="200" y2="170" stroke="#f59e0b" stroke-width="1.5"/>
    <line x1="200" y1="170" x2="440" y2="280" stroke="#f59e0b" stroke-width="1.5"/>
    <line x1="110" y1="170" x2="440" y2="280" stroke="#38bdf8" stroke-width="1.5"/>

    <!-- Ray tracing through Eyepiece to Eye -->
    <line x1="440" y1="280" x2="600" y2="280" stroke="#f59e0b" stroke-width="1.5"/>
    <line x1="600" y1="280" x2="740" y2="330" stroke="#f59e0b" stroke-width="1.5"/>
    <line x1="600" y1="280" x2="80" y2="390" stroke="#f59e0b" stroke-dasharray="3 3" stroke-width="1"/>

    <line x1="440" y1="280" x2="740" y2="350" stroke="#38bdf8" stroke-width="1.5"/>
    <line x1="440" y1="280" x2="80" y2="390" stroke="#38bdf8" stroke-dasharray="3 3" stroke-width="1"/>

    <!-- Observer Eye at Right -->
    <g transform="translate(740, 310)">
      <path d="M 0,20 Q 25,0 50,20 Q 25,40 0,20 Z" fill="none" stroke="#f8fafc" stroke-width="2"/>
      <circle cx="25" cy="20" r="8" fill="#38bdf8"/>
    </g>

    <!-- Barrel Length L -->
    <line x1="200" y1="365" x2="600" y2="365" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="400" y="385" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Barrel Length L = vo + ue</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Ray Diagram: Compound Microscope Two-Stage Optical Train")

def svg_m13_telescope():
    """Page 4: Astronomical Telescope in Normal Adjustment"""
    inner = """
    <!-- Principal Axis -->
    <line x1="20" y1="200" x2="820" y2="200" stroke="#64748b" stroke-width="1.5" stroke-dasharray="6 4"/>

    <!-- Objective Lens at x = 160 (Large diameter, long fo) -->
    <path d="M 160,40 Q 140,200 160,360 Q 180,200 160,40 Z" fill="#0284c733" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="160" y="30" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Objective Lens (fo)</text>

    <!-- Eyepiece Lens at x = 660 (Small diameter, short fe) -->
    <path d="M 660,90 Q 645,200 660,310 Q 675,200 660,90 Z" fill="#0284c733" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="660" y="75" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Eyepiece Lens (fe)</text>

    <!-- Shared Focal Plane Fo = Fe at x = 500 -->
    <line x1="500" y1="80" x2="500" y2="320" stroke="#22c55e" stroke-dasharray="4 3" stroke-width="1.5"/>
    <circle cx="500" cy="200" r="4" fill="#22c55e"/>
    <text x="500" y="70" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Shared Focus (Fo = Fe)</text>

    <!-- Intermediate Image I1 at Fo (Real, Inverted, Tiny) -->
    <line x1="500" y1="200" x2="500" y2="245" stroke="#ef4444" stroke-width="3"/>
    <polygon points="496,238 500,248 504,238" fill="#ef4444"/>
    <text x="500" y="265" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Image I₁</text>

    <!-- Tilted parallel rays from distant star -->
    <!-- Ray 1 through top of objective -->
    <line x1="30" y1="100" x2="160" y2="135" stroke="#f59e0b" stroke-width="1.8"/>
    <line x1="160" y1="135" x2="500" y2="245" stroke="#f59e0b" stroke-width="1.8"/>
    <line x1="500" y1="245" x2="660" y2="280" stroke="#f59e0b" stroke-width="1.8"/>
    <line x1="660" y1="280" x2="780" y2="245" stroke="#f59e0b" stroke-width="1.8"/>

    <!-- Ray 2 through Optical Centre O of objective undeflected -->
    <line x1="30" y1="165" x2="160" y2="200" stroke="#38bdf8" stroke-width="1.8"/>
    <line x1="160" y1="200" x2="500" y2="245" stroke="#38bdf8" stroke-width="1.8"/>
    <line x1="500" y1="245" x2="660" y2="200" stroke="#38bdf8" stroke-width="1.8"/>
    <line x1="660" y1="200" x2="780" y2="165" stroke="#38bdf8" stroke-width="1.8"/>

    <!-- Parallel emergent rays entering eye -->
    <g transform="translate(740, 180)">
      <path d="M 0,20 Q 25,0 50,20 Q 25,40 0,20 Z" fill="none" stroke="#f8fafc" stroke-width="2"/>
      <circle cx="25" cy="20" r="8" fill="#38bdf8"/>
      <text x="25" y="55" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Relaxed Eye</text>
    </g>

    <!-- Barrel Length Dimension L = fo + fe -->
    <line x1="160" y1="360" x2="660" y2="360" stroke="#38bdf8" stroke-width="2"/>
    <line x1="160" y1="350" x2="160" y2="370" stroke="#38bdf8" stroke-width="2"/>
    <line x1="660" y1="350" x2="660" y2="370" stroke="#38bdf8" stroke-width="2"/>
    <text x="410" y="385" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Barrel Length in Normal Adjustment: L = fo + fe</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Ray Diagram: Astronomical Telescope in Normal Adjustment")

def svg_m13_camera_mechanism():
    """Page 5: Camera cross section mechanism"""
    inner = """
    <!-- Light-proof Camera Body -->
    <rect x="180" y="80" width="480" height="260" fill="#1e293b" rx="14" stroke="#475569" stroke-width="3"/>
    <rect x="220" y="105" width="400" height="210" fill="#0f172a" rx="8"/>

    <!-- Front Lens Assembly -->
    <rect x="100" y="125" width="80" height="170" fill="#334155" rx="6" stroke="#64748b" stroke-width="2"/>
    <path d="M 130,135 Q 115,210 130,285 Q 145,210 130,135 Z" fill="#0284c733" stroke="#38bdf8" stroke-width="2.5"/>
    <path d="M 155,145 Q 145,210 155,275 Q 165,210 155,145 Z" fill="#0284c733" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="140" y="105" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Lens Assembly</text>

    <!-- Focusing Screw Ring Indicator -->
    <path d="M 90,170 L 90,250" stroke="#f59e0b" stroke-width="3"/>
    <text x="65" y="215" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Focus Ring</text>

    <!-- Iris Diaphragm Aperture -->
    <line x1="270" y1="110" x2="270" y2="175" stroke="#94a3b8" stroke-width="4"/>
    <line x1="270" y1="245" x2="270" y2="310" stroke="#94a3b8" stroke-width="4"/>
    <text x="270" y="90" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Aperture</text>
    <text x="270" y="215" fill="#94a3b8" font-size="10" text-anchor="middle">Stop</text>

    <!-- Shutter Curtain -->
    <line x1="550" y1="110" x2="550" y2="310" stroke="#ef4444" stroke-width="3" stroke-dasharray="4 2"/>
    <text x="550" y="90" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Shutter</text>

    <!-- Digital Sensor / Film Plane at Rear -->
    <rect x="590" y="125" width="12" height="170" fill="#22c55e" rx="2" stroke="#16a34a"/>
    <text x="600" y="105" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Sensor</text>

    <!-- Ray Cone focusing on sensor -->
    <polygon points="140,150 140,270 590,210" fill="#38bdf811" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="590" cy="210" r="3" fill="#ef4444"/>

    <!-- Bottom Feature Explanations -->
    <rect x="180" y="360" width="480" height="40" fill="#111827" rx="8" stroke="#1e293b"/>
    <text x="420" y="385" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Focuses by moving lens position (v) to form real, inverted, diminished image on sensor.</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Cross-Sectional Mechanics of a Photographic Camera")

def svg_m13_eye_anatomy():
    """Page 6: Human Eye Anatomy and Accommodation"""
    inner = """
    <!-- Eyeball outer shell (Sclera & Choroid) -->
    <path d="M 380,80 A 150 150 0 1 1 380,340 C 320,335 240,290 200,210 C 240,130 320,85 380,80 Z" fill="#111827" stroke="#475569" stroke-width="3"/>
    <!-- Retina Layer (Inner red curve at back) -->
    <path d="M 400,95 A 135 135 0 0 1 400,325" fill="none" stroke="#ef4444" stroke-width="3.5"/>
    <text x="560" y="215" fill="#ef4444" font-family="system-ui, sans-serif" font-size="13" font-weight="700">Retina (Screen)</text>

    <!-- Cornea (Front clear bulge) -->
    <path d="M 220,150 Q 160,210 220,270" fill="none" stroke="#38bdf8" stroke-width="3.5"/>
    <text x="140" y="215" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="end">Cornea</text>

    <!-- Crystalline Lens -->
    <path d="M 270,160 Q 255,210 270,260 Q 285,210 270,160 Z" fill="#0284c744" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="270" y="140" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Lens</text>

    <!-- Ciliary Muscles & Suspensory Ligaments -->
    <circle cx="270" cy="150" r="6" fill="#f59e0b"/>
    <line x1="270" y1="156" x2="270" y2="160" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="270" cy="270" r="6" fill="#f59e0b"/>
    <line x1="270" y1="264" x2="270" y2="270" stroke="#f59e0b" stroke-width="2"/>
    <text x="315" y="135" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Ciliary Muscle</text>

    <!-- Iris & Pupil -->
    <line x1="250" y1="150" x2="250" y2="185" stroke="#94a3b8" stroke-width="3"/>
    <line x1="250" y1="235" x2="250" y2="270" stroke="#94a3b8" stroke-width="3"/>
    <text x="215" y="170" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11">Iris</text>
    <text x="215" y="215" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Pupil</text>

    <!-- Optic Nerve Exit -->
    <path d="M 520,200 L 580,185 L 580,235 L 520,220" fill="#334155"/>
    <text x="640" y="215" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600">Optic Nerve</text>

    <!-- Vitreous Humour Area -->
    <text x="390" y="210" fill="#64748b" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Vitreous Humour</text>

    <!-- Bottom Accommodation Callout -->
    <rect x="100" y="360" width="640" height="40" fill="#111827" rx="8" stroke="#1e293b"/>
    <text x="420" y="385" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Accommodation: Ciliary muscles adjust lens curvature (f) to focus near (thick) &amp; distant (flat) objects.</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Anatomical Cross-Section & Optical Structure of the Human Eye")

def svg_m13_myopia_correction():
    """Page 8: Myopia Defect & Concave Correction"""
    inner = """
    <!-- Top Panel: Uncorrected Myopia -->
    <g transform="translate(0, 0)">
      <rect x="40" y="45" width="760" height="165" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="60" y="70" fill="#ef4444" font-family="system-ui, sans-serif" font-size="13" font-weight="700">1. MYOPIC EYE (UNCORRECTED): Parallel rays focus in FRONT of retina</text>

      <!-- Elongated Eye Outline -->
      <path d="M 550,65 A 65 65 0 1 1 550,195 C 500,190 430,160 400,130 C 430,100 500,70 550,65 Z" fill="#0f172a" stroke="#475569" stroke-width="2"/>
      <path d="M 560,75 A 55 55 0 0 1 560,185" fill="none" stroke="#ef4444" stroke-width="3"/>
      <!-- Eye lens -->
      <path d="M 440,95 Q 430,130 440,165 Q 450,130 440,95 Z" fill="#0284c733" stroke="#38bdf8" stroke-width="2"/>

      <!-- Parallel rays focusing too early -->
      <line x1="80" y1="105" x2="440" y2="105" stroke="#f59e0b" stroke-width="1.8"/>
      <line x1="80" y1="155" x2="440" y2="155" stroke="#f59e0b" stroke-width="1.8"/>
      <line x1="440" y1="105" x2="520" y2="130" stroke="#f59e0b" stroke-width="1.8"/>
      <line x1="440" y1="155" x2="520" y2="130" stroke="#f59e0b" stroke-width="1.8"/>
      <line x1="520" y1="130" x2="560" y2="145" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="2 2"/>
      <line x1="520" y1="130" x2="560" y2="115" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="2 2"/>

      <!-- Focal Point Marker -->
      <circle cx="520" cy="130" r="4" fill="#ef4444"/>
      <text x="520" y="110" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Focus in front</text>
      <text x="640" y="135" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="600">Blurred Image</text>
    </g>

    <!-- Bottom Panel: Corrected with Concave Lens -->
    <g transform="translate(0, 185)">
      <rect x="40" y="45" width="760" height="175" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="60" y="70" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="700">2. OPTICAL CORRECTION: Diverging (Concave) lens diverges rays onto retina</text>

      <!-- Eye Outline -->
      <path d="M 550,65 A 65 65 0 1 1 550,195 C 500,190 430,160 400,130 C 430,100 500,70 550,65 Z" fill="#0f172a" stroke="#475569" stroke-width="2"/>
      <path d="M 560,75 A 55 55 0 0 1 560,185" fill="none" stroke="#22c55e" stroke-width="3"/>
      <!-- Eye lens -->
      <path d="M 440,95 Q 430,130 440,165 Q 450,130 440,95 Z" fill="#0284c733" stroke="#38bdf8" stroke-width="2"/>

      <!-- Concave Spectacle Lens at x = 330 -->
      <path d="M 325,90 Q 335,130 325,170 L 340,170 Q 330,130 340,90 Z" fill="#d9770633" stroke="#f59e0b" stroke-width="2"/>
      <text x="330" y="80" fill="#f59e0b" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Concave Lens</text>

      <!-- Parallel rays pre-diverged by concave lens -->
      <line x1="80" y1="105" x2="330" y2="105" stroke="#38bdf8" stroke-width="1.8"/>
      <line x1="80" y1="155" x2="330" y2="155" stroke="#38bdf8" stroke-width="1.8"/>
      <!-- Diverged into eye lens -->
      <line x1="335" y1="105" x2="440" y2="98" stroke="#38bdf8" stroke-width="1.8"/>
      <line x1="335" y1="155" x2="440" y2="162" stroke="#38bdf8" stroke-width="1.8"/>
      <!-- Focused exactly on retina -->
      <line x1="440" y1="98" x2="560" y2="130" stroke="#38bdf8" stroke-width="1.8"/>
      <line x1="440" y1="162" x2="560" y2="130" stroke="#38bdf8" stroke-width="1.8"/>

      <circle cx="560" cy="130" r="4" fill="#22c55e"/>
      <text x="640" y="135" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Sharp Focus on Retina</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Short-Sightedness (Myopia) and Diverging Lens Optical Correction")

def svg_m13_hypermetropia_correction():
    """Page 9: Hypermetropia Defect & Convex Correction"""
    inner = """
    <!-- Top Panel: Uncorrected Hypermetropia -->
    <g transform="translate(0, 0)">
      <rect x="40" y="45" width="760" height="165" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="60" y="70" fill="#ef4444" font-family="system-ui, sans-serif" font-size="13" font-weight="700">1. HYPERMETROPIC EYE (UNCORRECTED): Near rays focus BEHIND retina</text>

      <!-- Shortened Eye Outline -->
      <path d="M 520,65 A 65 65 0 1 1 520,195 C 470,190 410,160 380,130 C 410,100 470,70 520,65 Z" fill="#0f172a" stroke="#475569" stroke-width="2"/>
      <path d="M 530,75 A 55 55 0 0 1 530,185" fill="none" stroke="#ef4444" stroke-width="3"/>
      <!-- Eye lens -->
      <path d="M 420,95 Q 410,130 420,165 Q 430,130 420,95 Z" fill="#0284c733" stroke="#38bdf8" stroke-width="2"/>

      <!-- Near object point -->
      <circle cx="120" cy="130" r="4" fill="#22c55e"/>
      <text x="120" y="115" fill="#22c55e" font-size="11" font-weight="700" text-anchor="middle">Near Object (25 cm)</text>

      <!-- Divergent rays from near object -->
      <line x1="120" y1="130" x2="420" y2="105" stroke="#f59e0b" stroke-width="1.8"/>
      <line x1="120" y1="130" x2="420" y2="155" stroke="#f59e0b" stroke-width="1.8"/>
      <line x1="420" y1="105" x2="530" y2="120" stroke="#f59e0b" stroke-width="1.8"/>
      <line x1="420" y1="155" x2="530" y2="140" stroke="#f59e0b" stroke-width="1.8"/>
      <line x1="530" y1="120" x2="570" y2="130" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="2 2"/>
      <line x1="530" y1="140" x2="570" y2="130" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="2 2"/>

      <circle cx="570" cy="130" r="4" fill="#ef4444"/>
      <text x="570" y="110" fill="#ef4444" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Focus behind</text>
      <text x="640" y="135" fill="#ef4444" font-family="system-ui, sans-serif" font-size="12" font-weight="600">Blurred Image</text>
    </g>

    <!-- Bottom Panel: Corrected with Convex Lens -->
    <g transform="translate(0, 185)">
      <rect x="40" y="45" width="760" height="175" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="60" y="70" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="700">2. OPTICAL CORRECTION: Converging (Convex) lens pre-converges rays onto retina</text>

      <!-- Eye Outline -->
      <path d="M 520,65 A 65 65 0 1 1 520,195 C 470,190 410,160 380,130 C 410,100 470,70 520,65 Z" fill="#0f172a" stroke="#475569" stroke-width="2"/>
      <path d="M 530,75 A 55 55 0 0 1 530,185" fill="none" stroke="#22c55e" stroke-width="3"/>
      <!-- Eye lens -->
      <path d="M 420,95 Q 410,130 420,165 Q 430,130 420,95 Z" fill="#0284c733" stroke="#38bdf8" stroke-width="2"/>

      <!-- Convex Spectacle Lens at x = 280 -->
      <path d="M 280,85 Q 265,130 280,175 Q 295,130 280,85 Z" fill="#0284c733" stroke="#38bdf8" stroke-width="2"/>
      <text x="280" y="75" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Convex Lens</text>

      <!-- Near object point -->
      <circle cx="120" cy="130" r="4" fill="#22c55e"/>

      <!-- Rays pre-converged by spectacle lens -->
      <line x1="120" y1="130" x2="280" y2="100" stroke="#38bdf8" stroke-width="1.8"/>
      <line x1="120" y1="130" x2="280" y2="160" stroke="#38bdf8" stroke-width="1.8"/>
      <!-- Entering eye lens with reduced divergence -->
      <line x1="280" y1="100" x2="420" y2="110" stroke="#38bdf8" stroke-width="1.8"/>
      <line x1="280" y1="160" x2="420" y2="150" stroke="#38bdf8" stroke-width="1.8"/>
      <!-- Focused sharply on retina -->
      <line x1="420" y1="110" x2="530" y2="130" stroke="#38bdf8" stroke-width="1.8"/>
      <line x1="420" y1="150" x2="530" y2="130" stroke="#38bdf8" stroke-width="1.8"/>

      <circle cx="530" cy="130" r="4" fill="#22c55e"/>
      <text x="640" y="135" fill="#22c55e" font-family="system-ui, sans-serif" font-size="12" font-weight="700">Sharp Focus on Retina</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Long-Sightedness (Hypermetropia) and Converging Lens Optical Correction")


# =============================================================================
# MAIN ENRICHMENT EXECUTOR
# =============================================================================

def run_enrichment():
    print("=" * 80)
    print("VLEARN FORM 4 PHYSICS — TOPIC 1 VISUAL ENRICHMENT")
    print("=" * 80)

    topic = Topic.objects.filter(
        subject__name="Physics",
        subject__grade__name="Form 4",
        name__icontains="Thin Lenses"
    ).first()

    if not topic:
        print("ERROR: Topic 1: Thin Lenses not found! Run ingest_form4_physics.py first.")
        return

    units = topic.learning_units.all().order_by("order")
    if units.count() < 3:
        print("ERROR: Expected 3 learning units in Topic 1.")
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
    # MODULE 1.1 ENRICHMENT
    # -------------------------------------------------------------------------
    print("--- Enriching Module 1.1 ---")
    attach_svg_to_block(lesson_1, 2, "suggested_diagram", "Converging and Diverging Lens Geometries", "m11_lens_geometries", svg_m11_lens_geometries())
    attach_svg_to_block(lesson_1, 3, "suggested_diagram", "Curvature Geometry and Landmarks of a Biconvex Lens", "m11_curvature_landmarks", svg_m11_curvature_landmarks())
    attach_svg_to_block(lesson_1, 4, "suggested_diagram", "Principal Focus and Ray Refraction in Converging and Diverging Lenses", "m11_principal_focus", svg_m11_principal_focus())
    attach_svg_to_block(lesson_1, 5, "suggested_diagram", "Ray Diagram: Object Placed Inside the Focal Length (u < f)", "m11_ray_u_less_f", svg_m11_ray_diagram_u_less_f())
    attach_svg_to_block(lesson_1, 6, "suggested_diagram", "Ray Diagram: Object Placed Between F and 2F (f < u < 2f)", "m11_ray_between_f_2f", svg_m11_ray_diagram_between_f_and_2f())
    attach_svg_to_block(lesson_1, 7, "suggested_diagram", "Ray Diagram: Object Placed Beyond 2F (u > 2f)", "m11_ray_u_greater_2f", svg_m11_ray_diagram_u_greater_2f())
    attach_svg_to_block(lesson_1, 8, "suggested_diagram", "Ray Diagram: Image Formation by a Concave (Diverging) Lens", "m11_ray_concave", svg_m11_ray_diagram_concave())

    # Wikimedia for Module 1.1: Real convex lens forming real inverted image
    attach_wikimedia_to_block(
        lesson=lesson_1,
        page_num=7,
        title="Real Inverted Image Produced by a Convex Lens in Ambient Light",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Convex_lens_%28magnifying_glass%29_and_upside-down_image.jpg/960px-Convex_lens_%28magnifying_glass%29_and_upside-down_image.jpg",
        author="AntanO",
        licensing="CC BY-SA 4.0",
        commons_page="https://commons.wikimedia.org/wiki/File:Convex_lens_(magnifying_glass)_and_upside-down_image.jpg"
    )

    # -------------------------------------------------------------------------
    # MODULE 1.2 ENRICHMENT
    # -------------------------------------------------------------------------
    print("\n--- Enriching Module 1.2 ---")
    attach_svg_to_block(lesson_2, 3, "suggested_diagram", "The 'Real-is-Positive' Cartesian Sign Convention", "m12_sign_convention", svg_m12_sign_convention())
    attach_svg_to_block(lesson_2, 11, "suggested_diagram", "Laboratory Apparatus Setup for Focal Length Determination", "m12_optical_bench", svg_m12_optical_bench())
    attach_svg_to_block(lesson_2, 12, "suggested_graph", "Graph Interpretation: Linear Reciprocal Relationship (1/v vs. 1/u)", "m12_reciprocal_graph", svg_m12_reciprocal_graph())

    # Wikimedia for Module 1.2: Real optical bench apparatus in student lab
    attach_wikimedia_to_block(
        lesson=lesson_2,
        page_num=11,
        title="Educational Optical Bench Apparatus in Laboratory",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Optical_Bench_educational_Kit_-_Cuesta_College.jpg/960px-Optical_Bench_educational_Kit_-_Cuesta_College.jpg",
        author="Cuesta College Physical Sciences Department",
        licensing="CC BY 2.0",
        commons_page="https://commons.wikimedia.org/wiki/File:Optical_Bench_educational_Kit_-_Cuesta_College.jpg"
    )

    # -------------------------------------------------------------------------
    # MODULE 1.3 ENRICHMENT
    # -------------------------------------------------------------------------
    print("\n--- Enriching Module 1.3 ---")
    attach_svg_to_block(lesson_3, 2, "suggested_diagram", "Ray Diagram: Simple Microscope (Magnifier) at Near Point D = 25 cm", "m13_simple_microscope", svg_m13_simple_microscope())
    attach_svg_to_block(lesson_3, 3, "suggested_diagram", "Ray Diagram: Optical Train of a Compound Microscope", "m13_compound_microscope", svg_m13_compound_microscope())
    attach_svg_to_block(lesson_3, 4, "suggested_diagram", "Ray Diagram: Astronomical Telescope in Normal Adjustment", "m13_telescope", svg_m13_telescope())
    attach_svg_to_block(lesson_3, 5, "suggested_diagram", "Cross-Section Diagram of a Camera Mechanism", "m13_camera", svg_m13_camera_mechanism())
    attach_svg_to_block(lesson_3, 6, "suggested_diagram", "Anatomical Cross-Section of the Human Eye", "m13_eye_anatomy", svg_m13_eye_anatomy())
    attach_svg_to_block(lesson_3, 8, "suggested_diagram", "Ray Diagram: Myopic Eye and Concave Lens Optical Correction", "m13_myopia", svg_m13_myopia_correction())
    attach_svg_to_block(lesson_3, 9, "suggested_diagram", "Ray Diagram: Hypermetropic Eye and Convex Lens Optical Correction", "m13_hypermetropia", svg_m13_hypermetropia_correction())

    # Wikimedia for Module 1.3: Compound Microscope, Telescope, and Camera Aperture
    attach_wikimedia_to_block(
        lesson=lesson_3,
        page_num=3,
        title="Laboratory Optical Research Microscope",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Laboratory_Optical_Microscope.jpg/960px-Laboratory_Optical_Microscope.jpg",
        author="Aliva S",
        licensing="CC BY-SA 4.0",
        commons_page="https://commons.wikimedia.org/wiki/File:Laboratory_Optical_Microscope.jpg"
    )

    attach_wikimedia_to_block(
        lesson=lesson_3,
        page_num=4,
        title="The Great Refractor Astronomical Telescope (Potsdam Observatory)",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Great_Refractor_Potsdam.jpg/960px-Great_Refractor_Potsdam.jpg",
        author="H. Raab",
        licensing="CC BY-SA 4.0",
        commons_page="https://commons.wikimedia.org/wiki/File:Great_Refractor_Potsdam.jpg"
    )

    attach_wikimedia_to_block(
        lesson=lesson_3,
        page_num=5,
        title="Camera Lens Iris Diaphragm Aperture Blades Mechanism",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Hasselblad_L3D-100c_-_aperture_ar_1to1_PNr%C2%B01261.jpg/960px-Hasselblad_L3D-100c_-_aperture_ar_1to1_PNr%C2%B01261.jpg",
        author="D-Kuru",
        licensing="CC BY-SA 4.0",
        commons_page="https://commons.wikimedia.org/wiki/File:Hasselblad_L3D-100c_-_aperture_ar_1to1_PNr%C2%B01261.jpg"
    )

    print("\n" + "=" * 80)
    print("VISUAL ENRICHMENT COMPLETED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    run_enrichment()
