"""
VLearn Form 4 Physics — Topic 5: Electromagnetic Induction
Visual Enrichment Engine (SVGs + Wikimedia Commons)

Enriches all 3 modules of Topic 5 (Electromagnetic Induction) with:
  - 12 high-precision dark-mode vector SVG diagrams (charge separation in moving conductors, 
    straight wire horseshoe magnet setup with centre-zero galvanometer, Lenz's Law bar magnet repulsion/attraction, 
    Fleming's Right-Hand Rule 3D vector alignment, A.C. generator construction with slip rings, 
    sinusoidal A.C. waveform across 360 degrees, D.C. generator split-ring commutator & pulsating D.C., 
    moving coil microphone cross-section, solid vs laminated core eddy current loops, 
    mutual induction primary/secondary coil linkage, Step-Up vs Step-Down transformer schematics, 
    and national electrical grid 400 kV transmission system).
  - 3 authentic Wikimedia Commons photographic assets (high-voltage substation transformer, 
    historic three-phase AC generator alternator, and power transmission switchgear).

Usage:
  /home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/venv/bin/python curriculum/enrich_form4_physics_topic5.py
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
# SVG BUILDERS — MODULE 5.1
# =============================================================================

def svg_m51_conductor_charge_separation():
    """Page 2: Conductor charge separation and origin of induced e.m.f."""
    inner = """
    <!-- Magnetic Pole Blocks: North (left, red) and South (right, blue) -->
    <rect x="60" y="80" width="100" height="260" fill="#ef444433" stroke="#ef4444" stroke-width="2" rx="6"/>
    <text x="110" y="215" fill="#ef4444" font-size="28" font-weight="800" text-anchor="middle">NORTH</text>

    <rect x="680" y="80" width="100" height="260" fill="#0284c733" stroke="#38bdf8" stroke-width="2" rx="6"/>
    <text x="730" y="215" fill="#38bdf8" font-size="28" font-weight="800" text-anchor="middle">SOUTH</text>

    <!-- Magnetic Field Lines (Left to Right) -->
    <line x1="160" y1="120" x2="680" y2="120" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="8 4"/>
    <line x1="160" y1="180" x2="680" y2="180" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="8 4"/>
    <line x1="160" y1="240" x2="680" y2="240" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="8 4"/>
    <line x1="160" y1="300" x2="680" y2="300" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="8 4"/>

    <!-- Copper Conductor Wire (Vertical Cylinder moving DOWNWARD) -->
    <rect x="400" y="100" width="40" height="220" fill="#f59e0b" stroke="#d97706" stroke-width="2" rx="4"/>
    <text x="420" y="210" fill="#000" font-size="11" font-weight="800" text-anchor="middle" transform="rotate(-90 420 210)">COPPER WIRE</text>

    <!-- Downward Motion Vector -->
    <line x1="420" y1="50" x2="420" y2="90" stroke="#22c55e" stroke-width="4"/>
    <polygon points="414,80 420,95 426,80" fill="#22c55e"/>
    <text x="435" y="70" fill="#22c55e" font-size="12" font-weight="700">Motion Downward (v)</text>

    <!-- Terminal Charge Deficit (+) at top, Accumulation (-) at bottom -->
    <circle cx="420" cy="115" r="12" fill="#ef4444"/>
    <text x="420" y="120" fill="#fff" font-size="14" font-weight="800" text-anchor="middle">+</text>

    <circle cx="420" cy="305" r="12" fill="#38bdf8"/>
    <text x="420" y="309" fill="#fff" font-size="14" font-weight="800" text-anchor="middle">-</text>

    <!-- Induced Voltage Callout -->
    <rect x="470" y="180" width="180" height="60" fill="#111827" rx="8" stroke="#1e293b"/>
    <text x="560" y="205" fill="#f8fafc" font-size="11" text-anchor="middle">Induced Potential Difference:</text>
    <text x="560" y="225" fill="#22c55e" font-size="14" font-weight="700" text-anchor="middle">Induced E.M.F. (ε)</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Microscopic Origin of Induced E.M.F.: Electron Drift and Charge Separation")

def svg_m51_straight_wire_induction():
    """Page 3: Straight wire moving between horseshoe magnet poles with galvanometer"""
    inner = """
    <!-- U-Shaped Horseshoe Magnet at x = 160 to 480 -->
    <path d="M 180,80 L 180,260 A 60 60 0 0 0 300,260 L 300,80" fill="none" stroke="#64748b" stroke-width="30"/>
    <!-- North Pole (Left, Red tip) -->
    <rect x="165" y="70" width="30" height="50" fill="#ef4444" rx="2"/>
    <text x="180" y="100" fill="#fff" font-size="16" font-weight="800" text-anchor="middle">N</text>

    <!-- South Pole (Right, Blue tip) -->
    <rect x="285" y="70" width="30" height="50" fill="#0284c7" rx="2"/>
    <text x="300" y="100" fill="#fff" font-size="16" font-weight="800" text-anchor="middle">S</text>

    <!-- Straight Conductor Wire passing between poles -->
    <line x1="120" y1="120" x2="360" y2="120" stroke="#f59e0b" stroke-width="5"/>

    <!-- Motion Arrows: Upward (Red) and Downward (Blue) -->
    <line x1="240" y1="120" x2="240" y2="60" stroke="#22c55e" stroke-width="3"/>
    <polygon points="235,70 240,58 245,70" fill="#22c55e"/>
    <text x="250" y="70" fill="#22c55e" font-size="11" font-weight="700">Upward Motion</text>

    <!-- Flexible Leads connecting wire to Galvanometer -->
    <path d="M 120,120 Q 80,200 120,320" fill="none" stroke="#f8fafc" stroke-width="2"/>
    <path d="M 360,120 Q 400,200 360,320" fill="none" stroke="#f8fafc" stroke-width="2"/>

    <!-- Centre-Zero Galvanometer at x = 520, y = 140 -->
    <circle cx="620" cy="220" r="90" fill="#111827" stroke="#38bdf8" stroke-width="3"/>
    <text x="620" y="160" fill="#38bdf8" font-size="16" font-weight="800" text-anchor="middle">G</text>

    <!-- Scale ticks: -30, -20, -10, 0, +10, +20, +30 -->
    <line x1="620" y1="170" x2="620" y2="180" stroke="#f8fafc" stroke-width="2"/>
    <text x="620" y="195" fill="#22c55e" font-size="12" font-weight="700" text-anchor="middle">0</text>

    <!-- Galvanometer Needle Deflected Right -->
    <line x1="620" y1="250" x2="660" y2="180" stroke="#ef4444" stroke-width="3"/>
    <circle cx="620" cy="250" r="6" fill="#ef4444"/>
    <text x="620" y="280" fill="#ef4444" font-size="11" font-weight="700" text-anchor="middle">Momentary Deflection</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Laboratory Setup: Straight Conductor Motion in Horseshoe Magnet Field with Galvanometer")

def svg_m51_lenz_law_magnet_solenoid():
    """Page 6: Lenz's Law magnet repulsion and attraction"""
    inner = """
    <!-- Solenoid Coil at x = 320 to 560, y = 140 -->
    <rect x="320" y="140" width="240" height="120" fill="#0284c715" stroke="#38bdf8" stroke-width="2" rx="8"/>
    <!-- Solenoid Windings (Copper loops) -->
    <path d="M 340,140 C 340,100 370,100 370,140 L 370,260 C 370,300 340,300 340,260 Z" fill="none" stroke="#f59e0b" stroke-width="3"/>
    <path d="M 400,140 C 400,100 430,100 430,140 L 430,260 C 430,300 400,300 400,260 Z" fill="none" stroke="#f59e0b" stroke-width="3"/>
    <path d="M 460,140 C 460,100 490,100 490,140 L 490,260 C 490,300 460,300 460,260 Z" fill="none" stroke="#f59e0b" stroke-width="3"/>
    <path d="M 520,140 C 520,100 550,100 550,140 L 550,260 C 550,300 520,300 520,260 Z" fill="none" stroke="#f59e0b" stroke-width="3"/>

    <!-- Induced North Pole on Solenoid Left Face -->
    <circle cx="320" cy="200" r="24" fill="#ef4444"/>
    <text x="320" y="207" fill="#fff" font-size="20" font-weight="800" text-anchor="middle">N</text>

    <!-- Approaching Bar Magnet (North pole facing left face of solenoid) -->
    <rect x="60" y="165" width="90" height="70" fill="#ef4444" rx="4"/>
    <text x="105" y="207" fill="#fff" font-size="20" font-weight="800" text-anchor="middle">N</text>

    <rect x="150" y="165" width="90" height="70" fill="#0284c7" rx="4"/>
    <text x="195" y="207" fill="#fff" font-size="20" font-weight="800" text-anchor="middle">S</text>

    <!-- Motion Arrow toward solenoid -->
    <line x1="120" y1="120" x2="220" y2="120" stroke="#22c55e" stroke-width="4"/>
    <polygon points="210,114 225,120 210,126" fill="#22c55e"/>
    <text x="170" y="105" fill="#22c55e" font-size="12" font-weight="700" text-anchor="middle">Magnet Pushed Right (v)</text>

    <!-- Repulsive Force Vectors (Opposing Motion) -->
    <line x1="290" y1="200" x2="250" y2="200" stroke="#ef4444" stroke-width="4"/>
    <polygon points="260,194 245,200 260,206" fill="#ef4444"/>
    <text x="270" y="235" fill="#ef4444" font-size="12" font-weight="700" text-anchor="middle">Repulsive Force (Lenz's Law)</text>

    <!-- Energy Conservation Explanation Box -->
    <rect x="590" y="100" width="220" height="200" fill="#111827" rx="10" stroke="#1e293b"/>
    <text x="700" y="130" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">ENERGY CONSERVATION</text>

    <g transform="translate(605, 150)">
      <text x="0" y="0" fill="#f8fafc" font-size="11">• Mechanical work is done</text>
      <text x="0" y="18" fill="#f8fafc" font-size="11">  against repulsive force.</text>

      <text x="0" y="50" fill="#22c55e" font-size="11" font-weight="700">• Work done = Electrical</text>
      <text x="0" y="68" fill="#22c55e" font-size="11" font-weight="700">  Energy of Induced Current.</text>

      <text x="0" y="105" fill="#f59e0b" font-size="10">Prevents creation of energy</text>
      <text x="0" y="120" fill="#f59e0b" font-size="10">from nothing!</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Lenz's Law and Energy Conservation: Induced Magnetic Opposition to Motion")

def svg_m51_fleming_right_hand_rule():
    """Page 7: Fleming's Right-Hand Generator Rule 3D vector alignment"""
    inner = """
    <!-- Right Hand Outline & 3D Vectors at x = 300, y = 220 -->
    <!-- Axis 1: Motion / Force (Thumb, Vertical UPWARDS) -->
    <line x1="300" y1="220" x2="300" y2="60" stroke="#22c55e" stroke-width="5"/>
    <polygon points="292,72 300,55 308,72" fill="#22c55e"/>
    <text x="320" y="80" fill="#22c55e" font-size="14" font-weight="800">THUMB: Motion / Force (Input)</text>

    <!-- Axis 2: Magnetic Field (First Finger, Horizontal RIGHT) -->
    <line x1="300" y1="220" x2="550" y2="220" stroke="#38bdf8" stroke-width="5"/>
    <polygon points="538,212 555,220 538,228" fill="#38bdf8"/>
    <text x="565" y="225" fill="#38bdf8" font-size="14" font-weight="800">FIRST FINGER: Magnetic Field (N → S)</text>

    <!-- Axis 3: Induced Current (Second Finger, Slanted OUT OF PAGE / DOWN-LEFT) -->
    <line x1="300" y1="220" x2="160" y2="340" stroke="#ef4444" stroke-width="5"/>
    <polygon points="172,338 150,348 162,326" fill="#ef4444"/>
    <text x="40" y="365" fill="#ef4444" font-size="14" font-weight="800">SECOND FINGER: Induced Current (Output)</text>

    <!-- Central 90 degree Angle Arc Indicators -->
    <path d="M 330,220 A 30 30 0 0 0 300,190" fill="none" stroke="#f59e0b" stroke-width="2"/>
    <text x="325" y="200" fill="#f59e0b" font-size="12" font-weight="700">90°</text>

    <!-- Memory Trick Card on Left -->
    <g transform="translate(40, 60)">
      <rect x="0" y="0" width="220" height="200" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="110" y="30" fill="#f59e0b" font-size="13" font-weight="700" text-anchor="middle">MEMORY AID</text>

      <text x="15" y="65" fill="#22c55e" font-size="12" font-weight="700">Thu<tspan fill="#f8fafc">mb = </tspan>Mo<tspan fill="#f8fafc">tion</tspan></text>
      <text x="15" y="105" fill="#38bdf8" font-size="12" font-weight="700">F<tspan fill="#f8fafc">irst Finger = </tspan>F<tspan fill="#f8fafc">ield</tspan></text>
      <text x="15" y="145" fill="#ef4444" font-size="12" font-weight="700">Se<tspan fill="#f8fafc">cond Finger = </tspan>C<tspan fill="#f8fafc">urrent</tspan></text>
      <text x="15" y="180" fill="#94a3b8" font-size="10" font-weight="600">Use Right Hand for Generators!</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Fleming's Right-Hand Generator Rule: Mutually Perpendicular 3D Vector Alignment")


# =============================================================================
# SVG BUILDERS — MODULE 5.2
# =============================================================================

def svg_m52_ac_generator_construction():
    """Page 2: A.C. generator construction with slip rings"""
    inner = """
    <!-- Permanent Magnets: North (left, red) and South (right, blue) -->
    <rect x="60" y="100" width="100" height="220" fill="#ef444433" stroke="#ef4444" stroke-width="2" rx="6"/>
    <text x="110" y="215" fill="#ef4444" font-size="24" font-weight="800" text-anchor="middle">N</text>

    <rect x="680" y="100" width="100" height="220" fill="#0284c733" stroke="#38bdf8" stroke-width="2" rx="6"/>
    <text x="730" y="215" fill="#38bdf8" font-size="24" font-weight="800" text-anchor="middle">S</text>

    <!-- Armature Coil (Slanted 3D rectangle at x = 220 to 440) -->
    <polygon points="240,130 420,150 400,280 220,260" fill="#f59e0b22" stroke="#f59e0b" stroke-width="3"/>
    <text x="320" y="210" fill="#f59e0b" font-size="13" font-weight="800" text-anchor="middle">Armature Coil</text>

    <!-- Axle Line -->
    <line x1="160" y1="205" x2="580" y2="205" stroke="#94a3b8" stroke-width="3" stroke-dasharray="8 4"/>

    <!-- Two Continuous Slip Rings (A and B) on Axle -->
    <circle cx="490" cy="205" r="18" fill="none" stroke="#f59e0b" stroke-width="4"/>
    <circle cx="540" cy="205" r="18" fill="none" stroke="#f59e0b" stroke-width="4"/>
    <text x="490" y="175" fill="#f59e0b" font-size="10" font-weight="700" text-anchor="middle">Slip Ring A</text>
    <text x="540" y="175" fill="#f59e0b" font-size="10" font-weight="700" text-anchor="middle">Slip Ring B</text>

    <!-- Carbon Brushes touching Slip Rings -->
    <rect x="483" y="230" width="14" height="25" fill="#64748b" stroke="#f8fafc"/>
    <rect x="533" y="230" width="14" height="25" fill="#64748b" stroke="#f8fafc"/>
    <text x="510" y="275" fill="#94a3b8" font-size="10" text-anchor="middle">Carbon Brushes</text>

    <!-- External Load Circuit -->
    <line x1="490" y1="255" x2="490" y2="330" stroke="#38bdf8" stroke-width="2"/>
    <line x1="540" y1="255" x2="540" y2="330" stroke="#38bdf8" stroke-width="2"/>
    <rect x="470" y="330" width="90" height="30" fill="#1e293b" stroke="#38bdf8" rx="4"/>
    <text x="515" y="350" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">A.C. Load</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Construction of an Alternating Current (A.C.) Generator with Continuous Slip Rings")

def svg_m52_ac_sinusoidal_waveform():
    """Page 3: Sinusoidal A.C. output waveform across 360 degrees"""
    inner = """
    <!-- Oscilloscope Grid Background (x = 80, y = 60 to 360) -->
    <rect x="80" y="60" width="680" height="300" fill="#030712" rx="12" stroke="#38bdf8" stroke-width="2"/>
    <line x1="80" y1="210" x2="760" y2="210" stroke="#334155" stroke-width="2"/>
    <line x1="250" y1="60" x2="250" y2="360" stroke="#1e293b" stroke-dasharray="4 4"/>
    <line x1="420" y1="60" x2="420" y2="360" stroke="#1e293b" stroke-dasharray="4 4"/>
    <line x1="590" y1="60" x2="590" y2="360" stroke="#1e293b" stroke-dasharray="4 4"/>

    <!-- Sinusoidal Wave Trace -->
    <path d="M 80,210 Q 165,80 250,210 Q 335,340 420,210 Q 505,80 590,210 Q 675,340 760,210" fill="none" stroke="#22c55e" stroke-width="4"/>

    <!-- Key Angles & Coil Inset Annotations -->
    <!-- 0 deg -->
    <circle cx="80" cy="210" r="5" fill="#f8fafc"/>
    <text x="80" y="235" fill="#f8fafc" font-size="11" font-weight="700" text-anchor="middle">0° (Vertical)</text>
    <text x="80" y="250" fill="#94a3b8" font-size="9" text-anchor="middle">e.m.f. = 0 V</text>

    <!-- 90 deg -->
    <circle cx="250" cy="110" r="5" fill="#ef4444"/>
    <text x="250" y="90" fill="#ef4444" font-size="11" font-weight="700" text-anchor="middle">90° (Horizontal)</text>
    <text x="250" y="75" fill="#22c55e" font-size="11" font-weight="800" text-anchor="middle">+V_peak</text>

    <!-- 180 deg -->
    <circle cx="420" cy="210" r="5" fill="#f8fafc"/>
    <text x="420" y="235" fill="#f8fafc" font-size="11" font-weight="700" text-anchor="middle">180° (Vertical)</text>
    <text x="420" y="250" fill="#94a3b8" font-size="9" text-anchor="middle">e.m.f. = 0 V</text>

    <!-- 270 deg -->
    <circle cx="590" cy="310" r="5" fill="#ef4444"/>
    <text x="590" y="335" fill="#ef4444" font-size="11" font-weight="700" text-anchor="middle">270° (Horizontal Inverted)</text>
    <text x="590" y="350" fill="#ef4444" font-size="11" font-weight="800" text-anchor="middle">-V_peak</text>

    <!-- 360 deg -->
    <circle cx="760" cy="210" r="5" fill="#f8fafc"/>
    <text x="740" y="235" fill="#f8fafc" font-size="11" font-weight="700" text-anchor="middle">360° (Complete Loop)</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Sinusoidal A.C. Voltage Waveform Output Across 360 Degrees of Armature Rotation")

def svg_m52_dc_generator_commutator():
    """Page 4: D.C. generator split-ring commutator & pulsating D.C. waveform"""
    inner = """
    <!-- Left Panel: Split-Ring Commutator Detail (x = 40, w = 360) -->
    <g transform="translate(40, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="180" y="30" fill="#f59e0b" font-size="13" font-weight="700" text-anchor="middle">SPLIT-RING COMMUTATOR</text>

      <!-- Two insulated half-rings -->
      <path d="M 180,100 A 60 60 0 0 1 180,220" fill="none" stroke="#f59e0b" stroke-width="10"/>
      <path d="M 180,100 A 60 60 0 0 0 180,220" fill="none" stroke="#38bdf8" stroke-width="10"/>

      <!-- Insulating Gaps at top and bottom -->
      <line x1="180" y1="90" x2="180" y2="110" stroke="#111827" stroke-width="6"/>
      <line x1="180" y1="210" x2="180" y2="230" stroke="#111827" stroke-width="6"/>

      <!-- Carbon Brushes pressing on sides -->
      <rect x="100" y="148" width="18" height="24" fill="#64748b" stroke="#fff"/>
      <rect x="242" y="148" width="18" height="24" fill="#64748b" stroke="#fff"/>
      <text x="109" y="190" fill="#22c55e" font-size="12" font-weight="800">+</text>
      <text x="251" y="190" fill="#ef4444" font-size="12" font-weight="800">-</text>

      <text x="180" y="275" fill="#f8fafc" font-size="11" text-anchor="middle">Swaps brush contacts every 180°</text>
      <text x="180" y="295" fill="#22c55e" font-size="11" font-weight="700" text-anchor="middle">Maintains Unidirectional Current</text>
    </g>

    <!-- Right Panel: Pulsating D.C. Waveform (x = 440, w = 360) -->
    <g transform="translate(440, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#030712" rx="10" stroke="#22c55e" stroke-width="2"/>
      <text x="180" y="30" fill="#22c55e" font-size="13" font-weight="700" text-anchor="middle">PULSATING D.C. WAVEFORM</text>

      <line x1="20" y1="240" x2="340" y2="240" stroke="#334155" stroke-width="2"/>

      <!-- Pulsating positive half-sine humps -->
      <path d="M 20,240 Q 95,100 170,240 Q 245,100 320,240" fill="none" stroke="#22c55e" stroke-width="4"/>

      <text x="95" y="90" fill="#22c55e" font-size="11" font-weight="700" text-anchor="middle">+V_peak</text>
      <text x="245" y="90" fill="#22c55e" font-size="11" font-weight="700" text-anchor="middle">+V_peak</text>

      <text x="180" y="275" fill="#f8fafc" font-size="11" text-anchor="middle">Current never reverses sign</text>
      <text x="180" y="295" fill="#22c55e" font-size="12" font-weight="700" text-anchor="middle">Unidirectional Direct Current (D.C.)</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="D.C. Generator Split-Ring Commutator Mechanism and Pulsating D.C. Waveform Output")

def svg_m52_moving_coil_microphone():
    """Page 5: Moving coil microphone cross-section"""
    inner = """
    <!-- Outer Mic Body / Housing (x = 100 to 740, y = 80 to 360) -->
    <rect x="100" y="80" width="640" height="280" fill="#111827" rx="14" stroke="#334155" stroke-width="2"/>

    <!-- Incoming Sound Waves (Left, Compression lines) -->
    <path d="M 30,150 Q 50,220 30,290" fill="none" stroke="#38bdf8" stroke-width="3"/>
    <path d="M 50,130 Q 70,220 50,310" fill="none" stroke="#38bdf8" stroke-width="3"/>
    <path d="M 70,110 Q 90,220 70,330" fill="none" stroke="#38bdf8" stroke-width="3"/>
    <text x="50" y="90" fill="#38bdf8" font-size="12" font-weight="700">Sound Waves</text>

    <!-- Flexible Diaphragm (Vertical curved line at x = 160) -->
    <path d="M 160,110 Q 180,220 160,330" fill="none" stroke="#f59e0b" stroke-width="4"/>
    <text x="160" y="90" fill="#f59e0b" font-size="12" font-weight="700" text-anchor="middle">Diaphragm</text>

    <!-- Attached Lightweight Voice Coil on former (x = 160 to 320) -->
    <rect x="165" y="180" width="140" height="80" fill="#f59e0b22" stroke="#f59e0b" stroke-width="2" rx="4"/>
    <!-- Wire windings -->
    <line x1="190" y1="180" x2="190" y2="260" stroke="#f59e0b" stroke-width="3"/>
    <line x1="220" y1="180" x2="220" y2="260" stroke="#f59e0b" stroke-width="3"/>
    <line x1="250" y1="180" x2="250" y2="260" stroke="#f59e0b" stroke-width="3"/>
    <line x1="280" y1="180" x2="280" y2="260" stroke="#f59e0b" stroke-width="3"/>
    <text x="235" y="215" fill="#fff" font-size="11" font-weight="800" text-anchor="middle">Voice Coil</text>

    <!-- Permanent Central Cup Magnet (E-shaped cross-section at x = 320 to 520) -->
    <rect x="320" y="120" width="200" height="40" fill="#ef444433" stroke="#ef4444" stroke-width="2"/>
    <text x="420" y="145" fill="#ef4444" font-size="12" font-weight="800" text-anchor="middle">NORTH POLE</text>

    <rect x="320" y="280" width="200" height="40" fill="#ef444433" stroke="#ef4444" stroke-width="2"/>
    <text x="420" y="305" fill="#ef4444" font-size="12" font-weight="800" text-anchor="middle">NORTH POLE</text>

    <rect x="380" y="180" width="140" height="80" fill="#0284c733" stroke="#38bdf8" stroke-width="2"/>
    <text x="450" y="225" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">SOUTH POLE</text>

    <!-- Audio Signal Wires to Right -->
    <line x1="305" y1="200" x2="680" y2="200" stroke="#22c55e" stroke-width="2.5"/>
    <line x1="305" y1="240" x2="680" y2="240" stroke="#22c55e" stroke-width="2.5"/>
    <rect x="580" y="185" width="140" height="70" fill="#111827" rx="6" stroke="#22c55e"/>
    <text x="650" y="215" fill="#22c55e" font-size="11" font-weight="700" text-anchor="middle">Audio Signal A.C.</text>
    <text x="650" y="235" fill="#94a3b8" font-size="9" text-anchor="middle">To Amplifier</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Cross-Sectional Structure and Operational Transduction of a Moving Coil Microphone")

def svg_m52_eddy_currents_lamination():
    """Page 7: Solid metal plate eddy currents vs Laminated core sheets"""
    inner = """
    <!-- Left Panel: Solid Metal Plate with Massive Eddy Currents (x = 40, w = 360) -->
    <g transform="translate(40, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="180" y="30" fill="#ef4444" font-size="13" font-weight="700" text-anchor="middle">SOLID METAL CORE (PARASITIC LOSS)</text>

      <!-- Solid Iron Block -->
      <rect x="60" y="70" width="240" height="170" fill="#64748b33" stroke="#94a3b8" stroke-width="2" rx="6"/>

      <!-- Large Circular Eddy Current Loops -->
      <circle cx="180" cy="155" r="60" fill="none" stroke="#ef4444" stroke-width="3" stroke-dasharray="8 4"/>
      <polygon points="180,95 190,95 185,85" fill="#ef4444"/>

      <circle cx="180" cy="155" r="35" fill="none" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="6 3"/>
      <polygon points="180,120 190,120 185,110" fill="#ef4444"/>

      <rect x="20" y="255" width="320" height="50" fill="#ef444415" rx="6" stroke="#ef444444"/>
      <text x="180" y="275" fill="#ef4444" font-size="11" font-weight="700" text-anchor="middle">High Current (I) → Massive I²R Heat Loss</text>
      <text x="180" y="292" fill="#94a3b8" font-size="9" text-anchor="middle">Wastes power &amp; causes overheating</text>
    </g>

    <!-- Right Panel: Laminated Sheet Core Solution (x = 440, w = 360) -->
    <g transform="translate(440, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="180" y="30" fill="#22c55e" font-size="13" font-weight="700" text-anchor="middle">LAMINATED SHEET CORE (SOLUTION)</text>

      <!-- Laminated Iron Core with Insulating Lines -->
      <rect x="60" y="70" width="240" height="170" fill="#64748b33" stroke="#22c55e" stroke-width="2" rx="6"/>
      <!-- Vertical Insulating Varnish Barriers -->
      <line x1="100" y1="70" x2="100" y2="240" stroke="#f59e0b" stroke-width="2"/>
      <line x1="140" y1="70" x2="140" y2="240" stroke="#f59e0b" stroke-width="2"/>
      <line x1="180" y1="70" x2="180" y2="240" stroke="#f59e0b" stroke-width="2"/>
      <line x1="220" y1="70" x2="220" y2="240" stroke="#f59e0b" stroke-width="2"/>
      <line x1="260" y1="70" x2="260" y2="240" stroke="#f59e0b" stroke-width="2"/>

      <!-- Tiny Restricted Eddy Loops -->
      <ellipse cx="120" cy="155" rx="12" ry="30" fill="none" stroke="#22c55e" stroke-width="2"/>
      <ellipse cx="200" cy="155" rx="12" ry="30" fill="none" stroke="#22c55e" stroke-width="2"/>

      <rect x="20" y="255" width="320" height="50" fill="#22c55e15" rx="6" stroke="#22c55e44"/>
      <text x="180" y="275" fill="#22c55e" font-size="11" font-weight="700" text-anchor="middle">Insulation Blocks Loops → Heat Loss Reduced</text>
      <text x="180" y="292" fill="#94a3b8" font-size="9" text-anchor="middle">Maximizes transformer operating efficiency</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Parasitic Eddy Currents in Solid Core vs. Energy Savings via Laminated Insulated Sheets")


# =============================================================================
# SVG BUILDERS — MODULE 5.3
# =============================================================================

def svg_m53_mutual_induction():
    """Page 2: Mutual induction primary and secondary coil linkage"""
    inner = """
    <!-- Primary Solenoid Coil P (Left, x = 100 to 340) -->
    <rect x="100" y="140" width="240" height="120" fill="#0284c715" stroke="#38bdf8" stroke-width="2" rx="8"/>
    <text x="220" y="205" fill="#38bdf8" font-size="14" font-weight="800" text-anchor="middle">PRIMARY COIL (P)</text>

    <!-- Secondary Solenoid Coil S (Right, x = 500 to 740) -->
    <rect x="500" y="140" width="240" height="120" fill="#22c55e15" stroke="#22c55e" stroke-width="2" rx="8"/>
    <text x="620" y="205" fill="#22c55e" font-size="14" font-weight="800" text-anchor="middle">SECONDARY COIL (S)</text>

    <!-- Primary Circuit Connections (A.C. Supply & Switch) -->
    <path d="M 140,260 L 140,350 L 300,350 L 300,260" fill="none" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="220" cy="350" r="14" fill="#111827" stroke="#38bdf8" stroke-width="2"/>
    <text x="220" y="354" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">~ AC</text>

    <!-- Secondary Circuit Connections (Galvanometer) -->
    <path d="M 540,260 L 540,350 L 700,350 L 700,260" fill="none" stroke="#22c55e" stroke-width="2"/>
    <circle cx="620" cy="350" r="14" fill="#111827" stroke="#22c55e" stroke-width="2"/>
    <text x="620" y="354" fill="#22c55e" font-size="12" font-weight="800" text-anchor="middle">G</text>

    <!-- Dynamic Magnetic Flux Linkage Lines (Connecting P to S across gap) -->
    <path d="M 220,140 Q 420,60 620,140" fill="none" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="6 3"/>
    <path d="M 220,260 Q 420,340 620,260" fill="none" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="6 3"/>
    <text x="420" y="90" fill="#f59e0b" font-size="12" font-weight="700" text-anchor="middle">Changing Magnetic Flux Linkage (ΔΦ/Δt)</text>
    """
    return wrap_svg(inner, W=840, H=420, title="The Principle of Mutual Induction Between Primary and Secondary Coils")

def svg_m53_stepup_stepdown_transformer():
    """Page 3: Step-Up vs Step-Down Transformer Schematics"""
    inner = """
    <!-- Left Panel: Step-Up Transformer (Np < Ns, Vs > Vp) -->
    <g transform="translate(40, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="180" y="28" fill="#22c55e" font-size="13" font-weight="700" text-anchor="middle">STEP-UP TRANSFORMER (Vs &gt; Vp)</text>

      <!-- Soft Iron Core Frame -->
      <rect x="80" y="60" width="200" height="180" fill="none" stroke="#64748b" stroke-width="24" rx="10"/>

      <!-- Primary Coil (Few turns, Np = 5) -->
      <path d="M 68,90 C 40,90 40,110 68,110 M 68,120 C 40,120 40,140 68,140 M 68,150 C 40,150 40,170 68,170 M 68,180 C 40,180 40,200 68,200" fill="none" stroke="#38bdf8" stroke-width="3"/>
      <text x="40" y="240" fill="#38bdf8" font-size="11" font-weight="700">Np = 5 turns</text>
      <text x="40" y="255" fill="#38bdf8" font-size="11">Vp = 240 V</text>

      <!-- Secondary Coil (Many turns, Ns = 15) -->
      <path d="M 292,80 C 320,80 320,95 292,95 M 292,100 C 320,100 320,115 292,115 M 292,120 C 320,120 320,135 292,135 M 292,140 C 320,140 320,155 292,155 M 292,160 C 320,160 320,175 292,175 M 292,180 C 320,180 320,195 292,195 M 292,200 C 320,200 320,215 292,215" fill="none" stroke="#22c55e" stroke-width="3"/>
      <text x="320" y="240" fill="#22c55e" font-size="11" font-weight="700" text-anchor="end">Ns = 15 turns</text>
      <text x="320" y="255" fill="#22c55e" font-size="11" text-anchor="end">Vs = 720 V</text>

      <text x="180" y="295" fill="#22c55e" font-size="12" font-weight="700" text-anchor="middle">Voltage Stepped Up | Current Decreased</text>
    </g>

    <!-- Right Panel: Step-Down Transformer (Np > Ns, Vs < Vp) -->
    <g transform="translate(440, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="180" y="28" fill="#f59e0b" font-size="13" font-weight="700" text-anchor="middle">STEP-DOWN TRANSFORMER (Vs &lt; Vp)</text>

      <!-- Soft Iron Core Frame -->
      <rect x="80" y="60" width="200" height="180" fill="none" stroke="#64748b" stroke-width="24" rx="10"/>

      <!-- Primary Coil (Many turns, Np = 15) -->
      <path d="M 68,80 C 40,80 40,95 68,95 M 68,100 C 40,100 40,115 68,115 M 68,120 C 40,120 40,135 68,135 M 68,140 C 40,140 40,155 68,155 M 68,160 C 40,160 40,175 68,175 M 68,180 C 40,180 40,195 68,195 M 68,200 C 40,200 40,215 68,215" fill="none" stroke="#38bdf8" stroke-width="3"/>
      <text x="40" y="240" fill="#38bdf8" font-size="11" font-weight="700">Np = 15 turns</text>
      <text x="40" y="255" fill="#38bdf8" font-size="11">Vp = 240 V</text>

      <!-- Secondary Coil (Few turns, Ns = 5) -->
      <path d="M 292,90 C 320,90 320,110 292,110 M 292,120 C 320,120 320,140 292,140 M 292,150 C 320,150 320,170 292,170 M 292,180 C 320,180 320,200 292,200" fill="none" stroke="#f59e0b" stroke-width="3"/>
      <text x="320" y="240" fill="#f59e0b" font-size="11" font-weight="700" text-anchor="end">Ns = 5 turns</text>
      <text x="320" y="255" fill="#f59e0b" font-size="11" text-anchor="end">Vs = 80 V</text>

      <text x="180" y="295" fill="#f59e0b" font-size="12" font-weight="700" text-anchor="middle">Voltage Stepped Down | Current Increased</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Comparative Construction of Step-Up and Step-Down Transformers on Laminated Soft Iron Cores")

def svg_m53_national_grid_system():
    """Page 7: National Electrical Grid Power Transmission System"""
    inner = """
    <!-- 4 Stages: Power Station (25 kV) -> Step-Up (400 kV Grid) -> Substation (11 kV) -> Consumer (240 V) -->
    <!-- Stage 1: Power Station Generator -->
    <g transform="translate(30, 80)">
      <rect x="0" y="0" width="160" height="220" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="80" y="25" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">POWER STATION</text>

      <circle cx="80" cy="100" r="35" fill="#0284c722" stroke="#38bdf8" stroke-width="2"/>
      <text x="80" y="105" fill="#38bdf8" font-size="14" font-weight="800" text-anchor="middle">~ GEN</text>

      <rect x="20" y="155" width="120" height="45" fill="#0284c715" rx="4" stroke="#0284c744"/>
      <text x="80" y="175" fill="#f8fafc" font-size="10" text-anchor="middle">Generated Voltage:</text>
      <text x="80" y="192" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">25,000 V (25 kV)</text>
    </g>

    <!-- Connection Line 1 to Step-Up Transformer -->
    <line x1="190" y1="180" x2="230" y2="180" stroke="#38bdf8" stroke-width="3"/>

    <!-- Stage 2: Step-Up Transformer (25 kV -> 400 kV) -->
    <g transform="translate(230, 80)">
      <rect x="0" y="0" width="160" height="220" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="80" y="25" fill="#22c55e" font-size="12" font-weight="700" text-anchor="middle">STEP-UP TRANSFORMER</text>

      <rect x="50" y="60" width="60" height="70" fill="none" stroke="#22c55e" stroke-width="8" rx="4"/>
      <text x="80" y="100" fill="#22c55e" font-size="10" font-weight="700" text-anchor="middle">1:16</text>

      <rect x="20" y="155" width="120" height="45" fill="#22c55e15" rx="4" stroke="#22c55e44"/>
      <text x="80" y="175" fill="#f8fafc" font-size="10" text-anchor="middle">Grid Transmission:</text>
      <text x="80" y="192" fill="#22c55e" font-size="12" font-weight="700" text-anchor="middle">400,000 V (400 kV)</text>
    </g>

    <!-- Long Distance Pylon Grid Transmission Lines -->
    <g transform="translate(390, 80)">
      <line x1="0" y1="180" x2="180" y2="180" stroke="#22c55e" stroke-width="4"/>

      <!-- Pylon Towers -->
      <polygon points="40,180 30,80 50,80" fill="none" stroke="#94a3b8" stroke-width="2"/>
      <line x1="20" y1="100" x2="60" y2="100" stroke="#94a3b8" stroke-width="2"/>

      <polygon points="140,180 130,80 150,80" fill="none" stroke="#94a3b8" stroke-width="2"/>
      <line x1="120" y1="100" x2="160" y2="100" stroke="#94a3b8" stroke-width="2"/>

      <text x="90" y="210" fill="#22c55e" font-size="11" font-weight="700" text-anchor="middle">High Voltage = Low Current (I)</text>
      <text x="90" y="230" fill="#f59e0b" font-size="10" font-weight="700" text-anchor="middle">I²R Loss Reduced 10,000×!</text>
    </g>

    <!-- Stage 3: Step-Down Substation & Domestic Consumer -->
    <g transform="translate(570, 80)">
      <rect x="0" y="0" width="240" height="220" fill="#111827" rx="10" stroke="#1e293b"/>
      <text x="120" y="25" fill="#f59e0b" font-size="12" font-weight="700" text-anchor="middle">SUBSTATION &amp; CONSUMER</text>

      <rect x="40" y="60" width="60" height="70" fill="none" stroke="#f59e0b" stroke-width="8" rx="4"/>
      <text x="70" y="100" fill="#f59e0b" font-size="10" font-weight="700" text-anchor="middle">Step-Down</text>

      <!-- House Icon -->
      <polygon points="170,70 140,100 200,100" fill="#38bdf8"/>
      <rect x="150" y="100" width="40" height="30" fill="#38bdf822" stroke="#38bdf8"/>

      <rect x="20" y="155" width="200" height="45" fill="#f59e0b15" rx="4" stroke="#f59e0b44"/>
      <text x="120" y="175" fill="#f8fafc" font-size="10" text-anchor="middle">Domestic Mains Supply:</text>
      <text x="120" y="192" fill="#f59e0b" font-size="12" font-weight="700" text-anchor="middle">240 V A.C. (Safe Use)</text>
    </g>

    <!-- Bottom Summary Bar -->
    <rect x="30" y="335" width="780" height="50" fill="#111827" rx="8" stroke="#1e293b"/>
    <text x="420" y="365" fill="#22c55e" font-size="12" font-weight="700" text-anchor="middle">
      NATIONAL GRID: 25 kV Generation → 400 kV Long Transmission (P_loss = I²R Minimized) → 240 V Domestic Consumption
    </text>
    """
    return wrap_svg(inner, W=840, H=420, title="National Electrical Grid Power Transmission and Voltage Transformation Flow")


# =============================================================================
# MAIN ENRICHMENT EXECUTOR FOR TOPIC 5
# =============================================================================

def run_enrichment_topic5():
    print("=" * 80)
    print("VLEARN FORM 4 PHYSICS — TOPIC 5 VISUAL ENRICHMENT")
    print("=" * 80)

    topic = Topic.objects.filter(
        subject__name="Physics",
        subject__grade__name="Form 4",
        name__icontains="Electromagnetic Induction"
    ).first()

    if not topic:
        print("ERROR: Topic 5: Electromagnetic Induction not found! Run ingest_form4_physics_topic5.py first.")
        return

    units = topic.learning_units.all().order_by("order")
    if units.count() < 3:
        print("ERROR: Expected 3 learning units in Topic 5.")
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
    # MODULE 5.1 ENRICHMENT
    # -------------------------------------------------------------------------
    print("--- Enriching Module 5.1 ---")
    attach_svg_to_block(lesson_1, 2, "suggested_diagram", "Microscopic Origin of Induced E.M.F.: Electron Drift and Charge Separation", "m51_conductor_charge_separation", svg_m51_conductor_charge_separation())
    attach_svg_to_block(lesson_1, 3, "suggested_diagram", "Laboratory Setup: Straight Conductor Motion in Horseshoe Magnet Field with Galvanometer", "m51_straight_wire_induction", svg_m51_straight_wire_induction())
    attach_svg_to_block(lesson_1, 6, "suggested_diagram", "Lenz's Law and Energy Conservation: Induced Magnetic Opposition to Motion", "m51_lenz_law_magnet_solenoid", svg_m51_lenz_law_magnet_solenoid())
    attach_svg_to_block(lesson_1, 7, "suggested_diagram", "Fleming's Right-Hand Generator Rule: Mutually Perpendicular 3D Vector Alignment", "m51_fleming_right_hand_rule", svg_m51_fleming_right_hand_rule())

    # -------------------------------------------------------------------------
    # MODULE 5.2 ENRICHMENT
    # -------------------------------------------------------------------------
    print("\n--- Enriching Module 5.2 ---")
    attach_svg_to_block(lesson_2, 2, "suggested_diagram", "Construction of an Alternating Current (A.C.) Generator with Continuous Slip Rings", "m52_ac_generator_construction", svg_m52_ac_generator_construction())
    attach_svg_to_block(lesson_2, 3, "suggested_diagram", "Sinusoidal A.C. Voltage Waveform Output Across 360 Degrees of Armature Rotation", "m52_ac_sinusoidal_waveform", svg_m52_ac_sinusoidal_waveform())
    attach_svg_to_block(lesson_2, 4, "suggested_diagram", "D.C. Generator Split-Ring Commutator Mechanism and Pulsating D.C. Waveform Output", "m52_dc_generator_commutator", svg_m52_dc_generator_commutator())
    attach_svg_to_block(lesson_2, 5, "suggested_diagram", "Cross-Sectional Structure and Operational Transduction of a Moving Coil Microphone", "m52_moving_coil_microphone", svg_m52_moving_coil_microphone())
    attach_svg_to_block(lesson_2, 7, "suggested_diagram", "Parasitic Eddy Currents in Solid Core vs. Energy Savings via Laminated Insulated Sheets", "m52_eddy_currents_lamination", svg_m52_eddy_currents_lamination())

    # -------------------------------------------------------------------------
    # MODULE 5.3 ENRICHMENT
    # -------------------------------------------------------------------------
    print("\n--- Enriching Module 5.3 ---")
    attach_svg_to_block(lesson_3, 2, "suggested_diagram", "The Principle of Mutual Induction Between Primary and Secondary Coils", "m53_mutual_induction", svg_m53_mutual_induction())
    attach_svg_to_block(lesson_3, 3, "suggested_diagram", "Comparative Construction of Step-Up and Step-Down Transformers on Laminated Soft Iron Cores", "m53_stepup_stepdown_transformer", svg_m53_stepup_stepdown_transformer())
    attach_svg_to_block(lesson_3, 7, "suggested_diagram", "National Electrical Grid Power Transmission and Voltage Transformation Flow", "m53_national_grid_system", svg_m53_national_grid_system())

    # Wikimedia Assets
    attach_wikimedia_to_block(
        lesson=lesson_3,
        page_num=7,
        title="Muurame High-Voltage Electrical Substation Transformer",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Muurame_electrical_substation_transformer.jpg/960px-Muurame_electrical_substation_transformer.jpg",
        author="Antti T",
        licensing="CC BY 4.0",
        commons_page="https://commons.wikimedia.org/wiki/File:Muurame_electrical_substation_transformer.jpg"
    )

    attach_wikimedia_to_block(
        lesson=lesson_2,
        page_num=2,
        title="Three-Phase Alternating Current Generator ASEA (Hellsjo Power Station)",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Three-phase_alternating_current_generator%2C_ASEA%2C_1890s%2C_view_1%2C_used_in_Hellsjo_power_station%2C_TM2907_-_Tekniska_museet_-_Stockholm%2C_Sweden_-_DSC01478.JPG/960px-Three-phase_alternating_current_generator%2C_ASEA%2C_1890s%2C_view_1%2C_used_in_Hellsjo_power_station%2C_TM2907_-_Tekniska_museet_-_Stockholm%2C_Sweden_-_DSC01478.JPG",
        author="Daderot",
        licensing="CC0 Public Domain",
        commons_page="https://commons.wikimedia.org/wiki/File:Three-phase_alternating_current_generator,_ASEA,_1890s,_view_1,_used_in_Hellsjo_power_station,_TM2907_-_Tekniska_museet_-_Stockholm,_Sweden_-_DSC01478.JPG"
    )

    attach_wikimedia_to_block(
        lesson=lesson_3,
        page_num=7,
        title="National Grid Substation Switchgear and Transformer Unit",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Substation_switchgear_and_transformer_-_geograph.org.uk_-_3665144.jpg/960px-Substation_switchgear_and_transformer_-_geograph.org.uk_-_3665144.jpg",
        author="Nigel Cox",
        licensing="CC BY-SA 2.0",
        commons_page="https://commons.wikimedia.org/wiki/File:Substation_switchgear_and_transformer_-_geograph.org.uk_-_3665144.jpg"
    )

    print("\n" + "=" * 80)
    print("TOPIC 5 VISUAL ENRICHMENT COMPLETED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    run_enrichment_topic5()
