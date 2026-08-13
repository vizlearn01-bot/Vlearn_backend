"""
VLearn Form 4 Physics — Topic 10: Radioactivity
Visual Enrichment Engine (Enhanced High-Contrast SVGs + Wikimedia Commons)

Enriches Topic 10 (Radioactivity) with:
  - 12 high-precision, high-contrast dark-mode vector SVG diagrams
  - 3 authentic Wikimedia Commons photographic assets

Usage:
  /home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/venv/bin/python curriculum/enrich_form4_physics_topic10.py
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
# ENHANCED SVG BUILDERS — MODULE 10.1
# =============================================================================

def svg_m101_radiation_penetration():
    """Page 3: Penetration chart (paper, aluminum, lead)"""
    inner = """
    <!-- Radioactive Source Block (x = 40) -->
    <rect x="40" y="100" width="80" height="220" fill="#111827" rx="10" stroke="#ef4444" stroke-width="3"/>
    <text x="80" y="210" fill="#ef4444" font-size="14" font-weight="800" text-anchor="middle" transform="rotate(-90 80 210)">Radioactive Lead Block</text>

    <!-- Paper Barrier (x = 240) -->
    <rect x="240" y="80" width="16" height="260" fill="#f8fafc" rx="4"/>
    <text x="248" y="365" fill="#f8fafc" font-size="13" font-weight="800" text-anchor="middle">Paper Sheet</text>

    <!-- Aluminum Barrier (x = 440) -->
    <rect x="440" y="80" width="24" height="260" fill="#94a3b8" rx="4"/>
    <text x="452" y="365" fill="#94a3b8" font-size="13" font-weight="800" text-anchor="middle">5mm Aluminum</text>

    <!-- Lead Shield (x = 640) -->
    <rect x="640" y="80" width="60" height="260" fill="#475569" rx="6"/>
    <text x="670" y="365" fill="#475569" font-size="13" font-weight="800" text-anchor="middle">Thick Lead</text>

    <!-- Alpha Radiation Track (Stopped by Paper) -->
    <line x1="120" y1="140" x2="240" y2="140" stroke="#f59e0b" stroke-width="6"/>
    <circle cx="240" cy="140" r="7" fill="#ef4444"/>
    <text x="180" y="130" fill="#f59e0b" font-size="14" font-weight="800">Alpha (α)</text>

    <!-- Beta Radiation Track (Passes paper, stopped by Aluminum) -->
    <line x1="120" y1="210" x2="440" y2="210" stroke="#38bdf8" stroke-width="5"/>
    <circle cx="440" cy="210" r="6" fill="#ef4444"/>
    <text x="180" y="200" fill="#38bdf8" font-size="14" font-weight="800">Beta (β⁻)</text>

    <!-- Gamma Radiation Track (Passes paper & Al, attenuated in Lead) -->
    <path d="M 120,280 Q 240,260 360,280 T 660,280" fill="none" stroke="#a855f7" stroke-width="4"/>
    <text x="180" y="270" fill="#a855f7" font-size="14" font-weight="800">Gamma (γ)</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Alpha, Beta, and Gamma Radiation Penetration Shielding Comparison Diagram")

def svg_m101_field_deflection():
    """Page 6: Electric and magnetic field deflections"""
    inner = """
    <!-- Top Positive Electric Plate -->
    <rect x="200" y="60" width="440" height="24" fill="#ef4444" rx="6"/>
    <text x="420" y="77" fill="#fff" font-size="14" font-weight="800" text-anchor="middle">Positive Electric Plate (+)</text>

    <!-- Bottom Negative Electric Plate -->
    <rect x="200" y="330" width="440" height="24" fill="#0284c7" rx="6"/>
    <text x="420" y="347" fill="#fff" font-size="14" font-weight="800" text-anchor="middle">Negative Electric Plate (-)</text>

    <!-- Radioactive Beam Source (x = 80) -->
    <rect x="60" y="160" width="80" height="90" fill="#111827" stroke="#38bdf8" stroke-width="3" rx="8"/>

    <!-- Beta Trajectory (Curving Upward to Positive Plate) -->
    <path d="M 140,205 Q 320,205 500,75" fill="none" stroke="#38bdf8" stroke-width="5"/>
    <text x="520" y="90" fill="#38bdf8" font-size="14" font-weight="800">Beta (β⁻)</text>

    <!-- Gamma Trajectory (Straight) -->
    <line x1="140" y1="205" x2="720" y2="205" stroke="#a855f7" stroke-width="4"/>
    <text x="740" y="210" fill="#a855f7" font-size="14" font-weight="800">Gamma (γ)</text>

    <!-- Alpha Trajectory (Curving Downward to Negative Plate) -->
    <path d="M 140,205 Q 320,205 500,335" fill="none" stroke="#f59e0b" stroke-width="5"/>
    <text x="520" y="330" fill="#f59e0b" font-size="14" font-weight="800">Alpha (α)</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Electric and Magnetic Field Trajectory Deflections of Alpha, Beta, and Gamma Rays")

def svg_m101_cloud_chamber_tracks():
    """Page 7: Wilson cloud chamber condensation tracks"""
    inner = """
    <!-- Left Chamber: Alpha Tracks (x = 40, w = 360) -->
    <g transform="translate(40, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#030712" rx="12" stroke="#f59e0b" stroke-width="2"/>
      <text x="180" y="32" fill="#f59e0b" font-size="14" font-weight="800" text-anchor="middle">ALPHA TRACKS (DENSE &amp; STRAIGHT)</text>

      <line x1="40" y1="160" x2="300" y2="100" stroke="#f8fafc" stroke-width="10" opacity="0.95"/>
      <line x1="40" y1="160" x2="310" y2="220" stroke="#f8fafc" stroke-width="10" opacity="0.95"/>
      <line x1="40" y1="160" x2="320" y2="160" stroke="#f8fafc" stroke-width="10" opacity="0.95"/>

      <text x="180" y="290" fill="#cbd5e1" font-size="12" text-anchor="middle">Heavy mass &amp; +2e charge produce intense ionization</text>
    </g>

    <!-- Right Chamber: Beta Tracks (x = 440, w = 360) -->
    <g transform="translate(440, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#030712" rx="12" stroke="#38bdf8" stroke-width="2"/>
      <text x="180" y="32" fill="#38bdf8" font-size="14" font-weight="800" text-anchor="middle">BETA TRACKS (WISPY &amp; ZIGZAG)</text>

      <path d="M 40,160 Q 100,120 160,180 T 280,100" fill="none" stroke="#f8fafc" stroke-width="3" opacity="0.75"/>
      <path d="M 40,160 Q 120,220 200,140 T 300,240" fill="none" stroke="#f8fafc" stroke-width="3" opacity="0.75"/>

      <text x="180" y="290" fill="#cbd5e1" font-size="12" text-anchor="middle">Light electron mass undergoes erratic gas scattering</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Wilson Cloud Chamber Condensation Tracks: Thick Straight Alpha vs. Thin Zigzag Beta Tracks")

def svg_m101_gm_tube_schematic():
    """Page 8: Geiger-Müller (GM) tube internal anatomy"""
    inner = """
    <!-- Outer Cylindrical Metal Cathode (x = 100 to 580) -->
    <rect x="120" y="100" width="460" height="200" fill="#111827" rx="12" stroke="#38bdf8" stroke-width="3"/>

    <!-- Thin Mica Front Window (x = 120) -->
    <rect x="110" y="120" width="12" height="160" fill="#94a3b8" rx="2"/>
    <text x="116" y="90" fill="#94a3b8" font-size="12" font-weight="800" text-anchor="middle">Mica Window</text>

    <!-- Central Anode Wire (x = 120 to 540, y = 200) -->
    <line x1="120" y1="200" x2="540" y2="200" stroke="#f59e0b" stroke-width="5"/>
    <text x="330" y="185" fill="#f59e0b" font-size="13" font-weight="800" text-anchor="middle">Central Anode Wire (+400V)</text>

    <!-- Argon Gas Molecules -->
    <circle cx="200" cy="150" r="5" fill="#a855f7"/>
    <circle cx="300" cy="240" r="5" fill="#a855f7"/>
    <circle cx="400" cy="160" r="5" fill="#a855f7"/>
    <text x="330" y="260" fill="#a855f7" font-size="12" font-weight="800" text-anchor="middle">Low-Pressure Argon Gas</text>

    <!-- Counter Pulse Circuit (Right Side) -->
    <rect x="620" y="140" width="160" height="120" fill="#1e293b" rx="10" stroke="#22c55e" stroke-width="2"/>
    <text x="700" y="175" fill="#22c55e" font-size="14" font-weight="800" text-anchor="middle">Scaler Counter</text>
    <text x="700" y="215" fill="#f8fafc" font-size="22" font-weight="800" font-family="monospace" text-anchor="middle">00482</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Geiger-Muller GM Tube Internal Anatomy: Mica Window, Central Anode Wire, and Pulse Counter Circuit")

def svg_m101_radioactivity_sandbox():
    """Page 8: Interactive Radioactivity Sandbox vector model"""
    inner = """
    <rect x="60" y="60" width="440" height="320" fill="#111827" rx="12" stroke="#38bdf8" stroke-width="3"/>

    <circle cx="280" cy="220" r="70" fill="#030712" stroke="#f59e0b" stroke-width="3"/>
    <text x="280" y="215" fill="#f59e0b" font-size="15" font-weight="800" text-anchor="middle">U-238 Core</text>

    <line x1="280" y1="150" x2="280" y2="80" stroke="#f59e0b" stroke-width="5"/>
    <text x="280" y="70" fill="#f59e0b" font-size="12" font-weight="800" text-anchor="middle">α Particle</text>

    <line x1="350" y1="220" x2="440" y2="220" stroke="#38bdf8" stroke-width="4"/>
    <text x="465" y="225" fill="#38bdf8" font-size="12" font-weight="800">β⁻ Particle</text>

    <g transform="translate(520, 60)">
      <rect x="0" y="0" width="280" height="320" fill="#111827" rx="10" stroke="#38bdf8" stroke-width="2"/>
      <text x="140" y="25" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">INTERACTIVE DECAY CONTROLS</text>

      <text x="15" y="60" fill="#cbd5e1" font-size="11">Half-Life T_1/2 (1 to 100 yrs):</text>
      <rect x="15" y="70" width="250" height="10" fill="#1e293b" rx="4"/>
      <circle cx="120" cy="75" r="7" fill="#22c55e"/>

      <text x="15" y="130" fill="#cbd5e1" font-size="11">Initial Atoms N_0 (1000 to 10000):</text>
      <rect x="15" y="140" width="250" height="10" fill="#1e293b" rx="4"/>
      <circle cx="180" cy="145" r="7" fill="#38bdf8"/>

      <rect x="15" y="190" width="250" height="40" fill="#22c55e15" rx="6" stroke="#22c55e"/>
      <text x="140" y="215" fill="#22c55e" font-size="12" font-weight="800" text-anchor="middle">Remaining N = 2500 (2 Half-Lives)</text>

      <rect x="15" y="250" width="250" height="40" fill="#f59e0b15" rx="6" stroke="#f59e0b"/>
      <text x="140" y="275" fill="#f59e0b" font-size="12" font-weight="800" text-anchor="middle">Activity A = 45.2 Bq</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Interactive Radioactivity Sandbox: Real-Time Decay Kinetics and Half-Life Model")


# =============================================================================
# ENHANCED SVG BUILDERS — MODULE 10.2
# =============================================================================

def svg_m102_alpha_decay_reaction():
    """Page 2: Alpha decay nuclear reaction balance"""
    inner = """
    <!-- Parent Nucleus (U-238) -->
    <circle cx="180" cy="210" r="75" fill="#78350f" stroke="#f59e0b" stroke-width="4"/>
    <text x="180" y="200" fill="#fff" font-size="18" font-weight="800" text-anchor="middle">²³⁸₉₂U</text>
    <text x="180" y="228" fill="#f59e0b" font-size="13" font-weight="700" text-anchor="middle">Parent Nucleus</text>

    <!-- Reaction Arrow -->
    <line x1="275" y1="210" x2="385" y2="210" stroke="#f8fafc" stroke-width="5"/>
    <polygon points="385,210 368,200 368,220" fill="#f8fafc"/>

    <!-- Daughter Nucleus (Th-234) -->
    <circle cx="480" cy="210" r="65" fill="#1e3a8a" stroke="#38bdf8" stroke-width="4"/>
    <text x="480" y="200" fill="#fff" font-size="18" font-weight="800" text-anchor="middle">²³⁴₉₀Th</text>
    <text x="480" y="228" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">Daughter Nucleus</text>

    <!-- Plus Sign -->
    <text x="570" y="218" fill="#f8fafc" font-size="28" font-weight="800">+</text>

    <!-- Alpha Particle (He-4) -->
    <circle cx="660" cy="210" r="32" fill="#ef4444" stroke="#f8fafc" stroke-width="3"/>
    <text x="660" y="205" fill="#fff" font-size="15" font-weight="800" text-anchor="middle">⁴₂He</text>
    <text x="660" y="228" fill="#fff" font-size="11" font-weight="700" text-anchor="middle">α particle</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Alpha Decay Nuclear Transmutation Diagram (Parent Nucleus Ejecting Helium Nucleus)")

def svg_m102_beta_decay_reaction():
    """Page 3: Beta decay nuclear reaction balance"""
    inner = """
    <circle cx="180" cy="210" r="65" fill="#334155" stroke="#94a3b8" stroke-width="4"/>
    <text x="180" y="205" fill="#fff" font-size="16" font-weight="800" text-anchor="middle">¹₀n (Neutron)</text>

    <line x1="265" y1="210" x2="375" y2="210" stroke="#f8fafc" stroke-width="5"/>
    <polygon points="375,210 358,200 358,220" fill="#f8fafc"/>

    <circle cx="460" cy="210" r="55" fill="#0284c7" stroke="#38bdf8" stroke-width="4"/>
    <text x="460" y="205" fill="#fff" font-size="15" font-weight="800" text-anchor="middle">¹₁p (Proton)</text>

    <text x="540" y="218" fill="#f8fafc" font-size="28" font-weight="800">+</text>

    <circle cx="620" cy="210" r="24" fill="#ef4444" stroke="#f8fafc" stroke-width="2"/>
    <text x="620" y="215" fill="#fff" font-size="13" font-weight="800" text-anchor="middle">⁰₋₁e</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Beta Decay Nuclear Transmutation Reaction (Neutron Converting into Proton and Electron)")

def svg_m102_decay_curve_halflife():
    """Page 5: Exponential decay curve graph"""
    inner = """
    <rect x="100" y="60" width="660" height="260" fill="#030712" rx="10" stroke="#38bdf8" stroke-width="2"/>
    <line x1="100" y1="280" x2="760" y2="280" stroke="#94a3b8" stroke-width="2"/>
    <line x1="100" y1="60" x2="100" y2="280" stroke="#94a3b8" stroke-width="2"/>

    <path d="M 100,80 Q 200,180 300,200 T 500,260 T 720,276" fill="none" stroke="#22c55e" stroke-width="5"/>

    <line x1="300" y1="200" x2="300" y2="280" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 2"/>
    <text x="300" y="305" fill="#f59e0b" font-size="13" font-weight="800" text-anchor="middle">T_1/2</text>

    <line x1="500" y1="260" x2="500" y2="280" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 2"/>
    <text x="500" y="305" fill="#f59e0b" font-size="13" font-weight="800" text-anchor="middle">2 T_1/2</text>

    <text x="430" y="360" fill="#f8fafc" font-size="14" font-weight="800" text-anchor="middle">Elapsed Time t →</text>
    <text x="45" y="170" fill="#f8fafc" font-size="14" font-weight="800" text-anchor="middle" transform="rotate(-90 45 170)">Remaining Nuclei N(t) →</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Radioactive Decay Curve Graph Showing Activity Halving Over Consecutive Half-Life Intervals")

def svg_m102_carbon_dating_cycle():
    """Page 7: Carbon-14 cycle and artifact dating"""
    inner = """
    <rect x="60" y="60" width="320" height="120" fill="#111827" rx="10" stroke="#38bdf8" stroke-width="2"/>
    <text x="220" y="90" fill="#38bdf8" font-size="14" font-weight="800" text-anchor="middle">1. ATMOSPHERIC C-14 GENERATION</text>
    <text x="220" y="120" fill="#cbd5e1" font-size="12" text-anchor="middle">Cosmic neutrons + N-14 → C-14 + p</text>
    <text x="220" y="145" fill="#22c55e" font-size="12" font-weight="700" text-anchor="middle">Constant ratio of C-14 to C-12 in air</text>

    <rect x="460" y="60" width="320" height="120" fill="#111827" rx="10" stroke="#22c55e" stroke-width="2"/>
    <text x="620" y="90" fill="#22c55e" font-size="14" font-weight="800" text-anchor="middle">2. LIVING TREE / ANIMAL</text>
    <text x="620" y="120" fill="#cbd5e1" font-size="12" text-anchor="middle">Photosynthesis maintains C-14 equilibrium</text>
    <text x="620" y="145" fill="#f59e0b" font-size="12" font-weight="700" text-anchor="middle">Activity = 15.0 counts/min per gram</text>

    <rect x="220" y="240" width="400" height="120" fill="#111827" rx="10" stroke="#ef4444" stroke-width="2"/>
    <text x="420" y="270" fill="#ef4444" font-size="14" font-weight="800" text-anchor="middle">3. ANCIENT ARTIFACT DECAY TIMELINE</text>
    <text x="420" y="300" fill="#cbd5e1" font-size="12" text-anchor="middle">Death stops C-14 intake. C-14 decays (T_1/2 = 5,730 yrs)</text>
    <text x="420" y="328" fill="#ef4444" font-size="13" font-weight="800" text-anchor="middle">Remaining C-14 ratio measures exact artifact age!</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Carbon-14 Atmospheric Production Cycle and Archaeological Artifact Decay Timeline")


# =============================================================================
# ENHANCED SVG BUILDERS — MODULE 10.3
# =============================================================================

def svg_m103_nuclear_fission_chain():
    """Page 2: Uranium-235 fission chain reaction"""
    inner = """
    <circle cx="80" cy="210" r="12" fill="#0284c7"/>
    <text x="80" y="215" fill="#fff" font-size="11" font-weight="800" text-anchor="middle">n</text>

    <circle cx="200" cy="210" r="50" fill="#78350f" stroke="#f59e0b" stroke-width="3"/>
    <text x="200" y="215" fill="#fff" font-size="15" font-weight="800" text-anchor="middle">U-235</text>

    <line x1="250" y1="210" x2="360" y2="130" stroke="#ef4444" stroke-width="4"/>
    <circle cx="380" cy="120" r="32" fill="#1e3a8a"/>
    <text x="380" y="125" fill="#fff" font-size="12" font-weight="800" text-anchor="middle">Ba-141</text>

    <line x1="250" y1="210" x2="360" y2="290" stroke="#ef4444" stroke-width="4"/>
    <circle cx="380" cy="300" r="28" fill="#166534"/>
    <text x="380" y="305" fill="#fff" font-size="12" font-weight="800" text-anchor="middle">Kr-92</text>

    <line x1="250" y1="210" x2="480" y2="190" stroke="#0284c7" stroke-width="3"/>
    <circle cx="490" cy="190" r="9" fill="#0284c7"/>

    <line x1="250" y1="210" x2="480" y2="210" stroke="#0284c7" stroke-width="3"/>
    <circle cx="490" cy="210" r="9" fill="#0284c7"/>

    <line x1="250" y1="210" x2="480" y2="230" stroke="#0284c7" stroke-width="3"/>
    <circle cx="490" cy="230" r="9" fill="#0284c7"/>

    <text x="550" y="215" fill="#0284c7" font-size="14" font-weight="800">3 Neutrons</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Uranium-235 Fission Chain Reaction Diagram Splitting into Barium, Krypton, and 3 Neutrons")

def svg_m103_thermonuclear_fusion():
    """Page 4: Deuterium-Tritium fusion reaction"""
    inner = """
    <circle cx="160" cy="150" r="32" fill="#0284c7" stroke="#f8fafc" stroke-width="2"/>
    <text x="160" y="155" fill="#fff" font-size="14" font-weight="800" text-anchor="middle">²₁H (D)</text>

    <circle cx="160" cy="270" r="38" fill="#6b21a8" stroke="#f8fafc" stroke-width="2"/>
    <text x="160" y="275" fill="#fff" font-size="14" font-weight="800" text-anchor="middle">³₁H (T)</text>

    <text x="160" y="215" fill="#f8fafc" font-size="24" font-weight="800" text-anchor="middle">+</text>

    <circle cx="320" cy="210" r="28" fill="#eab308"/>
    <text x="320" y="215" fill="#000" font-size="11" font-weight="800" text-anchor="middle">10⁷ K</text>

    <line x1="348" y1="210" x2="520" y2="150" stroke="#22c55e" stroke-width="4"/>
    <circle cx="550" cy="140" r="35" fill="#22c55e" stroke="#f8fafc" stroke-width="2"/>
    <text x="550" y="145" fill="#fff" font-size="14" font-weight="800" text-anchor="middle">⁴₂He</text>

    <line x1="348" y1="210" x2="520" y2="270" stroke="#0284c7" stroke-width="4"/>
    <circle cx="540" cy="280" r="16" fill="#0284c7" stroke="#f8fafc" stroke-width="2"/>
    <text x="540" y="284" fill="#fff" font-size="11" font-weight="800" text-anchor="middle">n</text>

    <text x="680" y="215" fill="#f59e0b" font-size="15" font-weight="800" text-anchor="middle">+ 17.6 MeV</text>
    """
    return wrap_svg(inner, W=840, H=420, title="Deuterium-Tritium Thermonuclear Fusion Reaction Diagram Yielding Helium and 17.6 MeV Energy")

def svg_m103_radiation_warning_shielding():
    """Page 10: Radiation warning trefoil and lead storage cask"""
    inner = """
    <g transform="translate(40, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="12" stroke="#eab308" stroke-width="2"/>
      <text x="180" y="32" fill="#eab308" font-size="14" font-weight="800" text-anchor="middle">RADIATION HAZARD TREFOIL</text>

      <circle cx="180" cy="160" r="80" fill="#eab308"/>
      <circle cx="180" cy="160" r="24" fill="#030712"/>
      <path d="M 180,160 L 180,80 A 80,80 0 0,1 249,120 Z" fill="#030712"/>
      <path d="M 180,160 L 249,200 A 80,80 0 0,1 180,240 Z" fill="#030712"/>
      <path d="M 180,160 L 111,200 A 80,80 0 0,1 111,120 Z" fill="#030712"/>

      <text x="180" y="290" fill="#eab308" font-size="13" font-weight="800" text-anchor="middle">CAUTION: RADIOACTIVE MATERIAL</text>
    </g>

    <g transform="translate(440, 60)">
      <rect x="0" y="0" width="360" height="320" fill="#111827" rx="12" stroke="#475569" stroke-width="2"/>
      <text x="180" y="32" fill="#cbd5e1" font-size="14" font-weight="800" text-anchor="middle">HEAVY LEAD STORAGE CASK</text>

      <rect x="80" y="70" width="200" height="180" fill="#334155" rx="12" stroke="#94a3b8" stroke-width="4"/>
      <rect x="130" y="110" width="100" height="100" fill="#030712" rx="6"/>

      <circle cx="180" cy="160" r="18" fill="#ef4444"/>
      <text x="180" y="165" fill="#fff" font-size="11" font-weight="800" text-anchor="middle">Source</text>

      <text x="180" y="290" fill="#22c55e" font-size="12" font-weight="700" text-anchor="middle">Dense lead absorbs all emitted radiation</text>
    </g>
    """
    return wrap_svg(inner, W=840, H=420, title="Nuclear Trefoil Warning Symbol, Lead Storage Cask, and Deep Geological Waste Storage")


# =============================================================================
# MAIN ENRICHMENT EXECUTOR FOR TOPIC 10
# =============================================================================

def run_enrichment_topic10():
    print("=" * 80)
    print("VLEARN FORM 4 PHYSICS — TOPIC 10 VISUAL ENRICHMENT")
    print("=" * 80)

    topic = Topic.objects.filter(
        subject__name="Physics",
        subject__grade__name="Form 4",
        name__icontains="Radioactivity"
    ).first()

    if not topic:
        print("ERROR: Topic 10: Radioactivity not found! Run ingest_form4_physics_topic10.py first.")
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

    # Module 10.1 SVGs
    print("--- Enriching Module 10.1 ---")
    attach_svg_to_block(lesson_1, 3, "suggested_diagram", "Alpha, Beta, and Gamma Radiation Penetration Shielding Comparison Diagram", "m101_radiation_penetration", svg_m101_radiation_penetration())
    attach_svg_to_block(lesson_1, 6, "suggested_diagram", "Electric and Magnetic Field Trajectory Deflections of Alpha, Beta, and Gamma Rays", "m101_field_deflection", svg_m101_field_deflection())
    attach_svg_to_block(lesson_1, 7, "suggested_diagram", "Wilson Cloud Chamber Condensation Tracks: Thick Straight Alpha vs. Thin Zigzag Beta Tracks", "m101_cloud_chamber_tracks", svg_m101_cloud_chamber_tracks())
    attach_svg_to_block(lesson_1, 8, "suggested_diagram", "Geiger-Muller GM Tube Internal Anatomy: Mica Window, Central Anode Wire, and Pulse Counter Circuit", "m101_gm_tube_schematic", svg_m101_gm_tube_schematic())
    attach_svg_to_block(lesson_1, 8, "suggested_simulation", "Interactive Radioactivity Sandbox: Real-Time Decay Kinetics and Half-Life Model", "m101_radioactivity_sandbox", svg_m101_radioactivity_sandbox())

    # Module 10.2 SVGs
    print("\n--- Enriching Module 10.2 ---")
    attach_svg_to_block(lesson_2, 2, "suggested_diagram", "Alpha Decay Nuclear Transmutation Diagram (Parent Nucleus Ejecting Helium Nucleus)", "m102_alpha_decay_reaction", svg_m102_alpha_decay_reaction())
    attach_svg_to_block(lesson_2, 3, "suggested_diagram", "Beta Decay Nuclear Transmutation Reaction (Neutron Converting into Proton and Electron)", "m102_beta_decay_reaction", svg_m102_beta_decay_reaction())
    attach_svg_to_block(lesson_2, 5, "suggested_diagram", "Radioactive Decay Curve Graph Showing Activity Halving Over Consecutive Half-Life Intervals", "m102_decay_curve_halflife", svg_m102_decay_curve_halflife())
    attach_svg_to_block(lesson_2, 7, "suggested_diagram", "Carbon-14 Atmospheric Production Cycle and Archaeological Artifact Decay Timeline", "m102_carbon_dating_cycle", svg_m102_carbon_dating_cycle())

    # Module 10.3 SVGs
    print("\n--- Enriching Module 10.3 ---")
    attach_svg_to_block(lesson_3, 2, "suggested_diagram", "Uranium-235 Fission Chain Reaction Diagram Splitting into Barium, Krypton, and 3 Neutrons", "m103_nuclear_fission_chain", svg_m103_nuclear_fission_chain())
    attach_svg_to_block(lesson_3, 4, "suggested_diagram", "Deuterium-Tritium Thermonuclear Fusion Reaction Diagram Yielding Helium and 17.6 MeV Energy", "m103_thermonuclear_fusion", svg_m103_thermonuclear_fusion())
    attach_svg_to_block(lesson_3, 10, "suggested_diagram", "Nuclear Trefoil Warning Symbol, Lead Storage Cask, and Deep Geological Waste Storage", "m103_radiation_warning_shielding", svg_m103_radiation_warning_shielding())

    # Wikimedia Assets
    attach_wikimedia_to_block(
        lesson=lesson_1,
        page_num=1,
        title="Historical Becquerel Uranium Salt Photographic Plate Fogging Silhouette (1896)",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/1/1e/Becquerel_plate.jpg",
        author="Henri Becquerel",
        licensing="Public domain",
        commons_page="https://commons.wikimedia.org/wiki/File:Becquerel_plate.jpg"
    )

    attach_wikimedia_to_block(
        lesson=lesson_1,
        page_num=8,
        title="Geiger-Muller Counter Hardware Tube Unit",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Geiger_counter.jpg/960px-Geiger_counter.jpg",
        author="Boffy b",
        licensing="CC BY-SA 3.0",
        commons_page="https://commons.wikimedia.org/wiki/File:Geiger_counter.jpg"
    )

    attach_wikimedia_to_block(
        lesson=lesson_3,
        page_num=3,
        title="Nuclear Power Plant Reactor Containment Dome Hardware Unit",
        verified_url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Perspective_of_the_BONUS_containment_building.jpg/960px-Perspective_of_the_BONUS_containment_building.jpg",
        author="United States Atomic Energy Commission",
        licensing="Public domain",
        commons_page="https://commons.wikimedia.org/wiki/File:Perspective_of_the_BONUS_containment_building.jpg"
    )

    print("\n" + "=" * 80)
    print("TOPIC 10 VISUAL ENRICHMENT COMPLETED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    run_enrichment_topic10()
